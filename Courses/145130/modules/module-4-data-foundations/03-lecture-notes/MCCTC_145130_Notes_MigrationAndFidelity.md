# Migration, and How to Find Out What You Lost
## 145130 Applications of AI · Module 4 · Week 11, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W11_MigrationAndFidelity.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W11_MigrationAndFidelity.pptx)

**Every number below came from running `migrate.py --format all --verify` on the build
machine against the real fixture.**

---

## Why this is a whole lesson

"Convert the data to a new format" sounds like a file operation. It is not. **Every format can
hold some of what a relational database holds and not the rest, and the part it cannot hold
disappears with no error message.**

So the migration is half the job. The other half is loading the export back and counting what
came home. That second half is the part almost nobody does, and it is the graded part of your
project.

---

## What each format can say

| | rows | columns | nested arrays | null, distinct from empty | relationships |
|---|---|---|---|---|---|
| **relational database** | yes | typed | no, use a junction table | **yes** | **enforced** |
| **JSON** | yes | yes | **yes** | **yes**, `null` | described, not enforced |
| **CSV, one file per table** | yes | all text | no | **no** | described, not enforced |
| **CSV, one flat file** | one row per join | all text | no | no | **gone** |

**The column that decides most arguments is the null column.** A CSV field that is empty and
a CSV field whose value is unknown are the same three characters: nothing at all.

---

## Worked example 1: JSON round trips exactly

Export every table, load it back into a fresh database built from the same `schema.sql`, and
compare each table with a fingerprint: the rows sorted, hashed, with `NULL` hashed as
something the empty string cannot produce.

```
  json
    table         rows out  rows back  fingerprint                match
    members             14         14  ce94ac920c46 -> ce94ac920c46  yes
    items               14         14  cd36b32df771 -> cd36b32df771  yes
    tags                16         16  c877ad2234d7 -> c877ad2234d7  yes
    item_tags           30         30  1a7d9cdb1ba1 -> 1a7d9cdb1ba1  yes
    loans               33         33  1f8b3a7fc2b3 -> 1f8b3a7fc2b3  yes
    quarantine           6          6  30914396dc60 -> 30914396dc60  yes
    round trip: exact
```

JSON has `null`, so the seven loans that have not come back come back as `NULL` rather than
as empty strings. Nothing had to be agreed in advance.

---

## Worked example 2: one CSV per table, and the convention that saves it

Same export, one CSV per table. **CSV has no way to say "no value"**, so this export writes
the two characters `\N` for a null, which is the convention the bulk loaders in MySQL and
PostgreSQL use, and it says so in a `READ-ME-FIRST.txt` next to the files.

With the convention honoured:

```
  csv-tables, sentinel honoured
    round trip: exact
```

With an importer that did not read the note:

```
  csv-tables, importer that never read READ-ME-FIRST.txt
    table         rows out  rows back  fingerprint                match
    members             14         14  ce94ac920c46 -> 1861c72a06a2  NO
    items               14         14  cd36b32df771 -> cd36b32df771  yes
    tags                16         16  c877ad2234d7 -> c877ad2234d7  yes
    item_tags           30         30  1a7d9cdb1ba1 -> 1a7d9cdb1ba1  yes
    loans               33         33  1f8b3a7fc2b3 -> 11219c45bc75  NO
    quarantine           6          6  30914396dc60 -> 30914396dc60  yes
    round trip: NOT exact
```

**Read the row counts on the failing tables. Fourteen out, fourteen back. Thirty three out,
thirty three back.** Every row is there and two tables are different, because the loans that
had not come back now say they were returned on the two character string `\N`, and the member
with no recorded program now has a program called `\N`.

```
SELECT COUNT(*) FROM loans WHERE returned_on IS NULL   ->   0
```

Seven loans were still out. **The new database believes none are.**

---

## Worked example 3: the flat export, which loses four things and says nothing

One denormalized row per loan, everything joined on, the shape somebody produces when asked
for "the data as a spreadsheet".

```
  csv-flat, one denormalized row per loan
    what                                          in the database  in the file
    loans                                                      33           33
    members                                                    14           13   <- a member with no loan is not in the file
    catalog items                                              14           12   <- an item never borrowed is not in the file
    tags, as rows you can join on                              16            0   <- now text inside one column
    item to tag links                                          30            0   <- 76 tag names survive, repeated as text down the rows
    quarantine rows                                             6            0   <- the file has no place for them
    loans still out                                             7            7   <- only because you decided empty means null
    round trip: NOT exact, and nothing in the file says so
```

**Thirty three loans went out and thirty three came back.** That is the check most people run
and it is the check that passes.

What went missing:

1. **A member with no loans.** A join produces rows where the join matches. Somebody who has
   never borrowed anything has nothing to join to, so they are not in the file.
2. **Two items nobody has borrowed.** Same reason, and these two are the answer to "what did
   we buy that nothing has used", which is a question the advisor actually asked.
3. **The item-to-tag relationship.** Thirty rows became text inside one column, repeated on
   every loan of that item. The tag names are technically still there. **The ability to join on
   them is not.**
4. **The whole quarantine table.** A flat file of loans has no place for rows that are not
   loans, so the six rows that need a person are absent.

---

## The wrong version, and what it produces

The wrong version is the check, not the export.

```python
before = connection.execute("SELECT COUNT(*) FROM loans").fetchone()[0]
after = len(list(csv.DictReader(open("loans_flat.csv", newline="", encoding="utf-8"))))
print("migration ok" if before == after else "MISMATCH")
```

```
migration ok
```

**Every claim in that output is true and the migration lost four things.**

**Why it is tempting.** A row count is one line, it is the number everybody quotes, and when
it matches it feels like proof. It is proof of exactly one thing: that no row of the table you
counted went missing. It says nothing about columns, nothing about nulls, nothing about the
tables you did not export, and nothing about rows that were never eligible to be exported in
the first place.

**A fidelity check compares content, per table.** Row counts, plus a fingerprint that
distinguishes `NULL` from the empty string, plus a list of what each format cannot hold.

---

## Preserve, convert, migrate: three different words

The competency says "preserve, convert, or migrate". They are not synonyms.

- **Preserve** is keeping the original so that a mistake later is recoverable. Your `raw/`
  folder is preservation, and it is why the rule is never to edit it.
- **Convert** is producing the same data in another format.
- **Migrate** is moving to a new home and then *using* the new home, which means the old one
  stops being updated. That is the risky one, because after a migration the thing you lost is
  gone rather than merely absent from a copy.

**Never migrate without a round trip.** Convert, load back, compare, and only then stop
writing to the old system.

---

## Vocabulary

| Term | What it means |
|---|---|
| **fidelity** | how much of the meaning survived the move |
| **round trip** | export, load back, compare with the original |
| **denormalize** | flatten related tables into one, repeating values |
| **sentinel** | an agreed value that stands for something the format cannot say, such as `\N` for null |
| **lossy** | a conversion that cannot be reversed exactly |
| **fingerprint** | a hash of a table's content, used to compare two databases |

---

## Self-check

**1.** Your export and your reload both report 33 loans. Name two things that could still be
different, and the check that would find each.

**2.** Why does the flat CSV lose a member who has never borrowed anything, when nobody
deleted them?

**3.** A teammate says CSV is fine because you can agree that an empty field means null. What
is right about that and what does it cost?

### Answers

**1.** **Nulls turned into strings**, found by a fingerprint that hashes `NULL` differently
from the empty string, or by `SELECT COUNT(*) FROM loans WHERE returned_on IS NULL` on both
sides. **Types changed**, for example an item id with a leading zero read back as a number,
found by comparing the values themselves rather than the count. A count only ever proves the
count.

**2.** Because the export is a join, and a join produces one row per match. A member with no
loans matches nothing, so no row is produced for them. Nothing was deleted: the row was never
eligible. That is why "it was a join" is the first thing to check when a count comes out low.

**3.** It is right: a documented convention is exactly how CSV can carry nulls, and `\N` is a
real one that real loaders use. **It costs you the guarantee.** The convention lives in a
README, not in the file, so every importer has to know it and one that does not will load the
sentinel as data, silently. The fidelity check in this module runs the load both ways on
purpose, to show what the missing note costs.
