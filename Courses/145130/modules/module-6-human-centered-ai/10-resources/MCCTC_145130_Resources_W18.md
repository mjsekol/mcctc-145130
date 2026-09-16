# Additional Resources · Week 18
## 145130 Applications of AI · Module 6 · Week 18
### Topics: running an acceptance procedure, corrections, the demonstration, the WebXam post-test, the end of the course

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has
not been confirmed live from the build machine.

**No new content this week.** Everything here is either something you are about to
run, something you are about to be assessed on, or something for next semester.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The three sheets in Lab M06-04 | Mon | On-level | 10 min |
| 2 | The reference acceptance record and corrections | Mon-Tue | On-level | 20 min |
| 3 | Interactive: `run_acceptance.py`, watched rather than read | Mon | Extension | 10 min |
| 4 | The demonstration script and checklist in the project spec | Thu-Fri | On-level | 15 min |
| 5 | Your own exit criteria checklist | Mon | On-level | 15 min |
| 6 | Every lecture note in this module, for the exit assessment | Wed | Review | 90 min |
| 7 | The module exit criteria and the three module READMEs before this one | Wed | Review | 30 min |
| 8 | The WebXam blueprint weights, so you revise the right things | Thu | On-level | 10 min |
| 9 | Official docs: Python `unittest` | Mon | Extension | 20 min |
| 10 | 145010 Web Design, what you are walking into | Fri | Extension | 20 min |
| 11 | The BPA event list this module feeds | Fri | Extension | 15 min |
| 12 | The thank-you note, and it is not optional | Fri | On-level | 10 min |

---

## 1. The primary reading, and it is three sheets

`05-labs/lab-m06-04-files/` · **Confident.**

`acceptance-run-sheet.md`, `corrections-sheet.md`, and
`acceptance-record-template.md`.

**Read the top of the run sheet before Monday.** There is a paragraph you read out
loud to your stakeholder, and it says three things: some cases are meant to fail, a
surprise failure gets written down rather than fixed in front of them, and anything
that does not make sense to them is a finding about your writing.

**Then read the three honesty boxes at the bottom.** They are the whole of Monday.

**Time.** 10 minutes. **Level.** On-level, and required.

---

## 2. The reference acceptance record and corrections

`09-project/reference-implementation/acceptance/` · **Confident.**

**Read `corrections.md` first.** It has the real before-and-after capture, including
a traceback, for a case that failed on its first run. **The before version did not
crash because it was missing a check. It crashed because it was missing a
judgement**, four steps away from the cause.

**Then read section 5 of `acceptance-record.md`, "Known and not fixed".** Three
entries. **A record with something in that section is an honest record, not a weak
one**, and yours should have one.

**Time.** 20 minutes. **Level.** On-level.

---

## 3. Interactive: watch a procedure run

`09-project/reference-implementation/acceptance/run_acceptance.py` ·
**instructor-only until Wednesday.**

**Ask your instructor to run it in front of you on Monday.**

```
python run_acceptance.py --port 5160
```

```
11 of 11 cases passed in 28.0 s
```

**The point is not the eleven passes.** It is that nobody explained anything to
anybody. That is what finished means, and it is the definition your implementation
plan is supposed to be using.

**Time.** 10 minutes. **Level.** Extension.

---

## 4. The demonstration script

`09-project/MCCTC_145130_Project_M06_InFrontOfRealPeople.md`, the five-minute
script and the ten-point checklist · **Confident.**

**Read the checklist and count the points.** A working run is worth two. **The
change you made and the question at the end are worth four between them.**

**Rehearse item 4 out loud with your partner, twice.** Breaking your automation live
is the part people fumble, because you have to make it fail in a way that raises no
exception while somebody is watching a clock.

**Item 6 is worth zero and is not optional.** A demonstration that skips it is
stopped and asked for it.

**Time.** 15 minutes. **Level.** On-level.

---

## 5. Your own exit criteria checklist

`10-resources/MCCTC_145130_ExitCriteria_M06.md` · **Confident.**

**Do this Monday, not Thursday.** A box you cannot tick on Monday is a conversation.
The same box on Thursday is a score.

**Time.** 15 minutes. **Level.** On-level.

---

## 6. Everything, for Wednesday

`03-lecture-notes/`, all eight · **Confident.**

The exit assessment covers Weeks 16 and 17 and nothing from this week.

**Revise in this order**, which is roughly the order of the marks:

1. `FromWhatHappenedToWhatItMeans` and `WhatTheyDidAndWhatTheySaid`. Nine of the
   twenty-five items come from these two.
2. `AnAutomationWithARealErrorPath`. Four items, and three of them are code.
3. `TheWireframeThatAnswersAQuestion`, the media element table specifically. Three
   items.
4. `TheAcceptanceProcedure`. Four items across all three parts.
5. `WhereItIsWorthApplyingAI`, `ATaskNotAnOpinion`, `TheTabletopAndTheFivePeople`.

**Do the self-checks.** Every note has three questions with answers, and twelve of
the twenty-four are close to an item on the paper.

**Time.** 90 minutes total. **Level.** Review.

---

## 7. The other five modules

`Courses/145130/modules/*/README.md` · **Confident.**

**Why on the last week.** The WebXam post-test on Thursday covers the whole course,
not this module. Each module README has a competency table saying what it claimed
and where it was assessed, which is a faster revision map than any set of notes.

**Time.** 30 minutes. **Level.** Review.

---

## 8. What the WebXam actually weights

`Courses/145130/_source/COMPETENCY_REFERENCE.md`, the blueprint table ·
**Confident.**

**Read the first table and nothing else.** Ninety-five items.

**Outcome 2.14, Artificial Intelligence, is 22.11 percent on its own**, which is
Modules 1, 2, 3 and one competency from this one. **Law, licensing, ethics and
privacy together come to about 21 percent**, which is Module 3.

**Programming is 6.32 percent of the exam.** Say that out loud to yourself before
Thursday and revise accordingly, and then remember what your instructor has been
saying all year: being able to evaluate an AI output is not a job, and having
shipped an AI-integrated application is.

**Time.** 10 minutes. **Level.** On-level, and it is the highest-value ten minutes
of revision available.

---

## 9. Official documentation, for the acceptance run

`https://docs.python.org/3/library/unittest.html` · **Confident.**

**Why a testing page in a week with no new content.** Because of one sentence in the
acceptance procedure: finished is a command somebody else runs that says pass or
fail without anybody explaining anything.

**Read three things:** how a test case is written, what `assertEqual` and
`assertRaises` do, and how to run a folder of tests from the command line.

**The question to answer:** what is the difference between a test that fails and a
test that errors, and why does the runner report them separately? **That is the
same distinction as a recorded FAIL against an unhandled traceback**, which is in
the reference corrections file.

**Time.** 20 minutes. **Level.** Extension.

---

## 10. What you are walking into next semester

`Courses/145010/` · **Confident**, it is in this repository.

**Why on Friday.** You start Web Design and then a twelve-week capstone for a real
client. **The capstone client is a person with opinions and behaviour, and those
two will disagree**, which is the whole of this module.

**The one thing to carry over:** the capstone has a stakeholder from day one. Write
their role down in week one and write down what finished means to them before you
build anything.

**Time.** 20 minutes. **Level.** Extension.

---

## 11. Where this module goes at BPA

`Courses/145130/CLAUDE.md`, the BPA alignment section · **Confident.**

**455 UX Design Team** is the direct fit: your study, your wireframes, your
re-test, and your change record are four of the pieces.

**V16 Virtual Artificial Intelligence Team** is the other one: the automation and
the opportunity analysis.

**Confirm this year's event names and deadlines with your instructor**, because they
change and nothing in this repository carries a date.

**Time.** 15 minutes. **Level.** Extension. Graded under BPA / Credential /
Capstone.

---

## 12. The thank-you note

**No link. Ten minutes and a piece of paper.**

Five people outside this class gave you fifteen minutes each and let you watch them
struggle. **The note goes out before the last day**, it names nothing about them,
and it says one specific thing you changed because of what they did.

**"We moved the category list to the top because three people never scrolled to
it"** is worth more to a person than any amount of thanks, because it tells them
their fifteen minutes did something.

**Your instructor reads them before they go.** That is not a trust problem, it is
the same rule as everything else this module: somebody checks before it leaves the
room.

**Time.** 10 minutes. **Level.** On-level, and it is part of the Polish score.
