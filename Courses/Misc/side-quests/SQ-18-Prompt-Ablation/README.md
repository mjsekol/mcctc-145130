# SQ-18 · Prompt Ablation
## Unlocks: 145130, Week 4 Wednesday · Time: one block · Difficulty: ★★
### Competencies: 2.14.3, 2.14.4

---

## The quest

Take one prompt that works. **Remove one element at a time**, run it again, and
record what changes.

That is the opposite of what you have been doing. Adding an element tells you what
it contributes on top of nothing. **Removing it tells you what the whole prompt
would lose without it**, which is the question you actually have when somebody
asks whether a line in a production prompt is earning its place.

**Done when** you have a table of at least eight variants with results, and a
conclusion about which element was doing the most work.

**Most students are surprised.** You are going to find elements you were sure
mattered and that do nothing, and you should expect that rather than assume you
made a mistake.

---

## What is in this folder

| File | What it is |
|---|---|
| `base_prompt.txt` | one prompt that works, with each element on a tagged line |
| `ablate.py` | the starter. It runs one variant, which is not an experiment |
| `stub_model_server.py` | a stand-in model, so this runs with nothing installed |
| `check_quest.py` | checks your work against the "done when" list |

This copy of `stub_model_server.py` is the same file as the one in 145130's
`05-labs/prompt-toolkit/`. It is duplicated here so the quest works on its own.

---

## The prompt you are taking apart

`base_prompt.txt` holds one element per line, each line tagged:

```
[ROLE] You are the club's equipment manager and you have run the Friday equipment checkout for three years.
[TASK] Write the instructions a brand new club member needs in order to run the Friday equipment checkout by themselves, with nobody else in the room to ask.
[CONTEXT] The sign-out sheet is taped inside the door of Room 214 and the cameras live in the cabinet under the window.
[FORMAT] Give me 5 steps in a numbered list.
[CONSTRAINT] Keep it under 60 words.
[CONSTRAINT] Do not add an introduction or a closing paragraph.
```

**The tags are for you, not for the model.** `ablate.py` strips them before
sending. They exist so that a program can take one line out and put the rest back
together.

**Use your own prompt if you have one.** Tag it the same way, pass it with
`--prompt-file`, and say in your findings which prompt you used.

---

## What you build

`build_variants()` in `ablate.py`, which currently returns one variant.

It has to produce:

1. **The control.** The whole prompt, labelled `full`.
2. **One variant per element**, with that element removed, labelled `no_role`,
   `no_task`, and so on.
3. **At least two variants with two elements removed**, labelled `no_a_no_b`.

With six elements that is nine variants.

**Why the double removals matter, and this is the part that makes the quest
worth doing.** A design where you only ever remove one thing cannot see an
**interaction**: a case where removing two elements together does something that
neither removal does alone. Those exist, they are common, and you will probably
find one here.

---

## Run it

```
python ablate.py
```

Against a real local model:

```
python ablate.py --endpoint http://127.0.0.1:11434 --model <your model name>
```

With no `--endpoint`, `ablate.py` starts the bundled stub on a free port and stops
it afterwards. **Nothing needs to be running first and nothing leaves your
machine.**

Every run is saved to `results/<label>.json` with its prompt, so you can read any
reply again without rerunning anything.

---

## Then write `findings.md`

**The table, pasted from what `ablate.py` printed.** Not retyped.

**A row-by-row reading.** For each variant, one line: what was removed and what
moved. **Including the rows where nothing moved.** Those are the interesting ones
and the ones people delete.

**Your conclusion**, under a heading with the word "conclusion" in it. It answers
one question: **which element was doing the most work, and what is your evidence?**

**And the scope.** Not "roles do not matter." Something like: on this task,
against this model, with the format and the constraints still present, removing
the role changed nothing measurable in length, shape, or hedging.

**The scope of the claim has to match the scope of the evidence.** That sentence
is the whole difference between a measurement and a story, and it is what this
quest is really assessing.

---

## Check your work

```
python check_quest.py
```

It checks the mechanical half: the variant count, the labels, the recorded runs,
and whether `findings.md` has a table and a conclusion. **It cannot tell you
whether your conclusion is any good**, and it says so when it passes.

---

## If it breaks

**`No tagged lines found in base_prompt.txt`**
Every element line starts with a tag in square brackets, in capitals, like
`[ROLE]`. A line without one is ignored, which is how you can put comments in the
file.

**`nothing is listening at ...`**
You passed `--endpoint` and nothing is there. Drop the flag and let it start the
bundled stub.

**Two variants have the same prompt.**
You removed the same element twice under different labels. `check_quest.py` catches
this, and the usual cause is building the double removals from the single-removal
list rather than from the element list.

**Every variant gives the same reply.**
Check that `assemble()` is being called on a list with an element actually
removed. Print one variant's prompt and read it.

---

## Two rules that do not move

**Everything runs on your own machine.** No account, no key, nothing leaves.

**No personal data in any prompt.** `ablate.py` writes your prompt into
`results/` and you will commit it. Invented names only.

---

## Where this goes next

The Prompt Autopsy performance task asks for five materially different prompts and
a documented comparison. **This quest is the technique that makes that project
honest**, and a student who does SQ-18 first usually produces a better autopsy in
less time.

**SQ-19 The Bias Audit** is the same discipline pointed at a different question:
keep the prompt identical and vary one detail about the person. It unlocks in Week
5 and the rule there is the one worth carrying: a test that can only come out one
way is not a test.
