# study_service.py
#
# The model service for the study planner. A student types what they have to
# study, this service asks the local model for a plan, and the planner app
# gets back one fixed shape every time.
#
# Endpoints:
#   GET  /health   is the service up
#   POST /plan     {"request": str} -> the response envelope
#
# The envelope, for every outcome:
#   {"ok": bool, "result": {...} or null, "source": str,
#    "elapsed_ms": int, "error": {...} or null}
#
# The result shape:
#   {"title": str, "steps": [str], "minutes": int}
#
# Run it:
#   python study_service.py

import json
import os
import re
import socket
import time
import urllib.error
import urllib.request

from flask import Flask, jsonify, request

SERVICE_NAME = "study-service"
SERVICE_VERSION = "1.0"

MODEL_URL = "http://127.0.0.1:11535"
MODEL_NAME = "llama3.2"
MODEL_API_KEY = "sk-local-ridge-7741"

MODEL_TIMEOUT_SECONDS = 20.0

# The model is asked again up to three times when it does not answer.
MAX_RETRIES = 3

TEMPLATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt_template.txt")

MAX_REQUEST_CHARACTERS = 4000
MAX_TITLE_CHARACTERS = 120
MAX_STEP_CHARACTERS = 160
MIN_STEPS = 2
MAX_STEPS = 8
MIN_MINUTES = 5
MAX_MINUTES = 240

SOURCE_MODEL = "model"
SOURCE_FALLBACK = "fallback"
SOURCE_NONE = "none"

HEALTH_PROBE_TIMEOUT_SECONDS = 0.5

app = Flask(__name__)
app.json.sort_keys = False


def envelope(ok, result, source, elapsed_ms, error=None):
    """The one response shape this service returns."""
    return {
        "ok": ok,
        "result": result,
        "source": source,
        "elapsed_ms": int(elapsed_ms),
        "error": error,
    }


def failure(kind, message):
    return {"kind": kind, "message": message}


def model_reachable():
    """True when something is listening at the model endpoint.

    This opens a socket and closes it. It never asks the model to generate,
    because a health check that costs an inference is a health check nobody
    runs.
    """
    remainder = MODEL_URL.split("://", 1)[1]
    host, port_text = remainder.split(":", 1)
    try:
        with socket.create_connection((host, int(port_text)),
                                      timeout=HEALTH_PROBE_TIMEOUT_SECONDS):
            return True
    except OSError:
        return False


def ask_model(prompt):
    """Send the prompt to the local model and return the answer text."""
    template = open(TEMPLATE_FILE, "r", encoding="utf-8").read()
    body = json.dumps({
        "model": MODEL_NAME,
        "prompt": template.replace("{text}", prompt),
        "stream": False,
    }).encode("utf-8")
    message = urllib.request.Request(
        MODEL_URL + "/api/generate",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MODEL_API_KEY}",
        },
        method="POST",
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(message, timeout=MODEL_TIMEOUT_SECONDS) as response:
        reply = json.loads(response.read().decode("utf-8"))
    if reply.get("done") is not True:
        raise ValueError("the reply does not say done: true")
    text = reply.get("response")
    if not isinstance(text, str) or text.strip() == "":
        raise ValueError("the reply has no response text")
    return text


def parse_plan(text):
    """Pull {"title", "steps", "minutes"} out of the model's answer."""
    fence = re.compile(r"```json\n(.*?)```", re.DOTALL)
    match = fence.search(text)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    steps = [str(step)[:MAX_STEP_CHARACTERS].strip()
             for step in data.get("steps", []) if str(step).strip()]
    return {
        "title": str(data.get("title", ""))[:MAX_TITLE_CHARACTERS].strip(),
        "steps": steps[:MAX_STEPS],
        "minutes": data.get("minutes"),
    }


def validate_plan(plan):
    """The reason this plan is unusable, or None when it is fine."""
    if plan is None:
        return "no study plan could be read out of the answer"
    if plan["title"] == "":
        return "the answer had no title, and the planner screen prints one"
    if len(plan["steps"]) < MIN_STEPS:
        return f"the answer had fewer than {MIN_STEPS} steps"
    if not isinstance(plan["minutes"], int) or isinstance(plan["minutes"], bool):
        return "the answer gave no number of minutes, and the timer needs one"
    if plan["minutes"] < MIN_MINUTES or plan["minutes"] > MAX_MINUTES:
        return f"the answer asked for {plan['minutes']} minutes, outside {MIN_MINUTES} to {MAX_MINUTES}"
    return None


def fallback_plan(text):
    """A plan built here, with no model involved."""
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
    return {
        "title": (first_line[:MAX_TITLE_CHARACTERS] or "Study session").strip(),
        "steps": [
            "Write down the one thing you understand least",
            "Spend the whole session on that one thing",
        ],
        "minutes": 30,
    }


@app.get("/health")
def health():
    return jsonify({
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "status": "ok",
        "model_endpoint": MODEL_URL,
        "model": MODEL_NAME,
        "model_key": MODEL_API_KEY,
        "model_reachable": model_reachable(),
        "checked_by": "tcp_connect",
        "timeout_seconds": MODEL_TIMEOUT_SECONDS,
    })


@app.post("/plan")
def plan():
    started_at = time.monotonic()
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or not isinstance(payload.get("request"), str):
        return jsonify(envelope(False, None, SOURCE_NONE, 0,
                                failure("bad_request",
                                        "the body needs a request field holding a string"))), 400
    text = payload["request"].strip()
    if text == "":
        return jsonify(envelope(False, None, SOURCE_NONE, 0,
                                failure("request_empty",
                                        "the request was empty once whitespace was removed"))), 400
    if len(text) > MAX_REQUEST_CHARACTERS:
        return jsonify(envelope(False, None, SOURCE_NONE, 0,
                                failure("request_too_long",
                                        f"the request is {len(text)} characters. "
                                        f"The limit is {MAX_REQUEST_CHARACTERS}."))), 400

    error = None
    try:
        answer = ask_model(text)
        parsed = parse_plan(answer)
        reason = validate_plan(parsed)
        if reason is None:
            elapsed = (time.monotonic() - started_at) * 1000
            return jsonify(envelope(True, parsed, SOURCE_MODEL, elapsed, None))
        error = failure("plan_validation_failed", reason)
    except urllib.error.HTTPError as http_error:
        error = failure("model_http_error",
                        f"the model server answered with HTTP {http_error.code}")
    except urllib.error.URLError as url_error:
        error = failure("unreachable", f"could not reach the model ({url_error.reason})")
    except (ValueError, OSError) as other:
        error = failure("model_unusable", f"the model answer could not be used ({other})")

    elapsed = (time.monotonic() - started_at) * 1000
    return jsonify(envelope(True, fallback_plan(text), SOURCE_MODEL, elapsed, error))


def main():
    host = os.environ.get("STUDY_SERVICE_HOST", "127.0.0.1")
    port = int(os.environ.get("STUDY_SERVICE_PORT", "5161"))
    print(f"{SERVICE_NAME} {SERVICE_VERSION} on http://{host}:{port}")
    print(f"model endpoint {MODEL_URL}, model {MODEL_NAME}")
    print("Press Ctrl+C to stop.")
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    main()
