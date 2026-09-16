# What Retrieval Still Gets Wrong
---
## Slide 1: A real sentence, correctly quoted, with a citation
- From a real document in your handbook
- And the answer is misleading
- Nobody fabricated anything
- The citation is what makes it worse
Speaker notes: Everything about this answer is honest. Real sentence, real file, correct quotation, exact character offsets. And a member who reads it walks away believing the wrong rule. Work out how that is possible and you have understood the last concept of this module.
Image: A retrieval result with a citation, looking entirely trustworthy.
---
## Slide 2: Two documents disagree
- The loan policy says two items at one time
- The electronics bench says up to three
- Neither document is wrong on its own
- The bench one even gives its reason
Speaker notes: A power supply, a scope, and a parts bin are one working setup rather than three projects, which is a perfectly good reason. A person holding both documents works it out in a second. A person holding one of them does not know the other exists.
Image: Two document excerpts side by side with the numbers two and three circled.
---
## Slide 3: Ask the system and see which one comes back
```
Question: "how many items can a member have out at one time"
1. +0.4422  02-loan-policy.md . What may be borrowed
3. +0.3289  02-loan-policy.md . Returns
4. +0.3123  07-electronics-bench.md . How many at once
```
Speaker notes: The three item rule came back at position four. The two item rule did not come back at all, even though two other chunks of that same document did. A member reads this and learns the exception rather than the rule, from a correctly cited source.
Image: None. This slide is code.
---
## Slide 4: The fix is not in your code
- Widening k makes both more likely to appear
- That is a mitigation, not a fix
- Somebody has to reconcile the documents
- Retrieval inherits every contradiction you have
Speaker notes: You can widen k or add a score threshold, and that is worth doing, and it only widens the window and hopes. The contradiction is still in the handbook and it will find somebody else. Corpus hygiene is not a coding task and it is the actual fix.
Image: A wider search window catching both documents, with the contradiction still drawn between them.
---
## Slide 5: It retrieves what is near, not what is true
```
Question: "what do I do if the resin printer fan is not running"
1. +0.3768  01-access-and-safety.md . Training holds
2. +0.2799  05-media-kits.md . Batteries
3. +0.2716  07-electronics-bench.md . The power supply
```
Speaker notes: The resin printer document is not in that list at all, and it contains the exact answer: if the cabinet fan is not running the printer does not run. Three true paragraphs, nothing answered. On a hash based stub this is guaranteed. On a real model it happens less and it still happens.
Image: None. This slide is code.
---
## Slide 6: Some questions have no passage
- How has equipment use changed over three years
- Which of our policies contradict each other
- What is not in the handbook
- None of those is a sentence anywhere
Speaker notes: Retrieval finds passages. If the answer is not in a passage there is nothing to find. The first one is an aggregate over a database. The second needs all of them read at once, which is the opposite of chunking. The third is an absence and nothing retrieves an absence.
Image: Three questions with a document icon crossed out beside each.
---
## Slide 7: Retrieval moves the security problem
- A fine tuned model has your data inside it
- A retrieval system reads your data at question time
- So whoever can ask reaches whatever the retriever reaches
- Index the holds report and it answers questions about people
Speaker notes: Yesterday traceability was the advantage. This is its other face. If you index the holds list along with the handbook, your assistant will faithfully tell anybody who asks which member has not returned the oscilloscope, with a citation. There is no prompt that fixes that. Decide what goes in the index.
Image: An index containing two kinds of document, with one answer path marked as a problem.
---
## Slide 8: The paragraph you owe every demonstration
- The stub builds its vector from a hash
- So the plumbing is proven
- And the ranking carries no information
- Not in either direction
Speaker notes: Say this before somebody else does. And notice the exact claim. It is not that the results were not very good. It is that the results say nothing about quality either way. One of the three questions today landed on the right document and that was luck.
Image: A demo screen with a short honest disclaimer printed under it.
---
## Slide 9: The shape of every bad AI demonstration
- You ask the question you tried while building it
- It works
- You show that question and move on
- Nobody is lying, and nobody learned anything
Speaker notes: This is not dishonesty by intent, it is what happens when the person demonstrating never asked a question they had not already asked. The fix takes two minutes. Ask three new questions before you present, write down what happened, and show the one that went badly.
Image: A rehearsed demo path drawn as a single narrow line, with untested questions all around it.
---
## Slide 10: What you are about to build
- Gate 2 W12, an AI written data plan, forty minutes
- Five parameters, every one has a real problem
- One of them is genuinely arguable
- Verify, do not recognise
Speaker notes: Build one is Gate 2 and it is not code this week. An AI wrote a four week implementation plan for the makerspace and it reads like a consultant wrote it. Five parameters, evidence for each, and a command anybody can rerun. Several of its claims are things you half believe, which is exactly what makes them work.
Image: A professional looking plan document with five evaluation parameters listed beside it.
---
