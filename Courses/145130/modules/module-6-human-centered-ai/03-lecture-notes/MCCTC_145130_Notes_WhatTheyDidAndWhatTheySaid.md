# What a user did, and what a user said
## 145130 Applications of AI · Module 6 · Week 16, Monday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W16_WhatTheyDidAndWhatTheySaid.md)

**There is no exported deck for this outline yet.** Gamma had no credits when this
module was built, so every deck in Module 6 is an outline waiting to be generated.
From the repository root:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W16_WhatTheyDidAndWhatTheySaid.md --export pptx
```

**Competency 2.15.2**, conduct and analyze research including focus testing and
beta testing with the end user in mind.

---

## Why this exists

You spent three weeks building something. You know where every file is, what
every word in the output means, and which flag you have to pass. **That knowledge
is now permanent and you cannot turn it off.**

The person who will use your program does not have it. There is no way to find out
what they do not know by thinking about it, because everything you would think
about is a thing you already know. The only way is to put the program in front of
one of them, say nothing, and write down what happens.

That is a usability test. It needs no software, no budget, and no permission. It
costs one hour and it is the highest-value hour in this module.

---

## The one idea

**What somebody did and what somebody said about it are two different kinds of
evidence, and they disagree constantly.**

You count the first. You record the second and mark it as an opinion. When they
disagree, the thing they did wins, because your program is used by people doing
things and not by people answering questions about it.

This sounds obvious written down. It is not obvious at four in the afternoon when
somebody you asked for a favour tells you your program was fine.

---

## Worked example 1 · the same session, two columns

A participant is asked to find out how many notes are about the network. Here is
the record, in the shape you will use all week.

```
P2, task 2

WHAT THEY DID                                   WHAT THEY SAID
opened the project folder in Explorer     0:00   "ok so where is this"
scrolled the folder, opened README.md     0:14
read the README                           0:22   "this is a lot"
closed it, opened a terminal              1:05
typed  python triage.py                   1:19
read the error                            1:24   "did I break it"
typed  python triage.py --help            1:41
typed  python triage.py --file notes.json 2:02
opened digest.md                          2:20   "oh that's nice"
counted network rows by eye               2:31   "three"
                                          2:48   "yeah that was no problem"
```

**Read the last line, then read the times.** Two minutes and forty-eight seconds,
one error, and a trip to `--help`, from somebody who ended the session saying it
was no problem.

**Both of those are true.** It was no problem for them, in the sense that they never got
stuck badly enough to give up. It also took nearly three minutes for a task you
expected to take twenty seconds, and the three minutes are the thing you can act
on.

**The finding:** P2 completed task 2 in 2:48 against an expected 0:20, after one
error and one trip to `--help`. Their report that it was no problem is an opinion and
does not change the finding.

---

## Worked example 2 · what the two columns catch that a survey does not

Same program, five participants, one number each.

```
participant   completed   time    attempts   said afterwards
P1            yes         0:41    1          "fine"
P2            yes         2:48    3          "no problem"
P3            yes         1:12    2          "good"
P4            no          gave up 4          "I'd ask somebody"
P5            yes         3:31    3          "it's alright"
```

**Four of five completed the task. Four of five said something positive.** A
survey would have reported a success rate of 80 percent and a satisfaction score
somewhere near the top, and both numbers would be true.

Now read the attempts column. **Four of the five needed more than one attempt to
start the program.** That is one finding, it has a count, and it points at exactly
one thing: nobody can tell from looking at your program how to start it.

**Neither column found that on its own.** Completion did not, because they mostly
completed. Opinion did not, because they were being kind. The attempt count did,
and an attempt count is free.

---

## Worked example 3 · the numbers worth writing down

Three, and every one of them costs nothing.

```
time on task      when did they start, when did they have the answer
attempts          how many times did they try before something worked
where they went   the first place they looked, right or wrong
```

**Time on task** is the one people skip because it feels fussy. It is the number
that turns "it was fine" into "it took four times as long as you expected."

**Attempts** is the one that finds the startup problem, every time.

**Where they went first** is the one that tells you what your program looks like
from outside. If four people out of five open the folder before the program, your
program is not the obvious thing in your project.

---

## The wrong version, and the exact thing it produces

Here is the wrong version. It is what almost everybody does the first time.

```
You: "Okay, so run it with the --file flag and then open digest.md."
P2:  [does exactly that]
You: "Did that work?"
P2:  "Yeah, that worked."
You: "Cool. What did you think?"
P2:  "It's good. Maybe the colours could be different."
```

**What that produced:** one opinion about colours from somebody who was never
allowed to get lost.

**What it cost, exactly.** You wanted to know whether a person can work out how to
start your program. That question is now unanswerable for this participant,
forever, and no later task can recover it, because you told them the answer in the
first sentence. You have spent fifteen minutes of a real person's time and you
have a note about colours.

**Two smaller things it produced.** "Did that work?" tells the participant that
something was supposed to work, so a person who is unsure will say yes. "What did
you think?" invites a review, and people review politely.

---

## Why the wrong version is tempting

**Because watching somebody struggle is genuinely uncomfortable.** Twenty seconds
of silence while somebody hunts through a folder feels like a minute. You will
want to help. Everyone does, including experienced people, which is why the rule
is written down rather than left to judgement.

**Because you asked them for a favour.** They are doing you a kindness and letting
them flounder feels like repaying it badly. It is not. Letting them flounder is
the entire favour you asked for, and you say so at the start so that they know.

**Because a compliment feels like a result.** "That was no problem" lands like
success. It is a sentence from somebody who took three minutes and hit an error.

---

## The rules for working with a real person

These are not advice. They are the conditions under which this work happens here.

**1. They say yes out loud**, after you read the consent line as written. If they
hesitate, the answer is no, and you thank them.

**2. No recording of any kind.** No video, no audio, no screen capture, no
photograph. You write on paper. A recording of a person is a thing that exists
afterwards and has to be kept somewhere, and nothing in this module is worth that.

**3. No personal data.** Participants are P1 through P5. Not their name, not their
class, not their year, not their job, not anything that would let somebody in this
building work out who they were.

**4. No classmates in the formal study.** They know what your program does and
they know what you want to hear. **Classmates are for the rehearsal and the
tabletop**, which are different things and are labelled as such.

**5. Nothing from a session goes into an AI tool.** Not the notes, not the quotes,
not a summary of either. This is the one people forget at eleven at night while
writing the report.

---

## The consent line

You read this word for word. It is short on purpose.

> I am testing a program I built, and I am not testing you. Anything that goes
> wrong is information I need. I am going to ask you to do a few things and then
> stay quiet while you do them, and that is on purpose rather than rude. I am not
> recording anything and I am not writing down your name. You can stop at any
> point, for any reason, and you do not have to tell me why. Is that okay?

**Wait for an answer out loud.** A nod is not a yes.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Usability test** | One person attempting a real task on your program while you watch and say nothing |
| **Facilitator** | You. The person who reads the script and then stops talking |
| **Participant** | The person doing the task. Identified as P1 through P5 |
| **Task** | A goal and a reason, given to the participant. Never a set of steps |
| **Time on task** | Seconds from the participant starting to the participant having the answer |
| **Attempts** | How many separate tries before something worked |
| **Behaviour** | Something the participant did. Countable |
| **Report** | Something the participant said about what they did. An opinion |
| **Pilot** | A rehearsal with somebody who is not one of your five. Not data |
| **Focus testing** | Watching a small number of intended users work, to find problems |
| **Beta testing** | Letting real users use a near-finished thing in real conditions |

**Focus testing and beta testing are both in the competency and they are not the
same.** Focus testing is a small number of people, watched, on tasks you chose.
Beta testing is real users doing their own work with a version that is nearly
done, and you find out what happened afterwards. **This module does focus
testing.** Beta testing would mean handing your program to the front office for a
week, which is a fine thing to propose in your report and is not what you have
time for.

---

## Self-check

**1.** A participant finishes every task and tells you the program was clear. Your
notes say one task took 55 seconds against an expected 10, and they opened the
wrong file twice. Write the one-sentence finding.

**2.** You are twenty seconds into a silence and the participant is scrolling
through the wrong folder. Name two things you may say and two things you may not.

**3.** Your partner offers to be participant number five because you are short.
What do you do, and why is the answer not "it is better than four"?

---

### Answers

**1.** Something close to: **"P3 completed the task in 55 seconds against an
expected 10, opening the wrong file twice first. Their report that it was clear is
an opinion and does not change the finding."**

The three things that have to be in it: the completion, the time against an
expectation, and the attempts. The fourth thing that has to be in it is the
separation, in words, between what you watched and what they told you.

**2.** **You may say:** "what are you trying to do right now?" and "take your
time, I am not timing you against anybody." Both keep the session moving without
supplying knowledge. You may also say nothing at all, which is usually correct.

**You may not say:** the name of any control or file, and "did that work?" The
first hands them the answer. The second tells them something was supposed to
happen, which turns their report into a guess.

**3.** **No, and you record that you were short rather than filling the gap.**

Your partner has seen every version of this program, knows what the words mean,
and knows what you want to hear. A session with them is not weak evidence, it is
evidence about a different question. **Four honest sessions with a note saying you
could not get a fifth is a better report than five sessions where one is a
teammate**, because the second one is not true and the first one is.

If you need a fifth, the answer is another adult in the building, another shop, or
somebody at home. Your instructor has a list.
