# Gate 2 · Week 17 · Supply Sweep
## 145130 Applications of AI · Module 6 · Week 17, Friday, Build 1

**40 minutes. Individual. Silent. No AI tool.**

**You may and should run it.** Files in `gate2-w17-files/`. **Port 5159.**

---

## The situation

The school store keeps a small stock of the things people run out of in the middle
of a build: filament, gloves, safety glasses, tape, lanyards, resin, SD cards.
Somebody wrote an automation to read the weekly inventory export, decide what to
reorder, sort each request note into a category through the model service, and give
the store manager a list.

**It runs. It produces a reorder list. The store manager has been using it.**

---

## Your job

**Find five defects, one per dimension.**

```
Correctness      off-by-one, wrong operator, bad boundary
Security         a rule about data, a credential, missing validation
Readability      a misleading name, a comment or docstring that lies
Performance      repeated work, unnecessary round trips
Requirements Fit something the spec asked for that is missing, or invented
```

**Read `REQUIREMENTS.md` before you read a line of code.** Every defect is a
disagreement between that file and `supply_sweep.py`.

**There is also one item that is genuinely arguable**, and it is not one of the
five.

---

## What is in the folder

| File | What it is |
|---|---|
| `REQUIREMENTS.md` | What this was supposedly built from. Eight requirements |
| `supply_sweep.py` | The program |
| `requests.json` | The weekly export. Seven requests, all invented |
| `sweep_service_stub.py` | The stand-in service. Takes `--port`. Six modes |

---

## How to run it

```
python sweep_service_stub.py --port 5159
python supply_sweep.py --service http://127.0.0.1:5159 --once
```

**The stub also answers this, and it is in the bundle for a reason:**

```
curl http://127.0.0.1:5159/stub/stats
```

**Other states worth producing:**

```
python sweep_service_stub.py --port 5159 --mode error500
python supply_sweep.py --service http://127.0.0.1:5159 --source missing.json --once
```

**Port 5159, every command.** A real model listens on 11434 and is not ours to
take, the lab stub has 5158, and a program that reaches the wrong server does not
fail, it answers.

---

## What to hand in

### Five findings, one per dimension

```
Dimension           which of the five
Line number         in supply_sweep.py
The requirement     which R it breaks
What goes wrong     for a real person, in one sentence
The fix             what you would change
```

**"What goes wrong for a real person" is the part that separates a 5 from a 3.**

### Plus one entry: the thing you are unsure about

```
What you noticed
The case that it is fine
The case that it is a defect
What would settle it
```

---

## Two things worth saying before you start

**One defect is invisible unless you produce a state.** Run it and compare a number
against the requirements. One of the four commands above makes it obvious.

**One defect is invisible unless you read a file the program wrote.** Open
everything it produces.

---

## Scoring

| Item | Points |
|---|---|
| Correctness finding | 1 |
| **Security finding** | **1, and missing it costs 2** |
| Readability finding | 1 |
| Performance finding | 1 |
| Requirements Fit finding | 1 |
| The unsure-about entry, with both cases | 1 |
| **Total** | **6, and the lowest possible score is negative** |

---

## One rule for today

**A finding with no line number is not a finding.** The program is 220 lines. Every
one of the five is on a line you can point at.
