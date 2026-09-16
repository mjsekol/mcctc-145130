# Lecture Notes: The Implementation Plan and the Contingency Plan
## 145130 Applications of AI · Module 5 · Week 15, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W15_ImplementationAndContingency.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W15_ImplementationAndContingency.pptx)

If you missed class, you can learn this concept from this file alone. You need
nothing running.

**Competency 5.6.8** names four documents: implementation plan, contingency
plan, data dictionary, and user help. Two of them are today. The data dictionary
was Week 13. User help is tomorrow.

---

## Why this exists

You are writing these in Week 15, after the build, and you should know that this
is backwards. In real work both documents come first. Here they come last
because you could not have written a useful one in Week 13 without having been
through the week you are about to describe.

Write them now while it is fresh, and write them so that the next team could
follow them. The test of both documents is the same: **could somebody run this
project on a day you are not there?**

---

## The concept in plain language

**An implementation plan** answers three questions. What has to be true before
anybody writes code. What gets built, in what order, by whom. How you know a
milestone is finished rather than nearly finished.

**A contingency plan** answers three different questions. What can go wrong.
What you do about each one. Who decides.

They are different documents because they are read at different times. The
implementation plan is read on a good day, when you are deciding what to do
next. The contingency plan is read on a bad day, by somebody who is already
behind and possibly not you.

### The four parts of an implementation plan

| Part | What goes in it | The test |
|---|---|---|
| Before you start | checks, not work. Things that have bitten somebody. | every item is a command with a yes or no answer |
| Milestones | five or fewer, each one demonstrable in under a minute | you can point at it, not describe it |
| Who does what | one owner per piece, and a named backup for each | no piece has two owners and no piece has none |
| How you know it is finished | a command somebody else runs, that says pass or fail | "it works on my machine" is not on the list |

### The four parts of a contingency plan

| Part | What goes in it | The test |
|---|---|---|
| What can go wrong | risks, ordered by how likely, not how bad | every one has happened to somebody here |
| What you do about each | one action per risk, written for somebody else | a person who is not you could do it |
| What you cut first | an ordered list, and a list of what you never cut | cutting on Monday is a decision, on Thursday it is a panic |
| Who decides | which decisions belong to whom, and how they get recorded | the hard ones have a named person |

---

## Worked example 1: before you start, from the reference plan

Eight rows. Nothing on the list is work. Every one of them has cost somebody in
this lab a morning.

| # | Has to be true | How you check it | If it is not |
|---|---|---|---|
| 3 | The .NET SDK builds a `net8.0` project | `dotnet build` on a scratch console project | tell the instructor. This blocks Week 14. |
| 4 | `dotnet new sln` produces a file your SDK can open | on SDK 10 it writes a `.slnx`, so you pass `--format sln` | pass the flag |
| 6 | You know your task and your result shape | written in one sentence each, in the decision log | you are not ready to start |
| 8 | Both people can run everything on their own machine | each of you runs the health check on your own laptop | fix it now |

**Item 6 is the one teams skip and the one that costs most.** A team that starts
building before it has written down its result shape builds two different
programs and finds out on Thursday.

**Item 8 is the one that matters in this module specifically.** One of you may be
at BPA Regional for most of Week 14. A team with one working machine has no
backup.

---

## Worked example 2: milestones you can point at

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | The design is agreed | Week 13 Thu | `doc_check.py` reports all four design documents complete, and the result shape in the I/O specification matches the one in the IPO chart word for word |
| M2 | The design survives a walkthrough | Week 13 Fri | the record lists three findings, each marked fixed, deferred with a reason, or rejected with a reason |
| M3 | The service answers | Week 14 Tue | your service returns your envelope for a good answer, a model failure, and a refused request, and the three have different `source` values |
| M4 | The application talks to the service | Week 14 Thu | it prints a result, and a different line when the answer came from the fallback |
| M5 | Every failure handled and documented | Week 15 Wed | four failures produce four different messages, and the log has three real entries |

**Why M3 comes before M4.** Build the layer that deals with mess first. A C#
program written against a service that does not exist yet gets written against
what you imagine the service will send, and what you imagine is always the happy
path.

**Why M2 is a milestone at all.** A walkthrough after the code is written finds
nothing, because nobody wants to hear the design is wrong on Thursday of Week
15. Week 13 Friday is early enough that changing your mind is cheap.

---

## Worked example 3: the cut list, in order, written in advance

This is the part of the contingency plan that gets used, and the reason to write
it in Week 13 is that in Week 15 you are too invested to cut anything.

| Order | What goes | Why this order |
|---|---|---|
| 1 | the second task. Ship one, done properly. | one task end to end demonstrates everything the exit criteria ask. Two half-tasks demonstrate nothing. |
| 2 | extra fields in your result shape | a field nobody renders is a field nobody misses |
| 3 | retries | the fallback keeps the program usable. A retry only makes a wait longer. |
| 4 | batch mode over a file | the interesting part is one request, not the loop around it |
| 5 | anything that looks good in a demo and does nothing | this is the whole point of the module |

**What you never cut**, whatever else happens:

- the four distinct failure messages
- the fallback, and saying out loud that an answer came from it
- the troubleshooting log
- the I/O specification and the dataflow diagram
- the commit at the end of every period

Those five are what the exit criteria are written against. A program that only
works when everything works is not the assignment.

---

## The wrong version, and what it produces

A real shape of submission, and what each line actually says:

> **Milestones.** 1. Design complete. 2. Service complete. 3. Client complete.
>
> **Who does what.** The team divides the work between the frontend and the
> backend. Each member is responsible for their own area.
>
> **How you know each milestone is finished.** Each milestone is finished when
> the code for it is written and committed, and the developer is satisfied that
> it works as intended on their machine.

**"Service complete" is not a milestone.** It has no test, so on any given day
it is 90 percent done and stays there.

**"The team divides the work" names nobody.** On the Tuesday one of them is at a
competition, there is no backup named, and half the system stops.

**"The developer is satisfied" is the whole problem in five words.** The
developer is always satisfied. That is why they stopped. Finished has to be
something a person who is not you can check without asking you a question.

And here is the same document's contingency plan:

> **What you do about each one.** If the model is unavailable, wait for it to
> come back or install a different one.

Wait for it to come back. In a 149 minute block. The real answer is one command,
`python stub_model_server.py`, and it is in the run book, and the plan does not
know that.

---

## Why the wrong version is tempting

Because both documents are written at the end, when you are tired, and both of
them can be filled with true sentences that commit you to nothing.

"Features that are not essential are cut first" is true. It is also useless,
because on Thursday of Week 15 every feature feels essential and the document
does not name any of them. A plan that names nothing decides nothing.

**The habit that prevents it:** every row of both documents has to name
something. A command, a file, a person, or a number. If a row has none of those
four in it, it is a sentence about planning rather than a plan.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Implementation plan** | what gets built, in what order, by whom, and how you know it is finished |
| **Contingency plan** | what can go wrong, what you do, what you cut, and who decides |
| **Milestone** | something demonstrable, not a stage of work |
| **Owner** | the one person who has to defend a piece of the system |
| **Backup** | the person who owns it on a day the owner is not there |
| **Cut list** | what gets dropped, in order, written before you are under pressure |
| **Acceptance procedure** | the agreed test of whether the deliverable is acceptable |
| **Decision log** | a dated record of what you decided and why, written the day you decided it |

---

## Self-check

**Question 1.** "Service complete" is not a milestone. Rewrite it as one, with a
test somebody else can run in under a minute.

**Question 2.** Your contingency plan says "a team member may be absent, the
other member covers their work." Name two things that sentence is missing that
would make it usable on a day you are at a competition.

**Question 3.** Your plan says you cut non-essential features first. Give the
strongest argument for keeping a list that vague, then say why this module asks
for a named, ordered list instead.

---

### Answers

**1.** One good answer: "The service answers `/generate` with my envelope for
three cases: a good model answer, a model failure, and a refused request, and
the three return `source` values of `model`, `fallback`, and `none`. Finished
when somebody runs the three commands in my run book and sees three different
`source` values." It names a file, three commands, and three observable values.

**2.** It does not say **who** covers **what**, so on the morning it happens
there is a conversation instead of work. And it does not say how the returning
person takes their half back, so the two of you edit the same files from two
different understandings. The reference plan fixes both with a named backup per
role and one rule: read the stand-up log before you take your tasks back.

**3.** The strongest argument for vagueness: you cannot know in Week 13 which
feature will turn out to be cheap and which will turn out to be the whole
project, so an ordered list written early will be wrong, and a wrong list is
worse than none because people follow it.

Why this module asks for the named list anyway: the ordering is not really about
which feature is cheapest. It is about which cuts protect the exit criteria and
which cuts destroy them. That ordering is knowable in Week 13, because the exit
criteria were published in Week 13. And the list has a second half, what you
never cut, which is the half that does the real work. When you do find that your
list was wrong about a feature, you change it and write down why, which is a
decision. Having no list is not a decision, it is an argument on a Thursday.
