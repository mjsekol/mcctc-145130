# Gate 2 Adversarial · Week 9
## 145130 Applications of AI · Module 3 · Week 9, Friday · Build 2, 40 minutes

**Individual. Open tooling, including the model, and open sources.** You may not ask another
student.

**This is the last Gate 2 of Grading Period 1, and it is the shortest.** Forty minutes of Build
2, because the module exit assessment ran yesterday and the rest of today is the GP1 close. Work
fast and write less per finding.

**Competencies:** 2.14.4 (evaluate an AI result on validity, relevance, authenticity, potential
bias, and hallucinations), 2.1.12 (privacy security compliance on systems), 2.1.1 (CIA), 2.14.6
(critically analyze scenarios involving AI usage), 1.2.1 (cite sources).

---

## The artifact

`gate2-w09-files/privacy-assessment-memo.md`

It assesses a proposed feature called Compass, an anonymous suggestion box with a locally hosted
model that sorts submissions and drafts replies. The memo is organized, covers the frameworks by
name, has a risk register, and concludes.

**Everything in it is invented for this exercise.** Riverbend City Schools does not exist,
Compass does not exist, and Fairmont Valley Unified District does not exist. **This is a
composite.** What is real is the shape: every failure in it is a failure that shows up in real
assessments, and one of them shows up in almost all of them.

---

## The specification the memo was supposedly written from

The office asked for this:

> Assess Compass before we build it. Tell us what data it touches, which framework governs each
> category and why, what could go wrong and who gets hurt, what the feature refuses to collect,
> where the model runs and whether anything leaves the building, how long we keep submissions and
> who deletes them, and who cannot use this feature as designed. Say clearly what you do not know.

---

## What you are scoring

The five AI Output Evaluation parameters, Ohio competency 2.14.4.

| Parameter | The question it asks |
|---|---|
| **Validity** | Is it correct? A false claim about something that exists. |
| **Relevance** | Does it answer what was asked, or something else? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and what does it consistently favour? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**There are six planted problems.** One in each of those five categories, and a sixth that is
**genuinely arguable**. Finding four is a passing score.

---

## What to submit

`gate2-w09.md`. For each finding, four lines and no more. You have forty minutes.

1. **The quote**, with its section number
2. **The parameter**
3. **What the memo would have to say instead**, in one sentence
4. **How you know**, or `COULD NOT VERIFY` plus where you looked

Then three short sections:

**The arguable one.** Name which, one paragraph for each side, one sentence on what the answer
depends on. **You are not asked to decide it.**

**The anonymity claim.** The memo's whole compliance position rests on section 2. Test it. You
have a tool for this from Wednesday. Write three sentences on whether the claim holds and what
you would have to measure to know.

**What the office asked for and did not get.** Go through the specification clause by clause.
There are at least three clauses with no answer anywhere in the memo.

---

## Scoring, out of 6

| Finding | Points |
|---|---|
| Each correctly identified problem, with a correct parameter and real evidence | 1 |
| Correct problem, wrong parameter, or no evidence | 0.5 |
| **The fabricated rule, missed** | **minus 2** |

The arguable one is scored separately, out of 3, on your reasoning. The anonymity section is
worth 3. The specification audit is worth 3.

---

## Before you start

Two things, and the first one settles more of this memo than the second.

**When the memo says a framework does or does not apply, ask what the framework follows.** You
learned on Tuesday that most of these follow the holder and the relationship, not the topic. A
sentence that turns on the topic alone is a sentence to check.

**When a framework's requirements are described, check the direction of the error.** A memo can
be wrong by claiming a framework requires less than it does, and wrong by claiming it requires
more. **Both are in this document, in the same section**, and the second one is the kind students
miss because it sounds cautious.

---

## Time

- 3 minutes: read the specification and the memo once
- 17 minutes: findings, four lines each
- 8 minutes: the anonymity test
- 7 minutes: the arguable one
- 5 minutes: the specification audit, and commit
