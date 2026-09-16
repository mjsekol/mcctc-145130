# doc_check.py  .  Module 5 documentation self-check
#
# Reads a documentation folder and reports what the syllabus asks for and
# your set does not have yet.
#
# Why this exists: documentation is 20 percent of your grade in this course
# and it is the part people leave to the last twenty minutes. This tells you
# in five seconds which document is missing a required section, which section
# is still a placeholder, and which one is three words long. It does not tell
# you whether what you wrote is any good. A person reads it for that, in the
# peer walkthrough.
#
#   python doc_check.py                 checks the folder this file sits in
#   python doc_check.py ../my-project   checks another folder
#   python doc_check.py . --list        prints the whole requirement list
#
# Exit code 0 when nothing is missing, 1 when something is.
#
# Standard library only. It reads files and writes nothing.

import argparse
import os
import re
import sys

# Every document Module 5 requires, and the sections each one must carry.
# The competency code next to each is the one it answers. The section names
# are matched loosely: a heading that contains the words in order, ignoring
# case and punctuation, counts.
REQUIRED = {
    "design/ipo-chart.md": {
        "competency": "5.1.3, 5.6.6",
        "sections": ["Input", "Process", "Output", "What this chart leaves out"],
    },
    "design/dataflow-diagram.md": {
        "competency": "5.6.7",
        "sections": ["The layers", "One request step by step",
                     "Trust boundaries", "Where state lives"],
    },
    "design/io-specification.md": {
        "competency": "5.6.5, 5.6.6",
        "sections": ["The service", "The request", "The response envelope",
                     "Result shapes", "Error kinds"],
    },
    "design/constraint-list.md": {
        "competency": "5.6.2",
        "sections": ["Constraints", "Processing requirements", "What each constraint costs"],
    },
    "design/data-dictionary.md": {
        "competency": "5.6.8",
        "sections": ["Every field", "Where each field comes from", "What happens when a field is wrong"],
    },
    "docs/implementation-plan.md": {
        "competency": "5.6.8",
        "sections": ["What has to be true before you start", "Milestones", "Who does what",
                     "How you know each milestone is finished"],
    },
    "docs/contingency-plan.md": {
        "competency": "5.6.8",
        "sections": ["What can go wrong", "What you do about each one",
                     "What you cut first", "Who decides"],
    },
    "docs/user-help.md": {
        "competency": "5.6.8",
        "sections": ["What this program does", "How to start it",
                     "What every message means", "When it says the answer is a fallback"],
    },
    "docs/troubleshooting-log.md": {
        "competency": "2.11.1, 2.11.2, 2.11.5, 2.11.8",
        "sections": ["Entry", "Symptom", "Methodology", "What you changed", "How you verified"],
    },
}

# A heading line in markdown. Group 1 is the hashes, group 2 is the text.
HEADING_PATTERN = re.compile(r"^\s{0,3}(#{1,6})\s+(.*\S)\s*$")
# Words a template leaves behind when nobody filled it in. Kept short on
# purpose: a check that fires on ordinary sentences gets ignored.
PLACEHOLDER_PATTERN = re.compile(
    r"(TODO|TBD|FIXME|XXX|lorem ipsum|your (text|answer|name) here|"
    r"replace this (line|section|text)|\[ *\]\( *\))",
    re.IGNORECASE)

MIN_SECTION_WORDS = 25


def normalise(text):
    """Lowercase, letters and spaces only, for forgiving heading matching."""
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text.lower()).split())


def read_sections(path):
    """A list of (level, heading, own_body_lines) for one markdown file.

    A heading's own body stops at the next heading of any level. Its full
    body, which is what gets counted, runs to the next heading at the same
    level or higher, so a section written with subheadings is measured by
    everything under it rather than by the blank line before its first
    subheading.
    """
    sections = []
    level = 0
    heading = None
    body = []
    with open(path, "r", encoding="utf-8") as handle:
        in_fence = False
        for line in handle:
            if line.strip().startswith("```"):
                in_fence = not in_fence
                body.append(line)
                continue
            match = None if in_fence else HEADING_PATTERN.match(line)
            if match:
                if heading is not None:
                    sections.append((level, heading, body))
                level = len(match.group(1))
                heading = match.group(2)
                body = []
            else:
                body.append(line)
    if heading is not None:
        sections.append((level, heading, body))
    return sections


def full_body(sections, index):
    """Everything under a section, including its subsections."""
    level = sections[index][0]
    lines = list(sections[index][2])
    for deeper_level, _, deeper_body in sections[index + 1:]:
        if deeper_level <= level:
            break
        lines.extend(deeper_body)
    return lines


def find_section(sections, wanted):
    """The first section whose heading contains the wanted words, or None."""
    target = normalise(wanted)
    for index, (_, heading, _) in enumerate(sections):
        if target in normalise(heading):
            return heading, full_body(sections, index)
    return None


def word_count(body):
    text = "".join(body)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    return len(text.split())


def check_file(folder, relative, rules):
    """Every problem with one document, as a list of sentences."""
    problems = []
    path = os.path.join(folder, relative)
    if not os.path.isfile(path):
        return [f"the file is missing. It answers {rules['competency']}."]

    sections = read_sections(path)
    if not sections:
        return ["the file has no headings at all, so nothing in it can be found."]

    for wanted in rules["sections"]:
        found = find_section(sections, wanted)
        if found is None:
            problems.append(f"no section about '{wanted}'")
            continue
        heading, body = found
        words = word_count(body)
        if words < MIN_SECTION_WORDS:
            problems.append(f"'{heading}' has {words} words, which is not an answer yet")

    with open(path, "r", encoding="utf-8") as handle:
        in_fence = False
        for number, line in enumerate(handle, 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = PLACEHOLDER_PATTERN.search(line)
            if match:
                problems.append(f"line {number} still says '{match.group(0)}'")

    return problems


def print_requirements():
    print("Module 5 documentation set")
    print()
    for relative, rules in REQUIRED.items():
        print(f"{relative}   ({rules['competency']})")
        for section in rules["sections"]:
            print(f"    # {section}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Check a Module 5 documentation set.")
    parser.add_argument("folder", nargs="?", default=os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--list", action="store_true", help="print the requirement list and stop")
    arguments = parser.parse_args()

    if arguments.list:
        print_requirements()
        return 0

    folder = os.path.abspath(arguments.folder)
    print(f"doc_check . {folder}")
    print()

    total_problems = 0
    for relative, rules in REQUIRED.items():
        problems = check_file(folder, relative, rules)
        total_problems += len(problems)
        if problems:
            print(f"INCOMPLETE  {relative}")
            for problem in problems:
                print(f"              {problem}")
        else:
            print(f"COMPLETE    {relative}")

    print()
    if total_problems == 0:
        print("Every required document and section is present and has something in it.")
        print("That is the floor, not the grade. A person reads it next.")
        return 0
    print(f"{total_problems} thing{'' if total_problems == 1 else 's'} to fix.")
    print("Present and long enough is the floor. A person reads it next.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
