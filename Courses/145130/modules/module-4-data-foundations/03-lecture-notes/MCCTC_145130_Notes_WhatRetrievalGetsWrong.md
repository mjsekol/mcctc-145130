# What Retrieval Still Gets Wrong
## 145130 Applications of AI · Module 4 · Week 12, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W12_WhatRetrievalGetsWrong.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W12_WhatRetrievalGetsWrong.pptx)

**Every result below is a real run against the stub on port 11634, captured on the build
machine.**

---

## Why this is the last concept of the module

Yesterday you learned to argue for retrieval. Today you learn to be trusted when you do.

**An argument with no fourth section is a sales pitch.** Anybody can say retrieval is cheap,
fresh, and traceable. The person worth listening to is the one who can say what it still gets
wrong, specifically, with an example on screen.

---

## Failure 1: it retrieves what is near, not what is true

The ranking is a similarity score. **Nothing in it knows whether a chunk is correct**,
whether it is current, or whether it is the exception rather than the rule.

Real run:

```
Question: "what do I do if the resin printer fan is not running"
1. score +0.3768   01-access-and-safety.md . Training holds
2. score +0.2799   05-media-kits.md . Batteries
3. score +0.2716   07-electronics-bench.md . The power supply
```

**The resin printer document is not in the list at all**, and `04-resin-printer-sop.md` says
plainly: if the cabinet fan is not running, the printer does not run. The system returned
three true paragraphs and answered nothing.

On this stub that is guaranteed, because the stub builds its vector from a hash. On a real
model it happens less and it still happens, and **when it happens the output looks exactly
the same as when it works.**

---

## Failure 2: it inherits every contradiction in the sources

This is the one to put in your memo.

Two documents in your handbook disagree:

| File | Heading | Sentence |
|---|---|---|
| `02-loan-policy.md` | How many at once | "A member may hold two items at one time." |
| `07-electronics-bench.md` | How many at once | "You may sign out up to three items from the electronics bench at one time." |

Ask the system:

```
Question: "how many items can a member have out at one time"
1. score +0.4422   02-loan-policy.md . What may be borrowed
2. score +0.3309   05-media-kits.md . Batteries
3. score +0.3289   02-loan-policy.md . Returns
4. score +0.3123   07-electronics-bench.md . How many at once
   You may sign out up to three items from the electronics bench at one time, because a
   power supply, a scope, and a parts bin are one working setup rather than three separate
   projects.
```

**The three-item rule came back. The two-item rule did not**, even though two other chunks of
that same document did.

A member reading that walks away believing the limit is three. The answer they got is a real
sentence, correctly quoted, from a real document, with a citation, **and it is the exception
rather than the rule.**

**The citation makes it worse.** An answer with a source attached reads as checked. Nobody
looks for the other half.

**The fix is not in your code.** Somebody has to reconcile the two documents. Widening `k` or
using a score threshold makes it more likely both sides appear, which is a mitigation and not
a fix: it widens the window and hopes.

---

## Failure 3: questions no chunk answers

Retrieval finds passages. If the answer is not in a passage, there is no passage to find.

- "How has equipment use changed over three years?" That is an aggregate across a database,
  not a sentence in a document.
- "Which policies contradict each other?" That requires reading all of them at once, which is
  the opposite of chunking.
- "What is not in the handbook?" Nothing can retrieve an absence.

**Know which of your questions is a retrieval question and which is a SQL question.** Your
project has both, in one repository, on purpose.

---

## Failure 4: the chunking decides what is answerable

From Monday, and this is real:

```
--- chunk 2  heading: 'Check the contents card'  characters 435-701
...
Loan length
Media kits are a three day loan.
```

The answer to "how long can I keep a camera kit" is filed under a heading about contents
cards, because the `Loan length` section is 32 characters and was attached to the chunk before
it.

**The retrieval is not failing. The chunking already decided.** And the ranking gives you no
hint that this happened: the hits look like ordinary hits.

---

## Failure 5: retrieval moves the security problem, it does not remove it

A fine tuned model has your data inside it. A retrieval system reads your data at question
time.

**So whoever can ask a question can reach whatever the retriever can reach.** If you index the
holds report along with the handbook, your assistant will now answer "who has not returned
the oscilloscope", to anybody who asks it, with a citation.

Yesterday's traceability is a real advantage. **This is its other face:** the system will
faithfully quote a document to somebody who should not be reading that document.

The control is the same control as everywhere else. Decide what goes in the index. Say it out
loud. It is not a model problem and there is no prompt that fixes it.

---

## The one paragraph you owe every demonstration

When you show a retrieval system to somebody, you owe them this:

> This is running against the course's stub, which builds its vector from a hash of the text.
> The same text always gives the same vector, and text that means the same thing gives a
> completely unrelated one. **So the plumbing is proven and the ranking carries no
> information.** Chunks were cut, embedded, stored, retrieved, ranked, and traced back to a
> line in a file. Whether the right chunk came back is not tested here and cannot be, until a
> real model answers the embeddings endpoint.

**"The results were not very good" does not say this.** The claim is not that the results were
poor. It is that the results carry no information about quality, in either direction. One of
the three questions above landed on the right document, and that was luck.

---

## The wrong version, and what it produces

The wrong version is a demonstration, not a program.

You ask the system the one question you tried while you were building it. It returns the right
chunk. You show that question to the room and move on.

**That is the shape of every bad AI demonstration**, and this course exists partly because of
how often it works. It is not dishonest by intent. It is what happens when the person
demonstrating never asked a question they had not already asked.

**The fix is two minutes long.** Before you demonstrate, ask three questions you have not
tried, and write down what came back. If one of them fails, show that one. A demonstration
with one honest failure in it is worth more than three successes, because the room now knows
what you would have told them if it had gone badly.

---

## Vocabulary

| Term | What it means |
|---|---|
| **relevance** | whether a retrieved chunk answers the question |
| **recall** | how much of the relevant material you managed to retrieve |
| **precision** | how much of what you retrieved was relevant |
| **grounded answer** | an answer built only from retrieved source text |
| **hallucination** | content presented as fact that has no source |
| **corpus hygiene** | keeping the source documents consistent and current |

**Notice that four of those six are about your documents, not about your code.** That is the
lesson of the week.

---

## Self-check

**1.** Your system returns a real sentence, correctly quoted, from a real document, with a
citation, and the answer is misleading. How is that possible, and whose job is the fix?

**2.** Somebody demonstrates a retrieval system and every answer is right. What do you ask
them?

**3.** Name a question about the makerspace that retrieval cannot answer and SQL can, and one
that SQL cannot answer and retrieval can.

### Answers

**1.** Because the document it quoted is the exception and the rule is in a different document
that did not come back. Retrieval finds what is near, and two documents that disagree are both
near. **The fix belongs to whoever owns the documents.** You can widen `k` or add a threshold
so both are more likely to appear, and that is a mitigation. The contradiction is still there
and will find somebody else.

**2.** How many of those questions they had asked before today, and what happened on a
question they had not. Then ask one of your own. A demonstration made of questions the
demonstrator already tested is a recording, not a test.

**3.** **SQL, not retrieval:** how many loans per category last month, which items nobody has
borrowed, who has something overdue. Those are aggregates over rows and appear in no
paragraph. **Retrieval, not SQL:** what should I do if the first layer will not stick, which
is three sentences of procedure sitting in a document with no structure a query could target.
