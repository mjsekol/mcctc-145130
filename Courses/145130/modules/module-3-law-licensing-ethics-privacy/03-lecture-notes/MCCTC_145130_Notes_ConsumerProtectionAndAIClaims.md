# Lecture Notes: Consumer Protection, and the Claims on Your Own Poster
## 145130 Applications of AI · Module 3 · Week 8, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W08_ConsumerProtectionAndAIClaims.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W08_ConsumerProtectionAndAIClaims.pptx)

If you missed class, you can learn this concept from this file alone. Run both programs.

**Competencies:** 1.3.4 (identify how federal and state consumer protection laws affect
products and services), 1.3.8 (verify compliance with computer and intellectual property
laws and regulations), 2.14.2 (how AI technology impacts society and the ethical
implications of its usage).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** It explains what
consumer protection law is for and what it asks of a person making claims about a product,
at the level of the competency. It does not state penalties, thresholds, or outcomes.

Primary sources:

- **The Federal Trade Commission**, which enforces the federal prohibition on unfair or
  deceptive acts or practices, and publishes guidance for businesses on advertising claims,
  endorsements, and substantiation. `https://www.ftc.gov` **[VERIFY]**
- **The Ohio Attorney General**, which enforces Ohio's Consumer Sales Practices Act. That
  act is part of the Ohio Revised Code. **[VERIFY]** the chapter number and the office's
  current address through the State of Ohio's official site, and confirm you are on a
  `.gov` page.
- **The United States Department of Justice** on the Americans with Disabilities Act and
  accessibility. `https://www.ada.gov` **[VERIFY]**

---

## Why this exists

You are going to describe something you built to somebody who has not used it.

That happens at the showcase, on the competition submission form, in a README, on an app
store page, and in a job interview. The moment money or a decision rides on your
description, you have moved from a class project into the territory this body of law
governs, and the standard is higher than "I believed it when I wrote it."

The reason to teach it in an AI course is specific. **AI products attract exactly the kind
of claim this law exists to control**, because the product is hard to test, the vocabulary
is unfamiliar to buyers, and a number like "94% accurate" sounds like a measurement even
when nobody can say a measurement of what.

---

## The core idea, in one line

**If you make a factual claim about a product, you need to have a reasonable basis for it
before you make it.**

That principle has a name in federal practice: **substantiation.** It is the thing students
find surprising. The rule is not that a false claim gets you in trouble after somebody
proves it false. **The rule is that you need the evidence before you publish the claim**, and
"nobody has disproved it" is not evidence.

### Deception and unfairness

Federal law prohibits unfair or deceptive acts or practices in commerce, and the FTC is the
agency that enforces it.

**Deception**, as the FTC describes it, turns on a representation, omission, or practice
that is likely to mislead a consumer acting reasonably in the circumstances, about something
material to their decision. Read that carefully:

- **Likely to mislead.** Nobody has to have actually been fooled.
- **A consumer acting reasonably.** The test is not the most careless reader and not the
  most expert one.
- **Material.** It has to be something that could affect a purchase or use decision.
- **An omission counts.** Leaving out the thing that changes the picture is a way of
  deceiving.

**Unfairness** is the second half. In broad terms it concerns practices that cause
substantial injury to consumers that consumers cannot reasonably avoid and that is not
outweighed by countervailing benefits. It is the concept behind enforcement over things like
data practices and dark patterns.

Read the FTC's own published guidance rather than my summary of it. **[VERIFY]**

### State law is real law too

The competency says "federal and state." Ohio has its own consumer protection statute, the
Consumer Sales Practices Act, enforced by the Ohio Attorney General. State consumer
protection law often covers conduct that federal enforcement never reaches, because a state
attorney general can act on a local complaint about a local business.

**A student business, a club selling something, and a summer freelance job are all inside
this.** Being small does not move you outside the law, it moves you outside anybody's
enforcement priority list, which is a different thing and not a plan.

### Three more obligations worth knowing by name

**Endorsements and material connections.** If somebody endorses your product and has a
connection to you that a reader would not expect, that connection has to be disclosed. Your
friend posting a review without saying you built it together is the shape of this problem.

**Fake reviews.** Writing your own five-star reviews, or paying for them, is squarely inside
deception. The FTC has taken enforcement action in this area. **[VERIFY]** the current rule.

**Accessibility.** The Americans with Disabilities Act is the framework here. Federal
requirements for web and mobile accessibility have been the subject of recent rulemaking,
so confirm the current requirements at `https://www.ada.gov` **[VERIFY]** rather than
repeating anything you read in a blog post. The practical version for you: **a product that
a blind user cannot use is a product with a defect, and it is the defect most likely to be
both a legal problem and an ethical one at the same time.**

---

## What this looks like in an AI product

| Pattern | What it is | Why it is a problem |
|---|---|---|
| **AI washing** | Describing a product as AI-powered when the work is done by rules, templates, or people | A claim about what the product is, and it is false |
| **Unbacked accuracy** | "94% accurate" with no stated test set, no denominator, no method | Measurable claim, no substantiation |
| **Cherry-picked demo** | The demo runs the three prompts that work | Omission, and omissions count |
| **Hidden automation** | A customer believes they are talking to a person | Material to how they behave, and undisclosed |
| **Silent capability change** | The model behind the product changes and the behaviour changes with it | Yesterday's substantiation does not cover today's product |
| **Comparative claims** | "Better than the leading tutor app" | A measurable claim about somebody else's product, and it needs a test |

**The one people find hardest to accept is the last row of that list.** A claim about a
competitor is a factual claim and needs the same basis as a claim about yourself.

---

## Worked example 1: one test run, three honest-looking accuracy numbers

Every number here is invented for this lesson.

```python
# accuracy.py: one test run, three accuracy numbers, all of them arithmetic.
CARDS_TESTED = 50
HINTS_RETURNED = 40          # 10 cards got no hint: the model was unreachable
RATED_ACCEPTABLE = 34        # a human read all 40 and accepted 34
RATED_AMBIGUOUS = 4          # of the 6 rejected, 4 were arguable either way

headline = 100 * RATED_ACCEPTABLE / (HINTS_RETURNED - RATED_AMBIGUOUS)
returned = 100 * RATED_ACCEPTABLE / HINTS_RETURNED
attempted = 100 * RATED_ACCEPTABLE / CARDS_TESTED

print(f"Accepted, out of hints that were not ambiguous : {headline:.1f}%")
print(f"Accepted, out of hints returned                : {returned:.1f}%")
print(f"Accepted, out of cards the user asked about    : {attempted:.1f}%")
print()
print("Same 34 acceptable hints in all three lines.")
print("The only thing that changed is the denominator.")
```

Output:

```
Accepted, out of hints that were not ambiguous : 94.4%
Accepted, out of hints returned                : 85.0%
Accepted, out of cards the user asked about    : 68.0%

Same 34 acceptable hints in all three lines.
The only thing that changed is the denominator.
```

**No error. Three correct divisions. A twenty-six point spread.**

Which one goes on the poster? The honest answer is the third one, **68%**, because it is the
only denominator that matches what a user experiences. A user asks about a card. Either a
useful hint appears or it does not. From where the user is standing, the ten cards that got
no hint at all were failures, and calling them "not returned" is a category the user does
not have.

The first number, 94.4%, is the one a team reaches for, and look at how it is built:
excluding ambiguous cases, then excluding failures. **Both exclusions have a sensible
engineering reason and neither of them is visible in the printed number.** That is the
mechanism of an unsubstantiated claim, in three lines of arithmetic.

**What substantiation looks like here.** Not a bigger number. A sentence next to the number:

> In a test of 50 chemistry cards, hints were produced for 40 and a teacher accepted 34 of
> those. Counting every card asked about, 68% produced an accepted hint. Test set and
> ratings are in `tests/hint-quality.md`.

## Worked example 2: sorting your own marketing copy

```python
# claims_check.py: sort marketing copy into claims you must be able to back up
# and claims that are opinion, then say which ones you have evidence for.

CLAIMS = [
    ("Study Buddy makes studying better", None),
    ("Study Buddy writes hints that are 94% accurate", None),
    ("Study Buddy runs entirely on your own computer",
     "read the source: MODEL_HOST is 127.0.0.1, one urlopen, nothing else"),
    ("Study Buddy is the best flashcard app for high school", None),
    ("Study Buddy never sends your notes anywhere",
     "ran it with the network adapter disabled; deck written, no error"),
    ("Study Buddy works with any subject", None),
]

OBJECTIVE_SIGNALS = ("%", "never", "entirely", "any", "all", "guaranteed",
                     "faster", "accurate", "free")

print(f"{'claim':<52} {'kind':<12} evidence")
print("-" * 92)
for text, evidence in CLAIMS:
    lowered = text.lower()
    objective = any(signal in lowered for signal in OBJECTIVE_SIGNALS)
    kind = "measurable" if objective else "opinion"
    if not objective:
        status = "none needed"
    elif evidence:
        status = evidence
    else:
        status = "NONE. Do not publish this claim."
    print(f"{text:<52} {kind:<12} {status}")

print()
print("A measurable claim with no evidence is the row to fix before launch.")
print("This program sorts sentences. It does not decide what the law requires.")
```

Output:

```
claim                                                kind         evidence
--------------------------------------------------------------------------------------------
Study Buddy makes studying better                    opinion      none needed
Study Buddy writes hints that are 94% accurate       measurable   NONE. Do not publish this claim.
Study Buddy runs entirely on your own computer       measurable   read the source: MODEL_HOST is 127.0.0.1, one urlopen, nothing else
Study Buddy is the best flashcard app for high school opinion      none needed
Study Buddy never sends your notes anywhere          measurable   ran it with the network adapter disabled; deck written, no error
Study Buddy works with any subject                   measurable   NONE. Do not publish this claim.

A measurable claim with no evidence is the row to fix before launch.
This program sorts sentences. It does not decide what the law requires.
```

**This program is wrong about two rows, on purpose, and finding them is the exercise.**

- **"Study Buddy is the best flashcard app for high school."** The program called it opinion
  because no keyword matched. A superiority claim comparing your product against others is
  the kind of claim that is treated as a factual one, and backing it up would require testing
  against those others. Classified wrong.
- **"Study Buddy makes studying better."** Called opinion. It is a performance claim about
  what the product does to a user's outcome, and that is the sort of thing you would need a
  basis for. At best it is on the line. Classified at least questionably.

**A keyword list cannot tell a factual claim from an opinion**, because the difference is
about what is being asserted, not about which words appear. Notice what the program did have
right: both rows with no evidence and a measurable claim were flagged, and the one place it
is confidently useful is the place you would have caught anyway.

**This is the running thread again.** A program that produces a clean table is not a program
that produced the right answer, and this time the wrong answer is on your own marketing copy.

---

## The wrong version, and what it does instead of an error

A team writes this for the showcase table, and a model wrote the first draft:

> **Study Buddy uses advanced AI to generate study hints with 94% accuracy. Trusted by
> students across the district. Works with any subject. Your data never leaves your
> computer.**

**Nothing errors. It reads like every product page you have ever seen.** Four sentences,
four problems.

| Claim | Problem |
|---|---|
| "94% accuracy" | The denominator was chosen after the fact and is not stated. Worked example 1 is the whole story. |
| "Trusted by students across the district" | How many students, and did any of them say that. If this means six friends, it is a representation likely to mislead about something material. |
| "Works with any subject" | The parser requires a colon on every line and was tested on chemistry. "Any" is measurable and there is no evidence. |
| "Your data never leaves your computer" | This one happens to be true, and it is the most important claim on the poster. It is also the only one somebody will build a decision on. |

**Look at that last row, because it is the point of the whole lesson.** The true claim sits
next to three shaky ones. A reader who checks and finds "works with any subject" is false has
no reason to believe the sentence about data, which was the one that mattered and the one you
could prove. **Unsubstantiated claims cost you the credibility of your substantiated ones.**

## Why the wrong version is tempting

**Everybody else's page reads like that.** You have read a thousand product pages and this is
the register they are written in. Copying the register imports the claims.

**The number is real arithmetic.** 94.4% came out of a real division of real ratings. It feels
dishonest to publish 68% when 94% is "also true", and that feeling is exactly the thing this
lesson is trying to interrupt. **Both are arithmetic. Only one of them answers the question a
buyer is asking.**

**Nobody at a high school showcase is going to sue you.** True, and irrelevant. The habit you
build here is the habit you take to a job where somebody will. You are also going to be asked
to write claims for somebody else's product one day, and the person asking you will not be
pleased when you slow down. **Deciding now what you will and will not write is much cheaper
than deciding it then.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **Deception** | A representation, omission, or practice likely to mislead a reasonable consumer about something material. |
| **Unfairness** | Practices causing substantial consumer injury that consumers cannot reasonably avoid and that is not outweighed by benefits. |
| **Substantiation** | Having a reasonable basis for a factual claim before you make it. |
| **Material** | Capable of affecting a consumer's decision. |
| **Puffery** | Broad subjective praise that no reasonable person treats as a factual claim. A narrow category. |
| **Comparative claim** | A factual claim about how your product compares with another. Needs a basis like any other. |
| **Material connection** | A relationship between an endorser and a seller that a reader would not expect. Has to be disclosed. |
| **AI washing** | Describing a product as AI-powered when it is not. |
| **Dark pattern** | An interface designed so that the choice the user wants is harder than the one the seller wants. |
| **Denominator** | The thing you divided by. Usually the most important undisclosed part of a performance claim. |

---

## Self-check

**Question 1.** Rewrite the four-sentence Study Buddy blurb so that every claim in it is one
you could back up with something in the repository. You may drop claims. Say what you dropped
and what evidence file each surviving claim points at.

**Question 2.** Your team's demo uses three prompts. Those three work reliably. Two others you
tried are bad about half the time. Is running the demo with only the three a deception
problem? Answer, defend it, then say what you would do.

**Question 3.** `claims_check.py` classified "the best flashcard app for high school" as
opinion. Explain in two sentences why a keyword list can never get this right, and write the
one question you would ask about any sentence to classify it yourself.

---

### Answers

**1.** For example:

> Study Buddy turns a page of notes into a flashcard deck. It runs on a locally hosted model
> on your own computer, and makes no network call except to that model on your own machine
> (see `study_buddy.py`, `MODEL_HOST`, and the single `urlopen`). In our test of 50 chemistry cards, 34 produced a hint
> a teacher accepted, which is 68% of cards asked about (`tests/hint-quality.md`). It has been
> tested on chemistry and biology notes formatted as `Term: definition`.

**Dropped:** "advanced AI", which asserts nothing checkable. "Trusted by students across the
district", which has no basis. "Works with any subject", replaced with the subjects actually
tested and the format required. The accuracy claim kept, with the denominator stated and a
file named.

**2.** **Yes, if you do not say so, and it is the omission that does it.** A demo is a
representation of how the product behaves, and choosing only the cases that work, without
saying that is what you did, is the kind of omission that misleads a reasonable person about
something material.

**What to do:** run the three, and then say one sentence out loud. "We also tested two
harder prompts and those work about half the time. Here is one." **Doing that in front of a
judge is a strength, not a weakness**, because a judge who discovers a weakness you disclosed
trusts the rest of your demo, and a judge who discovers one you hid does not.

**3.** A keyword list looks at which words appear, and the distinction is about what is being
asserted. "Best" can appear in a claim that is checkable by testing and in one that is pure
taste, and the same word does opposite jobs in the two sentences.

**The question to ask:** *could two honest people, with access to the product and enough
time, settle this by testing?* If yes, it is a factual claim and you need the evidence before
you publish it. If no, it is opinion. That question also catches the comparative claims a
keyword list misses, because "better than theirs" is settleable by testing both.
