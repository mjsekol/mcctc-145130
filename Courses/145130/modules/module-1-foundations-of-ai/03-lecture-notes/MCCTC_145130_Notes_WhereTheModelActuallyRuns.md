# Lecture Notes: Where the Model Actually Runs
## 145130 Applications of AI · Module 1 · Week 1, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W01_WhereTheModelRuns.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W01_WhereTheModelRuns.pptx)

If you missed class you can learn this from this file alone. You need the files
in `../05-labs/local-model-kit/`.

**Competency 2.4.2:** describe the fundamental architectures of emerging
technologies and how they integrate into the existing systems of information
technology.

---

## Why this exists

Every AI product you have used hides the same thing behind one text box: a
program somewhere sends an HTTP request to a model server and gets text back.
Today you start the model server yourself, send the request yourself, and read
what actually comes out.

There is a second reason, and it shapes the whole course. **No account, no key,
no data leaving the building.** Commercial AI developer services require their
users to be 18 or older, so this course does not use them. Everything runs on a
machine in this room.

---

## The concept in plain language

Two programs, one HTTP call between them.

```
your program
     |  POST /api/generate
     |  {"model": "llama3.2", "prompt": "...", "stream": false}
     v
a model server, or a stand-in for one
     |
     v  {"model": "...", "response": "...", "done": true}
```

That is the whole architecture today. Three fields come back, and **the entire
answer is a string sitting in `response`.**

### The fact the rest of the module hangs off

**The model returns text, not data.**

It does not return a label. It does not return a number. It returns a string,
and whether that string contains something your program can use is a question
your program has to ask and answer. Sometimes the string is JSON. Sometimes it is
JSON wrapped in a code fence. Sometimes it is a sentence. Sometimes it is a
polite refusal that is perfectly well-formed and completely useless.

Everything you build from here is downstream of that one fact.

### What a bigger system does about it

A real product does not scatter that work across every program that wants an
answer. It puts one small **service** in the middle: the application asks the
service, the service talks to the model, handles the mess once, and hands back
the same shape every time.

**You build that service in Module 5.** It is the performance task. It is not in
your kit today, and that is deliberate: **you are supposed to feel the problem
before you are handed the solution.** By Friday of Week 2 you will have written
the same parsing and the same failure handling twice, in two different programs,
and the argument for a shared layer will make itself.

---

## Worked example 1: one request, end to end

Start the stand-in on this module's port, in one terminal:

```
python stub_model_server.py --port 11634
```

Then, in another, `python one_request.py`. Captured on the build machine:

```
HTTP 200
{"model": "llama3.2", "created_at": "...", "response": "```json\n{\n  \"summary\":
\"Stub summary: the wifi keeps dropping\",\n  \"bullets\": [\n    \"the wifi keeps
dropping\"\n  ]\n}\n```", "done": true}
```

Read it twice. **The JSON you care about is inside a string, inside a code fence,
inside the JSON of the reply.** Getting a label out of that means stripping a
fence and parsing again, and your program has to survive the day the fence is not
there.

---

## Worked example 2: a request the server refuses

`one_request.py` sends a second request asking for streaming. Captured:

```
HTTP 400
{"error": "this stub only supports stream: false"}
```

Two things to take from this.

**The failure arrived as an HTTP status with a body that says why.** That is the
good case. Your program gets a number it can branch on and a sentence it can show
somebody.

**Not every server does what you assume.** This one does not stream. The one in
Lab M01-04 does. Assuming a capability and finding out at the seam is the most
ordinary integration failure there is.

---

## Worked example 3: the same answer, three different ways

Put the stand-in in different modes and send the same request. Real output from
the Week 2 lab, shortened:

| mode | what `response` contains |
|---|---|
| `success` | ```` ```json\n{"label": "network", ...}\n``` ```` |
| `success_prose` | `Label: network\nWhy: Stub match on the words ...` |
| `unusable` | `I am not able to help with that request.` |

**All three are HTTP 200 with `done: true`.** At the level of the request, all
three succeeded. Only the third one is useless, and nothing about the reply says
so. Your program finds out by trying to read a label and failing.

That is why `ask_model.py` in Lab M01-01 records **how** it got each label:

```
  MT-2002  network   read from json
```

`json`, `prose`, `off_list`, or `unparsed`. **Nothing gives you that for free.**
If your program does not record how it got a value, then three weeks later nobody
can tell a label the model produced from a fragment of text your code sliced out
of a sentence.

---

## The wrong version, and the exact damage it does

```python
answer = json.loads(response)["response"]
label = json.loads(answer)["label"]
print(label)
```

Two lines, and it works on a good day.

**It crashes on the fence.** The answer starts with ```` ```json ````, so the
second `json.loads` raises immediately.

**Patch that and it crashes on prose.** Put the server in `success_prose` and
there is no JSON at all.

**Patch that with a bare `except` and it gets worse**, because now an unusable
answer silently becomes whatever your fallback produces, and it prints in the
same column as a real label.

Here is that last failure, real, from the flawed program in this week's Gate 2,
run against a server answering in prose:

```
  label:   Label: hardware
Why:
```

**That is not a label. It is a slice of raw text.** It sits in the label column
looking like a label, and the program that produced it had a comment above the
parse claiming the model always answers with JSON.

### Write this down

> The request succeeding and the answer being usable are two different
> questions. Ask both, and record which one you are answering.

---

## Why the wrong version is tempting

Because it works the first time you run it. The happy path is genuinely two
lines, and every failure mode above needs the server to misbehave before you can
see it. **You will not discover any of them by testing the thing that works**,
which is why the stand-in has ten modes and why Lab M01-02 makes you use them.

---

## Vocabulary

| Term | What it means |
|---|---|
| **model endpoint** | the address a model server answers requests at |
| **`/api/generate`** | the path this course posts a prompt to |
| **`response`** | the field the model's whole answer arrives in, as text |
| **`done`** | the field saying the answer is finished rather than cut off |
| **code fence** | the triple-backtick wrapper a model often puts around JSON |
| **parse** | turning text into something a program can use |
| **provenance** | where a value came from, and how you got it |
| **service layer** | a program between an application and a model that handles the mess once. **Module 5** |
| **loopback** | the `127.0.0.1` address, meaning this machine only |

---

## Self-check

**1.** A request comes back HTTP 200 with `done: true`, and the `response` field
says "I am not able to help with that request." Did the request succeed? Answer
it, then say why the question is badly formed.

**2.** Your program prints a label for every ticket and never errors. Name two
things that could still be wrong with those labels.

**3.** Give one reason a real product puts a service between its application and
its model, in your own words.

### Answers

**1.** Yes, at the level of the request: it reached the server, the server
answered, and the answer is complete. The question is badly formed because
"succeed" is hiding two questions, and they come apart constantly: did I get a
reply, and is the reply usable. A program that collapses them will eventually
show a refusal, or a fragment of one, as though it were an answer.

**2.** Any two of: the label was sliced out of text that was never parsed; the
label is a category the model invented rather than one of the five allowed; the
answer came from a stand-in rather than a model and nobody recorded that; the
program fell back to a default when parsing failed and did not say so.

**3.** Any of: the messy parsing lives in one place instead of in every program;
the timeout and retry policy live in one place; the application can be changed
without touching model code, and the other way round; every caller gets the same
shape back so there is one thing to write tests against. You build it in Module 5.
