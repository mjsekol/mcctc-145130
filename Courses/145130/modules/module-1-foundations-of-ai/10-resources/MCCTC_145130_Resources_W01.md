# Additional Resources · Week 1
## 145130 Applications of AI · Module 1 · Week 1
### Topics: rules against weights, where the model runs, tokens and the context window, training and inference

Every link below is marked **Confident** or **[VERIFY]**. **Confident** means the address is one
your instructor would bet a class period on. **[VERIFY]** means it has not been confirmed live and
somebody clicks it before it is assigned. Broken links cost a period, so the list here is short and
honest rather than long.

**The most reliable sources in this module are the module's own files.** The lecture notes and the
kit in `05-labs/local-model-kit/` were written for this module and captured from real runs of it.
Start there. Outside links are for depth, not for the basics.

**Module 1 ports.** Stub model server **11634**. Streaming stand-in **11635**. Port 11434 is held
for a real model. Every command on this page passes its port.

**There is nothing between your program and the model in this module.** One HTTP request out to
`/api/generate`, one reply back, and the whole answer is text sitting in one field. Making sense of
that text is your job. In **Module 5** you build the service layer that does it in one place, which
is why there is no service in your kit and why Weeks 1 and 2 are meant to feel like work.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Week 1 lecture notes, four files | Mon-Thu | On-level | 20 min each |
| 2 | `local-model-kit/README.md`, all of it | Tue | On-level | 20 min |
| 3 | `stub_model_server.py`, the header comment | Tue | On-level | 20 min |
| 4 | `one_request.py` and `ask_model.py` | Tue | On-level | 25 min |
| 5 | The Module 1 performance task brief | Mon | On-level | 20 min |
| 6 | Official docs: `json` and `urllib.request` | Tue | On-level | 15 min |
| 7 | scikit-learn User Guide, Decision Trees | Mon | Extension | 25 min |
| 8 | Python Tutor, for branch order | Mon | Remediation | 15 min |
| 9 | A free video on what a neural network is | Mon | On-level | about 19 min |
| 10 | Ollama, the industry connection for local models | Thu | Extension | 15 min |
| 11 | Gate 1 Reps 01, 02, 06, 16, 17 | Mon-Thu | Review | 10 min each |
| 12 | `AI_USAGE.md` and `LICENSING.md` templates, below | Mon | Required | 15 min |
| 13 | SQ-20 Explain It to a Seventh Grader | Fri | Extension | one block |

---

## 1. Primary reading · the four Week 1 lecture notes

These are the on-level reading for this week. Each one carries three worked examples, the wrong
version and what it costs, a vocabulary table, and three self-check questions with answers. If you
were absent, the note is the class.

- Monday: [`../03-lecture-notes/MCCTC_145130_Notes_RulesYouWroteVersusWeightsFitted.md`](../03-lecture-notes/MCCTC_145130_Notes_RulesYouWroteVersusWeightsFitted.md)
- Tuesday: [`../03-lecture-notes/MCCTC_145130_Notes_WhereTheModelActuallyRuns.md`](../03-lecture-notes/MCCTC_145130_Notes_WhereTheModelActuallyRuns.md)
- Wednesday: [`../03-lecture-notes/MCCTC_145130_Notes_TokensAndTheContextWindow.md`](../03-lecture-notes/MCCTC_145130_Notes_TokensAndTheContextWindow.md)
- Thursday: [`../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md`](../03-lecture-notes/MCCTC_145130_Notes_TrainingAndInference.md)

**Why these rather than a textbook.** Every example in them runs against the stand-in on your
machine, on this module's ports, and every number in them came from a real run. A textbook chapter on
neural networks will be more general and less checkable. You want checkable this week.

**Read them in the order above.** Tuesday's note carries the fact the rest of the module hangs off:
the model returns text, not data.

**Time.** About 20 minutes each. **Level.** On-level.

---

## 2. Primary source · the kit README, all of it

[`../05-labs/local-model-kit/README.md`](../05-labs/local-model-kit/README.md) · **Confident**, it is
a file in this repository.

**What it is.** Two files and how to run them. What you are talking to and what you are not. The two
ports. The ten modes the stand-in can fail in. How to stop everything and check that you did.

**Why this one, and read it before Tuesday.** The single most expensive mistake available to you this
week is running a server on the wrong port. **A run against the wrong server looks exactly like a
working run.** You do not find out until the numbers make no sense, and by then you have written them
down. The README names the symptom in plain words: the stand-in with no `--port` argument lands on
11434, where nothing in this module is looking.

**The two commands, with the port passed.** Terminal 1:

```
python stub_model_server.py --port 11634
```

Terminal 2, PowerShell:

```
$env:RIDGE_MODEL_URL = "http://127.0.0.1:11634"
python one_request.py
```

**Nothing to install.** The stand-in is standard library Python. If a set of instructions anywhere
tells you to install something for Module 1, you are reading instructions from a different module.

**Assign a question.** *Find the captured reply in the README. Three fields come back. Which one
holds the answer, what type is it, and what is wrapped around the JSON inside it?* Then the harder
half: *what does your program have to do before it can read a label out of that?*

**Read the section on stopping everything, and do it.** A terminal closed without Ctrl+C leaves a
server running. The symptom the next day is a stand-in that will not start, or worse, one that starts
in the wrong mode and answers your program without you knowing.

**Time.** 20 minutes. **Level.** On-level, and required for anyone whose stand-in is not running.

---

## 3. Primary source · the header comment of `stub_model_server.py`

[`../05-labs/local-model-kit/stub_model_server.py`](../05-labs/local-model-kit/stub_model_server.py) ·
**Confident**, it is a file in this repository.

**What it is.** The first forty lines are the documentation for the whole stand-in: the two endpoints
it answers, the exact request and reply shapes, all ten failure modes with one line each, and the
three extra endpoints a real server does not have.

**Why this one.** It is a primary source and it cannot drift from the program, because it is the
program. Everything else you will read about calling a model is somebody describing a system you
cannot inspect. This one is on your desk, and you can make it fail on demand.

**Assign a question.**

1. *Find the line that gives the default port. Say what happens to your work if you accept it.*
2. *Read the ten modes. Three of them answer HTTP 200 with a body your program still cannot use.
   Name them, and say what tells the three apart from a working answer.*
3. *Find `/stub/stats`. The comment says a real server does not have it. Why is that worth stating,
   and what can you learn from it that you could not learn any other way?*

**Time.** 20 minutes. **Level.** On-level.

---

## 4. Primary source · `one_request.py` and `ask_model.py`

[`../05-labs/local-model-kit/one_request.py`](../05-labs/local-model-kit/one_request.py) and
[`../05-labs/lab-m01-01-files/ask_model.py`](../05-labs/lab-m01-01-files/ask_model.py) ·
**Confident**, they are files in this repository.

**What they are.** `one_request.py` is the smallest program that talks to a model server: two
requests, one that works and one the server refuses. `ask_model.py` is the finished side of Lab
M01-01, and it is the same idea with the parsing written out.

**Why these two, in this order.** `one_request.py` shows you the reply. `ask_model.py` shows you what
it takes to get one value out of it. Reading them back to back is the argument for Module 5 made with
line counts rather than with a slide.

**Assign a question.** *`ask_model.py` records a `how` field next to every label: `json`, `prose`,
`off_list`, or `unparsed`. Find where each one is set. Then say what a table of labels with no `how`
column would hide from somebody reading it three weeks later.*

**Second question, and it is the one Tuesday turns on.** *`one_request.py`'s second request comes back
HTTP 400 with a body that says why. Name one thing that is good about that failure, and one failure
mode in the stand-in's list that would have been worse for your program while looking better.*

**Time.** 25 minutes. **Level.** On-level.

---

## 5. Read the performance task brief in Week 1, not Week 3

[`../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md`](../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md) ·
**Confident**, it is a file in this repository.

**What it is.** The Module 1 performance task: a benchmark report and a one-page explainer, both
answering one client brief. It is handed out on Friday of Week 1.

**Why read it on Monday instead.** The brief is written as a person speaking, so you have to pull the
requirements out of it yourself. The explainer is due in Week 3 and is far better if it has been
sitting for two weeks. Knowing on Monday what you are building toward changes which parts of the week
you pay attention to.

**The brief is a composite.** It says so in the file. It was written for this course and no specific
person said those words. Noticing that a document tells you what it is counts for something, and
Week 2 is three days on documents that do not.

**Assign a question.** *The client asked for two things and did not ask for four others. Find the
paragraph that names what they did not ask for. Which one would you have given them anyway, and what
would it have cost you?*

**Time.** 20 minutes. **Level.** On-level.

---

## 6. Official documentation · `json` and `urllib.request`

`https://docs.python.org/3/library/json.html` · **Confident.**
`https://docs.python.org/3/library/urllib.request.html` · **Confident.**

**Why these two.** `one_request.py` is sixty lines and it uses exactly these two modules. Reading the
program next to the documentation for the two things it imports is the fastest way to stop treating
an HTTP call as something mysterious.

**Assign a question.** *`one_request.py` builds an opener with an empty `ProxyHandler` before it sends
anything. Find `ProxyHandler` in the `urllib.request` page. What would happen on a school network
without that line, and why does it matter that the address is 127.0.0.1?*

**Second question, for Tuesday.** *Find `json.loads` and read what it raises when the text is not
valid JSON. Now look at the captured reply in the kit README: the answer is JSON wrapped in a code
fence, inside a string. Write down what `json.loads` does to that string, and what your program has
to strip first.* That is the failure Gate 1 Rep 02 and Rep 10 are both built on.

**Time.** 15 minutes. **Level.** On-level.

---

## 7. What a decision tree actually is, in the documentation of a tool that builds them

**scikit-learn User Guide, Decision Trees** · `https://scikit-learn.org/stable/modules/tree.html` ·
**Confident.**

**Why this one.** Monday's concept is rules a person wrote against weights fitted to data. This page
is the other half of that sentence written by people who ship the code: a tree learned from data
rather than typed by hand. It shows the same readable-reason property the lab gives you, and it is
blunt about what trees give up.

**Assign a question.** *Find the list of advantages and the list of disadvantages. Which advantage is
the one Monday's lab is built around? Find the disadvantage about small changes in the data, and say
what it does to the claim that a tree is stable.*

**A companion page, if you want the other column:**
`https://scikit-learn.org/stable/modules/neural_networks_supervised.html` · **[VERIFY].** The page
you are looking for is the User Guide section on supervised neural network models, the one that
documents `MLPClassifier`. Confirm the address resolves before assigning it. If it moved, find
"Neural network models (supervised)" from the User Guide contents page.

**Do not install scikit-learn for this.** You are reading it, not running it. Module 4 is where
fitting a model becomes your problem.

**Time.** 25 minutes. **Level.** Extension.

---

## 8. Interactive practice · Python Tutor, for branch order

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

**What to do with it.** Paste Monday's three-branch `classify` function from
[`../05-labs/lab-m01-01-files/triage_rules.py`](../05-labs/lab-m01-01-files/triage_rules.py) and step
through it with the sentence `I cannot log in to the wifi`. Watch which branch is tested first.
Then move the account branch above the network branch and step through the same sentence again.

**Why this one.** The claim that order is a decision somebody made is hard to believe when you read
it. It is impossible to disbelieve when you watch the pointer walk down the list and stop early. The
answer changes and neither rule was wrong.

**The second interactive practice this week is the stand-in itself.** Start it on 11634, run
`one_request.py`, then stop the stand-in with Ctrl+C and run `one_request.py` again. Read what your
program prints when nothing is listening. Then start it again in `success_prose` mode and read what
it prints when something is listening and the answer contains no JSON. **Two failures, two completely
different fixes, and one of them arrives looking like success.** That is a laboratory, and it is on
your desk.

**Time.** 15 minutes. **Level.** Remediation.

---

## 9. A free video, under 20 minutes

**3Blue1Brown, "But what is a neural network?", chapter 1 of the Deep learning series.** About 19
minutes. **[VERIFY] the link before assigning.** The series is published on the channel's YouTube
page and indexed at `https://www.3blue1brown.com/topics/neural-networks` · **[VERIFY].** Search for
the exact title if that address does not resolve.

**Why this one.** It is the clearest free explanation of what "weights fitted to data" means, and it
never says magic. It shows the arithmetic, and it is honest that the arithmetic is all there is.

**The caveat you must state when you assign it.** The video classifies handwritten digits with a
fully connected network. **That is not a language model**, and the architecture behind the assistant
on a phone is different. What transfers is the idea of weights, layers, and fitting. What does not
transfer is the shape. Say this out loud, because a student who watches it and then explains a
language model as a digit classifier has learned something false with confidence.

**If the link fails.** There is no second video on this page that has been confirmed live. Search
for a video whose title is a question about what a neural network is, watch the whole thing yourself
before class, and check two things: that it shows weights and an activation being multiplied and
added, and that it does not claim the network understands anything.

**Time.** About 19 minutes. **Level.** On-level.

---

## 10. The industry connection · running a model on your own hardware

**Ollama** · `https://ollama.com/` · **Confident** for the site. The model listing at
`https://ollama.com/library` · **[VERIFY].**

**Why this one.** This is Thursday's lesson standing in a commercial setting. The whole industry
practice of running a model locally, on hardware you own, with no account and no key, is what this
course does for the whole semester, and this is the most widely used tool for it. Port 11434 is
reserved in this module because it is the port an Ollama-compatible server listens on by default.

**Assign a question.** *Find any model on the listing and read what it says about size and memory.
Then say which of training or inference that number is about, and explain how you know.* The answer
matters, because the confusion between the cost of training and the cost of inference is the single
most common wrong idea about what models cost.

**This is a reading assignment, not an install.** Nothing in Module 1 requires a real model runtime,
and nothing in this course requires an account or a key anywhere.

**No dated industry article is linked here.** An article's address could not be confirmed live, and a
broken link is worse than none. If you want a current one, bring it to class and run it through the
five evaluation parameters before anyone reads it as fact.

---

## 11. Gate 1 reps worth redoing on your own

From [`../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md`](../06-gate1-reps/MCCTC_145130_Gate1_FoundationsOfAI.md).
Your instructor assigns these from the instructor copy, and redoing them alone is the best short
review in the module.

- **Rep 01** (TRACE) and **Rep 18** (EXPLAIN): branch order, and how a correct program gives a wrong
  label
- **Rep 06** (FIX): the tree that calls a makerspace ticket `hardware`
- **Rep 02** (TRACE): the reply, the fence, and why the line that works is a line you should not
  write
- **Rep 16** (EXPLAIN): every ticket coming back unreadable, and the one endpoint that tells you
  which of two problems you have
- **Rep 17** (EXPLAIN): training against inference, in five sentences

**Ten minutes each, plain editor, no AI.** If you cannot do Rep 16 without notes, reread the ten
modes in the kit README rather than rereading the rep. The answer is the difference between nothing
answering and something answering uselessly.

**Level.** Review.

---

## 12. The two files every repository in this course carries

You set these up Monday in Build 2. They are graded under Written and Documentation, Module 3 audits
`LICENSING.md`, and the course rule behind both of them is the same one: **the only way to fail
outright is submitting work you cannot explain.** A log you kept while you worked is how you explain
it later, when you no longer remember.

**No personal data goes into either file, and no personal data goes into any AI tool in this course.**
No names of classmates, no student numbers, no emails, no anything about a real person who did not
publish it themselves.

### `AI_USAGE.md`

Copy this into the root of your repository. Add a session block every time you use an AI tool, while
you are working and not at the end of the week.

```markdown
# AI_USAGE.md

Every work session in which I used an AI tool. Added while I worked, not afterward.
No personal data about any real person goes into any tool, ever.

---

## Session: Week NN, Day, Build 1 or Build 2

**Tool and where it ran.**
Name the tool and say whether it ran on this machine or somewhere else.

**What I asked it for.**
The actual task, in one or two sentences. Paste the prompt if it was short.

**What I used.**
What of the output ended up in my work. Name the file and the lines.

**What I changed.**
What was wrong, unclear, or did not fit, and what I did about it.

**What I rejected, and why.**
What I threw out. This section being empty every time is itself a finding.

**Can I explain every line I kept?**
Yes or no. If no, say which lines and what you did next.

---

## Session: Week NN, Day, Build 1 or Build 2

**Tool and where it ran.**

**What I asked it for.**

**What I used.**

**What I changed.**

**What I rejected, and why.**

**Can I explain every line I kept?**
```

### `LICENSING.md`

Copy this into the root of your repository. Add a row the moment something arrives, not when the
project is graded. Tracing an asset back to its terms a week later is the part that goes wrong.

```markdown
# LICENSING.md

Everything in this repository that is not mine, and where its terms are stated.
If it is not on this page, it is my own work and I can defend that claim.

## Code that is not mine

| What it is | Where it came from | License | Where the terms are stated | What that requires of me |
|---|---|---|---|---|
| example: a 12-line retry loop | a blog post | unstated | nothing on the page | rewrote it myself rather than ship unstated terms |
|  |  |  |  |  |

## Models

| Model | Where it came from | License | Where the terms are stated | Restrictions I have to honour |
|---|---|---|---|---|
|  |  |  |  |  |

## Datasets

| Dataset | Where it came from | License | Where the terms are stated | What it may and may not be used for |
|---|---|---|---|---|
|  |  |  |  |  |

## Media: images, audio, fonts, icons

| Asset | Where it came from | License | Where the terms are stated | Attribution required |
|---|---|---|---|---|
|  |  |  |  |  |

## Anything whose terms I could not find

| What it is | Where I looked | What I decided to do |
|---|---|---|
|  |  |  |

**An unfindable license is a finding, not a blank.** Record the search, then either replace the
asset or state in writing why you are shipping something whose terms nobody can read.
```

**Time.** 15 minutes to set both up. **Level.** Required of everyone.

---

## 13. Side quest

**SQ-20 Explain It to a Seventh Grader**, from
[`../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md).
Unlocks in 145130, one block, difficulty one star.

**Why it belongs in Week 1 rather than Week 3.** The
[Module 1 performance task](../09-project/MCCTC_145130_Project_M01_BenchmarkAndExplainer.md) ends in a
written explainer for an adult. This side quest is the spoken version for a twelve-year-old, and it
is finished when an actual younger person can answer three comprehension questions afterward. Doing
it early tells you in one block which parts of the week you actually understand, which is a much
better thing to find out in Week 1 than in Week 3.

**Level.** Extension.

---

## For the student who is behind

1. The Tuesday lecture note, then the kit README, then get the stand-in answering on 11634.
   **Nothing else in Module 1 matters more in Week 1 than one request going out and one reply coming
   back.**
2. The Tuesday note's worked example 1, the captured reply, read twice. The answer is a string inside
   a fence inside the reply.
3. Gate 1 Reps 02 and 16.
4. The Wednesday lecture note's self-check question 3, written out in full.

## For the student who is ahead

- Every one of the stand-in's ten modes, run on your own machine, with one sentence each on what your
  program saw
- `ask_model.py`'s `read_label`, read line by line, and a written list of what it would do to an
  answer nobody has thought of yet
- The scikit-learn Decision Trees page, disadvantages section
- SQ-20
