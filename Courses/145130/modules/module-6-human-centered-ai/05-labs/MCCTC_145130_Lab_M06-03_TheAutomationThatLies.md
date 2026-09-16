# Lab M06-03 · The Automation That Lies
## 145130 Applications of AI · Module 6 · Week 17, Tuesday

**Files:** `lab-m06-03-files/`
**Time:** Tuesday Build 1 and Build 2.
**Due:** end of Build 2.

---

## The scenario

The front office wants the weekly note pile sorted before anybody gets in on
Monday. Somebody wrote an automation. It runs on a schedule, reads the inbox,
labels every note through the model service, and writes a digest.

**It has reported a successful run every day for two weeks. The service has been
down for four of them.**

---

## What you will build

The same automation, changed so that it can tell the difference between doing the
job and not doing the job, and so that a person who was not watching can find out
what happened.

---

## Ports, and this is a module rule

| What | Port |
|---|---|
| the service stub in this lab | **5158** |
| the checker's own fixture | **5170**, or any free port you pass |
| a real model server | **11434.** Reserved. Not ours to take |

**Every command you run passes a port.** There is no default anywhere in this
folder, on purpose. A program that reaches somebody else's server does not fail. It
answers.

---

## What is in the folder

| File | What it is |
|---|---|
| `note_sweep.py` | The starter. It runs. It is also the thing that lies |
| `sweep_service_stub.py` | A stand-in for your Module 5 service. Six behaviours |
| `check_sweep.py` | Checks your automation against the four requirements |
| `inbox/` | Eight invented notes. Nothing in them is from a real person |

---

# Part 1 · Produce the lie, four ways · 20 minutes

**Do this before you change a line.** You are going to make the starter report a
good run on four different bad days, and capture each one.

**Terminal one:**

```
python sweep_service_stub.py --port 5158
```

**Terminal two:**

```
python note_sweep.py --service http://127.0.0.1:5158 --once
```

That is a good day. Keep the output.

Now produce four bad days. For each one, restart the stub in the given mode and run
the sweep again, unchanged.

```
1  stop the stub entirely with Ctrl+C, then run the sweep
2  python sweep_service_stub.py --port 5158 --mode empty
3  python sweep_service_stub.py --port 5158 --mode error500
4  python sweep_service_stub.py --port 5158 --mode garbage
```

**Capture the sweep output for each into `evidence/`.**

Then do the one that matters most:

```
5  put the stub back in --mode ok, and run the sweep twice in a row
   without touching anything in inbox/
```

**Compare the two digest files** from run 5 and from the good day. Use a hash:

```
python -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('out/digest-r0001.md').read_bytes()).hexdigest()[:16])"
```

**Acceptance criteria.**

- [ ] Five captures in `evidence/`, one per situation
- [ ] All five show the starter printing `status  OK`
- [ ] A written line saying what exception was raised in each case. The answer is
      the same five times

---

# Part 2 · The freshness step · 20 minutes

Situation 5 is the failure nobody catches. Every file opened, every label came
back, and nothing in the folder had changed since the last run.

Write a step that notices.

**What it needs:**

- the newest modified time of the files in the inbox, from `path.stat().st_mtime`
- a stored value from the last good run, which means writing one somewhere
- a comparison with a small margin, because file systems disagree about fractions
  of a second

**The part that catches people.** The stored value has to move forward **only on a
run that worked**. Think about what happens on the day after a failure if it moves
anyway, and write your answer in a comment above the line.

**Acceptance criteria.**

- [ ] Running the sweep twice in a row with nothing touched fails the second time
- [ ] Touching any note in the inbox makes the next run pass again
- [ ] The comment about why the stored value is conditional is there and is right

---

# Part 3 · An expectation on every step · 25 minutes

Every step declares what it expected and reports what it got.

```
[ok  ] collect    expected at least 1 note file in the inbox, got 8
[FAIL] classify   expected 8 labelled notes, at least 1 from the service,
                  got 8 labelled, 0 from the service
```

**Three statuses, and they are not the same thing:**

```
OK        every step got what it expected                exit 0
DEGRADED  the work got done, not the way it was meant    exit 1
FAILED    a step did not get what it expected            exit 2
```

**The two counts that do the work:** how many results came out against how many
inputs went in, and how many came from the service against how many came from your
fallback rule.

**Acceptance criteria.**

- [ ] Every step prints a line with an expected and a got
- [ ] The run status comes from comparing those, not from a `try` block
- [ ] Exit codes are 0, 1, and 2
- [ ] A run where nothing came from the service does not print OK

---

# Part 4 · The incident file · 20 minutes

When a step did not get what it expected, write a file. **Four sections, always
these four:**

```
What was expected, and what happened
What to check first
Who to ask
What happens if nobody does anything
```

**The last one is the one people leave out and it is the one that makes somebody
act.**

Also: append one row to a run log **on every run, including the failed ones**.

**The run log holds counts.** No note text and no name goes into it, because the
notes are things people wrote about their own problems. That is a program rule and
it is also an acceptance case next week.

**Acceptance criteria.**

- [ ] A failed run writes an incident file with all four sections
- [ ] The run log has a row for every run you have done today, including failures
- [ ] Searching the run log for a phrase from a note finds nothing

---

# Part 5 · Check it · 10 minutes

```
python check_sweep.py --program note_sweep.py --port 5170
```

**The starter scores 2 of 6.** Anything better than that is progress you made
today, and you should be able to say which checks moved and why.

```
PASS  3 a working run exits 0
FAIL  2 four or more named steps in the printed record
FAIL  4a the source did not change and the program says so
FAIL  4b the service answered 200 with no result and the program says so
FAIL  5 an incident file or a run log exists after a bad run
PASS  1 the trigger fires more than once without you typing anything
```

**That output is from a real run on the build machine, against the unchanged
starter.**

**The checker tests shape.** It cannot tell whether your incident file says
anything worth reading. Your partner does that.

---

## If it breaks

**`note_sweep.py: error: the following arguments are required: --service`**
Correct and deliberate. There is no default. Pass `--service http://127.0.0.1:5158`.

**`one of the arguments --once --at --every is required`**
Also deliberate. An automation has a trigger. `--once` is the one you want while
you are working.

**Every run says `connection_refused` and you are sure the stub is running.**
Check the port in both windows. Then check that the stub actually bound: a stub
that could not get the port prints an error and stops, and a stub that stopped
looks exactly like a stub that is running if you are not looking at its window.

**Your second run passes freshness when it should fail.**
Your stored value is probably being written on every run instead of only on a good
one, or your margin is larger than the gap between the two runs. Print both numbers
and look at them.

**`--every 3` never stops.**
Add `--runs 2`. The checker needs the scheduler to stop on its own, and so do you.

---

## Submission checklist

- [ ] `evidence/` holds five captures from part 1
- [ ] A freshness step that fails the second run and passes after a touch
- [ ] Every step prints an expected and a got
- [ ] Exit codes 0, 1, 2
- [ ] An incident file with four sections
- [ ] A run log with a row for every run, and no note text in it
- [ ] `check_sweep.py` scores better than 2 of 6 and you can say which moved
- [ ] Committed at the end of each period

---

## [VERIFY] The n8n version

**n8n is not installed on the build machine and none of this has been tested in
it.** Your instructor will tell you on Monday whether it is available this year. If
it is, you may build the same automation there instead, and these are the five
nodes it would take:

```
[VERIFY] unverified on the build machine

1  Schedule Trigger        a cron expression
2  Read Binary Files       the inbox folder
3  IF                      newest file time against a stored value
4  HTTP Request            POST /generate, one per note
5  Write Binary File       the digest, plus an IF that branches to an
                           incident file when node 4 returned nothing
```

**The four things you are graded on are the same in either tool:**

- every step says what it expected and what it got
- a step that produced nothing from non-empty input is a failure
- a failed run still writes a record
- the incident names what to check, who to ask, and what happens if nobody does

**If you build it in n8n, you still hand in the four requirements**, as exported
workflow JSON plus screenshots of a failed run. **You also write down which parts
of this lab you could not do in n8n**, because that list is the interesting part.

---

# Extended options

## SCAFFOLDED

**Parts 1, 2, and 4 only.** Part 3 is given to you: a `StepResult` class and the
collect step are already written in
`lab-m06-03-files/scaffolded/step_result_start.py`, and you add expectations to the
other steps using the same shape.

```python
class StepResult:
    def __init__(self, name, ok, expected, got, detail=""):
        ...

def step_collect(inbox):
    notes = [...]
    ok = len(notes) > 0
    return notes, StepResult("collect", ok,
                             "at least 1 note file in the inbox",
                             f"{len(notes)}")
```

**More checkpoints:** your instructor checks after part 1 and again after part 2,
rather than at the end.

**Same acceptance criteria for the parts you do.** `check_sweep.py` should reach 4
of 6.

## STANDARD

The lab as written above.

## EXTENDED

Add a **second error path of your own**, one that raises no exception, and an
acceptance case for it.

**The hint, and it points at documentation rather than at the answer:** read the
`--mode` list at the top of `sweep_service_stub.py` and pick a behaviour nothing in
parts 1 to 4 catches. Then read what `urllib.request.urlopen` does about a reply
that arrives very slowly but does arrive, in the standard library documentation for
`urllib.request`, and decide whether your automation should care.

**Write down what a person would do about it**, in the same four sections, before
you write the code.

## APPLIED

**Same shape, no service.** Build an automation for something with no model in it
at all.

Three that work:

- **the commit sweep.** Every hour, check whether this repository has an
  uncommitted change older than ninety minutes, and write an incident if it has.
- **the folder sweep.** Every day, check that a folder somebody else writes into
  has something newer than yesterday, and write an incident if it does not.
- **the link sweep.** Every day, check that every relative link in a folder of
  Markdown files resolves, and write an incident listing the ones that do not.

**The four requirements are identical** and so is the grading. **The third one is
the one that will find something real**, in this repository, today.

---

## Which version, three observable signals

| If you see | Hand them |
|---|---|
| A student who has produced the five captures but cannot start part 3 after fifteen minutes | **SCAFFOLDED**. The `StepResult` shape is the blocker and it is not what is being assessed |
| A student who reaches 6 of 6 before the end of Build 1 | **EXTENDED**. The second error path is the harder problem and the mode list is right there |
| A student who says "my Module 5 project does not have anything to automate" | **APPLIED**. The link sweep needs no service, no model, and no project, and it will find a broken link in this repository |
