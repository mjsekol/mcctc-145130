"""Study Buddy: turn a page of notes into a flashcard deck.

Invented project. Part of the MCCTC 145130 Module 3 licensing audit fixture.

Run:
    python study_buddy.py notes/chemistry.txt
    python study_buddy.py notes/chemistry.txt --hints --port 11634

The --hints flag asks a locally hosted, Ollama-compatible model for a plainer
restatement of each definition. If no model is reachable, Study Buddy says so
and writes the deck without hints. It never reports a failure as "no hints
needed", because that would be a lie the user cannot see.

ALWAYS PASS --port. The default below is 11634, which is this module's port and
is not the port a real Ollama listens on. Relying on a default is how a run
against the wrong server ends up looking like a working run, which is the worst
kind of failure because nothing on the screen says anything is wrong.
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from make_cards import build_cards
from snippets.shuffle_from_blog import shuffle_in_place
from vendor.pocketgrid.pocketgrid import format_table

DEFAULT_PORT = 11634
MODEL_HOST = "127.0.0.1"
MODEL_NAME = "lantern-small"
TIMEOUT_SECONDS = 8

MODEL_URL = f"http://{MODEL_HOST}:{DEFAULT_PORT}/api/generate"


def model_url(port):
    """The endpoint for one port. Everything network goes through here."""
    return f"http://{MODEL_HOST}:{port}/api/generate"


def read_port(argv):
    """Read --port N. Refuse a missing or non-numeric value rather than guessing."""
    if "--port" not in argv:
        return DEFAULT_PORT
    index = argv.index("--port")
    if index + 1 >= len(argv):
        raise ValueError("--port needs a number after it, for example --port 11634")
    return int(argv[index + 1])


def ask_for_hint(definition, port):
    """Ask the local model for a plainer restatement. Return None on any failure."""
    payload = json.dumps({
        "model": MODEL_NAME,
        "prompt": "Restate this in plainer words, one sentence: " + definition,
        "stream": False,
    }).encode("utf-8")
    request = urllib.request.Request(
        model_url(port), data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            reply = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None
    # A reply that is not finished is not a hint. Refuse it rather than print half.
    if reply.get("done") is not True:
        return None
    text = reply.get("response")
    if not isinstance(text, str) or not text.strip():
        return None
    return text.strip()


def main(argv):
    if len(argv) < 2:
        print("Usage: python study_buddy.py <notes file> [--hints] [--port N]")
        return 1

    notes_path = Path(argv[1])
    want_hints = "--hints" in argv[2:]
    try:
        port = read_port(argv)
    except ValueError as error:
        print(error)
        return 1

    if not notes_path.exists():
        print(f"No notes file at {notes_path}. Check the path and try again.")
        return 1

    lines = notes_path.read_text(encoding="utf-8").splitlines()
    cards = build_cards(lines)
    if not cards:
        print("No term and definition lines found. Each line needs a colon in it.")
        return 1

    hints_requested = 0
    hints_written = 0
    if want_hints:
        for card in cards:
            hints_requested += 1
            hint = ask_for_hint(card["definition"], port)
            if hint is not None:
                card["hint"] = hint
                hints_written += 1
        if hints_written == 0:
            print(
                "No model answered at "
                f"{model_url(port)}. The deck was written without hints. "
                "This is a model problem, not an empty result."
            )

    shuffle_in_place(cards, seed=7)

    out_path = notes_path.with_name("deck.json")
    out_path.write_text(json.dumps(cards, indent=2), encoding="utf-8")

    rows = [[card["term"], card["definition"][:34]] for card in cards[:5]]
    print(format_table(["Term", "Definition (first 34 characters)"], rows))
    print(f"\n{len(cards)} cards written to {out_path}")
    if want_hints:
        print(f"Hints requested: {hints_requested}. Hints written: {hints_written}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
