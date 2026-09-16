# SQ-19 · The Bias Audit
## 145130 Applications of AI · Unlocks Module 3, Week 7

**Time:** two blocks. **Difficulty:** ★★★
**Competencies:** 2.14.2 (analyze how AI technology impacts society and the ethical implications
of its usage), 2.14.4 (evaluate an AI result on validity, relevance, authenticity, potential bias,
and hallucinations), 2.14.6 (critically analyze scenarios involving AI usage).

**A note on the catalog entry.** The Side Quest Catalog lists this quest's competencies as
2.14.2, 2.14.4, and 1.5.5. **1.5.5 is not in the 145130 competency reference**, which contains
1.5.7 rather than 1.5.5 under Global Environment. This bundle claims only codes that appear in
`Courses/145130/_source/COMPETENCY_REFERENCE.md`. See the note at the bottom of this file.

---

## The quest

Design a repeatable test for bias in a locally hosted model's output. Ask for the same kind of
thing many times, varying exactly one detail, and record what changes.

**The hardest part is designing a test that could come out either way.** A test that can only
confirm what you already believed is not a test, and this bundle is built to make that failure
visible rather than to lecture you about it.

---

## The rules, and they are not negotiable

1. **No real people.** No classmates, no teachers, no public figures, no names of anybody who
   exists.
2. **No student data.** Nothing from a roster, a gradebook, a chat, or a form.
3. **No classmates as subjects.** You are testing a model, not people.
4. **The method has to be reproducible from what you wrote.** Somebody who has never spoken to you
   should be able to run your probe and get comparable numbers.
5. **Every command passes `--port`.** This quest uses **11634**. A real Ollama listens on 11434 and
   so do several stubs in this course, and a run against the wrong server looks exactly like a
   working run.

---

## What is in this bundle

| File | What it is |
|---|---|
| `stub_model_server.py` | A calibration target. Not a model and not pretending to be one. |
| `bias_probe.py` | The harness. One template, one hole, a list of values, n repetitions, raw output to a file. |
| `analyze.py` | Counts what came back per variant. Decides nothing. |
| `instructor/` | Kept private by the publisher. Do not look for it. |

---

## Part 1: calibrate the instrument before you point it at anything

**This is the part people skip and it is the reason most bias audits are worthless.**

You are about to build a measuring device. Before you measure something unknown with it, you
measure two things you already know the answer to: **something with no signal**, and **something
with a signal you were told about in advance.**

### Step 1. Start the stub in neutral mode

```
python stub_model_server.py --port 11634 --mode neutral
```

It prints, at startup:

```
NO SKEW. One third each, whatever the prompt says.
If your probe reports a skew here, your probe is wrong.
```

### Step 2. Run the probe and the analysis

In a second terminal:

```
python bias_probe.py --port 11634 --n 10
python analyze.py probe-results.csv
```

**Here is a real run, from the build machine, against a server with no skew at all:**

```
variant            encouraging_ask  encouraging_practice          discouraging                 error          unclassified   total
----------------------------------------------------------------------------------------------------------------------------------
physics                    1 (10%)               2 (20%)               7 (70%)                0 (0%)                0 (0%)      10
history                    4 (40%)               5 (50%)               1 (10%)                0 (0%)                0 (0%)      10
Spanish                    4 (40%)               4 (40%)               2 (20%)                0 (0%)                0 (0%)      10
art                         0 (0%)               6 (60%)               4 (40%)                0 (0%)                0 (0%)      10
```

**Read the physics row. Seventy percent discouraging, against ten percent for history.**

There is no bias in that server. The declared behaviour is one third each, regardless of the
prompt. **That table is noise, and it looks exactly like a finding.**

If you had run ten repetitions, seen that, and written it up, you would have published a result
that is not there. **Nothing in the output would have told you.**

### Step 3. Now run it against a known signal

```
python stub_model_server.py --port 11634 --mode tilted
```

It prints the skew at startup, in full, so you know the answer before you measure:

```
SKEW, declared up front so you can check your probe against it:
  when the prompt contains 'physics', the reply weights are
    ask        20%
    practice   20%
    different  60%
  otherwise they are one third each.
```

**Real run, ten repetitions, against that server:**

```
physics                    4 (40%)               2 (20%)               4 (40%)                0 (0%)                0 (0%)      10
history                    4 (40%)               4 (40%)               2 (20%)                0 (0%)                0 (0%)      10
Spanish                    6 (60%)               1 (10%)               3 (30%)                0 (0%)                0 (0%)      10
art                        4 (40%)               5 (50%)               1 (10%)                0 (0%)                0 (0%)      10
```

**Forty percent, against a real skew of sixty.** And Spanish, which has no skew at all, came in at
thirty.

**Put the two tables side by side.** The server with no bias produced a bigger-looking result than
the server with bias. That is the whole of Part 1 and you should write it down in your own words
before going on.

### Step 4. Find out how many you actually need

Raise `--n` until the known signal comes out of the noise. **Real run, fifty repetitions per
variant, against the same tilted server:**

```
physics                   10 (20%)               8 (16%)              32 (64%)                0 (0%)                0 (0%)      50
history                   20 (40%)              17 (34%)              13 (26%)                0 (0%)                0 (0%)      50
Spanish                   17 (34%)              13 (26%)              20 (40%)                0 (0%)                0 (0%)      50
art                       17 (34%)              14 (28%)              19 (38%)                0 (0%)                0 (0%)      50
```

**Sixty-four percent against a declared sixty.** The signal is there and it is clear.

**Write down the number you needed.** That number is a property of your probe and of the size of
effect you are looking for, and it is the single most useful thing you will produce today.

**The quest's minimum is 30 recorded outputs. Part 1 exists to show you that 30 is a minimum and
not a sufficient number**, and your write-up has to say what you did about that.

---

## Part 2: design your own probe

Now change `bias_probe.py`. Checklist item 1 marks the two things you edit: the template and the
list of variants.

### Choose a probe design

Three, in increasing order of how carefully you have to handle the result.

**Design A: the subject.** The one shipped in the bundle. One prompt asking for encouragement, one
hole, four school subjects. Nothing about it touches a person's identity, and it still finds real
patterns: models do produce different advice about different fields.

**Design B: the situation.** Vary something about the circumstances rather than the person. A
student who has missed three weeks for illness, for a family matter, for a suspension, for a sports
trip. **This one is harder and better.** It measures whether a model's advice changes with a reason
it was told, which is closer to how these systems actually get used.

**Design C: the person.** Vary an invented name, an invented pronoun, or an invented background.
**This is what real bias audits do and it is the one that requires the most care.**

**If you choose Design C, three additional rules:**

1. **Every name is invented.** Not a classmate, not a teacher, not anybody.
2. **Write down, before you run anything, what you will do if the result is inflammatory.** The
   answer is: take it to your instructor before it goes anywhere, including into a presentation.
3. **Your write-up may not claim the cause.** You will have measured a difference in output. You
   will not have measured why, and the gap between those two is enormous.

### Then

- **Write your categories in `analyze.py` before you run the probe.** Commit that file first. The
  commit timestamp is your evidence, and the quest asks for it.
- **Run it. Record everything, including errors.** The harness writes `ERROR` rows on purpose and
  deleting them changes your denominator without telling anybody.
- **Read the unclassified pile.** That is where the thing you did not expect is hiding, and the
  analysis prints a count of it for exactly that reason.

---

## Part 3: point it at a real model

**If a locally hosted model is available on your lab machine**, point the probe at it. Change
nothing else. Same template, same variants, same repetition count, same categories, same file.

```
python bias_probe.py --port <the real model's port> --n 30
```

**Use the real model's own port, not 11634**, and write the port you used in your method. A run
against the wrong server produces results and tells you nothing.

**If no model is available**, that is a complete version of this quest. Part 1 and Part 2 against
the stub, with the calibration result, is a real piece of methodology work. **Say so in your
write-up rather than implying you tested a model you did not have.**

---

## Done when

- [ ] Your method is written clearly enough that somebody else could rerun it: template, variants,
      repetition count, port, categories, and the order you did things in
- [ ] At least **30 recorded outputs**, in a file, raw, errors included
- [ ] The calibration result from Part 1 is in your write-up, with both tables
- [ ] You state the number of repetitions you needed to see the known signal
- [ ] **Your conclusion separates what you measured from what you suspect**, in those words
- [ ] `analyze.py` was committed before `probe-results.csv` existed
- [ ] It lives in a repository with a README a stranger can follow
- [ ] You can explain every line you changed

---

## The three sentences your write-up has to contain

Somewhere in it, in your own words:

1. **"I measured this."** A difference in counts, per variant, with the numbers.
2. **"I did not measure this."** Whether the difference is larger than noise, whether it is bias,
   and what caused it. **Three separate things and a count answers none of them.**
3. **"Here is what would change my conclusion."** A result that would count against you.

**A write-up that says "the model is biased against X" has failed this quest**, however large the
difference was, because that sentence claims a cause. **"Prompts containing X produced
discouraging replies N percent of the time against M percent for the others, over K repetitions,
and I do not know why" is the same finding stated honestly**, and it is the one a professional
would put their name on.

---

## If it breaks

**`bias_probe.py: error: the following arguments are required: --port`**
Correct, and deliberate. There is no default port in this bundle. Pass `--port 11634`.

**`errors: 8` and every row says `ERROR unreachable`**
Nothing is listening on the port you gave. Start the stub in another terminal, and check the port
number in both windows matches.

**Your results change every time you run it.** They should. Pass `--seed` to the stub to make a run
repeatable while you are developing, and then **take the seed off for your real runs**, because a
single seed is one sample and reporting it as your result is the same error as running n equals 10.

**`No file at probe-results.csv. Run bias_probe.py first.`**
The analysis reads the file the probe writes. Run them in that order.

**Everything lands in `unclassified`.** Your category markers do not match what the model actually
says. **Read ten replies, then fix the markers, then note in your write-up that you changed the
categories after seeing data** and say what you did to avoid fitting them to the answer you wanted.

---

## Note on the catalog competency codes

The Side Quest Catalog entry for SQ-19 lists **1.5.5**. That code is in the 145060 competency
reference, where 1.5.5 is "recognize the ways in which bias and discrimination may influence
productivity and profitability."

**It is not in the 145130 competency reference.** The 145130 document has 1.5.7, intercultural
communication, under Global Environment, and no 1.5.5.

This bundle therefore claims 2.14.2, 2.14.4, and 2.14.6, all of which are in the 145130 reference.
**This is a note for the instructor, not a correction anybody should make silently.** The catalog
is a shared file and the discrepancy should be resolved there.
