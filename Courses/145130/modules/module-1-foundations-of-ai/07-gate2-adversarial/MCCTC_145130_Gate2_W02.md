# Gate 2: Adversarial Review · Week 2
## 145130 Applications of AI · Module 1 · Week 2, Friday

**40 minutes**, Friday Build 1, after that day's Gate 1 rep. Individual. You
may and should run the code. **You may not ask a model whether it is correct**,
because a model is what produced it.

The program is `gate2-w02-files/triage_client.py`, with `tickets.json` in the
same folder. Copy both. You need the stand-in in `../05-labs/local-model-kit/`.

---

## What you are looking at

Somebody handed an assistant the requirements in Part A and got
`triage_client.py`. It runs. It produces a triage board that looks right.

**Five defects, one in each category:** Correctness, Security, Readability,
Performance, Requirements Fit.

**There is also one design choice in this program that is genuinely arguable.**
It is not one of the five. Find it, take a side, and give the other side its
strongest form. You are not graded on which side you take.

**Two of the five will not show themselves on the happy path.** One shows up in
the folder after the program has run. One shows up only when the model answers
with something other than JSON.

---

## PART A: The requirements

> Write `triage_client.py` that reads help requests from a JSON file, asks the
> local model to label each one, and prints a triage board for the makerspace
> staff. It must:
>
> 1. Print a label for **every** ticket in the file.
> 2. Print **the model's raw answer** next to each label, so staff can see what it
>    actually said.
> 3. Say plainly when the program **could not read a label** out of the answer.
> 4. Send **exactly one request per ticket**.
> 5. **Never write a prompt or an answer to disk.**
> 6. Exit with a non-zero code if the model server cannot be reached, with a
>    message naming the command that starts it.

---

## PART B: Running it

Start the stand-in from `local-model-kit/`:

```
python stub_model_server.py --port 11634
```

Then, from the folder with the program:

```
$env:RIDGE_MODEL_URL = "http://127.0.0.1:11634"
python triage_client.py tickets.json
```

**Count the ticket blocks.** Then count the file:

```
python -c "import json; print(len(json.load(open('tickets.json'))['tickets']), 'tickets in the file')"
```

**Then check how many times the model was actually asked:**

```
python -c "import urllib.request as u; o=u.build_opener(u.ProxyHandler({})); print(o.open('http://127.0.0.1:11634/stub/stats').read().decode())"
```

**Then run it again with the model answering in prose instead of JSON:**

```
python -c "import json,urllib.request as u; o=u.build_opener(u.ProxyHandler({})); o.open(u.Request('http://127.0.0.1:11634/stub/mode', json.dumps({'mode':'success_prose'}).encode(), {'Content-Type':'application/json'}))"
python triage_client.py tickets.json
```

**Read the label column carefully on that run.**

**Then look at the folder.**

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real
person**, and **the fix**.

Then two more entries:

**The arguable one.** Name the design choice. Say what is wrong with it, say what
is right about it, and say what you would do. Both sides have to be real.

**What I was unsure about.** One specific thing. A blank costs more than a wrong
guess.

### How to spend 40 minutes

- **First 10:** run it. Count the blocks against the file, and check the call
  count.
- **Next 8:** run it in prose mode and read the label column. Then look at the
  folder.
- **Next 14:** read Part A one requirement at a time and point at the line that
  meets it. Two of them are not met.
- **Rest:** read each comment against the code under it. Ask whether it is
  telling the truth.

---

## Scoring

**8 points.**

| Item | Points |
|---|---|
| Five defects, one point each, with line, consequence, and fix | 5 |
| The arguable design choice, both sides real | 2 |
| What I was unsure about, naming something specific | 1 |

**A finding scores only with the line, the consequence, and the fix.**

### The security penalty

**Missing the security defect costs 2 points, not 1.** Your instructor states
this before you start. Four of five is a strong score.
