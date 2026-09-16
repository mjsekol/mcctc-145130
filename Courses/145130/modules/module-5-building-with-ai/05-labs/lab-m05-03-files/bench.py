# bench.py  .  Lab M05-03, The Broken Integration
#
# A small bench client for a model service. It reads help requests and asks the
# service for a headline for each one, then prints what came back.
#
# This program was written by somebody who finished the wiring and stopped
# there. It runs. It is also one of the things you are diagnosing this week, so
# read what it prints against what actually happened.
#
# Standard library only. No credential, because the service needs none.
#
#   python bench.py
#   python bench.py --text "the wifi drops in the back row"
#   python bench.py --file requests.json
#
# The service URL comes from DEMO_SERVICE_URL, or the module's default port.

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

SERVICE_URL_VARIABLE = "DEMO_SERVICE_URL"
DEFAULT_SERVICE_URL = "http://127.0.0.1:5157"

# How long this program waits for one answer from the service.
CLIENT_TIMEOUT_SECONDS = 60.0

TASK = "headline"


def service_url():
    configured = os.environ.get(SERVICE_URL_VARIABLE, "").strip()
    return (configured or DEFAULT_SERVICE_URL).rstrip("/")


def ask(url, task, prompt):
    """One request to the service. Returns the parsed envelope."""
    request = urllib.request.Request(
        url + "/generate",
        data=json.dumps({"task": task, "prompt": prompt}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(request, timeout=CLIENT_TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def show(envelope):
    """Print one answer."""
    result = envelope.get("result") or {}
    print(f"  [{envelope.get('task')}] OK in {envelope.get('elapsed_ms')} ms")
    print(f"  headline: {result.get('headline')}")


def run_one(url, text, label):
    print()
    print(f"== {label} ==")
    print(f'  "{text[:88]}"')
    try:
        show(ask(url, TASK, text))
    except Exception as error:
        print(f"  [{TASK}] finished with a problem, carrying on: {error}")


DEFAULT_REQUESTS = [
    ("MR-2101 invented sample, not a real person",
     "The 3D printer in room 118 stopped in the middle of a print and the filament jammed."),
    ("MR-2102 invented sample, not a real person",
     "My laptop keeps dropping the wifi in the back corner of the lab."),
    ("MR-2103 invented sample, not a real person",
     "Visual Studio will not install the workload on station 6 and rolls back at 40 percent."),
    ("MR-2104 invented sample, not a real person",
     "I am locked out of my account after changing my password on Monday."),
]


def main():
    parser = argparse.ArgumentParser(description="Bench client for the model service.")
    parser.add_argument("--text", help="one message to run instead of the built-in four")
    parser.add_argument("--file", help="a JSON array of {id, text} objects")
    arguments = parser.parse_args()

    url = service_url()
    print(f"bench . service {url}")
    started_at = time.monotonic()

    if arguments.text:
        run_one(url, arguments.text, "typed at the command line")
    elif arguments.file:
        with open(arguments.file, "r", encoding="utf-8") as handle:
            for item in json.load(handle):
                run_one(url, item["text"], item.get("id", "no id"))
    else:
        for label, text in DEFAULT_REQUESTS:
            run_one(url, text, label)

    print()
    print(f"bench finished in {time.monotonic() - started_at:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
