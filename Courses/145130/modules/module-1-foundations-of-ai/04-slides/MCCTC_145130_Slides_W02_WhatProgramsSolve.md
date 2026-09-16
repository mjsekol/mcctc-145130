# What Programs and Scripts Actually Solve
---
## Slide 1: Build an app that tracks the 3D printers
- That sentence names a solution
- It does not name a problem
- Nobody can argue with it
- Which is exactly the trouble
Speaker notes: Read that sentence and notice what is missing. Who is hurt. What goes wrong for them. How often. Three weeks from now a team using that sentence cannot decide whether a feature is in scope, because the sentence they agreed on cannot settle any argument.
Image: A project title with no people in it.
---
## Slide 2: Five reasons a program earns its place
- Repetition, the same steps too often
- Scale, more than a person can hold
- Speed, faster than a person can answer
- Consistency, identical every time
- Reach, where nobody is standing
Speaker notes: If none of these is true, the honest answer is often a checklist, a spreadsheet, or a conversation. Saying so out loud is a professional skill rather than a failure. You will be in meetings where the right answer is that this does not need software, and somebody has to be able to say it.
Image: Five icons, one per reason.
---
## Slide 3: The five places the competency names
- Desktop, one machine, one person
- Mobile, battery and a dropping network
- Enterprise, many users and a history
- AI, the answer is not exact
- Cloud, not your machine
Speaker notes: These overlap constantly and they are not boxes to sort programs into. They are a way of naming where a constraint came from. Your Module 5 application is a desktop program calling an AI service that might run on a cloud machine inside an enterprise network, and every one of those words explains a different design decision.
Image: Five overlapping regions rather than five separate boxes.
---
## Slide 4: One problem, five places
- Too many help requests to sort
- Desktop: a file that goes stale
- Mobile: photos, permissions, dropped network
- Enterprise: roles and a history that survives
- Cloud: not your machine, so where is the data
Speaker notes: Same problem in every row. What changes is the constraint, and the constraint is what actually determines the design. This is the exam skill: given a situation, say which constraints apply and why.
Image: One problem statement with five different sets of constraints branching off.
---
## Slide 5: The AI row is different
- The output is a suggestion
- Failure is normal, not exceptional
- Provenance has to travel with the answer
- The other four rows need none of that
Speaker notes: Four of those rows produce exact answers. The AI row does not, and that changes three things structurally. The anchor service already enforces the first one: classify may only return a label from a fixed list, because a program that trusts a made up label writes it straight into your database.
Image: An answer card with a suggestion stamp and a source line.
---
## Slide 6: Provenance, in real output
```
model endpoint http://127.0.0.1:11634, model llama3.2
  label:   could not be read out of the answer (unparsed)
  the model actually said: I am not able to help with that request.
Done. 12 tickets, 12 with no label this program was willing to report.
```
Speaker notes: That program worked. Nothing crashed, every ticket got an honest line, and not one of them got an invented label. Count the places it tells you: on every answer, in what the model actually said, and in the total. That is not paranoia. That is what it takes for a reader not to assume the better answer.
Image: None. This slide is code.
---
## Slide 7: Not a problem statement
```
"Build an app that tracks which lab station each 3D print is running on."
```
Speaker notes: One more time, and say what is wrong with it out loud. It names an app. It names a tracker. It leaves no room for a solution that is not software, including the whiteboard that would have fixed it in an afternoon.
Image: None. This slide is code.
---
## Slide 8: A problem statement
```
"Students come back for a print and cannot tell which of the four
 printers has it, so they open lids on prints that are still running
 and ruin them. It happens two or three times a week."
```
Speaker notes: Who is hurt. What goes wrong. How often. And nothing about what to build, which leaves every solution on the table. Read that to a stranger and they can suggest three fixes. Read them the previous slide and they can only agree.
Image: None. This slide is code.
---
## Slide 9: The test, and you will fail it twice
- Does your sentence name an app
- A tracker, a website, a dashboard
- Then you wrote a solution
- Rewrite until it names a person
Speaker notes: Everybody writes the solution version first. That is not a character flaw, it is what the format trains. The fix is mechanical: circle every noun that is a thing you would build, delete it, and see whether a sentence is left. If nothing is left, you have not found the problem yet.
Image: A sentence with every buildable noun circled and crossed out.
---
## Slide 10: What you are about to build
- Three problem statements, real ones
- From this building, from this week
- Then pick one and place it
- Which of the five, and which constraints
Speaker notes: Build one is three problem statements about people in this building, and I will read them out loud, and the room will tell you which ones named an app. Build two takes your best one and places it in the five: which setting, which constraints apply, and one sentence on whether a model belongs anywhere in it. Most of the time the honest answer is no.
Image: Three index cards with problem statements written on them.
---
