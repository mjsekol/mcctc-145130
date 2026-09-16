# Project: The Makerspace Data Pipeline
## 145130 Applications of Artificial Intelligence · Module 4 · Weeks 10-12

**Mode:** solo. **Gate:** 3, full tooling. Decision log, AI usage log, and a written data
protection analysis are all required.
**Due:** Week 12, Friday. The 15-minute slot that normally holds instruction is the final
commit window, because Friday introduces no new content. The last commit pushed in that
window is your submission. Build 1 is the module exit assessment and Build 2 is demos.

**Competencies:** 2.8.1, 2.8.2, 2.8.3, 2.8.4, 2.8.8, 2.8.9 (database types, purpose,
structures, elements, integrity, front end and back end) · 8.3.1, 8.3.2 (collect and
maintain data, import large data sets) · 8.5.4 (reports, forms, and query results with
calculated fields and functions) · 2.6.4 (preserve, convert, or migrate files to a new
format) · 8.2.3 (data integrity, security, and regulatory restrictions) · 1.4.3 (verify
compliance with security rules) · 1.4.6 (use an electronic database to create business and
technical information).

**You have done a version of this before.** Unit 5 of 145060 was one messy CSV, one
cleaning pass, one JSON file, and one report. **This one is harder in five specific ways,
and each of them is a place people lose marks:** three source formats instead of one, a
schema you design rather than one you are handed, referential integrity that the database
enforces rather than your code, a migration that loses data if you are careless and says
nothing, and a document set that has to become queryable.

---

## The brief

> I run the makerspace at Ridge Creek. Fourteen members this spring, fourteen pieces of
> equipment, and three files that do not agree with each other.
>
> The kiosk we used to sign people in died in February and all I have from it is one text
> export. The catalog comes out of the new kiosk as a JSON file. The loan log is a
> spreadsheet that four different volunteers type into at the front desk, and I know some of
> it is wrong because I have watched people type it.
>
> Two things get asked of me every month. The advisory board wants to know whether the
> equipment we bought is being used, and by which programs. And I need to know what has not
> come back, so I can go and ask for it.
>
> I also have a handbook nobody reads. Eight documents. Every single week somebody asks me
> a question that is answered in it. I would like to be able to point at the paragraph.
>
> What I do not want is a number I cannot explain to the board. If a row is bad, tell me
> which row and what is wrong with it, and I will go and ask the person who typed it.

**That is the brief.** It does not say what "being used" means as a number. It does not say
what to do with a loan that points at a member who is not in the export. It does not say
what "the equipment we bought is being used" means for a piece of equipment nobody has
touched. Deciding those, and defending the decisions, is most of the grade.

*(The Ridge Creek Makerspace, its members, its equipment, and its handbook are invented for
this course. Every name in the data is invented. No real person appears anywhere in it.)*

---

## Your data

`05-labs/fixtures/ridge-makerspace/`. Read its `README.md` first: it lists every kind of
mess in the files, so that when you hit one you know it is deliberate and not a broken
fixture.

| File | Format | What it holds |
|---|---|---|
| `raw/members_legacy.txt` | pipe delimited, comment lines, `mm/dd/yyyy` dates | 14 members |
| `raw/catalog.json` | JSON with a nested array and a nested object | 14 items |
| `raw/loans_spring.csv` | CSV from a spreadsheet, byte order mark, CRLF | 39 data rows |
| `handbook/*.md` | Markdown | 8 policy and procedure documents |

**Do not edit anything in `raw/` or `handbook/`.** Fix the data in code. A fix you made by
hand is a fix nobody can reproduce, which means you do not have a pipeline, you have a
one-off.

**There is no second route.** Everyone works the same dataset, because the memo, the labs,
the Gate 2 exercises, and the module exit assessment all reference it, and because a
dataset with known answers is how you find out your report is wrong.

---

## What you build

### A. The relational pipeline

1. **Ingest all three formats.** The `csv` module for the CSV, `json` for the JSON, and
   your own reader for the pipe delimited file. Not `split(",")`. The notes column has
   commas in it and quoted fields with quotes inside them.

2. **Design a schema and write it as an SQL script.** `schema.sql`, loaded with
   `executescript` or `sqlite3 db < schema.sql`. It must contain:
   - a primary key on every table
   - at least one many-to-many relationship, resolved with a junction table
   - `REFERENCES` on every foreign key, **and `PRAGMA foreign_keys = ON` on the connection**,
     because SQLite does not enforce them otherwise
   - at least two `CHECK` constraints that encode a rule from the brief
   - a comment above each table saying why it is shaped that way

3. **Clean, with every rule written down.** A row your rules can fix is fixed. A row they
   cannot is **quarantined**: stored, with its source file, its line number, and a reason a
   person can act on. **Nothing is dropped silently, and your program prints an arithmetic
   check that rows read equals rows loaded plus rows quarantined plus rows with no
   information in them.**

4. **Load in bulk.** `executemany`, not a loop of `execute`. Load order has to respect the
   foreign keys, and working out that order is part of the design.

5. **Migrate to at least two other formats, and measure what survived.** Export, load the
   export back into a fresh empty database built from the same `schema.sql`, and compare
   table by table. **A row count is not a fidelity check.** Report what each format costs.
   At least one of your formats must lose something, and your README must say exactly what
   and why.

6. **Report, with calculated fields.** Printed and written to a file. At least:
   - **four calculated fields**, at least two of which are grouped, and at least one of
     which uses a SQL function rather than arithmetic alone
   - a section that answers "which equipment is being used, and by which programs"
   - a section that answers "what has not come back"
   - the list of rows that need a person
   - **a single record form** for one item, printed on demand

7. **Tests.** At least eight, runnable with one command. **At least two must check a
   calculated field against arithmetic you did by hand before you wrote the query.** At
   least one must prove your foreign keys are actually enforced.

### B. The handbook index

8. **Chunk the eight handbook documents**, embed each chunk through the shared stack's
   embeddings endpoint, store the vectors, and query by similarity. Every hit must carry
   the file and the heading it came from.

   **Start the stub on this module's port and pass it explicitly, every time:**

   ```
   python Courses\145130\anchor-project\ai-stack\stub_model_server.py --port 11634
   ```

   ```
   python index_docs.py --model-url http://127.0.0.1:11634
   ```

   Module 4 uses **11634**. A real Ollama and several other course stubs all default to
   11434, and a run against the wrong server looks exactly like a working run. Never rely on
   the default.

   **Lab M04-05 is where you build this.** You may carry that code into your project. Say so
   in your decision log, and bring the honest paragraph from its step 17 with you.

9. **Nothing in your code may assume a vector length.** The stub returns 32 numbers. A real
   model returns hundreds. Read the length from the answer, store it with the index, and
   refuse a vector that disagrees.

10. **One honest paragraph in your README** about what your retrieval demo does and does not
    prove on the stub.

### C. The writing

11. **README, eight sections.** Listed below.
12. **`decision-log.md`.** One entry per decision that could have gone the other way, with
    the option you rejected and what your choice costs.
13. **`ai-usage-log.md`.** Every model interaction, what you kept, and how you checked it.
14. **`data-protection.md`.** Half a page. What this dataset would be if it were real, which
    fields you would not collect, who should see the section of your report that names
    people, and what you would have to ask before building this on real records. **Do not
    state a legal threshold and do not give legal advice.** The question is what the
    framework protects and why, and what you would ask and of whom.

---

## Required repository structure

```
makerspace-pipeline/
  schema.sql
  load.py
  report.py
  migrate.py
  chunker.py            or chunking inside index_docs.py
  embed.py
  vectorstore.py
  index_docs.py
  ask.py
  test_pipeline.py
  output/               created by your program, in .gitignore
  README.md
  decision-log.md
  ai-usage-log.md
  data-protection.md
  .gitignore
```

Splitting or merging files is fine. What is not fine is one 900 line program, because
nobody can test one 900 line program and the tests are 15 percent of the grade.

---

## The README, eight sections

1. **The question.** The advisor's two questions in your own words, and what you decided
   each one means as a number.
2. **How to run it and how to test it.** Exact commands, including the two terminal setup
   for the stub with `--port 11634` on one side and `--model-url http://127.0.0.1:11634` on
   the other.
3. **Data sources.** Each file, its format, its row count, and one sentence saying it is
   invented and no personal data is involved.
4. **The mess.** Every kind of problem you found, with one example and where it is. **Write
   this from reading the files, before you write cleaning code.**
5. **Rules I chose.** Every cleaning rule, one line each, including at least one you mark as
   arguable, with the other side stated.
6. **A real run.** The load counts, the report, the form, and the fidelity check, pasted.
7. **Checked by hand.** At least two calculated fields worked out from the raw rows, with
   the arithmetic shown, matching what the program prints.
8. **Known limitations.** At least four, observed rather than guessed. One of them must be
   about what the retrieval demo cannot show you.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use a commercial AI developer API | They require their users to be 18 or older. Every model call in this course is local. The stub ships with the shared stack so this lab runs with no model installed. |
| Put any real person's data in any file | Your repository is public. The fixture is invented and yours must stay invented. |
| Install a package | SQLite is in the standard library and needs no server. pandas is not on the lab machines, and dependency management is not what this module is about. |
| Edit the raw files | The mess is the assignment. |
| Guess a value you cannot read | The advisor asked to be told which rows are bad. A confident wrong number is worse than a flagged row, and this is the thing the brief says twice. |
| Call a fidelity check "the row counts match" | Thirty three rows went out and thirty three came back is exactly what a lossy migration looks like. |
| Hardcode 32 as a vector length | It works here and breaks on the first machine with a real model. |

---

## What a front end and a back end mean in this project

Your report is a front end. The database is the back end. **Every rule that must always be
true belongs in the back end.** If your loader refuses an orphan loan and your schema does
not, the rule is gone the first time somebody loads data another way. That is what the
`REFERENCES` clauses and the `CHECK` constraints are for, and it is the difference between a
schema that documents your intentions and a schema that enforces them.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 10 Thu, Build 2 | `decision-log.md` with the advisor's two questions rewritten as numbers you will calculate, and one sentence on what you will do with a row you cannot read. |
| **Measure, first pass** | Week 10 Fri, Build 2 | README section 4, **The mess**, written from **reading** the three raw files. No queries and no cleaning code yet. |
| **Measure, complete** | Week 11 Mon, Build 2 | The same section, extended with what your profiling queries in Lab M04-03 found, including line numbers. |
| **Analyze** | Week 11 Tue, Build 1 | Your schema, on paper or as a diagram, with every key and relationship marked, plus one calculated field worked out by hand from real rows. |
| **Improve** | Week 11 Tue, Build 2 to Week 12 Wed | Build, in this order, committing after each stage works: schema, ingest, clean and quarantine, load, migrate and verify, report, form, chunk, embed, query. |
| **Control** | Week 12 Thu, end of Build 2 | Tests passing, README complete, fidelity check run, the five-minute demo rehearsed once. |

**Measure is the checkpoint not to skip.** Every student who writes the mess down first
writes each cleaning rule once. Every student who skips it writes them three times, because
they discover the fourth shape of member id after the loader is finished.

**Analyze is where the advisor's trust comes from.** If you cannot work out one category's
average by hand from six rows, your program's answer for thirty three is a guess that agrees
with itself.

---

## Milestone schedule

| Day | Block | Goal |
|---|---|---|
| Week 10 Thu | Build 2 | Read the brief and the fixture README. Define. Decision log started. |
| Week 10 Fri | Build 2 | Measure, first pass, by reading the files. Repository created, first commit. |
| Week 11 Mon | Build 2 | Measure complete, with the profiling evidence from Lab M04-03. |
| Week 11 Tue | Build 1 | Analyze. Schema drawn, keys and relationships marked. One field by hand. |
| Week 11 Tue | Build 2 | `schema.sql` written and loaded, foreign keys proven on, all three formats ingested. |
| Week 11 Wed | Build 2 | Clean, quarantine, bulk load. The arithmetic check passes. |
| Week 11 Thu | Build 1 | Migrate to two formats and verify fidelity. |
| Week 11 Thu | Build 2 | Report with calculated fields, and the single item form. `data-protection.md` started. |
| Week 11 Fri | Build 2 | **Comparison memo due.** Project catch-up and BPA pre-submission. |
| Week 12 Mon | Build 2 | Chunk the handbook. Chunk boundaries decided and written down. |
| Week 12 Tue | Build 2 | Embed and store. The index reports the dimension it observed. |
| Week 12 Wed | Build 2 | Query by similarity, the honest paragraph, tests, README sections 6 and 7. |
| Week 12 Thu | Build 2 | Control. Tests, README, `data-protection.md`, rehearsal. |
| Week 12 Fri | commit window | Final commit in the 15 minutes before Build 1. **Build 2 is demos.** |

**Period 8 all three weeks** is available for this, and for BPA pre-submission work.

---

## Three worked scope examples

### Too small

> Reads the CSV with `DictReader`, loads every row into one SQLite table called `loans` with
> no foreign keys, prints a total count and an average, and writes the table back out as
> CSV.

One table is a spreadsheet with extra steps. No relationships means no referential
integrity, which means the orphan rows are in the totals. No schema decision was made, so
there is nothing to defend. Writing one table back out as one CSV loses nothing, so the
fidelity section has nothing in it. This is the 145060 project again, and it scores like it.

### About right

> Six tables with a junction table for tags, foreign keys enforced, and two `CHECK`
> constraints. All three formats read with their own reader. Eleven cleaning rules, each in
> its own function with a test. Six rows quarantined with line numbers and reasons, and an
> arithmetic check that the counts add up. Bulk loaded with `executemany` in foreign key
> order. Exported to JSON and to one CSV per table, both reloaded into a fresh database and
> compared table by table with a fingerprint; a third flat export kept deliberately to show
> what it loses. A report with seven calculated fields including an average over a filtered
> subset and a rate, a per-program section, an items-never-borrowed section, a holds
> section, and the quarantine list. A single item form. Fifty six handbook chunks embedded
> through the stub, dimension read from the answer, queried by cosine similarity with the
> source of every hit. Twelve tests, two of them checking hand arithmetic. README with all
> eight sections, one arguable rule stated with both sides, and a paragraph saying the stub's
> rankings mean nothing.

That is the reference implementation, and it is reachable in the time given.

### Too big

> Also adds a web front end, a login for staff, live overdue notifications, a maintenance
> cost predictor, and an interface that lets the advisor edit records in the browser.

A login is authentication, which is a security surface this project does not have time to
get right, and a half-secured login is worse than none. Prediction on 33 loans is noise with
a decimal point. Editing records in a browser means input validation, transactions, and
concurrency, which is a whole course. **The calibration question:** can you explain every
number in your report to the advisor, including where it came from and which rows are not in
it? If a feature makes that harder to answer, cut it.

---

## The five-minute demo

Week 12, Friday, Build 2. Your classmate plays the advisor.

1. **One number, traced.** (90 seconds) Point at one calculated field. Show the query,
   then show the raw rows it came from, then say the arithmetic out loud.
2. **One row that needs a person.** (60 seconds) Show it in the report, open the source file
   at that line number, and say why your program refused to guess.
3. **The migration that loses something.** (90 seconds) Run the fidelity check. Point at the
   row count that matches and the fingerprint that does not.
4. **One handbook question.** (60 seconds) Ask it, show the retrieved chunk, open the file
   at that heading, and say in one sentence what this demonstration does not prove.
5. **One question from the advisor.** (30 seconds)

**Steps 1, 3, and 4 are the graded ones.** They are the three things this module exists to
teach, and each of them is a claim you either can or cannot support live.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | All three formats ingested. Schema loaded from an SQL script with enforced foreign keys and at least two `CHECK` constraints. Bulk load in the right order. Two migrations with a real fidelity comparison. Four or more calculated fields, two grouped, one using a function. A single record form. A handbook index that builds and answers. |
| **Code Quality** | 20 | Cleaning rules in testable functions, not one long `if` chain. No bare `except`. `PRAGMA foreign_keys = ON` set on the connection. No hardcoded vector length. No credentials anywhere. Files small enough to test. |
| **Documentation** | 20 | Eight README sections. Decision log with a rejected option per entry. AI usage log with what was checked and how. `data-protection.md` written at the purpose level, naming what you would ask and of whom. |
| **Process** | 15 | DMAIC checkpoints on time, especially Measure before code and Analyze before the report query. Eight or more tests, two checking hand arithmetic, one proving foreign keys. A commit after each stage. |
| **Demonstration** | 10 | The five-minute demo, with a number traced to raw rows, a fidelity loss shown live, and an honest sentence about the retrieval demo. |
| **Polish** | 10 | A report the advisor reads without asking what a column means. Money and percentages formatted. Quarantine reasons a volunteer could act on. Error messages that name the file and the fix. |

**Security is not a separate row and it is still the fastest way to lose points here.** A
schema with `REFERENCES` clauses that nothing enforces loses Functionality and Code Quality
credit for the integrity requirement, however good the report looks, because the claim the
schema makes is not true.

---

## If you are stuck

**"My first column is called `\ufeffloan_id`."** That is the byte order mark a spreadsheet
writes. Open the file with `encoding="utf-8-sig"`.

**"My foreign keys are not doing anything."** Run
`connection.execute("PRAGMA foreign_keys").fetchone()`. If it says `0`, they are off. It is
a connection setting, not a file setting, and it is ignored inside a transaction.

**"`executescript` seems to turn my pragma off."** `executescript` commits first, which ends
the transaction. Set the pragma again after it.

**"My average looks too low."** Check whether it is averaging loans that have not come back.
A loan with no return date has no length yet, and including it as a zero drags the average
down for exactly the group with the worst problem.

**"A never-borrowed item is showing up as still out."** That is a `LEFT JOIN`. An item with
no loans still produces one row with every loan column `NULL`, and `returned_on IS NULL` is
true for that row. Guard on the loan's own key.

**"The retrieval results are nonsense."** They are supposed to be. The stub builds its
vector from a hash of the text. Say so in your README and in your demo.

**"Two handbook documents contradict each other."** Yes. Find it, and say what a retrieval
system does with a source set that disagrees with itself.
