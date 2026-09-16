# The Peer Walkthrough
---
## Slide 1: Twelve minutes, and both teams wrote "looks good"
- Nothing was found
- Both teams now believe their design was reviewed
- That is worse than not doing it at all
- A review that finds nothing is used as proof there was nothing
Speaker notes: Two teams sit down, both open their code, one says this is the client and this bit handles the errors, the other says yeah that looks good. Twelve minutes. Nothing found. And now both teams believe their design was reviewed, which is worse than not doing it, because a review that found nothing gets used as evidence that there was nothing to find.
Image: Two students at one screen with a clock showing twelve minutes and an empty findings sheet.
---
## Slide 2: The author reads. The reviewer interrupts.
- Not a demo. In a demo you show the parts that work.
- Every line, in order, including the ones you would skip
- Three roles: author, reviewer, recorder
- Cheapest defect-finding technique anybody has measured
Speaker notes: A walkthrough is the author reading their own work out loud to somebody whose job is to interrupt. It is not a demo. In a demo you show the parts that work. Here you read every line in order including the parts you would not have shown. It needs no tools, no environment, and no running code. One other person and forty minutes.
Image: Three role cards in a row, author, reviewer, recorder, each with one sentence of job description.
---
## Slide 3: The rule that makes it work
- The author does not defend
- "I do not understand this" means write it down
- Not explain it out loud
- The explanation is the thing missing from the document
Speaker notes: One rule. The author does not defend. When your reviewer says I do not understand this part, your only job is to write that down. Not to explain it. The explanation is the thing that is missing from the document, and saying it out loud makes the problem disappear from the room without removing it from the work. This is hard and everybody does it. Your partner should say you are defending, and you should stop.
Image: A speech bubble being crossed out and replaced with a pen writing on a findings sheet, accent red to accent blue.
---
## Slide 4: The script, and the order is the design
```
0-3    author states the task, the shape, what they are least sure of
3-10   DOCUMENTS FIRST. The I/O spec, field by field.
10-18  the dataflow diagram. What is checked at each boundary.
18-26  then the code. Failure paths only. Not the happy path.
26-33  reviewer drives. Author does not touch the keyboard.
33-40  findings read back, then one decision each
```
Speaker notes: Documents before code, always. If you start with code, everybody reads code, finds three small things, and the hour is gone. The expensive defects are disagreements between the documents and the code, and you only see those by holding one against the other. And from minute twenty six the author is off the keyboard, because you know where not to click.
Image: None. This slide is code.
---
## Slide 5: Five questions that always find something
```
1  Show me the line that does this requirement.
2  What happens if I give it nothing?
3  Which of these two numbers is bigger?
4  What does the person see when the model is off?
5  Read me this comment, then the line under it.
```
Speaker notes: Give these to your reviewer before you start. Number three takes ten seconds and finds a blocker: their client timeout against their service timeout times its attempts, said out loud. Number five is the hardest defect in this module, because a comment that describes what a number should do sitting above a number that does the opposite survives every casual review.
Image: None. This slide is code.
---
## Slide 6: A finding has three parts
- Where it is
- What is wrong or unclear
- How bad it is: blocker, major, minor
Speaker notes: A finding is something specific somebody can act on. Where it is, what is wrong, and how bad. Blocker means it does not work or two documents contradict each other. Major means it works and somebody will get it wrong. Minor means it is right and untidy. This is good and maybe make it clearer are not findings.
Image: A findings card template with the three fields, and three severity chips in green, amber, and accent red.
---
## Slide 7: The record is the deliverable, not the meeting
```
# Where                  Finding                        Sev      Decision
1 Program.cs:157         comment says long enough,      Blocker  Fixed today
                         value is 5 s, service takes 40
3 user-help.md           fallback section is 9 words    Major    Deferred, Thu
4 io-specification.md    says retries 5, code says 1    Blocker  Doc was wrong
```
Speaker notes: Every row ends in a decision. Fixed, deferred with an owner and a day, or rejected with a reason. A finding with no decision next to it is a finding nobody acted on, and the record exists to make that visible. Row four is the one that matters most: neither the document nor the code looked wrong alone.
Image: None. This slide is code.
---
## Slide 8: Rejecting a finding is allowed, in writing
```
Reviewer suggested caching answers.
Rejected: this service keeps no state on purpose, and a cache is a
store of other people's writing that we would then have to justify
under the privacy rules.
```
Speaker notes: You are allowed to reject a finding and you have to write down why. That is a good rejection and it is worth more than a grudging fix, because it shows somebody thought about it. What is not allowed is a finding that quietly vanishes because the author disagreed. That is the exact failure mode this whole exercise exists to prevent.
Image: None. This slide is code.
---
## Slide 9: Why this is uncomfortable, honestly
- Criticising your friend's work is awkward
- Being criticised feels like being graded
- No good walkthrough ends with less work for you
- What helps: findings name a file, never a person
Speaker notes: Be honest about this. Criticising your friend's work is uncomfortable. Being criticised feels like being graded. And by Week fifteen you are tired and the thing works, and there is no version of a good walkthrough that ends with you having less to do. What makes it bearable is that findings name a file and a line, never a person, and that you get to reject them in writing.
Image: Two students across a table with a document between them rather than a screen, neutral posture, navy.
---
## Slide 10: What you are about to build
- Forty minutes, the script, with another team
- Documents first, failure paths only, author off the keyboard
- Every finding gets a severity and a decision
- The record is committed today, findings unfixed included
Speaker notes: Build one is the walkthrough itself, forty minutes, with the team I pair you with. Build two is acting on what came out of it. The record gets committed today whether or not the findings are fixed, including the ones you deferred and the ones you rejected, because a record that only lists the findings you happened to fix is not a record.
Image: A committed record file in a repository view, with three findings visible, one fixed, one deferred, one rejected.
