# compare.py  .  Lab M01-01, the side by side
#
# Runs your decision tree and the model on the same twelve tickets and prints
# one row per ticket. It also writes comparison.csv so you can paste the
# numbers into your report without retyping them.
#
#   python compare.py
#
# The stub must be running:  python stub_model_server.py --port 11634
#
# READ THE how COLUMN, NOT ONLY THE LABEL
#
# json     the model's text contained a JSON object and we read the label out
# prose    no JSON, but a line started with Label:
# off_list the model named a category that is not one of the five
# unparsed nothing usable came back, and this program refuses to guess
#
# Your rules can always say why they answered. The model cannot. What you get
# instead is a record of how your own program turned text into a label, and
# that record only exists because somebody wrote the code that keeps it.

import csv
import json
import os
import sys

import ask_model
import triage_rules

HERE = os.path.dirname(os.path.abspath(__file__))
TICKETS_FILE = os.path.join(HERE, "tickets.json")
OUTPUT_FILE = os.path.join(HERE, "comparison.csv")


def main():
    with open(TICKETS_FILE, encoding="utf-8") as handle:
        tickets = json.load(handle)["tickets"]

    print(f"model endpoint {ask_model.MODEL_URL}\n")
    rows = []
    print("  ticket    staff      your rules  model      how        agree")
    print("  " + "-" * 62)
    for ticket in tickets:
        mine = triage_rules.classify(ticket["text"])
        try:
            answer = ask_model.classify_one(ticket["text"])
        except ask_model.ModelProblem as problem:
            print(f"  {problem}")
            return 1
        theirs = answer["label"] if answer["label"] else "no label"
        staff = ticket["human_label"]
        if staff == "argue":
            agree = "no answer"
        elif mine == theirs == staff:
            agree = "both"
        elif mine == staff:
            agree = "rules"
        elif theirs == staff:
            agree = "model"
        else:
            agree = "neither"
        print(f"  {ticket['id']}  {staff:<10} {mine:<11} "
              f"{theirs:<10} {answer['how']:<10} {agree}")
        rows.append({
            "id": ticket["id"],
            "staff_label": staff,
            "rules_label": mine,
            "rules_reason": triage_rules.explain(ticket["text"]),
            "model_label": theirs,
            "how_we_read_it": answer["how"],
            "model_raw_answer": answer["raw"],
            "who_matched_staff": agree,
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    settled = [r for r in rows if r["staff_label"] != "argue"]
    rules_right = sum(1 for r in settled if r["rules_label"] == r["staff_label"])
    model_right = sum(1 for r in settled if r["model_label"] == r["staff_label"])
    print("\n  On the nine settled tickets:")
    print(f"    your rules matched the staff on {rules_right}")
    print(f"    the model matched the staff on {model_right}")
    print(f"\n  Wrote comparison.csv. Every disagreement is a row in your report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
