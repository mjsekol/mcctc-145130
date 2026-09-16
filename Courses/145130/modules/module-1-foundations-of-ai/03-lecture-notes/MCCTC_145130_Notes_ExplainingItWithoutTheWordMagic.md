# Lecture Notes: Explaining It Without the Word Magic
## 145130 Applications of AI · Module 1 · Week 3, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W03_ExplainingWithoutMagic.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W03_ExplainingWithoutMagic.pptx)

If you missed class you can learn this from this file alone.

**Competency 1.2.1** and the module's first exit criterion: explain to a
non-technical adult what a language model does, without using the word magic.

---

## Why this exists

The explainer you write today is graded, and it is also the thing you will
actually do. You will be the person in your family, your job, and your team who
gets asked what this stuff is. The answer you give shapes what people around you
believe and what they are willing to paste into a text box.

There is a harder reason. **You do not know a mechanism until you can explain it
to somebody who cannot rescue you.** A classmate fills gaps for you out of shared
context. A grandparent, a coach, or a nine-year-old does not. Writing for them is
the test.

---

## The concept in plain language

Four rules. They are not style advice.

### 1. Name the audience before the first sentence

Write it at the top of your draft and delete it before you submit. "For my aunt,
who runs a salon and has used a chat assistant twice." Everything downstream
comes from that line: which words you may use, what they already know, and what
they actually want to know, which is usually "should I be worried" rather than
"how does attention work".

### 2. Spend your jargon budget on purpose

You get about three technical words in a one-page explainer. Choose them, define
each one on first use in words the reader already has, and then use them
consistently. A fourth word starts costing you the reader.

For this explainer the three that earn their place are **token**, **training**,
and **inference**. "Transformer", "parameters", "context window", and
"temperature" do not, for this audience.

### 3. Every claim in the explainer must be one you could defend

You have spent three weeks learning not to repeat unsupported numbers. Do not
start now because the format is friendly. If you write that the model on your
station produces about 39 tokens per second, that is a number you measured, and
your report has the run. If you want to say a model has a certain number of
weights, you need the model card open in front of you.

Simplifying is allowed. **Simplifying into something false is not**, and under
deadline the two feel identical. "It guesses the next piece of text" is a
simplification. "It looks up answers in a huge database" is false, and it is
shorter, and it is what your reader already believes.

### 4. Banned words, and what to write instead

| Do not write | Why | Write instead |
|---|---|---|
| magic | it is the opposite of an explanation | say what actually happens |
| it thinks, it knows, it decides | asserts the contested question | it produces, it selects, it was fitted to |
| it learns from you | false during use | your earlier words are sent back in each time |
| `simply`, `just`, `obviously` | tells the reader their confusion is their fault | delete the word |
| revolutionary, game-changing | carries no information | say what changed for whom |

---

## Worked example 1: the same idea at three distances

**Too technical for the audience:**

> "The model performs autoregressive next-token prediction over a learned
> distribution, conditioned on the context window."

Every word is correct. Your aunt has stopped reading.

**Too loose, and now false:**

> "It reads everything on the internet and finds the best answer for you."

It does not read anything when you use it, and it finds nothing. This version is
worse than the first, because the first merely failed to communicate.

**About right:**

> "It was shown an enormous amount of writing and adjusted until it got good at
> guessing what piece of text comes next. When you use it, that is all it is
> doing: guessing the next piece, adding it on, and guessing again. Nothing is
> looked up, which is why it can be completely wrong and sound exactly as sure as
> when it is right."

Same mechanism, no jargon beyond what is defined in the sentence, and it carries
the consequence the reader actually needs.

---

## Worked example 2: the three questions every reader has

They rarely ask these out loud. Answer them anyway, and the explainer stops being
a definition and becomes useful.

**"Is it lying to me?"** No, and that is the problem. Lying needs an intention to
deceive and a grasp of the truth. It produces likely text, and likely text is
often true and sometimes not, with no change in tone between the two.

**"Where does what I type go?"** For the system in our lab, nowhere. It runs on a
machine in the room, it is not connected to an account, and the service keeps no
copy. For a product on your phone, read its terms, because the answer is
different and it is the company's decision, not the model's.

**"Will it take my job?"** The honest answer is that nobody knows, that
confident answers in both directions are being sold to you, and that the useful
version of the question is narrower: which parts of a specific job are drafting
text that a person will check. Those parts change. The parts that need somebody
accountable do not, because no model can be accountable for anything.

Notice what that last answer does. **It refuses the question as asked and offers
a better one.** That is allowed, and it is more honest than a prediction you
cannot support.

---

## Worked example 3: cutting a draft

First draft, 41 words:

> "Basically, AI models are neural networks that have been trained on massive
> datasets, allowing them to generate human-like text by predicting subsequent
> tokens based on patterns learned during the training process, which is
> revolutionizing how we all work."

What is wrong. "Basically" is filler. "Massive datasets" is vague and unsourced.
"Human-like" is a claim about people rather than about the system.
"Revolutionizing how we all work" could not be false. And "tokens" arrives
undefined.

Second draft, 43 words, and it says more:

> "A language model is a huge set of numbers that was adjusted, over months, until
> it got good at one job: guessing what small piece of text comes next. A piece is
> called a token, roughly a short word. Ask it a question and it guesses, over and
> over, until it stops."

It is not shorter. It is specific, it defines its one technical word where the
word appears, and every sentence says something that could be wrong.

---

## The wrong version, and the damage it does

> "AI is like a really smart friend who has read everything and can help you with
> anything."

This is the most common explainer sentence in the world and it is worth taking
apart, because your reader will act on it.

"Smart friend" implies intention and care. "Has read everything" implies a
library it consults, which implies a lookup step, which does not exist. "Anything"
removes the boundaries you spent three weeks learning.

The damage is specific and predictable. A reader who believes this pastes
confidential information into a text box, because you do not hide things from a
friend. They accept a citation without checking, because a friend who has read
everything would not make one up. And when it is wrong they conclude it was
having a bad day, rather than that it works this way all the time.

**An explainer is not judged on whether it was enjoyable. It is judged on what
the reader does next.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **audience** | the specific person you are writing for |
| **jargon budget** | how many technical words your reader can absorb, which is fewer than you think |
| **analogy** | a comparison to something familiar, which always breaks somewhere |
| **anthropomorphism** | describing a system as though it had human intentions |
| **oversimplification** | a simplification that has become false |
| **hedge** | a word that weakens a claim, useful when honest and filler when not |

---

## Self-check

**1.** Your reader asks whether the school model is "as smart as" the one on
their phone. Write two sentences that answer honestly without using the word
smart.

**2.** Name the analogy in "it is like autocomplete on your phone, but much
bigger" and say exactly where it breaks.

**3.** Your explainer says "the model has 8 billion parameters". You read that
number in a forum post. What do you do?

### Answers

**1.** Something like: "The one on your phone is much larger and runs on hardware
we do not have, so it handles harder requests better. Ours runs in this room,
needs no account, and nothing you type leaves the building, which is why we use
it." Two sentences, both checkable, and the trade is stated rather than a ranking
asserted.

**2.** The analogy is that both predict what comes next from what you have typed,
and that much is genuinely right and worth using. It breaks in two places. Phone
autocomplete offers you a choice and you pick; a language model picks for you and
keeps going for hundreds of tokens. And phone autocomplete predicts your next
word from your own history, which readers often assume means the model is
learning from them personally. Say the second part out loud or the analogy
installs a wrong belief while teaching a right one.

**3.** Take it out, or find the model card and cite that. A forum post is not a
source for a number about the specific build running on your machine. If you
cannot confirm it, the sentence is not needed: nothing in a one-page explainer
depends on the parameter count, and the number is only there because it sounds
impressive. That is the test for any unsupported number in your own writing.
