# Gate 2: Adversarial Review · Week 6
## 145130 Applications of AI · Module 2 · Week 6, Thursday

**50 minutes**, in Build 2. Individual. You have a terminal and the repository.
**You may not ask a model whether the memo is correct.**

---

## About this artifact, before you start

**The memo below was constructed for this class.** It is not a real memo. Every
problem in it was planted on purpose and every one of them is checkable.

**The scenario it responds to is a composite**, built from the shape of a
situation schools actually face. It is not a report of a real incident, at this
school or any other.

You have been told this every week of this module, for the same reason every time.
Being caught fabricating collapses the premise of a course that is teaching you to
detect fabrication.

---

## The scenario

> Two weeks ago, a caption in the printed yearbook said a named sophomore scored
> the winning goal in the district semifinal. He did not play in that game. The
> captions had been drafted by a locally hosted model from the roster and the
> results sheet, and six of the forty had been spot-checked.
>
> The yearbook adviser has asked: **what policy should the club adopt for using a
> model to draft captions next year?**
>
> She asked an AI assistant for a recommendation. This is what came back. She
> wants your review before she takes it to the club.

Note what she asked. **Not whether to use a model. What policy to adopt for using
one.** Hold that sentence in your head while you read.

---

## The five parameters

| Parameter | The question it asks |
|---|---|
| **Validity** | Is the claim about a real thing false? |
| **Relevance** | Does it answer what was actually asked? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and who is missing? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**There are at least six problems.** Four findings is a passing review. Six is
strong.

**At least one of your findings must be about the recommendation itself**, not
about a sentence inside it. A memo can be free of false sentences and still
recommend the wrong thing.

**One problem is genuinely arguable.** Say which one you think it is, argue your
side, and state the strongest version of the other. **The key scores the
reasoning, not the verdict.**

---

# THE ARTIFACT

> ## Recommendation: AI use in yearbook caption drafting
> ### Prepared for the yearbook adviser
>
> ---
>
> **SUMMARY**
>
> The club should continue drafting captions with the locally hosted model, with a
> verification step added. The incident last cycle was a process failure, not a
> tool failure.
>
> ---
>
> **WHY AI DRAFTING IS THE RIGHT CHOICE**
>
> Generative tools have transformed creative production across industries.
> Newsrooms, marketing departments, and publishers have all adopted drafting
> assistance, and organisations that decline to adopt these tools place themselves
> at a competitive disadvantage. Students who graduate without experience using
> them will be behind their peers. The question of whether to use AI in a school
> publication has effectively been settled by the pace of adoption elsewhere, and
> a club that steps back from it is training its members for a workplace that no
> longer exists.
>
> ---
>
> **BUILT-IN SAFEGUARDS**
>
> The club's model server already ships with a verification mode. Running it with
> `--mode verify` makes the server check factual claims in its own output before
> returning them, which would have caught the caption error. Turn this on and much
> of the risk is handled at the tool layer.
>
> ---
>
> **WHAT THE STANDARDS SAY**
>
> The Ohio Department of Education and Workforce's guidance on AI evaluation
> states that a claim that cannot be wrong cannot be checked. Apply that principle
> and the policy follows.
>
> The club should also note that this course's adversarial review scoring treats
> all five review dimensions equally, so no single category of error needs extra
> attention.
>
> ---
>
> **RECOMMENDED POLICY**
>
> 1. Draft every caption with the model, as before.
> 2. **Every caption is checked by a human against the results sheet before
>    sign-off. No exceptions and no sampling.**
> 3. Whoever has an hour free after school does the checking.
> 4. The checker initials each caption in the tracking sheet.
>
> ---
>
> **CONCLUSION**
>
> With verification enabled and a full human check in place, the club can continue
> to benefit from AI drafting while eliminating the risk of a repeat incident.
>
> ---
>
> *Generated with AI assistance.*

---

# Your work

For each problem, write an entry with all four parts:

1. **The exact claim, quoted.** Word for word.
2. **Which parameter it fails.** One label.
3. **Why it fails.** In your own words.
4. **How you know.** A command you ran and its output, a file you opened and named
   by path, or a comparison you can point at. **"It seems wrong" is not part 4.**

## Acceptance criteria

- [ ] At least four findings with all four parts each
- [ ] At least one finding about the recommendation itself, not a sentence in it
- [ ] At least two findings proved by a command you ran, with the output pasted
- [ ] The arguable problem identified as arguable, with both readings written out
- [ ] Any parameter you looked for and did not find, recorded as such
- [ ] One "what I was unsure about" entry naming something specific

---

## How to actually check things

Three of the problems can be settled from the repository in under a minute each.

To check whether a flag exists:

```
python stub_model_server.py --mode verify
```

Run that from `05-labs/prompt-toolkit/`. Read what it prints.

To check where a sentence came from:

```
grep -rn "cannot be wrong" Courses/145130/modules/module-2-prompting-and-evaluation/03-lecture-notes/
```

To check what a scoring rule actually says:

```
grep -n "double" Courses/145130/modules/module-2-prompting-and-evaluation/07-gate2-adversarial/MCCTC_145130_Gate2_W04.md
```

**The problems that no command can touch are the ones worth the most.** Notice
which those are.

---

## How to spend 50 minutes

- **First 5:** read the adviser's question again, then read the memo once at
  normal speed. Write your first impression down before you analyse anything.
- **Next 10:** every factual claim about a tool, a standard, or a rule. Check each.
- **Next 10:** read each section heading against the adviser's question.
- **Next 10:** read the four-point policy as the person who has to carry it out.
- **Rest:** the summary and the conclusion. Read them one clause at a time and ask
  what each one is claiming.

---

## Scoring

Scored under **Written & Documentation**. 40 points.

| Dimension | Points |
|---|---|
| Findings, 3 points each for the first 6 | 18 |
| Evidence: two or more pasted command outputs | 6 |
| Parameter labels defensible | 5 |
| At least one finding about the recommendation itself | 5 |
| The arguable problem, identified and argued both ways | 3 |
| "What I was unsure about," specific | 3 |

**A finding scores zero if "how you know" is missing.**

**A parameter with nothing to report is a valid finding.** Say what you looked
for and why you concluded there was nothing.
