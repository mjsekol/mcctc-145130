# Revision Is a Controlled Experiment
## 145130 Applications of AI · Module 2 · Week 4, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W04_ChangeOneThing.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W04_ChangeOneThing.pptx)

**Competencies:** 2.14.3 (write and revise a prompt to generate the desired
response), 1.1.7 (apply problem-solving and critical-thinking skills when
formulating solutions).

---

## Why this exists

You now know five things you can change. That is the problem.

The natural move is to change three of them, get a much better reply, and stop.
You would have a better prompt and no knowledge. You could not tell anyone which
change mattered, you could not repeat the improvement on a different task, and if
the model gets swapped next semester you are back to guessing.

**This is the difference between getting a result and having a finding.** The
exit criterion for this module says you can take a vague request and produce a
prompt that gets usable output on the second try. On the second try, not the
eleventh. That only happens if you know which changes do what.

---

## The concept in plain language

Treat each prompt as a run of an experiment.

1. **Write the control.** The prompt you are starting from, unchanged.
2. **Change exactly one element.** Role, or task, or context, or format, or one
   constraint. One.
3. **Record both runs** with `ask.py`, under labels you will still understand next
   week.
4. **Compare on things you can count** before you compare on things you feel.
5. **Write down what changed and what you conclude**, in that order, and keep them
   separate.

That is it. It is the same discipline as changing one variable in a lab, and the
reason is the same: if you change two, the result cannot be attributed.

**Removing an element is as valid as adding one.** Take a prompt that works,
delete the role, and run it again. If the output is the same, the role was doing
nothing, and you have learned something no amount of adding would have told you.
That is called an **ablation**, and it is Side Quest 18.

---

## Worked example 1 · Why you cannot do this from memory

Do this before you read further. It takes four minutes and it is the point of the
lesson.

```
python ask.py --prompt-file demo-prompts/loose_json.txt --label a
python ask.py --prompt "Explain the Friday equipment checkout in bullets, under 40 words." --label b
python ask.py --prompt "You are the club's equipment manager. Explain the Friday equipment checkout." --label c
```

Close the terminal. Wait until the end of the block. Now write down, without
looking: which one was shortest, which one had a role, and which one produced a
list.

Then look:

```
python compare_runs.py runs
```

Most people get one of the three right. **This is not a memory problem you can
train away.** It is why the recording step is not optional bureaucracy.

---

## Worked example 2 · One change, attributed

Control:

```
python ask.py --prompt "Explain the Friday equipment checkout." --label ctrl --show
```

Change exactly one element, Format:

```
python ask.py --prompt "Explain the Friday equipment checkout. Give me 5 steps in a numbered list." --label fmt --show
python compare_runs.py runs --show ctrl fmt
```

| Label | Reply words | Shape | List items | Hedges |
|---|---|---|---|---|
| ctrl | 110 | prose | 0 | 5 |
| fmt | 63 | numbered | 5 | 0 |

**The finding you may write:** adding a format instruction with a count cut the
reply from 110 words to 63, removed every hedging phrase, and produced five
discrete items.

**The finding you may not write:** "the format instruction made it better." That
is a judgement about usefulness, which depends on who is reading it and for
what. Say it if you mean it, and say it separately, after the counts.

---

## Worked example 3 · The change that changed nothing

```
python ask.py --prompt "Explain the Friday equipment checkout. Be thorough and professional." --label adj
```

| Label | Reply words | Shape | List items | Hedges |
|---|---|---|---|---|
| ctrl | 110 | prose | 0 | 5 |
| adj | 110 | prose | 0 | 5 |

**Every column is identical.** The replies are not quite the same text: two
sentences are in a different order. Nothing else moved.

That distinction matters. A difference your comparison table cannot see, and that
you cannot attribute to any element, is not a finding. It is noise, and the honest
thing to write down is that the change produced no measurable difference and one
unattributable one.

**A change that produces no difference is a result.** It tells you that the
element you thought you added was not one, and writing it down stops you and
everybody who reads your work from spending another twenty minutes on adjectives.

Students routinely throw these runs away because they feel like failures. Keep
them. In an ablation table, the rows that do not move are the interesting ones.

---

## The wrong version, and the exact failure

Here is the run that looks like the most productive twenty minutes of the week:

```
python ask.py --prompt "You are the club's equipment manager. Write the instructions a new member needs to run Friday checkout alone. Exactly 5 numbered steps, under 60 words, no introduction." --label great --show
```

```
1. Match the serial number on the case to the number on the sheet.
2. Open the checkout sheet before anyone lines up.
3. Write the borrower's grade level, not their schedule.
4. Photograph any damage before the item leaves the room.
5. Set the return slot to the next school day, first period.
```

Fifty-four words, five clean steps, no padding, no introduction. It is the best
output of the week so far.

**It is also in the wrong order.** Step 1 matches a serial number against a sheet
you do not open until step 2. Nothing in the comparison table can see that, and
neither can you unless you read it as somebody who has to follow it. Hold that
thought until Week 5.

Now answer the question your decision log asks: **which change produced that?**

You cannot. You changed four things at once: role, task, format, and two
constraints. The reply is better than the control and you have no idea which part
of it was load-bearing. If the word cap was doing all the work, you do not know.
If the role was doing nothing, you do not know that either.

**Why this is tempting.** It is faster, and the output is better sooner. Both of
those are true. The cost arrives later, when somebody asks you to do it again on
a different task and you have to start from zero.

**The fix is small.** Keep the good prompt as the destination. Then run four more
prompts, each with exactly one of the four changes removed:

| Run | What is missing | Reply words | Shape |
|---|---|---|---|
| great | nothing | | |
| great minus role | the role line | | |
| great minus format | "numbered, 5 steps" | | |
| great minus cap | "under 60 words" | | |
| great minus no-intro | "no introduction" | | |

Five runs and every change is attributed. **That is SQ-18, and it is the best
hour you can spend on this skill.**

---

## Labels you will still understand next week

`test`, `test2`, `final`, `finalreal`, `asdf`. Every one of those will be
meaningless to you on Friday and you will rerun the work.

Use a label that names the change:

```
ctrl
ctrl_plus_role
ctrl_plus_format5
ctrl_plus_cap60
ctrl_plus_role_and_format
```

The last one is allowed as long as the name says it is two changes, so that
nobody, including you, mistakes it for an attributable result.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Control** | The run you are comparing everything against |
| **Variable** | The one element you changed this run |
| **Ablation** | Removing one element from a working prompt to see what it was doing |
| **Attribution** | Being able to say which change produced which difference |
| **Confound** | Two changes at once, so no difference can be attributed to either |
| **Null result** | A change that produced no difference. Still a result |

---

## Self-check

**1.** You change the role and the word cap in one run and the reply gets much
shorter. A classmate says "so the word cap works." What is wrong with that, and
what is the cheapest experiment that settles it?

<details><summary>Answer</summary>

It might be the cap. It might be the role, since a role can reduce hedging on its
own, which you saw on Tuesday. Two changes, one difference, no attribution.

**Cheapest experiment:** one more run, with the cap and no role. If it is still
short, the cap is doing it. One run, not a redo.
</details>

**2.** Your ablation shows that removing the role line changes nothing at all.
What do you write in the table, and what would be dishonest to write?

<details><summary>Answer</summary>

**Write:** removing the role produced no measurable change in length, shape, or
hedging on this task against this model.

**Dishonest:** "roles do not matter." You tested one role, on one task, against
one model, once. The scope of the claim has to match the scope of the evidence,
and this is the single most common way a true measurement becomes a false
statement.
</details>

**3.** Why is a run that produced no change worth recording, when the whole point
is to find changes?

<details><summary>Answer</summary>

Because it rules something out, and ruling things out is most of what an
experiment does. It also stops the next person repeating it.

There is a second reason that matters more in this course. If you only record the
runs that worked, your table is evidence for a conclusion you already had. That
is the same failure the bias lesson describes on Week 5 Thursday, applied to your
own work.
</details>
