# Content Desk · working IS373 reference

A member writes a plain-text draft. An admin reviews and publishes it. Visitors see published items only. A separate ETL path turns three bundled synthetic documents into two reviewable drafts with three source records.

## Run locally

Use Python 3.12+ with SQLite and venv for class. Verified here with Python 3.14.7. Extract `content-desk-source.zip` and open a terminal in the extracted `content-desk` folder.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app seed-demo
python app.py
```

On Windows PowerShell, replace the activation line with `.venv\Scripts\Activate.ps1` and use `python` if `python3` is unavailable.

Open **http://127.0.0.1:4191**. The seed command generates unique local passwords for `member` and `admin` and prints them once. Keep that terminal output. Re-running seed preserves existing passwords. You can also create a new member in the app. Public signup never grants admin access.

Runtime SQLite and the generated session secret are stored in `~/.local/share/is373-content-desk`, **outside the source tree**. Set `CONTENT_DESK_DATA` before starting if you need another private local directory. Stop with Ctrl+C and run `python app.py` again to check persistence. To use a fresh demo, select a new private runtime directory; do not delete data you want to keep.

## First useful result (about five minutes)

1. Log in as `member`; write a short draft. Notice that it is private.
2. Log out; verify that the public board does not list the draft.
3. Log in as `admin`; open Review, read it and publish it.
4. Log out; read the published item as a visitor.
5. As admin, open Import. Import the fixtures twice: first run creates two drafts and links an additional source; second run skips all three sources.

To customize the example, start with the three files in `fixtures/` and the title/home copy in `templates/`. Add a focused check for your own case while keeping the existing behavior checks.

## Check it

```sh
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider
```

On PowerShell use `$env:PYTHONDONTWRITEBYTECODE="1"` on its own line, then `python -m pytest -q -p no:cacheprovider`. Forty checks cover the working path, permission boundaries, CSRF, validation, escaped plain text, repeated imports, source conflicts, transaction rollback and persisted data after a new app instance.

## Small map

- `app.py`: HTTP routes, account/session checks and CLI seed.
- `store.py`: SQLite schema and commit/rollback boundary.
- `pipeline.py`: pure normalization plus atomic import service.
- `fixtures/`: three permitted synthetic JSON documents (one duplicate).
- `templates/` and `static/`: accessible, responsive server-rendered UI.
- `INDIVIDUAL-RECORD.md` and `GROUP-RECORD.md`: separate technical evidence records.
- `TEST-NOTES.md`: actual checks and remaining limits.

## Scope and sources

This is a **local teaching reference**, separate from the posted App Studio starter and its assignment criteria. It does not replace those assignments. The existing [APP-003 reference](https://github.com/kaw393939/is373-app-studio/tree/reference/app-003) uses FastAPI, Argon2id and JWT. This smaller Flask reference uses Werkzeug's password hashing, Flask's signed session cookie plus revocable SQLite session IDs, Flask-WTF CSRF protection, and server-side current-role lookups. It illustrates the same boundaries; it is not a drop-in replacement for the starter.

The dev server binds only to localhost. No production deployment is provided. A public service would need a deployment review, HTTPS/secure cookies, account recovery and operational controls. The bounded account-maintenance feature is a display-name update; no password reset, email verification or account deletion. Plain-text imported drafts are kept unchanged so their source fingerprint remains accurate. A new authored draft is the simple way to make a substantially different item.

There is no paid API, web scraping, external customer data or autonomous publication. All fixture content is authored for classroom reuse. No real student's grade, peer review, teamwork or individual understanding is claimed.

Primary references consulted: [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/), [Flask security guidance](https://flask.palletsprojects.com/en/stable/web-security/), [Flask-WTF CSRF protection](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/), [Werkzeug password helpers](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.generate_password_hash), [Python SQLite](https://docs.python.org/3/library/sqlite3.html).
