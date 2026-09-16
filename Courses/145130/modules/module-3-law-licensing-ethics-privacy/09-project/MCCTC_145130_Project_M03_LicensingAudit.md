# Performance Task: The Licensing Audit
## 145130 Applications of AI · Module 3 · Assigned Week 7 Wednesday · Due Week 8 Monday

**Competencies:** 9.6.1 (adhere to licensing and intellectual property laws), 1.3.8 (verify
compliance with computer and intellectual property laws), 7.1.7 (IP rights and controls in
interactive media), 1.7.13 (protect intellectual property and knowledge), 1.2.12 support (technical
writing to complete forms and create reports).

---

## The request

> From: the instructor, acting as your project's stakeholder
>
> We are submitting to the Congressional App Challenge and the deadline usually falls next week.
> Before anything goes in, I need to know whether every piece of what we are submitting is ours to
> use.
>
> I do not want a summary. I want a list of every third-party thing in the project, what its
> license actually says, and what has to happen before we submit. If something cannot be settled,
> tell me that and tell me who should settle it. If something has no license at all, I need to know
> that most of all.
>
> Do not give me legal advice. Give me the facts and the decisions I have to make.
>
> I need it Monday.

**That is a client request, not an assignment.** Part of the work is extracting the requirements
out of it. Read it twice before you start.

---

## What you are auditing

**Your own project.** The one going to the Congressional App Challenge, or your BPA entry, or the
most recent project you built in this program if neither applies. If you are on a team, the team
does one audit and every member owns specific components.

**If your project has fewer than five third-party components, audit the Study Buddy tree instead**
and then audit yours as the second half. The skill needs a tree with something in it.

---

## Deliverables

| File | What it is |
|---|---|
| `LICENSES.md` | The human-readable audit. Every component, what its license permits, requires, and forbids, and what has to happen |
| `asset-manifest.csv` | The machine-checkable version, same ten columns as Lab M03-01 |
| `THIRD-PARTY-NOTICES.md` | The notices that actually ship. Only for components whose license you found |
| `FINDINGS.md` | Ship blockers, open questions, and what was already correct |
| `decisions.md` | Every judgement call, what you chose, what you rejected, and why |
| `ai-usage.md` | What you asked a model, what came back, what you did with it, what you checked |

Run the completeness check before you submit:

```
python ../../05-labs/lab-m03-01-files/audit_check.py asset-manifest.csv <your project folder>
```

**A `PASS` means your audit is complete. It does not mean it is correct.** A human reads the
reading.

---

## DMAIC

This module uses DMAIC as every project in this program does. The checkpoints are graded under
Process.

### Define · Week 7, Wednesday, Build 2 · 15 minutes

Three sentences in `decisions.md`:

1. What is being submitted, and to whom. Name the audience, because the obligations turn on
   conveying and you have to know what is being conveyed to whom.
2. What "done" means for this audit. Write it as a test somebody else could run.
3. One thing in the project you already suspect has no license. Name it now, before you look.

### Measure · Week 7, Thursday, Build 1

**The component list, before you open a single license.** Walk the tree. Every vendored library,
every asset, every snippet, every model, every dataset, every font, every sound, every image.

Then the naive scan, so you have the number: how many components does a `LICENSE`-file scan miss.

**Checkpoint.** A numbered list and a count. Nothing read yet.

### Analyze · Week 7 Thursday Build 2, and Friday

Read every license. Permits, requires, forbids, and what triggers them. One row per component.

**Checkpoint.** Every row of the manifest filled except `action_needed`. Every `verified_by` cell
names a file you opened or a URL you loaded.

### Improve · Week 8, Monday, Build 1

`action_needed` for every row, `THIRD-PARTY-NOTICES.md`, and the fixes you can make in the block.
The image with no license comes out today. The attribution line gets written today.

**Checkpoint.** `audit_check.py` prints `PASS`, and at least one ship blocker is actually fixed
rather than described.

### Control · Week 8, Monday, Build 2

`FINDINGS.md`, and the part that makes this last: **how does the manifest stay true?** Write the
rule your team follows when somebody adds a component. One sentence, in the project README, where
somebody will read it.

**Checkpoint.** Committed, pushed, and the rule is in the README.

---

## Milestones

| When | What is due |
|---|---|
| Week 7 Wed, end of block | Define, three sentences |
| Week 7 Thu, end of Build 1 | Component list and the naive-scan count |
| Week 7 Fri, end of block | Manifest rows filled except `action_needed` |
| Week 8 Mon, end of Build 1 | `audit_check.py` prints `PASS`, one blocker fixed |
| **Week 8 Mon, end of block** | **Everything, committed and pushed** |

---

## Scope calibration

Three worked examples at different ambition levels. **All three can score 100.** Pick the one that
matches your project, not the one that sounds most impressive.

### Too small

> A team audits three components: two Python packages and one icon set. All three have license
> files. The manifest has three rows, everything says "in order", and `FINDINGS.md` says no
> blockers.

**Why it is too small.** Not because three is too few. **Because nothing was found, and nothing
was found because nothing without a license was looked for.** The fix is not to audit more
packages. It is to walk the tree for fonts, images, sounds, snippets, and anything downloaded, and
to include the model and any dataset. Those are where the findings are.

### About right

> A team audits nine components in their weather dashboard: three vendored Python packages, an icon
> set, a font, a CSS file copied from a tutorial, a background image, the local model, and a sample
> dataset. Six have licenses they could read. Three do not: the font, the background, and the CSS.
> The manifest passes the check. `FINDINGS.md` ranks the three blockers by how fast they can be
> fixed, escalates one licence compatibility question, and names the two components that were
> already correct.

**Why it is right.** It found things. It escalated rather than guessing. It ranked by fixability,
which is what a stakeholder actually needs on a Monday.

### Ambitious

> Same audit, plus: a short script that reads the manifest and the project tree and reports any
> component added since the last audit, wired into the team's checklist. Plus a one-page memo on
> the compatibility question, written for somebody who has to decide it, stating both positions and
> what the answer depends on without reaching a conclusion.

**Why this is ambitious and not reckless.** The script solves the real problem, which is that an
audit is true on the day it is written and false a week later. The memo is the EXTENDED option
from Lab M03-01 applied to the team's own project.

**What would make it reckless:** the memo reaching a conclusion. A student verdict on a contested
licensing question is a guess with a confident voice on it.

---

## Grading: the standard 100-point project rubric

| Dimension | Points |
|---|---|
| Functionality | 25 |
| Code Quality | 20 |
| Documentation | 20 |
| Process | 15 |
| Demonstration | 10 |
| Polish | 10 |

**What each dimension means for this deliverable:**

- **Functionality (25).** The audit is complete. Every component in the tree is in the manifest.
  `audit_check.py` passes. Every `permits`, `requires`, and `forbids` cell is traceable to
  something you read.
- **Code Quality (20).** The manifest is machine-readable and stays that way: correct quoting,
  correct encoding, no shifted columns. Any script you wrote runs and has a comment saying what it
  does not check.
- **Documentation (20).** `LICENSES.md`, `THIRD-PARTY-NOTICES.md`, and `FINDINGS.md`. A person who
  did not do the audit can act on them. `action_needed` says what to do, not what is wrong.
- **Process (15).** The five DMAIC checkpoints, on time, in the repository. `decisions.md` with
  rejected options. `ai-usage.md` with at least one rejection recorded.
- **Demonstration (10).** The five-minute demo below.
- **Polish (10).** No `N/A` where a documented absence belongs. No guesses stated as findings. The
  Control rule is in the project README.

---

## The five-minute demo script

Practise it once. Time it.

| Minute | What you say and show |
|---|---|
| 0:00 | **The number.** "Our project has N third-party components. A `LICENSE`-file scan finds M of them." Show both outputs |
| 0:45 | **The three you could read.** One component, the license open, the one condition pointed at on screen |
| 1:45 | **The one you could not.** The component with nothing, the file that records where it came from, and the words "no license found" |
| 2:45 | **The escalation.** The question you did not answer, the facts it depends on, and who you sent it to |
| 3:45 | **The fix you already made.** Show the diff |
| 4:15 | **The Control rule.** Read the sentence from your README out loud |
| 4:45 | **The honest close.** "Here is what I am still unsure about" |

**The last fifteen seconds carry the Demonstration score.** A demo with no uncertainty in it is a
demo nobody believes.

---

# Instructor appendix

## The reference implementation

`reference-implementation/licensing-audit/asset-manifest.csv`, a complete ten-row audit of the
Study Buddy tree. Verified on the build machine:

```
python 05-labs/lab-m03-01-files/audit_check.py \
    09-project/reference-implementation/licensing-audit/asset-manifest.csv \
    05-labs/lab-m03-01-files/study-buddy
```

```
manifest rows: 10
components found in the tree: 10

PASS  The manifest is complete.
```

**Do not release it during Week 7.** It is also the model answer for Lab M03-01.

## The three ways this project goes wrong, and the intervention

**1. The manifest is a list of packages.** The student walks `requirements.txt` or the imports and
stops. Every media asset, every snippet, and the model are missing.

**Intervention, at the Measure checkpoint, one question:** "What is on your poster?" Then: "Is it
on your list?" Nine times in ten the answer is no, and the student fixes it themselves in four
minutes.

**2. The student decides a question they should escalate.** Usually a compatibility question or a
NonCommercial question. The manifest reads confident and the reasoning is a guess.

**Intervention:** do not correct the verdict. Ask "what would have to be true for the other answer
to be right?" If they can answer, they knew it was arguable and wrote it as settled anyway, which
is a writing problem. If they cannot, they did not know, which is a reading problem. **Two
different fixes, and the question tells you which.**

**3. Blank cells where an absence belongs.** `N/A`, a dash, or nothing at all, on exactly the rows
that matter most.

**Intervention:** write `N/A` and `NO LICENSE FOUND` on the board and ask what a reader does with
each. This is worth doing to the whole room at the start of Week 8 Monday, because it is the most
common failure and it is invisible in a passing `audit_check.py`.

## What to say to a team whose scope is too big

> "Your list has forty-one components because you walked the whole virtual environment. The
> question is what you are conveying. Cut it to what ships and what is in the repository, and put
> the rest in an appendix with one sentence saying why they are out. That sentence is worth more
> than the forty rows."

## What to say to a team whose scope is too small

> "Three rows and no findings. Before you tell me the project is clean, tell me where the font came
> from, where the background image came from, and whether anything in this file was pasted from a
> page. If all three answers are good, I will believe the three rows. Come back with the answers,
> not with more rows."

## Scoring the escalations

**An escalation is worth more than a verdict, and it has to be said out loud before the project
starts**, or students will read "I do not know" as a loss.

A full-credit escalation has four parts: what is not in dispute with a source for each fact, the
positions and what each turns on, what the team did in the meantime, and who should decide.

**An escalation with no facts in it is not an escalation, it is a shrug.** Those get partial credit
and a specific note: name the facts.
