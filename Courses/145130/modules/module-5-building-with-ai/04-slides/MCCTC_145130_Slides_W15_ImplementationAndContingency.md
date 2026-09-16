# The Implementation Plan and the Contingency Plan
---
## Slide 1: "Service complete" has been 90 percent done for a week
- It has no test
- So it can never fail
- So it never finishes
- A milestone you cannot point at is not a milestone
Speaker notes: Here is a milestone from a real submission shape. Service complete. It has no test attached, so nobody can ever tell you it is not done, so on any given day it is ninety percent done and it stays there. A milestone you can only describe is not a milestone. A milestone is something you can point at in under a minute.
Image: A progress bar frozen at ninety percent with a date label that keeps changing, in muted grey and accent red.
---
## Slide 2: Two documents, read on two different days
- Implementation plan: read on a good day, deciding what is next
- Contingency plan: read on a bad day, by somebody behind
- And possibly by somebody who is not you
- That is why they are separate documents
Speaker notes: These are different documents because they get read at different times by people in different moods. The implementation plan is read on a good day when you are deciding what to do next. The contingency plan is read on a bad day by somebody who is already behind, and in this module there is a real chance that person is your partner while you are at BPA Regional.
Image: Two documents side by side, one under a calm blue header, one under an accent red header.
---
## Slide 3: The four parts, and the test for each
```
Before you start   checks not work       every item is a yes or no command
Milestones         five or fewer         you can point at it in a minute
Who does what      one owner, one backup no piece has two owners or none
How you know       a command they run    "works on my machine" is not on it
```
Speaker notes: Four parts and each one has a test. Before you start is checking, not work, and every item has a yes or no answer. Five milestones at most. One owner and one named backup for every piece. And finished means a command somebody who is not you can run, which is the part that makes all the rest real.
Image: None. This slide is code.
---
## Slide 4: The item every team skips
```
6  You know your task and your result shape
   check:  written in one sentence each, in the decision log
   if not: you are not ready to start. Go back to the IPO chart.

8  Both people can run everything on their own machine
   if not: fix it now. A team with one working machine has no backup.
```
Speaker notes: Item six is the one teams skip and it costs the most. A team that starts building before it has written down its result shape builds two different programs and finds out on Thursday. Item eight matters for this module specifically, because one of you may be gone for most of Week fourteen and a team with one working machine has no backup.
Image: None. This slide is code.
---
## Slide 5: Build the messy layer first
- M3, the service answers, comes before M4
- A client written against a service that does not exist yet
- gets written against what you imagine
- and what you imagine is always the happy path
Speaker notes: Look at the order of the milestones. The service comes before the client, and that is deliberate. A C sharp program written against a service that does not exist yet is written against what you imagine the service will send, and what you imagine is always the happy path. Build the layer that deals with mess first and the client has something real to disappoint it.
Image: Two stacked boxes with the lower one finished and the upper one under construction, an arrow pointing upward.
---
## Slide 6: The cut list, ordered, written in Week 13
```
1  the second task. Ship one, done properly.
2  extra fields in your result shape
3  retries
4  batch mode over a file
5  anything that demos well and does nothing
```
Speaker notes: This is the part of the contingency plan that actually gets used, and you write it in Week thirteen because in Week fifteen you are too invested to cut anything. One task end to end demonstrates everything the exit criteria ask for. Two half finished tasks demonstrate nothing at all.
Image: None. This slide is code.
---
## Slide 7: And the half that does the real work
```
never cut:
  the four distinct failure messages
  the fallback, and saying out loud that an answer came from it
  the troubleshooting log
  the I/O specification and the dataflow diagram
  the commit at the end of every period
```
Speaker notes: This is the more important half of the cut list. These five are what the exit criteria are written against. A program that only works when everything works is not the assignment, and it is not what you are being graded on, so the feature you want to save is never worth the failure handling you would trade for it.
Image: None. This slide is code.
---
## Slide 8: Five words that are the whole problem
- "the developer is satisfied that it works"
- The developer is always satisfied
- That is why they stopped
- Finished is checked by somebody who is not you
Speaker notes: This line came off a real submission shape. Each milestone is finished when the developer is satisfied it works on their machine. The developer is always satisfied. That is why they stopped working on it. Finished has to be something a person who is not you can check without asking you a question, which is exactly what the acceptance procedure in the reference implementation is.
Image: A single sentence on screen with the words the developer is satisfied circled in accent red.
---
## Slide 9: Why both documents fill up with true, useless sentences
- Written at the end, when you are tired
- Every sentence in them can be true and commit to nothing
- "Non-essential features are cut first" is true
- On Thursday every feature feels essential
Speaker notes: Both of these get written at the end when you are tired, and both can be filled with sentences that are perfectly true and commit you to nothing. Non essential features are cut first is true. It is also useless, because on Thursday of Week fifteen every feature feels essential and the document does not name any of them. A plan that names nothing decides nothing.
Image: A document full of grey text with one sentence highlighted and a caption reading this decides nothing.
---
## Slide 10: What you are about to build
- Every row names a command, a file, a person, or a number
- Five milestones, each with a test somebody else runs
- One owner and one named backup for every piece
- An ordered cut list, and the list you never cut
Speaker notes: Build one is your implementation plan, build two is your contingency plan, and there is one rule for both. Every row names a command, a file, a person, or a number. If a row has none of those four in it, it is a sentence about planning rather than a plan, and I will hand it back.
Image: A student plan on screen with four different rows highlighted, each in a different accent, labelled command, file, person, number.
