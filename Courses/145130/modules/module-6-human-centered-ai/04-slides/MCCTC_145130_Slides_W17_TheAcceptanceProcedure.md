# The acceptance procedure you agree before you test
---
## Slide 1: Somebody decides whether this is finished
- If nobody wrote down what finished means
- That decision is a conversation
- And the person with more authority wins it
- It is the last new concept in this course
Speaker notes: At some point somebody decides whether the thing you built is done. If nobody wrote down what done means, that decision is an argument, and arguments are won by whoever has more authority in the room. This is the last new concept in this course and next week is nothing but running what you write today.
Image: Two people across a desk with an empty sheet between them, accent red.
---
## Slide 2: A case has three parts and it can fail
```
Given    what exists, what is running, what is in the folder
When     one action somebody performs
Then     one result somebody can see, that could have been otherwise
```
Speaker notes: Given, when, then. And the test for whether you have written one: if two people can read your case and disagree about whether it passed, it is not a case. There has to be a fact that settles it, and if there is not, the case will always pass, because passing is less awkward than arguing.
Image: None. This slide is code.
---
## Slide 3: One of these cannot fail
```
AC-1  The program works correctly with normal input and gives the
      user helpful messages when something goes wrong.

AC-2  Given 8 notes in the inbox and nothing listening on port 5158,
      When the sweep is run once,
      Then it exits with a code that is not 0, and out/ holds an
      incident file whose text names the wire failure.
```
Speaker notes: AC-1 will pass forever. Correctly and helpful are words the writer had a picture for and did not write down. AC-2 can fail, and it did fail twice while this module was being built, which is the only reason the freshness step exists.
Image: None. This slide is code.
---
## Slide 4: Three words that mean a case cannot fail
- gracefully
- properly
- correctly
- Each one is a placeholder for unfinished thinking
Speaker notes: Three words. When you see any of them in a case, somebody stopped thinking one sentence early. They are not lazy words, they are honest ones in the wrong place: the writer knows what they mean and has not worked out how anybody else would check it.
Image: Three words on cards, each with a small accent red strike through.
---
## Slide 5: Eight cases, and two of them are failures
```
AC-1  8 notes, service up        run once      exit 0, digest has 8 rows
AC-2  same notes, nothing        run again     exit not 0, incident names
      touched since AC-1                       the freshness step
AC-3  nothing listening on 5158  run once      exit not 0, incident names
                                               the wire failure
AC-8  after AC-1 to AC-5         search log    no note text, no name
```
Speaker notes: Four of the eight, and notice AC-8. No note text and no name anywhere in anything the program writes. That is the program rule written as a case somebody can run, and nobody thinks of it until they are told. It is also the one that catches a real privacy defect.
Image: None. This slide is code.
---
## Slide 6: The platform line is one line
- Windows 11, Python 3.13.7, no model runtime
- Also to be run on a lab machine with Python 3.14
- That is competency 2.12.3, targeted platforms
- Where it ran, and where it still has to run
Speaker notes: Targeted platforms and device types sounds like a large piece of work. For a program like yours it is one line: where these results came from, and where they still need to be produced before anybody signs anything. Writing it costs nothing and it is the difference between it works and it works here.
Image: Two machine icons, one ticked and one with a pending mark.
---
## Slide 7: Agreed means somebody argued with it
- Read them the cases, not the code, not a demo
- Ask: is anything here that would not convince you
- Write down what they change
- A procedure nobody argued with is one nobody read
Speaker notes: Ten minutes. You read them eight rows. Not a demonstration, because a demonstration is the part you control. Then one question: is there anything on this list that would not convince you, or anything missing that would. Expect them to add a case and delete none. The changes are the deliverable.
Image: A printed case table with two handwritten additions in the margin.
---
## Slide 8: A correction has three parts
```
AC-4 failed. Exit code was 0 and no incident file appeared.
Changed:  added the freshness step, comparing newest inbox file time
          against last_source_mtime in state/last_run.json.
Re-ran:   AC-4 now exits 2 and writes out/incident-r0006.md.   PASS
```
Speaker notes: The failed case, what you changed, and the re-run that passed. A correction with no re-run under it is a plan, not a correction. And you never change the case because it is about to fail, because a procedure you edit while running it measures nothing at all.
Image: None. This slide is code.
---
## Slide 9: They are allowed to say no
- A reasoned no beats an empty yes
- It is scored that way
- Say this to your partner before you go
- Hiding a no is the failure this exists to prevent
Speaker notes: At the end of next week you ask them to accept, and they can say no. A recorded no, with the reason and what would change their answer, closes the same line on the rubric as a yes and is worth the same marks. Say that to your partner on the way out, because the pressure to come back with a yes is real.
Image: Two signature boxes, one signed and one with a written reason instead.
---
## Slide 10: What you are about to build
- Eight cases for your application and your automation
- At least two of them failure cases
- A stakeholder identified by role, not by name
- Then take it to them and write down what they change
Speaker notes: Build one is eight cases, two of them failures, with a platform line. Build two is taking it to the person and recording what they changed, or recording that they changed nothing and who they were. Next week you run this, in front of them, and you do not edit it while it runs.
Image: An acceptance procedure on a clipboard with a stakeholder role written at the top.
