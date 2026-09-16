# Lecture Notes: Conflicts of Interest, and the Three Sets of Rules You Live Under
## 145130 Applications of AI · Module 3 · Week 8, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W08_ConflictsOfInterest.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W08_ConflictsOfInterest.pptx)

If you missed class, you can learn this concept from this file alone. Run the program.

**Competencies:** 1.3.9 (identify potential conflicts of interest between personal,
organizational, and professional ethical standards, including personal gain and project
bidding), 1.3.3 (ethical character traits consistent with workplace standards).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** Conflict of
interest rules come from several places at once: employment contracts, professional codes,
purchasing policy, and in the public sector, state law. Which ones apply to you depends on
who you work for.

Two sources worth knowing by name:

- **The ACM Code of Ethics and Professional Conduct** and **the IEEE Code of Ethics**, the
  two professional codes most often cited in software. Both are published by the
  organizations themselves. **[VERIFY]** their current addresses before assigning them.
- **The Ohio Ethics Commission**, which administers Ohio's ethics law for public officials
  and public employees. A school district employee is in that category, which is directly
  relevant to a district buying software. **[VERIFY]** through the State of Ohio's official
  site, and confirm you are on a `.gov` page.

---

## Why this exists

You are going to be asked for a recommendation, sooner than you expect.

A teacher will ask which tool the class should use. A club will ask which vendor to go
with. A manager will ask which library to standardize on. Every one of those is a moment
where somebody trusts your judgement, and where you might have a reason to prefer one
answer that has nothing to do with the question.

**The failure is almost never corruption.** It is a person with a real preference, a real
relationship, and no place in the process where the relationship gets written down. By the
time anybody notices, a decision has been made and cannot be unwound without embarrassing
somebody.

---

## What a conflict of interest actually is

**A conflict of interest is a situation where your personal interest could influence, or
could reasonably appear to influence, a decision you are making on somebody else's behalf.**

Three things in that sentence do a lot of work.

**"Could influence."** Not "did influence". You do not have to be corrupt to have a
conflict. Having one is not an accusation, it is a fact about a situation.

**"Could reasonably appear to."** This is the part students argue with, and it is the part
that matters most. Even if you are certain you would be fair, a decision made by somebody
with an undisclosed interest cannot be trusted by anybody else, because they cannot see
inside your head. **The value being protected is not your integrity. It is the
decision's.**

**"On somebody else's behalf."** A conflict requires that you are acting for another party:
your school, your employer, your client, your team. Choosing a laptop for yourself cannot
be a conflict of interest. Choosing one for the district can.

---

## The three sets of standards, and where they collide

The competency's exact words are conflicts "between personal, organizational, and
professional ethical standards." Those are three separate rulebooks and you are under all
three at once.

| Standard | Where it comes from | Example of what it asks |
|---|---|---|
| **Personal** | Your own values, your family, your community | Loyalty to a friend. Helping your family's business |
| **Organizational** | Your employer, school, or client: policy, contract, purchasing rules | Do not accept gifts from vendors. Disclose outside work. Follow the bid process |
| **Professional** | Codes like the ACM's and the IEEE's, and the expectations of the field | Be honest about your qualifications. Give credit. Avoid harm. Do not misrepresent what a system can do |

**The collisions are the interesting part, and they are real.**

- Your personal standard says be loyal to your friend. Your professional standard says
  report the defect you found in their code. Both are real obligations.
- Your organizational standard says your employer's interests come first. Your professional
  standard says do not misrepresent what the system can do to a customer. When a manager
  asks you to soften a limitation in a sales document, those two are in direct conflict.
- Your personal standard says help the family business. Your organizational standard says
  disclose and step out of the decision.

**When they collide, the professional standard is the one that protects you.** It is the
one written down by people who are not in the room, and it is the one you can point at.
"Our code of ethics says I have to disclose this" is a sentence that ends an argument
without making it personal.

---

## The shapes a conflict takes

| Shape | What it looks like | What makes it a conflict |
|---|---|---|
| **Personal gain** | You recommend the tool you hold stock in, or built, or get paid to promote | Your gain is tied to the recommendation |
| **Project bidding** | You evaluate bids and one bidder employs your parent | Your evaluation affects somebody you are close to |
| **Gifts and hospitality** | A vendor pays for a conference trip, a laptop, dinner | Reciprocity is a real psychological effect and does not require a deal |
| **Outside employment** | You work weekends for a competitor of your employer | Two employers with opposing interests, one of you |
| **Self-dealing with data** | You use data you have access to at work for a project of your own | The access was given for a job, not for you |
| **Evaluating your own work** | You benchmark your own model, or grade your own team's entry | Nobody is a neutral judge of their own work |

### The AI-specific ones, because this is that course

**Benchmarking your own model.** If you built it, you choose the test set, you choose the
baseline, and you decide when to stop tuning. Every one of those is a place a preference
leaks in without anybody deciding to cheat.

**Recommending a tool you have a relationship with.** A free student licence, a
sponsorship, an internship, a club donation. Every one of those is a relationship, and none
of them is a bribe.

**Writing the evaluation criteria after seeing the products.** This is the quiet one. If
the requirements list is written after somebody has already fallen in love with a tool,
those requirements will describe that tool. The fix is to write the criteria first and date
the file.

---

## What you actually do about one

Four moves, in increasing order of severity. **Disclosure is the first move in every case,
and doing nothing is never one of the four.**

1. **Disclose.** Write it down, to the person who owns the decision, before the decision.
   In many situations disclosure is all that is needed.
2. **Recuse.** Take yourself out of that specific decision. Stay on the team, step out of
   the room for that vote.
3. **Divest.** Get rid of the interest. Sell the stock, end the side work, return the gift.
4. **Decline.** Turn down the role entirely, when the conflict is structural and cannot be
   separated from the job.

A disclosure that is worth the paper it is on is specific:

> "Before we score these, I need to disclose that my mother has worked at NorthPath
> Learning for six years, in a department unrelated to this product. I am happy to score
> the other two and step out for NorthPath, or step out of the evaluation entirely,
> whichever the committee prefers."

Notice what that does. It states the relationship, it states its size, it offers options,
and it hands the decision to somebody else. **Handing the decision to somebody else is the
whole mechanism.**

---

## Worked example: the same data, three different winners

**This scenario is a composite, invented for this lesson. The district, the vendors, and
the evaluators are not real.** A district is choosing an AI tutoring vendor. Three
evaluators scored three bids.

```python
# conflict_scan.py: find every score cast by an evaluator with a declared
# relationship to the vendor being scored.
# Every person, vendor, and relationship below is invented for this lesson.

SCORES = [
    ("Chen", "NorthPath Learning", 91),
    ("Chen", "Kettle Ridge AI", 62),
    ("Chen", "Open Tutor Co-op", 70),
    ("Delgado", "NorthPath Learning", 74),
    ("Delgado", "Kettle Ridge AI", 79),
    ("Delgado", "Open Tutor Co-op", 81),
    ("Ferris", "NorthPath Learning", 88),
    ("Ferris", "Kettle Ridge AI", 66),
    ("Ferris", "Open Tutor Co-op", 64),
]

RELATIONSHIPS = [
    ("Chen", "NorthPath Learning", "parent is employed there"),
    ("Ferris", "NorthPath Learning", "accepted a paid conference trip from them"),
]

flagged = {(person, vendor): reason for person, vendor, reason in RELATIONSHIPS}

totals = {}
clean_totals = {}
for person, vendor, score in SCORES:
    totals[vendor] = totals.get(vendor, 0) + score
    if (person, vendor) not in flagged:
        clean_totals[vendor] = clean_totals.get(vendor, 0) + score

print("Every score, with conflicts marked:\n")
for person, vendor, score in SCORES:
    reason = flagged.get((person, vendor))
    mark = f"  <-- CONFLICT: {reason}" if reason else ""
    print(f"  {person:<10} {vendor:<22} {score:>3}{mark}")

print("\nRanking using every score:")
for vendor, total in sorted(totals.items(), key=lambda pair: -pair[1]):
    print(f"  {vendor:<22} {total}")

print("\nRanking with conflicted scores removed:")
for vendor, total in sorted(clean_totals.items(), key=lambda pair: -pair[1]):
    print(f"  {vendor:<22} {total}")

print("\nThis program finds declared relationships. It cannot find undeclared ones,")
print("and it does not decide whether anybody was actually influenced.")

counts = {}
for person, vendor, score in SCORES:
    if (person, vendor) not in flagged:
        counts[vendor] = counts.get(vendor, 0) + 1

print("\nAverage of the scores that are left, which is not the same ranking:")
for vendor in sorted(clean_totals, key=lambda v: -clean_totals[v] / counts[v]):
    print(f"  {vendor:<22} {clean_totals[vendor] / counts[vendor]:.1f} "
          f"from {counts[vendor]} score(s)")
```

Output:

```
Every score, with conflicts marked:

  Chen       NorthPath Learning      91  <-- CONFLICT: parent is employed there
  Chen       Kettle Ridge AI         62
  Chen       Open Tutor Co-op        70
  Delgado    NorthPath Learning      74
  Delgado    Kettle Ridge AI         79
  Delgado    Open Tutor Co-op        81
  Ferris     NorthPath Learning      88  <-- CONFLICT: accepted a paid conference trip from them
  Ferris     Kettle Ridge AI         66
  Ferris     Open Tutor Co-op        64

Ranking using every score:
  NorthPath Learning     253
  Open Tutor Co-op       215
  Kettle Ridge AI        207

Ranking with conflicted scores removed:
  Open Tutor Co-op       215
  Kettle Ridge AI        207
  NorthPath Learning     74

This program finds declared relationships. It cannot find undeclared ones,
and it does not decide whether anybody was actually influenced.

Average of the scores that are left, which is not the same ranking:
  NorthPath Learning     74.0 from 1 score(s)
  Open Tutor Co-op       71.7 from 3 score(s)
  Kettle Ridge AI        69.0 from 3 score(s)
```

**Three rankings. Three different first places, from one set of numbers.**

- With every score counted, NorthPath wins by 38 points.
- With conflicted scores dropped, NorthPath comes last, because it now has one score against
  everyone else's three. That comparison is meaningless and the program printed it anyway.
- Averaging what is left puts NorthPath first again, on a single score from a single person.

**None of these three is the answer, and that is the lesson.** Once the conflict is in the
data, no arithmetic gets it out. A committee that discovers this after scoring has only bad
options. A committee that collected disclosures before scoring would have replaced two
evaluators and had nine clean scores.

Look at Chen's row for the thing that arithmetic cannot see. Chen scored NorthPath 91 and
the next-best vendor 70, a 21-point gap, the largest single gap in the table. **That is not
proof of anything.** Chen may be right. The point is that nobody can now tell, including
Chen, and the reason nobody can tell is a process failure that happened weeks earlier.

---

## The wrong version, and what it does instead of an error

What the wrong version looks like is nothing at all. Nobody says anything, the scores are
totalled, NorthPath wins by 38, and a purchase order goes out. **There is no error state.
There is no moment where the process notices.** The conflict only becomes visible if
somebody mentions it, and the whole difficulty of this topic is that mentioning it is
socially expensive and staying quiet is free.

Three sentences that keep people quiet, and what is wrong with each:

- **"It would not change my scoring."** Probably true and not the point. The decision has to
  be trustworthy to people who cannot read your mind.
- **"Everybody knows my mom works there."** Known informally is not disclosed. Nothing is
  written down, nobody decided what to do about it, and the people who did not know are not
  in the room to say so.
- **"It is only a conference trip, it is not a bribe."** Correct, it is not a bribe, and
  reciprocity does not require one. This is precisely why organizations have gift policies
  with low thresholds: not because a dinner buys a decision, but because the rule saves
  everybody from having to judge which dinner did.

## Why the wrong version is tempting

**Disclosing feels like accusing yourself.** It reads as an admission that you might be
unfair. It is the opposite: it is the move that lets the decision survive somebody finding
out later.

**The relationship is usually real and good.** Your mom works somewhere. Your friend built
the thing. You liked the conference. Nothing about the relationship is bad, and that makes
it feel strange to report.

**Nothing happens if you stay quiet, until something does.** Most undisclosed conflicts
never surface. The ones that surface do so at the worst possible moment: an audit, a protest
from a losing bidder, a news story, a competitor's complaint. **And the thing that ends the
career is almost never the conflict. It is the nondisclosure.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **Conflict of interest** | A situation where a personal interest could influence, or appear to influence, a decision made for somebody else. |
| **Appearance standard** | The test is how it looks to a reasonable outsider, not whether you would actually be swayed. |
| **Disclosure** | Writing the interest down, to the decision owner, before the decision. |
| **Recusal** | Removing yourself from one specific decision. |
| **Divestment** | Getting rid of the interest itself. |
| **Self-dealing** | Using a position or access for your own benefit. |
| **Project bidding** | A competitive purchasing process, where conflicts are most visible and most regulated. |
| **Gift policy** | An organizational rule about what may be accepted from vendors, usually with a low threshold. |
| **Professional code of ethics** | A published statement of obligations, such as the ACM's or the IEEE's. |

---

## Self-check

**Question 1.** Your team is entering a competition. One judge is a family friend who has
eaten dinner at your house twice. You are not required to do anything. Name the two moves
available to you, say which one you would pick, and say who the disclosure protects.

**Question 2.** A teammate proposes using a tool because "they gave our club a free upgrade
last year." Is this a conflict of interest? Answer yes or no, defend it, then say what
should happen next regardless of your answer.

**Question 3.** In the worked example, which single change to the process would have
prevented all three rankings from existing? Name the change, name when it has to happen, and
say what it costs.

---

### Answers

**1.** The two moves are **disclose** and **decline** the situation, which here would mean
asking for a different judge or withdrawing from that judge's bracket. Realistically you
disclose, in writing, to whoever runs the competition, before judging: name the
relationship, name how close it is, and let them decide.

**Who it protects is the question worth getting right. It is not you.** It is the judge, who
would otherwise be placed in an impossible position later, and every other team in the
bracket, whose result has to be trustworthy. Your own reputation is protected as a side
effect, which is a nice property of doing the right thing here and not the reason to do it.

**2.** Both answers can earn full credit if defended.

**Yes:** the club received a benefit from the vendor, and the teammate is citing that
benefit as a reason to choose them. That is reciprocity operating exactly as it does, and
the fact that it is being said out loud does not make it a technical argument.

**No, in the strict sense:** a conflict requires a personal interest, and the benefit went
to the club rather than to the teammate. This is better described as a relationship that
should be disclosed than as a personal conflict.

**What happens next is the same under either answer.** Write the relationship down. Then
notice the more serious problem in the teammate's sentence: **a free upgrade is not a
technical reason.** Ask for the evaluation criteria, written before anybody looked at
products, and score every tool against them.

**3.** **Collect disclosures before scores.** It has to happen before evaluators see the
bids, because a disclosure collected afterwards cannot un-see anything and cannot restore a
clean set of scores.

**What it costs:** two evaluators have to be replaced, which means finding two people, which
means the evaluation takes a week longer. That is the real cost and it is why this gets
skipped. Compare it with the cost in the example, which is a purchase the district cannot
defend and a process that has no defensible answer available to it at all.
