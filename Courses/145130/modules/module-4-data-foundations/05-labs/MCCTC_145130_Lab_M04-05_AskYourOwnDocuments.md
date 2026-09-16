# Lab M04-05: Ask Your Own Documents
## 145130 Applications of AI · Module 4 · Week 12, Monday and Tuesday

**Gate:** 3, open tooling. **Duration:** two blocks. **Part 1** is Monday Build 1, 40
minutes of build time after the Gate 1 rep, and needs no model at all. **Part 2** is Tuesday
Build 1, the same 40 minutes, and needs the shared stack's stub running.
**Competencies:** 2.8.1 (types of databases, including vector), 2.8.3 (compare database
structures), 2.8.2 (the use and purpose of a database), 1.4.6 (use an electronic database to
create technical information).

**Part 1, step 6 is no AI.** Deciding where a chunk should end is the judgement this lab is
for.

**Everything runs locally.** The embeddings come from the stub model server in
`Courses/145130/anchor-project/ai-stack/`. No account, no key, and nothing leaves the
building. That is not a course rule you are being made to follow. It is the reason this lab
can exist at all.

---

## The scenario

The makerspace has eight handbook documents and the advisor says nobody reads them. Every
week somebody asks a question that one paragraph in there answers.

You are going to make the handbook answerable: cut it into pieces, turn each piece into a
list of numbers, store the numbers, and find the pieces nearest to a question.

**And then you are going to be honest about what you built**, which is the harder half.

## What you will build

A vector store, in SQLite, with the standard library. Around fifty chunks, each carrying the
file, the heading, and the character offsets it came from, so any answer can be traced back
to a line somebody wrote.

---

## Files you need

`05-labs/lab-m04-05-files/`. Copy it.

| File | State |
|---|---|
| `chunker.py` | `split_sections` and `split_long` are written. `chunk_text` is yours. |
| `inspect_chunks.py` | finished. Prints chunk statistics with no model involved. |
| `vectorstore.py` | the schema and the class are written. `cosine`, `add`, and `search` are yours. |
| `embed.py` | finished. The only file that talks to the embeddings endpoint. |
| `index_docs.py` | finished. Chunks, embeds, and stores. |
| `ask.py` | finished. Embeds a question and prints the nearest chunks. |

The documents are the shared fixture, `05-labs/fixtures/ridge-makerspace/handbook/`.

---

# PART 1 · Monday · Chunking, with no model

```
python inspect_chunks.py
```

```
8 documents found and 0 chunks produced.
chunk_text is returning an empty list. That is part 1, step 4.
```

### Step 1. Read two documents as a person

Open `02-loan-policy.md` and `07-electronics-bench.md` and read them.

**Find the place where they disagree with each other.** It is one sentence in each file and
you will need it on Tuesday. Write both sentences down with their file and heading.

### Step 2. Decide what a piece of this handbook is

Before any code, answer these three in a comment at the top of `chunker.py`.

1. If somebody asks "how long can I keep a camera kit", **what is the smallest piece of text
   that answers it completely?** Find it in `05-media-kits.md` and count its characters.
2. A whole document embeds to an average of everything in it. Name two questions that a
   whole-document chunk of `01-access-and-safety.md` would answer badly, and say why.
3. What does a chunk need to carry besides its text, so that somebody can check the answer?

### Step 3. Read the two helpers you were given

`split_sections` returns one entry per Markdown heading, with the body and the offset where
it starts. `split_long` cuts a long body into overlapping windows, preferring a blank line,
then a sentence end, then a space.

**Find the line in `split_long` that stops it cutting a word in half**, and write down what
the `overlap` argument is for in one sentence.

### Step 4. Write `chunk_text`

Follow the docstring. Six keys per chunk, offsets that point at the real file, and the
heading repeated inside the stored text.

**The heading inside the text is not decoration.** The embedding only ever sees the text. A
chunk whose heading is missing from it has thrown away the strongest clue it had about what
it is.

Then:

```
python inspect_chunks.py
```

```
max_characters 900   overlap 120   headings used

documents   8
chunks      56
shortest    76 characters
longest     608 characters
average     267 characters
```

Your numbers may differ if you decided step 5 of the docstring differently. **They should be
in this neighbourhood.** Two hundred chunks means you are splitting somewhere you should not.
Eight means the headings are being ignored.

### Step 5. Read your own chunks

```
python inspect_chunks.py --show 05-media-kits.md
```

Read every chunk of that document out loud in your head. **Find one that would not answer a
question on its own** and write down which and why.

### Step 6. Change the settings and watch what matters, with no AI

Run these three and record the chunk count, the shortest, and the longest for each.

```
python inspect_chunks.py
python inspect_chunks.py --max-characters 250 --overlap 30
python inspect_chunks.py --no-headings
```

**One of those three changes almost nothing and one of them changes everything.** Work out
which lever actually controls the chunk size for this document set, and write one paragraph
explaining why. The answer is in the shape of the documents, not in the code.

### Step 7. Write the decision down

In your README: the `max_characters`, the `overlap`, and the heading rule you are going with,
and one sentence for each saying why. You will be asked to defend these on Tuesday.

**End of Part 1.** Commit.

---

# PART 2 · Tuesday · Embeddings, storage, and search

**Two terminals.** Terminal 1 runs the stub. Terminal 2 runs your programs.

**Terminal 1:**

```
python Courses\145130\anchor-project\ai-stack\stub_model_server.py --port 11634
```

```
Stub model server on http://127.0.0.1:11634 in success mode. Press Ctrl+C to stop.
```

**Stop it with Ctrl+C when you finish the lab.**

### Step 8. Ask for one embedding and count it

```
python -c "import embed; print(embed.probe('http://127.0.0.1:11634'))"
```

```
{'base_url': 'http://127.0.0.1:11634', 'model': 'llama3.2', 'dimensions': 32}
```

**Write that number down and then forget it.** It is the stub's number. A real model returns
hundreds, and a different real model returns a different number of hundreds. **Nothing you
write today may contain the number 32.**

### Step 9. Read `embed.py` and find the four failure kinds

It handles a refused connection, a timeout, a bad status, and a reply that is not what it
expects. List them in your README with what each one means for the person running the
program.

Then make one happen. In Terminal 1, press Ctrl+C, and in Terminal 2 run the probe again.
Record the message.

### Step 10. Write `cosine`

Follow the docstring. Two rules: different lengths raise `DimensionMismatch` with both
numbers, and a zero length vector returns 0.0 rather than dividing by zero.

Check it before you go on:

```
python -c "from vectorstore import cosine; print(cosine([1,0,0],[1,0,0]), cosine([1,0],[0,1]))"
```

```
1.0 0.0
```

### Step 11. Write `add`

The index learns its length from the first vector, writes it into `index_meta`, and **refuses
any vector of a different length, with both numbers in the message.**

### Step 12. Write `search`

A full scan. Score every chunk, sort, return the best k. An empty index returns an empty
list. A query vector of the wrong length raises.

**Sort on the score and on something stable.** Two chunks with the same score have to come
back in the same order every time, or nobody can check your work.

### Step 13. Build the index

With the stub running again:

```
python index_docs.py --model-url http://127.0.0.1:11634
```

```
Ridge Creek handbook . index
  documents     8
  chunks        56
  embedded      56
  failed        0
  dimensions    32  (read from the answer, never assumed)
  seconds       0.66
```

### Step 14. Ask it three questions

```
python ask.py "how long can I keep a camera kit" --model-url http://127.0.0.1:11634
python ask.py "what do I do if the resin printer fan is not running" --model-url http://127.0.0.1:11634
python ask.py "how many items can a member have out at one time" --k 4 --model-url http://127.0.0.1:11634
```

**Record all three results, including the ranks and the scores.** Then, for each one, say
whether the top hit actually answers the question.

### Step 15. The question from step 1

Look at the third result. **One side of the disagreement you found on Monday is in the list.
The other is not.**

Write, in your README:

1. Which side came back and which did not.
2. What a person would believe if they read only what came back.
3. What should be done about it, and by whom. The answer is not a change to your code.

### Step 16. Prove the length rule

```
python -c "from vectorstore import VectorStore; s=VectorStore('output/handbook.index'); print(s.dimensions); s.search([0.1]*384)"
```

Record the error. Then write one sentence about why this had to be an error rather than a
score.

### Step 17. Write the honest paragraph

One paragraph in your README, headed **What this demonstration does not prove**. It has to
say what the stub does to build a vector and what that means about every score you recorded
in step 14.

**This paragraph is worth more marks than the search function.** A retrieval demo that hides
this is the kind of confident wrong thing this course exists to catch.

**Stop the stub.**

---

## Acceptance criteria

- [ ] The two disagreeing sentences from step 1, with files and headings
- [ ] Step 2's three answers, in `chunker.py`, in your own words
- [ ] `python inspect_chunks.py` produces around 56 chunks across 8 documents
- [ ] Step 6's three runs recorded, with the paragraph naming the lever that matters
- [ ] The chunking decisions written down with reasons
- [ ] `cosine` returns 1.0 and 0.0 on the two checks
- [ ] `index_docs.py` reports 8 documents, all chunks embedded, 0 failed, and the dimension
      it observed
- [ ] The number 32 appears nowhere in `chunker.py`, `vectorstore.py`, or your own code
- [ ] All three questions in step 14 recorded, with ranks and scores
- [ ] Step 15's three answers
- [ ] The step 16 error recorded
- [ ] The step 17 paragraph
- [ ] The stub stopped

---

## If it breaks

**`connection_refused: nothing is listening at http://127.0.0.1:11634`**
The stub is not running, or it is on another port. Start it, or pass
`--model-url http://127.0.0.1:11634`.

**`NotImplementedError: part 2, step 6`**
That function is still the starter. Write it.

**`DimensionMismatch: this index holds vectors of 32 numbers and this one has ...`**
You rebuilt the index against a different model, or you mixed two runs. Delete
`output/handbook.index` and build it again.

**Every score is about the same and the order looks random.**
That is what the stub does. Read step 17 again. It is the result, not a bug.

**`sqlite3.IntegrityError: UNIQUE constraint failed: chunks.doc_id, chunks.ordinal`**
Two chunks in one document share an ordinal. Your `ordinal` counter is resetting per section
instead of running across the document.

**The chunk count is 8.**
`chunk_text` is treating each document as one section. Check that you are calling
`split_sections` when `use_headings` is true.

**The chunk count is over 200.**
Your `max_characters` is tiny, or `split_long` is being called with the wrong arguments so
every window is one line.

---

## Stretch goal

Add a `--doc` option to `ask.py` that restricts the search to one document. Then ask the same
question with and without it, and say in one sentence what that option is really for. It is
not a better search: it is a person supplying the context the retrieval could not find.

---

## Submission checklist

- [ ] `chunker.py` and `vectorstore.py` committed
- [ ] README with every write-up from steps 1, 2, 5, 6, 7, 9, 14, 15, 16, and 17
- [ ] `output/` in `.gitignore`. The index is rebuilt from the documents
- [ ] AI usage log updated, and it says part 1 step 6 was done without a model
- [ ] `git status` clean, pushed

**This code is the retrieval half of your performance task.** You may carry it into your
project. Say so in your decision log, and the honest paragraph from step 17 belongs in your
project README too.

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| End of Monday and `inspect_chunks.py` still prints 0 chunks | SCAFFOLDED |
| Chunks produced, working through `cosine` and `add` | STANDARD |
| Searching before 30 minutes on Tuesday, or asks why the scores all look alike | EXTENDED |
| "Why not search for the words," or asks where this is used for real | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `chunk_text` is provided complete, as a worked example. Part 1 becomes reading
  it, running it, and doing steps 5 and 6.
- **Step 12** is provided complete. You write `cosine` and `add` only.
- **Steps 1, 6, 14, 15, 16, and 17 stay.** They are the lab.
- **Checkpoints:** show your instructor the step 6 table at the end of Monday, and the step
  14 results on Tuesday.

**Acceptance criteria:** `cosine` and `add` working, the index building with the dimension
read from the answer, all three questions recorded, and steps 15 and 17 written.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Add a keyword search over the same chunks, using SQLite's full text
search, and run all three step 14 questions through both. Then write a comparison: which one
wins on each question, and what that tells you given that the stub's vectors are a hash.

**Added requirement 2.** Make `search` return a second score alongside the similarity: how
many of the question's words appear in the chunk. Then say in your README what you would do
with two scores, and why combining them into one number is a decision rather than an
improvement.

**Hint, not the answer.** Read the SQLite documentation page "SQLite FTS5 Extension",
`https://www.sqlite.org/fts5.html`. Look for `CREATE VIRTUAL TABLE ... USING fts5` and for
the `bm25()` function, and check whether FTS5 is compiled into your Python's SQLite with
`SELECT sqlite_compileoption_used('ENABLE_FTS5')`. **If it returns 0, say so in your README
and fall back to counting matched words yourself.** That is a real answer, not a failure.

**Acceptance criteria:** all STANDARD criteria, both searches running over the same chunks,
the comparison written, and an honest note about what the stub makes uncomparable.

---

## APPLIED

**For the student who asks where this is used for real.** A help desk that answers from a
company's own documents. A legal team searching its own filings. A study tool over your own
class notes. In all three the value is the same: the answer comes with a citation you can
open.

**Changed scenario.** Bring your own document set, with no personal information in anyone's
writing, and with permission from whoever wrote it: your own class notes, a game's public
wiki pages you have already saved, a club's rulebook, the documentation of a library you use.
**At least six documents.** If they are not Markdown, converting them is your first step, and
it counts as part of the lab.

Part 1 is the same three questions asked of your documents, and step 1 becomes: find two
places in your set that disagree, or state plainly that you looked and found none, with how
you looked.

**The extra requirement that makes it the same lab.** Steps 15, 16, and 17 are unchanged and
required. If your set really has no contradiction, step 15 becomes: find a question your set
answers in two places at different levels of detail, and say which chunk came back.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether every hit can
be traced to a line in a file you can open.
