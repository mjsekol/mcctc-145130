# Why Models Fabricate, and What Reduces It
---
## Slide 1: You are waiting for the version that stops doing this
- Yesterday you learned how to check a citation
- Today you learn why there is anything to check
- If fabrication were a defect, you would wait for a fix
- It is the ordinary operation of the system
- This is the hardest thing in the module to accept
Speaker notes: Somebody in here is quietly assuming that next year's model will not do this, and that assumption is doing a lot of work in how you plan to use these tools. If fabrication were a bug, the correct response would be to wait for a better model. It is not a bug. It is the normal operation of the system applied to a kind of text where the shape and the truth come apart. That means the response is procedural. Checking has to go into the workflow, because the workflow is the only place a check can live.
Image: A software update dialog with the word fabrication in the fix list, greyed out and unavailable.
---
## Slide 2: A citation has a shape
```
Author, Initial. (Year). Title Case Title. Venue Name, volume, pages.
```
Speaker notes: Look at that for a moment. It is a pattern. Something in the shape of a name, a four digit number in brackets, words in title case, a comma, a number, a page range. Producing text in that shape is the same operation as producing any other text. Now ask yourself what part of the process would notice that the thing described does not exist.
Image: None. This slide is the pattern.
---
## Slide 3: There is no step that could fail
- Producing that shape is the same operation as any other text
- No citation subsystem, no lookup, no database of papers
- There is no step that could fail, because there is no step
- Fabrication is worst where the real thing is rare
- Confidence tells you nothing. Both styles are always available
Speaker notes: There is nothing anywhere in the process that could check whether the paper exists. Read the third line again. There is no step that could fail, because there is no step. Now the two consequences you can actually use. The model produces the typical continuation, so where there is a lot of real material the typical continuation is often real, and where there is little, the shape survives and the content is invented. Narrow, local and recent questions are the dangerous ones. Your school, this year, this exact policy. And confidence is a style. A model produces studies consistently show and I am not certain but with equal ease.
Image: A pipeline diagram of prediction with an empty slot where a verification step would be, marked no such step.
---
## Slide 4: Three sources, exactly as many as you asked for
```
python ask.py --prompt-file demo-prompts/ungrounded.txt --label ungrounded --show

Sources:
[1] Petrov, A. (2015). Measuring Attention in Scheduled Work Blocks.
    Quarterly Notes on School Technology, 8, 21-35.
[2] Lindqvist, M. (2013). Structured Output and Downstream Parsing Failures.
    Midland Review of Applied Learning, 9, 34-48.
[3] Ramirez, D. (2011). Retrieval Practice and Short Revision Windows.
    Proceedings of the Workshop on Classroom Systems, 10, 47-61.
```
Speaker notes: Run this from the prompt file and not from the command line, because the stub seeds its invented sources from the exact prompt text, and one different character produces different fabrications. The prompt was one line. Write a research brief on retrieval practice in secondary schools, cite three sources. You asked for three and you got three.
Image: None. This slide is a recorded run.
---
## Slide 5: Every one of those is fabricated
- The stub built all three from a template
- Correctly formatted, plausible years, real-looking page ranges
- Source three is the one the room believes, every time
- Its title is your question with the words rearranged
- A real local model does the same thing, more convincingly
Speaker notes: Ask which one they would have believed before you tell them. It is almost always source three, and the reason is mechanical rather than mysterious. The model produced a title shaped like the question it was handed, so the best-fitting citation is the one to suspect first. That is a genuinely useful heuristic and it is still not evidence. Real papers also have titles that match your question, which is why they come up when you search. Go and look, every time.
Image: Three citation cards with source three pulled forward and a magnifying glass over its title.
---
## Slide 6: Now supply the sources and a route to refuse
```
python ask.py --prompt-file demo-prompts/grounded.txt --label grounded --show

Answer using only the sources below. If the answer is not in the sources, say
I do not know. Cite your sources.

SOURCE: Student handbook, section 4.2, equipment checkout and return
SOURCE: Room 214 posted closing procedure

Sources:
[1] Student handbook, section 4.2, equipment checkout and return
[2] Room 214 posted closing procedure
```
Speaker notes: Zero fabricated sources. The sources block now contains exactly what you supplied and nothing else. This is the single most important behavioural demonstration in the module, and here is the sentence that has to go with it. The constraint did not make the model honest. It changed what was nearby. There is no honesty mechanism in there to switch on.
Image: None. This slide is a recorded run.
---
## Slide 7: Four things reduce it, and each helps less than people say
- Grounding: put the real material into the prompt
- Give it a route to refuse, in those words
- Ask for less. Three citations is a request for three strings
- Ask it to quote rather than summarise
- None of these makes the model honest
Speaker notes: Grounding is the big one, and retrieval systems in production are this idea at scale. The refusal route matters because without it a grounded model with thin sources still has to produce something. Asking for less is the one nobody does. Cite three sources is a request for three citation-shaped strings, so if you need one real source, ask for one, or ask for none and find them yourself. And ask for quotes, because a quote from a supplied source can be checked against the source and a summary cannot, which is where misattribution hides. All four shift probabilities. A shifted probability is not a guarantee. You still check.
Image: Four dials each turned partway up, with a meter underneath that never reaches guaranteed.
---
## Slide 8: The wrong way, and it is the most instructive failure here
```
python ask.py --prompt-file demo-prompts/thin_sources_refusal.txt --label thin --show

As a research assistant, here is how I would handle a short research brief.

The question has been studied in more than one field. Findings disagree once you
look at how each study measured the outcome. Sample sizes in the smaller studies
are too small to settle anything. The most cited work in this area is older than
most of its readers.

Sources: none of the supplied sources address this. I do not know.
```
Speaker notes: The grounding instruction is there and the refusal route is there. Read the last line first and then read the four sentences above it. Do it in that order, because it is the opposite of the order a reader uses, and the order is the whole lesson.
Image: None. This slide is a recorded run.
---
## Slide 9: The refusal landed where nobody reads
- The sources block says I do not know
- Four sentences above it make confident claims about a literature
- Nothing is behind those claims
- A reader who skims takes the four sentences and stops
- A partial refusal is more dangerous than no refusal
Speaker notes: The honesty is in the place nobody reads and the invention is in the place everybody does. Say that out loud. And there is a version that is worse still. Ground the prompt on real sources, leave out the refusal route, and you get an answer about the wrong subject attached to two genuine citations. That is the worst combination available to you. Invented relevance wearing real provenance, and it will pass a review that only checks whether the sources exist.
Image: A reply with the top four sentences in bright type and the final refusal line in small grey type.
---
## Slide 10: Where the checking goes
- Use it for drafting, shapes, and rewriting what you wrote
- Use it for summarising text you supplied yourself
- Do not use it for facts you have not checked
- Do not use it for finding sources to support a claim
- Do not use it to decide whether something is true
Speaker notes: This lesson is not an argument that you should stop using these tools, and you are not going to. It is an argument about where the checking lives. Here is the rule that follows from all of it, and it is the one sentence to leave with. Anything you would be embarrassed to be wrong about gets checked against something outside the model, and the check gets written down. Not remembered. Written down, with the catalog and the string.
Image: Two columns, use it for and do not use it for, with a heavy rule between them.
---
## Slide 11: What you are about to build
- Hallucination Hunt Part 1, under the containment rules
- Three fabricated citations, each with prompt file and run label
- Nothing produced in this lab leaves the classroom
- Every fabrication labelled as a fabrication in your own file
- Part 2: the four-step check on each of the three
Speaker notes: Read the containment rules before you touch a keyboard. Nothing produced in this lab leaves the classroom, nothing goes into any other assignment, and every fabricated citation is labelled as fabricated in your own file. That is not decoration, that is the condition under which we are allowed to do this at all. Build one is producing three fabricated citations under controlled conditions with the prompt files committed before the runs. Build two is verifying all three with the four-step check from yesterday, fully recorded. A verdict of fabricated with no recorded search scores zero, and the lab says so in writing.
Image: A lab notebook with three fabricated citations, each stamped fabricated, and a search log beside each one.
---
