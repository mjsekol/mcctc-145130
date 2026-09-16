# Lecture Notes: Troubleshooting an Integration With a Named Method
## 145130 Applications of AI · Module 5 · Week 14, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W14_TroubleshootingAnIntegration.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W14_TroubleshootingAnIntegration.pptx)

**Week 14 is the competition week. There is no instruction segment this week.**
This file is the lesson, and it is the one you use in the lab the same day. You
can work all of it without asking anybody anything.

**Competencies 2.11.1, 2.11.2, 2.11.5, and 2.11.8:** identify the problem,
select a troubleshooting methodology, design a solution, and document the
problem and the verified solution. The WebXam has four items on this outcome.
The evidence is your written troubleshooting log.

---

## Why this exists

In 145060 you learned a six step method for finding a bug in one program:
reproduce it, form one theory, test the theory, change one thing, verify,
document.

An integration has three programs in it. The bug is almost never in the program
you are looking at, and the symptom almost never points at the layer that caused
it. So the six steps still apply, and step two gets harder, because "form one
theory" now has three places to point at.

That is what a **methodology** is for. It tells you where to look first, so you
are not picking at random and calling it intuition.

---

## The concept in plain language

The Ohio competency list names four methodologies. Pick one, by name, before you
start. Saying "I looked at it" is not a methodology, and it is not worth points.

### Top down

Start at the layer closest to the person and work down. The application, then
the service, then the model.

**Use it when** the symptom is something the person reported, and you have no
reason yet to suspect any particular layer. It is the default.

### Bottom up

Start at the layer closest to the machine and work up. The model, then the
service, then the application.

**Use it when** something changed underneath you: a new machine, a new model, a
different port, a fresh install. Also when the problem is about how things
behave rather than about what they say, like output arriving in the wrong order.

### Follow the path

Take one request and walk it end to end, writing down what you see at every
boundary it crosses.

**Use it when** the answer is arriving and it is wrong, rather than not arriving
at all. It is slow and it is the one that never fails to find something.

### Spot the differences

Compare a case that works with a case that does not, and list every difference
until one of them explains it.

**Use it when** you have a working baseline. This is why `scenario.py` has a
healthy scenario 0 in it. Without something that works, this method has nothing
to compare against.

### Choosing

| What you have | Method |
|---|---|
| a person's complaint and nothing else | top down |
| something in the environment changed | bottom up |
| an answer that arrives and is wrong | follow the path |
| a case that works and a case that does not | spot the differences |
| every case fails the same way | spot the differences, on what the cases have in common |

That last row is a real technique and it catches people out. When five different
inputs give one identical output, stop looking at what differs between them and
look at what they share.

---

## Worked example 1: three tools, in the order you reach for them

You have three ways to see inside this system, and they answer different
questions. Reach for them in this order.

**1. `health`. Is the service up, and can it see a model.**

```
  service          contract-demo-service
  model_endpoint   http://127.0.0.1:11535
  model_reachable  false
  timeout_seconds  5.0
  retries          0
```

Thirty seconds of work that tells you which half of the system to stop looking
at. `model_reachable` false means every answer will be a fallback, and that is a
different problem from the service being down.

**2. `contract_probe.py`. What is actually in the envelope.**

Your own program probably does not print `error.kind`. The probe always does.

```
  source       fallback
  elapsed_ms   28
  error kind:    task_validation_failed
  error message: there was no line in the answer that could be a headline
  verdict        the service built the answer without the model (task_validation_failed)
```

**3. The service's own console.** Every request it answered, with the status.
This is where you find out that your client never reached it at all.

---

## Worked example 2: three faults with the same symptom

Two students report the same thing: "It is fast, and every headline is the
first line of the request copied out."

Same sentence. Two different causes. This is scenario 2 and scenario 4 in the
Week 14 lab, and they are the same on purpose.

**Method: spot the differences**, against scenario 0, the healthy baseline.

`health` on both:

```
  model_reachable  true          <- both
```

So the model is there in both cases. That rules out the whole first branch and
takes about twenty seconds.

Now the probe. Fault B:

```
  error kind:    task_validation_failed
```

Fault D:

```
  error kind:    model_http_error
```

**One field apart.** And the two fixes are nothing like each other.

`task_validation_failed` means the model is answering and the answers do not fit
the task shape. Nobody needs to restart anything. Somebody needs to look at the
prompt template or at the validation rule, and that is a conversation, not a
command.

`model_http_error` means the model server is returning an error status. The
model server needs attention, and the service is behaving perfectly.

**A symptom does not identify a fault.** Two faults can produce the same
sentence from the person who reported it, and the only thing that separates them
is a field your own program was not printing.

### And sometimes the field is the same too

There is a third fault in today's lab that reports the same sentence again, and
this one has the same `error.kind` as one of the other two. Both say
`model_http_error`. The only thing that separates them is the number inside the
message.

```
Fault D   error message: the model server answered with HTTP 500
Fault E   error message: the model server answered with HTTP 404
```

A model server answers `POST /api/generate`, because that is the one path it
exists to have. A 404 on that path means whatever is listening there is not a
model server. Something else is on that port, answering politely, and every
reply looks plausible.

**This happened for real while these materials were being built.** A fixture
server failed to bind because another program on the machine already held port
11434, so the fixture exited, and the service spent an hour talking to the other
program. Nothing reported an error. That is why every stub in this module takes
a `--port`, why every command in every handout passes one, and why the first
thing you do after starting a server is read the line it prints.

---

## Worked example 3: a log entry that is worth reading

This is the form your entries take, and it is what gets graded. Every part below
is required.

> ## Entry 1 · Every fixture mode produced the same wrong answer
>
> ### Symptom
> The service was run against its fixture model server in five modes: fenced
> JSON, bare JSON, prose, refusal, and HTTP 500. Every mode came back
> `source` model, kind `plan_validation_failed`, with the fallback. Even the
> mode that returns perfectly shaped fenced JSON. Even the mode that returns
> HTTP 500, which could not possibly produce a validation failure.
>
> ### Methodology
> **Spot the differences.** Five inputs that should have produced at least
> three different outputs produced one, so the suspect is what they share, not
> what differs. What all five shared was the port.
>
> The first theory was that the parser was broken. Tested by calling
> `parse_plan` directly on the fixture's text, outside any server. It returned
> a correct plan. Theory dead in thirty seconds.
>
> The second theory was that the service was not talking to the fixture at
> all. Tested with `netstat -ano | findstr ":11434"`, which showed another
> process already listening there. The fixture had failed to bind and exited.
>
> ### What you changed
> One change. The fixture's default port moved from 11434 to 11435, and the
> service was pointed at 11435. Nothing about the parser was touched, because
> nothing about the parser was wrong.
>
> ### How you verified
> Re-ran all five modes on the new port. Fenced JSON gave `source` model with
> no error. Bare JSON and prose gave `plan_validation_failed`, which is the
> planted defect and correct for that program. HTTP 500 gave
> `model_http_error`. Nothing running gave `unreachable`. Five inputs, four
> different outputs.

**What makes that entry worth reading.** It names the method. It records a
theory that was wrong and how it died, which is the part people leave out and
the part that saves the next reader an hour. It changed exactly one thing. And
the verification is a command somebody else can run.

---

## The wrong version, and what it produces

Here is a log entry from a real submission shape, and every line of it is why
this document is graded.

> ### Entry 1
> **Symptom.** Nothing came back.
> **Methodology.** We tried a few things until it worked.
> **What you changed.** We changed the port and restarted everything, and we
> also updated the timeout and cleaned the build folders at the same time, and
> after that the results started coming back.
> **How you verified.** It worked.

Four problems, and they are worth naming separately.

**"Nothing came back" is not a symptom.** It is the absence of one. A symptom is
what you saw: the exact message, the exit code, how long it took, what `health`
said.

**"We tried a few things" is not a methodology.** No named method, so nobody
including the writer can say what was ruled out.

**Four changes at once.** Something fixed it and nobody knows which. Next week
the same problem comes back and the log is worth nothing, because it does not
say which of the four mattered.

**"It worked" is not verification.** Verification is a command and its output,
run by somebody who was not there.

---

## Why the wrong version is tempting

Because by the time it is working, you are relieved and you want to move on.

The log is written after the problem is solved, which is the moment you care
least about it. The version you write in ninety seconds is the version above.
The one that is worth something takes ten minutes and you write it for somebody
who is not in the room, possibly yourself in March.

**The habit that prevents it:** open the log **before** you start fixing, and
write the symptom down while you are still looking at it. Then write each theory
as you form it. The entry is then almost finished when the bug is, and the parts
people forget, the theory that was wrong and the exact command, are the parts
you wrote first.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Symptom** | exactly what you saw, with the message, the timing, and the exit code |
| **Theory** | one statement about the cause that a test could prove wrong |
| **Methodology** | a named way of choosing where to look. Four of them here. |
| **Top down** | start at the person's layer and work down |
| **Bottom up** | start at the machine's layer and work up |
| **Follow the path** | trace one request across every boundary it crosses |
| **Spot the differences** | compare a working case with a failing one, or compare failing cases with each other |
| **Reproduction** | the smallest set of steps that makes the problem happen every time |
| **Verification** | proving the fix worked, with a command somebody else can run |
| **Baseline** | a known-good run you keep so you have something to compare against |

---

## Self-check

**Question 1.** Every answer says `FALLBACK` and `health` reports
`model_reachable` true. Name the method you would use, the field you would look
at next, and two error kinds that would send you in completely different
directions.

**Question 2.** You change four things and the problem goes away. Say what you
have actually learned, and what you should do next.

**Question 3.** Your program's output and the service's console disagree about
how many requests were made. Which methodology fits, and what is the first thing
you would check?

---

### Answers

**1.** Spot the differences, against a run you know works, or top down if you
have no baseline. The field is `error.kind` in the envelope, which your own
program probably is not printing, so use `contract_probe.py`. Two kinds that
point in different directions: `task_validation_failed` means the model is
answering and the answers do not fit the task, so look at the prompt template or
the validation rule; `model_http_error` means the model server is returning an
error status, so the model server needs attention and your code is fine.

**2.** Almost nothing. You know the problem is gone and you do not know why, so
you cannot prevent it, cannot explain it, and cannot recognise it next time.
What to do next: undo the three changes you believe were unrelated, one at a
time, and confirm the problem stays fixed. If it comes back, you have found the
real one. That takes ten minutes and turns a lucky escape into knowledge.

**3.** Follow the path. Take one request and walk it across every boundary,
writing down what you see at each. The first thing to check is the address your
program is actually using, printed by the program itself at startup, against the
address the service says it is listening on. A request that never arrives cannot
be counted, and pointing at the wrong port is the most common cause in this lab.
