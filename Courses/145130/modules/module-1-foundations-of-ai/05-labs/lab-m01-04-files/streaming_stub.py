# streaming_stub.py  .  Lab M01-04, a server whose real speed you already know
#
# THIS IS NOT A MODEL. It does not read your prompt and it does not think. It
# sends a fixed list of words back one at a time, at a rate you set on the
# command line, and it reports the token count it actually sent.
#
# Why it exists: bench.py claims to measure time to first token and tokens per
# second. Before you trust a measuring instrument, you point it at something
# whose size you already know. Start this server with --first-delay-ms 300
# --delay-ms 25 --tokens 40 and bench.py should report a time to first token
# near 300 ms and a rate near 40 tokens per second. If it does not, the
# instrument is wrong, and you found that out on a day when it cost you
# nothing.
#
# The anchor stub, stub_model_server.py, deliberately refuses to stream, which
# is what a plain HTTP server looks like when streaming was never built. This
# one is the other half of the pair.
#
#   python streaming_stub.py --port 11635
#   python streaming_stub.py --port 11635 --tokens 40 --delay-ms 25 --first-delay-ms 300
#
# There is no API key here and there never should be. A local server needs none.

import argparse
import json
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_HOST = "127.0.0.1"   # loopback only. Nobody else on the network reaches it.
DEFAULT_PORT = 11635      # Module 1 streaming stub port

# A fixed sentence, repeated until the token count is reached. Fixed on
# purpose: the point of this server is that nothing about it varies except the
# timing you asked for.
WORDS = ("the model does not read your prompt it repeats this line so that "
         "the timing is the only thing being measured here today").split()


class StreamingStub(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, tokens, delay_ms, first_delay_ms, quiet=False):
        super().__init__(address, StreamingHandler)
        self.tokens = tokens
        self.delay_ms = delay_ms
        self.first_delay_ms = first_delay_ms
        self.quiet = quiet

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"


class StreamingHandler(BaseHTTPRequestHandler):

    protocol_version = "HTTP/1.1"

    def do_GET(self):
        if self.path == "/":
            self.send_plain(200, "Streaming stub is running. It is not a model.")
        else:
            self.send_object(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/generate":
            self.send_object(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            self.send_object(400, {"error": "the request body must be a JSON object"})
            return
        if not isinstance(request, dict) or not isinstance(request.get("prompt"), str):
            self.send_object(400, {"error": "model and prompt must both be strings"})
            return

        model = request.get("model", "streaming-stub")
        pieces = [WORDS[i % len(WORDS)] + " " for i in range(self.server.tokens)]
        if request.get("stream") is True:
            self.stream(model, pieces)
        else:
            time.sleep(self.server.first_delay_ms / 1000.0)
            time.sleep(self.server.delay_ms * len(pieces) / 1000.0)
            self.send_object(200, self.final_object(model, "".join(pieces), len(pieces)))

    def final_object(self, model, text, tokens):
        generated_ns = int(self.server.delay_ms * tokens * 1_000_000)
        return {
            "model": model,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "response": text,
            "done": True,
            "eval_count": tokens,
            "eval_duration": generated_ns,
        }

    def stream(self, model, pieces):
        """Send one JSON object per line, the way a streaming server does."""
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()
        # The pause before the first token stands in for a model being loaded
        # and reading the prompt. On real hardware this is the slow part.
        time.sleep(self.server.first_delay_ms / 1000.0)
        try:
            for piece in pieces:
                self.write_chunk(json.dumps({
                    "model": model,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                    "response": piece,
                    "done": False,
                }) + "\n")
                time.sleep(self.server.delay_ms / 1000.0)
            self.write_chunk(json.dumps(self.final_object(model, "", len(pieces))) + "\n")
            self.wfile.write(b"0\r\n\r\n")
            self.wfile.flush()
        except (ConnectionError, BrokenPipeError):
            self.close_connection = True

    def write_chunk(self, text):
        data = text.encode("utf-8")
        self.wfile.write(f"{len(data):X}\r\n".encode("ascii"))
        self.wfile.write(data)
        self.wfile.write(b"\r\n")
        self.wfile.flush()

    def send_object(self, status, data):
        self.send_raw(status, json.dumps(data).encode("utf-8"), "application/json")

    def send_plain(self, status, text):
        self.send_raw(status, text.encode("utf-8"), "text/plain; charset=utf-8")

    def send_raw(self, status, body, content_type):
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            self.close_connection = True

    def log_message(self, format, *args):
        if not self.server.quiet:
            super().log_message(format, *args)


def start_in_background(tokens=40, delay_ms=25, first_delay_ms=300,
                        host=DEFAULT_HOST, port=0):
    """Start a quiet streaming stub on its own thread and return the server."""
    import threading
    server = StreamingStub((host, port), tokens, delay_ms, first_delay_ms, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(
        description="A server that streams at a rate you choose. Not a model.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--tokens", type=int, default=40,
                        help="how many pieces of text to send")
    parser.add_argument("--delay-ms", type=float, default=25.0,
                        help="pause after each piece")
    parser.add_argument("--first-delay-ms", type=float, default=300.0,
                        help="pause before the first piece, standing in for load time")
    arguments = parser.parse_args()

    server = StreamingStub((arguments.host, arguments.port), arguments.tokens,
                           arguments.delay_ms, arguments.first_delay_ms)
    expected = arguments.tokens / (arguments.delay_ms * arguments.tokens / 1000.0)
    print(f"Streaming stub on {server.base_url}. It is not a model.")
    print(f"{arguments.tokens} tokens, {arguments.delay_ms} ms each, "
          f"{arguments.first_delay_ms} ms before the first one.")
    print(f"A correct benchmark should report about {expected:.1f} tokens per second "
          f"and about {arguments.first_delay_ms:.0f} ms to first token.")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
