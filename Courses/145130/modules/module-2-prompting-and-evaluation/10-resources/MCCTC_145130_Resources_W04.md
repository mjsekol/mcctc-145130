# Additional Resources · Week 4
## 145130 Applications of AI · Module 2 · Week 4
### Topics: the prompt is the whole input, the five elements, changing one thing at a time, and output your program can parse

Links marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed live and must
be clicked before it is assigned. Where a resource is named with no link at all, that is deliberate: a
name you can search for is worth more than a URL that turns out to be dead in front of a class.

**Most of the strongest resources this week are inside this repository.** That is not a shortcut. The
public writing on prompting turns over fast, much of it is marketing for a product you cannot use at
16, and almost all of it assumes a commercial API key. The lecture notes, the toolkit, and the
reference runs were built for the model you actually have.

**No resource this week asks you to put personal data into a prompt.** Not a name, not a schedule, not
a grade. `ask.py` records your prompt verbatim into a file you commit. Whatever you type gets
published to your repository. The course uses the invented names Ava Ruiz and Kai Mendoza.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The four Week 4 lecture notes | Mon-Thu | On-level | 20 min each |
| 2 | The Prompt Toolkit README | Before Mon | On-level | 10 min |
| 3 | The `/stub/parse` element checker | Tue-Wed | On-level | 15 min |
| 4 | Official docs: `json` module | Thu | On-level | 15 min |
| 5 | The JSON format, json.org | Thu | Remediation | 10 min |
| 6 | Official docs: `argparse` | Mon-Tue | On-level | 15 min |
| 7 | Automate the Boring Stuff, the JSON material | Thu | Remediation | 30 min |
| 8 | The reference Prompt Autopsy, five prompts and five runs | Tue-Thu | On-level | 20 min |
| 9 | 145060 Lab U0-02 Infographic Autopsy | Thu-Fri | Review | 25 min |
| 10 | SQ-18 Prompt Ablation | Wed onward | Extension | 1 block |
| 11 | Gate 1 rep bank, Reps 01-15 | Daily | Review | 10 min each |
| 12 | The self-checks in the Week 4 notes | Before Fri | Review | 20 min |
| 13 | A free video on prompt structure | Any | Remediation | under 20 min |
| 14 | Your model runtime and its structured-output documentation | Thu | Extension | 25 min |
| 15 | Is prompt engineering a real job, both sides | Fri | Extension | 10 min |

---

## 1. Primary reading

**The four Week 4 lecture notes**, in the order they are taught:

- `../03-lecture-notes/MCCTC_145130_Notes_ThePromptIsTheWholeInput.md` (Monday)
- `../03-lecture-notes/MCCTC_145130_Notes_FiveElementsOfAPrompt.md` (Tuesday)
- `../03-lecture-notes/MCCTC_145130_Notes_ChangeOneThingAtATime.md` (Wednesday)
- `../03-lecture-notes/MCCTC_145130_Notes_OutputYourProgramCanParse.md` (Thursday)

**Why this one.** Each note carries three worked examples with the actual output printed, produced by
the same stub that runs on your machine. You can rerun every one of them and get the same text back.
No book or video in this list can say that.

**Assign a question, not the page.** From the Monday notes, worked example 3: *the reply to the
question the model could not possibly answer still contains specifics. Name three of them, and say
where each one came from.* The answer is that they came from nowhere, which is the point of the whole
module.

**Time.** About 20 minutes each. **Level.** On-level.

---

## 2. The Prompt Toolkit README

`../05-labs/prompt-toolkit/README.md`

**Why this one.** It takes ten minutes and it prevents the two failures that cost the most class time:
a comparison built from memory, and a lab that cannot start because nothing is listening on the port.

Read three sections closely before Monday. The failure-mode table with seven stub modes, the exit-code
table with codes 0, 2, 3, 4, 5, and 6, and the section called "If it breaks."

**Assign a question:** *Three of the seven failure modes return HTTP 200. Name them, and say why a
program that checks only the status code will treat all three as success.*

**Time.** 10 minutes. **Level.** On-level.

---

## 3. The `/stub/parse` element checker

In the same README, the section called "Seeing what the stub read in your prompt."

**Why this one.** This is the interactive practice for the week, and it is the one that changes how
students revise. You paste your prompt and the machine prints which elements it detected: role,
audience, format, word cap, step count, whether an example is present, whether sources were supplied.

**When a revision changes nothing, check this first.** Most of the time the element you thought you
added is not the element the machine saw. That endpoint does not exist on a real server. It is a
teaching instrument, and Week 5 will take it away by asking you questions no machine can answer.

**Assign a question:** *Write a prompt you believe contains all five elements. Run it through
`/stub/parse`. Which element did the machine not see, and what wording change makes it see it?*

**Time.** 15 minutes. **Level.** On-level.

---

## 4. The `json` module

`https://docs.python.org/3/library/json.html` · **Confident.**

**Why this one.** Thursday's deliberate error is `json.loads` dying on column 1 of a reply that looks
like JSON. This is the page that defines what it will and will not accept.

**Assign a question:** *Find what `json.loads` raises when the text is not valid JSON. What is the
exception class, and what two pieces of location information does it carry?*

**Time.** 15 minutes. **Level.** On-level.

---

## 5. The JSON format itself

`https://www.json.org/` · **Confident.**

**Why this one.** The grammar diagrams on the front page show exactly where quotes, commas, and
brackets are allowed. A student who keeps producing single-quoted keys or a trailing comma sees in
thirty seconds that the grammar has no place for them.

It also settles a Thursday argument fast. A reply wrapped in "Here are some thoughts" is not malformed
JSON. It is not JSON at all, and the diagram shows why.

**Time.** 10 minutes. **Level.** Remediation.

---

## 6. The `argparse` module

`https://docs.python.org/3/library/argparse.html` · **Confident.**

**Why this one.** You will type `ask.py --prompt-file`, `--label`, `--endpoint`, `--timeout`, and
`--show` every day for three weeks. Fifteen minutes on how those flags are declared turns the toolkit
from a magic box into a program you could have written.

**Assign a question:** *Open `../05-labs/prompt-toolkit/ask.py` and find where the arguments are
declared. Which ones carry a default, and what happens if you leave `--label` off?*

**Time.** 15 minutes. **Level.** On-level.

---

## 7. Automate the Boring Stuff with Python

`https://automatetheboringstuff.com/` · **Confident** for the site. **[VERIFY]** the chapter number
and path for the JSON material in the current edition.

**Why this one.** It is free to read online, and its treatment of `json.loads` and `json.dumps` is the
clearest short explanation available to a student who has not met JSON before Thursday.

**Skip for now:** any section that calls a web API with a key. This course never requires a key, and
every model you use runs on a machine in this building.

**Time.** 30 minutes. **Level.** Remediation.

---

## 8. The reference Prompt Autopsy

`../09-project/reference-implementation/prompt-autopsy/`

Five prompt files in `prompts/`, five recorded runs in `runs/`, and a summary in `runs/run_log.md`.

**Why this one.** It is a finished version of the thing you are being asked to build, and it is worth
reading before you write your own prompt 1. Look at what "materially different" means in practice.
`p1_bare.txt` is six words, `p5_grounded_sourced.txt` is eighty-one, and the five files differ in
which element was added rather than in wording.

**Assign a question:** *Open `run_log.md`. Between `p3_role_audience` and `p4_format_constrained` the
prompt got shorter and the reply got much shorter. Predict which element did that, then open the two
prompt files and check.*

**Do not copy the reference task.** The most common failure in this project is a task too small to be
worth five prompts. The second most common is a borrowed task the student cannot defend in the demo.

**Time.** 20 minutes. **Level.** On-level.

---

## 9. The lab you already did as a junior

`../../../../145060/units/unit-00-onboarding/05-labs/MCCTC_145060_Lab_U00-02_InfographicAutopsy.md`

**Why this one.** You met the five evaluation criteria in Unit 0 of 145060, on a planted infographic.
Monday of Week 5 opens on the same distinction you argued about then: Validity is a wrong claim about
a real thing, and a Hallucination invents the thing. Rereading that criteria table on Thursday of Week
4 means you arrive Monday with the vocabulary already loaded.

The artifact in that lab was constructed for the class. Every error in it was planted and every one is
checkable. Read the note at the top that says so, because Week 5 asks you to hold the same line about
fabricated citations that you produce yourselves.

**Time.** 25 minutes. **Level.** Review.

---

## 10. Side quest

**SQ-18 Prompt Ablation** unlocks Wednesday of Week 4. One block, difficulty two stars.
Catalog entry: `../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.
Bundle: `../../../../Misc/side-quests/SQ-18-Prompt-Ablation/`.

Take one prompt that works. Remove one element at a time, run it again, and record what changes. Done
when you have a table of at least eight variants with results and a conclusion about which element was
doing the most work. SQ-18 ships its own copy of `stub_model_server.py`, so the bundle runs on its own
with nothing installed and nothing leaving your machine.

This is the best hour available on Wednesday's skill, and the catalog is honest that most students are
surprised by the result.

**No other Module 2 side quest unlocks this week.** SQ-19 The Bias Audit unlocks Thursday of Week 5.

---

## 11. Gate 1 reps

The Module 2 rep bank, `MCCTC_145130_Gate1_PromptingAndEvaluation.md`, lives in `06-gate1-reps/` and
is assigned by your instructor from the instructor copy. Week 4 works through Reps 01 to 15, two or
three a day.

The three worth repeating on your own time are Rep 09, which is three changes at once and what you can
conclude from it, Rep 11, and Rep 12. Rep 09 returns on Wednesday of Week 5 as review because it is
the rep most students fail twice.

**Level.** Review.

---

## 12. The self-checks you already have

Each of the four Week 4 lecture notes ends with three self-check questions and worked answers. That is
twelve questions. **Before Friday you should be able to answer all twelve without reading the answers
first.**

The three that predict Friday's Gate 2 performance best:

- Five Elements, question 2: your prompt has all five elements and the reply is still wrong about your
  school
- Change One Thing, question 3: why a run that produced no change is worth recording
- Output Your Program Can Parse, question 1: HTTP 200, `json.loads` succeeded, and the reply is still
  unusable

**Time.** 20 minutes. **Level.** Review.

---

## 13. A free video

**[VERIFY] No specific video is linked here, and that is honesty rather than laziness.** Prompting
videos go stale inside a year, most of them demonstrate a commercial product this course does not use,
and a link that is dead on Monday morning costs a period.

**Search for a video by this description:** one that names the parts of a prompt and shows the same
task run with and without each part. Twenty minutes or under.

**Vet it yourself first, against three tests.** Does it show the output, or only talk about it. Does
it change one thing at a time, or several at once. Does it require an account, a key, or a paid
product. A video that fails the third test is unusable here whatever its quality.

`https://py4e.com/` · **Confident** for the site, which publishes free lecture video. It carries no
prompting material, so use it only for a student who needs the Python behind `ask.py` rather than the
prompting.

**Level.** Remediation.

---

## 14. The industry connection for this week

**Named with no URL, on purpose.** Read the structured-output documentation for whichever model
runtime is installed on the lab machines. Search for it by that runtime name plus the words
"structured outputs" or "JSON mode". **[VERIFY]** whatever you find before class.

**Why this one.** Thursday teaches that "return JSON" is an invitation and "return only JSON, no other
text" is an instruction. Production systems attacked the same problem from the other side, by
constraining what the model is allowed to emit so the output cannot be anything but valid JSON.
Reading how a real runtime does that shows you the thing you fought with on Thursday is a known
engineering problem with a known engineering answer, and that the answer still says nothing about
whether the content is true.

**Assign a question:** *A runtime that guarantees valid JSON has solved which of Thursday's failure
modes, and which does it leave untouched?* It removes `malformed` and does nothing at all for
`not_done`, `missing_response`, or `empty_response`.

**Time.** 25 minutes. **Level.** Extension.

---

## 15. The contested question

**Is prompt engineering a real job?** The strongest version of each side is written out in
`../00-CRASH-COURSE.md`, section 7, question 3.

The case for: people are paid to build and maintain the prompts inside production systems, and
evaluating model output is a growing role. The case against: the specific tricks turn over fast,
models get better at ignoring a bad prompt, and the standalone job title is already less common than
it was.

What holds either way is the skill underneath, which is specifying a task precisely and evaluating a
result against that specification. That skill predates these models and will outlast them.

**Read both sides before you argue either one.** Anybody who can state only one of them has an opinion
rather than a position.

**Time.** 10 minutes. **Level.** Extension.

---

## For the student who is behind

1. The Prompt Toolkit README, all of it, and get `python test_toolkit.py` to print `Ran 29 tests` and
   `OK`. **Nothing else in this module runs until that passes.**
2. Monday's lecture notes, worked example 1, run by hand on your own machine
3. The json.org diagrams, before Thursday
4. Gate 1 Reps 01, 04, and 07, in that order

## For the student who is ahead

- SQ-18 Prompt Ablation, starting Wednesday
- `/stub/parse` on all five of your autopsy prompts, and find one element the machine did not see
- Write a retry that sends a stricter prompt after a parse failure, then prove it works against
  `--mode malformed`
- The structured-output documentation in resource 14, and bring the answer to its assigned question
