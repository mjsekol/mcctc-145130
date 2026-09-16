# Three Things a Language Model Cannot Do
---
## Slide 1: One request, two failures, uniform tone
- A fluent summary of the themes
- A total of 41.5 hours
- A quoted shop standard
- All three sound identical
Speaker notes: Here is one answer about a spreadsheet of print jobs. The summary is good. The total is text that looks like a total. The quoted standard does not exist. Nothing in the tone changes between the part that is fine and the part that is invented, and that uniformity is the actual hazard.
Image: One block of output with three sections shaded differently by trustworthiness.
---
## Slide 2: One, it cannot say where an answer came from
- There is no lookup step
- So there is no source record
- A citation is produced like any sentence
- As likely text
Speaker notes: This follows from the mechanism rather than from a gap in the technology. Output is tokens chosen for likelihood. A reference to a real paper and a reference to one that does not exist look identical from the inside, because both are plausible continuations of a sentence heading toward a citation.
Image: A citation with an empty box where the source would be.
---
## Slide 3: What partly fixes it
- Retrieval: search your own documents
- Put the relevant passages in the prompt
- Report which document each came from
- The provenance comes from your search
Speaker notes: Notice where the honesty comes from in that design. Your search has a record. The model still has none. Module 4 builds this and it is the right answer for most practical problems, because it updates the moment a document changes and you can point at the page.
Image: A search hitting a document set, with the found passage flowing into a prompt.
---
## Slide 4: Two, it cannot be relied on to be exact
- Arithmetic, counting, precise lookups
- Anything where close is wrong
- Likely and correct are different properties
- Nothing in the process prefers correct
Speaker notes: For a multiplication it has never encountered, the most likely tokens are the ones that look like an answer to that kind of question. This is not about model size. A larger model gets more of them right, which is a completely different claim from being reliable, and there is still no signal telling you which ones to check.
Image: A calculator next to a model, with only one of them marked reliable.
---
## Slide 5: The design that fixes it
```
model  -> work out what was being asked, pull out the amounts
code   -> validate each amount, then add them up
```
Speaker notes: Two lines and this is the shape of your Module 5 application. The model handles language. Your code handles anything that has to be exact. Never let a model do the arithmetic in your program, and be specific about that rule: it means the number must be computed by code even when the model offered you one.
Image: None. This slide is code.
---
## Slide 6: Three, and this one is an argument
```
"A language model does not understand what it is saying."
```
Speaker notes: You will see this stated as settled fact constantly, including on the page you scored last week. It is not settled. I am going to give you the strongest version of each side and then you are going to have to hold a position, which is what Friday's Gate 2 asks for.
Image: None. This slide is code.
---
## Slide 7: The case that it does not
- The mechanism contains nothing like meaning
- Nothing in it refers to the world
- It contradicts itself without discomfort
- It invents citations with equal confidence
Speaker notes: Tokens in, distribution out, sample, repeat. The system has never seen a 3D printer, waited for a bus, or been wrong about something and noticed. And it fails in ways understanding would prevent: nothing is tracking consistency, so it asserts a fact and contradicts it two paragraphs later.
Image: A closed loop with no connection to anything outside it.
---
## Slide 8: The case that the question is open
- Understand has never been defined testably
- The argument assumes simple parts cannot suffice
- Brains are also simple parts
- That is only pattern matching keeps being revised
Speaker notes: This is the side students have usually never heard argued well, so listen to it properly. Saying it is only pattern matching is a claim about what pattern matching cannot achieve, and that claim has been revised downward repeatedly over the last decade by people who were not expecting to revise it.
Image: A question mark over a definition that has never been written down.
---
## Slide 9: So write what is settled
- Settled: the mechanism, no learning during use
- Settled: confidence carries no information
- Settled: it fabricates sources
- Not settled: whether that is understanding
Speaker notes: In your own documents, describe what it does and what it fails at, and stay out of the word. It produces fluent text and fabricates citations with equal confidence is checkable. It does not understand anything is a position in an open argument, and stating it as fact to beginners is the defect you were asked to find last week.
Image: Two columns, settled and open, with the last row in the open column.
---
## Slide 10: The wrong lesson to take
- AI cannot be trusted, so avoid it
- Treats trust as a property of the technology
- The question is per task
- What happens when this answer is wrong
Speaker notes: This sounds cautious and it is a way of avoiding the actual work, which is deciding task by task where a mistake is recoverable. Draft an email and a person reads it before sending: recoverable. Compute a grade and nobody checks: not recoverable. The difference is whether a human who could catch it stands between the output and the consequence.
Image: Two pipelines, one with a person in the middle and one without.
---
## Slide 11: What you are about to build
- The pretest first, then this
- Three failures, one from your own work
- Name the design that contains each
- One has to be the contested one
Speaker notes: The pretest runs in Build 1 and it is not graded, it tells me where to spend Module 2. Build 2 is three failures with the design that contains each, and one of them has to be the argument from slide six, where you take a side and give the other side its strongest form before you disagree with it.
Image: A three row table: failure, why it follows, what contains it.
---
