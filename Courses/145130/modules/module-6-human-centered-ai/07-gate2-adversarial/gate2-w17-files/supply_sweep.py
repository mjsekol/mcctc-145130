"""Supply Sweep.

An automation for the school store. It runs on a schedule, reads the on-hand
counts exported from the inventory tool, decides what has to be reordered,
asks the model service to sort each request note into a category, writes a
reorder list, and records the run.

Built to the requirements in REQUIREMENTS.md.

    python supply_sweep.py --service http://127.0.0.1:5159 --once
    python supply_sweep.py --service http://127.0.0.1:5159 --every 5 --runs 2

Standard library only.
"""

import argparse
import csv
import datetime
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

RUN_LOG_HEADER = [
    "run_id", "status", "requests_seen", "reordered",
    "labelled_by_service", "note_text", "submitted_by",
]

KEYWORDS = {
    "safety": ["glove", "goggle", "glasses", "mask", "guard"],
    "consumable": ["filament", "resin", "paper", "ink", "blade"],
    "storage": ["sd card", "drive", "usb", "case"],
    "wearable": ["lanyard", "badge", "apron"],
}


def keyword_label(text):
    """Match words. Used when the service cannot give us a label."""
    lowered = text.lower()
    for label, words in KEYWORDS.items():
        for word in words:
            if word in lowered:
                return label
    return "other"


def service_is_up(service_url, timeout):
    """Ask the service whether it is running and can see a model."""
    try:
        with urllib.request.urlopen(f"{service_url.rstrip('/')}/health",
                                    timeout=timeout) as response:
            health = json.loads(response.read().decode("utf-8"))
        return bool(health.get("status") == "ok")
    except Exception:
        return False


def label_one(service_url, text, timeout):
    """Ask the service for one label. Returns (label, error_kind)."""
    payload = json.dumps({"task": "classify", "prompt": text}).encode("utf-8")
    request = urllib.request.Request(
        f"{service_url.rstrip('/')}/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            envelope = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return None, f"http_{exc.code}"
    except urllib.error.URLError:
        return None, "connection_refused"
    except ValueError:
        return None, "not_the_envelope"

    result = envelope.get("result")
    if not isinstance(result, dict) or not result.get("label"):
        return None, "empty_result"
    return result["label"], None


def notify_owner(message):
    """Send the incident to the person who owns the inventory export.

    The owner needs to know within the hour, because a missed reorder means an
    empty shelf on a day somebody planned a build around it.
    """
    print(f"  NOTICE: {message}")


def load_requests(path):
    """Read the export from the inventory tool."""
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return data.get("requests", [])


def needs_reorder(request):
    """True when this item is at or below its reorder threshold."""
    return request["on_hand"] < request["threshold"]


def write_reorder_list(rows, out_dir, run_id):
    """Write the list the store manager acts on."""
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"reorder-{run_id}.md"
    lines = [f"# Supply reorder, run {run_id}", "",
             f"{len(rows)} items at or below threshold.", "",
             "| Item | On hand | Threshold | Category |",
             "|---|---|---|---|"]
    for row in rows:
        lines.append(f"| {row['item']} | {row['on_hand']} | "
                     f"{row['threshold']} | {row['label']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def append_run_log(state_dir, run_id, status, seen, reordered, by_service, rows):
    """Append one row per run to the run log."""
    state_dir.mkdir(parents=True, exist_ok=True)
    path = state_dir / "run_log.csv"
    new_file = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new_file:
            writer.writerow(RUN_LOG_HEADER)
        for row in rows:
            writer.writerow([run_id, status, seen, reordered, by_service,
                             row["note"], row["submitted_by"]])
    return path


def run_once(args):
    run_id = datetime.datetime.now().strftime("%H%M%S")
    source = pathlib.Path(args.source)
    state_dir = pathlib.Path(args.state)
    out_dir = pathlib.Path(args.out)

    print(f"supply sweep, run {run_id}")
    print(f"  source  {source}")
    print(f"  service {args.service}")

    requests = load_requests(source)
    if not requests:
        notify_owner("the export held no requests. The export job did not run.")
        print("  status  FAILED")
        return 2

    rows = []
    by_service = 0
    for request in requests:
        if not needs_reorder(request):
            continue
        if service_is_up(args.service, args.timeout):
            label, error = label_one(args.service, request["note"], args.timeout)
        else:
            label, error = None, "service_down"
        if label is None:
            label = keyword_label(request["note"])
        else:
            by_service += 1
        rows.append({"item": request["item"],
                     "on_hand": request["on_hand"],
                     "threshold": request["threshold"],
                     "label": label,
                     "note": request["note"],
                     "submitted_by": request["submitted_by"]})

    reorder_path = write_reorder_list(rows, out_dir, run_id)
    status = "OK"

    if status == "OK":
        log_path = append_run_log(state_dir, run_id, status, len(requests),
                                  len(rows), by_service, rows)
        print(f"  run log {log_path}")

    print(f"  {len(requests)} requests seen, {len(rows)} reordered, "
          f"{by_service} labelled by the service")
    print(f"  reorder list {reorder_path}")
    print(f"  status  {status}")
    return 0


def seconds_until(hhmm):
    hour, minute = (int(part) for part in hhmm.split(":"))
    now = datetime.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += datetime.timedelta(days=1)
    return (target - now).total_seconds()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Supply sweep for the school store.")
    parser.add_argument("--service", required=True)
    parser.add_argument("--source", default="requests.json")
    parser.add_argument("--state", default="state")
    parser.add_argument("--out", default="out")
    parser.add_argument("--timeout", type=float, default=10.0)
    trigger = parser.add_mutually_exclusive_group(required=True)
    trigger.add_argument("--once", action="store_true")
    trigger.add_argument("--at", metavar="HH:MM")
    trigger.add_argument("--every", type=float, metavar="SECONDS")
    parser.add_argument("--runs", type=int, default=0)
    args = parser.parse_args(argv)

    if args.once:
        return run_once(args)

    completed = 0
    print("supply sweep scheduler started. Ctrl+C to stop.")
    try:
        while True:
            wait = seconds_until(args.at) if args.at else args.every
            print(f"  next sweep in {wait:.0f} seconds")
            time.sleep(wait)
            run_once(args)
            completed += 1
            if args.runs and completed >= args.runs:
                return 0
    except KeyboardInterrupt:
        print("\nscheduler stopped")
        return 0


if __name__ == "__main__":
    sys.exit(main())
