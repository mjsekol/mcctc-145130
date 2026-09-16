# Additional Resources · Week 17
## 145130 Applications of AI · Module 6 · Week 17
### Topics: wireframes and media elements, automation with a real error path, value you can defend, acceptance

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has
not been confirmed live from the build machine. Click it before you rely on it.

**Two tools this week are not installed on the build machine: Figma and n8n.**
Every step using either is marked [VERIFY] everywhere in this module, and both have
a runnable alternative that is the primary path. Paper is the wireframe tool. A
standard-library Python program is the automation tool.

**Nothing here requires an account or a commercial AI developer API.**

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The reference change record and both wireframes | Mon | On-level | 20 min |
| 2 | Official docs: Python `pathlib`, the `stat` section | Tue | On-level | 15 min |
| 3 | Official docs: Python `argparse` | Tue | Remediation | 25 min |
| 4 | The lab starter and the lab solution, side by side | Tue | On-level | 30 min |
| 5 | Interactive: `check_sweep.py` against your own program | Tue-Fri | On-level | 10 min |
| 6 | The reference run book | Tue | On-level | 15 min |
| 7 | The reference opportunity analysis | Wed | On-level | 25 min |
| 8 | RFC 2119, the words that make a requirement testable | Thu | Extension | 10 min |
| 9 | Official docs: Python `subprocess` and `tempfile` | Thu | Extension | 30 min |
| 10 | The reference acceptance procedure and record | Thu | On-level | 20 min |
| 11 | Automate the Boring Stuff, the scheduling chapter | Tue | On-level | 45 min |
| 12 | This week's four lecture notes and their self-checks | Any | Review | 20 min each |
| 13 | [VERIFY] The n8n documentation, if it is available this year | Tue | Extension | 30 min |

---

## 1. The primary reading, and it is in this repository

`09-project/reference-implementation/design/` · **Confident.**

Three files: `wireframe-v1.md`, `wireframe-v2.md`, and `change-record.md`.

**Why these.** They are the shape Monday's deliverable takes, in text rather than in
a design tool, which is what most of your programs actually produce.

**Read change 2 and its re-test result.** The prediction was that a participant
would answer without asking a question back. **One of two did.** The change stayed,
the finding did not close, and the record says both. That is what a real iteration
looks like and it is not tidy.

**Then read the preferences list underneath.** Three things the team wanted and
could not justify. **Yours being empty is the thing your instructor will ask
about.**

**Time.** 20 minutes. **Level.** On-level.

---

## 2. The official documentation page for Tuesday

`https://docs.python.org/3/library/pathlib.html` · **Confident.**

**Read one thing:** `Path.stat()`, and the `st_mtime` attribute it gives you.

That one number is the whole freshness step. **The question to answer before you
write any code:** what does it give you when two files were written by the same copy
operation a few milliseconds apart, and what does that mean for how you compare it?

**Time.** 15 minutes. **Level.** On-level.

---

## 3. Command line arguments, properly

`https://docs.python.org/3/library/argparse.html` · **Confident.**

**Why this one is here.** Your automation needs a trigger that is chosen at the
command line, and the lab's version uses a mutually exclusive group so that exactly
one of `--once`, `--at`, and `--every` is required.

**Read three things and stop:** `add_argument` with `required=True`,
`add_mutually_exclusive_group`, and what `choices` does.

**The design decision worth copying:** `--service` and `--port` have **no
defaults** anywhere in this module. A program that reaches the wrong server does
not fail. It answers.

**Time.** 25 minutes. **Level.** Remediation, and skip it if you are comfortable.

---

## 4. Interactive practice: the starter against the solution

`05-labs/lab-m06-03-files/note_sweep.py` and
`05-labs/instructor/lab-m06-03-solution/note_sweep.py` · the second one is
instructor-only until the lab is finished.

**Do this before you write anything on Tuesday.** Run the starter twice, once with
the stub on **port 5158** and once with it stopped, and read the last line of both.

```
python sweep_service_stub.py --port 5158
python note_sweep.py --service http://127.0.0.1:5158 --once
```

**They are the same line.** The two digest files are the same bytes. There is no
exception anywhere.

**Time.** 30 minutes. **Level.** On-level, and required.

---

## 5. Interactive practice: check your own automation

`05-labs/lab-m06-03-files/check_sweep.py` · **Confident.**

```
python check_sweep.py --program note_sweep.py --port 5170
```

**Run it at the start of Tuesday and again at the end.** The starter scores 2 of 6
on the build machine. Anything above that is progress you made, and you should be
able to say which checks moved and why.

**What it cannot do.** It reads no source code, so a comment cannot fool it, and it
reads no prose, so it cannot tell whether your incident file says anything worth
reading. **A team at 6 of 6 with a one-line incident file has passed the tool and
not the lab.**

**Time.** 10 minutes. **Level.** On-level.

---

## 6. The reference run book

`09-project/reference-implementation/automation/run-book.md` · **Confident.**

**Why this one.** Four sections, in the order somebody needs them at half past seven
in the morning, and one paragraph saying plainly that there is no email and there
will not be one, with the reason.

**The section to copy the shape of** is "When it fails", which is a table of the
step that failed against the one thing to check first.

**Time.** 15 minutes. **Level.** On-level.

---

## 7. The reference opportunity analysis

`09-project/reference-implementation/analysis/opportunity-analysis.md` ·
**Confident.**

**Why this one.** Three workflows, three estimates, and **two numbers per workflow**
rather than one, because the second number is what the estimate becomes if the
assumption is wrong.

**Read workflow 3 and the assumption under it.** It is the biggest number in the
document and it sits on the assumption with the most at stake, and the analysis
says so and recommends leaving it alone.

**Then read "What I did not measure", item 4.** Nobody asked the practice which
part of their week they would most like back. **That is the item professionals
miss.**

**Time.** 25 minutes. **Level.** On-level.

---

## 8. The words that make a requirement testable

**RFC 2119, key words for use in RFCs to indicate requirement levels** ·
`https://www.rfc-editor.org/rfc/rfc2119` · **Confident.**

**Why this one, on Thursday.** Two pages. It defines MUST, MUST NOT, SHOULD, SHOULD
NOT, and MAY, and it is the reason standards documents can be argued about
precisely.

**What it is for.** Your acceptance cases are full of sentences that sound firm and
are not. Rewrite each Then using one of these words and a number, and watch how many
of them turn out to be decisions you had not made.

**The honest caveat:** nobody expects your procedure to read like an RFC, and a
document in capital letters is harder to read. **Use the distinction, not the
typography.**

**Time.** 10 minutes. **Level.** Extension.

---

## 9. If you want to turn your procedure into a program

`https://docs.python.org/3/library/subprocess.html` and
`https://docs.python.org/3/library/tempfile.html` · **Confident.**

**Why these two.** They are what the EXTENDED option in Lab M06-04 needs.
`subprocess.run` with `capture_output=True` and `cwd=` runs your program somewhere
that is not your folder, and `tempfile.mkdtemp` gives you the somewhere.

**The rule that makes it worth doing:** it has to run on a machine that is not
yours, in a folder that is not yours, without anything being edited. **If it only
works in your project folder, it is a script, not a procedure.**

**Time.** 30 minutes. **Level.** Extension.

---

## 10. The reference acceptance procedure and record

`09-project/reference-implementation/acceptance/` · **Confident.**

**Why these.** The procedure has a platform line that is one line long, eight cases
with two failure cases, and a section recording what the stakeholder changed. The
record has a **Known and not fixed** section with three real entries.

**Read `corrections.md`.** It has the real before-and-after capture, including a
traceback, and it makes the point that an unhandled exception and a recorded failure
are different things that a scheduler cannot tell apart.

**Time.** 20 minutes. **Level.** On-level.

---

## 11. The free book chapter for the week

**Automate the Boring Stuff with Python, the scheduling and launching chapter** ·
`https://automatetheboringstuff.com/` · **Confident**, free to read online.

**Why this one.** It is the standard free treatment of exactly what Tuesday is
about: making something run without a person starting it, using `time.sleep`, the
`schedule` idea, and the operating system's own scheduler.

**What to take and what to leave.** Take the shape of a loop that waits and fires.
**Leave the part where the program does the work and says nothing about it**, because that is the version
this lab is teaching you to stop writing.

**Time.** 45 minutes. **Level.** On-level.

---

## 12. This week's lecture notes

`03-lecture-notes/` · **Confident.**

| Day | Note |
|---|---|
| Mon | `MCCTC_145130_Notes_TheWireframeThatAnswersAQuestion.md` |
| Tue | `MCCTC_145130_Notes_AnAutomationWithARealErrorPath.md` |
| Wed | `MCCTC_145130_Notes_WhereItIsWorthApplyingAI.md` |
| Thu | `MCCTC_145130_Notes_TheAcceptanceProcedure.md` |

**If you read one, read Tuesday's**, and specifically worked example 1, which has
two identical runs and two identical file hashes and no exception anywhere.

**Time.** 20 minutes each. **Level.** Review.

---

## 13. [VERIFY] n8n, if it is available this year

`https://docs.n8n.io/` · **[VERIFY]**, and **n8n is not installed on the build
machine**, so nothing in this module using it has been tested.

**Ask your instructor on Monday whether it is available.** If it is, the same
automation is five nodes: a Schedule Trigger, a file read, an IF comparing the
newest file time against a stored value, an HTTP Request per note, and a file write
with a branch to an incident file.

**The four things you are graded on are identical in either tool:** every step says
what it expected and what it got, a step that produced nothing from non-empty input
is a failure, a failed run still writes a record, and the incident names what to
check, who to ask, and what happens if nobody does.

**If you build it in n8n, you also write down which parts of the lab you could not
do in it.** That list is the interesting part and it is worth marks.

**Time.** 30 minutes. **Level.** Extension.
