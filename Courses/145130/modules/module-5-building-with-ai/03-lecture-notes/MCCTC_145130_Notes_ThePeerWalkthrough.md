# Lecture Notes: The Peer Walkthrough
## 145130 Applications of AI · Module 5 · Week 15, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W15_PeerWalkthrough.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W15_PeerWalkthrough.pptx)

If you missed class, you can learn this concept from this file alone. You need
your own design documents and a person.

**Competency 5.6.9** is reviewing the design through a peer walkthrough.
**Competency 1.1.9** is giving and receiving constructive feedback. The second
one is the harder of the two and it is why this has a script.

---

## Why this exists

You ran one of these in Week 13, on your design, before you built anything.
Today you run the second one, on the finished thing, and the two are different
exercises.

Week 13's walkthrough asked whether the design would work. Today's asks whether
the thing you built is the thing you designed, and whether anybody outside your
team can follow it.

The reason this is a competency at all is that it is the cheapest defect-finding
technique anybody has ever measured. It needs no tools, no environment, and no
running code. It needs one other person and forty minutes.

---

## The concept in plain language

**A walkthrough is the author reading their own work out loud, line by line, to
somebody whose job is to interrupt.**

It is not a demo. In a demo you show the parts that work. In a walkthrough you
read every line in order, including the parts you would not have shown.

Three roles, and they matter.

| Role | Does | Does not |
|---|---|---|
| **Author** | reads each part out loud and says what it does | defend, explain away, or say "I was going to fix that" |
| **Reviewer** | asks questions, points at things, writes findings down | fix anything, or design a better version out loud |
| **Recorder** | writes every finding in the record, in the author's own words | decide whether a finding is valid |

With two people, the reviewer records. With three, use all three roles.

### The one rule that makes it work

**The author does not defend.** When a reviewer says "I do not understand this
part", the author's only job is to write it down. Not to explain it. The
explanation is the thing that is missing from the document, and giving it out
loud makes the problem disappear from the room without removing it from the
work.

This is genuinely hard. Everybody does it. You will do it in the first five
minutes and your partner should say "you are defending" and you should stop.

### What a finding is

A finding is something specific that somebody can act on. Three parts: where it
is, what is wrong or unclear, and how bad it is.

**Not findings:** "this is good", "maybe make it clearer", "I would have done it
differently".

| Severity | Means | Example |
|---|---|---|
| **Blocker** | the thing does not work, or the documents contradict each other | the I/O spec says five labels and the code has six |
| **Major** | it works and somebody will get it wrong | the user help never says what a fallback is |
| **Minor** | it is right and it is untidy | a heading says Steps and the field is called `bullets` |

---

## Worked example 1: the script, forty minutes

Run it in this order. The order is the design of the exercise.

| Minutes | What happens |
|---|---|
| 0-3 | Author states the task, the result shape, and the one thing they are least sure about |
| 3-10 | **Documents first.** Author reads the I/O specification out loud, field by field. Reviewer has the code open. |
| 10-18 | Author reads the dataflow diagram. Reviewer asks, at each boundary, what is checked there |
| 18-26 | **Then the code.** Author walks the failure paths only. Not the happy path. |
| 26-33 | Reviewer drives. Author does not touch the keyboard. Reviewer tries to break it. |
| 33-38 | Recorder reads every finding back. Author says only whether they understood it |
| 38-40 | Author writes one sentence per finding: fixed today, deferred with a reason, or rejected with a reason |

**Documents before code, always.** If you start with code, everybody reads code,
finds three small things, and the hour is gone. The expensive defects are
disagreements between the documents and the code, and you only see those by
holding one against the other.

**The author does not touch the keyboard from minute 26.** You know where not to
click. That knowledge is the thing you are trying to make visible.

---

## Worked example 2: five questions that always find something

Give these to your reviewer before you start. They are not polite questions and
they are not meant to be.

**1. "Show me the line that does this requirement."** Read one requirement from
their spec, and make them point at the code. A requirement nobody can point at
is a finding, every time.

**2. "What happens if I give it nothing?"** Empty string, whitespace, a file
with no records. Somewhere in most builds is a path that sends an empty prompt
and lets the service refuse it, and prints the refusal as if it were a failure
of the service.

**3. "Which of these numbers is bigger?"** The client's timeout and the
service's timeout times its attempts. Ask them to say both numbers out loud. If
the client's is smaller, that is a blocker and it takes ten seconds to find.

**4. "What does the person see when the model is off?"** Then turn it off and
watch. The answer "it falls back" is not the answer. The answer is the exact
line on the screen, and whether that line says the model was not used.

**5. "Read me this comment, then read me the line under it."** Comments drift
away from code faster than anything else in a repository, and a comment that
describes what a number should do sitting above a number that does the opposite
is the hardest defect in this module to see.

---

## Worked example 3: the record, which is the deliverable

The walkthrough is not the deliverable. The record is. Here is the shape, with
real findings from this module's materials.

| # | Where | Finding | Severity | Decision |
|---|---|---|---|---|
| 1 | `Program.cs` line 157 | the comment says the timeout is long enough for the service's retry, and the value is 5 seconds while the service can take 40 | Blocker | Fixed the same day. Default raised to 45 and read from the environment. |
| 2 | `Program.cs` line 234 | a new `HttpClient` is created inside the per-note loop | Major | Fixed. One client for the run. |
| 3 | `user-help.md` fallback section | nine words. Does not say how you know, how much to trust it, or what to do | Major | Deferred to Thursday. Owner named, due before the demo. |
| 4 | `io-specification.md` | says the service retries up to five times. The code retries once, capped at three. | Blocker | Fixed. The document was wrong, not the code. |
| 5 | `data-dictionary.md` | lists a `confidence` float that does not exist anywhere in the code | Major | Fixed. Removed, and a note added about where it came from. |

**Every row ends in a decision.** Fixed, deferred with an owner and a date by
week and day, or rejected with a reason. A finding with no decision next to it
is a finding nobody acted on, and the record exists to make that visible.

**Rejecting a finding is allowed and it has to be written down.** "Reviewer
suggested caching answers. Rejected: this service keeps no state on purpose, and
a cache is a store of other people's writing that we would then have to justify
under the privacy rules." That is a good rejection and it is worth more than a
grudging fix.

---

## The wrong version, and what it produces

Two teams sit down. Both open their code. One says "so this is the client, it
calls the service, and this bit handles the errors". The other says "yeah that
looks good". Twelve minutes. Both write "looks good" in the record.

Nothing was found, and both teams now believe their design was reviewed.

**That is worse than not doing it**, because a review that found nothing is used
as evidence that there was nothing to find. The Week 13 walkthrough on this
module's own materials turned up a comment that contradicted its own value, a
document claiming five retries where the code had one, and a data dictionary
field that did not exist. None of those would have been caught by a person
saying "looks good".

What makes the difference is structure: documents first, failure paths only,
author off the keyboard, and five questions the reviewer did not have to think
of.

---

## Why the wrong version is tempting

Because criticising your friend's work is uncomfortable, and because being
criticised feels like being graded.

There is a second reason, and it is the honest one. By Week 15 you are tired,
the thing works, and a walkthrough can only produce more work for you. There is
no version of a good walkthrough that ends with you having less to do.

**What actually makes it bearable:** the findings are about the work and the
record says so. A finding names a file and a line, never a person. And you get
to reject findings, in writing, with a reason. A reviewer who knows their
finding will be recorded and answered says more than one who expects to be
argued with.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Walkthrough** | the author reads their work out loud to a reviewer whose job is to interrupt |
| **Inspection** | a stricter version with defined roles, entry criteria, and a checklist |
| **Finding** | where it is, what is wrong, and how bad it is |
| **Blocker** | it does not work, or two documents contradict each other |
| **Major** | it works and somebody will get it wrong |
| **Minor** | it is right and untidy |
| **Disposition** | what you decided about a finding: fixed, deferred, or rejected |
| **Record** | the written result. The deliverable. |

---

## Self-check

**Question 1.** Your reviewer says "I do not understand how the fallback works."
Give the wrong response and the right one, and say what the right one produces.

**Question 2.** Name two reasons documents are walked before code, and give an
example of a defect that only appears when you hold one against the other.

**Question 3.** Your reviewer suggests something you think is wrong. What do you
do, and what has to end up in the record?

---

### Answers

**1.** The wrong response is to explain it. The explanation is clear, the
reviewer nods, the moment passes, and nothing changes. The right response is to
write down that the reviewer could not tell how the fallback works from the
document, and to ask one question back: which part stopped making sense. That
produces a finding with a location in it, and the thing you would have said out
loud becomes the paragraph the document was missing.

**2.** First, the expensive defects are disagreements between the documents and
the code, and you can only see those with both open. Second, once people start
reading code they keep reading code, and the hour goes on small things. An
example: the I/O specification says the service retries up to five times, the
code retries once with a cap of three. Neither the document nor the code looks
wrong on its own. Held together, one of them has to change, and deciding which
is a real decision about how the system should behave.

**3.** You record it, with the severity the reviewer gave it, and you write your
rejection and the reason in the decision column. You do not argue it out in the
walkthrough, because the walkthrough is for finding things and not for settling
them. If it turns out to matter and the two of you cannot agree, both positions
go in the question log in one sentence each and the instructor settles it on the
next class day. What must end up in the record is the finding and your written
reason for rejecting it. A finding that vanishes because the author disagreed is
the failure mode this whole exercise exists to prevent.
