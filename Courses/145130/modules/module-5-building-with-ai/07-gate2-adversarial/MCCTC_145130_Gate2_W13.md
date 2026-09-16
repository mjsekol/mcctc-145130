# Gate 2: Adversarial Review · Week 13
## 145130 Applications of AI · Module 5 · Week 13, Friday · Build 2

**40 minutes.** Individual. Silent. You may and should run the code. **You may not
ask a model whether it is correct, because a model is what is being reviewed.**

The program is `gate2-w13-files/study_service.py`. It comes with a stand-in model
server, `fake_model.py`, in the same folder. Copy both.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got
`study_service.py` back. It runs. It has docstrings, named constants, and a clean
envelope. It looks like something you would be pleased to have written.

**Five defects, one in each category:** Correctness, Security, Readability,
Performance, Requirements Fit.

**Plus one item that is not a defect.** Item 6 is a design decision with a real
argument on each side. You are scored on your reasoning, not on which side you
pick.

**The security defect is not in a place that crashes.** It is visible on the happy
path, in a response anybody on the network can ask for.

---

## PART A: The requirements

> Write `study_service.py`, a Flask service that wraps the local model for the
> study planner. It must:
>
> 1. `POST /plan` takes `{"request": str}` and returns an envelope with `ok`,
>    `result`, `source`, `elapsed_ms`, and `error`.
> 2. Read the model endpoint, the model name, and the timeout **from the
>    environment**. **Store no credential anywhere**, because a local model needs
>    none.
> 3. Turn the model's answer into `{"title", "steps", "minutes"}` **whether or not
>    the model wraps it in a code fence**.
> 4. When the model cannot be used, build a plan without it and **set `source` to
>    `fallback`** so the caller knows.
> 5. `GET /health` answers in milliseconds and never asks the model to generate
>    anything.
> 6. Refuse a request over 4000 characters rather than working with part of it.

---

## PART B: Running it

Two terminals, in the folder you copied.

```
python fake_model.py --port 11535
```

```
python study_service.py
```

The service listens on 5161. Send it a request from a third terminal, or from any
tool you like.

```
python -c "import json,urllib.request; r=urllib.request.Request('http://127.0.0.1:5161/plan', json.dumps({'request':'I have a chemistry test Friday on moles.'}).encode(), {'Content-Type':'application/json'}); print(urllib.request.urlopen(r).read().decode())"
```

**The stand-in model has five modes.** Stop it and start it again with a different
one. This is the fastest way to find two of the five defects.

```
python fake_model.py --port 11535 --mode fenced_json
python fake_model.py --port 11535 --mode bare_json
python fake_model.py --port 11535 --mode prose
python fake_model.py --port 11535 --mode refusal
python fake_model.py --port 11535 --mode error
```

**Also ask the service about itself.**

```
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5161/health').read().decode())"
```

---

## What to submit

For each defect: **file and line number**, **which of the five dimensions**,
**what goes wrong for a real person**, and **the fix**.

Then item 6, the design decision, with the strongest argument on each side and
your own position.

Then one final entry: **what I was unsure about**, naming something specific. That
entry is scored, and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 10:** run it in `fenced_json` mode and confirm it works. Then run the
  same request in `bare_json` and `prose` and compare the three envelopes.
- **Next 10:** read Part A one requirement at a time and point at the line of code
  that meets it. A requirement you cannot point at is a finding.
- **Next 10:** ask the service for its health and read every field it sends back.
  Then read every constant at the top of the file and ask whether the code below
  uses it.
- **Rest:** read each comment against the code under it. Ask whether it is true.

---

## Scoring

Five defects, one point each. Item 6 is one point, scored on reasoning. The
unsure-about entry is one point. Seven points.

**The security defect is double-penalized.** Missing it costs two points rather
than one. Your instructor states this before you start.

**Five of seven is a strong score.**
