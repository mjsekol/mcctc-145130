# Three Ways to Import, and Why You Stage First
## 145130 Applications of AI · Module 4 · Week 11, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W11_ThreeWaysToImport.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W11_ThreeWaysToImport.pptx)

**Every example and count was executed on the build machine, Python 3.13.7, SQLite 3.50.4,
against the shared fixture.**

---

## Why this is more than reading a file

The competency says: **import large data sets into a database using a bulk command, an SQL
script, or a CSV file.** Those are three different routes and they exist for three different
reasons.

The thing they have in common is the mistake people make with all three: **converting the
data while reading it.** Today's rule is that you land the file first and decide later.

---

## Route 1: the bulk command

One call into the database, many rows.

```python
rows = [(line_number, fields) for ...]
connection.executemany(
    "INSERT INTO stg_loans (source_row, loan_id, member_id, item_id, "
    "checked_out, due, returned, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
```

**Why this is the default.** The statement is prepared once and reused. The values travel
separately from the SQL, so nothing in a value can ever be read as SQL. That second property
is not a bonus feature, it is the whole reason this route is safe and the next one is not.

Real result on the fixture:

```
stg_loans     40 rows   (csv module, executemany)
```

**Forty, and the file has thirty nine data rows.** One of them is a second copy of the header
that somebody pasted in the middle. Staging keeps it. Deciding what to do about it is a
later step, and the profiling query finds it by name.

---

## Route 2: the SQL script

A text file full of `INSERT` statements, run all at once.

```python
statements = []
for line_number, line in enumerate(handle, start=1):
    fields = line.rstrip("\n").split("|")
    values = ", ".join("'" + field.replace("'", "''") + "'" for field in fields)
    statements.append(f"INSERT INTO stg_members (source_row, ...) "
                      f"VALUES ({line_number}, {values});")
connection.executescript("\n".join(statements))
```

Real result:

```
stg_members   14 rows   (generated SQL script, executescript)
```

and the first line of the generated file:

```sql
INSERT INTO stg_members (source_row, member_id, full_name, grade_level, program, joined) VALUES (4, 'RC0142', 'Amara Delgado', '11', 'Engineering Technology', '09/02/2026');
```

**Why anybody does this.** The database is on another machine, or behind a process where all
you can send is a file, or the load has to be checked into a repository and reviewed like
code. A `.sql` file is portable in a way a Python program is not.

**Why it is the dangerous one.** Look at `field.replace("'", "''")`. That doubling is the
only thing standing between you and a broken script, and you had to remember it. Forget it,
and the first name with an apostrophe in it ends the SQL string early:

```
sqlite3.OperationalError: near "Dell": syntax error
```

In this fixture no name has an apostrophe, **so your bug will not show up today.** It will
show up the first time somebody named O'Brien joins, in front of somebody who is waiting for
the report.

---

## Route 3: reading the structured format

This one is not an alternative to the other two. It is always the first half, because the
file is never already SQL.

```python
with open(path, encoding="utf-8") as handle:
    document = json.load(handle)
for position, item in enumerate(document["items"], start=1):
    purchase = item.get("purchase") or {}
    rows.append([position, item["item_id"], ..., ";".join(item.get("tags", []))])
```

```
stg_items     14 rows   (json module, executemany)
```

**Notice the tags are joined into a string here**, and notice that this is the opposite of
what Tuesday of Week 10 told you to do. That is deliberate. Staging is a photograph of the
file. Splitting the array into a junction table is a schema decision, and decisions belong in
the next stage, not in the reader.

---

## The byte order mark, which costs everybody twenty minutes once

A spreadsheet saving as CSV writes three invisible bytes at the start of the file. With
plain UTF-8, your first column name is not what you think:

```
python -c "import csv; rows=list(csv.DictReader(open('loans_spring.csv', newline='', encoding='utf-8'))); print(repr(next(iter(rows[0].keys()))))"
```

```
'\ufeffloan_id'
```

and then `row["loan_id"]` raises `KeyError: 'loan_id'` on a line that reads correctly.

**The fix is `encoding="utf-8-sig"`.** And `str.strip()` does not remove it, because as far
as Python is concerned it is not whitespace.

---

## Why every staging column is TEXT

```sql
CREATE TABLE stg_loans (
    source_row  INTEGER NOT NULL,
    loan_id     TEXT, member_id TEXT, item_id TEXT,
    checked_out TEXT, due TEXT, returned TEXT, notes TEXT
);
```

`int('11')` and `int(' 11 ')` are both 11, and one of them tells you that a volunteer typed a
space. **The moment you convert, you have thrown away the evidence.**

Two rules for a staging table:

1. **Every column is TEXT and nothing is converted.**
2. **Every row carries the line number it came from**, so any problem you find can be handed
   to a person with a place to look.

---

## Worked example: the join that fails, and the join that works

This is the reason staging is worth a whole lesson.

The loans file writes `RC-0142`. The member file writes `RC0142`. Ask the naive question:

```sql
SELECT COUNT(*) AS loans_with_no_matching_member
FROM stg_loans l
WHERE l.loan_id <> 'loan_id'
  AND NOT EXISTS (SELECT 1 FROM stg_members m WHERE m.member_id = l.member_id);
```

```
38
```

**Thirty eight of thirty nine loans have no member.** That number is correct, it is
reproducible, and it is the answer to a question nobody meant to ask.

Now normalize both sides inside the query:

```sql
... WHERE 'RC-' || substr(replace(upper(trim(m.member_id)), '-', ''), 3)
        = 'RC-' || substr(replace(replace(upper(trim(l.member_id)), '-', ''), ' ', ''), 3)
```

```
1   RC-0199
```

**One.** A join compares values, not meanings. Two values that mean the same person and are
written differently are two different values, and SQL will tell you so with a straight face.

---

## The wrong version, and what it produces

The wrong version is a loader that cleans as it reads.

```python
for row in csv.DictReader(handle):
    member_id = row["member_id"].strip().upper().replace(" ", "")
    if not member_id.startswith("RC-"):
        member_id = "RC-" + member_id[2:]
    connection.execute("INSERT INTO loans ...", (member_id, ...))
```

It works. The data is correct. **And you can no longer ask what the file said.**

Try to answer "how many different ways was a member id typed" and the answer is one, because
you made it one. The Measure step of your project is now impossible, because you would be
profiling your own rules rather than the advisor's files.

**Why it is tempting.** It is fewer moving parts, fewer tables, and it is finished sooner.
For a one-off job against a source that will never change again, it is the right call, and
saying that out loud is part of understanding the trade.

---

## Vocabulary

| Term | What it means |
|---|---|
| **staging table** | a photograph of the source file, untouched and all TEXT |
| **bulk command** | one call that inserts many rows, such as `executemany` |
| **SQL script** | a file of statements, run with `executescript` |
| **byte order mark** | three invisible bytes a spreadsheet writes at the start of a UTF-8 CSV |
| **profiling** | asking the data what is in it, before writing any cleaning rule |
| **parameter binding** | sending values separately from the SQL, with `?` or `:name` |

---

## Self-check

**1.** Name the one thing `executemany` gives you that a generated SQL script never can, and
say why it matters even when you remember to escape.

**2.** Your staging table has 40 rows and the file has 39 data rows. What is the fortieth, and
why is it in the table rather than skipped at the door?

**3.** A classmate says the orphan check returned 38 so the member file must be broken. What
do you tell them, and what do you run?

### Answers

**1.** Values that can never be parsed as SQL, because they travel on a different channel from
the statement. Escaping is a rule you have to apply correctly every time, in every place, and
the day you miss one the failure is either a syntax error or an injection. Binding makes the
question not arise.

**2.** A second copy of the header row, pasted into the middle of the file. It is staged
because staging does not decide anything: a row is loaded, quarantined, or counted, never
quietly discarded. Query 2 in the profile finds it and names its line number, which is what a
person needs.

**3.** Tell them the query is correct and the question was wrong. The two files write member
ids in different shapes, so a text comparison matches almost nothing. Run the shapes query,
`SELECT member_id, COUNT(*) FROM stg_loans GROUP BY member_id`, look at `RC0142` next to
`RC-0142`, then run the orphan check again with the same normalizing expression applied to
both sides. The real answer is one.
