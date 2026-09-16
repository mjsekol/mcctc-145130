# Chunking: Deciding What a Piece of a Document Is
---
## Slide 1: Five days
- That is a true sentence from your handbook
- It is also useless
- Five days of what
- A chunk that is too small stops being an answer
Speaker notes: Five days. True, it is in the handbook, and it answers nothing, because the chunk no longer says five days of what. Now imagine the opposite mistake and you have both failure modes of today's lesson before we have written a line.
Image: A tiny scrap of paper with the words five days on it, alone on a desk.
---
## Slide 2: The other way to get it wrong
- A whole document is one vector
- That vector averages everything in the document
- Hours, guests, glasses, training, damage, fire
- It comes back for every question, which is none
Speaker notes: Embed a whole document and its vector is an average of everything in it. The access and safety document covers six unrelated things, so it is not strongly about any of them. A chunk that comes back for every question is the same as a chunk that comes back for none.
Image: Six small topic icons blending into one grey blob.
---
## Slide 3: Split on headings first
- A heading is a boundary somebody already chose
- They knew the content when they chose it
- Then split any section that is still too long
- Never in the middle of a word
Speaker notes: Somebody who understood this material already decided where the topics change, and they wrote it down as headings. Use that. Then cut anything still too long at a blank line, a sentence end, or a space, and repeat some characters at the seam so a cut sentence survives whole in one of the two pieces.
Image: A markdown document with its headings drawn as cut lines.
---
## Slide 4: Fifty six chunks, eight documents
```
documents   8
chunks      56
shortest    76 characters
longest     608 characters
average     267 characters
```
Speaker notes: That is the real output for your handbook with a nine hundred character maximum and a hundred and twenty character overlap. Look at the longest chunk. Six hundred and eight. Hold that number for the next slide.
Image: None. This slide is code.
---
## Slide 5: Now turn the lever
```
--max-characters 900  --overlap 120     56 chunks
--max-characters 250  --overlap 30      79 chunks
--no-headings                           22 chunks
--max-characters 5000 --overlap 0       56 chunks
```
Speaker notes: Read the last line. I raised the maximum from nine hundred to five thousand and nothing moved, because no section of this handbook is nine hundred characters long. For this corpus the length limit is a safety net that never catches anything. The heading rule is the chunking strategy.
Image: None. This slide is code.
---
## Slide 6: A parameter you did not measure
- Somebody will say 512 tokens with 64 overlap
- They will call it the industry standard
- Ask what it does to your documents
- Finding out takes one command
Speaker notes: You will hear that number. It is not wrong exactly, it is unmeasured, and on this corpus it would do nothing at all. There is no standards body for chunk size. The command that settles it for your documents takes four seconds and you now know how to run it.
Image: A confident quote bubble beside a terminal showing a chunk count that did not change.
---
## Slide 7: Here is a rule with a cost
- Loan length is a thirty two character section
- Too short to stand alone
- So it attaches to the chunk before it
- Which is about contents cards
Speaker notes: A section that short is the five days problem, so the chunker attaches it to the previous chunk rather than storing a stub. Defensible rule. And now the answer to how long can I keep a camera kit is filed under a heading about contents cards, and you would never find that out unless you read your own chunks.
Image: Two adjacent chunks with the short section shown glued onto the end of the wrong one.
---
## Slide 8: What a chunk has to carry
```python
{"doc_id": "05-media-kits.md", "heading": "Memory cards",
 "ordinal": 3, "char_start": 717, "char_end": 925,
 "text": "05-media-kits.md . Memory cards\n\nThe card in the kit is a lab card. ..."}
```
Speaker notes: Two things in there are not obvious. The heading is repeated inside the text, because the embedding only ever sees the text, and a chunk whose heading is missing from it has thrown away its strongest clue. And the offsets point at the real file, which is how any hit gets traced back to a line somebody wrote.
Image: None. This slide is code.
---
## Slide 9: The four line version, and its output
```
0 '# Ridge Creek Makerspace: Loan Policy\n\nInvented sample docum'
2 'ut.\n\n## Late items\n\nAn item is late when the current date is'
```
Speaker notes: This is text sliced every five hundred characters. Chunk two starts with u t full stop, which is the tail of the word out. The word is split across two pieces and the sentence is whole in neither. No heading, no offsets, no document id. It never crashes, which is why people ship it.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Part one of lab M04-05, no model needed today
- Write chunk_text, then read your own chunks
- Run three settings and find the lever that matters
- Then write down the boundary rule and why
Speaker notes: Build one is part one of the retrieval lab and it needs no embeddings endpoint at all. You write the chunker, then you read the chunks you produced, out loud in your head, and find one that cannot answer a question on its own. Then three settings and a paragraph about which lever actually moved anything.
Image: A document being cut into labelled pieces, each piece tagged with its source and offsets.
---
