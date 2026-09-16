"""audit_check.py: check that a licensing audit manifest is COMPLETE.

    python audit_check.py asset-manifest.csv study-buddy

What this checks:
  1. The manifest has every required column.
  2. Every component in the project tree appears in the manifest.
  3. Every manifest row points at a path that exists in the tree.
  4. No required cell is blank.
  5. A row whose license_id is UNKNOWN has something written in action_needed.
  6. verified_by names a file that exists in the tree, or starts with READ:,
     or is the exact words NONE FOUND.

WHAT THIS DOES NOT CHECK, AND WILL NEVER CHECK:
  Whether your legal reading is right. This program cannot tell you whether a
  license permits what you said it permits. A green result means your audit is
  complete. It does not mean your audit is correct. A human reads the reading.

This program is not legal advice and neither is its output.
"""
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "path",
    "component",
    "origin",
    "license_id",
    "license_file",
    "permits",
    "requires",
    "forbids",
    "action_needed",
    "verified_by",
]

# Cells that may never be blank. license_file may be blank when no license file
# exists, which is itself a finding, so it is not on this list.
NEVER_BLANK = ["path", "component", "origin", "license_id", "permits", "requires",
               "forbids", "verified_by"]


def is_generated(name):
    """True for directories Python or an editor made, which nobody has to license.

    Running the project creates __pycache__ folders. Without this check the tool
    would report them as components you failed to account for, which is a false
    finding, and a tool that produces false findings gets ignored.
    """
    return name.startswith((".", "__"))


def find_components(tree):
    """Derive the list of components an auditor has to account for from the tree."""
    components = []
    for group in ("vendor", "assets", "data"):
        group_dir = tree / group
        if group_dir.is_dir():
            for child in sorted(group_dir.iterdir()):
                if child.is_dir() and not is_generated(child.name):
                    components.append(child.relative_to(tree).as_posix())
    snippets = tree / "snippets"
    if snippets.is_dir():
        for child in sorted(snippets.glob("*.py")):
            if child.name != "__init__.py":
                components.append(child.relative_to(tree).as_posix())
    if (tree / "model").is_dir():
        components.append("model")
    return components


def load_rows(manifest_path):
    with manifest_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def main(argv):
    if len(argv) != 3:
        print("Usage: python audit_check.py <asset-manifest.csv> <project tree>")
        return 2

    manifest_path = Path(argv[1])
    tree = Path(argv[2])

    if not manifest_path.exists():
        print(f"FAIL  No manifest at {manifest_path}")
        return 1
    if not tree.is_dir():
        print(f"FAIL  No project tree at {tree}")
        return 1

    headers, rows = load_rows(manifest_path)
    problems = []

    missing_columns = [c for c in REQUIRED_COLUMNS if c not in headers]
    if missing_columns:
        problems.append("missing columns: " + ", ".join(missing_columns))
        print("FAIL  " + problems[0])
        return 1

    covered = set()
    for number, row in enumerate(rows, start=2):
        path_value = (row.get("path") or "").strip()
        covered.add(path_value)
        for column in NEVER_BLANK:
            if not (row.get(column) or "").strip():
                problems.append(f"row {number}: {column} is blank")
        if path_value and not (tree / path_value).exists():
            problems.append(f"row {number}: path {path_value} is not in the tree")
        license_id = (row.get("license_id") or "").strip().upper()
        if license_id == "UNKNOWN" and not (row.get("action_needed") or "").strip():
            problems.append(
                f"row {number}: license_id is UNKNOWN and action_needed is blank"
            )
        verified = (row.get("verified_by") or "").strip()
        if verified and verified != "NONE FOUND" and not verified.startswith("READ:"):
            if not (tree / verified).exists():
                problems.append(
                    f"row {number}: verified_by names {verified}, which is not in the tree"
                )

    for component in find_components(tree):
        if not any(c == component or c.startswith(component + "/") for c in covered):
            problems.append(f"component not in the manifest: {component}")

    print(f"manifest rows: {len(rows)}")
    print(f"components found in the tree: {len(find_components(tree))}")
    if problems:
        print(f"\nFAIL  {len(problems)} problem(s):")
        for problem in problems:
            print("  - " + problem)
        print("\nThis checks completeness only. It does not check your reading.")
        return 1

    print("\nPASS  The manifest is complete.")
    print("This checks completeness only. It does not check your reading.")
    print("A human still has to read every permits, requires, and forbids cell.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
