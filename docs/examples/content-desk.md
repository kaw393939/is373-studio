# A working content app you can run

> Reference scope: these earlier content-app examples demonstrate parts of the process. They do not implement the current hosted RAG requirement. Follow the [current portfolio/RAG/group briefs](/course/overview) and [project review rubric](/course/milestones); any practice scores below are historical teaching examples.

**Get one useful result:** save a private draft, publish it as an editor, then read it as a visitor. Content Desk has real SQLite accounts, sessions and server-side permissions. Its separate import task turns three synthetic documents into two drafts with their sources attached.

[Download the complete source](/examples/content-desk/content-desk-source.zip). This runs on your computer; GitHub Pages hosts this guide, not the Python server.

## Start here

Extract the ZIP. Open a terminal in its `content-desk` folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app seed-demo
python app.py
```

Open **http://127.0.0.1:4191**. The seed command prints unique passwords for local `member` and `admin` accounts. Use Python 3.12+ for class. Windows activation instructions are in the download's README.

**Try it:** member saves a draft → log out → admin reviews and publishes → log out → visitor reads it. Then, as admin, import the fixtures twice and explain why the second run adds nothing.

To customize this example, start with the three files in `fixtures/` and the title/home copy in `templates/`. A focused check can show what your own case does while the existing checks keep the shared behavior covered.

**Career connection:** you can demonstrate how a server protects a customer workflow and how you checked its failure cases.

::: details A short, sufficient technical explanation
“I chose review before publication. Another member cannot read or edit my draft, and a member cannot call the publish endpoint. After an admin publishes it, visitors can read it. I checked those requests directly and reopened the same database in a new app instance. The ETL import merges duplicate content while keeping all three source records.”

That explains the technical result. Add your actual contribution links, real peer feedback, one resulting change/retest and other evidence required by your assignment. Downloading a reference is not a completed student submission.
:::

::: details How this supports two projects
| Individual application | Shared ETL workflow |
| --- | --- |
| Member draft → admin review → public item | Three permitted fixtures → normalized/deduplicated drafts → human review |
| Accounts, private ownership, roles, stored content | Validation, provenance, repeated import and rollback checks |
| `INDIVIDUAL-RECORD.md` in the download | `GROUP-RECORD.md` in the download |

These are two independent technical records in one small reference. They do not claim a real group completed the work. Use your own repository and actual collaboration evidence.
:::

::: details What actually passed
**40 automated integration checks passed** during authoring on November 3, 2026. They exercise the complete workflow; invalid input; direct unauthorized requests; cross-member privacy; escaped plain text; CSRF on writes; login/logout and session revocation; persistence in a fresh app instance; ETL duplicates, permission failures and source conflicts; and rollback after a simulated database failure.

Run `python -m pytest -q -p no:cacheprovider` from the downloaded folder. Read the included `TEST-NOTES.md` for scope and limits. Automated success does not stand in for a real peer review, individual explanation or production deployment.
:::

::: details Small architecture and boundaries
**Browser → Flask routes → SQLite.** `app.py` handles HTTP and account/role decisions; `store.py` owns transactions; `pipeline.py` normalizes and loads documents. Templates render plain text. There is no paid API or external data dependency.

This is separate from your [App Studio APP-003 reference](https://github.com/kaw393939/is373-app-studio/tree/reference/app-003); follow your posted starter and assignment criteria. The reference illustrates the same current-role, revocable-session and server-permission boundaries in a smaller Flask application.

The server binds only to localhost. The generated secret and database stay outside the source at `~/.local/share/is373-content-desk`. This is a local teaching example, not a public deployment. Profile maintenance changes a display name; password recovery and account deletion are outside its scope. Imported drafts retain their source text; create a new authored draft to write a different item.

Technical references: [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/), [Flask security guidance](https://flask.palletsprojects.com/en/stable/web-security/), [Flask-WTF CSRF](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/), [Werkzeug password helpers](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.generate_password_hash) and [Python SQLite](https://docs.python.org/3/library/sqlite3.html).
:::

[Back to your individual project](/projects/individual) · [Shared content/ETL project](/projects/group) · [Examples](/examples/)
