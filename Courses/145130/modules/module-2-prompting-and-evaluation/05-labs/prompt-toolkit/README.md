# The Prompt Toolkit
## 145130 Applications of AI · Module 2 · Weeks 4-6

Three small programs you will use in every lab in this module, plus a stand-in
model server so the labs run on a machine with no model installed.

**Read this before Week 4, Monday.** It takes ten minutes and it saves you from
the two failures that cost the most class time: a comparison built from memory,
and a lab that cannot start because nothing is listening on the port.

---

## Why these exist

You are about to compare five prompts. You will not remember them. You will
remember the reply you liked, and you will quietly forget the two replies that
were almost identical, which is the finding you actually needed.

`ask.py` writes every run to a file. `compare_runs.py` counts what is different
between those files. You supply the judgement. That order matters, because a
judgement made after looking at the counts is a different thing from a
judgement made from an impression.

---

## The four files

| File | What it does |
|---|---|
| `ask.py` | Sends one prompt to a local model and records the run |
| `compare_runs.py` | Reads recorded runs and prints a table of what differs |
| `stub_model_server.py` | A stand-in model, so every lab runs with nothing installed |
| `test_toolkit.py` | The test suite that proves all of the above still works |

---

## The rule that never moves

**Every model in this course runs on a machine in this building.** The default
endpoint is `http://127.0.0.1:11434`, which is your own computer. Commercial
developer APIs require the account holder to be 18 or older, so this course
does not use one, and no lab will ever ask you for a key.

**No personal data goes into a prompt file.** Not a name, not a student ID, not
a grade, not a schedule. `ask.py` records your prompt verbatim into a file you
commit, so whatever you type is what gets published to your repository. Use
invented names. The course uses Ava Ruiz and Kai Mendoza for this.

---

## Starting the stub

Open a second terminal and leave it running:

```
python stub_model_server.py
```

```
Stub model server on http://127.0.0.1:11434 in success mode. Press Ctrl+C to stop.
Every source this server produces is invented. None of them are real.
```

Then, in your first terminal:

```
python ask.py --prompt "Give me 4 steps for the Friday equipment checkout." --label test --show
```

```
[test] 9 prompt words to http://127.0.0.1:11434
  51 reply words in 0.03s, recorded in runs\test.json
------------------------------------------------------------
Here are some thoughts on the Friday equipment checkout.

1. Open the checkout sheet before anyone lines up.
2. Match the serial number on the case to the number on the sheet.
3. Write the borrower's grade level, not their schedule.
4. Photograph any damage before the item leaves the room.
------------------------------------------------------------
```

If you see `FAILED (nothing is listening at http://127.0.0.1:11434)`, the stub
is not running, or it is running in the other terminal on a different port.

---

## What the stub is, and what it is not

**The stub is not a language model.** It is a caricature of one. It reads your
prompt with regular expressions, notices which of the five prompt elements you
included, and builds a reply from templates. The same prompt always gives the
same reply.

That is a feature for learning and a limit for everything else:

| What the stub teaches honestly | What only a real model can tell you |
|---|---|
| Which element changed the shape of the reply | Whether the wording is any good |
| That an unconstrained prompt gets padding | How much padding a real model adds |
| That asking for sources with none supplied invents sources | How convincing the invented ones are |
| That "return JSON" and "return only JSON" differ | Whether your model obeys either |
| How your program behaves when the model fails | How often a real model fails |

Every lab in this module says which of its findings hold against the stub and
which have to be confirmed against the lab's local model. Read that line.

**Every source the stub produces is fabricated.** The authors, journals,
volumes, and page numbers are built from templates. None of them exist. That is
on purpose: a fabricated citation you can study safely beats one you went
hunting for.

---

## The failure modes, and why you should cause them

A program that only works when the model works is not finished. Start the stub
in each of these modes and watch `ask.py` tell them apart:

```
python stub_model_server.py --mode error            HTTP 500
python stub_model_server.py --mode malformed        200, but the body is broken JSON
python stub_model_server.py --mode rate_limited     429 with Retry-After
python stub_model_server.py --mode not_done         valid JSON, done is false
python stub_model_server.py --mode missing_response valid JSON, no response field
python stub_model_server.py --mode empty_response   a reply of nothing but spaces
python stub_model_server.py --mode slow --delay 30  answers after you gave up
```

`ask.py` exits with a different code for each:

| Code | Meaning |
|---|---|
| 0 | the reply is usable |
| 2 | nothing is listening at the endpoint |
| 3 | the server answered with an HTTP error |
| 4 | the reply is not valid JSON |
| 5 | the reply parsed but is not usable (empty, not done, no response field) |
| 6 | no answer inside the timeout |

**The three that catch people out are 4, 5, and 6.** A reply that arrives, has
status 200, and is unusable does not look like a failure until you check. Codes
4 and 5 exist so that it does.

You can also flip the mode without restarting:

```
python -c "import urllib.request,json; urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:11434/stub/mode', data=json.dumps({'mode':'error'}).encode(), headers={'Content-Type':'application/json'}))"
```

---

## Seeing what the stub read in your prompt

```
python -c "import urllib.request,urllib.parse,json; q=urllib.parse.urlencode({'prompt':'You are a librarian. Give me 3 steps in a numbered list, under 40 words.'}); print(urllib.request.urlopen('http://127.0.0.1:11434/stub/parse?'+q).read().decode())"
```

```
{"role": "librarian", "audience": null, "format": "numbered", "json_only": false,
 "json_keys": [], "word_cap": 40, "step_count": 3, "has_example": false,
 "no_intro": false, "wants_sources": false, "grounded": false,
 "provided_sources": [], "allows_refusal": false, "topic": "default",
 "prompt_words": 15}
```

That endpoint does not exist on a real server. It is here so you can check that
the element you thought you added is the element the machine saw. When a
revision changes nothing, this is the first thing to check.

---

## Comparing runs

```
python ask.py --prompt-file prompts/v1.txt --label v1
python ask.py --prompt-file prompts/v2.txt --label v2
python compare_runs.py runs
```

```
| Label | Prompt words | Reply words | Seconds | Shape | Valid JSON | List items | Sources claimed | Hedges |
|---|---|---|---|---|---|---|---|---|
| v1 | 6 | 110 | 0.02 | prose | no | 0 | 0 | 5 |
| v2 | 69 | 54 | 0.00 | numbered | no | 5 | 0 | 0 |
```

Read the last two columns carefully.

- **Hedges** counts phrases like "it is worth noting" and "ultimately, it
  depends on your specific needs." Padding is what a model produces when the
  prompt did not tell it what finished looks like.
- **Sources claimed** is a count of citation-shaped lines. It is not a check.
  Nothing in this toolkit has ever confirmed that a source exists, and Week 5 is
  about the fact that nothing automatic can.

---

## Running the tests

```
python test_toolkit.py
```

Expect `Ran 29 tests` and `OK`, in about 18 seconds. Most of that is one test
that deliberately waits for a slow server to miss its deadline.

If a test fails after you changed something, read which one. The names say what
broke.

---

## If it breaks

**`FAILED (nothing is listening at http://127.0.0.1:11434)`**
The stub is not running. Start it in a second terminal. On Windows, closing the
terminal tab is what stops it, not Ctrl+C in the wrong window.

**`OSError: [WinError 10048]` when starting the stub**
Something is already on port 11434, usually a stub you forgot. Use
`--port 11500` and pass the same port to `ask.py` with `--endpoint`.

**`FAILED (the server answered with something that is not valid JSON)`**
Either the stub is in `malformed` mode, or you pointed `--endpoint` at
something that is not a model server. Check the port.

**`FAILED (no answer inside 20 seconds)`**
On a real local model, this can be genuine. Raise it with `--timeout 60` and
say in your log that you did. On the stub it means `--mode slow`.

**Your prompt file has a character the console will not print.**
The default console encoding on Windows is cp1252. Set
`PYTHONIOENCODING=utf-8` before running, and keep prompt files to plain ASCII.

---

## Where these files are used

| Used by | Where |
|---|---|
| Lab M02-01 Element Sweep | `../MCCTC_145130_Lab_M02-01_ElementSweep.md` |
| Lab M02-02 Hallucination Hunt | `../MCCTC_145130_Lab_M02-02_HallucinationHunt.md` |
| Prompt Autopsy performance task | `../../09-project/MCCTC_145130_Project_M02_PromptAutopsy.md` |
| Gate 2 Week 4 | `../../07-gate2-adversarial/MCCTC_145130_Gate2_W04.md` |
| SQ-18 Prompt Ablation | `../../../../../Misc/side-quests/SQ-18-Prompt-Ablation/` |

SQ-18 ships its own copy of `stub_model_server.py` so the side quest bundle
works on its own. The two copies are the same file.
