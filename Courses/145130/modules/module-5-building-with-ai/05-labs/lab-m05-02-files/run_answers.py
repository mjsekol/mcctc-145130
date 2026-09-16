# run_answers.py  .  Lab M05-02, Parse What The Model Said
#
# Runs your parser over every captured answer in answers/ and prints what it
# got, one answer at a time.
#
# Why this exists alongside the tests: a test tells you pass or fail. This
# tells you what your parser actually produced, which is what you need while
# you are still working out why it did that.
#
#   python run_answers.py
#   python run_answers.py 04
#
# Standard library only.

import os
import sys

import parse_plan

ANSWERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "answers")


def preview(text, lines=2):
    """The first couple of non-empty lines, shortened."""
    kept = [" ".join(line.split()) for line in text.splitlines() if line.strip()]
    return [line[:72] for line in kept[:lines]]


def run(filename):
    with open(os.path.join(ANSWERS, filename), "r", encoding="utf-8") as handle:
        text = handle.read()

    print(f"== {filename} ==")
    for line in preview(text):
        print(f"   model said: {line}")

    plan = parse_plan.parse_study_plan(text)
    if plan is None:
        print("   parsed:     None. Nothing in that answer looked like a plan.")
    else:
        print(f"   title:      {plan.get('title')!r}")
        print(f"   steps:      {len(plan.get('steps') or [])}")
        for step in plan.get("steps") or []:
            print(f"     - {step}")
        print(f"   minutes:    {plan.get('minutes')!r}")

    reason = parse_plan.validate_study_plan(plan)
    if reason is None:
        print("   usable:     yes")
    else:
        print(f"   usable:     no. {reason}")
    print()


def main():
    wanted = sys.argv[1] if len(sys.argv) > 1 else ""
    names = sorted(name for name in os.listdir(ANSWERS) if name.endswith(".txt"))
    names = [name for name in names if wanted in name]
    if not names:
        print(f"No answer files matched {wanted!r}. Files available:")
        for name in sorted(os.listdir(ANSWERS)):
            print(f"  {name}")
        return 2
    for name in names:
        run(name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
