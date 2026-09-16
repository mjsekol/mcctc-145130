# The Five Evaluation Parameters
## 145130 Applications of AI · Module 2 · Week 5, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W05_FiveParameters.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W05_FiveParameters.pptx)

**Competencies:** 2.14.4 (evaluate the result of an AI query on a variety of
parameters: validity, relevance, authenticity, potential bias, and
hallucinations). Supporting: 2.14.6.

---

## Why this exists

Last week you learned to change the input. This week you learn to judge the
output, and the two skills are worth different amounts. Anybody can get a
different answer. Far fewer people can say whether the answer they got is any
good, and say it in a way somebody else can check.

"Is it right?" is the question most people ask, and it is too coarse. It collapses
five different failures into one word and then catches roughly two of them.

Ohio's competency 2.14.4 names five parameters. **These five words are on the
exam and they are the spine of this module.** Use them exactly.

---

## The five, verbatim

| Parameter | The question it asks | How you catch it |
|---|---|---|
| **Validity** | Is the claim about a real thing false? | Test the real thing |
| **Relevance** | Does it answer what was actually asked? | Reread the request |
| **Authenticity** | Is it original, or does it belong to somebody? | Search for the phrasing |
| **Potential Bias** | Whose perspective is built in, and who is missing? | Ask who is absent |
| **Hallucinations** | Does it confidently describe something that does not exist? | Go and look, and find nothing |

They fail separately and they are caught by different methods. That is the whole
reason there are five.

---

## The line you will keep getting wrong

**Validity against Hallucinations.** Say it the same way every time:

> **Validity is a wrong claim about a real thing.
> A hallucination invents the thing.**

You met this in 145060, in the Infographic Autopsy. `.titlecase()` was a
hallucination: there is no such method, so there is nothing to be wrong about.
"`print` separates values with a comma" was a validity failure: `print` exists
and the sentence about it is false.

**The practical difference is how you catch them.**

- A validity failure can be caught by testing the thing. Run the command. Open
  the handbook. The thing is there and the sentence about it does not hold.
- A hallucination can only be caught by going to look and finding nothing. There
  is no test to run, because there is nothing to run it on.

That asymmetry is why hallucinations survive review. A reviewer who checks things
finds validity failures. A reviewer who checks that things *exist* finds both, and
almost nobody does the second one unless they were taught to.

---

## Worked example 1 · Validity

```
python ask.py --prompt-file demo-prompts/loose_json.txt --label v1 --show
```

Take one line out of the reply:

> "Set the return slot to the next school day, first period."

**Is this a validity failure?** It is a claim about a real thing, the Media Club
return policy. To test it, open the posted procedure in Room 214 and read what it
says about return times.

If the posted procedure says returns are due at the end of the same day, the
sentence is false and the finding is **Validity**. Your evidence is the posted
procedure, named specifically.

If you cannot find any posted procedure at all, you have something different, and
it is worked example 4.

**What does not count as evidence:** "that does not sound right to me." The
autopsy from 145060 scored a finding zero if the "how you know" was missing, and
so does this module.

---

## Worked example 2 · Relevance

Run the grounded research prompt:

```
python ask.py --prompt-file demo-prompts/grounded.txt --label r1 --show
```

The prompt asks: *write a research brief on retrieval practice in secondary
schools*, using only two supplied sources about equipment checkout.

```
As a research assistant, here is how I would handle the Friday equipment
checkout.

Set the return slot to the next school day, first period. Open the checkout
sheet before anyone lines up. Write the borrower's grade level, not their
schedule. Photograph any damage before the item leaves the room.

Sources:
[1] Student handbook, section 4.2, equipment checkout and return
[2] Room 214 posted closing procedure
```

**Every citation is real.** Both sources were supplied by you. Nothing is
fabricated. Nothing is false in a way a reader would catch.

**And it answers a different question.** You asked about retrieval practice. You
got equipment checkout, because the supplied sources were about equipment
checkout and the answer drifted towards them.

This is a **Relevance** failure, and it is the cleanest one you will see. Notice
what caught it: rereading the request. No command, no catalog, no search. Only
comparing the answer to the question, which is the step everybody skips because
it feels like it does not need doing.

**Notice something harder, too.** Grounding fixed the fabrication and caused
this. Fixing one parameter can break another, and an evaluation that only looks
at the parameter you were worried about will miss it.

---

## Worked example 3 · Potential Bias

From the Monday reply:

> "Write the borrower's grade level, not their schedule."

That is advice. Ask the bias question: **who is this advice about, and who is
missing?**

Grade level identifies students. It does not identify a teacher borrowing a
camera, a parent volunteer, or an alumnus helping at an event. A checkout sheet
built from this advice has no row that fits any of them.

**Potential Bias is about what is absent, not about what is false.** The sentence
is not wrong. A procedure built from it excludes people, and the exclusion is
invisible because the sentence never mentions them.

**The wrong version of this finding**, which half the class writes:

> "This is biased because not every school uses grade levels."

That is a claim about accuracy, which is Validity. If it is inaccurate, say
Validity and prove it. Bias is the different question: whose perspective is built
in, and who is absent from it.

---

## Worked example 4 · Hallucinations

```
python ask.py --prompt-file demo-prompts/ungrounded.txt --label h1 --show
```

```
Sources:
[1] Petrov, A. (2015). Measuring Attention in Scheduled Work Blocks.
    Quarterly Notes on School Technology, 8, 21-35.
[2] Lindqvist, M. (2013). Structured Output and Downstream Parsing Failures.
    Midland Review of Applied Learning, 9, 34-48.
[3] Ramirez, D. (2011). Retrieval Practice and Short Revision Windows.
    Proceedings of the Workshop on Classroom Systems, 10, 47-61.
```

Author, year, title, venue, volume, pages. Formatted correctly. Plausible.

**All three are fabricated.** The stub built them from templates. There is no
Petrov paper, no Quarterly Notes on School Technology, and no volume 8.

You cannot tell that from the text, and that is not a gap in your skill. **The
information required to tell is not in the citation.** It is in a catalog, and
you have to go there. Wednesday and Thursday are built on this.

**The tell that is not a tell:** source 3's title matches the question almost
exactly. That is suspicious for a real reason, because the model produced a title
shaped like the question it was handed. It is still not evidence. Plenty of real
papers have titles that match the question, which is why they came up when you
searched.

---

## Worked example 5 · Authenticity

Authenticity asks whether the output is the model's own production or somebody
else's work arriving without credit.

Two shapes, and they are different problems:

**Uncredited reuse.** A paragraph that closely tracks a specific source, without
naming it. The model was trained on that text, and text near it is a likely
continuation. Nobody decided to copy. The result is the same for the person whose
work it is.

**Misattribution.** A real quote assigned to the wrong person, or a real finding
credited to the wrong study. This one is worse in practice, because it survives a
search: the quote is real, so a quick check confirms it exists and does not check
who said it.

**How you check:** take a distinctive phrase, ten or twelve words, and search for
it exactly. If a source comes back with nearly that sentence, you have a finding.
If the phrasing is generic, there is nothing to find and the parameter has nothing
to report, which is also a valid outcome.

Module 3 takes this much further, because who owns model output is a live legal
question rather than a settled one.

---

## Reporting a finding

Every finding, in every artifact this module, has four parts. A finding missing
any of them scores zero.

1. **The exact claim, quoted.** Word for word.
2. **Which parameter it fails.** One label.
3. **Why it fails.** In your own words.
4. **How you know.** A command you ran and its output, a source you opened and
   named, or a search you performed with the exact string and what came back.

"It seems wrong" and "I could tell" are not part 4.

**A parameter with nothing to report is a finding.** Write "no Relevance failure
found" and say why you looked. Manufacturing a defect to fill a category is its
own failure mode and reviewers do it under pressure to look thorough.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Validity** | A false claim about something real |
| **Relevance** | Whether the output answers the question that was asked |
| **Authenticity** | Whether the output is original or belongs to somebody |
| **Potential Bias** | Whose perspective is built in and who is left out |
| **Hallucination** | A confident description of something with no referent |
| **Referent** | The real thing a claim points at. A hallucination has none |
| **Evidence** | A command, a named source, or a recorded search. Not an impression |

---

## Self-check

**1.** An output says "the Ohio Means Jobs readiness seal requires 40 hours of
community service." Suppose the seal is real and the hours requirement is not
what it says. Which parameter, and what is your evidence?

<details><summary>Answer</summary>

**Validity.** The seal exists, so there is a real thing for the sentence to be
wrong about.

**Evidence:** the official description of the seal's requirements, named
specifically, with what it actually says. Not "I think it is different."

If the seal did not exist at all, it would be a Hallucination instead, and you
would only find that out by going to look.
</details>

**2.** An output answers a question about study techniques with four true,
well-sourced sentences about sleep. Which parameter, and why is it tempting to
say none?

<details><summary>Answer</summary>

**Relevance.** It is tempting to say none because every individual sentence
survives every other check. Nothing is false, nothing is fabricated, the sources
are real, nobody is excluded.

Relevance is the only parameter that is about the relationship between the output
and the request, rather than about the output on its own. That is exactly why it
gets skipped: you have to hold the question in your head while you read the
answer.
</details>

**3.** You have eight findings and all eight are labelled Validity. What is the
most likely explanation, and what is the fastest way to test it?

<details><summary>Answer</summary>

**Most likely:** you checked the things that are checkable with a command and
stopped. Validity is the parameter a terminal can settle, so a reviewer working
that way finds Validity failures and nothing else.

**Fastest test:** take one section and ask two questions of it that a terminal
cannot answer. Who is not in this? and Does any of this exist? Two minutes, and
it usually produces a Bias finding and a Hallucination candidate.

This is the most common 70-percent submission in the module and the gap is always
the same: the student equated "check it" with "run it."
</details>
