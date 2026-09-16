# Additional Resources · Week 12
## 145130 Applications of AI · Module 4
### Topics: chunking, embeddings, vector stores, retrieval versus fine tuning

Links are marked **Confident** or **[VERIFY]**. **A [VERIFY] link has not been confirmed live
from this machine and must be clicked before it is assigned.**

**Everything this week runs locally**, against the shared stack's stub on **port 11634**. No
account, no key, and nothing leaves the building.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The shared stack's own I/O specification | Mon, Tue | On-level | 20 min |
| 2 | The stub model server source | Tue | On-level | 20 min |
| 3 | SQLite: FTS5 full text search | Tue, Wed | Extension | 30 min |
| 4 | Python documentation: `math` and `json` | Tue | Remediation | 10 min |
| 5 | A free video on embeddings | Any | Remediation | under 20 min |
| 6 | The handbook, read as a corpus | Mon | On-level | 20 min |
| 7 | Your own Week 12 numbers, for self-checking | All week | On-level | 5 min |
| 8 | The module's lecture notes, self-check sections | Before Friday | Review | 20 min |
| 9 | Gate 1 bank, the EXPLAIN reps | Before Friday | Review | 10 min each |
| 10 | Side quest: your own notes, made queryable | Fri, Period 8 | Extension | 1-2 blocks |

---

## 1. Primary reading: the shared stack's I/O specification

`Courses/145130/anchor-project/ai-stack/docs/io-spec.md` · **it is on your machine.**

**Why this one.** It is the contract, it was written for this course, and **section 7 is the
embeddings endpoint you use all week**. It also says, in the course's own words, that the stub
returns a deterministic 32 number vector built from a hash, and that a retrieval lab on the
stub tests your plumbing and never your results.

**Assign a question:** *Read section 7. What does the stub guarantee about the same text
producing the same vector, and what does it explicitly not guarantee?*

**Time.** 20 minutes, section 7 plus section 5. **Level.** On-level, and required before
Tuesday.

---

## 2. The stub model server source

`Courses/145130/anchor-project/ai-stack/stub_model_server.py` · **on your machine.**

**Why this one.** Four hundred lines of readable standard library Python, and the function you
want is `deterministic_embedding`. It is nine lines and it explains the whole of Week 12's
honesty problem.

**Assign a question:** *Read `deterministic_embedding`. Say in two sentences why two sentences
that mean the same thing get completely unrelated vectors from it.*

**Do not modify this file.** It is the shared stack and other modules depend on it.

**Time.** 20 minutes. **Level.** On-level. **This is the best twenty minutes in the week** for
anybody who is uneasy about what embeddings are.

---

## 3. SQLite FTS5 full text search

`https://www.sqlite.org/fts5.html` · **Confident.**

**Why this one.** It is the EXTENDED option for Lab M04-05: a keyword search over the same
chunks, so you can compare it with the vector search on the same questions.

**Check first**, because FTS5 is a compile-time option:

```
python -c "import sqlite3; print(sqlite3.connect(':memory:').execute(\"SELECT sqlite_compileoption_used('ENABLE_FTS5')\").fetchone())"
```

On the build machine this returns `(1,)` and a virtual table creates without error.
**Confirm it on a lab machine before assigning.** If it returns `(0,)`, say so in your README
and count matched words yourself instead. That is a real answer rather than a failure.

**Time.** 30 minutes. **Level.** Extension.

---

## 4. `math` and `json`

`https://docs.python.org/3/library/math.html` · **Confident.**
`https://docs.python.org/3/library/json.html` · **Confident.**

**Why these.** `math.sqrt` is the whole of cosine similarity, and `json.dumps` and
`json.loads` are how a vector gets into and out of a TEXT column.

**Assign a question:** *A vector comes back out of the database as a string. Which one line
turns it back into a list of floats, and what happens if the string is truncated?*

**Time.** 10 minutes. **Level.** Remediation.

---

## 5. A free video

**[VERIFY]. No specific video is linked**, because none has been confirmed from this machine.

**What to look for:** under twenty minutes, on what an embedding is. **Watch it first and
check two things.** Does it say that the meaning comes from the model rather than from the
vector database? And does it avoid claiming that similarity search is the same thing as
understanding? Many videos on this topic are made by companies selling a vector database, and
it shows.

**Level.** Remediation.

---

## 6. The handbook, read as a corpus

`05-labs/fixtures/ridge-makerspace/handbook/` · **on your machine.** Eight documents, about
four thousand words.

**Why this one.** You cannot judge a retrieval system over a corpus you have not read. **Read
all eight before Tuesday**, which takes twenty minutes, and you will be able to tell instantly
whether a result is the right paragraph.

**Assign a question:** *Find every place two documents say something about the same rule.
There is at least one pair that disagrees.*

**Time.** 20 minutes. **Level.** On-level. **Everybody, before Tuesday.**

---

## 7. Numbers for self-checking

Your chunk counts will differ if your rules differ, and that is fine as long as you wrote the
rules down. These are what the reference implementation produces:

- 8 documents, 56 chunks at `max_characters 900` and `overlap 120`
- shortest chunk 76 characters, longest 608, average 267
- 79 chunks at `max_characters 250` and `overlap 30`
- 22 chunks with headings ignored
- **56 chunks at `max_characters 5000`**, which is the number that should make you stop and
  think
- The stub returns 32 numbers. **That number belongs in your README and in no `.py` file.**

---

## 8. The self-checks you already have

This week's four notes are `ChunkingADocumentSet`, `EmbeddingsAndAVectorStore`,
`RetrievalVersusFineTuning`, and `WhatRetrievalGetsWrong`.

**`RetrievalVersusFineTuning` question 1 is the exit criterion for this module.** If you can
answer it without looking, you are ready for the exit assessment's item 21 and for the
corresponding section of your memo.

**Level.** Review.

---

## 9. Gate 1 reps for review

The EXPLAIN reps, 16 to 20, are the best short review for the analysis half of the exit
assessment. Reps 19 and 20 map onto exit assessment items 21 and 22 almost directly.

**Level.** Review.

---

## 10. Side quest: make your own notes queryable

An hour or two, and the best possible revision for the WebXam. Take your own notes from
Modules 1 to 4, or a set of documents you have permission to use with no personal information
in anybody's writing, and run the whole Week 12 pipeline over them: chunk, embed, store, query.

**Then do the honest part.** Ask three questions you have not tried, record what came back, and
write the paragraph about what the demonstration does not prove.

**Level.** Extension. This is the APPLIED option of Lab M04-05 and it counts for it.

---

## For the student who is behind

1. Resource 2, the stub's `deterministic_embedding` function, read and explained in two
   sentences
2. Lab M04-05 SCAFFOLDED, with `chunk_text` and `search` provided
3. Steps 14 to 17 of the lab, which are the graded half, regardless of how far the code got
4. Before Friday: the `RetrievalVersusFineTuning` notes and its three self-check questions

## For the student who is ahead

- Lab M04-05 EXTENDED, full text search alongside the vector search
- Resource 3, FTS5, including the compile option check
- The side quest in resource 10, over their own notes
- Argue the fine tuning side of one workload in their memo, in writing, as a rebuttal to their
  own recommendation
