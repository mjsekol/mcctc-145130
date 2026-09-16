# From what happened to what it means
## 145130 Applications of AI · Module 6 · Week 16, Thursday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W16_FromWhatHappenedToWhatItMeans.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W16_FromWhatHappenedToWhatItMeans.md --export pptx
```

**Competencies 2.15.2**, conduct and **analyze** research with the end user in
mind, and **1.8.4**, identify alternative actions when goals are not met.

---

## Why this exists

You have five sheets of paper with two columns on each. That is not a result. It
is raw material, and the step between it and a result is where most usability work
goes wrong.

It goes wrong in one specific way: **somebody writes a conclusion that their own
evidence does not support, in a confident voice, and nobody notices** because the
evidence is on a different page.

This lesson is one hour long and it is the most transferable hour in the module.
The same failure is the whole of Gate 2 this week, it is on the exit assessment,
and it is the reason Module 2 spent three weeks on evaluating AI output.

---

## The one idea

**A finding is an observation with a location, a severity, and a count. A
conclusion is a sentence that is supported by findings or it is an opinion in a
confident voice.**

You can check any conclusion in one move: **point at the observations under it.**
If you cannot point, it is not a conclusion.

---

## Worked example 1 · the sentence that does not follow

From a report, and the sessions it was written from.

**The report says:**

> Four of the five participants said the category labels were clear. 60 percent of
> users find the labels clear, so no change is needed.

**The sessions say:**

```
P1  chose "network" for a printer note       9 s    "seems clear"
P2  chose "network" for a printer note       4 s    "yeah, fine"
P3  asked what "other" meant, then chose it  --     "mostly clear"
P4  chose "hardware" for a printer note      3 s    "clear"
P5  chose "network" for a printer note      12 s    "it's alright"
```

**Two problems, and the second is worse.**

**The conclusion contradicts the behaviour.** Three of five chose the same wrong
label, quickly and confidently. The sentence is supported by what they said and
contradicted by what they did, and what they did wins.

**The percentage claims something five people cannot support.** Four of five
written as 60 percent of "users" says something about a population that was never
sampled. **A reader who sees a percentage assumes a survey.** Write counts. Always.

**The honest version:**

> Four of the five people I watched said the labels were clear. Three of those
> five chose "network" for a printer note, each in under twelve seconds. The
> labels are not clear, and the participants did not know it. Changing the labels
> is finding 1.

---

## Worked example 2 · the findings table

Every row carries four things. This is the shape you commit.

```
#  Finding                            Sev      Count  Evidence
1  Printer notes get "network".       Blocker  3/5    P1 L6, P2 L4, P5 L9
   Participants were confident and
   fast, so nobody self-corrected.
2  Nobody can start the program       Major    4/5    P1 L2, P2 L3-5,
   without a second attempt.                          P3 L2, P5 L2
3  "other" has no meaning anybody     Major    2/5    P3 L7, P4 L11
   could state.
4  The summary is above the           Minor    1/5    P2 L12
   category list, so the list is
   read second.
```

**Severity, and it is about consequence, not about annoyance:**

| Severity | What it means |
|---|---|
| **Blocker** | Somebody could not finish, or finished with a wrong answer and believed it |
| **Major** | Somebody finished, and it cost them attempts, time, or a detour |
| **Minor** | Somebody noticed it and it cost them nothing |

**Finding 1 is a blocker even though everybody finished.** They finished with the
wrong answer and did not know. **That is worse than failing**, because a person who
fails asks somebody. A person who is confidently wrong writes it down.

**Count and severity are separate and you rank by both.** Finding 4 has a count of
1 and is still a real finding. It goes at the bottom, and it stays on the list.

---

## Worked example 3 · turning the table into decisions

You have four findings and one Build 2. This is competency 1.8.4: what you do when
you cannot meet the goal you set.

```
#  Finding            Sev      Count  Decision
1  wrong label        Blocker  3/5    FIX this week. Wireframe change 1.
2  cannot start       Major    4/5    FIX this week. Wireframe change 2.
3  "other" unclear    Major    2/5    DEFER. Same fix as 1, probably.
                                      Re-test after change 1 before
                                      spending time on it.
4  summary first      Minor    1/5    REJECT for now. One participant,
                                      cost them nothing. On the list.
```

**Three decisions and only three: fix, defer with a reason, reject with a
reason.** A finding with no decision next to it is a finding nobody acted on, and
the table exists to make that visible.

**Deferring finding 3 because it might be fixed by change 1 is a real decision and
a good one.** It is not the same as ignoring it. The difference is the sentence
after it, which says what would settle the question.

**What you do not do is quietly drop finding 4** because it came from one person
and you disagree with it. Write the rejection down. It costs one line and it is the
line that stops somebody asking you about it in the demonstration.

---

## What five sessions can and cannot tell you

**Somebody in your class is going to say five people is not enough to prove
anything. They are partly right and this section is the honest version of both
sides.**

### The case that five is enough

Five people, watched on real tasks, reliably surface the problems that most people
hit. The reasoning is not complicated: a problem that affects most users will show
up in the first two or three sessions, because most users hit it. You do not need
a large sample to find a hole that nearly everybody falls in.

The practical version of the argument is about cost. **Five sessions is one
afternoon.** Fifty sessions is a project nobody funds, and the extra
forty-five mostly find the same problems again. A team that runs five sessions and
fixes three things has improved their program. A team that waits until they can
run fifty has shipped nothing.

### The case that five is not enough

Five people cannot tell you **how common** anything is. If three of your five hit a
problem, the honest statement is "three of the five people I watched." It is not 60
percent of anything, and treating it as a rate is a real error, not a rounding
one.

Five people also cannot find a problem that only affects a small group, which
includes most accessibility problems. A person using a screen reader, a person who
cannot use a mouse, a person whose first language is not English: none of them is
likely to be in a group of five, and the problems they hit are often blockers.

And **five people chosen badly is five people chosen badly.** Five participants who
all work in the front office will find front-office problems. Five participants
who are all seventeen will not find the problems a forty-year-old hits.

### What this module does about it

**It uses five, and it never writes a percentage.** That is the whole resolution
and it is the thing to remember.

The number five is a rule of thumb. The rule about counts is not a rule of thumb.
"Three of the five people I watched" is true whatever the right sample size turns
out to be, and it stays true when somebody reads your report next year.

---

## The wrong version, and what it produces

The report written straight from memory on Thursday night, with the session sheets
in a bag.

> **Findings**
>
> Overall the program tested well. Most users were able to complete the tasks and
> the general feedback was positive. The main issue was that some users found the
> interface a bit confusing at first, but they got used to it quickly. A few
> suggested adding colour to make the categories clearer. Overall, 80 percent of
> users completed all tasks successfully, which suggests the core workflow is
> sound.

**Count what is in there that anybody could act on. It is nothing.**

- "Tested well", "positive", "a bit confusing", "got used to it": no location, no
  count, no observation.
- "A few suggested adding colour": that is a feature request from people who used
  it for eleven minutes, presented as a finding.
- "80 percent of users completed all tasks": four of five, written as a rate, and
  the four includes the person who took three and a half minutes.
- "Suggests the core workflow is sound": a conclusion with nothing under it, and
  it is the sentence that means nothing will change.

**Every sentence in that paragraph is defensible in conversation and none of them
is checkable.** That is what makes it dangerous rather than merely weak.

---

## Why the wrong version is tempting

**Because it is what a report sounds like.** Every one of those sentences has the
rhythm of professional writing. Read it out loud and it sounds like somebody who
knows what they are doing.

**Because the sheets are messy and the summary is tidy.** Turning eleven scrawled
lines into "P2 needed three attempts" is work. Writing "most users managed fine"
is not.

**Because your program came out of it well**, and you built your program. The pull
toward the generous reading is strong and it is not dishonesty. It is the same
force that makes you help a participant at twenty seconds.

**The counter is mechanical, not moral.** Every sentence in your findings gets a
session number and a line number after it. A sentence that cannot get one does not
go in the findings. It can go in a section called **What I think but did not
measure**, which is a real section and is worth writing.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Observation** | Something you watched, written down with a time |
| **Finding** | An observation with a location, a severity, and a count |
| **Severity** | Blocker, major, or minor. About consequence, not annoyance |
| **Count** | How many of your participants, written as n of 5 |
| **Conclusion** | A sentence supported by findings |
| **Non sequitur** | A conclusion that does not follow from what is under it |
| **Decision** | Fix, defer with a reason, or reject with a reason |
| **Rate** | A proportion of a population. You do not have one |

---

## Self-check

**1.** One of your findings has a count of 1 out of 5. Somebody on your team wants
to drop it. What is the right answer and why?

**2.** Write the finding row for this: P4 spent 41 seconds looking for the output
file, opened two wrong files, found it, and then said "that was fine, I
did not know where to look."

**3.** Your report says "users found the automation confusing." Name three things
that sentence is missing, and rewrite it using this evidence: P1 and P3 both asked
what "DEGRADED" meant; P3 assumed it meant the run had failed.

---

### Answers

**1.** **Keep it, rank it last, and give it a decision.**

A count of 1 out of 5 is a real observation about a real person. It might be the
only person who will ever hit it, or it might be the first of many and you stopped
at five. You cannot tell from five sessions, and that is the honest reason to keep
it rather than an argument about thoroughness.

**What you may do is reject it in writing, with the count as the reason.** "One
participant, cost them nothing, not changing it this week" is a complete decision.
Dropping it off the table so that nobody can see it was ever found is not.

**2.**

```
#  Finding                                  Sev    Count  Evidence
n  The output file is not discoverable.     Major  1/5    P4, 41 s, two
   P4 opened two wrong files before                       wrong files
   finding it, then reported it as fine.
```

The marks are for: a location (the output file), a behaviour rather than a feeling
(two wrong files, 41 seconds), Major rather than Blocker (they finished), and the
count. **The extra mark is for keeping their sentence in the row**, because "that
was fine, I did not know where to look" is the exact disagreement between
behaviour and report that this week is about.

**3.** **Three things missing: a location, a count, and an observation.**
"Confusing" is a conclusion and "users" is not a number.

Rewritten:

> Two of five participants asked what "DEGRADED" meant in the run record. One of
> those two read it as the run having failed, which is wrong, and acted on that
> belief. The word needs a sentence next to it saying what the run did and did not
> do.

**The important half of that answer is the second sentence.** P3 did not only fail
to understand a word. They understood it wrongly and then acted, which makes this
a blocker rather than a major, and none of that survives the phrase "users found
it confusing."
