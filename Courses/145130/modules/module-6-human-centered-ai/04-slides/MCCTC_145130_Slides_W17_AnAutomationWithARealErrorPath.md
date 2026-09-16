# An automation with a real error path
---
## Slide 1: Two runs. One reached a service. One reached nothing.
```
note sweep, run r0001, started 02:30:55
  8 notes, 8 labelled, digest at out\digest-r0001.md
  status  OK

note sweep, run r0001, started 02:30:57
  8 notes, 8 labelled, digest at out\digest-r0001.md
  status  OK
```
Speaker notes: These are two real runs from this machine, the same command both times. In between them I stopped the service with control C. One of these runs made eight HTTP calls. The other made none at all and every label came from matching words. Nothing in the output tells them apart, and neither run raised an exception.
Image: None. This slide is code.
---
## Slide 2: The two digest files are the same bytes
```
digest_with_service.md     sha256 735ad1bba01a4ecd...
digest_without_service.md  sha256 735ad1bba01a4ecd...
```
Speaker notes: It is worse than the last slide. The output files those two runs produced are not similar. They are identical, byte for byte, and I checked with a hash. There is nothing anywhere for a person to notice. This program is not broken. It does exactly what it was written to do, and it was written to count replies.
Image: None. This slide is code.
---
## Slide 3: An automation runs when nobody is watching
- A program you start is judged on whether it did the job
- Somebody is standing there
- A scheduled automation is judged on something else
- Whether it can tell the difference itself
Speaker notes: That single fact changes what working means. When you run something by hand, you are the check. Nobody is standing next to a seven a.m. scheduled job. So the automation has to be able to tell the difference between doing the job and not doing the job, and most first automations cannot.
Image: An empty room with a screen glowing and a clock reading seven.
---
## Slide 4: Every step declares what it expected
```
  [ok  ] collect    expected at least 1 note file, got 8
  [ok  ] freshness  expected source newer than the last run, got 1 s newer
  [FAIL] classify   expected 8 labelled, at least 1 from the service,
                    got 8 labelled, 0 from the service
  [ok  ] record     expected 1 row appended, got 1 row, status FAILED
  status  FAILED
```
Speaker notes: Same situation, different program. Read the classify line. It does not say error. It says what it wanted and what it got, and the gap between them is the message. Somebody who has never seen this program can read that line and know exactly what happened. That is the whole design.
Image: None. This slide is code.
---
## Slide 5: Three statuses, and they are not the same thing
- OK: every step got what it expected
- DEGRADED: the work got done, not the way it was meant to
- FAILED: a step did not get what it expected
- Exit codes 0, 1, 2. A scheduler reads those
Speaker notes: Three outcomes, and degraded is the one people leave out. It means the digest exists and is usable and every row is marked as coming from a rule instead of the service. Calling that OK hides it. Calling it FAILED wakes somebody at seven in the morning for something that produced a usable file.
Image: Three status chips in green, amber and accent red with exit codes under them.
---
## Slide 6: The three counts
```
1  results out, against inputs in
2  came from the real thing, against came from a stand-in
3  is the input newer than the last run
```
Speaker notes: Three questions. The first is the most general and it is the one to memorise, because a step produced fewer results than it had inputs is a rule you can apply to any step in any automation without knowing what it does. The second catches the run on slide one. The third is the one we are really here for.
Image: None. This slide is code.
---
## Slide 7: The error path that raises nothing
- The inbox has eight files. They all open
- Every label comes back. Nothing crashes
- And nothing in there has changed since yesterday
- Upstream did not deliver, and your digest is yesterday's
Speaker notes: Here is the failure this lab is built around. Every file opens, every label comes back, and nothing in the folder has changed since the last run. The export job did not run, or it ran and wrote nothing. Your program produces yesterday's digest with today's run number on it, which is worse than no digest, because somebody will act on it.
Image: A folder with unchanged timestamps next to a freshly written output file, accent red arrow between them.
---
## Slide 8: The incident file has four sections, always
```
What was expected, and what happened
What to check first
Who to ask
What happens if nobody does anything
```
Speaker notes: The incident file is the deliverable, not the printed line. Four sections and they are always these four. The last one is the one people leave out and it is the one that makes somebody act. An incident that says what breaks next week reads very differently from one that says something failed.
Image: None. This slide is code.
---
## Slide 9: The try block is not an error path
- Go back to slide one and name the exception
- There is not one
- The connection was refused, caught, and fallen back from
- An exception is one way to fail, not the definition of failing
Speaker notes: Somebody will wrap the whole thing in try and except and call it done. Go back to slide one and ask what exception would have been raised. None. The connection was refused, the code caught it, fell back to a keyword rule, produced eight labels and returned. Every failure that matters here raises nothing at all.
Image: A try and except block greyed out with a small accent red cross beside it.
---
## Slide 10: What you are about to build
- Produce the lie on purpose, four ways, and capture each one
- Add a freshness step that fails on the second run
- Put an expectation on every step
- Write the incident file, four sections
Speaker notes: Build one is producing the failure four different ways with the stub, on port five one five eight, and capturing each. Build two is the freshness step and the expectations. The checker tells you how many of six checks you pass, and you will start at two. n8n would be five nodes and the same four rules, and it is not installed here.
Image: Two terminals side by side, one running a stub and one running a sweep that reports FAILED.
