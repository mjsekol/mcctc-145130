# Gate 2: Adversarial Review · Week 12
## 145130 Applications of AI · Module 4 · Week 12, Thursday

**40 minutes**, in Build 1 after the Gate 1 rep. Individual. You have a computer and you
should use it. **You may not ask a model whether this document is correct**, because a model
wrote it and you are grading the model.

The artifact is `gate2-w12-files/MCCTC_145130_Artifact_W12_DataPlan.md`.

---

## What you are looking at

This week is not code. Somebody gave an AI assistant one paragraph about the makerspace and
got back a four week implementation plan with a schema, a security section, a compliance
section, and a predictive module.

**It reads like a consultant wrote it.** It is organised, it is confident, it uses the right
vocabulary, and it ends with a table of phases and durations. Those are the properties of a
document that gets approved.

**You are scoring it on the five AI Output Evaluation parameters**, the same five you have
used since Module 2:

| Parameter | The question it asks |
|---|---|
| **Validity** | Is the claim true? |
| **Relevance** | Does it answer the question that was asked, for this organisation? |
| **Authenticity** | Can the sources and figures be traced to something real? |
| **Potential bias** | Who does this advantage, and who does it disadvantage, and does the document notice? |
| **Hallucinations** | Is anything here invented and presented as real? |

**Every parameter has at least one real problem in this document.** At least one of them is
genuinely arguable, and on that one you are scored on your reasoning rather than on your
verdict.

---

## What to submit

A scoring sheet with one section per parameter. For each parameter:

1. **A score out of 5.** 5 means no problem found. 1 means a problem serious enough to stop
   the plan.
2. **The evidence.** Quote the sentence and give the section number.
3. **How you settled it.** A command you ran and what it printed, a document you opened and
   what it said, or a piece of arithmetic. **A claim you settled by feel is not settled.**
4. **What it would cost** if the advisor acted on it.

Then two more entries:

- **The one you are least sure about**, naming it specifically and saying what evidence would
  settle it.
- **One sentence to the advisor**, telling them whether to approve this plan, in language a
  person who does not write code would act on.

### How to spend 40 minutes

- **First 5:** read the whole thing once without stopping. Write down your first impression
  in one sentence, before you start checking. You will compare it with your last impression.
- **Next 12:** take every technical claim about SQLite and test it. You have Python. Section
  2 and section 3 both make claims that take under a minute to settle each.
- **Next 8:** every number and every source. For each one, decide whether you could find it
  if you were asked to, and mark the ones you could not.
- **Next 8:** section 4 and section 5. Ask who each recommendation helps and who it does not,
  and whether the document mentions that anybody is affected differently.
- **Next 5:** read section 4 against the makerspace you actually have: one room, fourteen
  members, fourteen items, and one advisor.
- **Last 2:** write the sentence to the advisor.

---

## Two rules for this one

**Verify, do not recognise.** Several claims in this document are the kind of thing you have
heard before and half believe. That is what makes them work. A claim you have heard before is
not a claim you have checked.

**One of the problems is arguable and you are allowed to disagree with the key.** Say which
one you think it is, take a side, and say what would change your mind. That entry is scored
on the reasoning.

---

## Scoring

Five parameters, five points each, twenty five total. Plus one point for the least-sure entry
and one for the sentence to the advisor.

**A parameter scores full marks only when the evidence is reproducible**: a command anybody
can run, or a document anybody can open.

**Fifteen out of twenty five is a normal score on this one.** The document is better written
than most of the things it is wrong about.
