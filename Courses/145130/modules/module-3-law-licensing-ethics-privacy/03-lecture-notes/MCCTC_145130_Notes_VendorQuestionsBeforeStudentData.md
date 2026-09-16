# Lecture Notes: The Questions You Ask Before Anything Touches Student Data
## 145130 Applications of AI · Module 3 · Week 9, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W09_VendorQuestions.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W09_VendorQuestions.pptx)

If you missed class, you can learn this concept from this file alone. Run both programs.

**Competencies:** 2.1.12 (privacy security compliance on systems), 2.14.2 (how AI impacts
society and the ethical implications of its usage), 1.3.8 (verify compliance with computer
laws and regulations), 3.2.1 (data and application security: **taught here, not on the
blueprint**).

---

## Read this first

This file is not legal advice and it will not tell you whether a product is safe to use. It
teaches a set of questions and a way of judging whether an answer is an answer.

**No real vendor is named anywhere in this file, and every question-and-answer pair below is
invented.** They are written in the shapes real vendor responses take. Judging real answers is
the skill, and you practise it here on invented ones so that nobody is unfairly characterized.

---

## Why this exists

**You will be the person who is asked.** Not in five years. This year, or the year after.

A teacher who knows you are the AI student will ask whether some tool is fine to use with a
class. A club advisor will ask about a free tier. In a job, a manager will ask whether a
service can be dropped into a workflow this week. Everybody in the room will want the answer to
be yes, and you will be the only person who has ever read a data processing agreement.

The skill is not knowing the answer. **The skill is knowing the questions, and knowing when you
have been handed something that is not an answer.**

---

## The nine questions

These are section 8 of your privacy impact assessment, and they are the nine you ask in that
order.

| # | Question | Why it is on the list |
|---|---|---|
| 1 | Where does the software run, and does any input leave the building | Everything else changes depending on this answer |
| 2 | Is any input retained, by whom, and for how long | Retention is where a one-time use becomes a permanent record |
| 3 | Is any input used to train or improve anything | Different question from retention, and different from selling |
| 4 | Who can read the contents, and is that access logged | "Authorized personnel" is not a number |
| 5 | Where, physically, is the data stored | Location determines which legal regime reaches it |
| 6 | Who else is involved: sub-processors, model providers, analytics | The vendor's vendors are your vendors |
| 7 | What happens to the data when we stop using the service | The answer needs a trigger, an actor, and a deadline |
| 8 | What does the license permit us to do with the output | Week 7, applied to a service instead of a file |
| 9 | What does the contract say when it disagrees with the marketing page | The contract governs. Ask for it |

**Question 9 is the one people skip and it is the one that decides.** A marketing page, a
privacy policy, and a contract are three different documents that say different things, and
only one of them is enforceable.

### Where the answers actually live

| Source | What it is good for | What it is not |
|---|---|---|
| Marketing page | Finding out what they want you to believe | Evidence of anything |
| Privacy policy | The consumer-facing promises, which may not be the school-facing ones | The agreement your school is under |
| Contract or data processing agreement | The terms that govern | Usually not public. Ask for it |
| The source code | Settling a factual claim about behaviour, when you can read it | Available only for software you can see |
| Your own test | Settling a factual claim about behaviour, for anything | Proof of what happens when you are not watching |

**The order of trust runs right to left in that table.** A test you ran beats a document
somebody wrote about what the software does.

---

## The five carve-outs that survive a good-sounding answer

Every one of these is a sentence that is true and that leaves a hole.

**"We do not sell your data."** Selling is one narrow thing. Sharing, disclosing to
sub-processors, and using the data internally are all outside that sentence. **Ask about use,
not about sale.**

**"Your data is not used for training."** Often followed by a second sentence about
"aggregated and de-identified" information being used to improve the service. That may be
completely reasonable. It is also a separate question with its own answer, and you learned on
Wednesday that de-identified is a claim that has to be measured rather than asserted.

**"You retain ownership of your content."** Look for the licence grant that usually sits near
it. Retaining ownership while granting a broad, irrevocable, worldwide licence to use the
content is a normal contractual structure and it is not the same as the sentence implies.

**"Data is encrypted."** In transit, at rest, or both. Encrypted with keys held by whom. **A
vendor who holds the keys can read the data**, and "encrypted" without that detail answers
nothing.

**"We are FERPA compliant."** FERPA obligations sit on the school. A vendor can help the
school meet them or make it impossible, and a badge on a web page is not a contractual
commitment. **Ask what is in the agreement.**

---

## Why this course runs models locally

You have been told the constraint since Week 1: commercial AI developer APIs require users to
be 18 or older, so this course uses locally hosted models.

Now you can see the second reason, which is that **running locally answers questions 1 through
7 at once**, and it answers them in a way you can verify yourself rather than by trusting a
document.

That is a real advantage and it is not free. Local models are weaker and slower. You get worse
output, on worse hardware, and you can check every claim about where the data went. **That
trade is the single most concrete version of this module's whole subject**, and you should be
able to argue both sides of it, which is what Week 8 was for.

---

## Worked example 1: settle it by reading the code

A claim about where data goes is a factual claim. When you can see the source, you can settle
it in under a minute.

```python
# network_audit.py: every address and every network call in the source tree.
import os
import re

PROJECT = "study-buddy"
URL = re.compile(r"https?://[^\s\"'<>)]+")
CALLS = re.compile(r"\b(urlopen|urlretrieve|requests\.\w+|socket\.|http\.client|"
                   r"smtplib|ftplib)\b")

for folder, _, filenames in os.walk(PROJECT):
    for name in sorted(filenames):
        if not name.endswith(".py"):
            continue
        path = os.path.join(folder, name)
        text = open(path, encoding="utf-8", errors="replace").read()
        urls = sorted(set(URL.findall(text)))
        calls = sorted(set(CALLS.findall(text)))
        if urls or calls:
            print(path)
            for url in urls:
                local = url.startswith("http://127.0.0.1") or "localhost" in url
                print(f"   address: {url}  {'(this machine)' if local else '(REMOTE)'}")
            for call in calls:
                print(f"   network call: {call}")
```

Output:

```
study-buddy\study_buddy.py
   address: http://{MODEL_HOST}:{DEFAULT_PORT}/api/generate  (REMOTE)
   address: http://{MODEL_HOST}:{port}/api/generate  (REMOTE)
   network call: urlopen
```

**That is not the answer anybody wanted, and it is the most useful output in this file.**

Study Buddy builds its address from an f-string, so the literal address never appears in the
source. The scanner found the template instead of the address, could not tell what host it points
at, and labelled both lines `REMOTE` because they do not start with `127.0.0.1`. **The scan was
wrong in both directions at once:** it did not resolve the address, and the guess it made about
what it found was the opposite of the truth.

It did find one thing worth having. **One network call in the whole tree**, and it tells you
exactly where to look.

So look, with your own eyes, two lines above it in the source:

```python
DEFAULT_PORT = 11634
MODEL_HOST = "127.0.0.1"
```

**Now you know.** Notice what that took: reading the file, because the tool could not do it for
you.

**Be honest about the rest of what this program does not prove.** It scans Python source in this
tree. It would also miss an address read from a config file, a call inside a compiled dependency,
or anything in a language it does not scan. **It is a place to look, not proof**, and the
stronger evidence is behavioural: run the program with an explicit port and read what it says.

```
python study_buddy.py notes/chemistry.txt --hints --port 11634
```

```
No model answered at http://127.0.0.1:11634/api/generate. The deck was written without hints. This is a model problem, not an empty result.
```

**The program printed its own address, and it is on this machine.** That is behaviour rather than
text, which is why it beats the scan. Stronger still: turn the network adapter off, run it again,
and see whether it still writes the deck.

**And note the `--port`.** Every command in this module passes one. A real Ollama listens on
11434, several stubs in this course listen on 11434, and a run against the wrong server on a
shared default looks exactly like a working run. **Nothing on the screen tells you.** This module
uses 11634 and every recorded command says so.

## Worked example 2: is that an answer

```python
# answers_check.py: did the vendor answer the question, or a different one?
# Every question and answer below is invented for this lesson.

EXCHANGES = [
    ("Is any student input retained, and for how long?",
     "We take privacy extremely seriously and are fully committed to student safety.",
     False, "no retention period anywhere in the sentence"),
    ("Is any student input used to train or improve your models?",
     "We do not sell student data to third parties.",
     False, "answers a different question: selling is not training"),
    ("Is any student input used to train or improve your models?",
     "Student input is not used for model training. Aggregated, de-identified "
     "usage statistics are used for service improvement.",
     True, "answers it, and introduces a carve-out that needs its own question"),
    ("Where is the data stored?",
     "Our infrastructure is hosted on industry-leading secure cloud providers.",
     False, "names no country, no region, and no provider"),
    ("What happens to our data if we stop using the service?",
     "Upon written request within 30 days of termination, all customer data is "
     "deleted from production systems and purged from backups within 90 days.",
     True, "gives a trigger, an actor, and two deadlines"),
    ("Who at your company can read the contents of a student's question?",
     "Access is limited to authorized personnel on a need-to-know basis.",
     False, "authorized by whom, how many people, and logged where"),
]

answered = 0
for question, answer, is_answer, note in EXCHANGES:
    answered += is_answer
    print(f"\nQ: {question}")
    print(f"A: {answer}")
    print(f"   {'ANSWERS IT' if is_answer else 'DOES NOT ANSWER IT'}: {note}")

print(f"\n{answered} of {len(EXCHANGES)} answers actually answered the question.")
print("An answer that does not answer is a finding, not a delay.")
```

Output:

```

Q: Is any student input retained, and for how long?
A: We take privacy extremely seriously and are fully committed to student safety.
   DOES NOT ANSWER IT: no retention period anywhere in the sentence

Q: Is any student input used to train or improve your models?
A: We do not sell student data to third parties.
   DOES NOT ANSWER IT: answers a different question: selling is not training

Q: Is any student input used to train or improve your models?
A: Student input is not used for model training. Aggregated, de-identified usage statistics are used for service improvement.
   ANSWERS IT: answers it, and introduces a carve-out that needs its own question

Q: Where is the data stored?
A: Our infrastructure is hosted on industry-leading secure cloud providers.
   DOES NOT ANSWER IT: names no country, no region, and no provider

Q: What happens to our data if we stop using the service?
A: Upon written request within 30 days of termination, all customer data is deleted from production systems and purged from backups within 90 days.
   ANSWERS IT: gives a trigger, an actor, and two deadlines

Q: Who at your company can read the contents of a student's question?
A: Access is limited to authorized personnel on a need-to-know basis.
   DOES NOT ANSWER IT: authorized by whom, how many people, and logged where

2 of 6 answers actually answered the question.
An answer that does not answer is a finding, not a delay.
```

**Two of six.** And notice that the four failures are not lies. Every one of those sentences is
probably true. They are answers to questions nobody asked, and the reason they work is that
they arrive in the tone of an answer.

**The one that answered best is the one with the most specifics in it.** "Within 30 days of
termination", "from production systems", "purged from backups within 90 days". A trigger, an
actor, and deadlines. **Specificity is the signal**, and it is the property you can check for
without knowing anything about the vendor.

**The third exchange is the most interesting one.** It answers the question honestly and then
opens a new one. That is a good vendor answer and it generates a new row in your assessment
rather than closing one. **An answer that raises a question is not a failure, and the version
that closes everything with no residue is the one to be suspicious of.**

---

## The wrong version, and what it does instead of an error

Here is how the decision actually gets made, most of the time, in most organizations:

> A teacher asks in a hallway whether a tool is fine to use. Somebody looks at the vendor's
> website, sees a page headed "Privacy" with a FERPA badge on it, and says it looks fine. The
> tool is in use with two classes by Friday.

**Nothing errors. Nobody did anything wrong by their own lights.** Every step was reasonable
and the whole sequence skipped nine questions.

What was actually established: a vendor published a page claiming something. What was not
established: where the data goes, who reads it, how long it is kept, what happens on
termination, and whether anything in the agreement matches the page.

**And here is the part that makes it hard to undo.** By the time anybody asks, two classes have
gradebooks in it, students have accounts, and the cost of the answer being no has gone from
zero to a week of everybody's time. **The whole value of asking early is that "no" is still
cheap.**

The version that works is not slower by much:

> "Before we put student work in it, I need four things: where it runs, whether input is
> retained, whether input trains anything, and what the agreement says about deletion. If we
> cannot get those in a week, we pilot it with made-up data instead."

## Why the wrong version is tempting

**The badge looks like evidence.** A compliance badge on a marketing page is a claim by the
seller about the seller. It has the visual grammar of a certification and it is not one unless
something behind it says so.

**Asking feels like obstruction.** Everybody in the conversation wants to use the tool, the
teacher has a real problem, and you are the person introducing friction. **Say the thing that
makes it not obstruction: offer the pilot with invented data.** That gets the teacher moving
today and keeps the questions open.

**Nobody has ever been thanked for the incident that did not happen.** This is true and it is
the permanent condition of security and privacy work. The recognition is structurally unfair.
Do it anyway, and **write down what you asked and when, because that record is the only thing
that ever shows the work.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **Data processing agreement** | The contract governing what a vendor may do with data you send. What governs, unlike a web page. |
| **Sub-processor** | A vendor your vendor uses. Their practices become yours. |
| **Retention period** | How long input is kept. An answer without a number is not an answer. |
| **Carve-out** | A narrower exception inside a broad-sounding promise. |
| **De-identified** | Direct identifiers removed. A claim to be measured, not a state to be assumed. |
| **Licence grant** | The permission you give a service over content you upload. Sits near "you retain ownership". |
| **Encryption in transit and at rest** | Two different protections. Ask which, and who holds the keys. |
| **School official exception** | The FERPA provision a school relies on for disclosures to people acting for it. Ask what the agreement says about control. |
| **Specificity** | Triggers, actors, and deadlines. The property that separates an answer from a sentence. |

---

## Self-check

**Question 1.** A vendor writes: "We never sell student data, and your school retains full
ownership of all content submitted to the platform." Name the two questions this sentence does
not answer, and write the follow-up you send.

**Question 2.** Run `network_audit.py` on the Study Buddy tree. It reports two addresses it
could not resolve and marks both `REMOTE`, which is the wrong label. Say why the tool got it
wrong, name two other ways Study Buddy could still send data somewhere that this tool would never
see, and say what test you would run that does not depend on reading source at all.

**Question 3.** You are asked on a Tuesday whether a class can use a new AI tool on Friday.
Write your reply. It has to be short, it has to say yes to something, and it has to keep the
nine questions open.

---

### Answers

**1.** The two questions it does not answer:

- **Is the data used**, for training, for service improvement, or for anything else. "Never
  sell" is silent on use.
- **What licence does the school grant** over that content. Retaining ownership and granting a
  broad licence are compatible, and the licence grant is the operative clause.

The follow-up:

> "Two follow-ups on that. First, is student input used to train or improve any model or
> service, including in aggregated or de-identified form. Second, could you point me at the
> clause in the agreement that sets out the licence we grant you over submitted content. I am
> looking for what the contract says rather than the policy page."

**2.** Two ways:

- **The address could be assembled at runtime** or read from a configuration file, so no
  literal URL appears in the source for the scanner to find.
**Why the tool got it wrong.** The address is built from an f-string, so the literal never
appears in the source. The scanner matched the template, and its `startswith("http://127.0.0.1")`
test could not match a string that begins with a brace, so it fell through to `REMOTE`. **The
tool's default guess, when it does not know, is the alarming answer**, which is a design choice
worth noticing: a scanner that fails loud is usually right to, and it still produced a false
statement.

Two other ways it would never see:

- **An address read from a config file at runtime.** Nothing is in the source at all.
- **A dependency could make its own calls.** The scanner reads `.py` files in this tree. A
  library, a compiled extension, or a subprocess is outside what it looked at.

**The test that does not depend on reading source:** run the program with the network adapter
disabled, or on a machine with no network at all, and see whether it still does its job.
Stronger still, watch the machine's outbound connections while it runs. **That test is about
behaviour rather than about text, which is why it beats the scan.**

**3.** For example:

> "Yes to a pilot on Friday with made-up student names, and I will help you set it up. Before
> any real student work goes in, I need four answers from the vendor: where it runs, whether
> input is retained and for how long, whether input is used to train or improve anything, and
> what the agreement says happens to the data if we stop. I will send them today. If the
> answers are good we switch to real work next week, and the Friday lesson is not lost either
> way."

**What makes it work:** it says yes to the thing the teacher actually needs, which is a lesson
on Friday. It names four concrete questions rather than raising a general concern. It commits
to doing the work today. And it puts a date on the decision, so the pilot does not quietly
become the deployment.
