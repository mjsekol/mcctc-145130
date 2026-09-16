# Integrity, Transactions, and Where a Rule Lives
---
## Slide 1: The kiosk refused it. So did the database.
- Both said no to the same bad row
- They were not saying no for the same reason
- One of them still says no next year
- Today is about which one
Speaker notes: Here is a front end that checks the roster before it writes anything, and it works. Here is the database refusing the same row. Two refusals that look identical in the terminal and are completely different in what they promise. That difference is the whole lesson.
Image: Two terminal messages side by side, one a friendly sentence, one a constraint name.
---
## Slide 2: Four kinds of integrity
- Entity: every row is identifiable, primary key
- Domain: every value is legal, CHECK and NOT NULL
- Referential: every pointer points at something, foreign key
- Transactional: all or nothing, commit and rollback
Speaker notes: Four names, and they are worth learning because they tell you which tool to reach for when somebody describes a problem. Somebody says two records got merged, that is entity. Somebody says a grade of thirteen got in, that is domain. Somebody says half a record saved, that is transactional.
Image: Four labelled boxes, each with the constraint keyword that enforces it.
---
## Slide 3: All three, doing their jobs
```
same gamertag twice          UNIQUE constraint failed: players.gamertag
grade 13                     CHECK constraint failed: grade_level BETWEEN 9 AND 12
a player who does not exist  FOREIGN KEY constraint failed
```
Speaker notes: Three bad inserts, three refusals. Notice which message tells you the most. The CHECK names the rule it broke, because you wrote that rule in a form a person can read. The foreign key message does not even name the column, which is an argument for putting a readable message in the layer above.
Image: None. This slide is code.
---
## Slide 4: Now delete two lines and run it again
```
same gamertag twice          UNIQUE constraint failed: players.gamertag
grade 13                     CHECK constraint failed: grade_level BETWEEN 9 AND 12
a player who does not exist  NO ERROR
```
Speaker notes: The two lines I deleted were the pragmas. The primary key still works. The CHECK still works. The foreign key does not, and there is no warning anywhere. It is off by default on every new connection, the setting belongs to the connection rather than the file, and a pragma inside a transaction is ignored, which is why you often set it twice.
Image: None. This slide is code.
---
## Slide 5: Recording a match is two things
- Insert the match, get its id
- Insert every player in the lineup
- Somebody types the same player twice
- The database refuses. Watch what is left behind.
Speaker notes: This is the front end doing something ordinary. A match row, then a lineup. Then the manager types vexcalibur twice by accident, which happens at a desk with people talking. The database refuses the second one and prints a sensible message. Predict what is in the database afterwards.
Image: A two step sequence diagram, match then lineup, with a red cross on the second lineup row.
---
## Slide 6: A match played by nobody
```
The database refused it: UNIQUE constraint failed: appearances.match_id, appearances.gamertag

   8  2027-03-17  Cedar Valley   Rocket League  2-1   0 players
```
Speaker notes: The message said refused. The match is in the database with zero players. One line caused this, and it has a comment above it that sounds sensible: save the match straight away so the match id is safe. That commit made the match permanent before a single lineup row was attempted.
Image: None. This slide is code.
---
## Slide 7: One indentation level fixes it
```python
with connection:
    cursor = connection.execute("INSERT INTO matches ...")
    for player in lineup:
        connection.execute("INSERT INTO appearances ...")
```
Speaker notes: with connection is not with open. It does not close the connection. It manages a transaction: commit if the block finishes, roll back if anything in it raises. Everybody who has used with open assumes otherwise exactly once, and this is the once.
Image: None. This slide is code.
---
## Slide 8: Two ON DELETE clauses, two beliefs
- CASCADE on the match: appearances are part of it
- RESTRICT on the player: appearances are a record
- Delete a match, three rows go quietly with it
- Delete a player, refused
Speaker notes: An appearance is part of a match. It has no meaning once the match is gone, so cascading is right. An appearance is not part of a player. It is a record of something that happened and it stays true after they leave the team. Deleting a person should never delete history.
Image: Two delete arrows, one dragging child rows away, one blocked by a barrier.
---
## Slide 9: Where a rule lives
- Front end: a message the person can act on
- Loader: rules needing context, and collecting reasons
- Schema: holds for every writer, forever
- Put the rule in the schema, the message in the front end
Speaker notes: Those three are not duplicates of each other. One is readable and true for one program. One is true for everybody and unreadable. You want both, and if you only get one, take the schema, because the day somebody loads a spreadsheet directly is the day you find out which rules were real.
Image: Three layers stacked, with the bottom one shaded as the one that always holds.
---
## Slide 10: What you are about to build
- Lab M04-02, you attack a working system four ways
- The write-ups are the deliverable, not the code
- Fifteen lines of changes, eight findings
- Steps three and seven with no AI
Speaker notes: Build one is lab M zero four dash zero two. You are not building anything new. You are going to break a working system four different ways, write down exactly what happened each time, and then move three rules from where they are to where they belong. Step four is the one that matters and I am not telling you what happens.
Image: A kiosk screen with a small program drawn sneaking past it straight into the database.
---
