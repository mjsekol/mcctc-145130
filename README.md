# Applications of Artificial Intelligence · 145130
## AI Automation & Software Development · Mahoning County Career & Technical Center

Student materials for **145130 Applications of Artificial Intelligence**, senior year,
semester 1. Instructor: Michael Sekol.

Everything here is written to you, the student. Read it, run it, argue with it.

---

## What this course is

Applying AI to real workflows and real problems. Constructing prompts, rigorously
evaluating what comes back, understanding what the law requires, and building something
that works.

You finish able to build an AI-integrated application, defend every legal and ethical
choice you made building it, and explain to a non-technical person why it works and where
it fails.

**You arrive having finished two years of programming.** You write Python and C#, you use
Git without thinking about it, and you have shipped software. None of that is re-taught.

---

## How this course runs

**149-minute block, Periods 4/5B through 7.** Every day looks like this:

| Minutes | What happens |
|---|---|
| 10 | Bell ringer and standup: finished, working on, blocked by |
| 15 | Instruction. One concept, demonstrated live, including a deliberate failure |
| 50 | Build 1 |
| 5 | Reset |
| 55 | Build 2 |
| 14 | Demo and close. One team demos. Commit and push. |

**Period 8 is yours.** Forty-six self-directed minutes for BPA, credentials, side quests,
and capstone groundwork. It carries no new content and is graded under BPA / Credential /
Capstone.

**Friday introduces no new content.**

## The three gates

| Gate | AI use | What it is here |
|---|---|---|
| **Gate 1, Closed** | None | Timed reps, and in this course they are as often analytical as technical: evaluate this claim, identify this bias, find the fabricated citation. |
| **Gate 2, Adversarial** | AI is the opponent | The weekly core. You score AI output on validity, relevance, authenticity, potential bias, and hallucinations. At least one planted problem every week is genuinely arguable. |
| **Gate 3, Open** | Full tooling | Build with AI. Every build carries a decision log and a written legal and ethical analysis. |

## Where the models come from

Commercial AI developer APIs require users to be 18 or older. **This course never uses
them.** All model work runs against locally hosted models on lab hardware, which carry no
such terms and send no data outside the building.

Local models are slower and less capable than cloud models. That constraint is
instructional. You will feel directly what model size costs and what it buys.

**The architecture you build against:** Python serves the model, C# consumes it. A small
Flask service wraps a locally hosted language model, and your C# application calls it over
HTTP. That is how production AI systems are actually structured, with the machine learning
layer and the application layer separated.

## The rules that matter most

- **No work is graded that is not in a repository.** Every period ends with a commit.
- **Every project includes an AI usage log**: what you asked, what came back, what you
  changed, why.
- **Every project includes a licensing statement**: what you used, under what license,
  what you owe.
- **No personal information, real names, or school data enters any AI tool**, local or
  otherwise.
- **The only way to fail outright is to submit work you cannot explain.**

---

## What is in here

| Module | Weeks | Folder |
|---|---|---|
| 1 · Foundations of Artificial Intelligence | 1-3 | `module-1-foundations-of-ai/` |
| 2 · Prompt Engineering & Output Evaluation | 4-6 | `module-2-prompting-and-evaluation/` |
| 3 · Law, Licensing, Ethics & Privacy | 7-9 | `module-3-law-licensing-ethics-privacy/` |
| 4 · Data Foundations for AI | 10-12 | `module-4-data-foundations/` |
| 5 · Building With AI | 13-15 | `module-5-building-with-ai/` |
| 6 · Human-Centered AI & Automation | 16-18 | `module-6-human-centered-ai/` |

Every module folder is under `Courses/145130/modules/` and has the same shape:

```
03-lecture-notes/      read these if you missed class, or before you build
04-slides/             the decks from class, and their outlines
05-labs/               the guided labs and the files they use
07-gate2-adversarial/  the weekly AI output evaluations and the artifacts to score
09-project/            performance task briefs, templates, and problem drops
10-resources/          readings, practice, documentation
```

**Each module is self-contained**, with an entry check, a performance task, and exit
criteria. The course runs 18 weeks. Grading Period 1 is Weeks 1-9 and Grading Period 2 is
Weeks 10-18. **Week 18 carries acceptance testing, the WebXam post-test, and final
demonstrations.** Everything is scheduled by week and day, so your teacher will tell you
how the weeks line up with this year's calendar.

Plus `Courses/Misc/` for the Side Quest Catalog, the Lab Acceptable Use and Safety
Agreement, and the side quest bundles.

**Lecture notes are written so you can learn a concept from the file alone.** If you were
out, start there rather than asking someone what you missed.

## What is not in here, and why

Answer keys, module exit assessments, lesson plans, and the instructor's notes live in a
separate private repository. That is not secrecy for its own sake. A published answer key
is not recoverable, and the work is worth more to you unspoiled.

---

## Getting set up

Your junior-year toolchain still applies. This course adds:

- **A locally hosted model runner** on lab hardware
- **Flask**, for the service that wraps the model
- **.NET**, for the C# client
- **SQLite** for the database work, with MySQL and PostgreSQL covered as types

Your instructor sets up the lab model. Nothing here requires an AI account, an API key, or
a credit card, and nothing you write should ever need one.
