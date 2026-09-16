"""Check a Module 6 submission for the shape the project asks for.

    python deliverables_check.py your-project
    python deliverables_check.py --list

It checks that the required files exist, that each one has its required sections,
and that the sections have something in them. It also runs four content checks
that catch the four mistakes this module is about.

**Passing this is the floor, not the grade.** It cannot tell whether anything you
wrote is true. A person does that: your partner, your stakeholder, and your
instructor.

Exit code 0 when everything required is present, 1 otherwise. Warnings do not
change the exit code, and they are the interesting part.

Standard library only. Built and run on Python 3.13.7.
"""

import argparse
import pathlib
import re
import sys

MIN_WORDS = 25

# path -> list of required section headings
REQUIRED = {
    "README.md": [
        "What this is",
        "How to run it",
        "What is not finished",
    ],
    "decision-log.md": [
        "Decisions",
    ],
    "study/participant-script.md": [
        "consent",
        "tasks",
        "closing question",
    ],
    "study/tabletop-record.md": [
        "What broke",
        "Found nothing in",
    ],
    "study/usability-report.md": [
        "What was tested",
        "Who with",
        "Findings",
        "What I did not measure",
        "What we are changing",
    ],
    "design/change-record.md": [
        "Changes",
        "Preferences",
    ],
    "design/wireframe-v1.md": [],
    "design/wireframe-v2.md": [],
    "automation/run-book.md": [
        "How to start it",
        "The trigger",
        "The steps",
        "When it fails",
    ],
    "analysis/opportunity-analysis.md": [
        "The industry",
        "Workflow 1",
        "Workflow 2",
        "Workflow 3",
        "What I did not measure",
    ],
    "acceptance/acceptance-procedure.md": [
        "Platform",
        "Stakeholder",
        "Cases",
    ],
    "acceptance/acceptance-record.md": [
        "Results",
        "Corrections",
        "decision",
    ],
}

REQUIRED_FOLDERS = {
    "study/sessions": (5, "session record"),
    "automation/evidence": (1, "captured run"),
}


def outside_fences(text):
    """The lines of the file with fenced code blocks blanked out.

    A table inside a fenced block often has a row starting with '#', and that
    would otherwise be read as a heading, which cuts every section short.
    """
    lines = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return lines


def sections_present(text, headings):
    """A heading counts if it appears as a markdown heading, case-insensitively."""
    found, missing = [], []
    lowered = [line.strip().lstrip("#").strip().lower()
               for line in outside_fences(text) if line.strip().startswith("#")]
    for heading in headings:
        if any(heading.lower() in line for line in lowered):
            found.append(heading)
        else:
            missing.append(heading)
    return found, missing


def section_body(text, heading):
    """The words under a heading, up to the next heading of the same or higher level.

    Headings are located outside fenced blocks. The body is taken from the raw
    text, so a table inside a fence still counts as words.
    """
    raw = text.splitlines()
    lines = outside_fences(text)
    start = None
    level = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#") and heading.lower() in stripped.lstrip("#").strip().lower():
            start = i + 1
            level = len(stripped) - len(stripped.lstrip("#"))
            break
    if start is None:
        return ""
    body = []
    for offset, line in enumerate(lines[start:]):
        stripped = line.strip()
        if stripped.startswith("#"):
            this_level = len(stripped) - len(stripped.lstrip("#"))
            if this_level <= level:
                break
        body.append(raw[start + offset])
    return "\n".join(body)


def content_checks(root):
    """The four checks that are about what this module teaches, not about shape."""
    warnings = []

    report = root / "study" / "usability-report.md"
    if report.exists():
        text = report.read_text(encoding="utf-8", errors="replace")

        # 1. Findings have to cite a participant and a line.
        citations = re.findall(r"\bP[1-9]\b[^\n]{0,20}\bL\d+", text)
        if len(citations) < 5:
            warnings.append(
                f"usability-report.md has {len(citations)} citations shaped 'P3 L7'. "
                "Every finding needs at least one. A finding nobody can trace is "
                "not a finding.")

        # 2. No rates from five people.
        rates = re.findall(r"\d+\s*(?:%|percent)", text, re.I)
        if rates:
            warnings.append(
                f"usability-report.md contains a percentage: {rates[0]!r}. "
                "Five people do not make a rate. Write counts: 'three of the five "
                "people I watched'.")

    change = root / "design" / "change-record.md"
    if change.exists():
        text = change.read_text(encoding="utf-8", errors="replace")
        # 3. Every change needs the four lines.
        for label in ("observation", "change", "prediction", "how i will know"):
            if label not in text.lower():
                warnings.append(
                    f"change-record.md never uses the word {label!r}. Every change "
                    "carries four lines: the observation, the change, the "
                    "prediction, and how you will know.")

    analysis = root / "analysis" / "opportunity-analysis.md"
    if analysis.exists():
        text = analysis.read_text(encoding="utf-8", errors="replace")
        # 4a. There has to be arithmetic.
        if not re.search(r"\d+\s*[x*]\s*\d+", text):
            warnings.append(
                "opportunity-analysis.md has no multiplication in it. An estimate "
                "is time per task times how often the task happens.")
        # 4b. No market figures.
        # Skip lines that are telling the reader these things are not in here.
        checkable = [line for line in text.splitlines()
                     if not re.search(r"\b(no|zero|never|not|without)\b", line, re.I)]
        banned = re.findall(
            r"(market size|market for|growing at|growth rate|adoption rate|"
            r"industry (?:average|standard|threshold)|up to \d+\s*(?:%|percent))",
            "\n".join(checkable), re.I)
        if banned:
            warnings.append(
                f"opportunity-analysis.md contains {banned[0]!r}. No market size, "
                "adoption rate, or vendor claim anywhere in this module. Estimate "
                "from something you can defend.")

    # 5. Nothing that identifies a participant.
    sessions = root / "study" / "sessions"
    if sessions.is_dir():
        for path in sorted(sessions.glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            hits = re.findall(r"^\s*(?:Name|Participant name|Full name)\s*:",
                              text, re.I | re.M)
            if hits:
                warnings.append(
                    f"{path.name} has a field that looks like a real name. "
                    "Participants are P1 through P5 and nothing else.")
    return warnings


def check(root):
    complete, incomplete, missing = [], [], []

    for rel, headings in REQUIRED.items():
        path = root / rel
        if not path.exists():
            missing.append(rel)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.split()) < MIN_WORDS:
            incomplete.append((rel, f"only {len(text.split())} words in the whole file"))
            continue
        found, absent = sections_present(text, headings)
        if absent:
            incomplete.append((rel, "missing section(s): " + ", ".join(absent)))
            continue
        thin = [h for h in headings if len(section_body(text, h).split()) < MIN_WORDS]
        if thin:
            incomplete.append((rel, "thin section(s), under "
                               f"{MIN_WORDS} words: " + ", ".join(thin)))
            continue
        complete.append(rel)

    for rel, (count, what) in REQUIRED_FOLDERS.items():
        folder = root / rel
        if not folder.is_dir():
            missing.append(rel + "/")
            continue
        files = [p for p in folder.iterdir() if p.is_file()]
        if len(files) < count:
            incomplete.append((rel + "/", f"{len(files)} file(s), needs at least "
                                          f"{count} {what}"))
        else:
            complete.append(f"{rel}/  ({len(files)} files)")

    return complete, incomplete, missing


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a Module 6 submission.")
    parser.add_argument("project", nargs="?", help="the folder to check")
    parser.add_argument("--list", action="store_true",
                        help="print the required shape and exit")
    args = parser.parse_args(argv)

    if args.list:
        print("Required files and their sections:\n")
        for rel, headings in REQUIRED.items():
            print(f"  {rel}")
            for heading in headings:
                print(f"      ## {heading}")
        print()
        for rel, (count, what) in REQUIRED_FOLDERS.items():
            print(f"  {rel}/   at least {count} {what}")
        print(f"\nEvery listed section needs at least {MIN_WORDS} words under it.")
        return 0

    if not args.project:
        parser.error("give a folder to check, or pass --list")

    root = pathlib.Path(args.project)
    if not root.is_dir():
        print(f"No folder at {root}")
        return 2

    complete, incomplete, missing = check(root)

    for rel in complete:
        print(f"COMPLETE    {rel}")
    for rel, why in incomplete:
        print(f"INCOMPLETE  {rel}   {why}")
    for rel in missing:
        print(f"MISSING     {rel}")

    warnings = content_checks(root)
    if warnings:
        print()
        for warning in warnings:
            print(f"WARNING     {warning}")

    print()
    if missing or incomplete:
        print(f"{len(missing)} missing, {len(incomplete)} incomplete, "
              f"{len(complete)} complete.")
        print("Fix the missing ones first. A section that does not exist cannot be "
              "read by anybody.")
        return 1

    print("Every required file and section is present and has something in it.")
    print("That is the floor, not the grade. A person reads it next.")
    if warnings:
        print(f"{len(warnings)} warning(s) above. None of them stops the check, "
              "and every one of them is a thing your instructor will ask about.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
