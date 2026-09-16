# fake_model.py  .  Gate 2 W13 fixture
#
# A stand-in for a locally hosted, Ollama-compatible model server, so this
# review runs on one machine with nothing else installed.
#
#   POST /api/generate  {"model", "prompt", "stream": false}
#                    -> {"model", "response", "done"}
#
# It is not a model. It matches words and returns fixed shapes.
#
# It listens on 11535, not on 11434. Port 11434 is reserved for a real
# locally hosted model server, and a fixture that fights a real server
# for a port wastes a period. Pass --port anyway, every time. A run
# against somebody else's server on your port looks like a working run.
#
# There is no credential here and none is needed, which is part of what you
# are reviewing.
#
#   python fake_model.py
#   python fake_model.py --mode bare_json
#   python fake_model.py --mode prose
#   python fake_model.py --mode refusal
#   python fake_model.py --mode error
#   python fake_model.py --port 11500
#
# Modes:
#   fenced_json  the answer as JSON inside a ```json code fence
#   bare_json    the same JSON with no fence around it
#   prose        the same answer written as labelled prose
#   refusal      a polite sentence that fits no shape
#   error        HTTP 500
#
# GET /fixture/stats reports how many times it was asked to generate.
#
# Standard library only.

import argparse
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 11535

FENCED_JSON = "fenced_json"
BARE_JSON = "bare_json"
PROSE = "prose"
REFUSAL = "refusal"
ERROR = "error"
MODES = [FENCED_JSON, BARE_JSON, PROSE, REFUSAL, ERROR]

TEXT_PATTERN = re.compile(r"<<<TEXT\n(.*?)\nTEXT", re.DOTALL)
REFUSAL_TEXT = "I am not able to help with that request."


def plan_for(text):
    """A fixed study plan built from whatever the student asked about."""
    subject = " ".join(text.split())[:60] or "your next test"
    return {
        "title": f"Session on {subject}",
        "steps": [
            "Write down the one thing you understand least",
            "Work only on that for the first half",
            "Redo two problems you already got right",
        ],
        "minutes": 45,
    }


def answer_for(mode, prompt):
    match = TEXT_PATTERN.search(prompt)
    text = match.group(1) if match else prompt
    plan = plan_for(text)
    if mode == REFUSAL:
        return REFUSAL_TEXT
    if mode == BARE_JSON:
        return json.dumps(plan)
    if mode == PROSE:
        lines = [f"Title: {plan['title']}"]
        lines.extend("- " + step for step in plan["steps"])
        lines.append(f"Minutes: {plan['minutes']}")
        return "\n".join(lines)
    return "```json\n" + json.dumps(plan, indent=2) + "\n```"


class FakeModelServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=FENCED_JSON, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, FakeModelHandler)
        self.mode = mode
        self.quiet = quiet
        self.generate_calls = 0

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def handle_error(self, request, client_address):
        if not self.quiet:
            super().handle_error(request, client_address)


class FakeModelHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/fixture/stats":
            self.send_json(200, {"generate_calls": self.server.generate_calls,
                                 "mode": self.server.mode})
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/generate":
            self.send_json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            self.send_json(400, {"error": "the body must be a JSON object"})
            return
        if not isinstance(payload, dict) or not isinstance(payload.get("prompt"), str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return

        self.server.generate_calls += 1
        if self.server.mode == ERROR:
            self.send_json(500, {"error": "the fixture failed on purpose"})
            return

        self.send_json(200, {
            "model": payload.get("model", "fixture"),
            "response": answer_for(self.server.mode, payload["prompt"]),
            "done": True,
        })

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            self.close_connection = True

    def log_message(self, format, *args):
        if not self.server.quiet:
            super().log_message(format, *args)


def main():
    parser = argparse.ArgumentParser(description="A stand-in model server for Gate 2 W13.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=FENCED_JSON)
    arguments = parser.parse_args()

    server = FakeModelServer((arguments.host, arguments.port), mode=arguments.mode)
    print(f"fake model on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
