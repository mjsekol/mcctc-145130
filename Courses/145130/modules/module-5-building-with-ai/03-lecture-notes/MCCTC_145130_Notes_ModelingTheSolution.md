# Lecture Notes: Modeling the Solution Before You Build It
## 145130 Applications of AI · Module 5 · Week 13, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W13_ModelingTheSolution.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W13_ModelingTheSolution.pptx)

If you missed class, you can learn this concept from this file alone. You need
nothing running. This lesson is done on paper on purpose.

**Competency 5.1.3** asks you to model a solution using graphic tools
(flowcharts, IPO charts, UML, decision tables), pseudocode, and AI.
**Competency 5.6.6** asks you to design system inputs, outputs, and processes.
**Competency 5.6.7** asks you to document that design with the right tool.
The three go together, and the word that matters in all of them is **before**.

---

## Why this exists

You have been writing programs for two years and you have mostly designed them
in your head. That worked because you were the only person in the program and
the program fit on one screen.

This build has two programs, two languages, two people, and a contract between
them. The thing you are about to find out is that two people who have not
written the design down have written two different designs, and neither of them
knows it until Thursday.

A model of the solution costs you forty minutes and it is the cheapest forty
minutes in the module.

---

## The concept in plain language

There are five tools in the competency and they are not interchangeable. Each
one answers a different question, and picking the wrong one is how design
documents end up unread.

| Tool | The question it answers | When it is the right tool |
|---|---|---|
| **IPO chart** | what goes in, what happens, what comes out | first, always. One page. |
| **Dataflow diagram** | what moves between which layers, and where it is checked | when there is more than one program |
| **Flowchart** | what order the steps run in, and where the branches are | one function or one decision that is hard to hold in your head |
| **Decision table** | for every combination of conditions, what should happen | when you have three or more inputs that combine |
| **Pseudocode** | the exact logic, without a language getting in the way | the step before you write the function |
| **UML class diagram** | what the types are and what they hold | when you have several types and they refer to each other |

**And AI.** The competency names artificial intelligence alongside the graphic
tools, which means using a model to help you model. That is allowed here and it
has one rule attached: you may ask a model to draft a diagram or a decision
table, and you may not submit one you cannot defend line by line. Every draft
you take from a model goes into your decision log with what you changed and why.

---

## Worked example 1: the IPO chart, the first forty minutes

Here is the IPO chart for the anchor stack, cut down to the part that matters.
The full one is in `09-project/reference-implementation/design/ipo-chart.md`.

**Input**

| Input | From | Allowed values | Untrusted |
|---|---|---|---|
| command | the person | `health`, `summarize`, `classify`, `triage` | yes |
| text | the person | 1 to 4000 characters after cleaning | yes |
| model answer | the model, over HTTP | any text at all | yes, most of all |

**Process**

Read the command. Send task and prompt to the service. The service checks the
request, builds the prompt, calls the model with a timeout, reads the reply,
parses a shape out of it, checks the shape, and returns the envelope or a
labelled fallback. The application reads the envelope into typed objects and
prints.

**Output**

| Output | To | Shape |
|---|---|---|
| envelope | the C# client | `ok`, `task`, `result`, `source`, `elapsed_ms`, `error` |
| summarize result | the person | `summary` string, `bullets` 1 to 5 |
| classify result | the person | `label` from five, `confidence_note` sentence |

**The row people leave off is the last row of Input.** The model's answer is an
input to your system. It comes from outside, you do not control it, and it is
the input most likely to be shaped in a way you did not plan for. If it is not
on your input list, your design has a hole in it.

---

## Worked example 2: a decision table, because this is where people guess

Here is a question with a real answer that nobody gets right by intuition: what
should the program print, given the three things it can know?

The three conditions are: did the HTTP call succeed, what does `source` say, and
is `error` set.

| # | HTTP call | `source` | `error` | What the program does |
|---|---|---|---|---|
| 1 | succeeded, 200 | `model` | null | print the result. Say it came from the model. |
| 2 | succeeded, 200 | `fallback` | set | print the result. Say it came from the fallback, and print `error.kind`. |
| 3 | succeeded, 400 | `none` | set | do not print a result. Say the request was refused and name the kind. |
| 4 | succeeded, 200 | missing | anything | do not print. This is not the envelope. Say what port you are pointed at. |
| 5 | connection refused | n/a | n/a | say the service is not running and give the command that starts it |
| 6 | timed out | n/a | n/a | say how long you waited and that the model may still be loading |
| 7 | succeeded, 500 | `none` | set | say the service failed and point at its console |

Seven rows. Now count how many different messages a program needs: at least
five. A program that prints "Error" for rows 3 through 7 has thrown away the
only thing the person needed.

**The reason to build this table before you write code** is row 2. Row 2 is a
success that carries an error, and nobody writes row 2 by accident. You write it
because you filled in the table and saw an empty cell.

---

## Worked example 3: pseudocode, and the difference from code

Pseudocode for the part of the service that runs one task. Notice what it does
not have: no language, no imports, no syntax to get wrong. Notice what it does
have: every branch, named.

```
run_task(task, prompt):
    start the clock

    try:
        answer = ask the model, with a timeout, retrying only the kinds that can change
        result = parse the answer into this task's shape
        reason = check the result against this task's rules
        if reason is nothing:
            return envelope(ok: true, result, source: "model", error: none)
        error = ("task_validation_failed", reason)
    catch a model failure as e:
        error = (e.kind, e.message)

    result = build this task's fallback, with no model involved
    return envelope(ok: true, result, source: "fallback", error)
```

Ten lines, and every decision in the service is in them. The real function is
twenty lines of Python and does exactly this.

**The test of pseudocode:** hand it to your partner and ask them what happens
when the model answers with something the parser cannot use. If they can answer
from the pseudocode alone, it is finished. If they have to ask you, it is not.

---

## The wrong version, and what it produces

The wrong version is the design you did not write down, and here is what it
produces. This is a composite, built from what happens in this lab every year
and not from one real team.

Two students split a build on Monday. One takes the service, one takes the
application. They agree out loud that the service will "return the summary".

On Thursday they connect the two halves. The service returns:

```json
{"summary": "...", "bullets": ["...", "..."]}
```

The application was written to read:

```json
{"result": {"text": "...", "points": ["...", "..."]}}
```

Neither of them is wrong. They never agreed. The C# program runs, deserialises
successfully, and prints an empty line, because `System.Text.Json` sets a
missing field to its default rather than complaining.

```
  summary:
```

No error. One empty line. Two days of work that do not fit together, found on
Thursday of a three week module.

---

## Why the wrong version is tempting

Because you can see the code working and you cannot see the design working.

Forty minutes of tables on Monday produces nothing you can run. Forty minutes of
code on Monday produces something on a screen. On Monday the second one feels
like progress and the first one feels like homework.

The cost arrives later, and it does not arrive evenly. A design mistake found on
Monday costs you a conversation. The same mistake found on Thursday costs both
of you a rewrite, and Thursday of Week 13 is the last day the instructor is in
the room before the competition week.

**The habit that prevents it:** write the result shape down, in one place, in
JSON, and both of you paste the same block into your own file. Not a description
of the shape. The shape.

---

## Vocabulary

| Term | What it means |
|---|---|
| **IPO chart** | input, process, output, on one page. The first document you write. |
| **Dataflow diagram** | what moves between layers, and where each thing is checked |
| **Decision table** | every combination of conditions, and what should happen for each |
| **Pseudocode** | the logic in plain words, with every branch, and no language |
| **UML class diagram** | the types, what they hold, and what refers to what |
| **Requirement** | something the system must do, written so you can tell whether it does |
| **Constraint** | something you are not allowed to change, or a limit you have to live inside |
| **Contract** | the agreed shape that crosses a boundary, written down where both sides can read it |

---

## Self-check

**Question 1.** You have three inputs that combine: whether a file exists,
whether it parses as JSON, and whether it holds at least one record. Which of
the five tools is the right one, and how many rows will it have?

**Question 2.** Your partner says the IPO chart is pointless because the three
columns are obvious. Name two things that belong in the Input column that are
not obvious, and say why leaving them out causes a real problem later.

**Question 3.** You ask a model to draft your dataflow diagram and it produces
something that looks right. What are you required to do before it goes in your
repository, and what is the one thing that would make submitting it a failure
of this course rather than a shortcut?

---

### Answers

**1.** A decision table. Three conditions with two states each gives eight rows.
You write all eight even though some of them are impossible, because writing the
impossible ones is how you find out that two of them are not impossible.

**2.** Two answers among several. **Configuration** belongs in Input: the
service URL, the model name, the timeout. People treat those as part of the
program rather than as input, and then hardcode them, and then cannot move the
service. **The model's answer** belongs in Input: it arrives from outside, you
do not control it, and it is the input most likely to arrive in a shape you did
not plan for. Leave it off and your design has no place where you decided what
to do about a refusal.

**3.** You have to be able to defend every line of it, and you record in your
decision log that it came from a model, what you changed, and why. What makes it
a failure rather than a shortcut is submitting a diagram you cannot explain. The
one rule in this program that ends in a zero is submitting work you cannot
explain, and a model-drafted diagram you have not checked against your own code
is exactly that. Check it line by line against the real layers, and you will
usually find at least one thing in it that is not true of your system.
