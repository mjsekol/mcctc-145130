# Lab M03-01: License Archaeology
## 145130 Applications of AI · Module 3 · Week 7, Tuesday and Wednesday

**Gate:** 3 (open tooling, decision log required). **Duration:** Week 7 Tuesday Build 1, 40
minutes, and Week 7 Wednesday Build 2, 55 minutes.

**Files:** `lab-m03-01-files/`
**Competencies:** 9.6.1 (adhere to licensing and intellectual property laws), 1.3.8 (verify
compliance with computer and intellectual property laws), 7.1.7 (IP rights and controls in
interactive media), 1.7.13 (protect intellectual property and knowledge).

**Build 1 is 40 minutes of build work**, because the Gate 1 rep runs in its first 10
minutes.

---

## Before you start: this is not legal advice

**Your instructor is not a lawyer and this lab is not legal advice.** You are learning to
read a license and write down what it says, which is a professional skill and not a legal
opinion. Where you cannot settle something, the correct output is a written finding that says
what the answer depends on and who should decide it. **Escalating is a full-credit answer in
this lab. Guessing is not.**

**The project you are auditing is a composite.** Study Buddy, its team, and every third-party
component in its tree were invented for this course. The license identifiers are real
identifiers. The problems are real problems that appear in student and professional projects
constantly. None of the named projects, fonts, models, or datasets exist, so do not search for
them and do not cite them as real.

---

## The scenario

The Study Buddy team wants to put their flashcard app on the showcase table next week and
sell printed decks for two dollars each. Their README says every component is credited and
their repository has a LICENSE file at the top, so they think they are finished. You have been
asked to check before the poster goes to the printer.

## What you will build

A complete asset manifest for the Study Buddy project: every component, its license, what that
license permits, requires, and forbids, and what has to happen before anything ships.

---

## What is in `lab-m03-01-files/`

| File | What it is |
|---|---|
| `study-buddy/` | The project. Ten third-party components, some licensed, some not. |
| `asset-manifest-starter.csv` | The manifest, with the header row and one example row filled in. |
| `audit_check.py` | Checks your manifest for **completeness**. It never checks your reading. |

---

## Part 1 · Week 7 Tuesday, Build 1, 40 minutes: find everything

### Step 1. Run the project so you know what it does

```
cd lab-m03-01-files/study-buddy
python study_buddy.py notes/chemistry.txt
```

**Observable result.** A five-row table of terms, then `6 cards written to notes\deck.json`.
Delete `deck.json` when you are done looking at it.

### Step 2. List what has to be accounted for, before you go looking

In your notes, write down every third-party component in the tree. Walk `vendor/`, `assets/`,
`snippets/`, `model/`, and `data/`.

**Observable result.** A list of ten paths. **Do this before step 3.** An audit that starts
from what you find instead of from what has to be accounted for will always be incomplete, and
you saw exactly that failure in Monday's lecture.

### Step 3. Run the naive scan and compare it with your list

Type the first scan from `03-lecture-notes/MCCTC_145130_Notes_WhatIntellectualPropertyProtects.md`,
worked example 1, and run it from `lab-m03-01-files/`.

**Observable result.** Three lines and a confident closing sentence. Write down how many of
your ten components it failed to mention.

### Step 4. Find the license evidence for each of the ten

For each path on your list, open the directory and look for, in this order: a file named
`LICENSE`, `LICENSE.txt`, `COPYING`, or `NOTICE`; then a license header inside a source file;
then nothing.

**Observable result.** Ten rows in your notes, each one saying where the evidence is or
`NOTHING FOUND`. Three of them say nothing found.

### Step 5. Copy the starter manifest and fill in `path`, `component`, `origin`

```
cd lab-m03-01-files
copy asset-manifest-starter.csv asset-manifest.csv
```

Add a row per component. Leave the license columns blank for now.

**Observable result.**

```
python audit_check.py asset-manifest.csv study-buddy
```

prints `manifest rows: 10` and `components found in the tree: 10`, and then fails on blank
cells. Failing here is correct. You have not filled them in yet.

---

## Part 2 · Week 7 Wednesday, Build 2, 55 minutes: read, and write down what you read

### Step 6. Read the MIT license in full, and write its three answers

Open `study-buddy/vendor/pocketgrid/LICENSE`. It is 169 words.

**Observable result.** The `permits`, `requires`, and `forbids` cells for pocketgrid, in your
own words, with the requires cell traceable to one sentence you can point at.

### Step 7. Read Apache 2.0 section 4, at its published text

`study-buddy/vendor/lanternparse/LICENSE` points you at the Apache Software Foundation's
published text. Open it. Read section 4. Then open `vendor/lanternparse/NOTICE`.

**Observable result.** The lanternparse row filled in, and `verified_by` set to
`READ: https://www.apache.org/licenses/LICENSE-2.0 [VERIFY]`. Also one line in your findings
about whether the `NOTICE` contents appear anywhere in the Study Buddy README.

### Step 8. Read the GPL header in sortwell, and find what is missing

Open `study-buddy/vendor/sortwell/sortwell.py`. Read the header. Then look for a copy of the
license anywhere in the tree.

**Observable result.** Two findings written down. One about what is missing from the tree. One
about what the project's own `LICENSE` file says compared with what is inside `vendor/`.
**Neither finding is you deciding the question.** Both are you surfacing it.

### Step 9. Read the Creative Commons licenses, in the legal code

`assets/icons/LICENSE.txt` and `assets/sounds/LICENSE.txt` each point at a Creative Commons
page. On that page, the short summary is the **deed**. The link from it goes to the **legal
code**, which is the license. Read the legal code.

**Observable result.** The attribution items listed in the icons row's `requires` cell, and the
NonCommercial definition quoted in your findings in the license's own words.

### Step 10. Write the icons attribution line, correctly

Two icons were recolored. Check `assets/icons/icons.md`.

**Observable result.** One sentence in your findings that carries every attribution item,
including the statement that the material was modified.

### Step 11. Read the model license and the dataset card

`model/LICENSE.txt` and `data/flashcard_seed/DATASET_CARD.md`.

**Observable result.** The model row filled in, including the Section 4 restrictions and
Section 2's display requirement. And the dataset row, which has to say what is true today and
what would trigger the ShareAlike condition.

### Step 12. Fill in `action_needed` for every row, and run the check

**Observable result.**

```
python audit_check.py asset-manifest.csv study-buddy
```

prints

```
manifest rows: 10
components found in the tree: 10

PASS  The manifest is complete.
This checks completeness only. It does not check your reading.
A human still has to read every permits, requires, and forbids cell.
```

**A green result means your manifest is complete. It does not mean your audit is correct.**

### Step 13. Write `FINDINGS.md`

Three sections:

1. **Ship blockers.** Components that cannot go out as they are. Ranked by how fast they can be
   fixed.
2. **Open questions.** Things you could not settle, what the answer depends on, and who should
   decide. At least one of your entries belongs here.
3. **What was already correct.** Two of the ten components are fine. Say which and why, because
   an audit that only reports problems is not an audit.

---

## Acceptance criteria

- [ ] Ten rows in `asset-manifest.csv`, one per component
- [ ] `python audit_check.py asset-manifest.csv study-buddy` prints `PASS`
- [ ] Every `permits`, `requires`, and `forbids` cell traces to something you read
- [ ] Every `verified_by` cell names a file in the tree, a URL you opened, or `NONE FOUND`
- [ ] The three components with no license are identified as such, with the words "no license
      found" rather than a guess
- [ ] The icons attribution line carries all the items, including the modification statement
- [ ] `FINDINGS.md` has all three sections, and at least one entry in Open questions
- [ ] A decision log entry for any judgement call you made
- [ ] Committed and pushed

---

## If it breaks

**`FAIL  No project tree at study-buddy-typo`**
You are in the wrong directory, or you typed the path wrong. The second argument is a folder,
not a file. Run it from `lab-m03-01-files/`.

**`FAIL  missing columns: origin, license_id, license_file, permits, requires, forbids, action_needed, verified_by`**
Your header row lost columns. This happens when a spreadsheet re-saves with a different
delimiter or when you built the file by hand. Copy the header line out of
`asset-manifest-starter.csv` again.

**Your row count is right but the check reports components not in the manifest, and
`verified_by names nothing, which is not in the tree`**
A cell contains a comma and is not quoted, so the columns shifted right and the last column now
holds something from the middle of your row. Put double quotes around any cell containing a
comma, or let your editor's CSV mode do it.

**`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x93 in position 123: invalid start byte`**
Your manifest was saved in the Windows default encoding, not UTF-8, and it contains a curly
quote or a dash your spreadsheet inserted. Save as CSV UTF-8, or retype the cell with plain
straight quotes.

---

## Stretch goal

Write `THIRD-PARTY-NOTICES.md` for Study Buddy: the file that would actually ship, carrying every
notice the licenses require. Then diff it against the README's current credits section and count
how many items were missing. Do not include a notice for a component whose license you could not
find, because that would be a claim you cannot support.

---

## Submission checklist

- [ ] `asset-manifest.csv` in your repository
- [ ] `FINDINGS.md` with three sections
- [ ] `audit_check.py` output pasted into `FINDINGS.md`, showing `PASS`
- [ ] Decision log entry for every judgement call
- [ ] AI usage log entry if you used a model at any point
- [ ] Pushed

---

# Extended options

All four assess the same competency and grade on the same 100-point scale.

## How to choose, three observable signals

1. **The step 2 list.** A student who produced ten paths before looking at any file is ready for
   STANDARD or above. A student who produced four is on SCAFFOLDED.
2. **The step 8 answer.** A student who writes "sortwell is GPL so this project cannot be MIT" has
   decided a question rather than surfacing it. That is a reasoning error in the right direction,
   and it is the EXTENDED student. A student who writes "the GPL says you cannot sell software" has
   not read the header and belongs on SCAFFOLDED.
3. **Time at step 9.** A student still on the Creative Commons deed twelve minutes in is reading
   the summary and needs the SCAFFOLDED prompt that names the legal code link explicitly.

## SCAFFOLDED

Same target, smaller scope, more structure.

- The component list is given to you. All ten paths, in `instructor/` handout form.
- You audit **six** components: pocketgrid, sortwell, icons, sounds, images, model. The other four
  rows are filled in for you.
- Each of the six has a three-question worksheet: what does it permit, what does it require, what
  does it forbid, with the file to open named on the line.
- Checkpoint after every two components rather than at the end.
- `FINDINGS.md` is three bullet points rather than three sections.

**Same grading scale.** The competency is reading a license and writing down what it says, and six
components assesses that as well as ten.

## STANDARD

The lab as written above.

## EXTENDED

Everything in STANDARD, plus the compatibility question.

Write a one-page memo on the sortwell situation for somebody who has to decide it. Your memo has
to:

- State what is not in dispute, with a file path for each fact
- State the argument that the combined work carries the GPL's conditions
- State, fairly, why the boundary of a combined work is genuinely argued, and what the different
  positions turn on
- **Not reach a conclusion.** Recommend what the team does next and who decides

**The hint, and it points at documentation rather than an answer:** the Free Software Foundation
publishes its own position on this in its GPL frequently-asked-questions material. Read it, note
that it is one party's stated position, and look for what it says the answer depends on rather than
what it concludes. **[VERIFY]** the current address at `https://www.gnu.org/licenses/`.

## APPLIED

Same skill, different domain: **audit your own repository.**

Pick any project you have built in this program, from any of your three years. Run the component
list step on it. Produce a manifest with the same columns. Most of you will find between two and
six components you have never looked at, and at least one image whose source you cannot name.

Deliverables: the manifest, a `FINDINGS.md`, and one paragraph answering the question this whole
lab exists for: **if this went on a competition submission tomorrow, what would you have to fix
tonight.**

**This is the option to give the student who asks when they would ever use this.** The answer
arrives about eight minutes in, when they find the font.
