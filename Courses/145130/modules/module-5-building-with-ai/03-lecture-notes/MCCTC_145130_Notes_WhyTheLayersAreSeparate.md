# Lecture Notes: Why the Model Layer and the Application Layer Are Separate
## 145130 Applications of AI · Module 5 · Week 13, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W13_WhyTheLayersAreSeparate.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W13_WhyTheLayersAreSeparate.pptx)

If you missed class, you can learn this concept from this file alone. To run the
examples you need `05-labs/lab-m05-01-files/` and two terminal windows.

**In Module 1 you talked to a model directly**, sending a prompt to
`POST /api/generate` and reading whatever came back. This module puts a program
in between, and everything below is about why.

**This is the first of the three exit criteria for this module:** explain why the
model layer and the application layer are separate. You will be asked to say it
out loud at your demonstration, without reading it.

---

## Why this exists

You already know how to call something over HTTP. You did it in 145060 with a
weather feed and again with a local model. So the new thing this week is not the
HTTP call. It is the question of where you put the boundary.

Here is the problem in one sentence. **A language model answers in prose, and
your program needs a shape.** Somebody has to turn one into the other, and where
you put that somebody decides how much of your program has to know about mess.

Put it in the wrong place and every screen in your application ends up with a
little bit of parsing in it. Put it in the right place and your application
never sees a model word it did not ask for.

---

## The concept in plain language

There are two programs, not one.

**The model service** is Python. It talks to the model, sends the prompt, waits,
reads the answer, pulls a shape out of it, checks the shape, and hands back the
same six fields every single time.

**The application** is C#. It sends a task and a prompt over HTTP, reads six
fields, and prints something. It does not know what a token is. It does not know
what a code fence is. It does not know the model exists.

Between them is a written contract. For the demo service in this week's lab that
is `CONTRACT.md`, and it says exactly what goes in, exactly what comes back, and
exactly what every failure is called.

```
You -> your application (C#) -> your model service (Flask) -> local model or stub
          HttpClient               /health /generate           /api/generate
```

### The four reasons, and you should be able to give all four

**1. Different jobs, different languages.** Model runtimes, tokenizers, and
retrieval libraries are written in Python. Your application is C#. Rewriting a
model runtime in C# so you can avoid one HTTP call is a bad trade.

**2. One place knows about mess.** A model wraps JSON in a code fence about half
the time. Sometimes it writes "Sure, here is the JSON you asked for" first.
Sometimes it politely refuses. All of that is handled inside the service. The C#
side receives the same six fields whatever happened.

**3. One place knows how to fail.** The timeout, the retry policy, and the
fallback all live below the HTTP boundary. When the model is missing, the C#
program does not change at all. It gets an envelope with `source` set to
`fallback`.

**4. You can replace either side.** Point the service at a different model by
changing one environment variable. Put a web front end on the same service
without touching model code. Next semester in 145010 you will do exactly that.

---

## Worked example 1: the same program, with and without a model

Start the service with nothing behind it. From `05-labs/lab-m05-01-files/`,
without starting the stub at all:

```powershell
python contract_demo_service.py
python contract_probe.py health
```

Captured on the build machine, where no model runtime is installed:

```
  service          contract-demo-service
  model_endpoint   http://127.0.0.1:11535
  model_reachable  false
  checked_by       tcp_connect
  tasks            ["headline"]

  The service is up and cannot see a model. Every answer will be a
  fallback. That is a different problem from the service being down,
  and it has a different fix.
```

Now ask it to do something anyway:

```
  source       fallback
  elapsed_ms   2057
  result in full:
    headline: The 3D printer in room 118 jammed near the nozzle.
  error kind:    connection_refused
  error message: nothing is listening at http://127.0.0.1:11535
```

**Read that again and notice what did not happen.** Nothing crashed. Nothing
printed a stack trace. Nothing had to be recompiled. The caller got a headline,
the same field it always gets, and one extra piece of information: this did not
come from the model.

That is what a boundary buys you. The model disappeared and exactly one layer
noticed.

---

## Worked example 2: what the C# side would look like without the boundary

This is not in any file you have. It is what the same feature looks like when
the model and the application are the same program.

```csharp
// Do not write this.
string answer = await model.GenerateAsync(prompt);
if (answer.StartsWith("```json"))
{
    answer = answer.Substring(7).TrimEnd('`');
}
else if (answer.Contains("{"))
{
    answer = answer.Substring(answer.IndexOf('{'));
}
var result = JsonSerializer.Deserialize<Summary>(answer);
Console.WriteLine(result.Summary);
```

Four things are wrong with that, and none of them are about style.

1. Every screen that calls the model needs its own copy of the fence handling.
2. The day the model starts answering in prose, every one of those copies breaks.
3. There is no timeout, no retry, and no fallback, so the model being slow is
   now your application's problem.
4. `Deserialize` returns null when the shape does not fit, and the next line
   dereferences it. The failure is a crash three lines later with a message
   about a null reference, which tells the person nothing.

Compare that with a C# side that has a service under it:

```csharp
ClientResult<GenerateResponse> result = await client.GenerateAsync("headline", text);
if (result.Ok == false)
{
    ReportFailure(result.Failure);
    return 1;
}
PrintEnvelope(result.Value!);
```

No parsing. No guessing. No knowledge that a model exists.

---

## Worked example 3: the contract is the interesting part

One envelope, whatever happened. Here is a real answer from the demo service,
captured with the stub standing in for a model:

```json
{
  "ok": true,
  "task": "headline",
  "result": {"headline": "Stub headline: The 3D printer in room 118 jammed near the nozzle."},
  "source": "model",
  "elapsed_ms": 32,
  "error": null
}
```

And here is the same request when the model server returned HTTP 500:

```json
{
  "ok": true,
  "task": "headline",
  "result": {"headline": "The 3D printer in room 118 jammed near the nozzle."},
  "source": "fallback",
  "elapsed_ms": 31,
  "error": {"kind": "model_http_error", "message": "the model server answered with HTTP 500"}
}
```

Same six fields. Same order. `ok` is true in both, because in both cases the
caller got something it can use.

### Write this down

> `ok` and `error` are not opposites. Read `source` first.

`source: "fallback"` with `ok: true` and an error set is the normal, correct,
working state of this system when the model is unavailable. A program that
treats it as a failure will refuse to work on a day when it could have worked.

---

## The wrong version, and the exact thing it produces

The tempting shortcut is to decide that the boundary is extra work, and to have
the C# program read `ok` and stop there.

```csharp
if (envelope.Ok)
{
    Console.WriteLine(summary.Summary);   // looks fine
}
```

Run that against a service that cannot see a model, and here is what a person
sees:

```
  headline: My laptop keeps dropping the wifi in the back corner of the lab.
```

No error. No warning. Nothing red. That sentence was not written by a model. It
is the first sentence of the ticket, copied by a rule in the service, and the
program presented it as if a model had summarised it.

**This is the shape you have met in every course here: the dangerous failure is
the one that does not crash.** In 145060 it was a slice that lost a digit. Here
it is a summary that was never summarised.

---

## Why the wrong version is tempting

Because the boundary costs you something real and you pay it first.

Two programs means two things to start, two sets of logs, two places a bug can
be, and a whole file of contract to agree on before either one works. On Week 13
Monday that is all cost and no benefit, and the version with everything in one
program will be running before yours is.

The benefit arrives on the day the model is missing, or slow, or answering in a
shape you did not plan for. In this building that day is most days. The stack
you are reading was built on a machine with no model runtime installed at all,
and every line of output in these notes came off that machine.

**The habit that prevents it:** when you find yourself about to write a string
operation on something a model wrote, stop and ask which side of the boundary
you are on. If the answer is the application side, you are in the wrong file.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Layer** | one program with one job, that talks to the layer below it through an agreed interface |
| **Contract** | the written agreement about what crosses a boundary. This week, `CONTRACT.md`. |
| **Envelope** | the fixed set of fields every response carries, whatever happened |
| **Result shape** | the fields one task returns inside the envelope. `summarize` returns two, `classify` returns two. |
| **Source** | where the answer came from: `model`, `fallback`, or `none` |
| **Fallback** | an answer the service built without the model, labelled so the caller knows |
| **Service** | a program that answers requests over HTTP and does not have a screen |
| **Endpoint** | one address a service answers on, such as `/health` or `/generate` |
| **Loopback** | `127.0.0.1`, this machine only. Nothing on the network can reach it. |

---

## Self-check

**Question 1.** The C# program prints a summary and the person is happy. Name
the one field that tells you whether a model was involved, and say what the
other two possible values of that field mean.

**Question 2.** Your teammate says the boundary is a waste of time because the
whole thing would be shorter as one Python program. Give the strongest version
of their argument, then give the strongest answer to it.

**Question 3.** The service returns `{"ok": true, "source": "fallback", "error":
{"kind": "timeout", ...}}`. Is this a failure? Say what the C# program should do
and what the person should see.

---

### Answers

**1.** `source`. `model` means the model answered and the answer fit the task.
`fallback` means the service built the answer itself, without the model, and the
`error` field says why. `none` means the service refused the request before
calling the model, and `ok` is false.

**2.** The strongest version of their argument: one program is fewer moving
parts, there is no HTTP call to go wrong between your own two halves, you do not
have to keep a contract document in step with two codebases, and on a two week
project the boundary is pure overhead. That is all true.

The strongest answer: the boundary is not there to help you this week. It is
there because the model layer changes for reasons your application does not care
about, and your application changes for reasons the model layer does not care
about. Module 6 puts a usability study in front of the C# side and the service
does not move. Next semester you put a web front end on the same service. Also,
the model runtime is Python and your application is C#, so the two programs
already exist. The only question is whether the boundary between them is written
down.

**3.** Not a failure. `ok` is true, so `result` holds something usable. The C#
program should print the result **and** say plainly that it came from the
fallback and not from the model, with the reason. The person should see the
answer, the words `FALLBACK, not the model`, and `why: timeout: no answer from
the model within 5 seconds`. They can then decide for themselves how much to
trust it, which is a decision the program is not allowed to make for them.
