# User Help for the Person Who Is Stuck
---
## Slide 1: Nobody reads this when things are going well
- They read it because something did not work
- They are behind on something else
- They want one sentence telling them what to do
- Write for that moment, not for your architecture
Speaker notes: Every other document in this module is written for somebody building the system. This one is written for somebody using it, and it stopped working. That person is not a developer, is not interested in your layers, and is reading because they are annoyed. That changes everything about how it is written, and almost nobody makes the change.
Image: A person at a terminal with a frustrated posture and one open help page, in muted grey and navy.
---
## Slide 2: Four sections, in the order the reader needs them
- What this program does: should I be using this
- How to start it: I have it and nothing happened
- What every message means: it said something
- When it says fallback: it worked and looks wrong
Speaker notes: Four sections and the order is the order somebody needs them in, not the order that is tidy. The fourth one is specific to a program with a model in it, and it is the most important section in the whole document, because a fallback is the program working correctly and it does not look like it.
Image: Four numbered cards in a row, the fourth one enlarged and in accent blue.
---
## Slide 3: Three rules
- Every message the program can print is in the table
- Every row says what to do, not what happened
- No word the reader has to look up
Speaker notes: Three rules. Every message, not most of them, because a reader who hits a line that is not in your help has learned that reading it is a waste of time, and that lesson applies to the whole document. Every row says what to do. And no jargon, not because they are not clever, but because they are already looking one thing up and you have added a second.
Image: Three rule cards, each with a short example of the rule broken in accent red underneath.
---
## Slide 4: The message table
```
You see                                 It means            Do
from FALLBACK, not the model            built by a rule     read the why: line
reachable no                            no model found      start the stand-in
The model service is not answering.     service not running start it, window 2
The reply was not the shape expected.   wrong port          check the port
```
Speaker notes: Look at the middle column and notice what is not in it. Deserialise is not there. Envelope is not there. Nothing named after a class in your code is there. The reader does not have those words and does not need them, and every one you use costs them another lookup.
Image: None. This slide is code.
---
## Slide 5: The section that keeps somebody out of trouble
```
  source       fallback
  elapsed_ms   2057
  headline: The 3D printer in room 118 jammed near the nozzle.
  error kind:    connection_refused
  error message: nothing is listening at http://127.0.0.1:11535
```
Speaker notes: Show them the real output, then tell them what it means for them. A fallback headline is the first line of what somebody wrote, which is usually fine and never insightful. It is right when the first line happens to be the point and wrong when it is not. Then give them permission to refuse to use it.
Image: None. This slide is code.
---
## Slide 6: The same fact, three ways
```
for the compiler   the client resolves its base address from an environment
                   variable and surfaces a ServiceDown failure kind

for a manager      The application requires the model service to be
                   available. An appropriate error will be displayed.

for the stuck      If you see "The model service is not answering.",
                   go to window 2 and start the service again
```
Speaker notes: One fact, three ways. The first is all true and the reader has none of those words. The second has no jargon and also no information, because it does not say what the message is or what to do. The third quotes the exact line they are staring at, names the missing thing the way they started it, and gives the command. Twenty eight words.
Image: None. This slide is code.
---
## Slide 7: Nine words that are the most important section
```
## When it says the answer is a fallback

The fallback is used when the model is unavailable.
```
Speaker notes: This is a real submission shape. Nine words. It does not say how you know, it does not say how much to trust a fallback answer, and it does not say what to do about it. For a program with a model in it, this is the section that stops somebody handing on a page of first sentences as though a model had written them.
Image: None. This slide is code.
---
## Slide 8: Who this sentence locks out
- "Install the model runtime with administrator rights on your own laptop"
- Everybody on a lab machine
- Anybody on a school-managed computer
- And the stand-in server ships with the program
Speaker notes: Read that first line and count who it excludes. Everybody on a lab machine, which is most of this class most of the time. It also asks them to install something they do not need, because a stand in model server ships with the program, needs no rights and no download, and starts with one command. The honest version leads with the path that works for everybody.
Image: A door with a keycard reader and a queue of people who do not have a card, in muted grey.
---
## Slide 9: Why people write for the compiler instead
- You know how it works, so writing what you know is quick
- Working out what somebody else does not know is slow
- And jargon sounds more professional
- "Leverages an LLM via a RESTful microservice" sounds like documentation
Speaker notes: Two reasons and the second is the honest one. Writing what you know is quick. Working out what somebody else does not know is slow. And there is a pull toward sounding professional, because leverages an LLM via a RESTful microservice architecture sounds more like real documentation than it reads help requests and sorts them, and it is worse in every way that matters.
Image: Two sentences side by side, the long one in grey, the plain one in navy, with a reader icon beside the plain one.
---
## Slide 10: What you are about to build
- Your own message table, every line your program prints
- Your own fallback section, with real captured output
- Then hand it to one person who has never seen it
- Write down every question. Do not answer them.
Speaker notes: Build one is your message table and your fallback section. Build two is the test. Hand the program and the document to one person who has never seen either, sit behind them, and write down every question they ask out loud. Do not answer. Every question is a line missing from your help, and this is also where Module six starts.
Image: Two students, one at the keyboard and one behind with a notepad, in navy and accent blue.
