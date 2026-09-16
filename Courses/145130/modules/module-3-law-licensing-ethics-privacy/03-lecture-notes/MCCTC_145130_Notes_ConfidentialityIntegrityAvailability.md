# Lecture Notes: Confidentiality, Integrity, Availability, Applied to an AI Feature
## 145130 Applications of AI · Module 3 · Week 9, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W09_CIA.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W09_CIA.pptx)

If you missed class, you can learn this concept from this file alone. Run every program.

**Competencies:** 2.1.1 (explain the need for confidentiality, integrity, and availability
of information), 3.2.1 (identify and implement data and application security: **taught in
this module, and not on the WebXam blueprint**), 2.14.2 (how AI impacts society and the
ethics of its usage).

---

## Read this first

This file is not legal advice. CIA is not law at all. It is the three-part frame security
people use to describe what can go wrong with information, and it is the frame every
privacy law you meet tomorrow is built on top of.

**The fixture this week uses an invented roster.** Riverbend Middle does not exist and every
student in `roster.py` was written for this lab. **No real student data appears anywhere in
this course, in any file, ever.** That rule is not about this lab. It is the rule.

---

## Why this exists

You met CIA in your first year, in 145060's security week. You are meeting it again because
a generative feature breaks it in a way nothing before it did.

Here is the specific new thing. **Every system you have built until now could lose data,
corrupt data, or go down. None of them could invent data and present it in the same voice as
the real data.** That is an integrity failure with no precedent in the systems you have
written, and it is why this frame gets a whole day rather than a review slide.

---

## The three properties, stated properly

| Property | The question it asks | Who is hurt when it fails |
|---|---|---|
| **Confidentiality** | Can only the people who should see this see it | The person the information is about |
| **Integrity** | Is this information accurate, complete, and changed only by people allowed to change it | Anybody who acts on it |
| **Availability** | Can the people who need it get to it when they need it | The people the system was supposed to serve |

**All three are security.** Students consistently treat confidentiality as the whole subject
and treat the other two as operations problems. They are not. A system that is up and
private and wrong has failed, and the person it fails is the one who believed it.

### The three pull against each other, on purpose

This is the part worth understanding, because every design decision you make this week is a
trade among the three.

- Lock the roster so that only two people can open it: **confidentiality up, availability
  down.** The secretary who needs it on a Thursday cannot get it.
- Let everybody edit the attendance file so corrections happen fast: **availability up,
  integrity down.**
- Keep six backups of everything forever: **availability up, confidentiality down**, because
  now there are six copies to protect and one of them is on a drive in a closet.

**There is no configuration where all three are maximized.** A design document that claims
otherwise has not made the decisions yet. Your privacy impact assessment has a section for
each of the three, and the reason is that stating the trade out loud is the work.

---

## What a generative feature does to each one

### Confidentiality

The new confidentiality surface is the **prompt**. Anything you put in a prompt has been
handed to the model, and depending on where the model runs, to whoever operates it, to
whoever reads its logs, and to whatever it was configured to retain.

This is why the course rule is absolute: **no student personal data enters any AI tool,
ever.** Not because a local model is dangerous, but because the habit of asking "what is in
this prompt" has to be automatic before you ever work somewhere that uses a cloud one.

The second surface is the **log**, and it is the one that actually leaks in practice. Worked
example 1 is a log line, and it is carrying a counselor note.

### Integrity

Three integrity failures, in increasing order of how hard they are to see:

1. **Wrong data in the record.** Oldest problem in computing. A generative feature does not
   cause it and does make it louder, because it turns a wrong number into a confident
   paragraph sent to a family.
2. **Data changed by somebody who should not have changed it.** Also old. Access control and
   audit logs.
3. **A claim added next to the data that the data does not support.** New. The model writes a
   sentence that is plausible, fluent, and not in the record. Nothing was corrupted. Something
   was **added**, and it reads exactly like the rest.

Worked example 2 is number three, and it is the one to take away from today.

### Availability

A generative feature is a new dependency, and dependencies fail. The model server is down, the
machine is being used, the reply takes forty seconds, the reply comes back malformed.

**The availability question is not "will it fail". It is "what does the person do when it
does".** A feature with a clear manual fallback has a bad day. A feature that became the only
way to do the job has an emergency.

---

## Worked example 1: confidentiality, in one line of a log file

This is the starter and the solved version of the same function from this week's lab. Both
outputs are real.

**Before.** The log line carries the whole record.

```
python minimize.py
```

```
   log: purpose=attendance_letter record={'student_id': 'RM-40118', 'first_name': 'Priya', 'last_name': 'Raman', 'date_of_birth': '2011-03-14', 'grade': 7, 'home_address': '4417 Alder Court, Riverbend', 'guardian_name': 'S. Raman', 'guardian_email': 's.raman@example.invalid', 'guardian_phone': '555-0142', 'bus_route': '12', 'meal_status': 'reduced', 'services_plan': '504', 'photo_consent': False, 'absences_this_term': 9, 'tardies_this_term': 2, 'counselor_note': 'Missed two weeks in October for a family matter.'}
```

**Read what is in that line.** A home address. A services plan. A meal status. A counselor
note about a family matter. All of it written to a file that exists so that somebody can
debug a run, opened by whoever can read the folder, kept until somebody deletes it, and
almost certainly never covered by any retention rule anybody wrote down.

**After.** The same function, after the lab.

```
   log: purpose=attendance_letter ref=aef90667 fields_sent=6
```

Everything a person debugging a failed run actually needs is in that line: which purpose ran,
which record it was, and how much moved. **The name never helped anybody debug anything.**

`ref` is a hash of the student ID with a salt that is regenerated every run, so two log files
from two different days cannot be lined up to rebuild one student's history. Without the salt,
the reference would be a permanent identifier wearing a disguise.

## Worked example 2: integrity, and the sentence nobody put there

```python
# grounding_check.py: does this draft say anything the record does not support?
# Every record and draft below is invented.
import re

RECORD = {
    "first_name": "Priya",
    "last_name": "Raman",
    "guardian_name": "S. Raman",
    "absences_this_term": 9,
}

DRAFTS = {
    "Draft 1": (
        "Dear S. Raman, our records show that Priya Raman has been absent 9 "
        "times this term. Please contact the office to discuss."
    ),
    "Draft 2": (
        "Dear S. Raman, our records show that Priya Raman has been absent 9 "
        "times this term, 6 of them on Mondays, which often indicates a "
        "transportation problem. Attendance below 85 percent puts a student "
        "at risk. Please contact the office."
    ),
}

known = {str(value) for value in RECORD.values()}

for label, draft in DRAFTS.items():
    numbers = re.findall(r"\b\d+\b", draft)
    unsupported = [n for n in numbers if n not in known]
    print(f"{label}")
    print(f"  numbers in the draft : {numbers}")
    print(f"  not in the record    : {unsupported if unsupported else 'none'}")
    print()

print("Every number in the second list came from the model, not from the record.")
print("This finds numbers. It cannot find an invented claim with no number in it.")
```

Output:

```
Draft 1
  numbers in the draft : ['9']
  not in the record    : none

Draft 2
  numbers in the draft : ['9', '6', '85']
  not in the record    : ['6', '85']

Every number in the second list came from the model, not from the record.
This finds numbers. It cannot find an invented claim with no number in it.
```

**No error. Draft 2 is a better letter.** It is more specific, more helpful sounding, and it
offers an explanation. It is also making three claims that the school does not have: that six
absences were Mondays, that this indicates a transportation problem, and that there is an 85
percent threshold.

The phrase "our records show" is at the front of that sentence, and it is now false about most
of what follows it. **The school's letter, on the school's letterhead, has told a family
something untrue about their child.** That is an integrity failure and nothing crashed.

**Now read the last line of the program's own output, because it is the most important line in
this file.** The checker finds numbers. "Which often indicates a transportation problem" has no
number in it, so the checker never sees it, and that clause is the one that would upset a
family most. **An automated check on model output finds the category of problem you thought of.
The human reader is not optional.**

## Worked example 3: availability, and the honest failure

Run Study Buddy with hints and nothing listening on the model port:

```
python study_buddy.py notes/chemistry.txt --hints --port 11634
```

Output:

```
No model answered at http://127.0.0.1:11634/api/generate. The deck was written without hints. This is a model problem, not an empty result.
Term           Definition (first 34 characters)
-------------  ----------------------------------
Covalent bond  a bond formed when two atoms share
Molarity       the number of moles of solute per
Mole           the amount of a substance containi
Ionic bond     a bond formed when one atom transf
Isotope        an atom of an element with a diffe

6 cards written to notes\deck.json
Hints requested: 6. Hints written: 0.
```

Three things that make this an availability answer rather than an availability failure:

1. **The core function still works.** The deck was written. The model was an enhancement and
   it stayed one.
2. **The failure is named.** The address is printed, including the port, so a person can check
   whether anything is listening there. **Every command in this module passes `--port` on
   purpose.** A real Ollama listens on 11434 and so do several stubs in this course, and a run
   against the wrong server on a shared default looks exactly like a working run.
3. **The failure is not disguised as a result.** "This is a model problem, not an empty
   result" is in the output on purpose. The version of this message that says "no hints
   available" is a lie, because it tells the user something about the hints rather than
   something about the model.

**That third point is a confidentiality and integrity lesson wearing an availability costume.**
A system that reports its own failures as findings will eventually report "no records found"
when it means "the database was unreachable", and somebody will act on it.

---

## The wrong version, and what it does instead of an error

A team is told the log leaks, so they fix it:

```python
# "Fixed": nobody can read the log now.
import hashlib

def describe_for_log(record, purpose):
    blob = str(record).encode("utf-8")
    return "record=" + hashlib.sha256(blob).hexdigest()
```

The log line becomes:

```
record=6f1b0d4c8a2e...
```

**No error. The leak is gone. The confidentiality problem is solved and two new problems have
been created.**

- **Availability of the log is gone.** Nobody debugging a failed run can tell which purpose
  ran, how many fields moved, or what went wrong. The log now costs disk space and provides
  nothing.
- **It is not as private as it looks.** The hash is of the whole record with no salt, so the
  same record hashes to the same value every time. Anybody who can guess a record, or who has
  the roster, can hash candidates and match them. A hash of a value drawn from a small known
  set is not anonymous.

The solved version in the lab drops the fields instead of hashing them, keeps the purpose and
the count, and salts the one identifier it does keep. **Confidentiality went up, availability
of the log stayed, and the identifier is good for one run only.**

## Why the wrong version is tempting

**It makes the visible symptom disappear completely.** No names in the log. The complaint that
started the work is fully resolved, and a resolved complaint feels like a solved problem.

**Hashing sounds like security.** It is a security primitive and it is being used here for a
job it does not do. Hashing protects a secret drawn from a huge space, like a password with
many possibilities. A student ID from a roster of 400 is not that.

**Nobody tested the log.** The test for the fix was "are names gone". The test nobody ran was
"can I still debug a failure from this file", which is the reason the file exists.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Confidentiality** | Only the people who should see the information can see it. |
| **Integrity** | The information is accurate and complete, and is changed only by those allowed to change it. |
| **Availability** | The people who need the information can get to it when they need it. |
| **The CIA trade** | Raising one of the three usually lowers another. Design is choosing which. |
| **Prompt surface** | Everything you put into a prompt, and therefore everything you have disclosed to whoever runs the model. |
| **Grounding** | Whether a generated statement is supported by the source record. |
| **Ungrounded claim** | A fluent sentence the record does not support. An integrity failure with no crash. |
| **Salt** | A value mixed in before hashing so the same input does not always produce the same output. |
| **Pseudonym** | A reference that stands in for an identity. Only as private as the salt and the size of the candidate set. |
| **Graceful degradation** | The core function keeps working when an enhancement fails, and the failure is reported honestly. |

---

## Self-check

**Question 1.** For each change, say which of the three properties goes up, which goes down,
and name the person who feels the loss:

a. The attendance file is moved to a folder only the two office accounts can open
b. Draft letters are kept for a year so anybody can look back at what was sent
c. The model server is given a four-second timeout instead of thirty

**Question 2.** Run `grounding_check.py`. It reports `['6', '85']` as unsupported in Draft 2.
Name the fourth problem in Draft 2 that the program does not report, explain why it cannot, and
say what control catches it instead.

**Question 3.** The "fixed" log line is `record=6f1b0d4c8a2e...`, a hash of the whole record.
Give two separate reasons this is a worse solution than the one in the lab. One of your reasons
has to be about a property other than confidentiality.

---

### Answers

**1.**

a. **Confidentiality up, availability down.** The loss is felt by anybody in the office who is
   not one of those two accounts, including whoever covers the desk when both are out. The
   right question is whether there is a third account for exactly that situation.

b. **Availability up, confidentiality down.** The loss is felt by every student named in a
   year's worth of letters, now sitting in a folder long after any reason to keep them.
   Integrity drops slightly too: a year-old draft that was never sent looks exactly like one
   that was.

c. **Availability of the hints goes down, availability of the tool as a whole goes up.** A
   four-second timeout means more hint failures on a slow machine, and it means the secretary
   is never sitting in front of a frozen screen for half a minute. The loss is felt by the user
   on the slow machine, who now gets fewer hints. Integrity is untouched either way, which is
   worth noticing: a timeout choice does not make the output more or less true.

**2.** The fourth problem is **"which often indicates a transportation problem."** It is a
claim about why the student was absent, and the school does not have that information.

The program cannot report it because **the program looks for numbers**, and that clause has no
number in it. Any automated check on generated text finds the category of failure the author of
the check thought of. This one was built for invented figures, and an invented explanation is a
different category.

**The control that catches it is a human reader with a specific rule**, stated in the
assessment and printed on the checklist: *if the draft says anything the record does not, delete
that sentence.* A general instruction to "read it over" does not catch this, because the
sentence reads well. A specific rule does, because it turns reading into a comparison.

**3.** Two reasons:

**Confidentiality, and it is weaker than it looks.** The hash has no salt and the input comes
from a roster with a few hundred possible records. Anybody with the roster can hash every record
and match them, which makes the log readable again to exactly the people most likely to have the
roster.

**Availability, of the log itself.** The log exists so that somebody can work out what happened
during a failed run. The hashed line does not say which purpose ran or how many fields moved, so
the file has stopped doing its job. A log nobody can use is a file that costs storage and returns
nothing, and it will be deleted or ignored, at which point the next incident has no record at
all.
