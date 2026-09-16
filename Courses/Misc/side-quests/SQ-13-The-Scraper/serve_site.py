# serve_site.py
# Runs Corner Pocket Cards, an invented local card shop website, on your own
# computer. SQ-13 is scraped against this site and never against a real one.
#
# Usage, from this folder:
#     python serve_site.py            serves at http://127.0.0.1:8000/
#     python serve_site.py 8001       serves on a different port
#
# Press Ctrl+C in this terminal to stop it. Keep this terminal open and run
# your scraper in a second terminal.
#
# You do not need to understand how this file works. It uses a class, and
# classes are Unit 7. What it does:
#
#   - It only answers requests from this computer (127.0.0.1).
#   - It prints one line per request with the time since the previous one,
#     so you can see whether your scraper is waiting as long as it should.
#   - It refuses requests less than one second apart with 429 Too Many
#     Requests. The shop's terms ask for more than that. Read them.

import functools
import http.server
import sys
import threading
import time
from pathlib import Path

SITE_FOLDER = Path(__file__).resolve().parent / "site"
HOST = "127.0.0.1"
DEFAULT_PORT = 8000
MINIMUM_GAP_SECONDS = 1.0


class ShopHandler(http.server.SimpleHTTPRequestHandler):
    """Serves the site folder, enforces a minimum gap, and logs every request."""

    rate_limit = True
    last_request = 0.0
    lock = threading.Lock()

    def check_rate(self):
        """Record this request. Send 429 and return False if it came too soon."""
        with ShopHandler.lock:
            now = time.monotonic()
            first = ShopHandler.last_request == 0.0
            gap = now - ShopHandler.last_request
            ShopHandler.last_request = now
        if first:
            self.gap_text = "first request"
        else:
            self.gap_text = f"{gap:.1f} s after the previous request"
        if self.rate_limit and not first and gap < MINIMUM_GAP_SECONDS:
            self.send_response(429, "Too Many Requests")
            self.send_header("Retry-After", "3")
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(b"429 Too Many Requests. Read /terms.html for the request rate.\n")
            return False
        return True

    def do_GET(self):
        if self.check_rate():
            super().do_GET()

    def do_HEAD(self):
        if self.check_rate():
            super().do_HEAD()

    def log_request(self, code="-", size="-"):
        agent = self.headers.get("User-Agent", "(no User-Agent)")
        stamp = time.strftime("%H:%M:%S")
        code_number = getattr(code, "value", code)
        gap_text = getattr(self, "gap_text", "")
        print(f"[{stamp}] {self.command} {self.path} -> {code_number}  ({gap_text})  User-Agent: {agent}",
              flush=True)

    def log_message(self, format, *args):
        # log_request above already reports every request, including 404s.
        pass


def make_server(port, rate_limit=True):
    """Build the server without starting it. Test code uses this."""
    ShopHandler.rate_limit = rate_limit
    ShopHandler.last_request = 0.0
    handler = functools.partial(ShopHandler, directory=str(SITE_FOLDER))
    return http.server.ThreadingHTTPServer((HOST, port), handler)


def main():
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        if not sys.argv[1].isdigit():
            print("The port must be a whole number, for example: python serve_site.py 8001")
            return 1
        port = int(sys.argv[1])
    try:
        server = make_server(port)
    except OSError:
        print(f"Port {port} is already in use. Try another: python serve_site.py {port + 1}")
        return 1
    print(f"Corner Pocket Cards running at http://{HOST}:{port}/")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
