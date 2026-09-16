"""stub_model_server.py: a tiny Ollama-compatible server for calibrating a probe.

    python stub_model_server.py --port 11634 --mode neutral
    python stub_model_server.py --port 11634 --mode tilted
    python stub_model_server.py --port 11634 --mode slow
    python stub_model_server.py --port 11634 --mode error

ALWAYS PASS --port. There is no default and the program refuses to start without
one. A real Ollama listens on 11434 and so do several stubs in this course, and a
run against the wrong server looks exactly like a working run, which is the worst
kind of failure because nothing on the screen says anything is wrong. This quest
uses 11634.

WHAT THIS IS FOR, AND WHAT IT IS NOT

This is not a language model and it is not pretending to be one. It is a target
you point your probe at so you can find out whether your probe works.

  --mode neutral  picks its reply uniformly at random from three options,
                  independent of the prompt. There is no skew. If your probe
                  reports one, your probe is wrong.

  --mode tilted   has a documented skew, printed at startup. If your probe
                  cannot find it, your probe is not sensitive enough to find a
                  smaller one in a real model.

You calibrate an instrument on a signal you already know before you point it at
something unknown. That is the whole reason this file exists.

Everything it returns is invented text. No real person, product, or model is
described.
"""
import argparse
import json
import random
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# Three replies, in increasing order of how discouraging they are. The probe's
# job is to work out which one comes back and how often.
REPLIES = {
    "ask": "Ask your teacher for help with the next problem set. You can do this.",
    "practice": "Spend twenty minutes a day on practice problems and it will come.",
    "different": "This subject is not for everyone. It may be worth considering a "
                 "different path.",
}

# In tilted mode, the skew is on one word in the prompt and it is printed at
# startup so you can check your probe against a known answer.
TILT_TRIGGER = "physics"
TILT_WEIGHTS = {"ask": 0.20, "practice": 0.20, "different": 0.60}
FLAT_WEIGHTS = {"ask": 1 / 3, "practice": 1 / 3, "different": 1 / 3}


class Handler(BaseHTTPRequestHandler):
    mode = "neutral"
    rng = random.Random(0)

    def log_message(self, *args):
        return  # quiet

    def _send(self, code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "mode": Handler.mode})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/generate":
            self._send(404, {"error": "not found"})
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except json.JSONDecodeError:
            self._send(400, {"error": "body was not JSON"})
            return

        prompt = str(request.get("prompt", "")).lower()

        if Handler.mode == "error":
            self._send(500, {"error": "the model is unavailable"})
            return

        if Handler.mode == "slow":
            time.sleep(3)

        weights = FLAT_WEIGHTS
        if Handler.mode == "tilted" and TILT_TRIGGER in prompt:
            weights = TILT_WEIGHTS

        keys = list(weights)
        choice = Handler.rng.choices(keys, weights=[weights[k] for k in keys])[0]

        self._send(200, {
            "model": request.get("model", "stub"),
            "response": REPLIES[choice],
            "done": True,
        })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, required=True,
                        help="required, no default. This quest uses 11634.")
    parser.add_argument("--mode", default="neutral",
                        choices=["neutral", "tilted", "slow", "error"])
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    Handler.mode = args.mode
    Handler.rng = random.Random(args.seed)

    print(f"stub_model_server on http://127.0.0.1:{args.port}  mode={args.mode}  "
          f"seed={args.seed}")
    if args.mode == "tilted":
        print("SKEW, declared up front so you can check your probe against it:")
        print(f"  when the prompt contains {TILT_TRIGGER!r}, the reply weights are")
        for key, weight in TILT_WEIGHTS.items():
            print(f"    {key:<10} {weight:.0%}")
        print("  otherwise they are one third each.")
    elif args.mode == "neutral":
        print("NO SKEW. One third each, whatever the prompt says.")
        print("If your probe reports a skew here, your probe is wrong.")
    print("Ctrl+C to stop.")

    HTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
