# Lab M04-02: What a Constraint Actually Does
## 145130 Applications of AI · Module 4 · Week 10, Thursday

**Gate:** 3, open tooling. **Duration:** Build 1, 40 minutes of build time, after the
Gate 1 rep that opens the block.
**Competencies:** 2.8.8 (the importance of data integrity and security), 2.8.9 (front end
versus back end), 8.3.1 (collect and maintain data: insert, update, delete), 2.8.4
(transactions), 1.4.3 (verify compliance with rules).

**No AI for steps 3 and 7.** Those two steps are the whole point of the lab, and a model
will hand you the conclusion before you have watched it happen.

---

## The scenario

The esports database from Tuesday now has a front end: `kiosk.py`, which the team manager
runs after a match. It checks the score, the roster, and the roles before it writes
anything, and it prints a polite message when something is wrong.

It looks safe. Today you find out how much of that safety is real, and how much of it only
exists while everybody uses the kiosk.

## What you will build

Nothing new. You are going to attack a working system four different ways, write down
exactly what happened each time, and then move three rules from where they are to where they
belong.

**This is a diagnosis lab, and the write-ups are the deliverable.** Code changes are about
fifteen lines.

---

## Files you need

`05-labs/lab-m04-02-files/`. Copy the whole folder.

- `esports_flat.csv`, `schema.sql`, `build_db.py`, all finished, so everyone starts level
- `kiosk.py`, the front end
- `backdoor.py`, fifteen lines that write straight to the database

Rebuild the database first:

```
python build_db.py
python kiosk.py list
```

```
matches
   1  2027-01-13  Maple Ridge    Rocket League  3-1   3 players
   2  2027-01-20  Fort Hollow    Rocket League  2-3   3 players
   3  2027-01-27  Cedar Valley   Valorant       13-9   5 players
   4  2027-02-03  Northline      Valorant       11-13   5 players
   5  2027-02-10  Brookstone     Rocket League  4-2   3 players
   6  2027-02-17  Granite Hills  Valorant       13-7   5 players
   7  2027-02-24  Maple Ridge    Rocket League  5-2   3 players
players 8   matches 7   appearances 27
```

Keep a file called `findings.md` open. Every step below ends with something to write in it.

---

## Steps

### Step 1. Read the front end before you run it

Open `kiosk.py` and find the `check` function. **List every rule it enforces.** There are
five. Write them in `findings.md` under a heading "Rules the kiosk enforces".

### Step 2. Add a match the normal way

```
python kiosk.py add --date 2027-03-03 --opponent "Maple Ridge" --game "Rocket League" --ours 4 --theirs 3 --lineup vexcalibur:striker:5:2,static_mango:midfield:3:3,nightowl99:keeper:1:1
```

```
Recorded match 8: Maple Ridge on 2027-03-03, 4-3, 3 players.
```

Then try one with a player who is not on the roster:

```
python kiosk.py add --date 2027-03-10 --opponent "Fort Hollow" --game "Valorant" --ours 13 --theirs 5 --lineup bellwether:duelist:20:9,ghost_player:sentinel:4:2
```

```
The kiosk refused this match:
  - ghost_player is not on the team roster
```

**Write down:** which layer refused it, and how you know.

### Step 3. Go around the front end

`backdoor.py` writes the same bad row straight into the database. It never calls the kiosk.
Read it first, then run it.

```
python backdoor.py
```

**Write down the exact error.** Then answer this in `findings.md`, in your own words, before
you move on: **the kiosk and the database both refused that row. Were they refusing it for
the same reason?**

### Step 4. Turn the guard off

Comment out the `PRAGMA foreign_keys = ON` line in `backdoor.py` and run it again.

**Write down what happens.** Then run `python kiosk.py list` and write down the appearance
count. Then put the pragma back and rebuild with `python build_db.py`.

**This is the result that matters most in this lab.** Say it in one sentence in
`findings.md`, starting with the words "A `REFERENCES` clause is".

### Step 5. Find the rule that exists in only one place

`backdoor.py` wrote a role of `goalkeeper`. The kiosk has a `ROLES` list and would have
refused it. The schema does not mention roles at all.

**Move that rule into the back end.** Add a `CHECK` constraint on `appearances.role` in
`schema.sql`, rebuild, and run `backdoor.py` again with the pragma switched on.

Write down the new error.

**Then answer:** now that the database checks it, should the kiosk stop checking it? Give
your answer and one reason. There is a real argument on both sides and you are being graded
on the reason, not the verdict.

### Step 6. Break a match in half

The kiosk does not check whether the same player is in one lineup twice. The database does,
because of the two-column primary key on `appearances`. Run this:

```
python kiosk.py add --date 2027-03-17 --opponent "Cedar Valley" --game "Rocket League" --ours 2 --theirs 1 --lineup vexcalibur:striker:4:1,vexcalibur:keeper:0:2,nightowl99:midfield:1:1
```

```
The database refused it: UNIQUE constraint failed: appearances.match_id, appearances.gamertag
```

That reads like the system protected itself. Now run `python kiosk.py list`.

**Write down the last line of that listing, exactly.** Then find the line in `kiosk.py` that
caused it. It is one line and it has a comment above it that sounds sensible.

### Step 7. Fix it, with no AI

Two changes.

1. **Make the whole add one transaction.** Either remove the early commit and use
   `with connection:` around both inserts, or use explicit `BEGIN` and `ROLLBACK`. Look up
   what `with connection:` does in the `sqlite3` documentation before you use it, because
   it does not do what `with open(...)` does.
2. **Add the repeated-player check to the kiosk too**, so the person at the desk gets a
   sentence they can act on instead of a constraint name.

Rebuild, repeat step 6's command, and confirm that the listing shows the same counts as
before you ran it.

**Write down why both changes were needed**, in two sentences. One of them prevents a bad
message. The other prevents bad data.

### Step 8. Delete two things and watch them behave differently

```
python kiosk.py remove-player --player crabrangoon
python kiosk.py remove-match --match 7
python kiosk.py list
```

One of those is refused. The other takes rows with it that you did not name.

**Write down:** what happened in each case, which clause in `schema.sql` caused it, and one
sentence on why a team roster and a match history should behave differently when something
is deleted.

---

## Acceptance criteria

- [ ] `findings.md` has all five kiosk rules from step 1
- [ ] Step 3 error recorded, with the "same reason" question answered
- [ ] Step 4 recorded, including the appearance count, and the "A `REFERENCES` clause is"
      sentence
- [ ] The role `CHECK` is in `schema.sql`, the new error is recorded, and the front end
      question is answered with a reason
- [ ] Step 6's listing line recorded exactly, and the responsible line in `kiosk.py`
      identified
- [ ] Step 7 fixed, both changes, and step 6's command now leaves the database unchanged
- [ ] Step 8 recorded with the clause that caused each behaviour

---

## If it breaks

**`sqlite3.IntegrityError: FOREIGN KEY constraint failed`**
Something points at a row that is not there. In step 3 that is the lab working. In step 8
it is `ON DELETE RESTRICT` refusing to orphan the appearances.

**`sqlite3.IntegrityError: CHECK constraint failed: role IN (...)`**
Step 5 working.

**`sqlite3.OperationalError: database is locked`**
Two programs are writing at once, or you left a connection open in an interactive shell.
Close the other terminal and try again.

**The step 4 result is an error again.** You commented out the pragma in `kiosk.py` instead
of `backdoor.py`, or you rebuilt after commenting it out, which puts the ON line back in
play through `build_db.py`.

**`python kiosk.py list` shows 31 appearances after step 4.** That is correct and it is the
whole lesson. Rebuild before step 5.

---

## Stretch goal

The schema says a score cannot be negative. Nothing says a Rocket League match must have
three players and a Valorant match five. Decide whether that rule can be expressed as a
`CHECK` constraint at all, and write down your answer with the reason. If it cannot, say
where it should live instead, and what that costs.

---

## Submission checklist

- [ ] `findings.md` committed, with all eight write-ups
- [ ] `schema.sql` and `kiosk.py` changes committed
- [ ] Database not committed, `output/` in `.gitignore`
- [ ] AI usage log updated, and it must say that steps 3 and 7 were done without a model
- [ ] `git status` clean, pushed

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty minutes in and step 4 has not been run, or `findings.md` is empty | SCAFFOLDED |
| Working through steps 5 to 7 | STANDARD |
| Finished step 7 before 35 minutes, or asks whether the kiosk should keep its checks | EXTENDED |
| "Why would anybody write `backdoor.py`," or asks where this bites in real systems | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Step 1** lists three of the five rules for you. Find the other two.
- **Step 5** gives you the `CHECK` clause to paste. Your job is the written answer about
  whether the kiosk should keep its own check.
- **Step 7** part 1 only. The kiosk check is dropped.
- **Steps 3, 4, 6, and 8 stay.** They are the lab.
- **Checkpoints:** show your instructor `findings.md` after step 4 and after step 6.

**Acceptance criteria:** steps 3, 4, 5, 6, and 8 recorded, the transaction fix working, and
the "A `REFERENCES` clause is" sentence written.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Make the database enforce the rule that a match must have at least
one player. A `CHECK` constraint cannot see another table, so this needs a trigger. Write
it, and write down what it costs: when it runs, what it does to the transaction in step 7,
and why a rule that crosses two tables is harder than one that does not.

**Added requirement 2.** Add a `deleted_on` column to `players` and change `remove-player`
so it marks a player as gone instead of deleting the row. Then say in your README which of
the two behaviours a team roster should have, and what breaks if you pick wrong.

**Hint, not the answer.** Read the SQLite documentation page "CREATE TRIGGER",
`https://www.sqlite.org/lang_createtrigger.html`, and look for `RAISE(ABORT, ...)` and for
what `BEFORE`, `AFTER`, and `INSTEAD OF` mean about ordering. Then find the section of that
page that says which statement the trigger sees.

**Acceptance criteria:** all STANDARD criteria, the trigger firing on a real attempt, and
both written answers.

---

## APPLIED

**For the student who asks where this bites in real systems.** Every application with more
than one way in has this problem: a web form, a mobile app, an admin panel, a nightly import
script, and somebody with a database client. Rules in one of those hold in one of those.

**Changed scenario.** Use the `handbook/` loan policy in `05-labs/fixtures/ridge-makerspace/`
and design the integrity rules for the makerspace loans table instead of the esports one.
Steps 1 and 2 become: read `02-loan-policy.md` and `07-electronics-bench.md`, list every
rule in them that a database could enforce, and mark each one as "a `CHECK` could do this",
"a foreign key could do this", "this needs a trigger", or "no constraint can express this".
Then write the ones you marked `CHECK` and foreign key into a schema and prove each of them
with a deliberate bad insert.

**The extra requirement that makes it the same lab.** One of the rules you find contradicts
another one across the two documents. Find it, and say what a database should do when the
policy it is enforcing disagrees with itself.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether each rule was
sorted into the right category, with a reason.
