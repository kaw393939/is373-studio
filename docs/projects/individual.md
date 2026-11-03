# Your individual RAG application

**Build a working RAG chat on your own hosted portfolio website using a vector database, graph database, or both.** Everyone researches both database approaches and explains the choice. Reuse your existing app, server and project records. The portfolio and RAG are connected individual deliverables; the group content system is separate.

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

## Start here

[Independent database/RAG handout](/handouts/database-rag-research) · [Printable PDF](/handouts/IS373_Vector_Graph_and_RAG_Research.pdf) · [Career-informed portfolio](/projects/portfolio) · [Review dates](/course/section-001).

**The November 6 App Studio remains local with its original scope and rubric.** This later hosted RAG requirement does not change that submission.
