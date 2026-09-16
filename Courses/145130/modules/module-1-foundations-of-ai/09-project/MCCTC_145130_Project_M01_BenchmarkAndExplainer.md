# Performance Task: What Does a Local Model Actually Cost?
## 145130 Applications of AI · Module 1 · Weeks 1 to 3

**Mode:** solo, with one partner for the comparison. **Gate:** 3, full tooling.
**Due:** Week 3, Thursday, end of Build 2.
**Competencies:** 5.1.1 (how programs and scripts solve problems), 1.2.1 (extract
valid information and cite sources), 2.4.2 (architectures and integration),
2.14.1 (machine learning against decision trees), 2.14.4 (evaluate an AI result).

**Two deliverables, one brief:** a benchmark report and a one-page explainer.

---

## The brief

Read this as though a person said it to you, because this is how the request
actually arrives.

> We are being asked whether we can run one of these AI models on our own
> machines instead of sending anything outside the building. I think the answer is
> yes and I have no idea what it costs. Nobody has given me a number I can use.
>
> What I need from you is two things.
>
> First, tell me what it costs on our hardware. Not a number from a vendor. A
> number from this building, produced in a way that somebody else could repeat,
> with whatever caveats it needs. If you cannot measure something, say so rather
> than estimating it, because I am going to quote this to people who spend money.
>
> Second, I have to explain this to the board, and none of them have written a
> line of code. One page. If I read it out loud and somebody asks what the thing
> actually is, I need an answer that is true and that does not make me sound like
> I am selling something.

**This brief is a composite.** It was written for this course. The request is the
shape these requests take, and no specific person said these words.

**Notice what the client did not ask for.** They did not ask which model is best,
they did not ask for a recommendation, and they did not ask you to be impressive.
They asked for a number they can defend and a page they can read aloud.

---

## What you are handing in

```
benchmark-and-explainer/
  bench.py               finished, from the lab
  measure.py             the three functions you wrote
  compare_machines.py    finished, from the lab
  streaming_stub.py      finished, from the lab
  prompts/               the three prompt files, unchanged
  runs/                  every saved run, including your partner's
  report.md              the benchmark report
  explainer.md           one page, for one named adult
  decision-log.md        every decision you made and why
  README.md              how to reproduce every number in the report
```

---

## Requirements

### The benchmark report

1. **Three numbers per prompt:** median total latency, median time to first
   token, and tokens per second. Report the spread next to every median.
2. **A method section** covering all seven items: the prompt set, the repeat
   count, the warm-up policy, whether it streamed, how tokens were counted, the
   model and endpoint, and what else was running on the machine.
3. **A comparison against one classmate**, on an agreed method, with
   `compare_machines.py` output pasted. **If the program refused your comparison,
   paste the refusal and say what you changed.**
4. **Every number that could not be measured is reported as not measurable, with
   the reason.** No estimates in a numeric column.
5. **A section named "What these numbers do not establish."** At least three
   reasons, and they must be real ones.
6. **One sentence naming something other than the hardware that differed between
   your run and your classmate's.** There is always at least one.

### The explainer

7. **One page.** For one named adult who has never programmed. The name goes at
   the top of your draft and comes off before you submit.
8. **At most three technical words**, each defined on first use in words the
   reader already has.
9. **Every claim is one you could defend.** Any number in it is one you measured,
   and your report has the run.
10. **The word magic does not appear**, and neither do "it knows", "it thinks",
    or "it searches".

### Both

11. **A decision log.** Every choice you made, what you rejected, and why. The
    prompt set, the repeat count, the delay you gave the stand-in, the audience
    you chose.
12. **A README that lets somebody else reproduce every number**, including the
    exact commands with explicit ports.
13. **`AI_USAGE.md` updated** if you used a model at any point, including for the
    writing.

---

## Constraints, and why each exists

| You may not | Why |
|---|---|
| Report a number you did not measure | The client is going to quote this to people who spend money. |
| Use a package outside the standard library | The lab machines have only the standard library, and nothing here needs more. |
| Use a commercial AI service for any model work | Those services require their users to be 18 or older, and no student work leaves this building. |
| Present a stand-in server's numbers as a model's | The stand-ins exist to check the instrument. Saying so is most of the honesty in this report. |
| Compare two runs with different methods | A difference between them would be about the methods, and your reader cannot tell. |
| Write `error` as the whole of any message | Four different problems have four different fixes. |

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 1 Fri, end of Build 2 | One paragraph: what you will measure, and who the explainer is for, by name |
| **Measure** | Week 2 Mon to Fri | The list of every number you intend to report, with how you will produce each one |
| **Analyze** | Week 2 Fri to Week 3 Tue | The written method, everything another person would need to repeat your run, agreed with your partner before either of you measures |
| **Improve** | Week 3 Tue to Thu | Run it, read the warnings, tighten the method, run it again. Revise the explainer against your Week 2 markup |
| **Control** | Week 3 Thu, end of Build 2 | Report, explainer, decision log, README, every run saved |

**Analyze is the checkpoint that saves this project.** Two students who agree a
method on Tuesday produce a comparison. Two students who measure first and
compare afterwards produce two numbers and an argument.

---

## Milestone schedule, against actual class days

| Day | Goal |
|---|---|
| Week 1 Fri | Define paragraph written. Audience named |
| Week 2 Mon | Measure list started: every number, and how |
| Week 2 Fri | Measure list complete. Analyze method started |
| Week 3 Mon | `measure.py` passing 13 of 13. First two runs saved |
| Week 3 Tue | Method agreed in writing with your partner. Both runs done. Comparison run |
| Week 3 Wed | Report drafted. Explainer revised |
| Week 3 Thu | Everything submitted. Demo rehearsed |

---

## Three worked scope examples

These calibrate you. Do not build any of these three.

### Too small

> Run `bench.py` once against the stub and paste the table.

One run, no method, no comparison, no explainer, and the two `n/a` columns
unexplained. It answers none of what the client asked.

### About right

> Three prompts, three repeats, warm-up discarded, against the streaming stand-in
> at a known rate and against the anchor stub. A method agreed in writing with one
> partner before either of us ran anything, and a comparison with all three
> warnings read and addressed. A report with the spread next to every median, a
> section saying the stand-in numbers measure the instrument rather than a model,
> and three reasons the numbers do not establish anything about lab hardware. A
> one-page explainer for a named aunt, three technical words, every claim
> defensible.

Every requirement, at a size one person finishes and can explain. **This is the
bar.**

### Too big

> A web dashboard that benchmarks four models on eight prompts every hour,
> charts the results over time, and emails a weekly summary.

Four models you do not have, scheduling, charting, and email are each a project.
This is a good capstone idea and it is far too big for three weeks, and none of it
answers the client's two questions.

**The calibration question:** can you name, right now, the seven things in your
method section? If not, the core of this project is not designed yet.

---

## The 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Every number in the report was produced by a command in the README. `measure.py` passes 13 of 13. The comparison ran, or its refusal is pasted with what changed. |
| **Code Quality** | 20 | The three functions are correct including all `None` cases. Nothing invents a number. The README's commands pass explicit ports. |
| **Documentation** | 20 | The method section covers all seven items. The explainer meets requirements 7 to 10. The README reproduces the report. |
| **Process** | 15 | The decision log records what was rejected and why. The Analyze method was agreed before measuring, and the artifact shows it. |
| **Demonstration** | 10 | Five minutes, live, including one thing that did not work and what you did. |
| **Polish** | 10 | The report reads as something a coordinator could forward. No leftover placeholders, no unlabelled numbers. |

**The section that is worth the most for its size** is "What these numbers do not
establish." A report without it is a report that overstates, and overstating is
the failure this whole module is built to prevent.

---

## The five-minute demo

1. **What you measured and what you did not.** (45s)
2. **Your table, on screen, with the spread.** (60s)
3. **The comparison, including any warning you had to address.** (75s)
4. **One number you refused to report, and why.** (60s)
5. **Read two sentences of your explainer aloud.** (60s)

**Question you will be asked:** name one thing other than the hardware that
differed between your run and your partner's. Have the answer ready.

---

# INSTRUCTOR APPENDIX

## The reference implementation

`reference-implementation/benchmark/`, with its own README. Every run in it was
produced on the build machine and the commands are recorded.

**It is deliberately not a model project.** It has no `explainer.md` of
publishable quality and no partner comparison from a second machine, because
neither existed here. It exists to prove that every command in the student
requirements runs and produces what the requirements say it produces.

## The three ways this project goes wrong

**1. The student measures first and writes the method afterwards.**
*What you see:* a report whose method section describes what happened rather than
what was decided, and a comparison that `compare_machines.py` refused.
*The intervention:* Week 3 Tuesday's first 15 minutes, with no keyboards. Stand
over it. Two students who negotiate a method on Tuesday have a project; two who do
not have two numbers.

**2. The student treats `n/a` as a failure and fills it in.**
*What you see:* a tokens per second figure in a column that should be empty,
usually computed from total latency, and no note.
*The intervention:* ask where the number came from, then ask them to show you the
line in `measure.py` that produced it. There is not one, which means they
computed it by hand outside the program, which is worth the conversation.

**3. The explainer is written the night before and is full of the sentences the
module spent three weeks removing.**
*The intervention:* this is why the draft starts in Week 1 Wednesday. If a student
has no draft by Week 2 Friday, sit with them in Period 8 and get the audience
named and one paragraph written. The rest follows from the audience line.

## What to say to a team whose scope is too big

"Which of the client's two questions does the dashboard answer? Neither. Build the
thing that answers both, and put the dashboard in your decision log as something
you rejected, with the reason. That entry is worth marks and the dashboard is
not."

## What to say to a team whose scope is too small

"You have a table. The client asked for a number they can defend. Read your method
section out loud and ask whether I could reproduce your number from it. Then add
what is missing. That is the project."

## Grading notes

**Demonstration is scored at the desk for most students**, during Week 3
Wednesday and Thursday Build 2, using the five-point demo script. **Two students
give the full demo in the last 15 minutes of Thursday's Build 2**, named on
Wednesday so they can prepare. Every student needs a Demonstration score before
the module closes.

**A report that presents stand-in numbers as a model's numbers loses more than
Documentation.** It is a Process failure and a Polish failure too, and it is worth
saying so on the rubric rather than quietly deducting.

**If a real model runtime was available this year**, the bar moves: a report that
had access to real hardware and still reports only stand-in numbers has not done
the task. Say so at the start of Week 3.
