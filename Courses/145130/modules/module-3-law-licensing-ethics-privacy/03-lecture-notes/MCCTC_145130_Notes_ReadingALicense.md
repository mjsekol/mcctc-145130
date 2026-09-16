# Lecture Notes: Reading a License Instead of Reading About One
## 145130 Applications of AI · Module 3 · Week 7, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W07_ReadingALicense.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W07_ReadingALicense.pptx)

If you missed class, you can learn this concept from this file alone. Open every license
this file names and read it while you read this.

**Competencies:** 9.6.1 (adhere to licensing and intellectual property laws), 1.3.8
(verify compliance with computer and intellectual property laws and regulations), 1.7.13
(protect intellectual property and knowledge).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** More than that,
this file is deliberately not a license summary table. Summary tables are how people get
this wrong, and you are going to watch one fail later in this file.

Where this file describes what a license does, the license text is what governs, and the
license text is published by the people who wrote it:

- **The Open Source Initiative** maintains the Open Source Definition and a list of
  approved licenses, including the full text of many of them.
  `https://opensource.org/licenses` **[VERIFY]**
- **The Apache Software Foundation** publishes the Apache License, Version 2.0.
  `https://www.apache.org/licenses/LICENSE-2.0` **[VERIFY]**
- **The Free Software Foundation** publishes the GNU General Public License.
  `https://www.gnu.org/licenses/` **[VERIFY]**
- **Creative Commons** publishes its licenses. Every Creative Commons page has a short
  human-readable deed and, linked from it, the legal code. **The deed is a summary. The
  legal code is the license.** `https://creativecommons.org/licenses/` **[VERIFY]**

---

## Why this exists

Yesterday you learned that a project is a stack of works owned by different people. Today
you learn how to find out what each of those people actually let you do.

Here is the thing that makes this worth a whole day. **A license is a document written to
be read, and almost nobody reads it.** People read a table, or a badge on a repository
page, or an answer a model gave them. Then they get it wrong in a specific direction: they
believe permissive licenses have no obligations and copyleft licenses forbid selling
things. Neither of those is true, and both are believed by a lot of working developers.

You can be better than that by the end of this period, because the skill is small. It is
three questions, asked in order, with the text open.

---

## The three questions

Every license answers these three. Write the answers down in these words, because your
licensing audit asks for exactly them.

1. **What does it PERMIT?** What are you now allowed to do that you were not allowed to do
   before? Use, copy, modify, distribute, sublicense, sell.
2. **What does it REQUIRE?** What do you have to do in exchange? Keep a notice, ship a
   copy of the license, state your changes, credit the author in a particular form, pass
   the same license along.
3. **What does it FORBID?** What is off limits no matter what? Some licenses forbid almost
   nothing. Some forbid commercial use. Some forbid whole categories of application.

Then a fourth question that decides whether any of it is live today:

4. **What triggers the requirements?** Most conditions in most software licenses are
   written about **distributing** or **conveying** the work, not about using it privately.
   Running something on your own laptop and handing somebody a zip file are different acts
   with different obligations. Do not assume that is true of your license. Read yours and
   confirm it.

---

## Three families, and what actually separates them

| Family | Example | The bargain |
|---|---|---|
| **Permissive** | MIT, Apache 2.0 | Do nearly anything, keep the notices |
| **Copyleft** | GPL | Do nearly anything, and what you convey stays under the same terms |
| **Restricted use** | Many model licenses, CC NonCommercial | Do some things, and there is a list of things you may not do at all |

### MIT, in full, because you can read it in one minute

Open `05-labs/lab-m03-01-files/study-buddy/vendor/pocketgrid/LICENSE`. That file is 169
words, and the entire obligation is one sentence:

> The above copyright notice and this permission notice shall be included in all copies or
> substantial portions of the Software.

- **Permits:** use, copy, modify, merge, publish, distribute, sublicense, and sell.
- **Requires:** include the copyright notice and the permission notice.
- **Forbids:** nothing else. It disclaims warranty and limits liability, which are
  protections for the author rather than restrictions on you.

**MIT does not require you to open source your project.** It is the most common false
claim about MIT, and the text settles it in the time it takes to read one paragraph.

### Apache 2.0, and the two things it adds

Apache 2.0 is permissive like MIT and adds two things worth knowing about.

**A patent grant.** Contributors grant a patent license covering their contributions, and
that grant ends for you if you start patent litigation over the work. MIT says nothing
about patents at all.

**A redistribution section with a list.** Section 4 is the one to read, and it is a
checklist. It covers giving recipients a copy of the License, marking files you changed,
keeping the notices that were there, and carrying the contents of a `NOTICE` file if the
work has one. Lanternparse in the Study Buddy tree has a `NOTICE` file. Open it. Then look
at the Study Buddy README's credits section and notice that the NOTICE contents are not
there.

Read Section 4 yourself at the Apache Software Foundation's published text. **[VERIFY]**
Do not take my list as the list.

### The GPL, and the word that matters

The GPL is copyleft. The bargain is that the freedoms travel with the code: anyone you
convey the work to gets the same freedoms you got, including the source.

Two corrections, because both of these get said in this building every year:

**The GPL does not forbid selling software.** It permits commercial use and permits
charging money. What it does is require that whoever receives the conveyed work receives
the corresponding source and the same license terms.

**The GPL is not triggered by using something.** Its conditions are about conveying. If
you run a GPL program on your own machine and nobody else ever receives it, the conveying
conditions have not woken up.

The section about conveying modified source versions and the section about conveying
non-source forms are where the real requirements live. Read them at the Free Software
Foundation's published text. **[VERIFY]**

### Restricted-use licenses, including most model licenses

Open `study-buddy/model/LICENSE.txt`. It is an invented license written in the shape real
model licenses take, and it is the shape that surprises people:

- It permits use, modification, and derivative works.
- It requires you to display a specific sentence, ship a notice file unchanged, and name
  derivatives with a required prefix.
- It **forbids** a list of uses outright, and it ends your license automatically if you
  breach that list.
- It requires a separate negotiation above a user threshold.

**A model you can download and run is not necessarily under an open source license.** The
Open Source Initiative maintains the definition of that term, and a license with a list of
forbidden fields of use does not meet it. This distinction is Thursday's setup, and it is
worth having in your head now: **"open weights" is a statement about where the file is.
"Open source" is a statement about what the license says.**

---

## License compatibility, the problem nobody plans for

Here is the situation sitting in the Study Buddy tree right now. The project's own
`LICENSE` is MIT. Inside `vendor/sortwell/` there is code whose header says it is under
the GNU General Public License, version 3 or later.

If the team conveys Study Buddy to anybody, it is conveying a combined thing that includes
GPL-covered code. The widely stated understanding of how the GPL works is that a combined
work conveyed that way carries the GPL's conditions with it, so an MIT notice on the front
of the project does not describe what is actually being conveyed.

**Where this gets genuinely arguable:** what counts as one combined work, versus two
programs that talk to each other, is a real and long-running argument. Linking, importing,
calling over a network, and shipping side by side are treated differently by different
people, and the Free Software Foundation's published position is not the only position
anybody holds.

**What is not arguable:** the team has not noticed, has not written anything down, and has
a project page that states one license while the tree contains another. That is the
finding. An auditor's job here is not to win the argument. It is to surface the conflict,
say which facts the answer depends on, and escalate it before the project ships.

There is a second finding in the same folder that is not arguable at all. **There is no
copy of the GPL anywhere in the tree.** The license that was supposed to travel with that
code did not travel with it.

---

## Worked example 1: the identifier is a convenience, not the license

Many projects put a one-line machine-readable tag in a file. Look for it first, because it
is fast, and then go read the text anyway.

```python
# spdx.py: report the SPDX identifier for every component, or say there is none.
import os
import re

PROJECT = "study-buddy"
COMPONENTS = [
    "vendor/pocketgrid", "vendor/lanternparse", "vendor/sortwell",
    "snippets/shuffle_from_blog.py", "assets/fonts", "assets/icons",
    "assets/images", "assets/sounds", "model", "data/flashcard_seed",
]
TAG = re.compile(r"SPDX-License-Identifier:\s*(\S+)")


def identifier_for(path):
    files = [path] if os.path.isfile(path) else [
        os.path.join(path, n) for n in sorted(os.listdir(path))
    ]
    for name in files:
        if not os.path.isfile(name):
            continue
        found = TAG.search(open(name, encoding="utf-8", errors="replace").read())
        if found:
            return found.group(1)
    return None


for component in COMPONENTS:
    tag = identifier_for(os.path.join(PROJECT, component))
    print(f"{component:<32} {tag if tag else 'no identifier, read the text'}")
```

Output:

```
vendor/pocketgrid                no identifier, read the text
vendor/lanternparse              Apache-2.0
vendor/sortwell                  no identifier, read the text
snippets/shuffle_from_blog.py    no identifier, read the text
assets/fonts                     no identifier, read the text
assets/icons                     CC-BY-4.0
assets/images                    no identifier, read the text
assets/sounds                    CC-BY-NC-4.0
model                            no identifier, read the text
data/flashcard_seed              CC-BY-SA-4.0
```

**Four identifiers out of ten components.** Look at which ones are missing. Pocketgrid has
a complete, standard MIT license and no tag. Sortwell has a clear GPL header and no tag.
The model has a full license document and no tag.

**A component with no identifier is not a component with no license.** If you had written
a tool that treats a missing tag as a missing license, you would have flagged the two
cleanest components in the tree and missed nothing that was actually wrong.

## Worked example 2: which obligations are awake right now

```python
# triggers.py: which obligations wake up, given what you are actually doing.
# This prints the QUESTIONS a license makes you answer. It answers none of them.

PLANS = [
    {"label": "running it on your own laptop", "distributing": False, "modified": True},
    {"label": "putting the repository on GitHub", "distributing": True, "modified": True},
    {"label": "handing a zip to a judge", "distributing": True, "modified": False},
]

OBLIGATIONS = {
    "MIT": "ship the copyright notice and the permission notice",
    "Apache-2.0": "ship the license, the NOTICE contents, and mark changed files",
    "GPL-3.0-or-later": "ship the license and the corresponding source, under the GPL",
    "CC-BY-4.0": "give attribution in the form section 3 sets out",
    "CC-BY-NC-4.0": "give attribution, and stay inside the NonCommercial term",
}

for plan in PLANS:
    print(f"\nPlan: {plan['label']}")
    if not plan["distributing"]:
        print("  Nothing is conveyed to anybody else.")
        print("  Most conditions in these licenses are written about conveying.")
        print("  Read yours to confirm that is true of yours. Do not assume it.")
        continue
    for name, duty in OBLIGATIONS.items():
        print(f"  {name:<20} {duty}")
    if plan["modified"]:
        print("  You changed something, so every 'state your changes' clause applies.")
```

Output:

```

Plan: running it on your own laptop
  Nothing is conveyed to anybody else.
  Most conditions in these licenses are written about conveying.
  Read yours to confirm that is true of yours. Do not assume it.

Plan: putting the repository on GitHub
  MIT                  ship the copyright notice and the permission notice
  Apache-2.0           ship the license, the NOTICE contents, and mark changed files
  GPL-3.0-or-later     ship the license and the corresponding source, under the GPL
  CC-BY-4.0            give attribution in the form section 3 sets out
  CC-BY-NC-4.0         give attribution, and stay inside the NonCommercial term
  You changed something, so every 'state your changes' clause applies.

Plan: handing a zip to a judge
  MIT                  ship the copyright notice and the permission notice
  Apache-2.0           ship the license, the NOTICE contents, and mark changed files
  GPL-3.0-or-later     ship the license and the corresponding source, under the GPL
  CC-BY-4.0            give attribution in the form section 3 sets out
  CC-BY-NC-4.0         give attribution, and stay inside the NonCommercial term
```

**Every one of you moved from the first plan to the second plan in Week 1 of this program,
and nobody stopped to notice.** Pushing a repository to a public host is conveying. That
is the day the obligations wake up, and it happens on the day you would least expect an
obligation to start.

## Worked example 3: finding the requirement with your own eyes

The point of this one is speed. You should be able to settle a licensing argument in under
a minute.

```python
text = open("study-buddy/vendor/pocketgrid/LICENSE", encoding="utf-8").read()
print(len(text.split()), "words")
for paragraph in text.split("\n\n"):
    if "shall be included" in paragraph:
        print(paragraph.strip())
```

Output:

```
169 words
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

169 words. One condition. Next time somebody tells you what MIT requires, open the file
instead.

---

## The wrong version, and what it does instead of an error

Here is a license summary table of the kind a model will write for you in two seconds. It
is well formatted, confident, and covers exactly the licenses in your project.

```
| License    | Commercial use | Must credit | Must open source your code |
|------------|----------------|-------------|----------------------------|
| MIT        | Yes            | No          | Yes                        |
| Apache-2.0 | Yes            | Yes         | No                         |
| GPL-3.0    | No             | Yes         | Yes                        |
| CC-BY-4.0  | Yes            | Yes         | No                         |
```

**No error. No warning. A clean table with a header row.** Three of the cells in it are
wrong, and the reason each one is wrong is in a file you already have open.

| Cell | What the text says |
|---|---|
| MIT, "must open source your code": Yes | The MIT text has one condition and it is about notices. There is no such requirement. |
| MIT, "must credit": No | Including the copyright notice and the permission notice **is** the credit requirement. The table says MIT has no obligation, which is the opposite of its only obligation. |
| GPL-3.0, "commercial use": No | The GPL permits commercial use and permits charging money. What it requires is that the conveyed work carry the source and the same terms. |

Notice what the table got right, because that is what makes it dangerous. Apache and
CC-BY are described correctly enough to pass a glance. Three right rows are what buy the
wrong ones their credibility.

## Why the wrong version is tempting

**It is the shape of the answer you wanted.** You wanted a table. A table arrived. The
format matched the request so exactly that the content never got read.

**The columns are the wrong columns.** "Must open source your code" is not a question any
of these licenses answers as a yes or no, because it depends on what you are conveying and
how. A table cannot hold a conditional, so a table full of Yes and No values is a
guarantee that conditions have been flattened out of the answer.

**Checking it takes longer than believing it.** Reading four license texts takes twenty
minutes. Reading the table takes six seconds. That gap is the entire reason bad summaries
survive, and it is the reason Gate 2 exists in this course.

---

## Vocabulary

| Term | What it means |
|---|---|
| **License** | Permission from the rights holder on stated conditions. The document itself. |
| **Permit, require, forbid** | The three questions you answer about every license, in that order. |
| **Convey or distribute** | Giving the work to somebody else. Usually what triggers the conditions. |
| **Permissive license** | Few conditions, usually about keeping notices. MIT, Apache 2.0. |
| **Copyleft** | Conditions that make the conveyed work carry the same freedoms forward. GPL. |
| **Restricted use** | A license with a list of things you may not use it for at all. |
| **Patent grant** | A license to the contributors' patents covering their contributions. Apache 2.0 has one. MIT does not. |
| **NOTICE file** | A file whose contents Apache 2.0 requires you to carry forward. |
| **SPDX identifier** | A short machine-readable tag naming a license. A convenience, not the license. |
| **Compatibility** | Whether two licenses' conditions can both be satisfied by one conveyed work. |
| **Open source** | A license meeting the Open Source Definition. Not a synonym for downloadable. |
| **Open weights** | The model file is available. A statement about location, not about terms. |

---

## Self-check

**Question 1.** Without opening anything, write down MIT's one condition in your own words.
Then open `study-buddy/vendor/pocketgrid/LICENSE` and check yourself. If you were wrong,
write down which of the three questions you got wrong: permit, require, or forbid.

**Question 2.** A teammate says: "We are not distributing Study Buddy, we are only pushing
it to our public GitHub repository for the competition, so the license conditions do not
apply yet." Is the teammate right, and what is the one fact that settles it?

**Question 3.** Run worked example 1. Pocketgrid reports no identifier. Sortwell reports no
identifier. Explain why those two results mean completely different things, and say what
you would do next about each one.

---

### Answers

**1.** The condition is that the copyright notice and the permission notice have to be
included in copies or substantial portions. Most people who get this wrong get **require**
wrong in one of two directions: they say MIT requires nothing, or they say it requires
open sourcing your project. Both are require-column errors. Almost nobody gets permit
wrong, because the permit list is long and generous and people read that part.

**2.** The teammate is wrong. **Pushing to a public repository is conveying the work to
other people**, which is the act these conditions are written about. The fact that settles
it is that strangers can now obtain a copy. Nothing about the word "distributing" requires
money, a download page, or an installer. This matters for real: the repository is public
the moment you push, and the notices, the NOTICE contents, and the GPL question are all
live from that moment.

**3.** Pocketgrid has a complete, standard MIT license sitting in a file named `LICENSE`.
It has no SPDX tag because the classic MIT text does not carry one. Nothing is wrong and
nothing needs doing beyond recording it and carrying the notice.

Sortwell has no SPDX tag and no license file either. Its terms are stated in a header
comment inside the source, which is a valid way to state them, and the header says GPL
version 3 or later. So the missing tag is not the finding. The finding is that **the copy
of the license that should have travelled with GPL code is not in the tree**, and that the
project's own `LICENSE` says MIT. Next step for sortwell: write it up, mark it as the
highest severity item in the audit, and escalate it rather than deciding it yourself.

The general rule to take away: **a missing identifier is a signal to go read, not a
finding.** The finding is always something you found in the text, or the documented
absence of any text at all.
