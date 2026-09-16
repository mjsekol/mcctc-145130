# Lecture Notes: Who Gives Up First
## 145130 Applications of AI · Module 5 · Week 14, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W14_WhoGivesUpFirst.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W14_WhoGivesUpFirst.pptx)

**Week 14 is the competition week. There is no instruction segment this week.**
This file is the lesson. Work the numbers in example 1 on paper before you read
example 2. You can do everything here without asking anybody anything.

---

## Why this exists

There are three clocks running in this system and most people only know about
one of them.

The model takes as long as it takes. The service has a timeout and a retry
policy. Your application has a timeout of its own. Those three numbers have to
be set against each other, and when they are set wrong the symptom is not an
error message. It is a person staring at a terminal for twenty seconds and then
getting nothing.

This is the most common way an integration is built wrong in this lab, and it is
invisible until the model is slow.

---

## The concept in plain language

**The rule, in one line:**

> Your application has to wait longer than the service's own worst case, or the
> labelled fallback the service was about to hand you never arrives.

The service's worst case is not its timeout. It is its timeout multiplied by the
number of attempts it makes.

```
service worst case = model timeout x (retries + 1)
```

At the anchor stack's defaults that is 20 seconds times 2, which is 40 seconds.
So an application that gives up at 30 gives up first, every time, on a slow
model.

### Why the fallback is the thing worth waiting for

When the model does not answer, the service does not fail. It builds an answer
itself, marks `source` as `fallback`, and puts the reason in `error`. The person
gets something usable and an honest label.

If your application gives up before that arrives, the person gets nothing, and
the message they get says `timeout`, which points at the model when the real
problem was your own timeout setting.

**You threw away a good answer by being impatient.**

### Why more retries is the wrong fix

Retrying helps when the problem might be temporary: the server is starting, the
model is loading, the network blipped, the server asked you to slow down.

Retrying does not help when the reply itself is wrong. A malformed body retried
gets you the same malformed body and costs another twenty seconds. That is why
the service retries `connection_refused`, `unreachable`, `timeout`,
`rate_limited`, and `connection_broken`, and does not retry `malformed_json`,
`missing_field`, `empty_response`, or `task_validation_failed`.

And retries multiply the wait. Going from 1 retry to 3 takes the worst case from
40 seconds to 80. In a 149 minute block with thirty people on one model server,
that is not a small decision.

---

## Worked example 1: do the arithmetic before you read on

Three settings. Work out what happens in each. The answers are in example 2.

| | Model takes | Service timeout | Service retries | Client timeout |
|---|---|---|---|---|
| A | 8 s | 20 s | 1 | 30 s |
| B | 8 s | 3 s | 1 | 45 s |
| C | 8 s | 5 s | 1 | 5 s |

For each one, write down two things: how long the person waits, and what they
see at the end.

---

## Worked example 2: the same three, captured

**Setting A. The model is slow and the service is patient.**

The service's first attempt gets an answer at 8 seconds, inside its 20 second
timeout. No retry is needed. The client's 30 seconds is never tested.

```
  [summarize] from the model in 8014 ms
```

The person waits 8 seconds and gets a model answer.

**Setting B. The service gives up and falls back.** Captured with the service
timeout at 3 seconds and one retry:

```
  [classify] from FALLBACK, not the model in 6297 ms
  why: timeout: no answer from the model within 3 seconds
  label: network
  note:  No model answer. A keyword rule in the service matched 'wifi'.
```

6.3 seconds is two attempts at 3 seconds each. The client's 45 seconds was never
close to being tested. The person waits 6 seconds and gets a labelled fallback,
which is the system working correctly.

**Setting C. The client gives up first.** Captured from the Gate 2 W15 program,
whose client timeout is 5 seconds, against a service whose model takes 8:

```
  The model service took too long.
  the service at http://127.0.0.1:5157 did not answer within 5 seconds.
  The model may still be loading. Try again in a minute.

  The model service took too long.
  the service at http://127.0.0.1:5157 did not answer within 5 seconds.
  The model may still be loading. Try again in a minute.

exit code 0, wall clock 21.3 s
```

**21.3 seconds of waiting and no answer at all.** The service had a labelled
fallback ready at 8 seconds, twice, and nobody ever saw it. The message blames
the model. The model was fine.

That program also retried once on its own, which is why 5 seconds became 21
across two tasks.

Now the corrected version of the same program, against the same service, with a
45 second timeout and no client-side retry:

```
  [summarize] from the FALLBACK, not the model in 8000 ms
  why: model_http_error: the model server answered with HTTP 500
  summary: Tempo run on the back trail.
    - Tempo run on the back trail.
  [classify] from the FALLBACK, not the model in 8000 ms
  ...
exit code 0, wall clock 17.3 s
```

Still slow, because the model is still slow. The difference is that the person
gets the answer the service built for them, labelled, instead of nothing.

---

## Worked example 3: make the program tell you

The corrected client asks the service for both numbers and compares them itself.

```csharp
Console.WriteLine($"  service waits    {report.TimeoutSeconds:0.#} s per model call, {report.Retries} retry");
Console.WriteLine($"  this program waits {RequestTimeout.TotalSeconds:0.#} s");

double serviceWorstCase = report.TimeoutSeconds * (report.Retries + 1);
if (RequestTimeout.TotalSeconds <= serviceWorstCase)
{
    Console.WriteLine();
    Console.WriteLine($"  This program gives up at {RequestTimeout.TotalSeconds:0.#} s and the service can take");
    Console.WriteLine($"  {serviceWorstCase:0.#} s before it answers with its fallback. Raise {TimeoutVariable}.");
}
```

Captured against a service with a 20 second timeout and one retry:

```
TrackSide . service http://127.0.0.1:5157
  service          practice-service, status ok
  model reachable  yes
  service waits    20 s per model call, 1 retry
  this program waits 45 s
```

No warning, because 45 is larger than 40. Set the client's timeout to 10 and
the same command prints the warning instead.

**This is the cheapest thing in the whole module.** Six lines, and the failure
that used to take twenty-one seconds of silence to find now takes one command.

---

## The wrong version, and why it looks right

Here is the comment that was sitting above the wrong number in the Gate 2
program:

```csharp
// Long enough for the service to finish its own retry before we give up.
private static readonly TimeSpan RequestTimeout = TimeSpan.FromSeconds(5);
```

The comment is correct about what the value should do. The value does the
opposite. Somebody wrote the right idea and then typed a number that felt
reasonable, and nobody ever checked the number against the service's settings,
because on a fast day it never matters.

**A comment that says the right thing above a value that does the wrong thing is
worse than no comment.** The next reader believes the comment, stops thinking
about the number, and the defect survives another review.

---

## Why the wrong version is tempting

Because 5 seconds is a completely sensible number in every other program you
have written.

A web page that takes 5 seconds is broken. A database query that takes 5 seconds
is broken. You have two years of instinct saying that 5 seconds is generous, and
all of that instinct is wrong here, because there is a language model in the
path and a language model on lab hardware is slow in a way that nothing else you
have called is slow.

**The habit that prevents it:** never type a timeout as a number you feel good
about. Write it as arithmetic on the number below you, in a comment, next to the
value:

```csharp
// The service waits 20 s per model call and retries once, so its worst case
// is 40 s. This has to be larger than that.
private static readonly TimeSpan DefaultTimeout = TimeSpan.FromSeconds(45);
```

---

## Vocabulary

| Term | What it means |
|---|---|
| **Timeout** | how long one program waits before it gives up on an answer |
| **Worst case** | the longest a layer can take when nothing has failed outright |
| **Retry** | sending the same request again after a failure that might be temporary |
| **Retryable** | a failure kind that could give a different answer next time |
| **Retry-After** | a header a server sends with a 429, saying how long to wait |
| **Backoff** | waiting longer between each retry instead of the same pause |
| **Fallback** | the answer a layer builds itself when the layer below it could not help |
| **Wall clock** | the real time a person waited, as opposed to the time one call took |

---

## Self-check

**Question 1.** A service waits 15 seconds per model call and retries twice.
What is its worst case, and what is the smallest sensible timeout for an
application calling it?

**Question 2.** Your application times out and you fix it by raising retries
from 1 to 3. Say what this actually does to the person's experience, and say
what you should have changed instead.

**Question 3.** Your service returns `malformed_json` and a teammate wants to
retry it three times. Give their strongest argument, then say what you would do
and why.

---

### Answers

**1.** Three attempts at 15 seconds each is 45 seconds. The application's
timeout has to be larger than 45. Something like 60 gives room for the service's
own overhead and for a machine having a slow moment. Anything at or below 45
means the application can give up while the service is still working.

**2.** It makes it worse. Raising retries raises the service's worst case, which
means the application is now even more likely to give up first, and when it does
give up the person has waited longer for nothing. The thing to change is the
application's timeout, upward, past the service's worst case. If the real
problem is that the model is too slow to be usable, the fix is a smaller model
or a warm-up request at startup, not more attempts.

**3.** Their strongest argument: a truncated reply can be caused by a connection
that dropped part way through, which is exactly the kind of transient problem
retrying is for, so calling it deterministic is an assumption. That is a fair
point and the stack agrees with half of it, which is why `connection_broken` is
retried and `malformed_json` is not.

What I would do: leave it unretried and log the first 120 characters of the body
that failed to parse. If those logs show truncated JSON rather than a model that
writes prose, the classification was wrong and the fix is to move it into the
retryable set, with a note in the decision log saying what the logs showed. The
argument is settled by evidence, not by opinion, and you can get the evidence in
a week.
