"""pia_check.py: check that a privacy impact assessment is COMPLETE.

    python pia_check.py my-pia.md

What this checks:
  1. All eleven required sections are present, spelled as the template spells them.
  2. The data inventory table has at least five rows and no blank cells.
  3. Every inventory row names a retention answer that is not the word unknown.
  4. The risk table has at least four rows and every row has a mitigation.
  5. Every UNKNOWN anywhere in the document has a matching line in section 11.
  6. The document says somewhere that it is not legal advice.

WHAT THIS DOES NOT CHECK:
  Whether your analysis is right. A green result means you filled in the form.
  It does not mean the feature is safe to build, and it is not legal advice.
"""
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "1. The feature",
    "2. Why it is being proposed",
    "3. Data inventory",
    "4. Basis for handling this data",
    "5. Confidentiality, integrity, availability",
    "6. What this feature refuses to collect",
    "7. Risks and mitigations",
    "8. Model and vendor questions",
    "9. Retention and deletion",
    "10. Accessibility",
    "11. Recommendation and open questions",
]


def table_rows(text, heading):
    """Return the data rows of the first markdown table under a heading."""
    start = text.find(heading)
    if start == -1:
        return []
    block = text[start:]
    rows = []
    for line in block.splitlines()[1:]:
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            rows.append(cells)
        elif rows and not stripped:
            continue
        elif rows:
            break
    return rows[1:] if rows else []


def main(argv):
    if len(argv) != 2:
        print("Usage: python pia_check.py <pia file.md>")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"FAIL  No file at {path}")
        return 1
    text = path.read_text(encoding="utf-8")
    problems = []

    for section in REQUIRED_SECTIONS:
        if section not in text:
            problems.append(f"missing section: {section}")

    inventory = table_rows(text, "## 3. Data inventory")
    if len(inventory) < 5:
        problems.append(f"data inventory has {len(inventory)} rows, needs at least 5")
    for number, row in enumerate(inventory, 1):
        if any(not cell for cell in row):
            problems.append(f"data inventory row {number} has a blank cell")
        if len(row) >= 6 and row[5].strip().lower() in ("unknown", "?", "tbd"):
            problems.append(
                f"data inventory row {number} has no retention answer")

    risks = table_rows(text, "## 7. Risks and mitigations")
    if len(risks) < 4:
        problems.append(f"risk table has {len(risks)} rows, needs at least 4")
    for number, row in enumerate(risks, 1):
        if len(row) < 5 or not row[4].strip():
            problems.append(f"risk row {number} has no mitigation")

    open_section = text.split("## 11. Recommendation and open questions")[-1]
    unknown_count = len(re.findall(r"\bUNKNOWN\b", text))
    open_unknowns = len(re.findall(r"\bUNKNOWN\b", open_section))
    body_unknowns = unknown_count - open_unknowns
    if body_unknowns > 0 and open_unknowns < body_unknowns:
        problems.append(
            f"{body_unknowns} UNKNOWN marker(s) in the body but only "
            f"{open_unknowns} listed in section 11")

    if "not legal advice" not in text.lower():
        problems.append("the document never says it is not legal advice")

    print(f"sections found: {len(REQUIRED_SECTIONS) - sum(1 for p in problems if p.startswith('missing section'))} of {len(REQUIRED_SECTIONS)}")
    print(f"data inventory rows: {len(inventory)}")
    print(f"risk rows: {len(risks)}")

    if problems:
        print(f"\nFAIL  {len(problems)} problem(s):")
        for problem in problems:
            print("  - " + problem)
        print("\nThis checks completeness only. It does not check your analysis.")
        return 1

    print("\nPASS  The assessment is complete.")
    print("This checks completeness only. It does not check your analysis, and "
          "it is not legal advice.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
