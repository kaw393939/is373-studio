# Canvas updates to make when authenticated instructor access is available

**Status:** Prepared November 11, 2026. **No Canvas changes were made by this repository update.** The connected browser in ChatGPT was not available in this session. These files are public, contain no student records, and do **not** automatically publish to Canvas.

## 1. Homepage

Open [IS373 Canvas course 70733](https://njit.instructure.com/courses/70733), select the course **Home** page, and confirm which Page is actually set as the front page. If editing the RCE HTML source, replace the instructional content—not course-critical institutional navigation—with the student-oriented content in [canvas-homepage.html](canvas-homepage.html). Keep Canvas's built-in navigation, accessibility and authorized course materials intact.

After saving, check that the course still opens to this page and that it is **published**. Open [Student View](https://community.canvaslms.com/) using the course's own instructor controls and verify it works as a student, including on a phone-sized layout.

## 2. Clarify the November 10 RAG announcement

Find the original RAG announcement and check if the details and links are still correct. Either edit it appropriately or post a short follow-up using [canvas-rag-clarification.html](canvas-rag-clarification.html). Check announcement publication and visibility to students. **Do not post the same announcement twice.**

## 3. Verify both Plan assignments in Canvas without changing them

- [Individual Plan — Portfolio + RAG, assignment 769188](https://njit.instructure.com/courses/70733/assignments/769188): November 17, 1:00 p.m. Eastern; **two headed sections** under one individual record: portfolio/career and RAG/technical.
- [Group Plan — Content system, assignment 769189](https://njit.instructure.com/courses/70733/assignments/769189): November 17, 1:00 p.m. Eastern; one shared group record with individual contribution.
- Check **published/visible status, due/available/until dates, submission type, assignment-group placement, point values, and description**. Never infer that a due date in a public guide already matches the live Canvas gradebook.
- For Nov 24 Build, Dec 3 Checked Release and Dec 10 Improve, check their corresponding individual/group boxes using [the course's assignment list](https://njit.instructure.com/courses/70733/assignments). Do not alter due dates, weights or rubrics unless separately instructed.

## 4. Modules and navigation

From **Student View**, start at Home and see if the next click is obvious. Check that the Research/Plan module and assignment links are **published**, sequenced sensibly, and point to the current resources. Remove redundant links only after confirming no student work relies on them. Do not hide existing graded assignments or unpublished materials automatically. The new public [Get unstuck](https://kaw393939.github.io/is373-studio/course/get-unstuck) and [RAG student guide](https://kaw393939.github.io/is373-rag/students/) are optional aids, not prerequisites for submitting.

## 5. Final location and late-work policy: **verify, don't guess**

The public course guide has a final period of December 18, 8:30–11:00 a.m. Eastern and references a syllabus room subject to confirmation. Confirm the actual delivery mode (Zoom/in class/hybrid), invitation or room, presentation slots and required slide format before publishing a definitive claim.

Check Canvas's posted late/resubmission rules. If the policy is to permit revisions or waive penalties, communicate the applicable exact scope through Canvas; do not change a grade or automatically assume every assignment has a blanket extension.

## 6. Actual student acceptance test

Sign in as instructor, use Student View, and walk through:

1. **Home:** a student can identify the next workshop, the two Plan boxes and the difference between Plan and Build in under a minute.
2. **Plan assignment:** the Canvas submission control is active and explains both individual sections.
3. **Group Plan:** assignment is published and clearly explains the shared record and personal contribution.
4. **RAG help:** one tap reaches embeddings, chunking, the FastAPI bridge and the optional library survey. No links lead to a 404.
5. **Help:** a student with a stuck server knows what to share safely; no secrets in public issues.
6. **Final:** no contradictory Zoom/classroom directions between Home, Syllabus, Modules and announcements.

**Only mark “Canvas complete” after live instructor changes and Student View verification.** The GitHub course-site build and its Pages deployment are separate evidence.
