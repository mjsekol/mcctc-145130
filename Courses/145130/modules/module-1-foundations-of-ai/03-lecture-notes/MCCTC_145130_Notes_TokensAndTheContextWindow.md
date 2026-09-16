# Lecture Notes: Tokens and the Context Window
## 145130 Applications of AI · Module 1 · Week 1, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W01_TokensAndContext.md)

**There is no exported deck for this lesson yet.** The outline is current. The old export
showed the model service refusing a 4001 character prompt, and that service came out of this
module, so the export was removed rather than left in place: a deck that contradicts the
lesson is worse than no deck. The Gamma account ran out of credits before it could be
regenerated. Teach from the outline, or generate the deck once credits are available:

```
node tools/gamma.js Courses/145130/modules/module-1-foundations-of-ai/04-slides/MCCTC_145130_Slides_W01_TokensAndContext.md --export pptx
```

If you missed class you can learn this from this file alone. You need the files
in `../05-labs/local-model-kit/`.

**Competency 2.4.4:** describe emerging technologies, including large language
models. You cannot describe one honestly without these two words.

---

## Why this exists

Two of the most common wrong beliefs about these systems come from not knowing
these two words.

The first is that a model reads words. It does not. It reads **tokens**, and the
difference explains several behaviours that otherwise look like bugs.

The second is that a model remembers you. It does not. It has a **context
window**, which is a size limit on one request, and every product that feels
like a conversation is re-sending the earlier text every single time.

---

## The concept in plain language

### Tokens

A model does not see characters and it does not see words. Its input is chopped
into pieces called tokens, and the model works entirely in those pieces. A
common word is usually one token. A rare word, a name, a misspelling, or an
unusual string is several.

Why chop it that way at all? Because a model needs a fixed, finite list of things
it can see. There are far too many words in the world, especially once you
include names, typos, code, and every language. Pieces smaller than words give a
fixed list that can still represent anything, including a word the model has
never encountered, by spelling it out of smaller parts.

Three consequences you can observe:

- **Length limits are in tokens, not characters or words.** A limit of 8,000
  tokens is not 8,000 words.
- **Unusual text costs more.** A paragraph of code or of unfamiliar names uses
  more tokens than a paragraph of ordinary English of the same length.
- **The model's view of spelling is strange.** Asking a model how many letters
  are in a word is asking it about something it does not directly see.

**Do not repeat a conversion rate as though it were a measurement.** People
commonly say a token is about four characters of English. That is a rule of
thumb, it varies by tokenizer, and different models tokenize differently. When
you need the real number, ask the tokenizer of the model you are actually using.
The benchmark you build in Week 3 prints its assumption at the top of every
report for exactly this reason.

### The context window

The context window is the maximum number of tokens the model can take into
account at once. Everything is in there: your instruction, whatever text you
pasted, and whatever the program put in front of it.

**It is a size limit, not a memory.** Nothing survives between requests unless a
program deliberately puts it back in. A chat product feels continuous because it
re-sends the earlier turns as part of the input, every time, and pays for them
every time. When the conversation grows past the window, something has to be
dropped or shortened, which is why long conversations start losing the beginning.

---

## Worked example 1: a limit you cannot see is still there

Send the stand-in a fifty character prompt, then send it a fifty thousand
character prompt. Captured on the build machine:

```
prompt characters sent:      50   HTTP 200   15.1 ms   reply length 261
prompt characters sent:   52075   HTTP 200   16.3 ms   reply length 302
```

**Both succeeded, and that proves nothing.** The stand-in has no context window,
because it is not a model. It reads a couple of patterns out of your text and
returns a fixed shape, so it accepts a prompt of any size and answers at the
same speed either way.

A real model would not. Somewhere past its window one of three things happens,
and **only one of them tells you**:

- it refuses, and says how far over you were
- it truncates, and answers confidently about the part that fit
- something in front of it summarises the rest away

**The dangerous one is the middle one**, and it is dangerous precisely because the
run looks like the run above: HTTP 200, a fast answer, and no complaint.

**[VERIFY] on lab hardware.** With a real model runtime, find the limit by
walking a prompt up in size until the behaviour changes, and record which of the
three things happened. That number belongs in the pre-flight notes, because every
program in Module 5 has to know it.

---

## Worked example 2: what a system does when you cross the limit

There are only three options, and every product you use has picked one.

| Option | What it does | What it costs you |
|---|---|---|
| **Refuse** | reject the request and say why | you have to fix it, but you know |
| **Truncate** | drop text until it fits | you get an answer about part of your input and are not told which part |
| **Summarise** | compress older text and send the summary | you get continuity, and detail is quietly lost |

Our stand-in does none of the three, because it has no window at all. A chat
product usually truncates or summarises, silently.

**Truncating silently is the one to watch for**, because the output looks normal.
You asked about a ten-page document, the first four pages were sent, and the
answer is confident and complete about four pages. Nothing on the screen says so,
and the timing will not give it away either.

---

## Worked example 3: proving there is no memory

Two requests, one after the other, from the same program:

```python
send("Remember that my favourite label is account.")
send("What is my favourite label?")
```

The second request cannot be influenced by the first, and not because anything
forgot. **Nothing carries over, and you can check that rather than taking my word
for it.**

The only thing that could carry anything is the prompt, so print the prompt.
From `lab-m01-01-files/`:

```
python -c "import ask_model; print(ask_model.build_prompt('my name is Ada and my favourite label is account'))"
python -c "import ask_model; print(ask_model.build_prompt('what is my favourite label'))"
```

Captured on the build machine, second call:

```
You sort help requests for a school makerspace.
Answer with JSON only: {"label": one of ['hardware', 'software', 'network', 'account', 'other']}.
Task: classify
<<<TEXT
what is my favourite label
TEXT
```

**Nothing from the first call appears anywhere in the second.** `build_prompt`
assembles the whole input from the current ticket and a fixed instruction, and
there is nowhere for an earlier request to hide. That is the entire proof, and it
took two commands.

**That is a decision, not an accident, and it is a privacy decision as much as a
technical one.** No student writing is kept by anything in this module, so there
is nothing to leak and nothing to delete.

When you later build something that feels like a conversation, you will do it by
putting the earlier turns back into the prompt yourself. At that moment you own
the decision about what is kept, for how long, and for whom. **That decision is
worth making on purpose rather than inheriting it from a tutorial.**

---

## The wrong version, and why it is tempting

> "The context window is the model's memory. Everything you tell it stays in
> there, which is why it gets to know you over time."

This is wrong twice, and it is the single most common sentence in AI explainers
written by models.

**Wrong about memory.** The window is a size limit on one request. Nothing
persists on its own.

**Wrong about getting to know you.** The weights do not change while you use it.
Anything that looks like the system learning your preferences inside one session
is the earlier text being re-sent. Anything that looks like it across sessions is
a product storing a profile and putting it into your prompts, which is a
completely different thing and belongs to the product, not the model.

It is tempting because it matches the experience exactly. The thing behaves as
though it remembers. Believing the mechanism matches the feeling is how people
end up surprised by what a product kept, which is a privacy problem rather than a
technical one.

### Write this down

> The window is a size limit on one request. The feeling of memory is a program
> re-sending your earlier words and paying for them again.

---

## Vocabulary

| Term | What it means |
|---|---|
| **token** | one piece of text the model actually sees, roughly a short word or part of one |
| **tokenizer** | the program that chops text into tokens for a specific model |
| **vocabulary** | the fixed list of tokens a model can see |
| **context window** | the maximum number of tokens the model can consider at once |
| **truncation** | dropping text so a request fits inside the window |
| **prompt** | the whole input sent to the model, not only the part you typed |
| **stateless** | keeping nothing between requests |

---

## Self-check

**1.** Your program sends a 12-page document and the model's answer is confident
and detailed but only covers the first few pages. Nothing errored. Name the most
likely cause and say what your program should have done instead.

**2.** A classmate says a 4000 token limit means about 4000 words. Say what is
wrong with that and what you would do to get the real number.

**3.** Explain, in two sentences that a parent would understand, why a chat
assistant can seem to remember your name without the model remembering anything.

### Answers

**1.** The document went past the context window and something truncated it,
almost certainly without saying so. The program should have counted the tokens
first and then either refused with a message naming the size, or split the
document and combined the results, but never silently sent part of it and
presented the answer as being about the whole.

**2.** Tokens are usually smaller than words, so 4000 tokens is fewer than 4000
words, and how many fewer depends on the tokenizer and on the text. Code, names,
and unusual words cost more tokens per word than ordinary English. To get the
real number, run the text through the tokenizer of the model you are using rather
than applying any rule of thumb.

**3.** The program sends your earlier messages back to the model as part of every
new question, so the name is sitting in the input each time rather than stored
inside the model. The model reads it fresh every time, answers, and keeps nothing.
