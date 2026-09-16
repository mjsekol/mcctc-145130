"""SCAFFOLDED starting point for Lab M06-03, part 3.

Part 3 asks you to put an expectation on every step. This file gives you the
shape and one finished step, so that the part being assessed is the judgement
about what each step should expect, not the plumbing.

Copy `StepResult` and `step_collect` into your `note_sweep.py`, then write the
same shape for your other steps.

Run this file on its own to see what the shape prints:

    python step_result_start.py --inbox ../inbox

Standard library only. Run on Python 3.13.7 on the build machine.
"""

import argparse
import pathlib
import sys


class StepResult:
    """One step, and the two things that decide whether it worked.

    `expected` and `got` are written as words, because they end up in an
    incident file that a person reads at eight in the morning.
    """

    def __init__(self, name, ok, expected, got, detail="", degraded=False):
        self.name = name
        self.ok = ok
        self.expected = expected
        self.got = got
        self.detail = detail
        self.degraded = degraded

    def line(self):
        mark = "ok  " if self.ok else "FAIL"
        if self.ok and self.degraded:
            mark = "warn"
        return f"  [{mark}] {self.name:<10} expected {self.expected}, got {self.got}"


def step_collect(inbox):
    """Finished for you. The pattern is: do the work, then judge it."""
    notes = []
    for path in sorted(inbox.glob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()
        if text:
            notes.append({"id": path.stem, "path": path, "text": text})

    ok = len(notes) > 0
    return notes, StepResult(
        "collect",
        ok,
        "at least 1 note file in the inbox",
        f"{len(notes)}",
        detail="" if ok else
        "The inbox held no readable notes. The drop did not happen.",
    )


# ---------------------------------------------------------------------------
# YOUR TURN. Write these four, using the same shape.
#
# For each one, answer two questions before you write any code:
#   what did this step need in order to have worked?
#   what did it actually get?
#
# step_freshness(notes, state)
#     expected: something in the inbox is newer than the last good run
#     got:      ...
#
# step_classify(notes, service_url, timeout)
#     expected: one usable label per note, and at least one of them from
#               the service rather than from your keyword rule
#     got:      ...
#
# step_digest(rows, out_dir, run_id)
#     expected: ...
#     got:      ...
#
# step_record(state_dir, ...)
#     expected: ...
#     got:      ...
#
# The run status comes from comparing expected with got, across all of them.
# It does not come from whether anything raised.
# ---------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Show what the StepResult shape prints.")
    parser.add_argument("--inbox", default="../inbox")
    args = parser.parse_args(argv)

    inbox = pathlib.Path(args.inbox)
    if not inbox.is_dir():
        print(f"No folder at {inbox}. Pass --inbox with the path to the notes.")
        return 2

    notes, result = step_collect(inbox)
    print("one step, judged:")
    print(result.line())
    print()
    print(f"ok = {result.ok}")
    print("Now write four more like it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
