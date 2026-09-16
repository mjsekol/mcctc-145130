# compare_runs.py  ·  145130 Module 2 prompt toolkit
#
# Read every recorded run in a folder and print a table of what is measurably
# different between them.
#
# WHY THIS EXISTS
#   "This one is better" is where a prompt comparison usually stops, and it is
#   not a finding. This tool counts things: how long the reply is, whether it
#   parses as JSON, how many numbered items it has, how many sources it claims,
#   how many hedging phrases it contains. Those are facts. The judgement is
#   still yours, and you write it yourself.
#
# WHAT IT WILL NOT TELL YOU
#   Whether the reply is true. Whether a source exists. Whether the tone fits
#   your reader. No counter answers those. That is the whole reason the
#   evaluation rubric has five parameters and not one.
#
# Usage:
#   python compare_runs.py runs
#   python compare_runs.py runs --show v1 v3

import argparse
import json
import pathlib
import re
import sys

HEDGES = [
    "it is worth noting", "it is important to", "many experts", "many educators",
    "studies have shown", "ultimately", "depends on your specific",
    "there are many", "in general", "can vary",
]
NUMBERED_ITEM = re.compile(r"^\s*\d+[.)]\s+\S", re.M)
BULLET_ITEM = re.compile(r"^\s*[-*]\s+\S", re.M)
SOURCE_ITEM = re.compile(r"^\s*\[\d+\]\s+\S", re.M)


def shape_of(text):
    """Name the shape of a reply from what is actually in it."""
    stripped = text.strip()
    if stripped.startswith("{") or stripped.startswith("["):
        return "json"
    if stripped.startswith("|") or "\n|" in stripped:
        return "table"
    if NUMBERED_ITEM.search(stripped):
        return "numbered"
    if BULLET_ITEM.search(stripped):
        return "bullets"
    return "prose"


def parses_as_json(text):
    try:
        json.loads(text.strip())
        return True
    except ValueError:
        return False


def measure(run):
    text = run.get("response", "")
    return {
        "label": run.get("label", "?"),
        "prompt_words": run.get("prompt_words", len(run.get("prompt", "").split())),
        "reply_words": run.get("response_words", len(text.split())),
        "seconds": run.get("elapsed_seconds", 0.0),
        "shape": shape_of(text),
        "json_ok": "yes" if parses_as_json(text) else "no",
        "items": len(NUMBERED_ITEM.findall(text)) + len(BULLET_ITEM.findall(text)),
        "sources": len(SOURCE_ITEM.findall(text)),
        "hedges": sum(text.lower().count(h) for h in HEDGES),
    }


def load_runs(folder):
    runs = []
    for path in sorted(folder.glob("*.json")):
        try:
            runs.append(json.loads(path.read_text(encoding="utf-8")))
        except ValueError:
            print(f"skipped {path.name}: it is not valid JSON")
    return runs


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare recorded prompt runs.")
    parser.add_argument("runs_dir", nargs="?", default="runs")
    parser.add_argument("--show", nargs="*", default=[],
                        help="labels whose full reply you want printed under the table")
    arguments = parser.parse_args(argv)

    folder = pathlib.Path(arguments.runs_dir)
    if not folder.is_dir():
        print(f"There is no folder at {folder}. Run ask.py first.")
        return 2

    runs = load_runs(folder)
    if not runs:
        print(f"No recorded runs in {folder}. Run ask.py first.")
        return 2

    rows = [measure(r) for r in runs]
    header = ("| Label | Prompt words | Reply words | Seconds | Shape | Valid JSON "
              "| List items | Sources claimed | Hedges |")
    print(header)
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['label']} | {r['prompt_words']} | {r['reply_words']} | "
              f"{r['seconds']:.2f} | {r['shape']} | {r['json_ok']} | {r['items']} | "
              f"{r['sources']} | {r['hedges']} |")

    print(f"\n{len(rows)} run(s) compared.")
    print("Every number above is countable. None of them is a judgement.")
    print("Sources claimed is a count, not a check. Nothing here verified that any source exists.")

    by_label = {r.get("label"): r for r in runs}
    for label in arguments.show:
        run = by_label.get(label)
        if run is None:
            print(f"\nThere is no run labelled {label}.")
            continue
        print("\n" + "=" * 68)
        print(f"{label}")
        print("=" * 68)
        print(run.get("response", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
