# Shared ETL technical record · classroom briefing

**Technical reference, not evidence of a real team.** Its source belongs to the same small Content Desk example, but this record isolates the shared pipeline's purpose, data and checks.

## Need and choice

A fictional editor wants a short review queue from a few permitted source documents. We compared (A) importing every document as a draft and (B) merging identical normalized content while retaining each source ID. We chose B to reduce repeated review without losing provenance.

## Finished technical promise

Extract three bundled synthetic JSON documents; validate permission/category/text length; normalize Unicode and spacing; deduplicate case-insensitive title/body content; load two drafts and three source records atomically. A human admin chooses whether to publish. Re-importing is idempotent. A reused source ID with changed content is rejected for manual review.

No external website, AI model or sensitive dataset is used. All three fixtures are authored for classroom reuse under `classroom-synthetic` permission.

## Evidence to inspect

`test_fixtures_become_two_drafts_three_sources` checks expected output. `test_etl_repeated_run_is_idempotent` checks a second import. Other tests reject empty/invalid/unpermitted input and changed source IDs, preserve provenance after publication, and simulate a database failure to verify complete rollback of draft + source writes.

## How a real pair could share this scope

One person can own source validation/normalization and its failure checks; another can own the review/output flow and permission checks. Each reviews the other's changes, and both run an integrated import → review → publish check. Adjust the split to comparable effort. This is an example plan only: there are no invented teammate commits, human reviews or equal-work claims here.

A submitted group record still needs actual named contributions, peer feedback, one meaningful resulting change/retest and the posted assignment's evidence. A working pipeline alone does not establish collaboration.
