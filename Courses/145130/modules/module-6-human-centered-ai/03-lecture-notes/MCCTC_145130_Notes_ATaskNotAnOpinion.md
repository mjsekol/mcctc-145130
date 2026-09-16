# A task, not an opinion
## 145130 Applications of AI · Module 6 · Week 16, Tuesday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W16_ATaskNotAnOpinion.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W16_ATaskNotAnOpinion.md --export pptx
```

**Competencies 2.15.3**, design user tasks and evaluate results using use-case
scenarios, and **1.2.13**, identify stakeholders and solicit their opinions.

---

## Why this exists

Yesterday you learned to watch. Today you learn what to ask, and it turns out that
the question is where most of the damage gets done.

**A badly written task destroys the measurement before the session starts.** It
does it quietly, because the session still happens, the participant still does
things, and you still write things down. You come away with a full sheet of paper
and nothing you can act on.

There is no fixing it afterwards. A task that contained its own answer cannot be
un-asked, and that participant cannot be reused.

---

## The one idea

**A task gives a goal and a reason. It never gives the steps and it never contains
its own answer.**

Three parts, every time:

```
the starting state   where they are and what they have
the goal             what they want to end up knowing or having
the reason           why a person would want that
```

The reason is the part people leave out and it is the part that makes somebody try
properly. "Find out how many notes are about the network" is a chore. "You are
covering the help desk on Monday and you want to know how many of these are the
network before you start" is a thing a person leans into.

---

## Worked example 1 · the same request, three ways

**The instruction. Not a task.**

> Run the program by typing `python triage.py --file notes.json`, then open
> `digest.md`.

What it tests: whether the steps work when performed correctly. That is a smoke
test and it has a use. It tests nothing about whether anybody could find the
steps, and it burns a participant to find out something you already knew.

**The opinion question. Not a task.**

> Take a look at the program and tell me what you think of it.

What it tests: how polite the participant is. Everybody says some version of "it
seems good, maybe the colours." You cannot act on that on Monday morning.

**The task.**

> You are covering the front desk on Monday and there is a pile of notes from last
> week. You want to know how many of them are about the network before you start
> answering any of them. Show me how you would find that out.

What it tests: whether a person can start your program, find its output, and read
it. All three at once, which is why you get three findings out of one task.

---

## Worked example 2 · six drafted tasks, judged

Four of these are broken. This exact set is part 1 of Lab M06-01.

```
1  Click Run and then read the summary at the top of digest.md.
2  You want to know which of these notes are about somebody being locked
   out of their account. Show me how you would find that out.
3  Try the program out and see what you think of the categories.
4  Find out which notes came in more than once this week.
5  Your printer note got put in the wrong category. Fix it.
6  It is Monday morning and you have fifteen notes and twenty minutes.
   Decide which three you would deal with first, using whatever the
   program gives you.
```

| # | Verdict | Why |
|---|---|---|
| 1 | **Broken. Names the control and the file.** | Both questions you wanted answered are now answered for them. |
| 2 | **Good.** | Goal, reason implied, no control named, and the answer is checkable. |
| 3 | **Broken. It is an opinion question.** | "See what you think" produces a review, not a behaviour. |
| 4 | **Broken. The program cannot do it.** | The participant hunts for a feature that does not exist. That is thirty seconds of their time and it teaches you nothing you did not already know. |
| 5 | **Broken. It contains a finding.** | "Got put in the wrong category" tells them the program is wrong and tells them which note. Now you cannot find out whether they would have noticed. |
| 6 | **Good, and it is the best one here.** | It is a real decision with a real constraint, it uses the whole output, and there is no single expected path. |

**Task 4 is the one a tabletop catches and a reading does not.** Everybody reads
it and thinks it sounds reasonable. Somebody has to try it.

---

## Worked example 3 · the four things you may not say

Write these on the inside of your clipboard. They are the whole facilitator rule
set.

```
1  the name of a control      "click Run", "there is a --file flag"
2  "you can"                  "you can use the arrow keys"
3  "did that work?"           tells them something was supposed to work
4  the answer                 in any form, including your face
```

**What you may say, and it is a short list:**

- "What are you trying to do right now?"
- "What did you expect to happen?"
- "Take your time, I am not timing you against anybody." (You are timing. You are
  not comparing.)
- Nothing. Silence is the default and it is correct far more often than it feels.

**Number 4 includes your face.** You will make an expression when somebody goes
the wrong way. Look at your paper, not at their screen, and write. That is also
why you write times: it gives your hands something to do.

---

## The closing question, and it is not "did you like it"

One question at the end, after the tasks. Ask this one:

> If you had to do that again tomorrow, what would you do differently?

**Why this one works.** It asks about behaviour, not about feelings. It gets an
answer like "I would go straight to the terminal" or "I would look for the help
first", which is a thing you can act on. It also gets you the thing they were
embarrassed about, which is usually the real finding.

**What not to ask:** "Did you like it?" "Was that clear?" "Any suggestions?" All
three produce politeness, and the third one produces feature requests from
somebody who used your program for eleven minutes.

---

## The wrong version, and what it produces

A real script, written by somebody in a hurry, and the session it produces.

```
Task 1: Open the program and run it on notes.json.
Task 2: Look at the output and tell me if the categories make sense.
Task 3: Tell me one thing you would change.
```

**What comes back, every single time:**

```
P1  ran it, output appeared, "yeah the categories seem fine",
    "maybe more colours"
P2  ran it, output appeared, "these look right to me", "nothing really"
P3  ran it, output appeared, "I don't know what 'other' means",
    "call it something else"
P4  ran it, output appeared, "sure", "no"
P5  ran it, output appeared, "looks good", "make it faster"
```

**Five sessions, seventy-five minutes of other people's time, and one usable
finding**, which is P3 not knowing what "other" means. Everything else is a
politeness or a feature request.

**And notice what is missing.** Nobody had any trouble starting the program,
because task 1 started it for them. You now believe your program is straightforward
to start, and you have no evidence either way.

---

## Why the wrong version is tempting

**Because it is efficient.** You get through five participants quickly and
everybody leaves happy. The good version is slower, more awkward, and produces a
sheet full of problems.

**Because it feels fair to the participant.** Telling somebody what to type looks
like being helpful to a person who is doing you a favour. It is being helpful. It
is also spending their fifteen minutes on a question you did not need answered.

**Because "tell me one thing you would change" sounds like exactly what a designer
should ask.** It is the most common bad question in this field. The participant has
used your program for eleven minutes and you have used it for three weeks. Their
opinion about what to change is worth less than what you watched them do, and
asking for it invites them to invent one.

---

## Identifying who the study is for

**Competency 1.2.13 is identify stakeholders and solicit their opinions**, and it
is not the same as asking your participants what they think.

Three different groups, and confusing them is a common mistake.

| Group | Who | What you want from them |
|---|---|---|
| **Users** | The people who will use the thing. Your five participants stand in for them. | Behaviour. What they do. |
| **Stakeholders** | The people who decide whether it ships, pay for it, or own the problem. The front office person from the brief. | Opinions, and what finished means to them. |
| **You** | The people building it. | Nothing. You are not evidence. |

**You ask stakeholders what they think. You watch users.** Asking a stakeholder
for an opinion is correct and it is what Week 17 Thursday's acceptance
conversation is. Asking a user for an opinion is how you end up with the script in
the wrong version above.

Write down who your stakeholder is, by role, in your study README. You will need
them again in Week 17.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Task** | A starting state, a goal, and a reason. Never the steps |
| **Use-case scenario** | The realistic situation around a task, which is the reason part |
| **Leading** | Any words that supply knowledge you were trying to measure |
| **Script** | The whole of what you say: consent line, tasks, closing question |
| **Facilitator rules** | The four things you may not say |
| **Stakeholder** | Somebody who decides, pays, or owns the problem |
| **User** | Somebody who will do the work with the thing |
| **Smoke test** | Checking the steps work when performed correctly. A real thing, not a usability test |

---

## Self-check

**1.** Rewrite this as a task: "Use the search box to find all the notes from
Tuesday."

**2.** Your script has four tasks and the tabletop shows they take twenty minutes
total. Your sessions are fifteen minutes. What do you cut and how do you decide?

**3.** A participant, halfway through task 2, says "am I doing this right?" What do
you say?

---

### Answers

**1.** Something like: **"You remember somebody mentioning a problem on Tuesday
and you want to find what they wrote. Show me how you would find it."**

The marks are for removing "search box", which named a control, and for adding a
reason somebody would actually have. **"Find all the notes from Tuesday" with the
control removed is acceptable and weaker**, because it is a chore with no reason
attached, and people do chores half-heartedly.

**2.** **Cut by what you would change on Monday morning.** For each task, write the
sentence you would put in your report if it went badly. The task whose sentence
you care least about is the one that goes.

**A common wrong answer: cut the longest one.** The longest task is often the one
that is long because it is hard, and hard is where the findings are. **Task 6 in
worked example 2 is the long one and it is the best one.**

**Do not solve this by talking faster or by rushing the consent line.** Three tasks
inside the time is a real study. Four tasks that overrun means the last one runs
with a participant who is now late for something.

**3.** Something like: **"There is no right way. I want to see what you would
actually do."**

Do not say yes. Do not say no. Both of those answer the question you were trying
to ask. Do not say "you are doing fine", which is the same as yes with a friendly
tone.

If they ask twice, it is worth a note: **a participant who needs reassurance twice
is telling you the program gives no feedback about whether anything is working**,
and that is a finding with a location.
