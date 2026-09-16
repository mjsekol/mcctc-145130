# Lab M04-01: The Spreadsheet That Became a Database
## 145130 Applications of AI · Module 4 · Week 10, Tuesday

**Gate:** 3, open tooling. **Duration:** Build 1, 40 minutes of build time, after the
Gate 1 rep that opens the block.
**Competencies:** 2.8.2 (the use and purpose of a database), 2.8.4 (tables, records, fields,
relationships, schema, normalization, keys), 2.8.8 (data integrity), 8.3.1 (collect and
maintain data in the database).

**No AI for step 3.** Deciding what the keys are is the thinking this lab is for, and a
model will hand you an answer in four seconds that you cannot defend. Use whatever you like
from step 6 on, and log it.

---

## The scenario

The esports team keeps its season in one spreadsheet. Every player who played in a match
gets a row, and every one of those rows repeats the date, the opponent, the game, and the
score. Seven matches and twenty eight rows, and the same match written down five times.

The coach wants to know who played the most and who is carrying the team. Right now that
means counting rows by hand, and the answer is already wrong, because one row got pasted in
twice and one player's name is spelled two ways.

*(The team, the players, the opponents, and the scores are invented for this course.)*

## What you will build

A program that reads the flat file once and writes three connected tables into a SQLite
database: one row per player, one row per match, and one row per player per match. Then a
query that answers the coach's question from those three tables.

---

## Files you need

`05-labs/lab-m04-01-files/`. Copy the whole folder into your own lab folder.

- `esports_flat.csv`, 28 rows, the season as one flat file
- `schema.sql`, with one table written for you and two to write
- `build_db.py`, which runs and does nothing useful

**SQLite needs no install.** It is in Python's standard library, and a database is one file.

---

## Starter code

`build_db.py` runs right now:

```
python build_db.py
```

```
flat rows read      28
players             0
matches             0
appearances         0
duplicate rows      0
```

Twenty eight rows read, nothing collected. That is the starting line.

---

## Steps

### Step 1. Look at the repetition before you touch anything

Open `esports_flat.csv` in your editor, not in a spreadsheet. Find the three rows for the
match on 2027-01-13 against Maple Ridge. **Count how many times the score `3,1` appears in
those rows.**

Write the answer in a comment at the top of `build_db.py`. That number is the problem this
lab solves. Every repetition is a place where one row can disagree with another, and once
they disagree, no program can tell you which one is right.

### Step 2. Find the two things that are already wrong

Two problems are in the file on purpose.

1. One row appears twice, identically.
2. One gamertag appears with two different spellings of the player's name.

**Find them both and write down the line numbers.** You are looking for exactly two things,
so if you find a third, say what it is in your submission.

### Step 3. Decide the keys, on paper, with no AI

Answer these four questions in a comment block before you write any SQL.

1. **What is the key of `players`?** The name or the gamertag, and why. One of them is typed
   by a person and one of them is not.
2. **What is the key of `matches`?** Nothing in the file is a match id, so you are making one
   up. What combination of existing columns must never repeat, and why is that true about
   this team?
3. **What is the key of `appearances`?** It is two columns together. Say which two, and say
   what real-world claim that makes.
4. **Which of those keys are foreign keys somewhere else?**

**This is the hardest part of the lab and it takes about eight minutes.** Everything after
it is typing.

### Step 4. Write the `matches` table

In `schema.sql`, under the TODO. Every column needs a type and the ones that can never be
missing need `NOT NULL`. Add:

- a primary key
- a `UNIQUE` constraint on the combination from your step 3 answer
- a `CHECK` that a score cannot be negative
- a comment above the table saying why it is shaped that way

### Step 5. Write the `appearances` table

Two foreign keys and a two-column primary key. Look at the `players` table for the
`REFERENCES` syntax, and read the two `PRAGMA foreign_keys = ON` lines in `connect()` before
you write it.

Run this to confirm the schema loads:

```
python build_db.py
```

If the tables are wrong, you get the error at this step rather than three steps later.

### Step 6. Collect the players

Fill in `collect_players`. One record per gamertag. When the same gamertag appears with two
names, **keep the first spelling and record the conflict** so the program prints it. You are
not fixing the name. You are telling somebody that two rows disagree.

Expected after this step:

```
players             8
name conflict       nightowl99: kept 'Jamal Petrov', also saw 'Jamaal Petrov'
```

### Step 7. Collect the matches and the appearances, and insert them

Fill in `collect_matches` and `collect_appearances`, then write the three `executemany`
calls in `main`.

**The insert order matters.** A foreign key can only point at a row that already exists.
Work out the order before you type it, and if you get it wrong you will see exactly which
one is wrong.

Expected:

```
flat rows read      28
players             8
matches             7
appearances         27
duplicate rows      1
```

**Twenty eight rows in, twenty seven appearances out.** The one that vanished is the
duplicate, and your program said so. That is the rule for the whole module: nothing
disappears without being counted.

### Step 8. Break it on purpose, twice

**First, the foreign key.** Add this temporary line right after the three inserts:

```python
connection.execute("INSERT INTO appearances VALUES (99, 'ghost_player', 'striker', 1, 1)")
```

Run it. Write down the exact error. Then comment out both `PRAGMA foreign_keys = ON` lines
and run it again. **Write down what happens the second time.**

Put the pragmas back and delete the temporary line.

**Second, the CHECK.** Change one player's grade level to 13 in your collector, run it,
write down the error, and change it back.

**Both of those write-downs are graded.** The second result of the first experiment is the
single most useful thing in this lab.

### Step 9. Answer the coach

Write the query at the bottom of `main`. Join `players` to `appearances`, group by player,
and print matches played, total kills, and total deaths, ordered by kills.

You should get eight rows, with `bellwether` on top with 64 kills.

### Step 10. Change one thing in one place

`kettlecorn` moved up a grade level. Write one `UPDATE` statement that fixes it, run it, and
then say in one sentence how many rows you would have had to change in the flat file to do
the same thing.

---

## Acceptance criteria

- [ ] The repetition count from step 1 is in a comment
- [ ] Both planted problems found, with line numbers
- [ ] The four key decisions answered in a comment block, in your own words
- [ ] `schema.sql` has three tables, each with a primary key, a comment, and at least one
      constraint beyond the key
- [ ] `python build_db.py` prints 8 players, 7 matches, 27 appearances, 1 duplicate row, and
      the name conflict
- [ ] Both step 8 experiments recorded, including what happened with the pragmas off
- [ ] The step 9 query prints eight rows with `bellwether` first
- [ ] The step 10 `UPDATE` runs, and the sentence is written

---

## If it breaks

**`sqlite3.OperationalError: no such table: matches`**
The `CREATE TABLE` is still commented out in `schema.sql`, or it has a syntax error and
`executescript` stopped there. Load the script in isolation to see where it stops.

**`sqlite3.IntegrityError: FOREIGN KEY constraint failed`**
You inserted a row whose foreign key points at a row that is not there yet. Usually this is
the insert order: appearances before matches, or appearances before players.

**`sqlite3.IntegrityError: UNIQUE constraint failed: players.gamertag`**
You are inserting the same gamertag twice, which means `collect_players` is returning one
record per row instead of one per player.

**`sqlite3.IntegrityError: CHECK constraint failed: grade_level BETWEEN 9 AND 12`**
The constraint is doing its job. This is step 8's second experiment, or a real bad value.

**`sqlite3.IntegrityError: UNIQUE constraint failed: matches.played_on, matches.opponent`**
Your `collect_matches` is returning one record per row rather than one per match.

**Everything runs and the counts are all zero.**
You filled in the collectors but `main` still passes the old empty lists, or your functions
return before the loop.

---

## Stretch goal

Add a fourth table, `games`, with one row per game title, and make `matches.game_title` a
foreign key to it. Then answer: does the team win more at Rocket League or at Valorant.
Before you write it, decide whether a two-row lookup table earns its place here, and write
down your answer either way. **There is a real argument on both sides and the argument is
the point.**

---

## Submission checklist

- [ ] `schema.sql` and `build_db.py` committed
- [ ] The step 8 write-ups in your README or in a comment block
- [ ] `output/` in `.gitignore`. The database is rebuilt from the CSV every run, so it is
      not source
- [ ] AI usage log updated if a model was used from step 6 on
- [ ] `git status` clean, pushed

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Fifteen minutes in and step 3 is still blank, or the answer to "what is the key of matches" is "the date" | SCAFFOLDED |
| Schema written, working through the collectors | STANDARD |
| Counts correct before 30 minutes, or asks what happens if two players share a gamertag | EXTENDED |
| "Why not keep it in the spreadsheet," or asks where anybody actually does this | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `collect_matches` is provided complete, as a second worked example.
- **Step 3:** answer questions 1 and 3 only. Question 2 is answered for you in the starter
  comment, and your job is to say in one sentence why `(played_on, opponent)` works and
  `played_on` alone does not.
- **Step 8 stays, both halves.** It is the lesson.
- **Step 10 is removed.**
- **Checkpoints:** show your instructor the schema after step 5 and the counts after step 7.

**Acceptance criteria:** three tables with keys and constraints, the counts correct, both
step 8 experiments recorded, the step 9 query printing eight rows.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** A gamertag can be changed. Add a `player_aliases` table so that an
old gamertag still resolves to the same player, and load it with one invented alias. Then
show that your kills query still returns eight players and not nine.

**Added requirement 2.** Make the duplicate row impossible rather than collapsed. Use
`INSERT ... ON CONFLICT DO NOTHING` so the database refuses the second copy instead of your
Python noticing it first, and explain in your README which of the two places that rule should
live in and why.

**Hint, not the answer.** Read the SQLite documentation page titled "UPSERT",
`https://www.sqlite.org/lang_upsert.html`, and the `ON CONFLICT` section of "CREATE TABLE",
`https://www.sqlite.org/lang_conflict.html`. Both are confident links. Look at what the
conflict target is and what happens when you leave it out.

**Acceptance criteria:** all STANDARD criteria, the alias table working, the conflict clause
in the schema, and a written answer about where the rule belongs.

---

## APPLIED

**For the student who asks where this is used for real.** Every application with a login
does this. A username is a key that does not change and a display name is a value a person
types. Separating them is why you can change your display name without losing your account.

**Changed scenario.** Bring your own flat file with no personal data in it: a game's item
list, a fantasy league export, a robot's telemetry log, a club's inventory sheet with
invented names. **It must have at least one fact repeated across rows.** Steps 1, 2, and 3
are the same questions asked of your file. Steps 4 through 7 normalize it into at least
three tables with at least one junction table. Step 8 is unchanged and required.

**The extra requirement that makes it the same lab.** Your README states what the repeated
fact was, how many times it appeared, and what a person would have had to change by hand to
fix it in one place. Step 10 is the proof.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether the
normalization actually removes the repetition you identified in step 1.
