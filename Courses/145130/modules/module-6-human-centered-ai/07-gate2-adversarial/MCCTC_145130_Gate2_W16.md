# Gate 2 · Week 16 · The Report That Read Well
## 145130 Applications of AI · Module 6 · Week 16, Friday, Build 1

**40 minutes. Individual. Silent. No AI tool. No computer needed.**

**Everything you need is on paper**, in `gate2-w16-files/`.

---

## The situation

A team ran four usability sessions on a program called the Ridge Study Planner.
Then they handed the four session records to an AI assistant and asked it to write
the report. They read it, made a couple of small edits, and submitted it.

**It reads like a professional document.** It is going to be used to decide what
gets built next.

---

## Your job

**Score it on the five AI Output Evaluation parameters**, the same five you have
used since Module 2.

```
Validity        is what it says true, given the evidence
Relevance       is it about the thing that was asked
Authenticity    is it what it claims to be, from where it claims
Potential Bias  does it treat people or evidence unevenly
Hallucinations  does it contain things that are not there
```

**There is at least one real problem under every one of the five.** There is also
**one item that is genuinely arguable**, where a reasonable person could go either
way, and it is not one of the five.

---

## What is in the folder

| File | Read it |
|---|---|
| `program-description.md` | **First.** Several claims are about what the program has |
| `sessions.md` | The four records. Lines are numbered `L1`, `L2` |
| `generated-report.md` | The document you are scoring. Sections are numbered |

**Everything in the folder is invented**, including the program, the team, and the
participants. **It is internally consistent**, which means every claim in the report
can be settled by reading the description or the records.

---

## What to hand in

### Five findings, one per parameter

For each, all four of these:

```
Parameter        which of the five
The sentence     quoted, with its section number
The evidence     the record line or the description line that settles it
What it costs    what somebody would do wrong because of it
```

**"What it costs" is the part that separates a 5 from a 3.** A finding with no
consequence next to it is an observation.

### Plus one entry: the thing you are unsure about

```
The sentence            quoted
The case that it is fine
The case that it is not
What would settle it     the one thing you would go and check
```

**You are not scored on which side you land on.** You are scored on whether both
cases are real.

---

## Two things worth saying before you start

**The document is not all wrong.** Several sentences in it are correct and
supported, and a student who marks everything as a defect has not read it either.

**One of the problems is arithmetic.** It is checkable in ninety seconds with the
numbers in `sessions.md`, and it is the one most people walk past.

---

## Scoring

| Item | Points |
|---|---|
| Validity finding | 1 |
| Relevance finding | 1 |
| Authenticity finding | 1 |
| Potential Bias finding | 1 |
| **Hallucination finding** | **1, and missing it costs 2** |
| The unsure-about entry, with both cases | 1 |
| **Total** | **6, and the lowest possible score is negative** |

**Why the hallucination carries the double penalty.** In a code review it is the
security defect. Here it is the same idea: **a fabricated source is the failure this
whole course is built to detect.** A report with a made-up statistic in it gets
quoted by somebody who was not in the room, and then the statistic exists.

---

## One rule for today

**You may not write anything on your sheet that you cannot point at in one of the
three files.** That is the same rule the report broke.
