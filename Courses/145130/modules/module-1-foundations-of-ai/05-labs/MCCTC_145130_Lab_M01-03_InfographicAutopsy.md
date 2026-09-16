# Lab M01-03: Infographic Autopsy
## 145130 Applications of AI · Module 1 · Week 2, Wednesday and Thursday

**Gate:** 2 (adversarial). **Duration:** Wednesday Build 2, 55 minutes, and
Thursday Build 1, 40 minutes. Thursday's Build 1 opens with that day's Gate 1
rep, and Part 2 starts after it.
**Competencies:** PRIMARY 1.2.1 (extract relevant, valid information and cite
sources), 2.14.4 (evaluate an AI result on validity, relevance, authenticity,
potential bias, hallucinations). SUPPORTING 2.14.6, 2.4.4.

---

## About this artifact, before you start

**The page below was constructed for this class.** It is not a real infographic
found circulating anywhere. Every problem in it was planted on purpose, every one
is checkable, and the organisation named in it does not exist.

You are being told this for the same reason you were told it as juniors. A real
infographic gets corrected or taken down, and thirty students taking apart a
findable person's work is a different exercise than this one. What is real is the
**shape**: every problem below is a mistake that generated content actually
makes, presented the way it actually gets presented, which is confidently and
attractively.

**This is not the autopsy you did in 145060.** That one was a Python cheat sheet
and a terminal settled most of it in eight seconds. This page is about material
you learned last week, most of it is checkable only by reasoning or by reading a
source, and **at least one problem on it is a genuine argument rather than a
mistake.** Finding that one and arguing it properly is worth more than finding
three obvious ones.

---

## The scenario

This page is pinned on a wall in a computer lab and a teacher has been handing it
out. It is well designed, the tone is confident, and most people who read it will
believe all of it. Several will repeat it.

Your job is to be the person who checks.

## What you will build

A written autopsy: every problem you can find, quoted exactly, labelled with the
one criterion it fails, and supported by evidence you actually produced.

---

## The five criteria

Every finding gets exactly one label. Choosing the label is part of the work.

| Criterion | The question it asks |
|---|---|
| **Validity** | Is it correct? A false claim about something real. |
| **Relevance** | Does it answer what was asked, or something else? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and who is missing? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**The hard call is Validity against Hallucinations**, and you will make it more
than once.

- **Validity** is a wrong claim about a real thing. The thing exists; the
  statement about it is false.
- **Hallucination** invents the thing itself.

You can catch a validity failure by testing the real thing. You can only catch a
hallucination by going to look and finding nothing there.

---

# THE ARTIFACT

> # HOW A LANGUAGE MODEL WORKS
> ## The complete pipeline, explained. Version 3.2
>
> ---
>
> ### STEP 1 · TOKENIZE
>
> Your text is split into tokens before the model sees it. **A token is a word.**
> A 1,000-word essay is exactly 1,000 tokens, which makes planning your prompts
> straightforward.
>
> ---
>
> ### STEP 2 · LOAD THE CONTEXT WINDOW
>
> The context window is the model's long-term memory. Everything you have told it
> is stored there and recalled when it becomes relevant again.
>
> Our lab model has an **8,000 token context window, which holds roughly 6,000
> words** of conversation history.
>
> ---
>
> ### STEP 3 · RECONCILIATION
>
> Before it answers, the model runs its draft answer through the **reconciliation
> layer**, where each statement is checked against the training data and anything
> unsupported is discarded. This is the stage that makes modern models rarely
> hallucinate.
>
> ---
>
> ### STEP 4 · PREDICT AND EMIT
>
> The model produces text one token at a time, appending each token to its input
> before producing the next.
>
> Because it always selects the single most likely next token, **the same prompt
> always produces the same answer.**
>
> ---
>
> ### STEP 5 · LEARN
>
> At the end of each session, the conversation is added to the model's weights.
> **This is how it improves for you over time**, and why the assistant you use
> every day feels like it knows you.
>
> ---
>
> ### PERFORMANCE
>
> Training happened once, before the model was released. After that, every answer
> is inference.
>
> Our test machine produced **42 tokens per second, which is about 2,520 words
> per minute.**
>
> ---
>
> ### ADOPTION
>
> According to the **Halloran Institute for Applied Computing (2024)**, 84% of
> mid-sized firms now run at least one model on their own hardware.
>
> ---
>
> ### GETTING STARTED
>
> Any modern gaming laptop runs these models fine, so **cost is no longer a
> barrier to entry** for students who want to learn this.
>
> ---
>
> ### SIDEBAR · AI AND THE FUTURE OF HOLLYWOOD
>
> Generative video tools are reshaping film production. Studios are already using
> them for previsualisation and background plates, and the debate over performer
> likeness rights is intensifying. Expect the next decade of entertainment to look
> very different.
>
> ---
>
> > ### "A language model does not understand anything. It is only autocomplete."
>
> ---
>
> *Adapted from the official architecture documentation. © 2024. Share freely, no
> attribution needed.*

---

# Your work

## Part 1, Wednesday Build 2, 55 minutes, individual

Find problems. For each one, write an entry with all four parts:

1. **The exact claim, quoted.** Word for word.
2. **Which criterion it fails.** One label per finding.
3. **Why it is wrong.** In your own words.
4. **How you know.** Best: a command you ran, with the output pasted. Acceptable:
   a source you went and read, named specifically, with what it says. Also
   acceptable: a documented search that found nothing, saying where you looked.
   **Not acceptable:** "I could tell" or "it seems wrong."

**There are at least nine problems.** Seven findings is a passing autopsy. Nine is
strong. **One of them is not a mistake at all**, and how you handle that one is
worth more than any other single finding on the page.

### Two things this page can settle without leaving the folder

**One problem on this page contradicts another problem on this page.** You do not
need any source to catch that one. Read the whole page before you start writing
and look for two numbers that cannot both be true.

**One problem is arithmetic.** You have a calculator.

### One warning about your instrument

Some claims on this page are about what a model does. You have a stub, not a
model. **The stub cannot settle every claim**, and at least one claim on this
page is exactly the kind the stub gets wrong in a way that would mislead you.

If you find a claim your instrument cannot settle, say so in your finding. That
is a result, not a gap. Write down what you would need in order to settle it.

### Acceptance criteria, Part 1

1. At least seven findings, each with all four parts
2. Each finding labelled with exactly one criterion
3. At least two findings supported by something you produced: a command and its
   output, a calculation written out, or a documented search
4. At least one finding labelled Hallucinations and one labelled Validity, and
   you can say why each is not the other
5. The internal contradiction is found and named as such

---

## Part 2, Thursday Build 1, 40 minutes

Thursday's Gate 1 rep runs in the first 10 minutes of Build 1. Part 2 starts
after it.

**First 10 minutes: trade with one partner.** Read theirs. Add anything they
found that you missed, **marked clearly as theirs.**

**Next 20 minutes: write the summary section.** It answers all six.

1. Which problem would fool the most people, and why that one?
2. Which criterion was hardest to apply here, and what made it hard?
3. One problem needed you to go and look rather than reason from what you knew.
   Which one, what did you do, and what did you find?
4. **The argument.** One statement on this page is not a mistake. It is a
   position in a real disagreement, stated as settled fact to an audience that
   cannot tell the difference. Name it. Give the strongest case for it, then the
   strongest case against it, then say what you would actually write in its place.
   **You are not graded on which side you land on.** You are graded on whether
   both cases are real ones.
5. Two statements on this page are correct. Name them. Say how you decided they
   were correct rather than assuming everything on a page like this is wrong.
6. If you had read this page a month ago, how many of these would you have
   caught? Answer honestly. Nobody is graded on the number.

**Last 10 minutes: commit and push.**

### Acceptance criteria, full lab

- [ ] Seven or more findings with all four parts each
- [ ] Partner additions present and marked as theirs
- [ ] Two or more findings supported by something you produced
- [ ] The internal contradiction named
- [ ] Summary answers all six questions
- [ ] Question 4 gives both sides a real case
- [ ] Question 5 names two correct statements
- [ ] `AI_USAGE.md` entry if you used a model at any point
- [ ] Committed and pushed

---

## How to actually check things

**Use the terminal where it helps.** Some claims about the service and the window
can be settled in ten seconds with the kit in `local-model-kit/`.

**Use arithmetic where it helps.** Two claims on the page are numbers you can
check against each other or against a definition from last week.

**Use your own notes.** The lecture notes from Week 1 are sources, and they name
which parts came from running something on the build machine.

**For the adoption claim, go and look.** Search for the organisation. Record
where you searched and what you found. A search that finds nothing is a finding,
and it is the whole answer for that one.

**A claim you cannot test needs a different kind of checking.** Some of these are
not settled by any command. Notice which ones, because that difference is most of
what this lab teaches.

---

## If you get stuck

**"It looks fine to me."** You are reading at the section level. Read one
sentence at a time and ask: what would I have to do to prove this. If the answer
is one command or one calculation, do it.

**"I found four and I am out."** Go section by section instead of skimming for
what feels wrong. Almost every section has something in it, and two sections have
two.

**"I cannot tell Validity from Hallucination."** Ask whether the thing being
described exists at all. If it does not exist, it is a Hallucination. If it
exists and the sentence is false, it is Validity. Write down which you picked and
why. Showing the reasoning earns the credit even when the label is wrong.

**"Some of these are not about how models work."** Correct, and that is on
purpose. One whole section belongs to a different page, and one line at the
bottom is about something else entirely. Both are findings.

**"I think one of these is actually right."** Good. Two of them are. Say so and
say how you decided.

---

## Submission checklist

- [ ] `autopsy.md` in your repository
- [ ] Seven or more findings, each with claim, criterion, why, and how you know
- [ ] Two or more pieces of evidence you produced yourself
- [ ] Partner additions marked
- [ ] Summary answers all six questions
- [ ] Question 4 argued in both directions
- [ ] Pushed
