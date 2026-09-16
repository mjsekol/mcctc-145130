# Module 4 Exit Criteria
## Data Foundations for AI · Check yourself against this

The syllabus lists three exit criteria for this module. They are below, in the syllabus wording,
with what each one actually looks like when you can do it and what it looks like when you
cannot.

**Use this before the exit assessment.** Every line is something you can check on your own
work, today, without asking anybody.

---

## 1. "Choose a database structure for a stated workload and defend the choice"

- [ ] I can name the shape of a question: counting over groups, fetching one whole thing by
      its id, traversing relationships, or finding text that means something similar
- [ ] For each of those four shapes, I can name a structure that fits and say why
- [ ] **Every recommendation I make names one thing it makes harder**
- [ ] I can say which of the exam's words describe the shape of the data, which describe what
      the system is for, which describe deployment, and which describe a licence
- [ ] I can state a **size** at which my recommendation would change
- [ ] I can make the strongest argument against my own recommendation without weakening it

**You can do this when:** somebody describes a workload you have never heard of and you ask
what shape the question is before you answer.

**You cannot do this yet if:** your answer to any workload is a structure with no cost under
it, or if you would recommend the same structure for all four.

---

## 2. "Move data between three formats without losing fidelity"

- [ ] I can read a CSV with the `csv` module, a JSON file with `json`, and a delimited text
      file with my own reader
- [ ] I can load all three into one schema with `executemany`, in an order the foreign keys
      allow
- [ ] I can export to at least two formats and **load both back into a fresh empty database**
- [ ] **I compare table by table, not by row count**, and I can say why a row count is not a
      fidelity check
- [ ] I can name one thing CSV cannot represent, and the convention that works around it
- [ ] I can say what my own lossy export lost, exactly, and prove it with a command
- [ ] Nothing in my pipeline is dropped without being counted, and my program prints the
      arithmetic

**You can do this when:** somebody hands you an export and you ask to see the reload before you
believe it.

**You cannot do this yet if:** your fidelity check is `before == after` on a row count, or if
you cannot name a single thing your own export lost.

---

## 3. "Explain why retrieval beats fine tuning for most practical problems"

- [ ] I can say which of the two changes the model, and which does not
- [ ] **Cost:** I can say how the costs are shaped differently, not only that one is expensive,
      and name when the trade could go the other way
- [ ] **Freshness:** I can describe, step by step, what happens under each approach on the day
      the source documents change
- [ ] **Traceability:** I can show a retrieval result carrying its file, heading, and offsets,
      and say what somebody can do with that in ten seconds
- [ ] **What retrieval still gets wrong:** I can name at least three things, and **one of them
      names a real problem in the Ridge Creek handbook**
- [ ] I can name one thing fine tuning does better, and it is a way of behaving rather than a
      fact
- [ ] I can say one security problem that retrieval does not solve

**You can do this when:** you can give the argument in ninety seconds and the last thing you
say is the thing your own answer gets wrong.

**You cannot do this yet if:** your fourth point is "retrieval can return the wrong chunk" with
nothing behind it, or if you cannot name anything fine tuning is better at.

---

## The three things this module will not let you claim

These are not exit criteria. They are the three sentences that cost marks in every artifact in
this module, and if any of them is in your work, take it out.

1. **"The schema has foreign keys, so the data has integrity."** Run `PRAGMA foreign_keys` and
   report the number.
2. **"The row counts match, so the migration worked."** Compare content per table.
3. **"The retrieval works."** On the stub it proves the plumbing and nothing else, and saying
   so is worth more marks than the search function.

---

## Where each criterion is assessed

| Exit criterion | Where you are graded on it |
|---|---|
| 1. Choose and defend a structure | The comparison memo, 50 points, Written & Documentation. Exit assessment items 4, 20, 21 |
| 2. Move between formats without losing fidelity | The performance task, Functionality and Documentation. Exit assessment items 14, 15, 16, 25 |
| 3. Retrieval versus fine tuning | The memo's dedicated section, worth 10 of its 50. Exit assessment item 21. Your project README's honest paragraph |

**And one that is not on the list and is graded everywhere:** can you explain a number in your
own report by tracing it to the rows it came from. That is the first ninety seconds of your
demonstration and it is the thing the advisor said mattered most.
