# Exit Criteria Checklist · Module 6 · Human-Centered AI & Automation
## 145130 Applications of AI · Weeks 16-18

**Self-check.** Nobody collects this. It is the list you hold your own work against
before the demonstration, and the three headings are the syllabus wording.

**Tick something only when you could do it in front of somebody, today, without
looking anything up.**

**Do this on Monday of Week 18, not on Thursday.** A box you cannot tick on Monday
is a conversation. The same box on Thursday is a score.

---

## 1 · Run a usability test without leading the participant

- [ ] I can say the consent line from memory, including the sentence about
      recording and the sentence about stopping.
- [ ] I can name the **four things I may not say** and give an example of each.
- [ ] I have sat through **twenty seconds of silence** while somebody went the wrong
      way, and not helped.
- [ ] My tasks give a goal and a reason and **name no control, no file, and no
      flag.**
- [ ] I ran a **tabletop** before I spent a real participant, and it found
      something.
- [ ] My five participants are five people **who are not in this class**, and I can
      say how I found each of them.
- [ ] Nothing in any of my files names a participant, their class, their year, or
      their job.
- [ ] **Nothing from any session has gone into an AI tool.** Not the notes, not a
      summary.
- [ ] I can point at a line in one of my records where **what they did and what they
      said disagree.**

**The test.** Somebody watches you run a session with a person they brought, and
never hears you supply a single piece of knowledge.

---

## 2 · Change your own design because a user struggled, not because you preferred it

- [ ] Every change in my change record has **four lines**: the observation, the
      change, the prediction, and how I will know.
- [ ] Every observation line cites a **session record by number and line**.
- [ ] I have a **preferences list**, and it is not empty.
- [ ] I can name one change I wanted to make and moved to that list, and say what
      observation would have justified it.
- [ ] I **re-tested** with two people, at least one from outside this class.
- [ ] I can say what my prediction was and whether it held. **If one did not hold, I
      wrote down why rather than reverting quietly.**
- [ ] There is **no percentage anywhere** in my study. Counts out of five.
- [ ] Every finding has a **severity and a count**, and I can say why the top one is
      top when it does not have the highest count.
- [ ] Every finding has a **decision**: fix, defer with a reason, or reject with a
      reason.
- [ ] I chose a **media element** for at least one change and I can say what it
      cost.

**The test.** Somebody points at any change in your revised interface and asks
which participant caused it. You answer with a number and a line, in under ten
seconds.

---

## 3 · Identify a workflow worth automating and say why it is worth the effort

- [ ] My automation has a **scheduled trigger** that fires more than once without
      anybody typing.
- [ ] It has **four or more named steps**, and each one says what it expected and
      what it got.
- [ ] It has an **error path that raises no exception**, and I produced it on
      purpose and captured it.
- [ ] I can name the **two counts** that catch a step that did nothing.
- [ ] A failed run writes something a person can act on, with **four sections**:
      what was expected, what to check first, who to ask, and what happens if
      nobody does.
- [ ] My run log has a row for **every** run, including the failed ones.
- [ ] **No note text and no name is in any file my automation writes**, and I have
      checked by searching for a phrase from a note.
- [ ] Every estimate in my analysis shows its **multiplication** and states the
      **assumption** underneath.
- [ ] I can say what each number becomes if its assumption is wrong.
- [ ] There is **no market size, adoption rate, or vendor claim anywhere** in my
      analysis, and every number is in hours rather than money.
- [ ] My analysis has a **did-not-measure section** with at least three real
      entries.

**The test.** Somebody stops your service without telling you, at half past seven in
the morning, and the first thing you know about it is a file that tells you what to
check and who to ask.

---

## The Week 18 half, which is assessed separately

- [ ] My acceptance procedure has **eight cases, two of them failure cases**, and a
      **platform line** saying where it ran and where it still has to.
- [ ] Every case has a **Given, a When, and a Then**, and I can say for two of them
      how they could fail.
- [ ] None of my cases contains the words **gracefully, properly, or correctly.**
- [ ] A **stakeholder** agreed it, identified by role and never by name, and I wrote
      down what they changed.
- [ ] I ran it **without editing a case that was about to fail.**
- [ ] Every verdict has evidence: an exit code, a file name, a line of output, or a
      count. **Not "it worked".**
- [ ] Every correction has **three parts**: the case, the change, and the re-run.
- [ ] I **re-ran the whole procedure** after the last correction, not only the case
      I fixed.
- [ ] My record has a **known and not fixed** section, and I am not embarrassed by
      it.
- [ ] I asked for acceptance and recorded the answer **in their words**, including
      if it was a no.

---

## The documents

The three criteria above are what the module is for. These are what proves it.

- [ ] `study/participant-script.md`, consent line unchanged, one page
- [ ] `study/tabletop-record.md`, with fixes and a **Found nothing in** line
- [ ] `study/sessions/session-P1.md` through `P5`, two columns, times, numbered
- [ ] `study/usability-report.md`, with **What I did not measure**
- [ ] `design/wireframe-v1.md` and `design/wireframe-v2.md`
- [ ] `design/change-record.md`, four lines per change, plus the preferences list
- [ ] `automation/run-book.md`, four sections
- [ ] `automation/evidence/`, captured runs including the failures
- [ ] `analysis/opportunity-analysis.md`, three workflows, arithmetic, assumptions
- [ ] `acceptance/acceptance-procedure.md`, `corrections.md`, `acceptance-record.md`
- [ ] `decision-log.md`, written on the day, dated by week and day
- [ ] `README.md`, saying what is not finished

```
python deliverables_check.py your-project
```

**Passing that is the floor, not the grade.** It checks that sections exist and have
words in them, and it warns you about four specific things. **It cannot tell whether
anything you wrote is true.** A person does that: your partner, your stakeholder,
and your instructor.

---

## Things that are not on this list, on purpose

**How many participants liked it.** Nobody was asked and nobody should have been.

**How good your model's answers are.** You are running a small model on shared
hardware, or no model at all. **The quality of what it writes is not what this
module measures.**

**How many features your revised interface has.** Two changes you can defend beat
six you cannot. The rubric is written that way deliberately.

**Whether your automation is impressive.** Four steps with a real error path scores
higher than nine steps that only work when everything works.

---

## If you cannot tick something

| What you cannot tick | Go to |
|---|---|
| Anything in section 1 | `03-lecture-notes/MCCTC_145130_Notes_WhatTheyDidAndWhatTheySaid.md` and `MCCTC_145130_Notes_ATaskNotAnOpinion.md` |
| Anything in section 2, first half | `MCCTC_145130_Notes_FromWhatHappenedToWhatItMeans.md`, then Lab M06-02 |
| Anything in section 2, second half | `MCCTC_145130_Notes_TheWireframeThatAnswersAQuestion.md` |
| Anything in section 3, first half | `MCCTC_145130_Notes_AnAutomationWithARealErrorPath.md`, then Lab M06-03 |
| The estimates | `MCCTC_145130_Notes_WhereItIsWorthApplyingAI.md` |
| The Week 18 half | `MCCTC_145130_Notes_TheAcceptanceProcedure.md`, then Lab M06-04 |
| The tabletop | `MCCTC_145130_Notes_TheTabletopAndTheFivePeople.md` |

**Tell somebody before the demonstration rather than after it.** That sentence is
in the Module 5 checklist too, and it was true then.
