# sky_watch_server.py  ·  SQ-10 API First Contact fixture
#
# Sky Watch: a pretend public API that reports tonight's stargazing conditions
# at a few invented viewing spots. It needs no key and no account, like the
# public APIs this quest is about, and it runs on your own computer, so you can
# break it on purpose as many times as you like.
#
# Usage, from this folder:
#   python sky_watch_server.py                    normal mode, port 8095
#   python sky_watch_server.py --mode always_404  every request gets 404 Not Found
#   python sky_watch_server.py --mode slow        every request takes 20 seconds
#   python sky_watch_server.py --mode always_429  every request gets 429 Too Many Requests
#   python sky_watch_server.py --port 8096
#
# Normal mode behaves like a real service:
#   GET /api/v1/spots                   the list of viewing spots
#   GET /api/v1/spots/<id>/tonight      tonight's conditions at one spot
#   - A spot that does not exist gets 404, with a JSON error body.
#   - More than 5 requests in 10 seconds gets 429, with a Retry-After header.
#
# Every spot and every number is invented. Press Ctrl+C to stop the server.
# You do not need to understand how this file works to finish the quest.

import argparse
import json
import math
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 8095
DEFAULT_DELAY_SECONDS = 20.0
LIMIT = 5
WINDOW_SECONDS = 10.0
ALWAYS_429_WAIT = 30

NORMAL = "normal"
ALWAYS_404 = "always_404"
SLOW = "slow"
ALWAYS_429 = "always_429"
MODES = [NORMAL, ALWAYS_404, SLOW, ALWAYS_429]

SPOTS = {
    "mill-creek": {"name": "Mill Creek Overlook", "updated_at": "2027-01-15T18:00:00",
                   "cloud_cover_percent": 15, "moon": "waxing crescent", "visibility_miles": 10,
                   "best_hours": "21:00-01:00"},
    "lakeview": {"name": "Lakeview Beach Lot", "updated_at": "2027-01-15T18:00:00",
                 "cloud_cover_percent": 85, "moon": "waxing crescent", "visibility_miles": 3,
                 "best_hours": None},
    "ridge-trail": {"name": "Ridge Trail Parking", "updated_at": "2027-01-15T17:30:00",
                    "cloud_cover_percent": 40, "moon": "waxing crescent", "visibility_miles": 8,
                    "best_hours": "23:00-02:00"},
}


class SkyWatchServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, SkyWatchHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.recent = []
        self.lock = threading.Lock()

    def wait_needed(self):
        now = time.monotonic()
        with self.lock:
            self.recent = [t for t in self.recent if now - t < WINDOW_SECONDS]
            if len(self.recent) >= LIMIT:
                return max(1, math.ceil(WINDOW_SECONDS - (now - self.recent[0])))
            self.recent.append(now)
            return 0

    def handle_error(self, request, client_address):
        if not self.quiet:
            print("  (a client hung up before the reply was sent)")


class SkyWatchHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        mode = self.server.mode
        if mode == ALWAYS_404:
            self.send_json(404, {"error": "not found"})
            return
        if mode == ALWAYS_429:
            self.send_json(429, {"error": "slow down"}, {"Retry-After": str(ALWAYS_429_WAIT)})
            return
        if mode == SLOW:
            time.sleep(self.server.delay_seconds)
        wait = self.server.wait_needed()
        if wait:
            self.send_json(429, {"error": "slow down"}, {"Retry-After": str(wait)})
            return
        if path == "/api/v1/spots":
            self.send_json(200, {"spots": [{"id": spot_id, "name": s["name"]} for spot_id, s in SPOTS.items()]})
            return
        parts = path.split("/")          # ['', 'api', 'v1', 'spots', '<id>', 'tonight']
        if len(parts) == 6 and parts[1:4] == ["api", "v1", "spots"] and parts[5] == "tonight" and parts[4] in SPOTS:
            self.send_json(200, dict(SPOTS[parts[4]], id=parts[4]))
            return
        self.send_json(404, {"error": f"nothing at {path}"})

    def send_json(self, status, data, extra_headers=None):
        body = json.dumps(data, indent=2).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            for name, value in (extra_headers or {}).items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        if not self.server.quiet:
            print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''}")


def start_in_background(mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS, port=0):
    server = SkyWatchServer((HOST, port), mode=mode, delay_seconds=delay_seconds, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(description="Sky Watch, a pretend no-key public API for SQ-10.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=NORMAL)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS)
    arguments = parser.parse_args()
    server = SkyWatchServer((HOST, arguments.port), mode=arguments.mode, delay_seconds=arguments.delay)
    print(f"Sky Watch on http://{HOST}:{arguments.port} in {arguments.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
