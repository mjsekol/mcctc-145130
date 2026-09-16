# Gate 2: Adversarial Review · Week 3
## 145130 Applications of AI · Module 1 · Week 3, Friday

**40 minutes**, Friday Build 1, after that day's Gate 1 rep. Individual.
**No AI.** You may use a calculator, your Week 3
notes, and your own saved runs.

---

## What you are looking at

A district technology committee asked for a comparison of two local models before
buying hardware. Somebody produced this report with an assistant. **It was
constructed for this class**, and every problem in it was planted on purpose.
Both models named in it are invented and so are all the numbers.

It is well organised, it has a methods section, and it reaches a clear
recommendation. People buy hardware on documents like this.

---

## What you are scoring

The five AI Output Evaluation parameters. **Score each one from 1 to 5.**

| Parameter | The question it asks |
|---|---|
| **Validity** | Is it correct? A false claim about something real. |
| **Relevance** | Does it answer what was asked, or something else? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and who is missing? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**Your number is not what is scored. Your evidence is.**

**One decision in this report is genuinely arguable.** It is stated as an obvious
choice and it is not one. Find it, take a side, and give the other side its
strongest form.

---

# THE ARTIFACT

> # Local Model Comparison for Classroom Deployment
> ## Prepared for the technology committee. All data original to this study.
>
> ### Summary
>
> We compared two locally hosted models, **Lanternfish-7B** and **Quarrystone-4B**,
> on one lab workstation. **Lanternfish is the better choice for all classroom
> use** and we recommend standardising on it.
>
> ### Method
>
> Each model was given the same prompt, a request to summarise a paragraph of
> English text, and asked to produce a response. Measurements were taken with the
> **Ridgeline Classroom Inference Suite v4**, the standard tool for comparisons of
> this kind.
>
> We ran each prompt once. **Repeats were unnecessary because the results were
> consistent.**
>
> We threw away the first request from each model, because the first request
> includes loading the model into memory and that is not part of what a request
> costs afterwards.
>
> **We did not measure time to first token**, since it does not matter for a batch
> job.
>
> ### Results
>
> | Model | Tokens produced | Total latency | Tokens per second |
> |---|---|---|---|
> | Lanternfish-7B | 3,200 | 96.0 s | **33.3** |
> | Quarrystone-4B | 2,400 | 96.0 s | **25.0** |
>
> Quarrystone is therefore **33% slower** than Lanternfish.
>
> Figures for Quarrystone are reproduced from the manufacturer's published
> benchmark.
>
> ### Sustained token efficiency
>
> Lanternfish also scores higher on the **sustained token efficiency ratio
> (STER)**, the standard measure of how well a model maintains throughput over a
> long generation.
>
> ### Cost
>
> For comparison, cloud providers currently charge between $0.50 and $15.00 per
> million tokens depending on the model tier, and enterprise agreements can reduce
> this further. Districts weighing local deployment against cloud should model
> both.
>
> ### Recommendation
>
> Standardise on Lanternfish-7B for all classroom use.
>
> *Generated with AI assistance. Figures verified.*

---

## What to submit

### Part A: the five scores

For each parameter: **a score from 1 to 5, at least one line quoted exactly from
the artifact, and one sentence saying why that line supports your score.**

A parameter with nothing to report is a valid finding. Say what you looked for.

### Part B: your findings list

Every problem, with the exact claim quoted, which parameter it fails, why it is
wrong in your own words, and how you know. **At least one finding must be
supported by arithmetic you wrote out.**

**There are at least seven.** Five is a passing review. Seven is strong.

### Part C: the argument

Name the decision that is genuinely arguable. Strongest case for it, strongest
case against it, and what you would have done. Both cases have to be real.

### Part D: what I was unsure about

One specific thing, and what you would need to settle it.

---

## How to spend 40 minutes

- **First 8:** read it once without writing. Then read the method section again
  and ask what it makes impossible.
- **Next 12:** Part B, with a calculator. Two numbers in this report can be
  checked against each other.
- **Next 10:** Part A.
- **Next 8:** Part C.
- **Last 2:** Part D.

---

## Scoring

**8 points.**

| Part | Points |
|---|---|
| A: five parameters, each with a quoted line and a reason | 5 |
| C: the argument, both sides real | 2 |
| D: one specific thing you could not settle | 1 |

### The double penalty

**Scoring Validity 4 or 5 costs 2 points, not 1.** Your instructor states this
before you start. This is the measurement module, and there is a false number in
the results table that you have the tools to catch.
