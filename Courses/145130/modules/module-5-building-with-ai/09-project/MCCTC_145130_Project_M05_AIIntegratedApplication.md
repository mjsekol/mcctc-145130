# Performance Task · The AI-Integrated Application
## 145130 Applications of AI · Module 5 · Weeks 13-15

**100 points. Projects category, 35 percent of your grade.**
**Due Week 15, Thursday, at the end of the 15-minute commit window.**

---

## The brief

> From: the person who runs the front office
>
> Every week I get somewhere between forty and two hundred short pieces of writing
> from students and staff, and I have to sort them before I can do anything about
> them. Help requests. Sign-up notes. Equipment problems. Late passes with reasons
> on them. It changes week to week.
>
> They are short, they are messy, and about a third of them are the same thing
> said five different ways. What I need is something that reads a pile of them and
> gives me back something I can act on: a short version of each one and a category
> I can sort by.
>
> I have been told there is a language model on a computer in this building. I do
> not know what that means and I do not want to. What I want is something I can
> run on a Monday morning that works, and that tells me when it is guessing.
>
> Two things I will be difficult about. It has to still do something useful on a
> day the model is not working, because half the days here are that day. And none
> of what people write can end up in a file somewhere, because some of it is
> personal and none of it is mine to keep.

**That is the whole brief.** It does not say what the categories are. It does not
say what "a short version" means. It does not say what pile of writing you are
working with, because it changes week to week.

**Extracting the requirements from that is the first thing you are graded on.**

---

## What you are building

A C# front end that calls a locally hosted model through a Flask service of your
own, with structured output parsing and full failure handling, plus the design
documentation that goes with it.

**Your own task. Your own result shape. Your own program.**

You traced a demo service in Week 13. **Do not copy it, and you could not get
away with it if you tried.** It has one task, one result field, one validation
rule, and a parser that handles one shape out of four, and it says so in its own
header. It exists to show you what a contract looks like from the outside.

Your service has your own task, your own result shape, and a parser that handles
at least three shapes. What you take from the demo is the idea of an envelope,
not its contents.

If you hand in something shaped like a file you were given, you will be asked to
explain a design decision you did not make, and the only way to fail this program
outright is submitting work you cannot explain.

---

## The pieces

| # | Piece | Language |
|---|---|---|
| 1 | A model service that wraps a locally hosted model | Python, Flask |
| 2 | An application that calls it over HTTP | C#, `net8.0` |
| 3 | A stand-in model server so it runs with no model installed | Python, standard library |
| 4 | The design documentation set, nine documents | Markdown |
| 5 | A decision log and a troubleshooting log | Markdown |

**Piece 3 is not optional.** Your project has to run on a machine with no model
on it, because that is the state of most machines here most of the time. You may
use `09-project/project-files/stub_model_server.py` as your stand-in, and you say
so in your decision log. You may also write your own, and if you do, say why.

---

## Technical requirements

Every one of these exists for a reason, and the reason is next to it.

| # | Requirement | Why |
|---|---|---|
| R1 | The model runs locally. No commercial AI developer API. | Those services require users to be 18 or older. |
| R2 | No credential anywhere in the code, the config, or the repository. | A local model needs none. A credential that exists can leak. |
| R3 | No personal data reaches a model, a log, or a file. Every fixture is invented and labelled as invented. | Program rule, and the client asked for it in the brief. |
| R4 | Your service returns **one envelope shape for every outcome**, with a field that says where the answer came from. | Your application writes one deserializer. |
| R5 | Your service **falls back** when the model cannot be used, and says so. | The client asked for this in the brief. |
| R6 | Your application reports the **four wire failures separately**, each naming what to do. | One message for four problems wastes a period. |
| R7 | Your application's timeout is **larger than your service's worst case**, and the arithmetic is in a comment. | Otherwise the labelled fallback never arrives. |
| R8 | Your parser handles **at least three different shapes** a model can answer in. | A model that used a fence yesterday will not tomorrow. |
| R9 | Your validator returns **the reason**, not a boolean. | That sentence ends up in the envelope. |
| R10 | Input is checked **before** the model is called, and a refused request costs nothing. | A wrong request should not cost twenty seconds. |
| R11 | C# targets `net8.0`. Scaffold with `dotnet new sln --format sln`. | Lab machines may have an older SDK than the one you build on. |
| R12 | Every stub and service takes a `--port` or reads one from the environment, and every recorded command passes one. | A client that reaches somebody else's server does not fail. It answers. |
| R13 | Every period ends with a commit. | Version control is a daily ritual. |

**On R11.** On a machine with .NET SDK 10, `dotnet new sln` writes a `.slnx` file
that an older SDK cannot open. This was checked on the build machine. The full
scaffold, verified:

```
dotnet new console -n YourApp -f net8.0
dotnet new xunit -n YourApp.Tests -f net8.0
dotnet new sln -n YourApp --format sln
dotnet sln YourApp.sln add YourApp/YourApp.csproj YourApp.Tests/YourApp.Tests.csproj
dotnet add YourApp.Tests/YourApp.Tests.csproj reference YourApp/YourApp.csproj
dotnet build YourApp.sln
dotnet test YourApp.sln
```

---

## Required repository structure

```
your-project/
  README.md                  what it does, how to run it, what is not finished
  model_service/
    app.py                   your service
    model_client.py          the only file that talks to the model
    requirements.txt
  client_csharp/
    YourApp.sln              classic format
    YourApp/
    YourApp.Tests/
  stub_model_server.py       or a note saying which one you used
  fixtures/
    README.md                what each fixture is and that it is invented
  design/
    ipo-chart.md
    dataflow-diagram.md
    io-specification.md
    constraint-list.md
    data-dictionary.md
  docs/
    implementation-plan.md
    contingency-plan.md
    user-help.md
    troubleshooting-log.md
  decision-log.md
  peer-walkthrough-record.md
  evidence/                  captured output from real runs
```

**Check the documentation set with the tool.**

```
python doc_check.py your-project
```

It is in `09-project/project-files/`. It tells you what is missing and what is too
short. It cannot tell you whether anything you wrote is true. A person does that,
in the walkthrough.

---

## DMAIC checkpoints

The framework is the same one you have used since 145060. Here is what each phase
means for this build.

### Define · Week 13, Monday and Tuesday

Extract the requirements from a brief that does not contain them. Decide your task
and your result shape, and write the shape down in JSON.

**Checkpoint, Monday end of Build 2:** `decision-log.md` committed, with your task
in one sentence, your result shape as a JSON block, and one sentence on who the
person using it is.

### Measure · Week 13, Wednesday

Put numbers on it. What the limits are, what the worst case is, how long things
take.

**Checkpoint, Wednesday end of Build 2:** constraint list with three columns and
an I/O specification with four columns per field, both committed.

### Analyze · Week 13, Thursday and Friday

Model the solution before you build it, and have somebody else find the holes.

**Checkpoint, Thursday end of Build 2:** milestone M1, all four design documents
complete. **Friday:** milestone M2, the walkthrough record.

### Improve · Weeks 14 and 15

Build it. This is where the Agile ceremonies live: a written stand-up every day,
one milestone at a time, and a demonstration at the end.

**Checkpoint, Week 14 Tuesday:** M3, your service answers with three different
`source` values. **Week 14 Thursday:** M4, your application talks to your service.
**Week 15 Wednesday:** M5, every failure handled and documented.

### Control · Week 15

Prove it stays working and write down how somebody else keeps it working.

**Checkpoint, Week 15 Thursday:** the full documentation set, the evidence
captures, and the acceptance run.

---

## Milestones

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | The design is agreed | Week 13 Thu, end of Build 2 | `doc_check.py` reports all four design documents complete, and the result shape in the I/O specification matches the IPO chart word for word |
| M2 | The design survives a walkthrough | Week 13 Fri | the record lists at least three findings, each marked fixed, deferred with a reason, or rejected with a reason |
| M3 | The service answers | Week 14 Tue, end of Build 2 | three runs, three different `source` values, captured to `evidence/` |
| M4 | The application talks to the service | Week 14 Thu, end of Build 2 | four failures produced on purpose and captured, four different messages |
| M5 | Every failure handled and documented | Week 15 Wed, end of Build 2 | `doc_check.py` reports every document complete, and the troubleshooting log has three real entries |
| **Due** | **Everything** | **Week 15 Thu** | the last commit pushed inside the commit window is the submission |

---

## Three worked scope examples

All three of these would earn full marks. They differ in ambition, not in quality.

### Small, and completely finished

**Task:** one task, `categorize`. **Result shape:** `{"label": str, "why": str}`,
where `label` is one of four words the front office actually uses.

**What makes it a full-marks project:** every failure handled, four distinct
messages, a parser that survives four captured answer shapes, a fallback that uses
a keyword rule and says so, and nine documents that are all true. The application
reads one note from the command line.

**Why somebody would choose it:** a two-person team where one person is at BPA for
three days of Week 14. This scope survives that.

**The risk:** finishing on Tuesday of Week 15 and spending three days adding
things nobody asked for. Do not. Spend them on the documentation and the
walkthrough, which is where the marks are.

### Medium, and the one most teams should aim for

**Task:** two tasks, `shorten` and `categorize`. **Result shapes:**
`{"summary": str, "keep": [str]}` and `{"label": str, "confidence_note": str}`.

**What it adds:** the application reads a JSON file of notes and runs both tasks on
each, so there is a loop, a count, and a summary line at the end that has to be
true.

**Why somebody would choose it:** two tasks is where the contract starts doing
real work, because a second result shape means a second parser and a second set
of rules, and that is the part of the design that gets graded hardest.

**The risk:** the count at the end. Three of the Gate 2 exercises in this module
plant a false count, and it is the most common mistake in the project.

### Large, and only if both partners are here all of Week 14

**Task:** two tasks plus a **grouping pass** that finds notes about the same thing
and reports them together. **Result shape:** the two above, plus
`{"groups": [{"label": str, "ids": [str]}]}`.

**What it adds:** a second round trip, a decision about how similar is similar
enough, and a result shape that is a list of objects, which is materially harder
to parse and to validate.

**Why somebody would choose it:** the front office said a third of the notes are
the same thing said five ways, and this answers that directly.

**The risk, and it is real:** the grouping is the part that is interesting and the
part nobody asked for in writing. Every hour spent on it is an hour not spent on
failure handling, and failure handling is what the exit criteria and the rubric
are built around. **Your cut list puts grouping first.**

### Scope calibration, three signals

| If your team | Aim for |
|---|---|
| has one partner out for three or more days of Week 14 | Small |
| has both partners able to run everything on their own machine, and a committed result shape by Monday close | Medium |
| finished M3 by Monday of Week 14 and has already made the model fail four ways | Large |

---

## Grading · the 100-point project rubric

| Dimension | Points |
|---|---|
| Functionality | 25 |
| Code Quality | 20 |
| Documentation | 20 |
| Process | 15 |
| Demonstration | 10 |
| Polish | 10 |

### What each dimension means here

**Functionality, 25.** It runs with no model installed. Your service produces all
three `source` values. Your application produces four distinct failure messages.
Your parser handles at least three answer shapes. A refused request costs nothing.

**Code Quality, 20.** Scored on the five-dimension standard: Correctness,
Security, Readability, Performance, Requirements Fit. No credential anywhere. No
personal data anywhere. Names that say what the thing does. Comments that agree
with the code under them. One `HttpClient` for the run. Nothing compiled or read
from disk per request that could be done once.

**Documentation, 20.** Nine documents, all present, all true, all checkable
against your code. `doc_check.py` passing is the floor. The user help is scored on
whether somebody who has never seen the program can start it.

**Process, 15.** A commit at the end of every period, including Week 14. A
stand-up log with a row for every day. A decision log with real decisions in it,
dated by week and day. A troubleshooting log with three real entries, each naming
a methodology. A walkthrough record with decisions on every finding.

**Demonstration, 10.** The five-minute script below, or a desk demo on the same
checklist. Including the spoken question at the end.

**Polish, 10.** The output is readable by the person in the brief, not by you. The
README says what is not finished. Nothing in the repository is left over from a
lab.

---

## The five-minute demo script

Five minutes. Timed. You will be stopped.

| Minutes | What |
|---|---|
| 0:00 to 0:30 | **The problem, in the client's words, not yours.** What did the front office ask for. |
| 0:30 to 1:00 | **Your task and your result shape.** Show the JSON block. Say why those fields and not others. |
| 1:00 to 2:00 | **Run it working.** One note in, one answer out, and point at the line that says it came from the model. |
| 2:00 to 3:15 | **Break it, live, twice.** Stop your model and run it again. Then stop your service and run it again. Read both messages out loud. |
| 3:15 to 4:00 | **One decision you made and one you rejected.** From your decision log. Say what it cost. |
| 4:00 to 4:30 | **One thing that went wrong this module** and the log entry about it. Name the methodology. |
| 4:30 to 5:00 | **The question.** |

### The question

Every demonstration ends with the same question, asked of **one named person on
the team, without notes**:

> Why are the model layer and the application layer separate?

**Four reasons and an honest account of what the split costs.** This is an exit
criterion for the module and it cannot be assessed on paper.

### The ten-point demonstration checklist

| # | | Points |
|---|---|---|
| 1 | The problem stated in the client's terms | 1 |
| 2 | The result shape shown and justified | 1 |
| 3 | A working run, with the source of the answer pointed at | 2 |
| 4 | Two failures produced live, with both messages read out | 2 |
| 5 | One decision and one rejection, from the log | 1 |
| 6 | One troubleshooting entry, with the methodology named | 1 |
| 7 | The question, answered without notes | 2 |
| | **Total** | **10** |

---

## Submission checklist

- [ ] `dotnet build YourApp.sln` succeeds, targeting `net8.0`
- [ ] `dotnet test YourApp.sln` passes, and you can say how many tests
- [ ] Your service starts with an explicit port and prints it
- [ ] Your whole project runs on a machine with no model installed
- [ ] `python doc_check.py your-project` reports every document complete
- [ ] `evidence/` has captures for three `source` values and four wire failures
- [ ] `decision-log.md`, `troubleshooting-log.md`, `peer-walkthrough-record.md`
- [ ] The stand-up log has a row for every day of Week 14
- [ ] No credential anywhere. Check by searching for the word `key`.
- [ ] Every fixture is invented and labelled as invented
- [ ] `README.md` says what is not finished
- [ ] Committed and pushed inside the Week 15 Thursday commit window

---

## Exit criteria for this module

You can self-check against these. They are the three things the module is built to
produce, and they are also what the demonstration asks.

- [ ] I can wire an application to a model and handle the model failing, timing
      out, or returning garbage.
- [ ] I can parse unstructured model output into something my program can rely on.
- [ ] I can explain why the model layer and the application layer are separate.

The full checklist is in
`10-resources/MCCTC_145130_ExitCriteria_M05.md`.

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`. It is
**instructor-only**, like the anchor stack it documents. It adds the full
documentation set as worked examples and ships an acceptance procedure that runs
against the anchor. Do not hand any of it out.

**Verified on the build machine:** `python run_acceptance.py` reports
`10 of 10 cases passed in 22.0 s`. `python doc_check.py reference-implementation`
reports every document complete.

## The three ways this project goes wrong, and the intervention

**1. The team copies the demo service.** It is right there, it runs, and it is
the shape of an answer. You see it on Tuesday of Week 13 when a team's result
shape is a single `headline` string and their task is writing headlines.

**The intervention, on Tuesday and not later:** ask each partner separately, in
front of each other, why those five labels and not four or six. A team that copied
cannot answer, and the fix at that point costs them an hour. On Thursday of Week
15 it costs them the project.

**2. The team builds the interesting part and not the assignment.** Usually the
grouping pass from the large scope example, or a nicer terminal output. You see it
in Week 14 when M3 is late and something nobody asked for is finished.

**The intervention:** open their own contingency plan and read their own cut list
back to them. If they have not written one yet, that is the real problem and it
takes twenty minutes to fix.

**3. The documentation is written on Thursday of Week 15.** You see it because
`doc_check.py` passes and every document is true of a program nobody built.

**The intervention, in Week 13:** the milestones are ordered so that M1 and M2 are
both design. A team that has not committed four design documents by Thursday of
Week 13 does not get to start Week 14 on the build. Say that on Monday.

## What to say to a team whose scope is too big

> Show me your cut list. Which of the things you are building is first on it?

Then: "Cut it now, on a Monday, while it is a decision. On Thursday it is a panic
and you will cut something worse."

If they have no cut list, that is the conversation instead, and it is a better
one.

## What to say to a team whose scope is too small

Do not tell them to add a feature. Ask this instead:

> Make your model fail in a way you have not tried yet, and show me what your
> program says.

A small project with every failure handled is a full-marks project. A small
project that only works when everything works is not, and the gap between those
two is where the remaining time should go. Point them at the five stub modes they
have not used.

## Common grading question: how much scaffolding is too much

Using `project-files/stub_model_server.py` as their stand-in model server is fine
and should be encouraged, with a line in the decision log. The stub is the model
layer, which nobody is asking them to write.

**Copying `contract_demo_service.py` and renaming the task is not fine**, and it
is also not enough to pass: that file has one task, one field, one rule, and a
parser that handles one shape. A project built on it fails requirements R8 and R9
on its own terms. The test is the demonstration: ask them why a rule in their
validator is there. A team that wrote it can answer in one sentence.

**Students never receive the anchor stack**, which is instructor-only. If a
student has its code, find out how, because it did not come from the published
repository.
