# Three Ways to Import, and Why You Stage First
---
## Slide 1: Thirty eight of thirty nine loans have no member
- The query is correct
- The count is reproducible
- The member file has all fourteen of them
- Nothing is broken
Speaker notes: Here is a real result from your fixture. Thirty eight of thirty nine loans point at a member who does not exist. Every one of those numbers is true, the query is right, and the member file is fine. Work out what happened and you have understood today.
Image: A terminal showing the number 38 with a query above it, and a member file open beside it.
---
## Slide 2: The two files write the same id differently
- The loans file says RC-0142
- The member file says RC0142
- A join compares values, not meanings
- Two spellings are two values
Speaker notes: One hyphen. That is the whole thing. A join compares characters, and two values that mean the same person and are written differently are two different values. SQL will tell you so with a completely straight face, and the number it gives you will be correct and useless.
Image: Two id strings stacked with the hyphen highlighted in one of them.
---
## Slide 3: Normalize both sides and ask again
```
Orphan members, raw text join        38
Orphan members, both sides normalized 1   RC-0199
```
Speaker notes: One. There really is one loan pointing at a member who is in no source, and that is a row somebody has to go and ask about. The other thirty seven were a question nobody meant to ask. This pair of queries is the reason staging is worth a whole lesson.
Image: None. This slide is code.
---
## Slide 4: A staging table is a photograph
```sql
CREATE TABLE stg_loans (
    source_row  INTEGER NOT NULL,
    loan_id TEXT, member_id TEXT, item_id TEXT,
    checked_out TEXT, due TEXT, returned TEXT, notes TEXT
);
```
Speaker notes: Every column is TEXT and nothing is converted. Int of eleven and int of space eleven space are both eleven, and one of them was telling you a volunteer typed a space. The moment you convert you have thrown the evidence away. And every row carries its line number, so a problem can be handed to a person with a place to look.
Image: None. This slide is code.
---
## Slide 5: Route one, the bulk command
- executemany, one call, many rows
- Statement prepared once and reused
- Values travel separately from the SQL
- That second property is why it is the default
Speaker notes: This is the one you use unless you have a reason not to. Fast because the statement is prepared once. Safe because nothing in a value can ever be read as SQL, since the value never touches the statement. That is not a bonus feature, it is the whole argument.
Image: One arrow carrying a statement and a separate arrow carrying a stack of rows.
---
## Slide 6: Route two, the generated SQL script
```sql
INSERT INTO stg_members (source_row, member_id, full_name, grade_level, program, joined)
VALUES (4, 'RC0142', 'Amara Delgado', '11', 'Engineering Technology', '09/02/2026');
```
Speaker notes: A text file full of statements, run all at once. People do this when the database is on another machine, or when the load has to be checked into a repository and reviewed like code. A dot sql file is portable in a way a Python program is not.
Image: None. This slide is code.
---
## Slide 7: And here is what it costs you
- Every value has to be escaped, by you, every time
- This fixture has no apostrophe in any name
- So your bug will not show up today
- It shows up when O'Brien joins
Speaker notes: One doubled quote character is the only thing between you and a broken load. Forget it and the first name with an apostrophe ends the SQL string early. Nobody in this fixture has one, which is exactly why this is dangerous: the bug ships, works for months, and fails in front of somebody waiting for a report.
Image: A name with an apostrophe, and the SQL string underneath it visibly ending in the wrong place.
---
## Slide 8: Route three is always the first half
- json, csv, or your own parser
- Then route one or route two
- The file is never already SQL
- Keep the nesting as it arrived for now
Speaker notes: Reading the format is not an alternative to the other two, it is the first half of both. And notice what staging does with the tags array: it joins it into a string, which is the opposite of what Tuesday of Week 10 told you. That is on purpose. Splitting it is a schema decision and decisions come later.
Image: Three file icons flowing into one reader box and out into one loader box.
---
## Slide 9: The byte order mark, which costs everybody once
```
'﻿loan_id'
KeyError: 'loan_id'
```
Speaker notes: Three invisible bytes a spreadsheet writes at the front of the file. Your first column is not called loan id, and the error points at a line that reads perfectly. The fix is encoding utf dash eight dash sig, and strip does not remove it, because as far as Python is concerned it is not whitespace.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Lab M04-03, three importers, one staging database
- Then fourteen questions asked of the data
- Nine of them you write
- The answers go into your project README
Speaker notes: Build one is lab M zero four dash zero three. Two of the three importers are yours to write. Then you write nine profiling questions, and questions eight and nine are the pair you watched a moment ago. What you find today is the Measure step of your project and it is due at the end of build two.
Image: Three source files flowing into three staging tables, with a question mark above them.
---
