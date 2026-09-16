# Additional Resources · Week 13
## 145130 Applications of AI · Module 5 · Week 13
### Topics: why the layers are separate, modeling the solution, constraints and I/O requirements, parsing model output

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed
live. Click it before you rely on it, and tell your instructor if it has moved.

**Nothing here asks you to sign up for a commercial AI developer API.** Those services require their
users to be 18 or older, so every model in this course runs on lab hardware. If a resource tells you to
get an API key, you are reading the wrong resource for this class.

In-repository links are relative to this file and they all resolve. Those are the ones you should reach
for first, because they describe the exact system you are building against.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff, the regular expressions chapter | Thu | On-level | 40 min |
| 2 | Official docs: Python `re` module | Thu | On-level | 20 min |
| 3 | Official docs: Python `json` module | Mon, Thu | On-level | 15 min |
| 4 | The JSON grammar at json.org | Thu | Remediation | 10 min |
| 5 | RFC 8259, the JSON standard | Thu | Extension | 25 min |
| 6 | Flask documentation | Mon, Wed | On-level | 20 min |
| 7 | Interactive: a regex tester, plus the ten captured answers in this repo | Thu | On-level | 30 min |
| 8 | This week's four lecture notes and their self-checks | Any | Review | 20 min each |
| 9 | The contract: `CONTRACT.md` | Mon, Wed | On-level | 25 min |
| 10 | The dataflow document: `the Why The Layers Are Separate note` | Mon, Tue | On-level | 20 min |
| 11 | The reference design set, five documents | Tue, Wed | On-level | 35 min |
| 12 | Drawing tools for a dataflow diagram and a UML class diagram | Tue | On-level | 30 min |
| 13 | Industry connection: how local model runners describe structured output | Thu | Extension | 25 min |
| 14 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 15 | SQ-18 Prompt Ablation | Fri | Extension | 1 block |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, third edition, the chapter on pattern matching with regular
expressions** · `https://automatetheboringstuff.com/` · **Confident** for the site. **[VERIFY]** the
third edition's chapter number and its exact path before you assign it.

**Why this one.** Thursday's parser leans on one regular expression and one pair of string searches.
This chapter teaches the parts you need in the order you need them: character classes, groups, the
difference between greedy and non-greedy matching, and `re.DOTALL`. The fence pattern in the lecture
notes, `` ```[a-zA-Z0-9_-]*\n(.*?)``` ``, uses all four of those ideas in one line.

**Read it with one question in your hand:** why is the pattern written with `.*?` instead of `.*`? The
answer is in this chapter, and it is the difference between grabbing the first fenced block and
grabbing everything from the first block to the last.

**Skip for now:** anything in the book about scraping or about calling a web service with a key.

**Time.** 40 minutes. **Level.** On-level.

---

## 2. The `re` module

`https://docs.python.org/3/library/re.html` · **Confident.**

**Assign a question, not the page:** *What does `re.DOTALL` change, and what happens to the fence
pattern without it?*

The answer is that without `re.DOTALL` the dot does not match a newline, so a fenced block that
spans more than one line never matches, and a perfectly good model answer is thrown away. That is a
planted defect you will meet later in the module.

A second question worth ten minutes: *what is the difference between `search` and `match`?* Using
`match` when you meant `search` is a real defect that produces no error and no result.

**Time.** 20 minutes. **Level.** On-level.

---

## 3. The `json` module

`https://docs.python.org/3/library/json.html` · **Confident.**

**Why this one.** The service in this module calls `json.loads` on text a model wrote, which means it
calls it on text that is often not JSON. The page you want is the one that documents
`json.JSONDecodeError` and what it carries.

**Assign a question:** *Find the conversion table between JSON and Python. What Python type does
`json.loads("45")` return, and what does `json.loads("[1, 2]")` return?*

Neither one is a dictionary, and both parse without raising. That is why the reference parser has
`isinstance(data, dict)` in it, and why a parser without that line calls `.get` on an integer.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. The JSON grammar itself

`https://www.json.org/` · **Confident.**

**Why this one.** The diagrams on the front page show every place a quote, a comma, and a brace is
allowed. If you keep writing single quotes or a trailing comma in a hand-built fixture, thirty seconds
on this page shows you the grammar has no room for either one.

Read it before you write your own captured answer files. A fixture that is not valid JSON tests your
parser against a problem the model does not have.

**Time.** 10 minutes. **Level.** Remediation.

---

## 5. How JSON is actually defined

**RFC 8259, The JavaScript Object Notation (JSON) Data Interchange Format** ·
`https://www.rfc-editor.org/rfc/rfc8259` · **Confident.**

**Why this one.** It is short, it is readable, and it settles arguments. Two things in it are worth
your time this week. First, it says a JSON text can be any value, not only an object, which is the
standards-level reason `json.loads("45")` succeeds. Second, it says object member names should be
unique but does not forbid duplicates, and it says parsers differ on what they do about it.

**Assign a question:** *If a model returns an object with the key `minutes` twice, which value does
`json.loads` keep?* Then test it. Reading a rule and then running it is worth more than either one
alone.

**Time.** 25 minutes. **Level.** Extension.

---

## 6. Flask

`https://flask.palletsprojects.com/` · **Confident.**

**Why this one.** The model service in this module is a Flask application. You do not need much of
Flask, and this week you need exactly three things: how a route reads a JSON body, how a view returns
a JSON body with a status code you choose, and how to run the development server on a port you pick.

Read the Quickstart section, and stop after JSON handling. The parts about templates, sessions, and
deployment are not this course.

**One thing to notice.** Returning `(body, 400)` from a view is how the service refuses a request
before it costs anything. Wednesday's lesson is built on that: a bad request returns HTTP 400 with
`elapsed_ms` at zero, because the model was never called.

**Time.** 20 minutes. **Level.** On-level.

---

## 7. Interactive practice

**A regular expression tester** · `https://regex101.com/` · **[VERIFY]** before you assign it. Set the
flavor to Python, paste the fence pattern, and paste in a real captured answer. The right-hand panel
explains the pattern token by token, and the match highlighting shows you what the group captured.

**Then use the real data.** This repository ships ten captured model answers to the same prompt, and
they are better practice than anything you can invent, because nobody imagined them.

- [run_answers.py](../05-labs/lab-m05-02-files/run_answers.py) runs your parser over all ten and prints
  what each one produced
- [the ten answers](../05-labs/lab-m05-02-files/answers/01_plain_json.txt) sit in the same folder,
  numbered, one behaviour each
- [test_parse_plan.py](../05-labs/lab-m05-02-files/test_parse_plan.py) is the test file, standard
  library `unittest`, so it needs nothing installed

**The practice that teaches the most:** open `07_refusal.txt` and `10_wrong_keys.txt` and work out by
hand what your parser returns for each, before you run it. Both return nothing, for two different
reasons, and a validator that says the same sentence about both is a validator that has stopped being
useful.

Official docs for the test runner: `https://docs.python.org/3/library/unittest.html` · **Confident.**

**Time.** 30 minutes. **Level.** On-level.

---

## 8. This week's lecture notes

Four concepts, four files, and each one ends with three self-check questions and worked answers.

| Day | Notes |
|---|---|
| Monday | [Why the model layer and the application layer are separate](../03-lecture-notes/MCCTC_145130_Notes_WhyTheLayersAreSeparate.md) |
| Tuesday | [Modeling the solution before you build it](../03-lecture-notes/MCCTC_145130_Notes_ModelingTheSolution.md) |
| Wednesday | [Constraints, processing requirements, and what crosses the boundary](../03-lecture-notes/MCCTC_145130_Notes_ConstraintsAndIORequirements.md) |
| Thursday | [Parsing model output into something your program can rely on](../03-lecture-notes/MCCTC_145130_Notes_ParsingModelOutput.md) |

**You should be able to answer all twelve self-check questions without reading the answers.** The two
that matter most for the module exit are Monday question 1, which asks which field tells you whether a
model was involved, and Thursday question 3, which asks when you trim a model answer and when you
refuse it.

**Time.** 20 minutes each. **Level.** Review.

---

## 9. The contract

[CONTRACT.md](../05-labs/lab-m05-01-files/CONTRACT.md) · **Confident**, it is in this
repository.

**Why this one.** This is the document Monday's lesson is about. It says what goes into the service,
what comes back, every field, every type, and the name of every failure. Every module in this course
that touches the model builds against it.

**Read it with a pen.** Find the six fields of the envelope. Find the two result shapes. Find the list
of error kinds and count them. Then look at your own team's result shape and ask whether a stranger
could write a client against it using only what you wrote down.

**Time.** 25 minutes. **Level.** On-level.

---

## 10. The dataflow document

[Notes_WhyTheLayersAreSeparate.md](../03-lecture-notes/MCCTC_145130_Notes_WhyTheLayersAreSeparate.md) · **Confident.**

**Why this one.** Tuesday asks you to draw a dataflow diagram, and this is a worked one for the system
you are building against. It shows the three layers, what crosses each boundary, and where each thing
is checked.

**The part to copy is not the boxes.** It is the habit of writing, at every boundary, what that layer
is allowed to assume about what it received. A diagram with arrows and no assumptions on it is a
picture. A diagram that says "below this line the answer is validated" is a design.

Read it next to [Lab M05-01](../05-labs/MCCTC_145130_Lab_M05-01_TraceTheContract.md), which shows the same
system from the other side: the commands that start it and what each failure looks like when it is
working correctly.

**Time.** 20 minutes. **Level.** On-level.

---

## 11. The reference design set

Five documents, in [the reference implementation](../09-project/reference-implementation/design/ipo-chart.md)'s
design folder. **Confident**, all in this repository.

| Document | What it shows you |
|---|---|
| [ipo-chart.md](../09-project/reference-implementation/design/ipo-chart.md) | the first forty minutes, including the input row people leave off |
| [dataflow-diagram.md](../09-project/reference-implementation/design/dataflow-diagram.md) | what moves between layers and where it is checked |
| [io-specification.md](../09-project/reference-implementation/design/io-specification.md) | every field, with type, range, and what happens when it is wrong |
| [data-dictionary.md](../09-project/reference-implementation/design/data-dictionary.md) | every named field in one table, competency 5.6.8 |
| [constraint-list.md](../09-project/reference-implementation/design/constraint-list.md) | every constraint with its reason and its cost |

**Use these as a shape, not as an answer.** Your task is not the reference task, so your fields are not
the reference fields. What you are copying is the level of detail: three columns on a constraint, four
columns on a field, and a number on every processing requirement.

**The single most valuable row in any of them** is the last row of the IPO chart's input table: the
model's answer is an input to your system. It comes from outside, you do not control it, and it is the
input most likely to arrive in a shape you did not plan for.

**Time.** 35 minutes. **Level.** On-level.

---

## 12. Drawing the diagrams

You can draw Tuesday's diagrams on paper and photograph them. That is allowed and it is often faster.
If you want them in the repository as text that a diff can show, two options.

**Mermaid** · `https://mermaid.js.org/` · **[VERIFY]**. Mermaid writes diagrams as text inside a fenced
code block, and it has a class diagram syntax that covers what a UML class diagram needs for this
project: the type name, its fields with types, and the arrows between types. Text diagrams live in your
repository and change in a commit, which is worth more than a prettier picture nobody can edit.

**diagrams.net** · `https://www.diagrams.net/` · **[VERIFY]**. Free, runs in a browser, needs no
account if you save the file to your own machine. Better than Mermaid when you want boxes positioned
where you want them, which a dataflow diagram usually does.

**Whichever you pick, export or commit the source.** A diagram that exists only as an image in a chat
thread does not survive to Week 15, and Week 15 is when somebody reads it.

**If you ask a model to draft a diagram:** that is allowed, it is named in competency 5.1.3, and it
comes with one rule. You record in your decision log that a model drafted it, what you changed, and
why, and you have to be able to defend every line. Submitting a diagram you cannot explain is the one
thing in this program that ends in a zero.

**Time.** 30 minutes. **Level.** On-level.

---

## 13. Industry connection: getting a shape out of a local model

**[VERIFY].** No article is linked here, because the honest industry connection for this week is a
moving target and a named article would be stale by the time you read it.

**What to look for.** Local model runners now ship features that constrain a model's output to a
schema, so the runtime refuses to emit tokens that would break the shape. Search for the structured
output or format documentation of the model runner your lab uses, and for the term **constrained
decoding**. The Ollama project documents its API and its structured output support in the `docs` folder
of its public repository, at `https://github.com/ollama/ollama` · **[VERIFY]**.

**Read it against what you built.** Constrained decoding removes a class of parsing problem and does
not remove validation. A schema can force the model to emit an integer named `minutes`. It cannot stop
the model from choosing 600.

**The argument to be able to make both ways.** One side: if the runtime can guarantee the shape, hand
parsing is wasted work and a source of bugs. The other side: the guarantee holds only for the one
runtime you tested, your service is supposed to survive the model being swapped, and a parser that
handles prose is the thing that keeps working when somebody points the service at a different runner.
Both are real positions held by real teams. Your decision log should say which one you took and why.

**Time.** 25 minutes. **Level.** Extension.

---

## 14. A free video

**[VERIFY].** No specific video is named here, because a title and a channel that are wrong cost more
than no link at all.

**What to search for, and how to pick one.** Search for a video under 20 minutes on **regular
expressions in Python** or on **reading JSON in Python**. Watch the first two minutes before you
assign it, and use three tests:

1. It writes and runs code on screen rather than reading slides
2. It uses `re.search` and shows what a group captures
3. It does not ask you to install anything or sign up for anything

**Python for Everybody**, `https://www.py4e.com/` · **Confident** for the site, publishes free lecture
videos with no account, including material on regular expressions and on reading structured data.
Start there, and check the runtime before you assign it.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 15. Side quest and extension

**SQ-18 Prompt Ablation** ·
[the bundle](../../../../Misc/side-quests/SQ-18-Prompt-Ablation/README.md) · **Confident**, it is in
this repository. One block, difficulty ★★.

**Why it fits this week.** Thursday's lesson is about parsing whatever the model said. This quest is
about the other half: what in your prompt was making the model say it. You remove one element of a
working prompt at a time and record what changes. It ships its own stub model server, so it runs with
no model installed and no network.

**Most students are surprised by the result.** You will find elements you were certain mattered that do
nothing at all.

### Two extensions that need no bundle

**Add the eleventh answer.** Run your service against the stub, find a behaviour the ten captured
answers do not cover, save what came back as `11_something.txt`, and add a test for it in
[test_parse_plan.py](../05-labs/lab-m05-02-files/test_parse_plan.py). You are building a test set out of
what actually happened, which is worth more than any test set you could invent.

**Write the decision table nobody asked for.** Take three conditions from your own design that combine,
write all eight rows, and bring it to Friday's walkthrough. The rows you write because the table has a
gap are the ones that find the defect.

**Time.** One block for SQ-18, 30 minutes for either extension. **Level.** Extension.

---

## For the student who is behind

1. Monday's lecture notes, the section called "The four reasons", read out loud
2. json.org, the diagrams, for anyone still hand-writing fixtures that do not parse
3. [run_answers.py](../05-labs/lab-m05-02-files/run_answers.py) on the ten captured answers, with the
   reference parser, before writing any parser of your own
4. The `re` module page, the two questions in section 2 and nothing else

## For the student who is ahead

- RFC 8259, and the duplicate key experiment in section 5
- The structured output reading in section 13, and a decision log entry taking a position
- SQ-18 Prompt Ablation
- Draft the UML class diagram for your result shapes in Mermaid, and commit the source
