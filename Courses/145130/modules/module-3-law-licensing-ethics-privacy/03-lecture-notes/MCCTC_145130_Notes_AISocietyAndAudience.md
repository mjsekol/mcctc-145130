# Lecture Notes: Arguing Honestly About AI, With Somebody Unlike You
## 145130 Applications of AI · Module 3 · Week 8, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W08_AISocietyAndAudience.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W08_AISocietyAndAudience.pptx)

If you missed class, you can learn this concept from this file alone. Run the program on
your own paragraph.

**Competencies:** 2.14.2 (analyze how artificial intelligence technology impacts society
and the ethical implications of its usage), 1.5.7 (use intercultural communication skills to
exchange ideas and create meaning), 2.14.6 (critically analyze scenarios involving AI usage).

---

## Read this first

This file is not legal advice and it also does not tell you what to think.

**Your position paper requires you to argue the side you personally disagree with.** That is
not a trick and it is not an exercise in being fake. It is the fastest way to find out
whether you understood the question or only picked a team, and it is a skill you will use in
every technical argument you ever have.

---

## Why this exists

Two reasons, and the second one is the one that pays.

**First:** the competency asks you to analyze how AI affects society. An analysis is not a
verdict. It is a description of who gains, who loses, what is uncertain, and what depends on
choices people are making right now.

**Second:** you are going to argue about this for the rest of your career, with people who do
not share your assumptions. Your teammate, your client, a school board, a customer in another
country. **An argument that only works on people who already agree with you is not an
argument, it is a flag.**

---

## Where AI actually touches society

Keep this list next to you while you write. Most bad arguments about AI are bad because they
notice one row and treat it as the whole table.

| Area | The gain that is real | The loss that is real |
|---|---|---|
| **Work** | Tedious work gets done faster, and small teams do things only large ones could | Some work disappears, and the people who lose it are rarely the ones who gain |
| **Access to expertise** | A person with no lawyer, doctor, or tutor gets something rather than nothing | Something is not the same as a professional, and the people most likely to rely on it are the least able to check it |
| **Education** | Instant feedback, at any hour, patiently | Feedback is not learning, and a tool that does the task removes the practice |
| **Allocation decisions** | Consistency, and a written rule instead of a mood | A biased rule applied at scale, silently, to everybody, forever |
| **The information environment** | Anyone can produce and translate material | Anyone can produce and translate material, including material meant to deceive |
| **Accessibility** | Captions, descriptions, translation, and reading support at a cost near zero | Errors in those outputs land on people with the least ability to detect them |
| **Energy and water** | Efficiency gains in other systems | Training and serving models consumes real energy and water, in real places |
| **Concentration of power** | Tools available to small teams | The compute, the data, and the distribution belong to a handful of organizations |

**Notice the shape.** Almost every row has a real gain and a real loss, and they usually land
on different people. That is what makes these questions hard, and it is why "AI is good" and
"AI is bad" are both statements that fail to say anything.

---

## The method: argue the strongest version

**A straw man is the weakest version of the other side's argument.** It is the version that
is fun to refute and that nobody actually holds. Refuting it accomplishes nothing and it is
the single most common failure in student position papers.

**A steel man is the strongest version.** You state the other side's case so well that
somebody who holds it would read your paragraph and say "yes, that is what I think."

Here is the test. **Write the other side's position. Show it to somebody who actually holds
it. If they say you got it wrong, you did.** That is the whole method, and it is not
comfortable.

Why this is worth the discomfort:

1. **It is the only way to find out if you are right.** If you have only argued against the
   weak version, you have no idea whether your position survives the strong one.
2. **It is how you change anybody's mind.** Nobody has ever been persuaded by somebody who
   described their view badly.
3. **It is how you find the real disagreement.** Most arguments that look like arguments about
   facts are arguments about which value gets to win. Naming that is progress. Pretending the
   other side has the facts wrong when they do not is not.

### Three contested questions, with the strongest case on each side

**Should schools use AI writing detectors on student work?**

*For:* teachers face a workload problem they did not create and have almost no other tool.
Students who write their own work are harmed when classmates do not, and a school that does
nothing has decided that honesty costs the honest students something. A detector is imperfect
evidence, and imperfect evidence used carefully is better than no evidence at all.

*Against:* a detector produces a probability score, not a finding, and institutions
consistently treat scores as findings. Its errors are not random: they fall harder on students
who write unusually, including students writing in a second language and neurodivergent
students. The cost of a false accusation to one student is far larger than the benefit of
catching one cheater, and the school has no reliable way to appeal a number.

**Should AI be used to screen job applicants?**

*For:* human screening is already biased, inconsistent, and unauditable. A written rule can
be inspected, tested for disparate impact, and corrected. You cannot audit a hiring manager's
Tuesday afternoon.

*Against:* a system trained on past hiring decisions learns past hiring decisions, and it
applies them to everybody identically and invisibly. Auditability is a property the system
could have, not one it does have, and vendors rarely provide it. One biased screener affects
their own pile. One biased model affects every applicant at once.

**Should a school run models locally at higher cost, rather than using a cloud service?**

*For:* no student data leaves the building, no account is required, nothing depends on a
vendor's retention policy, and the school can inspect what runs. That is a privacy and
control answer that no contract can fully replace.

*Against:* local models are weaker and slower, which means students get a worse tool, and a
worse tool used in class is a real cost to real students today. Money spent on hardware is
money not spent on something else. A well-negotiated contract with a real audit right may
protect students better than hardware somebody has to maintain.

**This course made a choice on that third one and told you why**: commercial developer APIs
require users to be 18 or older, so this course runs locally. That is a constraint-driven
decision, not a claim that the argument is settled.

---

## Intercultural communication: the same argument, a different room

Competency 1.5.7 is about exchanging ideas and creating meaning across cultures. In this
module it has a precise job: **your argument will be read by somebody whose starting
assumptions are not yours, and you do not get to choose who.**

A concrete example you already have the pieces for. The United States approach to data
privacy is largely **sectoral**: separate rules for health, for education, for finance, for
children. The European approach under the GDPR is **rights-based**: a general framework
covering personal data with principles and individual rights that apply across sectors.

Now watch what happens to an argument built on one of those, read by somebody from the other.

- **"There is no law against it"** is a strong move in a sectoral system, where the absence
  of a specific rule for your sector is meaningful. It is a weak move in a rights-based
  system, where a general principle applies whether or not a specific rule names your sector.
- **"Users consented in the terms of service"** carries a lot of weight in one framing. In
  the other, consent is one lawful basis among several, with conditions on how it is
  obtained, and a checkbox is not automatically consent.

Neither framing is foolish and neither is plainly right. **The failure is not knowing which
one your reader is standing in.**

Beyond legal framing, four things worth asking rather than assuming:

- **Directness.** In some settings a blunt "this will not work" is respect for the reader's
  time. In others it is a loss of face for the person who proposed it. The same email reads as
  efficient or rude depending on where it lands.
- **How much context is stated.** Some communication norms put the whole argument in the
  words. Others leave much of it to shared context, and the words look thin to an outsider.
- **Who is authorized to disagree.** A student contradicting an instructor in a meeting is
  normal in some rooms and startling in others. If you run a design review and only some
  people speak, that may be your format rather than their opinions.
- **What counts as evidence.** A number, a published standard, a senior person's judgement,
  and a story about a customer are weighted very differently by different audiences.

**The rule that keeps this from turning into stereotyping: these are questions to ask about
the person in front of you, never predictions to make about them.** "People from X are
indirect" is a stereotype and it will make you wrong about the individual. "I do not know
whether this reader wants the conclusion first or last, so I will ask, or write it so both
work" is intercultural communication.

For your position paper, that produces two concrete requirements. **Name your audience, and
name one assumption they hold that you do not share.** Then write so that the argument still
works for them.

---

## Worked example: does your paragraph argue, or only assert

```python
# steelman_check.py: does this paragraph argue, or does it only assert?
# It checks for the parts of an argument. It cannot check whether they are true.

TESTS = {
    "states a claim": lambda t: any(
        w in t.lower() for w in ("should", "ought", "must", "is wrong", "is right")),
    "gives a reason": lambda t: any(
        w in t.lower() for w in ("because", "since", "the reason", "which means")),
    "points at evidence": lambda t: any(
        w in t.lower() for w in ("study", "record", "data", "measured", "report",
                                 "according to", "we tested")),
    "names who is affected": lambda t: any(
        w in t.lower() for w in ("students", "workers", "artists", "families",
                                 "teachers", "patients", "users")),
    "states the other side": lambda t: any(
        w in t.lower() for w in ("the strongest case", "critics", "opponents",
                                 "granting that", "the best argument against")),
    "answers the other side": lambda t: any(
        w in t.lower() for w in ("that reply fails", "the answer to that",
                                 "this does not hold because", "even so")),
}

PARAGRAPHS = {
    "Version A": (
        "Schools should not use AI writing detectors. People who want them "
        "only care about catching students and do not care about learning. "
        "Anyone who has used one knows they are terrible."
    ),
    "Version B": (
        "Schools should not use AI writing detectors on student work. The "
        "reason is that a detector produces a score, not a finding, and a "
        "school then treats the score as a finding. The strongest case for "
        "detectors is real: teachers have a workload problem and no other "
        "tool at all, and students who write their own work are harmed when "
        "classmates do not. The answer to that is that a tool whose errors "
        "fall hardest on students who write unusually, including students "
        "writing in a second language, transfers the workload problem onto "
        "the students least able to carry it. We tested three samples and "
        "recorded the scores in our log."
    ),
}

for label, text in PARAGRAPHS.items():
    got = sum(1 for check in TESTS.values() if check(text))
    print(f"\n{label}: {got} of {len(TESTS)} parts present")
    for name, check in TESTS.items():
        print(f"   {'yes' if check(text) else 'NO '}  {name}")
print("\nThis counts parts of an argument. It cannot tell you whether the")
print("argument is any good, and it cannot tell you whether it is honest.")
```

Output:

```

Version A: 2 of 6 parts present
   yes  states a claim
   NO   gives a reason
   NO   points at evidence
   yes  names who is affected
   NO   states the other side
   NO   answers the other side

Version B: 6 of 6 parts present
   yes  states a claim
   yes  gives a reason
   yes  points at evidence
   yes  names who is affected
   yes  states the other side
   yes  answers the other side

This counts parts of an argument. It cannot tell you whether the
argument is any good, and it cannot tell you whether it is honest.
```

**Version A and Version B reach the same conclusion.** Version A is the one that gets written
when you already know the answer. Read its second sentence again: it describes the other side
as people who do not care about learning. That is a claim about motives standing where a
reason should be, and it is the exact shape of a straw man.

Version B states the same position and states the case against it in a way a teacher who
wanted a detector would recognize as their own view. **That is the paragraph that can change
somebody's mind.**

**And the program is not the point.** It counts words. You could get 6 of 6 by sprinkling
phrases into Version A without changing a single idea, and the result would be a dishonest
paragraph with a full score. Use it to find missing parts, never to certify a paper.

---

## The wrong version, and what it does instead of an error

Ask a model for "both sides" of a contested AI question and this is a common result:

> **Some people believe AI will transform education for the better, while others worry it
> might have downsides. Supporters point to personalized learning and efficiency. Critics
> raise concerns about accuracy and over-reliance. Ultimately, the truth likely lies somewhere
> in the middle, and it will be important to balance innovation with responsibility as we move
> forward.**

**Nothing is wrong with a single sentence in it, and the whole thing is worthless.**

- **Nobody is named.** Who believes this. Which students gain and which lose. There is no
  actor anywhere in the paragraph.
- **"Downsides" and "concerns" are not arguments.** They are the shape of an argument with
  the content removed.
- **"The truth lies somewhere in the middle" is asserted, not argued.** Sometimes one side is
  right. Deciding in advance that the answer is halfway is not balance, it is a refusal to
  analyze.
- **The last clause is pure filler.** "Balance innovation with responsibility" is compatible
  with every possible policy, which means it recommends none.
- **It is unfalsifiable.** There is no version of the world where that paragraph is wrong,
  which is a reliable sign that it says nothing.

Score it on the five AI Output Evaluation parameters and it fails on **relevance** most of
all. It is on topic and answers nothing that was asked.

## Why the wrong version is tempting

**It sounds fair.** Even-handedness is a real virtue and this is a counterfeit of it. Real
even-handedness means stating both cases at full strength. This states neither.

**It cannot be attacked.** A paragraph with no claim in it cannot be wrong. If your goal is
to avoid criticism rather than to be right, it is the optimal paragraph, and that is worth
noticing about yourself when you catch yourself writing one.

**It is what the model produces by default**, because it is the average of an enormous amount
of writing that does the same thing. **Your position paper is graded partly on not doing
this**, and the rubric's specificity requirement exists for this exact reason.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Steel man** | The strongest version of the other side's argument, stated so its holders would accept it. |
| **Straw man** | The weakest version, effortless to refute and held by nobody. |
| **Ideological Turing test** | Can you state the other side so well that somebody who holds it cannot tell you disagree. |
| **Sectoral privacy framework** | Separate rules by sector: health, education, finance. The United States approach. |
| **Rights-based privacy framework** | General principles and individual rights across sectors. The GDPR's approach. |
| **Disparate impact** | A rule applied to everyone identically that lands differently on different groups. |
| **Automation bias** | Trusting an automated output more than the evidence warrants, because a machine produced it. |
| **Concentration** | Compute, data, and distribution held by a few organizations. |
| **Unfalsifiable** | A statement no possible evidence could count against. A warning sign, not a strength. |

---

## Self-check

**Question 1.** Pick the contested question you feel most strongly about. Write the strongest
case for the side you disagree with, in five sentences, with no hedging and no sentence that
describes the other side's motives. Then read it out loud and ask whether somebody who holds
it would sign it.

**Question 2.** Take the "truth lies somewhere in the middle" paragraph. Rewrite it so it says
something. It has to name at least two specific groups, make one claim that could be wrong, and
state one fact that would change your mind.

**Question 3.** You are presenting your position paper to an audience that starts from a
rights-based privacy framework rather than a sectoral one. Name one argument in your paper
that gets weaker in that room, and say what you would put in its place.

---

### Answers

**1.** No fixed answer. Two things make it right: **no sentence describes the other side's
motives**, and **the case is stated in terms the other side uses about itself.** If your
paragraph contains the words `they just want`, start over.

**2.** For example:

> AI tutoring tools help students who cannot get help any other way, and they will do the
> most for students whose families cannot pay for a tutor. They will also do the most damage
> to those same students, because a student with a tutor has somebody to catch the tool when
> it is wrong and a student without one does not. My claim is that a tool of this kind should
> not be deployed to a school without a way for a student to flag an answer and get a human
> response inside a day. **What would change my mind:** evidence that students who used the
> tool without any human backstop learned as much as students who had one.

It names two groups, makes a claim that could be false, and states the evidence that would
overturn it. **That last sentence is the part that separates an analysis from a position.**

**3.** Many answers. A common one: an argument resting on **"no law prohibits this"** or **"the
terms of service said so"** gets weaker in a rights-based room, where a general principle
applies regardless of whether a sector-specific rule exists, and where consent is one lawful
basis with conditions attached rather than a universal key.

**What to put in its place:** the argument from purpose and minimization. "We collect this
field because the feature cannot work without it, we hold it for this long, and here is what
we refused to collect." That argument works in both rooms, which is what makes it the stronger
one to have built your design on in the first place. You write exactly that argument next
week.
