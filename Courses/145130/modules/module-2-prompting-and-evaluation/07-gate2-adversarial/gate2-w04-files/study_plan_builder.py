# study_plan_builder.py
#
# Turns a list of study topics into study plans using the club's locally
# hosted model. Written for the Media Club study hall.
#
# Usage:
#   python study_plan_builder.py
#   python study_plan_builder.py --topics topics.txt --out plans.md
#
# Start the model first. The stub in 05-labs/prompt-toolkit works:
#   python stub_model_server.py

import argparse
import json
import pathlib
import urllib.error
import urllib.request

ENDPOINT = "http://127.0.0.1:11434/api/generate"
MODEL = "stub-caricature"
TIMEOUT_SECONDS = 20
MAX_TOPIC_LENGTH = 80
BANNED_NAMES_FILE = "banned_names.txt"
PROMPT_LOG = "sent_prompts.log"


def load_topics(path):
    """Read the topics file, one topic per line, skipping blank lines."""
    lines = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def load_banned_names():
    """Load the roster of names that must never reach the model."""
    path = pathlib.Path(BANNED_NAMES_FILE)
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()}


def screen_topic(topic):
    """Return an error message, or None if this topic is safe to send.

    Personal data must never reach the model, so every topic is screened
    against the roster before the prompt is built.
    """
    if len(topic) >= MAX_TOPIC_LENGTH:
        return f"topic is {len(topic)} characters, over the {MAX_TOPIC_LENGTH} limit"
    banned = load_banned_names()
    if topic.split()[0] in banned:
        return "topic contains a student name"
    return None


def build_prompt(topic):
    """Build the prompt for one topic."""
    return (
        "You are a study skills teacher.\n"
        f"Write a study plan for this topic: {topic}\n"
        "Give me 5 steps in a numbered list, under 60 words. "
        "Return only JSON, no other text, with keys topic, steps."
    )


def ask_model(prompt):
    """Send one prompt and return the parsed plan, or None if it failed."""
    body = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode("utf-8")
    request = urllib.request.Request(ENDPOINT, data=body,
                                     headers={"Content-Type": "application/json"},
                                     method="POST")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            reply = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, ValueError, TimeoutError) as error:
        print(f"  model call failed: {error}")
        return None

    text = reply.get("response", "")
    try:
        # Validate the reply before using it.
        validated = json.loads(text)
    except ValueError:
        print("  the reply was not JSON")
        return None
    return validated


def write_plans(plans, path):
    """Write one section per topic to the output file."""
    lines = ["# Study plans", ""]
    for topic, plan in plans:
        lines.append(f"## {topic}")
        lines.append("")
        for number, step in enumerate(plan.get("steps", []), 1):
            lines.append(f"{number}. {step}")
        lines.append("")
    pathlib.Path(path).write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build study plans from a topic list.")
    parser.add_argument("--topics", default="topics.txt")
    parser.add_argument("--out", default="plans.md")
    arguments = parser.parse_args()

    topics = load_topics(arguments.topics)
    print(f"{len(topics)} topics loaded from {arguments.topics}")

    plans = []
    failed = []
    log = open(PROMPT_LOG, "w", encoding="utf-8")
    for topic in topics:
        problem = screen_topic(topic)
        if problem is not None:
            print(f"  skipped: {problem}")
            failed.append(topic)
            continue
        prompt = build_prompt(topic)
        log.write(prompt + "\n" + ("-" * 60) + "\n")
        plan = ask_model(prompt)
        if plan is None:
            failed.append(topic)
            continue
        plans.append((topic, plan))
    log.close()

    write_plans(plans, arguments.out)
    print(f"{len(plans)} plans written to {arguments.out}, {len(failed)} skipped or failed")


if __name__ == "__main__":
    main()
