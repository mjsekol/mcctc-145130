# check_quest.py  ·  SQ-18 Prompt Ablation
#
# Checks your work against the quest's "done when" list, without looking at
# whether your conclusion is any good. That part is yours.
#
# Run it:
#   python check_quest.py
#
# It checks seven things:
#   1. ablate.py imports and build_variants() runs
#   2. build_variants() returns at least 8 variants
#   3. one of them is the full prompt
#   4. there is a removal variant for every element
#   5. at least two variants remove two elements
#   6. every variant prompt is different from every other
#   7. results/ holds a recorded run for at least 8 variants
#   8. findings.md exists, has a table, and has a conclusion section

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

PASS = "PASS"
FAIL = "FAIL"


def report(ok, name, detail=""):
    print(f"  [{PASS if ok else FAIL}] {name}")
    if detail and not ok:
        print(f"         {detail}")
    return ok


def main():
    print("SQ-18 Prompt Ablation, self-check\n")
    results = []

    try:
        import ablate
    except Exception as error:
        report(False, "ablate.py imports", f"{type(error).__name__}: {error}")
        return 1
    report(True, "ablate.py imports")

    elements = ablate.read_elements(ablate.BASE_PROMPT)
    if not elements:
        report(False, "base_prompt.txt has tagged elements",
               "every element line starts with a tag like [ROLE]")
        return 1
    print(f"  ..   {len(elements)} elements: {', '.join(l for l, _ in elements)}")

    try:
        variants = ablate.build_variants(elements)
    except Exception as error:
        report(False, "build_variants() runs", f"{type(error).__name__}: {error}")
        return 1
    report(True, "build_variants() runs")

    labels = [label for label, _ in variants]

    results.append(report(
        len(variants) >= 8, f"at least 8 variants (you have {len(variants)})",
        "the quest needs 8. One removal per element plus two doubles gets you there"))

    results.append(report(
        "full" in labels, "one variant is the unchanged prompt, labelled 'full'",
        "without a control you have nothing to compare against"))

    missing = [label for label, _ in elements if f"no_{label}" not in labels]
    results.append(report(
        not missing, "a removal variant for every element",
        f"missing: {', '.join('no_' + m for m in missing)}"))

    doubles = [label for label in labels if label.count("no_") == 2]
    results.append(report(
        len(doubles) >= 2, f"at least 2 double removals (you have {len(doubles)})",
        "a single-removal design cannot see an interaction. Label them no_a_no_b"))

    prompts = [prompt for _, prompt in variants]
    results.append(report(
        len(set(prompts)) == len(prompts),
        "every variant prompt is different from every other",
        "two variants with the same text are one variant run twice"))

    recorded = sorted(p.stem for p in (HERE / "results").glob("*.json")) \
        if (HERE / "results").is_dir() else []
    results.append(report(
        len(recorded) >= 8, f"at least 8 recorded runs in results/ (you have {len(recorded)})",
        "run: python ablate.py"))

    findings = HERE / "findings.md"
    if not findings.exists():
        results.append(report(False, "findings.md exists",
                              "write it. The table and the conclusion are the quest"))
    else:
        text = findings.read_text(encoding="utf-8").lower()
        results.append(report("|" in text and "---" in text,
                              "findings.md has a table"))
        results.append(report("conclusion" in text,
                              "findings.md has a conclusion section",
                              "a heading with the word conclusion in it"))
        results.append(report(len(text.split()) >= 150,
                              f"findings.md is more than 150 words (it is {len(text.split())})",
                              "the conclusion needs reasoning under it"))

    passed = sum(1 for r in results if r)
    print(f"\n{passed} of {len(results)} checks passed.")
    if passed == len(results):
        print("\nThe mechanical part is done. Two things no checker can tell you:")
        print("  Does your conclusion name which element was doing the most work?")
        print("  Does it say what its scope is, on this task and this model?")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
