# Lecture Notes: What Programs and Scripts Actually Solve
## 145130 Applications of AI · Module 1 · Week 2, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W02_WhatProgramsSolve.md)

**There is no exported deck for this lesson yet.** The outline is current. The old export
described the model service, which came out of this module, so it was removed rather than
left in place: a deck that contradicts the lesson is worse than no deck. The Gamma account
ran out of credits before it could be regenerated. Teach from the outline, or generate the
deck once credits are available:

```
node tools/gamma.js Courses/145130/modules/module-1-foundations-of-ai/04-slides/MCCTC_145130_Slides_W02_WhatProgramsSolve.md --export pptx
```

If you missed class you can learn this from this file alone.

**Competency 5.1.1:** describe how computer programs and scripts can be used to
solve problems across desktop, mobile, enterprise, AI, and cloud. Outcome 5.1 is
4.21 percent of your exam.

---

## Why this exists

You have written programs for two years. What you have rarely had to do is say,
out loud, **which kind of problem a program is the answer to**, and which kind it
is not.

That is the exam competency, and it is also the question that decides whether a
project is worth building. A team that cannot state the problem in one sentence
about a person builds something impressive that nobody uses.

---

## The concept in plain language

A program earns its place when at least one of these is true:

- **Repetition.** The same steps happen often enough that a person doing them is
  a waste of a person.
- **Scale.** There is more of it than a person can hold: too many rows, too many
  files, too many events per second.
- **Speed.** The answer is needed faster than a person can produce it.
- **Consistency.** The same input must produce the same output every time,
  including when the person who knows the rules is out sick.
- **Reach.** The work has to happen where a person is not: overnight, on a
  device, in a building nobody is standing in.

If none of those is true, the honest answer is often a checklist, a spreadsheet,
or a conversation, and saying so is a professional skill rather than a failure.

### The five places the competency names

| Where | What it means | What shapes the program |
|---|---|---|
| **desktop** | runs on one machine, for the person at it | the file system, one user, works offline |
| **mobile** | runs on a device in a pocket | battery, intermittent network, small screen, permissions |
| **enterprise** | runs the organisation's shared work | many users, roles, audit trails, data that must survive |
| **AI** | a model is part of the path from input to output | the answer is not exact, and failure has to be handled |
| **cloud** | runs on somebody else's shared hardware, reachable over a network | scale up and down, pay per use, and it is not your machine |

These overlap constantly. The C# application you build in Module 5 is a desktop
program calling an AI service that could be running on a cloud machine inside an
enterprise network. The categories are useful for describing where a constraint
comes from, not for sorting programs into boxes.

---

## Worked example 1: the same problem in five places

One problem: **the makerspace gets more help requests than anyone can sort.**

| Where | What the program would be | The constraint that shapes it |
|---|---|---|
| desktop | a program a lab manager runs on their own machine against a downloaded file | the file has to get to that machine somehow, and it goes stale |
| mobile | a form students fill in on their phones, with a photo | photos are large, the network in the back of the lab drops, permissions are needed for the camera |
| enterprise | a shared ticket board with roles, history, and a record of who changed what | several people at once, and the history has to survive a person leaving |
| AI | a classifier and summariser that suggest a label and a one-line summary | the suggestion is sometimes wrong, so a person must be able to see and override it |
| cloud | the ticket board running on rented hardware, reachable from home | it is not your machine, so data location and access become questions |

**Notice what changed and what did not.** The problem is identical in all five
rows. What differs is the constraint, and the constraint is what actually
determines the design.

---

## Worked example 2: the AI row is different from the other four

Four of those rows produce exact answers. The AI row does not, and that changes
three things about how you build it.

**The output is a suggestion until somebody checks it.** The anchor stack
enforces this structurally: `classify` may only return a label from a fixed list,
and a label outside that list is treated as a failed answer, because a program
that trusts a made-up label writes it into your database.

**Failure is normal, not exceptional.** The model being slow, down, or unusable
is a Tuesday, not a crisis, so the program has a planned answer for each. The
seam report you built yesterday is that plan, written down.

**Provenance has to travel with the answer.** Every answer says whether a model
or a rule produced it. In the other four rows nobody asks, because there is only
one possible answer to the question.

Here is the third point in real output, from `triage_client.py` run against the
stack with no model running:

```
model endpoint http://127.0.0.1:11634, model llama3.2
Triaging 12 help requests from tickets.json

== MT-2001 ==
  label:   could not be read out of the answer (unparsed)
  the model actually said: I am not able to help with that request.

Done. 12 tickets, 12 with no label this program was willing to report.
```

The program worked. Every ticket got an honest line, and not one of them got an
invented label. The last line makes it impossible to mistake what happened.

---

## Worked example 3: writing a problem statement that is about a person

This is the exercise, and it is harder than it looks.

**Not a problem statement, because it names a program:**

> "Build an app that tracks which lab station each 3D print is running on."

**A problem statement:**

> "Students come back for a print and cannot tell which of the four printers has
> it, so they open lids on prints that are still running and ruin them. It
> happens two or three times a week."

Read the second one and notice what it gives you that the first does not. Who is
hurt. What goes wrong. How often. And no mention of anything to build, which
leaves every solution still on the table, including a whiteboard.

**The test:** if your sentence names an app, a tracker, a website, a dashboard,
or a program, you have written a solution. Rewrite it until it names a person and
what goes wrong for them.

---

## The wrong version, and the cost

> "We are building an AI-powered platform to streamline the help request
> workflow."

Nothing in that sentence is checkable and nothing in it is about a person. It
does not say who is hurt, what goes wrong, or how often. It does say "AI-powered"
and "platform", which is how you can tell it was written to sound finished rather
than to be acted on.

The cost is concrete: three weeks later the team cannot decide whether a feature
is in scope, because the sentence they agreed on cannot settle any argument. A
good problem statement is a tool you use every week, and its job is to end
disputes.

---

## Why the wrong version is tempting

Because it sounds like the sentence in the vendor materials you have all read,
and because writing what actually hurts feels too small to be impressive. It is
not small. "Students ruin two prints a week" is a number somebody can act on, and
"streamline the workflow" is not.

### Write this down

> A problem statement names a person and what goes wrong for them, and mentions
> nothing you are going to build.

---

## Vocabulary

| Term | What it means |
|---|---|
| **script** | a short program, usually automating steps somebody used to do by hand |
| **desktop application** | runs on one machine for the person at it |
| **enterprise system** | shared, multi-user, with roles and a history that must survive |
| **cloud** | somebody else's shared hardware, reached over a network |
| **workflow** | the actual sequence of steps a person follows today |
| **problem statement** | one sentence naming who is hurt, what goes wrong, and how often |
| **scope** | what is and is not part of this piece of work |
| **constraint** | something true about the situation that limits the design |

---

## Self-check

**1.** Rewrite this as a problem statement: "We need a website where the robotics
team can sign out tools."

**2.** Name one constraint that applies to a mobile program and not to a desktop
one, and say how it changes the design.

**3.** A team proposes using a model to decide which help requests are urgent.
Give one reason that is a reasonable use, and one thing the design must include
because a model is in the path.

### Answers

**1.** Something like: "Tools go missing from the robotics cabinet and nobody
knows who had them last, so the team buys replacements two or three times a
season and loses build time looking." It names the people, what goes wrong, how
often, and what it costs, and it does not name a website.

**2.** Any of: the network drops, so the program has to work with a request that
never completes and try again later; battery, so constant polling is not free;
permissions, because the camera and location are not available until the person
grants them; screen size, which changes what can be shown at once. Each one
changes the design by forcing a decision that a desktop program can ignore.

**3.** Reasonable because urgency is fuzzy, the input is free text written by
students, and a person is going to read the queue anyway and can override a bad
call. The design must include provenance and an override: every suggestion says
it came from a model, a person can change it, and the change is recorded. Without
that, a wrong urgency is indistinguishable from a human decision and nobody can
audit it later.
