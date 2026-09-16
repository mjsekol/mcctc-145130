# The Five Elements of a Prompt
---
## Slide 1: You rewrote it four times and it got no better
- You have been rephrasing prompts since middle school
- Some versions work and you cannot say which part did it
- Write a better prompt names nothing you can change
- Today you get five named things to change instead
Speaker notes: Yesterday you learned that the model sees only the text you sent. That leaves the obvious question, which is which text. And the advice you have been given your whole life is write a better prompt, which is useless, because it does not name a single thing you could do differently. By the end of these fifteen minutes revise your prompt stops being a vibe and becomes a specific instruction.
Image: A prompt box with four crossed-out rewrites stacked above it, and five labelled slots below it waiting to be filled.
---
## Slide 2: The five elements
- Role: who is talking
- Task: what finished looks like
- Context: what the model cannot know
- Format: what shape the answer takes
- Constraints: what it may not do
Speaker notes: Copy these five down, because they go on the board and they stay there for three weeks. Every lab, every Gate two, and the module exit assessment uses these exact words. Notice that not one of them is make it better. Each one answers a different question, and the skill is knowing which question you are actually asking.
Image: Five stacked labelled bands in navy and accent blue, one per element, each with its question printed beside it.
---
## Slide 3: Each element does a different job
- Role narrows the voice, not the facts
- Task states a finish line, and removes the padding
- Context supplies facts the model could not have
- Format changes the shape of the output completely
- Constraints are the negative space: limits and exclusions
Speaker notes: Take these one at a time. Role produces text that reads like a pharmacist wrote it, and it adds no pharmacy knowledge. Task is the one people skip and the one that does the most work, because without a finish line the model has no reason to stop. Context is the only element that supplies a fact, and you cannot get a fact by asking more politely. Format has the biggest visible effect. Constraints are where most of the safety in a real production prompt lives.
Image: Five icons in a row: a mask, a finish line, a filing box, a set of brackets, and a stop sign.
---
## Slide 4: One task, five prompts, every number recorded
```
| Label | Prompt words | Reply words | Seconds | Shape | Valid JSON | List items | Sources claimed | Hedges |
|---|---|---|---|---|---|---|---|---|
| p1_bare | 6 | 110 | 0.02 | prose | no | 0 | 0 | 5 |
| p2_task | 48 | 65 | 0.00 | prose | no | 0 | 0 | 2 |
| p3_role_audience | 75 | 105 | 0.00 | prose | no | 0 | 0 | 2 |
| p4_format_constrained | 69 | 54 | 0.00 | numbered | no | 5 | 0 | 0 |
| p5_grounded_sourced | 81 | 84 | 0.01 | numbered | no | 5 | 3 | 0 |
```
Speaker notes: One task all week. Produce the instructions a new club member needs to run the Friday equipment checkout by themselves. Five prompts, each one adding an element to the one before it. Before I say anything, read down the prompt words column and then read down the reply words column, and take thirty seconds to notice something that should not be true.
Image: None. This slide is the recorded comparison table.
---
## Slide 5: Look at p1 to p2 before anything else
- The prompt got eight times longer
- The reply got shorter, a hundred and ten words to sixty-five
- Hedging phrases dropped from five to two
- Stating what finished looks like removed the padding
- Almost everyone predicts the opposite
Speaker notes: Take a vote on this before you show it, every time. Ask the room whether a longer prompt gives you a longer answer, and most hands go up. Six words gave a hundred and ten. Forty-eight words gave sixty-five. All p2 added was a statement of what finished looks like, so a new member can run checkout alone with nobody to ask, and the model stopped padding because it finally had a reason to stop.
Image: Two bars, prompt length growing while reply length shrinks, in accent blue and navy.
---
## Slide 6: Format changes the most and gets added last
- p3 to p4: prose became five numbered steps
- Hedging went to zero
- Format has the most visible effect of the five
- People add it last, after spending revisions on adjectives
- Add it early and you find out whether the content holds
Speaker notes: This is the combination that costs people the most time. Format is the element with the biggest visible effect and it is the one students reach for last. So they spend four revisions on the role and on adjectives, conclude that prompting does not do much, and never get to the element that would have changed the output most. There is a second reason to add it early. A five item list is much harder to hide padding in than a paragraph, so you find out quickly whether the content is any good.
Image: A paragraph of prose on the left dissolving into five clean numbered lines on the right.
---
## Slide 7: The same task, with and without a role
```
[norole] 5 prompt words ... 110 reply words
Here are some thoughts on the Friday equipment checkout.

[role] 11 prompt words ... 95 reply words
As a club's equipment manager, here is how I would handle the Friday equipment
checkout.
```
Speaker notes: Two runs. The second one adds you are the club's equipment manager and changes nothing else. The opening sentence changed, and the reply is fifteen words shorter. Now I am going to scroll down past the opening line, and I want you watching the six procedure steps underneath.
Image: None. This slide is the recorded run.
---
## Slide 8: The role changed the framing and not the procedure
- The six procedure steps underneath are identical, word for word
- What changed is the opening sentence and the hedging
- Hedging dropped from four sentences to two
- That accounts for the whole fifteen word difference
- A role is real, and its effect is on voice
Speaker notes: If you were hoping the role would make the procedure more accurate, look at the procedure. It did not change at all. A role is a genuine element with a genuine effect, and the effect is on voice, confidence and framing. This matters for Gate two and for the exam. Claiming that a role improves accuracy is a claim you cannot support from any run you have made, and in here a claim you cannot support is worth nothing.
Image: Two reply cards with different opening lines and an identical highlighted block of six steps underneath both.
---
## Slide 9: The wrong way, and it is the revision everyone writes first
```
Please write a really good, detailed, professional explanation of the equipment
checkout process. Make it accurate and make sure it is clear. Thank you.

[adjectives] 24 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\adjectives.json

[p1_bare] 6 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\p1_bare.json
```
Speaker notes: Read the prompt out loud first and let them agree it sounds like effort. Then put the two run headers side by side. Twenty-four words of adjectives produced the same reply as six words of nothing, word for word, against this stub. Eighteen extra words about quality bought exactly no change.
Image: None. This slide is the recorded run.
---
## Slide 10: Count the elements in that prompt
- Role none. Task none. Context none
- Format none. Constraints none
- Every word in it is about quality in general
- It is tempting because it feels like effort
- The machine cannot act on the word professional
Speaker notes: Really good is not a finish line. Professional is not a shape. Make it accurate is not a fact, and there is no accuracy switch to turn on. That prompt is longer, politer, and uses serious words, and none of that is an element. Effort spent on adjectives is effort that did not go into the five. There is one more tempting mistake and it is tomorrow's whole lesson. You add three elements at once, get a much better reply, and call that a finding. It is a better prompt. It is not a finding.
Image: A prompt with every adjective highlighted in red and five empty element slots beside it.
---
## Slide 11: What you are about to build
- Lab M02-01 steps six through eleven, all five prompts
- Paste the compare_runs output into your write-up
- Three observations, each naming a countable difference
- Then the Prompt Autopsy: pick one real task
- Get the task approved before you write any prompts
Speaker notes: Build one is the lab, steps six through eleven. Five recorded runs, the comparison table pasted in, and three observations. An observation names a countable difference and the element that produced it, so reply words fell from a hundred and ten to sixty-five when I added a task statement. Not it got better. Build two is the Prompt Autopsy, handed out today. First fifteen minutes are Define. One task, something real from this building or from your own life, and three sentences in the decision log saying what the task is, who the output is for, and what finished looks like. Get it approved before you write prompts, because the most common failure in this project is a task too small to be worth five prompts.
Image: A decision log page with three sentences filled in and a control prompt file beside it.
---
