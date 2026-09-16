# Retrieval Versus Fine Tuning
## 145130 Applications of AI · Module 4 · Week 12, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W12_RetrievalVsFineTuning.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W12_RetrievalVsFineTuning.pptx)

**This is an exit criterion for the module:** explain why retrieval beats fine tuning for most
practical problems. You will be asked to defend it in the exit assessment and in your memo.

---

## The two ways to make a model know your stuff

You have a model that has never seen the Ridge Creek handbook. There are two routes.

**Fine tuning** changes the model. You take an existing model and continue training it on your
material, so the knowledge ends up in the weights.

**Retrieval** does not change the model at all. You find the relevant pieces of your material
at question time and put them in the prompt.

A third thing exists and people confuse it with fine tuning: **prompting**, where you paste
context in by hand. Retrieval is prompting with the pasting automated and the pieces chosen by
similarity. **Fine tuning is the only one of the three that changes the model.** Getting that
distinction right is worth marks on its own.

---

## The four reasons, and what each one is really about

### 1. Cost

Retrieval over 56 chunks is a file and a loop. It took **0.64 seconds** to build the whole
index on the build machine, against a stub, and it would take minutes against a real model
because embedding is the slow part.

Fine tuning is hardware time, a prepared training set, somebody who knows what a learning rate
is, and an evaluation to find out whether it worked. And it is not once: it is again every
time the material changes.

**The honest version of this argument** is not "fine tuning is expensive". It is that the
costs are shaped differently. Retrieval costs a little on every query, forever. Fine tuning
costs a lot up front and little per query. At a very high query volume with material that
never changes, that trade can go the other way.

### 2. Freshness

Change the loan policy. Rebuild the index. Retrieval is correct immediately.

A fine tuned model **still believes the old policy, confidently**, and will keep saying it
until somebody retrains. There is no way to look at a model and tell which version of a fact
is in it.

**This is the argument that decides most real cases**, and it is the one people skip because
it sounds boring. Handbooks change. Policies change. Prices change. A system that is wrong
until the next training run is a system that is wrong.

### 3. Traceability to a source

This is the one to lead with in a memo, and here it is on screen:

```
Question: "how many items can a member have out at one time"
Retrieved 4 chunks. Nothing below was generated. Every line is from a handbook file.

4. score +0.3123   07-electronics-bench.md . How many at once   characters 483-668
   You may sign out up to three items from the electronics bench at one time, because a
   power supply, a scope, and a parts bin are one working setup rather than three separate
   projects.
```

**A file name, a heading, and a character range.** Somebody who knows the handbook can check
that in ten seconds.

A fine tuned model hands you a sentence with no source. The only way to check it is to go and
read the handbook, which is the thing the system was supposed to save you from. **A system you
have to verify by hand has not saved anybody any work.**

And there is a second thing traceability buys, which matters more in this school than in most
places: **when the answer is wrong, you can tell whether the retrieval went wrong or the
source was wrong.** Those have different fixes. With fine tuning they are the same
indistinguishable failure.

### 4. What retrieval still gets wrong

An argument with no fourth section is a sales pitch. Tomorrow is a whole lesson on this, and
here is the short version so you can write the memo today.

- **It retrieves what is near, not what is true.** The ranking has no idea whether a chunk is
  correct.
- **It inherits every contradiction in the source set.** Your handbook says two items in one
  document and three in another. A retrieval system that returns one of those gives a
  confident, sourced, half wrong answer, and **the citation makes it harder to doubt.**
- **It cannot answer a question whose answer is spread across many documents.** "How has our
  equipment use changed over three years" is not in any chunk.
- **It is only as good as the chunking**, which you decided on Monday with a parameter you may
  not have measured.
- **It moves the security problem rather than removing it.** A model that was fine tuned on
  your data has your data in it. A retrieval system reads your data at question time, so
  whoever can ask a question can reach whatever the retriever can reach. **If the holds list
  is in the index, the index answers questions about who has not returned things.**

---

## Where fine tuning actually wins

Be able to say this, because a memo that says retrieval is always better is not an analysis.

**Fine tuning wins when you are teaching behaviour rather than facts.** Always answer in this
format. Use this vocabulary. Refuse this kind of request. Sound like our support team. None of
that is a fact you can retrieve, because it is not written down anywhere as a passage.

It also wins when the material is enormous, stable, and queried constantly, so the up-front
cost is paid off, and when there is no room in the context window for retrieved passages.

**The usual real answer is both:** a model fine tuned for the shape of the answer, with the
facts retrieved at question time.

---

## The comparison, in one table

| | Retrieval | Fine tuning |
|---|---|---|
| Changes the model | no | yes |
| Cost shape | small, per query, forever | large, up front, repeated on change |
| Material changes | rebuild the index | retrain |
| Can cite a source | yes, exactly | no |
| Wrong answer is diagnosable | yes, retrieval or source | no |
| Teaches format and tone | poorly | well |
| Holds your data where | in your store, read at query time | inside the model weights |
| Needs a machine learning specialist | no | usually |

---

## The wrong version, and what it produces

The wrong version is a sentence in a plan:

> "We will fine tune a model on the handbook so it knows our policies."

Three problems.

1. **Eight documents is not a training set.** Fine tuning on a handful of documents does not
   reliably put facts into a model, and what it does put in cannot be inspected. The most
   likely outcome is a model that sounds like the handbook and makes up its contents.
2. **The first policy change makes it wrong**, silently, with no version number to check.
3. **You have thrown away the citation**, which is the thing the advisor actually asked for.
   Go back and read the brief: "I would like to be able to point at the paragraph."

**Why it is tempting.** It sounds more serious. "We fine tuned a model" is a sentence that
sounds like more work than "we chunked the handbook", and it is. **More work is not the same
as a better answer**, and being able to say that clearly is most of what this lesson is for.

---

## Vocabulary

| Term | What it means |
|---|---|
| **fine tuning** | continuing to train a model on your material, changing its weights |
| **retrieval augmented generation** | finding relevant passages and putting them in the prompt |
| **grounding** | giving a model the source text it should answer from |
| **freshness** | how quickly a change in your material reaches the answers |
| **traceability** | being able to point at where an answer came from |
| **context window** | how much text the model can be given at once |

---

## Self-check

**1.** Your handbook changes on a Tuesday. Describe exactly what happens next under each of
the two approaches.

**2.** A plan says fine tuning is better because it is faster at question time. Is that true,
and does it settle anything?

**3.** Name one thing retrieval cannot do that fine tuning can, and one security problem
retrieval does not solve.

### Answers

**1.** **Retrieval:** somebody runs the indexer. The chunks are recut, re-embedded, and the
next question gets the new policy. Minutes, and anybody can do it. **Fine tuning:** nothing
happens. The model gives the old answer, confidently, with no indication that it is out of
date, until somebody prepares a training set and retrains, which needs a person with a
particular skill and a machine to do it on.

**2.** It is true and it settles nothing on its own. A fine tuned model answers without a
retrieval step, so there is less work per question. Then ask the other three questions: what
does it cost to build, what happens when the handbook changes, and can it cite the paragraph.
**A single-axis comparison is the shape of a bad recommendation.**

**3.** Retrieval cannot teach a model **how to answer**: format, tone, refusals, vocabulary.
Those are behaviour and are not written down as retrievable passages. **The security problem:**
retrieval reads your data at question time, so anything the retriever can reach is reachable
by anybody who can ask a question. Putting the holds list in the index means the index will
answer questions about who has not returned equipment.
