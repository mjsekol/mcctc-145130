# Training and Inference
---
## Slide 1: You corrected it and it worked
- So you taught it, right
- Next session, same mistake
- Nothing you said stuck
- Here is what actually happened
Speaker notes: You have corrected a model mid conversation and watched the next answer get better. That is real. And then you came back the next day and it made exactly the same mistake, and that is real too. Both of those follow from one idea and by the end of the period you will be able to explain it to your parents.
Image: Two chat windows, one with a correction working and one the next day with the same mistake.
---
## Slide 2: Two completely different activities
- Training set the weights
- Inference uses them
- One happened once, elsewhere
- One happens when you press enter
Speaker notes: Almost every wrong belief about these systems comes from blending these two words together. Training is the process that produced the numbers. Inference is what happens on our lab machine. They are not two phases of one thing you are part of. One of them finished before you ever opened the program.
Image: A timeline with a single enormous block labelled training and many tiny ones labelled inference.
---
## Slide 3: What training actually did
- Showed it an enormous amount of text
- Asked it to predict the next piece
- Compared the guess to what followed
- Nudged the numbers, an unimaginable number of times
Speaker notes: That is the loop. Predict, compare, adjust, repeat. Months of specialised hardware. You will not do this in this class and nobody expects you to. What you need from it is the last fact: when it finishes, the result is a file full of numbers, and that file is the model.
Image: A loop diagram: predict, compare, adjust, repeat.
---
## Slide 4: What inference does
- Tokenize your text
- Run it through fixed weights
- Get a probability for every next token
- Choose one, append, run again
Speaker notes: That is the entire mechanism. There is no other step. Notice what is missing: there is no lookup, no checking, and no stage where it decides whether the answer is true. Correct output is output whose most likely continuation happened to match reality, and that is why there is never a warning when it does not.
Image: A loop showing one token being produced and appended, then the loop repeating.
---
## Slide 5: The weights do not change
- Not during your request
- Not because you corrected it
- The file on disk is the same file
- Nothing is learned while you use it
Speaker notes: Write this down. During inference nothing is learned. The improvement you saw inside a conversation was your own correction sitting in the input, being re-read from scratch every single turn. Take it out of the input and the behaviour disappears, which is exactly what happened the next day.
Image: A file on disk with an unchanged timestamp before and after a request.
---
## Slide 6: What the cost actually looks like
```
  prompt            median total   median ttft   tokens   tokens/sec
  p1_short             1335.7 ms      318.3 ms     40.0         39.3
```
Speaker notes: Read that as a story. A third of a second passed before any text existed at all. Then tokens arrived at about forty a second for a second. Total wait, one and a third seconds, for forty tokens. On real hardware the numbers differ and the shape does not: a pause, then a stream. The pause is the first token. The stream is the same thing happening again and again.
Image: None. This slide is code.
---
## Slide 7: Three things people mean by trained on our data
```
"I trained it by talking to it"  -> earlier text re-sent in the prompt
"We gave it our documents"      -> documents searched, parts put in the prompt
"We fine-tuned it"              -> more training, producing a new weights file
```
Speaker notes: Only the third one changes any weights, and it produces a different file rather than editing the one you have. The middle one is retrieval and it is what Module 4 builds. For most practical problems it is the right answer: cheaper, updated the second a document changes, and you can show which document the answer came from.
Image: None. This slide is code.
---
## Slide 8: The same prompt twice
- Our stub gives the same answer
- A real model often does not
- It samples with some randomness
- Turn that off and it repeats
Speaker notes: Our stub is a rule system so it is perfectly repeatable. A real model usually chooses the next token with some randomness rather than always taking the likeliest, so two identical prompts can produce two different answers. That matters for your own testing and it is why the service validates the shape of an answer instead of its exact text.
Image: One prompt with two different outputs branching from it.
---
## Slide 9: The belief this kills
- Every time you use it, it learns
- False during inference
- Products do improve, at the company
- Conversations improve, from the input
Speaker notes: This is the most widely believed false thing about these systems, and the two reasons people believe it are both partly right. Products genuinely do get better over time, on the company's schedule. Conversations genuinely do get more relevant as they go. Neither of those is the model learning from you while you use it.
Image: A crossed out arrow from a user back into a model file.
---
## Slide 10: The sentence for a non-technical adult
- A huge set of numbers
- Adjusted once until it guessed well
- Now it guesses the next piece
- Adds it on, guesses again
Speaker notes: That is the exit criterion for this module and you will write a full version of it in Week 3. Say it out loud now while it is fresh. And notice the clause I always add on the end: everything it produces is produced that way, including the parts that are true.
Image: A plain sentence on a clean background, no diagram.
---
## Slide 11: What you are about to build
- Send an identical prompt twice
- Record whether the answers match
- Design an experiment that would prove learning
- Then say why ours cannot run it
Speaker notes: Build one is the repeat test and it takes ten minutes. Build two is the interesting half. You design an experiment that would show a model learned from you, and then you find out that our stub cannot settle it, because a stub is not a model. Naming a question your instrument cannot answer is a result, and it is Week 3 arriving four days early.
Image: An experiment plan with a line through the step the stub cannot perform.
---
