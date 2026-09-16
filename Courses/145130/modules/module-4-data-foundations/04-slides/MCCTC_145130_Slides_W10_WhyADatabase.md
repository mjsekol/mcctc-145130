# Why a Database and Not a Pile of Files
---
## Slide 1: Two programs, one file, two answers
- Same CSV, same question, same afternoon
- Python says vexcalibur scored 38
- SQL says 32
- Neither program is broken
Speaker notes: Here are two programs. Same file, same question, run one minute apart. One says thirty eight and one says thirty two. Nobody made a typo and neither program has a bug in it. By the end of these fifteen minutes you will be able to say which number is right and, more useful, why the other one was ever produced.
Image: Two terminal windows side by side, one showing 38 and one showing 32, both looking equally confident.
---
## Slide 2: The loop counted every row
```python
for row in csv.DictReader(handle):
    totals[row["gamertag"]] += int(row["kills"])
```
Speaker notes: This is the Python. It opens the file, walks every row, and adds up the kills. It did exactly what it was told. One row in that file is in there twice, because somebody pasted an export under another export, and nothing in this loop has any reason to notice. Six kills counted twice. Thirty eight.
Image: None. This slide is code.
---
## Slide 3: The rule refused the second copy
```sql
CREATE TABLE appearances (
    match_id INTEGER NOT NULL,
    gamertag TEXT NOT NULL REFERENCES players (gamertag),
    PRIMARY KEY (match_id, gamertag)
);
```
Speaker notes: This is the SQL side. Look at the last line. One player appears at most once in one match. That is not a data structure decision, it is a claim about the real world, and the database enforces it for every program that ever writes to this table. The duplicate never got in. Thirty two.
Image: None. This slide is code.
---
## Slide 4: A database is data plus rules
- A spreadsheet holds data
- Your Python program holds rules
- A database holds both, for every writer
- The rules outlive the program that wrote them
Speaker notes: That is the whole idea and it is worth saying slowly. A spreadsheet holds data. A validating Python program holds rules. A database holds both in one place, and the rules apply to every program that ever connects, including the one your teammate writes next year without reading yours.
Image: Three boxes labelled spreadsheet, program, database, with the database box containing both of the other two.
---
## Slide 5: Three things a DBMS gives you
- Rules that survive a second writer
- A query language, so you describe the answer
- Transactions, so a crash never leaves half a record
Speaker notes: Three things, and the first is the one this week is about. The second is why your report is going to be six lines instead of sixty. The third arrives on Thursday, when we record a match and its lineup and somebody types the same player twice.
Image: None needed.
---
## Slide 6: Front end and back end
- The database is the back end
- A kiosk, a report, an export are front ends
- Rules that must always be true live in the back end
- A front end rule is true for its own users only
Speaker notes: Two words you will use for the rest of this course. The back end holds the records and the rules. A front end is anything a person looks at. On Thursday you will write fifteen lines that go around the front end entirely, and you will watch what the database does about it. Today, hold the sentence.
Image: Three front ends drawn as screens, all arrows pointing into one database cylinder.
---
## Slide 7: Watch this
```python
connection.executescript("""
    CREATE TABLE appearances (
        gamertag TEXT NOT NULL REFERENCES players (gamertag))""")
connection.execute("INSERT INTO appearances VALUES ('ghost_player')")
print("rows:", connection.execute("SELECT COUNT(*) FROM appearances").fetchone()[0])
```
Speaker notes: There is no player called ghost player. The REFERENCES clause right there says there has to be one. Predict what this prints before I press enter. Hands up for an error message.
Image: None. This slide is code.
---
## Slide 8: One row, no error
```
rows: 1
```
Speaker notes: No error. No warning. The clause is in the schema, spelled correctly, and it enforced nothing. SQLite does not check foreign keys unless you switch them on, and the setting belongs to the connection, not to the file. Every program has to ask for it, every time. The default is off.
Image: None. This slide is code.
---
## Slide 9: A constraint you did not switch on is a comment
- PRAGMA foreign_keys returns zero on a new connection
- Reading the schema tells you what somebody meant
- Running the pragma tells you what is true
- This costs a class period every year
Speaker notes: Write that first sentence down. It is the one sentence from today that shows up in a lab, in Friday's Gate 2, and in the module exam. Reading a schema tells you what somebody intended. There is exactly one command that tells you what is actually being enforced, and you will run it in every lab this week.
Image: A schema file with a REFERENCES line highlighted, next to a terminal showing the pragma returning zero.
---
## Slide 10: What you are about to build
- Three tables out of one flat spreadsheet
- You choose every key and defend it
- Break a foreign key on purpose, twice
- Lab M04-01, forty minutes, no AI for step three
Speaker notes: Build one is lab M zero four dash zero one. The esports season, twenty eight flat rows, into three connected tables. Step three is four questions about keys and you answer them on paper with no model. That is the thinking this whole module rests on and it takes about eight minutes. Step eight is where you comment out the pragmas and watch the bad row go in.
Image: A flat spreadsheet on the left, three connected tables on the right, an arrow between them.
---
