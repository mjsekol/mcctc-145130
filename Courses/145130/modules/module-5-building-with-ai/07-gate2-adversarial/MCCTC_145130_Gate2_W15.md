# Gate 2: Adversarial Review · Week 15
## 145130 Applications of AI · Module 5 · Week 15, Friday · Build 1

**40 minutes.** Individual. Silent. You may and should build and run the code.
**You may not ask a model whether it is correct, because a model is what is being
reviewed.**

The program is `gate2-w15-files/TrackSide/`, a C# console application targeting
`net8.0`. It comes with a stand-in service, `practice_service.py`, a note file,
`practice_notes.json`, and a one-note file, `one_note.json`, in the folder above
it. Copy the whole `gate2-w15-files` folder.

---

## What you are looking at

The cross country coach writes a note after every practice. Somebody handed an AI
assistant the requirements in Part A and got `TrackSide`. It builds with no
warnings. It has XML documentation comments, a failure kind for every case, and a
message for each one. It is the most professional-looking program in this module.

**Five defects, one in each category:** Correctness, Security, Readability,
Performance, Requirements Fit.

**Plus one item that is not a defect.** Item 6 is a design decision with a real
argument on each side. You are scored on your reasoning, not on which side you
pick.

**One of the requirements is fully met.** Check rather than assume.

---

## PART A: The requirements

> Write `TrackSide`, a console program for the cross country coach. It reads
> practice notes from a JSON file and, for each one, asks the model service to
> summarize it and classify it. It must:
>
> 1. Take the service URL **from the environment, never from the source**. Store
>    no credential anywhere, because a local model needs none.
> 2. **For every answer, say whether it came from the model or from the service's
>    fallback.**
> 3. Report the four service failures separately, each with what to do about it:
>    the service is not running, it did not answer in time, it answered with an
>    error status, it answered with something that is not the envelope.
> 4. **Wait long enough that the service's own retry finishes before this program
>    gives up.**
> 5. **Skip a note that is empty after trimming**, and say it was skipped.

---

## PART B: Running it

Two terminals, in the `gate2-w15-files` folder.

```
python practice_service.py --port 5157
dotnet build TrackSide/TrackSide.csproj
dotnet run --project TrackSide -- health
dotnet run --project TrackSide -- review
```

The stand-in service has five modes. **Run the same command in two of them and
compare the output line by line.**

```
python practice_service.py --port 5157 --mode model
python practice_service.py --port 5157 --mode fallback
python practice_service.py --port 5157 --mode garbage
python practice_service.py --port 5157 --mode error
python practice_service.py --port 5157 --mode slow --delay 8
```

**Use `one_note.json` with slow mode**, or you will wait a long time:

```
dotnet run --project TrackSide -- review --file one_note.json
```

**Time that run.** The number is the finding.

**Also stop the service entirely and run the program**, and separately point it
somewhere that is not the service.

---

## What to submit

For each defect: **line number**, **which of the five dimensions**, **what goes
wrong for a real person**, and **the fix**.

Then item 6, the design decision, with the strongest argument on each side and
your own position.

Then one final entry: **what I was unsure about**, naming something specific. That
entry is scored, and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 10:** run `review` in `model` mode and in `fallback` mode and put the two
  outputs side by side. In one of those runs the model was not used at all. Can
  you tell which from the output?
- **Next 10:** run `review --file one_note.json` against the service in slow mode
  with a delay of 8. **Time it with a clock.** Then read Part A requirement 4, and
  then read the comment above the timeout.
- **Next 10:** read Part A one requirement at a time and point at the line that
  meets it. One of the five is fully met. Note which, and move on.
- **Rest:** look at the note file. One of the four notes has nothing in it. Find
  what the program does with it. Then read every method name and ask whether it
  does what it says.

---

## Scoring

Five defects, one point each. Item 6 is one point, scored on reasoning. The
unsure-about entry is one point. Seven points.

**The security defect is double-penalized.** Missing it costs two points rather
than one. Your instructor states this before you start.

**Five of seven is a strong score.**
