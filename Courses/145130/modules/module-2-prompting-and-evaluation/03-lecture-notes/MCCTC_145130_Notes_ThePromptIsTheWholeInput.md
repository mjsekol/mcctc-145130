# The Prompt Is the Whole Input
## 145130 Applications of AI · Module 2 · Week 4, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W04_ThePromptIsEverything.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W04_ThePromptIsEverything.pptx)

**Competencies:** 2.14.3 (write and revise a prompt to generate the desired
response). Supporting: 2.14.6 (critically analyze scenarios involving AI usage).

---

## Why this comes first

You have been typing into chat boxes for years. That experience taught you a
habit: keep rephrasing until something looks right.

The habit works well enough that you have never had to know what is actually
happening, and it breaks the moment you need to explain why one version worked.
This week you will be asked to explain it. So before anything else, you need to
know what the machine on the other end can see.

**It can see exactly one thing: the text you sent.** Nothing else.

---

## The concept in plain language

A language model takes a sequence of text and predicts what text comes next. It
does that over and over until it decides it is finished. That is the whole
mechanism.

What it predicts from is called the **context**: everything it has been handed
this time, plus everything it has produced so far. When your program sends a
prompt and gets a reply, the context is your prompt. When you send a second
message in a chat interface, the interface quietly resends the earlier messages
too, which is why it feels like memory. It is not memory. It is resending.

Four things follow, and they explain most of what you will see this module.

**1. It does not know anything about you or your school.** It has never seen
Room 214, your club, your teacher, or your assignment. If your prompt does not
say it, the model does not have it.

**2. It does not look anything up.** There is no search step unless somebody
built one. A model asked for today's bus schedule produces text shaped like a
bus schedule.

**3. It fills gaps with what is typical.** Ask about equipment checkout without
saying anything about your equipment checkout, and it produces the checkout that
is most common across everything it was trained on. That answer can be useful. It
is not about you.

**4. Nothing in the process checks whether the output is true.** Producing a true
sentence and producing a false one are the same operation. This is the sentence
to carry through the whole module: **it is not lying to you, because lying
requires knowing.**

---

## Worked example 1 · Six words in, a hundred and ten out

Start the stub in a second terminal, then:

```
python ask.py --prompt "How do you do equipment checkout?" --label demo1 --show
```

```
[demo1] 6 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\demo1.json
------------------------------------------------------------
Here are some thoughts on the Friday equipment checkout.

Open the checkout sheet before anyone lines up. Match the serial number on the
case to the number on the sheet. Write the borrower's grade level, not their
schedule. Photograph any damage before the item leaves the room. Set the return
slot to the next school day, first period. Put anything with a missing part on
the repair shelf instead.

It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule. Ultimately, the right approach
depends on your specific needs and goals. Studies have shown that small changes
can produce meaningful improvements.
------------------------------------------------------------
```

Read the first paragraph again. It named a checkout sheet, a serial number, a
repair shelf, and a return slot.

**None of those came from you.** You wrote six words and none of them was
"sheet." Every specific detail in that reply is a detail that checkout
procedures usually have, which is a different claim from a detail your checkout
has.

Now read the last paragraph. Four sentences that say nothing. That padding is
what a model produces when nothing in the prompt said what finished looks like,
so it keeps going until it runs out of plausible continuation.

---

## Worked example 2 · Put the facts it cannot know into the box

```
python ask.py --prompt "The Media Club checkout sheet is taped inside the door of Room 214, and the cameras live in the cabinet under the window. How do you run checkout?" --label demo2 --show
```

```
[demo2] 28 prompt words to http://127.0.0.1:11434
  59 reply words in 0.02s, recorded in runs\demo2.json
------------------------------------------------------------
Here are some thoughts on the Friday equipment checkout.

Open the checkout sheet before anyone lines up. Match the serial number on the
case to the number on the sheet. Photograph any damage before the item leaves
the room.

It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule.
------------------------------------------------------------
```

Compare the two runs. 110 words became 59. The generic material about return
slots and repair shelves is gone, and what remains is the part that connects to
the sheet, the case, and the room you mentioned.

**Context did not add knowledge. It narrowed the target.** The reply moved
towards the material you supplied and away from the material you did not.

**Against the stub that narrowing is all you see.** A real model will usually go
further and quote your door and your cabinet back at you. That difference is on
the confirmation list in the crash course, and you should watch for it the first
time this runs against the lab's local model.

---

## Worked example 3 · Ask it something it cannot possibly have

```
python ask.py --prompt "What time does the late bus leave from the Advanced Technology Wing on Thursday?" --label demo3 --show
```

```
[demo3] 14 prompt words to http://127.0.0.1:11434
  93 reply words in 0.02s, recorded in runs\demo3.json
------------------------------------------------------------
Here are some thoughts on the task you described.

Start by writing down what finished looks like. Write down what you decided and
why. Name the one thing that would make this fail. Decide who reads the result
before you decide its shape. Check the part you are least sure about first.

It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule. Ultimately, the right approach
depends on your specific needs and goals. Studies have shown that small changes
can produce meaningful improvements.
------------------------------------------------------------
```

Read what did not happen. There is no error. There is no "I have no way to know
that." There is no question back to you. There are ninety-three confident words
about a bus, containing no information about any bus.

**There is no version of this system that could know that time.** It has no
timetable, no network call, and no mechanism for noticing that it has nothing to
work from. So it produced the most plausible continuation it had, which in this
case is generic advice.

A real local model will usually go one step worse than the stub here and invent a
specific time, because a specific time is the shape of an answer to a question
like this. That is the version to watch for, and it is the one that catches
careful people: confident, specific, about a real place, and wrong.

---

## The wrong version, and the exact error

Here is the mistake almost everybody makes in their first week of building with a
model. You write:

```
python ask.py --prompt "Use the checkout file I showed you earlier." --label wrong --show
```

There is no earlier. There is no file. Each call starts with an empty context
that contains only what you sent this time.

The stub answers anyway, which is the part that hurts:

```
[wrong] 8 prompt words to http://127.0.0.1:11434
  110 reply words in 0.03s, recorded in runs\wrong.json
------------------------------------------------------------
Here are some thoughts on the Friday equipment checkout.

Open the checkout sheet before anyone lines up. Match the serial number on the
case to the number on the sheet. Write the borrower's grade level, not their
schedule. Photograph any damage before the item leaves the room. Set the return
slot to the next school day, first period. Put anything with a missing part on
the repair shelf instead.
...
```

You do not get `Error: no previous conversation`. You get a hundred and ten words
about a file that was never sent, identical to what the six-word prompt produced,
because both prompts contained the same amount of information about your file,
which is none.

**The failure has no error message.** This is the module's running thread and you
will meet it eleven more times:

> **The dangerous outputs are the ones that look finished.**

**Why the wrong version is tempting.** Chat interfaces resend the history for you,
so "earlier" works there. That builds a belief that the model remembers. The
moment you call the model from a program, the interface is gone and so is the
resending, and the belief is still there.

---

## What actually gets sent

Look at a recorded run:

```
python -c "import json; r=json.load(open('runs/demo1.json',encoding='utf-8')); print(json.dumps({k:r[k] for k in ['model','prompt','prompt_words','response_words']}, indent=2))"
```

The `prompt` field is the entire input. There is no other field carrying
anything about you.

`ask.py` records your prompt verbatim into a file you commit. **That is why no
personal data goes into a prompt file.** Not a name, not an ID, not a grade, not
a schedule. Use invented names. This course uses Ava Ruiz and Kai Mendoza.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Prompt** | The entire text sent to the model on one call |
| **Context** | Everything the model can see: the prompt, plus what it has produced so far |
| **Context window** | The maximum amount of text the model can hold at once, measured in tokens |
| **Token** | The chunk a model actually works in. Roughly a short word or a piece of one |
| **Inference** | One run of the model, turning a context into output |
| **Grounding** | Putting the real source material into the prompt so the answer comes from it |
| **Endpoint** | The address your program sends the prompt to. Here it is your own machine |

---

## Self-check

**1.** You ask a model "what is our school's absence policy?" and get a detailed
four-paragraph answer. What do you now know about your school's absence policy?

<details><summary>Answer</summary>

Nothing. You know what an absence policy usually looks like across the text the
model was trained on. Unless your school's policy was in the prompt, no part of
that reply is evidence about your school, however specific it sounds.
</details>

**2.** A classmate says "I told it to be accurate, so it should be more
accurate now." What is wrong with that, in one sentence?

<details><summary>Answer</summary>

There is no accuracy switch to turn on. "Be accurate" is more text in the
context, and text that follows an instruction to be accurate tends to be more
hedged and more cautious in tone, which is a change in style rather than a change
in whether the claims are true.

Worth noticing: the instruction is not useless. It can make the model more
willing to say it is unsure. It cannot make the model check anything.
</details>

**3.** Your program calls the model twice: once asking for a list of clubs, once
asking it to pick the best one from "that list." The second call returns a
confident pick that is not on your list. Why, and what is the fix?

<details><summary>Answer</summary>

**Why:** the second call had no list. Each call starts fresh, so "that list" was
empty context and the model produced a plausible club name from nothing.

**The fix:** paste the actual list into the second prompt. If you want the model
to work with something, the something has to be in the prompt. That is what
grounding means, and it is Week 5 Wednesday.
</details>
