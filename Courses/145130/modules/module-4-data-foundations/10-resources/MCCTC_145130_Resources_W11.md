# Additional Resources · Week 11
## 145130 Applications of AI · Module 4
### Topics: importing, staging, migration and fidelity, calculated fields, protecting data

Links are marked **Confident** or **[VERIFY]**. **A [VERIFY] link has not been confirmed live
from this machine and must be clicked before it is assigned.**

**Nothing this week needs a model or an account.**

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff: CSV and JSON | Mon | Remediation | 35 min |
| 2 | Python documentation: `csv` | Mon | On-level | 15 min |
| 3 | SQLite: Core Functions and Date And Time Functions | Wed | On-level | 25 min |
| 4 | SQLite: SELECT, the grouping and HAVING sections | Wed | On-level | 25 min |
| 5 | RFC 4180, the CSV format | Tue | Extension | 15 min |
| 6 | Python documentation: `json` | Tue | On-level | 15 min |
| 7 | A free video on SQL aggregation | Any | Remediation | under 20 min |
| 8 | SQLite: Window Functions | Wed, Thu | Extension | 30 min |
| 9 | The makerspace handbook's own privacy document | Thu | On-level | 10 min |
| 10 | Reference numbers for self-checking your pipeline | All week | On-level | 5 min |
| 11 | The module's lecture notes, self-check sections | Before Friday | Review | 20 min |
| 12 | Gate 1 bank, reps 11 to 20 | Before Friday | Review | 10 min each |

---

## 1. Primary reading: Automate the Boring Stuff, the CSV and JSON chapter

`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the third
edition's chapter number and path.

**Why this one.** It covers `csv.reader`, `DictReader`, `DictWriter`, `json.load`, and
`json.dumps` in one place, at the level of somebody who has written Python for two years and
not used these modules recently.

**Skip for now:** anything about calling a web API with a key. This course never uses one.

**Time.** 35 minutes. **Level.** Remediation, and worth it for anybody whose Lab M04-03
importers are fighting them.

---

## 2. Python documentation: the `csv` module

`https://docs.python.org/3/library/csv.html` · **Confident.**

**Assign a question:** *Find what the documentation says about opening a file with
`newline=''`. What does it say goes wrong without it?*

Then a second one, because it is the week's real trap: *`csv` says nothing about byte order
marks. Which argument to `open()` deals with that, and why does `strip()` not?*

**Time.** 15 minutes. **Level.** On-level.

---

## 3. SQLite core functions, and date and time functions

`https://www.sqlite.org/lang_corefunc.html` · **Confident.**
`https://www.sqlite.org/lang_datefunc.html` · **Confident.**

**Why these.** Every calculated field in this module comes from these two pages: `printf`,
`round`, `coalesce`, `nullif`, `length`, `replace`, `substr`, `upper`, `trim`, and
`julianday`.

**Assign a question:** *`printf('%.2f', NULL)` and `round(NULL, 2)` behave differently. Find
the two entries and say which one keeps the NULL.*

**That question is on the exit assessment**, in both directions.

**Time.** 25 minutes. **Level.** On-level.

---

## 4. SELECT, specifically grouping and HAVING

`https://www.sqlite.org/lang_select.html` · **Confident.**

**Why this one.** It is long, and the two sections you need are short. Read the `GROUP BY` and
`HAVING` section and the `JOIN` section, and skip the rest until you need it.

**Assign a question:** *Why can `ORDER BY` use a column alias when `WHERE` cannot? The answer
is in the order the clauses are processed.*

**Time.** 25 minutes, reading two sections. **Level.** On-level.

---

## 5. How CSV is actually defined

**RFC 4180, Common Format and MIME Type for CSV Files** · `https://www.rfc-editor.org/rfc/rfc4180`
· **[VERIFY]** before assigning.

**Why this one.** It is short, it is the standards document behind the format, and it states
plainly that many programs do not follow it exactly, which is why real exports are messy.

**Assign a question:** *Does RFC 4180 say anything about how to represent a missing value?
Search it. What does that tell you about Tuesday's lesson?*

**The answer is the lesson.** The format has no concept of null, which is why a convention has
to be invented and written down.

**Time.** 15 minutes. **Level.** Extension.

---

## 6. Python documentation: the `json` module

`https://docs.python.org/3/library/json.html` · **Confident.**

**Assign a question:** *Find the conversion table between JSON and Python types. Which Python
type is missing from it, and what does that mean for a set?*

**Time.** 15 minutes. **Level.** On-level.

---

## 7. A free video

**[VERIFY]. No specific video is linked**, because none has been confirmed from this machine.

**What to look for:** under twenty minutes, on SQL aggregation and `GROUP BY`. **Watch it
first and check one thing:** does it explain the difference between `COUNT(*)` and
`COUNT(column)`? Most do not, and that difference is the hardest item on this module's exit
assessment.

**Level.** Remediation.

---

## 8. SQLite Window Functions

`https://www.sqlite.org/windowfunctions.html` · **Confident.**

**Why this one.** It is the EXTENDED option for Lab M04-03 and Lab M04-04, and it answers a
question `GROUP BY` cannot: how do I get a group's total onto every row of that group at the
same time.

**Assign a question:** *Find `PARTITION BY`. Then work out why a window function cannot go in
a `WHERE` clause, and what you have to wrap the query in instead.*

**Time.** 30 minutes. **Level.** Extension.

---

## 9. The handbook's own privacy document

`05-labs/fixtures/ridge-makerspace/handbook/08-records-and-privacy.md` · **it is on your
machine.**

**Why this one.** Thursday's lesson is built on it, your `data-protection.md` has to agree
with it, and its last section is a model of how to write about a records framework without
pretending to be a lawyer.

**Assign a question:** *Which section of your report does this document say may name a person,
and which says it may not? Then check your own report against it.*

**Time.** 10 minutes. **Level.** On-level. **Everybody, before Thursday's Build 2.**

---

## 10. Reference numbers for self-checking

For checking your own pipeline. **Your numbers can differ if your rules differ. If they do,
your README must say which rule causes the difference.**

- `loans_spring.csv`: 39 data rows, plus one repeated header and one blank line
- `members_legacy.txt`: 14 members, three comment lines
- `catalog.json`: 14 items, 16 distinct tags, 30 item-to-tag links
- Loans that survive the rules in the project spec: 33 loaded, 6 quarantined
- Loans with no return date: 7
- Items never borrowed: 2

**Everything else is your analysis to do, not a key to copy.**

---

## 11. The self-checks you already have

This week's four notes are `ThreeWaysToImport`, `MigrationAndFidelity`,
`CalculatedFieldsAndReports`, and `ProtectingDataYouHold`. Twelve questions with worked
answers.

**The two most worth the time:** MigrationAndFidelity question 1 and
CalculatedFieldsAndReports question 3. Both are on the exit assessment.

**Level.** Review.

---

## 12. Gate 1 reps for review

Reps 11 to 20. Reps 10, 18, and 19 turn up again in the exit assessment.

**Level.** Review.

---

## For the student who is behind

1. Resource 2, the `csv` page, with both questions answered
2. Lab M04-03 SCAFFOLDED, keeping steps 3, 6, and 7
3. Gate 1 reps 10 and 11
4. Before Friday: the CalculatedFieldsAndReports notes, and nothing else new

## For the student who is ahead

- Lab M04-03 EXTENDED and Lab M04-04 EXTENDED, both window functions
- RFC 4180, resource 5
- A third export format in the project, with its fidelity predicted in writing before it is
  run
