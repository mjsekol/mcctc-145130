# Lecture Notes: Extract Valid Information and Cite the Source
## 145130 Applications of AI · Module 1 · Week 2, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W02_ExtractAndCite.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W02_ExtractAndCite.pptx)

If you missed class you can learn this from this file alone.

**Competency 1.2.1:** extract relevant, valid information from materials and cite
sources of information. It carries into every written deliverable in this course,
and this afternoon it carries into the Infographic Autopsy.

---

## Why this exists

You are going to write, this module, a benchmark report and an explainer that
somebody else will act on. Everything in them has to be traceable to something.
That is not a school rule about citations. It is the difference between a
document that can be checked and one that can only be believed.

And there is a specific reason it lands in an AI course. A model produces text
that has the shape of sourced writing without any of the sourcing. It will write
"studies show", "according to industry data", and a precise-looking number, and
none of those came from a study, an industry, or a measurement. **Precision is
not evidence. It is a style.**

---

## The concept in plain language

A claim is traceable when a reader can get from your sentence to the thing that
supports it without asking you. That requires three things, and all three or it
does not count.

**1. The claim is specific enough to be wrong.** "Local models are slower" cannot
be checked. "The local model on station 6 produced 39 tokens per second on
prompt p1" can.

**2. The support is named precisely enough to find.** Not "the documentation".
The document, the section, and what it says. Not "a study". Who, when, what they
measured, how many.

**3. The support actually says what you said it says.** This is the one people
skip, and it is where most errors live. Go and read the sentence you are citing.

### The four kinds of support, ranked

| Support | Example | Strength |
|---|---|---|
| **A run you did** | "39.3 tokens/sec, `runs/bench-a.json`, command in the README" | strongest, because anyone can repeat it |
| **A primary source** | the specification, the license text, the vendor's own documentation page | strong, if you quote what it actually says |
| **A secondary source** | an article describing somebody else's work | weaker, and you should follow it to the primary |
| **A model's answer** | "the assistant said" | **not support at all** |

The last row is the one to internalise. A model's output is a thing to check, not
a thing to cite. If a model tells you something useful, your job is to go and
find where it is actually written, and cite that. If you cannot find it, you have
learned something important about the claim.

---

## Worked example 1: turning an untraceable claim into a traceable one

**Untraceable, from a student draft:**

> "Local AI models are much slower than cloud models, often by a factor of ten."

Nothing here can be checked. Which models. On what hardware. Measuring what.
Ten times what number.

**Traceable version:**

> "On the build machine, with a stand-in server configured to emit 40 tokens with
> 25 ms between them, `bench.py` reported a median total latency of 1335.7 ms and
> 39.3 tokens per second for prompt `p1_short`. The raw run is in
> `runs/bench-a.json`. No real model was available, so this measures the
> instrument and not a model. Numbers from lab hardware will differ and are not
> yet collected."

Longer, and it can be repeated by anyone with the folder. Notice the last two
sentences: **saying what you did not measure is part of the report.** A reader
who finds out later that a number came from a stand-in, when the report did not
say so, stops trusting the rest of it, and they are right to.

---

## Worked example 2: how to check a claim you cannot run

Some claims have no command. Here is the method, in order.

1. **Say what would settle it.** Write the sentence "this would be settled by
   ____". If you cannot finish it, the claim is not about the world.
2. **Find the primary source.** The specification, the law, the license, the
   vendor's own page. Not an article about it.
3. **Read the part that matters, not the headline.** Sources are routinely
   narrower than the claims made about them.
4. **Write down the search that failed.** "I looked for the origin of this figure
   in X and Y and did not find one" is a finding, and it belongs in your report.

Step 4 is the one worth arguing for. **An honest failed search is stronger
evidence than a vague success.** "I could not find where this number comes from"
tells a reader something real. "Studies show" tells them nothing.

---

## Worked example 3: a fabricated citation, and how it gets through

Here is the shape. A model produces a sentence like:

> "According to the Halloran Institute for Applied Computing, 84 percent of
> mid-sized firms now run at least one model on their own hardware."

**The Halloran Institute for Applied Computing does not exist. It was invented
for these notes**, and it is the shape a fabricated citation actually takes:
plausible name, plausible subject, a precise number, and a sentence that reads
exactly like every real citation you have seen.

It gets through for three reasons. It is specific, and specificity reads as
research. It is boring, so nobody has an emotional reason to check it. And
checking it takes real effort, while accepting it takes none.

**How you catch it:** the same way every time. Try to find the source. If the
organisation does not appear anywhere, or appears only in text that reads like
this text, you have your answer. Write down that you looked.

You will meet several of these in the Infographic Autopsy this afternoon.

---

## The wrong version, and why it is tempting

> "Research indicates that AI adoption improves productivity across most
> industries."

Four problems. "Research" names nobody. "Indicates" is doing a job that "shows"
would be held to. "Most industries" cannot be checked. And "productivity" is not
defined, so even a real study could not confirm or deny the sentence as written.

It is tempting because it is true-adjacent, nobody in the room will challenge it,
and it fills a paragraph. It is also exactly what a model produces when asked to
write an introduction, because it is the most likely continuation of that kind of
sentence in what the model was fitted to.

### Write this down

> A citation is a route a reader can walk without you. If they cannot walk it,
> you have decoration.

---

## The habit, in one paragraph

When you write a claim in this course, ask three questions before the sentence is
finished. What exactly am I asserting. What would show it. Where is that thing.
If the third question has no answer, you have two honest choices: weaken the
claim until it matches what you actually know, or go and get the evidence. You do
not have a third choice, and "everyone knows" is not one.

---

## Vocabulary

| Term | What it means |
|---|---|
| **claim** | a statement that could turn out to be false |
| **primary source** | the original document: the spec, the law, the data, the code |
| **secondary source** | something describing a primary source |
| **provenance** | where a piece of information came from |
| **traceable** | a reader can reach the support without asking you |
| **fabricated citation** | a reference to a source that does not exist |
| **falsifiable** | specific enough that some evidence could show it wrong |
| **failed search** | a documented attempt to find a source that found none, which is itself a result |

---

## Self-check

**1.** Rewrite this so it is traceable: "The new wing's 3D printers are much
faster than the old ones."

**2.** A model gives you a helpful fact with a named author and year. You cannot
find the paper anywhere. What do you write in your report?

**3.** Why is "I ran it and here is the output" stronger support than a vendor's
documentation page?

### Answers

**1.** Something like: "Printing the same 40 mm calibration cube at the same layer
height, the printer in room 118 finished in 22 minutes and the older printer in
room 104 finished in 35. Both runs are logged in `print-log.md` with the settings
used." The rewrite names the object, the settings, both numbers, and where the
record is. Without the settings the comparison is not a comparison.

**2.** Write that you could not find it, name where you looked, and do not use
the fact. The sentence belongs in the report: "This claim came from a model and I
could not locate the paper in X or Y, so I have not relied on it." That is a
finding about the claim, and leaving it out to keep the paragraph tidy is the
failure.

**3.** Because a reader can repeat it. Your output is a fact about a specific
system on a specific day, and the command is in the file, so anyone can run it
and get their own. Documentation says what the vendor intends, which is not
always what the installed version does, and it can be out of date, wrong, or
about a different build. Documentation is still worth citing. It is a
different kind of claim: what is supposed to happen, rather than what did.
