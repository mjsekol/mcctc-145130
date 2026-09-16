# Lab M03-02: The Steelman Exchange
## 145130 Applications of AI · Module 3 · Week 8, Thursday

**Gate:** 3 (open tooling), with a closed section. **Duration:** Week 8 Thursday, Build 1, 40
minutes, and Build 2, 55 minutes.

**Files:** `lab-m03-02-files/`
**Competencies:** 2.14.2 (analyze how AI technology impacts society and the ethical
implications of its usage), 2.14.6 (critically analyze scenarios involving AI usage), 1.5.7
(use intercultural communication skills to exchange ideas and create meaning), 1.1.9 (give and
receive constructive feedback).

**Build 1 is 40 minutes of build work**, because the Gate 1 rep runs in its first 10
minutes.

---

## Before you start

This lab is not about being open-minded and it is not about compromise. **It is a technical
exercise in stating a position you reject, accurately enough that somebody who holds it signs
off on your version.**

Two rules that run the whole lab:

1. **No sentence may describe the other side's motives.** Not what they want, not what they
   really care about, not what they are trying to do. Only what they claim and why.
2. **The other person decides whether you got it right.** Not you, and not the program.

**Nobody is graded on which side they were assigned, and nobody is graded on changing their
mind.** Several of you will finish this lab holding exactly the view you started with, more
firmly and for better reasons. That is a good outcome.

---

## The scenario

Your position paper is due next week, and it argues the side you disagree with. Every year
about half the class writes a paper that refutes a version of the other side that nobody holds,
gets a low score, and is surprised. Today you find out in 50 minutes instead of in a grade.

## What you will build

A paragraph stating the strongest case for a position you reject, signed off or sent back by a
classmate who actually holds it.

---

## What is in `lab-m03-02-files/`

| File | What it is |
|---|---|
| `steelman_check.py` | Counts the parts of an argument. It cannot check whether they are true. |
| `my-paragraph-starter.txt` | The file you replace with your paragraph. |

Run the demo first so you know what the tool does and does not do:

```
cd lab-m03-02-files
python steelman_check.py --demo
```

**Observable result.** Version A scores 2 of 6. Version B scores 6 of 6. Both reach the same
conclusion. Read both and work out what the four missing parts were doing.

---

## Part 1 · Build 1, 40 minutes: write the case you reject

### Step 1. Pick a question and declare your actual position

Choose one:

| # | Question |
|---|---|
| 1 | Should training a generative model on publicly posted work, without permission, count as fair use? |
| 2 | Should schools run AI writing detectors on student work? |
| 3 | Should AI-generated output be eligible for copyright? |
| 4 | Should a school district run models locally at higher cost rather than using a cloud vendor? |
| 5 | Should AI be used to screen job applicants? |
| 6 | Should students be required to disclose every use of AI in their work? |

Write one sentence in `position.md`: **what you actually think, and why, in your own words.**

**Observable result.** A dated line in `position.md`. You will read it again at the end of the
lab and it has to be the version you wrote before you did the work.

### Step 2. Find a partner who disagrees with you

Not a partner who is neutral. A partner who holds the other view on the same question.

**Observable result.** Two names written at the top of your file. If nobody in the room holds
the other view, tell your instructor: **that is itself a finding about the room**, and you will
be paired with somebody arguing the position rather than holding it.

### Step 3. Write the paragraph. No AI tools for this step

This step is closed. Plain editor, no model, no search.

Write five to eight sentences making **the strongest case for the side you do not hold.**

Rules:

- No sentence describes the other side's motives
- Name at least one specific group who gains and one who loses
- Give a reason, not a restatement of the claim
- State one thing that would make your own case weaker, and do not hide it

**The reason this step is closed:** a model will write you a fluent, balanced-sounding
paragraph that says nothing, and you would never find out whether you could do it. That
paragraph is the one you looked at on Thursday, and it scores well on the checker.

**Observable result.** `my-paragraph.txt`, five to eight sentences.

### Step 4. Run the checker and read what is missing

```
python steelman_check.py my-paragraph.txt
```

**Observable result.** A score out of 6. **Do not chase the score.** If a part is missing, ask
whether the paragraph actually needs it before you add a phrase. A paragraph that gains a point
by adding the words "critics argue" and nothing else has got worse, not better.

---

## Part 2 · Build 2, 55 minutes: the exchange

### Step 5. Trade paragraphs. Your partner is the judge

Your partner reads your paragraph and answers three questions in writing:

1. **Would you sign this?** Yes or no.
2. **What is the strongest part of my case that you would not have thought I would say?**
3. **What did I leave out that you would have put first?**

**Observable result.** Three written answers on each side. **Question 2 is where the credit is.**
If your partner cannot name anything, you wrote the version they already expected, which is the
version that convinces nobody.

### Step 6. Rewrite once, using only what your partner said

Fifteen minutes. You may add, cut, and reorder. You may not change which side you are arguing.

**Observable result.** `my-paragraph-v2.txt`, and a one-line note saying which of your partner's
three answers drove the biggest change.

### Step 7. Now write your own side, in three sentences

Not a full paper. Three sentences stating your real position, written after having spent an hour
inside the other one.

**Observable result.** `position-after.md`, three sentences, plus one sentence answering: **is
this different from what you wrote in step 1, and if it is not different at all, what did you
learn that made it stay the same?**

### Step 8. Name your audience

Your position paper next week has a reader. Write two lines:

- Who is the audience, specifically
- Name **one assumption they hold that you do not share**, and say what that changes about how
  you would argue

**Observable result.** Two lines in `position-after.md`. If your audience is "the teacher", go
back. The teacher is the grader, not the audience. Pick the school board, a client, a judge, a
teammate, or a reader in a country with a different legal framing.

---

## Acceptance criteria

- [ ] `position.md` written before step 3, with a date
- [ ] Partner named, and the partner actually holds the other view
- [ ] `my-paragraph.txt`, five to eight sentences, written with no AI tools
- [ ] No sentence in it describes the other side's motives
- [ ] At least one group who gains and one who loses, both named
- [ ] Your partner's three written answers, in your repository, marked as theirs
- [ ] `my-paragraph-v2.txt`, rewritten using your partner's answers
- [ ] `position-after.md` with three sentences, the reflection question, and the audience lines
- [ ] Committed and pushed

---

## If it breaks

**`No file at my-paragraph.txt. Check the path.`**
You are in the wrong directory, or the file is still called `my-paragraph-starter.txt`. The
checker takes a path, and it does not guess.

**The checker gives you 6 of 6 and your partner will not sign it.**
The checker was right and you asked it the wrong question. It counts parts. Your partner
evaluates substance. **Your partner outranks the program every time**, and this situation is
worth writing down in your reflection because it is exactly what a passing automated check
against a real reviewer looks like in industry.

**You cannot find a single argument for the other side.**
Two moves. First, go read what somebody who holds the position actually wrote, in their own
words, rather than a summary of it by somebody who disagrees. Second, ask what they are
worried about that you are not worried about. **Almost every genuine disagreement about AI is
two people weighting two real risks differently**, and once you name the risk the argument
appears.

**Your partner says "that is not what I think" and you cannot see the difference.**
Ask them to rewrite one sentence of yours in their own words, then diff the two sentences. The
difference is almost always a single word that carries a motive or a certainty you added.

---

## Stretch goal

Take your finished paragraph and rewrite it for a reader in a rights-based privacy framework
rather than a sectoral one. Which of your arguments got weaker, and what did you put in its
place? One paragraph, and it is the hardest 150 words in this module.

---

## Submission checklist

- [ ] `position.md`, `my-paragraph.txt`, `my-paragraph-v2.txt`, `position-after.md`
- [ ] Partner's written answers, marked as theirs
- [ ] Checker output pasted for both versions of your paragraph
- [ ] AI usage log entry. **Step 3 was closed, so the honest entry may be "none for step 3"**
- [ ] Pushed

---

# Extended options

All four assess the same competency and grade on the same 100-point scale.

## How to choose, three observable signals

1. **The step 1 sentence.** A student who cannot state their own position in one sentence is not
   ready to state somebody else's. Give them SCAFFOLDED.
2. **The first draft's second sentence.** If it starts `people who believe this just` or `they only care
   about`, the student is writing a straw man and does not yet see it. SCAFFOLDED, with
   the motive-sentence rule read out loud.
3. **The step 5 answer to question 2.** A partner who names something surprising means the student
   reached the steel man on the first try. That student goes to EXTENDED in Build 2 rather than
   rewriting.

## SCAFFOLDED

Same target, smaller scope, more structure.

- The question is chosen for you: number 2, detectors, because both sides are concrete and both
  are about you.
- You are given **three sentence stems** and you complete them:
  - "Teachers who want detectors are responding to a real problem, which is ___."
  - "The students who are harmed when nobody checks are ___, and here is how ___."
  - "The strongest version of this position does not claim ___, it claims ___."
- The paragraph is four sentences, not eight.
- The motive rule is checked first, by the instructor, before the partner sees it.
- Step 7 and step 8 are one line each.

**Same grading scale.** The competency is stating a position you reject, accurately, and four
sentences assesses that.

## STANDARD

The lab as written above.

## EXTENDED

Everything in STANDARD, plus the **ideological Turing test**.

Write two paragraphs on your question, one for each side, unlabelled. Give both to two
classmates who hold opposite views and ask each one: **which of these was written by somebody
who agrees with you?**

- If both guess right about which is which, both paragraphs are honest and one is stronger.
  Say which and why.
- If either one guesses wrong, you have written the strongest possible version of the thing you
  reject, which is the point of the whole exercise.

Write up what happened and what it tells you about your own position.

**The hint, and it points at a method rather than an answer:** the failure mode here is writing
the side you hold in your natural voice and the other side in a flatter one. Match the register.
If one paragraph has specifics and the other has generalities, the test is over before it starts.

## APPLIED

Same skill, completely different domain: **a technical argument on your own team.**

Pick a real disagreement inside your project team. A framework choice, a scope call, whether a
feature ships. Write the strongest case for the position you argued against, and take it to the
teammate who holds it. Same three questions, same sign-off.

Deliverable: the paragraph, the teammate's three answers, and a one-paragraph note on whether
the decision changed and what you would do differently in the next design review.

**Give this to the student who asks what this has to do with programming.** The answer arrives
when their teammate signs off and the actual disagreement turns out to be about something
neither of them had said out loud.
