# Protecting Data You Hold, and Saying Only What Is True About It
## 145130 Applications of AI · Module 4 · Week 11, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W11_ProtectingData.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W11_ProtectingData.pptx)

**This lesson makes no legal claims and gives no legal advice.** It describes what a
protection framework is for, and it is precise about what technical controls do and do not
do. Where something is a question for the district's own policy owner, it says so.

---

## Why this lesson sits here and not in Module 3

Module 3 was about the law. This is about the database you built on Monday, and one sentence:

> **Every field you keep is a field somebody has to protect, and the cheapest field to protect
> is the one you did not collect.**

You have now built a system that holds fourteen people's names, grade levels, programs, and
a record of what they borrowed and when. That is a small amount of data and it is enough to
answer questions nobody should be asking about a person.

---

## The three things people mix up

| Control | What it actually does | What it does not do |
|---|---|---|
| **Encryption at rest** | makes the file unreadable to somebody who has the disk and not the key | nothing about a person who is already signed in and can open the folder |
| **Encryption in transit** | stops somebody on the network reading the data as it moves | nothing about either end |
| **Access control** | decides who may open the thing at all | nothing about somebody who is allowed in and should not be |

**These are three different controls answering three different questions, and the most common
overstatement in this field is treating one as all three.**

The sentence to learn to distrust:

> "The data is encrypted, so member records are protected and access control is handled."

Three claims in one sentence and only the first is true. Encryption at rest protects a
stolen disk. It does nothing about the twelve people who can already open that shared folder,
because the file decrypts for them automatically. **That is what "at rest" means.** And
encryption is not access control, so the third clause has not been addressed at all.

**You will meet that exact sentence in this module's Week 12 Gate 2**, in a document that gets
several other things right.

---

## CIA: three words that separate three problems

You met these in 145060 and they are on this exam too.

- **Confidentiality.** Only the right people can read it.
- **Integrity.** It is correct and has not been changed by accident or on purpose.
- **Availability.** It is there when somebody needs it.

Everything in this module so far has been **integrity**: keys, constraints, transactions,
quarantine, and the fidelity check. Today is mostly **confidentiality**. And they trade
against each other, which is the part worth knowing: the strongest confidentiality control is
deleting the data, and that is also the worst thing you can do to availability.

---

## Worked example: what your own report gives away

Section 4 of the makerspace report:

```
4. HOLDS: MEMBERS WITH AN OVERDUE ITEM
  member   name           item     equipment                   due         days overdue
  -------  -------------  -------  --------------------------  ----------  ------------
  RC-0171  Sela Vaifale   EQ-0115  Vinyl cutter                2027-03-12            49
  RC-0174  Noor Haddad    EQ-0150  Robot chassis kit           2027-03-28            33
  RC-0181  Emiliano Cruz  EQ-0150  Robot chassis kit           2027-04-15            15
  RC-0142  Amara Delgado  EQ-0122  Digital oscilloscope        2027-04-27             3
  RC-0174  Noor Haddad    EQ-0102  Filament 3D printer, bay 2  2027-04-27             3
```

**That section names five people and says something unflattering about each of them.** Every
other section of the report is counts and totals and names nobody.

The makerspace's own handbook says the board report carries counts by category and by program
and no names, and that a question about who has something goes to a staff member. So the
report is correct to have that section and **the section must not leave the room.**

Your report already prints a line saying so. That line is not decoration: it is the only
thing standing between a correct report and a correct report pasted into an email.

**The design question to sit with:** should that section be a separate command, so the default
output carries no names at all and naming a person takes a deliberate act? The reference
implementation says yes in its known limitations and did not do it. **That is an honest answer
and it is not a good one. Do better than the reference.**

---

## Minimization, with the example in front of you

Your `members` table has a `grade_level` column. Go and find where the report uses it.

It does not. It is in the schema because it was in the source file.

**A field you keep and never use is pure cost.** It can be leaked, it can be wrong, it can be
used later for something nobody agreed to, and it protects nothing. The makerspace's own
privacy document says every field had to earn its place by answering a question the makerspace
actually has to answer.

Three questions to ask of every column, and put them in your `data-protection.md`:

1. **What question does this answer?** If you cannot name one, it should not be there.
2. **What is the worst thing somebody could do with it?**
3. **How long does it have to exist?**

---

## FERPA, at the level this course teaches it

The makerspace records are the **shape** of a student education record: a name, a grade level,
a program, and a history attached to a person at a school.

In the United States there is a federal framework covering student education records. **What
it is for** is to say who may see a student's record, and to give students and families a say
in it. That purpose is the thing to understand.

**What this course does not do, and you should not either:**

- state a threshold, a penalty, a deadline, or an exception
- tell somebody their system is or is not compliant
- give legal advice in a README

**What you do instead**, and this is the actual professional skill:

> "These records are the shape of a student record. Before this runs on real students, the
> person who owns the district's records policy has to see the field list, the retention rule,
> and who can read the holds report. Here is that list and here are my three questions."

**Naming the right person and arriving with a specific list is the whole job.** A developer
who says "I think this is fine" and a developer who says "I do not know, here is what I built
and here is who needs to look at it" are not equally useful, and only one of them is right.

Your fixture is invented for exactly this reason. It lets you practise the analysis without
holding anybody's record.

---

## Verifying compliance with a rule you were given

The competency is 1.4.3: **verify** compliance, not assume it. Verification means a check
somebody else could repeat.

| The rule | How you verify it | What "verified" looks like |
|---|---|---|
| foreign keys are enforced | `PRAGMA foreign_keys` on the live connection | `(1,)`, plus a test that inserts an orphan and expects an error |
| the board report names nobody | run it and search the output for a member id | a test asserting no `RC-` appears in the board sections |
| nothing is dropped silently | rows read equals loaded plus quarantined | the arithmetic line in the load output |
| no credentials in the repository | scan every source file for the obvious markers | a test that fails if one appears |

**A checklist somebody ticked is not verification.** A command anybody can run is.

---

## The wrong version, and what it produces

```python
# Protect the member data before it leaves the building.
import base64

encoded = base64.b64encode(open("makerspace.db", "rb").read())
open("makerspace.db.enc", "wb").write(encoded)
print("Database encrypted.")
```

```
Database encrypted.
```

**It is not encrypted.** Base64 is an encoding, not a cipher. It has no key, it is reversible
by anybody in one line, and its whole purpose is to move binary data through text channels.

```
python -c "import base64; print(base64.b64decode(open('makerspace.db.enc','rb').read())[:16])"
```

```
b'SQLite format 3\x00'
```

**Why it is tempting.** The output is unreadable, so it looks protected, and the word
"encoded" is one letter away from the word people mean. This is the shape of most security
theatre: a control that changes how something looks and not who can read it.

**The honest version of that program** is a comment saying the file is stored on a share whose
access list is managed by somebody else, naming who, and saying what that does and does not
protect.

---

## Vocabulary

| Term | What it means |
|---|---|
| **encryption at rest** | stored data is unreadable without a key |
| **encryption in transit** | data moving over a network is unreadable to a listener |
| **access control** | who is allowed to open the thing |
| **data minimization** | collecting and keeping only the fields that answer a question you have |
| **retention** | how long a record is kept before it is deleted |
| **CIA** | confidentiality, integrity, availability |
| **encoding** | changing how data is represented, with no secret involved |

---

## Self-check

**1.** A plan says the database is on an encrypted shared drive, so member records are
protected. Name the two separate overstatements and say what question is left unanswered.

**2.** Your `members` table has a column nothing in the report uses. Give two reasons to
remove it and one reason somebody might keep it.

**3.** Somebody asks whether your project is FERPA compliant. What do you say, and what do you
do next?

### Answers

**1.** First: encryption at rest protects against a stolen disk, not against somebody signed
in who can already open the folder, and for them the file decrypts automatically. Second:
encryption is not access control, so saying access is handled is a different claim that has
not been made true. **The unanswered question is who may open that folder**, which is the only
control that affects the holds list.

**2.** Remove it because a field you never read cannot be right and can still be leaked, and
because holding a field nobody agreed to is how a system ends up used for something it was
not built for. **Keep it** if there is a question somebody genuinely asks that needs it, such
as reporting participation by grade to the board, in which case it earns its place and the
report should actually use it.

**3.** Say that you are not the person who can answer that, and that you are not going to
guess. Then do the useful part: bring the field list, the retention rule, who can read each
section of the report, and the three questions you have, to the person who owns the district's
records policy. **Arriving with the list is the job. Guessing is not.**
