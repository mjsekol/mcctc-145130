# Lab M05-04 · The Documentation Autopsy
## 145130 Applications of AI · Module 5 · Week 15, Tuesday

**Competencies:** 5.6.8 (create documentation), 5.6.9 (review the design through
peer walkthrough), 1.2.5 (communicate for an intended audience)

**Reinforced, not assessed here:** 2.14.4 (evaluate an AI result on validity,
relevance, authenticity, potential bias, and hallucinations). You met that
rubric in Module 2. Today you point it at documentation instead of at an
article.

---

## The situation

A team ran out of time, handed a model the code of the demo service you traced
in Week 13, and asked it to write the documentation set. It produced nine files
in about forty seconds. The files look professional, the headings are all there,
and the team submitted them without reading them carefully.

The documents describe a program that does not exist. Not entirely, and that is
what makes this worth an hour.

**What you will build:** a scored evaluation of the set on the five AI Output
Evaluation parameters, and a rewrite of the two worst documents.

---

## Before you start

Copy `lab-m05-04-files/submitted-docs/` to your own folder. You also need the
system these documents claim to describe, which you already have:

| What | Where |
|---|---|
| the service itself | `05-labs/lab-m05-01-files/contract_demo_service.py` |
| its real contract | `05-labs/lab-m05-01-files/CONTRACT.md` |
| the stand-in model it calls | `05-labs/lab-m05-01-files/stub_model_server.py` |

You traced that service in Week 13 and you have run it. That is the point: you
can check every claim in these nine documents yourself, in a terminal, today.

---

## The tool

`09-project/project-files/doc_check.py` reads a documentation folder and reports
what is missing.

```
python doc_check.py submitted-docs
python doc_check.py --list
```

It checks three things: whether each required file exists, whether each required
section is there, and whether any section is too short to be an answer. **It
cannot read.** It has no idea whether anything in the documents is true, and
that is the whole point of today.

---

## Steps

**Step 1. Run the tool and record what it found.**

```
python doc_check.py submitted-docs
```

*Observable result:* nine lines, one per document, most of them INCOMPLETE, and
a count at the bottom. There are 19 of them. Save the output to a file. That is
your structural findings list and it is the part a program can do.

**Step 2. Read all nine documents, once, without stopping to write anything.**

Fifteen minutes. Do not take notes yet. You are looking for the general shape,
and if you start writing in the first document you will never reach the ninth.

**Step 3. Read the real system.**

Open `CONTRACT.md` from the Week 13 lab folder. Read sections 1 through 5. Then
open `contract_demo_service.py` and find, for each of these, what the code
actually does:

- How many endpoints does the service have, and what are they called
- How many retries does it make, and what is the cap
- What fields are in the result shape
- How long can a headline be
- Does it keep anything between requests
- What does `ok: false` mean
- Does it need a credential

**Step 4. Score the set on the five parameters.**

This is the Ohio 2.14.4 rubric and you have used it before. Score each parameter
out of 4 and write two sentences of evidence for each, quoting the document.

| Parameter | The question here |
|---|---|
| **Validity** | is what it says about this system true |
| **Relevance** | does it answer the question its section heading asks |
| **Authenticity** | is it about this program, or about programs in general |
| **Potential bias** | who can follow these instructions, and who cannot |
| **Hallucinations** | what does it describe that does not exist |

**Step 5. Find the five claims that are not true.**

There are at least five statements in this set that contradict the code. Find
them, quote each one, and say what the code actually does. One of them is in the
error section, one is about a field, one is about an endpoint, one is about
memory, and one is about what a field means.

**Step 6. Find the one that is genuinely arguable.**

Not everything wrong with this set is a factual error. One of the claims is a
design opinion you could defend, and the document states it as though it were a
requirement. Find it, give the strongest argument for it, give the strongest
argument against it, and say which side you come down on and why.

You are graded on the reasoning here and not on which side you pick.

**Step 7. Rewrite the two worst documents.**

You decide which two. Justify the choice in two sentences: worst is not the same
as most incomplete, and `doc_check.py` only measures the second one.

Your rewrites have to pass `doc_check.py` **and** be true. `CONTRACT.md` is a
finished example of one of these documents and is worth reading for shape, not
for text to copy. Your rewrite is about the demo service, so every claim in it
has to be checkable against code you can open.

**Step 8. Write the one paragraph that matters.**

The team's defence is that they were out of time and the model produced nine
files in forty seconds. Write one paragraph, for that team, answering: what did
those forty seconds actually cost, and what would have been a legitimate use of
a model here.

---

## Acceptance criteria

1. `doc-check-output.txt` is saved, from a real run.
2. All five parameters scored out of 4, each with two sentences of evidence that
   quote the document.
3. Five untrue claims found, each quoted, each with what the code actually does
   and where you found it.
4. The arguable one is identified, with both sides argued and a position taken.
5. Two documents rewritten, and both pass `doc_check.py`.
6. Every claim in your rewrites is checkable against the service's code, and you
   can point at where.
7. Your two sentences on why those two were the worst.
8. The final paragraph.

---

## If it breaks

**`doc_check.py` says a file is missing and you can see it**
Check the folder layout. It expects `design/` and `docs/` subfolders. If you
copied the files out of their folders, it will not find them.

**`doc_check.py` reports a section as too short and it looks long enough**
It counts the words under a heading, including everything under its subheadings,
and it does not count code blocks. Twenty five words is the floor.

**Your rewrite passes `doc_check.py` and you know it is thin**
That is correct behaviour and it is the lesson. Passing the tool is the floor,
not the grade. A person reads it next.

**You cannot find the fifth untrue claim**
Four of the five are in the I/O specification and the data dictionary. The fifth
is in the IPO chart and it is about something the service deliberately does not
do. Look for a sentence about speed.

---

## Stretch goal

Write the prompt that would have produced a better set. Not a longer prompt, a
better one. Then say, in three sentences, what a model still could not have
given this team even with a perfect prompt, and what that means about which
documents are safe to draft this way.

---

## Submission checklist

- [ ] `doc-check-output.txt`
- [ ] `evaluation.md`: five parameters, scored, with quoted evidence
- [ ] `untrue-claims.md`: five claims, each with the quote and the real
      behaviour
- [ ] `arguable.md`: both sides and your position
- [ ] Two rewritten documents, both passing `doc_check.py`
- [ ] Your final paragraph
- [ ] Committed and pushed

---

## Extended options

Choose one. All four are graded on the same scale and assess the same
competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes | Give them |
|---|---|
| Still reading document one, taking notes on every line | SCAFFOLDED |
| Has the doc_check output saved and is reading `CONTRACT.md` | STANDARD or EXTENDED |
| Asks whether a document can be wrong without being false | EXTENDED |
| Says they would never hand documentation to a model anyway | APPLIED |

### SCAFFOLDED

Two documents instead of nine. Read only `design/io-specification.md` and
`docs/user-help.md`, and check both against `CONTRACT.md`.

Score those two on the five parameters. Find **three** untrue claims instead of
five, and they are all in the I/O specification. Rewrite `user-help.md` only.

**Extra checkpoint:** show your instructor your three claims before you start
the rewrite.

**Then answer one question in writing:** `doc_check.py` said `user-help.md` was
almost complete. Was it. What did the tool miss, and why could it never have
caught it.

### STANDARD

The lab as written. Nine documents, five parameters, five claims, two rewrites.

### EXTENDED

Everything in STANDARD, plus **make the tool catch one more thing.**

`doc_check.py` cannot tell whether anything is true. It also cannot tell whether
a document uses a word the reader does not have. Add a check to it: a list of
words that should not appear in `docs/user-help.md`, and a report of any that
do.

Then argue with yourself in writing. A check like that has false positives, and
a check with false positives gets ignored. How would you pick the word list so
that it is worth having, and what would you do when a word on the list is
genuinely the right word.

*Hint, not the answer:* look at how `PLACEHOLDER_PATTERN` is written in the
existing file and read the comment above it about checks that fire on ordinary
sentences.

### APPLIED

Same skill, different domain. Find real documentation for something you use that
is wrong or unusable: a game's wiki, a piece of school software's help page, a
device manual, the instructions on a piece of equipment in another shop in this
building.

Score it on the same five parameters with quoted evidence. Find at least three
claims that are not true of the actual thing, and prove each one by using the
thing. Then rewrite the worst section for the person who would actually be
reading it, and name that person specifically.

Then answer the question this lab is really about: **was it written by somebody
who had used the thing?** Say what in the text told you, and whether an AI wrote
it, a person who built it wrote it, or a person who had never touched it wrote
it. All three failure modes look different on the page.
