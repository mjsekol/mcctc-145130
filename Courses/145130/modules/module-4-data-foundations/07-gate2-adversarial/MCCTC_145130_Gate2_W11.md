# Gate 2: Adversarial Review · Week 11
## 145130 Applications of AI · Module 4 · Week 11, Friday

**40 minutes**, in Build 1 after the Gate 1 rep. Individual. You may and should run the code.
**You may not ask a model whether it is correct**, because a model is what is being reviewed.

The program is `gate2-w11-files/box_office.py`. Copy the folder and run it.

---

## What you are looking at

The drama club's treasurer asked for a box office report. Somebody handed an AI assistant the
requirements in Part A and got this program back.

It runs. The numbers look reasonable. **One of them is wrong for two of the three
performances and right for the third**, which is the hardest kind of wrong number to notice,
because the one that is right makes the other two look like data rather than a bug.

**Five defects, one in each category**, plus **one judgement call** that is genuinely
arguable and is scored on your reasoning rather than your verdict.

| Dimension | What to look for |
|---|---|
| **Correctness** | A number that is not what the requirement says it is |
| **Security** | Input that decides what the database runs |
| **Readability** | A name that says one thing while the code does another |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something Part A asked for that is missing |

---

## PART A: The requirements

> Write `box_office.py`, which reports on the drama club's ticket sales.
>
> 1. Read `tickets.csv` and `nights.csv` and load them into SQLite.
> 2. Report one row per performance night: the room, tickets sold, revenue in dollars, the
>    average price of a ticket, and **what percent of the house was sold**.
> 3. **A comp ticket counts as sold. Its price is zero and it must not be included in the
>    average price**, because an average that includes the free ones is not the price anybody
>    paid.
> 4. Report one row per ticket type: how many and how much.
> 5. `--night` restricts the whole report to one performance.
> 6. Print the total revenue in dollars.

*(The drama club, the performances, the rooms, and the ticket records are invented for this
course. Prices are in whole cents in the file.)*

---

## PART B: What the AI produced

```
python box_office.py
```

```
RIDGE CREEK DRAMA CLUB . BOX OFFICE REPORT

BY NIGHT
  night        room              sold    revenue  median_price
  ------------ ---------------- ----- ---------- -------------
  2027-11-12   main auditorium    114  $1,068.00         $9.37
  2027-11-13   main auditorium    138  $1,406.00        $10.19
  2027-11-14   black box           59    $536.00         $9.08

  Total revenue: $3,010.00

BY TICKET TYPE
  type        count    revenue
  ---------- ------ ----------
  adult         140  $1,680.00
  student       115    $920.00
  senior         41    $410.00
  comp           15      $0.00
```

**Three ticket prices exist: student $8.00, adult $12.00, senior $10.00, and comps at $0.00.**
Look at the price column in the night table and ask whether every one of those three numbers
can be right.

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real person**, and
**the fix**.

Then two more entries:

- **The judgement call.** One thing in this program is a decision that could reasonably have
  gone the other way, and Part A does not settle it. Name it, take a side, give your reason,
  and say what would change your mind. **This is worth the same as finding a defect.**
- **What I was unsure about**, naming something specific. A blank costs more than a wrong
  guess.

### How to spend 40 minutes

- **First 6:** run it. Take the price column and check one number by hand from the type table.
  Adult, student, and senior counts are all there.
- **Next 8:** read every column heading against what the query under it calculates. Say each
  heading out loud as a sentence and ask whether the sentence is true.
- **Next 8:** run it with `--night`. Then run it with a `--night` value that is not a night.
  Then with one that has a single quote in it.
- **Next 8:** read Part A one requirement at a time and find the line that meets it.
- **Rest:** look at the two report functions side by side. One of them does something the
  other one does not need to.

---

## Scoring

Five defects at one point each, one point for the judgement call, one point for the
unsure-about entry. Your instructor states the security weighting before you start.

**Three of five defects is a normal score. Four is strong.** The judgement call is scored on
whether your reasoning is real, not on which side you took.
