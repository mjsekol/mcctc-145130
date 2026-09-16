# Week 14 Self-Directed Build Guide
## 145130 Applications of AI · Module 5 · the competition week

**Print this. Keep it on your desk all week.**

Mr. Sekol may be supervising BPA Regional competitors in the building every day
this week. Some of you are competing. The substitute in the room is not a
programmer and will not answer questions about code, and that is on purpose.

This guide tells you what to do each day, in order. Everything you need to learn
this week is in three lecture notes you were given on Thursday of Week 13. Nobody
is going to teach you anything out loud.

**That is not a punishment and it is not a gap.** Week 13 was the week with the
hard ideas in it, and it had a teacher. This week is build work, and build work
is what you do when nobody is watching.

---

## The rule when you are stuck

In this order, every time. Do not skip a step.

1. **Read the lecture note for today.** The answer is usually in it.
2. **Read the error message out loud.** All of it, to the end.
3. **Ask your teammate.**
4. **Ask another team.** They are allowed to help you and you are allowed to help
   them.
5. **Write the question on the STUCK board** and in your team's question log.
6. **Make your best assumption, write it down in the decision log, and keep
   going.**

Step 6 is the one people will not do. Do it. A team that stops for four periods
waiting for an answer has lost the week. A team that writes down an assumption and
keeps moving has a decision to defend, which is the assignment.

---

## The ports, every time

| What | Port | Started with |
|---|---|---|
| your model server, or the stub | **11535** | `python stub_model_server.py --port 11535` |
| your model service | **5157** | whatever environment variable your own service reads |
| a real model, if one exists on this machine | 11434 | not yours to start |

**Type the port every time, even when it feels unnecessary.** A server that
cannot get the port it asked for stops without much noise. If you left the port
out, the next program finds whatever else is there and talks to that instead, and
you get answers that look completely normal. You will meet that on Wednesday and
it will cost you twenty minutes then instead of a period now.

**After you start any server, read the line it prints.** If it does not print
that line, it did not start.

---

## Every day, whatever else happens

- [ ] Fill in today's row of your team's **stand-up log**: finished, working on,
      blocked by. Written, not spoken, this week.
- [ ] Do the Gate 1 rep in the first ten minutes of Build 1, on paper, no devices,
      no AI tool.
- [ ] **Commit and push before you leave.** Every period. Whatever state it is in.
- [ ] Write the exit ticket.

**If your role owner is at BPA today, the backup does that job.** That was named
in your implementation plan. Nobody waits.

**If you were at BPA and you are back**, read your team's stand-up log from every
day you missed, top to bottom, before you touch a file. Then take your tasks back
from your backup in writing, in the log.

---

## Monday · Milestone M3 · your service answers

**Read first, 15 minutes.** `Notes_FourFailuresFourMessages`, the section headed
"The concept in plain language", then worked example 1. Answer self-check
question 1 in writing and keep the paper.

### Build 1, after the rep, 40 minutes

Your service answers one good request with your envelope.

1. Start the stub with an explicit port. Read the line it prints.
2. Start your service with the model URL and the service port set. Read its lines.
3. Send it your request shape. You can use `contract_probe.py` from last week's
   lab, or anything else that sends JSON over HTTP.
4. Get your six fields back with `source` set to `model`.

**Done when:** one request in, your envelope out, `source` of `model`.

### Build 2, 55 minutes

The other two outcomes.

5. Stop the model server. Send the same request. You should get `source` of
   `fallback`, `ok` still true, and an `error` that says why.
6. Send a request that breaks your own input rules: an empty field, or something
   over your own cap. You should get `source` of `none`, `ok` false, and
   `elapsed_ms` of 0.
7. Capture all three into `evidence/day1.txt` and commit it.

**Done when:** three runs, three different `source` values, committed.

### If you finish early

Read tomorrow's note. Then make your service produce a fourth outcome: a model
that answers with something your parser cannot use.

### We finished everything

Write one paragraph in your decision log: what would break first if a hundred
people used your service at once, and how you know.

---

## Tuesday · Milestone M4 begins · who gives up first

**Read first, 15 minutes.** `Notes_WhoGivesUpFirst`. **Do worked example 1 on
paper before you read worked example 2.** Three settings, two answers each. Then
read example 2 and mark your own.

### Build 1, after the rep, 40 minutes

The two numbers.

1. Find your service's model timeout and its retry count.
2. Multiply the timeout by one more than the retries. That is your service's worst
   case.
3. Find your application's timeout. Set it above that number.
4. Write the arithmetic in a comment next to the value, in both programs. Not the
   number. The arithmetic.
5. Add the health comparison from worked example 3: your client asks the service
   for both numbers and warns you when yours is the smaller one.
6. Prove the warning works by setting your timeout low on purpose once, seeing the
   warning, and setting it back.

**Done when:** both numbers are in both programs with the arithmetic in a comment,
and your health command warns correctly.

### Build 2, 55 minutes

Your C# application calls your service.

7. Send your request over HTTP.
8. Read the envelope into typed objects.
9. Print the result, and say whether it came from the model or from the fallback.

**Done when:** `dotnet build` succeeds targeting `net8.0`, and the program prints
a visibly different line for a fallback than for a model answer.

**If `dotnet new sln` gives you a `.slnx` file**, use
`dotnet new sln --format sln` instead. Some lab machines have an older SDK that
cannot open the newer format.

### If you finish early

Make your model slow on purpose and watch your own program either wait properly
or give up first. Capture whichever happens.

### We finished everything

Write the decision log entry for your timeout. Why that number, what it is
arithmetic on, and what you would change it to if the service moved to another
machine.

---

## Wednesday · Lab M05-03 · the broken integration

**Read first, 15 minutes.** `Notes_TroubleshootingAnIntegration`, the four
methodologies and the Choosing table, then worked example 3, which is the shape of
a log entry. **Do not read worked example 2 today.** It gives two of the faults
away.

### Build 1, after the rep, 40 minutes

Lab M05-03, scenarios 0 through 3. The lab handout has the steps.

1. **Scenario 0 first**, and save the whole output to a file. It is your baseline
   and you will compare against it five times.
2. Open your troubleshooting log **before** you start diagnosing anything.
3. Faults A, B, and C. Symptom first, then a named methodology, then one change.

**Done when:** the baseline is saved and three evidence rows are filled from real
runs.

### Build 2, 55 minutes

4. Faults D and E. Two of the five faults report the same symptom as each other,
   and two of them report the same `error.kind`. The lab tells you where to look.
5. Write all five entries, plus a sixth about the bench program itself.

**Done when:** six evidence rows, five entries each naming a methodology, and
scenarios 2, 4, and 5 given three different causes.

### If you finish early

Invent a sixth fault in `scenario.py` and hand it to another team without telling
them what you did.

### We finished everything

Take one entry from your own build this week and rewrite it in the five part
shape. You need three of those by Friday.

---

## Thursday · Gate 2 W14, then M4 finished

**Build 1 is Gate 2.** Silent, individual, 40 minutes, no AI tool, because an AI
is what you are reviewing. The packet has everything in it, including the program
printed out and two real captured runs, so you can do the whole thing on paper if
you need to.

### Build 2, 55 minutes

Milestone M4 finished. Your application reports the four wire failures
separately, each with a different message that says what to do.

Produce all four on purpose and capture them into `evidence/day4.txt`:

1. **Service stopped.** Stop it and run your program.
2. **Wrong port.** Point your program at your model server instead of your
   service.
3. **Service slow.** Start your model in slow mode and set your client's timeout
   below your service's worst case, on purpose, once.
4. **Not your envelope.** Point your program at anything that answers HTTP and is
   not your service.

**Done when:** four captures, four different messages, each naming what to do.

### If you finish early

Start the Week 15 documentation set. The implementation plan is Monday's work and
you have lived through the thing it describes.

### We finished everything

Hand your program and nothing else to another team and ask them to break it.
Write down what they did.

---

## Friday · Build, log, commit

No new content and nothing to read.

### Build 1, after the rep, 40 minutes

**Three real log entries, from your own build this week.** Not from the lab. Five
parts each, each naming a methodology.

If you genuinely hit fewer than three problems this week, write up the ones you
had and say so in the file. **Do not invent entries.** A log of problems you
imagined is worth nothing and it is obvious from the outside.

### Build 2, 55 minutes

Catch up on M3 and M4 if either is short.

**Returning competitors take their roles back in writing**, in the stand-up log.
Say which tasks you are taking and what you are leaving with your backup.

### We finished everything

Read another team's I/O specification and try to write a client class against it
on paper. Then tell them what you could not work out.

---

## What gets graded from this week

| What | Where it goes |
|---|---|
| Milestone M3 and M4 | Projects |
| Lab M05-03 and its log | Lab & Practice |
| Gate 2 W14 | Written & Documentation |
| Troubleshooting log, three entries | Written & Documentation |
| Gate 1 reps | Lab & Practice |
| Stand-up log, five rows | Process, inside the project rubric |
| BPA competition work | BPA / Credential / Capstone |

**A week with no commits in it is a week with no grade in it**, whatever is on
your screen on Friday.
