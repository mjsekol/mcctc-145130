# Constraints, Requirements, and What Crosses the Boundary
---
## Slide 1: "The service should respond quickly"
- Cannot be tested
- Cannot be reviewed
- Cannot be failed
- Which means it is not a requirement
Speaker notes: Read that sentence. It sounds like a requirement and it is not one, because there is no way anybody could tell you that you missed it. A design with no numbers in it cannot be wrong, and that sounds like an advantage. It is the opposite of one. Every number you write down today is a number somebody can check on Friday.
Image: A requirements document with one vague line highlighted in accent red and a question mark beside it.
---
## Slide 2: Three things people mix up constantly
- Constraint: you are not allowed to change it
- Processing requirement: a number you chose and can defend
- I/O requirement: a field, its type, its range
- The test: can you change it by deciding to
Speaker notes: Three different things. A constraint you did not choose, like the model running locally because commercial developer APIs need users to be eighteen. A processing requirement is a number you picked and can defend. An I O requirement names a field. And the test that sorts them: can you change it by deciding to. If no, constraint. If yes and it is a number, requirement.
Image: Three labelled boxes with the sorting question as a decision diamond above them.
---
## Slide 3: A constraint with no reason gets broken
```
C1  model runs locally         those APIs require users to be 18 or older
C2  no credential anywhere     a local model needs none, and one that
                               exists can be leaked
C5  C# targets net8.0          lab machines may have an older SDK
C8  one model server per room   there is not a graphics card per seat
```
Speaker notes: Every constraint gets a reason next to it. A constraint with no reason is a rule somebody breaks the first time it is inconvenient, and they are right to. Look at C five. That one has a practical consequence you will hit tomorrow: on SDK ten, dotnet new sln writes a dot slnx file that an older SDK cannot open, so you pass the format flag.
Image: None. This slide is code.
---
## Slide 4: Now add the third column
- What it buys you
- What it costs you
- A list with only the first is marketing
- Local model: no key, and a weaker model
Speaker notes: Two columns is not enough. Every constraint buys you something and takes something away, and a constraint list that only says what you gained is marketing rather than design. A local model buys you no account, no key, nothing leaving the building. It costs you a smaller model that follows output instructions less reliably. Both of those are true and both belong in the document.
Image: A balance scale, navy, with a short gain list on one side and a short cost list on the other.
---
## Slide 5: These two numbers, against each other
```
P5  worst case for one request   timeout x attempts    20s x 2 = 40s
P6  the caller's own timeout     larger than P5        45s
```
Speaker notes: This is the pair people get wrong, and it is the most common way an integration in this lab is built wrong. Your service is allowed to take its timeout multiplied by its attempts. If your application gives up sooner, the labelled fallback your service was about to hand you never arrives. Write both numbers down, in both programs, and check them against each other out loud on Friday.
Image: None. This slide is code.
---
## Slide 6: Describing a field is not specifying it
- Describing: the text the user wants summarised
- Specifying: a string, 1 to 4000 characters, after cleaning
- Plus the fourth column: what happens when it is wrong
- If that column is empty you have not finished thinking
Speaker notes: Four columns per field. Name, type, allowed range, and what happens when it is wrong. That fourth column is the one people leave blank, and it cannot actually be blank, because something does happen. If you did not decide, the answer is whatever the language does by default, and the language does not know what your program is for.
Image: A four-column field table with the fourth column empty and circled in accent red.
---
## Slide 7: Checking before you work costs nothing
```
python contract_probe.py long-prompt

  HTTP status    400
  source       none
  elapsed_ms   0
  error        {"kind": "prompt_too_long", "message": "the prompt is 4001 charac...
```
Speaker notes: Look at elapsed underscore ms. Zero. The service did not call the model, did not wait, and did not spend anything. Checking input before you do work with it is not politeness. It is the difference between a wrong request costing nothing and a wrong request costing twenty seconds of somebody's period.
Image: None. This slide is code.
---
## Slide 8: Three missing limits, three silent failures
```
prompt   no cap     40,000 characters pasted, the model takes forever
minutes  no range   the model returns 600, timer runs ten hours
label    no list    the model invents "facilities", database accepts it
```
Speaker notes: None of those three crashes. All three produce output. The last one is the worst, because the row goes into your database and the report that groups by label quietly has a group nobody built a page for, and you find out in three weeks. This is the same shape as every dangerous bug in this program: it does not crash.
Image: None. This slide is code.
---
## Slide 9: Why people skip the specification
- You already know what the field is for
- Writing the range feels like writing the obvious
- The person who does not know is you in Week 15
- And your partner, while you are at a competition
Speaker notes: Be honest about this one. On the day you write it, everybody on your team understands the field, so writing down its range feels like writing down something obvious. The person who does not understand it is you in Week fifteen, and your partner in Week fourteen while you are at BPA Regional, and whoever reads this repository next semester.
Image: A calendar strip showing Weeks 13, 14, 15 with the same field name appearing in each and a different person reading it.
---
## Slide 10: What you are about to build
- Finish Lab M05-01 with the probe, six cases
- Then your own constraint list, with all three columns
- Your own I/O specification, field by field
- Both numbers: your worst case, your caller's timeout
Speaker notes: Build one finishes the contract trace with the probe, six cases, including the two the service refuses. Build two is your own constraint list and your own I O specification. The one thing I will check first on Friday is whether your caller's timeout is bigger than your service's worst case, because if it is not, nothing else in your design gets to matter.
Image: A student's constraint list on screen beside a terminal running the probe, both in navy and accent blue.
