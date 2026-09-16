# Lecture Notes: Four Failures, Four Messages
## 145130 Applications of AI · Module 5 · Week 14, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W14_FourFailuresFourMessages.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W14_FourFailuresFourMessages.pptx)

**Week 14 is the competition week. There is no instruction segment this week.**
This file is the lesson. Read it, work the three examples, and answer the
self-check before you go back to your build. It is written so you can do all of
that without asking anybody anything.

**This is the third exit criterion for this module:** wire an application to a
model and handle the model failing, timing out, or returning garbage.

---

## Why this exists

In 145060 you learned to handle a 404, a timeout, and a rate limit distinctly,
and you learned why "one message for every failure is a bug that does not
crash". That idea is the same. What is new is the shape.

Calling a model service has **two levels of failure**, and they are not the same
kind of thing. Your application can fail to reach the service. The service can
reach the model and get nothing usable. Those two have different owners,
different fixes, and different messages, and a program that mixes them up sends
the person looking in the wrong place.

---

## The concept in plain language

### Level one: the wire between your application and the service

Four outcomes. Four different fixes. Four different messages.

| Kind | What happened | What the person does |
|---|---|---|
| **ServiceDown** | nothing is listening at the service address | start the service, or fix the address |
| **Timeout** | the service is there and did not answer in time | wait and try again, or raise a timeout |
| **HttpError** | the service answered with a status and no usable envelope | look at the service's console |
| **MalformedPayload** | something answered, and it was not the envelope | you are pointed at the wrong port |

There is a fifth outcome that is not a failure of the wire: **RequestRejected**.
The service read your request and refused it, HTTP 400, and the envelope says
why. That is your mistake, not the service's, and nothing was asked of the
model.

### Level two: inside the envelope

The call succeeded. Now read `source`.

| `source` | `ok` | `error` | What it means |
|---|---|---|---|
| `model` | true | null | the model answered and the answer fit |
| `fallback` | true | set | the service built the answer itself. `error.kind` says why. |
| `none` | false | set | the request was refused and the model was never called |

**`ok` and `error` are not opposites. Read `source` first.** That sentence is on
the slide, in the io-spec, and in this file, because it is the single thing this
design most often gets wrong.

---

## Worked example 1: the four wire failures, captured

Every block below came off the build machine.

**ServiceDown.** Stop the service and run the client.

```
  The model service is not answering.
  nothing is listening at http://127.0.0.1:5157/.
  Start the service with: python contract_demo_service.py, then run this again.
```

Three lines: what happened, the detail, what to do. The client exits with code
1, so a script that called it can tell.

**MalformedPayload.** The most common mistake in this module, pointing the client
at the model endpoint instead of at the service.

```
  The reply was not the shape this program expects.
  the reply to HTTP 404 was not the response this program expects: the response has no source field
  Confirm http://127.0.0.1:11535/ is the model service and not another program. First 120 characters received: {"error": "not found"}
```

**Printing the first 120 characters of what it received is the whole trick.**
The person sees `{"error": "not found"}` and knows in one second that something
is answering and it is the wrong something. Without that line they spend the
period checking their JSON classes.

**Timeout.** The service is up and does not answer inside the client's own
timeout.

```
  The model service took too long.
  the service at http://127.0.0.1:5157 did not answer within 5 seconds.
  The model may still be loading. Try again in a minute.
```

**RequestRejected.** The service read it and said no.

```
  The model service refused this request.
  the service refused the request (prompt_empty): the prompt was empty once whitespace and control characters were removed
  Fix the request and send it again. Nothing was asked of the model.
```

That last sentence matters. It tells the person not to go looking at the model.

---

## Worked example 2: the C# that produces them

One class makes the HTTP call. Everything that can go wrong on the wire becomes
a `ClientFailure` with a kind, a message, and a sentence saying what to do.

```csharp
catch (TaskCanceledException) when (!token.IsCancellationRequested)
{
    // HttpClient reports its own timeout by cancelling the task. A
    // cancellation the caller asked for is a different thing, which is why
    // the token is checked before blaming a timeout.
    return ClientResult<TValue>.Failed(
        ClientFailureKind.Timeout,
        $"the service at {BaseAddress} did not answer within {http.Timeout.TotalSeconds:0.#} seconds.",
        "The model may still be loading. Try again, and raise the service timeout if it keeps happening.");
}
catch (HttpRequestException error) when (IsConnectionRefused(error))
{
    return ClientResult<TValue>.Failed(
        ClientFailureKind.ServiceDown,
        $"nothing is listening at {BaseAddress}.",
        "Start the service with: python contract_demo_service.py, then run this again.");
}
```

Two details you will get wrong if nobody tells you.

**`HttpClient` reports its own timeout as `TaskCanceledException`, not as a
timeout exception.** If you also use a `CancellationToken`, you have to check
whether the caller asked for the cancellation before you blame a timeout. That
is what the `when` clause is for.

**A refused connection arrives as `HttpRequestException` with a
`SocketException` inside it.** You read `socket.SocketErrorCode ==
SocketError.ConnectionRefused` to tell "nothing is there" from "something went
wrong on the way".

And the check that catches the wrong-port case, which no exception will catch
for you, because nothing threw:

```csharp
public string? Problem()
{
    if (string.IsNullOrWhiteSpace(Source)) return "the response has no source field";
    if (string.IsNullOrWhiteSpace(Task))   return "the response has no task field";
    if (Ok && !HasResult)                  return "the response says ok, but carries no result object";
    return null;
}
```

**A 200 status is not proof that the body is your envelope.** `System.Text.Json`
will happily deserialise `{"status": "ok", "data": {...}}` into your
`GenerateResponse` class and set every field it did not find to its default.
`Ok` becomes false, `Source` becomes null, nothing throws, and your program
prints something confident and empty.

---

## Worked example 3: the second level, inside the envelope

The call worked. Now read `source` and say what you found.

```csharp
string origin = envelope.CameFromModel ? "from the model" : "from the FALLBACK, not the model";
Console.WriteLine($"  [{envelope.Task}] {origin} in {envelope.ElapsedMs} ms");
if (envelope.Error is not null)
{
    Console.WriteLine($"  why: {envelope.Error.Kind}: {envelope.Error.Message}");
}
```

Captured, with the service unable to use the model:

```
  [headline] from the FALLBACK, not the model in 31 ms
  why: model_http_error: the model server answered with HTTP 500
  headline: Tempo run on the back trail.
```

And the same program with the model working:

```
  [headline] from the model in 32 ms
  headline: Stub headline: Tempo run on the back trail.
```

The person can tell the two apart in one word. Without that word the two runs
look the same, and the second one is a sentence copied out of the input by a
rule.

---

## The wrong version, and what it produces

Here is a real program from this module's Gate 2, and its real output.

```python
for task in TASKS:
    try:
        envelope = ask_with_retries(url, task, message["text"])
        show(envelope)
    except Exception:
        pass

from_model += 1
```

It runs. It never crashes. Here is what it printed with the service configured
so that the model was never used once:

```
Digest finished. 6 messages summarized by the model, 0 built from the fallback.
```

Every word of that is false. The model summarised nothing. The counter counted
loop iterations. The `except Exception: pass` swallowed two real failures. And
the program exited 0, so the script that ran it believed everything worked.

**Write this down**

> A program that reports success it did not have is worse than a program that
> crashes. A crash sends somebody to look. This sends nobody.

---

## Why the wrong version is tempting

Because `except Exception: pass` makes the red text go away, and the red text is
the thing that stops you from finishing.

It is one line, it is late in the period, the loop now runs to the end, and the
output looks complete. Not crashing feels like working. It is not the same
thing, and the gap between them is where this kind of bug lives.

**The habit that prevents it:** count what happened, not how many times the loop
went round. If your program prints a number at the end, that number has to come
from a variable that only goes up when the thing it names actually occurred.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Failure kind** | a fixed string naming what went wrong, for a program to branch on |
| **ServiceDown** | nothing is listening at the address |
| **MalformedPayload** | something answered and it was not the shape you expect |
| **RequestRejected** | the service read the request and refused it. Your mistake. |
| **Envelope** | the six fields every response carries |
| **`source`** | `model`, `fallback`, or `none`. The first field you read. |
| **Swallowing** | catching an exception and doing nothing, so the failure disappears |
| **Exit code** | the number a program gives the shell. 0 means finished. |

---

## Self-check

**Question 1.** Your program prints "Something went wrong" for all four wire
failures. Name the four fixes a person might need, and say which one they would
try first with no other information.

**Question 2.** `HttpClient` throws `TaskCanceledException` in two different
situations. Name both, and say how you tell them apart.

**Question 3.** The service returns HTTP 200 with the body
`{"status": "ok", "data": {"text": "hello"}}`. Your C# class deserialises it
without throwing. What does your program do next if you have not written a
`Problem()` check, and what does the person see?

---

### Answers

**1.** Start the service. Wait and run it again. Look at the service console.
Check the port you are pointed at. With no other information the person tries
the first one, restarting the service, which is right one time in four and
wastes several minutes the other three times. That is the cost of one message
for four problems.

**2.** It throws when its own timeout expires, and it throws when a
`CancellationToken` the caller passed in is cancelled. You tell them apart by
checking the token. A `TaskCanceledException` caught under a `when` clause that
says the token was not cancelled is the timeout case. Without that check you
report a timeout when the user pressed Ctrl+C.

**3.** `Ok` is false, `Source` is null, `Result` is an undefined `JsonElement`,
and nothing threw. A program that goes straight to printing will print an empty
summary, or hit a null reference two lines later and report a null reference
error, which says nothing about the real problem. With the `Problem()` check the
program reports that the reply has no `source` field, prints the first 120
characters it received, and the person sees `{"status": "ok", "data":` and
realises in one second that they are pointed at the wrong program.
