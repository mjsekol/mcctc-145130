# Where it is worth applying, and an estimate you can defend
## 145130 Applications of AI · Module 6 · Week 17, Wednesday

**Slides for this lesson:**
[outline](../04-slides/MCCTC_145130_Slides_W17_WhereItIsWorthApplyingAI.md)

**There is no exported deck for this outline yet.** Generate it from the
repository root with:

```
node tools/gamma.js Courses/145130/modules/module-6-human-centered-ai/04-slides/MCCTC_145130_Slides_W17_WhereItIsWorthApplyingAI.md --export pptx
```

**Competencies 2.14.5**, identify and analyze opportunities to apply AI across
business, industry, and society, **2.4.3**, research the value of emerging
technologies on the marketplace, and **7.1.9**, identify major applications for
interactive media.

---

## Why this exists

You are going to be asked, in an interview or by a manager, whether some idea is
worth doing. The honest answer has arithmetic in it.

**Almost everybody answers this question with a number they cannot defend.** They
say the market is growing, or adoption is accelerating, or a vendor claims a 40
percent efficiency gain. None of those numbers came from anything the speaker
checked, and none of them survives one follow-up question.

This lesson teaches the smaller, harder, more useful thing: **how long does the
task take, how often does it happen, and what has to be true for the saving to be
real.**

---

## The one idea

**Value you can defend is time saved per task, times how often the task happens,
with the assumption written underneath.**

```
minutes per task  x  times per year  =  minutes per year
                                        ------------------
                                        and then the assumption
```

**The assumption is not a footnote.** It is the part that can be wrong, and
stating it is what turns a number into an estimate rather than a claim.

---

## Finding the workflow: three signals

Not everything is worth automating. Three signals, and a workflow needs all three.

| Signal | Test |
|---|---|
| **Repeated** | It happens on a schedule or on an event, not once |
| **Rule-shaped or text-shaped** | Somebody could describe how they decide, or the work is reading and writing words |
| **Somebody is doing it by hand now** | There is a person and a time you can measure |

**The third one is the filter that does the most work.** If nobody is doing it,
there is no time to save and no person to ask. "Nobody does this and they should"
is a proposal, not an opportunity, and it needs a different argument.

### Where to look

**Pick an industry somebody you know has actually been inside.** A restaurant
kitchen. A garage. A warehouse. A vet's office. A salon. A farm. A church office.
A youth sports league.

**Not a technology company.** You do not know what happens inside one, and neither
does anybody you can ask, so every number you produce will be invented.

---

## Worked example 1 · one workflow, costed

A vet's office. The workflow is the morning intake summary.

```
The workflow:  the front desk reads every appointment note left by the
               overnight service and writes a one-line summary per animal
               on the board before the first appointment.

Who does it:   one person at the front desk.
How long:      18 minutes. Timed once, on one morning, by me, with a
               stopwatch, while she did it.
How often:     every weekday the practice is open. 250 days.

18 x 250 = 4500 minutes a year = 75 hours a year.
```

**The assumption, and it is the whole estimate:**

> This saving is real only if nobody re-reads the notes to check the summary. If
> the front desk reads every note anyway to make sure the summary is right, the
> saving is the writing time and not the reading time, which is about four minutes
> rather than eighteen, and the number becomes 16 hours a year.

**Both numbers are in the report.** 75 hours if the output is trusted. 16 hours if
every row is checked. **Which one is real depends on how good the output is**, and
you do not know that yet, which is why the estimate has two numbers in it.

---

## Worked example 2 · the same workflow, done badly

Here is what the first draft of this looks like, every time.

> The veterinary intake process is highly inefficient and represents a significant
> opportunity for AI automation. The veterinary software market is growing at 19
> percent annually, and practices that adopt AI tools report efficiency gains of up
> to 40 percent. Automating intake could save the practice roughly 15 hours a week,
> representing substantial cost savings.

**Four sentences, and three of them are invented.**

- **"Growing at 19 percent annually."** Where did 19 come from. Nobody in the room
  can check it and it has a decimal-looking specificity that makes it sound
  researched.
- **"Efficiency gains of up to 40 percent."** A vendor claim, repeated. "Up to" is
  doing enormous work and means "in the best case we found."
- **"Roughly 15 hours a week."** No arithmetic. 15 hours a week is 3 hours a day
  for the whole intake process, which is either a very large practice or a number
  somebody felt.
- **"Substantial cost savings."** Cost needs an hourly rate. You do not have one
  and you are not entitled to ask for one.

**The sentence that would have saved it:** "I did not find a figure I could verify
for how fast this market is growing, so I am not claiming one."

---

## Worked example 3 · what you will not claim

**Every opportunity analysis in this module has a required section titled "What I
did not measure."** It is worth marks and it is where most of the honesty lives.

```
What I did not measure

1  Quality. I did not test whether a model can write a usable one-line
   summary of a vet note. I am estimating the value of the task being
   done, not the value of it being done well.

2  The re-check. I do not know whether the front desk would trust the
   output. The whole estimate swings from 75 hours to 16 on that one
   question, and the way to find out is to build it and watch somebody
   use it for a week.

3  Set-up cost. Somebody has to build, run, and fix this. I did not
   estimate that, and if it takes 80 hours to build, the first year is
   a loss on the 16-hour version.

4  Whether the practice wants it. I timed one person on one morning. I
   did not ask anybody whether this is a problem they care about, and
   the thing that annoys them most might be something else entirely.
```

**Item 4 is the one professionals miss.** A saving nobody asked for is not a
saving, it is a project.

---

## Money, and why this module stops at hours

**Hours is a number you can defend. Money is a number you would be inventing.**

To get from 75 hours to a dollar figure you need an hourly cost for that person,
which means their pay, which is not yours to ask for and is not yours to guess.
Guessing it and then multiplying makes the final number look precise and makes it
wrong by whatever factor your guess was wrong by.

**In your analysis: hours per year, and stop.** If somebody wants dollars, you hand
them the hours and say that they have the rate.

**The honest exception:** if a cost is public and posted, you may use it and say
where it came from. A subscription price on a public page is a fact. A salary is
not.

---

## Where interactive media actually gets used

**Competency 7.1.9 is identifying the major applications for interactive media**,
and it is the same survey move as looking for AI opportunities: where is somebody
already spending time and attention.

The eight the outline names:

| Application | What it looks like | Where the AI opportunity usually is |
|---|---|---|
| **Sales and marketing** | Product configurators, interactive catalogues | Writing variations of copy, sorting inbound questions |
| **Interactive advertising** | Playable ads, quizzes, anything that responds | Generating variants, and this is also where the ethics get sharpest |
| **Education** | Simulations, interactive textbooks, practice systems | Generating practice items, and grading that a person checks |
| **Online learning** | Courses, tracked progress, adaptive paths | Summarising, transcribing, answering the same question the twentieth time |
| **Corporate training** | Compliance modules, onboarding, safety simulations | Turning a manual into questions, and translation |
| **Corporate communications** | Internal news, all-hands materials, intranets | Summarising long documents into what changed |
| **News** | Live data pages, interactive graphics, timelines | Sorting incoming tips, transcribing, and the place where fabrication is least acceptable |
| **Entertainment** | Games, streaming interfaces, interactive stories | Generated content, voices, and a live legal argument about both |

**Your three workflows might sit in one of those eight, or in none.** A vet's
morning intake is not interactive media, and saying so is a better answer than
forcing it. **Where your workflow does sit in one, say which and why**, because
that is the competency.

**The two rows worth arguing about are advertising and entertainment**, and the
argument is Module 3's. If you pick either, your analysis has to carry a paragraph
on who is affected and who did not consent, and you already have the framework for
writing it.

---

## The wrong version, and why it is tempting

The wrong version is not laziness. It is this:

> "I asked a model to research the market for this and it gave me the growth rate
> and three competitors."

**Why it is tempting:** it takes ninety seconds, the answer is fluent, it has
numbers in it, and it reads exactly like the market analysis section of a real
document. It also feels like research, because something that looked like research
happened.

**What it actually is:** the same failure you spent three weeks on in Module 2. A
number with no source, presented with confidence, in a shape that makes checking
feel unnecessary. **A market growth rate is a fabricated citation wearing a
different hat.**

**The rule for this module, with no exceptions:** no market size, no adoption rate,
no vendor claim, anywhere in the document. Not even attributed. If you cannot check
it, you do not write it.

**What you may write instead:** what you counted, who you asked, when you timed it,
and what you did not measure.

---

## Vocabulary

| Term | What it means here |
|---|---|
| **Workflow** | A repeated sequence somebody does, with a start and an end |
| **Opportunity** | A workflow where AI could change the time, the quality, or who does it |
| **Estimate** | A number with arithmetic and an assumption under it |
| **Claim** | A number with neither. Not the same thing |
| **Assumption** | The sentence that, if false, changes the number |
| **Market size** | The total value of a market. You will not be using this |
| **Adoption rate** | How fast people are taking something up. Same |
| **Vendor claim** | A number from the company selling the thing |
| **Interactive media** | Media a person acts on and that responds |

---

## Self-check

**1.** Somebody hands you this: "automating our scheduling would save about 10
hours a week." Write the three questions you ask, in order.

**2.** Your estimate is 120 hours a year. Your assumption is that nobody re-checks
the output. Name what you do next, in one sentence, and say why it is not "find a
better model."

**3.** Why does this module ban market growth figures even when a real article
contains one?

---

### Answers

**1.** In order:

1. **"How long does one of them take, and how do you know?"** Everything else
   depends on this and it is the one people have never measured.
2. **"How many are there a week?"** Two numbers, and now there is a
   multiplication.
3. **"Would anybody still have to check the output?"** This is the question that
   halves or zeroes most estimates, and it is the one nobody volunteers.

**The order matters.** Asking about checking first sounds like an attack. Asking
about the timing first is a normal question and it makes the third one normal too.

**2.** **You go and find out whether the output would be trusted**, by putting it
in front of the person who does the task and watching what they do with it.

**Why it is not "find a better model":** you do not yet know that the model is the
problem. The 120 hours evaporates if the person re-reads every row, and they might
re-read every row even when the output is perfect, because they are accountable
for it and reading is how they feel accountable. **That is a human problem and no
model fixes it.**

You already know how to find out. It is a usability session, and you ran five of
them last week.

**3.** **Because you cannot check it, and citing the article does not make it
checkable.**

An article's growth figure came from somewhere, usually a research firm's paid
report that neither you nor your reader can open. Repeating it moves the number one
step further from anybody who could verify it while making it look better sourced.

**There is a real counter-argument and it is worth stating.** Professionals cite
figures they have not personally verified all the time, and refusing to ever do so
makes some documents impossible to write. The honest version of that practice is to
name the source in the sentence, so a reader can weigh it: "a report from X, which
I have not read, is quoted as saying Y."

**This module bans it anyway**, for one reason: students here are being trained to
detect fabrication, and the fastest way to lose that habit is to be allowed to pass
along one unchecked number in a document that otherwise has arithmetic in it. **You
have something better available.** Your own multiplication, from a task you timed
yourself, is worth more in an interview than any market figure.
