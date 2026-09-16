# Lecture Notes: Three Things a Language Model Cannot Do
## 145130 Applications of AI · Module 1 · Week 3, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W03_WhatAModelCannotDo.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W03_WhatAModelCannotDo.pptx)

If you missed class you can learn this from this file alone.

**Exit criterion:** state three things a language model cannot do and why. This
lesson is that criterion, and one of the three is genuinely contested, which is
why it is here rather than on a slide in Week 1.

---

## Why this exists

You can now describe the mechanism. That description has consequences, and the
consequences are the practical part: they tell you where a model is the wrong
tool before you waste two weeks finding out.

The word to avoid is "cannot yet". Two of the three below follow from how these
systems work and are not waiting on a bigger model. The third is an argument, and
you will be asked to take a side in it.

---

## One: it cannot tell you where an answer came from

A model does not look anything up. There is no retrieval step and no source
record, so there is nothing to report. When it produces a citation, the citation
was produced the same way the rest of the sentence was: as likely text.

**Why this follows from the mechanism.** The output is a sequence of tokens
chosen for likelihood. A reference to a real paper and a reference to a paper
that does not exist look identical from the inside. Both are plausible
continuations of a sentence that was heading toward a citation, and nothing in
the process distinguishes them.

**What it means for you.** Every source a model gives you is a lead, not a
citation. Go and find it. When you cannot, write down that you looked, which is
what Week 2 Wednesday was about.

**What fixes it, partly.** Retrieval. Search your own documents, put the
relevant passages into the prompt, and have the program report which document
each passage came from. The provenance then comes from your search, which does
have a record, rather than from the model, which does not. Module 4 builds this.

---

## Two: it cannot be relied on for exact work

Arithmetic, counting, precise lookups, and anything where "close" is wrong.

**Why this follows from the mechanism.** The system produces the most likely next
token. For a multiplication it has never encountered, the most likely tokens are
the ones that look like an answer to that kind of question. Looking like an
answer and being one are different properties, and nothing in the process
prefers the second.

**This is not about model size.** A larger model gets more of them right, which
is a different claim from being reliable. A calculator is reliable. A system that
is usually right about arithmetic, with no way to tell which times, cannot be put
in a path where the number matters.

**What it means for you.** Never let a model do the arithmetic in your program.
Let it work out what was being asked, then do the calculation in code. That is
exactly the shape of the Module 5 application: the model handles the language,
your code handles anything that must be exact.

**Watch for this specific failure.** A model asked to summarise a table will
produce totals. The totals are text. Check them or do not print them.

---

## Three: this is the contested one

> **A language model does not understand what it is saying.**

You will see this stated as settled fact constantly, including in the artifact
you scored in Week 2. It is not settled, and being able to lay out both sides is
worth more to you than picking a winner.

### The strongest case that it does not understand

The mechanism is fully specified and contains nothing that looks like meaning.
Tokens in, probability distribution out, sample, repeat. Nothing in that loop
refers to anything in the world. The system has never seen a 3D printer, waited
for a bus, or been wrong about something and noticed.

It also fails in ways understanding would prevent. It asserts a fact and then
contradicts it two paragraphs later without discomfort, because nothing is
tracking consistency. It invents a citation with the same confidence it uses for
a real one, because it has no access to the difference.

### The strongest case that the question is not settled

"Understand" has never been defined precisely enough to test, and the argument
above assumes that a mechanism made of simple parts cannot produce understanding.
That assumption is doing a great deal of work and nobody has established it.
Brains are also made of simple parts doing simple things.

There is also an evidence problem for the confident negative. These systems do
things that, in any other context, we would take as evidence of understanding:
following instructions about text they have never seen, applying an explanation
to a new case, translating an idea between domains. Saying "that is only pattern
matching" is a claim about what pattern matching cannot achieve, and that claim
has been revised downward repeatedly.

### What is actually settled, and what to write

Settled: the mechanism, that the weights do not change during use, that output
confidence carries no information about correctness, and that it produces
fabricated sources.

Not settled: whether any of that amounts to understanding.

**What to write in your own documents:** describe what it does and what it fails
at, and stay out of the word. "It produces fluent text and fabricates citations
with equal confidence" is checkable. "It does not understand anything" is a
position in an open argument, and stating it as a fact in a document for
beginners is exactly the defect you were asked to find in Week 2.

---

## Worked example: the three failures inside one request

Ask a model to summarise a spreadsheet of print-shop jobs and give the total
hours.

| What it does | Which failure | What to do instead |
|---|---|---|
| gives you a fluent summary of the themes | none, this is the good use | keep it |
| gives a total of 41.5 hours | **two**: exact work | compute the total in code, then hand it the number |
| says "per the shop's standard, jobs over 4 hours need approval" | **one**: invented provenance | find the standard, or do not print the sentence |
| sounds equally confident about all three | the general problem | provenance and validation, in the program |

**One request, two failures, and the output looks uniform.** That uniformity is
the real hazard. There is no change in tone between the part that is fine and the
part that is invented.

---

## The wrong version, and why it is tempting

> "AI cannot be trusted, so we should not use it for anything important."

It is tempting because it sounds cautious and it costs less thought than the
alternative, which is deciding, task by task, where a mistake is recoverable.

It is wrong in the same way "AI is always right" is wrong: it treats
trustworthiness as a property of the technology rather than of a specific use.
The useful question is never whether to trust it. It is: **what happens when this
particular answer is wrong, and who catches it?**

Draft an email with it and a person reads the draft before sending. Recoverable.
Compute somebody's grade with it and nobody checks. Not recoverable.

### Write this down

> It cannot say where an answer came from, and it cannot be relied on to be
> exact. Both follow from the mechanism. Whether it understands anything is an
> open argument, and stating either side as fact is a defect.

---

## Vocabulary

| Term | What it means |
|---|---|
| **provenance** | where a piece of information came from |
| **fabrication, hallucination** | confidently producing something that does not exist |
| **retrieval** | searching your own documents and putting the relevant parts in the prompt |
| **grounding** | tying an answer to source material the program can point at |
| **contested** | a question on which informed people genuinely disagree |
| **recoverable error** | a mistake somebody will catch before it does harm |
| **calibration** | whether stated confidence matches actual accuracy |

---

## Self-check

**1.** A program uses a model to read receipts and total them. Name the failure,
say why a bigger model does not fix it, and describe the design that does.

**2.** Your classmate writes "the model does not understand anything, it is
autocomplete" in a report. Is that a defect? Defend your answer.

**3.** Name one task where a model being wrong is recoverable and one where it is
not, and say what makes the difference.

### Answers

**1.** Exact work. Totalling is arithmetic, and the model produces the tokens
that look like a total rather than computing one. A bigger model gets more of
them right without ever making them reliable, and there is still no signal saying
which ones to check. The design: use the model to pull the individual amounts out
of the text, validate each one against a shape, and add them up in your own code.
The model handles language. Code handles anything that must be exact.

**2.** It is a defect as written, because it states a contested position as
settled fact, and the report is for a reader who cannot tell the difference. It
is not a defect to hold the view: it is well argued and many serious people hold
it. The fix is a sentence: "the mechanism is next-token prediction, and whether
that amounts to understanding is an open question." A reviewer who flags it
should say that is the problem, rather than claiming the sentence is false.

**3.** Recoverable: drafting a first version of a lab write-up that you then edit,
because you read every sentence before it goes anywhere. Not recoverable: filling
in a dosage, a grade, a payment amount, or anything that is acted on without a
person reading it. The difference is whether a human with the ability to catch
the error is standing between the output and the consequence.
