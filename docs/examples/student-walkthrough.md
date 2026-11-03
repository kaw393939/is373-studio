# Walkthrough: what was checked and what remains

> Reference scope: these earlier content-app examples demonstrate parts of the process. They do not implement the current hosted RAG requirement. Follow the [current portfolio/RAG/group briefs](/course/overview) and [project review rubric](/course/milestones); any practice scores below are historical teaching examples.

**Teaching rehearsal, November 2, 2026.** A typical student's workload and learning have not been measured. The people, clients and peer comments in the worked records are fictional. No student submission, grade or group membership was manufactured.

## Follow the path

1. Open [Section 001](/course/section-001#before-next-class) and choose a class date. All four project-review stages are now published in Canvas; use their posted deadlines.
2. Continue the existing Studios; both posted deadlines remain November 6. App Studio starts locally.
3. Reuse the record to plan one task, compare two approaches and build a narrow workflow.
4. Use the checked-release handoff to separate local tests, CI and actual hosted evidence.
5. During protected classes, get a real peer issue, make a useful change and retest. Keep the same URLs for the December 18 demo.

## Confusions addressed

| Possible wrong turn | Clarification |
| --- | --- |
| “Are the review dates still only tentative?” | The four project-review stages are now published in Canvas. The original Studios remain due Nov 6; Plan Nov 17, Build Nov 24, Checked Release Dec 3 and Improve Dec 10 are official posted deadlines. |
| “I must deploy App Studio before Nov 6.” | Its published requirement is local; the later hosted project is a separate requirement. |
| “The static role selector proves authorization.” | Every preview labels the role and browser storage as simulated. Real server-role checks still need separate evidence. |
| “I need all the AI infrastructure.” | Start with a small corpus and actual RAG using vector, graph or both. Paid infrastructure and model training are not required. |
| “A fake customer's answer counts as peer review.” | Roleplay may support questions. Actual people must supply teamwork and peer/change/retest evidence. |
| “Demo details match IS117.” | IS373's posted demo is Dec 18; delivery mode still needs Canvas clarification. Protected work is Dec 8/10. |

## Actual technical evidence

The preview source includes `verify.mjs`: meaningful checks for required/oversized fields, state transitions, invalid JSON, rejected fixtures, deduplication, source retention and repeat-import behavior. These run against the same pure functions used by the browser previews. They do not test secure backend enforcement or a deployed service.

The browser receipt below records the task and narrow-screen checks separately. Full screen-reader testing and real-student observation remain pending. Do not infer them from source files or a successful build. <a href="/is373-studio/samples/README.md" target="_self">Preview README</a>.

## Next real-student check

Ask two or three volunteers to find the next task, locate the current Canvas deadlines, try a preview task and identify the missing backend evidence. Have real partners use the review routine, then log elapsed time, questions and wrong turns. This pilot is **pending**, not a completed usability study.

## Browser review receipt · November 2, 2026

These were agent-operated student-path checks, not a study of real students.

Followed home → class card → individual record/preview → group record/preview. Checked the December 10 card’s evening target. Saved a synthetic draft as Demo member, switched to Demo admin, and published it in the preview; B retained the same browser queue. Study Brief imported two items, skipped one duplicate and rejected one invalid row; a second import added none, skipped three and rejected one. Synthetic review data was reset afterward.

Fixed: misleading duplicate example navigation, unclear course-specific review wording, public source-link routing, and overgenerous scores for missing server/team evidence. Phone-width import controls, course navigation and career page fit without page-level horizontal overflow. No secure backend, actual hosted service, Canvas submission or human peer session was completed.

**Published-site check:** GitHub Pages navigation and static-preview JavaScript were verified after deployment. The local-link/anchor checks and preview logic checks also passed in GitHub Actions. External employer availability can still change.
