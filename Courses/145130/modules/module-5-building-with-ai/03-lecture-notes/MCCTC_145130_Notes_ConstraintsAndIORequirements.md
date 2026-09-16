# Lecture Notes: Constraints, Processing Requirements, and What Crosses the Boundary
## 145130 Applications of AI · Module 5 · Week 13, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W13_ConstraintsAndIO.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W13_ConstraintsAndIO.pptx)

If you missed class, you can learn this concept from this file alone. To run the
examples you need `05-labs/lab-m05-01-files/`, which has everything in it.

**Competency 5.6.2** is constraints and system processing requirements.
**Competency 5.6.5** is input and output requirements. **Competency 5.6.8**
includes the data dictionary. All three are documents, and all three are graded.

---

## Why this exists

Yesterday you drew the shape of the system. Today you put numbers on it.

A design with no numbers in it cannot be wrong, which sounds like an advantage
and is the opposite of one. "The service should respond quickly" cannot be
tested, cannot be reviewed, and cannot be failed. "The service answers `/health`
in under three seconds, always, without touching the model" can be all three.

Every number you write down today is a number somebody can check on Friday.

---

## The concept in plain language

Three different things, and people mix them up constantly.

**A constraint** is something you are not allowed to change, or a limit you have
to live inside. You did not choose it. Example: the model runs locally, because
commercial AI developer APIs require their users to be 18 or older.

**A processing requirement** is a number the system has to hit for it to be
worth using. You chose it, and you can defend it. Example: `/health` answers in
under three seconds.

**An I/O requirement** is exactly what goes in and exactly what comes out, field
by field, with types and ranges. Example: `prompt` is a string of 1 to 4000
characters after control characters and outer whitespace are removed.

The test that tells them apart: **can you change it by deciding to?** If no, it
is a constraint. If yes and it is a number, it is a processing requirement. If
it names a field, it is an I/O requirement.

---

## Worked example 1: constraints with the reason attached

A worked constraint list, for the kind of system you are building. The third
column is the one that makes this document worth writing.

| # | Constraint | Why | What it costs you |
|---|---|---|---|
| C1 | The model runs locally. No commercial AI developer API. | those services require users to be 18 or older | the model is smaller and follows output instructions less reliably |
| C2 | No credential anywhere in the code or the repository | a local model needs none, and a credential that exists can be leaked | you cannot reach anything that needs one |
| C3 | No student personal data reaches a model, a log, or a file | program rule | your fixtures are invented, so they are cleaner than real input and hide problems real input would find |
| C5 | C# projects target `net8.0` | lab machines may have an older SDK than the one you build on | on SDK 10, `dotnet new sln` writes a `.slnx` an older SDK cannot open, so you pass `--format sln` |
| C8 | One model server may serve the whole room | there is not a graphics card per seat | thirty clients can rate limit it, which is why the 429 path exists |

**A constraint with no reason is a rule somebody will break the first time it is
inconvenient, and they will be right to.** A constraint with no cost written
next to it is a sales pitch. Write all three columns.

---

## Worked example 2: processing requirements, measured not guessed

Every number below was measured on the build machine. That is the standard: a
processing requirement you have not measured is a guess with a table around it.

| # | Requirement | Number | How it was measured |
|---|---|---|---|
| P1 | `/health` answers without touching the model | under 3 seconds always | 0.1 s with the stub up, 0.6 s with nothing listening |
| P2 | One `/generate` call against the stub | under 100 ms | 17 to 32 ms across every captured run |
| P3 | Wait for one model answer | 20 seconds | covers a model loading into memory |
| P4 | Retries after the first try | 1, capped at 3 | more turns one broken model into a service that never answers |
| P5 | **Worst case for one request** | **timeout times attempts** | 20 s times 2 is 40 s at the defaults |
| P6 | **The caller's own timeout** | **longer than P5** | otherwise the caller gives up before the labelled fallback arrives |
| P8 | Prompt cap | 4000 characters | about three pages of typing |

**P5 and P6 are the pair that matters, and they are the pair people get wrong.**
Your service is allowed to take its timeout multiplied by the number of
attempts. If your application gives up sooner than that, the labelled fallback
your service was about to hand you never arrives, and the person gets nothing
instead of something. You will see this happen for real in Week 14.

Write both numbers down. In both programs. Then check them against each other,
out loud, in the peer walkthrough.

---

## Worked example 3: I/O requirements, and running the probe

Here is the difference between describing a field and specifying it.

**Describing:** "The prompt is the text the user wants a headline for."

**Specifying:**

| Field | Type | Rules | When it is wrong |
|---|---|---|---|
| `prompt` | string | 1 to 4000 characters after control characters and outer whitespace are removed | HTTP 400, `prompt_too_long` or `prompt_empty`, and the model is never called |

The second one can be tested. Run the probe against a running service:

```powershell
python contract_probe.py long-prompt
```

Captured on the build machine:

```
  request        {"task": "headline", "prompt": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..."}
  HTTP status    400
  ok           false
  task         headline
  result       null
  source       none
  elapsed_ms   0
  error kind:    prompt_too_long
  error message: the prompt is 4001 characters. The limit is 4000.
  verdict        the service refused the request (prompt_too_long)
```

Look at `elapsed_ms`. Zero. The service did not call the model, did not wait,
and did not spend anything. **Checking input before you do work with it is not
politeness. It is the difference between a wrong request costing nothing and a
wrong request costing twenty seconds of somebody's period.**

And the empty case:

```
  error kind:    prompt_empty
  error message: the prompt was empty once whitespace and control characters were removed
  verdict        the service refused the request (prompt_empty)
```

Three spaces is not a prompt. The rule says "after control characters and outer
whitespace are removed", and that clause is doing real work.

---

## The wrong version, and what it produces

The tempting version of the I/O specification is the one that says what a field
is and not what its limits are.

```
prompt: the text to summarise
minutes: how long the session should be
label: the category
```

Three lines, no types, no ranges. Now watch what each one lets through.

**No cap on `prompt`.** Somebody pastes a 40,000 character file. Without a cap
the service builds a prompt around it, sends it, and the model either takes a
very long time or refuses. With a cap, HTTP 400, zero milliseconds, and a
message saying the real length.

**No range on `minutes`.** The model returns 600 and the planner starts a ten
hour timer on a school night. With a range of 5 to 240, the answer is rejected
and the person gets a labelled fallback.

**No list for `label`.** The model invents `facilities`, which is a reasonable
category that your database has never heard of. The row goes in and the report
that groups by label quietly has a group nobody built a page for. You find out
in three weeks.

None of those three crash. All three produce output. That is why they are on
this page.

---

## Why the wrong version is tempting

Because specifying a field is slow and unglamorous and you already know what the
field is for.

Writing "1 to 4000 characters after cleaning" takes a minute and feels like
writing down something everybody already understands. And on the day you write
it, everybody does. The person who does not is you in Week 15, and your partner
in Week 14 while you are at a competition, and whoever reads this repository
next semester.

**The habit that prevents it:** for every field, fill in four columns. Name,
type, allowed range, and what happens when it is wrong. If the fourth column is
empty you have not finished thinking, because something has to happen and right
now the answer is whatever the language does by default.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Constraint** | something you may not change, or a limit you must live inside |
| **Processing requirement** | a number the system has to hit, that you can measure |
| **I/O requirement** | exactly what goes in and comes out, by field, with types and ranges |
| **Data dictionary** | every named field, its type, where it comes from, and what happens when it is wrong |
| **Worst case** | the longest a thing can take when nothing has failed outright |
| **Cap** | a hard upper limit, checked before the work is done |
| **Untrusted input** | anything that came from outside your program, which includes the model's answer |
| **Validation** | checking a value against its rules and deciding on purpose what happens when it fails |

---

## Self-check

**Question 1.** Your service waits 20 seconds for the model and retries once.
Your C# program's HTTP timeout is 30 seconds. State the problem in one sentence
and give the number you would change it to.

**Question 2.** "The application should be fast." Rewrite it as a processing
requirement somebody can fail you on, and say how you would measure it.

**Question 3.** Which of these is a constraint, which is a processing
requirement, and which is an I/O requirement: (a) the model runs on lab
hardware, (b) `bullets` holds 1 to 5 strings of at most 200 characters each,
(c) the first request after the server starts may take 30 seconds.

---

### Answers

**1.** The service's worst case is 20 seconds multiplied by two attempts, which
is 40 seconds, and the client gives up at 30, so on a slow model the client
reports a timeout of its own and the labelled fallback the service was about to
return never reaches the person. Set the client's timeout above 40. Forty-five
is the number the corrected client in this module uses, and it reads both
numbers from `/health` so it can warn you when they are the wrong way round.

**2.** One good answer: "One `/generate` call with the model reachable returns
in under 2 seconds at the median, measured over 20 consecutive calls with a
fixture ticket, recorded during the pre-flight." Measure it by running the same
request twenty times and writing down the times. The point is that somebody
else can run your measurement and get a number, and that number can fail.

**3.** (a) is a constraint. You did not choose the hardware and you cannot
change it by deciding to. (b) is an I/O requirement. It names a field and gives
its type and range. (c) is a processing requirement, and an awkward one: it is a
number about how the system performs, it is real, and the honest way to write it
is as a requirement on the caller, "the caller must tolerate a first request of
up to 30 seconds", because that is what somebody has to build against.
