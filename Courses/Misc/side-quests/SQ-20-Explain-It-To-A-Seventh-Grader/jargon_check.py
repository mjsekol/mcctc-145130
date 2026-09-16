"""Find the words in your script that you have not defined.

    python jargon_check.py my-script.md
    python jargon_check.py --list

It reads a script, looks for words from a list of terms a twelve-year-old will
not know, and reports the ones you used without explaining. It also flags every
sentence over 25 words and estimates how long the script takes to say out loud.

**It cannot tell you whether your explanation is correct**, and it cannot tell you
whether a definition you wrote is a good one. A twelve-year-old does that, which
is the whole quest.

Exit code 0 when nothing is flagged, 1 otherwise.

Standard library only. Built and run on Python 3.13.7.
"""

import argparse
import pathlib
import re
import sys

# Words a twelve-year-old has not met, in the sense this quest means. Some of
# them they have met as ordinary English and not as the thing you mean.
JARGON = [
    "algorithm", "api", "artificial intelligence", "attention", "context window",
    "corpus", "dataset", "deep learning", "embedding", "fine-tune", "fine tuning",
    "generative", "gpu", "hallucination", "inference", "large language model",
    "llm", "machine learning", "model", "neural network", "parameter",
    "probability", "prompt", "token", "training", "training data", "transformer",
    "vector", "weights",
]

# Phrases that count as you having explained the word. The explanation has to be
# in the same sentence or the one straight after, which is why this looks at
# sentences rather than at the whole file.
DEFINITION_CUES = [
    "means", "mean by", "is a way", "are a way", "is when", "is basically",
    "is really", "in other words", "think of it", "you can think of", "picture",
    "imagine", "is the name for", "are the name for", "is called", "are called",
    "we call", "people call", "call that", "call it", "call a", "stands for",
    "is like", "are like", "what that means", "here is what", "that is all",
]

MAX_SENTENCE_WORDS = 25
WORDS_PER_MINUTE = 130  # a slow, clear speaking pace. Time yourself and change it.


def strip_fences(text):
    """Blank out fenced code blocks. A script should not have any, and if it
    does, the code is not what we are checking."""
    out = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def sentences_with_offsets(text):
    """Every sentence, with the real character offsets it spans.

    The offsets have to come from the text itself. Adding up lengths and
    assuming one space between sentences drifts as soon as there is a paragraph
    break, and then every lookup lands in the wrong sentence.
    """
    out = []
    start = 0
    for match in re.finditer(r"(?<=[.!?])\s+", text):
        out.append((start, match.start(), text[start:match.start()]))
        start = match.end()
    if start < len(text):
        out.append((start, len(text), text[start:]))
    return out


def defined_near(sentences, start, end):
    """Is there a definition cue in the sentence holding this use, or the next one?

    The window used to be a character count either side. That was too generous:
    a cue three sentences away counted, so a word could look explained when the
    explanation was about something else.
    """
    for index, (s_start, s_end, piece) in enumerate(sentences):
        if s_start <= start < s_end or s_start < end <= s_end:
            nearby = piece.lower()
            if index + 1 < len(sentences):
                nearby += " " + sentences[index + 1][2].lower()
            return any(cue in nearby for cue in DEFINITION_CUES)
    return False


def find_undefined(text):
    lowered = text.lower()
    sentences = sentences_with_offsets(text)
    findings = []
    for term in JARGON:
        pattern = re.compile(r"\b" + re.escape(term) + r"\b")
        uses = list(pattern.finditer(lowered))
        if not uses:
            continue
        explained = any(defined_near(sentences, m.start(), m.end()) for m in uses)
        if not explained:
            line = text[:uses[0].start()].count("\n") + 1
            findings.append((term, len(uses), line))
    return sorted(findings, key=lambda f: -f[1])


def long_sentences(text):
    """Sentences over the word limit, with their word counts."""
    flat = re.sub(r"\s+", " ", re.sub(r"[#>*_`|\-]", " ", text))
    pieces = [p.strip() for p in re.split(r"(?<=[.!?])\s+", flat) if p.strip()]
    return [(len(p.split()), p) for p in pieces if len(p.split()) > MAX_SENTENCE_WORDS]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Find the words in your script you have not defined.")
    parser.add_argument("script", nargs="?", help="the script file to check")
    parser.add_argument("--list", action="store_true",
                        help="print the word list and the definition cues, then exit")
    parser.add_argument("--minutes", type=float, default=5.0,
                        help="how long the script is supposed to take. Default 5.")
    args = parser.parse_args(argv)

    if args.list:
        print("Words this tool looks for:\n")
        for term in JARGON:
            print(f"  {term}")
        print("\nPhrases that count as you having explained one, if they appear")
        print("in the same sentence as it or in the one straight after:\n")
        for cue in DEFINITION_CUES:
            print(f"  {cue}")
        print("\nIf you explained a word a way this list does not know about,")
        print("the tool will flag it and you will be right and it will be wrong.")
        print("Say so in your write-up rather than changing your wording to")
        print("please a program.")
        return 0

    if not args.script:
        parser.error("give a script file to check, or pass --list")

    path = pathlib.Path(args.script)
    if not path.exists():
        print(f"No file at {path}")
        return 2

    raw = path.read_text(encoding="utf-8", errors="replace")
    text = strip_fences(raw)

    undefined = find_undefined(text)
    long_ones = long_sentences(text)
    words = len(text.split())
    minutes = words / WORDS_PER_MINUTE

    print(f"{path.name}: {words} words, about {minutes:.1f} minutes at "
          f"{WORDS_PER_MINUTE} words a minute")
    if minutes > args.minutes * 1.2:
        print(f"  That is longer than the {args.minutes:.0f} minutes you have. Cut "
              f"about {int((minutes - args.minutes) * WORDS_PER_MINUTE)} words.")
    elif minutes < args.minutes * 0.5:
        print(f"  That is well under {args.minutes:.0f} minutes. Either you have "
              f"left something out, or you have been admirably ruthless.")
    print()

    if undefined:
        print("USED AND NOT EXPLAINED")
        for term, count, line in undefined:
            times = "time" if count == 1 else "times"
            print(f"  {term:<22} used {count} {times}, first at line {line}")
        print()
        print("  Each of these needs a sentence near it saying what it means, in")
        print("  words a twelve-year-old already has. Not a better technical")
        print("  definition. A different kind of sentence.")
        print()

    if long_ones:
        print(f"SENTENCES OVER {MAX_SENTENCE_WORDS} WORDS")
        for count, sentence in long_ones:
            print(f"  {count} words: {sentence[:80]}...")
        print()
        print("  A long sentence read out loud to a twelve-year-old loses them in")
        print("  the middle. Cut each one into two.")
        print()

    if not undefined and not long_ones:
        print("Nothing flagged.")
        print()
        print("That is the floor, not the grade. This tool cannot tell whether")
        print("your explanation is true, and it cannot tell whether a definition")
        print("you wrote actually helps anybody. A twelve-year-old does that,")
        print("and that is the quest.")
        return 0

    print(f"{len(undefined)} undefined term(s), {len(long_ones)} long sentence(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
