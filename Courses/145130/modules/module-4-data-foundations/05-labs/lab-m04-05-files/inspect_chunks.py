# inspect_chunks.py . Lab M04-05 starter, part 1
#
# Chunk the handbook and look at what came out, with no model involved.
#
#   python inspect_chunks.py
#   python inspect_chunks.py --max-characters 400 --overlap 40
#   python inspect_chunks.py --show 05-media-kits.md
#
# Part 1 of this lab needs no embeddings endpoint and no model. Chunking is a
# decision about text, and the decision is easier to judge when you can read the
# pieces.

import argparse
import os
import sys

from chunker import chunk_folder, DEFAULT_MAX_CHARACTERS, DEFAULT_OVERLAP

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOCS = os.path.join(HERE, "..", "fixtures", "ridge-makerspace", "handbook")


def summarize(chunks):
    by_document = {}
    for chunk in chunks:
        by_document.setdefault(chunk["doc_id"], []).append(chunk)
    lengths = [len(chunk["text"]) for chunk in chunks]
    print(f"documents   {len(by_document)}")
    print(f"chunks      {len(chunks)}")
    print(f"shortest    {min(lengths)} characters")
    print(f"longest     {max(lengths)} characters")
    print(f"average     {sum(lengths) // len(lengths)} characters")
    print()
    print(f"  {'document':<28} {'chunks':>6}  {'shortest':>8}  {'longest':>7}")
    print(f"  {'-' * 28} {'-' * 6}  {'-' * 8}  {'-' * 7}")
    for doc_id in sorted(by_document):
        sizes = [len(chunk["text"]) for chunk in by_document[doc_id]]
        print(f"  {doc_id:<28} {len(sizes):>6}  {min(sizes):>8}  {max(sizes):>7}")


def show(chunks, doc_id):
    print(f"\nEvery chunk of {doc_id}, in order:\n")
    for chunk in chunks:
        if chunk["doc_id"] != doc_id:
            continue
        print(f"--- chunk {chunk['ordinal']}  heading: {chunk['heading']!r}  "
              f"characters {chunk['char_start']}-{chunk['char_end']}  "
              f"length {len(chunk['text'])}")
        print(chunk["text"])
        print()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Chunk the handbook and look at the pieces.")
    parser.add_argument("--docs", default=DEFAULT_DOCS)
    parser.add_argument("--max-characters", type=int, default=DEFAULT_MAX_CHARACTERS)
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP)
    parser.add_argument("--no-headings", dest="use_headings", action="store_false",
                        help="ignore headings and cut on length alone")
    parser.add_argument("--show", help="print every chunk of one document")
    arguments = parser.parse_args(argv)

    chunks = chunk_folder(arguments.docs,
                          max_characters=arguments.max_characters,
                          overlap=arguments.overlap,
                          use_headings=arguments.use_headings)
    if not chunks:
        documents = [name for name in os.listdir(arguments.docs)
                     if name.endswith(".md")] if os.path.isdir(arguments.docs) else []
        if not documents:
            print(f"No .md files in {arguments.docs}")
            return 1
        print(f"{len(documents)} documents found and 0 chunks produced.")
        print("chunk_text is returning an empty list. That is part 1, step 4.")
        return 0
    headings = "used" if arguments.use_headings else "ignored"
    print(f"max_characters {arguments.max_characters}   overlap {arguments.overlap}"
          f"   headings {headings}\n")
    summarize(chunks)
    if arguments.show:
        show(chunks, arguments.show)
    return 0


if __name__ == "__main__":
    sys.exit(main())
