# Additional Resources · Week 9
## 145130 Applications of AI · Module 3
### Topics: CIA, privacy frameworks, data minimization, and vendor questions

**Every URL on this page is marked [VERIFY].** Click every one before class.

**Nothing on this page is legal advice.** Each source is named because it is the body that
publishes the material.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The Student Privacy Policy Office, on FERPA | Tue, all week | On-level | 40 min |
| 2 | HHS Office for Civil Rights, on HIPAA | Tue | On-level | 20 min |
| 3 | The PCI Security Standards Council | Tue | On-level | 15 min |
| 4 | The GDPR's own text, Articles 5, 6, 22, and 35 | Tue, Wed | Extension | 45 min |
| 5 | The European Data Protection Supervisor, on the EUDPR | Tue | Remediation | 10 min |
| 6 | The SEC, on Sarbanes-Oxley | Tue | Remediation | 10 min |
| 7 | The FTC, on COPPA | Tue | Extension | 15 min |
| 8 | NIST Privacy Framework and the AI Risk Management Framework | Wed, Thu | Extension | 45 min |
| 9 | Python `hashlib` and `secrets` documentation | Mon, Wed | On-level | 15 min |
| 10 | A free video on data minimization or re-identification | Any | Remediation | under 20 min |
| 11 | SQ-19 The Bias Audit | Fri | Extension | two blocks |
| 12 | Every self-check in this module, before Thursday | Thu | Review | 40 min |

---

## 1. The Student Privacy Policy Office

`https://studentprivacy.ed.gov` **[VERIFY]**

**Why this one.** FERPA is the framework that actually governs the workflows in your privacy impact
assessment, and it is the one on Tuesday's list that is about you personally: **the rights transfer
to the student at 18 or on postsecondary enrolment**, which is most of this room.

It is also not on this module's competency list. It appears in this course under 8.2.3, in Module
4. It is taught here because pretending FERPA is not the governing framework would make the whole
assessment a fiction.

**Assign a question:** *what is an education record, in the Office's own words? Then say whether
the free-text submission in the Gate 2 Compass memo would be one, and say what your answer depends
on.*

**Time.** 40 minutes. **Level.** On-level. **This is the most useful 40 minutes on the page.**

---

## 2. HHS Office for Civil Rights, on HIPAA

`https://www.hhs.gov/hipaa` **[VERIFY]**

**Why this one.** It settles the most common privacy error in public life in about ten minutes:
**HIPAA follows covered entities and business associates, not the topic.**

**Assign a question:** *find who the rules apply to. Then explain why your own doctor's chart and
your own fitness app are treated differently even when they hold the same fact.*

**Time.** 20 minutes. **Level.** On-level.

---

## 3. The PCI Security Standards Council

`https://www.pcisecuritystandards.org` **[VERIFY]**

**Why this one.** It is the fastest way to show that PCI DSS is not a law. **Look at who publishes
it.** A council of payment brands is not a legislature, and that single observation is worth a
point on the exit assessment and every compliance table a student will ever read.

**Assign a question:** *who publishes this standard, and how does it reach an organization that has
to follow it?*

**Time.** 15 minutes. **Level.** On-level.

---

## 4. The GDPR's own text

The European Commission publishes the regulation. `https://commission.europa.eu` **[VERIFY]**

**Why this one.** The GDPR does not govern your school, and its Article 5 principles are the
clearest published statement of the design checklist this module uses. **Read the regulation, not a
summary of it**, because Wednesday's whole lesson is built on four of its words: purpose
limitation, data minimisation, storage limitation.

**Assign a question:** *find Article 5 and write out the principles. Then find Article 6 and say how
many lawful bases there are. **Anybody who tells you the GDPR requires consent for everything has
not read Article 6.***

**Also worth finding:** Article 22 on decisions based solely on automated processing, and Article
35 on data protection impact assessments, **which is the ancestor of the document you are writing
this week.**

**Time.** 45 minutes. **Level.** Extension.

---

## 5. The European Data Protection Supervisor

`https://www.edps.europa.eu` **[VERIFY]**

**Why this one.** The EUDPR is the row on the competency list students find most confusing, and it
takes one sentence: **GDPR-shaped rules for the EU's own institutions, supervised by this office.**
Seeing the supervisor's own site makes it concrete.

**Time.** 10 minutes. **Level.** Remediation.

---

## 6. The SEC, on Sarbanes-Oxley

`https://www.sec.gov` **[VERIFY]**

**Why this one.** SOX is on the competency's privacy list and **it is not a privacy law.** It
concerns financial reporting accuracy and internal controls at public companies, and it is the
reason a lot of technology controls exist in corporate environments: change management, access
control, audit logs, records retention.

**Assign a question:** *what is this act actually about? Then say why a student might meet its
effects at a summer job without ever hearing its name.*

**Time.** 10 minutes. **Level.** Remediation.

---

## 7. The FTC, on COPPA

`https://www.ftc.gov` **[VERIFY]**

**Why this one.** Children under 13, and it becomes the first question the moment a capstone
touches an elementary school. **[VERIFY] the current rule**, which has been amended.

**Time.** 15 minutes. **Level.** Extension, and required reading for any student whose capstone has
a younger audience.

---

## 8. NIST frameworks

`https://www.nist.gov/privacy-framework` **[VERIFY]** and the AI Risk Management Framework,
`https://www.nist.gov/itl/ai-risk-management-framework` **[VERIFY]**

**Why these.** They are the published, non-legal structures that professionals use to organize
exactly the work your assessment does. **They are voluntary frameworks, not requirements**, and
saying that out loud is part of the value: not everything that structures this work is law.

**Assign a question:** *pick one function or category from either framework and say which section of
your own assessment it corresponds to.*

**Time.** 45 minutes. **Level.** Extension.

---

## 9. Python `hashlib` and `secrets`

`https://docs.python.org/3/library/hashlib.html` **[VERIFY]**
`https://docs.python.org/3/library/secrets.html` **[VERIFY]**

**Why these.** Lab M03-03 needs both, and the `secrets` page says in its own words what it is for,
which is the distinction between a value that has to be unpredictable and one that only has to be
unique.

**Assign a question:** *what does the `secrets` documentation say it is for, as against `random`?
Then say why the salt in `minimize.py` uses `secrets` and the shuffle in Study Buddy does not.*

**Time.** 15 minutes. **Level.** On-level.

---

## 10. A free video

**[VERIFY]. No specific video is linked.**

**What to look for:** something under 20 minutes on re-identification or on data minimization.
**Watch it yourself first**, and be careful of anything that presents anonymization as a solved
problem with a checklist, because Wednesday's lesson is that it is a measurement rather than a
procedure.

**Level.** Remediation.

---

## 11. Side quest

**SQ-19 The Bias Audit.** Bundle: `Courses/Misc/side-quests/SQ-19-The-Bias-Audit/`. ★★★, two
blocks, no account and no key. It carries into Module 4 for anybody who starts it this week.

---

## 12. Every self-check in this module, before Thursday

Twelve lecture notes, three self-check questions each, worked answers on every one. **Thirty-six
questions, and the exit assessment is Thursday.**

**A student who can answer all 36 without reading the answers first will not be surprised by
anything on the assessment.** The ten most worth the time, in this order:

1. Privacy Framework Map, question 1, all four situations
2. Data Minimization, question 2, the 800-student generalization
3. CIA, question 1, all three trades
4. Reading a License, question 2, the conveying question
5. Who Owns AI Output, question 1
6. Vendor Questions, question 1
7. What IP Protects, question 3, all four items
8. Consumer Protection, question 3
9. Conflicts of Interest, question 1
10. Creative Commons, question 3

**Level.** Review.

---

## For the student who is behind

1. The three properties table from the CIA notes, copied out by hand
2. `framework_router.py` run, with rows one and two read out loud
3. Gate 1 Reps 14 and 16
4. Before Thursday: self-checks 1, 2, and 3 from the list above and nothing else new

## For the student who is ahead

- Lab M03-03 EXTENDED, the retention script
- Resource 4, the GDPR text, Articles 5 and 35
- Resource 8, and map one NIST category onto their own assessment
- SQ-19
