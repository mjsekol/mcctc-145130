# Lecture Notes: Three Numbers Worth Measuring
## 145130 Applications of AI · Module 1 · Week 3, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W03_ThreeNumbersWorthMeasuring.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W03_ThreeNumbersWorthMeasuring.pptx)

If you missed class you can learn this from this file alone. You need the files
in `../05-labs/lab-m01-04-files/`.

**Exit criterion:** run inference locally and report tokens per second. This is
the lesson that makes that sentence mean something.

---

## Why this exists

You have put a model behind a service and watched it fail seven ways. One
question is left, and it is the one an employer asks: **what does this cost?**

Not in dollars. In time, on a person's screen, on the hardware you actually have.
A model that takes eleven seconds to answer is a different product from one that
takes one second, even when the answers are identical.

There is a second reason. Numbers about AI are everywhere and most of them are
unusable, because nobody says what was measured. By Friday you will be able to
read a benchmark and say exactly what it does and does not establish. That skill
is worth more than the numbers.

---

## The concept in plain language

Three numbers. They measure different things and different people care about
each one.

| Number | From when to when | Who feels it |
|---|---|---|
| **total latency** | you send the request, to the last byte arriving | anyone waiting for a whole answer at once |
| **time to first token** | you send the request, to the first piece of text | anyone watching an answer type itself out |
| **tokens per second** | tokens produced, divided by the seconds spent producing them | whoever is paying for the hardware |

### Why total latency is not enough

Two systems with identical total latency feel completely different.

System A shows nothing for four seconds, then the whole answer. System B shows
the first word after half a second and finishes at four. The wait is the same
number. The experience is not, and B is the one people describe as fast.

That is why every serious system reports time to first token separately, and why
your benchmark measures it separately.

### The arithmetic that gets it wrong

Here is the mistake, and it is the most common error in amateur benchmarks:

```
tokens_per_second = tokens / total_latency        wrong
tokens_per_second = tokens / generation_time      right

generation_time = total_latency - time_to_first_token
```

**No tokens were produced during the wait before the first one.** Dividing by
total latency spreads the tokens over time the model spent doing something else,
and reports a rate the model never ran at.

The error is always in the same direction. The divisor is always too big, so the
number is always too low. A benchmark with this bug never overstates a model. It
understates it, quietly, and the amount depends on how long the wait was, which
means it understates slow-to-start systems most.

---

## Worked example 1: the arithmetic, with real numbers

From the reference run on the build machine:

```
  prompt            median total   median ttft   tokens   tokens/sec
  p1_short             1335.7 ms      318.3 ms     40.0         39.3
```

Do it both ways.

**Wrong:** 40 tokens divided by 1.3357 seconds is **29.9** tokens per second.

**Right:** generation time is 1.3357 minus 0.3183, which is 1.0174 seconds.
40 divided by 1.0174 is **39.3** tokens per second.

Now the part that makes this worth a whole lesson. The server producing those
numbers was `streaming_stub.py`, started like this:

```
python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 300
```

Forty tokens, 25 milliseconds apart. **Its true rate is 40 tokens per second, and
its true time to first token is 300 milliseconds.** We know, because we set them.

The right method reported 39.3 against a true 40. The wrong method reported 29.9,
which is a quarter low. **The instrument was checked against something whose size
was already known**, and that is the only way anyone ever trusts an instrument.

---

## Worked example 2: when a number cannot be known

Point the same benchmark at the anchor stub, which refuses to stream, and this is
what comes back:

```
note: this server does not stream, so time to first token and tokens per second
are not measurable here

  prompt            median total   median ttft   tokens   tokens/sec   source
  p1_short               15.0 ms           n/a     48.0          n/a   character_estimate
```

Two columns say `n/a` and the note says why. The program had every opportunity to
produce a number here. It could have used total latency as the divisor and
printed 3200 tokens per second. It refuses.

That refusal is written into `measure.py`, in three functions, and the rule is
one line:

> **When you cannot know a number, return None. Never return a guess.**

A gap in a report is a fact about what you measured. A guess that fills the gap
is a lie with a decimal point on it.

---

## Worked example 3: the token count is a measurement too

Look at the `source` column in those two runs. One says `server_counter` and one
says `character_estimate`. They are not equally good.

| Token source | What it means | Trust |
|---|---|---|
| `server_counter` | the server reported how many tokens it produced | best available |
| `stream_chunks` | we counted the pieces that arrived | good, if one piece is one token |
| `character_estimate` | characters divided by an assumed ratio | weak, and the assumption is printed |

The assumed ratio in `bench.py` is 4.0 characters per token, and it is a constant
at the top of the file with a comment saying it is an assumption rather than a
measurement. It is printed into every saved run.

**This is why `compare_machines.py` refuses to compare token counts from
different sources.** A server counter against a character estimate is not two
measurements of the same thing.

---

## The wrong version, and why it is tempting

> "Our model runs at 42 tokens per second."

One number, no method. Which prompt. How many runs. Median or average or best.
Was the warm-up included. Was the count from the server or estimated. Streaming
or not. What else was running on the machine.

Without those, 42 is not a measurement. It is a number somebody typed, and you
cannot use it for anything, including comparing it against your own 39.3.

It is tempting because a single number is what people ask for, and because the
method paragraph feels like padding next to it. It is the opposite. **The method
is the measurement. The number is a summary of it.**

### Write this down

> Generation time is total latency minus time to first token. Divide by anything
> else and you report a rate that never happened.

---

## Vocabulary

| Term | What it means |
|---|---|
| **latency** | how long something takes, from request to answer |
| **total latency** | send to last byte |
| **time to first token, TTFT** | send to the first piece of generated text |
| **generation time** | total latency minus time to first token |
| **tokens per second** | tokens divided by generation time |
| **streaming** | sending the answer in pieces as it is produced |
| **warm-up** | a request sent and thrown away, so loading is not counted as running |
| **median** | the middle value, which one slow run cannot drag |

---

## Self-check

**1.** A run reports total latency 2400 ms, time to first token 900 ms, and 60
tokens. Compute tokens per second correctly, then compute what the common wrong
method would give.

**2.** Why does `bench.py` throw away the first request instead of including it?

**3.** Somebody reports 120 tokens per second with no time to first token, on a
server that does not stream. What did they almost certainly do, and is their
number too high or too low?

### Answers

**1.** Generation time is 2400 minus 900, which is 1500 ms, or 1.5 seconds. 60
divided by 1.5 is **40.0** tokens per second. The wrong method gives 60 divided
by 2.4, which is **25.0**, understating the rate by nearly 40 percent, because
the 900 ms wait produced no tokens and was counted as though it did.

**2.** Because the first request usually includes work that only happens once,
such as loading the model into memory, and that work is not part of what a
request costs afterwards. Including it makes a system look slower than it is for
every request after the first, and the amount depends on how many requests you
ran, which means the number changes with the size of the test rather than with
the system.

**3.** They divided by total latency, because on a server that does not stream
that is the only number they had. Their figure is **too low**, because the
divisor includes the time before the first token. The deeper problem is that
their token count is probably an estimate too, so they have two weak numbers
multiplied together and one confident result.
