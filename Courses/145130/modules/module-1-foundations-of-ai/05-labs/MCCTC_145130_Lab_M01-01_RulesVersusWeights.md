# Lab M01-01: Rules You Wrote Against Weights Somebody Fitted
## 145130 Applications of AI · Module 1 · Week 1, Monday and Tuesday

**Gate:** 1 for Part 1, then 3 for Part 2. **Duration:** two blocks.
Monday Build 1 and Tuesday Build 1 and 2. Each Build 1 opens with that day's
Gate 1 rep, so the lab has 40 minutes of Build 1 and 55 of Build 2.
**Competencies:** PRIMARY 2.14.1 (how machine learning and neural networks
operate differently than standard decision trees). SUPPORTING 2.4.2 (how an
emerging technology integrates with existing systems), 5.1.1 (how programs solve
problems).

**Files:** `lab-m01-01-files/`. The model stand-in is in `local-model-kit/`.

---

## The scenario

The makerspace gets more help requests than anyone can sort by hand. Somebody
proposes putting a model on it. Before that decision gets made, the staff want to
see both options side by side on the same tickets.

You are going to build one of the options yourself, run the other one, and write
down where each of them fails.

## What you will build

A decision tree that labels help requests, a comparison against a model on the
same twelve tickets, and a written report about the disagreements.

---

## What you get

| File | What it is |
|---|---|
| `tickets.json` | twelve invented help requests. Nobody named is a real person. |
| `triage_rules.py` | the starter. It runs and it answers `other` for everything. |
| `check_rules.py` | your self-check against the nine settled tickets |
| `ask_model.py` | finished. Talks to the model server. Do not change it. |
| `compare.py` | finished. Runs both and writes `comparison.csv`. |

**Three of the twelve tickets have no agreed answer.** They are marked `argue` in
the fixture. The makerspace staff could not settle them, and they are never
scored as right or wrong. What you write about those three is the part that gets
read first.

---

## Part 1, Monday Build 1, 40 minutes

The first 10 minutes of Build 1 are that day's Gate 1 rep. This part starts
after it and runs the remaining 40.

**Gate 1 rules apply here too. No AI for this part.** Plain editor. You are
writing rules, and the whole point is that a person wrote them.

### Step 1. Read the fixture

```
python -c "import json; d=json.load(open('tickets.json')); print(len(d['tickets']), 'tickets,', d['labels'])"
```

You should see `12 tickets, ['hardware', 'software', 'network', 'account', 'other']`.

### Step 2. Run the starter and watch it be useless

```
python check_rules.py
```

It reports **1 of 9**. The one it gets right is MT-2005, and it gets that one
right by accident, because the starter answers `other` for everything and
MT-2005 happens to be `other`. Write that down somewhere. A system that is right
for the wrong reason will be right until the day it matters.

### Step 3. Write the account branch

Open `triage_rules.py`. In `classify`, before the `return "other"`, add a branch
that returns `account` when the text is about getting in. Run `check_rules.py`
again. MT-2004 should pass.

### Step 4. Write the other three branches

Network, software, hardware. **The order you put them in is a decision you are
making**, and step 5 asks you to defend it.

Run `check_rules.py` after each branch. Fix one failure at a time.

### Step 5. Write down the order and why

In `report.md`, list your branches in the order the code asks them, and write one
sentence for each saying why it is where it is. If you moved one during step 4,
say which one and what broke.

### Step 6. Get to nine of nine

Keep going until `check_rules.py` reports `9 of 9 settled tickets match`.

### Step 7. Make `explain` tell the truth

Right now `explain` returns a placeholder. Make it return the branch that
actually fired, including which phrase matched. Run:

```
python triage_rules.py
```

You should see a label and a reason for the sample sentence.

**A warning about step 7 that costs people marks.** If you write `classify` and
`explain` as two separate chains of branches, they will drift apart the first
time you change one. Make them share.

### Acceptance criteria, Part 1

- [ ] `python check_rules.py` reports 9 of 9 settled tickets
- [ ] `python triage_rules.py` prints a label and a reason naming a real branch
- [ ] `report.md` lists your branch order with one sentence each
- [ ] Committed before you leave, with a message that says what you built

---

## Part 2, Tuesday, both builds

Now the other side. **Gate 3, full tooling.** You may use AI for the writing in
Part 2 as long as your `AI_USAGE.md` says what you asked for and what you
changed.

### Step 8. Start the model stand-in

**Nothing to install.** The stand-in uses the Python standard library only.

Terminal 1, from `local-model-kit/`:

```
python stub_model_server.py --port 11634
```

Terminal 2, from `lab-m01-01-files/`:

```
$env:RIDGE_MODEL_URL = "http://127.0.0.1:11634"
python ask_model.py
```

You should see the endpoint line, then twelve labels, each with the route it was
read by.

**Pass the port.** Module 1 uses 11634, and 11434 is reserved for a real model.
`local-model-kit/README.md` says why this matters more than it looks.

### Step 9. Read six of those labels against the tickets

Do not run the comparison yet. Read `ask_model.py`'s output next to the ticket
text for MT-2004, MT-2007, MT-2008, and MT-2009. Write down, in `report.md`,
what you notice before the program tells you.

Then open `ask_model.py` and read `build_prompt` and `read_label`. **Those
twenty lines are the entire difference between "the model answered" and "my
program has a label."**

### Step 10. Run the comparison

From `lab-m01-01-files/`:

```
python compare.py
```

It prints a table and writes `comparison.csv`. Real output from the build
machine, shortened:

```
  ticket    staff      your rules  model      how        agree
  --------------------------------------------------------------
  MT-2001  hardware   hardware    hardware   json       both
  MT-2004  account    account     hardware   json       rules
  MT-2007  argue      network     hardware   json       no answer
  MT-2008  software   software    hardware   json       rules

  On the nine settled tickets:
    your rules matched the staff on 9
    the model matched the staff on 7
```

Your numbers may differ if your branch order differs. That is allowed and it is
worth explaining.

### Step 11. The part that is actually the lab

In `report.md`, answer these five. Two paragraphs each at most.

1. **Pick one ticket where the two systems disagreed.** Quote the ticket. Say
   what your rules answered and why, quoting the reason your own program gave.
   Then say what the model answered, and say plainly whether you can find out
   why. Be specific about the difference between those two situations.

2. **The three `argue` tickets.** For each one, say what label you would put on
   it and what you would have to know about the makerspace to be sure. At least
   one of your three answers should conclude that the system should refuse to
   label it, and you should say what refusing would look like on a screen.

3. **Where your tree fails.** Name a help request, one you write yourself, that
   your rules would label wrongly. Run it through and paste the output. Then say
   whether you could fix it, and what your fix would break.

4. **The `how` column.** It says `json` on every row. Read `read_label` in
   `ask_model.py` and say what the other three values mean and when each would
   appear. Then say who decided that column would exist, and what your report
   would be missing without it.

5. **The uncomfortable question.** You have been calling the other column "the
   model". Read the first paragraph of `local-model-kit/README.md` under "It is
   not a model, and that matters", then say in your own words what your
   comparison does and does not establish. **This is the question worth the most
   marks on the page.**

### Acceptance criteria, full lab

- [ ] Nine of nine settled tickets, and `comparison.csv` committed
- [ ] `report.md` answers all five questions in Step 11
- [ ] Every claim about what a system did is backed by pasted output
- [ ] At least one `argue` ticket is answered with "the system should refuse"
- [ ] `AI_USAGE.md` updated if you used a model for any of the writing
- [ ] Committed and pushed

---

## If it breaks

**`ModuleNotFoundError: No module named 'triage_rules'`**
You are running `check_rules.py` from the wrong folder. Change into
`lab-m01-01-files/` first. Python looks for the module next to the script you
ran.

**`nothing answered at http://127.0.0.1:11634`**
The stand-in is not running, or it is on another port. Start it in its own
terminal from `local-model-kit/` and leave it running. If you started it without
`--port 11634` it is on 11434, where nothing here is looking.

**`OSError: [WinError 10048] Only one usage of each socket address ...`**
Something is already listening on that port, almost always a server somebody left
running in a closed terminal. Find it and stop it:

```
netstat -ano | findstr "LISTENING" | findstr "11634 11635"
Stop-Process -Id <the last number on the line> -Force
```

**Do not work around it by picking a different port.** The next person hits the
same leftover, and a program talking to a leftover server in the wrong mode
produces a run that looks completely normal.

**`the server answered HTTP 400: this stub only supports stream: false`**
Something asked for streaming. `ask_model.py` does not. Check you have not edited
it, and check which server is on that port.

**`check_rules.py` passes 8 of 9 and you cannot see why**
Read the FAIL line and then run that one sentence through `explain`. The branch
that fired will be named. It is almost always ordering rather than a missing
phrase.

---

## Stretch goal

Add a sixth possible answer to your tree: `needs more information`, returned when
the ticket is under twenty characters or contains no noun your branches know.
Then argue, in three sentences, whether adding it makes the system better or only
makes it look better.

---

## Submission checklist

- [ ] `triage_rules.py` with all four branches and a truthful `explain`
- [ ] `comparison.csv`
- [ ] `report.md` with Step 5 and all five Step 11 answers
- [ ] Pasted output for every claim about behaviour
- [ ] `AI_USAGE.md` entry if a model was used
- [ ] Pushed

---

# Extended Lab Options

All four assess 2.14.1 on the same scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty minutes in and fewer than four settled tickets passing | SCAFFOLDED |
| Working through branches, checking after each one | STANDARD |
| Nine of nine before the end of Build 1, or asks how `read_label` handles prose | EXTENDED |
| "Why would anyone use rules when models exist," or asks where this is used for real | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the account and network branches are provided complete. You write
  software and hardware.
- **Steps:** step 7 is removed. `explain` stays as it is.
- **Step 11 drops to questions 1, 2, and 5.**
- **Checkpoints:** show your instructor `check_rules.py` after each branch.

**Acceptance criteria:** nine of nine settled, `comparison.csv`, and Step 11
questions 1, 2, and 5 answered with pasted output.

**Grading:** same scale. Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need something not taught yet.

**Added requirement 1.** Run the stand-in in `success_prose` mode, where it
answers with no JSON at all, and show that `compare.py` still produces labels.
Then explain in your README which branch of `read_label` handled it and how the
`how` column changed.

**Added requirement 2.** Run it in `unusable` mode, where the answer is a polite
refusal. Explain what `read_label` does, why refusing to guess is the right
behaviour, and what a program that guessed would have printed instead.

**Hint, not the answer.** Switch modes without restarting:

```
python -c "import json,urllib.request as u; o=u.build_opener(u.ProxyHandler({})); o.open(u.Request('http://127.0.0.1:11634/stub/mode', json.dumps({'mode':'success_prose'}).encode(), {'Content-Type':'application/json'}))"
```

Then read `read_label` from the top and find the second route.

**Acceptance criteria:** all STANDARD criteria, both runs pasted into the README,
and both explanations in your own words naming real functions.

---

## APPLIED

**For the student who asks where rule systems are still used for real.** They are
everywhere: tax rules, eligibility for a program, safety interlocks, medical
triage protocols, anything where somebody has to be able to read the reason and
defend it to a person who was harmed by it.

**Changed scenario.** Instead of help requests, build the tree for **eligibility
for a school program**: invented rules, invented applicants, and the requirement
that every decision prints the rule that produced it. Write the rules from this
invented policy:

> A student may take the advanced section if they have completed the prerequisite
> course, or if an instructor has signed a waiver. A student who failed the
> prerequisite may not take it on a waiver alone. A student with fewer than 60
> attendance days in the prior year needs both the prerequisite and a waiver.

Build twelve invented applicants of your own, including at least two the policy
does not clearly cover.

**The extra requirement that makes it the same lab.** Answer Step 11 question 5
about your own system: what would be lost if a model made these decisions
instead, and who would be harmed by that loss. Name the person.

**Grading:** same scale. Requirements Fit is judged on whether every decision
prints a readable reason and whether the two uncovered applicants are handled
rather than guessed at.
