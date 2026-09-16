"""Self-check for Lab M03-03, Minimize the Roster.

    python check_minimize.py

It imports your minimize.py and runs nine checks. Passing every check is
necessary and not sufficient: your instructor still reads your README and asks
you to explain why each field is on a list.

This program checks behaviour. It is not legal advice and it does not decide
whether your program complies with anything.
"""
import importlib
import sys

import roster

MUST_INCLUDE = {
    "attendance_letter": {"first_name", "last_name", "guardian_name",
                          "guardian_email", "absences_this_term"},
    "bus_route_count": {"bus_route"},
    "ai_hint_request": set(),
}

MUST_EXCLUDE = {
    "attendance_letter": {"date_of_birth", "home_address", "meal_status",
                          "services_plan", "counselor_note", "photo_consent",
                          "bus_route", "guardian_phone"},
    "bus_route_count": set(roster.ALL_FIELDS) - {"bus_route"},
    "ai_hint_request": set(roster.ALL_FIELDS),
}

# Values that must never appear in a log line, taken from the fixture itself.
PERSONAL_FIELDS = ["first_name", "last_name", "date_of_birth", "home_address",
                   "guardian_name", "guardian_email", "guardian_phone",
                   "meal_status", "services_plan", "counselor_note",
                   "student_id"]


def report(passed, label, detail=""):
    print(f"{'PASS' if passed else 'FAIL'}  {label}")
    if not passed and detail:
        print("      " + detail)
    return 0 if passed else 1


def main():
    failures = 0
    minimize_module = importlib.import_module("minimize")
    minimize = minimize_module.minimize
    describe_for_log = minimize_module.describe_for_log

    sample = roster.ROSTER[0]

    # 1. minimize returns a new dict and leaves the roster alone.
    result = minimize(sample, "attendance_letter")
    result["injected"] = True
    failures += report("injected" not in roster.ROSTER[0],
                       "minimize returns a new dict, the roster is untouched")

    # 2 to 4. Each purpose keeps what it needs and drops what it does not.
    for purpose in ("attendance_letter", "bus_route_count", "ai_hint_request"):
        kept = set(minimize(sample, purpose))
        missing = MUST_INCLUDE[purpose] - kept
        leaked = MUST_EXCLUDE[purpose] & kept
        ok = not missing and not leaked
        failures += report(
            ok, f"{purpose}: keeps what it needs, drops what it does not",
            f"missing {sorted(missing)}; should not be there {sorted(leaked)}")

    # 5. An unknown purpose refuses rather than returning everything.
    try:
        minimize(sample, "curiosity")
        failures += report(False, "an unknown purpose raises ValueError",
                           "it returned a record instead of refusing")
    except ValueError:
        failures += report(True, "an unknown purpose raises ValueError")
    except Exception as error:
        failures += report(False, "an unknown purpose raises ValueError",
                           f"it raised {type(error).__name__} instead")

    # 6. No personal value reaches the log line.
    line = describe_for_log(sample, "attendance_letter")
    found = [f for f in PERSONAL_FIELDS
             if str(sample[f]) and str(sample[f]) in str(line)]
    failures += report(not found, "the log line carries no personal value",
                       f"found these field values in the line: {found}")

    # 7. The log line still says what happened.
    failures += report("attendance_letter" in str(line),
                       "the log line still names the purpose")

    # 8. Two students do not share a reference.
    other = roster.ROSTER[1]
    failures += report(
        describe_for_log(sample, "attendance_letter")
        != describe_for_log(other, "attendance_letter"),
        "two different students produce two different log lines")

    # 9. The same student produces the same line twice inside one run.
    failures += report(
        describe_for_log(sample, "attendance_letter")
        == describe_for_log(sample, "attendance_letter"),
        "the same student produces the same line twice in one run",
        "your reference is random rather than derived, so two entries about the "
        "same student in one run cannot be grouped, and the log cannot be used "
        "to trace a single failed record")

    # 10. A new run produces a different reference for the same student.
    first = describe_for_log(sample, "attendance_letter")
    minimize_module.RUN_SALT = "a-different-salt-entirely"
    second = minimize_module.describe_for_log(sample, "attendance_letter")
    failures += report(
        first != second,
        "changing RUN_SALT changes the reference",
        "your reference does not depend on RUN_SALT, so logs from different "
        "runs can still be matched together")

    print(f"\n{10 - failures} of 10 checks passed.")
    print("This checks behaviour only. It does not check your reasoning, and it "
          "is not legal advice.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
