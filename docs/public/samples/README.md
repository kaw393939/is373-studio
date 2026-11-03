# IS373 browser previews

Four fictional products, each with working A/B interface variants. Synthetic data and browser storage only. No real users, server, authentication, deployment, external publishing or human peer study. A demo role dropdown is not secure authorization.

## Run locally

Extract the source download, open a terminal inside `preview-source`, and run `python3 -m http.server 4193`. Open `http://127.0.0.1:4193/club-desk/a.html` or replace `club-desk` with `resource-roundup`, `study-brief` or `neighbor-notes`. A/B share a queue within the same product. Stop the server with Ctrl+C.

No API key, cloud account or npm packages are needed. Browser storage stays on the current origin. Reset clears only that product's synthetic queue. The worked-record navigation is intended for the published course site; offline source includes these previews and checks, not the full documentation site.

## Reproduce the limited checks

With Node 22 or newer: `node verify.mjs`. The script tests the same pure draft/status and ETL transformation functions used by the previews, with negative inputs and repeat import. It does not test secure backend authorization, a database, an actual deployed service, a browser task or human learning.

For the content task, save a draft, switch the explicitly simulated role and publish locally. For ETL, import the fixture, explain added/skipped/rejected counts, import again, then review an item. User text is rendered as text rather than HTML; a real product still needs independent server validation and permissions.

Fixtures are invented teaching records. Their example.org URLs are source identifiers, not real events or opportunities. No copyrighted feed or personal data is collected.
