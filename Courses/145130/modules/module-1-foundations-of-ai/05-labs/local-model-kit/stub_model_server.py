# stub_model_server.py  .  145130 shared AI stack
#
# A stand-in for a locally hosted, Ollama-compatible model server. It answers
# the two endpoints this course uses, with no model behind it:
#
#   POST /api/generate     {"model", "prompt", "stream": false}
#                       -> {"model", "response", "done"}
#   POST /api/embeddings   {"model", "prompt"}
#                       -> {"embedding": [float, ...]}
#
# Why this exists: no model runtime is installed on the build machine, and a
# lab period is too short to debug a model and an application at the same
# time. The stub lets you run the whole stack today, and it lets you make the
# model fail on purpose so you can watch the failure handling work.
#
# There is no API key here, and there never should be. A local model needs none.
#
# Usage:
#   python stub_model_server.py                            success mode, port 11434
#   python stub_model_server.py --mode slow --delay 30     answers too late
#   python stub_model_server.py --port 11500 --mode error
#
# Modes:
#   success           fenced JSON that matches the requested task
#   success_prose     the same answer as prose, with no JSON anywhere
#   unusable          a polite refusal that fits no task shape
#   slow              waits --delay seconds, then answers like success
#   error             HTTP 500
#   rate_limited      HTTP 429 with a Retry-After header
#   malformed         status 200, but the body is broken JSON
#   not_done          valid JSON with done: false
#   missing_response  valid JSON with no "response" field
#   empty_response    valid JSON whose response is only spaces
#
# Extra endpoints, which a real server does not have:
#   GET  /stub/stats   {"generate_calls": 3, "embeddings_calls": 0, "mode": "success"}
#   POST /stub/mode    send {"mode": "error"} to switch modes while running
#   POST /stub/reset   zero the counters

import argparse
import hashlib
import json
import re
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_HOST = "127.0.0.1"   # loopback only: nobody else on the network can reach it
DEFAULT_PORT = 11434         # the port Ollama listens on by default
DEFAULT_DELAY_SECONDS = 30.0
RETRY_AFTER_SECONDS = 1

SUCCESS = "success"
SUCCESS_PROSE = "success_prose"
UNUSABLE = "unusable"
SLOW = "slow"
ERROR = "error"
RATE_LIMITED = "rate_limited"
MALFORMED = "malformed"
NOT_DONE = "not_done"
MISSING_RESPONSE = "missing_response"
EMPTY_RESPONSE = "empty_response"
MODES = [SUCCESS, SUCCESS_PROSE, UNUSABLE, SLOW, ERROR, RATE_LIMITED,
         MALFORMED, NOT_DONE, MISSING_RESPONSE, EMPTY_RESPONSE]

GENERATE_PATH = "/api/generate"
EMBEDDINGS_PATH = "/api/embeddings"
STATS_PATH = "/stub/stats"
MODE_PATH = "/stub/mode"
RESET_PATH = "/stub/reset"

# The service puts a line like "Task: summarize" in every prompt, and wraps
# the untrusted text between <<<TEXT and TEXT. The stub reads both so its
# answer matches what was asked, which makes an end to end run mean something.
TASK_PATTERN = re.compile(r"^Task: ([a-z_]+)$", re.MULTILINE)
TEXT_PATTERN = re.compile(r"<<<TEXT\n(.*?)\nTEXT", re.DOTALL)

REFUSAL = "I am not able to help with that request."

# Keyword to label, for the classify task. A real model reasons. The stub
# scans for words, which is enough to prove the plumbing.
LABEL_KEYWORDS = [
    ("network", ("wifi", "wi-fi", "network", "ethernet", "internet", "vpn")),
    ("hardware", ("printer", "laptop", "screen", "monitor", "keyboard", "battery", "cable", "3d")),
    ("software", ("install", "visual studio", "python", "update", "crash", "driver", "app")),
    ("account", ("password", "login", "log in", "sign in", "locked out", "account")),
]
DEFAULT_LABEL = "other"

EMBEDDING_DIMENSIONS = 32


def first_sentence(text, limit=160):
    """The first sentence of a block of text, shortened if it runs long."""
    cleaned = " ".join(text.split())
    if cleaned == "":
        return "no text was supplied"
    for stop in (". ", "? "):
        position = cleaned.find(stop)
        if position != -1:
            cleaned = cleaned[:position + 1]
            break
    return cleaned[:limit].strip()


def useful_lines(text, count=3):
    """Up to `count` non-empty lines, shortened, for stub bullet points."""
    lines = [" ".join(line.split()) for line in text.splitlines()]
    lines = [line for line in lines if line != ""]
    return [line[:90] for line in lines[:count]] or ["the text had no lines to list"]


def pick_label(text):
    """The first label whose keywords appear in the text."""
    lowered = text.lower()
    for label, keywords in LABEL_KEYWORDS:
        for keyword in keywords:
            if keyword in lowered:
                return label
    return DEFAULT_LABEL


def stub_answer(prompt, as_json=True):
    """Build the text a cooperative model would return for this prompt."""
    task_match = TASK_PATTERN.search(prompt)
    task = task_match.group(1) if task_match else "summarize"
    text_match = TEXT_PATTERN.search(prompt)
    text = text_match.group(1) if text_match else prompt

    if task == "classify":
        label = pick_label(text)
        note = f"Stub match on the words in the message. Best fit is {label}."
        if as_json:
            return "```json\n" + json.dumps({"label": label, "confidence_note": note}) + "\n```"
        return f"Label: {label}\nWhy: {note}"

    summary = "Stub summary: " + first_sentence(text)
    bullets = useful_lines(text)
    if as_json:
        return "```json\n" + json.dumps({"summary": summary, "bullets": bullets}, indent=2) + "\n```"
    lines = [summary, ""]
    lines.extend("- " + bullet for bullet in bullets)
    return "\n".join(lines)


def deterministic_embedding(text, dimensions=EMBEDDING_DIMENSIONS):
    """A stable vector for a piece of text, for the retrieval work in Module 4.

    The same text always gives the same vector, and different text gives a
    different one. It carries no meaning, so two sentences that mean the same
    thing are not close together. That is the whole reason a retrieval lab
    built on the stub can only test the plumbing, never the quality.
    """
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    raw = []
    while len(raw) < dimensions:
        for byte in digest:
            raw.append(byte / 255.0 - 0.5)
            if len(raw) == dimensions:
                break
        digest = hashlib.sha256(digest).digest()
    length = sum(value * value for value in raw) ** 0.5
    if length == 0:
        return [0.0] * dimensions
    return [round(value / length, 6) for value in raw]


class StubModelServer(ThreadingHTTPServer):
    """An HTTP server that remembers its mode and counts the calls it answered."""

    # Handler threads must not keep the program alive, and closing the server
    # must not wait for a slow reply that is sleeping on purpose.
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, StubHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.generate_calls = 0
        self.embeddings_calls = 0
        self.prompts = []
        # Several requests can arrive at once, each on its own thread. The
        # lock stops two of them updating a count at the same moment.
        self.lock = threading.Lock()

    @property
    def base_url(self):
        host, port = self.server_address[0], self.server_address[1]
        return f"http://{host}:{port}"

    def handle_error(self, request, client_address):
        # A client that gives up and hangs up makes the standard server print
        # a traceback. During tests that is noise, not information.
        if not self.quiet:
            super().handle_error(request, client_address)

    def record_generate(self, prompt):
        with self.lock:
            self.generate_calls += 1
            self.prompts.append(prompt)

    def record_embeddings(self):
        with self.lock:
            self.embeddings_calls += 1

    def reset_counts(self):
        with self.lock:
            self.generate_calls = 0
            self.embeddings_calls = 0
            self.prompts = []


class StubHandler(BaseHTTPRequestHandler):

    # HTTP/1.0 on purpose. Each request gets its own connection, so a reply
    # that is slow or broken on purpose cannot leave a reused connection in a
    # confusing state for the next request.

    def do_GET(self):
        if self.path == STATS_PATH:
            self.send_json(200, {
                "generate_calls": self.server.generate_calls,
                "embeddings_calls": self.server.embeddings_calls,
                "mode": self.server.mode,
            })
        elif self.path == "/":
            self.send_text(200, "Stub model server is running")
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        request = self.read_json_body()
        if request is None:
            self.send_json(400, {"error": "the request body must be a JSON object"})
            return
        if self.path == MODE_PATH:
            self.change_mode(request)
        elif self.path == RESET_PATH:
            self.server.reset_counts()
            self.send_json(200, {"generate_calls": 0, "embeddings_calls": 0})
        elif self.path == GENERATE_PATH:
            self.generate(request)
        elif self.path == EMBEDDINGS_PATH:
            self.embeddings(request)
        else:
            self.send_json(404, {"error": "not found"})

    def change_mode(self, request):
        mode = request.get("mode")
        if mode not in MODES:
            self.send_json(400, {"error": f"mode must be one of {MODES}"})
            return
        self.server.mode = mode
        self.send_json(200, {"mode": mode})

    def generate(self, request):
        # Reject a request a real server would not handle the way the service
        # expects. This is how the stub catches a mistake in the client.
        prompt = request.get("prompt")
        model = request.get("model")
        if not isinstance(prompt, str) or not isinstance(model, str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return
        if request.get("stream") is not False:
            self.send_json(400, {"error": "this stub only supports stream: false"})
            return

        self.server.record_generate(prompt)
        mode = self.server.mode
        if mode == SLOW:
            time.sleep(self.server.delay_seconds)

        if mode == ERROR:
            self.send_json(500, {"error": "the stub failed on purpose"})
            return
        if mode == RATE_LIMITED:
            self.send_json(429, {"error": "too many requests"},
                           extra_headers={"Retry-After": str(RETRY_AFTER_SECONDS)})
            return
        if mode == MALFORMED:
            self.send_raw(200, b'{"model": "stub", "response": "the answer was cut off',
                          "application/json")
            return

        if mode == UNUSABLE:
            text = REFUSAL
        elif mode == SUCCESS_PROSE:
            text = stub_answer(prompt, as_json=False)
        else:
            text = stub_answer(prompt, as_json=True)

        reply = {
            "model": model,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "response": text,
            "done": True,
        }
        if mode == NOT_DONE:
            reply["done"] = False
        elif mode == MISSING_RESPONSE:
            del reply["response"]
        elif mode == EMPTY_RESPONSE:
            reply["response"] = "   "
        self.send_json(200, reply)

    def embeddings(self, request):
        prompt = request.get("prompt")
        model = request.get("model")
        if not isinstance(prompt, str) or not isinstance(model, str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return
        self.server.record_embeddings()
        mode = self.server.mode
        if mode == SLOW:
            time.sleep(self.server.delay_seconds)
        if mode == ERROR:
            self.send_json(500, {"error": "the stub failed on purpose"})
            return
        if mode == RATE_LIMITED:
            self.send_json(429, {"error": "too many requests"},
                           extra_headers={"Retry-After": str(RETRY_AFTER_SECONDS)})
            return
        if mode == MALFORMED:
            self.send_raw(200, b'{"embedding": [0.1, 0.2', "application/json")
            return
        self.send_json(200, {"model": model, "embedding": deterministic_embedding(prompt)})

    def read_json_body(self):
        """The request body as a dictionary, or None if it is not a JSON object."""
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            return None
        if not isinstance(data, dict):
            return None
        return data

    def send_json(self, status, data, extra_headers=None):
        self.send_raw(status, json.dumps(data).encode("utf-8"), "application/json", extra_headers)

    def send_text(self, status, text):
        self.send_raw(status, text.encode("utf-8"), "text/plain; charset=utf-8")

    def send_raw(self, status, body, content_type, extra_headers=None):
        # In slow mode the client has usually given up and closed the
        # connection by the time this runs. That is expected, not an error.
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            for name, value in (extra_headers or {}).items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            self.close_connection = True

    def log_message(self, format, *args):
        if not self.server.quiet:
            super().log_message(format, *args)


def start_in_background(mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS,
                        host=DEFAULT_HOST, port=0):
    """Start a quiet stub on its own thread and return the server.

    Port 0 lets the operating system pick a free port, which is what the
    tests use so two people running tests at once do not collide. Call
    server.shutdown() and then server.server_close() to stop it.
    """
    server = StubModelServer((host, port), mode=mode, delay_seconds=delay_seconds, quiet=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main():
    parser = argparse.ArgumentParser(
        description="A stand-in for an Ollama-compatible model server.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=SUCCESS)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS,
                        help="seconds to wait before answering in slow mode")
    arguments = parser.parse_args()

    server = StubModelServer((arguments.host, arguments.port), mode=arguments.mode,
                             delay_seconds=arguments.delay)
    print(f"Stub model server on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
