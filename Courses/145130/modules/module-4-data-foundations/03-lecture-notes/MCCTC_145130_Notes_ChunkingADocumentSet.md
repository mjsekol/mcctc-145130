# Chunking: Deciding What a Piece of a Document Is
## 145130 Applications of AI · Module 4 · Week 12, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W12_Chunking.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W12_Chunking.pptx)

**Every count below came from running `inspect_chunks.py` on the build machine against the
eight handbook documents. No model is involved in this lesson.**

---

## Why you cannot retrieve a whole document

A model has a context window, so you cannot hand it eight documents. And even if you could,
you should not: handing it the whole handbook to answer one question about the vinyl cutter
buries the sentence that matters in four thousand words that do not.

**Retrieval works on pieces. The size and the boundary of a piece decide what the system can
answer**, and those are decisions you make before any embedding exists.

---

## The two ways to get it wrong

**Too small, and a chunk stops being an answer.**

> "Five days."

True, and useless. Five days of what?

**Too big, and every chunk looks like every other chunk.** A whole document turns into one
vector, and that vector is an average of everything in the document. A document that covers
hours, guests, eye protection, training, damage, and fire is not strongly about any of them.
It comes back for every question, which is the same as coming back for none.

---

## Worked example 1: split on headings first

A heading is a boundary somebody who already knew the content chose. Use it.

```python
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")

def split_sections(text):
    """(heading, body, start_offset) for each Markdown heading."""
```

Then cut any section longer than `max_characters` at a blank line, a sentence end, or a
space, **never in the middle of a word**, repeating `overlap` characters at the seam.

Real output on the handbook:

```
max_characters 900   overlap 120   headings used

documents   8
chunks      56
shortest    76 characters
longest     608 characters
average     267 characters

  document                     chunks  shortest  longest
  ---------------------------- ------  --------  -------
  01-access-and-safety.md           7       184      474
  02-loan-policy.md                 8        98      361
  03-filament-printer-sop.md        6       164      440
  04-resin-printer-sop.md           7       115      321
  05-media-kits.md                  6        80      357
  06-laptop-carts.md                7        76      298
  07-electronics-bench.md           8        86      412
  08-records-and-privacy.md         7        90      608
```

---

## Worked example 2: measure the lever before you turn it

Three settings, three real runs:

| Run | Chunks | Shortest | Longest |
|---|---|---|---|
| `--max-characters 900 --overlap 120` | 56 | 76 | 608 |
| `--max-characters 250 --overlap 30` | 79 | 76 | 368 |
| `--no-headings` | 22 | 319 | 928 |
| `--max-characters 5000 --overlap 0` | **56** | 76 | 608 |

**Look at the last row.** Raising the maximum from 900 to 5000 changes nothing, because **no
section of this handbook is 900 characters long.** The longest chunk is 608. For this document
set, `max_characters` is a safety net that never catches anything, and **the heading rule is
the chunking strategy.**

Turn the headings off and 56 chunks become 22, with the longest at 928. That is the lever.

**The general rule.** A parameter you did not measure is a parameter you are guessing about.
Somebody will tell you that 512 tokens with 64 of overlap is the industry standard. Ask them
what it does to your documents, and then go and find out, which takes one command.

---

## Worked example 3: the rule with a cost, and the cost

Short sections are a problem. `05-media-kits.md` has this:

```markdown
## Loan length

Media kits are a three day loan.
```

Thirty two characters. Stored on its own it is the "five days" problem: a true sentence with
no subject. So the chunker attaches a section under `min_characters` to the chunk before it.

Here is what that produces, really:

```
--- chunk 2  heading: 'Check the contents card'  characters 435-701  length 303
05-media-kits.md . Check the contents card

Count the contents against the card at the kiosk before you leave and again before you
return. The staff member counts with you. That is a two minute step that settles every
argument about who lost the windscreen.

Loan length
Media kits are a three day loan.
```

**The answer to "how long can I keep a camera kit" is now filed under a heading about
contents cards.** That is a defensible rule producing a bad outcome for one question, and you
would never know unless you read your own chunks.

The alternatives, all defensible, all with costs:

- **Store it anyway**, and accept a chunk that cannot answer on its own.
- **Attach it to the chunk after**, so it leads the section it introduces rather than trailing
  one it has nothing to do with.
- **Attach the parent heading** so the chunk reads `05-media-kits.md . Loan length`.

**Read your chunks.** Nothing else finds this.

---

## What a chunk has to carry

```python
{
    "doc_id": "05-media-kits.md",
    "heading": "Memory cards",
    "ordinal": 3,
    "char_start": 717,
    "char_end": 925,
    "text": "05-media-kits.md . Memory cards\n\nThe card in the kit is a lab card. ...",
}
```

That is a real record out of the built index, printed on the build machine.

Two things in there are not obvious.

**The heading is repeated inside the stored text.** The embedding only ever sees `text`. A
chunk whose heading is not in it has thrown away the strongest clue it had about what it is
about.

**The character offsets point at the real file.** They are how a hit gets traced back to a
line somebody wrote. **That traceability is the honest reason to prefer retrieval over fine
tuning**, and it exists only if you keep the offsets here, on Monday, before anything
interesting happens.

---

## The wrong version, and what it produces

```python
def chunk(text, size=500):
    return [text[i:i + size] for i in range(0, len(text), size)]
```

Four lines, no dependencies, and it runs.

Run it on the loan policy and print the first sixty characters of each piece:

```
0 '# Ridge Creek Makerspace: Loan Policy\n\nInvented sample docum'
1 ' Electronics bench equipment is a fourteen day loan. Media k'
2 'ut.\n\n## Late items\n\nAn item is late when the current date is'
3 ' because the old loan is the record of\nwhat actually happene'
```

**Chunk 2 starts with the letters `ut.`**, which is the tail of the word "out" in the
sentence "the item stays on your record as still out". The word is split across two pieces
and the sentence it is in is in neither of them whole. Chunk 1
starts in the middle of a list of loan lengths with no heading above it to say what the list
is. No chunk knows which document it came from, none knows where it starts in the file, and
the sentence at every seam exists in neither piece.

**Why it is tempting.** It is the shortest thing that produces chunks, it never crashes, and
the output looks plausible in a list. Every problem with it shows up later, in the results,
where it looks like the model being bad rather than the chunker being lazy.

---

## Vocabulary

| Term | What it means |
|---|---|
| **chunk** | one retrievable piece of a document |
| **chunk boundary** | where one piece stops and the next starts |
| **overlap** | characters repeated at a seam so a cut sentence survives whole somewhere |
| **offset** | where in the original file this piece starts and ends |
| **corpus** | the whole set of documents you are retrieving over |
| **context window** | how much text a model can be given at once |

---

## Self-check

**1.** Raising `max_characters` from 900 to 5000 changed nothing on this handbook. Explain
why, and say what you would have to measure to know that in advance.

**2.** Your chunker produces 8 chunks from 8 documents. What is it doing, and what will that
do to your search results?

**3.** Why is the heading stored inside the chunk text and not only in its own column?

### Answers

**1.** Because the heading split already cut every section smaller than 900, so the length
limit never fires. The longest chunk in the whole corpus is 608 characters. To know in
advance, measure the length of the longest section in your documents. If it is under your
limit, your limit is doing nothing.

**2.** It is treating each document as one section, either because the heading split is off or
because the documents have no headings. Every chunk is then an average of everything in that
document, so the same few chunks come back for almost any question, and a question answered by
one paragraph competes with a whole file.

**3.** Because the embedding is computed from the text and nothing else. A column is for you,
for the report, and for tracing the source. **The model never sees it.** Putting the heading
in the text is how the chunk's own vector knows what the chunk is about.
