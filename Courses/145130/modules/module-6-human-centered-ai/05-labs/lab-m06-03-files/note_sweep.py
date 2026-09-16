"""The Weekly Note Sweep. STARTER.

This program runs. Every line in it works. It is also the version of this
automation that most people write first, and it has one problem:

    it reports a good run on a day it did no work at all.

Start the service stub, run this, and read the last line. Then stop the service
stub, run it again, and read the last line. They are the same line.

    python sweep_service_stub.py --port 5158
    python note_sweep.py --service http://127.0.0.1:5158 --once

That is step 1 of the lab, and it is the reason the rest of the lab exists.

WHAT YOU ARE ADDING
-------------------
Four things, marked TODO 1 through TODO 4 below.

  TODO 1  a freshness step, so the automation notices when the source did not
          change since the last run
  TODO 2  an expectation on every step: what it expected and what it got, and
          a status that comes from comparing those two
  TODO 3  an incident file, written when a step did not get what it expected,
          that names what a person should check and who to ask
  TODO 4  a run log, appended on every run including the failed ones

The scheduled trigger and the HTTP call are already written. Neither is what
this lab is about, and both take longer to get right than they are worth here.

Standard library only. Runs on Python 3.13.7.
"""

import argparse
import datetime
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

# The rule this program falls back to when the service cannot answer. It is not
# classification. It is words.
KEYWORDS = {
    "hardware": ["printer", "laptop", "monitor", "keyboard", "battery", "screen"],
    "software": ["install", "visual studio", "update", "crash", "license"],
    "network": ["wifi", "wi-fi", "internet", "vpn", "drops", "connection"],
    "account": ["password", "login", "locked out", "username", "sign in"],
}


def keyword_label(text):
    lowered = text.lower()
    for label, words in KEYWORDS.items():
        for word in words:
            if word in lowered:
                return label
    return "other"


# ------------------------------------------------------------------ step 1


def step_collect(inbox):
    """Read every note in the inbox. A note is one .txt file with words in it."""
    notes = []
    for path in sorted(inbox.glob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()
        if text:
            notes.append({"id": path.stem, "path": path, "text": text})
    return notes


# ------------------------------------------------------------------ step 2
#
# TODO 1. There is no freshness step here.
#
# Write one. It takes the notes and whatever the last run wrote down, and it
# answers one question: is anything in this inbox newer than the last time this
# automation swept it?
#
# You will need the last run to have written down the newest file time it saw.
# That is TODO 4's job, so these two are one piece of work in two places.
#
# Use `path.stat().st_mtime`, which is the time a file was last written, as a
# number of seconds. Compare with a small margin, because two file systems do
# not agree about fractions of a second.


# ------------------------------------------------------------------ step 3


def classify_one(service_url, text, timeout):
    """Ask the service for one label. Already written. Do not rewrite this.

    Returns (label, note_from_service, error_kind). A label of None means
    nothing usable came back, and the error kind says which of the five ways
    it went wrong.
    """
    payload = json.dumps({"task": "classify", "prompt": text}).encode("utf-8")
    request = urllib.request.Request(
        f"{service_url.rstrip('/')}/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return None, None, f"http_{exc.code}"
    except TimeoutError:
        return None, None, "timeout"
    except urllib.error.URLError as exc:
        if isinstance(getattr(exc, "reason", None), TimeoutError):
            return None, None, "timeout"
        return None, None, "connection_refused"

    try:
        envelope = json.loads(raw)
    except ValueError:
        return None, None, "not_the_envelope"

    if not isinstance(envelope, dict) or "source" not in envelope:
        return None, None, "not_the_envelope"

    result = envelope.get("result")
    if not isinstance(result, dict) or not result.get("label"):
        # HTTP 200, ok true, and nothing in it.
        return None, None, "empty_result"

    return result["label"], result.get("confidence_note", ""), None


def step_classify(notes, service_url, timeout):
    """Label every note.

    TODO 2 lives here as well as everywhere else. Right now this function
    counts nothing and tells nobody anything. Every note gets a label whether
    or not the service was involved, and the caller cannot tell the difference.
    """
    rows = []
    for note in notes:
        label, why, error = classify_one(service_url, note["text"], timeout)
        if label is None:
            label = keyword_label(note["text"])
            why = "keyword rule"
        rows.append({"id": note["id"], "label": label, "why": why,
                     "text": note["text"]})
    return rows


# ------------------------------------------------------------------ step 4


def step_digest(rows, out_dir, run_id):
    """Write the file a person reads."""
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"digest-{run_id}.md"
    buckets = {}
    for row in rows:
        buckets.setdefault(row["label"], []).append(row)

    lines = [f"# Note sweep digest, run {run_id}", "",
             f"{len(rows)} notes, {len(buckets)} categories.", ""]
    for label in sorted(buckets):
        lines.append(f"## {label} ({len(buckets[label])})")
        lines.append("")
        for row in buckets[label]:
            lines.append(f"- **{row['id']}** {row['text'].splitlines()[0][:90]}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ------------------------------------------------------------------ step 5
#
# TODO 4. There is no run log.
#
# Write one. A CSV in the state folder, one row per run, appended on every run
# including the runs that failed. A log that only records good runs is a log
# that says this automation has never failed.
#
# It also has to write down the newest source file time it saw on a good run,
# so that TODO 1 has something to compare against. Write that somewhere a
# program can read back, such as `state/last_run.json`.


# ------------------------------------------------------------------ one run


def run_once(args):
    run_id = "r0001"          # TODO 4 gives every run its own number
    inbox = pathlib.Path(args.inbox)
    out_dir = pathlib.Path(args.out)

    print(f"note sweep, run {run_id}, started {datetime.datetime.now():%H:%M:%S}")

    notes = step_collect(inbox)
    rows = step_classify(notes, args.service, args.timeout)
    digest = step_digest(rows, out_dir, run_id)

    # TODO 2 and TODO 3.
    #
    # This is the line that is not true. Read it next to the run you did with
    # the service stopped.
    print(f"  {len(notes)} notes, {len(rows)} labelled, digest at {digest}")
    print("  status  OK")
    return 0


# ------------------------------------------------------------------ trigger


def seconds_until(hhmm):
    """Seconds from now until the next occurrence of HH:MM local time."""
    hour, minute = (int(part) for part in hhmm.split(":"))
    now = datetime.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += datetime.timedelta(days=1)
    return (target - now).total_seconds()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="The Weekly Note Sweep. Starter version.")
    parser.add_argument("--service", required=True,
                        help="base URL of the model service, for example "
                             "http://127.0.0.1:5158. Required, on purpose: a "
                             "program that reaches the wrong server does not "
                             "fail, it answers.")
    parser.add_argument("--inbox", default="inbox")
    parser.add_argument("--state", default="state")
    parser.add_argument("--out", default="out")
    parser.add_argument("--timeout", type=float, default=10.0)

    trigger = parser.add_mutually_exclusive_group(required=True)
    trigger.add_argument("--once", action="store_true",
                         help="run one sweep now and exit")
    trigger.add_argument("--at", metavar="HH:MM",
                         help="the scheduled trigger: sweep once a day at this "
                              "local time")
    trigger.add_argument("--every", type=float, metavar="SECONDS",
                         help="sweep every N seconds, for showing the trigger "
                              "work without waiting a day")
    parser.add_argument("--runs", type=int, default=0,
                        help="stop after this many sweeps. 0 means keep going.")
    args = parser.parse_args(argv)

    if args.once:
        return run_once(args)

    completed = 0
    print("note sweep scheduler started. Ctrl+C to stop.")
    try:
        while True:
            if args.at:
                wait = seconds_until(args.at)
                fires = datetime.datetime.now() + datetime.timedelta(seconds=wait)
                print(f"  next sweep at {fires:%H:%M:%S}, in {wait / 60:.1f} minutes")
            else:
                wait = args.every
                print(f"  next sweep in {wait:.0f} seconds")
            time.sleep(wait)
            run_once(args)
            completed += 1
            if args.runs and completed >= args.runs:
                print(f"  {completed} sweeps done, stopping because --runs was set")
                return 0
    except KeyboardInterrupt:
        print("\nscheduler stopped")
        return 0


if __name__ == "__main__":
    sys.exit(main())
