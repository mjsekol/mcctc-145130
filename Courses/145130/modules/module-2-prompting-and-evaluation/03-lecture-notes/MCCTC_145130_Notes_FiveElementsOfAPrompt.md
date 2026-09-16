# The Five Elements of a Prompt
## 145130 Applications of AI · Module 2 · Week 4, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W04_FiveElements.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W04_FiveElements.pptx)

**Competencies:** 2.14.3 (write and revise a prompt to generate the desired
response). Supporting: 1.2.5 (communicate for an intended audience and purpose).

---

## Why this exists

Yesterday you learned that the model sees only the text you sent. That leaves an
obvious question: which text?

"Write a better prompt" is useless advice because it does not say what to change.
This lesson gives you five named things to change, so that "revise your prompt"
becomes a specific instruction instead of a vibe.

**These five names are the vocabulary for the rest of the module.** Every lab,
every Gate 2, and the module exit assessment uses them.

---

## The five elements

| Element | The question it answers | Example |
|---|---|---|
| **Role** | Who is talking | "You are the club's equipment manager." |
| **Task** | What finished looks like | "So a new member can run checkout alone, with nobody to ask." |
| **Context** | What the model cannot know | "The sign-out sheet is taped inside the door of Room 214." |
| **Format** | What shape the answer takes | "Exactly 5 steps, numbered." |
| **Constraints** | What it may not do | "Under 60 words. No introduction." |

Each one does a different job. None of them is "make it better."

---

## What each element actually does

**Role narrows the voice, not the facts.** "You are a hospital pharmacist"
produces text that reads like a pharmacist wrote it. It does not add pharmacy
knowledge that was not already there, and it does not make the pharmacy claims
true. Students consistently overrate this element because it is the most fun to
write.

**Task is the one people skip and the one that does the most work.** Not "write
about checkout" but "so that a new member can run checkout alone with nobody to
ask." The second version states a finish line. Without a finish line the model
has no reason to stop, which is where padding comes from.

**Context is facts the model cannot have.** Your room, your sheet, your deadline,
your data. This is the element that separates a generic answer from one about
your situation, and there is no substitute for it. You cannot get context by
asking more politely.

**Format is the element with the most visible effect and the one you add last.**
Prose becomes a numbered list becomes JSON. It changes the shape of the output
completely, and it is what makes an output usable by a program or scannable by a
person in a hurry.

**Constraints are the negative space.** Under 60 words. No introduction. Do not
recommend anything that costs money. Do not use any source I did not give you.
Constraints are where most of the safety in a production prompt lives.

---

## Worked example 1 · Element by element, on one task

The task all week: **produce the instructions a new club member needs to run the
Friday equipment checkout by themselves.**

Five prompt files live in
`../../09-project/reference-implementation/prompt-autopsy/prompts/`. Each one
adds elements to the one before it.

```
cd ../../09-project/reference-implementation/prompt-autopsy
python run_all.py
```

```
| Label | Prompt words | Reply words | Seconds | Shape | Valid JSON | List items | Sources claimed | Hedges |
|---|---|---|---|---|---|---|---|---|
| p1_bare | 6 | 110 | 0.02 | prose | no | 0 | 0 | 5 |
| p2_task | 48 | 65 | 0.00 | prose | no | 0 | 0 | 2 |
| p3_role_audience | 75 | 105 | 0.00 | prose | no | 0 | 0 | 2 |
| p4_format_constrained | 69 | 54 | 0.00 | numbered | no | 5 | 0 | 0 |
| p5_grounded_sourced | 81 | 84 | 0.01 | numbered | no | 5 | 3 | 0 |
```

| Prompt | What it adds | What changed |
|---|---|---|
| p1 | nothing. Six words | 110 words, 5 hedges |
| p2 | Task | 65 words, 2 hedges. **Longer prompt, shorter reply** |
| p3 | Role and audience | Reply adopts the voice, adds a safety line for a beginner |
| p4 | Format, count, word cap, no introduction | Prose becomes 5 numbered steps. Hedges drop to 0 |
| p5 | Context (supplied sources) and a refusal route | Cites the sources you gave it and nothing else |

**The line to notice is p1 to p2.** The prompt got eight times longer and the
reply got shorter. Stating what finished looks like removed the padding. Students
almost always predict the opposite.

---

## Worked example 2 · Role changes the voice and not the content

```
python ask.py --prompt "Explain the Friday equipment checkout." --label norole --show
python ask.py --prompt "You are the club's equipment manager. Explain the Friday equipment checkout." --label role --show
```

```
[norole] 5 prompt words ... 110 reply words
Here are some thoughts on the Friday equipment checkout.

[role] 11 prompt words ... 95 reply words
As a club's equipment manager, here is how I would handle the Friday equipment
checkout.
```

**The six procedure steps underneath are identical, word for word.** What changed
is the framing sentence and the amount of padding: the role dropped the hedging
from four sentences to two, which is the whole 15-word difference.

If you were hoping the role would make the procedure more accurate, look at the
procedure. It did not change at all.

This matters for Gate 2 and for the exam. A role is a real element with a real
effect, and the effect is on voice, confidence, and framing. Claiming it improves
accuracy is a claim you cannot support from any run you have made.

---

## Worked example 3 · Checking that the machine saw what you added

When a revision produces no change, the first thing to check is whether the
element arrived in a form the machine can act on:

```
python -c "import urllib.request,urllib.parse; q=urllib.parse.urlencode({'prompt':'You are the club equipment manager. Give me 5 steps in a numbered list, under 60 words.'}); print(urllib.request.urlopen('http://127.0.0.1:11434/stub/parse?'+q).read().decode())"
```

```
{"role": "club equipment manager", "audience": null, "format": "numbered",
 "json_only": false, "json_keys": [], "word_cap": 60, "step_count": 5, ...}
```

That endpoint exists only on the stub. A real model will not tell you what it
noticed, and you will be back to changing one thing at a time and watching the
output, which is tomorrow's lesson.

---

## The wrong version, and why it is tempting

Here is the revision students write first, every year:

```
Please write a really good, detailed, professional explanation of the equipment
checkout process. Make it accurate and make sure it is clear. Thank you.
```

Count the elements. **Role: none. Task: none, because "really good" is not a
finish line. Context: none. Format: none. Constraints: none.**

Every word in it is about quality in general, and none of it names a thing to
change. Run it and compare it to p1:

```
[adjectives] 24 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\adjectives.json
```

```
[p1_bare] 6 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\p1_bare.json
```

**Twenty-four words of adjectives produced a reply the same length as six words of
nothing.** The same six sentences of content and the same four hedging sentences,
in a different order.

Read the two replies side by side. Nothing got more specific. Nothing got shorter.
No hedging went away. The order of two sentences moved, and there is no element
you can point at to explain why it moved, which means it is not a result you can
use.

**Eighteen extra words about quality bought a reshuffle**, because none of them was
an element.

**Why it is tempting.** It feels like effort. It is longer, it is polite, and it
uses serious words. Effort spent on adjectives is effort that did not go into
the five elements, and the machine has no way to act on "professional" except to
produce text that sounds professional.

**The other tempting mistake:** adding three elements at once, getting a much
better reply, and calling that a finding. It is a better prompt. It is not a
finding, because you cannot say which of the three did it. That is tomorrow.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Role** | An instruction about who the speaker is |
| **Task** | A statement of what finished looks like |
| **Context** | Facts supplied in the prompt that the model could not otherwise have |
| **Format** | The requested shape of the output: prose, list, table, JSON |
| **Constraint** | A limit on the output: length, exclusions, what it may not use |
| **Grounding** | Supplying the actual source material and restricting the answer to it |
| **Hedging** | Padding that states no position: "ultimately, it depends on your needs" |

---

## Self-check

**1.** Classify each fragment as Role, Task, Context, Format, or Constraint.
(a) "for a ninth grader on their first Friday" (b) "under 60 words"
(c) "the cameras live in the cabinet under the window" (d) "you are the club
treasurer" (e) "so the club stops losing tripods"

<details><summary>Answer</summary>

(a) Task, specifically the audience half of it. Accept Role with an argument,
because "write for a ninth grader" and "write as a ninth grader" are different
instructions and students often mean the first. Say which you meant.
(b) Constraint. (c) Context. (d) Role. (e) Task: it names what finished looks
like.
</details>

**2.** Your prompt has all five elements and the reply is still wrong about your
school's procedure. Which element do you fix, and why not the others?

<details><summary>Answer</summary>

**Context.** Being wrong about your procedure means the model did not have your
procedure, and no amount of role, format, or constraint supplies a fact.

The trap is reaching for Constraints and writing "do not make anything up." That
instruction changes the tone towards caution and does not put your procedure in
the box. Only Context does that.
</details>

**3.** Which element usually produces the biggest visible change in the output,
and which one do people add last? Why is that combination a problem?

<details><summary>Answer</summary>

**Format produces the biggest visible change and it is added last.**

It is a problem because people spend their revisions on Role and adjectives,
conclude that prompting does not do much, and never reach the element that would
have changed the output the most. Add Format early and you find out quickly
whether the content is any good, because a five-item list is much harder to hide
padding in than a paragraph.
</details>
