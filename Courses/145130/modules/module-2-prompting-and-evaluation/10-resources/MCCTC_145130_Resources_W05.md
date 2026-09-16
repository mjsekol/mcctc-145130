# Additional Resources · Week 5
## 145130 Applications of AI · Module 2 · Week 5
### Topics: the five evaluation parameters, authenticity and citation checking, why models fabricate, and potential bias

Links marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed live and must
be clicked before it is assigned. Several resources below are named with no link at all. That is
deliberate. A title you can search for is worth more than a URL that turns out to be dead in front of
a class, and this is the week the course teaches you to prefer a checkable name over a confident
link.

**Read this before you use anything here.** Week 5 is about checking claims. A resource list that
asked you to trust its own links without checking them would be teaching the opposite of the week.
Every external link on this page is a claim. Check it.

**The containment rule for Wednesday and Thursday.** Everything you fabricate in the Hallucination
Hunt stays in the Hallucination Hunt. It does not go in another assignment, it does not leave the
classroom, and every fabricated citation is labelled as fabricated in your own file. Friday opens with
the reveal, where every fabrication the class produced is named out loud as fabricated.

**No personal data in any prompt.** Not on the bias work, not anywhere. SQ-19 states the same rule: no
real people, no student data, no classmates as subjects.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Lecture notes: The Five Evaluation Parameters | Mon | On-level | 25 min |
| 2 | Lecture notes: Authenticity and Citation | Tue | On-level | 25 min |
| 3 | Lecture notes: Why Models Fabricate | Wed | On-level | 25 min |
| 4 | Lecture notes: Potential Bias | Thu | On-level | 25 min |
| 5 | The five reference runs, as a scoring set | Mon, Thu | On-level | 30 min |
| 6 | 145060 Lab U0-02 Infographic Autopsy | Mon | Review | 25 min |
| 7 | Competency reference, 2.14.4 verbatim | Any | On-level | 10 min |
| 8 | Official docs: `urllib.request` | Wed | Extension | 15 min |
| 9 | Crossref and the DOI resolver | Tue-Thu | On-level | 20 min |
| 10 | A library catalog and a scholarly search | Tue-Thu | On-level | 20 min |
| 11 | Retraction Watch | Tue | Extension | 15 min |
| 12 | Three real papers on bias and model documentation | Thu | Extension | 45 min |
| 13 | SQ-19 The Bias Audit | Thu onward | Extension | 2 blocks |
| 14 | A free video on fabricated citations | Any | Remediation | under 20 min |
| 15 | Gate 1 Reps 16-20 and the twelve self-checks | Before Fri | Review | 25 min |

---

## 1. Primary reading

**`../03-lecture-notes/MCCTC_145130_Notes_FiveEvaluationParameters.md`**

**Why this one.** It carries the five parameters verbatim from Ohio competency 2.14.4, which is the
wording on the exam, and then works one full example per parameter. Five worked examples in one
document is the whole of Monday.

Pay attention to the section titled "The line you will keep getting wrong." Validity is a wrong claim
about a real thing. A Hallucination invents the thing. Every year a class can recite that sentence and
still label eight findings out of eight as Validity.

**Assign a question, not the page:** *Read worked example 2, Relevance. The output is true in every
sentence. Say in one sentence why Relevance is the only one of the five parameters that is about the
relationship between the output and the request, and why that is why it gets skipped.*

**Time.** 25 minutes. **Level.** On-level.

---

## 2. Authenticity and what a citation is for

`../03-lecture-notes/MCCTC_145130_Notes_AuthenticityAndCitation.md`

**Why this one.** It gives you the four-step check in the order that works, and worked example 3 is
the case Tuesday actually turns on: a check that comes back complicated rather than clean.

A citation is a set of instructions for checking a claim without trusting the person who made it. It
has four parts: who, what, where, when. Authenticity fails in two shapes, uncredited reuse and
misattribution, and **misattribution is the worse one because it survives a careless check.**

**Assign a question:** *Self-check question 2. A quote in an output is real, word for word, and is
attributed to the wrong person. Which parameter is that, and why is it not Validity?*

**Time.** 25 minutes. **Level.** On-level.

---

## 3. Why models fabricate

`../03-lecture-notes/MCCTC_145130_Notes_WhyModelsFabricate.md`

**Why this one.** Worked examples 1 and 2 are the ungrounded and grounded runs you will see on the
projector Wednesday. Worked example 3 is the one that matters most: the grounded run, with zero
fabricated sources, that answers a different question than the one asked. **Every citation real,
answer wrong.** Fixing one parameter broke another.

The section called "What reduces it, honestly" is the part to read twice. Three things reduce
fabrication: putting the relevant source text in the prompt, restricting the answer to that text with
a refusal route, and asking for a quote plus a section number rather than a summary. **None of the
three makes the model honest.** They change what is nearby, which changes what is likely.

**Assign a question:** *Self-check question 1. Why is a fabricated citation more likely when you ask
about your own school than when you ask about a famous topic?*

**Time.** 25 minutes. **Level.** On-level.

---

## 4. Potential bias

`../03-lecture-notes/MCCTC_145130_Notes_PotentialBias.md`

**Why this one.** Three questions produce a bias finding: who is the default person, which group is
absent, and what goes wrong for them. Without all three you have an observation, not a finding.

Worked example 2 is the one students skip and should not: an output with no bias finding in it. A pass
that always finds bias is not a pass, it is a habit.

**The line to hold.** Overstating a true claim is Validity. Bias is about absence.

**Assign a question:** *Self-check question 1. "This advice assumes you have a quiet place to study."
Is that a Potential Bias finding as written? What is missing from it?*

**Time.** 25 minutes. **Level.** On-level.

---

## 5. The five reference runs, as a scoring set

`../09-project/reference-implementation/prompt-autopsy/runs/`

**Why this one.** Monday Build 2 and Thursday Build 2 both score these. They are real recorded output
from the stub, they are already in your repository, and everybody in the room is scoring the same
text, which is what makes an argument about a label productive instead of a difference of memory.

**Use them like this.** Score all five on all five parameters using the four-part finding format:
quote the claim, name one parameter, say why, say how you know. Aim for at least one Hallucination and
one Validity, with a sentence on why each is not the other.

**Record at least one parameter as having nothing to report.** A student who finds all five parameters
in every artifact is pattern-matching to the rubric rather than reading.

**Time.** 30 minutes. **Level.** On-level.

---

## 6. The lab you did as a junior

`../../../../145060/units/unit-00-onboarding/05-labs/MCCTC_145060_Lab_U00-02_InfographicAutopsy.md`

**Why this one.** Monday of Week 5 opens with `.titlecase()` from that lab as the anchor for the
Validity against Hallucination line. A claim that `print` separates with commas is Validity, because
`print` exists and the sentence about it is false. A claim that `.titlecase()` is a string method is a
Hallucination, because there is nothing there to be wrong about.

Rereading the criteria table takes five minutes. Rereading your own old findings takes twenty and is
worth more, because you will find at least one you would now label differently.

**Time.** 25 minutes. **Level.** Review.

---

## 7. The official wording of 2.14.4

`../../../_source/COMPETENCY_REFERENCE.md`

**Why this one.** This is the official documentation for the week. The competency text in it is
transcribed from the Ohio Department of Education and Workforce Outcome and Competency Descriptions
for subject code 145130. Competency 2.14.4 is the one you are being assessed on, and it names the five
parameters in the order this module uses them.

Outcome 2.14 is 22.11 percent of the WebXam, the heaviest weight on the blueprint. This week is the
heaviest single competency inside it. That is not a reason to memorize a list. It is a reason to be
able to defend a label.

**[VERIFY]** the Ohio Department of Education and Workforce website if you want the source document
itself. No direct URL is given here, because the department reorganizes its site and a stale link to a
state document is the specific failure this week teaches you to catch. The repository copy names the
source document, its subject code, and its year, which is a citation you can follow.

**Time.** 10 minutes. **Level.** On-level.

---

## 8. The `urllib.request` module

`https://docs.python.org/3/library/urllib.request.html` · **Confident.**

**Why this one.** The toolkit README has two one-line commands built on `urllib.request`: the one that
flips the stub mode without restarting, and the one that queries `/stub/parse`. On Wednesday you will
want to run the same prompt several times without retyping it. Reading this page is what lets you
write that loop yourself rather than pasting a line you do not understand.

**Assign a question:** *Find what `urlopen` raises when the server answers with HTTP 500, and what
that exception carries that tells you the status code.* That is exit code 3 in `ask.py`.

**Time.** 15 minutes. **Level.** Extension.

---

## 9. Crossref and the DOI resolver

`https://www.crossref.org/` · **[VERIFY]** before assigning.
`https://doi.org/` · **[VERIFY]** before assigning.

**Why these.** This is the interactive practice for the week, and it is interactive in the only sense
that matters here: you type an exact string, you get a result, and you write down what came back
including nothing.

A DOI is an identifier registered for a published item. If an output hands you a DOI, resolving it is
the fastest check available, and a DOI that resolves to nothing is a strong result you can record.
Crossref holds metadata for a large share of registered scholarly items, so a title search there is
the second move.

**They are not a proof of fakery.** Plenty of real work has no DOI and is not in Crossref: a school
district policy, a state competency document, a local newspaper piece. **"Not in Crossref" is a
recorded negative result, not a verdict.** The lecture notes say the same thing in the section on
checks that come back complicated.

**Assign a question:** *Take one fabricated citation from your own Wednesday run. Search the venue
first, then the title, then the author. Write down the exact string you searched each time and what
came back. Which of the three searches told you the most, and why does the notes file say to search
the venue first?*

**Time.** 20 minutes. **Level.** On-level.

---

## 10. A library catalog and a scholarly search

`https://scholar.google.com/` · **[VERIFY]** before assigning.

**Named with no URL:** your school library catalog, the public library catalog for the county, and the
statewide research databases Ohio schools reach through INFOhio and the Ohio Web Library. **[VERIFY]**
all three, and get the current entry point from your librarian rather than from a link in a document
written a year ago.

**Why these.** Tuesday's check drill includes one citation that is a real document in this building.
No web search finds it. The point of including it is that a student whose only tool is a search engine
will record a false negative and call a real document fabricated, with a straight face.

**Talk to the librarian before Tuesday.** Ten minutes with somebody whose job is finding things will
improve the class average on this lab more than another hour of practice.

**Time.** 20 minutes. **Level.** On-level.

---

## 11. Retraction Watch

**Named with no URL. Search for it by that exact title.** **[VERIFY]** before assigning.

**Why this one.** It reports on published research that was later withdrawn. It is the industry
connection for Tuesday, and it is uncomfortable in a useful way: a citation can be real, correctly
formatted, resolvable, and still point at work that has been retracted. Authenticity and Validity come
apart there in a way no worked example makes as vivid.

**Read it for the shape, not for a specific case.** Do not carry a case out of it into your own
writing unless you have checked that case yourself, which is the entire method of this week.

**Time.** 15 minutes. **Level.** Extension.

---

## 12. Three real papers, named with no URLs

**Search each by its exact title.** **[VERIFY]** whatever you find, and prefer the version hosted by
the conference or by one of the authors.

- **"Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification"**, by Joy
  Buolamwini and Timnit Gebru
- **"Model Cards for Model Reporting"**, by Margaret Mitchell and co-authors
- **"Datasheets for Datasets"**, by Timnit Gebru and co-authors

**Why these three.** Gender Shades is about image classification rather than a language model, which
is the reason to read it in this course rather than a reason to skip it. Its method is exactly SQ-19:
hold everything constant, vary one attribute of the subject, measure what changes, and report the
numbers separately for each group instead of as one average. That is the difference between a bias
finding and a bias opinion.

The other two are about documentation. A model card says what a model was built for, what it was
measured on, and where it should not be used. A datasheet says the same for a dataset. Both exist
because "the model is accurate" is a claim with no scope in it, and Thursday teaches you to demand the
scope.

**These are written for adults in the field.** Read the abstract and the method. Nobody expects you to
read the related-work section. If a paper turns out to be behind a paywall, say so and move on rather
than hunting for a copy.

**Time.** 45 minutes for all three at abstract-and-method depth. **Level.** Extension.

---

## 13. Side quest

**SQ-19 The Bias Audit** unlocks Thursday of Week 5. Two blocks, difficulty three stars.
Catalog entry: `../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.
Bundle: `../../../../Misc/side-quests/SQ-19-The-Bias-Audit/`.

Design a repeatable test for bias in a locally hosted model. Ask for the same kind of thing many
times, varying only one detail, and record what changes. Done when your method is written clearly
enough for somebody else to rerun it, you have at least 30 recorded outputs, and your conclusion
separates what you measured from what you suspect.

**Rules, from the catalog:** no real people, no student data, no classmates as subjects.

**The hardest part is designing a test that could come out either way.** A test that can only confirm
what you already believed is not a test. Read Potential Bias worked example 3 before you design yours.

**SQ-18 Prompt Ablation** is still open for anybody who has not done it, and its method carries
straight into SQ-19.

---

## 14. A free video

**[VERIFY] No specific video is linked here.** This is the hardest week in the module to find a decent
free video for. Most of what exists is either a demonstration of a commercial product this course does
not use, or a list of tells for spotting fake citations, and **a list of tells is the opposite of what
this week teaches.** Tells have false positives and false negatives. The only reliable method is to go
and look.

**Search for a video by this description:** a librarian or researcher walking through a citation check
end to end, on screen, including a search that comes back empty. Twenty minutes or under. **Vet it
before you assign it:** if it never shows a search that fails, it is not showing the job.

**If you cannot find one that passes that test, do not assign one.** Tuesday's live four-step check in
front of the room does the same work, and the instructor narrating a search they would have got wrong
is worth more than a polished video.

**Level.** Remediation.

---

## 15. Gate 1 reps and the self-checks

**Gate 1.** The Module 2 rep bank, `MCCTC_145130_Gate1_PromptingAndEvaluation.md`, in
`06-gate1-reps/`, assigned by your instructor from the instructor copy. Week 5 runs Reps 16 to 20,
with Reps 09, 11, 12, and 18 returning as review. Rep 09 comes back on purpose, because most students
fail it twice before the attribution habit sticks.

**Self-checks.** The four Week 5 lecture notes carry twelve self-check questions with worked answers.
**Before Friday you should be able to answer all twelve without reading the answers first.**

The four that predict Friday's Gate 2 score best:

- Five Parameters, question 3: you have eight findings and all eight are labelled Validity
- Authenticity, question 3: your partner writes "this source is fake" with no search recorded
- Why Models Fabricate, question 2: a classmate grounds a prompt with three supplied sources and still
  gets an output you should not trust
- Potential Bias, question 2: an output that is accurate in every claim and cites real sources, and
  still has a bias finding in it

**Time.** 25 minutes. **Level.** Review.

---

## For the student who is behind

1. The Five Evaluation Parameters notes, worked examples 1 and 4 only, which are the Validity and
   Hallucination pair
2. Your own Infographic Autopsy from 145060, reread, with one finding relabelled
3. The four-step citation check from Tuesday, written on an index card and used on one citation
4. Before Friday: the twelve self-checks, and nothing new

**If your Hallucination Hunt has a verdict with no recorded search, that verdict scores zero.** Redo
the verification with your instructor before Friday rather than after.

## For the student who is ahead

- SQ-19 The Bias Audit, method design first
- A fourth fabrication attempt Wednesday with a different prompt shape, to see whether the shape
  changes what gets invented
- The three papers in resource 12, at abstract-and-method depth, and bring one method you could steal
  for SQ-19
- Check a citation from a real article you bring in yourself, and record the search either way
