# Tables, Records, Fields, Keys, and Why Repetition Is the Enemy
## 145130 Applications of AI · Module 4 · Week 10, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W10_TablesAndKeys.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W10_TablesAndKeys.pptx)

**Every example was executed on the build machine, Python 3.13.7, SQLite 3.50.4.**

---

## Why this matters before anything else

You will design a schema this week and defend it for the rest of the module. A schema is a
set of decisions, and the decisions are about **which facts get written down once**.

Every fact written down twice is a fact that can disagree with itself. That is not a
theoretical risk. It is in your fixture already.

---

## The vocabulary, in one table

| Word | What it is | In the esports data |
|---|---|---|
| **table** | one kind of thing | `players`, `matches`, `appearances` |
| **record** or **row** | one of that thing | one player |
| **field** or **column** | one fact about it | `grade_level` |
| **primary key** | the field, or combination, that identifies exactly one row | `gamertag` |
| **foreign key** | a field that points at a row in another table | `appearances.gamertag` |
| **relationship** | which rows go with which | a player has many appearances |
| **junction table** | a table whose only job is to connect two others | `appearances` |
| **normalization** | writing each fact down once | splitting the flat file into three tables |
| **transaction** | a group of changes that all happen or none do | recording a match with its lineup |

---

## Choosing a key: the one question

**Which of these two values would still be the same if the person changed their mind
tomorrow?**

In the esports file, `nightowl99` appears with two spellings of the same person's name:

```
2027-01-13,...,nightowl99,Jamal Petrov,12,keeper,1,2
2027-02-24,...,nightowl99,Jamaal Petrov,12,striker,6,1
```

Key on the name and you have nine players. Key on the gamertag and you have eight, plus a
disagreement you can report to somebody.

**A key is a promise, and the promise is about the real world.** `PRIMARY KEY (match_id,
gamertag)` is not a data structure choice. It is the claim that one player appears at most
once in one match. If that claim is ever false, the key is wrong, and the database will tell
you the first time it happens.

### Natural keys and made-up keys

A **natural key** is a value the real world already has: a gamertag, an item id, an ISBN.
A **surrogate key** is a number the database makes up.

The esports file has no match id at all. Nothing in it identifies a match except the date
and the opponent together. You have two defensible choices:

- `PRIMARY KEY (played_on, opponent)`, a natural key, so `appearances` carries both columns.
- `match_id INTEGER PRIMARY KEY` with `UNIQUE (played_on, opponent)`, so `appearances`
  carries one small number.

**The trade is real.** With the natural key, correcting a typo in a date means changing it in
every appearance row too. With the surrogate key, the correction is one row, and you now have
a number that means nothing outside this database. Pick one and write down why.

---

## Worked example 1: what repetition costs

`kettlecorn` moved up a grade. In the flat file:

```
python -c "print(sum(1 for line in open('esports_flat.csv') if 'kettlecorn' in line))"
```

```
3
```

Three rows to change, and the fourth time somebody does it they will miss one. In the
normalized version:

```sql
UPDATE players SET grade_level = 12 WHERE gamertag = 'kettlecorn';
```

One row. **That is what normalization buys.** Not elegance, not tidiness: one place to
change one fact.

---

## Worked example 2: the many-to-many, and why it needs its own table

A match has many players. A player is in many matches. **Neither table can hold the other
one**, because a column holds one value.

```sql
CREATE TABLE appearances (
    match_id INTEGER NOT NULL REFERENCES matches (match_id) ON DELETE CASCADE,
    gamertag TEXT NOT NULL REFERENCES players (gamertag) ON DELETE RESTRICT,
    role     TEXT NOT NULL,
    kills    INTEGER NOT NULL CHECK (kills >= 0),
    deaths   INTEGER NOT NULL CHECK (deaths >= 0),
    PRIMARY KEY (match_id, gamertag)
);
```

Read the primary key out loud: **one row per player per match**. The table exists to hold
that pairing, and it carries the facts that belong to the pairing rather than to either side:
which role they played and how they did.

`role` belongs here and not on `players`, because the same person plays striker in one match
and duelist in another. Working out which table a fact belongs to is the whole of schema
design, and the question is always: **what does this fact depend on?**

---

## Worked example 3: an array does not fit in a column

The makerspace catalog has this:

```json
{
  "item_id": "EQ-0110",
  "tags": ["printing", "resin", "training-required", "ventilation-required"]
}
```

Two options, and they are not equally good.

**Option A, one column:**

```sql
tags TEXT   -- 'printing;resin;training-required;ventilation-required'
```

Then "every item that needs training" is:

```sql
SELECT item_id FROM items WHERE tags LIKE '%training%';
```

which also matches a tag called `training-optional` the day somebody adds one. Renaming a tag
is a search and replace across every row. Counting items per tag needs string splitting in
SQL.

**Option B, two tables:**

```sql
CREATE TABLE tags (tag_id INTEGER PRIMARY KEY, tag TEXT NOT NULL UNIQUE);
CREATE TABLE item_tags (
    item_id TEXT NOT NULL REFERENCES items (item_id) ON DELETE CASCADE,
    tag_id  INTEGER NOT NULL REFERENCES tags (tag_id) ON DELETE CASCADE,
    PRIMARY KEY (item_id, tag_id)
);
```

Then the same question is:

```sql
SELECT i.item_id FROM items i
JOIN item_tags it ON it.item_id = i.item_id
JOIN tags t ON t.tag_id = it.tag_id
WHERE t.tag = 'training-required';
```

Real output from the reference database, seven items:

```
EQ-0101  EQ-0102  EQ-0110  EQ-0115  EQ-0120  EQ-0122  EQ-0150
```

**Option B costs you two tables and a join. It buys you a question you can answer exactly.**
Which one is right depends on whether anybody will ever ask that question, and in this module
the report asks it.

---

## The wrong version, and what it produces

Here is the schema people write on the first try.

```sql
CREATE TABLE season (
    played_on   TEXT,
    opponent    TEXT,
    game_title  TEXT,
    our_score   INTEGER,
    their_score INTEGER,
    gamertag    TEXT,
    player_name TEXT,
    grade_level INTEGER,
    role        TEXT,
    kills       INTEGER,
    deaths      INTEGER
);
```

It is the CSV with a `CREATE TABLE` in front of it. It loads, every query works, and it has
three problems that do not announce themselves.

1. **No primary key**, so the duplicated row goes in and every total is wrong by six kills.
2. **The match is repeated on every player row**, so two rows can disagree about the score and
   nothing stops them.
3. **The player's grade is repeated**, so `kettlecorn` can be in grade 11 and grade 12 in the
   same table at the same time.

Run it and it produces this:

```
python -c "import sqlite3,csv; c=sqlite3.connect(':memory:'); c.execute('CREATE TABLE season (gamertag TEXT, grade_level INTEGER)'); c.executemany('INSERT INTO season VALUES (?,?)', [('kettlecorn',11),('kettlecorn',12)]); print(c.execute('SELECT DISTINCT grade_level FROM season WHERE gamertag=\"kettlecorn\"').fetchall())"
```

```
[(11,), (12,)]
```

**Two answers to one question about one person, and no error anywhere.**

**Why the wrong version is tempting.** It is one table, every query is simple, no joins, and
it matches the file you were given. It is also what a model hands you if you ask for "a table
for this CSV", because that is literally what you asked for.

---

## Normalization, said plainly

You do not need the formal definitions this week. You need one rule:

**Every fact gets written down in exactly one place, and that place is decided by what the
fact depends on.**

- The score depends on the match. It goes in `matches`.
- The grade depends on the player. It goes in `players`.
- The role depends on the player **and** the match together. It goes in `appearances`.

If you can say which of those three a fact depends on, you have normalized it.

**And know when to stop.** The makerspace catalog has one purchase per item, so the purchase
columns live on `items`. A separate `purchases` table with exactly one row per item would be a
join that can never return more or fewer than one row. That is a table for the sake of looking
normalized.

---

## Self-check

**1.** A schema keys `matches` on `played_on` alone. It works perfectly on this file. Name the
day it breaks and what happens.

**2.** Why is `role` on `appearances` rather than on `players`?

**3.** Your teammate says the tags column is fine because `LIKE '%training%'` works. Give one
concrete question their design cannot answer and one it answers wrongly.

### Answers

**1.** The first day the team plays two matches, which is normal in an esports season and
happens in one afternoon at a tournament. The second insert raises
`UNIQUE constraint failed: matches.played_on`, and the load stops, or if there is no
constraint at all the two matches merge into one and every appearance points at whichever
one was written last.

**2.** Because a role depends on the player **and** the match together. `vexcalibur` played
striker three times and duelist once. On `players` there is room for one answer, and it would
be wrong for three of the four matches.

**3.** Cannot answer: "how many items carry each tag", without splitting strings in SQL, and
"rename `training-required` to `training`" without rewriting every row. Answers wrongly: "every
item that needs training" the moment anybody adds a tag containing the word training, because
`LIKE` matches characters and not tags.
