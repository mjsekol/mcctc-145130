# Retrieval Versus Fine Tuning
---
## Slide 1: The advisor said one sentence
- I would like to be able to point at the paragraph
- One approach can do that
- The other one cannot, ever
- That is most of today in one line
Speaker notes: Go back and read the brief. She did not ask for an assistant, she asked to be able to point at the paragraph. One of the two approaches we are comparing hands you a file name, a heading, and a character range. The other hands you a sentence with no source. Hold that while we do the other three arguments.
Image: A quoted line from the brief, with a citation reference drawn beside it.
---
## Slide 2: Two routes, and one of them is not what you think
- Fine tuning changes the model's weights
- Retrieval does not touch the model at all
- Prompting is pasting context in by hand
- Retrieval is prompting with the pasting automated
Speaker notes: Three things and people mix up two of them. Fine tuning is the only one that changes the model. Retrieval finds the relevant pieces at question time and puts them in the prompt, which is prompting with the choosing automated. Getting that distinction right is worth marks on its own.
Image: Two paths from a question, one going into a modified model, one going through a document store into an unmodified model.
---
## Slide 3: Cost, honestly
- Retrieval is a file and a loop, per query, forever
- Fine tuning is hardware, a training set, and a specialist
- And again every time the material changes
- The costs are shaped differently, not only bigger
Speaker notes: Do not say fine tuning is expensive and stop. Say the costs are shaped differently. Retrieval costs a little on every query forever. Fine tuning costs a lot once and little per query. At enormous query volume over material that never changes, that trade can actually go the other way.
Image: Two cost curves over time, one flat and continuous, one a large step then flat.
---
## Slide 4: Freshness decides most real cases
- Change the policy, rebuild the index, done
- A fine tuned model still believes the old policy
- Confidently, with no version number to check
- Until somebody retrains it
Speaker notes: This is the boring argument that wins. Handbooks change, policies change, prices change. There is no way to look at a model and tell which version of a fact is inside it. A system that is wrong until the next training run is a system that is wrong, and nobody can tell by looking.
Image: A policy document being edited, with one path updating instantly and one path stuck on an old version.
---
## Slide 5: Traceability, on screen
```
4. score +0.3123   07-electronics-bench.md . How many at once   characters 483-668
   You may sign out up to three items from the electronics bench at one time...
```
Speaker notes: A file name, a heading, and a character range. Somebody who knows the handbook checks that in ten seconds. And there is a second thing it buys: when the answer is wrong you can tell whether the retrieval went wrong or the source was wrong, and those have different fixes. With fine tuning they are the same indistinguishable failure.
Image: None. This slide is code.
---
## Slide 6: And the fourth section
- It retrieves what is near, not what is true
- It inherits every contradiction in your sources
- It cannot answer what no passage contains
- The chunking already decided what is answerable
Speaker notes: An argument with no fourth section is a sales pitch. Anybody can say cheap, fresh, traceable. The person worth listening to says what it still gets wrong, specifically, and tomorrow is a whole lesson on it. For today, know the four so you can write the memo.
Image: Four small warning marks, each beside one of the four points.
---
## Slide 7: Where fine tuning actually wins
- Teaching behaviour, not facts
- Always answer in this format, this tone
- Refuse this kind of request, sound like our team
- None of that is a passage you can retrieve
Speaker notes: Be able to say this, because a memo claiming retrieval is always better is not an analysis. Format, tone, refusals, vocabulary: those are behaviour, and they are not written down anywhere as a passage. The usual real answer is both, a model fine tuned for the shape and the facts retrieved at question time.
Image: A model producing the same format for three different retrieved facts.
---
## Slide 8: The sentence in a plan you should push back on
- We will fine tune a model on the handbook
- Eight documents is not a training set
- The first policy change makes it wrong, silently
- And you threw away the citation she asked for
Speaker notes: You will read this in a plan. It sounds more serious than we chunked the handbook, and it is more work. More work is not a better answer. The most likely outcome of fine tuning on eight documents is a model that sounds like the handbook and makes up its contents.
Image: A plan document with the sentence highlighted and three annotations beside it.
---
## Slide 9: One table to carry out of here
```
                     retrieval        fine tuning
changes the model    no               yes
material changes     rebuild index    retrain
can cite a source    yes, exactly     no
teaches format       poorly           well
```
Speaker notes: Four rows, and you should be able to reproduce them from memory in the exit assessment. The two that decide most arguments are the middle two. The bottom one is the one that stops your memo being a sales pitch.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- The retrieval versus fine tuning section of your memo
- All four points, specific, not generic
- Name a failure in the actual handbook
- Your search results from yesterday are the evidence
Speaker notes: Build two is the memo section that carries ten of its fifty marks. All four points. The fourth one has to name a failure you can point at in the Ridge Creek handbook, not a generic sentence about retrieval being imperfect. You ran the queries yesterday. The evidence is already in your README.
Image: A memo section with four headings and a quoted search result under the fourth.
---
