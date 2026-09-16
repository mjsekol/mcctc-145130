# Lab M04-04: The Report the Coach Reads
## 145130 Applications of AI · Module 4 · Week 11, Wednesday

**Gate:** 3, open tooling. **Duration:** Build 1, 40 minutes of build time, after the
Gate 1 rep that opens the block.
**Competencies:** 8.5.4 (generate and print forms, reports, and query results using
calculated fields and functions), 1.4.6 (use an electronic database to create business and
technical information), 2.8.4 (schema and relationships).

**Steps 7 and 8 are no AI.** They are two traps you have to watch spring, and a model will
tell you about them before you have seen them.

---

## The scenario

The esports database from Week 10 has seven matches in it. The coach wants a report she can
put in front of the athletic director and a one page record she can hand to a player.

She has one requirement and she means it: **every number on the page has to be one you can
explain.** She has been handed reports before with a column nobody could account for.

## What you will build

Four queries, each one a calculated field or a grouped summary, and a one player record
form. The report prints to the screen, saves to a text file, and saves the player table as a
CSV the coach can open in a spreadsheet.

---

## Files you need

`05-labs/lab-m04-04-files/`. Copy it.

- `esports_flat.csv`, `schema.sql`, `build_db.py`, all finished
- `report.py`, with the plumbing written and four of the six queries as TODOs

```
python build_db.py
python report.py
```

Five sections print. Four of them say `not written yet`.

**Read the comment block at the top of `report.py` before step 3.** It names the three
things that go wrong in this lab, and you are going to meet all three.

---

## Steps

### Step 1. Work one number out by hand first

Open `esports_flat.csv`. Find every row for `bellwether`. Add up the kills and add up the
deaths, on paper.

Write both totals and the ratio in a comment at the top of `report.py`.

**This is not busywork.** For the rest of the lab, when a query returns a number, you have
one number you already know. A calculated field checked only against your own program's
output proves that the program agrees with itself.

### Step 2. Notice where the column headings come from

Read the `section` function. The headings are not a list in Python. They come from
`cursor.description`, which means **the name you give a calculated field with `AS` is the
name the coach reads.**

Write one sentence in your README about why that is better than keeping a list of headings
next to each query.

### Step 3. The player table

Fill in `PER_PLAYER`. Columns, with exactly these names:

`gamertag`, `player_name`, `grade_level`, `matches_played`, `kills`, `deaths`, `kd_ratio`,
`kills_per_match`

Requirements:

- `LEFT JOIN` from `players` to `appearances`, so that a player who has never played still
  appears
- `kd_ratio` to two decimal places
- `kills_per_match` to one decimal place
- ordered by kills, highest first

**Check `bellwether` against your step 1 number before you go on.**

### Step 4. The game table

Fill in `PER_GAME`. One row per game title: matches, wins, losses, win rate as a percent,
average score for, average score against.

**Wins and losses come from one query, not two.** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is
the pattern, and you will use it in your project four times.

### Step 5. The match table

Fill in `PER_MATCH`. One row per match with the score, the result as a word, how many players
were in it, the team's total kills, and **the gamertag of that match's top scorer**.

The top scorer needs a subquery inside the `SELECT` list. Decide what happens when two
players tie, and write your decision in a comment. A query that returns a different answer
on two runs is a query the coach cannot trust.

### Step 6. The role table

Fill in `ROLE_SPREAD`. One row per role: how many times it was played, how many different
players played it, and the average kills in it.

`COUNT(*)` and `COUNT(DISTINCT gamertag)` are two different questions. Both are in this one.

### Step 7. A player joins the team, and your report breaks

A ninth grader joined and has not played yet. Add her:

```
python -c "import sqlite3; c=sqlite3.connect('output/esports.db'); c.execute('PRAGMA foreign_keys=ON'); c.execute(\"INSERT INTO players VALUES ('mothlamp','Rue Castellanos',9)\"); c.commit()"
```

Run the report again and **look at her `matches_played`**.

If it says `1`, your query has the bug this step is for. She has played nothing. Find out
why the `LEFT JOIN` produced a row that got counted, and fix it.

**Write down in your README:** what `COUNT(*)` counts, what `COUNT(a.match_id)` counts, and
why the difference only shows up when somebody has no matches.

### Step 8. The guard that got erased

Look at `mothlamp`'s `kd_ratio`.

If it says `0.00`, you have the second trap. You divided with `NULLIF`, which correctly gave
you NULL, and then `printf` turned the NULL into `0.00`. **A ratio of zero is a claim. It
says she plays and never gets a kill.**

Prove it to yourself:

```
python -c "import sqlite3; print(repr(sqlite3.connect(':memory:').execute(\"SELECT printf('%.2f', NULL)\").fetchone()[0]))"
```

Fix it so the column says something that is not a number. Then write one sentence about why
a guard early in a calculation is not enough.

### Step 9. The form

`python report.py form vexcalibur` already works. Run it, then run
`python report.py form mothlamp` and `python report.py form nobody`.

Write down what each of the three does, and whether the third one is a good message.

### Step 10. Two products, one query

`write_player_csv` uses the same `PER_PLAYER` query the report uses. Open
`output/by_player.csv`.

Write one sentence about what would go wrong if the CSV had its own copy of that query.

---

## Acceptance criteria

- [ ] `bellwether`'s kills, deaths, and ratio worked by hand in step 1, matching the report
- [ ] All four queries written, with the exact column names asked for
- [ ] The tie rule in step 5 decided and commented
- [ ] Step 7 fixed: `mothlamp` shows 0 matches played
- [ ] Step 8 fixed: her ratio is not a number
- [ ] Section 4 lists `mothlamp`
- [ ] Steps 2, 7, 8, 9, and 10 written up in your README
- [ ] `output/season_report.txt` and `output/by_player.csv` both written

---

## If it breaks

**`sqlite3.OperationalError: misuse of aggregate: COUNT()`**
An aggregate inside a `WHERE`. `WHERE` runs before the grouping. Use `HAVING`.

**Every player shows the same totals.**
No `GROUP BY`, or grouping by something that is the same for everybody.

**`kd_ratio` is `1` or `0` for everybody.**
Integer division. `kills / deaths` on two integers gives an integer. Multiply one side by
`1.0` first.

**`kd_ratio` is empty rather than `n/a`.**
`printf('%s', NULL)` returns an empty string, and `printf('%.2f', NULL)` returns `0.00`.
Neither is what you want. Decide with a `CASE`.

**`sqlite3.OperationalError: no such column: kills`**
You are using a column alias somewhere that runs before the alias exists. `ORDER BY` can see
aliases. `WHERE` cannot.

**`sqlite3.OperationalError: near "FROM": syntax error`**
A trailing comma at the end of your `SELECT` list. SQLite points at the word after the
comma, not at the comma.

**Two columns turned into one and the heading looks odd.**
A missing comma between two columns. `SELECT a b FROM t` is valid SQL: it means column `a`
renamed to `b`. No error, one column, wrong name. This is the fourth time this module has
shown you a program that runs and is wrong.

---

## Stretch goal

Add a section that shows, for each match, each player's kills as a percentage of that
match's team total. You will need the match total available on every player's row at the
same time, which a `GROUP BY` cannot give you. Look up SQLite window functions,
`https://www.sqlite.org/windowfunctions.html`, and find `SUM(...) OVER (PARTITION BY ...)`.

---

## Submission checklist

- [ ] `report.py` committed with all four queries
- [ ] README write-ups for steps 2, 7, 8, 9, and 10
- [ ] `output/` in `.gitignore`
- [ ] AI usage log updated, and it says steps 7 and 8 were done without a model
- [ ] `git status` clean, pushed

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty minutes in and `PER_PLAYER` still returns one column | SCAFFOLDED |
| Two or three queries written, working through the rest | STANDARD |
| All four before 35 minutes, or asks how to get a match total onto every row | EXTENDED |
| "Why not do the maths in Python," or asks who actually reads a report like this | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `PER_PLAYER` is provided complete, including both traps already fixed, as the
  worked example. Steps 7 and 8 then ask you to break it on purpose and put it back.
- **Step 5** drops the top scorer subquery. The rest of the match row stays.
- **Step 6** is removed.
- **Steps 1, 7, 8, and 9 stay.** They are the lab.
- **Checkpoints:** show your instructor the hand arithmetic after step 1 and the report after
  step 4.

**Acceptance criteria:** `PER_GAME` and `PER_MATCH` written, both traps demonstrated and
explained in writing, the form run three ways, and the hand check matching.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Do the stretch goal with a window function, and add a column showing
each player's rank within that match by kills.

**Added requirement 2.** Add a section that shows each player's form over time: their kills
in each match next to their own average so far, so the coach can see who is improving. This
needs a running average, which is another window function with a frame.

**Hint, not the answer.** Read `https://www.sqlite.org/windowfunctions.html`. Find
`PARTITION BY`, then find the part of the page about frames and the words
`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. Then work out why a window function
cannot go in a `WHERE` clause and what you have to wrap the query in instead.

**Acceptance criteria:** all STANDARD criteria, both window queries returning the right
number of rows, and a sentence about what a running average tells the coach that a season
average does not.

---

## APPLIED

**For the student who asks who reads a report like this.** Somebody who has to defend a
budget. The athletic director asks why the team needs two more licences, and "we played seven
matches and here is the use per player" is an answer. "It feels busy" is not.

**Changed scenario.** Use the makerspace database from your performance task instead of the
esports one, and write the report the advisor asked for rather than the report the coach
asked for. The four queries become: by category, by program, items never borrowed, and the
holds list. The form becomes a single item record.

**The extra requirement that makes it the same lab.** Steps 1, 7, and 8 are unchanged and
required. Work one category out by hand before you write the query. Then confirm that an item
nothing has borrowed is not counted as still out, and that a category with no loans does not
report a late rate of zero percent.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether each number in
the report answers a question the advisor actually asked.
