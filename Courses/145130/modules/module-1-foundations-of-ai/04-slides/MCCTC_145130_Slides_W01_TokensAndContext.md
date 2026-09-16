# Tokens and the Context Window
---
## Slide 1: It remembers me
- You have felt this
- The assistant knows your name
- It picks up where you left off
- Nothing is stored anywhere
Speaker notes: Everybody in this room has had the experience of a chat assistant seeming to remember something about them. That experience is real and the explanation everybody carries for it is wrong. By the end of this period you will know exactly what is happening instead, and it is more useful than the thing you believed.
Image: A phone screen showing a chat that appears to remember a previous conversation.
---
## Slide 2: The model does not read words
- It reads tokens
- A common word is usually one
- A name or a typo is several
- Pieces, not words, not characters
Speaker notes: This is the first of the two words. A model needs a fixed, finite list of things it can see, and there are far too many words in the world once you include names, typos, code, and every language. Pieces smaller than words give a fixed list that can still spell out anything, including a word the model has never encountered.
Image: One sentence chopped into uneven pieces, some smaller than a word.
---
## Slide 3: Three things that follow immediately
- Limits are in tokens, not characters
- Unusual text costs more
- Spelling questions are strange to it
Speaker notes: An eight thousand token limit is not eight thousand words. A paragraph of code uses more tokens than a paragraph of plain English the same length. And asking a model how many letters are in a word is asking it about something it does not directly see, which is why it gets those wrong far more often than you would expect from something that writes so well.
Image: Two paragraphs of equal length with very different token counts marked.
---
## Slide 4: Do not repeat the conversion rate
- People say four characters per token
- That is a rule of thumb
- It varies by tokenizer and by text
- Ask the tokenizer you are using
Speaker notes: You will hear a number for how many characters are in a token and somebody will state it as though it were measured. It is a rough average for one kind of text in one tokenizer. When you need the real number, run your text through the tokenizer of the model you are actually running. Your Week 3 benchmark prints its assumption at the top of every report for exactly this reason.
Image: The same sentence tokenized two different ways with different counts.
---
## Slide 5: The window is a size limit
- Not memory, a maximum per request
- Your instruction is in there
- Whatever you pasted is in there
- Whatever the program added is too
Speaker notes: Here is the second word and the one people get wrong. The context window is how much the model can take into account at once, for this one request. Nothing survives to the next request on its own. Everything that feels like continuity is a program putting the earlier text back in and paying for it again.
Image: A fixed size box with several kinds of text competing for space inside it.
---
## Slide 6: A limit you cannot see
```
prompt characters sent:      50   HTTP 200   15.1 ms   reply length 261
prompt characters sent:   52075   HTTP 200   16.3 ms   reply length 302
```
Speaker notes: Fifty characters, then fifty thousand. Both came back two hundred, at the same speed, with no complaint. That proves nothing at all, because our stand-in has no context window: it is not a model. A real model past its window does one of three things, and only one of them tells you.
Image: None. This slide is code.
---
## Slide 7: Three things a system can do at the limit
- Refuse, and say the number
- Truncate, and usually not say
- Summarise, and lose detail quietly
Speaker notes: Ours refuses. Most chat products truncate or summarise, silently. Truncating silently is the one to watch for, because the output looks completely normal. You asked about a ten page document, four pages were sent, and the answer is confident and complete about four pages. Nothing on the screen tells you.
Image: A long document with a scissors line partway through and no warning.
---
## Slide 8: Proving there is no memory
```
send({"task": "classify", "prompt": "Remember that my favourite label is account."})
send({"task": "classify", "prompt": "What is my favourite label?"})
```
Speaker notes: Two requests, one after the other, same session. The second cannot be influenced by the first, and not because the model forgot. The service keeps no session, no history, and no copy of any prompt. Its own documentation says it in one line: each request is answered and forgotten.
Image: None. This slide is code.
---
## Slide 9: So why does it feel continuous
- The product re-sends your earlier turns
- Every single time
- And pays for them every time
- Past the window, something gets dropped
Speaker notes: That is the whole explanation. The feeling of memory is your own earlier words being mailed back in with every new question. It also explains something you have noticed: long conversations start losing the beginning. That is not the assistant getting tired. That is the oldest text being dropped to make room.
Image: A growing stack of previous turns being re-sent with each new question.
---
## Slide 10: Why this is a privacy lesson too
- Later you will build the re-sending
- You decide what is kept
- For how long, and for whom
- Make that decision on purpose
Speaker notes: When you build something that feels like a conversation, you will do it by putting earlier turns back into the prompt yourself. At that moment the decision about what gets kept is yours, and it is worth making deliberately instead of inheriting it from whatever tutorial you copied. Module 3 spends three weeks on what that decision costs.
Image: A storage box with a label reading what I chose to keep.
---
## Slide 11: What you are about to build
- Send a short prompt, then an enormous one
- Record both. Both will work
- Then decide: refuse, truncate, or summarise
- Write what you would tell the person
Speaker notes: Build one is the two prompts, and the result is going to feel like a failure because both of them work. That is the finding. Build two is the design question and it is the part I am grading: your program has a document larger than the window, and you write down which of the three options you would pick and what you would tell the person either way. There is no right answer and there are several wrong ones.
Image: A prompt measured against a limit line, one character over and one under.
---
