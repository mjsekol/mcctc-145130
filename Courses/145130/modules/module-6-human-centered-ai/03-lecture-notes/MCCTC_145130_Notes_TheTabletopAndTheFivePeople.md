# The tabletop, and the five people
## 145130 Applications of AI · Module 6 · Week 16, Wednesday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W16_TheTabletop.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W16_TheTabletop.md --export pptx
```

**Competencies 2.15.3**, design user tasks and evaluate results through tabletop
exercises, **1.2.13**, identify stakeholders and solicit their opinions, and
**1.2.14**, use motivational strategies to accomplish goals.

---

## Why this exists

You have a script. It reads well, because you wrote it and you know what every
line means.

**You are about to spend fifteen minutes of a real person's time on it**, and
there are no refunds. If task 3 turns out to be impossible, you find that out
while they are sitting there, you apologise, and the session is now twelve minutes
long with three tasks in it.

A tabletop exercise is the study run on paper, with somebody in this room, before
anything real is spent. Twenty minutes. It finds the broken task every time.

---

## The one idea

**A tabletop is not a review of the script. It is a performance of the script.**

The partner does not read it and say whether it makes sense. The partner does
exactly what the script says, does nothing it does not say, and stops the moment it
asks for something they cannot do.

**That distinction is the whole exercise.** A partner who understands your script
finds nothing. A partner who performs it finds three things.

---

## Worked example 1 · the three things a tabletop always finds

Real, from tabletops run on this module's own materials.

**1. A task the program cannot do.**

```
Task 4: Find out which notes came in more than once this week.
Partner: [reads the output twice] "There's nothing in here about that."
You:     "Oh. Yeah, we never built that."
```

**Cost if you had not run the tabletop:** thirty to ninety seconds of a
participant's time, and a note that says nothing.

**2. A task with the answer inside it.**

```
Task 2: Open digest.md and count the network rows.
Partner: "Which file?"
You:     "It says it. digest.md."
Partner: "Right, so I didn't have to find it."
```

**Your partner said the important sentence.** You wanted to know whether somebody
could find the output. You told them.

**3. A task that takes ninety seconds, and there are four of them.**

```
Tabletop timings:  task 1  0:50
                   task 2  1:40
                   task 3  2:10
                   task 4  1:30
                   total   6:10
```

Six minutes with somebody who knows the program. **A participant who does not know
it takes two to three times as long**, which puts this script at somewhere between
twelve and eighteen minutes of tasks alone, inside a fifteen-minute session that
also has a consent line and a closing question in it.

**The fix is cutting a task, not talking faster.** Three tasks that finish is a
real study. Four tasks that overrun means the last one runs against a participant
who is now late.

---

## Worked example 2 · a tabletop that found nothing, and why

```
You:     "Task 1. You are covering the front desk Monday and you want to know
          how many notes are about the network. Show me how you would find
          that out."
Partner: "Yeah, I'd run it with --file and look at the digest."
You:     "Right. Task 2..."
```

Ninety seconds, four tasks, no problems found. Both of you now believe the script
is tested.

**Two things went wrong and neither of them is the script.**

- **The partner described what they would do instead of doing it.** Describing is
  reviewing. Nothing gets exercised.
- **The partner already knows the program**, so every task is trivially doable in
  their head. That is exactly why classmates make bad participants, and it is why
  a classmate makes a bad tabletop partner **unless they are deliberately trying to
  break it.**

**The fix, and it is one sentence to say before you start:**

> Your job is not to understand this. Your job is to do exactly what it says,
> nothing it does not say, and to stop the second it asks for something you cannot
> find.

---

## Worked example 3 · the tabletop record

The deliverable is not "we did a tabletop." It is a record, and it is short.

```
Tabletop record, run with a partner team, 20 minutes

#  What broke                                  Fix made
1  Task 4 asks for duplicate detection.        Task 4 cut. Replaced with a
   The program does not do it.                 prioritisation task.
2  Task 2 names digest.md.                     File name removed. Now reads
                                               "find the answer".
3  Four tasks, 6:10 with somebody who knows    Task 1 cut. It tested the same
   the program. Session is 15 minutes.         thing as task 3.
4  Consent line was being paraphrased.         Printed it and taped it to the
                                               clipboard.

Found nothing in: the closing question, the record sheet.
```

**Row 4 is the one that matters most and it is not about a task.** The consent
line is fixed text, and a student rewriting it in their own words is how the
recording rule and the stopping rule quietly disappear.

**"Found nothing in" is a required line.** It stops a record from implying that
everything was checked.

---

## Finding five people, and keeping them

This is competency 1.2.14, motivational strategies, and it is not a soft skill
here. It is the difference between a report and no report.

### Where they come from

| Source | Why they are good | What to watch |
|---|---|---|
| **Adults in the building** who are not in the IT program | Competent, busy, and honest. They will tell you it is confusing. | Your instructor has already asked four of them. Go through your instructor, never cold. |
| **Students in other shops** | A junior in welding or culinary is exactly the right participant. | Arrange it with both teachers first. |
| **Family at home** | Available, and a parent will say the thing an adult here is too polite to say. | Every rule still applies at the kitchen table. |
| **Younger siblings, twelve or over** | They say the honest thing immediately. | A parent has to be in the room. |

### How to ask, in one sentence

> I built a program for class and I need to watch five people try it for fifteen
> minutes. You do not need to know anything about computers. Would you have
> fifteen minutes on Thursday?

**Three things that sentence does.** It says how long. It says they need no
expertise, which is the fear. It names a day, so the answer is a yes or a
different day rather than a vague maybe.

**"Would you have fifteen minutes sometime?" gets a yes that never happens.**
Every time.

### Keeping the five

- **Confirm the day before.** One sentence. Half your no-shows are people who
  forgot.
- **Turn up early with everything.** A participant who watches you set up for four
  minutes is a participant whose fifteen minutes is now eleven.
- **Finish on time even if you are not finished.** Stopping at fifteen minutes is
  how you get a yes the next time.
- **Thank them, in writing, before the last week of the course.** It costs four
  minutes and it is the difference between a study and an imposition.

### Keeping each other

Your partner is also a person you have to keep moving, and Week 18 is the week
teams stop. Two things that work:

- **A stand-up with the same three sentences every day.** Finished, working on,
  blocked by. A blocked-by that repeats twice is a thing to say out loud to your
  instructor rather than to each other for a third time.
- **Name the next smallest thing.** "Finish the study" is not a task anybody
  starts on a Thursday. "Write the two findings from P3's record" is.

---

## The wrong version, and what it produces

The script goes straight from being written to being run, because the tabletop
felt like overhead.

```
Session 1, P1, 15 minutes booked

0:00  consent line, paraphrased, recording rule not mentioned
0:40  task 1
2:30  task 2, participant asks "which file?", you say digest.md
4:10  task 3
7:50  task 4: "find out which notes came in more than once"
8:20  participant is still looking
9:05  "sorry, we actually didn't build that"
9:20  task 5, rushed
11:40 closing question
12:00 participant has to leave
```

**What you have:** three usable tasks out of five, one finding you handed them the
answer to, ninety seconds of a person hunting for something that does not exist,
and a consent conversation that did not cover recording.

**What twenty minutes with a classmate would have cost:** twenty minutes with a
classmate.

---

## Why the wrong version is tempting

**Because the script looks finished.** You wrote it yesterday, you read it three
times, and nothing in it looks wrong. That is exactly the state the tabletop is
for: everything that is wrong with it is invisible to the person who wrote it.

**Because there is time pressure.** Sessions have to be booked, people have to be
found, and a tabletop feels like a delay in front of the real work. It is twenty
minutes that protects seventy-five.

**Because a polite partner will tell you it is fine**, and then you have done a
tabletop and still have the broken task. That is why the partner's job is written
down.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Tabletop exercise** | Running a procedure on paper, with people, before it is run for real |
| **Pilot** | The same idea, one step further: a full rehearsal session with somebody who is not one of your five |
| **Dry run** | Another word for the same thing |
| **No-show** | A confirmed participant who does not arrive. Plan for one |
| **Stand-up** | A short daily status: finished, working on, blocked by |
| **Blocker** | Something that stops work and that somebody else has to clear |

**Tabletop and pilot are not quite the same.** A tabletop reads the script and
performs it. A pilot runs the whole session, timed, on the real program, with a
person who is not one of your five. **If you have time for both, run the tabletop
Wednesday and the pilot in Period 8.** If you have time for one, run the tabletop.

---

## Self-check

**1.** Your tabletop partner reads your script and says "that all makes sense." You
have eighteen minutes left. What do you do?

**2.** You have four confirmed participants and it is Friday. Name the three moves
in order, and say which one you do first.

**3.** Why is a tabletop with a classmate legitimate when a session with a
classmate is not?

---

### Answers

**1.** **Run it again with the rule stated out loud**, and swap partners if you
can.

"That all makes sense" means they reviewed it rather than performing it. Say the
sentence: your job is to do exactly what it says, nothing it does not say, and to
stop the second it asks for something you cannot find. Then hand them the program
and the script and be quiet.

**If eighteen minutes is not enough for a second round with a new partner**, run
the two tasks you are least sure about, properly, rather than all four badly.

**2.** In order:

1. **Ask your instructor for one of the adults from the backup list**, now, on
   Friday, rather than on Monday. That list exists for exactly this.
2. **Ask somebody at home for the weekend**, which is a real fifth session and
   costs no class time.
3. **Ask a student in another shop for Monday**, arranged through both teachers.

**Do the first one first**, because it is the only one that is already half
arranged and because your instructor needs to know you are short before Monday
rather than after it.

**What you do not do is use a classmate and count it.** Four sessions with a note
saying you could not get a fifth is a true report. Five with a teammate in it is
not.

**3.** Because they are different jobs.

**In a session, you are measuring what somebody does not know.** A classmate knows
it all, so there is nothing to measure. Their behaviour tells you about a person
who has seen your program twenty times, and nobody like that will ever use it.

**In a tabletop, you are testing whether the instructions are followable and
possible.** A classmate is a perfectly good instrument for that, because the
question is not "what do you not know" but "does this script contain something
that cannot be done." **A classmate is actually better at this**, because they can
tell you that the thing you asked for does not exist in the program.
