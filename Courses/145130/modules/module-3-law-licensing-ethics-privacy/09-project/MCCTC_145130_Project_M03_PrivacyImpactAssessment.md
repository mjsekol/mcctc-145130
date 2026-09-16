# Performance Task: The Privacy Impact Assessment
## 145130 Applications of AI · Module 3 · Assigned Week 9 Monday · Due Week 9 Friday

**Competencies:** 2.1.12 (privacy security compliance on systems: HIPAA, PCI, SOX, ADA, GDPR,
EUDPR), 2.1.1 (confidentiality, integrity, availability), 2.14.2 (how AI impacts society and the
ethics of its usage), 1.3.8 (verify compliance with computer laws and regulations), 1.2.12
(technical writing to complete forms and create reports), 3.2.1 (data and application security:
**taught here, not on the WebXam blueprint**).

---

## The request

> From: the instructor, acting as the office that has to decide
>
> Somebody has proposed an AI feature for the building. Before anybody builds it, I need an
> assessment.
>
> Tell me what data it touches and why each field is needed. Tell me which framework governs each
> category and what that framework is for. Tell me what could go wrong and **who gets hurt, by
> name of role.** Tell me what the feature refuses to collect. Tell me where the model runs and
> whether anything leaves the building. Tell me how long we keep things and who deletes them. Tell
> me who cannot use this as designed.
>
> And tell me plainly what you do not know. I would rather have three honest unknowns than a
> document that answers everything.
>
> Friday, start of Build 2. Grading period closes.

---

## Pick a workflow

Three invented workflows. **All three are composites written for this course.** The workflows are
realistic because schools really do consider features like these. **None of them describes a real
proposal, a real school, or a real person.**

**Use no real student data, no real names, no real records, and no real messages.** If a step
tempts you toward a real one, invent a stand-in. That is not a workaround, it is the rule.

### Workflow B · The library homework helper

A kiosk in the library where a student types a homework question and a locally hosted model
answers. The proposal logs every question and answer "so we can improve the service" and posts a
weekly count of questions by subject on a staff dashboard.

### Workflow C · The counselor request triage

Students submit a free-text request to see a counselor through a web form. A locally hosted model
sorts the requests into "urgent", "this week", and "general", and orders the counselor's queue.
The proposal keeps the original text and the model's classification.

### Workflow D · The early dismissal call list

The front office receives dismissal requests from guardians by email all morning. A locally hosted
model reads the emails, extracts the student name and the dismissal time, and builds the call list
for the day. A secretary checks the list before any student is called.

**A workflow of your own is allowed** if you clear it by Monday of Week 9. It has to be a real
school workflow you can describe accurately, it has to be one you invent details for rather than
observe, and it has to involve a model making or supporting a decision about people.

**Workflow A, the attendance letter drafter, is taken.** It is the worked example from Wednesday's
lecture and you have already seen the answer.

---

## Deliverables

| File | What it is |
|---|---|
| `pia-<workflow>.md` | The assessment, from the template, all eleven sections |
| `refusals.md` | Expanded section 6, if it does not fit in the assessment |
| `questions-sent.md` | The questions you would send a vendor, and what you would do with each answer |
| `decisions.md` | Every judgement call, what you chose, what you rejected, and why |
| `ai-usage.md` | What you asked, what came back, what you did, what you checked |

Template: `pia-files/MCCTC_145130_PIA_Template.md`. **Keep the section headings exactly as they
are written**, because the checker matches them character for character.

Run the completeness check before you submit:

```
python pia-files/pia_check.py pia-<workflow>.md
```

It checks that you filled in the form. **It does not check your analysis and it is not legal
advice.** Both of those are in its own output, because a tool that does not state its limits
trains you to believe it has none.

---

## DMAIC

### Define · Week 9, Monday, Build 2 · 15 minutes

Sections 1 and 2. What exists afterwards that does not exist now, who asked for it, and the
question that sets everything else: **what happens if nobody builds it.**

**That question decides how much risk is acceptable.** A feature that saves an afternoon does not
get to take on a risk that would be unacceptable for a feature that saves nothing.

**Checkpoint.** Two sections and the nobody-builds-it answer.

### Measure · Week 9, Tuesday, Build 1

Section 3, the data inventory. One row per field, every cell filled. Build it **from the purpose**,
not from a database schema. A field you cannot write a "why it is needed" for is your first
finding.

**Checkpoint.** At least five rows. No blank cells. No `UNKNOWN` in the retention column.

### Analyze · Week 9, Tuesday Build 2 and Wednesday

Sections 4, 5, 6, and 7.

- Section 4 stays at the purpose level. **Name the framework and say what it is for.** Do not state
  a section number you have not read.
- Section 5 names the person who feels the loss in each of the three CIA paragraphs.
- **Section 6 is the section that carries this document.** Every field you considered and rejected,
  with a reason.
- Section 7 has at least four risks and at least one created by the model rather than the data
  store.

**Checkpoint.** Sections 4 through 7 drafted, section 6 with at least four refusals.

### Improve · Week 9, Thursday, Build 2

Sections 8, 9, and 10. The vendor questions, the retention plan including derived material, and
accessibility.

**The derived material list is where this section is won.** Draft files, application logs, the
model server's own request log, caches, exports, and backups. None of those are in the database the
retention policy was written about.

**Checkpoint.** Section 9 names a person for each category, or says plainly that it could not.

### Control · Week 9, Friday, Build 1

Section 11. One of the three recommendations, in those exact words, and every `UNKNOWN` from the
document listed with who could answer it and what you would do if the answer came back badly.

Then `pia_check.py`. It will tell you if your unknowns do not add up.

**Checkpoint.** `PASS`, committed, pushed by the start of Build 2.

---

## Milestones

| When | What is due |
|---|---|
| Week 9 Mon, end of block | Sections 1 and 2 |
| Week 9 Tue, end of Build 1 | Section 3, five rows or more, no blanks |
| Week 9 Wed, end of block | Sections 4 through 7, section 6 with four refusals or more |
| Week 9 Thu, end of block | Sections 8, 9, 10 |
| **Week 9 Fri, start of Build 2** | **Everything, `pia_check.py` passing, committed and pushed** |

**Grading Period 1 closes Friday.** The last commit pushed before Build 2 is the submission.

---

## Scope calibration

**All three of these can score 100.**

### Too small

> Workflow D. Section 3 has five rows: student name, guardian name, dismissal time, email, and
> date. Section 6 says "we do not collect anything unnecessary." Section 7 has four risks, all of
> them about the database. Section 11 says build as designed.

**Why it is too small.** Not the row count. **Section 6 is a sentence instead of a list, which
means no refusal was ever made**, and section 7 has no risk created by the model, which means the
model was treated as a neutral pipe. Workflow D's real risk is that the model extracts the wrong
name from an email and a child is called to the office who should not have been.

**The fix:** four named refusals with reasons, and one risk row whose cause is the model.

### About right

> Workflow C. Section 3 has seven rows, including one for the model's classification and one for
> whatever the web server logs, which the student marked as a finding rather than a row they could
> fill in. Section 5's integrity paragraph names the real failure: the model classifies an urgent
> request as general and the queue order is now a decision nobody made. Section 6 lists six
> refusals including the student's name in the prompt. Section 7 has six risks, three of them
> caused by the model. Section 8 has two answers and one `UNKNOWN`. Section 11 says build with the
> changes listed below, with four changes, and carries the one unknown down from section 8.

**Why it is right.** The classification is treated as data. The unanswered question is carried
through to the recommendation instead of disappearing. Somebody is named in every risk row.

### Ambitious

> The same assessment, plus a runnable `minimize.py` for the workflow with its own field lists and
> a `check.py` that proves the log line carries no personal value. Plus, in section 8, the actual
> test: the source scanned for outbound addresses, and the feature run with the network path
> blocked, with the output pasted in.

**Why this is ambitious and not reckless.** Both additions turn a claim in the document into
something checkable. Section 8 stops being a set of questions and becomes a set of answers with
evidence.

**What would make it reckless:** using a real workflow with real data to make it feel more real.
**That is not ambition, it is the one rule this course does not bend.**

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

- **Functionality (25).** The assessment does its job. Every section present, the inventory built
  from the purpose, at least four risks with a named harmed person, at least one risk caused by the
  model, and a recommendation consistent with the unknowns above it.
- **Code Quality (20).** Here this is **the design the assessment describes**. Minimization is
  specific per purpose. Nothing personal goes into a prompt. Failure modes fail closed. Any code
  you wrote runs and says what it does not check.
- **Documentation (20).** Section 6 and section 11. A person who did not write it can act on it.
  Every `UNKNOWN` in the body appears in section 11 with an owner.
- **Process (15).** Five DMAIC checkpoints on time. `decisions.md` with rejected options.
  `ai-usage.md` with at least one rejection recorded.
- **Demonstration (10).** The four-minute walk-through below.
- **Polish (10).** `pia_check.py` passes. No real data anywhere. No framework section number you
  did not read. The not-legal-advice statement is in the document.

---

## The four-minute walk-through

Friday, Build 2, to the class or to the instructor.

| Minute | What you say and show |
|---|---|
| 0:00 | **The feature in one sentence**, and what happens if nobody builds it |
| 0:30 | **One inventory row**, and why that field is needed. Then one you refused, and why |
| 1:15 | **The risk the model creates.** Not the database. The model |
| 2:00 | **The derived material.** Name the place data would have accumulated that nobody had written a rule about |
| 2:45 | **Your recommendation**, in the exact words, and the unknown that drove it |
| 3:30 | **What you are still unsure about** |

**The 1:15 and 2:00 slots are the ones that separate assessments.** Anybody can list a database
risk. Naming what the model itself introduces, and finding the log nobody owns, is the work.

---

# Instructor appendix

## The reference implementation

`reference-implementation/privacy-impact-assessment/pia-attendance-letters.md`, a complete
assessment of Workflow A. Verified on the build machine:

```
python 09-project/pia-files/pia_check.py \
    09-project/reference-implementation/privacy-impact-assessment/pia-attendance-letters.md
```

```
sections found: 11 of 11
data inventory rows: 6
risk rows: 5

PASS  The assessment is complete.
```

**Workflow A is the worked example from Wednesday's lecture and is not available to students**, so
this file can be projected during Week 9 without giving anybody their own answer. Use it for
section 6 and section 11 specifically.

## The three ways this project goes wrong, and the intervention

**1. The inventory comes from the schema.** The student lists every field the system has rather
than every field the feature needs, and then writes a "why it is needed" for each one after the
fact. The result reads complete and has made no decisions.

**Intervention, at the Measure checkpoint, one question:** "Which row would you delete if I told
you the feature has to run on three fields?" If they can answer instantly, the inventory was built
from the purpose. If they cannot, it was built from the schema. **Then ask them to build it again
from the sentence in section 1**, which takes ten minutes and produces a different document.

**2. Section 6 is a sentence.** "We do not collect anything unnecessary." Nothing was refused,
because a refusal leaves nothing behind and feels like empty work.

**Intervention:** name three specific fields the workflow could plausibly have taken and ask why
each one is out. Usually the student has good reasons and never wrote them down. **Say the durable
reason out loud: in six months somebody adds the field back and nobody remembers why it was out.**

**3. The recommendation contradicts the unknowns.** Section 8 has three `UNKNOWN` rows and section
11 says build as designed. `pia_check.py` catches the arithmetic version of this and not the
judgement version.

**Intervention:** read section 8 and section 11 out loud, in that order, and stop. Students hear it
immediately. **They write it because they want the thing built**, which is worth naming, because
that is exactly the bias they found in three Gate 2 artifacts.

## What to say to a student whose scope is too big

> "You have eighteen inventory rows because you assessed the whole student information system. The
> assessment is about this feature. Cut it to what this feature touches, and put the rest in one
> sentence saying the feature does not reach them. That sentence is worth more than the twelve rows
> you cut."

## What to say to a student whose scope is too small

> "Five rows, four risks, all of them about the database, build as designed. Before you add
> anything, answer one question: what is the worst thing this feature could do that a normal
> program could not? That is your model risk row, and once you have it, section 6 and section 11
> usually write themselves."

## Scoring the unknowns

**An honest `UNKNOWN` is worth more than a filled-in guess, and it has to be said before they
start** or they will read "I do not know" as a loss.

A full-credit unknown has three parts: what is not known, who could answer it, and what the student
would do if the answer came back badly. **An unknown with no owner is not an unknown, it is a
blank.**

## The rule that does not bend

No real student data. No real names, no real records, no real messages, no photographs of forms.
Every workflow in this task is invented and every detail a student adds is invented too.

**If a student brings in a real example because it would be more realistic, the answer is no, and
the reason is worth giving in full:** this is a course about handling other people's information
carefully, and the first place that gets tested is a classroom exercise where nobody would have
noticed.
