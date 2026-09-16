# Lab M06-04 · The Acceptance Run
## 145130 Applications of AI · Module 6 · Week 18, Monday

**Files:** `lab-m06-04-files/`
**Time:** Monday Build 1 and Build 2.
**Due:** the run sheet at the end of Build 1. The corrections at the end of Build 2.
The record is due Tuesday, end of Build 1.

---

## The scenario

On Thursday of Week 17 you wrote eight acceptance cases and a stakeholder agreed
to them. Today you run them, in front of that person, on the thing you built.

**You do not change a case because it is about to fail.** That is the one rule and
it is the reason the whole procedure exists.

---

## What you will produce

A results sheet with a verdict and evidence on every case, a corrections sheet with
a re-run under every fix, and the beginning of the acceptance record.

---

## What is in the folder

| File | When |
|---|---|
| `acceptance-run-sheet.md` | Build 1. Print one per team |
| `corrections-sheet.md` | Build 2. Print one per team |
| `acceptance-record-template.md` | The file you commit, due Tuesday |

**Your procedure is your own**, in `acceptance/acceptance-procedure.md`, committed
on Thursday of Week 17. **Use the committed version.** If you edited it over the
weekend, use the Thursday commit and note that you did.

---

# Part 1 · The pre-run, with the stakeholder · 10 minutes

**Read them the script at the top of the run sheet.** It says three things: some
cases are meant to fail, a surprise failure gets written down rather than fixed in
front of them, and anything that does not make sense to them is a finding about
your writing.

Then check the platform line is in your procedure. **If it is not, write it now**
and note that it was missing, because that is a real finding about Thursday.

**Acceptance criteria.**

- [ ] The script read out loud
- [ ] The platform line present, or written now and noted as missing
- [ ] The commit hash of the procedure you are running written on the sheet

---

# Part 2 · Run the eight cases · 30 minutes

**Three verdicts and only three.**

```
PASS      you saw the Then
FAIL      you did not
NOT RUN   you could not run it, with a reason. Not the same as a pass
```

**"What you actually saw" is an exit code, a file name, a line of output, or a
count.** Not "it worked".

**Two things will happen and both are normal.**

**Something fails that you did not expect.** Write it down. Do not fix it. Do not
explain it to the stakeholder at length. The sentence is: "that is a real failure,
we will fix it this afternoon and re-run it."

**The stakeholder asks what a case means.** Write that down too. It means the case
was not clear enough, and a case two people read differently is a case that will be
argued about later.

**Acceptance criteria.**

- [ ] Eight verdicts, with evidence on every one
- [ ] Every NOT RUN has a reason
- [ ] The counts at the bottom add to eight
- [ ] What the stakeholder said, written down
- [ ] The three honesty boxes ticked

**Between one and four failures is the normal range.** Eight passes usually means
the cases were written to pass, and you will be asked which one could have failed.

---

# Part 3 · Corrections · Build 2, 40 minutes

**Three parts per correction:** the case that failed, what you changed with a file
and a line, and the re-run that passed.

**A correction with no re-run under it is a plan.**

Then, and this is the part people skip:

**Re-run the whole procedure, not only the case you fixed.** A change that fixes
AC-4 and breaks AC-1 is ordinary and you will not find it by re-running AC-4. Eight
cases by hand is ten minutes.

**Acceptance criteria.**

- [ ] One entry per failed case, all three parts
- [ ] The whole procedure re-run after the last correction
- [ ] Final counts recorded
- [ ] Anything still failing written into the deferred section with what you agreed

---

# Part 4 · Start the record · Build 2, 15 minutes

Copy `acceptance-record-template.md` into `acceptance/acceptance-record.md` and
fill in everything except section 6, which is tomorrow.

**Section 5, known and not fixed, exists on purpose.** A record with something in
it is an honest record, not a weak one.

**No names anywhere in the file.** Role only.

**Acceptance criteria.**

- [ ] `acceptance/acceptance-record.md` committed
- [ ] Sections 1 to 5 complete
- [ ] Dates written as weeks and days
- [ ] No name anywhere in it

---

## If it breaks

**"Our stakeholder could not come."**
Send them the eight cases and the results afterwards, in writing, and record it as
answered in writing. **Do not run it alone and write down that they were there.**

**"All eight passed."**
Possible, and worth one question before you celebrate: which of your eight could
have failed, and what would have had to be true. If the answer is none of them, you
have a procedure rather than a test, and the fix is to add one case tonight that
could go either way.

**"A case turned out to be wrong, not the program."**
Say so out loud, to the stakeholder, before running it. Record it NOT RUN with the
reason. **Then you and the stakeholder decide together whether to change it.** That
decision belongs to both of you and it happens in the open, not in a text editor.

**"We fixed it and now a different case fails."**
Normal. That is what the full re-run is for and you found it the right way.

**"We ran out of time in Build 2."**
Finish the corrections in Tuesday Build 1, which was built with room for it. Write
down which entries are unfinished rather than leaving the sheet blank.

---

## Submission checklist

- [ ] Run sheet, eight verdicts with evidence, counts, stakeholder notes
- [ ] Corrections sheet, three parts per entry, full re-run recorded
- [ ] `acceptance/acceptance-record.md`, sections 1 to 5
- [ ] No name anywhere in any of it
- [ ] Committed at the end of each period

---

# Extended options

## SCAFFOLDED

**Five cases instead of eight**, chosen with your instructor before Build 1: two
that should pass, two failure cases, and the privacy case.

**The pre-run script is read for you** by your instructor, once, to the whole group,
so that the first five minutes are not spent on it.

**Part 4 is sections 1, 3, and 6 only.**

**Same criteria for the parts you do**, including evidence on every verdict.

## STANDARD

The lab as written above.

## EXTENDED

**Turn your procedure into a program.**

Eight cases you can run with one command, that prints PASS or FAIL per case and a
count at the end, and that starts and stops whatever it needs on a port you pass.

**The hint, and it points at documentation:** read
`subprocess.run` and `tempfile.mkdtemp` in the standard library documentation, and
look at how the three checkers you have already used in this course start a server
in a thread and shut it down in a `finally` block.

**The rule that makes it worth doing:** it has to run on a machine that is not
yours, in a folder that is not yours, without editing anything. **If it only works
in your project folder, it is a script, not a procedure.**

## APPLIED

**Run somebody else's procedure.**

Swap with another team. Take their committed procedure and their repository, and
run their eight cases without asking them a single question.

**Record every case you could not run, and why.** That list is the deliverable and
it is worth more to them than the verdicts are.

**Then swap the lists.** Almost every team will find that at least two of their
cases assume something only they know: a folder name, a port, a file that is on
their machine and not in the repository. **That is what a procedure is for and it
is the fastest way anybody learns it.**

---

## Which version, three observable signals

| If you see | Hand them |
|---|---|
| A team whose stakeholder is not coming and who has fewer than six cases written | **SCAFFOLDED**. Five cases run properly beats eight run badly, and the group pre-run saves the period |
| A team that finished the run in fifteen minutes with a full sheet | **EXTENDED**. They will run this procedure at least twice more this week and a program pays for itself by Wednesday |
| Two teams who both say all eight of their cases passed | **APPLIED**, and pair those two with each other. Each will find the other's assumptions inside five minutes |
