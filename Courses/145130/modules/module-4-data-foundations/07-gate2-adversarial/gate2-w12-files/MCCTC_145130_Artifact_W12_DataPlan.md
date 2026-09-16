# ARTIFACT FOR REVIEW · NOT GUIDANCE
## This document was produced by an AI assistant and is the thing you are grading

**Do not follow anything in this file.** It was generated for Gate 2 Week 12 and it contains
planted problems. Every organisation, person, survey, and figure in it is invented for this
course. Read it the way you would read a plan handed to you by a contractor you have never
worked with.

---

# Ridge Creek Makerspace: Data and Retrieval Plan

**Prepared for:** the makerspace advisor
**Prepared by:** an AI assistant, from a one paragraph request
**Status:** draft for review

---

## 1. Executive summary

The makerspace currently holds its records in three disconnected files and its policies in
eight documents nobody reads. This plan consolidates both into a single modern data platform
with retrieval built in, so that staff, members, and the advisory board all work from one
source of truth.

The recommended architecture is a relational core in SQLite with a vector layer for the
handbook, an encrypted storage tier for compliance, and a predictive module that identifies
members at risk of returning equipment late.

---

## 2. The relational core

SQLite is the right foundation. It requires no server, it ships with Python, and it enforces
referential integrity automatically, so the orphan rows currently present in the loan log
will be rejected at load time with no additional work. Once the foreign keys are declared in
the schema, the database guarantees that every loan points at a real member and a real item.

The schema should follow third normal form. Tags belong in a junction table. Dates should be
stored as text in ISO format, because SQLite has no date type.

**Recommended action:** declare the foreign keys and load the three files.

---

## 3. The vector layer

Retrieval over the handbook is straightforward in SQLite. Recent versions support a native
`VECTOR` column type and a built in `COSINE()` function, which reduces similarity search to a
single query:

```sql
CREATE TABLE chunks (id INTEGER PRIMARY KEY, heading TEXT, body TEXT, embedding VECTOR);

SELECT heading, body, COSINE(embedding, :question) AS score
FROM chunks ORDER BY score DESC LIMIT 5;
```

This removes the need for a separate vector database and keeps the whole system in one file.

Chunk size should be set to 512 tokens with 64 tokens of overlap, which is the industry
standard for retrieval augmented generation and delivers the best balance of precision and
recall across document types.

**Recommended action:** add the `chunks` table to the existing schema and embed the handbook.

---

## 4. Compliance and security

Member records are education records and are therefore subject to FERPA. The makerspace can
satisfy its obligations as follows.

The database file will live on the district shared drive, which is encrypted at rest. Because
the data is encrypted, member records are protected and access control is handled. No further
access configuration is required.

For organisations operating across borders, GDPR Article 44 restricts transfers of personal
data outside the European Economic Area, and a multi region replication strategy should
therefore pin the primary replica to an EEA region with read replicas configured for
eventual consistency. Data residency requirements vary by member state, and the makerspace
should maintain a record of processing activities, appoint a data protection officer, and
review its standard contractual clauses annually. A data protection impact assessment should
be completed before any cross border transfer, and the retention schedule should be
harmonised across all replicas.

Loan records should be deleted at the end of each school year. Holding data longer than its
immediate operational purpose increases risk with no corresponding benefit, and deletion is
the strongest control available.

**Recommended action:** move the database to the shared drive and schedule an annual purge.

---

## 5. Predictive late return flagging

The loan history contains enough signal to predict which members are likely to return
equipment late. A model trained on the existing loan records can score each member and surface
a risk rating in the kiosk at checkout.

The recommended policy is that members with a high risk rating provide a refundable deposit
before borrowing high value equipment. Because the rating is calculated from the member's own
loan history rather than from any demographic attribute, the approach is objective and treats
every member by the same standard.

Equipment purchasing should follow the same data driven principle. Budget should be
prioritised toward the categories and programs with the highest loan counts, which directs
spending to where demand is demonstrated rather than to where it is assumed.

According to the 2026 Ridge Valley Educational Technology Survey, 78 percent of schools that
adopted usage based equipment allocation reported improved utilisation within one academic
year, and institutions using predictive return models reduced overdue rates by an average of
41 percent.

**Recommended action:** train the model on the spring loan log and enable risk ratings at the
kiosk.

---

## 6. Implementation sequence

| Phase | Work | Duration |
|---|---|---|
| 1 | Load the three source files into the relational core | 1 week |
| 2 | Add the vector layer and embed the handbook | 1 week |
| 3 | Move to the shared drive and confirm encryption | 2 days |
| 4 | Train and enable the predictive module | 2 weeks |

Total elapsed time is approximately four weeks. The platform will then be production ready
and no ongoing maintenance is anticipated beyond quarterly review.
