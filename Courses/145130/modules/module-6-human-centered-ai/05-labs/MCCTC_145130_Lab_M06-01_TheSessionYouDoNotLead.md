# Lab M06-01 · The Session You Do Not Lead
## 145130 Applications of AI · Module 6 · Week 16, Tuesday and Wednesday

**Files:** `lab-m06-01-files/`
**Time:** Tuesday Build 1 and Build 2, then Wednesday Build 1.
**Due:** parts 1 and 2 Tuesday end of Build 2. Part 3 Wednesday end of Build 1.

---

## The scenario

The front office person from your Module 5 brief watched your demonstration and
said it looked great. Then they tried to use it on a Monday morning and could not
work out how to start it, and they did not tell you, because telling you would
have been awkward.

You are going to find out what they could not do, from five people who are not in
this class, in fifteen minutes each.

**Today you write the thing you take into the room.** Tomorrow you break it on a
classmate, before you spend a real person on it.

---

## What you will build

A one-page participant script, four tasks of your own, and a tabletop record
proving that somebody performed it and it survived.

---

## What is in the folder

| File | What it is |
|---|---|
| `participant-script.md` | The template. The consent line in it is fixed text |
| `session-record-sheet.md` | Print five. Two columns and three numbers per task |
| `drafted-tasks.md` | Six tasks written for a program called `notesort`. Four are broken |
| `tabletop-record-sheet.md` | What you fill in tomorrow |

---

# Part 1 · Judge six tasks · 20 minutes

Open `drafted-tasks.md`. **Read the paragraph describing `notesort` twice before
you read the tasks**, because one of the six asks for something the program does
not do and it reads perfectly reasonably.

For each of the six, write: usable or not, which of the five named problems it has,
and what you would change.

Then answer the two questions underneath. **The second one is the one worth
thinking about**, because a broken task can still test something real.

**Acceptance criteria.**

- [ ] All six judged
- [ ] Every broken one carries at least one named problem letter
- [ ] Both questions answered in one sentence each

---

# Part 2 · Four tasks for your own program · 35 minutes

Now write four tasks for the application you built in Module 5.

**Every task has three parts:**

```
starting state   where they are, what they have in front of them
goal             what they want to end up knowing or having
reason           why a person would actually want that
```

**Write the reason as a real Monday morning**, not as "so that you can test the
program."

### The checks, run them on your own four

```
[ ] No task names a control, a file, a flag, or a menu item
[ ] No task asks what they think
[ ] Every task can be done with the program as it exists today
[ ] No task tells them something is wrong
[ ] Every task has a reason a person would actually have
```

### Then build the script

Copy `participant-script.md` into your repository as `study/participant-script.md`
and fill in the four tasks.

**The consent line is fixed text and you do not rewrite it.** It is short on
purpose. The two sentences people lose when they paraphrase are the recording one
and the stopping one.

**Acceptance criteria.**

- [ ] `study/participant-script.md` committed
- [ ] Consent line present, word for word, unchanged
- [ ] Four tasks, each with a starting state, a goal, and a reason
- [ ] The facilitator rules and the closing question are on the page
- [ ] **It fits on one page.** If it does not, it will not fit in fifteen minutes

---

# Part 3 · The tabletop · Wednesday Build 1 · 40 minutes

Twenty minutes each way, with the team you are paired with.

**The reader says this out loud before starting:**

> My job is not to understand this. My job is to do exactly what it says, nothing
> it does not say, and to stop the second it asks for something I cannot find.

**Then the author is quiet.** Same rule as a session. The author writes down what
breaks and does not explain anything.

**Time every task.** Somebody who already knows the program is two to three times
faster than a participant. Multiply by 2.5 and check the total fits inside thirteen
minutes.

**Acceptance criteria.**

- [ ] `study/tabletop-record.md` committed
- [ ] Every problem found has a fix written next to it
- [ ] The **Found nothing in** line is filled in
- [ ] The timing table is filled in with the estimate
- [ ] If the estimate was over thirteen minutes, a task was cut and the record says
      which one and why

---

## If it breaks

**"My tabletop partner did not find anything."**
They reviewed your script rather than performing it. Say the rule out loud and run
it again with a different partner. If you cannot, run the two tasks you are least
sure about properly rather than all four badly. **A record with an empty table is
not a record.**

**"All four of my tasks name a file."**
Common, and the fix is mechanical: delete the file name and see whether the task
still makes sense. Usually it does, and it is now testing something.

**"I cannot think of a reason anybody would want this."**
That is a finding about your program, not about your task writing, and it is worth
a line in your decision log. Write the most honest reason you can and mark it as
thin.

**"My script is two pages."**
Cut a task. Do not shrink the font and do not shorten the consent line.

---

## Submission checklist

- [ ] Part 1 sheet, six judgements and two answers
- [ ] `study/participant-script.md`, one page, consent line unchanged
- [ ] `study/tabletop-record.md`, with fixes and the found-nothing line
- [ ] Your five participants named on your own paper list, not in any file
- [ ] Committed at the end of each period

---

# Extended options

Same competency, same scale. Your instructor hands you one of these.

## SCAFFOLDED

**Three tasks instead of four**, and two of them are given to you as templates with
the starting state and the reason already written. You supply the goal.

```
Task A  You are covering the front desk on Monday and there is a pile of
        notes from last week. You want to ______________________________
        before you start answering any of them. Show me how you would
        do that.

Task B  Somebody has asked you which problem came up most this week and
        you have five minutes before the meeting. You want to
        ______________________________. Show me how you would find out.
```

**More checkpoints:** your instructor checks your three tasks against the five
rules before you write the script, rather than after.

**Same tabletop, same record, same criteria.**

## STANDARD

The lab as written above.

## EXTENDED

Add a fifth task that is **deliberately harder than the program supports well**,
and write down beforehand what you expect to happen.

**The rule:** it has to be something the program can technically do, not something
it cannot. A task that is impossible is a broken task. A task that is possible and
awkward is where your worst finding is hiding.

Then write two sentences before you run anything: what you expect a participant to
do, and what you will conclude if they do it. **Committing a prediction before you
collect data is the whole of the method**, and it is the same move as the wireframe
prediction next week.

## APPLIED

**Write the script for a completely different thing.** Not your program.

Pick something physical in this building that a stranger has to operate: the
badge reader, a vending machine, the 3D printer's touchscreen, the sign-in tablet
at the front desk.

Write four tasks, the consent line, and the facilitator rules for it. Then run a
tabletop on it with your partner, using the real object.

**Why this version:** the method is not about software and a student who can only
apply it to their own program has learned a habit rather than a skill. **The
findings from a badge reader are often sharper**, because nobody is defensive about
it.

---

## Which version, three observable signals

| If you see | Hand them |
|---|---|
| A student whose four tasks all start with a verb like "click", "open", or "run", after the lesson | **SCAFFOLDED**. The templates remove the part they are stuck on and keep the part being assessed |
| A student who has four clean tasks written before Build 1 ends | **EXTENDED**. They have the skill and need the harder question |
| A student who says "my program is too simple for four tasks" | **APPLIED**. The problem is that they cannot see their own program from outside, and a badge reader fixes that in ten minutes |
