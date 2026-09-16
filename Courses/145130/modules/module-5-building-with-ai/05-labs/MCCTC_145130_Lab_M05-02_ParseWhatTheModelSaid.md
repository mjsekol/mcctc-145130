# Lab M05-02 · Parse What the Model Said
## 145130 Applications of AI · Module 5 · Week 13, Thursday

**Competencies:** 5.1.2 (algorithms and data structures in information
processing), 5.1.3 (model the solution), 5.6.6 (design inputs, outputs, and
processes)

---

## The situation

The study planner takes one sentence about what somebody has to study and hands
back a plan: a title, two to eight steps, and a number of minutes. The plan
comes from a language model running in this building, and the model answers in
prose. Somebody asked it for JSON, was specific about the shape, and got ten
different shapes back.

**What you will build:** a parser and a validator that turn any of those ten
answers into a study plan your program can rely on, or say plainly that there
was no plan in there.

**The tests are already written.** Twenty of them. Your job is to make them
pass, and you do not change the test file.

---

## Before you start

Copy `lab-m05-02-files/` to your own folder. Nothing has to be installed and no
server has to be running. This lab is standard library Python and ten text
files.

Read `03-lecture-notes/MCCTC_145130_Notes_ParsingModelOutput.md` first if you
missed Thursday's instruction.

---

## The result shape

This is the only shape the rest of the program will ever see.

```json
{"title": "Chemistry unit 4 catch-up",
 "steps": ["Re-read the mole conversion notes", "Redo problems 7 to 14"],
 "minutes": 45}
```

| Field | Type | Rules |
|---|---|---|
| `title` | string | not empty, at most 120 characters |
| `steps` | list of string | 2 to 8 items, each at most 160 characters, none empty |
| `minutes` | int | 5 to 240 |

---

## The starter

`parse_plan.py` runs, imports, and every function returns. It also parses
nothing, so the tests that matter fail. That is the starting line, not a bug.

Two functions, and keeping them apart is the point of the lab.

```python
parse_study_plan(text)     # pull a shape out. Return a dict or None.
validate_study_plan(plan)  # decide if it is usable. Return the reason, or None.
```

**Why they are separate.** A parser that also validates gives the caller one
answer, `None`, for ten different problems. The service above you has to put a
real sentence in the envelope's error message, and it cannot invent one you did
not give it.

Two commands you will use constantly:

```
python test_parse_plan.py
python run_answers.py
python run_answers.py 04
```

---

## Steps

**Step 1.** Run the tests before you change anything.

```
python test_parse_plan.py
```

*Observable result:* 20 tests run, 10 failures and 2 errors. Read the names of
the four that pass. Three of them pass because the starter returns `None`, which
happens to be right for those cases and is right by accident.

**Step 2.** Run the answers viewer and read all ten.

```
python run_answers.py
```

*Observable result:* ten blocks, each showing the first line the model said and
then `parsed: None`. Read the ten model answers before you write a line of code.
Six of them carry a usable plan and four of them must not reach the rest of the
program. Write down which is which before you start.

**Step 3.** Write `strip_fences`. Use `FENCE_PATTERN`, which is already at the
top of the file.

*Observable result:* nothing changes yet. Nothing calls it.

**Step 4.** Write `find_json_object`. Try `json.loads` on the whole stripped
string first. If that raises, try again on the widest run from the first `{` to
the last `}`.

**One line you have to write and will not think of:** check
`isinstance(data, dict)` before you return. `json.loads("45")` succeeds and
gives you an integer.

**Step 5.** Write the JSON half of `parse_study_plan`. Read `title`, `steps`,
and `minutes` out of the dict, pass them to `build_plan`, and return it.

```
python run_answers.py 01
```

*Observable result:* `01_plain_json.txt` now shows a title, three steps, and 45
minutes.

**Step 6.** Write `as_minutes`. A number comes back as it is. A string gets the
first run of digits pulled out of it, because a model asked for a number sends
"about 25 minutes" often enough that refusing it throws away a usable answer.

**Check `isinstance(value, bool)` first and return `None` for it.** In Python
`True` is an `int`. Without that line, `{"minutes": true}` becomes one minute,
one minute is inside your range, and somebody gets a one minute study session
with no error anywhere.

```
python run_answers.py 06
```

*Observable result:* `minutes: 25`.

**Step 7.** Write `as_steps` and `build_plan`. `build_plan` trims to the field
limits. **Trim here and only here.** Trimming is shape work, not judgement, so
it belongs to the parser.

```
python run_answers.py 02
python run_answers.py 03
```

*Observable result:* the fenced answer and the one with a sentence in front of
it both parse. If 03 does not, your widest-braced-run attempt is not running.

**Step 8.** Write the prose half. Two patterns are already at the top of the
file. `STEP_PATTERN` matches a bullet or a numbered line. `LABEL_PATTERN`
matches a `Label: value` line.

```
python run_answers.py 04
python run_answers.py 05
```

*Observable result:* both prose answers produce a title, three steps, and a
number.

**Step 9.** Write `validate_study_plan`. One sentence per rule, written for a
person and not for a stack trace. The sentence you write here is what ends up in
the envelope's error message, and somebody reads it at eleven at night trying to
work out what broke.

```
python run_answers.py
```

*Observable result:* six answers say `usable: yes`, and four say `usable: no`
with four different sentences.

**Step 10.** Write `fallback_study_plan`. It is allowed to be worse than a model
plan. It is not allowed to fail your own validator, because then one failure
becomes two.

**Step 11.** Run the tests.

```
python test_parse_plan.py
```

*Observable result:* `Ran 20 tests` and `OK`.

**Step 12.** Add an eleventh answer file of your own. Write down a shape the
model might send that none of the ten covers, save it in `answers/`, and run
`run_answers.py` on it. If your parser handles it, say so in your commit
message. If it does not, decide on purpose whether to handle it, and write that
decision down.

---

## Acceptance criteria

1. `python test_parse_plan.py` prints `Ran 20 tests` and `OK`.
2. `python run_answers.py` shows six `usable: yes` and four `usable: no`.
3. The four `no` answers give four **different** sentences.
4. `parse_study_plan` returns `None` for the refusal, and a dict for the answer
   with one step in it. Those are two different problems and they get two
   different answers.
5. Your validator's messages name the thing downstream that breaks, not the rule
   number.
6. Your eleventh answer file exists, and your commit message says whether your
   parser handled it.
7. You did not change `test_parse_plan.py`.

---

## If it breaks

**`AttributeError: 'int' object has no attribute 'get'`**
`json.loads` succeeded and returned something that is not a dictionary. The
model sent a number, a string, or a list. Add the `isinstance(data, dict)` check
in `find_json_object`.

**`TypeError: 'NoneType' object is not subscriptable`**
Something called `plan["steps"]` on a parse that returned `None`. Your validator
has to check `if plan is None` on its first line, before it reads any field.

**Five tests fail and all five are prose answers**
Your JSON attempt is returning a dict with nothing useful in it, so the prose
half never runs. The JSON branch has to fall through to prose unless it actually
found something.

**`test_minutes_written_as_words` fails with `'about 25 minutes' != 25`**
`as_minutes` is returning the string unchanged. Pull the digits out with
`DIGITS_PATTERN`, which is already defined for you.

---

## Stretch goal

A model sends `{"steps": "1. Do this\n2. Then this"}`, a single string where you
asked for a list. Handle it inside `as_steps` without touching anything else,
and add your own answer file that proves it. Then write two sentences on why
this belongs in `as_steps` rather than in `validate_study_plan`.

---

## Submission checklist

- [ ] `parse_plan.py`, all twenty tests passing
- [ ] Your eleventh answer file in `answers/`
- [ ] A commit message saying what your eleventh answer was and what happened
- [ ] `notes.md`: your four validator sentences, and one line each on why that
      sentence names a real consequence
- [ ] Committed and pushed

---

## Extended options

Choose one. All four are graded on the same scale and assess the same
competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes | Give them |
|---|---|
| Stuck on step 4, trying to write one regex that does everything | SCAFFOLDED |
| Through step 7, reading the prose answers before coding | STANDARD or EXTENDED |
| Asks what happens when two rules fail at once | EXTENDED |
| Says none of this looks like their project | APPLIED |

### SCAFFOLDED

Six answers instead of ten. Delete `04`, `05`, `09`, and `10` from your copy of
`answers/`, and skip step 8 entirely, so you never write the prose half. Your
parser handles JSON only, in three wrappings: bare, fenced, and after a
sentence.

Run `python test_parse_plan.py TestAnswersThatWork` and
`python test_parse_plan.py TestTheRulesThemselves` rather than the whole file.

**Extra checkpoints:** show your instructor after step 4 and again after step 6.

**Then answer one question in writing:** your parser now throws away every prose
answer. Is that acceptable, and what would tell you whether it is.

### STANDARD

The lab as written. Ten answers, twenty tests, the eleventh file.

### EXTENDED

Everything in STANDARD, plus **two rules at once.** Right now your validator
returns the first reason it finds. Change it to collect every reason and return
all of them, and change the envelope's error message to carry a list.

Then answer the harder question in writing: the caller now gets three sentences
instead of one. Is that better for a person reading a terminal, and is it better
for a program branching on the failure. Say which of the two you optimised for
and why.

*Hint, not the answer:* `CONTRACT.md` section 5, from last week's lab folder,
splits `kind` from `message` for a reason. Read what it says about which one a
program branches on before you decide what a list of reasons should look like.

### APPLIED

Same skill, no model. Find a real messy text format you have to read: a
gradebook export, a fitness app's data dump, a game's save file, a CSV a teacher
sent you with merged header rows.

Build the same two functions for it. `parse` returns a shape or `None`.
`validate` returns the reason it is unusable. Collect at least eight real
examples of the format, including at least two that should fail, save them in an
`answers/` folder, and write your own test file with at least twelve tests.

Then answer the question this lab is really about: **your source is not a model.
Is it still untrusted?** Half a page, with an example from your own eight files
of something you had to defend against.
