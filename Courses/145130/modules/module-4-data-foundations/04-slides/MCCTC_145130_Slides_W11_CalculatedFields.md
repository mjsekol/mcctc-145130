# Calculated Fields, and Reports Somebody Will Act On
---
## Slide 1: Nobody asked you for a database
- The advisor asked two questions
- She wants numbers she can put in front of a board
- The database is how you get there
- The report is the thing
Speaker notes: Read the brief again. She never says database. She says which equipment is being used, and what has not come back, and I do not want a number I cannot explain. Everything you built this week exists to produce one page. Today is that page.
Image: A database cylinder on the left, a one page report on the right, the report much larger.
---
## Slide 2: Three words in the competency
- Calculated field: worked out at query time, never stored
- Function: COUNT, SUM, AVG, ROUND, julianday, printf
- Form: one record, laid out for a person
- All three come out of one database
Speaker notes: A calculated field is a column that exists nowhere. It is worked out when the query runs from columns that are stored. That is why changing the rule means changing one query rather than reloading the data, and it is why the query is the documentation for the number.
Image: A stored column and a derived column drawn differently, with the derived one built from an expression.
---
## Slide 3: The anatomy of one
```sql
ROUND(AVG(CASE WHEN l.returned_on IS NOT NULL
               THEN julianday(l.returned_on) - julianday(l.checked_out_on)
          END), 1) AS avg_days_out_returned
```
Speaker notes: Four things at once. julianday turns a date string into a number so it can be subtracted, because SQLite has no date type. CASE with no ELSE returns null. AVG skips nulls. So this averages only the loans that came back, in one pass, without a second query.
Image: None. This slide is code.
---
## Slide 4: Check one number by hand, first
```
fabrication: 9 returned loans
6 + 6 + 6 + 7 + 6 + 5 + 8 + 13 + 6 = 63
63 / 9 = 7.0
```
Speaker notes: Nine loans came back, here are the nine durations, they add to sixty three, and sixty three over nine is seven point zero exactly. The query agrees. Do this before you write the query, not after. A calculated field checked against your own program's output only proves the program agrees with itself.
Image: None. This slide is code.
---
## Slide 5: The pattern you will use most
- SUM of CASE WHEN condition THEN 1 ELSE 0 END
- Counts matching rows inside the same pass
- Replaces running a second query and subtracting
- Use 100.0 not 100, or you get zero
Speaker notes: This one pattern gives you late returns, still out, overdue now, and the rate, all in the same statement. And write one hundred point zero, because two integers divided in SQLite give an integer. Fourteen over twenty four is zero. One point zero anywhere in the expression fixes it.
Image: A single query with four highlighted CASE expressions feeding four columns.
---
## Slide 6: Round at the edge, never in the middle
- printf formats the answer for a person
- Rounding each row before adding is a wrong total
- And the wrongness is untraceable
- The date is a parameter, not the clock
Speaker notes: Round for display, not while you are calculating. And overdue is a claim about a moment, so the as of date is an input. With the clock in the query the same command gives two answers on two days, no test can check a number, and a number you showed somebody last week cannot be reproduced.
Image: Two calculation chains, one rounding at every step and drifting, one rounding once at the end.
---
## Slide 7: Trap one, the row that is not a row
```
robotics   loans 3   still out 3   value out $754.75
```
Speaker notes: Robotics has three loans and two of them are still out. The report says three, and seven hundred and fifty four dollars out the door instead of six hundred and fifty eight. There is a piece of equipment nobody has ever borrowed, and the LEFT JOIN made it a row with every loan column null, so returned is null was true for a thing sitting on a shelf.
Image: None. This slide is code.
---
## Slide 8: COUNT star counts rows, COUNT column counts values
```sql
SUM(CASE WHEN l.loan_id IS NOT NULL
              AND l.returned_on IS NULL THEN 1 ELSE 0 END) AS still_out
```
Speaker notes: They are the same number until a LEFT JOIN produces a row with no values in it. Guard on the loan's own key and the number goes back to two. This exact defect is in one of the labs this week and in a Gate 2, because it produces a wrong number and no error, which is the shape of the whole module.
Image: None. This slide is code.
---
## Slide 9: Trap two, the guard the formatter undoes
- printf of a null prints 0.00 in SQLite
- ROUND of a null stays null
- One over zero is null, not an error
- A ratio of zero is a claim, not an absence
Speaker notes: You guard a division with NULLIF, you get a proper null, and then printf turns it back into a number that looks real. A kill to death ratio of zero point zero zero says this player plays and never scores. Every step between the data and the page is a place a null can become a number.
Image: A null value travelling through a pipeline and coming out the other end as 0.00.
---
## Slide 10: What you are about to build
- Four queries and a one record form
- Column names come from the query itself
- Both traps spring on you in steps seven and eight
- Lab M04-04, and step one is arithmetic on paper
Speaker notes: Build one is lab M zero four dash zero four. Four calculated field queries against the esports database, plus a player record form. Step one is adding up three rows on paper, and it is the step people skip. Steps seven and eight are the two traps, and I am not telling you what happens.
Image: A report page and a single record form side by side, both labelled with the same query name.
---
