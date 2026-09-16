# Lecture Notes: Creative Commons, Media, and the Attribution You Actually Owe
## 145130 Applications of AI · Module 3 · Week 7, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W07_CreativeCommonsAndMedia.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W07_CreativeCommonsAndMedia.pptx)

If you missed class, you can learn this concept from this file alone. Open the license
files in the Study Buddy tree while you read.

**Competencies:** 7.1.7 (intellectual property rights, responsibilities, and controls
related to interactive media), 9.6.1 (adhere to licensing and intellectual property laws),
1.3.8 (verify compliance with computer and intellectual property laws).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** Creative Commons
publishes its own licenses, and the license text is what governs. Every Creative Commons
license has two documents: a short human-readable **deed**, and the **legal code** linked
from it.

**The deed is a summary. The legal code is the license.** This is the one place in this
module where the difference is built into the product itself, and it is the best available
lesson on why a summary is not a source.

- Creative Commons licenses: `https://creativecommons.org/licenses/` **[VERIFY]**
- Fair use is part of United States copyright law, Title 17. The U.S. Copyright Office
  publishes material on it at `https://www.copyright.gov` **[VERIFY]**

---

## Why this exists

Your code is usually the part of a project you wrote. The media almost never is.

Every project you ship this year will carry a font you did not draw, icons you did not
make, a sound you did not record, and probably an image you did not take. Those are the
components most likely to be unlicensed, because they arrive by a path with no obvious
place to stop and ask: a search result, a right-click, a download button with no terms next
to it.

There is a second reason, and it is about being seen. **Nobody looks at your dependency
tree. Everybody looks at your poster.** The asset most likely to get a team an awkward
email is the hero image on the slide behind them at the showcase.

---

## The Creative Commons system is four elements, mixed

Creative Commons licenses are built from four elements. You read the abbreviation and you
know most of what you need before opening anything.

| Element | Code | What it means |
|---|---|---|
| Attribution | **BY** | You have to credit the creator, in the form the license sets out |
| ShareAlike | **SA** | If you share an adapted version, it goes out under the same license or a compatible one |
| NonCommercial | **NC** | Not for use primarily intended for commercial advantage or monetary compensation |
| NoDerivatives | **ND** | You may share the work, but not share adapted versions of it |

Every current Creative Commons license includes BY. Combine BY with the others and you get
the six: **CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND.**

Separately, **CC0** is not a license in the same sense. It is a tool a creator uses to give
up their rights in a work as far as the law allows, putting it as close to the public
domain as they can get it. CC0 material carries no attribution requirement. Crediting it
anyway is good manners and good practice, and it is not a condition.

**Creative Commons licenses are for creative works, not for software.** Creative Commons
itself says its licenses are not recommended for software, because software has its own
licenses that handle source code, patents, and distribution properly. When you see a CC
license on code, that is a signal that somebody picked a badge rather than a license.

---

## Attribution is a specific list, not a vibe

This is the part that surprises people. The attribution condition in a Creative Commons 4.0
license is not "say thanks". Section 3 of the license sets out a list of items you have to
keep or supply when you share the material. Read it yourself, in the legal code. The items
it covers include:

- the creator's name, as they asked to be identified
- a copyright notice, if one was supplied
- a notice referring to the license, and a notice referring to the disclaimer of warranties
- a link or address for the material itself
- a link or address for the license
- an indication that you modified the material, if you did, and a record of earlier
  modifications

A memory aid people use for the first four is **TASL: title, author, source, license.**
It is a useful hook and it is not the license. **[VERIFY]** it against Creative Commons'
own guidance before you teach it as the standard.

**The Study Buddy README says "Icons by the Lantern Icon Project."** That sentence is
friendly and it does not meet the condition. Worked example 1 shows exactly how far short
it falls.

---

## The two hard elements: NonCommercial and ShareAlike

### NonCommercial

The NonCommercial element is the one students most often assume they understand. The
definition in the 4.0 licenses turns on use that is **primarily intended for or directed
toward commercial advantage or monetary compensation.** Read that definition in the legal
code before you rely on any reading of it.

Now the Study Buddy situation. The chime is CC BY-NC 4.0. The team's stated plan is to sell
printed card decks for two dollars each at the showcase to raise money for a trip.

**Is that inside the NonCommercial term?** This is a real argument and both sides are real.

**The strongest case that it is outside the term:** the team is exchanging a product for
money. Money is changing hands and a good is being handed over. The fact that the money is
for a trip describes what the team does with the proceeds, not what the activity is.

**The strongest case that it is inside the term:** the chime is in the app, not in the
printed decks, so the thing being sold and the thing under the NC license may not be the
same thing at all. That is not a "we are a school so it is fine" argument. It is a
question about what is actually being exchanged.

**What an auditor does here:** does not decide it. Writes down the facts the answer depends
on, writes down that the cheapest fix is a different sound, and escalates it. "We are a
school club" is not a legal analysis and this course will not let you use it as one.

### ShareAlike

ShareAlike says that if you share an adapted version of the material, that adapted version
goes out under the same license or one Creative Commons has listed as compatible.

The Study Buddy dataset is CC BY-SA 4.0. Nothing from it ships in the current build, so the
sharing condition has not been triggered by anything the team has done. **Record that
finding as a finding, not as a blank row.** "Not triggered today, and here is what would
trigger it" is a complete audit entry. "N/A" is not.

---

## Media has its own traps

### Fonts

Font files are software, and font licenses are their own world. They routinely have terms
about **embedding** a font in a document or an application, about how many machines may
install it, and about whether you may convert it to another format. A font that is free to
install on your laptop is not automatically free to ship inside your app.

Study Buddy's font has no license file and the team does not remember the site. That is not
a small finding. It is an unlicensed component on the printed poster.

### Sound and music

A piece of recorded music usually involves **two separate copyrights**: one in the musical
composition and one in the particular sound recording of it. Getting permission for one is
not getting permission for the other. This is why "I bought the song" and "I can use the
song in my video" are unrelated statements.

### Stock sites and the word "royalty-free"

**Royalty-free does not mean free.** It means that after you obtain the license, you do not
owe a per-use royalty. The license itself usually costs money and usually has terms, often
including limits on print runs, on resale, and on use in a logo.

### Trademarks in your interface

Putting another organization's logo in your app implies a relationship you may not have.
Trademark is about identifying a source, so the risk is not "copying the image", it is
**suggesting somebody endorsed you.** The model license in the Study Buddy tree says this
out loud: it grants no trademark rights and then separately requires one specific sentence
to be displayed. Read those two clauses together and you can see exactly what the licensor
is protecting.

### Fair use, briefly and honestly

Fair use is part of United States copyright law. It is not a permission you are granted in
advance and it is not a checklist you can pass. It is a defense that a court weighs, using
four factors: the purpose and character of the use, the nature of the work, how much was
used and how substantial it was, and the effect on the market for the work.

**"It is educational" is not fair use.** Educational purpose is part of one of four
factors. Teams reach for fair use when they have already done the thing and want a reason
it was fine. That is backwards. **Use it as a reason to ask a lawyer, never as a reason to
ship.**

---

## Worked example 1: what your credit line is missing

This program checks whether a credit line carries the items an attribution has to carry. It
checks presence. It cannot check that any of the items are true, and it is not legal advice.

```python
# attrib.py: does a credit line carry the items a CC attribution has to carry?
REQUIRED = {
    "creator name": lambda line: any(ch.isupper() for ch in line) and "," in line,
    "title of the work": lambda line: '"' in line,
    "link to the material": lambda line: "http" in line,
    "license named": lambda line: "CC BY" in line or "Creative Commons" in line,
    "link to the license": lambda line: "creativecommons.org/licenses" in line,
    "modified stated": lambda line: "modified" in line.lower()
                                    or "unchanged" in line.lower(),
}

LINES = {
    "Study Buddy README, as written": "Icons by the Lantern Icon Project.",
    "A rewrite that carries the items": (
        '"Study 24" by A. Nkemdirim and R. Bautista, at '
        "https://example.invalid/study24, licensed CC BY 4.0, "
        "https://creativecommons.org/licenses/by/4.0/ , modified: two icons recolored."
    ),
}

for label, line in LINES.items():
    print(f"\n{label}")
    print(f"  {line}")
    for item, test in REQUIRED.items():
        print(f"    {'present' if test(line) else 'MISSING'}  {item}")
```

Output:

```

Study Buddy README, as written
  Icons by the Lantern Icon Project.
    MISSING  creator name
    MISSING  title of the work
    MISSING  link to the material
    MISSING  license named
    MISSING  link to the license
    MISSING  modified stated

A rewrite that carries the items
  "Study 24" by A. Nkemdirim and R. Bautista, at https://example.invalid/study24, licensed CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ , modified: two icons recolored.
    present  creator name
    present  title of the work
    present  link to the material
    present  license named
    present  link to the license
    present  modified stated
```

**Six for six missing.** The Study Buddy credit line names the project rather than the
creators, and carries none of the other five items. It reads like credit and satisfies
nothing.

The rewrite is one sentence longer. That is the entire cost of getting this right, and it
is why there is no excuse for getting it wrong.

## Worked example 2: reading the definition instead of guessing it

Open `study-buddy/assets/sounds/LICENSE.txt` and read what it points you at. Then open the
Creative Commons legal code for BY-NC 4.0 and find the definition of NonCommercial. Write
down the definition in the license's own words, then answer these two questions in writing:

1. What is the thing being sold at the showcase?
2. Is the licensed material part of that thing?

**Your answer is not a verdict. It is a record of which facts your answer depends on.**
That distinction is what separates an audit from an opinion, and it is what the licensing
audit rubric scores.

## Worked example 3: the fastest finding in the tree

```
study-buddy/assets/images/hero.png.txt
```

Open it. The source, as recorded in the team's own chat, is "found it in image search,
looked good". There is no license file in that directory.

**There is nothing to read, and that is the finding.** An image search result carries no
license. The absence of a license is not a gap in your audit, it is the result of your
audit, and it gets written down in exactly those words: no license found, no permission
identified, remove before the poster is printed.

---

## The wrong version, and what it does instead of an error

Here is what a team does when the showcase is on Friday and the poster is due tomorrow.

> "We are a school club and this is educational, so it is fair use. Also the image came up
> in a search that said free images, so it is public domain. We credited everyone in the
> README anyway."

**No error message. Nothing breaks. The poster prints, the showcase happens, and most of
the time nothing at all occurs.** That is what makes it durable. The feedback loop is
broken, so the behaviour never gets corrected by consequences.

Three claims, three separate mistakes:

1. **"Educational, so fair use."** Educational purpose is part of one factor out of four,
   and fair use is decided case by case rather than claimed in advance.
2. **"A search said free images, so public domain."** A search filter is not a license
   grant, and free-to-download is not public domain. Yesterday's distinction.
3. **"We credited everyone in the README."** Worked example 1 shows what that credit
   actually contained. And for the image, there was no license requiring credit, because
   there was no license.

## Why the wrong version is tempting

**Every part of it sounds like a rule.** Fair use is a real doctrine. Public domain is a
real category. Attribution is a real requirement. The sentence is built entirely out of
true-sounding pieces, arranged so that none of them is doing the job it names.

**It arrives at the moment you have no time.** The poster is due tomorrow. Every one of
those three claims is a way of not going back to step one, which is the only actual fix.
**Name that pressure now, because it is the thing that will get you, not a lack of
knowledge.** The licensing audit is scheduled in Week 7 specifically so that this question
is answered before your competition deadline rather than the night before it.

**Nobody has ever told them otherwise.** A student can go through twelve years of school
putting images into slide decks and never once be asked where the image came from.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Deed** | The short human-readable summary page of a Creative Commons license. |
| **Legal code** | The actual license text, linked from the deed. This is the license. |
| **BY** | Attribution. Credit in the form the license sets out. |
| **SA** | ShareAlike. Adapted versions you share go out under the same or a compatible license. |
| **NC** | NonCommercial. Not for use primarily intended for commercial advantage or monetary compensation. |
| **ND** | NoDerivatives. You may share the work but not share adapted versions. |
| **CC0** | A tool for giving up rights in a work as far as the law allows. No attribution condition. |
| **Adapted material** | A work based on the licensed material, in which the licensed material is recast or modified. |
| **Royalty-free** | No per-use royalty after you license it. Not the same as free of charge. |
| **Composition and recording** | The two separate copyrights usually involved in a piece of recorded music. |
| **Font embedding** | Including a font file inside a document or application. Often a separate license term. |
| **Fair use** | A United States doctrine weighed by a court on four factors. A defense, not a permission slip. |

---

## Self-check

**Question 1.** Rewrite the Study Buddy credit line for the icons so it carries every item
the attribution condition covers. Two of the icons were recolored. Say which item that fact
changes and why leaving it out would be a problem even though nobody would notice.

**Question 2.** The dataset is CC BY-SA 4.0 and nothing from it ships in the current build.
Write the audit entry for it. Your entry has to say what is true today and what would
change that, in two sentences.

**Question 3.** A teammate says: "The font is free, I downloaded it without paying." Name
the two separate things the teammate has confused, and say what you would ask them to
produce before the poster is printed.

---

### Answers

**1.** A line that carries the items, for example:

> "Study 24" by A. Nkemdirim and R. Bautista, at `https://example.invalid/study24`,
> licensed CC BY 4.0, `https://creativecommons.org/licenses/by/4.0/`, modified: two icons
> recolored.

The recoloring changes the **indication that you modified the material**. Leaving it out is
a problem for two reasons that have nothing to do with being caught. First, it is a
condition of the license, and the license is the reason you are allowed to use the icons at
all. Second, an uncredited modification attributes your version of the work to the original
artists. If your recolor is worse than theirs, you have put your work under their name.

**2.** For example:

> **flashcard-seed-v1, CC BY-SA 4.0.** Used for parser testing only. No part of this
> dataset appears in any build, so the ShareAlike condition on sharing adapted material has
> not been triggered by anything the team has done. It would be triggered the moment the
> team publishes a cleaned, filtered, or reformatted version of the data, at which point
> that version goes out under the same or a compatible license. Separately, the dataset card
> records that about 15 percent of the items came from a publisher glossary whose own terms
> say no redistribution, and the dataset license cannot grant rights the collectors did not
> have.

**3.** The teammate has confused **price** with **license**, and **installing** with
**shipping**. Free to download says nothing about what terms came with the download, and a
license permitting you to install a font on your machine is often a different question from
a license permitting you to embed it in a poster file or an application you hand to other
people.

Ask them to produce **the license file or the license page from the site they downloaded it
from**. If they cannot find the site, the answer is not "it is probably fine". The answer
is a different font, which costs ten minutes, or a font the team can name the license for.
