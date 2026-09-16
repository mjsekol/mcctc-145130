# Output Your Program Can Parse
## 145130 Applications of AI · Module 2 · Week 4, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W04_ParseableOutput.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W04_ParseableOutput.pptx)

**Competencies:** 2.14.3 (write and revise a prompt to generate the desired
response), 1.1.7 (apply problem-solving and critical-thinking skills). Supporting:
2.14.4 (evaluate an AI result).

---

## Why this exists

Everything this week has been about a human reading the reply. Today the reader
is a program.

That changes the requirements completely. A human can cope with a friendly
sentence before the list. A parser cannot. A human reading "about 6 items" knows
what to do. `int("about 6")` does not.

You have written programs that consume APIs. An API has a contract: you know the
shape before you call it. **A model has no contract.** It will hand you something
shaped roughly like what you asked for, most of the time, and your program has to
survive the rest of the time.

---

## The concept in plain language

Three rules, in order of how often they are skipped.

**1. Ask for the shape, and say "only."**
"Return JSON" is an invitation. "Return only JSON, no other text" is an
instruction. The difference is four words and it is the difference between a
program that works and one that crashes on Tuesday.

**2. Validate before you trust.**
Parsing succeeding does not mean the data is what you asked for. A reply can be
valid JSON with the wrong keys, the right keys with the wrong types, or the right
types with nonsense inside. Check the keys you need, check the types, then use
it.

**3. Decide what happens when it is wrong, before it is wrong.**
The model will eventually return something unusable. That is not an exception
case, it is a normal Tuesday. Your program needs a plan: a default, a retry with
a stricter prompt, or a clean refusal that tells the user what happened. Silence
is not a plan.

---

## Worked example 1 · The four words that matter

```
python ask.py --prompt-file demo-prompts/loose_json.txt --label loose --show
```

The prompt file contains:

```
Explain the Friday equipment checkout. Return JSON with keys subject, steps.
```

```
[loose] 11 prompt words to http://127.0.0.1:11434
  120 reply words in 0.03s, recorded in runs\loose.json
------------------------------------------------------------
Here are some thoughts on the Friday equipment checkout.

{
  "subject": "the Friday equipment checkout",
  "steps": [
    "Open the checkout sheet before anyone lines up",
    "Set the return slot to the next school day, first period",
    "Put anything with a missing part on the repair shelf instead",
    "Match the serial number on the case to the number on the sheet",
    "Write the borrower's grade level, not their schedule",
    "Photograph any damage before the item leaves the room"
  ]
}

It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule. Ultimately, the right approach
depends on your specific needs and goals. Studies have shown that small changes
can produce meaningful improvements.
------------------------------------------------------------
```

Look at that and decide: is it JSON?

Now hand it to a parser:

```
python -c "import json; r=json.load(open('runs/loose.json',encoding='utf-8')); json.loads(r['response'])"
```

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Line 1, column 1.** The parser did not get as far as your JSON. It read `H`
from "Here are some thoughts," which is not how a JSON document starts, and
stopped.

Now the strict version:

```
python ask.py --prompt-file demo-prompts/strict_json.txt --label strict
python -c "import json; r=json.load(open('runs/strict.json',encoding='utf-8')); d=json.loads(r['response']); print('parsed OK, keys:', sorted(d))"
```

```
parsed OK, keys: ['steps', 'subject']
```

The prompt file differs by four words: `only` and `no other text`.

---

## Worked example 2 · Parsing is not validating

Here is a reply that parses perfectly and is still useless:

```python
import json

reply = '{"subject": "checkout", "steps": "I will list them shortly", "count": "about six"}'
data = json.loads(reply)          # succeeds
print(type(data["steps"]).__name__)
print(data["count"] + 1)
```

```
str
TypeError: can only concatenate str (not "int") to str
```

`steps` was supposed to be a list and is a string. `count` was supposed to be a
number and is the words "about six". The JSON is valid. The data is wrong.

**The check your program needs, written out:**

```python
def usable(data):
    """Return an error message, or None if the reply can be used."""
    if not isinstance(data, dict):
        return "the reply is not an object"
    if not isinstance(data.get("subject"), str) or not data["subject"].strip():
        return "subject is missing or empty"
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        return "steps is missing or is not a non-empty list"
    if not all(isinstance(s, str) and s.strip() for s in steps):
        return "at least one step is not text"
    return None
```

```python
print(usable(json.loads('{"subject": "checkout", "steps": "soon"}')))
print(usable(json.loads('{"subject": "checkout", "steps": ["open the sheet"]}')))
```

```
steps is missing or is not a non-empty list
None
```

**Notice what `usable` does not do.** It says nothing about whether the steps are
correct, safe, in the right order, or about your school. It checks shape. Shape
is all a program can check. Everything else is Week 5.

---

## Worked example 3 · Every way a reply can be unusable

`ask.py` already tells these apart, and you should cause each one on purpose
before you build anything that depends on a model. In a second terminal:

```
python stub_model_server.py --mode malformed
python ask.py --prompt "anything" --label x
```

```
FAILED (the server answered with something that is not valid JSON)
  {"model": "stub", "response": "The checkout sheet is
```

Run through the rest and watch the exit codes change:

| Mode | What `ask.py` reports | Exit code |
|---|---|---|
| `error` | the server answered HTTP 500 | 3 |
| `malformed` | not valid JSON | 4 |
| `missing_response` | the reply has no 'response' field | 5 |
| `not_done` | the reply is not marked done | 5 |
| `empty_response` | the reply is empty | 5 |
| `rate_limited` | waits for Retry-After, retries 3 times, then HTTP 429 | 3 |
| `slow --delay 30` | no answer inside 20 seconds | 6 |
| (nothing running) | nothing is listening at the endpoint | 2 |

**Three of those return HTTP 200.** `not_done`, `missing_response`, and
`empty_response` all look like success at the network layer. A program that only
checks the status code treats all three as a working reply.

---

## The wrong version, and why it is tempting

This is the code that gets written, and it is wrong in four separate places:

```python
import json
import urllib.request

def get_steps(prompt):
    body = json.dumps({"model": "local", "prompt": prompt}).encode()
    reply = urllib.request.urlopen("http://127.0.0.1:11434/api/generate", body)
    text = json.loads(reply.read())["response"]
    return json.loads(text)["steps"]
```

1. **No timeout.** A slow model hangs your program with no message.
2. **No failure handling.** An HTTP 500 raises out of the function with a
   traceback the user cannot act on.
3. **No validation.** `["steps"]` raises `KeyError` on a reply that parsed fine.
4. **No plan for unusable output.** There is no answer to "what does this return
   when the model is having a bad day."

**Why it is tempting.** It works the first fifty times. You are developing
against a model that is running, on a machine that is not busy, with prompts you
already know work. Every one of those four holes is invisible until the day it is
not.

**This is the shape of Gate 2 tomorrow.** The program you review will look better
than this one and will still have a defect in each of these areas.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Structured output** | Output in a shape a program can read: JSON, CSV, a fixed template |
| **Parse** | Turn text into a data structure |
| **Validate** | Check that the parsed data has the keys, types, and values you need |
| **Schema** | The shape you expect: which keys, which types, which are required |
| **Fallback** | What your program does when the reply is unusable |
| **Contract** | A guarantee about the shape of a response. An API has one. A model does not |

---

## Self-check

**1.** Your program gets HTTP 200 and `json.loads` succeeds on the body. Name
three ways the reply can still be unusable.

<details><summary>Answer</summary>

Any three of: `done` is false, so the reply is partial rather than short; there is
no `response` key at all; `response` is an empty string or only whitespace; the
`response` text is not the JSON you asked for; the JSON inside has the wrong keys;
the keys are right and the types are wrong.

The first three are the ones `ask.py` gives exit code 5 for, and they are the ones
people miss, because status 200 reads as success.
</details>

**2.** Why does "Return only JSON, no other text" work better than "Return JSON,"
given that the model is not obeying you in any real sense?

<details><summary>Answer</summary>

Because it narrows the text that is a plausible continuation. Text that follows
"return JSON with keys" often has a friendly sentence in front of it, because
that is how such answers are usually written. Text that follows "only JSON, no
other text" much less often does.

You are shifting a probability, not issuing a command. **Which is exactly why your
program still has to check.** A shifted probability is not a guarantee, and Week 5
is full of cases where it did not hold.
</details>

**3.** A classmate's program handles a failed model call by returning an empty
list, silently. What is the argument for that, and what is the argument against?
Which would you ship, and why?

<details><summary>Answer</summary>

**For:** the program never crashes, the caller has one type to handle, and a user
in the middle of something is not shown a stack trace.

**Against:** an empty list is indistinguishable from "the model answered and there
genuinely were no steps." The failure disappears. Nothing gets logged, nobody
finds out, and the bug is invisible until somebody notices the feature quietly
does nothing.

**A defensible answer either way, and the reasoning is what is scored.** The
common professional choice is to return the empty result *and* record what
happened, so the user is not interrupted and the failure is still countable.
"Never crash" and "never hide" are both real values, and the way to hold both is
to separate what the user sees from what the log records.
</details>
