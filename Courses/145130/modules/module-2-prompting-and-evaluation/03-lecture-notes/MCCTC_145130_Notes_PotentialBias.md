# Potential Bias: Whose Perspective Is Built In
## 145130 Applications of AI · Module 2 · Week 5, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W05_PotentialBias.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W05_PotentialBias.pptx)

**Competencies:** 2.14.4 (evaluate an AI result on potential bias), 2.14.6
(critically analyze scenarios involving AI usage), 1.1.7 (problem-solving and
critical thinking).

---

## Why this exists

This is the parameter students score worst on, every year, for a predictable
reason: they use the everyday meaning of the word.

In everyday use, "biased" means unfair, or wrong, or written by someone with an
agenda. In 2.14.4 it means something narrower and more useful, and the narrow
meaning is what the exam assesses and what a professional review needs.

**The narrow meaning:** whose perspective is built into this output, and who is
missing from it.

Not "is it unfair." Not "is it wrong." Who is assumed, and who is absent.

---

## The concept in plain language

Every output describes a default person. Read a paragraph of advice and ask who
it is talking to, and you will find assumptions the text never states: that they
have a ride home, that they have a quiet place to work, that they can read
English at grade level, that they are a student and not a teacher or a parent or
an alum.

Those assumptions are not lies. Every one of them is true of somebody. **The
finding is that the output treats that somebody as everybody**, and a system
built from it will not have a place for anyone else.

**Where it comes from.** A model produces the typical continuation from what it
was trained on. Whoever writes the most on a topic supplies the typical
perspective, and whoever writes the least is absent. Nobody chose that. It is an
average, and an average has no representative in the room.

**A second source, closer to home:** your prompt. A prompt that says "write advice
for students who want to raise their grade" has already decided the reader is a
student, wants a higher grade, and can act to get one. The output inherits every
one of those and adds more.

---

## The three questions that produce a bias finding

Students get stuck because they read looking for something offensive. Read
looking for absences instead, using three questions in this order.

**1. Who is the default person here?**
Write down, in one sentence, who this output assumes it is talking to or about.
If you cannot, read it again for the assumptions it never states.

**2. Who in this building does this not fit?**
Name a real category of person: a student with a job after school, a student who
takes the bus, a teacher, a parent volunteer, an English learner, a student on an
IEP, an alum. Be specific, and pick one you can describe.

**3. Does the output acknowledge them, or is it silent?**
Silence is the finding. An output that says "this assumes you have time after
school, which not everyone does" has done the work. One that never raises it has
built a default and hidden it.

---

## The distinction you must hold

**Potential Bias is not Validity.**

| If your claim is | The parameter is |
|---|---|
| "This statement is false" | Validity |
| "This statement is not true for everyone" | **Usually Validity**, overstating a claim |
| "This assumes a kind of person and is silent about others" | Potential Bias |

The middle row is where most of the class lands, and it is the one to argue about
out loud. "Handwritten notes help you remember more" being overstated is a
Validity problem, and it is fixed by qualifying the claim.

The Bias version of the same sentence is different: **it assumes a reader who can
write by hand, has notes to take, and is in a class where note-taking is the
mode**, and it does not say so. That one is not fixed by qualifying the claim. It
is fixed by acknowledging who the advice is for.

---

## Worked example 1 · The grade level line

From Week 4's runs:

> "Write the borrower's grade level, not their schedule."

**Who is the default person?** A student. Grade level is a property students
have.

**Who does it not fit?** A teacher borrowing a camera for a class. A parent
volunteer at an event. An alum helping at a shoot. None of them has a grade
level.

**Is it acknowledged?** No. The sentence is stated as the rule.

**The finding:** Potential Bias. A checkout sheet built from this has a column
that only students can fill, and the people who cannot fill it will either be
turned away or recorded wrongly. Nothing in the sentence is false.

**The fix, which is what makes it a real finding:** the field is "who is
borrowing this and how do we reach them," and grade level is one way to answer
that for one group.

---

## Worked example 2 · An output with no bias finding

> "Photograph any damage before the item leaves the room."

Run the three questions.

**Default person:** anyone handling equipment. **Who does it not fit?** It
requires a camera, which everyone in the room has, and it requires being able to
see the damage, which is worth a sentence for a student with a visual impairment
and is a stretch. **Acknowledged?** Nothing to acknowledge.

**No bias finding here, and write that down.** "I looked for a Potential Bias
failure in the procedure section and did not find one" is a finding. It tells a
reader you checked.

**Manufacturing a finding to fill the category is its own failure**, and reviewers
do it under pressure to look thorough. It costs credibility, because the reader
who checks your weakest finding decides how much to trust your strongest one.

---

## Worked example 3 · Testing for it rather than arguing about it

An opinion about bias is hard to settle. A test is not.

**The method:** keep the prompt identical and vary exactly one detail about the
person. Record every output. Compare.

```
python ask.py --prompt "Write 4 pieces of advice for a student who is falling behind in a programming class." --label bias_plain
python ask.py --prompt "Write 4 pieces of advice for a student with an after-school job who is falling behind in a programming class." --label bias_job
python ask.py --prompt "Write 4 pieces of advice for a student who takes the bus and is falling behind in a programming class." --label bias_bus
```

```
python compare_runs.py runs --show bias_plain bias_job
```

```
| Label | Prompt words | Reply words | Shape | Hedges |
|---|---|---|---|---|
| bias_bus | 20 | 93 | prose | 5 |
| bias_job | 20 | 93 | prose | 5 |
| bias_plain | 16 | 93 | prose | 5 |
```

**Against the stub these three come back identical**, because the stub
is a caricature and does not model this. Say so in your write-up. That is an
honest negative result about the stub and it is not evidence about a real model.

**Against a real local model this is the whole exercise**, and it is Side Quest 19,
the Bias Audit. The rule there is worth stating now: **a test that can only come
out one way is not a test.** Design it so it could show you nothing, and mean it.

Two hard rules for any bias test in this course: **no real people as subjects, and
no student data in any prompt.** Invented people only.

---

## The wrong version, and why it is tempting

Here is the finding students write, and it is wrong in a specific way:

> "This output is biased because it only mentions American schools."

Read it again. It might be a real finding and as written it is not one, because
it does not say who is harmed by the absence or why it matters here.

Compare:

> "Every example is a US public high school with a 7-period day. Our exchange
> students and any reader outside the US get advice built on a schedule they do
> not have, and the output never says the schedule is an assumption."

Same observation. The second one names the absent group, says what goes wrong for
them, and identifies the unstated assumption. That is a finding. The first is an
observation wearing a finding's clothes.

**Why the short version is tempting.** It is true, it is fast, and it sounds like
analysis. It is also unactionable: nobody can fix a paper based on it, which is
the test for whether you have written a finding.

**The other wrong version, and it is worth naming:** deciding an output is biased
because you disagree with its conclusion. Bias is about what is absent, not about
whether you like what is present. If you find yourself only detecting bias in
outputs you disagree with, you have found a bias in your review process, and
that is the finding.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Potential Bias** | Whose perspective is built in and who is left out |
| **Default person** | The unstated reader or subject an output assumes |
| **Absence** | A group the output never mentions, which is where bias shows |
| **Overstatement** | A true claim extended past its evidence. Usually Validity |
| **Controlled variation** | Changing one detail about the person and comparing outputs |
| **Confirmation** | Only finding what you were already looking for |

---

## Self-check

**1.** "This advice assumes you have a quiet place to study." Is that a Potential
Bias finding as written? What is missing?

<details><summary>Answer</summary>

It is the start of one and it is not complete. It names the assumption, which is
the hard part, and it does not name who that leaves out or what goes wrong for
them.

**Complete it:** a student sharing a room, a student at a relative's house after
school, a student whose quiet hours are at work. For any of them the advice is
not hard, it is inapplicable, and the output never says so. Now it is actionable.
</details>

**2.** An output about study techniques is accurate in every claim and cites real
sources. Can it still have a Potential Bias failure? Give an example.

<details><summary>Answer</summary>

**Yes, and this is the whole point of the parameter being separate.**

Example: every technique it recommends needs materials, time outside school
hours, and somewhere to work. Every claim is true and every source is real. A
student with an evening job can do none of it, and the output does not mention
that the techniques assume free evenings.

Accuracy and inclusion are different properties. An output can be perfect on one
and silent on the other, which is why "is it right" catches this parameter about
never.
</details>

**3.** You suspect a model gives different advice depending on a detail about the
student. Design the smallest honest test, and say what result would show you were
wrong.

<details><summary>Answer</summary>

**The test:** one prompt, three versions differing in exactly one detail about the
person, everything else identical word for word. Run each several times if the
model is not deterministic. Record every output with `ask.py`. Compare on
something countable first: length, how many recommendations, whether any
recommendation appears in one version and not another.

**What would show you were wrong:** the outputs are materially the same across all
three versions. You have to say that in advance and you have to be willing to
report it.

**The failure to avoid:** running it, finding nothing, and going hunting for a
fourth variation until something moves. That turns a test into a search for
confirmation, and the result stops meaning anything.
</details>
