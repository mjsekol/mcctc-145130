# Performance Task: The Prompt Autopsy
## 145130 Applications of AI · Module 2 · Assigned Week 4 Tuesday · Due Week 5 Tuesday

**Competencies:** PRIMARY 2.14.3 (write and revise a prompt to generate the
desired response). SUPPORTING 2.14.4 (evaluate an AI result), 1.1.7
(problem-solving and critical thinking), 1.2.5 (communicate for an intended
audience and purpose).

**Grade category:** Projects, 35 percent of the course grade.

---

## The brief

> From: the Media Club advisor
>
> I keep hearing that the way you ask matters more than which model you use, and
> I have no idea whether that is true or whether it is something people say.
>
> Here is what I actually need. Pick something we really have to write in this
> club, something that takes a person real time. Then find out how much of the
> quality of what comes back is under our control, and tell me what to do about it.
>
> I do not need a demonstration that AI can write things. I know it can. I need to
> know which part of asking is doing the work, so that the next person does not
> spend an afternoon rewording.
>
> Give me something I can hand to a new member.

**That is the whole request.** Notice what it does not say: which task, what
counts as quality, how many prompts, or what the deliverable looks like. **Working
out what she actually needs is part of the assessment**, and it is scored under
Process.

---

## What you are building

**One task. Five materially different prompts. A documented comparison.**

Not five rewordings. Five prompts that differ in ways you can name, so that the
differences between their outputs can be attributed to something.

---

## Required repository structure

```
prompt-autopsy/
  prompts/
    v1_<what it is>.txt      through v5, names say what each one is
  runs/                       recorded by ask.py, one JSON per run
  autopsy.md                  the comparison and the analysis
  decisions.md                the decision log
  handout.md                  the one page for a new member
  README.md                   how to reproduce every run
```

---

## DMAIC checkpoints

This project runs on the same framework as every project in this program.

| Phase | When | What lands |
|---|---|---|
| **Define** | Week 4 Tue, Build 2 | The task, the audience, and what finished looks like, in three sentences. Approved before you write prompts |
| **Measure** | Week 4 Wed, Build 2 | The control prompt and two more, recorded. The comparison table started |
| **Analyze** | Week 4 Thu, Build 2 | All five recorded. The table complete. Which element produced which difference |
| **Improve** | Week 4 Fri, Build 2 | The written analysis, and a sixth prompt built from what you learned |
| **Control** | Week 5 Mon, Build 1 | The handout, the README, and the reproduction check |

**Agile ceremonies live inside Improve**, as they do in every project in this
program. Friday's Build 2 opens with a five-minute standup: finished, working on,
blocked by.

---

## Milestones

| Week and day | Due at the end of the block |
|---|---|
| Week 4 Tue | Task approved. Three-sentence Define in `decisions.md`. Control prompt recorded |
| Week 4 Wed | Three prompts recorded. Comparison table started |
| Week 4 Thu | Five prompts recorded. Table complete. One decision-log entry per prompt |
| Week 4 Fri | Written analysis: four or more observations, each attributing a countable difference to one element |
| **Week 5 Mon** | **Everything pushed by the end of Build 1.** Desk checks run during this block |
| Week 5 Tue | The partner exchange, in Build 2. Late work is graded here at a penalty |

---

## Technical requirements

1. **One task**, held constant across all five prompts. If the task changes, the
   comparison means nothing.
2. **Five prompts that differ materially.** For each pair, you can name what
   changed in four words or less. Rewordings do not count.
3. **Every prompt in its own file, committed before its run.** A prompt written
   after seeing the output is not a prediction, it is a memory.
4. **Every run recorded with `ask.py`.** No pasted-from-the-screen outputs. The
   run files are the evidence.
5. **A comparison table produced by `compare_runs.py`**, pasted verbatim.
6. **At least four written observations**, each naming a countable difference and
   attributing it to exactly one element.
7. **At least one recorded null result**: a change that produced no measurable
   difference.
8. **A sixth prompt**, built from what the first five taught you, with a
   prediction written before you run it and a comparison to what actually happened.
9. **A one-page handout** a new club member could use without you in the room.
10. **A README that reproduces every run**, including the endpoint and how to start
    the stub.

---

## Constraints, and why each one exists

**The model runs on a machine in this building.** Commercial developer APIs require
the account holder to be 18 or older. No account, no key, nothing leaves.

**No personal data in any prompt file.** `ask.py` records your prompt verbatim into
a file you commit and push. Whatever you type is published. Use Ava Ruiz and Kai
Mendoza.

**The task must be one where you can tell whether the output is usable.** You are
the person who would use it, or you can ask the person who would. A task you cannot
evaluate produces an autopsy with no findings.

**The task must be real.** Something the club, a team, a job, or you actually has
to write. An invented task produces invented quality judgements.

**Prompt files are committed before their runs.** This is the version control
discipline the whole program runs on, and here it does real work: it is the only
thing that distinguishes a prediction from a story about a prediction.

---

## Three worked scope examples

### Too small

> **Task:** write the caption for one Instagram post about a game.
>
> Five prompts, five captions, and by prompt three there is nothing left to
> change. The output is twelve words, so every countable difference is one or two
> words, and the comparison table has nothing in it.

**Why it fails:** the output is too short to carry a measurable difference. If your
longest reply is under thirty words, the table cannot show you anything and your
observations will be about wording, which is taste.

**How to fix it without starting over:** widen the task to the thing the caption is
part of. A week of captions, or the caption plus the alt text plus the post text,
gives you output with structure in it.

### Right sized

> **Task:** the equipment checkout instructions a new member needs to run Friday
> checkout alone, with nobody in the room to ask.
>
> Output is between forty and a hundred and twenty words. There is a shape
> (sequence of steps), a content requirement (the things that must be mentioned),
> an audience (somebody who has never done it), and a way to tell whether it worked
> (hand it to a new member and watch).

**Why it works:** long enough to differ measurably, short enough to read five
versions in a block, and the quality question has an answer that is not taste.

**Other tasks at this size:** a practice-plan summary for a teammate who missed;
the description field for a robotics build log entry; the "what we need from you"
section of a sponsorship email; the instructions for setting up the camera for a
livestream; a shift-swap request that actually gets answered.

### Too big

> **Task:** write the club's yearbook section.
>
> Five prompts, five multi-page outputs, and you spend the whole of Week 4 reading
> instead of comparing. The comparison table is meaningless because the outputs
> differ in a hundred ways at once.

**Why it fails:** with enough output, every pair of runs differs everywhere, so
nothing can be attributed. This is the same problem as changing three elements at
once, arriving from the other direction.

**How to fix it without starting over:** take one section of it. The same five
prompts on one section give you a real result, and you can say in your analysis
that you expect it to hold for the rest and that you did not test that.

---

## The 100-point project rubric

| Dimension | Points |
|---|---|
| Functionality | 25 |
| Code Quality | 20 |
| Documentation | 20 |
| Process | 15 |
| Demonstration | 10 |
| Polish | 10 |

**What each means here:**

**Functionality, 25.** Five materially different prompts on one held-constant task.
Every run recorded. The comparison table produced from the run files. The sixth
prompt with a prediction made before the run.

**Code Quality, 20.** Prompt files named for what they are. Run labels that still
mean something next week. The README reproduces every run on a machine that is not
yours. No personal data anywhere.

**Documentation, 20.** `autopsy.md` with four or more attributed observations and
one null result. `decisions.md` with an entry per prompt. The handout is one page
and is written for a new member, not for the instructor.

**Process, 15.** Define approved before prompts were written. Prompt files
committed before their runs, visible in the history. DMAIC checkpoints hit on the
days in the milestone table. The decision log records what you changed and why,
including the changes that did not work.

**Demonstration, 10.** Scored at a desk check during Week 5 Monday's Build 1 or in
the Week 5 Tuesday exchange. Five minutes, using the demo script below.

**Polish, 10.** The handout could be handed to somebody. The table is readable.
The analysis says what it knows and what it does not.

---

## The five-minute demo script

Time it. Five minutes goes quickly and the last section is the one that gets cut,
so practise it first.

**0:00 to 0:30 · The task.** What you picked and why it is a real thing somebody
has to write. One sentence on how you can tell whether the output is usable.

**0:30 to 1:30 · The control and the worst one.** Show prompt 1 and its reply.
Read two lines of the reply aloud. Say what is wrong with it in one sentence.

**1:30 to 3:00 · The table, and one attribution.** Put the comparison table up.
Pick **one** difference and walk it: these two prompts differ by this element, this
column moved by this much, so this element produced that. **One, in detail, beats
five in a rush.**

**3:00 to 3:45 · The null result.** The change that did nothing. Say what you
expected, what happened, and what you now know that you did not know before.

**3:45 to 4:30 · The sixth prompt.** Your prediction, then what actually happened.
**If your prediction was wrong, say so.** A wrong prediction that was written down
in advance scores better than a right one that was not.

**4:30 to 5:00 · What you would tell the next person.** One sentence, the one from
your handout.

**The question you will be asked:** what is the scope of your main claim? Have the
answer ready. It is the sentence that starts "on this task, against this model."

---

## If you are stuck

**"I cannot pick a task."** Answer this instead: what did you or somebody near you
have to write in the last month that took longer than it should have? That is your
task. If nothing comes, take the equipment checkout task from the worked example
and say in your decision log that you did.

**"My five prompts are all basically the same."** Put the five-element table next
to them and say out loud, for each pair, which element changed. If you cannot say
it in four words, it did not change.

**"Nothing I change makes any difference."** Two possibilities and they need
different fixes. Either the change is not arriving in a form the model acts on, in
which case make it larger and more explicit, or the element genuinely is not doing
anything on this task, in which case **write it down as a null result and move to
the next element.** Do not keep pushing on the one that does nothing.

**"My comparison table shows differences but I cannot say why."** You changed more
than one thing between those two prompts. Find a pair that differs by exactly one,
and if there is no such pair, make one. It is one extra run.

**"I am behind."** The Define and the five recorded runs are the spine. Cut the
handout to half a page and cut one observation before you cut a run.

---

## Submission

- [ ] `prompt-autopsy/` in your repository with the structure above
- [ ] Five prompt files plus the sixth, each committed before its run
- [ ] At least six recorded runs in `runs/`
- [ ] `autopsy.md`: the table pasted verbatim, four or more attributed
      observations, one null result, the sixth-prompt prediction and outcome, and a
      scoped conclusion
- [ ] `decisions.md`: an entry per prompt
- [ ] `handout.md`: one page, for a new member
- [ ] `README.md`: reproduces every run, names the endpoint, says how to start the
      stub
- [ ] No personal data in any file
- [ ] Pushed by the end of Week 5 Monday's Build 1
- [ ] AI usage log updated
