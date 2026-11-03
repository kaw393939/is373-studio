import copy
import re
from pathlib import Path
import sqlite3
import pytest
from werkzeug.security import generate_password_hash
from app import create_app
from pipeline import extract_fixtures, import_documents, normalize
from store import connect

PASSWORD = 'Unique classroom phrase 54!'

@pytest.fixture
def app(tmp_path):
    app = create_app({'TESTING':True,'DATABASE':str(tmp_path/'desk.sqlite'),'SECRET_KEY':'test-only-secret'})
    with connect(app.config['DATABASE']) as db:
        for username,role in [('member','member'),('other','member'),('admin','admin')]:
            db.execute('INSERT INTO users(username,password_hash,display_name,role) VALUES(?,?,?,?)',
                       (username,generate_password_hash(PASSWORD),username.title(),role))
    return app


def token(client, path='/login'):
    page = client.get(path)
    match = re.search(rb'name="csrf_token" value="([^"]+)"',page.data)
    assert match, f'No CSRF token at {path}: {page.status_code}'
    return match.group(1).decode()


def post(client,path,data=None,form='/login',follow=False):
    data = dict(data or {})
    data['csrf_token'] = token(client,form)
    return client.post(path,data=data,follow_redirects=follow)


def login(client,username='member'):
    response = post(client,'/login',{'username':username,'password':PASSWORD})
    assert response.status_code == 302


def draft(client,title='A useful classroom idea',body='Bring one small working example and ask for specific feedback.'):
    response = post(client,'/drafts/new',{'title':title,'body':body,'category':'Learning'},form='/drafts/new')
    assert response.status_code == 302
    return response.headers['Location']


def rows(app,table):
    with connect(app.config['DATABASE']) as db:
        return db.execute('SELECT * FROM '+table).fetchall()


def test_member_draft_admin_publish_public_read(app):
    member,admin,visitor = app.test_client(),app.test_client(),app.test_client()
    login(member)
    location = draft(member)
    assert visitor.get(location).status_code == 404
    assert b'A useful classroom idea' not in visitor.get('/').data
    login(admin,'admin')
    assert b'A useful classroom idea' in admin.get('/review').data
    result = post(admin,location+'/publish',form=location)
    assert result.status_code == 302
    assert visitor.get(location).status_code == 200
    assert b'A useful classroom idea' in visitor.get('/').data


def test_anonymous_private_requests_are_denied(app):
    client = app.test_client()
    for path in ['/dashboard','/review','/pipeline','/account','/drafts/new']:
        assert client.get(path).status_code == 401
    assert post(client,'/drafts/new',{'title':'Hello','body':'A long enough draft body here.','category':'Learning'}).status_code == 401


def test_member_cannot_use_admin_direct_endpoints(app):
    client = app.test_client()
    login(client)
    location = draft(client)
    for path in ['/review','/pipeline']:
        assert client.get(path).status_code == 403
    assert post(client,location+'/publish',form=location).status_code == 403
    assert post(client,'/pipeline',form='/dashboard').status_code == 403
    assert rows(app,'articles')[0]['status'] == 'draft'


def test_other_member_cannot_read_or_overwrite_draft(app):
    owner,other = app.test_client(),app.test_client()
    login(owner)
    location = draft(owner)
    login(other,'other')
    article_id = location.rsplit('/',1)[-1]
    assert other.get(location).status_code == 404
    edit = f'/drafts/{article_id}/edit'
    assert other.get(edit).status_code == 403
    assert post(other,edit,{'title':'Hijacked','body':'This should never replace the original text.','category':'Events'},form='/dashboard').status_code == 403
    assert b'Hijacked' not in owner.get(location).data
    assert b'A useful classroom idea' not in other.get('/dashboard').data


def test_owner_can_update_own_draft(app):
    client=app.test_client();login(client)
    location=draft(client);article_id=location.rsplit('/',1)[-1]
    edit=f'/drafts/{article_id}/edit'
    response=post(client,edit,{'title':'A clearer title','body':'This revision has a more useful example and a specific task.','category':'Events'},form=edit)
    assert response.status_code==302
    assert b'A clearer title' in client.get(location).data


@pytest.mark.parametrize('title,body,category',[('','A sufficiently long body here.','Learning'),('Okay','tiny','Learning'),('Title','A sufficiently long body here.','Invalid'),('x'*101,'A sufficiently long body here.','Events')])
def test_invalid_draft_does_not_write(app,title,body,category):
    client=app.test_client();login(client)
    response=post(client,'/drafts/new',dict(title=title,body=body,category=category),form='/drafts/new')
    assert response.status_code==400
    assert rows(app,'articles')==[]


def test_plain_text_is_escaped(app):
    client=app.test_client();login(client)
    location=draft(client,body='<script>alert("not executable")</script> This is just plain text.')
    page=client.get(location)
    assert b'&lt;script&gt;' in page.data
    assert b'<script>' not in page.data


def test_member_cannot_choose_admin_role_at_signup(app):
    client=app.test_client()
    response=post(client,'/register',{'username':'newperson','display_name':'New Person','password':PASSWORD,'role':'admin'},form='/register')
    assert response.status_code==302
    with connect(app.config['DATABASE']) as db:
        user=db.execute("SELECT * FROM users WHERE username='newperson'").fetchone()
        assert user['role']=='member'
        assert user['password_hash']!=PASSWORD
        assert user['password_hash'].startswith('scrypt:')


def test_duplicate_and_invalid_signup(app):
    client=app.test_client()
    assert post(client,'/register',{'username':'member','display_name':'New Person','password':PASSWORD},form='/register').status_code==409
    assert post(client,'/register',{'username':'bad name','display_name':'New Person','password':'short'},form='/register').status_code==400
    assert len(rows(app,'users'))==3


def test_login_rejects_bad_password_and_sql_input(app):
    client=app.test_client()
    for username in ['member',"member' OR 1=1 --"]:
        assert post(client,'/login',{'username':username,'password':'incorrect'}).status_code==401
    assert client.get('/dashboard').status_code==401


def test_login_throttles_repeated_failures(app):
    client=app.test_client()
    for _ in range(5):
        assert post(client,'/login',{'username':'member','password':'incorrect'}).status_code==401
    assert post(client,'/login',{'username':'member','password':PASSWORD}).status_code==429


def test_logout_revokes_a_copied_cookie(app):
    client=app.test_client();login(client)
    old=client.get_cookie('content_desk_session').value
    response=post(client,'/logout',form='/dashboard')
    assert response.status_code==302
    assert client.get('/dashboard').status_code==401
    replay=app.test_client();replay.set_cookie('content_desk_session',old)
    assert replay.get('/dashboard').status_code==401


def test_role_lookup_is_current_not_a_client_claim(app):
    client=app.test_client();login(client,'admin')
    with connect(app.config['DATABASE']) as db:
        db.execute("UPDATE users SET role='member' WHERE username='admin'")
    assert client.get('/review').status_code==403


def test_expired_session_is_denied(app):
    client=app.test_client();login(client)
    with connect(app.config['DATABASE']) as db:db.execute('UPDATE sessions SET expires=0')
    assert client.get('/dashboard').status_code==401


@pytest.mark.parametrize('path',['/register','/login','/logout','/account','/drafts/new','/pipeline','/articles/1/publish'])
def test_mutating_requests_require_csrf(app,path):
    client=app.test_client();login(client,'admin')
    assert client.post(path,data={}).status_code==400


def test_profile_name_change_is_owned_and_role_stays_member(app):
    client=app.test_client();login(client)
    result=post(client,'/account',{'display_name':'A New Name','role':'admin'},form='/account')
    assert result.status_code==302
    assert b'A New Name' in client.get('/account').data
    assert client.get('/review').status_code==403


def test_published_item_cannot_be_edited_in_place(app):
    owner,admin=app.test_client(),app.test_client();login(owner);location=draft(owner)
    login(admin,'admin');post(admin,location+'/publish',form=location)
    article_id=location.rsplit('/',1)[-1]
    assert owner.get(f'/drafts/{article_id}/edit').status_code==409
    assert post(admin,location+'/publish',form=location).status_code==409


def test_fixtures_become_two_drafts_three_sources(app):
    result=import_documents(app.config['DATABASE'],3,extract_fixtures())
    assert result=={'added':2,'linked':1,'skipped':0,'rejected':[]}
    assert len(rows(app,'articles'))==2
    assert len(rows(app,'sources'))==3
    assert all(row['status']=='draft' for row in rows(app,'articles'))


def test_etl_repeated_run_is_idempotent(app):
    docs=extract_fixtures();path=app.config['DATABASE']
    import_documents(path,3,docs)
    result=import_documents(path,3,docs)
    assert result=={'added':0,'linked':0,'skipped':3,'rejected':[]}
    assert len(rows(app,'articles'))==2


@pytest.mark.parametrize('value',[[],None,{},[None],['a document'],[{'source_id':'bad'}]])
def test_etl_empty_or_invalid_is_not_loaded(app,value):
    if isinstance(value,list) and len(value)==1:
        assert len(import_documents(app.config['DATABASE'],3,value)['rejected'])==1
    else:
        with pytest.raises(ValueError):import_documents(app.config['DATABASE'],3,value)
    assert rows(app,'articles')==[]


def test_etl_rejects_unpermitted_source_and_preserves_valid_rows(app):
    docs=extract_fixtures();docs[1]['permission']='unknown'
    result=import_documents(app.config['DATABASE'],3,docs)
    assert result['added']==1 and result['linked']==1 and len(result['rejected'])==1
    assert len(rows(app,'sources'))==2


def test_changed_source_id_is_reported_not_overwritten(app):
    docs=extract_fixtures();path=app.config['DATABASE']
    import_documents(path,3,docs)
    docs[0]['body']='This has different content that should be reviewed manually.'
    result=import_documents(path,3,[docs[0]])
    assert len(result['rejected'])==1
    assert len(rows(app,'articles'))==2


def test_etl_rolls_back_whole_load_if_database_fails(app):
    path=app.config['DATABASE']
    with connect(path) as db:
        db.execute("CREATE TRIGGER fail_second BEFORE INSERT ON articles WHEN NEW.category='Events' BEGIN SELECT RAISE(ABORT,'simulated disk/constraint failure'); END")
    with pytest.raises(sqlite3.IntegrityError):import_documents(path,3,extract_fixtures())
    assert rows(app,'articles')==[] and rows(app,'sources')==[]


def test_imported_source_provenance_survives_publish(app):
    client=app.test_client();login(client,'admin')
    result=post(client,'/pipeline',form='/pipeline')
    assert result.status_code==200 and b'2</b> drafts added' in result.data
    article_id=rows(app,'articles')[0]['id'];location=f'/articles/{article_id}'
    assert b'synthetic-study-a' in client.get(location).data
    assert b'synthetic-study-b' in client.get(location).data
    assert b'write a revised draft' in client.get(location).data
    assert b'href="/drafts/new"' in client.get(location).data
    post(client,location+'/publish',form=location)
    assert b'synthetic-study-a' in app.test_client().get(location).data
    assert client.get(f'/drafts/{article_id}/edit').status_code==409


def test_data_and_login_survive_new_app_instance(app):
    client=app.test_client();login(client);location=draft(client)
    cookie=client.get_cookie('content_desk_session').value
    restarted=create_app({'TESTING':True,'DATABASE':app.config['DATABASE'],'SECRET_KEY':'test-only-secret'})
    new_client=restarted.test_client();new_client.set_cookie('content_desk_session',cookie)
    assert new_client.get('/dashboard').status_code==200
    assert b'A useful classroom idea' in new_client.get(location).data
    new_login=restarted.test_client();login(new_login)
    assert new_login.get('/dashboard').status_code==200


def test_security_headers_and_cookie_flags(app):
    client=app.test_client();login(client)
    response=client.get('/dashboard')
    assert response.headers['Cache-Control']=='no-store'
    assert "frame-ancestors 'none'" in response.headers['Content-Security-Policy']
    cookie=client.get_cookie('content_desk_session')
    assert cookie.http_only and cookie.same_site=='Lax'
