# ablate.py  ·  SQ-18 Prompt Ablation  ·  STARTER
#
# Takes one prompt that works, removes one element at a time, runs each version,
# and prints a table of what changed.
#
# Right now it runs exactly one variant, the full prompt, which tells you
# nothing. Writing build_variants() is the quest.
#
# Run it:
#   python ablate.py                          against the bundled stub
#   python ablate.py --endpoint http://127.0.0.1:11434 --model llama3
#
# The prompt lives in base_prompt.txt, one element per line, each line tagged:
#
#   [ROLE] You are the club's equipment manager...
#   [TASK] Write the instructions a brand new club member needs...
#   [CONTEXT] The sign-out sheet is taped inside the door of Room 214...
#   [FORMAT] Give me 5 steps in a numbered list.
#   [CONSTRAINT] Keep it under 60 words.
#   [CONSTRAINT] Do not add an introduction or a closing paragraph.
#
# The tags are for you, not for the model. They are stripped before sending.

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent


def quest_folder():
    """The SQ-18 folder, whether this file sits in it or in instructor/."""
    for folder in (HERE, HERE.parent):
        if (folder / "stub_model_server.py").exists():
            return folder
    return HERE


QUEST = quest_folder()
BASE_PROMPT = QUEST / "base_prompt.txt"
RESULTS = HERE / "results"

TAG = re.compile(r"^\s*\[([A-Z]+)\]\s*(.+?)\s*$")

HEDGES = [
    "it is worth noting", "it is important to", "many experts", "many educators",
    "studies have shown", "ultimately", "depends on your specific",
    "there are many", "in general", "can vary",
]
NUMBERED_ITEM = re.compile(r"^\s*\d+[.)]\s+\S", re.M)
BULLET_ITEM = re.compile(r"^\s*[-*]\s+\S", re.M)


def read_elements(path):
    """Return [(label, text), ...] from a tagged prompt file.

    A tag that appears more than once gets a number, so two CONSTRAINT lines
    become constraint1 and constraint2 and you can remove them separately.
    """
    elements = []
    counts = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TAG.match(line)
        if not match:
            continue
        tag, text = match.group(1).lower(), match.group(2)
        counts[tag] = counts.get(tag, 0) + 1
        elements.append((tag, text))

    labelled = []
    seen = {}
    for tag, text in elements:
        if counts[tag] > 1:
            seen[tag] = seen.get(tag, 0) + 1
            labelled.append((f"{tag}{seen[tag]}", text))
        else:
            labelled.append((tag, text))
    return labelled


def assemble(elements):
    """Join element texts into the prompt that actually gets sent."""
    return "\n".join(text for _, text in elements)


def build_variants(elements):
    """Return [(label, prompt_text), ...]: the full prompt plus every ablation.

    THIS IS THE QUEST. Right now it returns one variant and one variant is not
    an experiment.

    What it has to produce:

      1. ("full", the whole prompt)
      2. One variant per element, with that element removed. Label it
         "no_<label>", so removing the role gives "no_role".
      3. At least two variants with TWO elements removed, so you can look for
         an interaction: a case where removing two together does something
         neither does alone. Label those "no_a_no_b".

    With six elements that is 1 + 6 + 2 = 9 variants, and the quest needs 8.

    Read the elements list before you write this. It is a list of
    (label, text) pairs, in the order they appear in the file, and the order
    matters: the prompt has to stay readable when a line is taken out of it.
    """
    return [("full", assemble(elements))]


def send(prompt, endpoint, model, timeout_seconds=30.0):
    """Send one prompt. Return the reply text, or None with a printed reason."""
    body = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    request = urllib.request.Request(
        endpoint.rstrip("/") + "/api/generate", data=body,
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            reply = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"    the server answered HTTP {error.code}")
        return None
    except (urllib.error.URLError, TimeoutError):
        print(f"    nothing is listening at {endpoint}, or it did not answer in time")
        return None
    except ValueError:
        print("    the server answered with something that is not valid JSON")
        return None

    if reply.get("done") is not True:
        print("    the reply is not marked done")
        return None
    text = reply.get("response")
    if not isinstance(text, str) or not text.strip():
        print("    the reply is empty or has no response field")
        return None
    return text


def measure(text):
    """Countable facts about a reply. No judgements live in here."""
    stripped = text.strip()
    if stripped.startswith("{") or stripped.startswith("["):
        shape = "json"
    elif stripped.startswith("|") or "\n|" in stripped:
        shape = "table"
    elif NUMBERED_ITEM.search(stripped):
        shape = "numbered"
    elif BULLET_ITEM.search(stripped):
        shape = "bullets"
    else:
        shape = "prose"
    return {
        "words": len(text.split()),
        "shape": shape,
        "items": len(NUMBERED_ITEM.findall(text)) + len(BULLET_ITEM.findall(text)),
        "hedges": sum(text.lower().count(h) for h in HEDGES),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Remove one prompt element at a time.")
    parser.add_argument("--endpoint", default=None,
                        help="an Ollama-compatible endpoint; omit to use the bundled stub")
    parser.add_argument("--model", default="stub-caricature")
    parser.add_argument("--prompt-file", default=str(BASE_PROMPT))
    arguments = parser.parse_args(argv)

    elements = read_elements(pathlib.Path(arguments.prompt_file))
    if not elements:
        print(f"No tagged lines found in {arguments.prompt_file}. "
              "Every element line starts with a tag like [ROLE].")
        return 2
    print(f"{len(elements)} elements: {', '.join(label for label, _ in elements)}")

    variants = build_variants(elements)
    print(f"{len(variants)} variants to run")
    if len(variants) < 8:
        print("  the quest needs at least 8. build_variants() is not finished.")

    server = None
    endpoint = arguments.endpoint
    if endpoint is None:
        sys.path.insert(0, str(QUEST))
        import stub_model_server as stub
        server = stub.start_in_background()
        endpoint = server.base_url
        print(f"  bundled stub on {endpoint}")

    RESULTS.mkdir(exist_ok=True)
    rows = []
    try:
        for label, prompt in variants:
            print(f"  {label}")
            text = send(prompt, endpoint, arguments.model)
            if text is None:
                continue
            (RESULTS / f"{label}.json").write_text(
                json.dumps({"label": label, "prompt": prompt, "response": text},
                           indent=2), encoding="utf-8")
            row = measure(text)
            row["label"] = label
            rows.append(row)
    finally:
        if server is not None:
            server.shutdown()
            server.server_close()

    print()
    print("| Variant | Reply words | Shape | List items | Hedges |")
    print("|---|---|---|---|---|")
    for row in rows:
        print(f"| {row['label']} | {row['words']} | {row['shape']} | "
              f"{row['items']} | {row['hedges']} |")
    print(f"\n{len(rows)} variant(s) recorded in {RESULTS}")
    print("Every number above is countable. The conclusion is still yours to write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
