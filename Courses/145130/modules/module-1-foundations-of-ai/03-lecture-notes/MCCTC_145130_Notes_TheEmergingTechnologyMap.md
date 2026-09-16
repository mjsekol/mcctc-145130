# Lecture Notes: The Emerging Technology Map
## 145130 Applications of AI · Module 1 · Week 2, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W02_EmergingTechnologyMap.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W02_EmergingTechnologyMap.pptx)

If you missed class you can learn this from this file alone. Nothing here needs a
computer.

**Competencies 2.4.1** (identify emerging technologies applicable to the
marketplace) **and 2.4.4** (describe them). Outcome 2.4 is 4.21 percent of your
exam, about four items, and this is the day those items come from.

---

## Why this exists

Two reasons, and the second one is the real one.

The exam names a specific list, so you learn the list. That is the small reason.

The large reason: every one of these technologies arrives at a workplace the same
way. Somebody buys it, and then somebody has to make it work with the systems
that are already there, which nobody designed with it in mind. **The interesting
question is never what the technology is. It is what it has to be bolted onto.**

---

## The list, and what each one actually is

These are the technologies the competency names. For each one: what it is in a
sentence, where it shows up, and the integration problem it brings with it.

### Large language models

**What:** a neural network that produces text one token at a time, fitted to an
enormous amount of writing.
**Where:** drafting, summarising, classifying, answering questions about
documents.
**The integration problem:** the output is prose, and prose is not a data type.
Something has to turn it into a shape your program can rely on, and something has
to decide what happens when it cannot. That something is the model service in
this course.

### Machine learning

**What:** the broader family. Any system whose behaviour was fitted to data
rather than written by a person. Language models are one branch.
**Where:** fraud flags, recommendations, predictive maintenance, quality
inspection on a production line, anything where showing the pattern
is more practical than stating it.
**The integration problem:** it needs data, and the data lives in systems that
were built for something else. Module 4 is about that.

### Artificial intelligence

**What:** the umbrella term, and the one to be careful with. It covers everything
above and a long history of systems that were not fitted to data at all.
**Where:** on every product page, whether or not there is any machine learning
in the product.
**The integration problem:** the word is a marketing term as often as a technical
one. When somebody says a product has AI in it, the useful follow-up is: what
does it do that a rule could not.

### Internet of Things

**What:** ordinary physical objects with a network connection and a sensor or a
switch: thermostats, door sensors, energy meters, equipment monitors.
**Where:** buildings, farms, factories, delivery vehicles.
**The integration problem:** a great many small devices, on a network built for a
smaller number of computers, most of them unable to run security updates. A device
with a five-year life and no patch path is a standing risk.

### SMART devices

**What:** the consumer end of the same idea, with a screen or a voice interface:
phones, watches, speakers, displays, appliances.
**Where:** everywhere, including the pockets of everyone in this room.
**The integration problem:** they are personal devices doing organisational work,
and the data crosses that line constantly.

### BYOD, bring your own device

**What:** the policy of letting people use their own hardware for work or school.
**Where:** most workplaces, and most schools.
**The integration problem:** it is a policy problem wearing a technology costume.
Who may install what, what the organisation may see, what happens when somebody
leaves, and what happens when the device is lost. Module 3 returns to it.

### Services virtualization

**What:** running a service as software on shared hardware rather than on a
machine dedicated to it. Includes virtual machines and containers.
**Where:** nearly all server work, and the reason cloud services exist.
**The integration problem:** the thing you are running now has no fixed address
and no fixed machine, so anything that assumed it did has to be rebuilt.

### Mixed reality

**What:** displays that put computer-generated content into the space around you,
including augmented and virtual reality.
**Where:** training simulations, maintenance guidance, design review, surgery
planning, retail.
**The integration problem:** it needs a live feed from the systems that hold the
real information. A headset showing the wrong torque spec is worse than a piece
of paper showing the right one.

### Additive manufacturing

**What:** building an object by adding material in layers rather than cutting it
away. The general name for what most people call 3D printing.
**Where:** prototyping, spare parts, dental and medical devices, tooling.
**The integration problem:** the digital file is now the part. Version control,
access control, and intellectual property questions that used to apply to
drawings now apply to something you can hold.

---

## Worked example 1: the same building, four technologies

Walk your own building and find one of each. Do not take this list on faith. Go
and look, and if a category has nothing in it, that is a finding worth writing
down.

| Technology | What to look for |
|---|---|
| Internet of Things | anything with a sensor reporting somewhere: door contacts, thermostats, energy meters, equipment monitors |
| additive manufacturing | a 3D printer, and the question of who owns the files queued on it |
| services virtualization | ask whether the systems you use run on their own machines or shared ones |
| BYOD | the phone in your pocket, and the written rule about what it may connect to |

**The exercise is the integration question, not the spotting.** For each one you
find, write the sentence: this had to be connected to _______, which was built
before it existed.

---

## Worked example 2: where a language model is the wrong tool

This is the part of the lesson people skip, and it is the part employers care
about.

| Problem | Right tool | Why not a language model |
|---|---|---|
| add up a column of numbers | arithmetic in your program | it produces likely text, and a likely number is not a correct number |
| decide who may open a door | a rule and an access list | the decision has to be auditable and identical every time |
| find every ticket containing the word wifi | a search | search is exact, instant, and free |
| compute a student's grade | the gradebook formula | the formula is the policy, and it must be readable by a parent |
| summarise 200 open tickets into themes | a language model | no rule states what a theme is, and the output is for a person to read |

The pattern in the last row: a language model earns its place when the task is
fuzzy, the input is language, and a person is going to read the output and can
catch a mistake. It loses its place the moment the answer has to be exact,
identical every time, or defensible to somebody who was not in the room.

---

## Worked example 3: the marketplace question, honestly

2.4.1 asks you to identify emerging technologies applicable to the marketplace.
The temptation is to answer with whatever is loudest. Here is a better method,
and it is four questions:

1. **What does it do that the existing thing could not?** If the answer is
   "nothing, but faster", that is still an answer, and it is often the true one.
2. **What does it have to be connected to?** Everything real connects to
   something older.
3. **Who carries the cost when it is wrong?** Not the vendor.
4. **What is the failure mode?** Not whether it fails. What it looks like when
   it does.

A technology you can answer all four about is one you can actually talk about in
an interview. A technology you can only describe is one you have read about.

---

## The wrong version, and why it is tempting

> "Emerging technologies are transforming every industry and will change the way
> we all work and live."

Every word of that is defensible and the sentence carries no information. It
names no technology, no industry, no change, and nothing that could turn out to
be false. You could have written it in any year of the last forty.

It is tempting because it sounds like a conclusion, and because it is exactly
what a language model produces when you ask it about emerging technology. That is
not a coincidence: it is the most likely continuation, and the most likely
continuation of a vague question is a vague answer.

You will meet this sentence again on Friday, in Gate 2, planted inside something
longer.

### Write this down

> A sentence that could not be wrong is not a claim. Ask what evidence would
> change it. If there is none, it is decoration.

---

## Vocabulary

| Term | What it means |
|---|---|
| **emerging technology** | a technology new enough that most organisations have not decided how to use it |
| **Internet of Things** | ordinary objects with network connections and sensors |
| **SMART device** | a consumer device with a screen or voice interface and a network connection |
| **BYOD** | bring your own device: using personal hardware for organisational work |
| **virtualization** | running a service as software on shared hardware |
| **container** | a lightweight package holding a service and what it needs to run |
| **mixed reality** | displays that place computer-generated content in the space around you |
| **additive manufacturing** | building an object by adding material in layers |
| **legacy system** | the system that was already there, which the new thing has to work with |

---

## Self-check

**1.** A vendor says their scheduling product "uses AI". Write the one question
you ask next, and say what a good answer and a bad answer each sound like.

**2.** Name one integration problem shared by the Internet of Things and BYOD,
and say why it is the same problem.

**3.** A team wants a language model to calculate shipping costs from a rate
table. Say why that is the wrong tool and what you would use instead.

### Answers

**1.** "What does it do that a rule could not?" A good answer names a specific
fuzzy task, such as reading free-text requests and grouping them. A bad answer
repeats the word AI, or describes something a lookup table has done for thirty
years, which is a sign the word is on the box rather than in the product.

**2.** Both put devices the organisation does not fully control onto a network the
organisation is responsible for. It is the same problem because the risk comes
from the ownership boundary, not from the hardware: somebody else decides when
the device is updated, what runs on it, and where it goes at the end of the day.

**3.** A rate table is exact, and the answer has to be identical every time and
defensible to a customer. A language model produces likely text, so it can
produce a plausible wrong number with no warning, and two identical requests can
differ. Use a lookup against the table in your own code. If somebody wants
natural language on the front, use the model to work out what was being asked and
then do the arithmetic in code.
