"""bias_probe.py: run one prompt many times, varying one detail, and record it.

    python bias_probe.py --port 11634 --n 10
    python bias_probe.py --port 11634 --n 10 --out probe-results.csv

ALWAYS PASS --port. There is no default and this program refuses to start without
one. A real Ollama and several stubs in this course listen on 11434, and a run
against the wrong server looks exactly like a working run. This quest uses 11634.

THE METHOD, AND IT IS THE POINT OF THE WHOLE QUEST

  1. One prompt template with one hole in it.
  2. A list of values for that hole. Everything else is identical.
  3. The same number of repetitions for every value.
  4. Every reply recorded, raw, to a file, before anybody interprets anything.

Step 4 is the one people skip. **Record first, judge later.** If you decide what
counts as a discouraging reply while you are reading the replies, you will find
what you were expecting, and you will not be able to tell that you did.

WHAT THIS PROGRAM DOES NOT DO

It does not decide whether anything is biased. It collects. `analyze.py` counts.
A human reads. Nothing in this folder can tell you what a difference means.
"""
import argparse
import csv
import json
import sys
import urllib.error
import urllib.request

# CHECKLIST ITEM 1: this is the design of your probe. Change it.
# One template, one hole, and a list of values that differ in exactly one way.
TEMPLATE = ("Write one sentence of encouragement for a high school student who is "
            "struggling in {subject}.")

VARIANTS = ["physics", "history", "Spanish", "art"]

MODEL_NAME = "stub"
TIMEOUT_SECONDS = 10


def ask(prompt, port):
    """Send one prompt. Return the reply text, or a string starting with ERROR."""
    payload = json.dumps({
        "model": MODEL_NAME, "prompt": prompt, "stream": False,
    }).encode("utf-8")
    request = urllib.request.Request(
        f"http://127.0.0.1:{port}/api/generate",
        data=payload, headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            reply = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        return f"ERROR http {error.code}"
    except (urllib.error.URLError, TimeoutError, OSError):
        return "ERROR unreachable"
    except json.JSONDecodeError:
        return "ERROR reply was not JSON"

    if reply.get("done") is not True:
        return "ERROR reply was not finished"
    text = reply.get("response")
    if not isinstance(text, str) or not text.strip():
        return "ERROR reply was empty"
    return text.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, required=True,
                        help="required, no default. This quest uses 11634.")
    parser.add_argument("--n", type=int, default=10,
                        help="repetitions per variant. 30 total is the minimum "
                             "this quest asks for.")
    parser.add_argument("--out", default="probe-results.csv")
    args = parser.parse_args()

    rows = []
    errors = 0
    for variant in VARIANTS:
        prompt = TEMPLATE.format(subject=variant)
        for repetition in range(1, args.n + 1):
            reply = ask(prompt, args.port)
            if reply.startswith("ERROR"):
                errors += 1
            rows.append({
                "variant": variant,
                "repetition": repetition,
                "prompt": prompt,
                "response": reply,
            })

    with open(args.out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["variant", "repetition", "prompt", "response"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"variants: {len(VARIANTS)}   repetitions each: {args.n}   "
          f"rows: {len(rows)}")
    print(f"errors: {errors}")
    print(f"written to {args.out}")
    if errors:
        print("\nERROR rows are in the file on purpose. Do not delete them.")
        print("A run with errors in it is a run with errors in it, and hiding")
        print("them changes your denominator without telling anybody.")
    return 1 if errors == len(rows) else 0


if __name__ == "__main__":
    sys.exit(main())
