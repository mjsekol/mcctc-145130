# one_request.py  .  the smallest thing that talks to a model server
#
# Two requests, both real. The first one works. The second one asks for
# something this server will not do, so you can see what a failure at this
# seam actually looks like.
#
#   python one_request.py
#
# Start the stub first, on this module's port:
#   python stub_model_server.py --port 11634
#
# The address comes from RIDGE_MODEL_URL, or 127.0.0.1:11634.
#
# WHAT TO NOTICE
#
# The answer comes back inside one field called "response", and it is TEXT.
# Not a label, not a number, not a shape your program can rely on. Turning
# that text into something a program can use is your job, and in Module 5 you
# will build a service whose whole purpose is doing it in one place.

import json
import os
import urllib.error
import urllib.request

MODEL_URL = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634").rstrip("/")
MODEL_NAME = os.environ.get("RIDGE_MODEL", "llama3.2")

# Ignore any proxy the school network has configured. Loopback traffic should
# not be sent anywhere.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def send(body):
    """POST to /api/generate and print what came back, whatever it is."""
    request = urllib.request.Request(
        MODEL_URL + "/api/generate",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST")
    try:
        with DIRECT.open(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
        print(f"HTTP {response.status}")
        print(raw[:400])
    except urllib.error.HTTPError as error:
        # A refused request still has a body, and the body says why.
        print(f"HTTP {error.code}")
        print(error.read().decode("utf-8")[:400])
        error.close()
    except urllib.error.URLError as error:
        print(f"nothing answered at {MODEL_URL}: {error.reason}")
        print("Start the stub with: python stub_model_server.py --port 11634")


print("=== a request this server will answer ===")
send({"model": MODEL_NAME, "prompt": "the wifi keeps dropping", "stream": False})

print()
print("=== a request this server refuses ===")
send({"model": MODEL_NAME, "prompt": "the wifi keeps dropping", "stream": True})
