# Gate 2: Adversarial Review · Week 14
## 145130 Applications of AI · Module 5 · Week 14, Thursday · Build 1

**40 minutes.** Individual. Silent. **You may not ask a model whether this code is
correct, because a model is what is being reviewed.**

**This packet is designed to work on paper.** The program is printed in Part C and
two real captured runs are in Part D. If the network is down, or your machine will
not start, or you are reading this on a bus back from a competition, you can do
every part of this exercise with a pen. Students who can run it should.

The program is `gate2-w14-files/club_digest.py`. It comes with a stand-in service,
`practice_service.py`, and a message file, `club_messages.json`, in the same
folder.

---

## What you are looking at

The robotics club officers wanted a digest of the week's messages read out at the
Friday meeting. Somebody handed an AI assistant the requirements in Part A and got
`club_digest.py`. It runs. It has docstrings and named constants and a tidy loop.

**Five defects, one in each category:** Correctness, Security, Readability,
Performance, Requirements Fit.

**Plus one item that is not a defect.** Item 6 is a design decision with a real
argument on each side. You are scored on your reasoning, not on which side you
pick.

**One of the five is about something the program keeps.** Look for it.

---

## PART A: The requirements

> Write `club_digest.py`. It reads the week's club messages from a JSON file and
> produces a digest. It must:
>
> 1. Take the service URL from the environment.
> 2. **Keep no copy of anybody's message.** Read it, send it, print the answer,
>    keep nothing.
> 3. **Skip a message that is empty after trimming**, and say it was skipped.
> 4. **Stop after the first failure that trying again cannot fix**, and say which
>    message it stopped on.
> 5. End with a count of how many answers came **from the model** and how many came
>    **from the fallback**.

---

## PART B: Running it, if you can

Two terminals, in the folder you copied.

```
python practice_service.py --port 5157
```

```
python club_digest.py
```

The stand-in service has five modes. Two of them matter most here.

```
python practice_service.py --port 5157 --mode model
python practice_service.py --port 5157 --mode fallback
```

**Run the program once in each mode and compare the last line of the two runs.**
That is the fastest way to find the Correctness defect.

Then look in the folder the program ran from and see what appeared there.

---

## PART C: The program

The whole of `club_digest.py` is below, with line numbers down the left. If you
are working on a machine, open the file rather than this listing. The line numbers
match either way.

```
  1  # club_digest.py
  2  #
  3  # Turns the week's robotics club messages into a digest the officers read out
  4  # at the Friday meeting. Each message is sent to the model service to be
  5  # summarized and classified, and the results are printed.
  6  #
  7  # The model runs locally. The service wraps it. This program never reads a
  8  # raw model answer.
  9  #
 10  #   python club_digest.py
 11  #   python club_digest.py --file club_messages.json
 12  #
 13  # The service must already be running.
 14  
 15  import argparse
 16  import json
 17  import os
 18  import sys
 19  import time
 20  import urllib.error
 21  import urllib.request
 22  
 23  SERVICE_URL_VARIABLE = "DIGEST_SERVICE_URL"
 24  DEFAULT_SERVICE_URL = "http://127.0.0.1:5157"
 25  
 26  # Seconds to wait for one answer from the service.
 27  timeout_ms = 45
 28  
 29  # How many times to send the same request again when the service says no.
 30  RETRY_ATTEMPTS = 3
 31  RETRY_PAUSE_SECONDS = 2.0
 32  
 33  LOG_FILE = "digest_log.txt"
 34  
 35  TASKS = ["summarize", "classify"]
 36  
 37  
 38  def service_url():
 39      """Where the service is listening."""
 40      configured = os.environ.get(SERVICE_URL_VARIABLE, "").strip()
 41      return (configured or DEFAULT_SERVICE_URL).rstrip("/")
 42  
 43  
 44  def log_everything(message, answer):
 45      """Keep a copy of what went out and what came back, handy for debugging."""
 46      with open(LOG_FILE, "a", encoding="utf-8") as handle:
 47          handle.write(f"{message['id']}\t{message['from']}\t{message['text']}\t{answer}\n")
 48  
 49  
 50  def ask(url, task, prompt):
 51      """Send one request to the service. Returns the envelope, or raises."""
 52      request = urllib.request.Request(
 53          url + "/generate",
 54          data=json.dumps({"task": task, "prompt": prompt}).encode("utf-8"),
 55          headers={"Content-Type": "application/json"},
 56          method="POST",
 57      )
 58      opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
 59      with opener.open(request, timeout=timeout_ms) as response:
 60          return json.loads(response.read().decode("utf-8"))
 61  
 62  
 63  def ask_with_retries(url, task, prompt):
 64      """Send one request, trying again when the service does not answer well."""
 65      last_error = None
 66      for attempt in range(1, RETRY_ATTEMPTS + 1):
 67          try:
 68              return ask(url, task, prompt)
 69          except urllib.error.HTTPError as error:
 70              body = error.read().decode("utf-8", "replace")
 71              error.close()
 72              last_error = f"HTTP {error.code}: {body[:120]}"
 73              print(f"    attempt {attempt} did not work, trying again")
 74              time.sleep(RETRY_PAUSE_SECONDS)
 75          except urllib.error.URLError as error:
 76              last_error = f"could not reach the service ({error.reason})"
 77              print(f"    attempt {attempt} did not work, trying again")
 78              time.sleep(RETRY_PAUSE_SECONDS)
 79      raise RuntimeError(last_error or "no answer")
 80  
 81  
 82  def show(envelope):
 83      """Print one answer from the service."""
 84      task = envelope.get("task")
 85      result = envelope.get("result") or {}
 86      if task == "summarize":
 87          print(f"    summary: {result.get('summary')}")
 88          for bullet in result.get("bullets", []):
 89              print(f"      - {bullet}")
 90      elif task == "classify":
 91          print(f"    label:   {result.get('label')}")
 92          print(f"    note:    {result.get('confidence_note')}")
 93  
 94  
 95  def run(url, messages):
 96      """Work through every message and print the digest."""
 97      from_model = 0
 98      from_fallback = 0
 99  
100      for message in messages:
101          print()
102          print(f"== {message['id']} from {message['from']} ==")
103          print(f'   "{message["text"]}"')
104  
105          for task in TASKS:
106              try:
107                  envelope = ask_with_retries(url, task, message["text"])
108                  show(envelope)
109                  log_everything(message, envelope)
110              except Exception:
111                  pass
112  
113          from_model += 1
114  
115      print()
116      print(f"Digest finished. {from_model} messages summarized by the model, "
117            f"{from_fallback} built from the fallback.")
118      return 0
119  
120  
121  def read_messages(path):
122      """The messages in a JSON file, or None."""
123      if not os.path.isfile(path):
124          print(f"No file at {os.path.abspath(path)}.")
125          return None
126      try:
127          with open(path, "r", encoding="utf-8") as handle:
128              return json.load(handle)
129      except json.JSONDecodeError as error:
130          print(f"{path} is not valid JSON: {error}")
131          return None
132  
133  
134  def main():
135      parser = argparse.ArgumentParser(description="Build the club digest.")
136      parser.add_argument("--file", default="club_messages.json")
137      arguments = parser.parse_args()
138  
139      url = service_url()
140      print(f"club_digest . service {url}")
141  
142      messages = read_messages(arguments.file)
143      if messages is None:
144          return 2
145      print(f"Reading {len(messages)} club messages from {arguments.file}")
146      return run(url, messages)
147  
148  
149  if __name__ == "__main__":
150      sys.exit(main())
```

---

## PART D: Two real runs, captured

Both of these came off a real machine. The service was in `fallback` mode for the
second one, which means **the model was not used for a single answer in that
run.**

### Run 1, the service in `model` mode

```
club_digest . service http://127.0.0.1:5157
Reading 6 club messages from club_messages.json

== CM-01 from invented sample, not a real student ==
   "The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped. I think the bed is off level on one corner."
    summary: Coach note: The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped.
      - The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped. I think the bed is off level on one corner.
    label:   hardware
    note:    The note mentions equipment that fits hardware.

== CM-03 from invented sample, not a real student ==
   "   "
    attempt 1 did not work, trying again
    attempt 2 did not work, trying again
    attempt 3 did not work, trying again
    attempt 1 did not work, trying again
    attempt 2 did not work, trying again
    attempt 3 did not work, trying again

== CM-06 from invented sample, not a real student ==
   "Someone left a box of servo horns on the soldering bench and nobody knows whose they are."
    summary: Coach note: Someone left a box of servo horns on the soldering bench and nobody knows whose they are.
    label:   other
    note:    The note mentions equipment that fits other.

Digest finished. 6 messages summarized by the model, 0 built from the fallback.

exit 0, wall clock 12.6 s
```

### Run 2, the service in `fallback` mode

**The model was used zero times in this run.**

```
club_digest . service http://127.0.0.1:5157
Reading 6 club messages from club_messages.json

== CM-01 from invented sample, not a real student ==
   "The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped. I think the bed is off level on one corner."
    summary: The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped.
      - The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped.
    label:   hardware
    note:    No model answer. A keyword rule matched hardware.

== CM-03 from invented sample, not a real student ==
   "   "
    attempt 1 did not work, trying again
    attempt 2 did not work, trying again
    attempt 3 did not work, trying again
    attempt 1 did not work, trying again
    attempt 2 did not work, trying again
    attempt 3 did not work, trying again

Digest finished. 6 messages summarized by the model, 0 built from the fallback.

exit 0, wall clock 12.5 s
```

### The file that appeared next to the program

```
CM-01	invented sample, not a real student	The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped. I think the bed is off level on one corner.	{'ok': True, 'task': 'summarize', 'result': {...}, 'source': 'model', ...}
CM-01	invented sample, not a real student	The 3D printer in the shop bay finished the gearbox mounts but the last two came out warped. I think the bed is off level on one corner.	{'ok': True, 'task': 'classify', 'result': {...}, 'source': 'model', ...}
```

---

## What to submit

For each defect: **line number**, **which of the five dimensions**, **what goes
wrong for a real person**, and **the fix**.

Then item 6, the design decision, with the strongest argument on each side and
your own position.

Then one final entry: **what I was unsure about**, naming something specific. That
entry is scored, and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 10:** read Part D carefully, both runs, line by line. Read the last line
  of each. Then read Part A requirement 5.
- **Next 10:** read Part A one requirement at a time and point at the line of code
  that meets it. A requirement you cannot point at is a finding. Requirements 2
  and 3 are both worth the time.
- **Next 10:** count the seconds. Both runs took over twelve seconds for six short
  messages against a service on the same machine. Where did they go?
- **Rest:** read every name in the file and ask whether it says what the thing
  does. Then write your unsure-about entry.

---

## Scoring

Five defects, one point each. Item 6 is one point, scored on reasoning. The
unsure-about entry is one point. Seven points.

**The security defect is double-penalized.** Missing it costs two points rather
than one. Your instructor states this before you start.

**Five of seven is a strong score.**
