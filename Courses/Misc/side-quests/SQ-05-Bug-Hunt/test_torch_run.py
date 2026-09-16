"""Test cases for torch_run.py  ·  SQ-05 Bug Hunt

Run it like this, from the folder that holds torch_run.py:

    python test_torch_run.py

Each test feeds a scripted list of commands to the program and checks something
about what came back. A failing test tells you WHAT is wrong, not WHERE. Finding
where is the quest.

You do not need to understand this file to use it. You may read it. You may not
edit it. Changing a test so it passes is not fixing a bug.
"""

import re
import subprocess
import sys

PROGRAM = "torch_run.py"
passed = 0
failed = 0
results = []


def run(commands):
    """Feed commands to the program, one per line, and return everything it printed."""
    proc = subprocess.run(
        [sys.executable, PROGRAM],
        input="\n".join(commands) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    return proc.stdout


def torch_counts(out):
    """Every torch count the program reported, in order.

    The "> " prompt from input() shares a line with the next print, so a plain
    startswith check misses them. Match the number wherever it appears.
    """
    return [int(m) for m in re.findall(r"Torches:\s*(-?\d+)", out)]


def check(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        results.append(("PASS", name, ""))
    else:
        failed += 1
        results.append(("FAIL", name, detail))


# --------------------------------------------------------------------------
# 1. A blocked move must not cost a torch.
#    "south" from the entrance hits solid rock. Nothing moved, so nothing burns.
# --------------------------------------------------------------------------
out = run(["inventory", "south", "inventory", "quit"])
counts = torch_counts(out)
check(
    "A blocked move does not burn a torch",
    len(counts) >= 2 and counts[0] == counts[1],
    f"torch count changed across a blocked move: {counts[:2]}",
)

# --------------------------------------------------------------------------
# 2. The lantern must stop torches burning. The in-game text promises this.
# --------------------------------------------------------------------------
out = run(["east", "take", "inventory", "west", "inventory", "quit"])
counts = torch_counts(out)
check(
    "Carrying the lantern stops torches burning",
    len(counts) >= 2 and counts[0] == counts[1],
    f"torch count fell while carrying the lantern: {counts[:2]}",
)

# --------------------------------------------------------------------------
# 3. The torch count must never go below zero.
# --------------------------------------------------------------------------
out = run(["north", "south", "north", "south", "north", "south", "quit"])
negatives = [line for line in out.splitlines() if "Torches left: -" in line]
check(
    "Torch count never goes negative",
    not negatives,
    f"saw a negative torch count: {negatives[:1]}",
)

# --------------------------------------------------------------------------
# 4. Running out of torches ends the game. You must not act after dying.
# --------------------------------------------------------------------------
out = run(["north", "take", "south", "north", "north", "quit"])
if "The dark takes you." in out:
    after = out.split("The dark takes you.", 1)[1]
    check(
        "Nothing happens after the torches run out",
        "You step out into daylight." not in after,
        "the player won the game after already dying in the dark",
    )
else:
    check("Nothing happens after the torches run out", True)

# --------------------------------------------------------------------------
# 5. "Moves taken" must count moves, not every command typed.
#    This run makes exactly 4 moves and types 5 other commands.
# --------------------------------------------------------------------------
out = run(["look", "look", "inventory", "east", "take", "west", "north", "take", "north"])
line = [l for l in out.splitlines() if "Moves taken:" in l]
check(
    "Moves taken counts only movement",
    bool(line) and line[0].strip().endswith("Moves taken: 4"),
    f"expected 4 moves, got: {line[0].strip() if line else 'no line at all'}",
)

# --------------------------------------------------------------------------
# 6. The lantern can only be taken once.
# --------------------------------------------------------------------------
out = run(["east", "take", "take", "quit"])
check(
    "The lantern can only be picked up once",
    out.count("You take the brass lantern.") == 1,
    f"the lantern was picked up {out.count('You take the brass lantern.')} times",
)

# --------------------------------------------------------------------------
# 7. The starting torch count must come from MAX_TORCHES, not be typed twice.
#    We rewrite the constant in a temporary copy and check the intro follows it.
# --------------------------------------------------------------------------
import pathlib
src = pathlib.Path(PROGRAM).read_text(encoding="utf-8")
if "MAX_TORCHES = 3" in src:
    tmp = pathlib.Path("_tmp_maxtorches_check.py")
    tmp.write_text(src.replace("MAX_TORCHES = 3", "MAX_TORCHES = 7", 1), encoding="utf-8")
    proc = subprocess.run([sys.executable, str(tmp)], input="quit\n",
                          capture_output=True, text=True, timeout=10)
    tmp.unlink()
    check(
        "The intro text follows MAX_TORCHES",
        "7 torches" in proc.stdout,
        "changing MAX_TORCHES to 7 did not change the opening message",
    )
else:
    check("The intro text follows MAX_TORCHES", False,
          "could not find 'MAX_TORCHES = 3' to test against")

# --------------------------------------------------------------------------
# 8. The winning path still works. A fix that breaks this is not a fix.
# --------------------------------------------------------------------------
out = run(["east", "take", "west", "north", "take", "north"])
check(
    "The game can still be won",
    "You step out into daylight." in out,
    "the normal winning route no longer wins",
)

# --------------------------------------------------------------------------
print()
print("TORCH RUN TEST RESULTS")
print("=" * 52)
for status, name, detail in results:
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")
print("=" * 52)
print(f"  {passed} passed, {failed} failed, {len(results)} total")
print()
if failed:
    print("  Not done yet. Each failure is one bug you have not found.")
else:
    print("  All tests pass. Now write up what each bug was and why it happened.")
sys.exit(1 if failed else 0)
