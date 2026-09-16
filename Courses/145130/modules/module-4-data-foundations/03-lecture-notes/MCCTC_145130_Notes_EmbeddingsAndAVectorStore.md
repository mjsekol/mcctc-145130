# Embeddings, and a Vector Store You Can Read
## 145130 Applications of AI · Module 4 · Week 12, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W12_VectorStore.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W12_VectorStore.pptx)

**Every command and every number below was run on the build machine against the shared
stack's stub model server on port 11634.**

---

## What an embedding is

An **embedding** is a list of numbers that stands for a piece of text. A model produces it,
and the direction the list points is meant to encode what the text is about, so that two
pieces of text about the same thing point in similar directions.

That is the whole idea, and two things follow from it that people skip.

**An embedding is not readable.** A wrong one looks exactly like a right one. There is no
version of "eyeballing the output" here, which is why every reply is checked for shape before
it is used and why the length is never assumed.

**The meaning comes from the model, not from the store.** Your vector store is a table and a
loop. If the model is a hash function, the numbers are stable and meaningless, and the store
will happily rank them.

---

## The call, and the number you must not write down

```
POST http://127.0.0.1:11634/api/embeddings
{"model": "llama3.2", "prompt": "how long can I keep a camera kit"}
-> {"model": "llama3.2", "embedding": [0.2657, 0.1585, ...]}
```

```
python -c "import embed; print(embed.probe('http://127.0.0.1:11634'))"
```

```
{'base_url': 'http://127.0.0.1:11634', 'model': 'llama3.2', 'dimensions': 32}
```

**Write 32 in your README and nowhere else.** The stub returns 32 numbers. A real model
returns hundreds, and a different real model returns a different number of hundreds. **Code
with 32 in it passes every test on this machine and breaks on the first lab machine with a
model on it**, which is the worst possible place for it to break.

Read the length from the answer, store it with the index, and refuse anything that disagrees:

```python
current = self.dimensions
if current is None:
    self.set_meta("dimensions", len(vector))
elif len(vector) != current:
    raise DimensionMismatch(
        f"this index holds vectors of {current} numbers and this one has {len(vector)}. ...")
```

**Both numbers go in the message.** An error that says "dimension mismatch" tells nobody
which two things did not match.

---

## Worked example 1: cosine similarity, in eight lines

The cosine of the angle between two vectors. 1.0 is the same direction, 0.0 is at right
angles, -1.0 is opposite.

```python
def cosine(a, b):
    if len(a) != len(b):
        raise DimensionMismatch(f"cannot compare {len(a)} numbers with {len(b)}")
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    if length_a == 0.0 or length_b == 0.0:
        return 0.0
    return dot / (length_a * length_b)
```

```
python -c "from vectorstore import cosine; print(cosine([1,0,0],[1,0,0]), cosine([1,0],[0,1]))"
```

```
1.0 0.0
```

**Why cosine and not distance.** Cosine ignores length, so a chunk does not score higher for
being longer. That is exactly what you want when the things you are comparing are paragraphs
of different sizes.

---

## Worked example 2: the store is two tables

```sql
CREATE TABLE index_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);

CREATE TABLE chunks (
    chunk_id   INTEGER PRIMARY KEY,
    doc_id     TEXT NOT NULL,
    heading    TEXT NOT NULL,
    ordinal    INTEGER NOT NULL,
    char_start INTEGER NOT NULL,
    char_end   INTEGER NOT NULL,
    text       TEXT NOT NULL,
    UNIQUE (doc_id, ordinal)
);

CREATE TABLE vectors (
    chunk_id INTEGER PRIMARY KEY REFERENCES chunks (chunk_id) ON DELETE CASCADE,
    dim      INTEGER NOT NULL,
    vector   TEXT NOT NULL
);
```

Everything from Week 10 is in there. A primary key. A foreign key with a cascade, because a
vector is part of its chunk and has no meaning without it. A `UNIQUE` constraint saying a
document has one chunk per ordinal. **A vector database is a database.**

The vector is stored as JSON text. At this size that is the right call: you can open the file
with any tool and read it. At a million chunks it is the wrong call, because parsing JSON for
every row is then the slow part, and packed binary floats are roughly a third of the size.
**Say which size you are at when you choose.**

Real build:

```
Ridge Creek handbook . index
  documents     8
  chunks        56
  embedded      56
  failed        0
  dimensions    32  (read from the answer, never assumed)
  seconds       0.64
```

---

## Worked example 3: search is a full scan, and that is fine

```python
rows = self.connection.execute(
    "SELECT c.chunk_id, c.doc_id, c.heading, ..., v.vector "
    "FROM chunks c JOIN vectors v ON v.chunk_id = c.chunk_id").fetchall()
scored = []
for chunk_id, doc_id, heading, ordinal, start, end, text, vector_json in rows:
    scored.append({..., "score": cosine(query_vector, json.loads(vector_json))})
scored.sort(key=lambda hit: (-hit["score"], hit["doc_id"], hit["ordinal"]))
return scored[:k]
```

**Every row is compared. At 56 chunks that is the right answer**, and saying so is more useful
than pretending an index is required. A real vector database adds an approximate nearest
neighbour index, which matters in the millions and costs you exactness in return.

**Look at the sort key.** It sorts on the score **and** on something stable. Two chunks with
the same score have to come back in the same order every run, or nobody can check your work,
including you.

Real query:

```
Question: "how long can I keep a camera kit"
Retrieved 4 chunks. Nothing below was generated. Every line is from a handbook file.

1. score +0.3437   05-media-kits.md . What is in a kit   characters 85-408
2. score +0.2701   04-resin-printer-sop.md . Loan length   characters 1357-1549
3. score +0.2372   06-laptop-carts.md . Laptop Carts   characters 15-59
4. score +0.2068   03-filament-printer-sop.md . Standard Operating Procedure   characters 52-139
```

**Hit 2 is about the resin printer.** Hits 3 and 4 are the "Invented sample document for this
course" lines. That is what a hash-based stub does, and it is tomorrow's lesson.

---

## The error kinds, and why they are named

`embed.py` is the only file that talks to the endpoint, and it turns every failure into a kind
you can branch on:

| Kind | What it means for the person running it |
|---|---|
| `connection_refused` | the server is not running. Start it. |
| `timeout` | the server is there and slow. Do not restart it. |
| `model_http_error` | the server answered and refused. Check the model name. |
| `malformed_json`, `missing_field`, `empty_embedding`, `bad_value` | the answer is not the shape we expect. Usually the wrong port. |

Real, with nothing listening:

```
The embeddings endpoint did not answer: connection_refused: nothing is listening at http://127.0.0.1:11634
Start the stub in another terminal:
  python Courses\145130\anchor-project\ai-stack\stub_model_server.py --port 11634
```

**Four problems, four fixes, four messages.** One message that says "error" for all of them
wastes a period, and you learned that in Module 1.

---

## The wrong version, and what it produces

```python
DIMENSIONS = 32          # the model's embedding size

def add(self, chunk, vector):
    assert len(vector) == DIMENSIONS
    ...
```

Against the stub this is correct, every test passes, and the index builds in under a second.

Against a real model it produces this, on the first chunk:

```
AssertionError
```

with no message, no numbers, and nothing to tell the next person that the constant at the top
of the file is the problem.

**Why it is tempting.** You measured it. `probe()` said 32, so 32 is a fact about the system,
and putting a measured fact in a constant is usually good practice. **It is a fact about the
stub**, and the stub is scaffolding.

The test that catches it is the one that builds the whole index with a fake embedder returning
384 numbers, and then again with 7. Both pass on the corrected version. Neither passes on this
one.

---

## Vocabulary

| Term | What it means |
|---|---|
| **embedding** | a list of numbers standing for a piece of text |
| **dimensions** | how many numbers are in one embedding |
| **cosine similarity** | the cosine of the angle between two vectors, from -1.0 to 1.0 |
| **vector store** | a table of vectors plus a way to find the nearest |
| **full scan** | comparing every row, with no index |
| **approximate nearest neighbour** | an index that finds close-enough neighbours without comparing everything |

---

## Self-check

**1.** Your index holds 32 number vectors and a question arrives as 384 numbers. Why must this
be an error and not a score?

**2.** Name two things the sort key `(-score, doc_id, ordinal)` gives you that `(-score)` alone
does not.

**3.** Your search returns results, the plumbing works, and your partner says the system is
finished. What is missing?

### Answers

**1.** Because cosine similarity between vectors of different lengths is not defined, and if
you padded or truncated to force it you would get a number. That number would sort, print, and
look exactly like a real score. **The failure mode of not raising is a search that works and
is meaningless**, which is the hardest kind of wrong to find.

**2.** A result order that is the same on two runs, so a test can check it and so you can
compare today's output with yesterday's. And a tie broken by something a person can predict,
so "why did that one come first" has an answer.

**3.** Any evidence that the results are good. The plumbing being proven and the quality being
proven are different claims, and on the stub only the first one is available, because the stub
builds its vector from a hash of the text. Say that out loud before somebody else does.
