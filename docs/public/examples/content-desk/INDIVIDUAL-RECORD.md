# Individual technical record · Content Desk

**Teaching reference built with agent assistance.** These are actual implementation decisions and checks, not a claim about student authorship or a completed student submission.

## Need and choice

A small campus club needs a way to collect short notices without letting an unreviewed draft appear publicly. We compared (A) member draft → admin publication and (B) publish immediately → admin removal. We implemented A because a private review boundary is easier to explain and check. This is a reasoned design comparison; no real customer preference test was performed.

## Finished technical promise

Member signup/login, own private draft creation and editing, admin review/publication, public published-only reading, logout with server revocation, persistent SQLite storage and profile-name maintenance.

## Evidence to inspect

`test_member_draft_admin_publish_public_read` follows the whole path. `test_other_member_cannot_read_or_overwrite_draft` makes direct unauthorized requests. `test_member_cannot_use_admin_direct_endpoints` checks that a hidden button is not the permission mechanism. `test_data_and_login_survive_new_app_instance` reopens the same database in a fresh application instance.

The UI uses plain-language status and a single primary action at each step. Server-rendered templates automatically escape plain text. Forms use CSRF tokens. An existing source fingerprint prevents in-place editing of an imported record; new authored drafts remain editable until publication.

## What a learner still supplies

Their own audience/brand choices, explanation of the code and help received, actual revision/contribution links, a real peer task and feedback, a resulting improvement/retest, and the setup/delivery evidence required by their posted assignment. This reference supplies no grade and cannot earn a student's points by being downloaded.
