# Revision Is a Controlled Experiment
---
## Slide 1: It got better and you cannot say what did it
- You change three things and the reply improves
- You now have a better prompt and no knowledge
- You cannot repeat it on a different task
- The model gets swapped and you are guessing again
Speaker notes: You now know five things you can change, and that is the problem. The natural move is to change three of them, get a much better reply, and stop. That is the difference between getting a result and having a finding. The exit criterion for this module says you can take a vague request and produce a prompt that gets usable output on the second try. On the second try, not the eleventh. That only happens if you know which changes do what.
Image: A prompt with three edits made at once and a single arrow to a better reply, with a question mark over which edit caused it.
---
## Slide 2: Treat every prompt as a run of an experiment
- Write the control, unchanged
- Change exactly one element
- Record both runs under labels you will still understand
- Compare on things you can count before things you feel
- Write what changed, then separately what you conclude
Speaker notes: This is the same discipline as changing one variable in a chemistry lab, and the reason is identical. Change two and the result cannot be attributed to either. Notice the fourth line especially. Countable first, judgement second, and kept apart on the page. And notice that removing an element counts. Take a prompt that works, delete the role, run it again, and if the output is the same then the role was doing nothing. No amount of adding would have told you that.
Image: Five numbered steps in a vertical column, the middle one boxed and labelled one element only.
---
## Slide 3: Why you cannot do this from memory
- Run three prompts, close the terminal, wait an hour
- Write down which was shortest and which had a role
- Most people get one of the three right
- This is not a memory problem you can train away
Speaker notes: Do this before you believe me. Run three prompts this morning, close the terminal, and at the end of the block write down without looking which one was shortest, which one had a role, and which one produced a list. Then open compare_runs and check. Most of you get one of three. That is not carelessness and it is not a study skills problem. It is why the recording step is not optional bureaucracy, and it is why your labels matter more than you think.
Image: Three unlabelled terminal windows fading out, with a recall sheet beside them mostly blank.
---
## Slide 4: One change, attributed
```
python ask.py --prompt "Explain the Friday equipment checkout." --label ctrl --show
python ask.py --prompt "Explain the Friday equipment checkout. Give me 5 steps in a numbered list." --label fmt --show

| Label | Reply words | Shape | List items | Hedges |
|---|---|---|---|---|
| ctrl | 110 | prose | 0 | 5 |
| fmt | 63 | numbered | 5 | 0 |
```
Speaker notes: Two runs. One element different between them, which is format with a count. Everything else is identical, word for word, and I want you to see that in the prompts before you look at the table. Now read the table. Reply words, shape, list items, hedges. Four columns, three of them moved.
Image: None. This slide is the recorded run.
---
## Slide 5: What you may write, and what you may not
- May write: a format instruction cut 110 words to 63
- May write: every hedging phrase gone, five discrete items
- May not write: the format instruction made it better
- Better depends on who is reading it and for what
- Say it if you mean it, separately, after the counts
Speaker notes: The first two are measurements. Anybody can check them by opening your recorded runs. The third one is a judgement about usefulness, and usefulness depends on a reader and a purpose that the table knows nothing about. You are allowed to say it. You say it in a different sentence, after the counts, so a reader can tell which part is evidence and which part is you. That separation is most of what Written and Documentation is worth in this course.
Image: Two panels labelled what the table says and what I think, with a hard rule between them.
---
## Slide 6: The change that changed nothing
```
python ask.py --prompt "Explain the Friday equipment checkout. Be thorough and professional." --label adj

| Label | Reply words | Shape | List items | Hedges |
|---|---|---|---|---|
| ctrl | 110 | prose | 0 | 5 |
| adj | 110 | prose | 0 | 5 |
```
Speaker notes: Every column is identical. Not close. Identical. The two replies are the same text. Sit with that for a second, because your instinct right now is that this run was wasted and should be deleted before anybody sees it.
Image: None. This slide is the recorded run.
---
## Slide 7: A change that produced nothing is a result
- It tells you the element you added was not an element
- It stops the next person spending twenty minutes on adjectives
- Students throw these runs away. Keep yours
- In an ablation table the flat rows are the interesting ones
Speaker notes: Write it down and keep it. A null result rules something out, and ruling things out is most of what an experiment does. There is a second reason and it matters more in this course. If you only record the runs that worked, your table is not evidence, it is a collection of support for a conclusion you already had. That is the same failure the bias lesson describes on Thursday of next week, applied to your own work.
Image: An ablation table with one flat row highlighted in accent blue rather than greyed out.
---
## Slide 8: The wrong way, and it looks like the best work of the week
```
python ask.py --prompt "You are the club's equipment manager. Write the instructions a new member needs to run Friday checkout alone. Exactly 5 numbered steps, under 60 words, no introduction." --label great --show

1. Match the serial number on the case to the number on the sheet.
2. Open the checkout sheet before anyone lines up.
3. Write the borrower's grade level, not their schedule.
4. Photograph any damage before the item leaves the room.
5. Set the return slot to the next school day, first period.
```
Speaker notes: Fifty-four words. Five clean steps. No padding, no introduction. It is the best output of the week so far and everybody in the room can see it. Read step one and step two again, slowly, as somebody who has to follow them.
Image: None. This slide is the recorded run.
---
## Slide 9: Two problems, and the second one is worse
- Step one matches a sheet you do not open until step two
- Nothing in the comparison table can see that
- You changed four things at once in that prompt
- Role, task, format, and two constraints
- If the word cap did all the work, you do not know
Speaker notes: The ordering problem is real and no counter in your table will ever catch it. You catch it by reading the output as the person who has to follow it, and we come back to that next week. Now the second problem. Your decision log asks which change produced that reply, and you cannot answer. Four things moved at once. The reply is better than the control and you have no idea which part of it was load bearing. Why is this tempting? It is faster and the output is better sooner. Both of those are true. The cost arrives later, when somebody asks you to do it again on a different task.
Image: An arrow from a four-change prompt to a good reply, with the arrow split into four unlabelled strands.
---
## Slide 10: The fix is five runs, not a redo
- Keep the good prompt as the destination
- Run four more, each with exactly one change removed
- Great minus role, minus format, minus cap, minus no-intro
- Five runs and every change is attributed
- That is an ablation, and it is Side Quest 18
Speaker notes: You do not throw the good prompt away. You keep it as the destination and you work backwards from it. Remove the role and run it. Remove the format and run it. Four ablation runs and now every one of your four changes has a number attached to it. One more thing, and it costs you nothing. Name your runs after the change. Ctrl, ctrl plus role, ctrl plus cap sixty. Test, test two, final and finalreal are meaningless to you by Friday and you will rerun the work.
Image: A five-row ablation table with the missing element named in each row.
---
## Slide 11: What you are about to build
- Lab M02-01 steps twelve through sixteen, the ablation
- Four ablation runs, each labelled with what is missing
- Every row completed, including the rows that did not move
- One sentence naming which element did the most work
- Then Prompt Autopsy prompts two and three, recorded
Speaker notes: Build one is the ablation. Take your best prompt from yesterday and remove one element at a time. Acceptance is at least four recorded runs, the table completed including any row where nothing changed, and one sentence naming which element was doing the most work with the evidence for it. Build two is the autopsy, prompts two and three, each materially different from the control and each recorded. Every prompt file gets committed before its run, and your decision log names what changed between each pair and why you chose that change. Side Quest 18, Prompt Ablation, unlocks today in Period 8 and it is the best hour available on this skill.
Image: A repository showing four ablation prompt files and four matching recorded runs, paired by name.
---
