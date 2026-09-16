# Additional Resources · Week 3
## 145130 Applications of AI · Module 1 · Week 3
### Topics: three numbers, a method somebody else can repeat, what a model cannot do, the explainer

Every link below is marked **Confident** or **[VERIFY]**. **Confident** means the address is one
your instructor would bet a class period on. **[VERIFY]** means somebody clicks it before it is
assigned.

**This is the measurement week, so the standard applies to this page too.** A resource list with an
unchecked link on it is a results table with an unmeasured number in it. Both are the same defect,
and Gate 2 W03 is built out of it.

**Module 1 ports.** Stub model server **11634**. Streaming stand-in **11635**. Port 11434 is held
for a real model. Every command on this page passes its port.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Week 3 lecture notes, four files | Mon-Thu | On-level | 20 min each |
| 2 | `bench.py` header comment and `measure.py` | Mon | On-level | 25 min |
| 3 | Official docs: `time.perf_counter` and `timeit` | Mon | On-level | 15 min |
| 4 | Official docs: `statistics.median` | Tue | On-level | 10 min |
| 5 | The streaming stand-in at a known rate, interactive | Mon Tue | On-level | 30 min |
| 6 | MLPerf, the industry version of Tuesday | Tue | Extension | 25 min |
| 7 | plainlanguage.gov | Thu | On-level | 25 min |
| 8 | The contested question, both sides, with sources to find | Wed | Extension | 30 min |
| 9 | A free video on how a language model generates text | Wed | Remediation | under 20 min |
| 10 | Gate 1 Reps 03, 07, 12, 14, 19, 20 | Mon-Fri | Review | 10 min each |
| 11 | All twelve Module 1 lecture note self-checks | Before Fri | Review | 45 min |
| 12 | SQ-20 and SQ-19 | Fri | Extension | one to two blocks |
| 13 | The exit criteria checklist | Fri | Required | 10 min |

---

## 1. Primary reading · the four Week 3 lecture notes

The on-level reading for the week.

- Monday: [`../03-lecture-notes/MCCTC_145130_Notes_ThreeNumbersWorthMeasuring.md`](../03-lecture-notes/MCCTC_145130_Notes_ThreeNumbersWorthMeasuring.md)
- Tuesday: [`../03-lecture-notes/MCCTC_145130_Notes_AMeasurementNobodyCanRepeat.md`](../03-lecture-notes/MCCTC_145130_Notes_AMeasurementNobodyCanRepeat.md)
- Wednesday: [`../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md`](../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md)
- Thursday: [`../03-lecture-notes/MCCTC_145130_Notes_ExplainingItWithoutTheWordMagic.md`](../03-lecture-notes/MCCTC_145130_Notes_ExplainingItWithoutTheWordMagic.md)

**Read Monday's note before Monday.** It is the one note in the module whose arithmetic you have to
be able to do from memory, because the
[performance task](../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md) depends on it and
because the common wrong method looks completely reasonable on the board.

**Wednesday's note is the one to reread before the exit assessment.** It is the only place in the
module that gives you the contested question with both sides written out at their strongest, and
printing either side as a fact is a defect the module grades you on.

**Thursday's note is the writing instruction for the explainer.** Its worked example 3 is a draft
being cut, shown at each cut. If your explainer is a page of confident sentences you could not
defend, that section is the fix.

**Time.** About 20 minutes each. **Level.** On-level.

---

## 2. Primary source · the header of `bench.py`, and `measure.py`

[`../05-labs/lab-m01-04-files/bench.py`](../05-labs/lab-m01-04-files/bench.py) and
[`../05-labs/lab-m01-04-files/measure.py`](../05-labs/lab-m01-04-files/measure.py) ·
**Confident**, they are files in this repository.

**What it is.** `bench.py` is finished and its opening comment is the written specification for the
three numbers: what each one measures, who feels it, and what the program refuses to do. `measure.py`
is the arithmetic, and it is the part you write.

**Why this one.** It is a primary source for the thing you are being graded on, and it is thirty
lines of prose rather than thirty pages. It also states, in writing, why the program posts straight to
the model endpoint: measure one layer at a time, so that a slow answer can be attributed to
something.

**Assign a question.** *Find the section of the header comment headed with what the program refuses
to do. Name one refusal, and say what a report would claim if the program had not refused.*

**Second question, for Monday.** *`measure.py` returns `None` in four cases rather than returning
zero or guessing. Find one of them. Say what a column of zeros would have made a reader believe.*
The misconception this whole lab exists to prevent is reading `n/a` as a broken program. It is a
correct answer to a question nobody could answer.

**Time.** 25 minutes. **Level.** On-level.

---

## 3. Official documentation · `time.perf_counter` and `timeit`

`https://docs.python.org/3/library/time.html#time.perf_counter` · **Confident.**
`https://docs.python.org/3/library/timeit.html` · **Confident.**

**Why these two.** `bench.py` times everything with `time.perf_counter`, and the documentation says
why in one sentence about resolution and about the clock not going backwards. If you have ever timed
something with a wall clock and got a negative number, that sentence is the reason.

**Assign a question.** *Read what `perf_counter` says about its reference point. Why does that mean
you may subtract two readings but may never report one of them on its own?*

**Second question, and it is the interesting one.** *The `timeit` documentation describes a standard
way to time small pieces of Python. Read its notes on what it does to get a reliable number. Then say
why `bench.py` does not use it.* The answer is in the difference between timing your own code and
timing somebody else's server over HTTP, and getting there yourself is worth more than being told.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. Official documentation · `statistics.median`

`https://docs.python.org/3/library/statistics.html#statistics.median` · **Confident.**

**Why this one.** Tuesday's lesson reports a median rather than an average, and the lecture note says
why: one machine that paused for a garbage collection drags an average and leaves a median alone.
Reading the definition of both in the standard library makes that concrete rather than a rule you
were handed.

**Note what `measure.py` does.** It implements its own median rather than importing this one.
**Assign a question:** *Read both. Do they agree on the even-length case? Show it with four numbers.*
If they disagree, that is a defect worth reporting, and reporting it is worth more than the lab.

**Time.** 10 minutes. **Level.** On-level.

---

## 5. Interactive practice · the streaming stand-in at a known rate

[`../05-labs/lab-m01-04-files/streaming_stub.py`](../05-labs/lab-m01-04-files/streaming_stub.py) ·
**Confident**, it is a file in this repository.

**What it is.** A server that streams a chosen number of tokens at a chosen rate, with a chosen delay
before the first one. You know the right answer before you measure, which is the only way to find out
whether your measuring program is correct.

**Run one, and it is the best thirty minutes on this page:**

```
python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 300
```

```
python bench.py --label known-rate --repeats 3 --model streaming-stub --endpoint http://127.0.0.1:11635 --hardware "your machine, streaming stand-in at 40 tokens per second"
```

**What to look at.** The stand-in was set to 40 tokens per second. Your report should land near 40
and near 300 ms to first token. If it reports near 30, your divisor is total latency rather than
generation time, and the wrong number looks completely reasonable.

**Then change one thing and predict first.** Set `--first-delay-ms 900` and write down, before you
run it, which of the three numbers moves and which two do not. Then run it.

**Why this one.** Every other benchmark you will ever read was produced against a system whose true
rate nobody knew. This one has a true rate printed on the command line. Measuring something whose
answer you already know is how you find out that your instrument lies.

**Anchor the stub first.** Running the non-streaming stub on 11634 gives you `n/a` in the time to
first token column, and that is correct rather than broken. A server that does not stream cannot tell
you when the first token arrived.

**Time.** 30 minutes. **Level.** On-level.

---

## 6. The industry connection · MLPerf

**MLCommons** · `https://mlcommons.org/` · **Confident** for the site. The benchmark listing at
`https://mlcommons.org/benchmarks/` · **[VERIFY].**

**What it is.** An industry consortium that publishes benchmark suites for machine learning,
including inference benchmarks, with rules about what a submitted result has to disclose.

**Why this one.** Tuesday's lesson is that a difference between two numbers is a fact about two whole
situations, and that seven things are the method. MLPerf is that argument taken seriously by an
industry with money on the outcome. The reason their rules are long is the reason your partner
negotiation on Tuesday takes fifteen minutes with no keyboards.

**Assign a question.** *Find any rule about what a submission must disclose. Which of Tuesday's seven
method items does it correspond to? Find one thing they require that your method did not, and say
whether your comparison survives without it.*

**If the deep address does not resolve**, search the site for "inference" from the front page. Do not
substitute a news article about MLPerf for MLPerf. A summary of a standard is not the standard, which
is Week 2's lesson arriving again.

**Time.** 25 minutes. **Level.** Extension.

---

## 7. Writing the explainer · plainlanguage.gov

`https://www.plainlanguage.gov/` · **Confident** for the site. The guidelines at
`https://www.plainlanguage.gov/guidelines/` · **[VERIFY].**

**What it is.** The United States federal government's plain-language guidance, written for people
who have to explain complicated things to members of the public who did not choose to read about
them.

**Why this one rather than a style guide.** Your reader is a named adult who has never programmed and
is not obliged to care. That is the same reader this guidance was written for. It is free, it has no
product, and it is specific: it tells you to name your audience first, which is exactly what
Thursday's lecture note tells you.

**Where it does not apply, and say this out loud.** Plain language guidance will tell you to shorten.
Thursday's worked example shows a 41-word draft being replaced by a longer one that says more.
**Short is not the goal. Defensible and understood is the goal**, and a sentence that is short because
it dropped the true part is the failure this module names. Take the audience discipline from this
site and take the honesty standard from the lecture note.

**Assign a question.** *Find any one guideline you disagree with for this particular explainer. Say
what it would cost you to follow it.*

**Time.** 25 minutes. **Level.** On-level.

---

## 8. The contested question, with sources you have to find yourself

Wednesday's third item is contested, and the module grades you on giving the other side its strongest
form before you disagree with it. That means you need to read somebody who holds it.

**Start with the lecture note**,
[`../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md`](../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md),
the section that gives the strongest case on each side and the section on what is actually settled.
**Confident**, it is a file in this repository.

**Then find one published argument on each side, and this is the assignment.** No links are supplied
here, for two reasons. The first is that no external address on this question was confirmed live, and
a fabricated citation in the module that teaches citation would be the worst artifact in the course.
The second is that finding them is competency 1.2.1 doing real work.

**One paper often cited on the sceptical side is known by the phrase "stochastic parrots" in its
title. [VERIFY] the full title, the authors, the venue, and the year before you cite it**, and record
where you looked. If you cannot verify it, say so in your write-up and cite something you can. That
is a passing answer. Citing it from memory is not.

**What you are looking for on each side.**

- On the sceptical side: an argument that rests on the mechanism, rather than on a list of mistakes.
  A list of mistakes is evidence about this model, not about the question.
- On the other side: an argument that the word "understand" has never been defined precisely enough
  to test. That is the strongest form, and it is not the same as claiming the model does understand.

**What to write.** The sentence you would print in a report, which almost certainly names what is
settled and leaves the rest open. Both of the other two limits follow from the mechanism and are not
contested. Put those in the report as facts.

**Time.** 30 minutes. **Level.** Extension.

---

## 9. A free video, under 20 minutes

**[VERIFY]. No specific video is linked here, because none was confirmed live.** A made-up link on
this page would be a fabricated citation in the module about fabricated citations.

**What to search for, and what to check before assigning it.** A video that shows a language model
producing text one token at a time, with the next-token probabilities visible. Watch it yourself
first, and check four things:

1. Does it show tokens rather than words? A video that says "the model predicts the next word" has
   dropped the thing Week 1 Wednesday was about.
2. Does it distinguish training from inference, and say that inference changes nothing?
3. Does it claim the model looks anything up? There is no lookup step, which is why there is no
   warning when the answer is invented.
4. Does it settle the contested question in either direction as though it were settled? If it does,
   play it anyway and stop it there. That is a two-minute Gate 2 exercise and a better use of the
   video than watching it through.

**A safer substitute if the search fails.** Run the streaming stand-in on port 11635 with
`--delay-ms 200` and watch the tokens arrive one at a time on your own screen. You will not see the
probabilities, and you will see the shape.

**Level.** Remediation.

---

## 10. Gate 1 reps worth redoing on your own

From [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md).

- **Rep 03** (TRACE): tokens per second, both divisions written out. **Do this one until it is
  automatic.** It is on the exit assessment in some form and it is the arithmetic the project rests
  on.
- **Rep 07** (FIX): the function that divides by total latency, and what it must return when there is
  no time to first token
- **Rep 12** (WRITE): `generation_ms`, which returns `None` in two different situations. Both of them.
- **Rep 14** (WRITE): two sentences explaining a token to an adult, defining every technical word in
  the same sentence. This is the explainer in miniature.
- **Rep 19** (EXPLAIN): the vendor's 42 tokens per second, and the minimum you would need
- **Rep 20** (EXPLAIN): the contested question, both sides, in six sentences or fewer

**Ten minutes each, plain editor, no AI.** If you can do Reps 03, 14, and 20 cold, you can tick all
three exit criteria.

**Level.** Review.

---

## 11. The twelve self-checks, before Friday

Every Module 1 lecture note ends with three self-check questions and worked answers, in
[`../03-lecture-notes/`](../03-lecture-notes/). Twelve notes, thirty-six questions.

**Before Friday's exit assessment you should be able to answer all thirty-six without reading the
answers first.** That is the single best review available and it takes about forty-five minutes.

The ones most worth the time if you have less than that:

- Rules against weights, question 2
- Where the model runs, question 2
- Tokens and the context window, question 3
- Training and inference, question 3
- Three numbers worth measuring, question 1
- Three things a model cannot do, question 3

**Level.** Review.

---

## 12. Side quests

Both from
[`../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md).

**SQ-20 Explain It to a Seventh Grader.** One block, one star. A recorded five-minute explanation for
a twelve-year-old, finished when an actual younger person can answer three comprehension questions
afterward. This is the module's exit criterion with a harder audience and a real test attached. If
your explainer got a grade but you are not sure it worked, this tells you.

**SQ-19 The Bias Audit.** Two blocks, three stars. A repeatable test for bias in a locally hosted
model's output, at least thirty recorded outputs, with a written method anybody could rerun. **The
rules matter: no real people, no student data, no classmates as subjects.** It is the natural
continuation of Tuesday, because the hardest part is designing a test that could come out either way,
and a test that can only confirm what you already believed is not a test. It leans on Module 2, so
start it only if Module 1 is finished.

**Level.** Extension.

---

## 13. The exit criteria checklist

[`MCCTC_145130_ExitCriteria_M01.md`](MCCTC_145130_ExitCriteria_M01.md) · **Confident**, it is a file
in this folder.

You get it on Friday and nobody collects it. **Read it on Monday instead.** It states the three things
you have to be able to do by the end of the module, what each one looks like when you can do it, what
a weak version looks like, and exactly where to go if you cannot do it yet. Finding out on Monday
which of the three is your weak one gives you four days. Finding out on Friday gives you Period 8.

**Level.** Required of everyone.

---

## For the student who is behind

1. Rep 03, done on paper until the two divisions are automatic
2. Monday's lecture note, the arithmetic section, and `measure.py` next to it
3. The streaming stand-in run at a known rate, once, with the numbers written down
4. Wednesday's lecture note, the two limits that follow from the mechanism. **Leave the contested one
   for last** and give it the shortest honest treatment you can defend.
5. Rep 14, which is the explainer in two sentences

## For the student who is ahead

- Lab M01-04 EXTENDED, the five-token and two-hundred-token runs, and what tokens per second does at
  each end
- A three-way comparison with two partners, and the method negotiation that has to survive three
  people
- The `timeit` question in section 3, answered in writing
- MLPerf's disclosure rules against your own method, item by item
- SQ-20, then SQ-19
