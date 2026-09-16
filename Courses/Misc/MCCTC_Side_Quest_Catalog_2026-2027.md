# Side Quest Catalog
## AI Automation & Software Development · MCCTC · 2026-2027

**What a side quest is.** An optional, self-contained build that extends something
from class. Fridays are for these, along with BPA preparation and catch-up. They are
graded under **BPA / Credential / Capstone**, which is 10 percent of the course
grade in all four courses.

**What a side quest is not.** It is not extra credit for finishing early, and it is
not busywork. Every quest below produces something that exists afterward: a program
that runs, a document somebody could use, or a repository you would show an
interviewer.

---

## Rules that apply to every quest

1. **It lives in a repository.** Work that is not committed is not submitted. Same
   rule as everything else.
2. **The README is part of the grade.** What it is, how to run it, what it does when
   it works.
3. **You must be able to explain it.** The only way to fail outright in this program
   is to submit work you cannot explain. That includes side quests.
4. **AI runs on locally hosted models.** No quest in this catalog requires a student
   to hold a commercial API key, and none ever will. Commercial developer APIs
   require users to be 18 or older.
5. **Free tiers only.** No quest requires a credit card. Deployment is Render, free
   tier.
6. **No personal data in any AI tool.** Ever, on any quest.

---

## How to use this catalog

**Numbering is stable.** SQ-01, SQ-02, SQ-05, SQ-10, and SQ-13 are named in the
145060 syllabus and keep those numbers permanently. Do not renumber them.

**Difficulty** is relative to where a student is when the quest unlocks, not
absolute.

| Tier | Meaning |
|---|---|
| ★ | One Friday. Most students finish. |
| ★★ | One to two Fridays. Requires something not taught. |
| ★★★ | Multi-week. Suitable as a BPA or competition entry. |

**Competency codes** are verified against the Ohio DEW Outcome & Competency
Descriptions in `Courses/145060/_source/COMPETENCY_REFERENCE.md`.

---

# Junior Year · 145060 Programming

## SQ-01 · Hello, Version Control
**Unlocks:** Unit 0, Week 1 · **Time:** one block · **Difficulty:** ★
**Competency:** 5.1.8, 5.4.1, 5.4.2, 1.2.12

**Required before any other work in this course is graded.** Delivered as Lab
U0-01. Create a repository, write a `.gitignore` before the first commit, write a
program that runs, write a README a stranger can follow, and push it.

**Done when:** the repository is on GitHub with three or more commits whose messages
say why, `.gitignore` is the first commit, and nothing in it should not be there.

---

## SQ-02 · The Regex Wrangler
**Unlocks:** Unit 1, Week 3 · **Time:** one to two blocks · **Difficulty:** ★★
**Competency:** 5.2.4 (string operations including pattern matching)

Regular expressions are the tool for finding structure inside text. You have not
been taught them. That is the quest.

Build a program that reads a block of messy text you actually have, a group chat
export, a copied schedule, a list of assignment titles, and pulls out every item
matching one pattern: dates, times, phone-shaped numbers, dollar amounts, or
anything else with a shape.

**Start here:** the Python documentation page for the `re` module, and the
`re.findall` function specifically. Read the first section only.

**Done when:** your program finds every match in your sample text, you can explain
what each character in your pattern does, and your README shows the input and the
output side by side.

**Stretch:** find the case your pattern misses. There is always one. Write it in
`Known limitations`.

---

## SQ-03 · The Terminal Is Not Scary
**Unlocks:** Unit 0, Week 2 · **Time:** one block · **Difficulty:** ★
**Competency:** 5.4.1

Learn twelve shell commands well enough to navigate without a mouse. Change
directories, list files, make and remove folders, copy, move, read a file, search
inside files, and clear the screen.

**Done when:** you can complete a scavenger hunt through a folder tree, provided by
the instructor, using only the terminal, and your README documents each command in
your own words with one example.

**Why it matters:** every quest after this one is faster, and every remote server
you ever touch has no graphical interface.

---

## SQ-04 · Number Bases by Hand
**Unlocks:** Unit 1, Week 4 · **Time:** one block · **Difficulty:** ★
**Competency:** 2.3.1, 2.3.2 · **Exam weight: 4.44%**

Write a converter between binary, decimal, and hexadecimal **without** using
Python's built-in `bin()`, `hex()`, or `int(x, base)`. Doing it by hand is the
point, because the WebXam asks you to do it by hand.

**Done when:** your program converts in all six directions, you have checked at
least five values against Python's built-ins, and your README explains the
algorithm in plain English.

**Stretch:** add ASCII. Print the character for a number and the number for a
character, and explain what Unicode adds to that picture.

---

## SQ-05 · Bug Hunt
**Unlocks:** Unit 3, Week 7 · **Time:** one block · **Difficulty:** ★★
**Competency:** 5.4.6, 5.4.7, 5.6.13

**Materials are built and in `side-quests/SQ-05-Bug-Hunt/`.** `torch_run.py` is a
113-line dungeon crawl with **seven** planted defects and a runnable test suite,
`test_torch_run.py`. Students find them, document each, and fix them without breaking
anything else.

**Done when:** `python test_torch_run.py` reports 8 passed 0 failed, and `BUGS.md`
has an entry per defect naming the line, what it did, what it should have done, the
fix, and how they found it.

**The rule that makes it hard:** you may not rewrite the program. You may only fix
it. Rewriting is how students avoid learning to read code they did not write, and
reading code you did not write is most of a real job.

---

## SQ-06 · Flowchart the Thing You Already Built
**Unlocks:** Unit 3, Week 6 · **Time:** one block · **Difficulty:** ★
**Competency:** 5.1.3, 5.6.7

Take a program you already wrote and produce a flowchart and an IPO chart for it,
after the fact. Then hand both to somebody who has not seen your code and ask them
to describe what the program does.

**Done when:** your reader's description matches what the program actually does. If
it does not, the diagram is wrong, and fixing it is the assignment.

**Why after the fact:** modeling before coding is taught in Unit 3 and most students
do not believe in it. Doing it backwards on your own code shows you what the diagram
would have caught.

---

## SQ-07 · The Halloween Build
**Unlocks:** Unit 3, Week 8 · **Time:** two blocks · **Difficulty:** ★★
**Competency:** 5.3.6, 5.3.8, 5.1.2

Extend your text adventure with something genuinely unsettling: a room that changes
when you return to it, an inventory item that goes missing, an exit that only appears
after you have visited three other rooms.

**Setting is your choice and horror is optional.** A haunted house, a school after
hours, a spacecraft, a normal Tuesday that stops being normal.

**Done when:** the state change works reliably, you can explain the condition that
triggers it, and one classmate has played it start to finish without your help.

---

## SQ-08 · Deploy Something Nobody Asked For
**Unlocks:** Unit 8, Week 18, or any time after · **Time:** two blocks · **Difficulty:** ★★
**Competency:** 5.6.16, 5.6.8

Put something on the public internet. Render, free tier, no credit card. It does not
have to be impressive. It has to be live, at a URL you can send to somebody.

**Done when:** the URL loads from a phone on cell data, not school wifi, and your
README explains what deployment actually did to your code.

**The lesson:** the gap between "it works on my machine" and "it works" is larger
than it looks, and everybody underestimates it exactly once.

---

## SQ-09 · The Automation That Saves You Ten Minutes
**Unlocks:** Unit 5, Week 11 · **Time:** one to two blocks · **Difficulty:** ★★
**Competency:** 5.5.7, 5.5.3, 5.1.1

Pick a real item from your Problem Inventory. Automate it. File renaming, sorting
downloads, pulling numbers out of a spreadsheet into a summary, reformatting
something you retype every week.

**Done when:** you have used it at least three times on real data, and your README
states honestly how much time it saves and how long it took to build. Those two
numbers are often embarrassing and reporting them accurately is part of the grade.

---

## SQ-10 · API First Contact
**Unlocks:** Unit 7, Week 16 · **Time:** two blocks · **Difficulty:** ★★
**Competency:** 5.5.4, 5.5.7, 9.3.3

Consume a public API that needs no key and no account. Weather, transit, earthquakes,
public data portals. Read the response, parse it, and print something a person would
actually want.

**Then break it on purpose.** Turn off the network. Request something that does not
exist. Request it fifty times fast.

**Done when:** your program handles a 404, a timeout, and a rate limit **distinctly**,
with a message that tells the user which one happened and what to do about it.
Printing "Error" for all three fails this quest.

**No API keys.** If a service wants a key, pick a different service.

---

## SQ-11 · Thirty Scripts Moving the Mouse
**Unlocks:** Unit 5 or later · **Time:** one block · **Difficulty:** ★★
**Competency:** 5.5.3, 5.1.1

Automate a graphical application with PyAutoGUI. Move the mouse, click, type,
screenshot, find an image on screen.

**This is a side quest and never a whole-class lab, deliberately.** Thirty scripts
moving thirty mice simultaneously is a bad afternoon for everyone.

**Rules:** on your own machine or a designated station, never on a shared display,
and your script must have a failsafe that stops it. Read the PyAutoGUI documentation
on failsafes **before** you write anything that moves the pointer.

**Done when:** it completes a real repetitive task, and you can stop it instantly.

---

## SQ-12 · Read the Source
**Unlocks:** any time after Unit 4 · **Time:** one block · **Difficulty:** ★★
**Competency:** 5.1.6, 5.6.13, 1.2.1

Find a small open-source Python project on GitHub, under about 500 lines. Read it.
Write a two-page report: what it does, how it is organized, one thing the author did
that you would not have thought of, and one thing you would change.

**Then check its license** and state what shipping it in your own project would
require of you.

**Done when:** the report exists and your reading is specific enough to quote line
numbers.

---

## SQ-13 · The Scraper
**Unlocks:** Unit 5, Week 11 · **Time:** two blocks · **Difficulty:** ★★★
**Competency:** 5.5.7, 5.3.11, 1.7.13

Extract structured data from a website that does not offer an API, clean it, and
output a report with calculated fields.

**The constraints are the quest, and they are not optional:**

- Read `robots.txt` first and obey it. Put what it said in your README.
- Read the site's terms of service. Quote the relevant sentence.
- Rate limit yourself to at most one request every two seconds.
- Never scrape anything behind a login.
- Never collect personal information about anybody.
- If the site offers an API, use the API instead and say so.

**Done when:** you have a clean dataset, a report with at least one calculated
field, and a README section titled `Why this was allowed` that cites the robots file
and the terms.

**A student who decides mid-quest that a site should not be scraped, and writes up
why, has completed this quest.** That judgment is the skill.

---

## SQ-14 · The Local Model in Your Program
**Unlocks:** Unit 7, Week 16 · **Time:** two blocks · **Difficulty:** ★★★
**Competency:** 5.5.4, latent 2.14.3, 2.14.4

Call the lab's locally hosted model from your own Python code. Send it a prompt,
receive the response, parse it, and use it for something inside a program you wrote.

**Then measure it.** Run the same prompt ten times. Record how the output varies.
Time it.

**Done when:** your program works, and your README contains a table of the ten runs
with an honest assessment of validity, relevance, and hallucinations across them.

**The finding most students report:** the same prompt does not give the same answer,
and building on top of that is a genuinely different engineering problem. Say so in
your write-up.

---

# Junior Year · 145065 Object-Oriented Programming

## SQ-15 · Same Program, Two Languages
**Unlocks:** 145065, C# half · **Time:** two blocks · **Difficulty:** ★★
**Competency:** 5.1.4, 5.1.6

Take a working Python program of yours and rewrite it in C#. Same behavior, same
output.

**Done when:** both produce identical output on the same inputs, and your README has
a section on what was harder in each language and what each one made obvious.

---

## SQ-16 · The Class That Should Not Be a Class
**Unlocks:** 145065, after inheritance · **Time:** one block · **Difficulty:** ★★
**Competency:** 5.1.4, 5.3.12

Find an example, in your own old code or in a public project, where somebody used a
class and a function would have been better. Rewrite it both ways.

**Done when:** you can argue both sides in writing, and you commit to one with
reasons. There is no correct answer and the argument is the grade.

---

## SQ-17 · Unit Tests for Something You Already Wrote
**Unlocks:** 145065 · **Time:** one to two blocks · **Difficulty:** ★★
**Competency:** 5.4.4, 5.4.5, 5.6.14

Write a real test suite for an old program. Cover the normal case, the edge cases,
and at least three inputs designed to break it.

**Done when:** the suite runs, at least one test **fails** and exposes a real defect
you did not know about, and you fixed it.

**If nothing fails, you have not tried hard enough.** Write nastier tests.

---

# Senior Year · 145130 Applications of AI

## SQ-18 · Prompt Ablation
**Unlocks:** 145130, Module 2 · **Time:** one block · **Difficulty:** ★★
**Competency:** 2.14.3, 2.14.4

**Materials are built and in `side-quests/SQ-18-Prompt-Ablation/`.** A base prompt, an
ablation runner, a stub model server so it runs with no model installed, and a self-check.

Take one prompt that works. Remove one element at a time, run it again, and record
what changes. Role, format instruction, examples, constraints, tone.

**Done when:** you have a table of at least eight variants with results, and a
conclusion about which element was doing the most work. Most students are surprised.

---

## SQ-19 · The Bias Audit
**Unlocks:** 145130, Module 3 · **Time:** two blocks · **Difficulty:** ★★★
**Competency:** 2.14.2, 2.14.4, 2.14.6

**Materials are built and in `side-quests/SQ-19-The-Bias-Audit/`.** A probe runner, an
analyzer, and a stub model server so the method is testable with no model installed.

Design a repeatable test for bias in a locally hosted model's output. Ask for the
same kind of thing many times, varying only one detail, and record what changes.

**Rules:** no real people, no student data, no classmates as subjects. The test must
be something anybody could rerun from your written method.

**Done when:** your method is written clearly enough to reproduce, you have at least
30 recorded outputs, and your conclusion distinguishes what you measured from what
you suspect.

**The hardest part is designing a test that could come out either way.** A test that
can only confirm what you already believed is not a test.

---

## SQ-20 · Explain It to a Seventh Grader
**Unlocks:** 145130 · **Time:** one block · **Difficulty:** ★
**Competency:** 2.14.2, 1.2.5

Write and record a five-minute explanation of how a language model produces text,
aimed at a twelve-year-old. No jargon that you do not define.

**Done when:** an actual younger student, a sibling or a middle-school class, can
answer three comprehension questions afterward.

**Why:** you cannot explain what you do not understand, and this is the fastest way
to find out which you have.

---

# Senior Year · 145010 Web Design & Capstone

## SQ-21 · The Accessibility Pass
**Unlocks:** 145010 · **Time:** one to two blocks · **Difficulty:** ★★
**Competency:** 145010 outcome 6.1, 6.5, latent 2.15.3

Take a page you built. Navigate it using only the keyboard. Then run it through a
screen reader with your eyes closed.

**Done when:** you can complete every task on the page without a mouse and without
looking, and your README lists what you fixed and what you could not.

**Most students find their own page unusable within ninety seconds.** That is the
quest working.

---

## SQ-22 · Make It Load in Under a Second
**Unlocks:** 145010 · **Time:** one block · **Difficulty:** ★★
**Competency:** 145010 outcome 6.5, 2.12

Measure your page's load time. Then cut it in half without removing features.

**Done when:** you have before and after measurements taken the same way, and your
README explains each change and what it cost you.

---

## SQ-23 · The Form That Fights Back
**Unlocks:** 145010, after forms · **Time:** two blocks · **Difficulty:** ★★★
**Competency:** 145010 outcome 6.4, 9.3.3, 5.5.1

Build a form. Then attack your own form: empty fields, absurdly long input, script
tags, SQL-shaped strings, emoji, right-to-left text.

**Done when:** every attack is handled with a message a normal person would
understand, nothing crashes, and your README documents each attack and the defense.

**Never attack a site you do not own.** Yours only. This rule is in the Lab
Acceptable Use and Safety Agreement and it is not negotiable.

---

## SQ-24 · Ship for a Real Stakeholder
**Unlocks:** 145010 capstone, or any time with instructor approval · **Time:** multi-week · **Difficulty:** ★★★
**Competency:** 5.6.1, 5.6.10, 5.6.15, 5.6.17, 1.2.2

Find somebody outside this class who has a problem, and solve it for them. A club, a
teacher, a coach, a family business, a nonprofit.

**Requirements:** a written agreement on scope before you start, at least two
meetings with them, a delivered working thing, and a handoff document they can use
without you.

**Done when:** the stakeholder confirms in writing that they are using it, or
explains why they are not. **Both outcomes complete the quest.** A build that was
not adopted, with an honest account of why, teaches more than one that was.

---

## Instructor notes

### Assigning these
Do not hand out a menu on day one. Unlock quests as their prerequisites land, and
name a specific quest to a specific student when you see the signal for it. A quest
handed to the right student at the right moment gets finished. A list emailed to
thirty students gets read by none.

### Grading
BPA / Credential / Capstone, 10 percent. Use the Project rubric scaled to the quest,
or the 30-point Problem Drop rubric for the smaller ones. Every quest's "Done when"
is written to be checkable without judgment calls.

### The five syllabus-named quests
SQ-01, SQ-02, SQ-05, SQ-10, and SQ-13 appear by number in the 145060 syllabus.
Those numbers are fixed. Everything else in this catalog was built to fill the gaps
and can be renumbered or replaced.

### SQ-05 is built
`side-quests/SQ-05-Bug-Hunt/` holds the student brief, the defective program, the
test suite, and an instructor key with a reproduction command for every defect. The
suite was verified at 7 failed against the shipped program and 8 passed against the
reference fix. The fixed file lives in `instructor/` so it is not in the folder
students work in.

### Gaps worth filling later
No quest currently covers outcome 5.7 Configuration Management (6.67% of the 145060
exam) or 1.3.7 labor laws. Both are candidates for new quests. The 1.3.7 gap is
noted in `Courses/145060/_source/COMPETENCY_REFERENCE.md` and needs a decision about
where it lives.

---

**Version 1.0 · September 2026.** Produced for this program because no catalog
existed. Numbers for the five syllabus-named quests are authoritative. The other
nineteen are proposals and should be edited freely.
