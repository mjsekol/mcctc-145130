"""check_quest.py  ·  SQ-10 API First Contact self-check

Runs YOUR first_contact.py against Sky Watch five times, breaking Sky Watch a
different way each time, and checks the quest's done-when rule:

    Your program handles a 404, a timeout, and a rate limit DISTINCTLY,
    with a message that tells the user which one happened and what to do.

Run it from this folder:

    python check_quest.py

It starts and stops its own Sky Watch servers on free ports. You do not need
one running. It takes about 10 seconds.

What it expects from first_contact.py:
    python first_contact.py <spot id>
reads the server address from SKY_WATCH_URL and the timeout from
SKY_WATCH_TIMEOUT. The starter file already does both.

Passing this check is necessary, not sufficient. Your instructor still reads
your messages and asks you to explain your code.
"""

import os
import socket
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROGRAM = HERE / "first_contact.py"
SERVER = HERE / "sky_watch_server.py"


def free_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def start_server(mode):
    port = free_port()
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    process = subprocess.Popen([sys.executable, str(SERVER), "--port", str(port), "--mode", mode],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=environment)
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        try:
            socket.create_connection(("127.0.0.1", port), timeout=0.2).close()
            return process, port
        except OSError:
            time.sleep(0.1)
    process.kill()
    raise RuntimeError("Sky Watch did not start. Is sky_watch_server.py in this folder?")


def run_program(port, spot, timeout="2"):
    environment = dict(os.environ, SKY_WATCH_URL=f"http://127.0.0.1:{port}", SKY_WATCH_TIMEOUT=timeout,
                       PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    try:
        result = subprocess.run([sys.executable, str(PROGRAM), spot], capture_output=True, text=True,
                                encoding="utf-8", env=environment, timeout=60)
    except subprocess.TimeoutExpired:
        return "(your program was still running after 60 seconds. Is there a timeout on the request?)"
    return (result.stdout + result.stderr).strip()


def scenario(mode, spot):
    process, port = start_server(mode)
    try:
        return run_program(port, spot)
    finally:
        process.terminate()
        process.wait(timeout=10)


def main():
    if not PROGRAM.exists():
        print("There is no first_contact.py in this folder yet.")
        return 1
    print("Running first_contact.py five times. This takes about 10 seconds.\n")
    outputs = {
        "success": scenario("normal", "mill-creek"),
        "404": scenario("normal", "no-such-spot"),
        "timeout": scenario("slow", "mill-creek"),
        "429": scenario("always_429", "mill-creek"),
        "no server": run_program(free_port(), "mill-creek", timeout="10"),
    }
    failures = 0
    for name, text in outputs.items():
        first_line = text.splitlines()[0] if text else "(nothing printed)"
        print(f"{name:>9}: {first_line}")

    print()
    for name, text in outputs.items():
        if "Traceback" in text:
            print(f"FAIL  {name}: your program crashed with a traceback. Catch this failure.")
            failures += 1
        if text == "":
            print(f"FAIL  {name}: your program printed nothing.")
            failures += 1
    for name in ["404", "timeout", "429"]:
        if outputs[name].strip().lower() in ["error", "error.", "something went wrong", "request failed"]:
            print(f"FAIL  {name}: '{outputs[name]}' does not say which failure happened.")
            failures += 1
    distinct = {outputs["404"], outputs["timeout"], outputs["429"]}
    if len(distinct) < 3:
        print("FAIL  the 404, timeout, and 429 messages are not all different. Printing the same message for all three fails this quest.")
        failures += 1
    if outputs["success"] in distinct:
        print("FAIL  the success output is the same as a failure message.")
        failures += 1

    if failures == 0:
        print("PASS  404, timeout, and 429 each got their own message, and nothing crashed.")
        print("Now read your three messages out loud. Does each one tell a person what to DO?")
        return 0
    print(f"\n{failures} problem(s) to fix.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
