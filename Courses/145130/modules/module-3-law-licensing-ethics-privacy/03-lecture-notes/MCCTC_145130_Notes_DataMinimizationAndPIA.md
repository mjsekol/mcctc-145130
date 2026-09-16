# Lecture Notes: Data Minimization, and the Assessment You Write Before You Build
## 145130 Applications of AI · Module 3 · Week 9, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W09_DataMinimizationAndPIA.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W09_DataMinimizationAndPIA.pptx)

If you missed class, you can learn this concept from this file alone. Run every program.

**Competencies:** 2.1.12 (privacy security compliance on systems), 3.2.1 (identify and
implement data and application security: **taught here, not on the WebXam blueprint**),
2.1.1 (confidentiality, integrity, availability).

---

## Read this first

This file is not legal advice. A privacy impact assessment is not a legal filing and writing
one does not make anything compliant with anything. **It is an engineering document that
forces the questions to get asked while changing the answer is still cheap.**

The roster in this week's lab is invented. **No real student data appears anywhere in this
course, in any file, ever.**

---

## Why this exists

Every privacy control you can build falls into one of two groups.

**Controls that protect data you are holding.** Encryption, access control, logging, audits,
backups, retention schedules. All real, all necessary, all of them can fail, and every one of
them is a thing somebody has to keep doing correctly forever.

**Controls that mean you are not holding it.** There is one of these. It is called
minimization, and it is the only control on this list that cannot be misconfigured, forgotten,
bypassed, or left running by somebody who joins four years from now.

**A field you never collected cannot leak, cannot be subpoenaed, cannot be sold in a breach,
cannot end up in a prompt, and does not need a retention rule.** That asymmetry is why this
lesson comes before the assessment rather than after it.

---

## The three ideas, and where they come from

The GDPR's Article 5 principles are the clearest published statement of these, which is why
this course uses them as a design checklist even though the GDPR does not govern your school.
Read the regulation's own text. **[VERIFY]**

**Purpose limitation.** Data is collected for a specified purpose and not then used for some
other unrelated one. The practical version: **write the purpose down before you collect, and
compare it with the field list.** If a field is not needed for the purpose you wrote, it is not
a field you need.

**Data minimisation.** What you collect is adequate, relevant, and limited to the purpose. The
practical version: **every field on a form is a decision somebody made.** Most forms have
fields on them because somebody thought they might be interesting one day.

**Storage limitation.** Data is kept no longer than is necessary for the purpose. The practical
version: **deletion is a feature and it has to be built.** Nothing deletes itself, and the
reason old data accumulates is not malice, it is that nobody was ever assigned the job.

---

## Minimization in code, not in a policy document

A policy that says "we minimize data" is a sentence. Here is the same idea as a program,
which is what this week's lab makes you write.

```python
PURPOSES = {
    "attendance_letter": [
        "student_id", "first_name", "last_name",
        "guardian_name", "guardian_email", "absences_this_term",
    ],
    "bus_route_count": ["bus_route"],
    "ai_hint_request": [],
}


def minimize(record, purpose):
    if purpose not in PURPOSES:
        raise ValueError(f"Unknown purpose {purpose!r}.")
    allowed = PURPOSES[purpose]
    return {field: record[field] for field in allowed if field in record}
```

Three design decisions in eleven lines, and each one is worth saying out loud.

**The list is per purpose, not per program.** The same record is handled differently depending
on what is being done with it, which is purpose limitation expressed as a data structure.

**An unknown purpose raises.** It would have been shorter to return the whole record when the
purpose is unrecognized. That version fails **open**: every future typo, renamed feature, and
hurried new caller silently receives everything. Failing closed makes the mistake loud on the
first run rather than quiet forever.

**`ai_hint_request` is an empty list.** That is the course rule as code. The model gets a
pattern, never a person. An empty list is not a placeholder, it is the answer, and a reviewer
should be able to see the rule being enforced rather than promised.

Output of the solved version:

```
Fields the roster carries: 16
 attendance_letter: 6 field(s) -> ['absences_this_term', 'first_name', 'guardian_email', 'guardian_name', 'last_name', 'student_id']
   bus_route_count: 1 field(s) -> ['bus_route']
   ai_hint_request: 0 field(s) -> []
   log: purpose=attendance_letter ref=aef90667 fields_sent=6

Riders per route, from records holding one field each: {'12': 3, '7': 2}
```

**Sixteen fields in. One field out, for the route count, and the count is still correct.** That
last line is the argument for minimization in one line of output: the job got done with one
field, and every other field would have been a field at risk for no benefit.

---

## Worked example: removing names does not make people anonymous

This is the misconception that costs organizations the most, and it takes five records to
disprove.

```python
# reidentify.py: the names are gone. Is anybody actually anonymous?
from roster import ROSTER

COMBINATIONS = [
    ("grade",),
    ("grade", "bus_route"),
    ("grade", "bus_route", "meal_status"),
    ("grade", "bus_route", "meal_status", "services_plan"),
]

for fields in COMBINATIONS:
    groups = {}
    for record in ROSTER:
        key = tuple(record[f] for f in fields)
        groups[key] = groups.get(key, 0) + 1
    unique = sum(1 for count in groups.values() if count == 1)
    print(f"{' + '.join(fields):<48} {unique} of {len(ROSTER)} records are alone "
          f"in their group")

print()
print("No name, no ID, no address, no birthday in any of those groupings.")
print("Add enough ordinary fields and every row identifies one person.")
```

Output:

```
grade                                            0 of 5 records are alone in their group
grade + bus_route                                0 of 5 records are alone in their group
grade + bus_route + meal_status                  5 of 5 records are alone in their group
grade + bus_route + meal_status + services_plan  5 of 5 records are alone in their group

No name, no ID, no address, no birthday in any of those groupings.
Add enough ordinary fields and every row identifies one person.
```

**Watch the third line.** Grade and bus route together identify nobody. Add one more ordinary
field and **every single record is unique.**

There is no name in any of those groupings. No student ID, no address, no date of birth.
Three boring fields, none of which feels sensitive on its own, and the data set has stopped
being anonymous.

Fields like grade, route, and meal status are **quasi-identifiers**: values that identify
nobody alone and identify somebody in combination. Anybody who knows a few facts about a
student, which at a school is everybody, can now find their row. And the row they find has
`services_plan` and `counselor_note` in it.

**This is why "we removed the names" is not an answer, and it is why the minimization list
comes first.** You cannot anonymize your way out of holding data you did not need.

---

## The assessment: what each section is for

Your privacy impact assessment has eleven sections. They are not equally important and you
should know which ones carry the document.

| Section | What it is for | How it is usually failed |
|---|---|---|
| 1. The feature | Establish what exists afterwards that does not now | Describing the technology instead of the change |
| 2. Why it is proposed | Name the problem and the cost of doing nothing | Skipping "what if nobody built it", which sets the acceptable risk |
| 3. Data inventory | Force a decision per field | Filling it in from the database schema instead of from the purpose |
| 4. Basis for handling | Name the framework and what it is for | Stating a section number the writer is not sure of |
| 5. CIA | State the trade you chose | Three paragraphs claiming all three are fine |
| **6. What it refuses to collect** | **The strongest section in a good assessment** | Left blank, because refusing is invisible work |
| 7. Risks and mitigations | Name harms and what is left after the fix | Mitigations that are "train staff" and nothing else |
| 8. Model and vendor questions | Find out what happens to the input | Believing a marketing page instead of reading a contract or the code |
| 9. Retention and deletion | Decide who deletes what, and how you would prove it | Forgetting derived material |
| 10. Accessibility | Find who cannot use this | Treating it as a nice-to-have |
| **11. Recommendation and open questions** | **Make a call, and list every UNKNOWN** | Recommending "build as designed" with unresolved unknowns above it |

### Section 6 is the one that separates a real assessment from a form

**Anybody can list the fields they collected.** Listing the fields you considered and rejected,
with a reason each, is the part that proves a design decision happened.

It is also the section that reads as empty work, because a refusal leaves nothing behind.
Nobody sees the counselor note that was not sent to the model. **Write it down, or in six
months somebody will add the field back and nobody will remember why it was out.**

### Section 9 is where retention plans actually fail

Ask a team where the data lives and they say "the database". Ask again and they find:

- Draft files on a workstation
- Application logs
- The model server's own request log, which nobody configured and which is on by default in
  many setups
- Cached responses
- Exports somebody made once for a meeting
- Backups, which by design outlive the deletion you performed

**Derived material is the answer to "how did this data still exist two years later".** Every
item on that list is real, and none of them are in the database that the retention policy was
written about.

### Section 11 has to make a call

Three options, and the wording matters: **build as designed**, **build with the changes listed
below**, or **do not build this until the open questions are answered.**

An assessment with unresolved UNKNOWNs in section 8 and "build as designed" in section 11 is
internally inconsistent, and `pia_check.py` will tell you so. **The check is mechanical and
the inconsistency is not.** A team that wants to build something will write the unknowns
honestly in the middle and then lose their nerve at the end.

---

## The wrong version, and what it does instead of an error

A team is asked to build the attendance drafter. Here is their design note.

> "We will pull the full student record from the SIS, since we already have access, and pass it
> to the model with the letter template. That way if we want to add personalization later we do
> not have to change the data layer. We will strip names before logging so nothing identifying
> ends up in the log."

**Nothing errors. This design works. It would pass a demo and it is faster to write than the
right one.** Four problems, in increasing order of how long they take to notice.

1. **The full record goes into the prompt.** The counselor note, the services plan, and the
   meal status are now in the model's input. Whether that matters depends entirely on where
   the model runs, and the design note does not say, which means nobody decided.
2. **"In case we want to add personalization later" is the purpose limitation failure**, word
   for word. The data is being collected for a purpose that does not exist yet.
3. **"Strip names before logging" is the anonymization failure** that worked example 2
   disproved a page ago. Grade, route, and meal status are still in the log and three of them are enough.
4. **The data layer decision is the one that will outlive everybody.** The next team inherits a
   function that returns everything, and every future feature will be built on it, because that
   is what is there. **A permissive default at the data layer is the most durable design
   mistake in this whole file.**

## Why the wrong version is tempting

**It is genuinely less work today.** One query that returns everything is simpler than six
queries that return what each thing needs. The cost is paid later and by somebody else, which
is the standard shape of technical debt and the standard shape of a privacy incident.

**"We already have access" feels like an argument.** It is not. Having access is a fact about
permissions. Whether this feature should use it is a design question, and conflating the two is
how features end up holding data nobody ever decided they should hold.

**Future flexibility sounds responsible.** It is the phrase that gets the field added. Ask the
follow-up: what specifically, for whom, and when. If the answer is "we are not sure yet", the
field goes out and comes back when somebody is sure, which costs one afternoon at that point
and costs nothing now.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Data minimisation** | Collecting only what is adequate, relevant, and limited to the purpose. |
| **Purpose limitation** | Data collected for a stated purpose is not reused for an unrelated one. |
| **Storage limitation** | Data is kept no longer than the purpose needs. |
| **Fail closed** | On an unrecognized input, refuse. The opposite of returning everything. |
| **Quasi-identifier** | A field that identifies nobody alone and somebody in combination. |
| **Re-identification** | Recovering an identity from data whose direct identifiers were removed. |
| **Derived material** | Logs, caches, drafts, exports, and backups. Where retention plans fail. |
| **Privacy impact assessment** | The document written before building, that forces the questions while answers are cheap. |
| **Residual risk** | What is left after the mitigation. A risk table with none is not finished. |
| **Prompt surface** | Everything placed in a prompt, and therefore disclosed to whoever runs the model. |

---

## Self-check

**Question 1.** Your team wants to add a `date_of_birth` field to the attendance letter
feature, because "we might want to say happy birthday one day." Write the two sentences you say
in the design review. One states the principle, one gives the team a path to yes.

**Question 2.** Run `reidentify.py`. It reports 5 of 5 unique on three fields. Does that mean a
real district roster of 800 students would also be fully unique on those three fields? Answer,
and say what you would have to do to find out.

**Question 3.** List four places the attendance letter data could exist that are not the student
information system, and for each one name who would have to delete it. If you cannot name a
person for one of them, say so, because that is the finding.

---

### Answers

**1.** For example:

> "Purpose limitation says we collect for the purpose we wrote down, and the purpose we wrote
> down is an absence letter, which does not use a birthday. So it is out of the field list for
> this feature. If somebody wants a birthday feature, that is a separate purpose with its own
> line in the inventory, and I will help write it the day somebody actually asks for it."

The second sentence is the one that matters. **A refusal with no path to yes gets overruled
eventually**, because the person asking has a real idea and no way to pursue it. A refusal with
a path is a process, and a process survives the meeting.

**2.** **No, it does not follow, and assuming it does would be exactly the error this course is
about.** Five records is a tiny sample and uniqueness depends on how the values are distributed,
not on the number of fields alone. With 800 students there would be far more students per grade
and per route, so many groups would have several people in them.

**What you would have to do to find out:** run the same grouping over the real population size
and look at the distribution of group sizes, particularly the smallest groups. **And notice what
that measurement would require:** access to the real roster, which is the data you were trying
to protect. In practice you do it on synthetic data shaped like the real thing, or you ask
somebody who already has the access to run it and report only the group size counts.

**The finding that does survive from five records:** three ordinary non-sensitive fields were
enough to split this group completely, so "we removed the names" is not evidence of anything.
That claim needs measuring, every time, and the burden is on whoever says the data is anonymous.

**3.** Four, with who deletes each:

1. **Draft letters on the office workstation.** The secretary, from a checklist item.
2. **The application log.** The technology coordinator, on an annual schedule.
3. **The model server's own request log.** This is the one where most teams cannot name a
   person, because nobody configured it and nobody knows it exists. **That is the finding**:
   it goes in section 8 as a question and in section 11 as a change required before the first
   real run.
4. **Sent email in the office mailbox.** Whoever runs the district's records retention for
   correspondence, and this feature does not get to change that schedule.

A fifth worth naming: **backups.** Backups exist to outlive deletion, which means a deletion
plan that ignores them is describing a thing that did not happen. Name it and say what the
district's backup cycle does, or record that you do not know.
