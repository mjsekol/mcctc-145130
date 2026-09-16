# Authenticity, and What a Citation Is For
---
## Slide 1: You have cited sources for years for the wrong reason
- You were taught citation as formatting and honesty
- Both of those are true
- Neither of them is why the rule exists
- A citation is instructions for checking a claim
- Without having to trust the person who made it
Speaker notes: Since about sixth grade you have been told to cite your sources, and it was framed as a rule about formatting and about not stealing. That framing is true and it is not the reason. A citation is a set of instructions that lets a reader go and check a claim without trusting you. That is its job. A citation that does not let a reader go and look has failed at its job, no matter how correctly it is punctuated. This matters more than it used to, because claims are now cheap to generate and so are citations.
Image: A claim on the left and a source document on the right, with a numbered path between them a reader can walk.
---
## Slide 2: Four parts, and each one narrows the search
- Who: find the person or organisation responsible
- What: find the specific work, not the whole publication
- Where: the exact page, section, timestamp, or table
- When: know which version you are looking at
- Studies have shown has none of the four
Speaker notes: Run any citation through those four and see what is missing. A recent survey found has one part and about half of another, and neither of them lets you go and look. Here is the sentence to write down. A claim with an uncheckable source is not weakly supported, it is unsupported, and you treat it exactly the same as a claim with no source at all. That is a harder standard than you have been held to before and it is the standard in this module.
Image: Four narrowing funnels stacked, labelled who, what, where, when, ending at a single page.
---
## Slide 3: The raw material, and the version that drops things
```
SOURCE. Media Club equipment memo, section 3 (constructed for this lesson).

"Cameras returned after 3:15 are logged as late. A late return does not carry a
penalty on the first occasion. On a second late return in the same quarter, the
member loses checkout privileges for two weeks. The advisor may waive this for
a documented conflict."

BADLY EXTRACTED
"You get banned for two weeks if you are late."
```
Speaker notes: That memo is invented for this lesson and I am labelling it as invented, which is a habit you should copy. Now read the extraction underneath it. It is short, it is confident, and it is the sentence most people would write in a hurry. Take twenty seconds and find everything it dropped.
Image: None. This slide is the source and the extraction.
---
## Slide 4: It is wrong in three separate ways
- It drops the first occasion exception
- It drops the same quarter scope
- It drops the advisor waiver
- Every one of those changes what somebody would do
Speaker notes: This is why extraction is a graded skill rather than a formality. A member reading the bad version thinks one late return costs them two weeks, so they do not check out the camera at all, and the club loses a photographer for a game. Nothing in the bad version is invented. It is all compression, and compression is where accuracy goes when you are in a hurry. A summary that changes what somebody would do is not a summary.
Image: The original paragraph with three clauses highlighted and struck through in the compressed version.
---
## Slide 5: The version a reader can check
```
WELL EXTRACTED

A camera returned after 3:15 is logged late. The first late return in a quarter
carries no penalty; a second costs two weeks of checkout privileges, and the
advisor may waive it for a documented conflict.
(Media Club equipment memo, section 3)
```
Speaker notes: Notice what that citation hands the reader. The document, and the section. They can open it and check whether you dropped anything, which is the entire point. It is one line, it costs you nothing, and it converts a sentence people have to trust into a sentence people can verify.
Image: None. This slide is the extraction.
---
## Slide 6: The four-step check, in the order that works
- Does the venue exist? Search the publication name in quotes
- Does the work exist? Search the title in quotes
- Does the author exist, and did they write this
- Do the year, volume and page range match
- Record the catalog, the exact string, and what came back
Speaker notes: The order is deliberate. A publication is quicker to find than an article, so if the venue does not exist you are finished in thirty seconds. Step four is the interesting one, because a real work with wrong numbers is a Validity failure rather than a hallucination, and you will meet at least one of those. Now the rule that catches most of the class. A negative result is a result only if you recorded the search. I could not find it, with no search string, is not a finding.
Image: Four numbered steps descending, each with a stopwatch showing it takes less time than the one below.
---
## Slide 7: What a recorded check looks like
```
NOT A FINDING
"This source is fake."

A FINDING
The venue "Proceedings of the Workshop on Classroom Systems" returned no
results. A similarly named workshop does exist, and searching its proceedings
index for the title returned nothing. Volume 10 of that index covers a
different year than 2011.
```
Speaker notes: That second paragraph is worth more than the word fake, and here is why. It shows the reader precisely what was checked, and it is honest about the part that is still ambiguous. Most of you will hit a check that comes back complicated, where the venue almost exists or the author is real and writes about something else. That is the most valuable outcome in this lab and most students treat it as a failure. Do not resolve ambiguity by rounding to a verdict. Partial matches are common and they are exactly where a careless checker stops.
Image: None. This slide is a finding.
---
## Slide 8: The wrong way, and it is the first thing everybody tries
- Ask the model whether its own citation is real
- It says yes, or it cannot verify, or it apologises
- None of those is a check, because nothing looked anything up
- A fake citation and yes that is real are both likely text
- Asking a second model is two guesses, not a check
Speaker notes: Do the wrong version live and do it confidently. Ask the model, get an answer, and then say out loud why it is worthless. Asking a model whether its output is true is asking the same process to produce a second piece of text. If a citation-shaped continuation was likely, then yes that is a real paper is also a likely continuation. The subtler version is asking a different model, which is better because the errors are less correlated, and still not a check. Here is the line. A check has to touch the world. A catalog, a library, an index, the actual document.
Image: A model producing a citation and then producing a yes beside it, with a dotted line to an untouched library.
---
## Slide 9: Misattribution survives the check most people run
- Uncredited reuse: a passage that tracks a source, unnamed
- Misattribution: a real quote assigned to the wrong person
- Misattribution is worse, because the quote is real
- A searcher confirms it exists and stops
- The invented quote fails that same search and gets caught
Speaker notes: Two shapes and they are different problems. Uncredited reuse happens because the model was trained on that text and text near it is a likely continuation. Nobody decided to copy, and the effect on the person whose work it is does not care about the mechanism. Misattribution is the dangerous one for a reason worth understanding. It passes the check. Somebody searches the quote, finds it immediately, sees that it is real, and stops one question too early. The invented quote gets caught. The misattribution keeps travelling.
Image: Two quotes, one failing a search with a red cross, one passing a search with the wrong name attached.
---
## Slide 10: How you cite everything in this module
- A document: title, and section or page
- A web page: title, publisher, the URL, and that you opened it
- A model output: the run label and the prompt file
- A search that found nothing: catalog, exact string, no results
- Model output gets cited like anything else
Speaker notes: Look hard at the third row. If a sentence in your brief came out of a model, you say so and you point at the run. That is not an admission, it is a citation, and a reader who wants to check can open runs slash v three dot json and read the prompt that produced it. Module three takes the legal side of this much further, because who owns the output of a generative model is a live, unsettled question, and this course is not going to pretend otherwise.
Image: A four-row citation card, one row per source type, with the model output row circled.
---
## Slide 11: What you are about to build
- Four supplied citations, the four-step check on each
- Two are fabricated, one is real, one is deliberately ambiguous
- Record the catalog, the exact string, and what came back
- Then extract three claims from a reference run and cite them
- One of the three has to be one you could not verify
Speaker notes: Build one is the check drill. Four citations, and you do not get told which is which. For the ambiguous one, write down what is still unresolved rather than picking a verdict, because that is what is being assessed. Build two is extraction. Three claims, each with a citation a reader could follow, and one of them has to be a claim you could not verify, which you say plainly instead of dropping. At close, the exit ticket is one question. What is the difference between I could not find it and a recorded negative result.
Image: Four citation cards face down on a desk with a search log beside them, three lines already filled in.
---
