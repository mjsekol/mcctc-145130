# Additional Resources · Week 2
## 145130 Applications of AI · Module 1 · Week 2
### Topics: the emerging technology map, the seam and how it fails, citing a source, what programs solve

Every link below is marked **Confident** or **[VERIFY]**. **Confident** means the address is one
your instructor would bet a class period on. **[VERIFY]** means somebody clicks it before it is
assigned.

**This week is the week to notice the marking.** Wednesday's lesson is about traceable claims, and a
resource page that presented unchecked links as facts would be teaching the opposite of the lesson.
Two of the links below are marked **[VERIFY]** on purpose, and checking them is an assignment rather
than a chore.

**Module 1 ports.** Stub model server **11634**. Streaming stand-in **11635**. Port 11434 is held
for a real model. Every command on this page passes its port.

**Nothing sits between you and the model this week.** There is no layer catching failures on your
behalf, so the failure policy is yours to write. That is Tuesday's work, and it is also the argument
you will make for building a service layer in **Module 5**.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Week 2 lecture notes, four files | Mon-Thu | On-level | 20 min each |
| 2 | Tuesday's note, worked examples 1 to 3 | Tue | On-level | 20 min |
| 3 | `stub_model_server.py`, the ten modes read | Tue | On-level | 15 min |
| 4 | The ten modes run on your own machine | Tue | On-level | 30 min |
| 5 | RFC 9110, HTTP Semantics, selected sections | Tue | Extension | 30 min |
| 6 | Official docs: `urllib.error` and `http.HTTPStatus` | Tue | On-level | 15 min |
| 7 | Model cards, the industry habit behind Wednesday | Wed | Extension | 20 min |
| 8 | A citation to verify, as the Wednesday exercise | Wed | On-level | 20 min |
| 9 | NIST AI Risk Management Framework | Mon Wed | Extension | 25 min |
| 10 | A free video on emerging technologies | Mon | Remediation | under 20 min |
| 11 | Gate 1 Reps 04, 05, 08, 09, 10, 15 | Mon-Thu | Review | 10 min each |
| 12 | SQ-12 Read the Source | Fri | Extension | one block |
| 13 | Your own `LICENSING.md`, checked against Thursday | Thu | Required | 10 min |

---

## 1. Primary reading · the four Week 2 lecture notes

The on-level reading for the week. Each carries three worked examples, the wrong version and what it
costs, vocabulary, and three self-check questions with answers.

- Monday: [`../03-lecture-notes/MCCTC_145130_Notes_TheEmergingTechnologyMap.md`](../03-lecture-notes/MCCTC_145130_Notes_TheEmergingTechnologyMap.md)
- Tuesday: [`../03-lecture-notes/MCCTC_145130_Notes_IntegratingIntoSystemsThatExist.md`](../03-lecture-notes/MCCTC_145130_Notes_IntegratingIntoSystemsThatExist.md)
- Wednesday: [`../03-lecture-notes/MCCTC_145130_Notes_ExtractValidInformationAndCite.md`](../03-lecture-notes/MCCTC_145130_Notes_ExtractValidInformationAndCite.md)
- Thursday: [`../03-lecture-notes/MCCTC_145130_Notes_WhatProgramsAndScriptsSolve.md`](../03-lecture-notes/MCCTC_145130_Notes_WhatProgramsAndScriptsSolve.md)

**Why these rather than a vendor page about emerging technology.** Monday's list is nine terms that
appear on your exam, and every vendor page about them is selling something. The note gives each one a
sentence on what it is and a sentence on what it has to be bolted onto, which is the part the exam
asks about and the part a brochure leaves out.

**Monday's note is the one to read before class rather than after.** The walk through the building
goes better if you already know what services virtualization means, because you will be looking for
it rather than being told where it is.

**Time.** About 20 minutes each. **Level.** On-level.

---

## 2. What a failure actually is · Tuesday's note, worked examples 1 to 3

[`../03-lecture-notes/MCCTC_145130_Notes_IntegratingIntoSystemsThatExist.md`](../03-lecture-notes/MCCTC_145130_Notes_IntegratingIntoSystemsThatExist.md) ·
**Confident**, it is a file in this repository.

**What it is.** Worked example 1 is a seven-row table produced by `seam_report.py` on the build
machine: one help request, sent once per stand-in mode, so the only thing changing between rows is
the failure. Worked example 2 is the retry rule. Worked example 3 is the four sentences a caller
owes the person at the keyboard.

**Why this one.** Tuesday's whole lesson is that a finished seam has three parts: a contract, a
failure policy, and a record of where each value came from. This is all three, written down, against
a system you can start on your desk in ninety seconds. **There is no service document to read this
week, because there is no service.** That absence is the lesson.

**Assign a question.**

1. *Find the `unusable` row. Every transport-level check passes and the answer is useless. Name the
   five checks that passed, and say what a program would have to do to catch it.*
2. *Two rows retried and five did not. Write the rule in one sentence before you read the one in
   worked example 2. Then find the honest complication underneath it, about a real model sampling
   with randomness, and say whether it changes your rule.*
3. *Worked example 3 gives `timeout` and `rate_limited` the same sentence. Say why that is correct,
   and name two kinds that must not share one.*

**Time.** 20 minutes. **Level.** On-level.

---

## 3. Primary source · the ten modes, in `stub_model_server.py`

[`../05-labs/local-model-kit/stub_model_server.py`](../05-labs/local-model-kit/stub_model_server.py) ·
**Confident**, it is a file in this repository.

**What it is.** The comment block at the top documents all ten failure modes, one line each, plus the
three extra endpoints a real server does not have.

**Why this one.** Lab M01-02 asks you to break the seam on purpose. **Step 2 of the lab is reading
this comment block**, and students who skip it pick three modes that fail the same way and produce a
table with nothing in it. Read the ten before you choose five.

**Assign a question.** *Sort the ten modes into two groups: the ones where nothing usable arrives, and
the ones where something arrives that your program still cannot use. Which group is more dangerous,
and why?* The second group is the one that reaches a person looking like an answer.

**Then read `/stub/stats`.** It reports how many times the stand-in was asked to generate, which is
how you see a retry from outside your own program. That column is what turns a claim about your retry
rule into evidence.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. Interactive practice · the stub's ten modes

[`../05-labs/local-model-kit/stub_model_server.py`](../05-labs/local-model-kit/stub_model_server.py) ·
**Confident**, it is a file in this repository.

**What it is.** A stand-in model server with ten selectable behaviours: `success`, `success_prose`,
`unusable`, `slow`, `error`, `rate_limited`, `malformed`, `not_done`, `missing_response`, and
`empty_response`. This is the interactive practice source for the week, and it is better than any
online sandbox because you control the failure.

**Start it in the mode you want:**

```
python stub_model_server.py --port 11634 --mode slow --delay 6
```

**Or switch modes while it is running**, by posting to `/stub/mode` on port 11634, which is what the
seam lab does.

**Why this one.** A real model fails rarely and at inconvenient times. This one fails on demand, ten
different ways, and every failure maps to a row in Tuesday's seven-row table. You get a week of
production incidents in one Build block.

**Do the run yourself, in this order.** `seam_report.py` waits five seconds before giving up, so start
the stand-in with `--mode success --delay 6` and send a request. It will time out. Then read the
elapsed time, the kind your own code worked out, and the call count from `/stub/stats` together, and
say what a person staring at the screen would have experienced. **The point of Tuesday is that all
three matter and none of them is a crash.**

**Time.** 30 minutes. **Level.** On-level.

---

## 5. Official documentation · RFC 9110, HTTP Semantics

`https://www.rfc-editor.org/rfc/rfc9110` · **Confident.**

**What it is.** The standards document that defines what HTTP methods and status codes mean. It is
long. You are not reading all of it.

**Why this one.** Tuesday's seam report table is every row HTTP 200 with five of seven answers not
coming from the model. That is legal, and this is the document that says so. Knowing the difference
between "the transport succeeded" and "the answer is good" is the whole lesson, and here it is from
the source rather than from a blog.

**Assign a question.** *Find what the document says about idempotent methods. Your requests are all
POST, which the standard does not call idempotent, and your retry rule is about the kind of failure
rather than about the method. Say why that is defensible here, and name one system where it would not
be.* There is a real argument on both sides and you are graded on the argument.

**Use the search inside the page.** Reading a standards document by scrolling is how students decide
standards documents are unreadable.

**Time.** 30 minutes. **Level.** Extension.

---

## 6. Official documentation · `urllib.error` and `http.HTTPStatus`

`https://docs.python.org/3/library/urllib.error.html` · **Confident.**
`https://docs.python.org/3/library/http.html#http.HTTPStatus` · **Confident.**

**Why these two.** `one_request.py` catches `urllib.error.HTTPError` and prints the body anyway,
because the stand-in's 400 carries a body that says why: `this stub only supports stream: false`.
Discarding that body throws away the one sentence that names the fix.

**Assign a question.** *Find what `HTTPError` says about being both an exception and a response. Then
explain why your program has to read the body of a 400 rather than discarding it, and what the person
at the keyboard loses if it does not.*

**A status code reference**, if you want the human-readable version rather than the RFC:
`https://developer.mozilla.org/en-US/docs/Web/HTTP/Status` · **[VERIFY].** MDN has reorganised its
HTTP reference before. If that address does not resolve, search MDN for "HTTP response status codes"
and take whatever path it currently uses.

**Time.** 15 minutes. **Level.** On-level.

---

## 7. The industry connection · model cards

**Hugging Face Hub documentation, model cards.** Site `https://huggingface.co/` · **Confident.**
The documentation page at `https://huggingface.co/docs/hub/model-cards` · **[VERIFY].**

**What it is.** The industry's standard way of writing down, next to a released model, what it was
trained on, what it is for, what it is not for, and what is known about how it fails.

**Why this one.** Wednesday's lesson is that a claim is traceable when a reader can reach the support
without asking you. A model card is that idea applied to a model, by the people shipping it. It is
also the strongest available answer to the vendor who says their product uses AI and will not say
more.

**Assign a question.** *Open any model card on the Hub. Find one claim on it you could check and one
claim you could not. Say what would have to be added to the second one to make it checkable.*

**Related, and this one is the reason the habit exists.** A widely cited paper on the same idea for
datasets is titled **Datasheets for Datasets**. **[VERIFY] the authors, the year, and the publication
before anyone quotes it.** That verification is the Wednesday exercise, not an inconvenience. If you
cannot find it, write down where you looked and report the failed search, which is exactly what the
lecture note tells you to do.

**Time.** 20 minutes. **Level.** Extension.

---

## 8. A citation to verify, as the Wednesday exercise

**There is no link in this section on purpose.**

Wednesday's instruction segment opens with the Halloran Institute line, which the lecture note is
open about having been invented for the slide. The exercise that follows is the one that matters, and
it does not need a supplied link. Take a claim about AI that you are confident about, from anywhere,
including from a model, and try to reach its support.

**What you produce, either way.**

- If you find the source, quote what it **actually** says. It is usually narrower than the claim.
- If you do not find it, write down where you looked, what you searched for, and what you concluded.
  **A documented failed search is a result.** An undocumented one is a gap somebody else has to redo.

**Why no link.** Handing you a pre-checked citation to check is a worksheet. The competency, 1.2.1, is
about what you do when nobody has checked it for you, which is every time after this class.

**Time.** 20 minutes. **Level.** On-level.

---

## 9. The emerging technology connection, from a source that is not selling anything

**NIST, the Artificial Intelligence Risk Management Framework.** Site `https://www.nist.gov/` ·
**Confident.** The framework's landing page at
`https://www.nist.gov/itl/ai-risk-management-framework` · **[VERIFY].**

**Why this one.** Monday's deliberate error is the sentence that could not be wrong. This is the
opposite kind of document: a government standards body writing down what could go wrong with these
systems, in categories, without a product to sell. It is also the vocabulary you will meet again in
Module 3.

**Assign a question.** *Find any one named risk category. Write the version of it that applies to the
two programs on your desk, in one sentence, naming which of the two carries the risk.*

**If the deep address does not resolve**, search nist.gov for "AI Risk Management Framework" and
confirm you have landed on a NIST page rather than on somebody's summary of it. Landing on a summary
and citing it as NIST is the exact failure Wednesday is about.

**Time.** 25 minutes. **Level.** Extension.

---

## 10. A free video, under 20 minutes

**[VERIFY]. No specific video is linked here, because none was confirmed live.** Padding this section
with a video nobody has watched would cost a class period, and it would be the same defect the
Infographic Autopsy is built out of.

**What to search for, and what to check before assigning it.** A video that names the emerging
technologies on Monday's list and says what each one connects to. Watch the whole thing first, and
check three things:

1. Does it give any number without a source? If yes, that video is now a Gate 2 artifact rather than
   a resource, and it is a good one.
2. Does it define machine learning and artificial intelligence as different things, or use them
   interchangeably? The note says which is the subset of which.
3. Does it make a claim that could not be wrong? If the whole video is transformation and disruption,
   it teaches nothing Monday needs.

**A video that fails check 1 is worth ten minutes of class time**, played and stopped. Say so when you
show it.

**Level.** Remediation.

---

## 11. Gate 1 reps worth redoing on your own

From [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md).

- **Rep 04** (TRACE) and **Rep 09** (FIX): tracing a claim, and rewriting one so a reader can check it
- **Rep 08** (FIX): a claim cut back to what it can actually support
- **Rep 05** (TRACE) and **Rep 13** (WRITE): the retry rule in four situations, and the one sentence
  each kind of failure earns
- **Rep 10** (FIX): the program that assumes the model answered with JSON
- **Rep 15** (WRITE): a problem statement that names who is hurt and names nothing you would build

**Ten minutes each, plain editor, no AI.** Rep 09 and Rep 04 are the two most worth redoing before
Friday, because Gate 2 W02 rewards a reader who checks rather than a reader who runs.

**Level.** Review.

---

## 12. Side quest

**SQ-12 Read the Source**, from
[`../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md).
Unlocks any time after Unit 4 of 145060, so it is open to you. One block, difficulty two stars.

**Why this one this week.** It ends with checking the project's license and stating what shipping it
in your own work would require of you. That is Thursday's `LICENSING.md` habit done against a real
repository instead of a template, and it is the closest thing in the catalog to Wednesday's
competency, 1.2.1.

**Pick something under about 500 lines.** A student who picks a framework spends the block scrolling.

**Level.** Extension.

---

## 13. Your own `LICENSING.md`, ten minutes on Thursday

You created it in Week 1. **Open it Thursday and check it against what actually happened this week.**

Three questions:

1. Did anything enter your repository this week that is not yours? Starter code, a snippet, an image,
   a font, a dataset, a model.
2. For each one, can a reader reach its terms without asking you? That is the same test as a
   traceable claim, applied to a file.
3. Is there anything whose terms you could not find? **That goes in the last table as a finding**,
   with where you looked, rather than being left blank.

**Module 3 audits this file.** A student who starts the audit in Week 7 from an empty file spends a
period reconstructing six weeks from memory, and reconstructing from memory is how invented
citations get written.

**Level.** Required of everyone.

---

## For the student who is behind

1. Monday's lecture note, the nine technologies, one sentence each in your own handwriting
2. Tuesday's lecture note, worked example 1, the seven-row table, with the `unusable` row read last
   and out loud
3. Wednesday's lecture note, the four kinds of support ranked
4. Thursday's lecture note, worked example 3, the problem statement about a person

## For the student who is ahead

- Lab M01-02 EXTENDED, all ten stub modes plus a refused request
- RFC 9110 on idempotency, and the argument about the retry rule
- The model card question, done against three different models and compared
- SQ-12
