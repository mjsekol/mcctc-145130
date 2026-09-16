# Additional Resources · Week 15
## 145130 Applications of AI · Module 5 · Week 15
### Topics: implementation and contingency plans, user help for a non-developer, the peer walkthrough and code review

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed
live. Click it before you rely on it.

**This week you are writing, not building.** That changes what a good resource is. Almost everything
here is either a document in this repository that you can hold your own work against, or a short piece
of writing guidance you can apply in the same period you read it.

**Nothing here requires an account or a commercial AI developer API.** Those services require their
users to be 18 or older, and this course does not use them.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Google Technical Writing One | Tue | On-level | 60 min |
| 2 | The Write the Docs documentation guide | Tue | On-level | 30 min |
| 3 | Plain language guidelines | Tue | Remediation | 25 min |
| 4 | Official docs: Python `unittest` | Mon | On-level | 20 min |
| 5 | RFC 2119, the words that make a requirement testable | Mon | Extension | 10 min |
| 6 | Interactive: `doc_check.py` against your own documents | Mon-Wed | On-level | 20 min |
| 7 | Interactive: the flawed documentation set in Lab M05-04 | Tue | On-level | 45 min |
| 8 | This week's three lecture notes and their self-checks | Any | Review | 20 min each |
| 9 | The reference implementation plan and contingency plan | Mon | On-level | 30 min |
| 10 | The reference user help | Tue | On-level | 25 min |
| 11 | The run book and the contract, as models for two sections you owe | Tue | On-level | 30 min |
| 12 | The acceptance runner, which is what "finished" means | Mon, Thu | On-level | 20 min |
| 13 | Industry connection: how code review is actually run at scale | Wed | Extension | 45 min |
| 14 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 15 | SQ-05 Bug Hunt, and the extension that needs a real person | Fri | Extension | 1 block |

---

## 1. Primary reading

**Google Technical Writing One** · `https://developers.google.com/tech-writing` · **[VERIFY]** before
you assign it. It is free to read, and the reading portion needs no account.

**Why this one.** It is short, it is written for engineers who did not sign up to be writers, and every
section ends with an exercise you do on your own text rather than on an example. Four of its lessons
map directly onto what you owe this week.

**The four sections worth your time, and what each one fixes in your user help.**

| Section | What it fixes |
|---|---|
| Words, and defining new terms | your message table, which currently contains the word "envelope" |
| Active voice | "the request was refused" becomes "the service refused your request" |
| Short sentences | the row in your table that runs to three lines and gets skipped |
| Lists and tables | the paragraph that should have been four numbered steps |

**Do the active voice exercises on your own user help, not on the book's examples.** The book's examples
are already broken in an instructive way. Yours are broken in your way, and yours is the one you have
to fix.

**Time.** 60 minutes for the four sections. **Level.** On-level.

---

## 2. Write the Docs

**The Write the Docs documentation guide** · `https://www.writethedocs.org/guide/` · **[VERIFY]**. Free,
no account, written by people who do this for a living.

**Why this one.** It is the best free source on the question Tuesday's lesson opens with: who is this
document for, and what were they doing when they reached for it. The guide is organised around
document types rather than around tools, so you can find the page about the kind of thing you are
writing.

**The idea to take from it.** A single document that tries to be a tutorial, a reference, and a
troubleshooting guide at once is worse at all three than three short documents would be. Your user help
is a troubleshooting guide with a short starting section in front of it. It is not a description of
your architecture, and every paragraph about your architecture that survives into it is a paragraph
that tells the reader this file was not written for them.

**Time.** 30 minutes. **Level.** On-level.

---

## 3. Writing for somebody who is annoyed

**The federal plain language guidelines** · `https://www.plainlanguage.gov/guidelines/` · **[VERIFY]**.
Free, no account.

**Why this one.** It is guidance for writing things that people read when they are stressed, behind, and
not in the mood, which is exactly the state of the person opening your user help. It covers the three
rules from Tuesday's lesson in more detail than the lesson has room for: address the reader directly,
say what to do rather than what happened, and use the words the reader already has.

**The test to run on your own message table.** Cover the first column and read only the third. Every
row should still be an instruction a person could follow. If a row reads "the deserialisation failed",
that row is describing your program to itself.

**Time.** 25 minutes. **Level.** Remediation.

---

## 4. The official documentation page for the week

`https://docs.python.org/3/library/unittest.html` · **Confident.**

**Why a testing page in a writing week.** Because of one row in the implementation plan: *how you know
it is finished is a command somebody else runs, that says pass or fail.* "It works on my machine" is
not on that list, and the only way off that list is a command.

**Read three things and stop.** How a test case is written, what `assertEqual` and `assertRaises` do,
and how to run a whole folder of tests from the command line. That last one is the line you put in your
implementation plan under "finished when".

**Assign a question:** *What is the difference between a test that fails and a test that errors, and
why does the runner report them separately?* A team that cannot answer that will report a broken test
file as a broken feature.

**Time.** 20 minutes. **Level.** On-level.

---

## 5. The words that make a requirement testable

**RFC 2119, Key words for use in RFCs to indicate requirement levels** ·
`https://www.rfc-editor.org/rfc/rfc2119` · **Confident.**

**Why this one.** It is two pages. It defines MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY, and it is
the reason standards documents can be argued about precisely.

**What it is for this week.** Your implementation plan and your contingency plan are full of sentences
like "the service should answer quickly". Rewrite each one using a word from this list and a number,
and watch how many of them turn out to have been decisions you had not made yet. "The client's timeout
MUST exceed the service's worst case" is a sentence somebody can fail you on. "Should be long enough"
is not.

**The honest caveat.** Nobody expects your plan to read like an RFC, and a document written entirely in
capital letters is harder to read, not clearer. Use the distinction, not the typography.

**Time.** 10 minutes. **Level.** Extension.

---

## 6. Interactive practice: check your own documents

[doc_check.py](../09-project/project-files/doc_check.py) · **Confident**, it is in this repository.

**Why this one.** Milestone M1 is defined as this script reporting your design documents complete. Run
it on your own repository before Monday is over, not on Thursday. A missing section found on Monday is
a conversation. The same section found on Thursday is a scramble.

**Run it, read what it complains about, and then read what it does not check.** It cannot tell you
whether your I/O specification is right, only whether it is there. The part it cannot check is the part
the walkthrough exists for.

**Time.** 20 minutes. **Level.** On-level.

---

## 7. Interactive practice: audit somebody else's documentation

[Lab M05-04, The Documentation Autopsy](../05-labs/MCCTC_145130_Lab_M05-04_TheDocumentationAutopsy.md) ·
**Confident**, with its [instructor key](../05-labs/MCCTC_145130_Lab_M05-04_TheDocumentationAutopsy_KEY.md).

The lab ships a complete documentation set from an invented team, and it is wrong in ways that look
right at a glance. Eight files:

| File | What to look for |
|---|---|
| [io-specification.md](../05-labs/lab-m05-04-files/submitted-docs/design/io-specification.md) | a field with a type and no range |
| [ipo-chart.md](../05-labs/lab-m05-04-files/submitted-docs/design/ipo-chart.md) | the input row that is missing |
| [dataflow-diagram.md](../05-labs/lab-m05-04-files/submitted-docs/design/dataflow-diagram.md) | a boundary with nothing checked at it |
| [data-dictionary.md](../05-labs/lab-m05-04-files/submitted-docs/design/data-dictionary.md) | a field that disagrees with the I/O specification |
| [implementation-plan.md](../05-labs/lab-m05-04-files/submitted-docs/docs/implementation-plan.md) | a milestone you cannot point at |
| [contingency-plan.md](../05-labs/lab-m05-04-files/submitted-docs/docs/contingency-plan.md) | a risk with no named owner |
| [user-help.md](../05-labs/lab-m05-04-files/submitted-docs/docs/user-help.md) | a message the program prints that is not in the table |
| [troubleshooting-log.md](../05-labs/lab-m05-04-files/submitted-docs/docs/troubleshooting-log.md) | four changes at once and no verification |

**Why auditing somebody else's set is the practice, not reading a good one.** You know what your own
documents mean, so you cannot see what they fail to say. On a stranger's documents that protection is
gone, and the gaps are visible in ten minutes. Then you go back to your own with the same eyes.

**Time.** 45 minutes. **Level.** On-level.

---

## 8. This week's lecture notes

| Day | Notes |
|---|---|
| Monday | [The implementation plan and the contingency plan](../03-lecture-notes/MCCTC_145130_Notes_ImplementationAndContingencyPlans.md) |
| Tuesday | [User help for the person who is stuck](../03-lecture-notes/MCCTC_145130_Notes_UserHelpForThePersonWhoIsStuck.md) |
| Wednesday | [The peer walkthrough](../03-lecture-notes/MCCTC_145130_Notes_ThePeerWalkthrough.md) |

**The hardest sentence of the week is in Wednesday's notes, and it is not about code.**

> The author does not defend.

When a reviewer says they do not understand a part, your only job is to write that down. The
explanation you want to give out loud is the thing that is missing from the document, and saying it in
the room removes the problem from the room without removing it from the work. You will do this in the
first five minutes and your partner should stop you.

**Time.** 20 minutes each. **Level.** Review.

---

## 9. The reference implementation plan and contingency plan

[implementation-plan.md](../09-project/reference-implementation/docs/implementation-plan.md) ·
**Confident.**
[contingency-plan.md](../09-project/reference-implementation/docs/contingency-plan.md) · **Confident.**

**Why these two together.** They are read at different times by different people, and that is the whole
reason they are two documents. The implementation plan is read on a good day by somebody deciding what
to do next. The contingency plan is read on a bad day by somebody already behind, and possibly not by
you.

**The row to copy from the implementation plan:** every item under "before you start" is a check with a
yes or no answer, not a piece of work. Every one of them has cost somebody in this lab a morning.

**The section to copy from the contingency plan:** the cut list, in order, written in advance. Cutting
on Monday is a decision. Cutting on Thursday is a panic, and by Thursday you are too invested in the
second task to cut it.

**Hold both against your own.** The test for either document is the same: could somebody run this
project on a day you are not there? In this module that is not hypothetical, because one of you may
have been out of the building all of Week 14.

**Time.** 30 minutes. **Level.** On-level.

---

## 10. The reference user help

[user-help.md](../09-project/reference-implementation/docs/user-help.md) · **Confident.**

**Why this one.** It is the model for the document you owe on Tuesday, and the section worth studying is
the one about fallbacks, because that section only exists in help for a program with a model in it.

**Read the second column of its message table and notice what is absent.** No word from inside the
program. Not "deserialise", not "envelope", not a class name. The reader does not have those words and
does not need them.

**Then read the fallback section and ask what it is protecting the reader from.** It is protecting them
from acting on a page of first sentences and believing a model wrote them. It ends in a decision the
reader is allowed to make, which is the correct ending for a section about output you cannot fully
trust.

**Time.** 25 minutes. **Level.** On-level.

---

## 11. Two more in-repository documents you should read as writing

[Lab M05-01](../05-labs/MCCTC_145130_Lab_M05-01_TraceTheContract.md) · **Confident.** Read this as the model
for the "how to start it" section of your own user help. Every command is complete, every command names
its port, and every block of output is what you actually see rather than a description of it.

[CONTRACT.md](../05-labs/lab-m05-01-files/CONTRACT.md) · **Confident.** Read this when you are
building your message table, because the list of error kinds in it is the list of things your program
can say. **Rule one of user help is that every message the program can print is in the table.** The
contract is where you get the complete list, and a complete list is the difference between help that
earns a second visit and help that does not.

**Time.** 30 minutes for both. **Level.** On-level.

---

## 12. What "finished" means, as a command

[run_acceptance.py](../09-project/reference-implementation/acceptance/run_acceptance.py) · **Confident.**

**Why this one.** Your implementation plan has a column called "how you know it is finished", and this
is what belongs in it: a script somebody else runs that prints pass or fail. Read it to see how each
requirement turned into one check.

**The thing to notice.** The acceptance checks are written against the requirements, not against the
code. A check that says "the function returns a dictionary" is testing the implementation. A check that
says "a prompt of 4001 characters is refused with HTTP 400 and the model is never called" is testing
the requirement, and it stays true when you rewrite the function.

**Then write three of your own.** Three requirements from your I/O specification, three checks, one
command. That is the strongest single line you can put in your implementation plan.

**Time.** 20 minutes. **Level.** On-level.

---

## 13. Industry connection: how code review is actually run

**Google's engineering practices documentation, the code review guide** ·
`https://google.github.io/eng-practices/review/` · **[VERIFY]** before you assign it. Free, no account.

**Why this one.** Wednesday's walkthrough is the in-person version of something that mostly happens in
writing now, and this guide is the most widely read free description of how the written version works.
Two parts of it matter to you this week: the standard the reviewer is asked to hold to, and the guidance
on how to write a review comment somebody can act on.

**The line from it that maps onto your severity table.** A reviewer is not asked to demand perfection.
They are asked to decide whether the change definitely improves the system. That is the same judgement
your Blocker, Major, and Minor scale is making, and it is the reason "I would have done it differently"
is not a finding.

**A second, more specific source: [VERIFY].** Search for the paper **Modern Code Review: A Case Study at
Google**, which is published free by its authors. It reports what review is actually used for in
practice, and the finding that surprises people is that defect-finding is not the main thing reviewers
do. Knowledge transfer and keeping the codebase readable score higher. Bring that to Wednesday and
argue about it, because it changes what you should be asking your reviewer for.

**Where your walkthrough is still better than a written review.** A walkthrough catches disagreements
between the documents and the code, and a written review of a code change usually never opens the
documents at all. That is why Wednesday's script puts documents first and holds the code against them.

**Time.** 45 minutes. **Level.** Extension.

---

## 14. A free video

**[VERIFY].** No specific video is named, because a wrong title and a wrong channel cost more than no
link.

**What to search for, and there are two useful directions.**

**On the review side:** search for a short video on **software inspection** or **code walkthrough**, and
look for one that names the roles of author, reviewer, and recorder. A video that treats a walkthrough
as a demo of working features is describing the wrong exercise, and you can tell inside two minutes.
The background term to search alongside it is **Fagan inspection**, which is the original formal
version of what you are doing on Wednesday.

**On the writing side:** search for a short talk on **writing error messages** or on **documentation for
users**. A conference talk from a documentation conference is usually the right length and is usually
posted free.

**Three tests before you commit to one.** It shows real text or real code on screen. It is under 20
minutes. It does not require you to install or register for anything.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 15. Side quest and extensions

**SQ-05 Bug Hunt** · [the bundle](../../../../Misc/side-quests/SQ-05-Bug-Hunt/README.md) ·
**Confident**, it is in this repository. One block, difficulty ★★.

**Why it fits this week.** Seven defects in a program somebody else wrote, and the rule is that you may
fix but not rewrite. That is a code review with the fixes attached, and the constraint teaches the
thing Wednesday is about: reading somebody else's work well enough to change one part safely and leave
the rest working.

### The extension that matters most, and it needs a person

**Test your user help on somebody who did not build your program.** A friend in another class, a
sibling, a teammate from another team. Hand them the document and the running program and say nothing
else. Then watch, and write down every moment they stop.

**You are not allowed to help them.** The moment you explain something out loud is the moment you have
found a gap in the document and hidden it. Write the question down instead. Every question they ask is
a row your table is missing.

**The measure.** Somebody who has never seen the program should be able to start it and understand one
failure message, using your help alone, in under ten minutes. If they cannot, you have a finding, and a
finding with a fix in it is worth more in Thursday's assessment than a document with no findings
against it.

### A second extension, for the team that is ahead

**Write the contingency plan entry for a risk that already happened to you.** Go back through Week 14's
troubleshooting log, pick the failure that cost you the most time, and write the risk row you would
have needed in Week 13 to have handled it in ten minutes instead. That is the one row in your plan you
can prove is worth having.

**Time.** One block for SQ-05, 30 minutes for the help test, 20 minutes for the risk row.
**Level.** Extension.

---

## For the student who is behind

1. Tuesday's lecture notes, the message table, and nothing else from that file yet
2. [The reference user help](../09-project/reference-implementation/docs/user-help.md), read once as a
   reader rather than as a writer
3. Your own program run against a stopped service, with every line it printed copied into your table
4. [doc_check.py](../09-project/project-files/doc_check.py), so you know what is missing before Thursday

## For the student who is ahead

- RFC 2119, applied to every requirement sentence in your implementation plan
- The code review reading in section 13, and a position in your decision log on what review is for
- Three acceptance checks of your own, written against requirements rather than against functions
- The user help test with a real person, which is the hardest thing on this page and the most useful
