# Lab M05-03 · The Broken Integration
## 145130 Applications of AI · Module 5 · Week 14, Wednesday

**Competencies:** 2.11.1 (identify the problem), 2.11.2 (select a
troubleshooting methodology), 2.11.5 (design a solution), 2.11.8 (document the
problem and the verified solution)

**This lab runs without your instructor.** Everything you need is in this
handout and in the lecture notes for today. There is nobody to ask, which is the
point: five things are broken and your job is to find out what, using a named
method and not by guessing.

---

## The situation

Five people come to the makerspace help desk this week about the same program.
It reads help requests, asks a model service for a headline for each one, and
prints the answers. Each of the five reports something different, except
that two of them report exactly the same thing.

Nothing is wrong with the program itself in any of the five cases, and the
program is still the problem, because in all five it said everything was fine.

**What you will build:** six troubleshooting log entries, each naming a
methodology, a symptom, one change, and a verification.

---

## Before you start

**Copy the whole `lab-m05-03-files/` folder**, not one file out of it. Everything
this lab needs is inside it and nothing outside it is required.

| File | What it is |
|---|---|
| `scenario.py` | starts the two servers in one state, runs the bench, stops everything |
| `contract_demo_service.py` | the same demo service you traced in Week 13 |
| `stub_model_server.py` | the stand-in model server, with ten behaviours |
| `bench.py` | the program people are complaining about |
| `contract_probe.py` | prints the envelope field by field, including `error.kind` |

Flask has to be installed, once:

```
python -m pip install flask
```

---

## What each scenario is

```
python scenario.py list
```

| # | What the person reported |
|---|---|
| 0 | Nothing. This one is healthy. Capture it first. |
| 1 | The printout looks the way it always did, and every run now takes about eight seconds instead of under one. |
| 2 | It is fast, and every headline is the first line of the request copied out. |
| 3 | The run takes almost half a minute. The student assumed it had crashed and closed the window. |
| 4 | It is fast, and every headline is the first line of the request copied out. |
| 5 | A classmate says their model server is definitely running, they can see it in a window, and every headline is still the first line copied out. |

**Two of the five report the same symptom. That is on purpose.** A symptom does
not identify a fault. Finding the one field that separates 2 from 4 is the
hardest part of this lab and it is worth more than the others together.

**Scenario 5 is a real incident.** While these materials were being built, a
stub server failed to start because another program on the same machine was
already using its port, and the service spent an hour talking to that other
program instead. Every reply looked plausible. Nothing said anything was wrong.
That is why every stub in this module takes a `--port` and why every command in
this handout passes one.

---

## Steps

**Step 1. Capture the healthy run first.**

```
python scenario.py 0
```

*Observable result:* a service URL, then the bench output, then everything
stops. Save the whole thing to a file. You will compare against it five times,
and your memory of what it looked like is not good enough.

**Look for the tell.** In the healthy run, every headline starts with two
particular words that do not appear anywhere in the request. Write those two
words down. When they stop appearing, the model stopped being used.

**Step 2. Run each fault once and write the symptom down before you touch
anything.**

```
python scenario.py 1
python scenario.py 2
python scenario.py 3
python scenario.py 4
python scenario.py 5
```

*Observable result:* five runs. For each one write down three things: how long
the run took, whether the two words from step 1 are there, and anything else
that differs from your baseline.

**Open your troubleshooting log now, before you start diagnosing.** Write the
symptom while you are still looking at it. That is the part people forget.

**Step 3. Name your methodology for each fault before you look any further.**

The four are top down, bottom up, follow the path, and spot the differences.
Today's lecture notes say when each one fits. Write the name in the log entry.
You are allowed to change your mind and you write that down too.

**Step 4. Use health.**

```
python scenario.py 1 --hold
```

The stack stays up and prints the service URL. In a second terminal:

```
set DEMO_SERVICE_URL=http://127.0.0.1:PORT
python contract_probe.py health
```

Replace PORT with the number `scenario.py` printed. On PowerShell the first line
is `$env:DEMO_SERVICE_URL = "http://127.0.0.1:PORT"`. `scenario.py --hold`
prints both forms for you.

*Observable result:* ten fields. `model_reachable`, `timeout_seconds`, and
`retries` are the three that matter. Press Ctrl+C in the first terminal when you
are finished.

**Step 5. Use the probe on a real request.**

```
python contract_probe.py headline --text "The 3D printer in room 118 jammed near the nozzle."
```

*Observable result:* the envelope, with `error kind` and `error message`
printed in full on their own lines. `bench.py` prints neither. **This is what
separates scenario 2 from scenario 4, and scenario 4 from scenario 5.**

For two of the faults the kind is the same and the number inside the message is
not. Copy the whole message, not the kind.

**Step 6. Do steps 4 and 5 for all five faults.** Fill in this table as you go.

| # | wall clock | `model_reachable` | `timeout_seconds` | `retries` | `source` | `error.kind` | the number in `error.message` |
|---|---|---|---|---|---|---|---|
| 0 | | | | | | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

**Step 7. Write the five log entries.** Use the shape in today's lecture notes.
Each one has five parts and all five are graded.

- **Entry heading**, naming the fault
- **Symptom.** What you saw, with the timing and the exact words
- **Methodology.** Named, plus at least one theory that turned out to be wrong
  and the command that killed it
- **What you changed.** One change, not four, written as what a person would do
- **How you verified.** A command and what it printed

**Step 8. The sixth entry, and it is about `bench.py` itself.**

Look at your table again. In scenarios 1 through 5, the model was never
successfully used, not once. Now read what `bench.py` printed in every one of
those runs.

Write a sixth log entry about the program itself. Name the three things
`bench.py` does that hide what is happening, quote the line of code for each,
and say what it should do instead. The three are all in the same file and none
of them is longer than four lines.

---

## Acceptance criteria

1. Your baseline capture from scenario 0 is saved in your repository as a file.
2. The table has all six rows and every cell filled from a real run.
3. Five log entries, and all four methodologies are named at least once across
   them.
4. At least two of the five entries record a theory that turned out to be wrong.
5. Scenarios 2 and 4 have **different** causes in your log, and you name the
   field that separates them.
6. Scenarios 4 and 5 have **different** causes, and you name the number that
   separates them.
7. Each entry changes exactly one thing.
8. Every verification is a command and its output, not the words "it worked".
9. The sixth entry names three problems in `bench.py`, with a line of code for
   each.

---

## If it breaks

**`stub_model_server.py is missing from this folder.`**
You copied one file instead of the folder. Copy the whole `lab-m05-03-files`
folder and run `scenario.py` from inside it.

**`ModuleNotFoundError: No module named 'flask'`**
Install it once with `python -m pip install flask`.

**`the model service never came up on port NNNNN`**
Something stopped the service from starting. Run
`python contract_demo_service.py` by hand in this folder and read what it says.
Nine times out of ten it is Flask not being installed.

**The probe says `Nothing answered.`**
You are using a port from an earlier run. Every run of `scenario.py` picks a new
free port. Read the port off the run that is open right now.

**Scenario 3 seems to hang.**
It does not. It takes about twenty-five seconds on purpose, and that is the
whole symptom. Time it rather than stopping it.

**Scenario 5 looks the same as scenario 4 and you cannot tell them apart.**
Read the whole `error message` line, not the kind. There is a three digit
number in it and it is different in the two runs. Then ask what kind of program
would answer that way.

---

## Stretch goal

Fix one of the three problems in `bench.py`, the one you think costs the person
the most, and run all five scenarios again. Write a sixth log entry with the
before and after output side by side, and one sentence on how many of the four
faults would now be obvious from the bench output alone.

---

## Submission checklist

- [ ] `baseline-scenario-0.txt`, the healthy capture
- [ ] `evidence-table.md`, six rows, every cell from a real run
- [ ] `troubleshooting-log.md`, six entries
- [ ] Every entry names a methodology and verifies with a command
- [ ] Committed and pushed before the end of the period

---

## Extended options

Choose one. All four are graded on the same scale and assess the same
competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes | Give them |
|---|---|
| Ran a fault before running scenario 0, and has nothing to compare against | SCAFFOLDED |
| Has the baseline saved and is already using `--hold` | STANDARD or EXTENDED |
| Notices that 2 and 4 look identical and says so out loud | EXTENDED |
| Says this is not how problems come to them in real life | APPLIED |

### SCAFFOLDED

Two faults instead of five. Do scenario 0, then scenario 1, then scenario 3.
Those two have symptoms you can see from the bench output alone, so you can
solve both without ever opening the probe.

Then do the entry about `bench.py`, and only name **one** of the three
problems. The one to look for: run scenario 1 and read the words next to each
task name. Does that word match what actually happened.

**Extra checkpoint:** show your baseline capture to somebody before you run
scenario 1. If you did not save it to a file, stop and do that first.

### STANDARD

The lab as written. Five faults, six entries.

### EXTENDED

Everything in STANDARD, plus: **make a sixth fault yourself.**

`scenario.py` has a `SCENARIOS` dictionary at the top. Add a scenario 6 that
produces a fault none of the other five produce, run it, and write the log entry
for it. Then hand your `scenario.py` to another team without telling them what
you did and see whether they can diagnose it from the bench output and the
probe.

*Hint, not the answer:* the stub model server has ten modes and this lab only
uses four of them. `stub_model_server.py` lists all ten in its header comment,
and section 5 of `CONTRACT.md`, from the Week 13 lab folder, says which error
kind each one produces and whether it is retried. Pick one where the retried
column changes the timing.

### APPLIED

Same skill, no model, no stack. Find a real integration on a machine you are
allowed to use that is currently not working, or that you can break safely: a
printer that will not print from one application but will from another, a game
launcher that cannot reach its server, a phone that syncs on wifi and not on
cellular, a school laptop that reaches one site and not another.

Diagnose it with a named methodology and write it up in the same five part
shape. The rules are the same: one change at a time, a theory that was wrong
recorded, and a verification anybody could repeat.

Then answer the question this lab is really about: **what was your equivalent of
`health`?** Name the one check that told you which half of the system to stop
looking at, and say how long it took.
