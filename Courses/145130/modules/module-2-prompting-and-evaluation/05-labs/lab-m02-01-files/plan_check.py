# plan_check.py  ·  starter for Lab M02-01, Part 4
#
# Asks the local model for a study plan, then decides whether the reply is
# usable. Right now it decides that everything is usable, which is the bug you
# are here to fix.
#
# Run it:
#   python plan_check.py "how a hash table handles a collision"
#   python plan_check.py --loose "how a hash table handles a collision"
#
# Start the stub first, in a second terminal, from 05-labs/prompt-toolkit:
#   python stub_model_server.py

import argparse
import json
import pathlib
import sys

# Find the toolkit by walking up from this file until a prompt-toolkit folder
# turns up. Doing it this way means the program still works if you copy it
# somewhere else, which you will.
def find_toolkit():
    for folder in pathlib.Path(__file__).resolve().parents:
        candidate = folder / "prompt-toolkit"
        if (candidate / "ask.py").exists():
            return candidate
    raise SystemExit("Could not find prompt-toolkit above this file. "
                     "Keep this program inside 05-labs.")


sys.path.insert(0, str(find_toolkit()))

import ask   # noqa: E402

ENDPOINT = "http://127.0.0.1:11434"
MODEL = "stub-caricature"
REQUIRED_STEPS = 4


def build_prompt(topic, loose):
    """Build the prompt for one topic.

    Two versions on purpose. Step 18 asks you to run both and compare what
    comes back, because the difference between them is four words.
    """
    shape = ("Return JSON with keys topic, steps."
             if loose else
             "Return only JSON, no other text, with keys topic, steps.")
    return (
        "You are a study skills teacher.\n"
        f"Write a study plan for this topic: {topic}\n"
        f"Give me {REQUIRED_STEPS} steps in a numbered list, under 60 words. "
        + shape
    )


def usable(data):
    """Return an error message, or None if this reply can be used.

    STEP 19: this is the function you write.

    Right now it approves everything, including replies that would break the
    program that uses them. That is not a placeholder to be polite about. A
    validator that always says yes is worse than no validator, because the
    next person reads the call and believes the data was checked.

    It must catch all of these:
      - the reply is not a JSON object at all
      - there is no 'topic', or it is empty
      - there is no 'steps', or it is not a list
      - 'steps' does not have exactly REQUIRED_STEPS items
      - any step is not text, or is blank
    """
    return None


def main():
    parser = argparse.ArgumentParser(description="Ask for a study plan and check the reply.")
    parser.add_argument("topic")
    parser.add_argument("--loose", action="store_true",
                        help="ask for JSON without the word only, to see what changes")
    parser.add_argument("--endpoint", default=ENDPOINT)
    parser.add_argument("--timeout", type=float, default=20.0)
    arguments = parser.parse_args()

    prompt = build_prompt(arguments.topic, arguments.loose)
    try:
        text, elapsed, _ = ask.send(prompt, arguments.endpoint, MODEL, arguments.timeout)
    except ask.AskError as error:
        # ask.send() raises a different code for each way the call can fail.
        # STEP 21 asks you to cause every one of them and record what happened.
        print(f"FAILED ({error.message})")
        if error.detail:
            print(f"  {error.detail}")
        return error.code

    print(f"reply in {elapsed:.2f}s, {len(text.split())} words")

    try:
        data = json.loads(text)
    except ValueError:
        print("UNUSABLE: the reply is not JSON")
        print("-" * 60)
        print(text[:200])
        print("-" * 60)
        return 4

    problem = usable(data)
    if problem is not None:
        print(f"UNUSABLE: {problem}")
        return 5

    print(f"OK: {data['topic']}")
    for number, step in enumerate(data["steps"], 1):
        print(f"  {number}. {step}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
