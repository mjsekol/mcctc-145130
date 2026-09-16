# Lecture Notes: Which Framework Governs Which Data
## 145130 Applications of AI · Module 3 · Week 9, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W09_PrivacyFrameworkMap.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W09_PrivacyFrameworkMap.pptx)

If you missed class, you can learn this concept from this file alone. Run the program.

**Competencies:** 2.1.12 (describe privacy security compliance on systems: HIPAA, PCI, SOX,
ADA, GDPR, EUDPR), 1.3.4 (how federal and state consumer protection laws affect products and
services), 1.3.8 (verify compliance with computer laws and regulations).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** This file teaches
what each framework is **for** and **who it follows**, which is the level the competency asks
for and the level where certainty is available. It does not state section numbers, breach
thresholds, penalty amounts, or who exactly is in scope, because those are the details that
change and that a wrong lesson does the most damage with.

One of the exit criteria for this module is "name which privacy framework governs a given
category of data." Today is that day, and there is a correction built into that sentence that
you will meet in the first paragraph of the next section.

Primary sources, each one published by the body that administers the framework:

| Framework | Who publishes it | Address |
|---|---|---|
| HIPAA | U.S. Department of Health and Human Services, Office for Civil Rights | `https://www.hhs.gov/hipaa` **[VERIFY]** |
| PCI DSS | PCI Security Standards Council | `https://www.pcisecuritystandards.org` **[VERIFY]** |
| SOX | U.S. Securities and Exchange Commission | `https://www.sec.gov` **[VERIFY]** |
| ADA | U.S. Department of Justice | `https://www.ada.gov` **[VERIFY]** |
| GDPR and EUDPR | European Commission, and the European Data Protection Supervisor for the EUDPR | `https://commission.europa.eu` and `https://www.edps.europa.eu` **[VERIFY]** |
| FERPA | U.S. Department of Education, Student Privacy Policy Office | `https://studentprivacy.ed.gov` **[VERIFY]** |
| COPPA | Federal Trade Commission | `https://www.ftc.gov` **[VERIFY]** |

---

## Why this exists, and the correction in the exit criterion

**The question "what framework governs this category of data" is the wrong question, and it
is wrong in a way that costs people real money.**

Most of these frameworks do not follow the data. **They follow the holder and the
relationship.** The same fact, in two different hands, can be under one framework, under
another, or under none.

Blood pressure readings at a hospital are one thing. The identical numbers, typed by the same
person into a fitness app they downloaded, are usually a completely different thing. Nothing
about the data changed. **The holder changed, and the holder is what the framework attaches
to.**

So the exit criterion is really three questions:

1. **What is the information?**
2. **Who is holding it, and in what relationship to the person it is about?**
3. **Where are the people it is about?**

Answer all three and the framework is usually obvious. Answer only the first and you will be
confidently wrong, in the way the internet is confidently wrong about HIPAA every single day.

---

## The six on the competency list, plus two you need

### HIPAA

**What it is for:** protecting health information held in the health care system.

**Who it follows:** covered entities, which broadly means health plans, health care
clearinghouses, and health care providers who transmit health information electronically in
connection with certain transactions, plus their business associates, which are the
organizations that handle that information on their behalf.

**Its two main pieces** are the Privacy Rule, about uses and disclosures of protected health
information, and the Security Rule, about safeguards for electronic protected health
information. Enforcement in the United States is through the Department of Health and Human
Services, Office for Civil Rights.

**The mistake everybody makes:** "that is a HIPAA violation" said about a school, an employer,
a neighbour, or a social media post. **HIPAA does not follow the topic.** A nurse telling
somebody about your visit is a very different situation from your friend telling somebody,
and only one of them is inside HIPAA.

### PCI DSS

**What it is for:** protecting payment card data.

**Who it follows:** organizations that store, process, or transmit cardholder data.

**The thing to know, and the thing most often gotten wrong: PCI DSS is not a law.** It is a
standard published by the PCI Security Standards Council, and it reaches you through contracts
with card brands, banks, and processors. The consequences of failing it are contractual, not
statutory. It is the odd one out on the competency's list and saying so out loud is worth a
point on any assessment.

**Why it matters to you anyway:** the requirements are concrete and they are a good model for
thinking about any sensitive data. Do not store what you do not need. Encrypt what you
transmit. Restrict access. Log it. Test it.

### SOX

**What it is for:** the accuracy and reliability of financial reporting by public companies,
after a series of accounting scandals.

**Who it follows:** public companies and the people who audit them.

**Why it is on a privacy list at all:** it is the reason a lot of technology controls exist in
corporate environments. Change management, access control, audit logs, and records retention
are all things SOX pushed into IT departments, and you will work inside those controls one
day. **It is not a privacy law.** It is a financial integrity law that produced privacy-shaped
controls, and knowing that distinction is worth more than memorizing it as a privacy
framework.

### ADA

**What it is for:** prohibiting discrimination on the basis of disability.

**Who it follows:** employers, state and local government entities, and places of public
accommodation, under different titles of the act.

**Why it is here:** accessibility is the part of this list that touches the interface you are
building rather than the database behind it. Web and mobile accessibility requirements for
covered entities have been the subject of recent federal rulemaking, so **confirm the current
requirements at `https://www.ada.gov` [VERIFY] rather than repeating anything you read in a
blog post, including this file.**

**The practical version:** a school is a covered entity, and a feature a student using a
screen reader cannot operate is a defect with a legal dimension.

### GDPR

**What it is for:** protecting personal data as a matter of individual rights, across all
sectors.

**Who it follows:** organizations processing personal data in the context of an EU
establishment, and, under conditions the regulation sets out, organizations outside the EU
that offer goods or services to, or monitor the behaviour of, people in the EU.

**The parts to know by name**, because they are the best available checklist for designing
anything:

- **The principles**, in Article 5: lawfulness, fairness, and transparency; purpose
  limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality;
  and accountability.
- **The lawful bases**, in Article 6. Consent is one of several. It is not the default and it
  has conditions attached to how it is obtained.
- **Data subject rights**, including access, rectification, erasure, restriction, portability,
  and objection.
- **Automated decision-making**, in Article 22, which concerns decisions based solely on
  automated processing that produce legal or similarly significant effects on a person.
- **Data protection impact assessments**, in Article 35, for processing likely to result in a
  high risk to people's rights and freedoms. **That is the ancestor of the document you are
  writing this week.**

Read the regulation's own text for any of these. **[VERIFY]**

### EUDPR

**What it is for:** the same kind of protection, applied to the European Union's own
institutions, bodies, offices, and agencies.

**Who it follows:** those institutions. It is supervised by the European Data Protection
Supervisor.

**Why it exists as a separate thing:** the EU wrote general rules for everybody else and then
had to bind itself under a parallel instrument. **If you can say "EUDPR is GDPR-shaped rules
for the EU's own institutions," you have the competency.**

### FERPA, which is not on the competency list and is the one that governs you

**What it is for:** privacy of education records at schools that receive funds under an
applicable U.S. Department of Education program.

**Who it follows:** those schools.

**What it gives people:** parents, and students once the rights transfer to them, have rights
to inspect education records, to request correction of records they believe are inaccurate,
and to control disclosure of personally identifiable information from those records, subject to
exceptions the regulation lists. One of those exceptions, the one a school relies on daily, is
for school officials with a legitimate educational interest.

**The rights transfer to the student when they turn 18 or enrol in a postsecondary
institution.** Most of you are at or near that line, which makes this the framework on this
page that is about you personally.

**Why it is not on this module's competency list:** FERPA appears in this course under
competency 8.2.3, in Module 4. It is taught here because your privacy impact assessment is
about a school workflow, and pretending FERPA is not the governing framework would make the
assessment a fiction.

### COPPA, in one paragraph

Protects the personal information of children under 13 online, enforced by the FTC. It comes up
the moment a product is directed at children or you have actual knowledge you are collecting
from them. If your capstone touches an elementary school, this is your first question.
**[VERIFY]** the current rule, which has been amended.

---

## Worked example: routing to candidates, not to answers

```python
# framework_router.py: name the CANDIDATE frameworks for a situation, and the
# question that decides. It never says a framework applies. Nothing here is
# legal advice. Every situation below is invented.

SITUATIONS = [
    ("blood pressure readings", "a hospital", "United States"),
    ("blood pressure readings", "a fitness app the user downloaded", "United States"),
    ("card numbers", "the school store", "United States"),
    ("quarterly revenue figures", "a public company", "United States"),
    ("attendance records", "a public school", "United States"),
    ("names and emails", "a company website", "European Union"),
    ("names and emails", "an EU institution", "European Union"),
    ("a web page a screen reader cannot use", "a public school", "United States"),
]

RULES = [
    (lambda d, h, w: "blood" in d and "hospital" in h,
     "HIPAA", "Is this holder a covered entity or a business associate?"),
    (lambda d, h, w: "blood" in d and "app" in h,
     "probably NOT HIPAA",
     "Who holds it? HIPAA follows the holder and the relationship, not the topic."),
    (lambda d, h, w: "card" in d,
     "PCI DSS (a contract, not a statute)",
     "What do the card brand rules and the processor agreement require?"),
    (lambda d, h, w: "revenue" in d and "public company" in h,
     "SOX", "Does this feed financial reporting or its internal controls?"),
    (lambda d, h, w: "attendance" in d and "school" in h,
     "FERPA", "Is this an education record, and who is receiving it?"),
    (lambda d, h, w: w == "European Union" and "institution" in h,
     "EUDPR", "Is the holder an EU institution, body, office, or agency?"),
    (lambda d, h, w: w == "European Union" and "institution" not in h,
     "GDPR", "Are these people in the EU, and is the holder in scope?"),
    (lambda d, h, w: "screen reader" in d,
     "ADA", "Which title covers this entity, and what does current guidance require?"),
]

for data, holder, where in SITUATIONS:
    hits = [(name, question) for test, name, question in RULES
            if test(data, holder, where)]
    print(f"\n{data}  |  held by {holder}  |  {where}")
    for name, question in hits:
        print(f"   candidate: {name}")
        print(f"   decide by asking: {question}")
    if not hits:
        print("   candidate: none matched. That is a gap in this table, not in the law.")

print("\nThis program routes to candidates. It decides nothing, and it is not")
print("legal advice. Two of these rows also have state law that is not listed.")
```

Output:

```

blood pressure readings  |  held by a hospital  |  United States
   candidate: HIPAA
   decide by asking: Is this holder a covered entity or a business associate?

blood pressure readings  |  held by a fitness app the user downloaded  |  United States
   candidate: probably NOT HIPAA
   decide by asking: Who holds it? HIPAA follows the holder and the relationship, not the topic.

card numbers  |  held by the school store  |  United States
   candidate: PCI DSS (a contract, not a statute)
   decide by asking: What do the card brand rules and the processor agreement require?

quarterly revenue figures  |  held by a public company  |  United States
   candidate: SOX
   decide by asking: Does this feed financial reporting or its internal controls?

attendance records  |  held by a public school  |  United States
   candidate: FERPA
   decide by asking: Is this an education record, and who is receiving it?

names and emails  |  held by a company website  |  European Union
   candidate: GDPR
   decide by asking: Are these people in the EU, and is the holder in scope?

names and emails  |  held by an EU institution  |  European Union
   candidate: EUDPR
   decide by asking: Is the holder an EU institution, body, office, or agency?

a web page a screen reader cannot use  |  held by a public school  |  United States
   candidate: ADA
   decide by asking: Which title covers this entity, and what does current guidance require?

This program routes to candidates. It decides nothing, and it is not
legal advice. Two of these rows also have state law that is not listed.
```

**Rows one and two are the whole lesson.** Identical data, two holders, two different answers.
If you built a router that keyed on the data alone, both rows would say HIPAA and one of them
would be wrong.

**Read the last line of the output as carefully as the table.** The program says two rows also
have state law that is not listed. Card data and health data both attract state law in many
places, and this table has no column for it. **A routing table is a starting point that is
always incomplete**, and a tool that never says so trains you to believe it is complete.

---

## The wrong version, and what it does instead of an error

Here is a compliance table a model will produce for you on request. It is well formatted and
it will be believed.

```
| Framework | What it protects            | Type          |
|-----------|-----------------------------|---------------|
| HIPAA     | All medical information     | Federal law   |
| PCI DSS   | Credit card information     | Federal law   |
| SOX       | Customer privacy            | Federal law   |
| ADA       | Website accessibility       | Federal law   |
| GDPR      | All data of EU citizens     | EU law        |
| EUDPR     | EU citizens' data privacy   | EU law        |
```

**No error. Six rows, three columns, correct spelling throughout.** Five of the six rows
contain something false.

| Row | What is wrong |
|---|---|
| HIPAA, "all medical information" | It follows covered entities and business associates, not the topic. Health information in other hands is usually outside it. |
| PCI DSS, "Federal law" | **It is not a law.** It is an industry standard enforced through contracts. This is the single most checkable error in the table. |
| SOX, "customer privacy" | SOX is about financial reporting and internal controls at public companies. It is not a customer privacy law. |
| GDPR, "EU citizens" | The GDPR's protections turn on people **in** the EU and on where processing happens, not on citizenship. A US citizen living in Berlin is not outside it, and an EU citizen living in Ohio is not automatically inside it. |
| EUDPR, "EU citizens' data privacy" | Its distinguishing feature is **who holds the data**: the EU's own institutions. The row omits the only thing that separates it from the row above. |

The ADA row is the one that is fine, and it is fine in the shallowest possible way.

## Why the wrong version is tempting

**Every row is short and every row is parallel.** A table with a uniform shape reads as a
table of facts of a uniform kind. These six are not facts of a uniform kind: one of them is
not a law, one of them is not about privacy, and two of them differ from each other only in a
way this table has no column for.

**The word "citizens" sounds precise.** It is the wrong precision, and it is wrong in a way
that would change what a real product has to do. This is exactly how a plausible summary
produces a real engineering error: somebody writes a check for citizenship, and the check is
looking at the wrong property.

**It matches what you half-remembered.** Everything in that table is close to something true,
which is the hardest kind of wrong to catch. **You catch it by having one primary source open
next to the table.** Every framework on this page publishes its own material at an address in
the table at the top of this file.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Covered entity** | Under HIPAA, an organization the rules attach to: health plans, clearinghouses, and providers who transmit covered transactions electronically. |
| **Business associate** | An organization that handles protected health information on behalf of a covered entity. |
| **PHI** | Protected health information, the category HIPAA's rules govern. |
| **PCI DSS** | A payment card industry standard, enforced by contract rather than by statute. |
| **SOX** | Sarbanes-Oxley. Financial reporting accuracy and internal controls at public companies. |
| **Personal data** | Under the GDPR, information relating to an identified or identifiable person. |
| **Controller and processor** | Under the GDPR, who decides the purposes and means, and who processes on their behalf. |
| **Lawful basis** | The reason processing is permitted. Consent is one of several. |
| **Data minimisation** | Collecting only what is adequate, relevant, and limited to the purpose. |
| **Storage limitation** | Keeping data no longer than is necessary for the purpose. |
| **DPIA** | Data protection impact assessment. The GDPR instrument your assessment is modelled on. |
| **Education record** | The category FERPA governs, held by schools that receive applicable federal funds. |
| **Eligible student** | A student to whom FERPA rights have transferred, at 18 or on postsecondary enrolment. |

---

## Self-check

**Question 1.** For each, name the most likely framework and the one question you would ask to
confirm it:

a. A hospital gives a vendor access to patient records so the vendor can build a scheduling tool
b. Your club takes card payments for T-shirts at a fair
c. A school emails a list of students in a club to a parent volunteer
d. A US company's website signs up users in Paris

**Question 2.** Explain in two sentences why "HIPAA protects all medical information" is false,
and give an example where two identical pieces of health information are treated differently.

**Question 3.** A teammate says: "GDPR does not apply to us, our project is for our school and
we are in Ohio." Their conclusion is probably right and their reasoning is wrong. Explain the
difference, and say what fact would change the answer.

---

### Answers

**1.**

a. **HIPAA.** The vendor is handling protected health information on behalf of a covered
   entity, which is the business associate relationship. **The question to ask:** what does the
   agreement between them say about what the vendor may do with the data, including whether
   anything may be used to improve the vendor's product.

b. **PCI DSS**, through the payment processor's contract, and probably state law as well.
   **The question to ask:** what does the processor's agreement require, and is any card data
   being stored anywhere at all. The best answer to the second is no.

c. **FERPA.** A club roster from a school is an education record and the parent volunteer is
   the recipient. **The question to ask:** does an exception cover this disclosure, or is
   consent needed. Note that this is a real question and not a formality, which is why club
   rosters are handled more carefully than people expect.

d. **GDPR** is the candidate, and the company being in the United States does not settle it.
   **The question to ask:** is the company offering goods or services to people in the EU, or
   monitoring their behaviour, in the way the regulation describes.

**2.** HIPAA attaches to covered entities and their business associates rather than to the
subject matter, so health information held by somebody outside that set is usually outside
HIPAA. Two sentences is enough: the framework follows the holder and the relationship, not the
topic.

**Example:** your allergy, recorded in your doctor's chart, sits inside HIPAA. The identical
allergy, typed by you into a diet app you downloaded, generally does not, and is governed by
that app's own terms, by consumer protection law, and by whatever state law applies. Same
fact, different holder, different rules.

**3.** The conclusion is probably right. The reasoning is wrong because **"we are in Ohio" is
not the test.** The GDPR reaches organizations outside the EU under conditions the regulation
sets out, which is why a great many US organizations have had to deal with it.

The real reason the answer is probably no is a different one: the school is not offering
services to people in the EU or monitoring their behaviour, so nothing brings it into scope.

**What would change the answer:** the school enrolling students who are in the EU, or the
project being made available to and used by people in the EU. **Notice that both of those are
facts about users, not facts about where the team sits**, and that is the whole point. If your
capstone gets used by somebody's cousin in Dublin, the reasoning that ended at "we are in Ohio"
has nothing left to say.
