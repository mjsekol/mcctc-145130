"""A stand-in for the model service, set up for the supply sweep.

This is the same fixture the Module 6 labs use, with the school store's four
categories in place of the help-desk ones.

Why this file exists
--------------------
The automation you are writing this week calls a service over HTTP. There is no
model runtime on most machines in this building, and on the days there is one it
is busy. So this program answers the same two endpoints your Module 5 service
answers, with the same six-field envelope, and it lets you choose how it
misbehaves.

It is not a model. It matches words in the text and returns fixed shapes. It is
a test fixture, which means it exists so you can produce a failure on purpose
instead of waiting for one.

Endpoints
---------
GET  /health    -> {"service", "version", "status", "model_reachable", "tasks"}
POST /generate  -> the six-field envelope: ok, task, result, source, elapsed_ms,
                   error

Modes, chosen with --mode
-------------------------
ok          answers every request from the "model"
slow        waits --delay seconds, then answers like ok
error500    answers HTTP 500 with an envelope
garbage     answers HTTP 200 with a body that is not the envelope
empty       answers HTTP 200, ok true, source model, and result null
flaky       answers every other /generate with HTTP 500, starting with the
            second one

The last one is the interesting mode. It is a success on the wire and nothing
in the payload. An automation that counts replies instead of results reports a
good run on a day it did nothing at all.

There is no default port, on purpose. A real model server listens on 11434 and
several stubs in this course listen near it, and a program that reaches the
wrong server does not fail. It answers.

Run it:
    python sweep_service_stub.py --port 5158
    python sweep_service_stub.py --port 5158 --mode empty
    python sweep_service_stub.py --port 5158 --mode slow --delay 20

Standard library only. Built and run on Python 3.13.7.
"""

import argparse
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# The four categories the store manager batches orders by, plus "other".
LABELS = ["safety", "consumable", "storage", "wearable", "other"]

KEYWORDS = {
    "safety": ["glove", "goggle", "glasses", "mask", "guard"],
    "consumable": ["filament", "spool", "resin", "tape", "paper", "ink", "blade"],
    "storage": ["sd card", "drive", "usb", "case", "cabinet"],
    "wearable": ["lanyard", "badge", "apron"],
}

MAX_BODY_BYTES = 16384

# Set by main(). Read by the handler.
MODE = "ok"
DELAY = 0.0
CALL_COUNT = {"health": 0, "generate": 0}


def pick_label(text):
    """Match words. This is not classification and it is not pretending to be."""
    lowered = text.lower()
    for label in LABELS[:-1]:
        for word in KEYWORDS[label]:
            if word in lowered:
                return label
    return "other"


def envelope(ok, task, result, source, elapsed_ms, error):
    """Six fields, in this order, for every outcome. That is the whole point."""
    return {
        "ok": ok,
        "task": task,
        "result": result,
        "source": source,
        "elapsed_ms": elapsed_ms,
        "error": error,
    }


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        """Quiet. The automation prints its own record and two logs is noise."""

    def _send(self, status, payload_bytes, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload_bytes)))
        self.end_headers()
        self.wfile.write(payload_bytes)

    def _send_json(self, status, payload):
        self._send(status, json.dumps(payload).encode("utf-8"))

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/health":
            CALL_COUNT["health"] += 1
            self._send_json(
                200,
                {
                    "service": "sweep-service-stub",
                    "version": "1.0",
                    "status": "ok",
                    "mode": MODE,
                    "model_reachable": MODE in ("ok", "slow"),
                    "tasks": ["classify"],
                },
            )
        elif path == "/stub/stats":
            self._send_json(200, dict(CALL_COUNT))
        else:
            self._send_json(404, {"error": "not found"})

    def do_POST(self):
        path = self.path.split("?")[0]
        if path != "/generate":
            self._send_json(404, {"error": "not found"})
            return

        CALL_COUNT["generate"] += 1
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_BODY_BYTES:
            self._send_json(
                413,
                envelope(False, None, None, "none", 0,
                         {"kind": "body_too_large",
                          "message": f"the body is {length} bytes. The limit is {MAX_BODY_BYTES}."}),
            )
            return

        raw = self.rfile.read(length) if length else b""
        try:
            body = json.loads(raw.decode("utf-8")) if raw else {}
        except (ValueError, UnicodeDecodeError):
            self._send_json(
                400,
                envelope(False, None, None, "none", 0,
                         {"kind": "bad_request", "message": "the body was not JSON"}),
            )
            return

        task = str(body.get("task", "")).strip().lower()
        prompt = body.get("prompt", "")

        if task != "classify":
            self._send_json(
                400,
                envelope(False, task or None, None, "none", 0,
                         {"kind": "unknown_task",
                          "message": f"unknown task {task!r}. Known tasks: classify"}),
            )
            return

        if not isinstance(prompt, str) or not prompt.strip():
            self._send_json(
                400,
                envelope(False, task, None, "none", 0,
                         {"kind": "prompt_empty",
                          "message": "nothing left in the prompt after whitespace was removed"}),
            )
            return

        started = time.monotonic()

        if MODE == "slow":
            time.sleep(DELAY)

        if MODE == "flaky" and CALL_COUNT["generate"] % 2 == 0:
            self._send_json(
                500,
                envelope(False, task, None, "none", 0,
                         {"kind": "service_error",
                          "message": "the service hit a bug answering this request"}),
            )
            return

        if MODE == "error500":
            self._send_json(
                500,
                envelope(False, task, None, "none", int((time.monotonic() - started) * 1000),
                         {"kind": "service_error",
                          "message": "the service hit a bug answering this request"}),
            )
            return

        if MODE == "garbage":
            self._send(200, b"<html><body>Service is starting up</body></html>", "text/html")
            return

        if MODE == "empty":
            # HTTP 200. ok true. source model. And nothing in it.
            self._send_json(
                200,
                envelope(True, task, None, "model",
                         int((time.monotonic() - started) * 1000), None),
            )
            return

        label = pick_label(prompt)
        result = {
            "label": label,
            "confidence_note": f"Stub match on the words in the note. Best fit is {label}.",
        }
        self._send_json(
            200,
            envelope(True, task, result, "model",
                     int((time.monotonic() - started) * 1000), None),
        )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Stand-in model service for the note sweep.")
    parser.add_argument("--port", type=int, required=True,
                        help="required, on purpose. This lab uses 5158.")
    parser.add_argument("--mode", default="ok",
                        choices=["ok", "slow", "error500", "garbage", "empty", "flaky"])
    parser.add_argument("--delay", type=float, default=20.0,
                        help="seconds to wait in slow mode")
    args = parser.parse_args(argv)

    global MODE, DELAY
    MODE = args.mode
    DELAY = args.delay

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"sweep service stub listening on http://127.0.0.1:{args.port}  mode={MODE}")
    if MODE == "empty":
        print("  mode empty: every reply is HTTP 200 with ok true and result null.")
        print("  Nothing on the wire says anything is wrong. Your run record has to.")
    if MODE == "slow":
        print(f"  mode slow: every /generate waits {DELAY} seconds first.")
    if MODE == "flaky":
        print("  mode flaky: every second /generate answers HTTP 500.")
        print("  Half the work gets done. The run record has to say which half.")
    print("  Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
