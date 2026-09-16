"""steelman_check.py: does this paragraph argue, or does it only assert?

    python steelman_check.py my-paragraph.txt
    python steelman_check.py --demo

It checks whether the PARTS of an argument are present. It cannot check whether
any of them are true, whether the argument is good, or whether it is honest. You
can score six of six on a dishonest paragraph by sprinkling in phrases, and if
that is what you do, you have written something worse than the version that
scored two.

Use it to find a missing part. Never use it to certify a paper.
"""
import sys

TESTS = {
    "states a claim": lambda t: any(
        w in t.lower() for w in ("should", "ought", "must", "is wrong", "is right")),
    "gives a reason": lambda t: any(
        w in t.lower() for w in ("because", "since", "the reason", "which means")),
    "points at evidence": lambda t: any(
        w in t.lower() for w in ("study", "record", "data", "measured", "report",
                                 "according to", "we tested")),
    "names who is affected": lambda t: any(
        w in t.lower() for w in ("students", "workers", "artists", "families",
                                 "teachers", "patients", "users")),
    "states the other side": lambda t: any(
        w in t.lower() for w in ("the strongest case", "critics", "opponents",
                                 "granting that", "the best argument against")),
    "answers the other side": lambda t: any(
        w in t.lower() for w in ("that reply fails", "the answer to that",
                                 "this does not hold because", "even so")),
}

DEMO = {
    "Version A": (
        "Schools should not use AI writing detectors. People who want them "
        "only care about catching students and do not care about learning. "
        "Anyone who has used one knows they are terrible."
    ),
    "Version B": (
        "Schools should not use AI writing detectors on student work. The "
        "reason is that a detector produces a score, not a finding, and a "
        "school then treats the score as a finding. The strongest case for "
        "detectors is real: teachers have a workload problem and no other "
        "tool at all, and students who write their own work are harmed when "
        "classmates do not. The answer to that is that a tool whose errors "
        "fall hardest on students who write unusually, including students "
        "writing in a second language, transfers the workload problem onto "
        "the students least able to carry it. We tested three samples and "
        "recorded the scores in our log."
    ),
}


def score(label, text):
    got = sum(1 for check in TESTS.values() if check(text))
    print(f"\n{label}: {got} of {len(TESTS)} parts present")
    for name, check in TESTS.items():
        print(f"   {'yes' if check(text) else 'NO '}  {name}")
    return got


def main(argv):
    if len(argv) != 2:
        print("Usage: python steelman_check.py <file.txt>   or   --demo")
        return 2
    if argv[1] == "--demo":
        for label, text in DEMO.items():
            score(label, text)
    else:
        try:
            text = open(argv[1], encoding="utf-8").read()
        except FileNotFoundError:
            print(f"No file at {argv[1]}. Check the path.")
            return 1
        score(argv[1], text)
    print("\nThis counts parts of an argument. It cannot tell you whether the")
    print("argument is any good, and it cannot tell you whether it is honest.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
