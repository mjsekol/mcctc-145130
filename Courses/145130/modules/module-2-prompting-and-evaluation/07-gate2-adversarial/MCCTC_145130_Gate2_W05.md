# Gate 2: Adversarial Review · Week 5
## 145130 Applications of AI · Module 2 · Week 5, Friday

**50 minutes.** Individual. You have a terminal, the repository, and a library
catalog. **You may not ask a model whether the brief is correct, because the
brief is model output and that is what is being reviewed.**

---

## About this artifact, before you start

**The brief below was constructed for this class.** It is not a real brief
produced by a real assistant for a real coordinator. Every problem in it was
planted on purpose and every one of them is checkable.

You are being told this for the same reason the Infographic Autopsy told you in
145060: a real document has a real author, and thirty students taking apart a
findable person's work is a different exercise than this one. What is real is the
**shape**. Every problem below is one that generated briefs actually make,
presented the way they actually get presented, which is confidently and in a neat
format.

Treat it as though it landed in your inbox.

---

## The scenario

The school's STEM coordinator is deciding whether to replace the paper hall pass
with a digital sign-out on a shared tablet at each classroom door. She asked an AI
assistant for a short research brief. She has forwarded it to you before she
takes it to the principal.

**Your job is to be the person who checks it before she does.**

---

## The five parameters

Every finding gets exactly one label. Choosing the label is part of the work.

| Parameter | The question it asks |
|---|---|
| **Validity** | Is the claim about a real thing false? |
| **Relevance** | Does it answer what was actually asked? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and who is missing? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**There are at least six problems.** Four findings is a passing review. Six is
strong.

**One of them is genuinely arguable.** Two careful reviewers will label it
differently and both will be right to. Your job on that one is not to pick the
correct label. It is to say which you picked, make the strongest case for it, and
say what the other reading would be. **The key scores the reasoning, not the
verdict.**

---

# THE ARTIFACT

> ## Should we move to digital hall passes?
> ### Research brief prepared for the STEM coordinator
>
> ---
>
> **THE QUESTION**
>
> Whether to replace the paper hall pass with a digital sign-out on a shared
> tablet at each classroom door.
>
> ---
>
> **WHAT THE RESEARCH SHOWS**
>
> Digital sign-out systems reduce the time students spend out of class. A study of
> secondary schools found that schools moving to a digital system saw a measurable
> drop in time away from instruction (Hargrove, P. (2019). Corridor Movement and
> Instructional Time in Secondary Schools. Review of School Operations, 14,
> 88-104).
>
> The district's own analysis reached the same conclusion
> (`Courses/145130/_source/MCCTC_145130_HallPass_Study.pdf`, section 3).
>
> ---
>
> **HOW TO EVALUATE THE VENDORS**
>
> When you assess any AI-assisted feature in the vendor's product, use the six
> parameters from the Ohio competency for evaluating an AI result: validity,
> relevance, authenticity, potential bias, hallucinations, and cost.
>
> You should also remember that validity is a wrong claim about a real thing,
> while a hallucination invents the thing.
>
> ---
>
> **HARDWARE CONSIDERATIONS**
>
> The most important hardware decision facing the school this year is the
> replacement cycle for student laptops. Devices older than four years struggle
> with modern development environments, and a phased replacement over two budget
> years is generally the best approach. Consider standardising on one
> manufacturer to reduce support overhead, and negotiate a service contract that
> covers accidental damage, which is the largest single cause of device loss in
> secondary schools.
>
> ---
>
> **IMPLEMENTATION**
>
> 1. Students scan the door tablet's code with their phone to open the pass.
> 2. The pass appears on the student's phone screen for staff to check in the
>    corridor.
> 3. The student's phone records the return time when they scan back in.
> 4. Staff can view live pass data on their own phones during the period.
>
> ---
>
> **RECOMMENDATION**
>
> Adopt the digital system. The paper system works fine for most students, but the
> digital system provides better data and reduces time out of class.
>
> ---
>
> *Generated with AI assistance.*

---

# Your work

For each problem you find, write an entry with all four parts:

1. **The exact claim, quoted.** Word for word.
2. **Which parameter it fails.** One label.
3. **Why it fails.** In your own words.
4. **How you know.** Best: a command you ran and what it printed. Acceptable: a
   document you opened and named by path or section, or a search you performed
   with the exact string and what came back, including "no results." **Not
   acceptable: "it seems wrong" or "I could tell."**

## Acceptance criteria

- [ ] At least four findings, each with all four parts
- [ ] Each labelled with exactly one of the five parameters
- [ ] At least two findings proved by a command you ran, with the output pasted
- [ ] At least one Hallucination and one Validity, with a sentence saying why each
      is not the other
- [ ] The arguable problem identified as arguable, with both readings written out
- [ ] Any parameter you looked for and did not find, recorded as such
- [ ] One "what I was unsure about" entry naming something specific

---

## How to actually check things

You have the repository. Two of the problems can be settled from it in under
thirty seconds each.

To check whether a file exists:

```
ls Courses/145130/_source/
```

To check what a competency actually says:

```
grep -n "2.14.4" Courses/145130/_source/COMPETENCY_REFERENCE.md
```

To find out whether a sentence came from somewhere:

```
grep -rn "invents the thing" Courses/145130/modules/
```

**A claim you cannot settle with a command needs a different kind of checking.**
Some of the problems here are not about facts at all, and no command will touch
them. Notice which, because that difference is most of what this module has been
teaching.

---

## How to spend 50 minutes

- **First 5:** read it once at normal speed, the way the coordinator will. Write
  down your first impression before you analyse anything. You will want it later.
- **Next 10:** every citation and every file path. Check each one.
- **Next 10:** read the question at the top, then read each section and ask
  whether that section answers it.
- **Next 10:** the implementation steps. Read them as four different students.
- **Rest:** the recommendation. Read it one word at a time.

---

## Scoring

Scored under **Written & Documentation**. 40 points.

| Dimension | Points |
|---|---|
| Findings, 3 points each for the first 6 | 18 |
| Evidence: two or more pasted command outputs that actually prove the claim | 8 |
| Parameter labels defensible, with Validity and Hallucination distinguished | 6 |
| The arguable problem, identified and argued both ways | 5 |
| "What I was unsure about," specific | 3 |

**A finding scores zero if "how you know" is missing.** "This is wrong" is an
opinion. The evidence is the assignment.

**A parameter with nothing to report is a valid finding.** Manufacturing a problem
to fill a category costs you more than leaving the category empty, because the
reader who checks your weakest finding decides how much to trust your strongest
one.
