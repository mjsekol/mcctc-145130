# Lab M02-02: The Hallucination Hunt
## 145130 Applications of AI · Module 2 · Week 5, Wednesday and Thursday

**Gate:** 3 (open), with a containment rule. **Duration:** Wednesday Build 1 and
Build 2, Thursday Build 1. Due at the end of Thursday's Build 1.
**Competencies:** PRIMARY 2.14.4 (evaluate an AI result on hallucinations),
1.2.1 (extract relevant, valid information and cite sources). SUPPORTING 2.14.6,
1.1.7.

---

# Read this before anything else

**You are about to make a machine produce fake citations on purpose.** That is
the assignment. It is also the only assignment in this course that manufactures
something false, so it comes with rules that are not negotiable.

## The containment rules

1. **Every fabricated citation you produce stays in this lab's files.** It does
   not go in another assignment, a BPA submission, a social post, a group chat, a
   message to a friend, or a sentence you say to somebody outside this room
   without the words "this is fake" attached.
2. **Every fabricated citation in your file is labelled `FABRICATED` on the same
   line.** Not in a heading three paragraphs up. On the line.
3. **Every fabricated citation is verified and the verification is recorded.**
   Producing one is trivial. Checking one is the assignment and the grade.
4. **Nothing from this lab is ever presented as real to anyone.** Not as a joke,
   not as a test of somebody else, not to see if a teacher notices.
5. **No real person's name goes in any prompt or any output you keep.** Use Ava
   Ruiz, Kai Mendoza, Priya Okonkwo, or Dante Whitfield.

**Why the rules exist.** A fabricated citation is small, portable, and
convincing. It survives being copied. The point of this lab is that you cannot
tell one from a real one by reading it, which is exactly why one that escapes this
room is a problem: nobody downstream can tell either.

**If you are not comfortable producing fabrications**, say so and do the
ALTERNATIVE version in the extended options. It assesses the same competency using
fabrications that were produced for you. That is a legitimate choice and it costs
you nothing.

---

## The scenario

The Media Club is writing a one-page argument for the school board about whether
the club should get a larger equipment budget. Somebody offered to have a model
"find some research to back it up."

**Before anyone does that, the club needs to know what that actually produces.**
You are going to find out, under conditions where nothing can go wrong.

## What you will build

Three fabricated citations, each produced deliberately and recorded with the
prompt that produced it; a full verification record for each; and a grounded
rerun showing what changes when you supply the sources yourself.

---

# Before you start

Terminal 2, from `05-labs/prompt-toolkit`:

```
python stub_model_server.py
```

Work in `05-labs/` in a folder of your own. You need `prompts/`, `runs/`, and one
file called `hunt.md`.

**Put this at the top of `hunt.md`, before you run anything:**

```
# Hallucination Hunt
# EVERY CITATION IN THIS FILE THAT IS MARKED FABRICATED IS FAKE.
# None of them exist. They were produced for a classroom exercise and
# they are not to be used, quoted, or repeated anywhere.
```

---

# PART 1 · Wednesday Build 1 · Produce three

**Step 1.** Write `prompts/h1.txt`. Ask for a short research brief on something
your club argument would want, and ask for sources. Keep it open: no supplied
sources, no restriction, no route to say it does not know.
**Result:** a prompt of two or three lines.

**Step 2.** Run it.

```
python ../prompt-toolkit/ask.py --prompt-file prompts/h1.txt --label h1 --runs-dir runs --show
```

**Result:** a reply with a `Sources:` block. Count the entries.

**Step 3.** Write `prompts/h2.txt`. Same subject, **different shape**. Change the
role, or the format, or the number of sources requested. One materially different
prompt, not a reword.
**Result:** a second run with a different `Sources:` block.

**Step 4.** Write `prompts/h3.txt`. Ask about something **narrower and more
local**: this county, this school year, this kind of club specifically.
**Result:** a third run. Look at whether the citations got more specific.

**Step 5.** Copy the three citations you are going to work with into `hunt.md`,
one per line, each ending with the word `FABRICATED`, each with its run label.

**Step 6.** Before you check anything, write your prediction for each one: real,
fake, or cannot tell, and the reason. **Write it down now.** You will compare it
to what you find, and the comparison is one of the graded questions.

### Acceptance criteria, Part 1

- [ ] Three prompt files, committed before their runs
- [ ] Three recorded runs in `runs/`
- [ ] Three citations copied into `hunt.md`, each labelled `FABRICATED` on the
      line, each with its run label
- [ ] A prediction for each, written before any checking
- [ ] The warning block at the top of `hunt.md`

---

# PART 2 · Wednesday Build 2 · Check every one

Use the four-step order from Tuesday. **Check in this order**, because a
publication is quicker to find than an article, so a dead venue ends the search in
thirty seconds.

**Step 7.** For each citation, check the **venue**. Search the publication name in
quotation marks, in the school or county library catalog and in a general search.
**Record:** the catalog or service, the exact string, and what came back including
"no results."

**Step 8.** Check the **work**. Search the title in quotation marks. Then search it
without the subtitle.
**Record:** the same three things, twice.

**Step 9.** Check the **author**. Search the author name with two or three words
from the subject.
**Record:** the same three things. An author who appears nowhere is a signal. An
author who exists and writes about something unrelated is a different finding.

**Step 10.** Check the **details**: the year, the volume, the page range. These
only matter if steps 7 to 9 found something, and when they do, this is where a
real work with wrong numbers shows up. **That is a Validity failure, not a
hallucination**, and saying which is part of the grade.

**Step 11.** Write a verdict for each: fabricated, real, or unresolved.
**Unresolved is an allowed verdict** and sometimes the honest one.

**If a search returns something real or partly real, stop and write down exactly
what matched and what did not.** That is the most valuable outcome available in
this lab. Do not round it to "fake" because that is the answer you expected.

### Acceptance criteria, Part 2

- [ ] Three verification records, each with venue, title, author, and details
- [ ] Every search recorded with the service, the exact string, and the result
- [ ] At least one recorded negative result stated as a negative result
- [ ] A verdict for each, with "unresolved" used if that is what you found
- [ ] **No verdict without a recorded search.** A verdict with nothing under it
      scores zero, and it scores zero even when it is right

---

# PART 3 · Thursday Build 1 · Make it stop, then see what broke instead

**Step 12.** Take the prompt from `h1.txt` and write `prompts/h1_grounded.txt`
with three changes:

1. Supply real sources, as `SOURCE:` lines. Use documents that actually exist and
   that you can open: the student handbook and its section, a posted procedure, a
   club record, a page you have read.
2. Add: "Answer using only the sources below."
3. Add: "If the answer is not in the sources, say I do not know."

**Step 13.** Run it and compare.

```
python ../prompt-toolkit/ask.py --prompt-file prompts/h1_grounded.txt --label h1_grounded --runs-dir runs --show
python ../prompt-toolkit/compare_runs.py runs --show h1 h1_grounded
```

**Result:** the Sources column changes. Record both replies side by side in
`hunt.md`.

**Step 14.** Now read the **body** of the grounded reply against the question you
asked.

**Do not skip this step.** Fixing the fabrication can break something else. If
the grounded answer is about the sources rather than about your question, that is
a **Relevance** failure, and you have now watched an evaluation on one parameter
miss a failure on another.
**Record:** which parameters the grounded reply passes and which it now fails.

**Step 15.** Answer these four questions in `hunt.md`. They are the analysis and
they carry most of the grade.

1. **Which of your three citations would have fooled you a week ago, and what
   specifically made it convincing?** Name the feature, not the feeling.
2. **Compare your step 6 predictions to your step 11 verdicts.** How many did you
   get right? Answer honestly. Nobody is graded on the number.
3. **Grounding changed what the model produced. Did it make the model more
   honest?** Answer the mechanism, not the outcome.
4. **You are the person who says yes or no to "let me find some research to back
   this up" for the school board letter.** What do you say, and what would you
   need in place to say yes? A cost belongs in the answer.

**Step 16.** Read your whole `hunt.md` once, looking only for one thing: is every
fabricated citation labelled `FABRICATED` on its own line? Fix any that are not.
**This is the last step and it is the one that gets checked first.**

### Acceptance criteria, Part 3

- [ ] `h1_grounded.txt` with all three changes, committed before its run
- [ ] Both replies recorded side by side
- [ ] Step 14's parameter comparison written out
- [ ] All four analysis questions answered
- [ ] Every fabricated citation labelled on its line
- [ ] Committed and pushed

---

## If it breaks

**The model refuses to make up sources, or returns no `Sources:` block.**
Against the stub, check that your prompt actually asks for sources: it needs a
word like cite, citation, sources, or references. Against a real local model, some
will refuse. **That is a finding, not a failure.** Record the refusal, record the
prompt, and switch to the ALTERNATIVE version in the extended options for the
citations themselves. The verification work is unchanged and it is the graded
part.

**The three runs come back with the same citations.**
The stub seeds its invented sources from the exact prompt text, so two prompts
that differ by one character give different sources, and two identical prompts
give identical ones. If h1 and h2 match, your files are the same file. Check with
`fc prompts\h1.txt prompts\h2.txt` in cmd.

**`FAILED (nothing is listening at http://127.0.0.1:11434)`**
The stub is not running, or something else is on that port. Start it with
`--port 11534` and pass `--endpoint http://127.0.0.1:11534` to every command.

**Your search returns thousands of results and none of them is it.**
The title is generic. Search the venue instead, in quotation marks. A publication
that does not exist ends the question in one search, and a publication that does
exist gives you an index to search inside.

**You cannot decide between fabricated and unresolved.**
Then it is unresolved, and say what would settle it. Reaching for a verdict you
cannot support is the exact habit this lab exists to break.

---

## Stretch goal

Find the shortest prompt change that stops your model inventing sources, and the
shortest one that does not.

Run an ablation on your grounded prompt: remove the supplied sources but keep the
refusal route; remove the refusal route but keep the sources; remove both. Record
what each version produces. **One of those four combinations produces the most
dangerous output in this lab.** Say which and why in `hunt.md`.

---

## Submission checklist

- [ ] `hunt.md` opens with the warning block
- [ ] Every fabricated citation labelled `FABRICATED` on its line
- [ ] Three prompt files, plus `h1_grounded.txt`
- [ ] Four or more recorded runs
- [ ] Three full verification records with exact search strings
- [ ] Step 6 predictions, written before the checking
- [ ] All four analysis questions answered
- [ ] Step 14's parameter comparison
- [ ] No personal data anywhere
- [ ] `git status` clean, pushed
- [ ] AI usage log updated

---

# Extended Lab Options

All four assess 2.14.4 and 1.2.1 on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Twenty minutes into Part 2 and the record says "I looked and could not find it" with no search string | SCAFFOLDED |
| Three citations captured and the first venue search recorded by the end of Wednesday Build 1 | STANDARD |
| Finished Part 2 early, or asks why the model invented these particular sources | EXTENDED |
| Says they are not comfortable producing fabrications, or asks where this happens outside school | ALTERNATIVE / APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Part 1:** `h1.txt` is provided complete in
  `lab-m02-02-files/scaffolded/h1.txt`. The student writes h2 and h3.
- **Part 2:** a filled-in verification record for one citation is provided as a
  worked model in `lab-m02-02-files/scaffolded/worked_record.md`. The student
  copies its structure for their three.
- **Part 3:** the grounded prompt is provided with the `SOURCE:` lines blank. The
  student supplies real sources they can open.
- **Checkpoints:** show the instructor your three citations at the end of Part 1,
  and your first completed verification record twenty minutes into Part 2.

**Steps that stay, and they are not negotiable:** step 6 (the prediction), step 11
(a verdict per citation), step 14 (the parameter comparison), and all four
questions in step 15.

**Acceptance criteria:** three citations labelled, three verification records with
exact search strings, a grounded rerun, and all four analysis questions.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions.

**Added requirement 1.** Your three citations are three samples. Produce twelve
more from the same prompt with one word changed each time, and answer a question
the three could not: **does the invented venue name change with the subject, or is
the model drawing from a small set of venue-shaped names?** Record the twelve and
say what your evidence supports.

**Hint, not the answer.** Look at the venue names across all fifteen. Count the
distinct ones. Then decide what a small number of distinct venues would mean and
what a large number would mean, **before** you count. A prediction made after
looking is not a prediction.

**Added requirement 2.** Read `invented_sources()` in
`prompt-toolkit/stub_model_server.py`. Explain in `hunt.md` how it produces its
citations, then write one honest paragraph: which of your requirement 1
conclusions are about language models, and which are about this stub. **Be
specific about which is which**, because that distinction is the whole difference
between a finding and a story.

**Acceptance criteria:** all STANDARD criteria, fifteen recorded runs, a prediction
made before counting, a correct explanation of `invented_sources()`, and the honest
paragraph.

---

## ALTERNATIVE · for a student who does not want to produce fabrications

**This is a legitimate choice and it costs no marks.**

Three fabricated citations are provided in
`lab-m02-02-files/alternative/supplied_citations.md`, produced by the stub and
labelled. **Skip Part 1 entirely.**

**Everything else is identical.** Parts 2 and 3 are the graded work, and they are
unchanged: the four-step verification with recorded searches, the grounded rerun,
the parameter comparison, and the four analysis questions.

**One replacement for step 6:** write your prediction for each supplied citation
before you check it, the same way, and compare in step 15's question 2.

**One addition:** in `hunt.md`, one paragraph on why you chose this version. This
is not a justification you owe anybody. It is practice at stating a boundary in
writing, which is a thing you will have to do in a job, and it is worth doing once
where the stakes are a lab grade.

---

## APPLIED

**For the student who asks where this happens outside school.** It happens in
court filings, in medical summaries, in policy briefs, and in student work, and
the failure mode is identical every time: a citation-shaped string that nobody
checked, travelling further than the person who produced it expected.

**Changed scenario.** Instead of the club budget argument, take a claim you have
actually seen asserted with a source attached: a claim in a video description, a
statistic in a post, a "studies show" in an article. **Do not pick a person to
target.** Pick a claim.

**Do Part 1 differently.** Rather than producing fabrications, produce the
**check**: take the claim's source as given and run the full four-step
verification on it. If it has no source, that is your first finding and you then
ask a model for one, which puts you back in Part 1 with a live example.

**Everything else is the same**, including Part 2's recorded searches, Part 3's
grounded rerun on the same question, and all four analysis questions.

**The extra requirement that makes it the same lab.** One paragraph: **what would
have had to be true for the original claim to be checkable by its reader**, and
whether the person who posted it could reasonably have known. Be fair. The answer
is often that they could not, and that is the finding.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether
every verdict has a recorded search under it.
