# Analyzing a Scenario Involving AI
## 145130 Applications of AI · Module 2 · Week 6, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W06_AnalyzingAScenario.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W06_AnalyzingAScenario.pptx)

**Competencies:** 2.14.6 (critically analyze scenarios involving AI usage),
1.1.7 (apply problem-solving and critical-thinking skills when making decisions),
2.14.4 (evaluate an AI result).

---

## Why this exists

For two weeks you have evaluated outputs. This week the thing in front of you is
a situation: somebody used a model, something happened, and you have to say what
you think.

The exam asks this directly. So does every job that uses these tools. And it is
the place where a person with good instincts and no method produces an opinion
that nobody can check, which is worth nothing in a meeting.

**A method is the difference between a verdict and an analysis.** The verdict is
the least interesting part of either.

---

## The six-step method

Do them in order. The order is the method, because steps 1 and 2 are the ones
that get skipped and they are the ones that change the answer.

**1. State what actually happened, with nothing added.**
Facts only, in one short paragraph. No motives, no adjectives. If the scenario
does not say somebody knew something, you do not get to say they knew it.

**2. List what you were not told.**
Every gap that would change your answer. This is the step that separates an
analysis from a reaction, and it is the step nobody does.

**3. Name who is affected, including the people not in the scenario.**
The person who used the tool, the people the output describes, the people who act
on it, and the people who are never mentioned and are affected anyway.

**4. Identify the decision point.**
Somewhere there was a moment where a different choice would have produced a
different outcome. Name it exactly. Usually it is earlier than people think and
it is usually not the moment of using the tool.

**5. Say what should have happened, and what it would have cost.**
A recommendation with no cost is not a recommendation. Time, money, effort,
inconvenience, or a result somebody wanted and does not get.

**6. State what would change your answer.**
One fact that, if it were different, would flip your conclusion. **If you cannot
name one, you have an opinion rather than an analysis.**

---

## Why step 6 is the whole thing

A conclusion you would hold no matter what is not a conclusion about the
scenario. It is a position you brought with you.

Writing down the fact that would change your mind does three things:

- It makes your reasoning checkable by somebody who disagrees.
- It tells you what to go and find out, if you can.
- It stops you defending a verdict when the facts move, which is the most
  expensive habit in professional judgement.

This is the same shape as a testable theory in troubleshooting and the same shape
as a bias test that could come out either way. **A claim that cannot be wrong
cannot be checked.**

---

## Worked example · a scenario, worked all the way through

> **Scenario (a composite, constructed for this lesson from patterns that are
> common in schools; it is not a report of a real incident).**
>
> A junior on the yearbook staff is behind on captions for the sports section.
> She pastes the roster into a locally hosted model along with the game results
> and asks it to write one caption per photo. It produces forty captions in two
> minutes. They read well. She checks six of them against the results sheet, finds
> them correct, and uses all forty.
>
> Two weeks later the yearbook goes to print. One caption says a sophomore scored
> the winning goal in the district semifinal. He did not play in that game. The
> caption named him because his name is next to that game on the roster sheet for
> a different reason: he was listed as a manager that week.

### Step 1 · What happened, nothing added

A student used a model to generate forty captions from a roster and a results
sheet, spot-checked six, used all forty, and one caption stated a false fact
about a named student. It was printed.

**What is not in that paragraph:** that she was careless, that she should have
known, that the model failed. None of those are in the scenario, and two of them
are conclusions.

### Step 2 · What you were not told

- Whether anyone else reviewed the captions before print.
- Whether the yearbook has a fact-checking step at all.
- Whether the roster's "manager" notation was visible in what she pasted.
- Whether the six she checked were chosen at random or were the first six.
- How much time she had, and whether a slower method was available.

**The fourth one matters most and nobody asks it.** If she checked the first six,
she checked the six that were quickest to check, and a spot check that is not random is not a spot
check. That single fact changes what you recommend.

### Step 3 · Who is affected

- **The sophomore.** A false claim about him, printed, permanent, with his name
  on it. He is the person most affected and he is not in the scenario.
- **The junior.** Her work, her name on the section.
- **Readers**, who cannot tell which captions were checked.
- **Next year's staff**, who inherit whatever practice comes out of this.
- **Other students in the roster**, whose data went into a prompt.

### Step 4 · The decision point

Not "when she used the model." Using it was reasonable, it saved real time, and
the output was mostly right.

**The decision point is the spot check.** Six of forty, and a spot check on
generated output is not a sample of a process that is uniformly good or bad. It
is a sample of a process that is right about the common cases and wrong about the
unusual ones. **The manager notation is the unusual case, and an unusual case is
exactly what a small spot check misses.**

There is an earlier decision point worth naming: the yearbook has no
fact-checking step, so this was going to happen with or without a model. A model
made it faster.

### Step 5 · What should have happened, and what it costs

Every generated caption that names a person and an action gets checked against
the results sheet. Forty checks, roughly fifteen minutes.

**The cost is real:** fifteen minutes she did not have, which is why she did not
do it. A recommendation that ignores the reason somebody did not do the right
thing is a recommendation nobody will follow.

**A cheaper version that gets most of the benefit:** check every caption that
names a person, skip the ones that do not. That might be twelve checks rather
than forty.

### Step 6 · What would change the answer

**If the roster she pasted did not distinguish managers from players**, then no
amount of checking the captions against the roster would have caught it, and the
recommendation moves from "check the captions" to "fix the source data." Same
scenario, different fact, different conclusion.

That is what step 6 is for.

---

## The wrong version, and why it is tempting

Here is the analysis that gets written first:

> "She should not have used AI for this. It made up a fact about a real student
> and that is exactly why you cannot trust these tools for anything that matters."

**What is wrong with it:**

- It skips step 1: the model did not make up the student or the game. It drew a
  wrong connection from real data she supplied.
- It skips step 2 entirely, so it cannot be checked.
- It has no cost in it. Forty captions by hand is hours, and the recommendation
  pretends that is free.
- It fails step 6. There is no fact that would change it, which means it is a
  position about AI rather than an analysis of this scenario.

**Why it is tempting.** It is the strongest-sounding sentence available, it takes
thirty seconds, and it is partly right. The partly-right is what makes it
dangerous: it will be graded as analysis by anyone who agrees with it.

**The mirror-image version is equally wrong:**

> "The model was 39 out of 40, which is better than a tired student at midnight.
> The process worked."

Also skips step 3, because the sophomore is not in it, and treats an error rate
as the only thing that matters when the harm is concentrated on one named person.

---

## Presenting a contested question

Some scenarios do not have a right answer, and you will be scored on whether you
noticed.

When the question is genuinely contested, the format is:

1. The strongest version of the case on one side. **The strongest, not the one
   most convenient to knock down.**
2. The strongest version of the other.
3. What you would do, and why, given that both are real.
4. What would change your mind.

**A scored analysis of a contested question that reads as though one side is
beyond argument has lost marks, even if you picked the side the instructor
agrees with.** The reasoning is the assessment.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Scenario analysis** | A structured account of a situation, its gaps, and what follows |
| **Decision point** | The moment where a different choice changes the outcome |
| **Composite** | A constructed scenario built from common patterns, not a real incident |
| **Falsifier** | The fact that would change your conclusion |
| **Stakeholder** | Anyone affected, including people not mentioned |
| **Spot check** | Verifying a sample. Only meaningful if the sample is random |

---

## Self-check

**1.** Why is "what you were not told" a separate step instead of something you
mention if it comes up?

<details><summary>Answer</summary>

Because it will not come up. Under time pressure, the mind treats the scenario as
complete and reasons from what is present. Forcing a list produces gaps you would
not have noticed, and in the worked example the gap about the spot check being
random changes the recommendation.

It is also what makes your analysis checkable. A reader who knows one of your
gaps can tell you, and your conclusion updates instead of being defended.
</details>

**2.** A classmate's scenario analysis concludes "the school should ban these
tools for yearbook work." What single question tells you whether they did step 5?

<details><summary>Answer</summary>

**"What does that cost, and who pays it?"**

A ban costs the hours the tool was saving, and the person who pays is the student
doing the captions at midnight. An analysis that does not price its own
recommendation has not finished, whether or not the recommendation is right.
</details>

**3.** In the worked example, why is the decision point the spot check rather
than the moment of using the model?

<details><summary>Answer</summary>

Because using the model was a reasonable choice that mostly worked, and removing
it does not clearly produce a better outcome. A tired student writing forty
captions by hand at midnight also gets one wrong.

The spot check is where a different choice changes the outcome: six non-random
checks out of forty gave the appearance of verification without its substance.
**A check that produces confidence without producing evidence is worse than no
check**, because it stops anyone else looking.
</details>
