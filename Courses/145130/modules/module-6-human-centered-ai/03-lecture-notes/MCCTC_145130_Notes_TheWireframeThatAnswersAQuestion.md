# The wireframe that answers a question
## 145130 Applications of AI · Module 6 · Week 17, Monday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W17_TheWireframeThatAnswersAQuestion.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W17_TheWireframeThatAnswersAQuestion.md --export pptx
```

**Competencies 2.15.3**, design user tasks and evaluate results through wireframe
testing, and **7.3.1**, select the media elements to be used: sound, video,
graphics, text, animation.

---

## Why this exists

You have findings. Now you change the thing.

**The failure mode here is not laziness. It is enthusiasm.** You have been wanting
to change three things about your program for two weeks, none of them came up in a
single session, and you are about to change them anyway and call it
evidence-driven design.

That is the exit criterion for this module, word for word: **change your own
design because a user struggled, not because you preferred it.** Preferring things
is allowed. Calling a preference evidence is not.

---

## The one idea

**A wireframe is a question with a drawing attached.**

Every change carries four lines, and the third one is the one nobody writes:

```
The observation:  what you watched, with session numbers
The change:       what moves, in one sentence
The prediction:   what a participant will do differently
How I will know:  the re-test, and what you will count
```

**The prediction is the part that can be wrong**, which is what makes the whole
thing a question rather than a decoration.

---

## Worked example 1 · a change with all four lines

A text wireframe. Boxes and words, in a fenced block, committed as a file. This is
the version the build machine can hold, and paper is equally valid.

**Version 1, what the program prints today:**

```
+--------------------------------------------------+
| Note sweep digest, run r0007                     |
|                                                  |
| 8 notes, 3 categories.                           |
|                                                  |
| SUMMARY                                          |
| Most of this week's notes are about equipment.   |
| Two are urgent.                                  |
|                                                  |
| hardware (5)                                     |
|  - note-01  The 3D printer in room 118...        |
|  - note-02  my laptop keeps dropping the wifi... |
| ...                                              |
+--------------------------------------------------+
```

**The change record:**

```
The observation:  3 of 5 read the SUMMARY block and stopped. They answered
                  the task from the summary and never scrolled to the
                  category list. P1 L4, P3 L7, P5 L2.
The change:       the category counts move above the summary, as one line.
The prediction:   a participant names the right category without scrolling.
How I will know:  re-test with 2 people, same task, count scroll actions
                  before they answer.
```

**Version 2:**

```
+--------------------------------------------------+
| Note sweep digest, run r0007                     |
|                                                  |
| hardware 5  ·  software 2  ·  other 1            |
|                                                  |
| SUMMARY                                          |
| Most of this week's notes are about equipment.   |
| Two are urgent.                                  |
|                                                  |
| hardware (5)                                     |
|  - note-01  The 3D printer in room 118...        |
| ...                                              |
+--------------------------------------------------+
```

**One line moved. That is a complete change** and it is more defensible than a
redesign, because you can tell whether it worked.

---

## Worked example 2 · the re-test, and what it costs

Two people, the same task, twenty minutes total. That is the whole re-test.

```
Re-test of change 1, wireframe v2, paper

P6 (outside the class)
  read the top line, answered "hardware", 6 s, no scroll         PASS
P2 (returning participant from the study)
  read the top line, answered "hardware", 4 s, no scroll         PASS
  said: "oh that's at the top now"

Prediction was: a participant names the right category without scrolling.
Result: 2 of 2 did. The change stays.
```

**Two people is what you have time for and the report says so.** It is not five,
it does not need to be five, and writing "re-tested with two people, one of whom
had seen version 1" is the honest sentence.

**The returning participant is a known weakness and it is worth using anyway.** P2
has seen version 1, so their speed is partly memory. What they are good for is the
sentence "oh that's at the top now," which tells you the change is noticeable.
**Note the weakness in the report rather than hiding the fact that P2 came back.**

### When the prediction fails

This happens and it is a result.

```
P7  read the top line, then scrolled anyway, answered from the list, 14 s
P8  read the top line, answered "hardware", 5 s, no scroll

Prediction was: a participant names the right category without scrolling.
Result: 1 of 2 did. Change stays, finding is not closed. P7 scrolled
        because the top line has no label on it and reads as a title.
        Next change: put the word "categories" in front of it.
```

**A failed prediction with an observation after it is worth more than a successful
one with nothing.** It is also the only way you find the second problem.

---

## Worked example 3 · choosing the media element

**Competency 7.3.1 is selecting the media elements to be used**, and the selection
is a design decision with costs, not a shopping list.

| Element | Good for | What it costs |
|---|---|---|
| **Text** | Anything somebody has to search, copy, translate, or read with a screen reader | Almost nothing to produce. Easily ignored when there is too much of it |
| **Graphics** | A shape, a relationship, a proportion, a layout | One file to make and keep. Cannot be searched. Needs alternative text |
| **Animation** | A change over time, or where something went | Attention, every time it plays. Hard to skip. A repeating one is a distraction with no off switch |
| **Video** | A procedure involving hands, or a physical thing | Minutes of work per second of output. Cannot be skimmed. Needs captions |
| **Sound** | An alert when the person's eyes are elsewhere | Useless in a shared lab, and it is the one people propose anyway |

**The rule: pick the cheapest element that answers the question the user was stuck
on.**

### Worked, on a real finding

```
Finding 2: 4 of 5 could not start the program without a second attempt.

Proposed:  a short video showing how to start it.
Cost:      twenty minutes to record, cannot be skimmed, out of date the
           next time a flag changes, and somebody has to be watching it
           at the moment they are stuck.
Cheaper:   the program, run with no arguments, prints the exact command
           to run. One line of text. Zero seconds of anybody's attention.
Chosen:    the one line of text.
```

**Somebody in your team will want the video.** The question that settles it is:
what is the person doing at the moment they need this. They are sitting at a
terminal that has printed an error one second ago. **Text, right there, wins every time.**

### Where video and animation do earn their place

They are not always wrong, and a report that rejects everything is not thinking.

- **Video earns it for a physical procedure.** Clearing a filament jam. Seating a
  card. You cannot write that faster than you can show it.
- **Animation earns it when the question is "where did it go".** A row that moves
  from one list to another, shown moving, answers a question text has to describe.
- **Graphics earn it for proportion.** Five categories and their counts as a bar
  is read faster than five numbers, and this is why the digest has a top line.

**Sound is the one to be hardest on.** In a room with twenty machines, a sound
alert is either muted or it belongs to somebody else's computer. Accessibility is
the other half: a person who cannot hear it gets nothing. **If sound is the only
signal, the design is broken for somebody.**

---

## Figma, and why this lesson is on paper

**Figma is not installed on the build machine and no step in this module using it
has been verified here.** Every Figma instruction anywhere in Module 6 is marked
**[VERIFY]** and your instructor will tell you on Monday whether it is available
this year.

**Paper is the primary path and it is not a consolation prize.** Three reasons,
and they are real:

- **Speed.** You can draw version 2, re-test it with two people, and draw version
  3, inside one Build 2. You cannot do that in any design tool.
- **Nobody polishes a rectangle.** A wireframe that looks finished gets
  commented on as a finished thing, and people stop telling you it is wrong.
- **It works on the thing you actually built.** Most of your programs print text
  to a terminal. A text wireframe in a fenced block is a higher-fidelity model of
  that than a rounded rectangle in a design tool.

**[VERIFY] If Figma is available**, the same four lines apply and the same re-test
applies. The tool changes nothing about the method. Export a PNG into your
repository so that the change record and the drawing live together.

---

## The wrong version, and what it produces

```
Change 2: move the category list to the top and colour each category.
Why:      it looks much better and it is what other tools do.
```

**What that produces, three weeks later:** somebody asks why the list moved,
nobody remembers, and the change gets reverted by the next person who has an
opinion.

**What it produces now:** a redesign nobody can tell the value of. You changed two
things at once, so if the re-test improves you do not know which one did it, and if
it gets worse you do not know which one to undo.

**And the reason is the weakest one available.** "What other tools do" is a
statement about other people's users doing other people's tasks. You have five
sessions of evidence about your own users and you are not using it.

**The colour part is not forbidden.** It moves to the preferences list:

```
Preferences: changes we wanted and could not justify from a session

- colour per category. Nobody struggled with anything colour would fix.
  Would also fail for anybody who cannot distinguish the colours, so if
  we do it, the colour is not the only signal.
- a different name for "other". Two participants asked what it meant, so
  this one might move to findings after the re-test.
```

**An empty preferences list is suspicious**, and your instructor will ask about it.
Everybody wants to change things. Writing them down as preferences is honesty, not
confession.

---

## Why the wrong version is tempting

**Because you are right about some of them.** You have used this program for three
weeks and you have real instincts about it. Some of your preferences are genuinely
good ideas, and the discipline is not to suppress them, it is to label them.

**Because a big redesign feels like more work done.** Moving one line looks like
you did nothing. It is the change you can defend, measure, and undo.

**Because the findings are about boring things.** Nobody's finding is "the visual
design lacks impact." The findings are about people not being able to start the
program and not knowing what a word means, and fixing those is unglamorous.
**Those are the ones that are worth marks and the ones that are worth doing.**

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Wireframe** | A low-detail model of what the thing shows and where. Boxes and words |
| **Fidelity** | How finished a model looks. Low fidelity gets more honest criticism |
| **Iteration** | Version 2 exists because version 1 was tested, not because time passed |
| **Prediction** | What you expect a participant to do differently. Can be wrong |
| **Re-test** | Running the same task against the new version |
| **Media element** | Sound, video, graphics, text, or animation |
| **Alternative text** | The words that stand in for a graphic for somebody who cannot see it |
| **Preferences list** | Changes you want and cannot justify, written down as such |

---

## Self-check

**1.** Your re-test shows the prediction was wrong. Name the two things you write
down and the one thing you do not do.

**2.** A teammate wants an animation showing each note flying into its category
when the run finishes. Write the question that settles it and then answer it.

**3.** Why does this module ask for two people in the re-test rather than five?

---

### Answers

**1.** **You write down the result and the observation that explains it.** The
result is "1 of 2 did what I predicted." The observation is the new thing you saw,
such as "P7 scrolled anyway because the top line has no label and reads as a
title."

**The thing you do not do is revert the change and say nothing.** A change that
half worked, with the reason the other half did not, is a finding. A change that
quietly disappears is a week of work nobody can learn from, including you.

**The third thing, which is worth doing:** say in the report that the finding is
not closed. A finding is closed when the behaviour changed, not when you made a
change.

**2.** **The question: what is the person doing at the moment they would see it?**

The answer, honestly: reading a digest to decide what to work on first. They are
not watching the run happen. The run happens at seven in the morning on a schedule
and nobody is there.

So the animation plays to an empty room, and on the occasions somebody is
watching, it delays the thing they came for. **Rejected**, and it goes on the
preferences list with that sentence next to it.

**The version that would survive the question:** if a person does watch the run,
and the useful thing is knowing which step it is on, then a single line of text
that updates per step answers the same question for none of the cost.

**3.** **Because five fresh participants for a re-test is not realistic in one
week, and pretending otherwise produces five sessions with classmates in them.**

Two people, with at least one from outside the class, is enough to tell you whether
a specific prediction came true. That is a much narrower question than the original
study asked, and narrow questions need fewer people.

**What two people cannot do is find new problems.** They will find some, and you
should write those down, and you should not claim that the re-test validated the
whole interface. **It tested one prediction.** Say that.
