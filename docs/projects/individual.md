# Deliverable 2 - Individual RAG app + technical research

**Your product is your own working hosted RAG application. Your research is vector/graph databases, RAG, chunking, content import and evaluation.** Use a vector database, graph database, or both. Everyone researches both database approaches and explains the choice. Reuse your existing app, server and project records. This is distinct from **Deliverable 1, your career-informed portfolio**, and **Deliverable 3, your group content system**. The app can run within your portfolio site; present it as its own technical product and case study. Keep its evidence under **2. Individual RAG app + technical research**.

## Understand the whole process

RAG means retrieval-augmented generation: retrieve relevant external evidence, then give it to a model to help generate an answer. A chat interface alone does not demonstrate retrieval. Show what content entered the system, how you represented it, which evidence came back and how the answer used it.

- Import permitted content; keep a source manifest with document IDs, origin, date/version and permission.
- Parse, clean and deduplicate. Research chunking and explain how you preserve source locations.
- Vector path: create chunks, generate real embeddings, store vectors and metadata, embed the question and retrieve similar passages.
- Graph path: define entities and typed relationships, retain supporting source passages, import them into a graph database and retrieve relevant paths/facts for the question.
- Combined path: explain how the two retrieval methods contribute different evidence.
- Generate a source-supported answer, show usable references and handle insufficient evidence honestly.

All students explain chunking, embeddings and graph modeling in their research. Implement the steps that fit your chosen retrieval architecture; a graph-only project does not need an unused vector index.

## A manageable first system

Start with approximately five short permitted documents and five evaluation questions. Include an exact-term question, a paraphrase, a relationship question where appropriate, and an unanswerable question. These are starting-scope guidelines; agree an equivalent corpus/query set with the instructor when the domain differs.

Use real retrieval and generation for the working demo. Record the actual database, embedding model if used, generation model/provider and versions/configuration. Keep credentials on the server. A mocked response can help test the interface but must be labeled and does not establish a working RAG system.

Keep database services private, enforce server-side permissions for import/admin actions, limit public requests and document cost/resource limits. Do not put secrets or private student records in the corpus. A small checked system is enough; paid infrastructure, model training and a production-scale service are not required.

## Evidence to show

| Evidence | What it should establish |
| --- | --- |
| Source and import record | Where content came from; stable IDs; repeat import without duplicates; how changed content is handled |
| Representation | A real chunk plus metadata/embedding configuration, or entities/relationships with source support |
| Retrieval trace | Question, returned source/chunk IDs or graph paths and what was relevant/missing |
| Answer evaluation | Expected evidence, actual answer, citation support and an unanswerable case |
| Hosted operation | Working website/chat, persistent storage, chosen revision and repeatable setup |
| Improvement | Real peer issue, your response, meaningful change and retest |

Compare a simple keyword/structured baseline with your selected approach. Compare two bounded design choices such as chunk boundaries, metadata filters, graph schema or answer presentation; one implementation and a documented experiment are sufficient.

## Research now; implement in the next stage

For the research workshop and Plan, explain the process, compare approaches, prepare sources/questions and identify model access, cost and hosting questions. A running app is not required at Plan. The handout is a research guide; ContentDesk is an ETL/authentication reference, not a complete RAG starter. Bring unresolved setup/model-access questions to the workshop before committing to a stack or paid service. Working hosted implementation is required at Build. [Plan example](/examples/plan).

For a partner walkthrough, use the [research review index and workshop prompts](/templates/project-record#research-review-index) in your existing combined individual record. Let a reader trace one source through representation, retrieval and a cited answer; mark proposed steps and expected outputs as planned until executed. Explain the alternative considered, the reason for your choice and the next check. Record peer questions, decisions, changes and verification in the existing issue/record workflow, without another report or issue quota.

## Start here

[Independent database/RAG handout](/handouts/database-rag-research) · [Printable PDF](/handouts/IS373_Vector_Graph_and_RAG_Research.pdf) · [Career-informed portfolio](/projects/portfolio) · [Review dates](/course/section-001).

Optional student support: the [step-by-step RAG guide](https://github.com/kaw393939/is373-rag/blob/main/docs/students/index.md) includes [copy-ready AI coding prompts](https://github.com/kaw393939/is373-rag/blob/main/docs/students/prompts.md), a [five-question evaluation guide](https://github.com/kaw393939/is373-rag/blob/main/docs/students/check.md), and an optional small local lab. This is not another deliverable, a required stack, or a complete hosted solution. Keep this course brief and Canvas as the authority.

Optional instructor example: the [IS373 RAG research library](https://github.com/kaw393939/is373-rag/blob/main/docs/research/index.md) and [repository](https://github.com/kaw393939/is373-rag) show research, proposed architecture and planned validation. They contain documentation, not a working RAG app or a mandatory stack. Use the original sources to inform your own bounded specification and actual checks.

**The November 6 App Studio remains local with its original scope and rubric.** This later hosted RAG requirement does not change that submission.
