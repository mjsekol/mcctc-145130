# Reading a License Instead of Reading About One
---
## Slide 1: You have had this argument already
- Somebody says MIT means you must open source
- Somebody says GPL means you cannot sell it
- Both are false and both get repeated
- The file that settles it is on your disk
Speaker notes: You have heard both of those claims in this building. Working developers repeat them too. Today you settle arguments like that in under a minute, by opening a file instead of asking anybody, and the file turns out to be shorter than the argument.
Image: Two speech bubbles disagreeing, with a plain text file sitting between them.
---
## Slide 2: Three questions, always in this order
- What does it PERMIT that you could not do before
- What does it REQUIRE from you in exchange
- What does it FORBID no matter what
- What TRIGGERS the requirements
Speaker notes: Every license answers these. Write the answers in these words because your licensing audit asks for exactly them. The fourth one is the question nobody asks and it decides whether any of the rest is live today.
Image: Four numbered bands down the page, the fourth in accent blue.
---
## Slide 3: The whole MIT obligation, found in eight seconds
```python
text = open("vendor/pocketgrid/LICENSE", encoding="utf-8").read()
print(len(text.split()), "words")
for paragraph in text.split("\n\n"):
    if "shall be included" in paragraph:
        print(paragraph.strip())
```
Speaker notes: Watch how fast this settles. I am reading the license file itself and pulling out the one paragraph that states a condition. No summary, no search, no model. The file on my disk.
Image: None. This slide is code.
---
## Slide 4: One hundred sixty nine words, one condition
```
169 words
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```
Speaker notes: That is the entire obligation of the MIT license. Not open source your project. Not credit us on the About screen. Include the notice. Next time somebody tells you what MIT requires, do this instead of arguing.
Image: None. This slide is code.
---
## Slide 5: Three families, one bargain each
- Permissive: do nearly anything, keep the notices
- Copyleft: what you convey stays under the same terms
- Restricted use: a list of things you may not do
- Model licenses are usually the third kind
Speaker notes: Three families. The third one is where most model licenses live, and it is the one students have never met. Open the model license in your fixture and you find a list of forbidden uses and an automatic termination clause. That is not an open source license and the difference matters on Thursday.
Image: Three doors, each with a different sign on it, the third with a list.
---
## Slide 6: Two corrections worth saying out loud
- The GPL permits commercial use and charging money
- Its conditions are about conveying, not about using
- Apache 2.0 adds a patent grant. MIT has none
- Apache section four is a checklist. Read it
Speaker notes: Both GPL corrections get said wrong in this room every year. The GPL is not an anti-money license. It is a same-terms-travel-with-it license. And Apache adds a patent grant that MIT is completely silent on, which is the reason a lot of companies prefer it.
Image: Two myth cards crossed out, two fact cards beside them.
---
## Slide 7: Which obligations are awake right now
```
Plan: running it on your own laptop
  Nothing is conveyed to anybody else.

Plan: putting the repository on GitHub
  MIT                  ship the copyright notice and the permission notice
  Apache-2.0           ship the license, the NOTICE contents, and mark changed files
  GPL-3.0-or-later     ship the license and the corresponding source, under the GPL
  CC-BY-4.0            give attribution in the form section 3 sets out
  You changed something, so every 'state your changes' clause applies.
```
Speaker notes: Look at the second plan. Every one of you moved from the first plan to the second in week one of this program and nobody stopped to notice. Pushing to a public repository is conveying. That is the day the obligations wake up.
Image: None. This slide is code.
---
## Slide 8: The identifier is a convenience, not the license
- Four of ten components carry an SPDX tag
- Pocketgrid has a full MIT license and no tag
- Sortwell has a clear GPL header and no tag
- No identifier is a signal to go read
Speaker notes: If you had written a tool that treats a missing tag as a missing license, you would have flagged the two cleanest components in the tree and missed nothing that was actually wrong. A missing tag is never a finding. A finding is something you read, or a documented absence of anything to read.
Image: A ten-row list with four tags shown and six blanks.
---
## Slide 9: The conflict sitting in your fixture
- The project LICENSE says MIT
- vendor/sortwell says GPL version 3 or later
- There is no copy of the GPL in the tree
- Auditors surface conflicts. They do not settle them
Speaker notes: What counts as one combined work is a genuine long-running argument and you are not going to settle it this period. What is not arguable is that the front of the project says one thing, the tree contains another, nobody has written anything down, and the license that was supposed to travel with that code is missing. That is your finding.
Image: A project card labelled MIT with a GPL-labelled folder inside it.
---
## Slide 10: The wrong version, with three false cells
```
| License    | Commercial use | Must credit | Must open source your code |
|------------|----------------|-------------|----------------------------|
| MIT        | Yes            | No          | Yes                        |
| Apache-2.0 | Yes            | Yes         | No                         |
| GPL-3.0    | No             | Yes         | Yes                        |
| CC-BY-4.0  | Yes            | Yes         | No                         |
```
Speaker notes: A model writes this in two seconds. Three cells are wrong and you have the files open to prove it. Notice what it got right, because that is what makes it dangerous. Apache and CC BY pass a glance, and three correct rows buy the wrong ones their credibility.
Image: None. This slide is code.
---
## Slide 11: What you are about to build
- Open every license in the Study Buddy tree
- Write permits, requires, forbids, triggers for each
- Find the one component with no license file
- Escalate the conflict. Do not settle it
Speaker notes: Build one is Lab M03-01, and the requirement is that every cell in your table traces to something you read, not something you were told. Build two is the first pass of your licensing audit manifest. Where a component has nothing, write nothing found. That is a result, not a gap.
Image: A permits, requires, forbids table with one row marked escalate.
---
