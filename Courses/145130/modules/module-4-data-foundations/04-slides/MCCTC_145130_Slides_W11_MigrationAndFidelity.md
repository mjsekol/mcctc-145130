# Migration, and How to Find Out What You Lost
---
## Slide 1: Thirty three rows out, thirty three rows back
- The row count matches exactly
- The migration lost four things
- Nothing in the file says so
- This is the check most people run
Speaker notes: Here is an export of the makerspace loans. Thirty three rows went out and thirty three came back, so the migration is fine. It is not fine. It lost two catalog items, a member, every tag relationship, and every quarantined row. A row count is the check that passes.
Image: A terminal showing 33 equals 33 with a green tick, and four small items falling off the side of the screen.
---
## Slide 2: Convert is half the job
- Every format holds some of what a database holds
- The rest disappears with no error
- So export, then load it back, then compare
- Nobody skips the first half
Speaker notes: Migrate the data to a new format sounds like a file operation. It is not. Each format can say some things and not others, and the things it cannot say vanish quietly. The half everybody does is the export. The half that is graded is loading it back and counting what came home.
Image: An arrow out to a file and an arrow back, with a magnifying glass on the return arrow.
---
## Slide 3: What each format can actually say
- JSON has null, nesting, and arrays
- CSV has rows and columns and all text
- CSV has no way at all to say no value
- A flat file has no relationships left
Speaker notes: The column that decides most arguments is the null column. In a CSV, a field that is empty and a field whose value is unknown are the same thing: nothing at all. And the seven loans that have not come back are exactly the rows that difference matters for.
Image: A four by four grid of formats against capabilities, with ticks and crosses.
---
## Slide 4: JSON round trips exactly
```
  json
    members    14   14  ce94ac920c46 -> ce94ac920c46  yes
    loans      33   33  1f8b3a7fc2b3 -> 1f8b3a7fc2b3  yes
    round trip: exact
```
Speaker notes: A fingerprint is a hash of every row, sorted, with null hashed as something the empty string cannot produce. Same rows, same fingerprint, both ways. JSON has null natively, so nothing had to be agreed in advance and nothing was lost.
Image: None. This slide is code.
---
## Slide 5: One CSV per table, with a convention
```
  csv-tables, sentinel honoured                    round trip: exact
  csv-tables, importer that never read the note
    members    14   14  ce94ac920c46 -> 1861c72a06a2  NO
    loans      33   33  1f8b3a7fc2b3 -> 11219c45bc75  NO
```
Speaker notes: Same export both times. The only difference is whether the importer knew that backslash N means null. Read the row counts on the failing lines: fourteen out, fourteen back, thirty three out, thirty three back. Every row is there and two tables are different.
Image: None. This slide is code.
---
## Slide 6: Seven loans were still out. Now none are.
- The sentinel loaded as data, not as null
- returned_on is now the two characters backslash N
- The count of rows is perfect
- The meaning of two tables is gone
Speaker notes: Seven pieces of equipment have not come back, and the new database believes every item is on the shelf. The convention was written down, in a file next to the export, and an importer that did not read it produced a database that passes every count and answers one question wrongly.
Image: Seven equipment icons marked out, then the same seven marked returned, with a query result of zero.
---
## Slide 7: The flat export, and what it costs
- A member with no loan is not in the file
- Two items nobody borrowed are not in the file
- Thirty tag links became text in one column
- Six quarantined rows have nowhere to go
Speaker notes: A flat export is a join, and a join produces rows where the join matches. Somebody who has never borrowed anything matches nothing, so they are not there. Nothing was deleted. The row was never eligible, and that is the first thing to check when a count comes out short: ask whether the export was a join.
Image: A denormalized spreadsheet with three small callouts pointing at things that are not in it.
---
## Slide 8: The check that looks like proof
```python
before = connection.execute("SELECT COUNT(*) FROM loans").fetchone()[0]
after  = len(list(csv.DictReader(open("loans_flat.csv"))))
print("migration ok" if before == after else "MISMATCH")
```
```
migration ok
```
Speaker notes: Every claim in that output is true, and the migration lost four things. A row count proves exactly one thing: that no row of the one table you counted went missing. It says nothing about columns, nothing about nulls, and nothing about the tables you did not export.
Image: None. This slide is code.
---
## Slide 9: Preserve, convert, migrate are three words
- Preserve keeps the original so mistakes are recoverable
- Convert produces the same data elsewhere
- Migrate means the old system stops being updated
- Never migrate without a round trip
Speaker notes: Your raw folder is preservation, and that is why the rule is never to edit it. Migration is the risky one, because after a migration the thing you lost is gone rather than merely absent from a copy. Convert, load back, compare, and only then stop writing to the old system.
Image: Three arrows labelled with the three words, the third one with the old system greyed out.
---
## Slide 10: What you are about to build
- Two export formats from your own database
- Load both back into a fresh empty schema
- Compare table by table, not by row count
- At least one format must lose something, and you say what
Speaker notes: Build two is the migration stage of your project, and the requirement is not only to export. Load it back into a database built from the same schema file and compare each table. At least one of your formats has to lose something, and the README has to say exactly what and why. That is the graded part.
Image: One database, two export files, both arrows returning into a second empty database with a comparison line between them.
---
