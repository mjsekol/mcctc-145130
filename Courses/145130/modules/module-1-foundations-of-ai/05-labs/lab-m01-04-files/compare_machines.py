# compare_machines.py  .  your run against a classmate's run
#
#   python compare_machines.py runs/station-06.json runs/station-11.json
#
# WHY THIS PROGRAM REFUSES THINGS
#
# Two numbers can only be compared when they were produced the same way. If
# you sent different prompts, or a different number of repeats, or one of you
# counted tokens with the server's own counter while the other estimated from
# characters, then the two numbers are not two measurements of the same thing.
# They are two different measurements, and the difference between them tells
# you about your methods rather than about your machines.
#
# So this program checks the method first and stops when it does not match. A
# comparison it refuses to make is more useful than one it makes badly.

import json
import pathlib
import sys


def load(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def method_problems(left, right):
    """Return the reasons these two runs cannot be compared."""
    problems = []
    if left["method"]["prompt_set"] != right["method"]["prompt_set"]:
        problems.append(
            f"different prompt sets: {left['method']['prompt_set']} "
            f"against {right['method']['prompt_set']}. Identical prompts or nothing.")
    if left["method"]["repeats"] != right["method"]["repeats"]:
        problems.append(
            f"different repeat counts: {left['method']['repeats']} "
            f"against {right['method']['repeats']}. A median of three and a median "
            f"of ten are not the same kind of number.")
    return problems


def method_warnings(left, right):
    """Return the things that weaken the comparison without ruining it."""
    warnings = []
    left_sources = {b["summary"]["token_source"] for b in left["results"].values()}
    right_sources = {b["summary"]["token_source"] for b in right["results"].values()}
    if left_sources != right_sources:
        warnings.append(
            f"tokens were counted differently: {sorted(left_sources)} "
            f"against {sorted(right_sources)}. Only the timings are comparable.")
    if left["method"]["streamed"] != right["method"]["streamed"]:
        warnings.append(
            "one run streamed and the other did not, so only total latency is "
            "comparable between them.")
    if left["model"] != right["model"]:
        warnings.append(
            f"different models: {left['model']} against {right['model']}. You are "
            f"comparing two models and two machines at once, and you will not be "
            f"able to say which caused a difference.")
    return warnings


def cell(value, unit=""):
    return "n/a" if value is None else f"{value}{unit}"


def main():
    if len(sys.argv) != 3:
        print("usage: python compare_machines.py <yours.json> <theirs.json>")
        return 2
    left, right = load(sys.argv[1]), load(sys.argv[2])

    print(f"{left['label']}  against  {right['label']}\n")
    print(f"  {left['label']}: {left['hardware_note']}")
    print(f"  {right['label']}: {right['hardware_note']}\n")

    problems = method_problems(left, right)
    if problems:
        print("  These two runs cannot be compared.")
        for problem in problems:
            print(f"    {problem}")
        print("\n  Agree on a method, run again, and come back.")
        return 1

    for warning in method_warnings(left, right):
        print(f"  warning: {warning}")
    if method_warnings(left, right):
        print()

    print(f"  prompt            {left['label'][:14]:<14} {right['label'][:14]:<14} "
          f"difference")
    print("  " + "-" * 62)
    for name in left["method"]["prompt_set"]:
        a = left["results"][name]["summary"]
        b = right["results"][name]["summary"]
        gap = round(b["median_total_ms"] - a["median_total_ms"], 1)
        direction = "slower" if gap > 0 else "faster"
        print(f"  {name:<17} {cell(a['median_total_ms'], ' ms'):<14} "
              f"{cell(b['median_total_ms'], ' ms'):<14} "
              f"{abs(gap)} ms {direction}")
        print(f"  {'  tokens/sec':<17} {cell(a['tokens_per_second']):<14} "
              f"{cell(b['tokens_per_second']):<14}")
        print(f"  {'  first token':<17} {cell(a['median_ttft_ms'], ' ms'):<14} "
              f"{cell(b['median_ttft_ms'], ' ms'):<14}")

    print("\n  Warm-up requests, which neither total counts:")
    print(f"    {left['label']}: {left['warmup_ms']}")
    print(f"    {right['label']}: {right['warmup_ms']}")
    print("\n  Before you write the sentence 'machine A is faster', name one thing "
          "other than the\n  hardware that differed between these two runs. There is "
          "always at least one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
