# Tables, Keys, and the Fact Written Down Twice
---
## Slide 1: One player, two names, same person
- nightowl99 is Jamal Petrov on line 4
- nightowl99 is Jamaal Petrov on line 27
- Key on the name and you have nine players
- Key on the gamertag and you have eight
Speaker notes: Same account, same person, two spellings, because a human typed it twice. Your entire schema turns on which of those two columns you pick as the key, and the file is telling you the answer if you look at it. Today is about picking keys and then living with the choice.
Image: Two CSV lines side by side with the two spellings circled and the identical gamertag underlined.
---
## Slide 2: The words, once, properly
- Table is one kind of thing
- Row is one of that thing
- Column is one fact about it
- Primary key identifies exactly one row
- Foreign key points at a row elsewhere
Speaker notes: Five words and you know four of them already. The one worth slowing down on is primary key, because a key is a promise about the real world rather than a detail about storage. If the promise is ever false, the key is wrong, and the database will tell you the first time it happens.
Image: One table drawn with a row highlighted and one cell highlighted inside it.
---
## Slide 3: The question that picks a key
- Which value stays the same if they change their mind
- A gamertag is chosen once
- A name is typed every time
- The file already proves which is stable
Speaker notes: One question. Which of these two values would still be the same tomorrow if the person changed their mind about the other one. A gamertag is an account. A name is typed by whoever is at the desk. You do not have to guess which is stable here because the file contains the evidence.
Image: A tag tied to an object, versus a sticky note that has been rewritten twice.
---
## Slide 4: A match has many players, a player has many matches
```sql
CREATE TABLE appearances (
    match_id INTEGER NOT NULL REFERENCES matches (match_id),
    gamertag TEXT NOT NULL REFERENCES players (gamertag),
    role     TEXT NOT NULL,
    PRIMARY KEY (match_id, gamertag)
);
```
Speaker notes: Neither table can hold the other, because a column holds one value. So the relationship gets its own table. Read that primary key out loud: one row per player per match. And notice where role lives. Role depends on the player and the match together, which is why it is here and not on players.
Image: None. This slide is code.
---
## Slide 5: What does this fact depend on
- Score depends on the match
- Grade depends on the player
- Role depends on both together
- Answer that and you have normalized it
Speaker notes: That is normalization without the formal definitions. Every fact gets written down once, and where it goes is decided by what it depends on. If you can say which of the three a fact depends on, you are finished. You do not need third normal form to do this week's work.
Image: Three facts with arrows pointing to the table each one belongs in.
---
## Slide 6: What repetition costs, exactly
```
kettlecorn appears in 3 rows of the flat file
UPDATE players SET grade_level = 12 WHERE gamertag = 'kettlecorn';
1 row changed
```
Speaker notes: Kettlecorn moved up a grade. In the flat file that is three rows to edit and a fourth time somebody will miss one. In the normalized version it is one statement and one row. That is the whole argument for normalization in two lines, and it is not about elegance, it is about one place to change one thing.
Image: None. This slide is code.
---
## Slide 7: An array does not fit in a column
- The catalog gives four tags per item
- One column means LIKE and hope
- Two tables means a question with an exact answer
- Renaming a tag stops being a search and replace
Speaker notes: The makerspace catalog hands you a tags array. Put it in one column and every item that needs training becomes a LIKE query that also matches a tag called training optional the day somebody adds one. Two tables cost you a join. They buy you a question you can answer exactly, which the report asks.
Image: A JSON item with its tags array, and beside it two small tables joined.
---
## Slide 8: Here is the wrong one
```sql
CREATE TABLE season (
    played_on TEXT, opponent TEXT, our_score INTEGER,
    gamertag TEXT, player_name TEXT, grade_level INTEGER,
    role TEXT, kills INTEGER, deaths INTEGER
);
```
Speaker notes: This is the CSV with a CREATE TABLE in front of it, and it is what you get if you ask a model for a table for this file, because it is literally what you asked for. It loads. Every query works. Predict what goes wrong before I show you.
Image: None. This slide is code.
---
## Slide 9: Two answers, one person, no error
```
SELECT DISTINCT grade_level FROM season WHERE gamertag = 'kettlecorn';
[(11,), (12,)]
```
Speaker notes: No primary key, so the duplicate row goes in. The match is repeated on every player row, so two rows can disagree about the score. The grade is repeated, so one person is in two grades at the same time. Nothing raised. The table is perfectly happy and you now have two answers to one question about one person.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Three tables out of twenty eight flat rows
- Four key decisions, written down, no AI
- Two deliberate breaks in step eight
- Then one UPDATE that touches one row
Speaker notes: Build one is lab M zero four dash zero one. Step three is the four key questions and it is the part of the lab that is not typing. Step eight breaks a foreign key with the pragma on and then with it off, and you write down both results. The second one is the sentence you carry into Friday's Gate 2.
Image: A flat spreadsheet with an arrow into three connected tables, keys marked.
---
