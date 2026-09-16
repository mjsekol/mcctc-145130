# Module 1 Exit Criteria
## 145130 Applications of AI · Module 1 · Foundations of Artificial Intelligence
### Three things you can do by the end of this module

**Nobody collects this page.** You get it in Week 3, Friday, and the honest use of it is to read it in
Week 1 instead. Finding out on Monday which of the three is your weak one gives you the rest of the
module. Finding out on Friday gives you Period 8.

**Why these three and not others.** They are the three the syllabus commits to, in the syllabus
wording, and each one is a thing you do rather than a thing you have seen. You can sit through every
period of this module and still not be able to do any of them, which is why the check exists
separately from your grade.

**The course rule behind all three.** The only way to fail outright is submitting work you cannot
explain. Every criterion below is a form of explaining, including the one that looks like arithmetic.

**Module 1 ports.** Stub model server **11634**. Streaming stand-in **11635**. Port 11434 is held for
a real model. Pass the port on every command.

---

## Criterion 1

> **Explain to a non-technical adult what a language model does, without using the word magic.**

### What it looks like when you can do this

You can talk for two minutes to somebody who has never programmed, and at the end they can say back
to you, in their own words, roughly what happened when they typed a question into an assistant.

Specifically, you can get four things across without a diagram:

1. **Text goes in as tokens**, which are pieces usually smaller than words, and you can define the
   word token in the same sentence you first use it.
2. **The model produces text one token at a time**, each one chosen from the text it has been given so
   far, and nothing is looked up.
3. **Training happened once, elsewhere, and set the weights. Inference is what runs when you press
   enter, and it changes nothing.** This is why a correction you type does not stick.
4. **Any feeling of memory is a program re-sending your earlier words**, not the model remembering
   you.

You spend at most three technical words on purpose, and you define each one on first use. You make no
claim you could not defend if the adult pushed back.

### The self-test you can run alone

**Write the four sentences from memory, on paper, with no notes and no computer. Ten minutes.**

Then read them out loud and mark every sentence that fails one of these:

- It contains a technical word you did not define in that same sentence.
- It contains a claim you could not defend if somebody asked "how do you know?"
- It contains the word **magic**, the word **brain**, the word **thinks**, or the word **knows**.
- It says the model looked something up, searched, or remembered.

**Then the real test, and it is the one that counts.** Read it to an actual adult who has never
programmed. A parent, a neighbour, a teacher from another pathway. **They are not allowed to ask
clarifying questions.** Afterwards, ask them to tell you what a language model does. If what comes
back is not close, the explainer is not finished, and which sentence broke is now obvious to you in a
way it was not before.

### What a weak version looks like

- **"It is basically a really smart autocomplete that has read the whole internet."** Confident,
  memorable, and it makes two claims you cannot defend. "Smart" is doing work you did not pay for,
  and "the whole internet" is a number you do not have.
- **A page of correct sentences with no audience.** Thursday's note calls this out. If the first line
  does not name who is reading, you wrote it for yourself.
- **Simplifying into something false.** "It remembers your previous questions" is understandable and
  wrong. The true version is one sentence longer.
- **Reciting the word token without defining it**, and then using vector, parameter, and inference in
  the next three sentences. Three technical words is a budget, not a suggestion.
- **Using the word magic ironically.** "It is not magic, it is math" is still a sentence whose content
  is the word magic. Say what it actually does instead.

### If you cannot do this yet

| Go to | Where |
|---|---|
| **Lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_ExplainingItWithoutTheWordMagic.md`](../03-lecture-notes/MCCTC_145130_Notes_ExplainingItWithoutTheWordMagic.md), worked example 1 (the same idea at three distances) and worked example 3 (a draft being cut) |
| **Second lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_TokensAndTheContextWindow.md`](../03-lecture-notes/MCCTC_145130_Notes_TokensAndTheContextWindow.md), self-check question 3, which is this criterion in two sentences |
| **Third lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md`](../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md), the section headed with the sentence that answers the exit criterion |
| **Lab** | [`../05-labs/MCCTC_145130_Lab_M01-01_RulesVersusWeights.md`](../05-labs/MCCTC_145130_Lab_M01-01_RulesVersusWeights.md), step 11 question 5, which is where the difference between a rule and a fitted model stops being a slide |
| **Gate 1 rep** | **Rep 14** (WRITE), two sentences explaining a token to an adult with every technical word defined in the same sentence. Then **Rep 17** (EXPLAIN), training against inference in five sentences. Both in [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md) |
| **Side quest** | SQ-20 Explain It to a Seventh Grader, in [`../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md). Harder audience, real comprehension test |

---

## Criterion 2

> **State three things a language model cannot do, and why.**

### What it looks like when you can do this

You can name three limits, and for each one you can say **where it comes from**, not only that it
exists. A limit with no mechanism behind it is a rumour you repeated.

Two of the three follow from how the thing works, and you should be able to state those as facts:

1. **It cannot tell you where an answer came from.** There is no lookup step, so there is no record to
   report. That is also why a fabricated citation arrives with the same confidence as a real one, and
   why no warning is possible.
2. **It cannot be relied on to be exact.** Counting, totalling, and precise recall are not what the
   mechanism does, and a program that needs an exact number has to get it from somewhere that
   computes it.

**The third one is contested, and this is the part the module grades hardest.** Whether the model
understands anything is an open argument. You can do this criterion when you can give the strongest
version of the side you disagree with **before** you disagree with it, and when you can say what is
actually settled and what is not.

For each limit you can also name **the design that contains it**. A limit you cannot design around is
a complaint. A limit you can design around is engineering. If the model cannot be exact, the program
computes the total and asks the model only for the wording.

### The self-test you can run alone

**Three limits, on paper, no notes, ten minutes.** For each one write three things:

- the limit, in one sentence
- **why**, naming the mechanism rather than an example
- the design that contains it, naming what your program does instead

**Then the harder half.** Take the contested one and write the strongest case for the side you do not
hold, in three sentences, with no "but" at the end. Read it back. **If somebody who holds that view
would recognise it as their own argument, you can do this criterion. If it reads as a straw version
you set up to knock down, you cannot yet.**

**A second check, five minutes.** Take one of your two mechanism-based limits and ask: could I show
this on the stand-in on my desk? The exactness limit is showable. The provenance limit is showable in
a different way, by looking at the reply. Three fields come back, `model`, `response`, and `done`, and
none of them says where inside the model the answer came from. The `how` field your own program
records says how **you** got a value out of the text. Nothing anywhere says where the text came from,
and nothing ever will.

### What a weak version looks like

- **Three examples instead of three limits.** "It got the date of the fire drill wrong" is evidence
  about one answer. The limit is the reason it could not have known.
- **"It hallucinates."** One word doing the work of a mechanism. Say what a hallucination is, why
  there is no warning, and what your program does about it.
- **"It cannot do math."** Too strong and slightly wrong, which is worse than either. It can produce
  correct arithmetic often. It cannot be relied on to, which is a different claim and the one that
  changes your design.
- **Settling the contested question in either direction.** Writing "it does not understand anything,
  it is only autocomplete" as a fact is a defect. So is writing that it understands. Both get marked.
- **Naming a limit that is really a policy.** "It will not tell you how to build a weapon" is a choice
  somebody made in a product, not something the mechanism cannot do.
- **Three limits that are the same limit.** Cannot cite, makes up sources, and gets references wrong
  are one limit written three ways.

### If you cannot do this yet

| Go to | Where |
|---|---|
| **Lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md`](../03-lecture-notes/MCCTC_145130_Notes_ThreeThingsAModelCannotDo.md). Read the two mechanism sections first, then the section that gives the strongest case on each side of the contested one, then the section on what is actually settled |
| **Second lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_ExtractValidInformationAndCite.md`](../03-lecture-notes/MCCTC_145130_Notes_ExtractValidInformationAndCite.md), worked example 3, a fabricated citation and how it gets through |
| **Third lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md`](../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md), for why there is no lookup step to report |
| **Lab** | [`../05-labs/MCCTC_145130_Lab_M01-03_InfographicAutopsy.md`](../05-labs/MCCTC_145130_Lab_M01-03_InfographicAutopsy.md). Every finding on it is one of these limits showing up in a real-looking artifact. Summary question 4 is the contested argument |
| **Gate 1 rep** | **Rep 20** (EXPLAIN), the "only autocomplete" sentence argued both ways in six sentences or fewer, and you are not graded on which side you prefer. Then **Rep 19** (EXPLAIN), the vendor's unusable number. Both in [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md) |
| **Gate 2** | [`../07-gate2-adversarial/MCCTC_145130_Gate2_W01.md`](../07-gate2-adversarial/MCCTC_145130_Gate2_W01.md), redone from the start after the reveal, scoring yourself before you read your old answers |

---

## Criterion 3

> **Run inference locally and report tokens per second.**

### What it looks like when you can do this

**Alone, on a lab machine, with nobody helping**, you can start a model server, run a measured
request against it, and report a number you can defend.

That breaks into four things:

1. **You can start a server on this module's ports.** The stand-in on 11634, the streaming stand-in
   on 11635, and you pass the port explicitly rather than accepting a default.
2. **You can tell a working run from a run against the wrong server.** You know that a stand-in with
   no `--port` lands on 11434, where nothing in this module is looking, and you know what your
   program prints when nothing answers.
3. **You can compute tokens per second correctly.** Generation time is total latency minus time to
   first token. Dividing the token count by total latency reports a rate the model never ran at, and
   the wrong number always looks reasonable.
4. **You can say what your number does not establish.** It is one prompt set, one repeat count, one
   machine, one warm-up policy. A difference between your number and somebody else's is a fact about
   two whole situations until the method matches.

### The self-test you can run alone

**Thirty minutes, one machine, no help, no notes.**

Start the stand-in at a rate you choose and write the rate down before you run anything:

```
python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 300
```

```
python bench.py --label self-test --repeats 3 --model streaming-stub --endpoint http://127.0.0.1:11635 --hardware "lab machine, self-test"
```

**The check.** The stand-in was set to 40 tokens per second, so your report should land near 40 and
near 300 ms to first token. **If it reports near 30, your divisor is wrong.** That is the whole
criterion in one number.

**Then the part that is not arithmetic.** Write three sentences: what you measured, what the number
means for somebody waiting at a screen, and one thing the number does not establish. If the third
sentence is hard, reread Tuesday's note rather than writing something vague.

**A second self-test, five minutes, and it catches the most common failure.** Start the non-streaming
stub on 11634 and run the benchmark against it. Your time to first token column will read `n/a`.
**Say out loud why that is correct.** A server that does not stream cannot tell you when the first
token arrived, and a zero there would be a made-up number.

**A third, one minute.** Do Rep 03 on paper. A run reports 90 tokens, 3000 ms total, 600 ms to first
token. Write both divisions. If you have to think about which is which, you are not finished.

### What a weak version looks like

- **A number with no method.** "My machine runs at 38 tokens per second" is the vendor sentence from
  Rep 19 with your name on it. Nobody can use it and nobody can check it.
- **Dividing by total latency.** It understates the rate, it looks completely reasonable, and it is
  the single most common defect in this module. The wrong method understated a real run by a quarter.
- **One run reported as a measurement.** One run is an anecdote. Three repeats with a median, and the
  spread reported next to it, is a measurement.
- **Treating `n/a` as a bug and putting a zero there.** You invented a number. In Module 3 that is a
  different and more serious conversation.
- **A comparison across two machines with two different methods**, reported as a fact about the
  machines. It is a fact about the methods until you fix the method.
- **Running the stand-in with no `--port`.** It lands on 11434, and nothing in this module is looking
  there. If something else in the building is, **a run against the wrong server looks exactly like a
  working run.**

### If you cannot do this yet

| Go to | Where |
|---|---|
| **Lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_ThreeNumbersWorthMeasuring.md`](../03-lecture-notes/MCCTC_145130_Notes_ThreeNumbersWorthMeasuring.md), the section on the arithmetic that gets it wrong, and worked example 2 on when a number cannot be known |
| **Second lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_WhereTheModelActuallyRuns.md`](../03-lecture-notes/MCCTC_145130_Notes_WhereTheModelActuallyRuns.md), if the problem is starting the layers rather than the arithmetic |
| **Third lecture note** | [`../03-lecture-notes/MCCTC_145130_Notes_AMeasurementNobodyCanRepeat.md`](../03-lecture-notes/MCCTC_145130_Notes_AMeasurementNobodyCanRepeat.md), the seven method items and why a median rather than an average |
| **Lab** | [`../05-labs/MCCTC_145130_Lab_M01-04_MeasuringInference.md`](../05-labs/MCCTC_145130_Lab_M01-04_MeasuringInference.md). Part 1 is thirteen hand-computed cases against `check_measure.py`, including four `None` cases. If that reports 13 of 13 and you wrote the three functions yourself, the arithmetic is finished |
| **The ports** | [`../05-labs/local-model-kit/README.md`](../05-labs/local-model-kit/README.md), the ports section and the section on stopping everything. Read it before you blame your own code |
| **The task** | [`../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md`](../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md), for what the client asked for and what they did not |
| **Gate 1 rep** | **Rep 03** (TRACE), both divisions written out, done until it is automatic. Then **Rep 07** (FIX) for the divisor and **Rep 12** (WRITE) for the two situations that have to return `None`. All in [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md) |

---

## Your five-minute self-check

Tick honestly. Nobody sees this page.

- [ ] I explained what a language model does to a real adult who has never programmed, and they told
      it back to me close enough that I did not have to correct them.
- [ ] I did it without the words magic, brain, thinks, knows, looks up, searches, or remembers.
- [ ] I can name three limits and the mechanism behind each, not three examples.
- [ ] I can give the strongest case for the side of the contested question I do not hold.
- [ ] I started a model server alone, on port 11634 or 11635, passing the port explicitly.
- [ ] I ran the stand-in at a known rate and my report landed near that rate rather than a quarter
      under it.
- [ ] I can write both divisions for tokens per second from memory.
- [ ] I can name one thing my number does not establish.
- [ ] My `AI_USAGE.md` has a session block for every session in which I used a tool.
- [ ] My `LICENSING.md` has a row for everything in my repository that is not mine, including the
      things whose terms I could not find.

**Any box you could not tick is an appointment in Period 8**, and that is what Period 8 is for. A
student who reaches Module 2 without criterion 3 spends Module 2 debugging Module 1.

---

## What Module 2 assumes you can already do

Module 2 is Prompt Engineering and Output Evaluation. It is the heaviest module on the exam blueprint,
and it spends none of its time re-teaching this one. It starts on day one assuming five things.

**1. A model server starts without help, and you pass the port.** Module 2 assigns its own ports. What
carries over is the habit of passing them explicitly and the knowledge of what happens when you do
not. Every prompt experiment in Module 2 is a run against a server, and a run against the wrong server
looks exactly like a working run.

**2. You know the answer arrives as text, and you record how you got a value out of it.** Module 2
compares prompts by their results. A result your program sliced out of a sentence and a result it
parsed cleanly are not the same evidence, and a table that does not say which is which cannot settle
anything. That is what the `how` field in Lab M01-01 was for, and Module 2 is where not having one
starts costing you conclusions.

**3. You can measure a change rather than sense one.** Module 2 asks whether one prompt is better than
another. That is Week 3 of this module with a different variable: an agreed method, repeats, a median,
and a written statement of what the difference does not establish. Prompt work without measurement is
opinion with a table around it.

**4. You can evaluate an output on the five parameters.** Validity, Relevance, Authenticity, Potential
Bias, Hallucinations. You met them in Gate 2 W01 and used them again in Gate 2 W03. In Module 2 they
stop being a Friday exercise and become the daily instrument.

**5. You keep `AI_USAGE.md` and `LICENSING.md` while you work.** Module 2 generates far more AI output
per period than Module 1 did, and Module 3 audits the licensing file. Starting that audit from an
empty file means reconstructing six weeks from memory, and reconstruction from memory is where
invented details come from. You will have spent two modules learning to spot those in other people's
work.

**One thing Module 2 does not assume.** It does not assume you have resolved the contested question.
Nobody has. It assumes you know it is contested and that you will not print either side as a fact.
