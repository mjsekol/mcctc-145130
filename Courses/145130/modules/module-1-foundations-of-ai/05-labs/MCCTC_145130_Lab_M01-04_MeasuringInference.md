# Lab M01-04: Measuring Inference
## 145130 Applications of AI · Module 1 · Week 3, Monday

**Gate:** 1 for Part 1, then 3 for Part 2. **Duration:** one block. Build 1
opens with that day's Gate 1 rep, so Part 1 has 40 minutes and Part 2 has 55.
**Competencies:** PRIMARY 5.1.1 (how programs and scripts solve problems),
1.2.1 (extract valid information and cite sources). SUPPORTING 2.4.2, 2.14.4.

**Files:** `lab-m01-04-files/`.

This lab is the on-ramp to the Module 1 performance task. What you build today is
the instrument you use for the rest of the week.

---

## The scenario

Somebody has to decide whether a model can go in front of students on lab
hardware. That decision needs a number, and the number has to be one another
person could produce.

## What you will build

Three functions of arithmetic, checked against thirteen cases worked out by hand,
and then a benchmark run against a server whose true speed you already know.

---

## Why the arithmetic is the lab

`bench.py` is finished. It does the timing, the streaming, the retries, and the
saving. **The part that goes wrong in real benchmarks is not the timing. It is
the division**, and that is the part you write.

One rule governs all three functions:

> **When you cannot know a number, return None. Never return a guess.**

---

## Part 1, Build 1, 40 minutes

The first 10 minutes of Build 1 are that day's Gate 1 rep. Part 1 starts after
it.

**Gate 1 rules apply here too. No AI.** Plain editor. These are thirteen small cases and you can
reason every one of them out.

### Step 1. Run the self-check and see where you stand

From `lab-m01-04-files/`:

```
python check_measure.py
```

It reports **5 of 13**. Look at which five pass. Every one of them is a case
where the right answer is `None`, and the starter returns `None` for everything.
Five right answers, zero understanding. Write that down.

### Step 2. Read the three docstrings before writing anything

`measure.py` has three functions and each one explains what it is for and why the
`None` cases exist. The `None` cases are the whole lesson.

### Step 3. Write `median`

The middle value. With an even count there is no single middle, so average the
two middle values. With an empty list there is no answer at all.

**Why median and not average:** one slow run, usually the first, drags an average
somewhere no run actually was.

### Step 4. Write `generation_ms`

Total latency minus time to first token.

Two cases return `None` and they are different problems:

- `ttft_ms` is `None`, because the server did not stream and nobody knows when
  the first token arrived.
- `ttft_ms` is larger than `total_ms`, because that measurement contradicts
  itself and a negative duration is not a duration.

### Step 5. Write `tokens_per_second`

Tokens divided by seconds of generation, rounded to one decimal place.

Return `None` when the generation time is unknown or is zero or less. **A rate
over no time is not a large rate. It is not a rate.**

More than one decimal place claims a precision this measurement does not have.

### Step 6. Get to thirteen of thirteen

```
python check_measure.py
```

**Every expected value in that file was worked out by hand before the code
existed.** That is the only way a test is worth anything. If you copy the
expected value out of what your program already printed, your test agrees with
your bug.

### Acceptance criteria, Part 1

- [ ] `python check_measure.py` reports 13 of 13
- [ ] `tokens_per_second` returns one decimal place, not more
- [ ] You can say out loud why `generation_ms(800, 900)` is `None` rather than -100
- [ ] Committed

---

## Part 2, Build 2, 55 minutes

**Gate 3, full tooling.**

### Step 7. Point the benchmark at a server that will not stream

Terminal 1, from `local-model-kit/`:

```
python stub_model_server.py --port 11634
```

Terminal 2, from `lab-m01-04-files/`:

```
python bench.py --label stub-check --repeats 3 --endpoint http://127.0.0.1:11634 --hardware "your machine, anchor stub"
```

**Pass the ports every time.** 11634 is Module 1's stub port and 11635 is the
streaming stand-in. 11434 is reserved for a real model. A benchmark that talks
to the wrong server produces a run that looks completely normal, and you will
not find out until the numbers make no sense.

Real output from the build machine:

```
note: this server does not stream, so time to first token and tokens per second
are not measurable here

  prompt            median total   median ttft   tokens   tokens/sec   source
  ----------------------------------------------------------------------------
  p1_short               15.0 ms           n/a     48.0          n/a   character_estimate
  p2_paragraph           15.3 ms           n/a     57.0          n/a   character_estimate
  p3_structured          15.2 ms           n/a     57.0          n/a   character_estimate
```

**Two columns say `n/a` and that is correct.** The program could have divided by
total latency and printed a confident three thousand tokens per second. It
refuses, because your `generation_ms` returned `None`.

Notice the `source` column too. Those token counts are estimates from a character
ratio the program prints in every saved run.

### Step 8. Now point it at a server whose true speed you know

Stop the stub. Terminal 1:

```
python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 300
```

It prints what a correct benchmark should report. **Read that line before you
run anything.**

Terminal 2:

```
python bench.py --label known-rate --repeats 3 --model streaming-stub --endpoint http://127.0.0.1:11635 --hardware "your machine, streaming stand-in at 40 tokens per second"
```

Real output from the build machine:

```
  prompt            median total   median ttft   tokens   tokens/sec   source
  ----------------------------------------------------------------------------
  p1_short             1335.7 ms      318.3 ms     40.0         39.3   server_counter
  p2_paragraph         1330.8 ms      314.9 ms     40.0         39.4   server_counter
  p3_structured        1336.0 ms      318.9 ms     40.0         39.3   server_counter

  widest gap between the fastest and slowest repeat of one prompt: 8.0 ms
```

**39.3 against a true 40. 318 ms against a true 300.** You have now checked an
instrument against something whose size you already knew, which is how anybody
ever comes to trust one.

**`streaming_stub.py` is not a model** and its first line says so. It sends fixed
words at a fixed rate. Nothing it tells you is about a model.

### Step 9. Do the division wrong, on paper

Take your own `p1_short` row. Compute tokens per second the common wrong way:
tokens divided by **total** latency. Write both numbers down.

From the build machine's numbers: 40 divided by 1.3357 is 29.9, against the
correct 39.3, against a true 40.

Then answer in `measurement_note.md`: **is the wrong method always too low,
sometimes too high, or unpredictable?** Say why in one sentence, and make it a
sentence about the divisor.

### Step 10. Change one thing and watch it move

Run the streaming stand-in again with a different first delay:

```
python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 900
```

Re-run the benchmark with a new label. Compare the two.

Answer in `measurement_note.md`: **which of the three numbers changed a lot,
which barely changed, and what does that tell you about which number a user of
your program would feel?**

### Step 11. Write the note

`measurement_note.md`, under a page, four sections.

1. **The three numbers**, defined in your own words, one sentence each.
2. **Your two runs**, tables pasted.
3. **Step 9 and step 10 answers.**
4. **What none of this establishes.** Name every reason these numbers say nothing
   about a real model. There are at least three.

---

## Acceptance criteria, full lab

- [ ] 13 of 13 on the self-check
- [ ] Both runs saved in `runs/` and pasted into the note
- [ ] The `n/a` run explained rather than treated as a failure
- [ ] Step 9 answered with a sentence about the divisor
- [ ] Step 10 identifies which number moved
- [ ] Section 4 names at least three reasons these numbers are not about a model
- [ ] `AI_USAGE.md` updated if you used a model
- [ ] Committed and pushed

---

## If it breaks

**`check_measure.py` says `FAIL median of four: expected 2.5, got 3.0`**
You returned the upper middle instead of averaging the two middle values. With
four values there are two in the middle and the answer is between them.

**`FAIL tokens over no time: expected None, got ZeroDivisionError`**
You divided before checking. The guard has to come first.

**`ModuleNotFoundError: No module named 'measure'`**
Run from inside `lab-m01-04-files/`. Python looks next to the script you ran.

**`nothing answered at http://127.0.0.1:11634`**
No server is running on that port, or it is on a different one. Start the stub
with `--port 11634`, or pass `--endpoint http://127.0.0.1:11635` for the
streaming stand-in. If you started the stub with no `--port` it is on 11434,
which this module never uses.

**Every token count says `character_estimate` on the streaming stand-in**
You are talking to the anchor stub, not the streaming one. They are different
programs. Check which terminal is running what.

**`tokens/sec` prints something like 39.28571428571429**
You skipped the rounding. One decimal place, because more digits claim precision
you do not have.

**`OSError: [WinError 10048] Only one usage of each socket address ...`**
Something is already listening on that port, almost always a server somebody left
running in a closed terminal. Find it and stop it:

```
netstat -ano | findstr "LISTENING" | findstr "11634 11635"
Stop-Process -Id <the last number on the line> -Force
```

**Do not work around it by picking a different port.** The next person to run the
lab will hit the same leftover, and a service talking to a leftover stub in the
wrong mode produces a run that looks completely normal.

---

## Stretch goal

Run `bench.py --no-stream` against the streaming stand-in, so a server that
**can** stream is asked not to. Compare that run against the streamed one and
explain why total latency is nearly the same while two other numbers disappear.

---

## Submission checklist

- [ ] `measure.py` with all three functions
- [ ] Two saved runs in `runs/`
- [ ] `measurement_note.md`, four sections, under a page
- [ ] `AI_USAGE.md` entry if a model was used
- [ ] Pushed

---

# Extended Lab Options

All four assess the same competencies on the same scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty minutes in and fewer than eight cases passing | SCAFFOLDED |
| Self-check passing, working through the two runs | STANDARD |
| Thirteen of thirteen before the reset, or asks how the token counter is chosen | EXTENDED |
| "Why does any of this matter," or asks where benchmarks are used for real | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `median` is provided complete. You write the other two.
- **Steps:** step 10 is removed.
- **Step 11 drops to sections 1, 2, and the step 9 answer.**
- **Checkpoints:** show the instructor your self-check after each function.

**Acceptance criteria:** 13 of 13, both runs saved, and the step 9 answer with a
sentence about the divisor.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught.

**Added requirement 1.** `bench.py` records a `token_source` for every run and it
can be one of three values. Find the function that chooses, and explain in your
note why the order of those checks matters and what would break if it preferred
the character estimate.

**Added requirement 2.** Run the streaming stand-in with `--tokens 5` and again
with `--tokens 200`, everything else the same. Report what happens to tokens per
second and to time to first token, and explain why one of them is stable and the
other is noisier at the small setting.

**Hint, not the answer.** For requirement 1, read `count_tokens` and then read the
three lines after it in `one_streamed_call`. For requirement 2, look at what is
in the denominator of each number and how many events went into it.

**Acceptance criteria:** all STANDARD criteria, both explanations in your own
words naming real functions, and the two extra runs saved.

---

## APPLIED

**For the student who asks where benchmarks are used for real.** Everywhere a
purchase has to be justified: server sizing, phone battery claims, network
throughput, build times on a developer's machine, and every vendor comparison
anybody has ever shown you.

**Changed scenario.** Benchmark something in this building that is not a model.
Pick one:

- how long a lab machine takes from power button to a usable sign-in screen
- how long a 3D print of the same object takes on two different printers
- how long a full build of one of your own Module 5 projects takes

**The requirements that make it the same lab.** A written method before you
measure, covering everything another person would need. At least three repeats.
Median and spread reported together. One number you deliberately refuse to report
because you could not measure it honestly, and a sentence saying why. And section
4 of the note: what your numbers do not establish.

**Grading:** same scale. Requirements Fit is judged on whether the written method
came first and whether the refused number is a real one rather than a decoration.
