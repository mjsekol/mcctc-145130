# check_measure.py  .  Lab M01-04, the self-check for measure.py
#
# Every expected value below was worked out by hand before the code existed.
# That is the only way a test is worth anything: if you copy the expected
# value out of what your program already printed, the test agrees with the
# bug.
#
#   python check_measure.py

import sys

import measure

CASES = [
    # (label, what to call, arguments, expected)
    ("median of one value", measure.median, ([4.0],), 4.0),
    ("median of three, out of order", measure.median, ([3.0, 1.0, 2.0],), 2.0),
    ("median of four, out of order", measure.median, ([4.0, 1.0, 3.0, 2.0],), 2.5),
    ("median of an empty list", measure.median, ([],), None),

    ("generation time, both known", measure.generation_ms, (5000.0, 800.0), 4200.0),
    ("generation time, no first token", measure.generation_ms, (5000.0, None), None),
    ("generation time that contradicts itself", measure.generation_ms, (800.0, 900.0), None),
    ("generation time, first token was the whole thing", measure.generation_ms, (900.0, 900.0), 0.0),

    ("120 tokens in 4 seconds", measure.tokens_per_second, (120, 4000.0), 30.0),
    ("no tokens at all", measure.tokens_per_second, (0, 1000.0), 0.0),
    ("tokens over no time", measure.tokens_per_second, (50, 0.0), None),
    ("tokens over an unknown time", measure.tokens_per_second, (50, None), None),
    ("a rate that needs rounding", measure.tokens_per_second, (37, 1200.0), 30.8),
]


def main():
    failures = 0
    for label, function, arguments, expected in CASES:
        actual = function(*arguments)
        if actual == expected:
            print(f"  PASS  {label}")
        else:
            failures += 1
            print(f"  FAIL  {label}: expected {expected!r}, got {actual!r}")
    print(f"\n{len(CASES) - failures} of {len(CASES)} pass.")
    if failures:
        print("Read the first FAIL line. The expected value was worked out by hand.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
