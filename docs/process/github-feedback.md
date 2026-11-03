# Keep the review in one useful issue

Use the [class review routine](/process/collaboration), then record the result in **the repository for the project being reviewed**. Course-site issues are for course-material problems, not private student work or project submissions.

## Issue → change → check → PR

1. Open **Issues → New issue**, or update an existing issue for the same problem.
2. Link the version, explain the task, expected result and what actually happened.
3. The owner responds, makes a bounded branch/change and runs the relevant checks.
4. Open a PR linked to the issue. Explain the change and checks; follow the posted review and CI requirements. Review the actual diff, not only a green badge.
5. Retest the original task. Link the result and final revision, merge when the required checks/reviews pass, and close a resolved issue.

Keep the issue/PR/check links in your existing spec or record. Do not create a separate weekly report or copy an AI transcript. A continuing issue can span stages; posted lesson-specific issue/PR requirements still apply.

```md
Title: [Stage] One clear problem
Version / task:
Expected result:
Observed result and its effect:
Useful strength / possible next action:
Owner response / change or PR link:
Retest — person, date, version, result:
Remaining problem / next step:
```

A reviewer should describe their actual observation. If unavailable later, label your own retest honestly and ask the instructor how to complete any peer-check requirement; do not invent a reviewer. GitHub permissions control who can close an issue. [Official closing guidance](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue).

**An issue does not submit coursework.** Use the matching Canvas submission setting. If the instructor later opens demo signup, a request is not a reservation; wait for confirmation and follow Canvas. [Demo status](/demo-days) · [What reviews contain](/course/milestones).
