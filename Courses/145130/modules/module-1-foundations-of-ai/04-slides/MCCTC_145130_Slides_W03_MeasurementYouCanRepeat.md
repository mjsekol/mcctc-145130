# A Measurement Nobody Can Repeat
---
## Slide 1: Mine was faster than Diego's
- One run each
- No prompts recorded
- No warm-up mentioned
- Conclusion: my machine is better for AI
Speaker notes: This sentence is going to be written in this room today and it might even be true. The problem is that nobody can tell, including the person who wrote it, and in two weeks somebody buys hardware because of it. Today is about the difference between a number and a comparison.
Image: Two laptops side by side with a single stopwatch between them.
---
## Slide 2: Seven things that are the method
- The exact prompts, and the repeat count
- Whether a warm-up was thrown away
- Streaming or not
- How tokens were counted
- What else the machine was doing
Speaker notes: Miss any one of these and your number is still a number. It is no longer a comparison. And the last one is the one nobody writes down: a video call in another window is part of your measurement whether you recorded it or not.
Image: A method checklist with several rows unticked.
---
## Slide 3: A comparison the program refuses
```
  These two runs cannot be compared.
    different repeat counts: 3 against 5. A median of three and a
    median of ten are not the same kind of number.

  Agree on a method, run again, and come back.
```
Speaker notes: That refusal is the feature, not an inconvenience. Those two runs were on the same machine against the same server, so the difference between their numbers is pure method. A program that printed the table anyway would have handed you a difference and invited you to explain it in terms of hardware.
Image: None. This slide is code.
---
## Slide 4: A comparison it allows, with warnings
```
  warning: tokens counted differently: server_counter vs character_estimate
  warning: one run streamed and the other did not
  warning: different models: streaming-stub against llama3.2

  p1_short   1335.7 ms   15.0 ms   1320.7 ms faster
```
Speaker notes: The table prints because the prompts and repeats match. Three warnings sit above it and any one of them makes that difference a sentence about two servers rather than two machines. Both of those runs were on the same computer. A reader who skips the warnings walks away believing one machine is eighty nine times faster.
Image: None. This slide is code.
---
## Slide 5: Refuse or warn, and why the difference
- Refuse when nothing survives
- Warn when something still holds
- Repeat counts ruin everything
- Token sources leave the timings fine
Speaker notes: This is a design decision you will make in your own programs. Different repeat counts make every summary number incomparable, so there is nothing worth printing. Different token counting ruins the token figures and leaves the timings perfectly good, so print what holds and warn about what does not.
Image: Two gates, one closed and one open with a caution sign.
---
## Slide 6: The comparison that actually works
```
  bench-a  40 tokens/sec configured   ->  39.3 measured, ttft 318 ms
  bench-b  25 tokens/sec configured   ->  24.7 measured, ttft 713 ms
```
Speaker notes: Same method, same machine, two stand-in servers set to different rates. Both measurements within two percent and the ratio between them is right. What it still cannot tell you is anything about a model, because neither server is one, and your report has to say that in those words.
Image: None. This slide is code.
---
## Slide 7: One run is not a measurement
- bench.py prints the spread
- Widest gap: 8.0 ms on medians of 1330
- Under one percent, so they agree
- Six hundred would be a different story
Speaker notes: Report the spread next to the median, always. A median with no spread beside it hides exactly the information a reader needs in order to decide whether to believe it. If your three repeats disagree by half a second, the median is a confident summary of a mess.
Image: Three dots close together, then three dots far apart, same median.
---
## Slide 8: Why median and not average
- Three runs: 1.3, 1.3, and 4.1 seconds
- The average is 2.2
- No run took 2.2 seconds
- The median is 1.3, which one did
Speaker notes: One slow run drags an average somewhere no run actually was. The median is what a typical run cost, and the four point one still shows up in the spread line, where it belongs as a question to investigate rather than as a number smeared into your headline.
Image: Three timing bars with an average line sitting where no bar is.
---
## Slide 9: Before you write the word faster
- Name one thing that differed
- Other than the hardware
- There is always at least one
- The program asks you this
Speaker notes: Compare machines prints that prompt at the bottom of every comparison, on purpose. The pull toward a clean conclusion is strongest exactly when the numbers are new, and this is the thirty seconds that stops you. If you genuinely cannot name one, you have not read the method fields in both saved runs.
Image: A blank line in a report waiting for one sentence.
---
## Slide 10: What you are about to build
- Agree a method with a partner first
- Then both run it
- Then compare, and read the warnings
- Write the sentence about what differed
Speaker notes: Build one is the negotiation, and it comes before either of you runs anything: same prompts, same repeats, same warm-up, same token source. Build two is the run and the comparison. If the program refuses you, that is the lab working, and fixing it is the assignment rather than a setback.
Image: Two students agreeing a written method before touching a keyboard.
---
