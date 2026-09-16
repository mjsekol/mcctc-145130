# contract_probe.py  .  Module 5
#
# Sends one request to a model service and prints the response envelope one
# field at a time, with the meaning of each field next to it, in the order the
# contract documents them.
#
# Why this exists: a finished application reads the envelope so fast that you
# never see it. This prints it slowly, so you fill in the trace table by
# reading rather than guessing. It also prints `error.kind` and
# `error.message` in full, which your own program probably will not, and which
# is the field that separates faults that look identical.
#
# Nothing here talks to a model. It talks to the service, which is the point:
# the service is the only thing your application is ever allowed to know about.
#
# Standard library only. There is no credential in this file and the service
# needs none, because the model is local.
#
# Run it with the service already running:
#   python contract_probe.py health
#   python contract_probe.py headline --text "the 3D printer jammed again"
#   python contract_probe.py headline --text "..." --raw
#   python contract_probe.py bad-task
#   python contract_probe.py long-prompt
#   python contract_probe.py empty-prompt
#
# The service URL comes from DEMO_SERVICE_URL, or defaults to 5157, which is
# the port this module runs a service on. Pass the port explicitly every time.
# A client pointed at somebody else's server on a default port does not fail.
# It answers, and the answers look fine.
#
# Exit code 0 means the probe got an answer it could read. Exit code 1 means it
# could not reach the service at all.

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

SERVICE_URL_VARIABLE = "DEMO_SERVICE_URL"
DEFAULT_SERVICE_URL = "http://127.0.0.1:5157"
REQUEST_TIMEOUT_SECONDS = 60.0

# What each envelope field is for. Printed beside the value so you are reading
# the contract while you read the answer.
FIELD_NOTES = [
    ("ok", "true when result holds a usable answer, from the model or the fallback"),
    ("task", "the task that ran, echoed back to you"),
    ("result", "the task result shape, or null when ok is false"),
    ("source", "model, fallback, or none. Read this one first."),
    ("elapsed_ms", "milliseconds the service spent, including any retry"),
    ("error", "kind and message, or null"),
]


def service_url():
    """Where the service is. Configuration, never a value typed into the code."""
    configured = os.environ.get(SERVICE_URL_VARIABLE, "").strip()
    return (configured or DEFAULT_SERVICE_URL).rstrip("/")


def opener():
    # An empty ProxyHandler means never use a proxy. The service is on this
    # machine. A school web proxy would fail on 127.0.0.1 and has no business
    # seeing what anybody typed.
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def post_json(url, payload):
    """POST one JSON body. Returns (status, body_text). Raises OSError if unreachable."""
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with opener().open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        error.close()
        return error.code, body


def get_json(url):
    """GET one URL. Returns (status, body_text). Raises OSError if unreachable."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with opener().open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        error.close()
        return error.code, body


def shorten(value, limit=68):
    """One line, short enough to sit in a table cell."""
    text = value if isinstance(value, str) else json.dumps(value)
    text = " ".join(text.split())
    return text if len(text) <= limit else text[:limit] + "..."


def print_envelope(status, body_text, show_raw):
    """Print the envelope field by field. Returns True if it was readable."""
    print(f"  HTTP status    {status}")
    try:
        envelope = json.loads(body_text)
    except json.JSONDecodeError:
        print("  The body was not JSON at all. You are probably pointed at the")
        print("  wrong port. First 120 characters received:")
        print("  " + shorten(body_text, 120))
        return False
    if not isinstance(envelope, dict):
        print("  The body was JSON, but not an object. This is not the envelope.")
        return False

    missing = [name for name, _ in FIELD_NOTES if name not in envelope]
    for name, meaning in FIELD_NOTES:
        value = envelope.get(name, "<missing>")
        print(f"  {name:<11}  {shorten(value):<72}  {meaning}")
    if missing:
        print(f"  Missing fields: {', '.join(missing)}. That is not the envelope.")

    result = envelope.get("result")
    if isinstance(result, dict):
        print("  result in full:")
        for name, value in result.items():
            if isinstance(value, list):
                print(f"    {name}:")
                for item in value:
                    print(f"      - {item}")
            else:
                print(f"    {name}: {value}")

    error_object = envelope.get("error")
    if isinstance(error_object, dict):
        # Printed in full and never shortened. The kind is what a program
        # branches on, and the message often carries the one number that
        # separates two faults with the same symptom.
        print(f"  error kind:    {error_object.get('kind')}")
        print(f"  error message: {error_object.get('message')}")

    if show_raw:
        print("\n  raw body:")
        print(json.dumps(envelope, indent=2))
    return not missing


def read_verdict(envelope_text):
    """The one sentence the trace table wants in its last column."""
    try:
        envelope = json.loads(envelope_text)
    except json.JSONDecodeError:
        return "unreadable: the body was not JSON"
    source = envelope.get("source")
    error = envelope.get("error") or {}
    if source == "model":
        return "the model answered and the answer fit the task"
    if source == "fallback":
        return f"the service built the answer without the model ({error.get('kind')})"
    if source == "none":
        return f"the service refused the request ({error.get('kind')})"
    return f"unknown source {source!r}. This is not the envelope."


def run_health(url):
    status, body = get_json(url + "/health")
    print(f"  HTTP status    {status}")
    try:
        report = json.loads(body)
    except json.JSONDecodeError:
        print("  The body was not JSON. Check the port.")
        return False
    for name in ("service", "version", "status", "model_endpoint", "model",
                 "model_reachable", "checked_by", "timeout_seconds", "retries", "tasks"):
        print(f"  {name:<16} {shorten(report.get(name, '<missing>'))}")
    if report.get("model_reachable") is False:
        print()
        print("  The service is up and cannot see a model. Every answer will be a")
        print("  fallback. That is a different problem from the service being down,")
        print("  and it has a different fix.")
    return True


def run_generate(url, task, text, show_raw):
    print(f"  request        {json.dumps({'task': task, 'prompt': shorten(text, 48)})}")
    status, body = post_json(url + "/generate", {"task": task, "prompt": text})
    readable = print_envelope(status, body, show_raw)
    print(f"  verdict        {read_verdict(body)}")
    return readable


def main():
    parser = argparse.ArgumentParser(
        description="Print one model service envelope, field by field.")
    parser.add_argument("command",
                        choices=["health", "headline", "bad-task",
                                 "long-prompt", "empty-prompt"])
    parser.add_argument("--text",
                        default="The 3D printer in room 118 jammed near the nozzle.")
    parser.add_argument("--raw", action="store_true", help="also print the whole body")
    arguments = parser.parse_args()

    url = service_url()
    print(f"contract_probe . service {url}")
    print()
    try:
        if arguments.command == "health":
            run_health(url)
        elif arguments.command == "bad-task":
            run_generate(url, "translate", "hola", arguments.raw)
        elif arguments.command == "long-prompt":
            run_generate(url, "headline", "a" * 4001, arguments.raw)
        elif arguments.command == "empty-prompt":
            run_generate(url, "headline", "    ", arguments.raw)
        else:
            run_generate(url, arguments.command, arguments.text, arguments.raw)
    except OSError as error:
        print("  Nothing answered.")
        print(f"  {error}")
        print(f"  Start the service, or set {SERVICE_URL_VARIABLE} to where it is listening.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
