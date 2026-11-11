---
title: Get unstuck in IS373
description: Find a small next step without rebuilding your server, changing stacks or starting another assignment.
---

# Get unstuck: one problem, one next step

If you are behind, **keep your existing work**. You do not need a new server, GitHub repository, AI framework, or fully rewritten application merely to recover from a blocker. Use the [next-class card](/course/section-001#before-next-class) to see the current workshop and the [Plan/Build milestone checklist](/course/milestones) to see what counts now.

## First decide what is blocking you

| I am stuck on… | Start here |
| --- | --- |
| Which assignment to submit | [Two Canvas boxes and three deliverables](/course/milestones#the-immediate-plan-hand-in) |
| My existing App Studio project | [App Studio original README](https://github.com/kaw393939/is373-app-studio) |
| Docker, Traefik or HTTPS | [Existing Server Studio guide](https://github.com/kaw393939/373_hosting) |
| Building an individual RAG | [Reuse your FastAPI app](https://kaw393939.github.io/is373-rag/students/from-app-studio) |
| Understanding retrieval | [Embeddings](https://kaw393939.github.io/is373-rag/students/embeddings) and [chunking](https://kaw393939.github.io/is373-rag/students/chunking) |
| An irrelevant RAG answer | [RAG debugging checklist](https://kaw393939.github.io/is373-rag/students/stuck) |
| Group project scope or a partner | [Group content brief](/projects/group) |
| Preparing a demonstration | [Demo Day evidence](/demo-days) |

## Bring a useful blocker report

Copy just these **five fields** into your existing GitHub issue or bring them to class:

1. **Current repo / app URL:** link to your own project, not just the instructor's template.
2. **Expected:** one small action and what should happen.
3. **Observed:** the exact error or unexpected result (remove secrets and private data).
4. **What I tried:** one or two concrete attempts and their results.
5. **My next question:** the specific help you need to continue.

Keep passwords, API keys, raw `.env` contents and private student information out of public issues and AI chats. If a classmate helped, record what you personally tested and understood.

## A prompt to ask an AI coding partner

```text
I am an IS373 student using my existing project. Read its README, SPEC,
and relevant files before editing. Here is my actual blocker:
[goal / expected result / observed redacted error / what I tried].
Explain the likely cause in plain English, propose the smallest safe test,
and wait for my approval before changes. Do not rebuild my server, erase
my database, reset credentials, change DNS or introduce a new stack.
After a change, show which tests you actually ran and one question I
should be able to answer about the code.
```

**A mock interface is not completed RAG**; source-backed retrieval and actual model generation are required by the original assignment for the hosted demonstration. If you cannot run the model yet, label that step incomplete while working through import and retrieval.

[Current class and next steps](/course/section-001) · [Original assignment](https://njit.instructure.com/courses/70733/assignments) · [Technical research handouts](/handouts/) · [Student RAG resources](https://kaw393939.github.io/is373-rag/students/)
