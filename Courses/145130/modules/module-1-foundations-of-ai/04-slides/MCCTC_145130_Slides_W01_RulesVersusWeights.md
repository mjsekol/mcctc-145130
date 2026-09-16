# Rules You Wrote Against Weights Somebody Fitted
---
## Slide 1: Why did it say that
- Your program said hardware
- The ticket was about a password
- Somebody has to answer why
- One of these systems can
Speaker notes: Here is a help request about being locked out of an account. Two systems labelled it. One said account and one said hardware. In a minute I am going to ask each of them why, and only one of them is going to be able to tell me. That difference is the whole competency for today and it is the most likely thing from this module to show up on your exam.
Image: Two identical help request cards with different labels stamped on them.
---
## Slide 2: Rules a person wrote
```python
if "locked out" in text.lower():
    return "account"
if "wifi" in text.lower():
    return "network"
return "other"
```
Speaker notes: Three lines. A person wrote every one of them and a person chose the order. You can read it. You can put a print statement above any branch. When it gives a wrong answer, there is a line to change. Hold on to those three facts because in two slides all three of them go away.
Image: None. This slide is code.
---
## Slide 3: The reason is a line you can point at
```
account
branch account (getting in) fired on the phrase 'locked out'
```
Speaker notes: That second line came out of the program itself. It is not a guess about what happened. The function that produced the label produced the reason at the same time, from the same branch. Nothing else in this course is going to be able to do that, so look at it while you can.
Image: None. This slide is code.
---
## Slide 4: Weights fitted to data
- A very large pile of numbers
- Nudged until outputs matched examples
- Nobody wrote a rule
- Nobody can read one
Speaker notes: A neural network is numbers. They were adjusted automatically, over and over, in whatever direction made the system's answers closer to a huge collection of examples. When it finishes, the numbers are the whole system. There is no list of rules inside it, no comments, and no line to point at.
Image: A dense grid of small numbers, with no structure a person could read.
---
## Slide 5: The trade, both directions
- Trees are readable and brittle
- Networks are flexible and opaque
- Neither column is the good one
- You are choosing what to give up
Speaker notes: Write this down because it is the sentence people get wrong. A model is not a better if statement. You are giving up the readable reason in order to get coverage of cases nobody wrote a rule for. That is a trade, and which side you want depends on whether you would rather explain a wrong answer or have fewer of them.
Image: A balance scale, readable reason on one side, coverage on the other.
---
## Slide 6: Watch what happens to one ticket
- MT-2004 is about a password
- The sentence contains the word screen
- Your tree asks about getting in first
- The other system matched screen
Speaker notes: Here is the ticket. I am locked out of my account after changing my password, and the login screen accepts it on my phone. Three words in there could trigger three different branches. What the system answers depends entirely on which question somebody decided to ask first.
Image: The ticket text with locked out, password, and screen each highlighted.
---
## Slide 7: The real comparison
```
  ticket    staff      your rules  service    source    agree
  ------------------------------------------------------------
  MT-2004  account    account     hardware   model     rules
  MT-2008  software   software    hardware   model     rules
```
Speaker notes: This is a real run from the lab you are about to do. Two tickets where the hand written rules agreed with the makerspace staff and the other side did not. Before anybody celebrates, look at the column headed source, because there is a problem with it and it is the most useful thing on this slide.
Image: None. This slide is code.
---
## Slide 8: The wrong way to say it
- We used AI instead of if statements
- Because AI is more accurate
- More accurate at what, than what
- Measured how, on which examples
Speaker notes: This sentence turns up in project write ups every single year. Accuracy is not a property a technology has. It is a number a specific system got on a specific test. And notice what the sentence quietly threw away: the tree could tell you which branch fired, and whatever replaced it cannot. That cost is real and the sentence does not mention it.
Image: The sentence on a slide with the words more accurate circled in red.
---
## Slide 9: Where the clean story breaks
- Some trees are built from data
- An algorithm picks each branch
- That is machine learning, with a tree
- The exam means hand written trees
Speaker notes: I am telling you this because somebody in here will find it and I would rather you hear it from me. The neat sentence, trees are written and networks are learned, is a starting point and not the whole truth. The property that actually divides them is whether a human authored the boundaries and whether you can read the result.
Image: Two trees side by side, one drawn by hand, one produced by an algorithm.
---
## Slide 10: A tree fails visibly, a model fails fluently
- Nothing works, says ticket MT-2012
- The tree falls through and says so
- A model produces a label anyway
- With a confident sentence explaining it
Speaker notes: This is the difference that matters when a person is going to read the output. The tree has a no branch matched state and it reports it. A model has no such state. Asked for a label, it produces the tokens that look like a label, and it will explain its reasoning in a sentence that reads perfectly well and describes reasoning that never happened.
Image: Two screens, one showing a blank result with a reason, one showing a confident wrong answer.
---
## Slide 11: What you are about to build
- Your own triage tree, nine tickets
- Then the same tickets through the service
- One table, every disagreement
- And an argument about three of them
Speaker notes: Build one is your decision tree in triage rules dot py, and check rules dot py tells you when the nine settled tickets pass. Build two runs both systems on the same twelve tickets and writes a comparison file. Three of those tickets have no agreed answer on purpose, and what you write about those three is the part I am going to read first.
Image: A comparison table with two columns of labels and a disagreement column.
---
