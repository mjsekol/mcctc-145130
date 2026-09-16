# Performance Task · In Front of Real People
## 145130 Applications of AI · Module 6 · Weeks 16-18

**100 points. Projects category, 35 percent of your grade.**
**Due Week 18, Wednesday, at the end of Build 2.**

---

## The brief

> From: the person who runs the front office
>
> You showed me your program a few weeks ago and I said it looked great, and I
> meant it. Then on the Monday I sat down to use it on the actual pile and I could
> not work out how to start it. I did not tell you because you had presented
> it to a room an hour before and it seemed like a strange thing to bring up.
>
> I got there eventually. What I want to say is that I do not think you know what
> it is like to use your thing without you sitting next to me, and I do not think
> you can find that out by asking me, because I will be polite about it.
>
> The other half is this. Sorting these notes is twenty minutes of my Monday, every
> Monday, and it is the same twenty minutes every time. If your program can do it
> while I am not here, that is worth more to me than anything else you could build.
> But it has to tell me when it has not worked. I have had things run overnight
> before and produce a file that looked fine and was last week's.
>
> And I want to know what else around here is like that, because if this works I
> would like to know what is next and roughly what it is worth.

**That is the whole brief.** It does not say who you should watch, what you should
change, what you should automate, or how to work out what anything is worth.

**Extracting four deliverables from that is the first thing you are graded on.**

---

## What you are building

Four things, and one of them is not a program.

| # | Deliverable | Due |
|---|---|---|
| 1 | **A usability study** of your Module 5 application, with five people who are not in this class | Week 17, Mon |
| 2 | **A revised interface**, wireframed from what testing found and re-tested | Week 17, Wed |
| 3 | **A working automation**: a scheduled trigger, four or more steps, and a real error path | Week 17, Fri |
| 4 | **An opportunity analysis**: one industry, three workflows, an estimate you can defend | Week 17, Wed |

Plus, in Week 18: **an acceptance procedure agreed with a stakeholder, run, corrected, and signed.**

---

## The rules for working with real people

**These are not advice. They are the conditions under which this work happens
here, and breaking one stops the work rather than costing marks.**

**1. They say yes out loud**, after you read the consent line as written. If they
hesitate, the answer is no, and you thank them.

**2. No recording of any kind.** No video, no audio, no screen capture, no
photograph. You write on paper.

**3. No personal data leaves the session.** Participants are P1 through P5. Not
their name, their class, their year, their job, or anything that would let somebody
in this building work out who they were.

**4. No classmates as participants for the formal study.** They know what your
program does and they know what you want to hear. **Classmates are for the
rehearsal and the tabletop**, which are different things and are labelled as such.

**5. Nothing from a session goes into an AI tool.** Not the notes, not the quotes,
not a summary of either.

**6. You thank them, in writing, before the last day of the course.** Five people
gave you their time. It costs four minutes.

---

## Technical requirements

| # | Requirement | Why |
|---|---|---|
| R1 | Five sessions, five people, none of them in this class. | A classmate's session is evidence about a different question. |
| R2 | Every finding cites a session record by number and line. | A finding nobody can trace is not a finding. |
| R3 | **No percentages anywhere in the study.** Counts out of five. | A reader who sees a percentage assumes a survey of a population. You do not have one. |
| R4 | Every design change carries four lines: the observation, the change, the prediction, and how you will know. | A change with no observation above it is a preference. |
| R5 | A preferences list, holding everything you wanted to change and could not justify. | Preferences are allowed. Preferences described as evidence are not. |
| R6 | The revised interface is re-tested with **two people, at least one from outside the class**. | A prediction you never check is a decoration. |
| R7 | The automation has a **scheduled trigger**, at least **four named steps**, and an error path **that raises no exception**. | An automation runs when nobody is watching. |
| R8 | Every step declares what it expected and reports what it got, and the run status comes from comparing them. | Not from whether anything raised. |
| R9 | A failed run writes a record and something a person can act on, with four sections. | An incident nobody can act on is a log line. |
| R10 | **No note text, message text, or person's name reaches any file your automation writes.** | Program rule, and it is an acceptance case. |
| R11 | Every estimate shows its multiplication and states its assumption. | An estimate without arithmetic is a claim. |
| R12 | **No market size, adoption rate, or vendor claim anywhere.** Hours, never money. | You cannot check any of them, and money needs a rate that is not yours to ask for. |
| R13 | Every program takes an explicit `--port` or `--service`. No defaults. | A program that reaches the wrong server does not fail. It answers. |
| R14 | Everything runs locally. No commercial AI developer API. | Those services require their users to be 18 or older. |
| R15 | Every period ends with a commit. | Version control is a daily ritual. |

---

## Required repository structure

```
your-project/
  README.md                       what it is, how to run it, what is not finished
  decision-log.md                 written on the day, dated by week and day
  study/
    participant-script.md         the consent line unchanged, your tasks
    tabletop-record.md            what broke, the fixes, and Found nothing in
    sessions/session-P1.md ...    five records, two columns, numbered lines
    usability-report.md           findings with severity, count, and evidence
  design/
    wireframe-v1.md               what it looked like when it was tested
    wireframe-v2.md               what it looks like now
    change-record.md              four lines per change, plus preferences
  automation/
    <your program>
    run-book.md                   how to start it, the trigger, the steps, failure
    evidence/                     captured runs, including the failures
  analysis/
    opportunity-analysis.md       one industry, three workflows, the estimates
  acceptance/
    acceptance-procedure.md       platform, stakeholder, eight cases
    corrections.md                the case, the change, the re-run
    acceptance-record.md          results, corrections, the decision
```

**Check the shape with the tool.**

```
python deliverables_check.py your-project
python deliverables_check.py --list
```

It is in `09-project/project-files/`. It tells you what is missing, what is too
short, and it warns you about four specific things: findings with no citation, a
percentage in your report, a change record missing the four lines, and a market
figure in your analysis. **It cannot tell you whether anything you wrote is true.**

---

## DMAIC checkpoints

### Define · Week 16, Monday and Tuesday

Work out what you are studying and who for. Not "the program." A specific thing a
specific person does.

**Checkpoint, Monday end of Build 2:** `study/README.md` or `decision-log.md` with
your study goal in one sentence, and a list of five candidate participants with a
time each is free. **Names on your own paper, not in any file.**

### Measure · Week 16, Wednesday to Week 17, Monday

Run the sessions. Watch, write two columns, say nothing.

**Checkpoint, Week 16 Wednesday:** M1. **Week 16 Friday:** M2, at least three
records committed.

### Analyze · Week 17, Monday

Turn the records into findings with a severity, a count, and a decision each.

**Checkpoint, Monday end of Build 1:** M3, the usability report.

### Improve · Week 17, Tuesday to Friday

Build. **This is where the Agile ceremonies live**: a written stand-up every day,
one milestone at a time, and a demonstration at the end.

**Checkpoints:** M4 Wednesday, M6 Wednesday, M7 Thursday, M5 Friday.

### Control · Week 18

Prove it stays working, in front of the person who agreed what working means.

**Checkpoint, Week 18 Monday:** the acceptance run. **Tuesday:** the signed record.
**Wednesday:** everything committed.

---

## Milestones

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | The study is designed and piloted | Week 16 Wed, end of Build 2 | script with the consent line unchanged, four tasks, five names with times, and a tabletop record with fixes and a Found-nothing line |
| M2 | Three sessions recorded | Week 16 Fri, end of Build 2 | three records with two columns, times, and P-identifiers |
| M3 | The usability report | Week 17 Mon, end of Build 1 | every finding cites a record by number and line, every row has a severity and a count, and there is no percentage anywhere |
| M4 | The revised interface, re-tested | Week 17 Wed, end of block | three changes with four lines each, a preferences list, and a re-test with two people including at least one from outside the class |
| M5 | The automation | Week 17 Fri, end of Build 2 | the checker runs, the error path is produced on purpose and captured, and a failed run writes something a person can act on |
| M6 | The opportunity analysis | Week 17 Wed, end of Build 2 | three workflows, three estimates with arithmetic, and a did-not-measure section with at least three entries |
| M7 | The acceptance procedure, agreed | Week 17 Thu, end of Build 2 | eight cases including two failure cases, a platform line, a stakeholder role, and a record of what they changed |
| **Due** | **Everything** | **Week 18 Wed, end of Build 2** | the last commit pushed inside the window is the submission |

---

## Three worked scope examples

**All three would earn full marks.** They differ in ambition, not in quality.

### Small, and completely finished

**Study:** three tasks, five people, on the output of your Module 5 application.
**Changes:** two, one line each. **Automation:** four steps, a schedule, and one
error path. **Analysis:** three workflows in an industry a family member works in.

**What makes it full marks:** every finding traceable, both changes re-tested, the
error path produced on purpose and captured, and a did-not-measure section in every
document that has one.

**Why somebody chooses it:** a two-person team where one partner is out for two
days. This scope survives that.

**The risk:** finishing the study on Friday of Week 16 and spending Week 17
polishing the report. **Do not.** The marks in Week 17 are in the automation and
the analysis.

### Medium, and the one most teams should aim for

**Everything above, plus:** four tasks rather than three, and an automation with
five steps and **two** error paths, one of which is the stale source.

**What it adds:** the second error path is where the learning is. The first one is
a pattern you follow. The second one you have to find, by asking what could go
wrong that would raise nothing.

**Why somebody chooses it:** both partners are here all three weeks and the Module
5 application runs.

**The risk:** the fifth participant. Every medium team that falls short falls short
there, and the answer is on Monday of Week 16 and not on Thursday.

### Large, and only with a running Module 5 application on day one

**Everything above, plus** an automation that runs against the student's **own**
Module 5 service rather than the bundled stub, and an opportunity analysis with a
fourth workflow that the team proposes rather than observes.

**What it adds:** a real integration, and a section of the analysis that is
explicitly a proposal rather than a measurement, labelled as one.

**The risk, and it is real:** your own service becomes the project. Every hour spent
making the service work is an hour not spent on the study, and **the study is worth
more of this rubric than the automation is.** Your cut list puts the own-service
integration first.

### Scope calibration, three signals

| If your team | Aim for |
|---|---|
| has a partner out for two or more days, or a Module 5 application that does not currently start | **Small** |
| has both partners present, a running application, and three participants confirmed by Wednesday of Week 16 | **Medium** |
| had five participants confirmed on Monday of Week 16 and a service that runs on both machines | **Large** |

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

**Functionality, 25.** The automation runs on a schedule without you typing
anything. It has four or more named steps. It produces a status that distinguishes
working from not working. **Its error path is produced on purpose and captured**,
and it raises no exception. A failed run writes something a person can act on.

**Code Quality, 20.** Scored on the five-dimension standard: Correctness, Security,
Readability, Performance, Requirements Fit. **Security here is R10**, and it is
checked by searching your run log for a phrase from a note. No credential anywhere.
Every command passes a port.

**Documentation, 20.** The study, the change record, the run book, the analysis, and
the acceptance record. `deliverables_check.py` passing is the floor. **The graded
part is the four sections most people leave empty:** what you did not measure, the
preferences list, the did-not-measure section in the analysis, and known-and-not-fixed
in the acceptance record.

**Process, 15.** A commit at the end of every period. A stand-up row for every day.
A decision log with real decisions in it, dated by week and day. Five sessions
recorded on the day they happened. **A tabletop record that found something.**

**Demonstration, 10.** The five-minute script below, or a desk demo on the same
checklist. Including the spoken question at the end.

**Polish, 10.** The revised interface is readable by the person in the brief, not by
you. The README says what is not finished. Nothing in the repository is left over
from a lab. **The thank-you notes are written and sent.**

---

## The five-minute demonstration script

Five minutes. Timed. You will be stopped.

| Minutes | What |
|---|---|
| 0:00 to 0:30 | **The problem, in the client's words, not yours.** What did the front office actually say. |
| 0:30 to 1:30 | **One thing a participant did that surprised you.** With the session number and the time on task. Not a quote. |
| 1:30 to 2:15 | **The change you made because of it**, with the four lines, and what the re-test showed. Including a prediction that did not hold, if you have one. |
| 2:15 to 3:15 | **Run the automation, then break it live.** Make it fail in a way that raises no exception, and read the incident file out loud. |
| 3:15 to 4:00 | **One number from your opportunity analysis**, with the multiplication and the assumption said out loud. |
| 4:00 to 4:30 | **One thing you did not measure**, and what you would do about it with another week. |
| 4:30 to 5:00 | **The question.** |

### The question

Every demonstration ends with the same question, asked of **one named person on the
team, without notes**:

> What did you change because a user struggled, and how do you know it was because
> they struggled?

**The count, the session, the change, and the re-test.** Four things, one sentence
each, no adjectives. This is an exit criterion for the module and it cannot be
assessed on paper.

### The ten-point demonstration checklist

| # | | Points |
|---|---|---|
| 1 | The problem stated in the client's terms | 1 |
| 2 | One participant behaviour, with a session number and a time | 2 |
| 3 | The change, with its four lines, and the re-test result | 2 |
| 4 | The automation failing live, with no exception, and the incident read out | 2 |
| 5 | One estimate with the arithmetic and the assumption said out loud | 1 |
| 6 | One thing not measured | 0 |
| 7 | The question, answered without notes | 2 |
| | **Total** | **10** |

**Item 6 is worth zero on purpose and it is not optional.** A demonstration that
skips it is stopped and asked for it. The points are elsewhere; the habit is the
point.

---

## Submission checklist

- [ ] Five session records, P1 to P5, none of them a classmate
- [ ] The consent line unchanged in `study/participant-script.md`
- [ ] No name, class, year, or job anywhere in any file
- [ ] Every finding cites a record by number and line
- [ ] **No percentage anywhere in the study**
- [ ] Three changes with four lines each, and a preferences list
- [ ] A re-test with two people, at least one from outside the class
- [ ] The automation runs on a schedule and has four or more named steps
- [ ] A captured failure that raised no exception, in `automation/evidence/`
- [ ] **Searching your run log for a phrase from a note returns nothing**
- [ ] Three estimates with arithmetic and an assumption each
- [ ] **No market size, adoption rate, or vendor claim anywhere**
- [ ] `python deliverables_check.py your-project` reports everything complete
- [ ] The acceptance record, with the stakeholder's decision in their own words
- [ ] Thank-you notes written to all five participants
- [ ] `README.md` says what is not finished
- [ ] Committed and pushed inside the Week 18 Wednesday window

---

## Exit criteria for this module

You can self-check against these. They are the three the module is built to
produce.

- [ ] I can run a usability test without leading the participant.
- [ ] I changed my own design because a user struggled, not because I preferred it.
- [ ] I can identify a workflow worth automating and say why it is worth the effort.

The full checklist is in `10-resources/MCCTC_145130_ExitCriteria_M06.md`.

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`. It is
**instructor-only**. It is a complete worked submission about the note sweep from
Lab M06-03, which is a program no student built, so a student who copies it is
handing in research about somebody else's system.

**Verified on the build machine:** `python run_acceptance.py --port 5160` reports
`11 of 11 cases passed in 28.0 s`. `python deliverables_check.py
reference-implementation` reports everything complete with zero warnings.

## The three ways this project goes wrong, and the intervention

**1. The team does not have five participants.** By far the most common, and it is
visible on Friday of Week 16 if you ask out loud and write the numbers where
everybody can see them.

**The intervention, on Friday of Week 16 and not later:** hand them one of the four
adults on your backup list, in person, with a time. **A team at zero on Friday is a
team that will hand in three sessions**, and the difference between Friday and
Wednesday is the difference between a full study and an excuse.

**2. The redesign fixes something nobody touched.** You see it Monday of Week 17,
in a change record where the observation line says "we noticed" or is blank.

**The intervention:** ask for the session number. If there is not one, the change is
not forbidden, it moves to the preferences list, in writing, and it is scored as a
preference. **Say that calmly.** A redesign of preferences is not a failing project.
A redesign of preferences described as evidence-driven is.

**3. The automation is a script with a try block round it.** You see it Tuesday of
Week 17, about twenty minutes into the lab.

**The intervention:** ask what exception the starter raised during the
demonstration. None. Then ask what their program does when the service answers 200
with nothing in it, and have them run it.

## What to say to a team whose scope is too big

> Show me your cut list. Which of the things you are building is first on it?

Then: "Cut it now, on a Tuesday, while it is a decision. On Wednesday of Week 18 it
is a panic and you will cut the study, which is worth more of the rubric than
anything you are protecting."

If they have no cut list, that is the conversation instead, and it is a better one.

## What to say to a team whose scope is too small

Do not tell them to add a feature. Ask this:

> Make your automation fail in a way that raises no exception, and show me what the
> person reading the incident file would do next.

A small project with a real error path and an honest study is a full-marks project.
A large one where everything works only when everything works is not.

## The grading question you will be asked

**"Does a study with four participants fail?"**

**No.** A study with four participants, a note saying they could not get a fifth,
and everything else done properly is a strong submission. **A study with five
participants where one is a teammate is not**, because one of those is true and the
other is not.

**Say that to the class in Week 16**, before anybody is short, so that nobody is
choosing between an honest four and a dishonest five in a panic on a Sunday.
