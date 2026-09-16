"""Check an automation against the four things Lab M06-03 asks for.

Run it on your own program, from the folder your program lives in:

    python check_sweep.py --program note_sweep.py --port 5170

It starts a stand-in service on the port you give it, drives your program
through five situations, and reports what it saw. It does not read your source
code, so it cannot be fooled by a comment and it cannot be satisfied by one.

It checks:

  1  a scheduled trigger that fires more than once without you typing anything
  2  four or more named steps in the printed run record
  3  a run that succeeds when everything is working
  4  a real error path: a run where a step did not get what it expected, the
     program says so, and the exit code is not 0
  5  something a human can act on: an incident file or an equivalent record
     naming what to check

It cannot check whether what you wrote in the incident file is useful. A person
does that, and the lab says who.

There is no default port, on purpose. Pass one that nothing else is using.
Ports 5158, 5157, 11434, 11535, 11534 and 11634 are taken elsewhere in this
course.

Standard library only. Runs on Python 3.13.7.
"""

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PASS = "PASS"
FAIL = "FAIL"

MODE = {"value": "ok"}
LABELS = ["hardware", "software", "network", "account"]
KEYWORDS = {
    "hardware": ["printer", "laptop", "monitor", "keyboard", "battery", "screen"],
    "software": ["install", "visual studio", "update", "crash", "license"],
    "network": ["wifi", "wi-fi", "internet", "vpn", "drops", "connection"],
    "account": ["password", "login", "locked out", "username", "sign in"],
}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        """Quiet."""

    def _json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] == "/health":
            self._json(200, {"service": "check-sweep-fixture", "version": "1.0",
                             "status": "ok", "mode": MODE["value"],
                             "model_reachable": MODE["value"] == "ok",
                             "tasks": ["classify"]})
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8"))
        except ValueError:
            body = {}
        prompt = str(body.get("prompt", ""))

        if MODE["value"] == "empty":
            self._json(200, {"ok": True, "task": "classify", "result": None,
                             "source": "model", "elapsed_ms": 0, "error": None})
            return

        label = "other"
        lowered = prompt.lower()
        for name in LABELS:
            if any(word in lowered for word in KEYWORDS[name]):
                label = name
                break
        self._json(200, {"ok": True, "task": "classify",
                         "result": {"label": label,
                                    "confidence_note": f"Fixture match, best fit {label}."},
                         "source": "model", "elapsed_ms": 1, "error": None})


def start_fixture(port):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def run(program, service, workdir, extra, timeout=90):
    command = [sys.executable, program, "--service", service,
               "--inbox", "inbox", "--state", "state", "--out", "out"] + extra
    finished = subprocess.run(command, cwd=workdir, capture_output=True,
                              text=True, timeout=timeout)
    return finished


def make_inbox(workdir, notes):
    inbox = workdir / "inbox"
    if inbox.exists():
        shutil.rmtree(inbox)
    inbox.mkdir(parents=True)
    for name, text in notes.items():
        (inbox / name).write_text(text, encoding="utf-8")


NOTES = {
    "note-01.txt": "The 3D printer in room 118 jammed and the first layer will not stick.",
    "note-02.txt": "my laptop keeps dropping the wifi in the back corner of the lab",
    "note-03.txt": "Visual Studio will not install the workload on station 6.",
    "note-04.txt": "I am locked out after I changed my password on Friday.",
    "note-05.txt": "The second monitor on station 11 comes on about half the time.",
}

STEP_WORDS = re.compile(r"\b(collect|gather|read|fresh|stale|classify|label|"
                        r"digest|report|record|log|write|check|notify|verify)\b",
                        re.I)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check an automation against Lab M06-03.")
    parser.add_argument("--program", default="note_sweep.py")
    parser.add_argument("--port", type=int, required=True,
                        help="required, on purpose. Pick one nothing else is using.")
    parser.add_argument("--workdir", default=".")
    args = parser.parse_args(argv)

    workdir = pathlib.Path(args.workdir).resolve()
    program = pathlib.Path(args.program)
    if not (workdir / program).exists():
        print(f"No program at {workdir / program}")
        return 2

    service = f"http://127.0.0.1:{args.port}"
    server = start_fixture(args.port)
    results = []

    for folder in ("state", "out"):
        target = workdir / folder
        if target.exists():
            shutil.rmtree(target)

    try:
        # 3. A good run.
        MODE["value"] = "ok"
        make_inbox(workdir, NOTES)
        good = run(str(program), service, workdir, ["--once"])
        good_ok = good.returncode == 0
        results.append(("3 a working run exits 0",
                        PASS if good_ok else FAIL,
                        f"exit {good.returncode}"))

        # 2. Four or more named steps in the run record.
        lines = [line for line in good.stdout.splitlines() if STEP_WORDS.search(line)]
        named = len({STEP_WORDS.search(line).group(0).lower() for line in lines})
        results.append(("2 four or more named steps in the printed record",
                        PASS if named >= 4 else FAIL,
                        f"{named} distinct step words seen"))

        # 4. The error path. Nothing has changed since the good run.
        MODE["value"] = "ok"
        stale = run(str(program), service, workdir, ["--once"])
        stale_caught = stale.returncode != 0 or "FAIL" in stale.stdout.upper()
        results.append(("4a the source did not change and the program says so",
                        PASS if stale_caught else FAIL,
                        f"exit {stale.returncode}"))

        # 4b. The service answers 200 with nothing in it.
        MODE["value"] = "empty"
        make_inbox(workdir, NOTES)
        time.sleep(1.1)
        empty = run(str(program), service, workdir, ["--once"])
        empty_caught = empty.returncode != 0 or "FAIL" in empty.stdout.upper()
        results.append(("4b the service answered 200 with no result and the program says so",
                        PASS if empty_caught else FAIL,
                        f"exit {empty.returncode}"))

        # 5. Something a human can act on.
        out_dir = workdir / "out"
        state_dir = workdir / "state"
        artefacts = list(out_dir.glob("incident*")) + list(state_dir.glob("*.csv"))
        results.append(("5 an incident file or a run log exists after a bad run",
                        PASS if artefacts else FAIL,
                        f"{len(artefacts)} file(s): " +
                        ", ".join(p.name for p in artefacts[:4])))

        # 1. The scheduled trigger fires more than once on its own.
        MODE["value"] = "ok"
        make_inbox(workdir, NOTES)
        try:
            timed = run(str(program), service, workdir,
                        ["--every", "3", "--runs", "2"], timeout=60)
            fired = len(re.findall(r"run\s+r?\d", timed.stdout))
            trigger_ok = fired >= 2
            detail = f"{fired} sweeps seen in one invocation"
        except subprocess.TimeoutExpired:
            trigger_ok = False
            detail = "the scheduler did not stop. Support --runs so it can be checked."
        results.append(("1 the trigger fires more than once without you typing anything",
                        PASS if trigger_ok else FAIL, detail))
    finally:
        server.shutdown()
        server.server_close()

    print()
    width = max(len(name) for name, _, _ in results)
    for name, verdict, detail in results:
        print(f"{verdict}  {name:<{width}}  {detail}")
    failures = sum(1 for _, verdict, _ in results if verdict == FAIL)
    print()
    if failures:
        print(f"{failures} of {len(results)} checks failed.")
        print("This tool checks shape. It cannot check whether your incident file")
        print("tells a person anything worth knowing. Your partner does that.")
        return 1
    print(f"All {len(results)} checks passed.")
    print("That is the floor, not the grade. The incident file gets read by a person.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
