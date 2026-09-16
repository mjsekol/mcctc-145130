# Why a Database and Not a Pile of Files
## 145130 Applications of AI · Module 4 · Week 10, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W10_WhyADatabase.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W10_WhyADatabase.pptx)

**Every example here was executed on the build machine, Python 3.13.7, SQLite 3.50.4. The
output is real.**

---

## Why this is the first day of the module

AI runs on data. Not on clever prompts and not on model size: on whether the thing you fed
it was true. Every module after this one assumes you can get data into a shape you can
defend, and this week is where that starts.

You already know how to read a CSV. What you have not been asked yet is **who guarantees the
file is right**, and the answer so far has always been you, in Python, one rule at a time,
in one program. That works until there is a second program.

---

## The concept in plain language

A **database** is a store of data plus a set of rules about what may be in it. A **database
management system**, or DBMS, is the software that keeps those rules whether or not the
program writing the data remembers them.

That second sentence is the whole idea. A spreadsheet holds data. A Python program that
validates a spreadsheet holds rules. **A database holds both, in one place, for every writer,
forever.**

Three things a DBMS gives you that a pile of files does not:

1. **Rules that outlive your program.** A `NOT NULL` column is still `NOT NULL` when somebody
   loads the table from a different script next year.
2. **A query language.** You describe the answer you want rather than the loop that finds it,
   and the system decides how.
3. **Transactions.** Several changes either all happen or none of them do, so a crash never
   leaves half a record.

---

## Worked example 1: the same question, two ways

The esports team's season, as one flat CSV. Here is "total kills per player" in Python:

```python
import csv

totals = {}
with open("esports_flat.csv", newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        tag = row["gamertag"]
        totals[tag] = totals.get(tag, 0) + int(row["kills"])
for tag in sorted(totals, key=totals.get, reverse=True):
    print(tag, totals[tag])
```

Real output:

```
bellwether 64
quietstorm 46
lowercase 40
vexcalibur 38
nightowl99 30
static_mango 24
kettlecorn 23
crabrangoon 14
```

Here is the same question in SQL, against the three-table version:

```sql
SELECT p.gamertag, SUM(a.kills) AS kills
FROM players p JOIN appearances a ON a.gamertag = p.gamertag
GROUP BY p.gamertag ORDER BY kills DESC;
```

```
bellwether    64
quietstorm    46
lowercase     40
vexcalibur    32
nightowl99    30
static_mango  24
kettlecorn    23
crabrangoon   14
```

**Look at `vexcalibur`.** The Python says 38. The SQL says 32.

Neither program is broken. The CSV has one row pasted in twice, and Python counted it twice
because nothing told it not to. The database refused the second copy, because `appearances`
has a primary key of `(match_id, gamertag)` and a player cannot appear in one match twice.

**The rule did the work, not the query.** Write that down.

---

## Worked example 2: what a rule looks like when it holds

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
connection.executescript("""
    CREATE TABLE players (gamertag TEXT PRIMARY KEY, player_name TEXT NOT NULL);
    CREATE TABLE appearances (
        match_id INTEGER NOT NULL,
        gamertag TEXT NOT NULL REFERENCES players (gamertag),
        kills    INTEGER NOT NULL CHECK (kills >= 0),
        PRIMARY KEY (match_id, gamertag)
    );
""")
connection.execute("PRAGMA foreign_keys = ON")
connection.execute("INSERT INTO players VALUES ('vexcalibur', 'Devon Whitaker')")
connection.execute("INSERT INTO appearances VALUES (1, 'vexcalibur', 6)")
print("one appearance in:", connection.execute(
    "SELECT COUNT(*) FROM appearances").fetchone()[0])
connection.execute("INSERT INTO appearances VALUES (1, 'vexcalibur', 6)")
```

Real output:

```
one appearance in: 1
Traceback (most recent call last):
  ...
sqlite3.IntegrityError: UNIQUE constraint failed: appearances.match_id, appearances.gamertag
```

**That error is the product.** Nothing in your program had to remember the rule. The database
remembered it and refused.

---

## Worked example 3: the front end and the back end

Two words you will use for the rest of this course.

The **back end** is the database: the records and the rules. The **front end** is anything a
person looks at: a kiosk screen, a report, a web page, an app.

```
   the kiosk screen          a report            a spreadsheet export
          |                      |                        |
          +----------------------+------------------------+
                                 |
                          one database
                      records, keys, constraints
```

**Every rule that must always be true belongs in the back end.** A rule in the front end is
true for the people who use that front end and nobody else.

You will prove this on Thursday by writing a fifteen line program that goes around the front
end entirely, and watching what the database does about it. Today, hold the sentence.

---

## The wrong version, and what it produces

Here is the version people write when they believe the front end is enough.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.executescript("""
    CREATE TABLE players (gamertag TEXT PRIMARY KEY, player_name TEXT NOT NULL);
    CREATE TABLE appearances (
        match_id INTEGER NOT NULL,
        gamertag TEXT NOT NULL REFERENCES players (gamertag),
        kills    INTEGER NOT NULL
    );
""")
connection.execute("INSERT INTO appearances VALUES (1, 'ghost_player', 6)")
print("rows:", connection.execute("SELECT COUNT(*) FROM appearances").fetchone()[0])
```

Real output:

```
rows: 1
```

**No error.** There is no player called `ghost_player`, the `REFERENCES` clause says there
has to be, and the row went in anyway.

Two things are wrong and they are different.

1. `PRAGMA foreign_keys = ON` is missing. **SQLite does not enforce foreign keys unless you
   ask, on every connection.** The default is off. Verified:

   ```
   python -c "import sqlite3; print(sqlite3.connect(':memory:').execute('PRAGMA foreign_keys').fetchone())"
   ```

   ```
   (0,)
   ```

2. There is no `PRIMARY KEY` on `appearances`, so a duplicate would also be accepted.

**Why the wrong version is tempting.** It looks identical to the right one. The `REFERENCES`
clause is right there in the schema, in the correct syntax, and reading the file tells you
integrity is handled. It is not handled. It is described.

That is the sentence to carry out of today: **a constraint you did not switch on is a
comment.**

---

## Vocabulary

| Term | What it means here |
|---|---|
| **database** | a store of data plus the rules about what may be in it |
| **DBMS** | the software that enforces those rules for every writer |
| **schema** | the written description of the tables, columns, keys, and constraints |
| **constraint** | a rule the database enforces, such as `NOT NULL`, `CHECK`, `UNIQUE`, or a foreign key |
| **transaction** | a group of changes that all happen or none happen |
| **front end** | anything a person interacts with |
| **back end** | the database, which does not care which front end is asking |
| **SQLite** | a database that is one file and a library, with no server to run |

**SQLite is not a toy.** It is the most widely deployed database engine there is, because it
is inside phones, browsers, and applications. It is a library rather than a server, which is
why it needs no install and why two people writing at once is the thing it does worst.

---

## Self-check

**1.** Your program validates every row before inserting it, and it has done for a year. Your
teammate writes a second script that loads a spreadsheet directly. What happened to your
validation?

**2.** A schema has `REFERENCES members (member_id)` on every foreign key. What is the one
command you run to find out whether that means anything?

**3.** `vexcalibur` scored 38 in Python and 32 in SQL. Which one is right, and what makes it
right?

### Answers

**1.** Nothing happened to it. It still runs, for your program. It never ran for theirs, and
it never will. The rules that survive a second writer are the ones in the schema, which is
what the back end is for.

**2.** `PRAGMA foreign_keys` on the connection you are using. `(0,)` means the clauses are
documentation. `(1,)` means they are enforcement. The setting is per connection, not per
file, so every program has to switch it on for itself.

**3.** 32. The CSV contains one row twice, and a player cannot appear in the same match
twice. The 38 is not a Python bug: Python was told to add up every row and it did exactly
that. **The difference is that one of the two had a rule and the other had a loop.**
