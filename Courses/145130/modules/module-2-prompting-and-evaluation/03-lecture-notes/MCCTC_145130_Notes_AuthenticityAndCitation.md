# Authenticity, and What a Citation Is For
## 145130 Applications of AI · Module 2 · Week 5, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W05_AuthenticityAndCitation.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W05_AuthenticityAndCitation.pptx)

**Competencies:** 1.2.1 (extract relevant, valid information from materials and
cite sources of information), 2.14.4 (evaluate an AI result on authenticity).

---

## Why this exists

You have been told to cite sources since middle school, usually as a rule about
formatting and honesty. That framing is true and it is not the reason the rule
exists.

**A citation is a set of instructions for checking a claim without trusting the
person who made it.** That is its job. A citation that does not let a reader go
and look has failed at its job, no matter how correctly it is formatted.

This matters more than it used to. When claims are cheap to generate and
citations are cheap to generate, the only thing that separates a checked claim
from an unchecked one is whether somebody went and looked.

---

## The concept in plain language

**Authenticity asks: is this the model's own production, or is it somebody's work
arriving without credit?**

Two shapes, and they are different problems.

**Uncredited reuse.** A passage that tracks a specific source closely, with no
attribution. Nobody decided to copy anything. The model was trained on that text,
and text near it is a likely continuation. The effect on the person whose work it
is does not care about the mechanism.

**Misattribution.** A real quote assigned to the wrong person, or a real finding
credited to the wrong study. **This one is more dangerous, because it survives a
careless check.** The quote is real, so searching it confirms it exists, and if
you stop there you have confirmed the wrong thing.

Module 3 takes the legal side of this much further. Who owns the output of a
generative model is a live, unsettled question, and this course does not pretend
otherwise.

---

## What makes a citation checkable

Four parts. Each one narrows the search.

| Part | What it lets a reader do |
|---|---|
| **Who** | Find the person or organisation responsible |
| **What** | Find the specific work, not the whole publication |
| **Where** | Go to the exact place: page, section, timestamp, table number |
| **When** | Know which version you are looking at |

"Studies have shown" has none of them. "A recent survey found" has one and a
half. Neither is a citation, because neither lets you go and look. **A claim with
an uncheckable source is not weakly supported. It is unsupported**, and it should
be treated the same as a claim with no source at all.

---

## Worked example 1 · Extracting a claim and citing it properly

Here is the raw material, a paragraph from an invented school memo. It is
invented for this lesson and labelled so:

> **Media Club equipment memo, section 3 (constructed for this lesson).**
> "Cameras returned after 3:15 are logged as late. A late return does not carry a
> penalty on the first occasion. On a second late return in the same quarter, the
> member loses checkout privileges for two weeks. The advisor may waive this for a
> documented conflict."

**The claim you want to extract:** what happens if a camera comes back late.

**Badly extracted:** "You get banned for two weeks if you are late."

That is wrong in three ways. It drops the first-occasion exception, it drops the
"same quarter" scope, and it drops the waiver. Every one of those changes what
somebody would do.

**Well extracted, with the citation:**

> A camera returned after 3:15 is logged late. The first late return in a quarter
> carries no penalty; a second costs two weeks of checkout privileges, and the
> advisor may waive it for a documented conflict.
> (Media Club equipment memo, section 3)

Notice what the citation gives a reader: the document, and the section. They can
go and check whether you dropped anything. That is the point.

---

## Worked example 2 · Checking a citation, in the order that works

Take one fabricated citation from Monday's run:

> Ramirez, D. (2011). Retrieval Practice and Short Revision Windows.
> Proceedings of the Workshop on Classroom Systems, 10, 47-61.

**Check in this order, and record each step.**

1. **Does the venue exist?** Search for the publication name in quotation marks.
   A publication is quicker to find than an article, so if the venue does not
   exist, you are done in thirty seconds.
2. **Does the work exist?** Search the title in quotation marks. Use the library
   catalog and a general search. Try the title without the subtitle.
3. **Does the author exist, and did they write it?** An author with no trace
   anywhere is a strong signal. An author who exists but has no connection to
   this title is a misattribution candidate.
4. **Do the details match?** Year, volume, page range. This is where a real work
   with wrong numbers shows up, which is a Validity failure rather than a
   hallucination.

**Record, for each citation:** the catalog or search you used, the exact string
you searched, and what came back, including "no results."

**A negative result is a result only if you recorded the search.** "I could not
find it" with no search string is not a finding. "I searched the school library
catalog for the exact title in quotation marks and got zero results, then
searched without the subtitle and got zero results" is.

---

## Worked example 3 · When the check comes back complicated

Sometimes step 1 finds something close. A venue exists with a similar name, or
the author is real and writes about something else.

**That is the most valuable outcome in this lab, and most students treat it as a
failure.** It is not. Write down exactly what you found and exactly what you did
not:

> The venue "Proceedings of the Workshop on Classroom Systems" returned no
> results. A similarly named workshop does exist, and searching its proceedings
> index for the title returned nothing. Volume 10 of that index covers a
> different year than 2011.

That paragraph is worth more than "fake." It shows the reader precisely what was
checked, and it is honest about the part that is still ambiguous.

**Do not resolve ambiguity by rounding to a verdict.** The whole reason this is
hard is that partial matches are common and they are exactly where a careless
checker stops.

---

## The wrong version, and why it is tempting

Here is the check students run first:

```
Ask the model: "Is this citation real?"
```

The model says yes, or it says it cannot verify, or it apologises and produces a
different citation. None of those is a check.

**Why it is not a check.** Asking a model whether its output is true is asking
the same process to produce a second piece of text. The second text is not
evidence about the first, because nothing in either run consulted anything. If
the model produced a fabricated citation because a citation-shaped continuation
was likely, then "yes, that is a real paper" is also a likely continuation.

**Why it is tempting.** It is fast, it is in the tool you already have open, and
the answer is confident. All three of those are properties of the failure, not of
a check.

**The related version, which is subtler:** asking a *different* model. Better,
because the errors are less correlated. Still not a check, because neither model
looked anything up. A second opinion from something that cannot look is two
guesses.

**A check has to touch the world.** A catalog, a library, an index, the actual
document. That is the line.

---

## Citing in your own work, for this module

Every artifact you submit this module cites its sources this way:

| You used | You cite |
|---|---|
| A document | Title, section or page |
| A web page | Title, publisher, the URL, and that you opened it |
| A model output | The run label and the prompt file, in your repository |
| A search that found nothing | The catalog, the exact string, and "no results" |

**Model output gets cited like anything else.** If a sentence in your brief came
out of a model, say so and point at the run. That is not an admission, it is a
citation, and a reader who wants to check can open `runs/v3.json` and read the
prompt that produced it.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Authenticity** | Whether the output is original or belongs to somebody |
| **Attribution** | Naming who a claim, quote, or finding belongs to |
| **Misattribution** | A real thing credited to the wrong person or work |
| **Provenance** | The traceable history of where a piece of information came from |
| **Verifiable citation** | One that tells a reader how to go and look |
| **Negative result** | A recorded search that found nothing. Evidence, if recorded |

---

## Self-check

**1.** An output says: "Research from Ohio State found that students who study in
25-minute blocks retain more." Name every part of a checkable citation that is
missing, and say what you would search for first.

<details><summary>Answer</summary>

**Missing:** who (no researcher named), what (no study title), where (no journal,
no page, no report), when (no year). The only part present is an institution,
which is not enough to find anything.

**Search first:** not the claim. Search for whether a specific study exists by
asking the institution's research listing or a scholarly index for the topic and
the institution. Expect this to be slow, because "a large university studied a
popular topic" is not a search that narrows.

**The finding you can already write, before any search:** this is not a citation.
It cites an institution, which is a way of borrowing credibility without
providing a way to check. Whether the underlying claim is true is a separate
question you have not answered yet.
</details>

**2.** You find that a quote in an output is real, word for word, but is from a
different person than the output says. Which parameter, and why is this worse than
an invented quote?

<details><summary>Answer</summary>

**Authenticity**, specifically misattribution. Accept Validity with an argument,
since the sentence "X said Y" is false about a real person, and say which you
meant.

**Worse than an invented quote** because it survives the check most people run. A
person who searches the quote finds it immediately, sees that it is real, and
stops. The invented quote fails that same search and gets caught. The
misattribution passes it and keeps travelling.
</details>

**3.** Your partner writes "this source is fake" as a finding, with no search
recorded, and they turn out to be right. How do you score it, and what do you say?

<details><summary>Answer</summary>

**Score it zero, and say why without softening it.** The finding required
evidence and there is none. Being right by guess is not the skill being assessed,
and a habit of guessing correctly is worth nothing the first time it guesses
wrong on something that matters.

**What to say:** "You got the right answer and you have not shown me anything I
can check. Run the search, paste what came back, and it is worth full credit."
That is a two-minute fix and it is the whole point of the exercise.
</details>
