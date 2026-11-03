---
outline: false
> Reference scope: these earlier content-app examples demonstrate parts of the process. They do not implement the current hosted RAG requirement. Follow the [current portfolio/RAG/group briefs](/course/overview) and [project review rubric](/course/milestones); any practice scores below are historical teaching examples.

---

# Two individual examples

These are **fictional teaching records**. The source and browser previews are real, but the people, customer situations and critique scenarios are invented. No genuine peer walkthrough or secure backend is claimed. Future criteria are not posted, so every score below is **practice feedback using the familiar 40/35/25 structure**, not an official final-project grade.

| Example | Main task | Try A/B | Practice score |
| --- | --- | --- | ---: |
| **Club Desk** | A club editor drafts a notice; a reviewer publishes it. | [A](/samples/club-desk/a.html) · [B](/samples/club-desk/b.html) | 58/100 |
| **Resource Roundup** | A student editor submits a resource note for review. | [A](/samples/resource-roundup/a.html) · [B](/samples/resource-roundup/b.html) | 50/100 |

**Open the record at your current step.** Copy the method and level of detail, not the fictional claims. A/B share one project-specific browser queue. A role dropdown is a simulation; it cannot prove the real app's permissions.

## Club Desk

<details>
<summary>Open Club Desk's filled record, practice assessment and feedback</summary>

### 1. Understand / baseline

**Reader/task:** a club communications editor needs to save an announcement without accidentally sending unfinished information. An authorized reviewer decides what is ready.

**Baseline:** the fictional student starts from APP-001–003: branded homepage, accounts/private dashboard and member/admin roles. Those are prerequisites for the proposed real implementation; this public preview does not supply or verify them.

**Observation versus assumption:** the existing App Studio requires server roles and reviewed learning evidence. The claim that club editors need a queue is a persona hypothesis, not an interview finding. Three synthetic notices are enough to explore the task; no real club data or member list is needed.

**Scope:** one plain-text title/body, draft and published states, validation and role-specific actions. No attachments, mass email, rich-text editor or social network. Reuse SPEC, LEARNING and the same app repository.

### 2. Plan

| Story | Observable success check | Preview / real-app boundary |
| --- | --- | --- |
| As an editor, save a draft for review. | A valid title/body appears as Pending review and remains after reload. | Preview: browser storage. Real app: authenticated request and database evidence needed. |
| As an editor, understand a rejected input. | Blank or oversized fields produce a useful message without adding a row. | Shared preview function checks this narrow rule. Server validation remains required. |
| As a reviewer, publish a pending draft. | An admin can publish; a member's forged request is rejected by the server. | Preview only simulates the admin action. It cannot establish the server check. |

**Option A:** form and queue side by side. **Option B:** narrower numbered steps, with the queue after the form. They share content and logic. Choose A provisionally because it keeps the changed status beside the input on desktop; use the stacked responsive view on small screens. This is a design judgment, not measured preference.

**Real-app contract:** a member-authenticated draft route validates title/body; an admin-only publish route verifies the role on the server; content records store the state. Reuse prepared account helpers instead of inventing authentication. The exact routes/tests must be agreed in the actual SPEC.

### 3. Build and checked-release handoff

The linked A/B previews save drafts, validate fields, show a queue and simulate review. The title is limited to 80 characters and body to 500. Items stay in this browser's storage under Club Desk; Resource Roundup has a separate queue.

**Actual source checks:** the shared check script rejects blank/oversized input, trims fields, rejects a member transition in the preview function and handles repeated publication. That function is client code, so these results do not establish secure authorization.

**Release note:** preview source is downloadable and can run on a local static server. A real FastAPI backend, database tests, CI and agreed hosted release are **evidence still needed**, not implied by this page. The original App Studio remains local-only.

### 4. Improve

**Simulated critique:** “The status helps, but I might mistake the role dropdown for a login.” The example explicitly labels the control *Simulated role — not a login*, repeats the storage/authorization limit and calls the action *Publish in preview*.

**Retest task:** save a notice, switch roles, publish it, reload and explain where the record lives. A real peer must still perform this task, open an actual issue and check a meaningful feedback-driven change. This scenario is not their feedback.

**Next actual improvement to seek:** ask a peer to locate the pending draft without coaching. If they miss it, change the queue heading/order and retest the same task. Do not record that change as completed before it happens.

### Practice assessment and feedback

| Criterion | Score | Evidence and feedback |
| --- | ---: | --- |
| Working result | 14/40 | Narrow UI workflow exists; authenticated backend, persistence and forged-request evidence are absent. |
| Specification/checks/GitHub evidence | 22/35 | Clear stories and pure-function checks; add actual backend/CI links and genuine peer issue/change/retest. |
| Explanation/observation | 22/25 | Boundaries and choice are clear in writing. A real student still needs to explain them aloud. |
| **Total** | **58/100** | Finish the missing technical and human evidence before claiming full completion. |

**Specific feedback:** preserve this small scope. Implement and check the member/admin boundary in the actual server before adding features. Have a peer show that a valid draft works and an unauthorized publish fails; keep the revision and result.

</details>

## Resource Roundup

<details>
<summary>Open Resource Roundup's filled record, practice assessment and feedback</summary>

### 1. Understand / baseline

**Reader/task:** a student resource editor writes a short note for a bulletin; a reviewer checks clarity before publication. Start from the same assigned homepage/accounts/roles foundation, using a different brand and audience.

**Need hypothesis:** first-year readers may need an action and context, not just a resource name. This was not established through student interviews. The fictional author uses synthetic notes to test the presentation and keeps real student circumstances out of the record.

**Scope:** title, short note, pending/published status and a review action. Keep content plain text. A real application needs the existing server's role enforcement and persistence. A public demo dropdown is not a replacement.

### 2. Plan

**Two approaches:** A shows writing and review together; B emphasizes a short, numbered sequence. The provisional choice is B because a new editor can focus on one action. The record does not yet have a measured comparison to support that preference.

**Stories/checks:** a member saves a useful resource note; empty input is rejected with an action to take; an admin publishes it while the real server refuses a member's publish request; a reader can tell pending from published. For the UI review, use the same synthetic note in A and B and ask the peer to explain its state.

**Brand choice:** a calm, helpful voice and short sentences. Use the title to name the resource and the body to explain the next action. A proposed example note is “Bring a draft and one question to writing support”—a teaching fixture, not an actual service announcement.

### 3. Build and checked-release handoff

[Try the real browser preview](/samples/resource-roundup/b.html). It uses the same checked draft/status logic as Club Desk with its own storage key and content labels. The alternate layout is working, not another backend.

**Actual limits:** the preview has no real account, database, admin identity, network service or deployment. No genuine peer issue/PR or individual-authorship check exists for this fictional person. A real student should replace those gaps with their app's evidence, not copy the scenario's claims.

### 4. Improve

**Simulated critique:** “The title is clear, but I still need to know what to put in the note.” The example uses a prompt asking who the note is for and what they should know, with the length limit beside the field. Its confirmation says Pending review rather than implying immediate real publication.

**Next real check:** ask a peer to draft a note and explain whether it has been published. Observe without coaching, then change and retry one confusing part. Required human evidence remains pending.

### Practice assessment and feedback

| Criterion | Score | Evidence and feedback |
| --- | ---: | --- |
| Working result | 12/40 | Browser draft/review works; secure backend and persistence evidence are missing. |
| Specification/checks/GitHub evidence | 18/35 | Small stories and shared logic checks; A/B rationale and actual peer/PR/CI trail need stronger evidence. |
| Explanation/observation | 20/25 | The audience goal is clear, but the record needs one actual observed result from the author/peer. |
| **Total** | **50/100** | Replace the unsupported preference with an observed task and complete the real app evidence. |

**Specific feedback:** compare the same draft task in A and B with a real peer. Record where they hesitate, choose a direction for that reason and retest after a small change. Keep planned backend work labeled until it runs.

</details>

<a href="/is373-studio/samples/README.md" target="_self">Source and actual check script</a> · [Group examples](/examples/group) · [Your project record](/templates/project-record).
