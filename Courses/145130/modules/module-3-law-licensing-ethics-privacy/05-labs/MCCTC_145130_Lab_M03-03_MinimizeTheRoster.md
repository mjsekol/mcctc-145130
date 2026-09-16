# Lab M03-03: Minimize the Roster
## 145130 Applications of AI · Module 3 · Week 9, Monday and Wednesday

**Gate:** 3 (open tooling, decision log required). **Duration:** Week 9 Monday Build 1, 40
minutes, and Week 9 Wednesday Build 2, 55 minutes.

**Files:** `lab-m03-03-files/`
**Competencies:** 2.1.1 (explain the need for confidentiality, integrity, and availability),
2.1.12 (privacy security compliance on systems), 3.2.1 (identify and implement data and
application security: **taught in this module, not on the WebXam blueprint**).

**Build 1 is 40 minutes of build work**, because the Gate 1 rep runs in its first 10
minutes.

---

## Before you start

**Every record in `roster.py` is invented.** Riverbend Middle does not exist, and the students,
guardians, addresses, and identifiers in that file were written for this lab. **No real student
data goes into any file in this course, ever, and that includes yours.**

This lab is not legal advice. It is a privacy control written in code.

The fields in the fixture are the fields a real student information system actually carries,
which is the point. Look at how much is there. Then look at how little any one job needs.

---

## The scenario

The front office at Riverbend Middle wants three things built on top of the roster: a weekly
absence letter drafted for a secretary to review, a count of riders per bus route, and a hint
feature that asks a locally hosted model to rephrase a sentence. One programmer has written a
function that returns the whole record for all three, because it was faster.

## What you will build

A `minimize` function that hands each purpose only the fields that purpose needs, and a log line
that records what happened without recording who it happened to.

---

## What is in `lab-m03-03-files/`

| File | What it is |
|---|---|
| `roster.py` | The invented roster. Five records, sixteen fields each. Do not edit it. |
| `minimize.py` | The starter. It runs and does nothing useful. Four checklist items. |
| `check_minimize.py` | Ten checks. Run it whenever you like. |

---

## Part 1 · Week 9 Monday, Build 1, 40 minutes: the field lists

### Step 1. Run the starter and read the log line

```
cd lab-m03-03-files
python minimize.py
```

**Observable result.** Every purpose reports 16 fields. The last line of each block is a log
entry containing a home address, a meal status, a services plan, and a counselor note about a
family. **Read that line properly before you go on.** It is the reason this lab exists.

### Step 2. Run the checks and see where you are starting from

```
python check_minimize.py
```

**Observable result.** `4 of 10 checks passed.` Three of the failures are field lists, one is
the unknown-purpose behaviour, and two are about the log line.

### Step 3. Fill in `attendance_letter`

The purpose is a letter to a guardian about a student's absences, reviewed and sent by a
secretary.

For each of the sixteen fields, ask one question: **does the letter change if this field is
missing?** If it does not, the field is out.

**Observable result.** A field list of five to seven entries. The check tells you whether you
kept what is needed and dropped what is not. **Two fields are judgement calls and the check
allows either answer.** Write your reasoning for both in your decision log, because the
reasoning is what is graded.

### Step 4. Fill in `bus_route_count`

The purpose is a count of how many students ride each route.

**Observable result.** A field list with **one** entry. If your list is longer, ask what the
count uses the extra field for. This is the purpose that looks too small to be right, and it is
right.

### Step 5. Fill in `ai_hint_request`

The purpose is asking a locally hosted model to rephrase a sentence in plainer words.

**Observable result.** An empty list. **That is the answer, not a placeholder.** The model gets
a pattern, never a person. This course's rule is absolute, and this is the line of code where
the rule becomes something a reviewer can check rather than something a document promises.

### Step 6. Make an unknown purpose refuse

Checklist item 2. `minimize(record, "curiosity")` must raise `ValueError`.

**Observable result.** The check reports `an unknown purpose raises ValueError`. In your decision
log, write two sentences on why returning the whole record would have been worse, and use the
words **fail closed**.

---

## Part 2 · Week 9 Wednesday, Build 2, 55 minutes: the log line

### Step 7. Write `reference`

Checklist item 4. It takes a student ID and returns a short opaque value, good for this run only.

The salt is already in the file: `RUN_SALT`, regenerated every time the program starts. Your
reference has to depend on it.

**Observable result.** Checks 9 and 10 pass. The same student gets the same reference twice in
one run, and a different one in the next run.

### Step 8. Rewrite `describe_for_log`

Checklist item 3. The line says what happened and how much moved. It does not say who.

**Observable result.** Checks 6 through 10 pass. Your log line contains no value from the
record, still names the purpose, and differs between two students.

### Step 9. Run everything

```
python minimize.py
python check_minimize.py
```

**Observable result.** `10 of 10 checks passed.` Paste both outputs into your `README.md`.

### Step 10. Answer the re-identification question in writing

Write `notes.md`. Somebody proposes exporting the roster with the names and IDs removed, keeping
grade, bus route, and meal status.

- Run the grouping yourself over the five records and report what you find
- Say whether the same result would hold for a roster of 800, and what you would have to do to
  find out
- Say what the finding **does** support even from five records

**Observable result.** Three short paragraphs. The second one is the hard one and the honest
answer is that five records do not tell you.

### Step 11. Write the field justification table

For every one of the sixteen fields, one row: is it in any list, which one, and one sentence of
why or why not.

**Observable result.** A sixteen-row table in `notes.md`. **The rows that say no are worth more
than the rows that say yes**, because a refusal you did not write down gets reversed by the next
person in six months.

---

## Acceptance criteria

- [ ] `python check_minimize.py` prints `10 of 10 checks passed.`
- [ ] `attendance_letter` holds between five and seven fields and none of the forbidden ones
- [ ] `bus_route_count` holds exactly one field
- [ ] `ai_hint_request` is empty
- [ ] An unknown purpose raises `ValueError` with a message that names the purpose
- [ ] The log line carries no value from the record and still names the purpose
- [ ] Changing `RUN_SALT` changes the reference
- [ ] `notes.md` has the three re-identification paragraphs and the sixteen-row table
- [ ] Decision log entries for the two judgement-call fields and for failing closed
- [ ] Committed and pushed

---

## If it breaks

**`ModuleNotFoundError: No module named 'roster'`**
You are running from the wrong directory. `roster.py`, `minimize.py`, and `check_minimize.py`
have to be in the folder you run from.

**`FAIL  attendance_letter: keeps what it needs, drops what it does not` with `missing []` and a
long "should not be there" list**
Your field list is still `ALL_FIELDS`, or you added fields back. Read the list in the failure
message: every one of those is a field the letter does not use.

**`FAIL  an unknown purpose raises ValueError` with `it raised KeyError instead`**
You indexed `PURPOSES[purpose]` before checking membership. Check first, then index. The order
matters because the message a caller sees is part of the interface.

**`FAIL  the log line carries no personal value` and the listed fields include `student_id`**
You put the raw ID in the line instead of the reference. The ID is a direct identifier and the
whole point of `reference` is that the log does not carry one.

**`FAIL  the same student produces the same line twice in one run`**
Your reference is random rather than derived. A random value changes on every call, so the same
student gets two different references inside one run and nobody can trace a single failed
record through the log. Derive it from the salt and the ID with a hash, so it is stable within
a run and different across runs.

---

## Stretch goal

Add a fourth purpose, `late_bus_alert`: a text message to a guardian saying route 12 is running
thirty minutes late. Write the field list, then write down the thing that surprised you. Most
students expect it to need the student, and it needs the route and a contact. Then say what that
tells you about the other three lists.

---

## Submission checklist

- [ ] `minimize.py` with all four checklist items done
- [ ] `check_minimize.py` output pasted into `README.md`, showing 10 of 10
- [ ] `notes.md` with the re-identification answer and the sixteen-row table
- [ ] Decision log entries
- [ ] AI usage log entry if you used a model
- [ ] Pushed

---

# Extended options

All four assess the same competency and grade on the same 100-point scale.

## How to choose, three observable signals

1. **The step 3 first draft.** A student whose `attendance_letter` list has twelve fields is
   asking "could this be useful" instead of "does the letter change without it". SCAFFOLDED, with
   the question written on their screen.
2. **The step 4 reaction.** A student who writes one field and then says "that cannot be right"
   and checks it is ready for EXTENDED. A student who writes four fields and moves on has not
   asked the question yet.
3. **Step 6.** A student who implements the refusal and then explains fail-closed without being
   prompted goes straight to EXTENDED in Build 2.

## SCAFFOLDED

Same target, smaller scope, more structure.

- `attendance_letter` and `bus_route_count` only. `ai_hint_request` is filled in for you, with a
  comment explaining why it is empty.
- The sixteen fields come as a printed two-column worksheet: field name, and the question "does
  the letter change without it, yes or no". Tick the boxes, then type the list.
- `reference` is written for you. You write `describe_for_log` using it.
- `notes.md` is the sixteen-row table only. The re-identification paragraphs are replaced by one
  sentence: what did removing the names not accomplish.
- Checkpoint after step 4 and after step 8.

**Same grading scale.** The competency is deciding, per purpose, which fields are needed, and two
purposes assesses that.

## STANDARD

The lab as written above.

## EXTENDED

Everything in STANDARD, plus **retention**.

Add a `retention.py` that takes the three purposes and, for each one, records: how long the data
is kept, who deletes it, and what derived material exists that the retention rule was not written
about. Then write a function that, given a list of file paths a run produced, reports which of
them have an owner and which do not.

Run it against your own lab folder. **You will find at least one file with no owner**, and that
is the finding.

**The hint, and it points at documentation rather than an answer:** read the GDPR's Article 5
principles, at the regulation's own published text, and find the one called storage limitation.
Write your retention rules in the shape that principle describes. **[VERIFY]** the address before
you assign it.

## APPLIED

Same skill, completely different domain: **the club sign-up form.**

Take any form your school, a club, or a team actually uses. A sign-up sheet, a field trip form, a
tryout registration. Do not photograph it and do not bring a filled-in copy: **write down the
field names only.**

Then:

1. List every field the form collects
2. Name the purpose the form exists for, in one sentence
3. For each field, say whether the purpose changes if it is missing
4. Write the minimized version of the form
5. Write one paragraph on which removed field you expect the most pushback about, and what you
   would say

Deliverable: the four lists and the paragraph.

**Give this to the student who asks when they would ever use this.** The answer arrives at step 3,
usually at the date-of-birth field, which almost every form collects and almost none of them use.
