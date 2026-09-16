# The acceptance procedure you agree before you test
## 145130 Applications of AI · Module 6 · Week 17, Thursday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W17_TheAcceptanceProcedure.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W17_TheAcceptanceProcedure.md --export pptx
```

**Competencies 2.12.1**, create a written procedure agreed by the stakeholders and
project team for determining the acceptability of the project deliverables,
**2.12.3**, develop test cases that are realistic, compare with expected
performance, and include targeted platforms and device types, and **1.2.13**,
identify stakeholders and solicit their opinions.

**This is the last new concept in the course.** Week 18 runs what you write today.

---

## Why this exists

At some point somebody decides whether the thing you built is finished. If nobody
wrote down what finished means, that decision is a conversation, and the person
with more authority wins it.

**An acceptance procedure is a written agreement about what finished means, made
before anybody has a reason to argue.** It protects both sides. It stops a
stakeholder inventing a new requirement in the last week, and it stops you handing
over something that does half of what they expected.

It is one exam item out of ninety-five. It is most of next week.

---

## The one idea

**A test case has a starting state, an action, and an observable result, and it can
fail.**

```
Given    what exists, what is running, what is in the folder
When     one action somebody performs
Then     one result somebody can see, that could have come out otherwise
```

**If two people can read the case and disagree about whether it passed, it is not a
case.** That is the entire test.

---

## Worked example 1 · two cases, one of which is not a test

```
AC-1  The program works correctly with normal input and gives the user
      helpful messages when something goes wrong.

AC-2  Given 8 notes in the inbox and nothing listening on port 5158,
      When the sweep is run once,
      Then it exits with a code that is not 0, and out/ holds an incident
      file whose text names the wire failure.
```

**AC-1 cannot fail.** "Correctly" and "helpful" are words the writer had a picture
for and did not write down. Two people will disagree about whether it passed and
there is no fact that settles it, so it will pass, always, because passing is less
awkward.

**AC-2 can fail**, and it failed twice during this module's own build.

**The three words that mean a case cannot fail:** *gracefully*, *properly*,
*correctly*. Every one of them is a placeholder for something the writer did not
finish thinking about.

---

## Worked example 2 · a procedure, in the shape you will write

Eight cases. Two of them are failure cases, and the failure cases are the point.

```
Acceptance procedure, note sweep automation

Platform: Windows 11, Python 3.13.7, no model runtime installed.
          Also to be run on a lab machine with Python 3.14 before sign-off.
Stakeholder: the person who runs the weekly export. Role, not name.

ID    Given                        When                 Then
AC-1  8 notes, service on 5158     run once             exit 0, digest has 8 rows
AC-2  the same 8 notes, nothing    run once again       exit not 0, incident file
      touched since AC-1                                names the freshness step
AC-3  8 notes, nothing listening   run once             exit not 0, incident names
      on 5158                                           the wire failure
AC-4  8 notes, service answers     run once             exit not 0, incident names
      200 with result null                               empty_result
AC-5  0 notes in the inbox         run once             exit not 0, incident says
                                                        the drop did not happen
AC-6  8 notes, service on 5158     run with --every 3   two sweeps happen with no
                                   --runs 2             further typing
AC-7  after AC-1 to AC-5           open the run log     one row per run, including
                                                        the failed ones
AC-8  after AC-1 to AC-5           search the run log   no note text and no name
                                   for note text        anywhere in it
```

**AC-8 is the one students do not think of and it is the one that matters most
here.** It is the program rule, written as a case somebody can run.

**AC-6 is the trigger**, and it needs `--runs` to exist so that a person checking
it does not have to wait a day or kill a process.

**The platform line is competency 2.12.3** and it is one line. It says where this
was run and where it still has to be run, which is the honest version of "targeted
platforms and device types" for a program like this.

---

## Worked example 3 · running it, and what a failure looks like

Real output, from the reference procedure in this module, on the build machine:

```
python run_acceptance.py --port 5160
```

```
Acceptance procedure, Module 6 reference automation
python     3.13.7

PASS  AC-1  a normal run exits 0 and every step reports   (exit 0, 5 steps reported)
PASS  AC-2  the digest holds one row for every note   (8 rows for 8 notes)
PASS  AC-3  every digest row says where its label came from   (8 of 8 rows marked)
PASS  AC-4  nothing changed since the last run, so the run fails   (exit 2, freshness named: True)
PASS  AC-5  the failed run wrote an incident naming what to check   (1 incident file(s))
PASS  AC-6  no service listening at all is a failure with a named kind   (exit 2)
PASS  AC-7  HTTP 200 with no result is caught, not counted as work   (exit 2, empty_result named: True)
PASS  AC-8  half the answers failing is DEGRADED, not OK and not FAILED   (exit 1)
PASS  AC-9  the run log has a row for every run, failures included   (5 rows, statuses ['DEGRADED', 'FAILED', 'OK'])
PASS  AC-10 no note text reaches any file the automation writes   (no note text in the run log)
PASS  AC-11 the scheduled trigger fires twice without anybody typing   (2 sweeps in one invocation)

11 of 11 cases passed in 28.0 s
```

**Nobody explained anything to anybody.** That is what finished means.

**Your procedure does not have to be a program.** A person with the table from
worked example 2 and a terminal can run all eight by hand in ten minutes, and that
is a complete acceptance procedure. **Automating it is worth doing when you will
run it more than three times**, which you will, because Week 18 runs it at least
twice.

### When a case fails

```
FAIL  AC-4  nothing changed since the last run, so the run fails   (exit 0)
```

**You write it down. You do not change the case.** The correction has three parts:

```
AC-4 failed. Exit code was 0 and no incident file appeared.
Changed:    added the freshness step, comparing the newest inbox file time
            against last_source_mtime in state/last_run.json.
Re-ran:     AC-4 now exits 2 and writes out/incident-r0006.md.   PASS
```

**A correction with no re-run under it is a plan, not a correction.**

---

## Agreeing it with a stakeholder

The word in the competency is **agreed**, and it is doing work. A procedure you
wrote and nobody read is not agreed.

### Who the stakeholder is

**Somebody who decides, pays, or owns the problem.** Not one of your five
participants acting as a user, although it can be the same person wearing a
different hat. For most teams here it is an adult in the building who agreed to
the role, or the person from the original brief.

**Identify them by role, never by name, in the document.** Personal data rule, and
it costs nothing.

### The conversation, in ten minutes

1. **Read them the cases.** Not the code, not a demonstration. The eight rows.
2. **Ask the one question:** "Is there anything on this list that would not
   convince you, or anything missing that would?"
3. **Write down what they change.** That is the deliverable.
4. **If they change nothing**, write that down too, with their role, so that it is
   a recorded outcome rather than a gap.

**The changes are the point.** A procedure nobody argued with is a procedure nobody
read. Expect a stakeholder to add one case and delete none, because people think of
things they care about and rarely think of things they do not.

### They are allowed to say no

At the end of Week 18 you ask them to accept. **A stakeholder can say no**, and a
no with a reason written down is a better deliverable than a yes with nothing
under it.

**Say that out loud to your partner before you go**, because the pressure to come
back with a yes is real and hiding a no is the failure this whole thing exists to
prevent.

---

## The wrong version, and what it produces

> "We showed our program to the front office and they said it looked great and they
> would definitely use it. Stakeholder acceptance: obtained."

**Nothing in that is acceptance.**

- **Nobody ran a case.** They watched a demonstration, which is the part you
  controlled.
- **"Looked great" is a compliment.** People are kind to students.
- **"Would definitely use it" is a prediction**, made by somebody with no reason to
  be careful about it.
- **There is a name in it** if you write the real one, which breaks the personal
  data rule for no benefit.

**What it produces:** a document that says the project succeeded, backed by
nothing, in a folder where every other document has evidence in it. It is the one
page a reader would not believe, and it damages the pages either side of it.

---

## Why the wrong version is tempting

**Because a demonstration is the thing you practised.** You know how to show your
program working. Handing somebody a table of eight cases and asking them to
disagree with it is a different and less comfortable skill.

**Because the compliment is real.** They did say it looked great, and they probably
meant it, and writing it down feels like recording something true. It is true and
it is not evidence.

**Because you are eight days from the end of the course** and a clean yes closes a
line on a checklist. **A recorded no closes the same line** and is worth the same
marks, and everybody is surprised by that until they read the rubric.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Acceptance procedure** | The written set of cases that define finished |
| **Test case** | Given, when, then. One action, one observable result |
| **Given** | The starting state |
| **Observable result** | Something two people would agree they saw |
| **Failure case** | A case where the thing is supposed to go wrong |
| **Targeted platform** | The machine and version a case was run on |
| **Correction** | The failed case, what changed, and the re-run |
| **Acceptance** | A stakeholder saying it does what you both agreed |
| **NOT RUN** | A recorded outcome. Not the same as a pass |

---

## Self-check

**1.** Rewrite this as a runnable case: "The system should handle large inputs
gracefully."

**2.** You are about to run AC-4 in front of your stakeholder and you realise it
will fail. Name your options and say which one you take.

**3.** Your stakeholder accepts, and one case is still failing. What do you write
down?

---

### Answers

**1.** Something like:

```
Given  an inbox holding 500 note files,
When   the sweep is run once,
Then   it finishes within 120 seconds, the digest holds 500 rows, and the
       run log records one row with a status.
```

The marks are for a number in the Given, a number in the Then, and an outcome that
could fail. **"Gracefully" is gone**, replaced by three things somebody can see.

**The extra mark is for choosing a limit you can defend.** Where does 120 seconds
come from. If the answer is that it sounded right, say so in the case: "120 s,
chosen as twice the time observed on 8 notes scaled up, not measured."

**2.** Three options, and only two of them are allowed.

- **Change the case so it passes.** **Not allowed.** This is the thing the whole
  procedure exists to prevent. A procedure you edit while running it measures
  nothing.
- **Run it, record FAIL, fix it in the next build.** **This is the answer.** It is
  what the case is for and your stakeholder is watching a procedure work rather
  than watching you fail.
- **Say out loud, before running it, that you think the case itself is wrong**, and
  agree with the stakeholder to record it NOT RUN with the reason. **Allowed, and
  only when the case describes something you never agreed to build.** The decision
  belongs to both of you and it happens in the open.

**Take the second one.** Between one and four failures on a first run is normal.
Eight passes usually means the cases were written to pass.

**3.** **You write down that they accepted with a known failure, which case it is,
and what you both agreed happens about it.**

```
Stakeholder decision: accepted, with AC-5 outstanding.
AC-5 (empty inbox) still exits 0 rather than writing an incident.
Agreed: the digest is usable and the empty-inbox case has not happened in
the four weeks the export has been running. Recorded as known, not fixed.
Owner: the team. Would be the first thing fixed if this continued.
```

**This is a completely normal outcome in real work and it is a full-marks
deliverable.** What is not full marks is an acceptance record that says everything
passed when one thing did not, because the next person reads AC-5 as passing and
builds on it.
