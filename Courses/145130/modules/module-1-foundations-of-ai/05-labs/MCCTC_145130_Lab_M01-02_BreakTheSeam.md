# Lab M01-02: Break the Seam
## 145130 Applications of AI · Module 1 · Week 2, Tuesday

**Gate:** 3, full tooling. **Duration:** one block. Build 1 opens with that
day's Gate 1 rep, so this lab has 40 minutes of Build 1 and 55 of Build 2.
**Competencies:** PRIMARY 2.4.2 (fundamental architectures of emerging
technologies and how they integrate into existing systems). SUPPORTING 5.1.1,
2.14.6.

**Files:** `lab-m01-02-files/seam_report.py`. The stand-in is in
`local-model-kit/`.

---

## The scenario

The makerspace decides to try the model on help requests. Before anyone turns it
on for real, somebody has to answer one question in writing: **what does a person
see when the model is down?**

Nobody knows, because nobody has made it fail on purpose. You are going to.

## What you will build

A table with one row per failure, produced by forcing each failure through a
running system, and a written integration note the staff could act on.

---

## Why this is worth a whole block

A seam is where a new system is bolted onto systems that already exist. Nearly
every interesting failure lives at the seam rather than inside either side.

A finished seam has three parts:

1. **A contract.** What crosses, and what every field means.
2. **A failure policy.** How long you wait, whether you retry, what you say.
3. **A record of provenance.** Something that says where a value came from.

**Nothing sits between you and the model.** There is no layer catching failures
on your behalf, which means all three are yours to write. In Module 5 you build
the layer that does this once for every program that needs it. Today you find out
why anybody would bother.

---

## Steps

### Step 1. Start the stand-in

**Nothing to install.** From `local-model-kit/`, one terminal. **Start it in
slow mode with a short delay**, because the default delay is 30 seconds and you
have a period:

```
python stub_model_server.py --port 11634 --mode success --delay 6
```

**Pass the port.** Module 1 uses 11634, and 11434 is reserved for a real model.

### Step 2. Read the stand-in's modes

Open `local-model-kit/stub_model_server.py` and read the comment block at the
top. There are ten modes. Read what each one does before you pick.

### Step 3. Run the starter and see what it gives you

From `lab-m01-02-files/`, in a second terminal:

```
$env:RIDGE_MODEL_URL = "http://127.0.0.1:11634"
python seam_report.py
```

It runs one mode, calls everything `ok`, and prints `something happened` in the
last column. All three of those are your job.

### Step 4. Choose your modes

Edit `MODES_TO_TEST`. **At least five, and one of them must be `slow`.**

You already set `--delay 6` in step 1, and `seam_report.py` waits five seconds
before giving up. In your report, say why you picked that delay instead of 30 or
instead of 2.

### Step 5. Write `kind_of`

Name what happened using **only what a caller can observe**: whether anything
arrived at all, the status code, and the body. You get a fixed list of names in
`KINDS`. Do not invent others.

**Work from the outside in.** Did anything arrive. Was the status 200. Was the
body JSON. Did it say `done`. Was there text in `response`. **That order is not a
style choice** and step 6 of your report asks you to say why.

### Step 6. Write `sentence_for`

One sentence per kind, and each one names exactly one thing the person can do.

- Two problems with two different fixes **may not** share a sentence.
- Two problems with the same fix **may**, and you should be able to say which and
  why.
- No sentence may be the word `error` with nothing else.

### Step 7. Write `should_retry`

**This is a rule, not a list.** Write the rule in your report as one sentence
first, then make the function match it. `attempt()` already calls it for you and
the `model calls` column will show whether a retry happened.

### Step 8. Run it and read every column

```
python seam_report.py
```

Read the sentence next to each row. If two rows produced the same sentence, ask
whether they are the same problem with the same fix. Sometimes they are. Usually
that is a branch you have not written.

**Then find the row that should bother you.** One mode returns HTTP 200, valid
JSON, `done: true`, and real text in `response`, and the answer is still useless.
Your `kind_of` will call it `ok`, and it is right to. Say in your report which
mode that is, why every check passed, and what a program would have to do to
catch it.

### Step 9. Write the integration note

`seam_note.md`, and this is what the makerspace staff would actually read. Five
sections, and keep the whole thing under a page.

1. **What happens when the model is down**, in one sentence a person who does not
   program could act on.
2. **Your table**, pasted from `seam_report.md`.
3. **Your retry rule**, in one sentence, with the rows that prove it.
4. **The row that looked fine and was not**, from step 8, and what it would take
   to catch it.
5. **One recommendation you would make to the staff**, and one thing you would
   measure before making it. A recommendation with nothing to measure is an
   opinion.

---

## Acceptance criteria

- [ ] Five or more modes tested, including `slow`
- [ ] `seam_report.md` written, with a `model calls` column that is not all ones
- [ ] `kind_of` works outside in and uses only the names in `KINDS`
- [ ] No two problems with different fixes share a sentence
- [ ] `should_retry` matches a rule you wrote in one sentence
- [ ] `seam_note.md` has all five sections and fits on a page
- [ ] Section 4 names the mode that passed every check and was still useless
- [ ] `AI_USAGE.md` updated if you used a model
- [ ] Committed and pushed

---

## If it breaks

**`nothing answered` on every row**
The stand-in is not running, or it is on another port. Check which port it
printed when it started. Without `--port 11634` it is on 11434.

**`OSError: [WinError 10048] Only one usage of each socket address ...`**
Something is already listening, almost always a server left running in a closed
terminal:

```
netstat -ano | findstr "LISTENING" | findstr "11634 11635"
Stop-Process -Id <the last number on the line> -Force
```

**Do not work around it by picking a different port.** The next person hits the
same leftover, and a program talking to a leftover server in the wrong mode
produces a run that looks completely normal.

**The `slow` row takes forever and the period ends**
You started the stand-in without `--delay 6`, so it is waiting the default 30
seconds. Stop it and start it again.

**`KeyError: 'generate_calls'`**
You are pointed at something that is not this stand-in. `/stub/stats` exists only
here, which is the point: a real model server does not have it.

**The mode never changes and every row looks the same**
`set_mode` posts to `RIDGE_MODEL_URL`. Check which address that variable holds in
the terminal you ran from.

**Every row says `ok`**
You have not written `kind_of` yet. The starter returns `"ok"` for everything.

---

## Stretch goal

Add a row that is not a stub mode at all: **stop the stand-in entirely** and send
one request. Record what the person sees. Then explain, in two sentences, why
`refused` deserves a different sentence from `timeout` when both of them mean
"no answer from the model".

---

## Submission checklist

- [ ] `seam_report.py` with your modes and your three functions
- [ ] `seam_report.md`
- [ ] `seam_note.md`, five sections, one page
- [ ] Your retry rule written as one sentence
- [ ] `AI_USAGE.md` entry if a model was used
- [ ] Pushed

---

# Extended Lab Options

All four assess 2.4.2 on the same scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Fifteen minutes in and the stand-in is still not running | SCAFFOLDED |
| Table printing, working through `kind_of` | STANDARD |
| Seven modes and a correct retry rule before the reset break | EXTENDED |
| "Why would a real system ever do this," or asks where seams are in other jobs | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `MODES_TO_TEST` is filled in with five modes including `slow`, and
  `kind_of` is provided complete.
- **Steps:** step 7 becomes: read the `model calls` column and say which rows
  differ from the rest. No rule, no `should_retry`.
- **Step 9 drops to sections 1, 2, and 4.**
- **Checkpoints:** show the instructor your table after three sentences are
  written.

**Acceptance criteria:** five modes, a table, five distinct sentences, and the
one-sentence answer to "what happens when the model is down".

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Test all ten modes. Three of them produce kinds you have
not seen. Add a sentence for each and say what a real model doing that would
mean.

**Added requirement 2.** `attempt()` retries at most twice. Change it so the
number of attempts is a setting, run `slow` with one attempt and with three, and
report the total elapsed time for each. Then say what number you would ship and
why, in terms of a person waiting at a keyboard.

**Hint, not the answer.** For requirement 2, the `elapsed_ms` column already
records one request. You will need to record the whole attempt loop instead, and
you will need to decide whether the number you report is per attempt or per
answer. Say which you chose.

**Acceptance criteria:** all STANDARD criteria, ten modes, the two timed runs
pasted, and a shipped number with a reason about a person rather than about a
server.

---

## APPLIED

**For the student who asks where else a seam shows up.** Everywhere two systems
meet and one of them can be unavailable: a card reader and a payment network, a
badge scanner and a door controller, a delivery app and a mapping service, a
scoreboard and a timing system.

**Changed scenario.** Pick a seam in a system you can actually observe in this
building or in a job you have. Write the same integration note for it, without
any code:

1. What crosses the seam, and what the receiving side assumes about it.
2. Three ways the far side can fail, named specifically.
3. What a person currently sees for each one. Go and find out rather than
   guessing, and say how you found out.
4. One failure that would pass every check the receiving side makes and still be
   wrong. This is the hard one and it is the point.
5. One recommendation and one thing to measure first.

**The extra requirement that makes it the same lab.** Section 4 must be a real
example from the system you chose, not a hypothetical.

**Grading:** same scale. Requirements Fit is judged on whether section 3 reports
what you observed rather than what you assume, and whether section 4 is real.
