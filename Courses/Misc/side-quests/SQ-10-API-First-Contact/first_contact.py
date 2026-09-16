# first_contact.py  ·  SQ-10 API First Contact starter
#
# Tonight's stargazing conditions at one spot, from the Sky Watch API.
# This file runs right now and makes one real request. Try it with Sky Watch
# running in another terminal:
#
#   python sky_watch_server.py
#   python first_contact.py mill-creek
#
# Then break Sky Watch on purpose and watch this file crash. Your quest is to
# make it stop crashing, and to make every kind of failure say something
# different and useful. The checklist is in README.md.

import json
import os
import sys
import urllib.request

# Settings come from the environment, so the same file works against Sky Watch,
# against a different port, or against a real public API later.
BASE_URL = os.environ.get("SKY_WATCH_URL", "http://127.0.0.1:8095").rstrip("/")
TIMEOUT_SECONDS = float(os.environ.get("SKY_WATCH_TIMEOUT", "5"))

# Sky Watch runs on this computer. Talk to it directly, never through a proxy.
# If you switch to a real public API on the internet, the school network may
# need its proxy, so read the note about this in README.md first.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def main():
    if len(sys.argv) < 2:
        print("Usage: python first_contact.py <spot id>")
        return 2
    spot_id = sys.argv[1]
    url = f"{BASE_URL}/api/v1/spots/{spot_id}/tonight"

    # CHECKLIST ITEM 1: this line has no protection at all. Every failure
    # below it crashes the program with a traceback.
    with DIRECT.open(url, timeout=TIMEOUT_SECONDS) as response:
        data = json.loads(response.read().decode("utf-8"))

    # CHECKLIST ITEM 2: print something a person would want, not raw JSON.
    print(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
