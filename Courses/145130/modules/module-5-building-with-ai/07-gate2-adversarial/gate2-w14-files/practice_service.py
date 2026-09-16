# practice_service.py  .  Gate 2 W15 fixture
#
# A stand-in model service for the Gate 2 review. It speaks the same response
# envelope the shared AI stack speaks, so the program under review is talking
# to the real contract, and it can be told to answer badly on purpose.
#
# It is not the real service. It has no model behind it and it does no
# parsing. It exists so that this review runs on one machine, in one folder,
# with nothing else started.
#
# There is no credential here and none is needed. The model is local.
#
#   python practice_service.py --port 5157
#   python practice_service.py --mode fallback
#   python practice_service.py --mode slow --delay 30
#   python practice_service.py --mode garbage
#   python practice_service.py --port 5099
#
# Modes:
#   model     a normal answer. source is "model".
#   fallback  the service could not use the model. source is "fallback".
#   slow      waits --delay seconds, then answers like fallback.
#   garbage   HTTP 200 with a body that is not the envelope.
#   error     HTTP 500 with the envelope.
#
# Every mode refuses an empty prompt with HTTP 400 and prompt_empty, the way
# the real service does, because one of the things under review is whether
# the program bothers to check before it sends.
#
# Standard library only.

import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5157
DEFAULT_DELAY_SECONDS = 30.0

MODEL = "model"
FALLBACK = "fallback"
SLOW = "slow"
GARBAGE = "garbage"
ERROR = "error"
MODES = [MODEL, FALLBACK, SLOW, GARBAGE, ERROR]

LABELS = ["hardware", "software", "network", "account", "other"]
MAX_PROMPT_CHARACTERS = 4000


def first_sentence(text, limit=140):
    cleaned = " ".join(text.split())
    for stop in (". ", "? "):
        position = cleaned.find(stop)
        if position != -1:
            cleaned = cleaned[:position + 1]
            break
    return cleaned[:limit].strip()


def pick_label(text):
    lowered = text.lower()
    for label, words in (
        ("network", ("wifi", "network", "internet")),
        ("hardware", ("printer", "laptop", "watch", "timer", "shoe")),
        ("software", ("install", "app", "update", "spreadsheet")),
        ("account", ("password", "login", "account")),
    ):
        if any(word in lowered for word in words):
            return label
    return "other"


def envelope(ok, task, result, source, elapsed_ms, error=None):
    return {
        "ok": ok,
        "task": task,
        "result": result,
        "source": source,
        "elapsed_ms": elapsed_ms,
        "error": error,
    }


def model_answer(task, prompt):
    if task == "classify":
        label = pick_label(prompt)
        return {"label": label,
                "confidence_note": f"The note mentions equipment that fits {label}."}
    return {"summary": "Coach note: " + first_sentence(prompt),
            "bullets": [line.strip() for line in prompt.splitlines() if line.strip()][:3]}


def fallback_answer(task, prompt):
    if task == "classify":
        label = pick_label(prompt)
        return {"label": label,
                "confidence_note": f"No model answer. A keyword rule matched {label}."}
    return {"summary": first_sentence(prompt),
            "bullets": [first_sentence(prompt)]}


class PracticeService(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=MODEL, delay_seconds=DEFAULT_DELAY_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, PracticeHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.generate_calls = 0

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def handle_error(self, request, client_address):
        if not self.quiet:
            super().handle_error(request, client_address)


class PracticeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {
                "service": "practice-service",
                "version": "1.0",
                "status": "ok",
                "model_endpoint": "http://127.0.0.1:11535",
                "model": "fixture",
                "model_reachable": self.server.mode == MODEL,
                "checked_by": "fixture",
                "timeout_seconds": 20.0,
                "retries": 1,
                "tasks": ["classify", "summarize"],
                "mode": self.server.mode,
                "generate_calls": self.server.generate_calls,
            })
        else:
            self.send_json(404, envelope(False, "unknown", None, "none", 0,
                                         {"kind": "not_found", "message": "no such endpoint"}))

    def do_POST(self):
        if self.path != "/generate":
            self.send_json(404, envelope(False, "unknown", None, "none", 0,
                                         {"kind": "not_found", "message": "no such endpoint"}))
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            self.send_json(400, envelope(False, "unknown", None, "none", 0,
                                         {"kind": "bad_request",
                                          "message": "the request body must be a JSON object"}))
            return
        if not isinstance(payload, dict):
            self.send_json(400, envelope(False, "unknown", None, "none", 0,
                                         {"kind": "bad_request",
                                          "message": "the request body must be a JSON object"}))
            return

        task = str(payload.get("task", "")).strip().lower()
        prompt = payload.get("prompt")
        if task not in ("summarize", "classify"):
            self.send_json(400, envelope(False, task or "unknown", None, "none", 0,
                                         {"kind": "unknown_task",
                                          "message": f"unknown task '{task}'. Known tasks: classify, summarize"}))
            return
        if not isinstance(prompt, str):
            self.send_json(400, envelope(False, task, None, "none", 0,
                                         {"kind": "bad_request",
                                          "message": "the request needs a prompt field holding a string"}))
            return
        if len(prompt) > MAX_PROMPT_CHARACTERS:
            self.send_json(400, envelope(False, task, None, "none", 0,
                                         {"kind": "prompt_too_long",
                                          "message": f"the prompt is {len(prompt)} characters. The limit is {MAX_PROMPT_CHARACTERS}."}))
            return
        if prompt.strip() == "":
            # Every mode refuses this one. An empty prompt is the caller's
            # mistake and the service never asks the model about it.
            self.send_json(400, envelope(False, task, None, "none", 0,
                                         {"kind": "prompt_empty",
                                          "message": "the prompt was empty once whitespace and control characters were removed"}))
            return

        self.server.generate_calls += 1
        mode = self.server.mode

        if mode == SLOW:
            time.sleep(self.server.delay_seconds)
        if mode == GARBAGE:
            self.send_json(200, {"status": "ok", "data": {"text": "not the envelope"}})
            return
        if mode == ERROR:
            self.send_json(500, envelope(False, task, None, "none", 0,
                                         {"kind": "service_error",
                                          "message": "the service hit an unexpected error"}))
            return
        if mode == MODEL:
            self.send_json(200, envelope(True, task, model_answer(task, prompt), "model", 14, None))
            return
        self.send_json(200, envelope(
            True, task, fallback_answer(task, prompt), "fallback",
            int(self.server.delay_seconds * 1000) if mode == SLOW else 21,
            {"kind": "model_http_error", "message": "the model server answered with HTTP 500"}))

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            # In slow mode the caller has usually given up already. That is
            # the point of slow mode, not an error.
            self.close_connection = True

    def log_message(self, format, *args):
        if not self.server.quiet:
            super().log_message(format, *args)


def main():
    parser = argparse.ArgumentParser(description="A stand-in model service for Gate 2 W15.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=MODEL)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS)
    arguments = parser.parse_args()

    server = PracticeService((arguments.host, arguments.port),
                             mode=arguments.mode, delay_seconds=arguments.delay)
    print(f"practice-service on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
