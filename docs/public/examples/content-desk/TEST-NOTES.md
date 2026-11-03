# Actual technical checks · November 3, 2026

- Python 3.14.7, Flask 3.1.3, Flask-WTF 1.2.2, pytest 9.2.0.
- `python -m pytest -q docs/public/examples/content-desk/test_app.py`: **40 passed in 8.36s** during authoring. Subsequent verified command/result may be recorded in the course review.
- Real file-backed SQLite test databases live in pytest's temporary directory, not the website source or download. Test clients exercise actual routes, database writes, password verification, signed cookies and CSRF protection.
- End-to-end member draft → admin review/publish → anonymous read passed.
- Direct member/admin and cross-member requests are denied. Role changes and expired/revoked sessions are checked against the server.
- Login/logout, invalid registration, duplicate username, bad passwords, SQL-shaped input, five-attempt login throttle and cookie/header flags passed.
- Missing CSRF tokens are denied on every mutating route. User HTML renders as escaped plain text.
- ETL valid/empty/invalid/duplicate/changed/unpermitted sources, retained provenance, a repeated import and transaction rollback passed.
- The restart check creates a new application instance against the same on-disk database and signing key, then verifies persisted draft/session/login behavior. It is an integration check, not a production deployment exercise.

## Limits kept visible

The code was created with agent assistance and checked with automated tests. No real human student or peer participated. No grade, customer validation or proven equal team effort is claimed. Manual browser/mobile review is a separate check; the automated result alone does not establish usability or accessibility compliance.

The app is a bounded local reference, not a hardened public service. Login has a small local throttle; signup remains local-only without a public anti-abuse service. Profile maintenance covers a display-name change. No email/password recovery, MFA, account deletion, content-version history, real-world source validation or paid AI integration is included.

## Actual browser check · round 1

The root reviewer used Chrome through the computer-use tool on the local reference app at port 4191: member login → new draft “Fictional project check-in” → saved article 1; logout → public board empty; admin login → review queue → read → publish; logout → visitor sees the published item. This is an actual automated browser walkthrough, not a human peer review. The screenshot is saved in the workspace at `outputs/learner-review-2026-11-03/screenshots/is373-round1.png`.

A separate local learner-artifact trial extracted the source into a fresh venv, customized a campus bulletin case and ran 41 checks (40 reference checks plus one focused case). That work and its route/database receipts are in `outputs/learner-review-2026-11-03/is373/`; it does not imply genuine teamwork or a production deployment.

## Actual browser check · round 2

The root reviewer used Chrome on the same local reference: Import → three bundled fixtures produced two drafts, one additional source, zero rejected; repeating Import produced zero drafts, zero additional sources and three already imported. Review → “Build together on Tuesday” displayed both source IDs and the new preserved-source helper with its “write a revised draft” link. These are actual automated browser observations, not human feedback. The separate round-2 learner trial followed that revision route and checked saving/reviewing/publishing the authored revision through actual Flask routes.
