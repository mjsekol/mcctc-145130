# Why Models Fabricate, and What Reduces It
## 145130 Applications of AI · Module 2 · Week 5, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W05_WhyModelsFabricate.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W05_WhyModelsFabricate.pptx)

**Competencies:** 2.14.4 (evaluate an AI result on hallucinations), 2.14.6
(critically analyze scenarios involving AI usage), 1.2.1 (extract valid
information and cite sources).

---

## Why this exists

Yesterday you learned to check a citation. Today you learn why there is anything
to check, and the answer changes what you do about it.

If fabrication were a defect, the response would be to wait for a better model.
It is not a defect. **It is the ordinary operation of the system, applied to a
kind of text where the shape and the truth come apart.** That means the response
is procedural: build checking into the workflow, because the workflow is the only
place a check can live.

This is the hardest lesson in the module to accept, because it asks you to stop
looking for the version that does not do this.

---

## The concept in plain language

A model predicts text. A citation has a shape:

```
Author, Initial. (Year). Title Case Title. Venue Name, volume, pages.
```

Producing something in that shape is the same operation as producing any other
text. There is no separate citation subsystem, no lookup, no database of papers,
and nothing anywhere in the process that could check whether the thing described
exists. **There is no step that could fail, because there is no step.**

Three consequences you can use.

**1. The best-fitting citation is the one to suspect first.** If your question is
about retrieval practice and short revision windows, a title like "Retrieval
Practice and Short Revision Windows" is exactly what the model is most likely to
produce. It reads as a perfect match and it is a perfect match to your prompt,
not to the literature.

**2. Fabrication is worst where the real thing is rare.** The model produces the
typical continuation. Where there is lots of real material, the typical
continuation is often real. Where there is little, the shape survives and the
content is invented. Specific, narrow, local, and recent questions are the
dangerous ones. Your school, this year, this exact policy.

**3. Confidence tells you nothing.** Hedging and certainty are both styles. A
model can produce "studies consistently show" and "I am not certain, but" with
equal ease, and neither tracks whether the claim is true.

---

## What reduces it, honestly

Four things help, and each one helps less than people say.

**Grounding: put the real material in the prompt.** This is the big one. Supply
the sources and restrict the answer to them, and the nearby text now contains
real material, so the continuation is more likely to be drawn from it. Retrieval
systems in production are this idea at scale.

**Give it a route to refuse.** "If the answer is not in the sources, say I do not
know." Without this, a grounded model with thin sources still has to produce
something, and what it produces comes from training.

**Ask for less.** "Cite three sources" is a request for three citation-shaped
strings. If you only need one and you only want a real one, ask for one, or ask
for none and find them yourself.

**Ask it to quote rather than summarise.** A quote from a supplied source can be
checked against the source with a search. A summary cannot, which is why
misattribution hides in summaries.

**None of these makes the model honest.** It has no mechanism for honesty. They
change what is nearby, which changes what is likely. That is a probability
shift, and a probability shift is not a guarantee. **You still check.**

---

## Worked example 1 · Ungrounded

```
python ask.py --prompt-file demo-prompts/ungrounded.txt --label ungrounded --show
```

The prompt is one line: *Write a research brief on retrieval practice in
secondary schools. Cite three sources.*

```
Sources:
[1] Petrov, A. (2015). Measuring Attention in Scheduled Work Blocks.
    Quarterly Notes on School Technology, 8, 21-35.
[2] Lindqvist, M. (2013). Structured Output and Downstream Parsing Failures.
    Midland Review of Applied Learning, 9, 34-48.
[3] Ramirez, D. (2011). Retrieval Practice and Short Revision Windows.
    Proceedings of the Workshop on Classroom Systems, 10, 47-61.
```

You asked for three. You got exactly three, correctly formatted, with plausible
years and page ranges that look like page ranges.

**Every one is fabricated.** The stub built them from a template, which is what
makes it safe to study them. A real local model does the same thing for the same
reason, and its versions are usually more convincing.

Source 3 is the one the room believes, every time. Its title is your question
with the words rearranged.

---

## Worked example 2 · Grounded, with a refusal route

```
python ask.py --prompt-file demo-prompts/grounded.txt --label grounded --show
```

The prompt now carries three additions:

```
Answer using only the sources below. If the answer is not in the sources, say
I do not know. Cite your sources.

SOURCE: Student handbook, section 4.2, equipment checkout and return
SOURCE: Room 214 posted closing procedure
```

```
Sources:
[1] Student handbook, section 4.2, equipment checkout and return
[2] Room 214 posted closing procedure
```

**Zero fabricated sources.** The sources block contains exactly what you supplied
and nothing else.

That is the most important behavioural demonstration in the module, and here is
the sentence that goes with it: **the constraint did not make the model honest, it
changed what was nearby.**

---

## Worked example 3 · The grounded run also failed

Read the body of that grounded reply:

```
As a research assistant, here is how I would handle the Friday equipment
checkout.

Set the return slot to the next school day, first period. Open the checkout
sheet before anyone lines up. Write the borrower's grade level, not their
schedule. Photograph any damage before the item leaves the room.
```

The question asked for a brief on retrieval practice. The answer is about
equipment checkout, because the sources you supplied were about equipment
checkout and grounding pulled the answer towards them.

**Every citation is real and the answer is wrong.** That is a **Relevance**
failure sitting inside a run you would have called a success.

Two things to take from it:

1. Fixing one parameter can break another. An evaluation that checks only the
   parameter you were worried about will miss it.
2. Grounding on the wrong sources is worse than not grounding, because the output
   now carries real citations that make it look checked.

---

## The wrong version, and why it is tempting

**Grounding on sources that do not cover the question.** Run the version where
the sources are missing entirely and the refusal route is present:

```
python ask.py --prompt-file demo-prompts/thin_sources_refusal.txt --label thin --show
```

```
As a research assistant, here is how I would handle a short research brief.

The question has been studied in more than one field. Findings disagree once you
look at how each study measured the outcome. Sample sizes in the smaller studies
are too small to settle anything. The most cited work in this area is older than
most of its readers.

Sources: none of the supplied sources address this. I do not know.
```

Read that carefully, because it is the most instructive failure in the module.

**The refusal landed on the citations and not on the body.** The sources block
says "I do not know." Four sentences above it make confident claims about a
literature, with nothing behind them. A reader who skims takes the four
sentences and never reaches the last line.

**A partial refusal is more dangerous than no refusal**, because the honesty is
in the place nobody reads and the invention is in the place everybody does.

**Why the tempting version is tempting.** The grounding instruction feels like the
whole fix, and
"say I do not know" feels like politeness rather than mechanism. It is mechanism,
and as the run above shows, it is not enough mechanism on its own.

The version that is worse still is grounding on real sources that do not cover
the question:

```
python ask.py --prompt-file demo-prompts/grounded_no_refusal.txt --label noroute --show
```

Real sources, no refusal route, and an answer about equipment checkout attached
to two genuine citations. **That is the worst combination available:** invented
relevance wearing real provenance.

**The second tempting version:** asking the model to double-check its own
citations. Covered yesterday, and the answer is the same. Asking the same process
to produce a second piece of text is not a check. A check touches the world.

---

## What this means for how you work

You are not going to stop using these tools, and this lesson is not an argument
that you should. It is an argument about where the checking goes.

| Use it for | Do not use it for |
|---|---|
| Drafting, shapes, structure | Facts you have not checked |
| Options you had not considered | Anything with a number in it, unchecked |
| Rewriting something you wrote | Finding sources to support a claim |
| Summarising text you supplied | Summarising text you did not supply |
| Naming what you might have missed | Deciding whether something is true |

**The rule that follows from all of it:** anything you would be embarrassed to be
wrong about gets checked against something outside the model, and the check gets
written down.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Hallucination** | A confident description of something with no referent |
| **Grounding** | Supplying real source material in the prompt and restricting the answer to it |
| **Refusal route** | An explicit instruction permitting "I do not know" |
| **Retrieval** | Fetching relevant real documents and putting them in the prompt automatically |
| **Plausibility** | How much something looks right. Not evidence |
| **Correlated errors** | Two models making the same mistake, which is why a second opinion is not a check |

---

## Self-check

**1.** Why is a fabricated citation more likely when you ask about your own
school's policy than when you ask about the water cycle?

<details><summary>Answer</summary>

The model produces the typical continuation from what it was trained on. There is
an enormous amount of real text about the water cycle, so the typical
continuation is usually real. There is little or none about your school's
specific policy, so the shape of an answer survives and the content is produced
from what such policies usually say.

**The general rule:** the narrower, more local, and more recent the question, the
less real material there is for the answer to be drawn from, and the more of the
answer is shape.
</details>

**2.** A classmate grounds their prompt with three supplied sources and gets an
answer citing only those three. They conclude the output is now trustworthy. What
is right and what is wrong about that?

<details><summary>Answer</summary>

**Right:** the fabrication risk is genuinely reduced. The sources are real because
they supplied them, and the answer is more likely to be drawn from them.

**Wrong:** "trustworthy" covers four other parameters. The answer can still
misattribute a claim to the wrong supplied source, summarise one inaccurately,
answer a different question than was asked, or leave out a group the sources also
leave out. Worked example 3 is exactly this: every citation real, answer wrong.

Grounding addresses hallucinations. It does not address the other four.
</details>

**3.** You are building a program that answers questions about the student
handbook. Describe, in three steps, how you would reduce fabrication, and name
the one thing that is still required afterwards.

<details><summary>Answer</summary>

1. **Put the relevant handbook text in the prompt**, rather than asking the model
   what the handbook says. Find the right section first, by search or by section
   number.
2. **Restrict the answer to the supplied text and give it a refusal route:** "use
   only the text below; if it is not there, say the handbook does not cover this."
3. **Ask for a quote plus a section number**, not a summary, so a reader can check
   the answer against the handbook in one step.

**Still required afterwards:** a human check, and a way for a user to see the
quoted section. Steps 1 to 3 shift probabilities. None of them verifies anything,
and a system that presents an unverified answer as authoritative has moved the
problem rather than solved it.
</details>
