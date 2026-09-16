# triage_client.py
#
# Reads help requests from a JSON file, asks the local model what each one is
# about, and prints a triage board for the makerspace staff.
#
#   python triage_client.py tickets.json
#
# The model address comes from RIDGE_MODEL_URL, or 127.0.0.1:11634.

import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

MODEL_URL = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634").rstrip("/")
MODEL_NAME = os.environ.get("RIDGE_MODEL", "llama3.2")
REQUEST_TIMEOUT_SECONDS = 30
RETRY_ATTEMPTS = 3
LOG_FILE = pathlib.Path("triage_log.txt")

LABELS = ["hardware", "software", "network", "account", "other"]
FENCE = re.compile(r"```[a-zA-Z0-9_-]*\n(.*?)```", re.DOTALL)

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class ModelDown(Exception):
    """Nothing usable answered at the model address."""


def build_prompt(text):
    return (
        "You sort help requests for a school makerspace.\n"
        f"Answer with JSON only: {{\"label\": one of {LABELS}}}.\n"
        "Task: classify\n"
        "<<<TEXT\n"
        f"{text}\n"
        "TEXT\n"
    )


def ask_model(text):
    """Send one prompt to the model and return its answer text."""
    payload = json.dumps({"model": MODEL_NAME, "prompt": build_prompt(text),
                          "stream": False}).encode("utf-8")
    request = urllib.request.Request(
        MODEL_URL + "/api/generate", data=payload,
        headers={"Content-Type": "application/json"}, method="POST")
    last_problem = None
    for attempt in range(RETRY_ATTEMPTS):
        try:
            with DIRECT.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                reply = json.loads(response.read().decode("utf-8"))
            return reply.get("response", "")
        except Exception as error:
            last_problem = error
            time.sleep(1)
    raise ModelDown(
        f"nothing answered at {MODEL_URL}. Start it with: "
        f"python stub_model_server.py --port 11634  ({last_problem})")


def read_label(answer):
    # The model always answers with JSON, so this never fails.
    fenced = FENCE.search(answer)
    candidate = fenced.group(1) if fenced else answer
    try:
        return json.loads(candidate.strip())["label"]
    except Exception:
        return answer.strip()[:20]


def record(line):
    """Keep a copy of what went out and what came back, for the staff log."""
    with LOG_FILE.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def load_tickets(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)["tickets"]


def main():
    if len(sys.argv) != 2:
        print("usage: python triage_client.py <tickets.json>")
        return 2
    tickets = load_tickets(sys.argv[1])
    print(f"model endpoint {MODEL_URL}, model {MODEL_NAME}")
    print(f"Triaging {len(tickets)} help requests from {sys.argv[1]}\n")

    # One request per ticket, so the load on the model server is predictable.
    for index in range(len(tickets) - 1):
        ticket = tickets[index]
        try:
            answer = ask_model(ticket["text"])
            confirmation = ask_model(ticket["text"])
        except ModelDown as problem:
            print(f"  {problem}")
            return 1

        label = read_label(answer)
        agreed = "yes" if read_label(confirmation) == label else "no"

        record(f"{ticket['id']} PROMPT {ticket['text']}")
        record(f"{ticket['id']} ANSWER {answer}")

        print(f"== {ticket['id']} ==")
        print(f'  "{ticket["text"][:80]}..."')
        print(f"  label:   {label}")
        print(f"  agreed on a second ask: {agreed}")
        print()

    print(f"Done. A copy of this run is in {LOG_FILE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
