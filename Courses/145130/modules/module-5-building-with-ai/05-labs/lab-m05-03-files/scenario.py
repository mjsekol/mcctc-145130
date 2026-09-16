# scenario.py  .  Lab M05-03, The Broken Integration
#
# Starts this folder's two servers in one healthy state or one of five broken
# states, runs bench.py against them, and stops everything again.
#
# It tells you the service URL and nothing else. Everything else about the
# state of the stack is yours to find out, because finding out is the lab.
#
# Why this exists: you are diagnosing five different faults, and setting each
# one up by hand across three terminals costs more of the period than the
# diagnosis does. This does the setup. The diagnosis is still yours.
#
# Every port is chosen by asking the operating system for a free one, so two
# people can run this at the same moment on the same machine and neither
# breaks the other. Your own work does not get that for free, which is why
# every command in this module names its port.
#
#   python scenario.py list
#   python scenario.py 0        the healthy baseline. Run this one first.
#   python scenario.py 1
#   python scenario.py 3 --hold
#
# With --hold the servers stay up after the bench run and it prints the
# service URL, so you can point contract_probe.py at it and look closer. Press
# Ctrl+C to stop.
#
# Everything it needs is in this folder: stub_model_server.py,
# contract_demo_service.py, bench.py, and contract_probe.py. Nothing outside
# it is required, apart from Flask.
#
# Standard library only. Nothing here needs a credential or a network.

import argparse
import os
import socket
import subprocess
import sys
import time

STARTUP_TIMEOUT_SECONDS = 25.0
POLL_SECONDS = 0.25

HERE = os.path.dirname(os.path.abspath(__file__))
STUB = "stub_model_server.py"
SERVICE = "contract_demo_service.py"

# One healthy baseline and five faults. Each is a real configuration of the
# real programs in this folder, not a simulation of one. The `note` is what
# you are allowed to know before you start: the symptom somebody reported,
# never the cause.
#
# Two of the five faults report the same symptom, and two of them report the
# same error kind. Both of those are on purpose.
SCENARIOS = {
    "0": {
        "title": "Healthy. This is what a working run looks like",
        "note": ("Nothing is wrong here. Capture this one first so you have "
                 "something to compare against."),
        "stub_mode": "fenced_json",
        "stub_delay": 30.0,
        "timeout": 20.0,
        "retries": 1,
        "decoy": False,
    },
    "1": {
        "title": "Fault A",
        "note": ("The printout looks the way it always did, and every run now takes "
                 "about eight seconds instead of under one."),
        "stub_mode": None,          # the stub is never started
        "stub_delay": 30.0,
        "timeout": 5.0,
        "retries": 0,
        "decoy": False,
    },
    "2": {
        "title": "Fault B",
        "note": ("It is fast, and every headline is just the first line of the "
                 "request copied out."),
        "stub_mode": "refusal",
        "stub_delay": 30.0,
        "timeout": 5.0,
        "retries": 0,
        "decoy": False,
    },
    "3": {
        "title": "Fault C",
        "note": ("The run takes almost half a minute. The student assumed it had "
                 "crashed and closed the window."),
        "stub_mode": "slow",
        "stub_delay": 8.0,
        "timeout": 3.0,
        "retries": 1,
        "decoy": False,
    },
    "4": {
        "title": "Fault D",
        "note": ("It is fast, and every headline is just the first line of the "
                 "request copied out."),
        "stub_mode": "error",
        "stub_delay": 30.0,
        "timeout": 5.0,
        "retries": 0,
        "decoy": False,
    },
    "5": {
        "title": "Fault E",
        "note": ("A classmate says their model server is definitely running, they "
                 "can see it in a window, and every headline is still the first "
                 "line copied out."),
        "stub_mode": None,
        "stub_delay": 30.0,
        "timeout": 5.0,
        "retries": 0,
        # Something is listening where the model should be. It is a real,
        # healthy program. It is not a model. This happened for real while this
        # module was being built, on port 11434, and it cost an hour.
        "decoy": True,
    },
}


def free_port():
    """A port nothing is using right now."""
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def wait_for_port(port, label, timeout=STARTUP_TIMEOUT_SECONDS):
    """True once something is listening on the port."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                return True
        except OSError:
            time.sleep(POLL_SECONDS)
    print(f"  {label} never came up on port {port}.")
    return False


def start(command, environment):
    """Start one program with its own console output hidden."""
    return subprocess.Popen(command, cwd=HERE, env=environment,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def stop(process):
    if process is None or process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def run(scenario_key, hold):
    setup = SCENARIOS[scenario_key]
    model_port = free_port()
    service_port = free_port()
    service_url = f"http://127.0.0.1:{service_port}"

    print(f"Scenario {scenario_key}: {setup['title']}")
    print(f"  reported: {setup['note']}")
    print()
    print("  Starting the two servers. Both ports were free when this ran.")

    environment = dict(os.environ)
    environment.update({
        "DEMO_MODEL_URL": f"http://127.0.0.1:{model_port}",
        "DEMO_MODEL_TIMEOUT": str(setup["timeout"]),
        "DEMO_MODEL_RETRIES": str(setup["retries"]),
        "DEMO_SERVICE_HOST": "127.0.0.1",
        "DEMO_SERVICE_PORT": str(service_port),
        "DEMO_SERVICE_URL": service_url,
        "PYTHONIOENCODING": "utf-8",
    })

    stub = decoy = service = None
    try:
        if setup["stub_mode"] is not None:
            stub = start([sys.executable, STUB,
                          "--port", str(model_port),
                          "--mode", setup["stub_mode"],
                          "--delay", str(setup["stub_delay"])], environment)
            if not wait_for_port(model_port, "the model server"):
                return 1

        if setup["decoy"]:
            # A second copy of the service, listening where the model should
            # be. It is a real, healthy program. It is not a model, and it does
            # not answer POST /api/generate.
            decoy_environment = dict(environment)
            decoy_environment["DEMO_SERVICE_PORT"] = str(model_port)
            decoy_environment["DEMO_MODEL_URL"] = "http://127.0.0.1:1"
            decoy = start([sys.executable, SERVICE], decoy_environment)
            if not wait_for_port(model_port, "the program on the model port"):
                return 1

        service = start([sys.executable, SERVICE], environment)
        if not wait_for_port(service_port, "the model service"):
            return 1
        print(f"  model service  {service_url}")
        print(f"  model port     {model_port}")

        # What this scenario did is deliberately not printed. /health and
        # contract_probe.py will tell you, and reading them is the exercise.
        print()
        print("  bench.py output follows. Everything below this line is what a")
        print("  person using the program would see.")
        print("  " + "-" * 66)

        subprocess.run([sys.executable, "bench.py"], cwd=HERE,
                       env=environment, check=False)
        print("  " + "-" * 66)

        if not hold:
            print()
            print("  Everything is stopped. To look closer at this scenario, run it")
            print(f"  again as: python scenario.py {scenario_key} --hold")
        else:
            print()
            print("  The servers are still up. In another terminal, in this folder:")
            print(f"    set DEMO_SERVICE_URL={service_url}")
            print("    python contract_probe.py health")
            print("  On PowerShell the first line is")
            print(f'    $env:DEMO_SERVICE_URL = "{service_url}"')
            print("  Press Ctrl+C here when you are finished.")
            try:
                while True:
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n  Stopping.")
        return 0
    finally:
        stop(service)
        stop(decoy)
        stop(stub)


def main():
    # bench.py writes straight to the console. Without this, the lines this
    # script prints would sit in a buffer and appear after bench's output,
    # which makes the transcript read out of order.
    sys.stdout.reconfigure(line_buffering=True)

    parser = argparse.ArgumentParser(
        description="Start this folder's servers in one broken state.")
    parser.add_argument("scenario", help="0, 1, 2, 3, 4, 5, or the word list")
    parser.add_argument("--hold", action="store_true",
                        help="leave the servers running after the bench run")
    arguments = parser.parse_args()

    if arguments.scenario == "list":
        for key, setup in SCENARIOS.items():
            print(f"  {key}  {setup['title']}")
            print(f"     reported: {setup['note']}")
        return 0

    if arguments.scenario not in SCENARIOS:
        print(f"There is no scenario '{arguments.scenario}'. Try: python scenario.py list")
        return 2

    for needed in (STUB, SERVICE, "bench.py"):
        if not os.path.isfile(os.path.join(HERE, needed)):
            print(f"{needed} is missing from this folder. Copy the whole "
                  f"lab-m05-03-files folder, not one file out of it.")
            return 2

    return run(arguments.scenario, arguments.hold)


if __name__ == "__main__":
    sys.exit(main())
