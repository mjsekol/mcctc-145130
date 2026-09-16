# Privacy Impact Assessment
## Template · 145130 Applications of Artificial Intelligence · Module 3

Copy this file, rename it `pia-<your-workflow>.md`, and fill in every section.
Keep the section headings exactly as they are written here. `pia_check.py` looks
for them character for character, and it will tell you which one you renamed.

**This assessment is not legal advice and neither is anything in this course.**
It is the document a team writes before building, so that the questions get
asked while changing the answer is still cheap.

**No real student data.** Every record you use is invented. If your workflow
tempts you to use a real name, a real ID, or a real message, that is a sign the
workflow needs an invented stand-in, not that the rule needs an exception.

---

## 1. The feature

One paragraph. What would exist after this is built that does not exist now.
Write it so somebody who has never heard of the project understands it.

## 2. Why it is being proposed

Who asked for this and what problem are they actually trying to solve. Name the
person's role, not a person. Then answer the question that decides most of the
rest of this document: **what would happen if nobody built it.**

## 3. Data inventory

Every field the feature touches. One row per field. If you cannot name why a
field is needed, that is your first finding, not a gap to fill in later.

| Field | Where it comes from | Why the feature needs it | Who can see it | Where it rests | How long it is kept | Framework that governs it |
|---|---|---|---|---|---|---|
| | | | | | | |

**Rules for this table.** Every cell is filled. "How long it is kept" is never
UNKNOWN. If you genuinely cannot determine a framework, write UNKNOWN and put a
matching line in section 11.

## 4. Basis for handling this data

What gives the school the standing to handle each category in the table. Stay at
the purpose level. Name the framework and what it is for, not a section number
you are unsure of. Where a framework does not apply, say that and say why, and
say which one does.

## 5. Confidentiality, integrity, availability

Three short paragraphs, one each.

- **Confidentiality.** Who could see this who should not, and by what route.
- **Integrity.** What happens if a value is wrong, or is changed by somebody who
  should not have changed it. For an AI feature, include what happens when the
  model states something the record does not support.
- **Availability.** What happens to the people this serves when the feature is
  down. Name the manual fallback. A feature with no fallback has made itself
  load bearing.

## 6. What this feature refuses to collect

The strongest section in a good assessment. List every field you considered and
decided against, and why. A design that never holds a field cannot leak it.

## 7. Risks and mitigations

At least four rows. At least one must be a risk created by the model itself
rather than by the data store.

| Risk | Who is harmed | How likely | How bad | Mitigation | What is left after the mitigation |
|---|---|---|---|---|---|
| | | | | | |

## 8. Model and vendor questions

The questions you would have to get answered before this feature touches
anything real, with the answer if you have it and UNKNOWN if you do not.

At minimum:
- Where does the model run, and does any input leave the building
- Is any input retained, and for how long, and by whom
- Is any input used to train or improve anything
- Who can read the logs
- What happens to the data if the school stops using the tool
- What does the license permit this school to do with the output

## 9. Retention and deletion

For each category in section 3: how long, who deletes it, how you would prove it
was deleted, and what happens to derived material such as logs, caches, and
drafts. Derived material is where retention plans usually fail.

## 10. Accessibility

Who cannot use this feature as designed, and what you would change. Consider
screen readers, students who read slowly, students whose first language is not
English, and students without a device at home. Accessibility is not an add-on
here: a feature only some students can use produces unequal results from equal
effort.

## 11. Recommendation and open questions

One of three recommendations, in these words:

- **Build as designed.**
- **Build with the changes listed below.**
- **Do not build this until the open questions below are answered.**

Then a numbered list of every UNKNOWN in this document, who could answer it, and
what you would do if the answer came back badly.

---

## Sign-off

| Role | Name | What they reviewed |
|---|---|---|
| Author | | Whole document |
| Peer reviewer | | Sections 3, 7, and 11 |
| Stakeholder | | Sections 1, 2, and 11 |

**Review cadence.** Reassess at the end of each grading period, and immediately
if the model, the vendor, or the data inventory changes.
