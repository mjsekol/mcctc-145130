# Calculated Fields, Forms, and Reports Somebody Will Act On
## 145130 Applications of AI · Module 4 · Week 11, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W11_CalculatedFields.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W11_CalculatedFields.pptx)

**Every query and every value below was executed on the build machine, Python 3.13.7,
SQLite 3.50.4.**

---

## Why the report is the product

Nobody asked you for a database. The advisor asked two questions and wants numbers she can
put in front of a board. **The database is how you get there. The report is the thing.**

The competency is "generate and print forms, reports, and results of queries using calculated
fields and functions". Three words in that matter:

- **Calculated field.** A column that is not stored anywhere. It is worked out when the query
  runs, from columns that are stored.
- **Function.** `COUNT`, `SUM`, `AVG`, `ROUND`, `julianday`, `printf`, `COALESCE`, `NULLIF`.
- **Form.** One record, laid out for a person, rather than a table of many.

---

## Worked example 1: the anatomy of a calculated field

```sql
SELECT
    i.category,
    COUNT(l.loan_id)                                        AS loans,
    COUNT(DISTINCT l.member_id)                             AS members,
    ROUND(AVG(CASE WHEN l.returned_on IS NOT NULL
                   THEN julianday(l.returned_on) - julianday(l.checked_out_on)
              END), 1)                                      AS avg_days_out_returned
FROM items i
LEFT JOIN loans l ON l.item_id = i.item_id
GROUP BY i.category
```

Four things are happening and each is worth naming.

- **`COUNT(l.loan_id)` counts values, not rows.** That distinction is the whole of example 3.
- **`COUNT(DISTINCT l.member_id)` is a different question from `COUNT(*)`.** One member
  borrowing the same printer nine times is nine loans and one member. Put both on the page.
- **`julianday()` turns a date string into a number so it can be subtracted.** SQLite has no
  date type; this is how you get "days between".
- **`CASE WHEN ... END` with no `ELSE` returns NULL**, and `AVG` skips NULLs. That is how you
  average only the returned loans without a second query.

Real output:

```
  category     loans  members  avg days out  late returns  still out  overdue now  late rate %  value out $
  -----------  -----  -------  ------------  ------------  ---------  -----------  -----------  -----------
  computing        5        5           1.6             0          0            0          0.0         0.00
  electronics      4        4          12.3             0          1            1         25.0       512.00
  fabrication     12       10           7.0             2          3            2         33.3      2877.00
  media            9        9           3.8             2          1            0         22.2       899.00
  robotics         3        3           9.0             0          2            2         66.7       658.00
```

**Checked by hand before the query was written.** Fabrication is four items with twelve loans
between them. Nine came back, after 6, 6, 6, 7, 6, 5, 8, 13, and 6 days. That is 63 days over
9 loans, which is 7.0 exactly. The query agrees.

**Do the arithmetic first.** A calculated field checked against your own program's output only
proves the program agrees with itself.

---

## Worked example 2: a rate, and where to round

```sql
printf('%.1f',
    100.0 * SUM(CASE WHEN (l.returned_on IS NOT NULL AND l.returned_on > l.due_on)
                       OR (l.loan_id IS NOT NULL AND l.returned_on IS NULL
                           AND l.due_on < :as_of)
                     THEN 1 ELSE 0 END)
    / COUNT(l.loan_id))
```

Three rules in that one expression.

1. **`100.0` rather than `100`.** Two integers divided give an integer in SQLite:
   `SELECT 14/24` returns `0`, and `SELECT 1.0*14/24` returns `0.5833333333333334`. One `1.0`
   anywhere in the expression fixes it.
2. **`SUM(CASE WHEN ... THEN 1 ELSE 0 END)` counts things that match a condition**, inside the
   same pass as everything else. This is the pattern you will use most. It replaces running a
   second query and subtracting.
3. **Round at the edge, never in the middle.** `printf` formats the answer for a person. If
   you round each row before adding them up, the total is wrong in a way nobody can trace.

**And the date is a parameter, not `date('now')`.** Overdue is a claim about a moment. With
the clock in the query, the same command gives two answers on two days, no test can check a
number, and nothing you showed somebody last week can be reproduced.

---

## Worked example 3: the two traps that produce numbers instead of errors

### Trap 1: the LEFT JOIN row that is not a row

Two pieces of equipment have never been borrowed. A `LEFT JOIN` keeps them and fills every
loan column with NULL, so **`returned_on IS NULL` is true for an item sitting on the shelf.**

Without the guard, robotics reported 3 still out and $754.75 of equipment out the door. The
arithmetic said 2 and $658.00.

```sql
SUM(CASE WHEN l.loan_id IS NOT NULL
              AND l.returned_on IS NULL THEN 1 ELSE 0 END)  AS still_out
```

**`COUNT(*)` counts rows. `COUNT(column)` counts values.** They are the same number until a
`LEFT JOIN` makes a row with no values in it.

### Trap 2: the guard the formatter undoes

```
python -c "import sqlite3; c=sqlite3.connect(':memory:'); print(repr(c.execute(\"SELECT printf('%.2f', NULL)\").fetchone()[0]))"
```

```
'0.00'
```

Verified on SQLite 3.50.4. Also verified:

| Expression | Result |
|---|---|
| `printf('%.2f', NULL)` | `'0.00'` |
| `printf('%s', NULL)` | `''` |
| `printf('%d', NULL)` | `'0'` |
| `ROUND(NULL, 1)` | `NULL` |
| `1.0 / NULLIF(0, 0)` | `NULL` |
| `1.0 / 0` | `NULL`, **not an error** |

Two things to take from that table. **SQLite does not raise on division by zero**, so `NULLIF`
is about being explicit rather than about avoiding a crash. And **`ROUND` keeps a NULL while
`printf` turns it into a number**, so the two obvious ways to format behave differently at
exactly the moment it matters.

The fix is a `CASE` around the formatter:

```sql
CASE WHEN SUM(a.deaths) > 0
     THEN printf('%.2f', 1.0 * SUM(a.kills) / SUM(a.deaths))
     ELSE 'n/a' END AS kd_ratio
```

**A ratio of `0.00` is a claim.** It says this player plays and never gets a kill. `n/a` says
we cannot tell yet, which is true.

---

## Forms: one record, for a person

A report answers a question about many things. A **form** shows one thing, so somebody can
act on it.

```
RIDGE CREEK MAKERSPACE . ITEM RECORD
as of 2027-04-30

  Item            EQ-0110
  Name            Resin 3D printer
  Category        fabrication
  Condition       good
  Loan length     5 days
  Tags            printing, resin, training-required, ventilation-required
  Purchased       2026 for $649.50 from Booster club
  Replacement     $649.50

  Status          on the shelf

  Loan history
  loan    member   name            out         due         returned    status
  ------  -------  --------------  ----------  ----------  ----------  -------
  L-1012  RC-0190  Tobias Nkemelu  2027-03-10  2027-03-15  2027-03-15  on time
  L-1017  RC-0166  Dante Rossi     2027-03-16  2027-03-21  2027-03-24  late
  L-1030  RC-0151  Priya Raghavan  2027-04-07  2027-04-12  2027-04-20  late
```

Same database, same joins, different product. **The status line is a calculated field too**,
built from a `CASE` over the return date and the due date and the as-of date.

---

## Two products from one query

The report a person reads and the CSV a spreadsheet opens should come from **one query**, not
two copies of one query.

```python
cursor = connection.execute(BY_CATEGORY, {"as_of": as_of})
writer.writerow([description[0] for description in cursor.description])
writer.writerows([list(row) for row in cursor])
```

`cursor.description` gives you the column names the query itself chose, which means **the name
you write after `AS` is the heading the advisor reads.** Naming a calculated field well is now
part of the report rather than part of the code.

Two copies of a query drift. The day somebody adds a column to one, the other is missing it,
and both files look finished.

---

## The wrong version, and what it produces

```python
rows = connection.execute("SELECT * FROM loans").fetchall()
totals = {}
for row in rows:
    category = lookup_category(row[2])          # another query, per row
    totals[category] = totals.get(category, 0) + 1
```

It works. It also does three things wrong at once.

1. **A query per row**, to answer something one `GROUP BY` answers.
2. **The calculation is now in Python**, where the advisor cannot read it. When she asks where
   7.0 came from, you have to explain a loop instead of showing her a sentence.
3. **`SELECT *` and `row[2]`.** Add a column to the table and `row[2]` is a different column,
   with no error.

**Why it is tempting.** You already know Python and you do not yet know SQL well. That is a
real reason and it is temporary. The database is faster at this, the query is shorter, and
**the query is the documentation.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **calculated field** | a column worked out when the query runs, not stored |
| **aggregate** | a function over many rows: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| **GROUP BY** | collapse rows into one per group |
| **HAVING** | a filter applied after grouping, where `WHERE` runs before |
| **COALESCE** | the first value that is not NULL |
| **NULLIF** | NULL when two values are equal, used to stop a division |
| **view** | a saved query that behaves like a table |
| **form** | one record, laid out for a person |

---

## Self-check

**1.** `SELECT 14/24` returns 0 in SQLite. Name the fix and say why it is not a rounding
problem.

**2.** Your report shows a category with 3 loans and 3 still out, and you know one of them
came back. What is the first thing to check?

**3.** You guard a division with `NULLIF` and the column still prints `0.00`. What happened?

### Answers

**1.** Multiply one side by `1.0`, or cast one side to REAL. It is not a rounding problem
because no rounding happened: integer division threw the fractional part away before any
rounding could apply. `SELECT 1.0*14/24` gives `0.5833333333333334`.

**2.** Whether the category contains an item with no loans at all, and whether the query is a
`LEFT JOIN`. An item that has never been borrowed produces one row with every loan column
NULL, and `returned_on IS NULL` counts it as still out. Guard on the loan's own key.

**3.** `printf` turned the NULL back into a number. `printf('%.2f', NULL)` is `'0.00'` in
SQLite. The guard protected the division and the formatter undid it. **Every step between the
data and the page is a place a NULL can become a number**, so guard the display too, with a
`CASE`.
