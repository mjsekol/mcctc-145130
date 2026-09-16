# Ridge Creek Makerspace fixtures

Every file here is invented. There is no Ridge Creek Makerspace, no real member, no real
loan, and no real equipment purchase. Nothing here was scraped from a live site. You use
invented data for the same reason the anchor stack does: personal data does not enter an
AI tool in this program, and that includes the sample data you test with.

You use one dataset for the whole module so that the work compounds. Week 10 designs a
schema for it, Week 11 loads and reports on it, and Week 12 makes the handbook queryable
beside it.

---

## What is here

| Path | Format | Rows or files | What it is |
|---|---|---|---|
| `raw/loans_spring.csv` | CSV, UTF-8 with a byte order mark, CRLF line endings | 39 data rows | the loan log, exported from the front desk spreadsheet |
| `raw/catalog.json` | JSON, nested | 14 items | the equipment catalog, exported from the kiosk |
| `raw/members_legacy.txt` | pipe delimited text with comment lines | 14 members | the last export from the old sign-in kiosk |
| `handbook/` | Markdown | 8 documents | the makerspace handbook, for the Week 12 retrieval work |

---

## `raw/loans_spring.csv`

Columns: `loan_id`, `member_id`, `item_id`, `checked_out`, `due`, `returned`, `notes`.

**This file is messy on purpose, and every kind of mess in it is one you will meet in a
real export.** Do not fix the file. Fix it in code, and write down what you decided.

What is in it, so you know the mess is deliberate rather than a broken fixture:

- A **byte order mark** at the start, which is what a spreadsheet writes when it saves as
  CSV. Read it with `encoding="utf-8-sig"` or your first column name will not be
  `loan_id`.
- A **repeated header row** in the middle, where somebody pasted a second export under
  the first.
- A **blank row**.
- **Member ids in four shapes**: `RC-0142`, `rc-0151`, ` RC-0143 ` with spaces, and
  `RC0142` with no hyphen.
- **Two date formats**: `2027-03-07` and `03/07/2027`.
- A **word in a date column**: one `returned` value is `still out`.
- An **empty `returned`**, which legitimately means the item has not come back.
- A **duplicate `loan_id`** with a different return date on the second copy.
- A **`member_id` that is in no member source** and an **`item_id` that is in no
  catalog**. Those two are your referential integrity cases.
- A row whose **due date is before its checkout date**, and a row whose **return date is
  before its checkout date**.
- Notes containing commas and a pair of embedded double quotes, so `split(",")` will
  give you the wrong answer and the `csv` module will give you the right one.

**Nothing in this file is unreadable garbage.** Every problem row is a row a person could
resolve by asking somebody. That is the point: your pipeline decides which rows a person
has to look at, rather than deciding to silently drop them.

## `raw/catalog.json`

A single object with a `catalog_version`, a `generated_by` note, and an `items` array.
Each item carries a `tags` array and a nested `purchase` object.

Those two nested shapes are the reason this file is in the module. A table has one value
per field. An array and a nested object do not fit in one field without losing something,
and deciding what to do about that is a schema decision, not a formatting detail.

Two items, `EQ-0121` and `EQ-0151`, never appear in the loan log. They are there so that
"items that were never borrowed" is a question your report can answer.

## `raw/members_legacy.txt`

Pipe delimited, with three comment lines at the top that start with `#`. Ids have no
hyphen. Dates are `mm/dd/yyyy`. One member has an empty `program`, and one member never appears in the loan log at all. Two members have
program names that mean the same thing and are spelled differently, which is a
normalization decision you have to make and defend.

## `handbook/`

Eight short Markdown documents. They are the document set you chunk, embed, and query in
Week 12.

**Two of them disagree.** `02-loan-policy.md` says a member may hold two items at one
time. `07-electronics-bench.md` says you may sign out up to three items from the
electronics bench. A retrieval system that returns one of those and not the other gives
a confident answer that is missing half the picture. Finding that is part of the Week 12
work, and it is the honest version of "retrieval is traceable to a source": the source is
traceable, and the source set can still contradict itself.

---

## Rules for using these files

1. **Do not edit anything in `raw/` or `handbook/`.** Copy them, read them, load them.
   Every lab and the project assume the mess is still there.
2. **Do not add a real person to any of them.** If you extend the dataset, invent.
3. **Fix data in code, not by hand.** A fix you made by hand in a spreadsheet is a fix
   nobody can reproduce, which means your pipeline is not a pipeline.
