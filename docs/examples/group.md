---
outline: false
> Reference scope: these earlier content-app examples demonstrate parts of the process. They do not implement the current hosted RAG requirement. Follow the [current portfolio/RAG/group briefs](/course/overview) and [project review rubric](/course/milestones); any practice scores below are historical teaching examples.

---

# Two group examples

These are **fictional teams and critique scenarios**, with real browser-only fixture previews. Human collaboration, client interviews, peer sessions and a deployed service remain unverified. Scores use the current Studio's familiar 40/35/25 structure for **practice only**; future final criteria remain unposted.

| Example | One small workflow | Try A/B | Practice score |
| --- | --- | --- | ---: |
| **Study Brief** | Synthetic campus notices → normalized, deduplicated review queue. | [A](/samples/study-brief/a.html) · [B](/samples/study-brief/b.html) | 67/100 |
| **Neighbor Notes** | Synthetic volunteer notes → categorized briefing draft. | [A](/samples/neighbor-notes/a.html) · [B](/samples/neighbor-notes/b.html) | 60/100 |

Try importing twice. Explain added, skipped and rejected counts, then inspect a source identifier. These are **fixtures, not live opportunities or extracted web pages**. A successful browser import does not prove server persistence, safe publishing or equal real teamwork.

## Study Brief

<details>
<summary>Open Study Brief's filled record, practice assessment and feedback</summary>

### 1. Understand / baseline

**Reader/problem:** a student briefing editor needs a manageable queue rather than repeated notices. The proposed business workflow is input → clean/classify/deduplicate → human review. This is consistent with the course's content/ETL direction.

**Evidence boundary:** the team and customer are invented. “Editors lose time to duplicate notices” is a hypothesis, not a measured productivity claim. Start with four synthetic rows: two valid unique items, one duplicate and one missing-title negative case. No live scraping, paid model API or personal data is needed.

**Baseline:** reuse existing Git/Studio methods and the team's source contract. The individual accounts/roles app is separate; do not count that app as an implemented group pipeline.

### 2. Plan

**Option A:** source editor and output queue together, useful for tracing an import. **Option B:** narrower numbered steps: inspect/import, then review. Choose A provisionally for the import-debugging task; compare with a real peer before claiming it is easier.

**Data contract:** each fixture has an id, source label, title, category, URL identifier and body. Normalize whitespace/category and use the canonical URL without a fragment as the duplicate key. Preserve the original source id/label. Reject a missing title or non-http/https identifier. New records must remain “Needs human review.”

| Story | Expected check |
| --- | --- |
| Import the agreed fixture. | Add two unique items, skip one duplicate, reject one missing title. |
| Repeat the import. | Add zero new items; keep the two saved items and their source trace. |
| Explain a rejected row. | Show which row failed and a useful reason without deleting saved output. |
| Review the result. | A person marks an item reviewed; nothing automatically publishes or sends. |

**Comparable task split:** Partner A owns the source contract/parser and negative cases; Partner B reviews it. Partner B owns the review queue/output and task checks; Partner A reviews it. Both choose the scope/A/B direction, integrate and share QA. A real pair would link actual issues/PRs and adjust effort when a task grows; this proposed split is not evidence that work happened.

### 3. Build and checked-release handoff

The A/B previews parse local JSON, normalize records, deduplicate, preserve source trace and load browser storage. The UI shows added/skipped/rejected counts. There is no external extraction, production database or automated publishing.

**Actual checks run:** the shared script confirms the first fixture has **two valid rows, one rejection and one duplicate**; repeated load adds **zero** and skips the existing two; source id/label are retained. It also checks malformed JSON, wrong input shape and an unsafe source protocol. These pure checks run on the same functions used by the browser.

**Release gap:** the source is reproducible as a static preview. A real group still needs its own source permission evidence, executed pipeline/repository, meaningful integration checks and agreed delivery/handoff. A fixture transformation is a useful first slice, not proof that the whole proposed service exists.

### 4. Improve

**Simulated critique:** “The list looks clean, but I cannot tell what happened to the bad rows.” The example puts counts and row-specific rejection messages beside the input. Confirmation repeats the need for human review.

**Required real follow-up:** another team imports the fixture, explains one rejection and runs it again. Open a genuine issue about an observed obstacle; choose a meaningful change, retest and record both members' contributions. That session has not occurred in this worked scenario.

### Practice assessment and feedback

| Criterion | Score | Evidence and feedback |
| --- | ---: | --- |
| Working result | 24/40 | Narrow fixture ETL and browser review queue work; external extraction/backend/delivery are absent. |
| Specification/checks/GitHub evidence | 21/35 | Testable contract, repeat-import checks and planned cross-review; actual human contribution and review trail remain missing. |
| Explanation/observation | 22/25 | The pipeline and limits are clear in writing; real members still need to explain their own slices. |
| **Total** | **67/100** | A useful bounded slice; finish the actual shared repository, human evidence and agreed service boundary. |

**Specific feedback:** keep the fixture small. Have the other member independently predict the first and repeated import counts, then run and explain them. Add a real source only after agreeing permission, failure handling and the output review step.

</details>

## Neighbor Notes

<details>
<summary>Open Neighbor Notes' filled record, practice assessment and feedback</summary>

### 1. Understand / baseline

**Reader/task:** a community newsletter editor wants a short review queue of volunteer notes. The client and records are fictional; no real nonprofit interview or permission to collect its data is implied.

**Scope:** five fixture rows: three unique useful notes, one duplicate and one deliberately unsafe URL. Extract the JSON, normalize/category-label it, preserve source identifiers and load a human-review queue. No real signups, notifications or public opportunity claims.

### 2. Plan

**Approaches:** A keeps source and output together; B gives new editors a sequential import/review flow. Choose B as an initial clarity hypothesis. A remains a useful inspection alternative; both share the data and transformation functions.

**Stories/checks:** importing the fixture adds three unique rows, skips one duplicate and rejects the unsafe URL; importing again creates no duplicates; a reader can find each source label/id; a person reviews the note before any real publication. Malformed JSON should leave already-saved output intact.

**Work split:** Partner A designs the fixture contract and implements normalization/duplicate checks; Partner B cross-reviews and adds a negative fixture. Partner B designs the output/review task; Partner A cross-reviews its state/labels. Both integrate, compare approaches and take QA tasks of comparable effort. These are scenario roles, not completed real team contributions.

### 3. Build and checked-release handoff

[Try version B](/samples/neighbor-notes/b.html). Source identifiers are displayed as text because the example.org records are invented. Marking reviewed changes local preview state; it sends and publishes nothing.

**Actual pure-function result:** the second dataset has **three valid unique rows, one duplicate and one rejected URL**. The shared merge function prevents repeated imports. Browser task behavior and real peer observations require their own checks; the unit result does not imply they happened.

**Unfinished:** no live source extractor, permission agreement with a client, server persistence, deployment or actual teammate review. Do not put those claims in a résumé or final record until evidenced.

### 4. Improve

**Simulated critique:** “These sound like real volunteer opportunities.” The preview calls every row a synthetic fixture, labels the source URLs as identifiers and says that no booking, publishing or external message occurs. That wording is a teaching design response, not feedback received from an actual user.

**Next real review:** ask a peer to identify a real versus simulated element and explain the rejected source. If the distinction is unclear, revise the labels, try the same task again and keep the actual issue/change/retest record.

### Practice assessment and feedback

| Criterion | Score | Evidence and feedback |
| --- | ---: | --- |
| Working result | 22/40 | Fixture transform/review works; real service and persistence claims remain unsupported. |
| Specification/checks/GitHub evidence | 18/35 | Expected counts and negative case are clear; source permission, real integration/review and contribution trail are absent. |
| Explanation/observation | 20/25 | Clear synthetic-data boundary; add actual member explanations and peer observations. |
| **Total** | **60/100** | Stronger evidence and collaboration matter more than another feed or AI component. |

**Specific feedback:** replace the imagined review with an actual cross-team task. Before adding a live feed, document its permission and failure behavior. Keep a human review gate and show who built and checked each slice.

</details>

<a href="/is373-studio/samples/README.md" target="_self">Run the actual source checks</a> · [Individual examples](/examples/individual) · [Group expectations](/projects/group).
