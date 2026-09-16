# Performance Task: The Database Comparison Memo
## 145130 Applications of Artificial Intelligence · Module 4 · Weeks 10-11

**Mode:** solo. **Gate:** 3, full tooling, AI usage log required.
**Due:** Week 11, Friday, end of Build 2.
**Length:** 900 to 1,400 words. A memo, not an essay. Headings, a table, and short
paragraphs.
**Grade category:** Written & Documentation.

**Competencies:** 2.8.1 (types of databases) · 2.8.2 (use and purpose of a database and a
DBMS) · 2.8.3 (compare database structures) · 2.8.9 (front end versus back end) ·
1.2.5 (communicate for an intended audience and purpose) · 1.2.12 (technical writing).

**Written & Documentation is 20 percent of this course, and this memo is the largest single
piece of it in Module 4.** It is graded as writing. A memo that is technically right and
unreadable by its stated audience does not score well, and neither does a readable memo that
recommends something it cannot defend.

---

## The situation

The makerspace advisor from the pipeline project reads your memo. That person runs a
makerspace, teaches a class, and has never written a query. They can follow an argument and
they can tell when they are being sold something.

They have asked for four things in one system:

1. **The equipment report.** Which equipment is being used, by which programs, and what has
   not come back.
2. **Handbook answering.** An assistant that can point at the paragraph that answers a
   question, over the eight handbook documents.
3. **A maintenance record.** Every repair, filament change, firmware update, and cleaning,
   per item, so the budget request has something behind it.
4. **Who works with whom.** Which members use the same equipment, so the advisor can pair a
   new member with somebody who already knows the machine.

**They are asking for one system. Part of your job is to tell them how many they actually
need, and why.**

---

## What the memo must do

### 1. A recommendation for every workload

For each of the four, name a database **type** and a database **structure**, and defend it.
The vocabulary you must be able to use correctly:

- **Types:** relational, object-oriented, NoSQL (document, key-value, column, graph),
  graph, data warehouse, distributed, open source, cloud, artificial intelligence.
- **Structures:** flat file, hierarchical, relational, data lake, object-oriented, cloud,
  multi-modal.
- **A vector index** is how retrieval is stored. Say plainly where it sits: whether you are
  calling it a database type of its own, a feature bolted onto a relational database, or a
  separate store beside one. Different vendors answer that differently and you are allowed
  to pick a side as long as you say which.

### 2. A cost for every recommendation

**Every recommendation names at least one thing it makes harder.** A recommendation with no
cost is a sales pitch. If relational is right for workload 1, say what a schema change costs
you six months from now. If a vector index is right for workload 2, say what it costs to
keep in step with the documents.

### 3. One comparison table

Rows are the structures. Columns are what they are good at, what they are bad at, and the
workload on this list they fit. It has to be readable by somebody who skips your prose.

### 4. The retrieval versus fine tuning paragraph

For workload 2, answer the question directly: **why does retrieval beat fine tuning for most
practical problems?** Cover all four of these and be specific:

- **cost**
- **freshness**
- **traceability to a source**
- **what retrieval still gets wrong**

The fourth one is where memos separate. "Retrieval can return the wrong chunk" is worth
little. **Name a failure you can point at in the Ridge Creek handbook**, and say what it
does to an answer that comes with a citation attached.

### 5. Front end and back end

One short section. Which part of your recommendation is the back end, which parts are front
ends, and one rule from the makerspace that must live in the back end rather than in a
front end, with the reason.

### 6. One honestly contested call

Pick the recommendation you are least sure about. State the strongest case against your own
answer, in its own words, not a weakened version of it. Then say what would have to change
for you to switch.

**This section is scored on whether the counterargument is real.** A counterargument you
have weakened on purpose scores zero for the section.

---

## What the memo may not do

| Not allowed | Why |
|---|---|
| A performance claim with no source | "Graph databases are 100 times faster for this" is a number you cannot support. Say "faster at multi-step relationship queries" and explain the mechanism instead. |
| An invented product benchmark, case study, or company | You are being trained to catch fabrication. Producing it costs the assignment. |
| A recommendation copied from a model with no evaluation | Allowed as a starting point, logged, and then checked. See the AI usage requirement. |
| A URL you have not opened | Mark anything you are unsure of `[VERIFY]` and say so. |
| Legal claims about student records | The privacy framework is a Module 3 and Module 4 topic at the purpose level. Describe what a framework protects and why. Do not state a threshold, a penalty, or advice. |

---

## AI usage requirement

You may use a local model. **You must log it**, in `ai-usage-log.md` beside the memo, with:

- what you asked
- what it said, in one line
- **what you kept and what you rejected**
- **how you checked the part you kept**

**At least one entry must be something you rejected, with the reason.** A local model asked
to compare database types produces confident, generic, mostly-true prose, and the parts that
are wrong are wrong in ways that read exactly like the parts that are right. If you used a
model and rejected nothing, one of two things is true and neither is good.

---

## Rubric, 50 points

Scored as Written & Documentation. This rubric is specific to this memo and does not replace
the 100-point project rubric, which grades the pipeline.

| Dimension | Points | 5 of 5 looks like | 3 of 5 looks like | 1 of 5 looks like |
|---|---|---|---|---|
| **Fit of recommendation to workload** | 15 | All four recommendations follow from the shape of the question being asked, and the memo says what shape that is. | Recommendations are reasonable. Two of them are justified by what the database is rather than by what the workload needs. | The memo recommends one structure for everything, or matches types to workloads with no stated reason. |
| **Costs named** | 10 | Every recommendation names a real cost, and at least one cost is specific enough to be checked. | Most recommendations name a cost. At least one cost is generic ("it is more complex"). | Costs are missing or are restated advantages. |
| **Retrieval versus fine tuning** | 10 | All four points covered. The "what it still gets wrong" point names a failure in the actual handbook. | All four covered, but the failure mode is generic. | One or two points covered, or the answer confuses fine tuning with prompting. |
| **Accuracy of vocabulary** | 5 | Types, structures, keys, normalization, front end, and back end all used correctly. | One term used loosely. | A term is used to mean something it does not, such as calling a document store a data lake. |
| **The contested call** | 5 | The counterargument is genuinely strong and the switching condition is concrete. | A counterargument is stated but softened. | The section is missing, or the counterargument is a straw man. |
| **Written for its audience** | 5 | The advisor could act on it. Headings, a readable table, no unexplained jargon, under the word limit. | Readable, with two or three terms an advisor would have to look up. | Written for the instructor, not the advisor, or over the word limit. |

**Automatic deductions.** An unsourced performance statistic, an invented case, or a legal
claim costs 10 points and a rewrite. A missing AI usage log costs 5.

---

## Three worked scope examples

### Too small

> "Use SQLite for the report and a vector database for the handbook. SQLite is a relational
> database and relational databases are good for structured data. Vector databases are good
> for semantic search."

Both sentences are true and neither is an argument. No workload was analyzed, nothing was
compared, no cost was named, and workloads 3 and 4 are missing.

### About right

See the model memo your instructor holds. It recommends relational for three of the four
workloads, argues the fourth is close, names a cost for every recommendation, points at the
contradiction between `02-loan-policy.md` and `07-electronics-bench.md` as the retrieval
failure mode, and says what would make it switch to a graph database.

### Too big

> A fifteen page survey of every database type with a history section, vendor comparisons,
> pricing, and a benchmark table.

The advisor stops reading on page two. Pricing and benchmarks are numbers you would have to
invent or could not verify, and inventing them costs 10 points. **The memo is a
recommendation, not a textbook chapter.**

---

## Submission checklist

- [ ] 900 to 1,400 words, word count stated at the top
- [ ] A recommendation and a cost for all four workloads
- [ ] One comparison table
- [ ] The retrieval versus fine tuning section, all four points, with a real handbook failure
- [ ] The front end and back end section, with one rule that must live in the back end
- [ ] The contested call, with a counterargument you would not be embarrassed to defend
- [ ] `ai-usage-log.md`, with at least one rejection
- [ ] No unsourced statistic, no invented case, no legal advice
- [ ] Committed and pushed
