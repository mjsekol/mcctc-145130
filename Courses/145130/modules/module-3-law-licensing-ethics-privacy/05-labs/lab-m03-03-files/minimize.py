"""Starter for Lab M03-03, Minimize the Roster.

This file runs right now and does nothing useful. That is on purpose. Read it,
run it, then start at CHECKLIST ITEM 1.

The rule you are building toward: a program that never holds a field cannot leak
that field, cannot mis-handle it, and cannot put it in a prompt by accident. Data
minimization is a privacy control you write in code, not a policy you write in a
document.

Run:
    python minimize.py
    python check_minimize.py
"""
import hashlib
import secrets

from roster import ALL_FIELDS, ROSTER

# A fresh value every time the program starts. Nothing written with this salt
# can be matched to anything written with a different one.
RUN_SALT = secrets.token_hex(8)


# CHECKLIST ITEM 1
# Fill in the field list for each purpose. A field belongs on a list only if the
# purpose cannot be carried out without it. "It might be handy" is not a reason.
PURPOSES = {
    "attendance_letter": ALL_FIELDS,   # <- wrong on purpose. Fix it.
    "bus_route_count": ALL_FIELDS,     # <- wrong on purpose. Fix it.
    "ai_hint_request": ALL_FIELDS,     # <- wrong on purpose. Fix it.
}


def minimize(record, purpose):
    """Return a NEW dict holding only the fields this purpose needs.

    CHECKLIST ITEM 2
    An unknown purpose must raise ValueError. Think about why refusing is the
    safe behaviour here and returning the whole record is not.
    """
    return dict(record)


def describe_for_log(record, purpose):
    """Return one line that is safe to write to a log file.

    CHECKLIST ITEM 3
    Right now this prints the whole record into the log, which is the bug this
    lab is really about. A log line should say what happened, not who it
    happened to. Use a reference built from RUN_SALT so the same student looks
    different in every run.
    """
    return f"purpose={purpose} record={record}"


def reference(student_id):
    """CHECKLIST ITEM 4: a short opaque reference for one student, this run only."""
    return student_id


def main():
    print("Fields the roster carries:", len(ALL_FIELDS))
    for record in ROSTER[:2]:
        for purpose in PURPOSES:
            sent = minimize(record, purpose)
            print(f"{purpose:>18}: {len(sent)} field(s) -> {sorted(sent)}")
        print("   log:", describe_for_log(record, "attendance_letter"))
        print()


if __name__ == "__main__":
    main()
