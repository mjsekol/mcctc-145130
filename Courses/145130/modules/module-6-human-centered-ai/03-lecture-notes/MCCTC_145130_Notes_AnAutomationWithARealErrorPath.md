# An automation with a real error path
## 145130 Applications of AI · Module 6 · Week 17, Tuesday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W17_AnAutomationWithARealErrorPath.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W17_AnAutomationWithARealErrorPath.md --export pptx
```

**Competency 1.8.4**, identify alternative actions to take when goals are not met.

---

## Why this exists

An automation is a program that runs when nobody is watching. That single fact
changes what "working" means.

A program a person starts is judged by whether it did the job, because there is
somebody standing there who can see that it did not. **A scheduled automation is
judged by whether it can tell the difference between doing the job and not doing
the job**, because there is nobody standing there at all.

Most first automations cannot tell the difference. They are not broken. They were
written to count the wrong thing.

---

## The one idea

**Every step declares what it expected before it runs, and reports what it got.
The run status comes from comparing those two numbers, not from whether anything
raised an exception.**

```
OK        every step got what it expected
DEGRADED  the work got done, and not the way it was supposed to be done
FAILED    a step did not get what it expected, and a person has to decide
```

A scheduler reads exit codes, so those three become 0, 1, and 2.

---

## Worked example 1 · the run that reports success on a day it did nothing

Everything below was run on the build machine, Python 3.13.7, with the starter
program in `05-labs/lab-m06-03-files/note_sweep.py`.

**Terminal one, the stand-in service:**

```
python sweep_service_stub.py --port 5158
```

**Terminal two, the automation, with the service running:**

```
python note_sweep.py --service http://127.0.0.1:5158 --once
```

```
note sweep, run r0001, started 02:30:55
  8 notes, 8 labelled, digest at out\digest-r0001.md
  status  OK
```

**Now stop the service with Ctrl+C and run exactly the same command:**

```
note sweep, run r0001, started 02:30:57
  8 notes, 8 labelled, digest at out\digest-r0001.md
  status  OK
```

**Read those two blocks again.** One of them reached a service eight times. The
other reached nothing at all. Nothing in the output distinguishes them.

**It gets worse, and this is the part to sit with.** The two digest files those
runs produced are identical. Not similar. The same bytes:

```
digest_with_service.md     sha256 735ad1bba01a4ecd...
digest_without_service.md  sha256 735ad1bba01a4ecd...
```

**Nothing raised.** No exception, no stack trace, no warning. Every file opened.
Every label came back. The program did exactly what it was written to do.

**It was written to count replies.**

---

## Worked example 2 · the three counts that catch it

Three questions, and each one catches a different failure. The first is the most
general and it is the one worth memorising.

```
1  How many results came out, against how many inputs went in?
2  How many came from the thing that was supposed to do the work,
   against how many came from a stand-in?
3  Is the input newer than the last time I ran?
```

**Question 1 catches a step that silently produced nothing.** It generalises to
every step in every automation. "A step produced fewer results than it had inputs"
is a rule you can apply without knowing anything about what the step does.

**Question 2 catches the run above.** Eight labels came back and none came from
the service. That is not a crash. It is the job being done by a keyword rule, and
whether that counts as success is a decision somebody has to make on purpose.

**Question 3 catches the failure nobody else catches**, and it is the one this
lab is really about. See worked example 4.

---

## Worked example 3 · what a step that declares itself looks like

From `05-labs/instructor/lab-m06-03-solution/note_sweep.py`, run with the service
stopped:

```
note sweep, run r0001, started 02:31:13
  inbox   inbox
  service http://127.0.0.1:5158
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [ok  ] freshness  expected source newer than the last run, got first run, nothing to compare
  [FAIL] classify   expected 8 labelled notes, at least 1 from the service, got 8 labelled, 0 from the service
  [ok  ] record     expected 1 row appended to the run log, got 1 row, status FAILED
  status  FAILED
  incident written to out\incident-r0001.md
  run log state\run_log.csv
```

Exit code 2.

**Read the classify line.** It does not say "error". It says what it wanted and
what it got, and the gap between them is the whole message. Somebody who has never
seen this program can read that line and know what happened.

**Read the record line.** The run log gets a row on a failed run. **A log that only
records successful runs is a log that says this automation has never failed.**

The shape in code:

```python
class StepResult:
    def __init__(self, name, ok, expected, got, detail="", degraded=False):
        self.name = name
        self.ok = ok
        self.expected = expected      # in words, for a person at 8 a.m.
        self.got = got
        self.detail = detail
        self.degraded = degraded
```

`expected` and `got` are strings, on purpose. They end up in an incident file that
a human reads, and a human does not want a tuple.

---

## Worked example 4 · the error path that is not an exception

**The inbox has eight files. Every one of them opens. Every label comes back. And
nothing in the folder has changed since yesterday.**

Upstream did not deliver. The export job did not run, or it ran and wrote nothing,
or somebody moved the folder. Nothing in your program went wrong, and the digest
you are about to produce is yesterday's digest with today's run number on it.

**That is worse than no digest**, because somebody will act on it.

Here is the automation catching it. Two runs in a row with nothing touched:

```
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [FAIL] freshness  expected source newer than the last run, got nothing in the inbox has changed since the last run
  [ok  ] record     expected 1 row appended to the run log, got 1 row, status FAILED
  status  FAILED
  incident written to out\incident-r0002.md
```

And here is the incident file, in full, because the file is the deliverable:

```markdown
# Note sweep incident, run r0002

**Status: FAILED. The step that stopped it: `freshness`.**

## What was expected, and what happened

- Expected: source newer than the last run
- Got: nothing in the inbox has changed since the last run

Every file in the inbox is the same file the last run swept. Nothing crashed.
The upstream export did not deliver new notes.

## What to check first

Compare the newest file time in the inbox with the `last_source_mtime` in
`state/last_run.json`. If they match, the export job did not run.

## Who to ask

The owner of the export job. Bring the two timestamps with you. Saying the file
is old is an opinion. Two numbers is a report.

## What happens if nobody does anything

Every run from now on sweeps the same notes and produces the same digest with a
new run number on it. That is worse than no digest, because somebody will act on
it.
```

**Four sections and they are always the same four:**

```
what was expected and what happened
what to check first
who to ask
what happens if nobody does anything
```

**The last one is the one people leave out and it is the one that makes somebody
act.** An incident that says what breaks next week gets read differently from one
that says something failed.

---

## The bookkeeping detail that catches people out

The freshness check needs to remember the newest file time it saw. That goes in a
state file. **Two things live in that file and only one of them is conditional.**

```python
def save_state(state_dir, state, run_id, status, newest_mtime):
    updated = dict(state)
    updated["last_run_id"] = run_id
    updated["last_status"] = status
    updated["next_run_number"] = int(run_id[1:]) + 1   # always
    if status == "OK":
        updated["last_source_mtime"] = newest_mtime    # only on a good run
    ...
```

**The run number always moves forward**, so a failed run gets its own number and
its own incident file rather than overwriting the last one.

**The watermark only moves on an OK run**, because the watermark means "the
newest source I have successfully swept". A failed run swept nothing, so there is
nothing to record. Move it on a failed run and the notes that run did not process
are marked as already done, and they never reach any digest.

---

## The wrong version, and why it is tempting

The wrong version is not a beginner mistake. It is this:

```python
try:
    notes = collect(inbox)
    rows = classify(notes, service)
    write_digest(rows)
    print("status  OK")
except Exception as exc:
    print(f"status  FAILED: {exc}")
```

**That looks like error handling and it catches nothing that happened above.** Go
back to worked example 1 and ask what exception would have been raised. There is
no exception. The service refused a connection, the code caught it, fell back to a
keyword rule, produced eight labels, and returned.

**Why it is tempting:**

- **It is what error handling looks like in every tutorial.** Wrap the thing, catch
  the thing, report the thing.
- **It works for the failures you can imagine.** A missing file. A bad JSON parse.
  Those really do raise, and the block really does catch them.
- **The failures that matter here do not raise.** A service answering HTTP 200 with
  nothing in it is a successful HTTP request. A folder full of yesterday's files is
  a folder full of files.

**The rule that replaces it:** an exception is one way a step can fail to get what
it expected. It is not the definition of failing.

---

## n8n, and why this lab is Python

**n8n is not installed on the build machine and no step in this module using it
has been verified here.** Every n8n instruction in Module 6 is marked **[VERIFY]**.

**If n8n is available on your lab machines**, the same automation is five nodes and
the shape is identical:

```
[VERIFY] the five nodes, unverified on this machine

1  Schedule Trigger        fires on a cron expression
2  Read Binary Files       the inbox
3  IF                      newest file time vs a stored value
4  HTTP Request            POST /generate, one per note
5  Write Binary File       the digest, plus an IF that branches to an
                           incident file when node 4 returned nothing
```

**The four things that stay true in either tool**, and they are what you are graded
on:

- every step says what it expected and what it got
- a step that produced nothing from non-empty input is a failure
- a failed run still writes a record
- the incident names what to check, who to ask, and what happens if nobody does

**The Python version is the primary path** because it was verified here, it needs
no install, and it runs on any machine in this building. It is not a substitute for
the real thing. It is the thing.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Trigger** | What starts the run. A schedule, a file appearing, an event |
| **Step** | One unit of work with one expectation |
| **Expectation** | What a step needs to have got in order to have worked |
| **Run status** | OK, DEGRADED, or FAILED |
| **Exit code** | The number a scheduler reads. 0, 1, 2 here |
| **Watermark** | The stored marker of how far the last good run got |
| **Stale source** | Input that has not changed since the last run |
| **Incident** | A file a person reads when a run failed |
| **Run log** | One row per run, every run, including the bad ones |
| **Silent failure** | A failure that raises nothing and produces output |

---

## Self-check

**1.** Your automation calls a service eight times, gets HTTP 200 every time, and
every response body has `"result": null`. Nothing raises. Which of the three
counts catches it, and what is the run status?

**2.** Somebody argues that a run where every label came from the keyword rule
should be FAILED rather than DEGRADED, because the service never answered. Give
the strongest argument on each side and then say which one you would ship.

**3.** Why does the watermark only move forward on an OK run, and what breaks if it
moves on every run?

---

### Answers

**1.** **Count 2 catches it directly**, and count 1 catches it if your code counts
usable results rather than replies.

Eight replies came back and zero results did, so "how many came from the service"
is 0 of 8. **Status is FAILED**, because the thing that was supposed to do the work
did none of it. The digest still exists and every row on it came from a keyword
rule, which is why the row has to say so.

**The subtlety worth naming:** if your code appends a row per reply, count 1 will
say 8 of 8 and you will pass your own check. The count has to be of results you can
use, not of times the loop went round.

**2.** **For FAILED:** the automation exists to have a model categorise notes. It
categorised nothing. Every row on the digest is a keyword match, which is a fallback
that was never meant to be the product, and calling it anything other than a
failure means somebody reads the digest and trusts labels that were never
classified.

**For DEGRADED:** the work got done. Every note has a label, the store manager can
act on the list, and every row is marked as coming from a rule. A status of FAILED
tells a scheduler to raise an alarm at seven in the morning for something that
produced a usable, honestly labelled output. **Cry wolf twice and nobody reads the
third alert.**

**This one is genuinely arguable and it is the arguable item in this week's Gate
2.** The reference implementation ships DEGRADED, on the grounds that the output is
usable and marked, and it writes an incident anyway so nobody has to read a log to
find out. **What is not defensible is OK**, in either direction, because that hides
it.

**3.** **Because the watermark means "the newest source I have successfully
swept", and a failed run swept nothing.**

Here is what breaks if it moves on every run. Monday's delivery arrives. The run
fails because the service was down, so no digest was produced from Monday's notes.
The watermark moves to Monday's file times anyway.

Tuesday the automation runs again. The notes are still Monday's, because nobody has
delivered since. The watermark already says Monday, so freshness reports a stale
source and stops. **Monday's notes are never processed by any run, ever**, and the
incident file blames the export owner for a delivery that actually arrived.

**Two things are wrong at once**, which is what makes it hard to find: work was
silently dropped, and the report points at the wrong person. And it only shows up
after a failure, which is a state nobody tests twice in a row by hand.
