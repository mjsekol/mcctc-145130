# Three Numbers Worth Measuring
---
## Slide 1: Our model runs at 42 tokens per second
- One number, no method
- Which prompt, how many runs
- Median, average, or best
- Was the warm-up counted
Speaker notes: You will read a sentence like this about once a week for the rest of your career. Without the method it is not a measurement, it is a number somebody typed, and you cannot use it for anything including comparing it against your own. By Friday you will be able to say exactly what a benchmark does and does not establish.
Image: A large confident number on a slide with nothing else on it.
---
## Slide 2: Three numbers, three different people
- Total latency, anyone waiting
- Time to first token, anyone watching it type
- Tokens per second, whoever bought the hardware
Speaker notes: These measure different things and different people care about each one. Two systems with identical total latency can feel completely different: one shows nothing for four seconds then the whole answer, the other shows a word after half a second. Same wait. Only one of them gets called fast.
Image: Three stopwatches, each starting and stopping at different points.
---
## Slide 3: The arithmetic everybody gets wrong
```
tokens_per_second = tokens / total_latency        WRONG
tokens_per_second = tokens / generation_time      RIGHT

generation_time = total_latency - time_to_first_token
```
Speaker notes: No tokens were produced during the wait before the first one. Dividing by total latency spreads the tokens over time the model spent doing something else and reports a rate it never ran at. This is the most common error in amateur benchmarks and it is on your exam.
Image: None. This slide is code.
---
## Slide 4: The error always goes one way
- The divisor is always too big
- So the number is always too low
- It never overstates a model
- It understates slow-starting ones most
Speaker notes: This is worth a second. A bug that is sometimes high and sometimes low gets noticed, because the numbers jump around. A bug that is always low looks like a consistent, slightly disappointing result, and nobody investigates a consistent result. Systematic errors hide better than random ones.
Image: An arrow pointing only downward from a true value.
---
## Slide 5: Do it both ways, with real numbers
```
  p1_short   median total 1335.7 ms   ttft 318.3 ms   tokens 40

  wrong:  40 / 1.3357 = 29.9 tokens/sec
  right:  40 / (1.3357 - 0.3183) = 40 / 1.0174 = 39.3 tokens/sec
```
Speaker notes: Same run, two answers, and a quarter of a difference between them. Now here is the part that makes this worth a whole period rather than a slide.
Image: None. This slide is code.
---
## Slide 6: We already knew the answer
- The server was a stand-in
- Started at 40 tokens, 25 ms each
- Its true rate is 40 per second
- The right method reported 39.3
Speaker notes: The server producing those numbers was not a model. It was a stand-in we started ourselves with the rate on the command line, so we knew the truth before we measured. The correct method landed within two percent. The wrong one was a quarter low. That is how anybody ever comes to trust an instrument: you point it at something whose size you already know.
Image: A ruler being checked against a known reference block.
---
## Slide 7: When a number cannot be known
```
note: this server does not stream, so time to first token and
tokens per second are not measurable here

  p1_short    15.0 ms    n/a    48.0    n/a   character_estimate
```
Speaker notes: Point the same program at the anchor stub and two columns say not applicable. The program had every chance to fill them. It could have divided by total latency and printed three thousand tokens per second. It refuses, and the note says why.
Image: None. This slide is code.
---
## Slide 8: The rule, written into the code
- When you cannot know a number, return None
- Never return a guess
- A gap is a fact about your method
- A guess is a lie with a decimal point
Speaker notes: That rule lives in three functions in measure dot py and it is the part of today's lab you write. It is also the sentence I want in your benchmark report. A reader can work with a gap. A reader cannot work with a number that looks exactly like the real ones and was invented.
Image: A report with a clearly marked blank field rather than a filled one.
---
## Slide 9: The token count is a measurement too
- server counter, best available
- stream chunks, good if one piece is one token
- character estimate, weak, and we print the assumption
Speaker notes: Look at the source column in every run. These three are not equally trustworthy, and the benchmark records which one it used for every single number. That is why compare machines refuses to compare a server counter against a character estimate: those are not two measurements of the same thing.
Image: Three labels with decreasing confidence bars.
---
## Slide 10: What you are about to build
- Three functions in measure.py
- check_measure.py has thirteen cases
- Every expected value worked out by hand
- Then point bench.py at a known rate
Speaker notes: Build one is median, generation time, and tokens per second, and the self check will not pass until the None cases are right. Build two starts the streaming stand-in at a rate you choose and confirms your benchmark reports it. If your number is a quarter low, you know exactly which line to look at.
Image: A test run showing thirteen passes.
---
