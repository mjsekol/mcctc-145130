# Lecture Notes: Ethical Character, in Code, Where Nobody Is Watching
## 145130 Applications of AI · Module 3 · Week 8, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W08_EthicalCharacterAtWork.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W08_EthicalCharacterAtWork.pptx)

If you missed class, you can learn this concept from this file alone. Run every program.

**Competencies:** 1.3.3 (use ethical character traits consistent with workplace standards:
honesty, personal integrity, compassion, justice), 2.14.2 (analyze how AI technology
impacts society and the ethical implications of its usage).

---

## Read this first

This file is not legal advice and it is also not a lecture about being a good person. You
do not need one and it would not work.

**Ethics in this course is a technical subject.** It is about what your program does to
somebody who is not in the room, which is a question with observable answers. Every section
below turns a character trait into something you can look at in a file.

---

## Why this exists

Your program is a decision that runs by itself, thousands of times, for people you never
meet.

That is different from every other place where character shows up in your life. If you are
unkind to somebody's face, you see their face. If you write a leaderboard that publishes
the two lowest scores in the class, you see a working feature and a green test run. The
harm is real and it is not in your field of view.

This course has a rule that sits on top of every other rule: **the only way to fail
outright is to submit work you cannot explain.** That rule exists because it is the one
place where honesty and competence turn out to be the same thing. Today is about why.

---

## The four traits, and where each one lives in a repository

The competency names honesty, personal integrity, compassion, and justice. Here is what
each one looks like when it stops being a word and starts being a file.

| Trait | Where you can see it | What its absence looks like |
|---|---|---|
| **Honesty** | The AI usage log, the decision log, the README's limitations section | A README that describes what the program was supposed to do |
| **Personal integrity** | What you do at 11pm the night before a deadline, in a commit nobody reviews | A commit message that says "fixed tests" when it means "deleted the failing test" |
| **Compassion** | The default settings, the error messages, who the feature is hardest on | A feature that works for the median user and punishes the tails |
| **Justice** | Who the system treats differently, and whether that difference was decided on purpose | A ranking whose metric rewards something other than what it claims to measure |

### Honesty is a documentation format, not a feeling

The honest version of a project is not the one with no problems. It is the one whose
documentation matches the program.

Three artifacts carry it in this program:

- **The AI usage log.** What you asked, what came back, what you did with it, and what you
  checked. It is not a confession. It is a record, and it is the thing that makes your work
  reproducible by somebody else.
- **The decision log.** What you chose, what you rejected, and why. The rejected options are
  the part that matters. A decision log with no rejected options is a list.
- **The limitations section of the README.** Every real README has one. If yours does not,
  either you have not looked or you have not written down what you found.

### Personal integrity is what the diff says

Integrity is the gap between what you do when reviewed and what you do when not reviewed.
In software, that gap is visible, because every change is recorded forever with your name
on it.

The 11pm failure modes, named now so you recognize them when they happen:

- Deleting the failing test instead of fixing the failure
- Widening an exception handler until the error stops appearing
- Committing generated work you have not read
- Writing "works on my machine" as the testing section

Every one of those is a real thing that real professionals do under pressure, and every one
of them is visible in the history to anybody who looks.

### Compassion is the default setting

Compassion in software is boring and specific. It is the defaults, the error messages, and
what happens to the person having the worst day.

- **The default.** Whatever you set as the default is what almost everybody gets. If
  publishing a name is the default, names get published.
- **The error message.** "Invalid input" tells a person they are wrong. "That date needs to
  look like 2026-03-14" tells them what to do. Same length, different day.
- **The tails.** Your feature works for the person in the middle. Ask what it does to the
  person with no phone, the person whose name has characters your validator rejects, the
  person reading it on a screen reader.

### Justice is about the metric

Justice in a program almost always comes down to one question: **what does this system
measure, and is that the thing it claims to be about?**

A leaderboard ranked by cards drilled is not a leaderboard of who learned the most. It is a
leaderboard of who had the most free time. Worked example 3 makes that concrete, and it is
the same failure you met in your first year here, when a name filter removed applicants
whose names had accents. **A rule can be applied identically to everybody and still be
unjust, because identical treatment of different situations is not the same as fairness.**

---

## Worked example 1: the test that decides the course grade

This program picks lines out of a file and asks you to explain them. Run it on your own
work before a demo. Then run it on work you did not write, and notice how different the two
feel.

```python
# explain_check.py: pick lines out of your own file and make you explain them.
import sys

path = sys.argv[1]
count = int(sys.argv[2]) if len(sys.argv) > 2 else 3

lines = open(path, encoding="utf-8").read().splitlines()
real = [(n, text) for n, text in enumerate(lines, 1)
        if text.strip() and not text.strip().startswith("#")]

step = max(1, len(real) // count)
picked = real[step // 2::step][:count]

print(f"{path}: {len(real)} lines of code, {count} to explain.\n")
for n, text in picked:
    print(f"line {n}: {text.strip()}")
    print("  why is this line here, and what breaks without it?")
    print("  what would you have written instead, and why did you not?\n")
print("If you cannot answer both questions for every line, the work is not ready.")
```

Run:

```
python explain_check.py study-buddy/study_buddy.py 3
```

Output:

```
study-buddy/study_buddy.py: 82 lines of code, 3 to explain.

line 17: import urllib.request
  why is this line here, and what breaks without it?
  what would you have written instead, and why did you not?

line 49: return None
  why is this line here, and what breaks without it?
  what would you have written instead, and why did you not?

line 82: "No model answered at "
  why is this line here, and what breaks without it?
  what would you have written instead, and why did you not?

If you cannot answer both questions for every line, the work is not ready.
```

Line 49 is the interesting one. It is the line that refuses to return a reply the model did
not finish. Somebody who wrote that line can tell you in one sentence why a half-finished
hint is worse than no hint. Somebody who pasted it cannot, and the difference shows up
inside about four seconds.

**The tool is blunt on purpose.** Line 82 is half of a string, and the honest answer to
"why is this line here" is "because that message spans three lines." That answer takes two
seconds and proves the same thing. The test is not whether the question is deep. It is
whether you are the person who wrote it.

## Worked example 2: an AI usage log entry that is worth writing

An honest log is not long. It is specific.

```
## Entry 4

Task: write the failure message for when no model answers.
Asked: "Write a one-sentence message for when a local model is unreachable,
        for high school users, that does not blame the user."
Came back: three options. Two said "something went wrong". One said "no hints
        available right now".
What I did: rejected all three. "No hints available" says the hints do not
        exist, which is the exact lie this project is not allowed to tell.
        Wrote my own, naming the address and saying it is a model problem.
Checked: ran study_buddy.py --hints --port 11634 with nothing listening on
        that port, and read the output. Confirmed it says "model problem, not an
        empty result".
```

Read that entry and notice what makes it honest. It records a rejection and the reason. **A
log containing only the times a model was right is not a log, it is a highlight reel.**

## Worked example 3: the leaderboard, and what it measures

Every student in this program is invented.

```python
# leaderboard.py: the drill leaderboard, as a team first writes it.
SESSIONS = [
    {"name": "Marisol Vega", "cards": 118, "accuracy": 0.61},
    {"name": "Devon Whitaker", "cards": 96, "accuracy": 0.94},
    {"name": "Priya Raman", "cards": 40, "accuracy": 0.88},
    {"name": "Aiden Kowalczyk", "cards": 12, "accuracy": 0.42},
    {"name": "Zainab Osei", "cards": 9, "accuracy": 0.33},
]

print("THIS WEEK'S DRILL LEADERBOARD")
for place, row in enumerate(sorted(SESSIONS, key=lambda r: -r["cards"]), 1):
    print(f"{place}. {row['name']:<20} {row['cards']:>4} cards  "
          f"{row['accuracy']:.0%} correct")
```

Output:

```
THIS WEEK'S DRILL LEADERBOARD
1. Marisol Vega          118 cards  61% correct
2. Devon Whitaker         96 cards  94% correct
3. Priya Raman            40 cards  88% correct
4. Aiden Kowalczyk        12 cards  42% correct
5. Zainab Osei             9 cards  33% correct
```

**No error. Twelve lines of code and a clean table.** Now look at what it actually does.

- **Justice.** It ranks by cards drilled and calls that a leaderboard. The student at the
  top has the lowest accuracy of the top three. The metric measures time available, and
  time available is not distributed evenly across a class. Zainab works evenings at the
  family store, which you know from the roster in Week 9.
- **Compassion.** Places four and five publish a low number next to a real name, in a
  feature nobody asked to be in. The default is public and the default is everybody.
- **Honesty.** The heading says "leaderboard", which implies the ranking is about
  performance. The ranking is about volume.

Fixes that cost almost nothing: rank by accuracy on cards attempted at least twenty times,
or drop the ranking entirely and show each student their own progress. Make participation
opt in. Show the top three and stop. **Each of those is a one-line change and each of them
is an ethical decision, which is the point of this example.**

---

## The wrong version, and what it does instead of an error

The wrong version is not a program today. It is a sentence, and you will hear it this year:

> "I understand it, I only could not have written it myself."

**Nothing about that sentence is an error.** It is honest, it is said sincerely, and it is
the single most common way a good student ends up submitting work they cannot defend.

Here is why it does not hold. Understanding code while reading it and being able to produce
it are different skills, and reading is far the weaker signal. You can follow a proof and
not be able to prove it. You can follow a game and not be able to play it. **Code you
understand while reading is code you cannot debug at 11pm**, because debugging requires
knowing what the author was trying to do, and you were not the author.

The rule in this program is not there to punish you for using tools. Gate 3 gives you every
tool there is. **The rule is there because the submission is a claim, and the claim is "I
made this and I stand behind it."** If that claim is not true, everything downstream of it
is unreliable: your estimate of how long the next feature takes, your teammate's assumption
that somebody understands this file, and the judge's belief in your demo.

## Why the wrong version is tempting

**It is true in the moment.** You did read it. It did make sense. That feeling is real and
it is not evidence.

**The deadline is real and the consequence is not visible.** Submitting the code you do not
understand has no immediate cost. The cost shows up at the demo, in the next sprint, or at
the moment somebody asks a question in front of a judge.

**Everybody else seems fine.** This is the one worth naming out loud. In a room where
everybody is using the same tools, the person who slows down to understand looks slower.
They are. **For one week.** By Week 9, they are the one the team asks.

---

## Vocabulary

| Term | What it means |
|---|---|
| **AI usage log** | Your record of what you asked a model, what came back, what you did, and what you checked. |
| **Decision log** | What you chose, what you rejected, and why. The rejections carry the value. |
| **Limitations section** | The part of a README that says what the program does not do and where it fails. |
| **Default** | The setting almost everybody will have, because almost nobody changes settings. |
| **Metric** | What a system actually measures, which is often not what it claims to be about. |
| **Disparate impact** | A rule applied identically that lands differently on different groups. |
| **Explainability, in this course** | Whether you can say why each line is there and what you rejected. |
| **Professional code of ethics** | A published statement of professional obligations. The ACM and IEEE both publish one. **[VERIFY]** their current addresses before assigning them. |

---

## Self-check

**Question 1.** Run `explain_check.py` on a file you wrote last week, with a count of five.
Answer both questions for all five lines out loud, timed. Then write down how many you
could answer in under fifteen seconds each, and what you will do about the ones you could
not.

**Question 2.** Rewrite the leaderboard so it is defensible. You may change the metric, the
audience, the defaults, or remove it. State which trait each of your changes serves, and
name one thing your version is now worse at. Every design choice gives something up, and an
answer that claims to give up nothing has not been thought through.

**Question 3.** A teammate's commit message says "cleaned up tests, all green now." The diff
deletes two test functions. Write what you say to them. You have to be specific enough to be
useful and not so accusing that they stop talking to you, because you have to work with this
person for two more weeks.

---

### Answers

**1.** No fixed answer. The number is yours. What matters is what you do with it: the lines
you could not explain get read, traced, and rewritten before the next demo, and if a line
came from a model, its usage log entry gets written now rather than later.

**2.** Many valid answers. A strong one:

> Rank nobody. Show each student their own accuracy over time, and show one class number:
> the median accuracy this week. Opting in to a public top three is possible from the
> settings screen and is off by default.
>
> - **Justice:** the metric is accuracy, not volume, so a student with two free hours and a
>   student with twenty minutes are measured on the same thing.
> - **Compassion:** the default is private, so being in the feature is a choice rather than
>   a consequence of existing.
> - **Honesty:** nothing is called a leaderboard, because nothing is being led.
>
> **What it is worse at:** competition motivates some students, and this version removes
> that entirely. The median line can also be misread as a target. A team that wants the
> motivation back should add it as something a student opts into, not as the default.

**3.** For example:

> "Hey, quick one about commit 4a1c. The message says cleaned up tests but the diff removes
> `test_empty_deck` and `test_missing_colon`. Were those failing? If they were, I would
> rather we fix the failure and keep them, because those two are the ones that catch the
> parser bug we hit last week. Want to look at it together in Build 2?"

What makes it work: it names the specific commit, describes what the diff does rather than
what the person is, asks a question instead of stating a motive, gives a concrete reason the
tests matter, and offers to help. **The gap between the message and the diff is the thing
being raised, and that is a factual observation, which is a far simpler thing to discuss
than a character judgement.**
