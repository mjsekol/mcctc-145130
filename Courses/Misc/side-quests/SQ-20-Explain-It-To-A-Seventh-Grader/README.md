# SQ-20 · Explain It to a Seventh Grader
## 145130 Applications of AI · Unlocks any time · fits Module 6, Week 16

**Time:** one block. **Difficulty:** ★
**Competencies:** 2.14.1 (describe how machine learning and neural networks operate
differently than standard decision trees), 2.14.2 (analyze how AI technology impacts
society and the ethical implications of its usage), 1.2.5 (communicate information
for an intended audience and purpose).

**A note on the catalog entry.** The Side Quest Catalog lists this quest's
competencies as **2.14.2 and 1.2.5**. Both are in
`Courses/145130/_source/COMPETENCY_REFERENCE.md` and both are claimed here. **This
bundle adds 2.14.1**, because describing how the thing actually produces text is
most of what you are explaining, and 2.14.2 on its own does not cover it. See the
note at the bottom of this file.

---

## The quest

**Write and deliver a five-minute explanation of how a language model produces
text, to a twelve-year-old.**

No word you do not define. No sentence they lose you in the middle of.

**Done when:** a real person of that age can answer three comprehension questions
afterwards, in their own words, and one of those questions is about something you
never mentioned.

**Why this one.** You cannot explain what you do not understand, and this is the
fastest way anybody has found to tell which you have.

---

## The rules, and they are the same as a usability session

1. **Twelve or older.** If they are family, a parent is in the room.
2. **Nothing is recorded.** No video, no audio, no photograph. You write.
3. **No name goes into anything you hand in.** "The listener", or "my cousin", and
   nothing more specific.
4. **They can stop at any point**, and you thank them either way.
5. **Nothing from it goes into an AI tool.** Not your notes, not their answers.

---

## What is in this bundle

| File | What it is |
|---|---|
| `jargon_check.py` | Finds the words in your script you used and did not explain. Standard library |
| `sample-script.md` | The version everybody writes first. Run the checker on it before you run it on yours |
| `comprehension-questions.md` | The three questions, and the rule that you write them before you speak |
| `instructor/` | Kept private by the publisher. Do not look for it |

---

## Part 1 · Run the checker on somebody else's bad script first

**Before you write anything.**

```
python jargon_check.py sample-script.md
```

**Real output, from the build machine:**

```
sample-script.md: 226 words, about 1.7 minutes at 130 words a minute

USED AND NOT EXPLAINED
  model                  used 5 times, first at line 1
  prompt                 used 4 times, first at line 8
  training               used 4 times, first at line 3
  context window         used 2 times, first at line 11
  training data          used 2 times, first at line 7
  dataset                used 1 time, first at line 2
  hallucination          used 1 time, first at line 15
  ...

SENTENCES OVER 25 WORDS
  57 words: So a large language model is a type of neural network that has been trained on a...
  ...

14 undefined term(s), 5 long sentence(s).
```

**Read the sample script yourself, out loud, first.** Every sentence in it is true.
It is also two hundred and twenty-six words and there are fourteen words in it that
a twelve-year-old has never met.

**That is the version you are about to write.** Everybody does. The point of doing
this first is that you meet the pattern in somebody else's writing, where it stands
out more.

Then:

```
python jargon_check.py --list
```

That prints the word list and the phrases that count as you having explained one.
**Read the last paragraph of that output.** If you explained a word in a way the
list does not know about, the tool will flag it, and you will be right and it will
be wrong. **Say so in your write-up rather than changing your wording to please a
program.**

---

## Part 2 · Write the three questions

**Before you write the explanation.** Use `comprehension-questions.md`.

Questions written afterwards get written to match whatever you happened to say.
Questions written first are a prediction, and a prediction can be wrong.

**One of the three must be about something you never mention.** That is the one
that tells you whether the idea landed or only the words did.

**Write down what would count as understanding, for each one, before you ask.** It
stops you deciding afterwards that whatever they said was close enough.

---

## Part 3 · Write the script

Five minutes. About 650 words at a slow, clear pace.

**Three things that make the difference, and none of them is about being simpler.**

**Start with something they already have.** Not a definition. A thing that has
happened to them. The predictive text on a phone works, and so does a friend who
finishes your sentences, and so does a song you can hum the next note of.

**Every word from the list gets a sentence next to it, in words they already
have.** Not a better technical definition. A different kind of sentence.

**Say the limits, not only the mechanism.** What it cannot do, and what it does
when it does not know, and what a person should be careful with. That is competency
2.14.2 and it is the half that people leave out because it is less fun to explain.

Then:

```
python jargon_check.py my-script.md
```

**Zero flagged is the floor, not the grade.** The tool cannot tell whether your
explanation is true and it cannot tell whether a definition you wrote helps
anybody.

---

## Part 4 · Deliver it and ask the three questions

Read it, or say it. Five minutes.

**Then stop talking.** Ask the three questions and do not help.

**Same rules as a usability session.** You may not ask "does that make sense", you
may not finish their sentence, and you may not explain it again in the middle of an
answer. You may wait, and you may say "can you say a bit more about that".

**Write down what they said, not what you think they meant.**

---

## Done when

- [ ] `jargon_check.py` reports nothing flagged on your script, **or** you can name
      every flag it raised and say why you disagree with it
- [ ] Your three questions were written **before** the script, and the file shows it
- [ ] One of the three is about something you never mentioned
- [ ] You wrote down what would count as understanding, before you asked
- [ ] A real person aged twelve or over heard it and answered all three
- [ ] You recorded what they said, in their words, including the parts that were
      wrong
- [ ] **Nothing was recorded and no name appears anywhere**
- [ ] Your write-up names one sentence you would change and what they said that
      made you think so
- [ ] You thanked them

---

## The two sentences your write-up has to contain

Somewhere in it, in your own words:

1. **"They understood this."** With the question, and what they actually said.
2. **"They did not understand this, and here is the sentence I would change."**

**A write-up where all three questions landed and nothing would change is the one
to be suspicious of.** It happens, and when it does, the usual cause is a third
question that was not really about something new.

---

## If it breaks

**`jargon_check.py: error: give a script file to check, or pass --list`**
Correct, and deliberate. Give it a file, or pass `--list`.

**Everything you wrote is flagged.** Normal on a first draft. Work down the list by
how many times each word was used, because the ones you leaned on hardest are the
ones doing the most damage.

**It flags a word you definitely explained.** Read the explanation out loud. If the
explanation is two sentences away from the word, a listener has the same problem
the tool does. If it really is next to the word and the tool still missed it, you
are right, and that goes in your write-up.

**You cannot get it under five minutes.** Cut the mechanism, not the limits. Most
people's first draft spends four minutes on how it works and thirty seconds on what
it cannot do, and the second part is the part that changes what somebody does on
Monday.

**Your listener says "yeah, that makes sense" and cannot answer question 3.**
That is the most common result and it is a real finding. It means the words landed
and the idea did not. **Do not count it as a pass**, and write down which sentence
you think was carrying the idea.

---

## Note on the catalog competency codes

The Side Quest Catalog lists SQ-20 as **2.14.2 and 1.2.5**.

**Both of those are in the 145130 competency reference and both are claimed here.**
1.2.5 is communicate information for an intended audience and purpose, which is the
whole quest. 2.14.2 is analyzing how AI technology impacts society and the ethical
implications, which is Part 3's third rule and Part 4's second question.

**This bundle also claims 2.14.1**, describing how machine learning and neural
networks operate differently than standard decision trees, because explaining how
the thing produces text is most of the five minutes and 2.14.2 does not cover it.

**That is an addition rather than a correction, and the catalog is a shared file
that this bundle did not change.** Whoever owns the catalog may want to add 2.14.1
to the entry.
