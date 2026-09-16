# Lecture Notes: User Help for the Person Who Is Stuck
## 145130 Applications of AI · Module 5 · Week 15, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W15_UserHelp.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W15_UserHelp.pptx)

If you missed class, you can learn this concept from this file alone. You need
nothing running.

**Competency 5.6.8** includes user help. **Competency 1.2.5** is communicating
for an intended audience and purpose, and that is what this really is.

---

## Why this exists

Every other document in this module is written for somebody who is building the
system. User help is written for somebody who is using it and it stopped
working. That person is not a developer, is not interested in your architecture,
and is reading because they are annoyed.

That changes everything about how it is written, and almost nobody makes the
change. Most user help in the world is a description of the software written by
the person who wrote the software.

---

## The concept in plain language

**Write for the moment somebody reaches for it.** Nobody reads user help when
things are going well. They read it when something did not work, they are behind
on something else, and they want one sentence that tells them what to do.

Four sections, in this order, because that is the order the reader needs them.

| Section | Answers | Written for |
|---|---|---|
| What this program does | should I be using this at all | somebody who was handed it |
| How to start it | I have it and nothing happened | somebody at a terminal right now |
| What every message means | it said something and I do not know what | somebody looking at one line of output |
| When it says the answer is a fallback | it worked and the answer looks wrong | somebody about to act on bad output |

The fourth section is specific to this kind of program and it is the one that
matters most. A fallback is the program working correctly and it does not look
like it.

### Three rules

**1. Every message the program can print is in the table.** Not most of them.
All of them. If a person sees a line that is not in your help, your help has
told them that reading it was a waste of time.

**2. Every row says what to do, not what happened.** "Connection refused" is
what happened. "Start the service with this command" is what to do.

**3. No word the reader has to look up.** Not because they are not clever, but
because they are looking something up already and you have added a second thing.

---

## Worked example 1: the message table

A worked message table. Three columns, and the third one is the reason anybody
opened the file.

| You see | It means | Do |
|---|---|---|
| `from FALLBACK, not the model` | the answer was built by a rule, not by the model | read the `why:` line under it |
| `reachable no` | the service is running and cannot find a model | start the model, or the stand-in |
| `The model service is not answering.` | the service is not running, or it is on another port | start it in window 2, and check the port your program printed |
| `The model service took too long.` | the service did not answer in 30 seconds | the model is probably still loading. Run it again. |
| `The reply was not the shape this program expects.` | something else is answering on that port | you are almost certainly pointed at the model instead of the service |
| `The model service refused this request.` | the request was wrong before it reached the model | the line under it says which rule. Usually the text was empty or too long. |

Notice that the second column never uses a word from inside the program.
"Deserialise" does not appear. "Envelope" does not appear. `ClientFailureKind`
does not appear. The reader does not have those words and does not need them.

---

## Worked example 2: the fallback section, written for somebody about to be wrong

This is the section that only exists in help for a program with a model in it.
Here is its shape.

**What a fallback is**, in two sentences with no jargon:

> When the model cannot be used, the service builds an answer by rule instead.
> It takes the first line of what you sent and uses that.

**How you know**, with the real output:

```
  source       fallback
  elapsed_ms   2057
  result in full:
    headline: The 3D printer in room 118 jammed near the nozzle.
  error kind:    connection_refused
  error message: nothing is listening at http://127.0.0.1:11535
```

**What it means for you**, which is the part that keeps somebody out of trouble:

> A fallback headline is the first line of what somebody wrote, which is usually
> fine and never insightful. It is right when the first line happens to be the
> point and wrong when it is not.

**What to do about it**, as numbered steps ending in a decision the person is
allowed to make:

> 3. If every answer is a fallback and you needed real summaries today, do not
>    use the output. Say so rather than handing on a page of first sentences.

**Why the program does not fail instead**, because somebody will ask:

> Because most of the time a fallback is better than nothing, and because a
> program that stops working the moment the model is unavailable would be
> unusable in this building, where the model is unavailable fairly often.

---

## Worked example 3: the same sentence, three ways

One thing to say: the program needs a service running before it will work.

**Written for the compiler.**

> The service client resolves its base address from an environment variable,
> defaulting to the loopback endpoint, and surfaces a `ServiceDown` failure kind
> when the socket is refused.

Every word is true. The reader does not have any of those words.

**Written for a manager.**

> The application requires the model service to be available. In the event that
> the service is not available, an appropriate error will be displayed to the
> user.

No jargon, and also no information. It does not say what the message is or what
to do about it.

**Written for the person who is stuck.**

> If you see `The model service is not answering.`, the second thing on the
> list is not running. Go to window 2 and start the service again, then run your
> command again.

Twenty-eight words. It quotes the exact message they are looking at, names the
thing that is missing in a way that matches how they started it, and gives the
command.

---

## The wrong version, and what it produces

From a real submission shape:

> ## What this program does
>
> The headline service is a CLI-adjacent microservice that leverages an LLM to
> perform abstractive headline generation on arbitrary text payloads via a
> RESTful interface.
>
> ## How to start it
>
> Install the model runtime with administrator rights on your own laptop, pull
> the model, then export the environment variables and start the service. If
> you are technical this takes about five minutes.
>
> ## What every message means
>
> Error messages are printed to stderr with a description of the problem. Check
> the service logs for more detail.
>
> ## When it says the answer is a fallback
>
> The fallback is used when the model is unavailable.

Four sections, all present, and the document is worthless. Take them in order.

**Section 1** has nine words the reader does not have: CLI, LLM, payloads,
RESTful, microservice, and architecture among them. It never says what the
program is for.

**Section 2 locks out most of its readers.** "Administrator rights on your own
laptop" describes nobody using a lab machine. It also does not mention that a
stand-in model server ships with the program, so the first sentence is asking
somebody to install something they do not need.

**Section 3 is a pointer, not help.** It says messages exist, which the reader
knew, and sends them to a log they cannot read.

**Section 4 is one sentence and it is incomplete.** It does not say how you
know, does not say how much to trust a fallback answer, and does not say what to
do. This is the most important section in help for this kind of program and it
is nine words long.

---

## Why the wrong version is tempting

Because you know how the program works, so writing what you know is quick, and
working out what somebody else does not know is slow.

There is also a pull toward sounding professional. "Leverages an LLM via a
RESTful microservice architecture" sounds more like real documentation than "it
reads help requests and sorts them", and it is worse in every way that matters.

**The habit that prevents it:** hand the document and the program to one person
who has never seen either, sit behind them, and write down every question they
ask out loud. Do not answer. Every question is a line missing from your help.
That is the exercise you run in the lab this week, and it is also the beginning
of Module 6.

---

## Vocabulary

| Term | What it means |
|---|---|
| **User help** | documentation for the person using the program, not building it |
| **Audience** | who you are writing for, decided before you write anything |
| **Message table** | every line the program can print, what it means, and what to do |
| **Jargon** | a word that is precise inside your team and empty outside it |
| **Precondition** | something that has to be true before a step will work |
| **Observability** | how much a person can tell about what the program is doing |
| **Fallback** | an answer built without the model, labelled as such |

---

## Self-check

**Question 1.** Your help says "an appropriate error will be displayed." Name
two things that sentence fails to give the reader, and rewrite it for one real
message.

**Question 2.** Your program can print eleven different messages and your help
covers eight. Say what the reader concludes when they hit one of the other
three.

**Question 3.** Your user help tells the reader to install a model runtime with
administrator rights. Name who that excludes in this building, and say what the
honest version of that section says instead.

---

### Answers

**1.** It does not tell them which message they are looking at, and it does not
tell them what to do about it. Rewritten: "If you see `The model service is not
answering.`, the service is not running. In window 2, run `python
model_service/app.py`, then run your command again."

**2.** They conclude the help is incomplete, and from then on they do not open
it, including for the eight it does cover. Coverage is not a percentage with
partial credit. A help table that misses messages teaches the reader that
looking is a waste of time, and that lesson applies to the whole document.

**3.** It excludes everybody on a lab machine, which is most of the class most
of the time, and anybody working on a shared or school-managed computer. The
honest version starts with the path that works for everybody: a stand-in model
server ships with the program, it needs no administrator rights and no download,
and here is the one command that starts it. Installing a real model runtime
belongs later, as an option, labelled as needing rights the reader may not have.
