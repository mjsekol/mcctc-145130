# The local model kit
## 145130 Applications of AI · Module 1

Two files. A stand-in model server, and the smallest program that talks to it.

`stub_model_server.py` is a **verbatim copy** of the course's canonical stand-in,
from `Courses/145130/anchor-project/ai-stack/`. It lives here so every Module 1
lab runs from your own repository with nothing else installed. **The anchor
project is authoritative.** If this copy and the anchor ever disagree, the anchor
is right.

**There are no credentials in this folder and there never will be.** A local
model needs no account and no key, and no prompt leaves the building.

---

## What you are talking to, and what you are not

In this module **your program talks to the model server directly**. One HTTP
request out, one HTTP reply back, and everything after that is your code making
sense of text.

```
your program  ->  POST /api/generate  ->  a model server, or this stand-in
              <-  {"model", "response", "done"}
```

**The answer arrives as text, inside one field.** Not a label, not a number, not
a shape you can rely on. Turning that text into something a program can use is
your job in this module, and you will find out exactly how much work it is.

**In Module 5 you build the layer that does it in one place.** A small service
that sits between an application and a model, handles the mess once, and hands
the application the same shape every time. That service is the Module 5
performance task, which is why it is not in this folder. **You are supposed to
feel the problem first.** Feeling it is the point of Weeks 1 and 2.

---

## Ports, and why this matters more than it looks

**Module 1 uses these two ports. Always pass them explicitly.**

| What | Port |
|---|---|
| the stub model server | **11634** |
| the streaming stand-in, in `../lab-m01-04-files/` | **11635** |

**Port 11434 is reserved for a real model** and nothing in this module uses it.
That is the port an Ollama-compatible server listens on by default, and it is the
port several other modules' stand-ins would take if nobody assigned them.

**The reason is not tidiness.** Two programs cannot both hold one port, and the
second to start will either refuse to start or, worse, your program will quietly
talk to somebody else's server. **A run against the wrong server looks exactly
like a working run**, and you will not find out until the numbers make no sense.

`stub_model_server.py` is a verbatim copy, so **typing it with no arguments lands
it on 11434**, where nothing in this module is looking. The fix is the `--port`
argument.

---

## Start it, two terminals

**Terminal 1, the model stand-in:**

```
python stub_model_server.py --port 11634
```

```
Stub model server on http://127.0.0.1:11634 in success mode. Press Ctrl+C to stop.
```

**Terminal 2, your program.** Set the address once per terminal:

```
$env:RIDGE_MODEL_URL = "http://127.0.0.1:11634"
python one_request.py
```

Captured on the build machine:

```
=== a request this server will answer ===
HTTP 200
{"model": "llama3.2", "created_at": "...", "response": "```json\n{\n  \"summary\":
\"Stub summary: the wifi keeps dropping\",\n  \"bullets\": [\n    \"the wifi keeps
dropping\"\n  ]\n}\n```", "done": true}

=== a request this server refuses ===
HTTP 400
{"error": "this stub only supports stream: false"}
```

**Read the first reply twice.** Three fields, and the entire answer is a string
sitting in `response`, with a code fence around it that somebody has to strip.
**Read the second one too.** Not every server does what you assume, and the
failure arrives as an HTTP status with a body that says why.

---

## The stand-in's ten modes

Switch while it is running, or start it in the mode you want. **These exist so
you can make the model fail on purpose**, which is the only way to practise
failure handling without waiting for a real failure.

| Mode | What it sends back |
|---|---|
| `success` | the right shape for the task, as JSON inside a code fence |
| `success_prose` | the same answer as prose, with no JSON anywhere |
| `unusable` | a polite refusal that fits no task shape |
| `slow` | waits `--delay` seconds, then answers like `success` |
| `error` | HTTP 500 |
| `rate_limited` | HTTP 429 with `Retry-After: 1` |
| `malformed` | status 200 with a body that is cut off |
| `not_done` | valid JSON with `"done": false` |
| `missing_response` | valid JSON with no `"response"` field |
| `empty_response` | a response that is only spaces |

```
python stub_model_server.py --port 11634 --mode slow --delay 6
```

`GET /stub/stats` reports how many times the stand-in was asked to generate,
which is how you can see a retry from outside. `POST /stub/mode` switches mode
while it runs. **Neither endpoint exists on a real server.**

---

## It is not a model, and that matters

It matches keywords and returns fixed shapes. It does not read your prompt in any
meaningful sense, and it is perfectly repeatable, which a real model usually is
not.

That has a consequence you will meet in Week 2: **some questions about model
behaviour cannot be settled with this stand-in.** When you hit one, say so in
your write-up and say what you would need instead. Naming a question your
instrument cannot answer is a result.

---

## Settings

All optional, all environment variables, never in code.

| Variable | Module 1 value |
|---|---|
| `RIDGE_MODEL_URL` | `http://127.0.0.1:11634` |
| `RIDGE_MODEL` | `llama3.2` |

**Use `127.0.0.1`, not `localhost`.** On the machine this was built on, a refused
connection to `localhost` took about 4 seconds because Windows tries IPv6 first,
and the same refusal to `127.0.0.1` took about 2.

---

## Stop everything, and check

Ctrl+C in terminal 1. Then check nothing was left behind:

```
netstat -ano | findstr "LISTENING" | findstr "11634 11635"
```

No output means both ports are free. **If something is still listening**, the
last number on the line is the process id, and this stops it:

```
Stop-Process -Id <the number> -Force
```

**This happens more often than you would think**, because a terminal closed
without Ctrl+C leaves the server running. The symptom the next day is a stand-in
that will not start, or worse, a stand-in that starts in the wrong mode and
answers your program without you knowing. Check the ports before you blame your
code, and check them again before you leave.

Clean up the leftovers when you are finished for the day:

```
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
```

---

## If it breaks

| What you see | What it means | What to do |
|---|---|---|
| `nothing answered at http://127.0.0.1:11634` | the stand-in is not running | start terminal 1 |
| `HTTP 400 this stub only supports stream: false` | you asked for streaming | this server does not stream. Lab M01-04 has one that does |
| `Address already in use` | something from an earlier run is still up | the netstat and Stop-Process pair above |
| every answer looks unchanged after `--mode` | you switched the mode on a different server | check which port each terminal is on |
| `KeyError: 'generate_calls'` | you are pointed at something that is not this stand-in | `/stub/stats` exists only here, which is the point |
