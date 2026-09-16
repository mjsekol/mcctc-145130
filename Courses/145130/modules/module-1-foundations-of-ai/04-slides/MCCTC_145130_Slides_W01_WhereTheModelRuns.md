# Where the Model Actually Runs
---
## Slide 1: The AI is down
- Four words, three different problems
- Three different fixes
- You have said this sentence
- After today you cannot
Speaker notes: Somebody says the AI is down. What is actually down. Nothing is listening at all, or something is listening and answering badly, or your own program cannot read the answer it got. Those are three different problems with three different fixes, and one sentence covering all three costs a period. Today you start the server yourself and find out which is which.
Image: Three stacked boxes, only one of them dark.
---
## Slide 2: Two programs, one HTTP call
- Your program sends a prompt
- A model server sends text back
- That is the whole architecture today
- Nothing sits in between
Speaker notes: This is the smallest thing that counts as an AI system. One program posts a prompt, another answers with text. There is no layer catching failures for you and no layer turning the text into something tidy. Everything that has to happen to that text is going to happen in your code, and by Friday of next week you will have opinions about that.
Image: Two boxes with one arrow out and one arrow back.
---
## Slide 3: What actually comes back
```
HTTP 200
{"model": "llama3.2", "created_at": "...",
 "response": "```json\n{\"label\": \"network\"}\n```",
 "done": true}
```
Speaker notes: Three fields. Look at where the answer is. It is a string, sitting in response, with a code fence around it, inside the JSON of the reply. To get the word network out of that you strip a fence and parse again, and you write code that survives the day the fence is not there. Read that block twice, because the rest of this module hangs off it.
Image: None. This slide is code.
---
## Slide 4: The model returns text, not data
- Not a label. Not a number
- A string, and nothing promises what is in it
- Sometimes JSON. Sometimes a sentence
- Sometimes a polite refusal
Speaker notes: Write this one down. Everything downstream comes from it. The model has no obligation to answer in the shape you wanted, and when it does not, nothing tells you. Your program finds out by trying to read a value and failing, which means your program has to be written expecting to fail.
Image: One string with four very different contents branching from it.
---
## Slide 5: A request this server refuses
```
HTTP 400
{"error": "this stub only supports stream: false"}
```
Speaker notes: That is the second request in one underscore request dot py. It asked for streaming and this server does not do streaming. Notice what you got: a status code you can branch on and a sentence you can show somebody. That is the good kind of failure. Notice also what happened: the program assumed a capability that was not there, which is the most ordinary integration failure in the world.
Image: None. This slide is code.
---
## Slide 6: Three answers, all HTTP 200
- Fenced JSON with a label inside
- A sentence starting Label
- I am not able to help with that request
- All three succeeded. One is useless
Speaker notes: Same request, three modes of the stand-in. Every one of them is status two hundred with done true and real text. At the level of the request all three worked. Only the third one is useless, and nothing in the reply says so. Your program finds out by trying to read a label and coming up empty.
Image: Three reply cards side by side, all marked 200, one crossed out.
---
## Slide 7: So record how you got it
```
  MT-2002  network   read from json
  MT-2007  hardware  read from prose
  MT-2011  no label  read from unparsed
```
Speaker notes: That third column is not free. Somebody wrote the code that keeps it. Without it, three weeks from now nobody can tell a label the model produced from a fragment of text your parser sliced out of a sentence. Provenance is a field you decide to keep, and nobody adds one later, because by then the runs that needed it are gone.
Image: None. This slide is code.
---
## Slide 8: The two-line version, and why it breaks
```python
answer = json.loads(response)["response"]
label = json.loads(answer)["label"]
```
Speaker notes: This works on a good day and it is the version everybody writes first. It crashes on the code fence, because the answer starts with three backticks. Patch that and it crashes on prose. Patch that with a bare except and it gets worse, because now a refusal quietly becomes whatever your fallback produces and it prints in the same column as a real label.
Image: None. This slide is code.
---
## Slide 9: What that looks like when it happens
- label: Label: hardware
- Why:
- That is not a label
- It is a slice of somebody's sentence
Speaker notes: This is real output from a program in next week's Gate 2, run against a server answering in prose. The label column now holds two lines of somebody else's writing, and it wraps. The program that produced it had a comment above the parse claiming the model always answers with JSON. The comment was wrong and the code trusted it.
Image: A terminal where a label column has wrapped onto a second line of prose.
---
## Slide 10: No account, no key, ever
- Commercial developer services require users 18 or older
- This course never uses one
- Nothing you type leaves the building
- Nothing in this module stores anything
Speaker notes: This is not only a rule about your age. The model runs on a machine in this room and there is no account to make. And notice the last line: nothing in this module keeps a session, a history, or a copy, because nobody wrote code to make one. Next week you will review a program that starts doing it without being asked.
Image: A building outline with the whole system inside it and no arrows leaving.
---
## Slide 11: In Module 5 you build the layer
- One service between the application and the model
- It handles the mess once
- Every caller gets the same shape
- You are supposed to feel the problem first
Speaker notes: A real product does not scatter this work across every program that wants an answer. It puts one small service in the middle. That service is your Module 5 performance task, which is exactly why it is not in your kit today. By Friday of next week you will have written the same parsing twice in two different programs, and the argument for a shared layer will make itself.
Image: The same two boxes with a third appearing between them, greyed out and labelled Module 5.
---
## Slide 12: What you are about to build
- Start the model server yourself
- Send one request and read three fields
- Then ask for streaming and get refused
- Then finish yesterday's comparison
Speaker notes: Build one is two terminals and one request, and you are not finished until you can point at the response field and say what kind of thing is in it. Then the refused request, which is your first failure at a seam. Build two is yesterday's comparison with the other column finally filled in, and the question about that column is the one worth the most marks.
Image: Two terminals side by side, each with a different program running.
---
