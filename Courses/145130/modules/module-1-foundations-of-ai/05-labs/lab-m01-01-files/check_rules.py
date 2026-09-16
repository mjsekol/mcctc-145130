# check_rules.py  .  Lab M01-01, your self-check
#
# Runs your triage_rules.classify against the nine tickets the makerspace
# staff agreed on. The three tickets marked argue are reported separately and
# are never counted as right or wrong, because there is no agreed answer to
# check against.
#
#   python check_rules.py
#
# No model, no network, no service. This file only reads your rules.

import json
import pathlib
import sys

import triage_rules

TICKETS_FILE = pathlib.Path(__file__).with_name("tickets.json")


def load_tickets():
    with TICKETS_FILE.open(encoding="utf-8") as handle:
        return json.load(handle)["tickets"]


def main():
    tickets = load_tickets()
    settled = [t for t in tickets if t["human_label"] != "argue"]
    disputed = [t for t in tickets if t["human_label"] == "argue"]

    failures = 0
    print(f"Checking {len(settled)} settled tickets against your rules.\n")
    for ticket in settled:
        actual = triage_rules.classify(ticket["text"])
        expected = ticket["human_label"]
        mark = "PASS" if actual == expected else "FAIL"
        if actual != expected:
            failures += 1
        print(f"  {mark}  {ticket['id']}  your rules said {actual:<9} staff said {expected}")

    print(f"\n{len(settled) - failures} of {len(settled)} settled tickets match. {failures} to go.")

    print("\nThe three tickets with no agreed answer. Nothing here is scored.")
    for ticket in disputed:
        print(f"  {ticket['id']}  your rules said {triage_rules.classify(ticket['text'])}")
        print(f"        reason: {triage_rules.explain(ticket['text'])}")

    if failures:
        print("\nKeep going. Read the first FAIL line and find the branch that fired.")
    else:
        print("\nAll settled tickets match. Now go and disagree with the staff on purpose:")
        print("pick one settled ticket and argue in your report that the agreed label is wrong.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
