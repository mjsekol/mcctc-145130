# Lab M04-03: Three Files, One Staging Area
## 145130 Applications of AI · Module 4 · Week 11, Monday

**Gate:** 3, open tooling. **Duration:** Build 1, 40 minutes of build time after the Gate 1
rep, continuing into Build 2 if you need it.
**Competencies:** 8.3.2 (import large data sets using a bulk command, an SQL script, or a
CSV file), 8.3.1 (collect and maintain data), 2.8.4 (schema and records), 1.4.6 (use an
electronic database to create technical information).

**This lab is the Measure step of your performance task.** What you find today goes straight
into README section 4 of your project. Do it properly and Wednesday's cleaning code gets
written once.

---

## The scenario

The makerspace advisor sent you three files and no explanation. A pipe delimited text export
from a kiosk that no longer exists, a JSON catalog, and a spreadsheet the front desk types
into. You are going to load all three into one database **without fixing anything**, and then
ask the database what is wrong with them.

## What you will build

A staging database. Three tables, one per source file, every column TEXT, every row carrying
the line number it came from. Then a file of questions you run against it.

**Nothing is cleaned in this lab. Nothing is converted. Nothing is dropped.** A staging table
is a photograph of the file. The moment you convert a value you have thrown something away,
and you can no longer ask what the file actually said.

---

## Files you need

`05-labs/lab-m04-03-files/`. Copy it. It reads the shared fixture at
`05-labs/fixtures/ridge-makerspace/`, so leave the raw files where they are and pass
`--data` if your copy ends up somewhere else.

- `stage.py`, with one of the three importers finished as the worked example
- `profile.sql`, with five questions written and nine to write
- `profile.py`, finished, which runs every question in `profile.sql` and prints the answers

Read the fixture's own `README.md` before you start. It lists every kind of mess that is in
the files on purpose, so that when you find one you know it is the assignment and not a
broken fixture.

---

## Starter code

```
python stage.py
```

```
staged, nothing converted, nothing dropped
  stg_loans     40 rows   (csv module, executemany)
  stg_members    0 rows   (generated SQL script, executescript)
  stg_items      0 rows   (json module, executemany)
```

One of three. Then:

```
python profile.py
```

Five questions answered, nine saying `not written yet`.

---

## Steps

### Step 1. Three ways to import, and when each one is used

Before you write anything, read the docstring on each of the three functions in `stage.py`
and write one sentence per technique in your README about when you would use it.

| Technique | What it is | When somebody uses it |
|---|---|---|
| `executemany` with placeholders | one call, many rows, values sent separately from the SQL | the default, and the only one that is safe from injection by construction |
| A generated SQL script | a text file of `INSERT` statements, run with `executescript` | when the database is somewhere you can only send a file |
| Reading a structured format | `json`, `csv`, or your own parser, then one of the above | always, because the file is never already SQL |

### Step 2. Look at the number the starter printed

`stg_loans` has **40** rows and the fixture README says the file has **39 data rows**.
**Find the extra one before you go further.** Question 2 in `profile.py` will tell you, and
you should predict it first.

Write down why that row is in the staging table and not thrown away at the door.

### Step 3. Notice what the finished importer does about the byte order mark

Find `encoding="utf-8-sig"` in `stage_loans_with_executemany`. Change it to `"utf-8"`, run
`stage.py`, and write down what changes. Then change it back.

**You will meet this again in your project**, and it costs twenty minutes the first time
because the line that fails looks correct.

### Step 4. Write the SQL script importer

Fill in `stage_members_with_sql_script`. Read the pipe delimited file, skip the comment
lines, build one `INSERT` statement per member as text, write the whole thing to
`output/load_members.sql`, and run it with `connection.executescript(script)`.

**Escape every value.** A single quote inside a value ends the SQL string early. In this
fixture no name has an apostrophe, which means your bug will not show up today and will show
up the first time somebody named O'Brien joins.

Expected: **14 rows**. Open `output/load_members.sql` and read the first three lines.

### Step 5. Write the JSON importer

Fill in `stage_items_from_json`. Each item has a `tags` **array** and a `purchase`
**object**. Flatten each item into one staging row.

**Keep the tags joined with a semicolon for now.** Splitting them into their own table is a
schema decision and this is staging, not deciding. You make that decision in your project.

Expected: **14 rows**.

### Step 6. Ask what shape the dates are in

Write question 6 in `profile.sql`: what is actually in the `returned` column. Group the rows
into four buckets: empty, `yyyy-mm-dd`, `mm/dd/yyyy`, and not a date at all. Use `GLOB` for
the patterns.

Then question 7, the same idea for `checked_out`.

**Predict the numbers before you run it**, and write your prediction down.

### Step 7. The join that fails, and the join that works

This is the most important pair of questions in the lab.

Write question 8: count the loans whose `member_id` does not appear in `stg_members`,
**joining the raw text as it is**.

Write question 9: the same count, but normalize both sides first. The loans file writes
`RC-0142` and the members file writes `RC0142`, so both sides need the same expression
applied before they are compared.

**Run them and compare the two numbers.** Then write one sentence in your README about what
question 8 would have told the advisor.

### Step 8. Finish the rest

Questions 10 through 14:

- orphan items, normalizing both sides
- rows whose dates contradict each other, with the source line number
- program names in the member file, with `length(program)` next to each one
- how many tags each item carries, counted from the text
- items that nothing borrowed

**Question 12 has a finding in it that you will miss unless you look at the character
count.** That is why the length column is there.

### Step 9. Write the mess down

Copy your findings into README section 4 of your project, **The mess**, as a table: what,
an example, and where. That section is a DMAIC Measure deliverable and it is due at the end
of today's Build 2.

---

## Acceptance criteria

- [ ] `python stage.py` prints 40, 14, and 14
- [ ] `output/load_members.sql` exists and holds 14 `INSERT` statements
- [ ] The step 3 experiment recorded, with what changed
- [ ] All 14 questions in `profile.sql` return real answers
- [ ] The step 6 predictions written down before the run, with a note on any you got wrong
- [ ] Questions 8 and 9 both written, both numbers recorded, and the sentence about what
      question 8 would have told the advisor
- [ ] Question 12's finding identified, with the character counts
- [ ] The mess table copied into your project README section 4

---

## If it breaks

**`A source file does not look the way this program expects: unexpected columns ... ['\ufeffloan_id', ...]`**
The byte order mark. Your first column name has three invisible characters in front of it.
Use `encoding="utf-8-sig"`. This is step 3 happening for real. If your own code uses
`csv.DictReader` instead, the same cause shows up as `KeyError: 'loan_id'` on a line that
looks correct, which is harder to read and is why this importer checks the header.

**`sqlite3.OperationalError: near "s": syntax error`**
Your generated SQL has an unescaped apostrophe, or a value that was not quoted at all.
Print the statement before you run it.

**`sqlite3.Warning: You can only execute one statement at a time`**
You passed a script with several statements to `execute`. `executescript` is the one that
takes many.

**`TypeError: sequence item 0: expected str instance, int found`**
You are joining a list that has numbers in it. `loan_days` and `year` come out of JSON as
numbers, and a staging column is TEXT, so convert them with `str()` at the edge.

**Question 8 returns 39, or 0.**
39 means you did not exclude the repeated header row. 0 means you joined on something that
is always equal, such as a column name you got wrong in a way SQLite read as a string
literal.

**`profile.py` says a question is `not written yet` after you wrote it.**
The title line has to start with the comment marker, the word `QUERY`, and a colon, with
nothing before it. `profile.py` splits the file on exactly that.

---

## Stretch goal

Add a question that finds every loan whose `notes` column contains a comma, and then explain
in one sentence why `split(",")` would have given you the wrong number of columns for those
rows and the `csv` module did not.

---

## Submission checklist

- [ ] `stage.py` and `profile.sql` committed
- [ ] `output/` in `.gitignore`. The staging database and the generated script are both built
      from the raw files every run
- [ ] Findings written into your project README section 4
- [ ] AI usage log updated
- [ ] `git status` clean, pushed

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty five minutes in and step 4 is not producing 14 rows | SCAFFOLDED |
| Both importers working, writing questions | STANDARD |
| All 14 questions answered before 40 minutes, or asks why staging exists at all | EXTENDED |
| "Why not fix it as we read it," or asks where staging is used for real | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Step 4** is provided complete as a third worked example. You read it and answer one
  question: what does the escaping line do, and what breaks without it.
- **Step 8** drops to two questions of your choice from the five listed.
- **Steps 3, 6, and 7 stay.** They are the lab.
- **Checkpoints:** show your instructor the counts after step 5 and questions 8 and 9 after
  step 7.

**Acceptance criteria:** three importers working with the right counts, questions 6, 7, 8,
and 9 written and answered, the step 3 experiment recorded, and the mess table started.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Make the loans importer stream instead of building a list of forty
rows in memory first. Pass a generator to `executemany` and confirm the counts are
unchanged. Then say in your README what this buys you, and be honest: at forty rows it buys
nothing, and the number where it starts to matter is the answer.

**Added requirement 2.** Write a question that uses a window function to number each
member's loans in the order they were taken, and return only each member's first loan.
SQLite supports window functions.

**Hint, not the answer.** Read the SQLite documentation page "Window Functions",
`https://www.sqlite.org/windowfunctions.html`, and find `ROW_NUMBER()` and the `PARTITION BY`
clause. Then work out why you cannot put a window function in a `WHERE` clause, and what you
have to wrap it in instead.

**Acceptance criteria:** all STANDARD criteria, the generator version producing the same
counts, the window query returning one row per member, and both written answers.

---

## APPLIED

**For the student who asks where staging is used for real.** Every data warehouse works this
way: land the source exactly as it arrived, then transform. The reason is that the transform
is going to be wrong at least once, and when it is, you want the original still sitting
there rather than a source system you have to ask for again.

**Changed scenario.** Stage a dataset you already have, with no personal information in it:
a game's export, a robotics telemetry log, a club's inventory sheet with invented names, a
public transit schedule file you already downloaded for another class. **It must come in at
least two different formats, or you must convert one of them yourself so that it does.**

Steps 1 through 5 are the same techniques applied to your files. Step 6 becomes: pick the
column in your data that is most likely to be typed inconsistently, and write the two
questions that show every shape it was typed in and what it looks like after one normalizing
expression. Steps 7 and 8 become five questions of your own, at least one of which compares
a naive join with a normalized one.

**The extra requirement that makes it the same lab.** Your README states one finding that
you would not have found by opening the file and reading it, and says which question found
it.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether the questions
you wrote could actually change what your cleaning code does.
