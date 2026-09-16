# stub_model_server.py  .  Module 5
#
# A stand-in for a locally hosted, Ollama-compatible model server. It answers
# the one endpoint this module uses, with no model behind it:
#
#   POST /api/generate   {"model", "prompt", "stream": false}
#                     -> {"model", "response", "done"}
#
# Why this exists: most machines here have no model runtime on them, and a
# class period is too short to debug a model and an application at the same
# time. This lets you run your whole build today, and it lets you make the
# model fail on purpose so you can watch your own failure handling work.
#
# It is not a model. It matches words and returns fixed shapes. Anything you
# learn from its answers is about your plumbing, never about quality.
#
# There is no credential here and there never should be. A local model needs
# no account and no key.
#
# **Always pass --port.** A server that cannot get the port it asked for stops
# without much noise, and then the next program finds whatever else is on that
# port and talks to that instead. That does not look like a failure. It looks
# like an answer. This module uses 11535. Port 11434 belongs to a real model
# server if one is ever running here.
#
#   python stub_model_server.py --port 11535
#   python stub_model_server.py --port 11535 --mode bare_json
#   python stub_model_server.py --port 11535 --mode slow --delay 8
#
# Modes:
#   fenced_json  the answer as JSON inside a fenced code block
#   bare_json    the same JSON with no fence around it
#   prose        the same answer written as labelled prose
#   refusal      a polite sentence that fits no shape
#   slow         waits --delay seconds, then answers like fenced_json
#   error        HTTP 500
#   rate_limited HTTP 429 with a Retry-After header
#   malformed    status 200 with a body that is cut off
#   not_done     valid JSON with "done": false
#   empty        a response that is only spaces
#
# Extra endpoints a real server does not have:
#   GET  /stub/stats   how many times it was asked to generate
#   POST /stub/mode    send {"mode": "error"} to switch while it runs
#
# Standard library only.

import argparse
import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 11535
DEFAULT_DELAY_SECONDS = 30.0
RETRY_AFTER_SECONDS = 1

FENCED_JSON = "fenced_json"
BARE_JSON = "bare_json"
PROSE = "prose"
REFUSAL = "refusal"
SLOW = "slow"
ERROR = "error"
RATE_LIMITED = "rate_limited"
MALFORMED = "malformed"
NOT_DONE = "not_done"
EMPTY = "empty"
MODES = [FENCED_JSON, BARE_JSON, PROSE, REFUSAL, SLOW,
         ERROR, RATE_LIMITED, MALFORMED, NOT_DONE, EMPTY]

GENERATE_PATH = "/api/generate"
STATS_PATH = "/stub/stats"
MODE_PATH = "/stub/mode"

# A service puts the text it wants worked on between markers, with a line
# saying the text is data and not instructions. The stub reads the markers so
# its answer is about the text you actually sent.
TEXT_PATTERN = re.compile(r"<<<TEXT\n(.*?)\nTEXT", re.DOTALL)
REFUSAL_TEXT = "I am not able to help with that request."


def first_sentence(text, limit=110):
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


def stub_answer(mode, prompt):
    """The text a cooperative model would return for this prompt."""
    match = TEXT_PATTERN.search(prompt)
    text = match.group(1) if match else prompt

    if mode == REFUSAL:
        return REFUSAL_TEXT

    answer = {
        "headline": "Stub headline: " + first_sentence(text),
        "points": useful_lines(text),
    }
    if mode == PROSE:
        lines = ["Headline: " + answer["headline"], ""]
        lines.extend("- " + point for point in answer["points"])
        return "\n".join(lines)
    if mode == BARE_JSON:
        return json.dumps(answer)
    return "```json\n" + json.dumps(answer, indent=2) + "\n```"


class StubModelServer(ThreadingHTTPServer):
    """An HTTP server that remembers its mode and counts the calls it answered."""

    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=FENCED_JSON, delay_seconds=DEFAULT_DELAY_SECONDS,
                 quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, StubHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.generate_calls = 0
        self.lock = threading.Lock()

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def handle_error(self, request, client_address):
        if not self.quiet:
            super().handle_error(request, client_address)

    def record_generate(self):
        with self.lock:
            self.generate_calls += 1


class StubHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == STATS_PATH:
            self.send_json(200, {"generate_calls": self.server.generate_calls,
                                 "mode": self.server.mode})
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
        elif self.path == GENERATE_PATH:
            self.generate(request)
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
        prompt = request.get("prompt")
        model = request.get("model")
        if not isinstance(prompt, str) or not isinstance(model, str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return
        if request.get("stream") is not False:
            self.send_json(400, {"error": "this stub only supports stream: false"})
            return

        self.server.record_generate()
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

        reply = {
            "model": model,
            "response": stub_answer(mode if mode != SLOW else FENCED_JSON, prompt),
            "done": True,
        }
        if mode == NOT_DONE:
            reply["done"] = False
        elif mode == EMPTY:
            reply["response"] = "   "
        self.send_json(200, reply)

    def read_json_body(self):
        """The request body as a dictionary, or None if it is not a JSON object."""
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            return None
        return data if isinstance(data, dict) else None

    def send_json(self, status, data, extra_headers=None):
        self.send_raw(status, json.dumps(data).encode("utf-8"),
                      "application/json", extra_headers)

    def send_text(self, status, text):
        self.send_raw(status, text.encode("utf-8"), "text/plain; charset=utf-8")

    def send_raw(self, status, body, content_type, extra_headers=None):
        # In slow mode the caller has usually given up and closed the
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


def start_in_background(mode=FENCED_JSON, delay_seconds=DEFAULT_DELAY_SECONDS,
                        host=DEFAULT_HOST, port=0):
    """Start a quiet stub on its own thread and return the server.

    Port 0 lets the operating system pick a free one, which is what a test
    should use so two people running tests at once do not collide. Call
    server.shutdown() and then server.server_close() to stop it.
    """
    server = StubModelServer((host, port), mode=mode, delay_seconds=delay_seconds,
                             quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(
        description="A stand-in for an Ollama-compatible model server.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help="pass this every time, even when it is the default")
    parser.add_argument("--mode", choices=MODES, default=FENCED_JSON)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS,
                        help="seconds to wait before answering in slow mode")
    arguments = parser.parse_args()

    server = StubModelServer((arguments.host, arguments.port), mode=arguments.mode,
                             delay_seconds=arguments.delay)
    print(f"Stub model server on {server.base_url} in {server.mode} mode. "
          f"Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
