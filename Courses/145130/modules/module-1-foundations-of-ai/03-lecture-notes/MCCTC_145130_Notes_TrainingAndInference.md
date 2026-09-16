# Lecture Notes: Training and Inference
## 145130 Applications of AI · Module 1 · Week 1, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W01_TrainingAndInference.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W01_TrainingAndInference.pptx)

If you missed class you can learn this from this file alone.

**Competency 2.14.1 and 2.4.4.** This is the lesson that lets you answer the
exit criterion: explain to a non-technical adult what a language model does,
without using the word magic.

---

## Why this exists

You now know a model is weights fitted to data. Two questions are left, and both
of them are on the exam and in every conversation you will have about this
outside school.

**Where did the weights come from?** Training.
**What happens when you press enter?** Inference.

They are completely different activities. Confusing them produces most of the
wrong beliefs people hold about AI, including the expensive one: that using a
model teaches it.

---

## The concept in plain language

### Training

Training is the process that set the weights. Roughly: show the system an
enormous amount of text, repeatedly ask it to predict the next piece, compare its
prediction to what actually came next, and nudge the weights in whatever
direction would have made the prediction better. Do that an unimaginable number
of times.

Three properties matter for you.

**It happened once, somewhere else.** Not on your machine and not during your
use.

**It was expensive in a way that is hard to picture.** Months of specialised
hardware. You will not train one of these in this class and nobody expects you
to.

**It is finished.** The model you download is the weights afterwards. They are a
file.

### Inference

Inference is what happens when you press enter. Your text is tokenized, run
through the fixed weights, and the system produces a probability for every
possible next token. One is chosen. It is appended to the input. The whole thing
runs again. And again, until a stopping condition.

Three properties matter for you.

**The weights do not change.** Nothing is learned. The file on disk is the same
file after your request as before it.

**It costs time and electricity, on your machine.** Small compared to training,
not small compared to the rest of your program. Week 3 measures it.

**Text comes out one token at a time.** That is not a display effect. It is the
mechanism, and it is why time to first token is a different number from total
latency.

### The sentence that answers the exit criterion

> A language model is a very large set of numbers that was adjusted, once, until
> it got good at guessing what piece of text comes next. When you use it, those
> numbers do not change. It guesses the next piece, adds it on, and guesses
> again, until it stops. Everything it produces is produced that way, including
> the parts that are true.

Read that last clause again. **The truth of an answer is not a separate step.**
There is no checking stage. Correct output is output whose most likely
continuation happened to match reality.

---

## Worked example 1: where the cost actually lands

From the Week 3 reference run, against a stand-in server configured to send 40
tokens with 25 milliseconds between them and 300 milliseconds before the first:

```
  prompt            median total   median ttft   tokens   tokens/sec
  p1_short             1335.7 ms      318.3 ms     40.0         39.3
```

Read that as a story about inference. About a third of a second passed before
any text existed. Then tokens arrived at about 40 per second for a second. Total
wait, one and a third seconds, for forty tokens.

On real hardware with a real model the numbers differ, and the shape does not.
There is a pause, then a stream. **The pause is the model reading your input and
producing the first token. The stream is it doing the same thing again, over and
over.**

---

## Worked example 2: the same prompt twice

Send an identical request to the stub twice and you get identical answers,
because the stub is a rule system and rule systems are deterministic.

A real model usually does not behave that way. At each step it has a probability
for every possible next token, and most systems choose with some randomness
rather than always taking the most likely one. Turn that randomness off and the
output becomes repeatable. Leave it on and two identical prompts can produce
different answers.

**This matters for your own testing.** A test that asserts an exact string from a
model will pass today and fail tomorrow without anything changing. That is why
the service in this course validates the **shape** of an answer rather than its
text: a label from a fixed list, a summary with at least one bullet.

It also matters for the Infographic Autopsy in Week 2, where one of the planted
claims is about exactly this, and where the stub **cannot settle it** because the
stub is deterministic. Naming a question your instrument cannot answer is itself
a finding.

---

## Worked example 3: what "fine tuning" is, and is not

You will hear that a model can be "trained on your data". Usually one of three
different things is meant, and they are not interchangeable.

| What people say | What is actually happening | Do the weights change |
|---|---|---|
| "I trained it by talking to it" | earlier text is being re-sent in the prompt | no |
| "We gave it our documents" | documents are searched and the relevant parts are put into the prompt | no |
| "We fine-tuned it" | further training on extra examples, producing a new weights file | yes, in the new file |

The middle row is retrieval, and it is what Module 4 builds. It is the right
answer for most practical problems: cheaper, updatable the moment a document
changes, and you can show which document an answer came from.

---

## The wrong version, and why it is tempting

> "Every time you use it, it learns from your question and gets a little better."

This is false during inference, and it is the most widely believed false thing
about these systems.

It is tempting for three good reasons. Products do improve over time, so the
observation is not imaginary. Conversations do get more relevant as they go on,
because the earlier turns are in the input. And some products genuinely do store
what you type and use it in later training, which is a real thing that happens at
the company, on their schedule, not in your session.

The belief matters because of what it implies. If using a model taught it, you
would expect your corrections to stick, and they do not. You would expect two
students to get different quality from the same model, and they do not, except
for the words they typed. And you would expect it to be safe to correct a model's
mistake and move on, which is exactly how a wrong answer ends up in a submitted
project.

### Write this down

> Training set the weights, once, somewhere else. Inference uses them and changes
> nothing. What feels like learning inside a session is your own earlier words
> being sent back in.

---

## Vocabulary

| Term | What it means |
|---|---|
| **training** | the process that set the weights, using many examples |
| **inference** | using the fixed weights to produce an answer |
| **weights file** | the file you download and load; the model itself |
| **next-token prediction** | producing a probability for the next token, then choosing one |
| **deterministic** | the same input always gives the same output |
| **sampling** | choosing the next token with some randomness rather than always the likeliest |
| **fine tuning** | further training on extra examples, producing new weights |
| **retrieval** | searching your own documents and putting the relevant parts into the prompt |

---

## Self-check

**1.** A student corrects the model in a chat, gets a better answer, and writes
in their decision log that they "trained the model to handle this case". Rewrite
that sentence so it is true.

**2.** Your program sends the same prompt to a local model twice and gets two
different answers. Name the likeliest cause and one thing you could change to
make the answers repeatable.

**3.** A company wants an assistant that knows its own repair manuals. Give one
reason to choose retrieval over fine tuning, and one reason somebody might still
choose fine tuning.

### Answers

**1.** Something like: "I added a correction to the prompt, and the model's next
answer used it. The model itself did not change, and the correction has to be in
the prompt every time or the behaviour goes away."

**2.** The system is sampling, choosing the next token with some randomness
instead of always taking the most likely one. Turning the randomness down or off,
if the runtime exposes that setting, makes the output repeatable. Note the second
half of the trade: repeatable output is simpler to test and often less useful,
because the most likely continuation is also the blandest one.

**3.** Retrieval: the manuals change, and retrieval picks up a change the moment
the document is updated, while fine tuning means training again. It is also far
cheaper, and you can show which manual page an answer came from, which matters
when somebody is repairing equipment. Fine tuning: when the goal is a consistent
style, format, or vocabulary rather than facts, retrieval does not help much,
because you are trying to change how it writes rather than what it knows.
