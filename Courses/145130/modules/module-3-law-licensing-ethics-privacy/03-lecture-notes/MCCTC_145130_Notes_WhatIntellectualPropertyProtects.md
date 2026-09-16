# Lecture Notes: What Intellectual Property Actually Protects
## 145130 Applications of AI · Module 3 · Week 7, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W07_WhatIPProtects.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W07_WhatIPProtects.pptx)

If you missed class, you can learn this concept from this file alone. Run every
command.

**Competencies:** 9.6.1 (adhere to licensing and intellectual property laws including
copyright, trademark, and digital rights management), 1.7.13 (protect intellectual
property and knowledge), 7.1.7 (intellectual property rights, responsibilities, and
controls related to interactive media), 7.1.4 (important historical developments and
future trends in interactive media).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** It explains what
these bodies of law are for, at the level of the competency, so that you can recognize
when one applies and know who to ask. It deliberately does not state case outcomes,
damage amounts, or thresholds. Those change, and a wrong one in a lesson is worse than
none.

When you need an answer that matters, go to the source that governs it:

- **The U.S. Copyright Office**, for copyright and for registration.
  `https://www.copyright.gov` **[VERIFY]**
- **The United States Patent and Trademark Office**, for trademarks and patents.
  `https://www.uspto.gov` **[VERIFY]**
- **The statute itself.** United States copyright law is Title 17 of the United States
  Code. The Copyright Office publishes it. **[VERIFY]** the current address before you
  send students to it.
- **The license text**, for anything you downloaded. The license is the document. A blog
  post about the license is not the document.

This module has one rule that outranks all of the above: **when the law is unsettled,
say it is unsettled.** You will meet the biggest unsettled question in this field on
Thursday.

---

## Why this exists

You are three weeks from shipping something in public. The Congressional App Challenge
deadline usually falls next week, BPA submissions follow, and your capstone is next
semester. Every one of those goes somewhere a stranger can see it.

The moment a project becomes public, a question that did not matter starts to matter: is
every piece of this yours to use. Not "did it work". Not "did anybody notice". Is it
yours to use.

Most students have never been asked that question, because most school projects never
leave the room. The gap between a class project and a shipped product is mostly this
question, and the answer takes one afternoon if you ask it early and takes the whole
project apart if you ask it late.

There is a second reason, and it is the one this course cares about most. **You are
about to build things with models trained on other people's work.** You cannot have an
honest opinion about that until you know what protection those people actually have.

---

## The four kinds of protection, and what each one covers

These are four separate systems. They protect different things, they start at different
moments, and they last for different lengths of time. Mixing them up is the single most
common mistake in this area, including in AI-written summaries.

| | What it protects | When it starts | What it does not cover |
|---|---|---|---|
| **Copyright** | Original works of authorship fixed in a tangible form: code, text, images, music, video | Automatically, at the moment the work is fixed | Ideas, procedures, processes, systems, methods of operation, concepts, principles, discoveries |
| **Trademark** | Words, names, symbols, and designs that identify the source of goods or services | Through use in commerce, and strengthened by federal registration | The product itself. It protects the badge, not the car |
| **Patent** | Inventions: new and useful processes, machines, and compositions of matter | Only when granted, after you apply and are examined | Anything you kept to yourself instead of applying for |
| **Trade secret** | Information that has value because it is not generally known, and that you take reasonable steps to keep secret | The moment you start protecting it | Anything you published, and anything somebody else worked out independently |

### Copyright, in more detail, because it is the one you meet daily

Two facts from the statute matter more than everything else in this section.

**First: copyright is automatic.** United States copyright law protects original works of
authorship fixed in a tangible medium of expression. No notice is required. No
registration is required for the protection itself. The commit you pushed this morning is
a copyrighted work. So is the sketch in your notebook, and so is the photo a stranger
posted.

Registration is a separate step with separate benefits, and for United States works it
generally has to happen before a lawsuit can be filed. Ask the Copyright Office, not this
file, about that.

**Second: copyright covers the expression, not the idea.** The statute says this
directly. Copyright does not extend to any idea, procedure, process, system, method of
operation, concept, principle, or discovery, regardless of the form it is described in.

That second rule is doing enormous work in your life as a programmer. **The idea of a
flashcard app is not protected. The particular code somebody wrote for theirs is.** You
can read a blog post describing an algorithm, close the tab, and write your own
implementation. You cannot copy and paste theirs and call it yours. The line between
those two is not a technicality. It is the line the whole system runs on.

### What "publicly available" does not mean

**Public does not mean public domain.** Those two phrases share a word and share nothing
else.

- **Publicly available** means you can see it. A photo on a website is publicly available.
- **Public domain** means nobody holds a copyright in it any more, or nobody ever did.
  Works whose copyright has expired, works of the United States federal government, and
  works whose creators formally dedicated them to the public are in the public domain.

A file you can download is not a file you can use. That is the single most expensive
misunderstanding in this module, and it is the one planted in Study Buddy's poster image.

### Digital rights management, and the law that sits behind it

**Digital rights management (DRM)** is a technological control that limits what you can do
with a copy: a stream you cannot save, a book that only opens in one app, a game that
checks in with a server.

DRM is not itself a law. The law next to it is the part of United States copyright law,
added by the Digital Millennium Copyright Act in 1998, that prohibits circumventing a
technological measure that controls access to a copyrighted work. That prohibition is
separate from infringement: breaking the lock can be a violation on its own, even in
situations where what you wanted to do with the work would have been fine.

The Librarian of Congress grants exemptions to that prohibition through a rulemaking that
happens on a regular cycle, which is why the answer to "is this allowed" genuinely changes
over time. Check the Copyright Office's current exemption list rather than repeating
something you read once. **[VERIFY]**

### Trade secrets and the thing you are not allowed to give away

Competency 1.7.13 asks you to protect intellectual property and knowledge, including
processes. Trade secret is the part of that list students skip, and it is the one most
likely to touch you first, at your first job.

A trade secret is information with value because it is not generally known, kept secret by
reasonable measures. A customer list, a pricing formula, an internal process, the prompt
that finally made the model behave. There is federal trade secret law and Ohio has its own
trade secret law as part of the Ohio Revised Code. **[VERIFY]** the citation with the
state before quoting it to anybody.

The practical consequence is short. **If you take an internship and paste your employer's
internal document into anything, you may have destroyed the protection on it.** Not
infringed it. Destroyed it, because the protection depended on it not being generally
known. This is the reason a model that runs on your own hardware and sends nothing out of
the building is worth the performance you give up.

---

## Interactive media is many works at once

Competency 7.1.7 is about interactive media specifically, and there is a reason it gets
its own line. **An app is not one work. It is a stack of works owned by different people,
under different terms, that happen to be running in the same window.**

Open Study Buddy and count:

| Layer | The work | Who might own it |
|---|---|---|
| Code you wrote | Literary work | You, or your school, or your employer |
| Code you copied in | Literary work | Whoever wrote it, under whatever license |
| Icons | Pictorial work | The icon artist |
| Font | Software and design | The type foundry |
| Sound | Sound recording | The recordist |
| Text content | Literary work | Whoever wrote it |
| The name and the logo | Trademark | You, if you use it as a badge in commerce |
| The model | Weights under a contract, plus everything the training raises | Contested. See Thursday |
| The dataset | A collection, with items under their own terms | Two answers, not one |

Every one of those layers can be fine on its own and still produce a project you cannot
ship, because the layers have conditions that do not agree with each other. That is
Tuesday and Wednesday.

## A short history, because the pattern repeats

Competency 7.1.4 asks for historical developments and future trends. The useful version of
that history is not a list of dates. It is one pattern that has repeated for over a
century.

**A copying technology arrives. It does something the existing rules did not anticipate.
Courts and legislatures fight about it. The rules get rewritten. The technology becomes
ordinary.** Player pianos, photocopiers, cassette tapes, videocassette recorders, the
personal computer, the web, peer-to-peer file sharing, streaming.

Three milestones worth knowing by name:

- **The Copyright Act of 1976**, the modern framework in United States law, which took
  effect in 1978 and made protection automatic on fixation.
- **United States accession to the Berne Convention in 1989**, which is why a notice is
  not required for protection.
- **The Digital Millennium Copyright Act of 1998**, which brought the anti-circumvention
  rules and the notice-and-takedown process the whole modern web runs on.

**The trend you are living in is the next turn of the same wheel.** Generative models are
a copying technology in a sense nobody had a rule for, and the rules are being written
right now, in courtrooms and legislatures, while you are in this room. That is why
Thursday's lesson has no answer at the end of it. Be suspicious of anybody who gives you
one.

---

## Worked example 1: find the licenses, the naive way

Every command below runs from `05-labs/lab-m03-01-files/`, where the Study Buddy tree
lives. This is the way most people look for licenses in a project.

```python
# scan.py, first attempt. Find every third-party component that has no license.
import os

PROJECT = "study-buddy"

for folder, subfolders, filenames in os.walk(PROJECT):
    if "LICENSE" in filenames:
        print("licensed:", folder)

print("Scan complete. Everything above is licensed.")
```

Output:

```
licensed: study-buddy
licensed: study-buddy\vendor\lanternparse
licensed: study-buddy\vendor\pocketgrid
Scan complete. Everything above is licensed.
```

Three licensed components. The project looks clean.

## Worked example 2: the same project, looked at properly

```python
# scan.py, second attempt. A license can live in a file, in a header, or nowhere.
import os

PROJECT = "study-buddy"
LICENSE_FILENAMES = ("LICENSE", "LICENSE.txt", "LICENCE", "COPYING", "NOTICE")
HEADER_WORDS = ("SPDX-License-Identifier", "Licensed under",
                "GNU General Public License", "MIT License", "Creative Commons")

COMPONENTS = [
    "vendor/pocketgrid", "vendor/lanternparse", "vendor/sortwell",
    "snippets/shuffle_from_blog.py", "assets/fonts", "assets/icons",
    "assets/images", "assets/sounds", "model", "data/flashcard_seed",
]


def evidence_in(path):
    """Return the first piece of license evidence found for one component."""
    if os.path.isfile(path):
        files = [path]
    else:
        files = [os.path.join(path, name) for name in sorted(os.listdir(path))]
    for name in files:
        if os.path.basename(name) in LICENSE_FILENAMES:
            return "file: " + os.path.basename(name)
    for name in files:
        if not os.path.isfile(name):
            continue
        text = open(name, encoding="utf-8", errors="replace").read()
        for word in HEADER_WORDS:
            if word in text:
                return "header in " + os.path.basename(name)
    return None


for component in COMPONENTS:
    found = evidence_in(os.path.join(PROJECT, component))
    print(f"{component:<32} {found if found else 'NOTHING FOUND'}")
```

Output:

```
vendor/pocketgrid                file: LICENSE
vendor/lanternparse              file: LICENSE
vendor/sortwell                  header in sortwell.py
snippets/shuffle_from_blog.py    NOTHING FOUND
assets/fonts                     NOTHING FOUND
assets/icons                     file: LICENSE.txt
assets/images                    NOTHING FOUND
assets/sounds                    file: LICENSE.txt
model                            file: LICENSE.txt
data/flashcard_seed              file: LICENSE.txt
```

Ten components. Three have nothing at all. One carries its license only in a source file
header, which the first scan never looked at.

**The first scan did not report those seven as problems. It did not report them at all.**

## Worked example 3: the whole obligation of one license is one sentence

The MIT license is short. Students still get it wrong constantly, because they read a
summary instead of the text. Find the condition yourself:

```python
text = open("study-buddy/vendor/pocketgrid/LICENSE", encoding="utf-8").read()
for paragraph in text.split("\n\n"):
    if "shall be included" in paragraph:
        print(paragraph.strip())
```

Output:

```
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

That is the entire obligation. Not "you have to open source your project". Not "you have
to credit them on the About screen". **Include the notice.** One sentence, found in eight
seconds, and it settles an argument you will otherwise have four times this year.

---

## The wrong version, and what it does instead of an error

Worked example 1 is the wrong version, and it is worth looking at again now that you have
seen the right answer.

```
licensed: study-buddy
licensed: study-buddy\vendor\lanternparse
licensed: study-buddy\vendor\pocketgrid
Scan complete. Everything above is licensed.
```

**No error. No warning. Three green lines and a confident closing sentence.**

The program did exactly what it was told. It found every folder containing a file named
`LICENSE` and said so. The problem is what it was told to do. The seven components with no
license file were never in the output, so nothing on the screen said they existed.

This is the shape you have been shown since your first year here: **a program that
produces output is a different claim from a program that produces the right answer.** Here
that shape has a legal consequence. A scan like this one is how a team ends up telling a
competition judge that its licensing is clean.

## Why the wrong version is tempting

**It produces a list, and a list feels like an inventory.** Three lines of output looks
like work. Nothing in the format tells you the list is the wrong list.

**It starts from the files instead of from the components.** The second scan starts by
naming what has to be accounted for, then goes looking. The first one starts by looking,
then reports what it happened to find. That difference is the whole method of an audit,
in one line of code.

**The closing sentence is a claim nobody checked.** The program prints "Everything above
is licensed", which is true and useless, and a reader turns it into "everything is
licensed", which is false. Watch for that move in AI-written summaries this week. It is
the most common one.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Copyright** | Automatic protection for an original work of authorship once it is fixed in a tangible form. |
| **Fixed** | Written down, saved, recorded. Protection starts here, not at registration. |
| **Idea and expression** | Copyright covers the expression, not the idea, procedure, process, or method. |
| **Public domain** | No copyright applies. Different from publicly available, which means you can see it. |
| **Trademark** | A word, name, symbol, or design identifying the source of goods or services. |
| **Patent** | A granted right in an invention, which you get only by applying and being examined. |
| **Trade secret** | Valuable information kept secret by reasonable measures. Publishing it ends it. |
| **DRM** | A technological control on what you can do with a copy. |
| **Anti-circumvention** | The rule against breaking a technological measure that controls access to a work. |
| **Infringement** | Using a protected work in a way the owner has the exclusive right to control, without permission. |
| **License** | Permission from the rights holder, on stated conditions. The document, not a summary of it. |
| **Attribution** | Credit in the form a license requires, which is usually more specific than you expect. |

---

## Self-check

**Question 1.** A classmate says: "I found the algorithm in a blog post, so I can copy the
code from the post into our project." Name the one distinction that decides whether that
is true, and say what the classmate would have to do differently for the answer to change.

**Question 2.** Run worked example 1 against the Study Buddy tree. Worked example 2 names
ten components. How many of those ten did the first program fail to mention, and could you
have worked that number out from the first program's output alone?

**Question 3.** For each item, name which of the four kinds of protection is the one that
matters, and say why the other three are not the answer:

a. The name "Study Buddy" printed on a poster at a public showcase
b. The exact wording of the hint prompt your team spent two weeks tuning
c. A photo you took of the lab and posted to the project README
d. A new method of compressing model weights that your team worked out

---

### Answers

**1.** The distinction is **idea versus expression**. Copyright does not cover the
algorithm, the procedure, or the method. It covers the particular code that expresses it.
So reading the post, understanding the method, closing the tab, and writing the code
yourself is a different act from copying the code out of the page. For the answer to
change on the copy-and-paste version, the classmate would need permission: a license on
the page, an explicit grant, or a dedication to the public domain. "It was posted
publicly" is not one of those.

**2.** It failed to mention **eight** of the ten: `vendor/sortwell`,
`snippets/shuffle_from_blog.py`, `assets/fonts`, `assets/icons`, `assets/images`,
`assets/sounds`, `model`, and `data/flashcard_seed`. It mentioned only `vendor/pocketgrid`
and `vendor/lanternparse`, plus the project root.

**No, you could not have worked that number out from the first program's output.** The
first program prints what it found. It never prints what it was supposed to account for,
so there is no denominator anywhere in its output. That is exactly the defect. Five of the
eight it missed do carry license evidence, in a file named `LICENSE.txt` or in a source
header the program never opened. Three carry nothing at all. The output gives you no way
to tell those two groups apart, or to know either group exists. If you wrote a confident
number before checking, you did the same thing the program did.

**3.**

a. **Trademark.** The name is being used as a badge that tells people which project this
   is. Copyright does not usually protect a short name. Patent is for inventions. Trade
   secret is the opposite of a name on a poster.
b. **Trade secret.** It has value because nobody else has it, and you can keep it by not
   publishing it. Copyright might cover the exact wording as a very short text, which is
   weak protection. There is nothing to register and nothing to badge.
c. **Copyright.** It is an original work fixed in a tangible form the moment the camera
   saved it. It is yours automatically. Note that the people in the photo raise a
   different question, which is privacy, and that is Week 9.
d. **Patent** is the one that could cover the method itself, and getting it means
   applying, being examined, and publishing the method in the application. **Trade secret
   is the live alternative**, and the choice between them is a real strategy decision:
   patent and tell everybody, or keep quiet and hope nobody works it out. Copyright covers
   your implementation of it, not the method.
