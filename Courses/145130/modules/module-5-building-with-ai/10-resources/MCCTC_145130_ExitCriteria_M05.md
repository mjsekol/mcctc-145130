# Exit Criteria Checklist · Module 5 · Building With AI
## 145130 Applications of AI · Weeks 13-15

**Self-check.** Nobody collects this. It is the list you hold your own work
against before the demonstration, and the three headings are the syllabus wording.

Tick something only when you could do it in front of somebody, today, without
looking anything up.

---

## 1 · Wire an application to a model and handle the model failing, timing out, or returning garbage

- [ ] My application talks to my service over HTTP and never reads a raw model
      answer.
- [ ] I can make the model **fail** on purpose, and my program still gives the
      person something usable.
- [ ] I can make the model **time out** on purpose, and I know how long my program
      will wait before it gives up.
- [ ] I can make the model return **something my parser cannot use**, and my
      service says so by name rather than crashing.
- [ ] My application reports the **four wire failures separately**: the service is
      not running, it did not answer in time, it answered with an error status, it
      answered with something that is not my envelope.
- [ ] Every one of those four messages says **what to do**, not only what
      happened.
- [ ] My application's timeout is **larger than my service's worst case**, and I
      can say both numbers out loud.
- [ ] I have run all four failures myself and captured what they printed.

**The test.** Somebody stops your model server without telling you and asks you to
run your program. Nothing about that should surprise you.

---

## 2 · Parse unstructured model output into something your program can rely on

- [ ] My parser handles **at least three different shapes** a model can answer in.
- [ ] I can name those three shapes without looking.
- [ ] My parser returns a shape **or nothing**, and it does not decide whether the
      shape is good enough.
- [ ] My validator returns **the reason** a result is unusable, in a sentence a
      person can act on, not `True` or `False`.
- [ ] I check that what came back is the **kind of thing** I expected, not only
      that it parsed.
- [ ] I know which problems I **trim** and which I **refuse**, and I can say why
      the line is where it is.
- [ ] I have kept the answers my model actually gave me, in files, and I test
      against all of them.
- [ ] A model that refuses produces a named reason in my envelope, not a crash and
      not silence.

**The test.** Somebody hands you a model answer you have never seen, in a shape
you did not plan for. You can say what your program does with it before you run
it.

---

## 3 · Explain why the model layer and the application layer are separate

- [ ] I can give **four reasons**, without notes, and none of them is another one
      reworded.
- [ ] I can give the **strongest argument against** the split, honestly, and then
      answer it.
- [ ] I can point at the file that is the **contract** between my two layers.
- [ ] I can say which layer owns the timeout, the retry, and the fallback, and
      why it is that one.
- [ ] I can say what would have to change in my application if the model were
      swapped for a different one. The answer should be nothing.
- [ ] I can explain what `ok` and `source` each mean, and why they are not the
      same question.

**The test.** This exact question is asked of one named person on your team at the
demonstration, out loud, with no notes. Practise it on your partner first.

---

## The documents

The three criteria above are what the module is for. These are what proves it.

- [ ] `design/ipo-chart.md`, including a section on what the chart leaves out
- [ ] `design/dataflow-diagram.md`, including the trust boundaries
- [ ] `design/io-specification.md`, every field with a type and a range
- [ ] `design/constraint-list.md`, three columns, including what each one costs
- [ ] `design/data-dictionary.md`, including what happens when each field is wrong
- [ ] `docs/implementation-plan.md`, with milestones somebody else can check
- [ ] `docs/contingency-plan.md`, with an ordered cut list and a never-cut list
- [ ] `docs/user-help.md`, with every message in a table and a real fallback
      section
- [ ] `docs/troubleshooting-log.md`, three real entries, each naming a methodology
- [ ] `decision-log.md`, written on the day each decision was made
- [ ] `peer-walkthrough-record.md`, with a decision on every finding

```
python doc_check.py your-project
```

**Passing that is the floor, not the grade.** It checks that sections exist and
have words in them. It cannot tell whether anything you wrote is true. A person
does that, in the walkthrough, and so does your instructor.

---

## Things that are not on this list, on purpose

**How good your model's answers are.** You are running a small model on shared
hardware. The quality of what it writes is not what this module measures and it is
mostly not something you control.

**How many features you built.** A small project with every failure handled scores
higher than a large one that only works when everything works. The rubric is
written that way deliberately.

**Whether it looks nice.** Polish is ten points out of a hundred. Functionality
and Code Quality together are forty-five.

---

## If you cannot tick something

| What you cannot tick | Go to |
|---|---|
| Anything in section 1 | `03-lecture-notes/MCCTC_145130_Notes_FourFailuresFourMessages.md` and `MCCTC_145130_Notes_WhoGivesUpFirst.md` |
| Anything in section 2 | `03-lecture-notes/MCCTC_145130_Notes_ParsingModelOutput.md`, then Lab M05-02 |
| Anything in section 3 | `03-lecture-notes/MCCTC_145130_Notes_WhyTheLayersAreSeparate.md`, and `05-labs/lab-m05-01-files/CONTRACT.md` |
| The troubleshooting log | `03-lecture-notes/MCCTC_145130_Notes_TroubleshootingAnIntegration.md`, then Lab M05-03 |
| The documents | `05-labs/lab-m05-01-files/CONTRACT.md`, which is a finished example of one of them, and `python doc_check.py --list` for the required shape of the rest |

**Tell somebody before the demonstration rather than after it.** A box you cannot
tick on Wednesday is a conversation. The same box on Friday is a score.
