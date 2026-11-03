"""Content Desk: a small, locally runnable member → admin → public workflow."""
from datetime import timedelta
from functools import wraps
from pathlib import Path
import os
import re
import secrets
import sqlite3
import time
import click
from flask import Flask, abort, flash, g, redirect, render_template, request, session, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash, generate_password_hash
from pipeline import CATEGORIES, extract_fixtures, import_documents
from store import connect, initialize


def create_app(config=None):
    runtime = Path(os.environ.get('CONTENT_DESK_DATA', str(Path.home() / '.local' / 'share' / 'is373-content-desk'))).resolve()
    app = Flask(__name__, instance_relative_config=True, instance_path=str(runtime))
    app.config.update(DATABASE=str(Path(app.instance_path) / 'desk.sqlite'),
                      SESSION_COOKIE_NAME='content_desk_session',
                      SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',
                      SESSION_COOKIE_SECURE=False, PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
                      MAX_CONTENT_LENGTH=32 * 1024, WTF_CSRF_TIME_LIMIT=3600)
    if config:
        app.config.update(config)
    if not app.config.get('SECRET_KEY'):
        secret_path = Path(app.instance_path) / '.secret'
        secret_path.parent.mkdir(parents=True, exist_ok=True)
        secret_path.parent.chmod(0o700)
        try:
            with secret_path.open('x') as file:
                file.write(secrets.token_hex(32))
            secret_path.chmod(0o600)
        except FileExistsError:
            pass
        app.config['SECRET_KEY'] = secret_path.read_text().strip()
    app.jinja_env.autoescape = True
    initialize(app.config['DATABASE'])
    CSRFProtect(app)

    @app.before_request
    def load_user():
        g.user = None
        sid = session.get('sid')
        if sid:
            with connect(app.config['DATABASE']) as db:
                g.user = db.execute('SELECT users.* FROM sessions JOIN users ON sessions.user_id=users.id WHERE sessions.id=? AND expires>?',
                                    (sid, int(time.time()))).fetchone()
            if not g.user:
                session.clear()

    @app.after_request
    def headers(response):
        response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Cache-Control'] = 'no-store'
        return response

    def logged_in(view):
        @wraps(view)
        def decorated(*args, **kwargs):
            if not g.user:
                abort(401)
            return view(*args, **kwargs)
        return decorated

    def admin(view):
        @wraps(view)
        @logged_in
        def decorated(*args, **kwargs):
            if g.user['role'] != 'admin':
                abort(403)
            return view(*args, **kwargs)
        return decorated

    def throttle(username):
        now = int(time.time())
        buckets = ((f'login:{username}', 5), (f'ip:{request.remote_addr}', 30))
        with connect(app.config['DATABASE']) as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('DELETE FROM attempts WHERE started<=?', (now-300,))
            for bucket, limit in buckets:
                row = db.execute('SELECT count FROM attempts WHERE bucket=?', (bucket,)).fetchone()
                if row and row['count'] >= limit:
                    abort(429)
            for bucket, _ in buckets:
                db.execute('INSERT INTO attempts VALUES(?,?,1) ON CONFLICT(bucket) DO UPDATE SET count=count+1', (bucket,now))

    def content_fields():
        title, body = request.form.get('title','').strip(), request.form.get('body','').strip()
        category = request.form.get('category','')
        if not 3 <= len(title) <= 100 or not 20 <= len(body) <= 4000 or category not in CATEGORIES:
            return None
        return title, body, category

    def get_article(article_id):
        with connect(app.config['DATABASE']) as db:
            article = db.execute('SELECT articles.*,users.display_name FROM articles JOIN users ON users.id=owner_id WHERE articles.id=?', (article_id,)).fetchone()
        if not article:
            abort(404)
        return article

    @app.get('/')
    def home():
        with connect(app.config['DATABASE']) as db:
            articles = db.execute("SELECT * FROM articles WHERE status='published' ORDER BY id DESC").fetchall()
        return render_template('home.jinja', articles=articles)

    @app.route('/register', methods=['GET','POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username','').strip().lower()
            password = request.form.get('password','')
            name = request.form.get('display_name','').strip()
            if not re.fullmatch(r'[a-z0-9_-]{3,30}',username) or not 12 <= len(password) <= 128 or not 2 <= len(name) <= 60:
                return render_template('auth.jinja', register=True, error='Use a 3–30 character username, 2–60 character name and 12–128 character password.'), 400
            try:
                with connect(app.config['DATABASE']) as db:
                    db.execute('INSERT INTO users(username,password_hash,display_name,role) VALUES(?,?,?,?)',
                               (username,generate_password_hash(password),name,'member'))
            except sqlite3.IntegrityError:
                return render_template('auth.jinja', register=True, error='That username is unavailable.'),409
            flash('Account created. Log in to write your first draft.')
            return redirect(url_for('login'))
        return render_template('auth.jinja', register=True)

    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username','').strip().lower()[:30]
            password = request.form.get('password','')
            if len(password) > 128:
                abort(400)
            throttle(username)
            with connect(app.config['DATABASE']) as db:
                user = db.execute('SELECT * FROM users WHERE username=?', (username,)).fetchone()
            if not user or not check_password_hash(user['password_hash'],password):
                return render_template('auth.jinja', error='Username or password was not recognized.'),401
            previous = session.get('sid')
            sid = secrets.token_urlsafe(32)
            with connect(app.config['DATABASE']) as db:
                db.execute('DELETE FROM sessions WHERE id=? OR expires<=?', (previous or '', int(time.time())))
                db.execute('INSERT INTO sessions VALUES(?,?,?)', (sid,user['id'],int(time.time())+3600))
                db.execute('DELETE FROM attempts WHERE bucket=?', ('login:'+username,))
            session.clear()
            session['sid'] = sid
            session.permanent = True
            return redirect(url_for('dashboard'))
        return render_template('auth.jinja')

    @app.post('/logout')
    @logged_in
    def logout():
        with connect(app.config['DATABASE']) as db:
            db.execute('DELETE FROM sessions WHERE id=?', (session['sid'],))
        session.clear()
        flash('You are logged out.')
        return redirect(url_for('home'))

    @app.get('/dashboard')
    @logged_in
    def dashboard():
        with connect(app.config['DATABASE']) as db:
            articles = db.execute('SELECT * FROM articles WHERE owner_id=? ORDER BY id DESC', (g.user['id'],)).fetchall()
        return render_template('dashboard.jinja', articles=articles)

    @app.route('/account', methods=['GET','POST'])
    @logged_in
    def account():
        if request.method == 'POST':
            name = request.form.get('display_name','').strip()
            if not 2 <= len(name) <= 60:
                return render_template('account.jinja', error='Use a name of 2–60 characters.'),400
            with connect(app.config['DATABASE']) as db:
                db.execute('UPDATE users SET display_name=? WHERE id=?', (name,g.user['id']))
            flash('Your display name was updated.')
            return redirect(url_for('account'))
        return render_template('account.jinja')

    @app.route('/drafts/new', methods=['GET','POST'])
    @logged_in
    def new_draft():
        if request.method == 'POST':
            fields = content_fields()
            if not fields:
                return render_template('editor.jinja', article=None, categories=sorted(CATEGORIES), error='Use a title of 3–100 and body of 20–4,000 characters.'),400
            with connect(app.config['DATABASE']) as db:
                cursor = db.execute('INSERT INTO articles(owner_id,title,body,category) VALUES(?,?,?,?)', (g.user['id'],*fields))
                article_id = cursor.lastrowid
            flash('Draft saved. An admin can now review it.')
            return redirect(url_for('article', article_id=article_id))
        return render_template('editor.jinja', article=None, categories=sorted(CATEGORIES))

    @app.route('/drafts/<int:article_id>/edit', methods=['GET','POST'])
    @logged_in
    def edit_draft(article_id):
        article = get_article(article_id)
        if article['owner_id'] != g.user['id']:
            abort(403)
        if article['status'] != 'draft':
            abort(409)
        # Imported drafts stay traceable to the source; publish or create a separate new draft.
        if article['fingerprint']:
            abort(409)
        if request.method == 'POST':
            fields = content_fields()
            if not fields:
                return render_template('editor.jinja', article=article, categories=sorted(CATEGORIES), error='Check the title, body and category.'),400
            with connect(app.config['DATABASE']) as db:
                db.execute('UPDATE articles SET title=?,body=?,category=? WHERE id=?', (*fields,article_id))
            flash('Draft updated.')
            return redirect(url_for('article',article_id=article_id))
        return render_template('editor.jinja', article=article, categories=sorted(CATEGORIES))

    @app.get('/articles/<int:article_id>')
    def article(article_id):
        article = get_article(article_id)
        if article['status'] != 'published' and (not g.user or (g.user['id'] != article['owner_id'] and g.user['role'] != 'admin')):
            abort(404)
        with connect(app.config['DATABASE']) as db:
            sources = db.execute('SELECT * FROM sources WHERE article_id=? ORDER BY id', (article_id,)).fetchall()
        return render_template('article.jinja', article=article, sources=sources)

    @app.get('/review')
    @admin
    def review():
        with connect(app.config['DATABASE']) as db:
            articles = db.execute("SELECT articles.*,users.display_name FROM articles JOIN users ON users.id=owner_id WHERE status='draft' ORDER BY articles.id").fetchall()
        return render_template('review.jinja', articles=articles)

    @app.post('/articles/<int:article_id>/publish')
    @admin
    def publish(article_id):
        get_article(article_id)
        with connect(app.config['DATABASE']) as db:
            updated = db.execute("UPDATE articles SET status='published' WHERE id=? AND status='draft'", (article_id,))
            if updated.rowcount != 1:
                abort(409)
        flash('Published. Visitors can now read this item.')
        return redirect(url_for('article',article_id=article_id))

    @app.route('/pipeline', methods=['GET','POST'])
    @admin
    def pipeline():
        report = None
        if request.method == 'POST':
            report = import_documents(app.config['DATABASE'],g.user['id'],extract_fixtures())
        return render_template('pipeline.jinja', report=report)

    for code, message in {400:'Check the form and try again.',401:'Log in to continue.',403:'Your account does not have permission for this action.',404:'This item is not available.',409:'This action conflicts with the current record.',413:'That request is too large.',429:'Too many login attempts. Wait five minutes.'}.items():
        def handle(error, message=message):
            return render_template('error.jinja', code=error.code, message=message),error.code
        app.register_error_handler(code,handle)

    @app.cli.command('seed-demo')
    def seed_demo():
        """Create local demo accounts; print newly generated passwords once."""
        with connect(app.config['DATABASE']) as db:
            for username, name, role in [('member','Demo Member','member'),('admin','Demo Editor','admin')]:
                if db.execute('SELECT id FROM users WHERE username=?',(username,)).fetchone():
                    click.echo(f'{username}: already exists (password unchanged)')
                    continue
                password = secrets.token_urlsafe(15)
                db.execute('INSERT INTO users(username,password_hash,display_name,role) VALUES(?,?,?,?)',
                           (username,generate_password_hash(password),name,role))
                click.echo(f'{username} password: {password}')
    return app

if __name__ == '__main__':
    create_app().run(host='127.0.0.1',port=4191,debug=False)
