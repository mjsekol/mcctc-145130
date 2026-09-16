# Lecture Notes: Rules You Wrote Against Weights Somebody Fitted
## 145130 Applications of AI · Module 1 · Week 1, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W01_RulesVersusWeights.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W01_RulesVersusWeights.pptx)

If you missed class you can learn this from this file alone. You need Python and
the files in `../05-labs/lab-m01-01-files/`.

**Competency 2.14.1:** describe how machine learning and neural networks operate
differently than standard decision trees. It is the single most likely thing
from this module to be on your exam.

---

## Why this exists

You are about to spend a semester putting a model inside a program. Before you
do, you need a clear answer to one question, because everything else in the
course hangs off it:

**When this thing gives an answer, can anyone say why?**

For the software you have written for two years, the answer is yes. There is a
line. You can put a print statement above it. For a model, the answer is no, and
that is not a gap in your skills. It is a property of the thing.

---

## The concept in plain language

**A decision tree is rules a person wrote, in an order a person chose.**

```python
if "locked out" in text:
    return "account"
if "wifi" in text:
    return "network"
return "other"
```

Three facts about that follow immediately. You can read it. You can point at the
branch that fired. When it is wrong, you change a line.

**A neural network is a very large collection of numbers, called weights, that
were adjusted automatically until its outputs matched a large collection of
examples.**

Nobody wrote the rules. The numbers were set by a process that repeatedly nudged
them in whatever direction reduced the gap between what the system produced and
what the examples showed. When it is done, the numbers are the system. There is
no list of rules anywhere in it, and no comment explaining any of them.

So: you cannot read it, you cannot point at the weight that produced an answer,
and when it is wrong you cannot change the line, because there is no line.

### The trade, stated plainly

| | Decision tree | Neural network |
|---|---|---|
| Where the behaviour comes from | a person wrote it | fitted to examples |
| Can you read the reason | yes, it is a branch | no |
| Fixing a specific wrong answer | change that rule | no direct way |
| Handling a case nobody thought of | falls through, usually badly | often handles it |
| Two people get the same answer | always | usually, not guaranteed |
| Explaining it to a parent | possible | hard, honestly |

**Neither column is the good one.** Trees are readable and brittle. Networks are
flexible and opaque. You pick based on whether you would rather be able to
explain a wrong answer or avoid more of them.

---

## Where this simplification breaks, and you need to know

Read this paragraph twice, because the version of 2.14.1 most people repeat is
missing it.

**Decision trees are not always hand-written.** There are algorithms that build
a tree from data, choosing each branch by which question best separates the
examples. A tree built that way is machine learning, by any reasonable
definition, and the technique is used constantly in industry on table-shaped
data.

So the clean sentence "trees are hand-written and networks are learned" is a
useful starting point and not the whole truth. The sentence that survives
scrutiny is this one:

> **The real difference is whether a human authored the decision boundaries, and
> whether the resulting system can be read.** A hand-written tree scores yes on
> both. A learned tree scores no on the first and yes on the second. A neural
> network scores no on both.

The Ohio competency says "standard decision trees", which means the hand-written
kind. Answer the exam question about that kind. Know that the fuller picture
exists, because somebody will raise it, and because Gate 2 this week has a
planted claim that lives exactly in this gap.

---

## Worked example 1: a tree with a readable reason

From the lab's reference solution, run on Python 3.13.7:

```python
print(classify("I am locked out of my account after changing my password."))
print(explain("I am locked out of my account after changing my password."))
```

Real output:

```
account
branch account (getting in) fired on the phrase 'locked out'
```

Two lines. The second one is the whole argument for this side of the trade.
**The system told you which rule produced the answer**, and you can go and read
that rule.

---

## Worked example 2: the order is a decision, and it changes answers

Same rules, different order. Take the help request MT-2004:

> "I am locked out of my account after changing my password on Monday. The login
> screen accepts the new one on my phone but not on the lab machines."

The word `screen` is in it. So is `locked out`. So is `password`. A tree that
asks about physical objects first says `hardware`. A tree that asks about getting
in first says `account`. Both trees are correct programs. They disagree because
two people made different choices about what to ask first.

Here is that exact disagreement, captured from a real run of `compare.py` on the
build machine:

```
  ticket    staff      your rules  service    source    agree
  ------------------------------------------------------------
  MT-2004  account    account     hardware   model     rules
  MT-2008  software   software    hardware   model     rules
```

Two tickets where the rule tree matched the makerspace staff and the other side
did not.

**And now the uncomfortable part.** The column headed `service` in that run did
not come from a neural network. It came from the stub model server, which is
itself a keyword matcher. When there is no model installed, that comparison is
one rule system against another rule system, and the `source` column saying
`model` means only that the service could not tell the difference.

That is not a flaw in the lab. It is the lab. **Where an answer came from is a
separate question from what the answer was**, and you have to ask it every time.

---

## Worked example 3: what the two systems do with a sentence nobody planned for

MT-2012 is one sentence: `Nothing works.`

The rule tree has no branch that matches, so it falls through to `other` and says
so:

```
  MT-2012  your rules said other
        reason: no branch matched, so the tree fell through to other
```

A model will usually produce a label anyway, with a fluent sentence explaining
it. It does not have a "no branch matched" state to fall into. Asked for a
label, it produces the tokens that look like a label.

**A tree fails visibly. A model fails fluently.** When you are deciding which to
put in front of a person, that difference matters more than the accuracy numbers
in anybody's comparison.

---

## The wrong version, and what it costs

Here is a sentence that shows up in student writing every year:

> "We used AI instead of if statements because AI is more accurate."

Three problems, and they compound.

**It compares the wrong things.** More accurate on what task, measured against
what, on which examples. Accuracy is not a property a technology has. It is a
number a specific system gets on a specific test set.

**It throws away the readable reason without saying so.** The tree could tell
you which branch fired. Whatever replaced it cannot. That is a real cost and
the sentence does not mention it.

**It is unfalsifiable as written.** There is no test anyone could run that would
change the author's mind, which means the sentence is not a claim about the
world. Gate 2 will ask you to score writing like this, and "unfalsifiable as
written" is a finding.

### Write this down

> A model is not a better if statement. It is a different trade: you give up the
> readable reason to get coverage of cases nobody wrote a rule for.

---

## Why the wrong version is tempting

Because it is usually said by somebody who watched a model do something a rule
system could not, and they are not making that up. The experience is real. The
mistake is turning "it handled a case my rules missed" into "it is more
accurate", which is a much bigger claim with no evidence attached.

The habit that prevents it: every time you want to write "better", finish the
sentence. Better at what, than what, measured how. If you cannot finish it, you
do not yet have a claim.

---

## Vocabulary

| Term | What it means |
|---|---|
| **decision tree** | a set of rules arranged so that each answer is reached by a path through them |
| **branch** | one rule in a tree, and the path taken when it matches |
| **weight** | one number inside a neural network, set during training |
| **neural network** | a system whose behaviour comes from many weights fitted to examples |
| **machine learning** | any approach where behaviour is fitted to data rather than authored |
| **fitted** | adjusted until outputs matched examples |
| **interpretable** | a system whose reason for an answer can be read |
| **fall through** | what a tree does when no branch matches |

---

## Self-check

**1.** A tree and a model both label a help request `hardware`. One of them can
tell you why. Which piece of information does the other one give you instead,
and why is it not the same thing?

**2.** Your tree labels MT-2004 as `hardware`. Nothing in the program is broken.
Explain in two sentences how both of those can be true.

**3.** A classmate writes: "A decision tree cannot be machine learning because a
person wrote it." Say what is right about that sentence and what is wrong with
it.

### Answers

**1.** The model gives you a fluent explanation, which is not the same thing,
because it was produced the same way the label was: as likely text. It was not
read off the process that produced the label, so it can sound completely
convincing and describe reasoning that never happened. The tree's reason is the
branch that actually fired.

**2.** The program did exactly what it was written to do: a branch about physical
objects was asked before a branch about getting in, and the phrase `screen`
matched. The wrongness is in the ordering decision, not in the execution, which
is why running it again more carefully will never find it and reading the order
will.

**3.** Right: a hand-written tree is not machine learning, and "standard decision
tree" in the competency means the hand-written kind. Wrong: the sentence claims
trees in general cannot be learned, and they can. Algorithms build trees from
data by choosing each branch to best separate the examples, and those trees are
machine learning. The property that actually divides the two cases is who
authored the decision boundaries.
