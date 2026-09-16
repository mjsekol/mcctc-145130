# Additional Resources · Week 10
## 145130 Applications of AI · Module 4
### Topics: what a database is, keys and normalization, database types, integrity

Links are marked **Confident** or **[VERIFY]**. **A [VERIFY] link has not been confirmed live
from this machine and must be clicked before it is assigned.** Broken links cost a class
period.

**Nothing this week needs a model, an account, or a network connection.** SQLite is in
Python's standard library.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | SQLite documentation: Foreign Key Support | Mon, Thu | On-level | 20 min |
| 2 | Python documentation: `sqlite3` | All week | On-level | 25 min |
| 3 | SQLite: Datatypes In SQLite | Tue, Wed | On-level | 15 min |
| 4 | SQLite: CREATE TABLE | Tue | On-level | 20 min |
| 5 | An interactive SQL practice site | Any | Remediation | 30 min |
| 6 | A free video on relational design | Any | Remediation | under 20 min |
| 7 | SQLite: Quirks, Caveats and Gotchas | Wed, Thu | Extension | 25 min |
| 8 | DB Browser for SQLite | Any | On-level | 10 min |
| 9 | The module's own lecture notes, self-check sections | Before Friday | Review | 20 min |
| 10 | Gate 1 bank, reps 01 to 10 | Before Friday | Review | 10 min each |
| 11 | Side quest: your own flat file, normalized | Fri flex | Extension | 1 block |

---

## 1. Primary reading: SQLite Foreign Key Support

`https://www.sqlite.org/foreignkeys.html` · **Confident.**

**Why this one.** It is the primary source for the single most important fact in this module,
and it says plainly that foreign key enforcement is off by default for backwards
compatibility.

**Assign a question, not the page:** *Find the section that says when foreign key enforcement
is on. Quote the sentence. Then find what happens to the setting inside a transaction.*

The answer to the second half explains why the labs set the pragma twice.

**Time.** 20 minutes. **Level.** On-level.

---

## 2. Python documentation: the `sqlite3` module

`https://docs.python.org/3/library/sqlite3.html` · **Confident.**

**Why this one.** It is the API you use every day this module, and two sections of it answer
questions students will otherwise guess at: the placeholder syntax, and what
`with connection:` does.

**Assign a question:** *Find the section about using the connection as a context manager. What
does it commit, what does it roll back, and what does it NOT do?*

**The last part is the one people get wrong.** It does not close the connection.

**Time.** 25 minutes. **Level.** On-level.

---

## 3. Datatypes In SQLite

`https://www.sqlite.org/datatype3.html` · **Confident.**

**Why this one.** It explains type affinity, which is why `CREATE TABLE t (x VECTOR)` is
accepted, and it explains that SQLite has no date type, which is why every date in this module
is text in `YYYY-MM-DD`.

**Assign a question:** *What happens if you declare a column with a type SQLite has never
heard of?*

That question is a Week 12 bell ringer, so reading it now pays twice.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. CREATE TABLE

`https://www.sqlite.org/lang_createtable.html` · **Confident.**

**Why this one.** Everything you need for the project schema: `PRIMARY KEY` including the
multi-column form, `NOT NULL`, `UNIQUE`, `CHECK`, and `REFERENCES` with `ON DELETE`.

**Assign a question:** *Find the difference between `ON DELETE CASCADE` and `ON DELETE
RESTRICT`, and write one sentence about when each is right for a school roster.*

**Time.** 20 minutes. **Level.** On-level.

---

## 5. Interactive SQL practice

**[VERIFY] before assigning.** Two that are commonly used and free to use in a browser:

- SQLBolt · `https://sqlbolt.com/` · **[VERIFY]**
- Select Star SQL · `https://selectstarsql.com/` · **[VERIFY]**

**Why either.** Both run queries in the browser with no account, which matters because this
course does not ask students to create accounts. **Click through the first lesson of whichever
you assign before you assign it**, and confirm it still runs without a sign-in.

**A guaranteed alternative that needs no link:** the fixture database. `sqlite3` is in the
standard library, and `05-labs/fixtures/ridge-makerspace/` is on the shared drive. A student
who needs query practice has a real database and a list of fourteen questions already written,
in `instructor/lab-m04-03-solution/profile.sql`, which your instructor can hand out after the
lab.

**Time.** 30 minutes. **Level.** Remediation.

---

## 6. A free video

**[VERIFY]. No specific video is linked**, because none has been confirmed from this machine.

**What to look for:** a video under twenty minutes on relational database design or
normalization, not on a specific product. **Watch it yourself before assigning it**, and check
two things: does it say that foreign keys need enforcing, and does it explain normalization as
"write each fact once" rather than as a list of numbered forms. Many do neither.

**Level.** Remediation.

---

## 7. Quirks, Caveats and Gotchas In SQLite

`https://www.sqlite.org/quirks.html` · **Confident.**

**Why this one.** This is the honest page, written by the people who built it, about the places
SQLite does not behave the way a reader of other databases expects. Flexible typing is on it.
So is the fact that a column declared `INTEGER PRIMARY KEY` behaves differently from every
other primary key.

**Assign a question:** *Pick the quirk you think is most likely to bite your project, and say
in two sentences what it would look like when it did.*

**Time.** 25 minutes. **Level.** Extension. **Good for the student who finishes Lab M04-01
early.**

---

## 8. DB Browser for SQLite

`https://sqlitebrowser.org/` · **[VERIFY]**, and check whether it is installable on lab
machines before you mention it.

**Why this one.** Being able to open the database file and look at the rows makes the whole
module concrete, and it is the fastest way to settle "did my insert actually happen".

**If it cannot be installed**, this is not a loss. Everything it does is one line of Python:

```
python -c "import sqlite3; print(sqlite3.connect('output/makerspace.db').execute('SELECT * FROM loans LIMIT 5').fetchall())"
```

**Time.** 10 minutes. **Level.** On-level.

---

## 9. The self-checks you already have

Every Module 4 lecture note ends with three self-check questions and worked answers, in
`03-lecture-notes/`. This week's four are `WhyADatabase`, `TablesRecordsKeys`,
`DatabaseTypesAndStructures`, and `IntegrityAndWhereARuleLives`.

**Before Friday, a student should be able to answer all twelve without reading the answers
first.** The ones most worth the time: WhyADatabase question 2, TablesRecordsKeys question 1,
and IntegrityAndWhereARuleLives question 3.

**Level.** Review.

---

## 10. Gate 1 reps for review

Reps 01 to 10 cover this week. Reps 02, 04, and 09 are the ones that turn up again in the exit
assessment. Your instructor assigns them from the instructor copy.

**Level.** Review.

---

## 11. Side quest: your own flat file

Not a catalog side quest, and worth an hour. Take a flat file you already have with no personal
information in it, a game export, a fantasy league sheet, a robotics telemetry log, and
normalize it into at least three tables with at least one junction table. That is the APPLIED
option of Lab M04-01, and it is the best possible preparation for the performance task.

**Level.** Extension.

---

## For the student who is behind

1. Monday's lecture notes, both programs typed and run
2. The `PRAGMA foreign_keys` command, run once, with the answer written down
3. Gate 1 reps 02 and 03
4. Lab M04-01 SCAFFOLDED, with the checkpoints

## For the student who is ahead

- Lab M04-01 EXTENDED, the alias table and `ON CONFLICT`
- Lab M04-02 EXTENDED, which needs a trigger
- The quirks page, resource 7
- Start the comparison memo's contested call section early
