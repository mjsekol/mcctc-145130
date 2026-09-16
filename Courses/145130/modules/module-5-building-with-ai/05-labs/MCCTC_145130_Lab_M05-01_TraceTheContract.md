# Lab M05-01 · Trace the Contract
## 145130 Applications of AI · Module 5 · Week 13, Monday and Tuesday

**Competencies:** 5.6.5 (I/O requirements), 5.6.6 (design inputs, outputs, and
processes), 5.1.1 (how programs solve problems), 5.6.7 (document a design)

---

## The situation

The front office gets a pile of short pieces of writing every week and somebody
has to read all of them before anything happens. Somebody built a small program
that asks a language model running in this building to write a headline for each
one, so the pile can be skimmed instead of read.

In Module 1 you talked to a model directly. You sent a prompt to
`POST /api/generate` and read whatever came back. **That is not what you are
looking at today.** Today there is a program in between: a service that talks to
the model so your application does not have to.

**What you will build:** a filled-in trace table with seven real cases in it, and
a one page I/O summary you could hand to somebody writing a client.

**You are not writing code today.** You are learning to read a contract, because
tomorrow you write your own and on Thursday somebody else has to build against
it.

---

## Before you start

Copy `lab-m05-01-files/` to your own folder. Everything you need is in it. You
need three terminal windows and about ninety minutes across two days.

| File | What it is |
|---|---|
| `stub_model_server.py` | a stand-in for a model server, with ten behaviours you can choose |
| `contract_demo_service.py` | **a teaching prop.** A service you trace. Read its header. |
| `contract_probe.py` | prints one envelope, field by field, with the meaning of each |
| `CONTRACT.md` | the contract for the demo service. Read this first. |

Install Flask once, from anywhere:

```
python -m pip install flask
```

**Read `CONTRACT.md` first**, sections 1 through 4. This lab is a guided reading
of that file with a terminal open next to it.

### About the demo service

`contract_demo_service.py` is **not the service you are going to build.** It has
one task, one result field, one validation rule, and a parser that handles
exactly one of the four shapes a model answers in. Its header comment says all of
that in more detail and you should read it.

It is here so you have a running contract to trace before you design your own.
Copying it will not produce a passing project, and you will find out in this very
lab that its parser is not good enough.

### Every command names its port

This module runs the model server on **11535** and the service on **5157**.
Port 11434 is reserved for a real model server if one is ever running here.

**Type the port every time, even when it is the default.** A server that cannot
get the port it asked for stops without much noise, and then the next program
finds whatever else is on that port and talks to that instead. That does not look
like a failure. It looks like an answer.

---

## Steps

### Part 1, Monday. Start the two servers and capture the healthy cases.

**Step 1.** In terminal 1, in your copy of the lab folder:

```
python stub_model_server.py --port 11535
```

*Observable result:*

```
Stub model server on http://127.0.0.1:11535 in fenced_json mode. Press Ctrl+C to stop.
```

**Read that line.** If it does not appear, the server did not start, and
everything after this will talk to whatever else is on that port. Leave it
running.

**Step 2.** In terminal 2, same folder. In PowerShell:

```
$env:DEMO_MODEL_URL = "http://127.0.0.1:11535"
$env:DEMO_SERVICE_PORT = "5157"
python contract_demo_service.py
```

In `cmd`, use `set DEMO_MODEL_URL=http://127.0.0.1:11535` and
`set DEMO_SERVICE_PORT=5157` instead.

*Observable result:* three lines, the service name and port, then the model
endpoint and the timeout, then a warning about a development server. That warning
is correct and expected.

**Step 3.** In terminal 3, same folder, run the health probe. The probe defaults
to 5157, so there is nothing to set, and it prints the address it used on its
first line. Read that line every time.

```
python contract_probe.py health
```

*Observable result:* ten fields, ending in `tasks ["headline"]`. Write down what
`model_reachable` says, and write down `timeout_seconds` and `retries`. You will
need both numbers on Tuesday.

**Step 4.** Run the headline case with a request of your own invention. Do not
use anything a real person actually sent you.

```
python contract_probe.py headline --text "The 3D printer in room 118 jammed near the nozzle. I cleared it but the first layer will not stick."
```

*Observable result:* six envelope fields, then `result in full`, then a verdict
line. Copy `ok`, `source`, `elapsed_ms`, and `error` into row 1 of your trace
table.

**Look at the headline.** It starts with two particular words that do not appear
anywhere in what you sent. Write those two words down. When they stop appearing,
the model stopped being used.

**Step 5.** Run the same command again with `--raw` on the end.

*Observable result:* the whole body, printed as JSON, after the table. Read the
field order. It is the same every time, and that is the point of the envelope.

### Part 2, Monday. Make the service refuse you.

**Step 6.** Send a task the service does not know.

```
python contract_probe.py bad-task
```

*Observable result:* HTTP 400, `source` of `none`, `result` of null, and an error
kind of `unknown_task`. Row 2. **Write down `elapsed_ms`.**

**Step 7.** Send a prompt one character over the cap.

```
python contract_probe.py long-prompt
```

*Observable result:* HTTP 400 and `prompt_too_long`, and the message names the
real length. Row 3.

**Step 8.** Send four spaces.

```
python contract_probe.py empty-prompt
```

*Observable result:* HTTP 400 and `prompt_empty`. Row 4.

### Part 3, Tuesday. Break the model three different ways.

**Step 9.** Go to terminal 1, press Ctrl+C, and start the stub again in a
different mode. Leave the service running the whole time.

```
python stub_model_server.py --port 11535 --mode bare_json
```

Then, in terminal 3, run the headline command from step 4 again.

*Observable result:* `source` is now `fallback`, `ok` is still true, and there is
an error kind. Row 5. **The model answered perfectly well.** Read the answer the
stub sends in `bare_json` mode and work out why the service could not use it.

**Step 10.** Same again, in `error` mode.

```
python stub_model_server.py --port 11535 --mode error
```

*Observable result:* `fallback` again, with a different error kind. Row 6. Note
`elapsed_ms` and compare it with row 5.

**Step 11.** Now stop the stub entirely and do not start it again.

```
python contract_probe.py health
python contract_probe.py headline --text "The 3D printer in room 118 jammed near the nozzle."
```

*Observable result:* `model_reachable` is now false, and three extra lines appear
explaining what that means. **The service did not go down.** Then the headline
command gives `fallback` with a third error kind. Row 7.

**Write down `elapsed_ms` and compare it with row 6.** The difference is worth a
sentence.

**Step 12.** Fill in the last column of every row: in one sentence, what should a
program show the person for this case.

**Step 13.** Write the one page I/O summary. Four short sections: the request, the
envelope, the result shape, and the error kinds you saw. Write it for somebody who
has not read `CONTRACT.md`.

**Step 14.** Stop everything. Ctrl+C in terminal 2. Then check nothing was left
behind:

```
netstat -ano | findstr "5157 11535"
```

No output means both ports are free. A port still in use here is the thing that
causes scenario 5 in next week's lab.

---

## The trace table

Copy this into your repository as `trace-table.md` and fill it in.

| # | What you sent, and the stub's mode | HTTP | `ok` | `source` | `elapsed_ms` | `error.kind` | What a program should show |
|---|---|---|---|---|---|---|---|
| 1 | headline, `fenced_json` | | | | | | |
| 2 | an unknown task | | | | | | |
| 3 | 4001 characters | | | | | | |
| 4 | four spaces | | | | | | |
| 5 | headline, `bare_json` | | | | | | |
| 6 | headline, `error` | | | | | | |
| 7 | headline, no stub running | | | | | | |

---

## Acceptance criteria

Check these yourself before you submit.

1. All seven rows are filled in with values you actually saw, not values you
   expected.
2. Rows 2, 3, and 4 all have `elapsed_ms` of 0, and you can say why in one
   sentence.
3. Rows 5, 6, and 7 all have `ok` true and an `error` set, and your last column
   does not call any of them a failure.
4. Rows 5, 6, and 7 have **three different error kinds**, and you can say what
   each one means.
5. Row 7's `elapsed_ms` is much larger than row 6's, and you can say what the
   difference is made of.
6. You can say what the demo service did with the `bare_json` answer, and why
   that is the service's fault and not the model's.
7. Your I/O summary names all six envelope fields, the result shape, and what
   `source` can be.
8. Committed and pushed before the end of the period.

---

## If it breaks

**`ModuleNotFoundError: No module named 'flask'`**
Run `python -m pip install flask`.

**`OSError: [WinError 10048] Only one usage of each socket address ... is normally permitted`**
Something from an earlier run is still on that port. Find it with
`netstat -ano | findstr "5157 11535"`, or use a different port with
`set DEMO_SERVICE_PORT=5158` and then `set DEMO_SERVICE_URL=http://127.0.0.1:5158`
before you run the probe. **Do not solve this by dropping the port and using the
default.** That is how you end up talking to somebody else's server.

**The probe prints `Nothing answered.` and a `WinError 10061`**
The service is not running, or you are pointed at the wrong port. Check terminal
2. Check the first line the probe printed, which is the address it used.

**The probe prints `The body was not JSON at all` and shows something else**
You are pointed at the model server, not at the service. The model is on 11535
and the service is on 5157. This is the most common mistake in this lab and it is
worth making once on purpose.

**Every row says `fallback`, including row 1**
Your stub is not in `fenced_json` mode, or the service is pointed at a different
port from the one the stub printed. Read both lines again.

---

## Stretch goal

Add an eighth row. Point `DEMO_SERVICE_URL` at the **stub model server** on 11535
and run any headline command. Record what the probe prints, and explain in two
sentences why nothing crashed and how the probe worked out that the body was not
the envelope.

---

## Submission checklist

- [ ] `trace-table.md`, seven rows, every cell from a real run
- [ ] `io-summary.md`, one page, four sections
- [ ] Your answer to acceptance criterion 5, about where the two seconds went
- [ ] Your answer to acceptance criterion 6, about the `bare_json` answer
- [ ] Committed and pushed

---

## Extended options

Choose one. All four are graded on the same scale and assess the same
competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes | Give them |
|---|---|
| Still trying to get three terminals running at step 2 | SCAFFOLDED |
| Through step 5 and filling the table without asking | STANDARD or EXTENDED |
| Asks what happens if two people run the service at once | EXTENDED |
| Asks what any of this has to do with their own project | APPLIED |

### SCAFFOLDED

Same target, less setup. Never start the stub at all, so skip terminal 1 entirely
and every answer is a fallback from the first command. Fill in rows 1, 2, and 7
only, three rows instead of seven, and note that row 1 will say `fallback` too.

Your I/O summary is the envelope table and the `source` table, and does not need
the result shape.

**Extra checkpoint:** after step 3, show your instructor your health output before
you go on. If `model_reachable` says anything other than false, stop and sort that
out first.

### STANDARD

The lab as written. Seven rows, three parts, the I/O summary.

### EXTENDED

Everything in STANDARD, plus three more rows from three more stub modes.

```
python stub_model_server.py --port 11535 --mode malformed
python stub_model_server.py --port 11535 --mode not_done
python stub_model_server.py --port 11535 --mode empty
```

For each, record the error kind and answer one question in writing: **would
retrying this request help, and why?**

Then check your three answers against section 5 of `CONTRACT.md` and write down
any you got wrong.

*Hint, not the answer:* `contract_demo_service.py` has a set called
`RETRYABLE_KINDS` in it. Read the comment above it about what the kinds in the set
have in common **before** you look at which ones they are.

### APPLIED

Same skill, different domain, no model involved. Pick any program on your machine
that talks to another program over HTTP and has documentation you can read. A
game launcher's local API, a printer's web interface on the school network with
permission, a public transit feed.

Send it three requests you are allowed to send, one good and two wrong, and build
the same trace table for what came back.

Then answer the question this lab is really about: **does that service have an
envelope?** Is there one shape that comes back for every outcome, or does a
failure look completely different from a success? Write half a page on which
design you would rather build a client against, with an example of each from what
you captured.
