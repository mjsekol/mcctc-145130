# Gate 2: Adversarial Review · Week 4
## 145130 Applications of AI · Module 2 · Week 4, Friday

**50 minutes.** Individual. You may and should run the code. **You may not ask a
model whether it is correct, because the kind of thing being reviewed is model
output.**

The program is `gate2-w04-files/study_plan_builder.py`. Copy the whole
`gate2-w04-files/` folder somewhere you can work, and run it.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got the program in
`study_plan_builder.py`. It runs. It is formatted well, the functions are small,
the docstrings are complete, and the comments sound sure of themselves.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It accepts input it should refuse, or sends something it should not |
| **Readability** | A name or a comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing, or something invented |

**One of the five is genuinely arguable.** Two reasonable people can disagree
about whether it is a defect at all. Your job on that one is not to pick the
right side. It is to say what you would need to know to decide, and to make the
strongest case you can for the side you land on. **The key scores the reasoning,
not the verdict.**

---

## PART A: The requirements

> Write `study_plan_builder.py` for the Media Club study hall.
>
> It reads a list of study topics and turns each one into a short study plan
> using the club's locally hosted model.
>
> 1. Read topics from `topics.txt`, one topic per line, ignoring blank lines.
> 2. For each topic, ask the model for **exactly 4 numbered steps**, under 60
>    words, returning only JSON with keys `topic` and `steps`.
> 3. **Refuse any topic longer than 80 characters.** A topic is a topic, not an
>    essay.
> 4. If the model fails on one topic, record that topic as failed and keep going
>    with the rest. One bad topic must not stop the run.
> 5. Write the results to `plans.md`, one section per topic.
> 6. **No student's name or other personal detail may reach the model.** The
>    topics file is written by students, so every topic is screened against
>    `banned_names.txt` before any prompt is built.

---

## PART B: What the AI produced

```
python stub_model_server.py          (in a second terminal, from 05-labs/prompt-toolkit)
python study_plan_builder.py
```

A real run:

```
6 topics loaded from topics.txt
  skipped: topic contains a student name
  skipped: topic is 80 characters, over the 80 limit
  skipped: topic is 94 characters, over the 80 limit
3 plans written to plans.md, 3 skipped or failed
```

**Read those five lines against the six requirements before you read any code.**
Two of the six are already broken in that output, and you can find both without
opening the program.

The program also writes `sent_prompts.log`, which holds every prompt it actually
sent. **That file is the evidence for one of the five defects.** Open it.

---

## How to spend 50 minutes

- **First 5:** run it. Compare the run output line by line against the six
  requirements. Write down anything that does not match.
- **Next 10:** open `topics.txt` and count the characters in each line. Python
  will do it: `python -c "print([len(l) for l in open('topics.txt').read().splitlines() if l.strip()])"`
- **Next 10:** open `sent_prompts.log` and read every prompt that was sent. Ask
  what requirement 6 says, and then ask whether it happened.
- **Next 10:** read `plans.md` and count things. Then read the prompt the program
  builds and count the same things.
- **Rest:** read each comment and each variable name against the code under it.
  Ask whether it is true.

---

## What to submit

For each defect:

1. **File and line number.**
2. **Dimension.** One of the five.
3. **What goes wrong for a real person or a real run.** Not "it is wrong." Who
   is affected and how.
4. **The fix.** Specific enough that somebody could apply it.
5. **How you know.** The command you ran and what it printed, or the exact lines
   you are comparing.

Then one final entry: **what I was unsure about**, naming something specific.
That entry is scored, and leaving it blank costs more than a wrong guess.

**For the arguable defect, say so.** Write which one you think it is, the case for
it being a real defect, the case for it not being one, and what you would measure
to settle it.

---

## Scoring

Five defects. Five points each, one per dimension, plus five for the
unsure-about entry and five for the arguable-defect reasoning. Thirty points.

**The security defect is worth double.** Missing it costs ten. Your instructor
states this before you start, and it is stated here so nobody can say they did
not know.

**Four of five found is a strong score.** Nobody is expected to find all five on a
first Gate 2, and one of the five is designed to be missed.

---

## What this is not

This is not a hunt for style you disagree with. A function you would have named
differently is not a defect. A defect is something that produces a wrong result,
lets through something it should refuse, misleads a future reader about what the
code does, does unnecessary work, or fails to do what the specification asked
for.

If your finding cannot be written as "here is what goes wrong," it is a
preference, and preferences are not what is being assessed today.
