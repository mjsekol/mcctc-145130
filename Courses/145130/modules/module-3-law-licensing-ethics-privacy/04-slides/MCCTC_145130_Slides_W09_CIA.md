# Confidentiality, Integrity, Availability, Applied to an AI Feature
---
## Slide 1: Your old systems could not do this
- They could lose data, corrupt it, or go down
- None of them could invent data
- And present it in the voice of the real data
- That is new, and it is why this gets a day
Speaker notes: You met CIA in your first year. You are meeting it again because a generative feature breaks integrity in a way nothing you have built before could. A system that is up and private and wrong has failed, and the person it fails is the one who believed it.
Image: Three old failure modes on one side, one new one on the other.
---
## Slide 2: Three properties, all three are security
- Confidentiality: only the right people can see it
- Integrity: accurate, complete, changed only by the allowed
- Availability: the people who need it can reach it
- Students treat one as the whole subject
Speaker notes: Almost everybody treats confidentiality as security and the other two as operations problems. They are not. Today every one of these gets a real failure and a real fix, and two of the three failures produce no error message at all.
Image: Three pillars, equal height, one labelled with each property.
---
## Slide 3: They pull against each other on purpose
- Lock the roster: confidentiality up, availability down
- Let everybody edit: availability up, integrity down
- Six backups: availability up, confidentiality down
- No configuration maximizes all three
Speaker notes: A design document that claims all three are fine has not made the decisions yet. Your assessment has a section for each, and stating the trade out loud is the work. When you write that section, name who feels the loss.
Image: A three-way slider where moving one moves the others.
---
## Slide 4: One line of a log file
```
log: purpose=attendance_letter record={'student_id': 'RM-40118',
'first_name': 'Priya', ... 'home_address': '4417 Alder Court',
'meal_status': 'reduced', 'services_plan': '504',
'counselor_note': 'Missed two weeks in October for a family matter.'}
```
Speaker notes: A home address. A services plan. A meal status. A counselor note about a family. Written to a file that exists so somebody can debug a run, readable by whoever can open the folder, kept until somebody deletes it, and almost certainly covered by no retention rule anybody wrote down.
Image: None. This slide is code.
---
## Slide 5: The same line, after the lab
```
log: purpose=attendance_letter ref=aef90667 fields_sent=6
```
Speaker notes: Everything a person debugging a failed run actually needs. Which purpose, which record, how much moved. The name never helped anybody debug anything. The reference is salted per run, so two log files from two days cannot be lined up to rebuild one student's history.
Image: None. This slide is code.
---
## Slide 6: Integrity, and the sentence nobody put there
```
Draft 1  numbers in the draft : ['9']
         not in the record    : none

Draft 2  numbers in the draft : ['9', '6', '85']
         not in the record    : ['6', '85']
```
Speaker notes: Draft two is a better letter. More specific, more helpful sounding, and it offers an explanation. It also claims six absences were Mondays and that there is an eighty five percent threshold, neither of which the school has. The phrase our records show is at the front of that sentence and is now false about most of it.
Image: None. This slide is code.
---
## Slide 7: The checker misses the worst part
- "Which often indicates a transportation problem"
- No number in it, so the checker never sees it
- That clause would upset a family most
- Automated checks find the category you thought of
Speaker notes: This is the most important line in today's lesson. An automated check on model output finds the kind of problem its author imagined. The human reader is not optional, and the human reader needs a specific rule, not an instruction to read it over.
Image: A draft with the numeric flags shown and one unflagged clause circled.
---
## Slide 8: Availability, done honestly
- The deck was still written. The core worked
- The failing address is printed
- The failure is not disguised as a result
- "No hints available" would have been a lie
Speaker notes: A system that reports its own failures as findings will eventually report no records found when it means the database was unreachable, and somebody will act on it. That is an availability failure wearing an integrity costume, and it is the same running thread as every week of this program.
Image: A terminal showing the deck written and the failure named.
---
## Slide 9: The fix that makes it worse
```python
def describe_for_log(record, purpose):
    blob = str(record).encode("utf-8")
    return "record=" + hashlib.sha256(blob).hexdigest()
```
Speaker notes: The team is told the log leaks, so they hash the whole record. The leak is gone. And two new problems arrived, one of which is that this is not as private as it looks.
Image: None. This slide is code.
---
## Slide 10: Two new problems, no error message
- No salt, small candidate set, so it is guessable
- Anybody with the roster can hash and match
- The log no longer says what happened
- A log nobody can use will be ignored or deleted
Speaker notes: Hashing protects a secret drawn from a huge space, like a password. A student ID from a roster of four hundred is not that. And the test they ran was are names gone. The test nobody ran was can I still debug from this file, which is the reason the file exists.
Image: A hash column beside a roster, with arrows matching them up.
---
## Slide 11: What you are about to build
- Write minimize with one field list per purpose
- Make an unknown purpose refuse, not return everything
- Rewrite the log line so it carries no personal value
- Salt the reference so runs cannot be joined
Speaker notes: Build one is Lab M03-03, and the self-check runs ten tests. Build two is the CIA section of your privacy impact assessment, one paragraph each, and every paragraph names the person who feels the loss. Three paragraphs claiming everything is fine scores zero.
Image: A ten-line check output with every line passing.
---
