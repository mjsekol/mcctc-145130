# club_digest.py
#
# Turns the week's robotics club messages into a digest the officers read out
# at the Friday meeting. Each message is sent to the model service to be
# summarized and classified, and the results are printed.
#
# The model runs locally. The service wraps it. This program never reads a
# raw model answer.
#
#   python club_digest.py
#   python club_digest.py --file club_messages.json
#
# The service must already be running.

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

SERVICE_URL_VARIABLE = "DIGEST_SERVICE_URL"
DEFAULT_SERVICE_URL = "http://127.0.0.1:5157"

# Seconds to wait for one answer from the service.
timeout_ms = 45

# How many times to send the same request again when the service says no.
RETRY_ATTEMPTS = 3
RETRY_PAUSE_SECONDS = 2.0

LOG_FILE = "digest_log.txt"

TASKS = ["summarize", "classify"]


def service_url():
    """Where the service is listening."""
    configured = os.environ.get(SERVICE_URL_VARIABLE, "").strip()
    return (configured or DEFAULT_SERVICE_URL).rstrip("/")


def log_everything(message, answer):
    """Keep a copy of what went out and what came back, handy for debugging."""
    with open(LOG_FILE, "a", encoding="utf-8") as handle:
        handle.write(f"{message['id']}\t{message['from']}\t{message['text']}\t{answer}\n")


def ask(url, task, prompt):
    """Send one request to the service. Returns the envelope, or raises."""
    request = urllib.request.Request(
        url + "/generate",
        data=json.dumps({"task": task, "prompt": prompt}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(request, timeout=timeout_ms) as response:
        return json.loads(response.read().decode("utf-8"))


def ask_with_retries(url, task, prompt):
    """Send one request, trying again when the service does not answer well."""
    last_error = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            return ask(url, task, prompt)
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", "replace")
            error.close()
            last_error = f"HTTP {error.code}: {body[:120]}"
            print(f"    attempt {attempt} did not work, trying again")
            time.sleep(RETRY_PAUSE_SECONDS)
        except urllib.error.URLError as error:
            last_error = f"could not reach the service ({error.reason})"
            print(f"    attempt {attempt} did not work, trying again")
            time.sleep(RETRY_PAUSE_SECONDS)
    raise RuntimeError(last_error or "no answer")


def show(envelope):
    """Print one answer from the service."""
    task = envelope.get("task")
    result = envelope.get("result") or {}
    if task == "summarize":
        print(f"    summary: {result.get('summary')}")
        for bullet in result.get("bullets", []):
            print(f"      - {bullet}")
    elif task == "classify":
        print(f"    label:   {result.get('label')}")
        print(f"    note:    {result.get('confidence_note')}")


def run(url, messages):
    """Work through every message and print the digest."""
    from_model = 0
    from_fallback = 0

    for message in messages:
        print()
        print(f"== {message['id']} from {message['from']} ==")
        print(f'   "{message["text"]}"')

        for task in TASKS:
            try:
                envelope = ask_with_retries(url, task, message["text"])
                show(envelope)
                log_everything(message, envelope)
            except Exception:
                pass

        from_model += 1

    print()
    print(f"Digest finished. {from_model} messages summarized by the model, "
          f"{from_fallback} built from the fallback.")
    return 0


def read_messages(path):
    """The messages in a JSON file, or None."""
    if not os.path.isfile(path):
        print(f"No file at {os.path.abspath(path)}.")
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as error:
        print(f"{path} is not valid JSON: {error}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Build the club digest.")
    parser.add_argument("--file", default="club_messages.json")
    arguments = parser.parse_args()

    url = service_url()
    print(f"club_digest . service {url}")

    messages = read_messages(arguments.file)
    if messages is None:
        return 2
    print(f"Reading {len(messages)} club messages from {arguments.file}")
    return run(url, messages)


if __name__ == "__main__":
    sys.exit(main())
