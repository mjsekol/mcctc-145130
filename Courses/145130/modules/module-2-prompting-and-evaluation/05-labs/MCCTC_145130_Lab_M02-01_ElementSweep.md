# Lab M02-01: The Element Sweep
## 145130 Applications of AI · Module 2 · Week 4, Monday to Thursday

**Gate:** 3 (open). Full tooling. Decision log required.
**Duration:** four blocks across Week 4. Part 1 Monday Build 2, Part 2 Tuesday
Build 1, Part 3 Wednesday Build 1, Part 4 Thursday Build 1.
**Competencies:** PRIMARY 2.14.3 (write and revise a prompt to generate the
desired response). SUPPORTING 1.1.7 (problem-solving and critical thinking),
2.14.4 (evaluate an AI result).

**Files:** `lab-m02-01-files/plan_check.py`. Toolkit in `prompt-toolkit/`.

---

## The scenario

The Media Club's study hall wants a tool that turns a topic into a short study
plan. Somebody has already tried it, got a wall of vague text, and decided the
model is not good enough. **They changed the prompt four times and never wrote
down what they changed.**

Your job is to find out which parts of a prompt actually move the output, with
evidence, so that the next person does not have to guess.

## What you will build

A recorded sweep of five prompts, an ablation table that attributes each
difference to one element, and a program that decides whether a model reply is
usable before it trusts it.

---

# Before you start

Two terminals. **Terminal 2 holds the stub and stays open.**

```
cd 05-labs/prompt-toolkit
python stub_model_server.py
```

```
Stub model server on http://127.0.0.1:11434 in success mode. Press Ctrl+C to stop.
Every source this server produces is invented. None of them are real.
```

In Terminal 1, work from `05-labs/lab-m02-01-files/`.

**Read this before you write a single prompt file.** `ask.py` records your prompt
verbatim into a file you commit. **No personal data in any prompt file.** Not a
name, not an ID, not a grade, not a schedule. Use Ava Ruiz and Kai Mendoza if you
need a person.

---

# PART 1 · Monday Build 2 · Five prompts, one element at a time

**The task, for all five prompts:** produce a study plan for the topic "how a hash
table handles a collision," good enough that a classmate who missed the lesson
could use it.

Make a folder `prompts/`. Write five files. **Each one adds exactly one element to
the one before it.**

**Step 1.** `prompts/p1_bare.txt`. The question and nothing else. One line, under
ten words.
**Result you should see:** a file you would be slightly embarrassed to submit.
That is correct. It is the control.

**Step 2.** `prompts/p2_task.txt`. Add the **task**: what finished looks like and
who it is for. Do not add a role, a format, or a constraint.
**Result:** the file is three or four times longer than p1 and still has no
instructions about shape.

**Step 3.** `prompts/p3_role.txt`. Everything in p2, plus a **role** line.
**Result:** exactly one new sentence compared to p2. If you changed anything else,
delete it.

**Step 4.** `prompts/p4_format.txt`. Everything in p3, plus a **format**: a shape
and a count.
**Result:** one new sentence again.

**Step 5.** `prompts/p5_constrained.txt`. Everything in p4, plus **constraints**: a
word cap, and one thing it may not do.
**Result:** five files, each differing from the last by one element. Open them
side by side and check. **This is the part people get wrong, and it is the part
everything else depends on.**

### Acceptance criteria, Part 1

- [ ] Five prompt files, committed **before** any run
- [ ] Each filename says what it adds
- [ ] Any two consecutive files differ by exactly one element
- [ ] No personal data in any file
- [ ] A `decisions.md` with one line per prompt saying which element you added

---

# PART 2 · Tuesday Build 1 · Run them and count

**Step 6.** Run all five.

```
python ../prompt-toolkit/ask.py --prompt-file prompts/p1_bare.txt --label p1 --runs-dir runs
```

Repeat for p2 through p5, changing the file and the label.
**Result:** five files in `runs/` and five rows in `runs/run_log.md`.

**Step 7.** Build the table.

```
python ../prompt-toolkit/compare_runs.py runs
```

**Result:** a markdown table. Paste it into `sweep.md` exactly as printed.

**Step 8.** Read the table before you read any reply. Answer in `sweep.md`:
which prompt produced the longest reply, and was it the longest prompt?
**Result:** for most people the answer is no, and it surprises them.

**Step 9.** Now read the replies.

```
python ../prompt-toolkit/compare_runs.py runs --show p1 p5
```

**Result:** two full replies printed under the table.

**Step 10.** Write three observations in `sweep.md`. **Each one names a countable
difference and attributes it to exactly one element.**

A good observation:

> Adding the format instruction in p4 changed the Shape column from prose to
> numbered and dropped the Hedges column from 5 to 0. The only difference between
> p3 and p4 is the format sentence.

A bad observation:

> p4 was better.

**Step 11.** Write one sentence in `sweep.md` about a column that did **not**
change between two runs, and what that tells you.
**Result:** a null result, recorded on purpose. You will need it in Part 3.

### Acceptance criteria, Part 2

- [ ] Five recorded runs in `runs/`
- [ ] The comparison table pasted verbatim into `sweep.md`
- [ ] Three observations, each naming a countable difference and one element
- [ ] One recorded null result
- [ ] Committed

---

# PART 3 · Wednesday Build 1 · Take it apart

An **ablation** starts from a prompt that works and removes one element at a time.
Adding tells you what an element contributes on top of nothing. Removing tells you
what the whole prompt would lose without it, which is the question you actually
have.

**Step 12.** Copy `prompts/p5_constrained.txt` to `prompts/best.txt`. This is your
new control.

**Step 13.** Make four files, each a copy of `best.txt` with exactly one element
**deleted**: `no_role.txt`, `no_task.txt`, `no_format.txt`, `no_constraints.txt`.
**Result:** four files, each shorter than `best.txt` by one element.

**Step 14.** Run all five, labelled `best`, `no_role`, `no_task`, `no_format`,
`no_constraints`.
**Result:** five more rows in the table.

**Step 15.** Build the ablation table in `sweep.md`:

| Run | Element removed | Reply words | Shape | Items | Hedges | What changed |
|---|---|---|---|---|---|---|
| best | none | | | | | control |
| no_role | role | | | | | |
| no_task | task | | | | | |
| no_format | format | | | | | |
| no_constraints | constraints | | | | | |

**Every row gets filled in, including the rows where nothing moved.** A row of
"no change" is a result and it is the most useful row in the table.

**Step 16.** Write your conclusion in `sweep.md`: **which element was doing the
most work, and what is your evidence?**

Then write the scope of that claim. Not "roles do not matter." Something like: on
this task, against this model, removing the role changed nothing measurable in
length, shape, or hedging. **The scope of the claim has to match the scope of the
evidence.** This is the single most common way a true measurement becomes a false
statement.

**Step 17.** If a removal changed nothing and you expected it to, check whether
the element was ever there in a form the machine could act on:

```
python -c "import urllib.request,urllib.parse; q=urllib.parse.urlencode({'prompt': open('prompts/best.txt',encoding='utf-8').read()}); print(urllib.request.urlopen('http://127.0.0.1:11434/stub/parse?'+q).read().decode())"
```

**Result:** a list of what the stub detected. If the element you thought you wrote
is `null` there, that is your answer. **That endpoint exists only on the stub.** A
real model will not tell you, and you will be back to changing one thing at a time.

### Acceptance criteria, Part 3

- [ ] Five ablation runs recorded with the labels above
- [ ] The ablation table complete, including no-change rows
- [ ] A conclusion naming one element, with evidence
- [ ] The scope of that claim written out
- [ ] Committed

---

# PART 4 · Thursday Build 1 · Output a program can use

Open `plan_check.py`. **Read the whole file before you change anything.** It runs
and it is wrong in one specific, documented way.

**Step 18.** Run it both ways.

```
python plan_check.py "how a hash table handles a collision"
python plan_check.py --loose "how a hash table handles a collision"
```

**Result, the strict version:**

```
reply in 0.03s, 57 words
OK: a study plan for a unit exam
  1. Write down what the exam actually covers before planning anything
  ...
```

**Result, the loose version:**

```
reply in 0.04s, 60 words
UNUSABLE: the reply is not JSON
------------------------------------------------------------
As a study skills teacher, here is how I would handle a study plan for a unit exam.

{
  "topic": "a study plan for a unit exam",
...
```

Look at what the loose version returned. **There is JSON in there.** The parser
never reached it, because it read `A` from "As a study skills teacher" and
stopped. Read `build_prompt` and find the four words that are the entire
difference.

Record both runs in `sweep.md`.

**Step 19.** Write `usable()`. The docstring lists the five things it must catch.
**Result:** the function returns an error message for a bad reply and `None` for a
good one.

**Step 20.** Test it without calling the model at all:

```
python -c "
import plan_check as p
print(p.usable('not an object'))
print(p.usable({'steps': ['a','b','c','d']}))
print(p.usable({'topic': 'x', 'steps': 'soon'}))
print(p.usable({'topic': 'x', 'steps': ['a','b']}))
print(p.usable({'topic': 'x', 'steps': ['a','b','c','  ']}))
print(p.usable({'topic': 'x', 'steps': ['a','b','c','d']}))
"
```

**Result:** five different error messages, then `None`. If any of the first five
prints `None`, that case is not caught yet.

**Step 21.** Break the model on purpose and record what your program does. In
Terminal 2, restart the stub in each mode, then rerun `plan_check.py`:

| Mode to run the stub in | What you should see | Exit code |
|---|---|---|
| `--mode error` | the server answered HTTP 500 | 3 |
| `--mode malformed` | the reply is not valid JSON | 4 |
| `--mode missing_response` | the reply has no 'response' field | 5 |
| `--mode not_done` | the reply is not marked done | 5 |
| `--mode empty_response` | the reply is empty | 5 |
| stub stopped entirely | nothing is listening | 2 |

Check an exit code with `echo %ERRORLEVEL%` in cmd, or run
`python plan_check.py "x"; echo $?` in Git Bash.

**Result:** a table in `sweep.md` of mode against what you saw. **Three of those
modes return HTTP 200.** Write one sentence about why that matters.

### Acceptance criteria, Part 4

- [ ] Both runs from step 18 recorded, with the four-word difference named
- [ ] `usable()` catches all five cases and approves a correct reply
- [ ] The step 20 output pasted
- [ ] The failure-mode table filled in from runs you actually did
- [ ] One sentence on why an HTTP 200 failure is the dangerous kind
- [ ] Committed and pushed

---

## If it breaks

**`FAILED (nothing is listening at http://127.0.0.1:11434)`**
The stub is not running, or Terminal 2 is on a different port. Start it again. On
Windows, closing the terminal tab is what stops it.

**`OSError: [WinError 10048] Only one usage of each socket address ... is normally permitted`**
Something is already on port 11434, usually a stub you forgot about. Use
`--port 11500` and pass `--endpoint http://127.0.0.1:11500` to every command.

**`json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`**
You are handing a reply to a JSON parser and the reply starts with a sentence.
That is step 18 and it is the lesson, not a bug in your code.

**`ModuleNotFoundError: No module named 'ask'`**
You are running `plan_check.py` from the wrong folder, or you moved it. It finds
the toolkit relative to its own location, so run it from
`05-labs/lab-m02-01-files/`.

**Everything prints `None` in step 20.**
You have not written `usable()` yet, or you wrote it and it returns `None` on
every path. Read the docstring again and check the `steps` type before you check
its length.

---

## Stretch goal

Make `plan_check.py` retry once with a stricter prompt when the first reply is
unusable, then give up. Two rules: **say in the output that it is retrying**, so a
user is never silently waiting through two calls, and **never retry more than
once**, because a model that produced garbage twice will produce it a third time
and you are spending somebody's afternoon.

Record in `sweep.md` how many of the failure modes from step 21 a retry could
plausibly fix, and how many it cannot. The answer is smaller than people expect.

---

## Submission checklist

- [ ] `prompts/` with nine files: five from Part 1, `best.txt`, and three or four
      ablation files
- [ ] `runs/` with at least ten recorded runs
- [ ] `sweep.md` with the comparison table, three observations, a null result, the
      ablation table, a scoped conclusion, both step 18 runs, the step 20 output,
      and the failure-mode table
- [ ] `plan_check.py` with `usable()` written
- [ ] `decisions.md` current
- [ ] No personal data in any prompt file
- [ ] `git status` clean, pushed
- [ ] AI usage log updated

---

# Extended Lab Options

All four assess 2.14.3 on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Fifteen minutes into Part 1 and there are no prompt files, or the five files differ by more than one element each | SCAFFOLDED |
| Five clean prompt files by the end of Monday's Build 2 | STANDARD |
| Finished Part 2 before the reset on Tuesday, or asks what the stub is actually doing to decide | EXTENDED |
| "When would anyone do this for real," or is bored by the study plan task | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Part 1:** `p1_bare.txt` and `p2_task.txt` are provided complete, in
  `lab-m02-01-files/scaffolded/`. The student writes p3, p4, and p5.
- **Part 3:** the ablation drops from four removals to two, role and format.
  Those two produce the clearest difference and the lesson survives.
- **Part 4:** `usable()` is provided with the first two checks written. The
  student writes the remaining three.
- **Checkpoints:** show the instructor your five prompt files at the end of Part
  1, and your ablation table at the end of Part 3, before moving on.

**Steps that stay, and they are not negotiable:** step 11 (the null result), step
16 (the scoped conclusion), step 18 (both runs), and step 21 (the failure modes).
Those four carry the competency.

**Acceptance criteria:** five prompt files differing by one element each, five
recorded runs, a two-row ablation table, a scoped conclusion, `usable()` complete,
and the failure-mode table for at least three modes.

**Grading:** same scale. Requirements Fit is judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need things not taught.

**Added requirement 1.** Your ablation in Part 3 removes one element at a time from
a five-element prompt, which is five runs. That design cannot see **interactions**:
a case where two elements together do something neither does alone. Design and run
an experiment that could detect one, and report whether you found one.

**Hint, not the answer.** You currently have the full prompt and four
one-removed versions. What would you need to compare in order to tell whether
removing the format matters *more* when the role is also gone? Think about which
pairs of runs differ by exactly one element, and how many such pairs your current
set contains.

**Added requirement 2.** Read `stub_model_server.py` and explain in `sweep.md` how
`select_points()` decides which content to include, and why a longer prompt can
produce a shorter reply. Then say, in one honest paragraph, which of your Part 3
conclusions are about prompts in general and which are about this stub in
particular.

**Acceptance criteria:** all STANDARD criteria, an interaction experiment with its
runs recorded, a correct explanation of `select_points()` in your own words, and
the honest paragraph.

---

## APPLIED

**For the student who asks when anyone does this for real.** This is what a team
does before it ships a prompt inside a product. The prompt in a shipping feature
is version-controlled, tested, and changed one element at a time, for exactly the
reason you found in Part 3: nobody can afford a change they cannot attribute.

**Changed scenario.** Drop the study plan. Pick a task from somewhere you actually
spend time: a shift-swap message for a job, a summary of a practice schedule for a
teammate who missed it, a description of a part for a robotics build log. **It must
be a task where you can tell whether the output is usable**, because you are the
person who would use it.

**Everything else is the same**, including the five prompts, the ablation, the
scoped conclusion, and Part 4. Part 4's `plan_check.py` keeps its study plan
prompt, or you change `build_prompt` to your task and change the keys `usable()`
checks. Either is fine, and say which you did.

**The extra requirement that makes it the same lab.** One paragraph in `sweep.md`:
which element mattered most on your task, which mattered most on the study plan
task your classmates ran, and whether you would expect that difference on a third
task. **Say what you do not know.**

**Grading:** same scale and dimensions. Requirements Fit is judged on whether the
five prompts differ by one element each and whether the conclusion is scoped to
the evidence.
