# SQ-10 · API First Contact
## 145060 Programming · Unlocks Unit 7, Week 16

**Time:** two blocks. **Difficulty:** ★★
**Competencies:** 5.5.4 (call other programs), 5.5.7 (read inputs from an API),
9.3.3 (secure coding, error handling).

---

## The quest

Consume an API, read the reply, and print something a person would actually want. Then
break it on purpose and make it fail gracefully.

This bundle ships its own practice API, **Sky Watch**, that runs on your own computer, so
you can do the whole quest with no internet and no account. Sky Watch reports tonight's
stargazing conditions at a few invented viewing spots.

Real public APIs that need no key exist too, for weather, transit, earthquakes, and public
data. You may point your finished program at one of those for extra credit, but Sky Watch
is what the quest is graded against, because the lab network is not reliable and a real
service can be down the day you present.

**No API keys.** If a service wants a key, pick a different service. Sky Watch needs none.

---

## What is in this bundle

| File | What it is |
|---|---|
| `sky_watch_server.py` | The practice API. Runs on your computer. Has failure modes. |
| `first_contact.py` | The starter. It works on the happy path and crashes on every failure. |
| `check_quest.py` | A self-check that runs your program five ways and grades the done-when rule. |
| `instructor/` | Kept private by the publisher. Do not look for it. |

---

## How to run it

Start Sky Watch in one terminal and leave it open:

```
python sky_watch_server.py
```

In a second terminal, run the starter:

```
python first_contact.py mill-creek
```

It prints the raw data for one spot. Try `python first_contact.py` with no spot to list
them. Now break Sky Watch on purpose and watch the starter fall apart:

```
python sky_watch_server.py --mode always_404
python sky_watch_server.py --mode slow
python sky_watch_server.py --mode always_429
```

Run the starter against each. It crashes with a traceback every time. That is your quest.

---

## What to build

Turn the starter into a program that:

1. **Prints something a person wants.** Not raw JSON. Tonight's conditions and whether it
   is worth going out, in plain words.
2. **Handles a 404, a timeout, and a rate limit distinctly.** Each gets its own message
   that says which failure happened and what to do about it. A 404 means check the spot
   name. A timeout means try again later. A 429 means wait the time it asked for.
3. **Never crashes.** No traceback reaches the user. Every failure is caught and turned
   into a clear message.
4. **Never lies.** A failure is never reported as "no data." If you could not reach Sky
   Watch, say so, not that there is nothing to see tonight.

### The checklist in the starter

The starter has two checklist items marked in comments. Item 1 is the unprotected request
that crashes. Item 2 is printing something readable instead of raw data. Start there.

---

## Check yourself

Run the self-check. It starts its own Sky Watch servers, runs your program five ways, and
tells you whether you met the done-when rule:

```
python check_quest.py
```

It passes when a 404, a timeout, and a rate limit each get their own message and nothing
crashes. Passing the check is necessary, not sufficient: your instructor still reads your
messages and asks you to explain your code.

---

## Done when

- [ ] `python check_quest.py` passes
- [ ] A 404, a timeout, and a rate limit each produce a **different** message that says what
      happened and what to do
- [ ] The program never crashes with a traceback, on any failure
- [ ] A failure is never reported as "no data"
- [ ] Output is something a person would want to read, not raw JSON
- [ ] It lives in a repository with a README, committed and pushed
- [ ] You can explain every line you wrote

**Printing "Error" for all three failures fails this quest.** So does a program that only
works on the happy path.

---

## If you want more

Point your finished program at a real public API that needs no key. Search for one; several
public-data feeds are free and keyless. Add a note in your README saying which one and
whether it needed the same failure handling Sky Watch did. It will.
