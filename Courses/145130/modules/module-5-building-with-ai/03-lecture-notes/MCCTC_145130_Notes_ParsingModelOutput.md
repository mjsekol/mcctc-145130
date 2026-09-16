# Lecture Notes: Parsing Model Output Into Something Your Program Can Rely On
## 145130 Applications of AI · Module 5 · Week 13, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W13_ParsingModelOutput.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W13_ParsingModelOutput.pptx)

If you missed class, you can learn this concept from this file alone. To run the
examples you need `05-labs/lab-m05-02-files/`, which has ten captured model
answers in it and needs nothing else installed.

**This is the second exit criterion for this module:** parse unstructured model
output into something your program can rely on. **Competency 5.1.2** is
algorithms and data structures in information processing, and this is what that
looks like when the data comes from a model.

---

## Why this exists

You asked a model for JSON. You were specific. Your prompt said "Reply with JSON
only, shaped exactly like this", and you gave it an example.

Here are three real answers to that prompt, all three answering the same
question. They are in `05-labs/lab-m05-02-files/answers/`, ten of them, and every
one is a shape a model really produces.

```
{"title": "Chemistry unit 4 catch-up", "steps": ["Re-read the mole conversion notes", ...], "minutes": 45}
```

```
```json
{
  "title": "Chemistry unit 4 catch-up",
  ...
}
```
```

```
Sure, here is the study plan you asked for in JSON:

```json
{"title": "Algebra 2 quiz prep", ...}
```

Let me know if you would like it broken into smaller sessions.
```

All three are cooperative answers. None of them is the model being difficult.
And exactly one of the three is what `json.loads` will accept.

**That is the job.** Not making the model behave. Turning whatever it said into
a shape, or saying plainly that there was no shape in there.

---

## The concept in plain language

Two functions, and the split between them is the whole lesson.

**`parse`** pulls a shape out of the mess. It returns the shape or `None`. It
does not decide whether the shape is good enough to use.

**`validate`** decides whether the shape is good enough to use. It returns the
reason it is not, or `None` when it is fine.

Keeping them apart matters for one concrete reason: a parser that also validates
gives the caller one answer, `None`, for ten different problems. The service
above you has to put a real sentence in the envelope's `error.message`, and it
cannot invent one you did not give it.

```python
plan = parse_study_plan(text)          # a dict, or None
reason = validate_study_plan(plan)     # a sentence, or None
if reason is None:
    return envelope(ok=True, result=plan, source="model", error=None)
return envelope(ok=True, result=fallback_study_plan(request), source="fallback",
                error={"kind": "task_validation_failed", "message": reason})
```

### The order the parser tries things

JSON first, because a JSON answer is unambiguous. Prose second, because reading
prose means guessing, and **you guess last**.

1. Strip the code fence, if there is one.
2. Try `json.loads` on the whole thing.
3. If that failed, try again on the widest run from the first `{` to the last `}`.
4. If that failed, read it as prose: labelled lines, bullets, numbered items.
5. If nothing produced anything, return `None`.

Step 3 is what rescues "Sure, here is the JSON you asked for". Step 1 is the
single most common reason a first attempt at parsing model output fails.

---

## Worked example 1: the three functions that do the work

```python
FENCE_PATTERN = re.compile(r"```[a-zA-Z0-9_-]*\n(.*?)```", re.DOTALL)


def strip_fences(text):
    """The inside of the first fenced block, or the text unchanged."""
    match = FENCE_PATTERN.search(text)
    return match.group(1).strip() if match else text.strip()


def widest_braced_run(text):
    """From the first brace to the last, or None."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end <= start:
        return None
    return text[start:end + 1]


def find_json_object(text):
    """A dict parsed out of the text, or None."""
    candidate = strip_fences(text)
    for attempt in (candidate, widest_braced_run(candidate)):
        if attempt is None:
            continue
        try:
            data = json.loads(attempt)
        except (json.JSONDecodeError, ValueError):
            continue
        if isinstance(data, dict):
            return data
    return None
```

Three details are load bearing.

**The language tag is optional.** `[a-zA-Z0-9_-]*` matches ` ```json `,
` ```JSON `, and a bare ` ``` `. A pattern that requires the word `json` throws
away a perfectly good answer, and you will meet that exact defect in Gate 2 this
week.

**`isinstance(data, dict)`.** `json.loads("45")` succeeds and returns an integer.
`json.loads("[1,2]")` succeeds and returns a list. Neither is your result shape,
and without that check your next line is `data.get(...)` on an int.

**The loop tries both candidates.** Not one, and not an if-else ladder. Two
attempts in order, first one that works wins.

---

## Worked example 2: coercion, and where to stop

Here is a real captured answer. It is valid JSON and it is not what you asked
for:

```json
{"title": "Spanish 3 vocabulary", "steps": [...], "minutes": "about 25 minutes"}
```

You asked for a number. You got a sentence with a number in it.

```python
def as_minutes(value):
    """A whole number of minutes from a number, or from a string with digits."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        match = DIGITS_PATTERN.search(value)
        if match:
            return int(match.group(0))
    return None
```

Run the whole set through the reference parser:

```
== 06_minutes_as_text.txt ==
   model said: {"title": "Spanish 3 vocabulary", "steps": ["Write the 20 unit words on
   title:      'Spanish 3 vocabulary'
   steps:      3
   minutes:    25
   usable:     yes
```

**The `bool` check on the first line is not paranoia.** In Python, `True` is an
`int`. Without that line, `{"minutes": true}` becomes 1 minute, and 1 minute is
inside your allowed range, so validation passes and somebody gets a one minute
study session with no error anywhere.

### Where to stop coercing

**Trimming is not failing. Inventing is failing.**

Six bullets when the limit is five gets cut to five and used. A bullet 400
characters long gets shortened and used. The answer meant what it meant and the
shape was untidy.

A label the model made up gets refused even though it is a perfectly good
string. The difference is that a trimmed bullet still means what the model
meant, and an invented category does not mean anything the rest of your system
can act on.

---

## Worked example 3: validation that writes a sentence, not a boolean

```python
def validate_study_plan(plan):
    """The reason this plan is unusable, or None when it is fine."""
    if plan is None:
        return "no study plan could be read out of the answer"
    if not isinstance(plan.get("title"), str) or plan["title"] == "":
        return "the answer had no title, and the planner screen prints one"
    steps = plan.get("steps")
    if not isinstance(steps, list) or len(steps) < MIN_STEPS:
        found = 0 if not isinstance(steps, list) else len(steps)
        return (f"the answer had {found} step{'' if found == 1 else 's'}, "
                f"and a plan needs at least {MIN_STEPS}")
    minutes = plan.get("minutes")
    if not isinstance(minutes, int) or isinstance(minutes, bool):
        return "the answer gave no number of minutes, and the timer needs one"
    if minutes < MIN_MINUTES or minutes > MAX_MINUTES:
        return (f"the answer asked for {minutes} minutes, outside the "
                f"{MIN_MINUTES} to {MAX_MINUTES} the timer allows")
    return None
```

Every rule names the thing downstream that breaks without it. Run it over the
captured answers and the messages are what a person reads at eleven at night:

```
== 08_one_step.txt ==
   usable:     no. the answer had 1 step, and a plan needs at least 2

== 09_minutes_out_of_range.txt ==
   usable:     no. the answer asked for 600 minutes, outside the 5 to 240 the timer allows

== 07_refusal.txt ==
   parsed:     None. Nothing in that answer looked like a plan.
   usable:     no. no study plan could be read out of the answer

== 10_wrong_keys.txt ==
   parsed:     None. Nothing in that answer looked like a plan.
   usable:     no. no study plan could be read out of the answer
```

Four different failures, four different sentences. Compare that with a validator
that returns `False` four times.

---

## The wrong version, and the exact thing it produces

Here is the parser most people write first. It is one line and it works.

```python
plan = json.loads(text)
```

Run it on the ten captured answers and it works on exactly one of them. The
other nine raise:

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

That message is honest and useless. It does not say the answer was in a code
fence. It does not say the model wrote a sentence first. It does not say the
model refused. One exception, nine causes.

Now the version people write second, which is worse:

```python
match = re.search(r"```json\n(.*?)```", text, re.DOTALL)
if not match:
    return None
```

This is a real defect you will find in Gate 2 this week. It looks careful. It
handles the fence. And it throws away every bare JSON answer and every prose
answer, silently, and the service reports `task_validation_failed`, which sends
whoever reads the log looking at the model instead of at the regex.

Here is that defect running, captured:

```
### mode fenced_json: HTTP 200 source='model' error=None
### mode bare_json:   HTTP 200 source='model' error='plan_validation_failed'
### mode prose:       HTTP 200 source='model' error='plan_validation_failed'
```

Two perfectly good answers, thrown away by one regex.

---

## Why the wrong version is tempting

Because it works on the first answer you test with.

You write the prompt, you run it once, the model wraps its JSON in a fence, your
fence regex matches, and you move on. Everything you saw said it worked. The
model is not deterministic, and the next answer, on a different day with a
different prompt, does not have a fence.

**The habit that prevents it:** capture answers and keep them. Ten files in a
folder. Every time the model does something new, save that answer next to the
others and add a test for it. You are building a test set out of what actually
happened, and it is worth more than any test set you could invent, because you
did not have to imagine any of it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Unstructured output** | text a model wrote, in whatever shape it chose |
| **Structured result** | a fixed set of named fields with known types |
| **Parsing** | pulling a shape out of text. Returns the shape or nothing. |
| **Validation** | deciding whether a shape is good enough to use. Returns the reason it is not. |
| **Coercion** | turning a value of one type into the type you needed, when that is safe |
| **Code fence** | three backticks, sometimes with a language name, around a block |
| **Fallback** | a result your own code built without the model |
| **Fixture** | a saved input you test against, kept so the test means the same thing next week |

---

## Self-check

**Question 1.** `json.loads` succeeds and your next line is `data.get("title")`,
and it raises `AttributeError`. What did the model send, and what one line
prevents it?

**Question 2.** Your validator returns `True` or `False`. Name two things the
service above you cannot do because of that.

**Question 3.** A model returns seven bullets when your limit is five, and a
label of `facilities` when your list has five other words in it. One of those
you trim and use, one you refuse. Say which is which and give the rule that
tells them apart.

---

### Answers

**1.** The model sent valid JSON that is not an object: a number, a string, or
a list. `json.loads("45")` returns an integer and integers have no `.get`. The
line that prevents it is `if not isinstance(data, dict): return None`, placed
immediately after the parse and before anything reads a field.

**2.** It cannot put a real reason in `error.message`, so the envelope says
something generic and the person reading it has no idea which rule failed. And
it cannot tell the difference between "the answer had no bullets" and "there was
no answer at all", which are two different problems with two different fixes:
one is a prompt problem and one is a connection problem.

**3.** Trim the seven bullets down to five and use them. Refuse the label. The
rule: trimming keeps what the model meant, and an invented category does not
mean anything the rest of the system can act on. Seven bullets cut to five is
still five true bullets. A label outside your list is a value your database, your
report, and your filters have never heard of, and it gets written down and found
three weeks later.
