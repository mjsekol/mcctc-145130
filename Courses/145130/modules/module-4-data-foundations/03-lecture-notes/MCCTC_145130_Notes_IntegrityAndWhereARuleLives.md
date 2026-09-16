# Integrity, Transactions, and Where a Rule Lives
## 145130 Applications of AI · Module 4 · Week 10, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W10_WhereARuleLives.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W10_WhereARuleLives.pptx)

**Every example and every error message was executed on the build machine, Python 3.13.7,
SQLite 3.50.4.**

---

## The question this lesson answers

You have a rule: a loan must point at a real member. **Where do you put it?**

There are three places, and they are not equivalent.

1. In the front end, so the person typing gets told.
2. In your loader, so bad rows never reach the database.
3. In the schema, so the database refuses regardless of who is asking.

**The answer is usually all three, and the one that counts is the third.** Today is about
why, and about the three ways the third one quietly fails to be there at all.

---

## Four kinds of integrity

| Kind | The claim | How it is enforced |
|---|---|---|
| **Entity integrity** | every row is identifiable and no two are the same row | `PRIMARY KEY` |
| **Domain integrity** | every value is one this column can legally hold | data type, `NOT NULL`, `CHECK` |
| **Referential integrity** | every pointer points at something that exists | `FOREIGN KEY` |
| **Transactional integrity** | a change is all or nothing | `BEGIN`, `COMMIT`, `ROLLBACK` |

Learn the four names. The exam uses them, and more usefully, they tell you which tool to
reach for when somebody describes a problem.

---

## Worked example 1: the three constraints, doing their jobs

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
connection.executescript("""
    CREATE TABLE players (
        gamertag    TEXT PRIMARY KEY,
        player_name TEXT NOT NULL,
        grade_level INTEGER NOT NULL CHECK (grade_level BETWEEN 9 AND 12)
    );
    CREATE TABLE appearances (
        match_id INTEGER NOT NULL,
        gamertag TEXT NOT NULL REFERENCES players (gamertag),
        PRIMARY KEY (match_id, gamertag)
    );
""")
connection.execute("PRAGMA foreign_keys = ON")
connection.execute("INSERT INTO players VALUES ('vexcalibur', 'Devon Whitaker', 12)")

for label, sql in [
    ("same gamertag twice", "INSERT INTO players VALUES ('vexcalibur', 'Devon W', 12)"),
    ("grade 13", "INSERT INTO players VALUES ('zzz', 'Someone', 13)"),
    ("a player who does not exist", "INSERT INTO appearances VALUES (1, 'ghost_player')"),
]:
    try:
        connection.execute(sql)
        print(f"{label:<28} NO ERROR")
    except sqlite3.IntegrityError as error:
        print(f"{label:<28} {error}")
```

Real output:

```
same gamertag twice          UNIQUE constraint failed: players.gamertag
grade 13                     CHECK constraint failed: grade_level BETWEEN 9 AND 12
a player who does not exist  FOREIGN KEY constraint failed
```

**Notice which message tells you the most.** The `CHECK` names the rule it broke, because
you wrote the rule in a form a person can read. The foreign key message does not name the
column. That is an argument for writing readable constraints and for adding your own message
in the layer above.

---

## Worked example 2: the same three, with the pragma off

Delete both `PRAGMA foreign_keys = ON` lines and run it again.

```
same gamertag twice          UNIQUE constraint failed: players.gamertag
grade 13                     CHECK constraint failed: grade_level BETWEEN 9 AND 12
a player who does not exist  NO ERROR
```

**The primary key and the `CHECK` still work. The foreign key does not.**

This is the single most important fact in Week 10, and it is specific to SQLite:

```
python -c "import sqlite3; print(sqlite3.connect(':memory:').execute('PRAGMA foreign_keys').fetchone())"
```

```
(0,)
```

**Foreign keys are off by default, on every new connection.** The setting belongs to the
connection, not to the file, so every program that touches the database has to switch it on
for itself. And because a `PRAGMA` inside a transaction is ignored, and `executescript`
commits, you often have to set it twice:

```python
connection.execute("PRAGMA foreign_keys = ON")
connection.executescript(open("schema.sql").read())
connection.execute("PRAGMA foreign_keys = ON")   # executescript ended the transaction
```

**A `REFERENCES` clause you did not switch on is a comment.** It is in the file, it is
correctly spelled, and it enforces nothing.

---

## Worked example 3: a transaction, and the commit that ruins it

Recording a match is two things: the match row, then its lineup. Here is the version that
looks careful and is not.

```python
cursor = connection.execute("INSERT INTO matches (...) VALUES (...)")
match_id = cursor.lastrowid
connection.commit()          # save the match straight away so the match_id is safe
for player in lineup:
    connection.execute("INSERT INTO appearances (...) VALUES (...)")
connection.commit()
```

Give it a lineup with the same player in it twice. Real output:

```
The database refused it: UNIQUE constraint failed: appearances.match_id, appearances.gamertag
```

That reads like the system protected itself. Then ask what is in the database:

```
players 8   matches 8   appearances 27
```

```
   8  2027-03-17  Cedar Valley   Rocket League  2-1   0 players
```

**A match played by nobody.** The early commit made the match permanent before a single
appearance was attempted, so when the second appearance raised, the first one rolled back
with the open transaction and the match did not.

The fix is one indentation level:

```python
with connection:
    cursor = connection.execute("INSERT INTO matches (...) VALUES (...)")
    match_id = cursor.lastrowid
    for player in lineup:
        connection.execute("INSERT INTO appearances (...) VALUES (...)")
```

**`with connection:` is not `with open(...)`.** It does not close the connection. It manages
a transaction: commit if the block finishes, roll back if it raises. Everybody who has used
`with open` assumes otherwise once.

Proof that it rolls back, from the corrected version:

```
IntegrityError: UNIQUE constraint failed: appearances.match_id, appearances.gamertag
matches before 7 after 7
appearances 27
```

---

## `ON DELETE`: two clauses, two different beliefs about the world

```sql
match_id INTEGER NOT NULL REFERENCES matches (match_id) ON DELETE CASCADE,
gamertag TEXT NOT NULL REFERENCES players (gamertag) ON DELETE RESTRICT,
```

Delete a player:

```
The database refused it: FOREIGN KEY constraint failed
```

Delete a match:

```
1 match row(s) deleted.
players 8   matches 6   appearances 24
```

**Three appearances went with it and nobody asked for them.**

The two clauses encode different claims. An appearance is **part of** a match: it has no
meaning once the match is gone, so cascading is right. An appearance is **not part of** a
player: it is a record of something that happened, and it stays true after the player leaves
the team.

**`RESTRICT` does not solve the problem. It refuses to guess**, which forces a person to
decide. For a graduating senior what you usually want is neither: a `left_on` date, so the
record stays and the roster does not.

---

## Where a rule lives, and what each place is for

| Where | Good at | Fails when |
|---|---|---|
| **Front end** | a message the person can act on: "vexcalibur is in the lineup twice" | somebody uses a different front end |
| **Loader** | rules that need context the database does not have, and collecting reasons | somebody loads data another way |
| **Schema** | holding for every writer, forever | nobody switched the pragma on |

**Put the rule in the schema, and put the message in the front end.** Those are not
duplicates of each other. One of them is true for everybody and unreadable. The other is
readable and true for one program.

**And some rules cannot go in a `CHECK` at all.** "A Rocket League match has exactly three
players" is about another table, and a `CHECK` can only see the row it is on. That needs a
trigger, or it needs to live in the loader with an honest note saying so.

---

## Vocabulary

| Term | What it means |
|---|---|
| **entity integrity** | every row is uniquely identifiable |
| **domain integrity** | every value is legal for its column |
| **referential integrity** | every foreign key points at a row that exists |
| **transaction** | a group of changes that all happen or none do |
| **rollback** | undoing an open transaction |
| **cascade** | deleting the children when the parent goes |
| **restrict** | refusing to delete a parent that still has children |
| **pragma** | a SQLite setting, set per connection |

---

## Self-check

**1.** Your schema has `REFERENCES` on every foreign key and an orphan row is in the table.
Name two different causes, and the one command that tells you which.

**2.** A program inserts a match, commits, then inserts five appearances and commits again.
The third appearance fails. What is in the database, and what should have happened?

**3.** Why does the team roster use `ON DELETE RESTRICT` and the match history use
`ON DELETE CASCADE`, when both are foreign keys into `appearances`?

### Answers

**1.** Either the pragma was never switched on, or it was switched on but the row went in
through a program that did not switch it on. Run `PRAGMA foreign_keys` on your connection for
the first, and `PRAGMA foreign_key_check` to list every row currently violating a foreign key
for the second. The second is the one that finds damage already done.

**2.** The match row is permanent, the first two appearances are rolled back, and the
database now holds a match with no lineup and no error to tell anybody. **What should have
happened is nothing**: one transaction around both inserts, so a failure anywhere leaves the
database exactly as it was.

**3.** They are foreign keys **out of** `appearances` into two different parents, and the two
parents mean different things. A match owns its appearances, so deleting the match should
take them. A player does not own their appearances: those are a record of events that stay
true after the player leaves. Cascading there would delete history because somebody left the
team.
