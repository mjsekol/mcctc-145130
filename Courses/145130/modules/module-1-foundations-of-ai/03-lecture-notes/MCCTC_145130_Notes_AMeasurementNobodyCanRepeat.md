# Lecture Notes: A Measurement Nobody Can Repeat
## 145130 Applications of AI · Module 1 · Week 3, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W03_MeasurementYouCanRepeat.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W03_MeasurementYouCanRepeat.pptx)

If you missed class you can learn this from this file alone. You need the files
in `../05-labs/lab-m01-04-files/` and a classmate's saved run.

**Competency 1.2.1** carries the weight here: extract relevant, valid
information and cite sources. Today the source is your own machine.

---

## Why this exists

Yesterday you produced numbers. Today you compare yours against a classmate's,
and you discover how many ways that can be meaningless.

This is the hardest idea in the module, and it is not technical. It is this:
**a difference between two numbers tells you about the machines only if
everything else was the same.** Everything else is never the same. The work is in
finding out what differed and saying so.

---

## The concept in plain language

A measurement is repeatable when somebody else can produce it from what you
wrote down. That requires you to record the method, not only the result.

For a model benchmark the method is at least these seven things:

| What | Why it matters |
|---|---|
| the exact prompts | longer prompts take longer, and different text tokenizes differently |
| how many repeats | a median of three and a median of ten are different kinds of number |
| whether a warm-up was thrown away | the first request can include loading the model |
| streaming or not | without streaming, time to first token cannot be measured at all |
| how tokens were counted | a server counter and a character estimate are not comparable |
| which model, and which build | the name is not enough; builds differ |
| what else the machine was doing | a video call in another window is part of your measurement |

Miss any one of those and your number is still a number. It is no longer a
comparison.

---

## Worked example 1: a comparison the program refuses to make

`compare_machines.py` checks the method before it compares anything. Run on the
build machine against two runs that differ only in repeat count:

```
bench-a  against  bench-c-five-repeats

  bench-a: build machine, streaming stand-in set to 40 tokens per second
  bench-c-five-repeats: build machine, same stand-in, five repeats instead of three

  These two runs cannot be compared.
    different repeat counts: 3 against 5. A median of three and a median of ten
    are not the same kind of number.

  Agree on a method, run again, and come back.
```

It exits with code 1 and produces no table.

**That refusal is the feature.** The two runs were made on the same machine
against the same server, so the difference between their numbers is pure method.
A program that printed the table anyway would have handed you a difference and
invited you to explain it in terms of hardware.

---

## Worked example 2: a comparison it allows, with warnings

Now two runs that share a method but differ elsewhere:

```
  warning: tokens were counted differently: ['server_counter'] against
           ['character_estimate']. Only the timings are comparable.
  warning: one run streamed and the other did not, so only total latency is
           comparable between them.
  warning: different models: streaming-stub against llama3.2. You are comparing
           two models and two machines at once, and you will not be able to say
           which caused a difference.

  prompt            bench-a        bench-no-strea difference
  p1_short          1335.7 ms      15.0 ms        1320.7 ms faster
    tokens/sec      39.3           n/a
    first token     318.3 ms       n/a
```

The table is printed, because the prompts and repeats match. Three warnings sit
above it, and any one of them is enough to make "1320 ms faster" a sentence about
the two servers rather than about the two machines.

**Read the warnings before the table.** A reader who reads only the table walks
away believing one machine is 89 times faster than the other. Both runs were on
the same machine.

---

## Worked example 3: the comparison that works, and what it still cannot say

```
  bench-a: build machine, streaming stand-in set to 40 tokens per second
  bench-b: build machine, streaming stand-in set to 25 tokens per second

  prompt            bench-a        bench-b        difference
  p1_short          1335.7 ms      2329.7 ms      994.0 ms slower
    tokens/sec      39.3           24.7
    first token     318.3 ms       713.4 ms
  p2_paragraph      1330.8 ms      2334.0 ms      1003.2 ms slower
    tokens/sec      39.4           24.7
    first token     314.9 ms       716.8 ms
```

Same method, same machine, and the stand-in servers were configured for 40 and
25 tokens per second. The benchmark reported 39.3 and 24.7. Both within two
percent of the truth, and the ratio between them is right.

**What it still cannot say:** anything about a model. Neither server is a model.
This is a working instrument measured against known quantities, which is exactly
what you want before you point it at something unknown, and it is not a result
about AI.

Your report has to say that in those words. The person reading it will otherwise
assume the numbers describe a model, because that is what a benchmark usually
describes.

---

## The variance question, and why one run is not a measurement

`bench.py` prints this line at the end of every run:

```
  widest gap between the fastest and slowest repeat of one prompt: 8.0 ms
```

Eight milliseconds of spread on medians around 1330. That is under one percent,
which means the repeats agree and the median means something.

Now imagine the gap were 600 ms on the same medians. The median would still print
a confident number, and it would be summarising three measurements that disagree
by half a second. Something was changing between runs, and until you know what,
you do not have a measurement of anything.

**Report the spread next to the median, always.** A median with no spread beside
it hides exactly the information that would tell a reader whether to believe it.

### Why median rather than average

One slow run drags an average somewhere no run actually was. If three runs take
1.3, 1.3, and 4.1 seconds, the average is 2.2, and no run took 2.2 seconds. The
median is 1.3, which is what a typical run cost, and the 4.1 shows up in the
spread line where it belongs as a question to investigate.

---

## The wrong version, and the damage

> "I ran it once on my machine and once on Diego's. Mine was faster, so my
> machine is better for AI."

Count the problems. One run each, so nothing is known about spread. No mention of
warm-up, so one of them may have included loading. No mention of prompts, repeats,
or token counting. No mention of what else was running. And a conclusion about
"AI" drawn from one program on one prompt.

The damage is not that the conclusion is wrong. It might be right by accident.
The damage is that nobody can tell, including the person who wrote it, and in two
weeks somebody buys hardware because of it.

---

## Why the wrong version is tempting

Because it is what the data looks like when you first get it, and because the
comparison is genuinely interesting. The pull toward a clean conclusion is
strongest exactly when the numbers are new.

The habit that prevents it: before writing any sentence with "faster" in it,
write the sentence "one thing that differed between these runs other than the
hardware was ____". There is always at least one. `compare_machines.py` prints
that prompt at the bottom of every comparison for this reason.

### Write this down

> A difference between two numbers is a fact about two whole situations, not
> about the one thing you were interested in.

---

## Vocabulary

| Term | What it means |
|---|---|
| **method** | everything about how a measurement was produced |
| **repeatable** | somebody else can produce it from your written method |
| **variance, spread** | how much the repeats disagreed |
| **median** | the middle value of the repeats |
| **warm-up** | a request sent and discarded so loading is not counted |
| **confounded** | two things changed at once, so neither can be blamed |
| **control** | holding something fixed on purpose so it cannot explain a difference |
| **instrument** | the thing doing the measuring, which can be wrong |

---

## Self-check

**1.** You and a classmate both ran three repeats of the same prompts on the same
model. Yours reports 39 tokens per second and theirs reports 24. Name three
things other than the hardware that could explain that, and say how you would
rule each one out.

**2.** Your three repeats are 1.2, 1.3, and 6.8 seconds. The median is 1.3. What
do you report, and what do you do next?

**3.** Why does `compare_machines.py` refuse on different repeat counts but only
warn on different token sources?

### Answers

**1.** Any three of: something else running on one machine, which you rule out by
closing it and running again; one run including the warm-up and the other not,
which you rule out by reading the `warmups` field in both saved runs; different
token counting, which you rule out by reading the `token_source` column;
different models or builds, which you rule out by reading the `model` field;
different power settings on a laptop, which you rule out by plugging both in. The
general move is the same every time: read the method fields in the saved run
before theorising about hardware.

**2.** Report the median of 1.3 seconds **and** the spread, which is 5.6 seconds,
and say plainly that the repeats disagree. Then investigate rather than publish:
run more repeats, watch what else is happening on the machine, and check whether
the slow one was first. A median that summarises disagreeing numbers is a
confident summary of a mess.

**3.** Different repeat counts make the summary statistics incomparable, and
nothing in the output would survive, so there is nothing worth printing.
Different token sources leave the timings perfectly comparable and only ruin the
token figures, so the honest move is to print what still holds and warn about
what does not. The general rule: refuse when nothing can be salvaged, warn when
something can.
