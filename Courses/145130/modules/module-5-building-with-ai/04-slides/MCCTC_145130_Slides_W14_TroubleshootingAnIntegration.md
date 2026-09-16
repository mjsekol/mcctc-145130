# Troubleshooting an Integration With a Named Method
---
## Slide 1: Two students, the same complaint, two different faults
- "It is fast, and every summary is one sentence from the ticket"
- Word for word the same report
- Two completely different causes
- Two fixes that have nothing to do with each other
Speaker notes: Two people report the same thing in the same words. It is fast and every summary is one sentence lifted straight out of the ticket. Same sentence, two different faults, and the fixes have nothing in common. A symptom does not identify a fault, and today is about how you get from one to the other without guessing.
Image: Two identical speech bubbles pointing at two different layers of the stack, in navy and accent red.
---
## Slide 2: The six steps still work. Step two got harder.
- Reproduce, one theory, test it, change one thing, verify, document
- An integration has three programs in it
- The bug is rarely in the one you are looking at
- Step two now has three places to point at
Speaker notes: You learned six steps last year for finding a bug in one program. All six still apply. What changed is step two. An integration has three programs in it, the bug is almost never in the one you are looking at, and the symptom almost never points at the layer that caused it. So forming one theory now means choosing where to look first, and that is what a methodology is.
Image: The six-step loop with step two enlarged and three arrows leaving it toward three layers.
---
## Slide 3: Four methods. Name one before you start.
```
top down               person's layer first, then down
bottom up              machine's layer first, then up
follow the path        one request, every boundary it crosses
spot the differences   a working case against a failing one
```
Speaker notes: Four methods from the Ohio competency list. You name one, out loud, before you start, and you write it in the log. Saying I looked at it is not a methodology and it is not worth points. Top down is the default when all you have is a complaint. Bottom up is for when something underneath you changed.
Image: None. This slide is code.
---
## Slide 4: Which one, given what you have
```
a complaint and nothing else          top down
something in the environment changed  bottom up
an answer arrives and is wrong        follow the path
a case that works and one that does not   spot the differences
every case fails the same way         spot the differences, on what they share
```
Speaker notes: Read that last row twice. When five different inputs give you one identical output, stop looking at what differs between them and look at what they have in common. That is a real technique and it catches people out, because the instinct is always to compare the failing cases against each other.
Image: None. This slide is code.
---
## Slide 5: Three tools, in this order
- health: is the service up, can it see a model
- contract_probe: what is actually in the envelope
- the service console: every request it answered
Speaker notes: Three ways to see inside this system and they answer different questions. Health takes thirty seconds and tells you which half to stop looking at. The probe prints error dot kind, which your own program probably does not. And the service console tells you the thing neither of the others can: whether your request arrived at all.
Image: Three tool cards in a row, each with the one question it answers in accent blue underneath.
---
## Slide 6: One field apart
```
Fault B   model_reachable  true
          error  {"kind": "task_validation_failed", ...}

Fault D   model_reachable  true
          error  {"kind": "model_http_error", ...}
```
Speaker notes: Same complaint, same health answer, and the envelope is one field apart. Validation failed means the model is answering and the answers do not fit your task, so somebody looks at the prompt template or the rule. HTTP error means the model server is returning an error status, so the model server needs attention and your code is fine. Nothing else separates them.
Image: None. This slide is code.
---
## Slide 7: Keep a baseline, or spot the differences has nothing to spot
- Scenario 0 in today's lab is a healthy run
- Capture it first, before you look at any fault
- The stub summary prefix is the tell
- Without a known-good run you are comparing to memory
Speaker notes: Today's lab has a scenario zero and it is not broken. Run it first and capture what a working run looks like, because spot the differences needs something to compare against and your memory of what it used to look like is not good enough. The healthy run says Stub summary at the front of every summary. That prefix is the tell.
Image: Two terminal captures side by side, the healthy one with a phrase highlighted that is missing from the other.
---
## Slide 8: An entry that is worth reading, and one that is not
```
Methodology.  Spot the differences. Five inputs, one output, so the
              suspect is what they share. Theory one: the parser.
              Tested by calling parse directly. Dead in 30 seconds.
              Theory two: wrong port. netstat showed another process.

Methodology.  We tried a few things until it worked.
```
Speaker notes: The first one names the method, records a theory that was wrong and how it died, and that is the part people leave out and the part that saves the next reader an hour. The second one tells nobody anything, including the person who wrote it, three weeks later when the same problem comes back.
Image: None. This slide is code.
---
## Slide 9: Four changes at once teaches you nothing
- Something fixed it and nobody knows which
- The problem comes back and the log is worthless
- Undo the three you think were unrelated, one at a time
- Ten minutes turns luck into knowledge
Speaker notes: This is the most common failure in a troubleshooting log and it does not look like a failure, because the problem went away. You changed four things and something fixed it. You cannot prevent it, explain it, or recognise it next time. Undo the three you believe were unrelated, one at a time. Ten minutes, and a lucky escape becomes something you know.
Image: Four change labels with three of them being lifted away one at a time, navy and accent blue.
---
## Slide 10: What you are about to build
- Lab M05-03, one healthy run and four faults
- Name your methodology before you start each one
- Open the log before you start fixing
- Change one thing, verify with a command
Speaker notes: Today's lab gives you a healthy baseline and four faults, and two of the four report exactly the same symptom on purpose. You write one log entry for each fault, with a named method, the theory that was wrong, the single thing you changed, and the command that proves it. Open the log first, while you are still looking at the symptom.
Image: A split screen, a scenario running on the left and a log entry being typed on the right.
