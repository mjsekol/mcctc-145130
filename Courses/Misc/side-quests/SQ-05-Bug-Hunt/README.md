# SQ-05 · Bug Hunt
## Torch Run · 145060 Programming · Unlocks Unit 3, Week 7

**Time:** one block. **Difficulty:** ★★
**Competencies:** 5.4.6 (correct syntax and runtime errors), 5.4.7 (debug logic
errors), 5.4.5 (test a program using defined test cases), 5.6.13 (perform code
reviews).

---

## The situation

`torch_run.py` is a short dungeon crawl somebody else wrote. It runs. You can play
it and win. **It contains seven defects.**

Your job is to find all seven, fix them, and write up what each one was.

## The rule that makes this hard

**You may not rewrite the program. You may only fix it.**

Deleting the file and writing your own from scratch is not permitted and it is not
what this quest teaches. Reading code somebody else wrote, understanding it well
enough to change one thing safely, and leaving the rest working is most of a real
programming job. It is also the part nobody practises.

**You may not edit `test_torch_run.py`.** Changing a test until it passes is not
fixing a bug. It is hiding one.

---

## What the program is supposed to do

This is the specification the original author was given. Every defect is a place
where the program disagrees with it.

> **Torch Run**
>
> A short dungeon crawl. Four rooms: entrance, hall, storeroom, vault.
>
> 1. The player starts at the entrance carrying `MAX_TORCHES` torches. **The opening
>    message must state the real starting number**, so changing the constant changes
>    the message.
> 2. **Moving from one room to another burns one torch.** Attempting a direction that
>    is solid rock is not a move and **must not burn anything**.
> 3. **The brass lantern, found in the storeroom, replaces torches.** While the player
>    is carrying it, moving burns nothing. The in-game text promises this.
> 4. **Each item can be picked up once.** Taking the lantern a second time does not
>    give a second lantern.
> 5. **When torches reach zero and the player has no lantern, the game ends
>    immediately.** The player does not get a further move and cannot win afterwards.
>    The torch count is never negative.
> 6. The iron key is in the hall. Reaching the vault while carrying it wins the game.
> 7. **The win message reports how many moves were taken.** `look`, `take`,
>    `inventory`, and unrecognised commands are not moves.

---

## How to work

**Play it first, for five minutes.** Win it. Lose it. Type nonsense at it. You cannot
review code you have never watched run.

**Then run the tests:**

```bash
python test_torch_run.py
```

Seven of the eight tests fail. **Each failing test tells you WHAT is wrong. It does
not tell you WHERE.** Finding where is the quest.

The eighth test checks that the game can still be won. If your fix breaks that one,
you have traded one defect for another.

**Fix one defect at a time and rerun the tests after each.** Fixing three things at
once and then running the tests tells you nothing about which change did what.

---

## What to submit

A repository containing:

1. **`torch_run.py`**, fixed, with all eight tests passing.
2. **`BUGS.md`**, a written report with one entry per defect:
   - **Line number** in the original file
   - **What the code did**
   - **What it was supposed to do**, quoting the requirement number
   - **Your fix**
   - **How you found it.** Was it a failing test, playing the game, or reading?
3. **Commits.** One per defect, minimum, each message naming the defect it fixes.
   Your history should read as seven separate repairs, not one lump.

## Done when

- [ ] `python test_torch_run.py` reports 8 passed, 0 failed
- [ ] `BUGS.md` has seven entries, each with all five parts
- [ ] At least seven commits, each fixing one thing
- [ ] The program is still recognisably the same program
- [ ] You can explain every line you changed

---

## Hints, if you are stuck

**Stuck at four or five found.** The ones people miss are not in the movement code.
Read requirement 1 and requirement 7 again, then go looking for where the program
disagrees with them. Neither of those defects is visible while playing normally.

**A test fails and you cannot see why.** Run the exact commands the test runs, by
hand, and watch what happens. The test file shows you the command sequence for each
case.

**You fixed something and now the win test fails.** Good, that is the test doing its
job. Your fix changed behaviour something else depended on. Read your change again
and ask what else touched that variable.

**You cannot find the seventh.** Count how many defects you have entries for, then
reread the specification one numbered requirement at a time and point at the line
that satisfies each. If you cannot point at a line, that is your seventh.

---

## Grading

Scored under **BPA / Credential / Capstone**. 40 points.

| Dimension | Points | Standard |
|---|---|---|
| Defects fixed | 14 | 2 per defect, confirmed by the test suite |
| Write-up | 14 | 2 per entry, all five parts present |
| Process | 6 | One commit per defect with a message naming it |
| Explanation | 6 | You can talk through any change on request |

**A defect fixed without a write-up entry scores half.** A write-up entry for
something you did not actually fix scores zero. The report and the code have to
agree.
