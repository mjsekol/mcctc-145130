# Lecture Notes: Integrating Into Systems That Already Exist
## 145130 Applications of AI · Module 1 · Week 2, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W02_IntegratingIntoExistingSystems.md)

**There is no exported deck for this lesson yet.** The outline is current. The old export
described the model service, which came out of this module, so it was removed rather than
left in place: a deck that contradicts the lesson is worse than no deck. The Gamma account
ran out of credits before it could be regenerated. Teach from the outline, or generate the
deck once credits are available:

```
node tools/gamma.js Courses/145130/modules/module-1-foundations-of-ai/04-slides/MCCTC_145130_Slides_W02_IntegratingIntoExistingSystems.md --export pptx
```

If you missed class you can learn this from this file alone. You need the files
in `../05-labs/local-model-kit/` and `../05-labs/lab-m01-02-files/`.

**Competency 2.4.2:** describe the fundamental architectures of emerging
technologies and how they are integrating into the existing systems of
information technology.

---

## Why this exists

Yesterday you named nine technologies and the systems each one has to be bolted
onto. Today you stand at one of those joints and push on it until it fails, and
you write the policy for what happens when it does.

The joint is called a **seam**. Yours is one HTTP call to a model server. Nearly
all the interesting failures live there rather than inside either side of it.

**Nothing sits between you and the model in this module.** There is no layer
catching failures on your behalf, which means the failure policy is yours to
write. That is today's work, and it is also the argument you will make for
building a service layer in Module 5.

---

## The concept in plain language

A finished seam has three parts. You need all three before you can call an
integration done.

**A contract.** What goes out, what comes back, what every field means. Yours is
one page: `POST /api/generate` with a model, a prompt, and `stream: false`, and
a reply with `model`, `response`, and `done`.

**A failure policy.** What happens when the far side is down, slow, or wrong.
Not "it errors". Specifically: how long you wait, whether you try again, how many
times, and what the person is told.

**A record of provenance.** Something that says where a value came from and how
you got it. Not a field somebody hands you. A field **you** decide to keep.

If you remember one thing: **an integration without a record of provenance is
not finished**, and nobody will add one later, because by then the runs that
needed it are gone.

---

## Worked example 1: the same request, seven ways

This table came out of `seam_report.py` on the build machine. One help request,
sent once per stand-in mode, so the only thing changing between rows is the
failure.

| stub mode | HTTP | kind | retried | model calls | elapsed ms |
|---|---|---|---|---|---|
| success | 200 | ok | no | 1 | 15.7 |
| success_prose | 200 | ok | no | 1 | 0.7 |
| error | 500 | http_error | no | 1 | 15.3 |
| rate_limited | 429 | rate_limited | **yes** | **2** | 12.5 |
| malformed | 200 | malformed_json | no | 1 | 15.3 |
| unusable | 200 | **ok** | no | 1 | 15.8 |
| slow | none | timeout | **yes** | **2** | 5020.6 |

Four things to stop on.

**The `kind` column is not given to you.** Your program works it out from what it
can observe: did anything arrive, was the status 200, was the body JSON, did it
say done, was there text. Working outward in that order is not a style choice.
Each check only makes sense if the one before it passed.

**The `retried` column is your rule, not the server's.** Nothing retries for you.

**Look at the `unusable` row.** The stand-in answered "I am not able to help with
that request." HTTP 200, valid JSON, `done: true`, real text in `response`.
**Every transport-level check passes and the answer is useless.** A program that
only checks the transport calls this `ok`, and it is right to, and it is still
going to show a refusal to somebody as though it were an answer.

That row is the argument for Module 5 in one line: **somebody has to check the
answer against what the task actually needs, and it should not be every program
separately.**

**Look at `success_prose` at 0.7 ms.** The timing on a loopback socket is noise.
Week 3 is about why that matters.

---

## Worked example 2: which failures are worth retrying

Two rows retried. Five did not. The rule is not a list to memorise:

> **Retry a failure that might come out differently next time. Never retry one
> that will not.**

A timeout, a rate limit, and a refused connection are about timing. Wait, and the
same request can succeed. Malformed JSON is about the content of the answer, and
sending the same request to the same system gets the same broken answer while
costing another wait.

Retrying a broken body is not caution. It is the same mistake, repeated, at the
expense of somebody's period.

**One honest complication.** A real model samples with randomness, so a second
ask genuinely can parse when the first did not. That is a real argument for
retrying an unparseable answer **once**, and it is a different argument from
retrying a timeout. If you make it, make it out loud and cap it.

---

## Worked example 3: the sentences a caller owes

Four distinct fixes, so at least four distinct sentences:

```python
def sentence_for(kind):
    if kind == "ok":
        return "Answer from the model."
    if kind == "refused":
        return "No model is running. Start the model server, then try again."
    if kind in ("timeout", "rate_limited"):
        return "The model did not answer in time. Wait a moment and try again."
    if kind == "http_error":
        return "The model server has a problem of its own. Tell an adult."
    return ("The model answered with something this program cannot use "
            f"({kind}). Save the reply and report it.")
```

**`timeout` and `rate_limited` sharing a sentence is correct**, because the
action is identical. Two problems with two different actions may not share one.

Notice the last branch keeps the kind in the message. The person cannot act on
`malformed_json`, but the adult they show it to can.

---

## The wrong version, and the exact damage it does

```python
try:
    answer = ask_model(text)
    print(read_label(answer))
except Exception:
    print("AI unavailable")
```

**The first line hides provenance.** A label parsed cleanly from JSON and a
fragment sliced out of a sentence print identically.

**The second line hides the fix.** The server being down, a rate limit, a
malformed body, and a prompt the server refused all print the same four words,
and they have four different fixes. The one piece of information the person
needed is the one thing thrown away.

There is a third cost, and it arrives later. Three weeks on, somebody asks how
often the model actually gave a usable answer, and nobody can tell, because
nothing was ever recorded.

---

## Why the wrong version is tempting

It is short, it never crashes, and it looks defensive. Wrapping everything in one
`except` feels like care. It is the opposite: a decision not to think about which
failures can happen, made once, silently, and paid for by whoever is using the
program when one happens.

The habit that prevents it: **list the failures on paper before you write any
handling.** Today's seam report is that list, produced by forcing every one of
them. Write the list first and the code writes itself.

### Write this down

> An integration is three things: a contract, a failure policy, and a record of
> where each value came from. Two out of three is not two thirds finished.

---

## Vocabulary

| Term | What it means |
|---|---|
| **seam** | the joint where a new system meets one that already existed |
| **contract** | the agreed shape of what crosses the seam |
| **failure policy** | how long you wait, whether you retry, and what you say |
| **provenance** | where a value came from, and how you got it |
| **transient failure** | one that might succeed if repeated |
| **deterministic failure** | one that will fail the same way every time |
| **timeout** | the limit on how long you wait before giving up |
| **rate limit** | a server telling you to send fewer requests |
| **`/stub/stats`** | how the stand-in reports its call count, so you can see a retry from outside |

---

## Self-check

**1.** Your program sends 40 requests and 12 come back with a kind of
`malformed_json`. Is that a failure of your program? Answer it, and say what you
would put on the screen and what you would record.

**2.** A teammate adds three retries around a `malformed_json` result. Say what
it costs, what it gains, and what you would do instead.

**3.** The `unusable` row is HTTP 200 with `done: true` and real text. Say why a
transport-level check calls it `ok`, and what would have to happen for a program
to catch it.

### Answers

**1.** Not a failure of your program, and your program is the only thing that can
report it honestly. On screen: show that 12 answers could not be read, with the
kind. In the record: keep the kind and the raw answer for each one, because that
is the evidence somebody needs to work out whether the prompt is wrong, the model
is wrong, or the parser is.

**2.** It costs three times the wait for the same unusable answer, because the
failure is about the content rather than the timing. It gains something only if
the model samples with randomness, in which case a second ask can genuinely
differ. What I would do: one extra attempt at most, with the reason written down,
and never three.

**3.** Because every question a transport-level check asks has the right answer:
something arrived, the status was 200, the body was JSON, `done` was true, and
`response` held text. Nothing at that level asks whether the text contains what
the task needed. Catching it requires checking the answer against the shape the
task requires, which means somebody has to define that shape first. That check is
what the Module 5 service exists to do in one place.
