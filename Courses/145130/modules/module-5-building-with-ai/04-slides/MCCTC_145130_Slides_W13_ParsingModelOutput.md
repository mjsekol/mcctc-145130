# Parsing Model Output Into Something You Can Rely On
---
## Slide 1: You asked for JSON. You were specific.
- Your prompt said "Reply with JSON only"
- You gave it an example of the shape
- Here are three real answers to that prompt
- Exactly one of them json.loads will accept
Speaker notes: You wrote a careful prompt. You said reply with JSON only, shaped exactly like this, and you gave an example. I have ten real answers to that prompt saved in the lab folder. Three of them are on the next slide. All three are cooperative. None of them is the model being difficult. And exactly one of the three is something json dot loads will take.
Image: Three terminal panes side by side showing three differently shaped answers to the same prompt.
---
## Slide 2: All three of these are the model cooperating
```
answer 1   {"title": "Chemistry unit 4", "steps": [...], "minutes": 45}

answer 2   [FENCE json]
           {"title": "Chemistry unit 4", ...}
           [FENCE]

answer 3   Sure, here is the study plan you asked for in JSON:
           [FENCE json]
           {"title": "Algebra 2 quiz prep", ...}
           [FENCE]
           Let me know if you would like it broken into smaller sessions.
```
Speaker notes: The word FENCE in square brackets stands for three backticks, which cannot be printed inside a block like this one. So: bare JSON, then JSON in a fence, then JSON with a sentence in front of it and a sentence after it. None of these is wrong from the model's point of view. Your job is not to make the model behave. Your job is to turn whatever it said into a shape, or to say plainly that there was no shape in there.
Image: None. This slide is code.
---
## Slide 3: Two functions, and the split is the lesson
- parse pulls a shape out. Returns it, or nothing.
- validate decides whether the shape is usable
- validate returns the reason, not a boolean
- A parser that validates gives you one answer for ten problems
Speaker notes: Two functions, and keeping them apart is the whole point. Parse pulls a shape out of the mess and returns the shape or None. It does not judge. Validate judges and returns the reason it said no, in a sentence. Put them together and the caller gets None for ten different problems, and the service above you has to write a real reason into the envelope and cannot invent one you did not give it.
Image: Two boxes with one arrow between them, the first labelled shape, the second labelled judgement.
---
## Slide 4: JSON first, prose second, because you guess last
```
1. strip the code fence, if there is one
2. json.loads the whole thing
3. json.loads the widest run from first { to last }
4. read it as prose: labelled lines, bullets, numbers
5. nothing worked, return None
```
Speaker notes: Order matters. JSON first because a JSON answer is unambiguous. Prose second because reading prose means guessing, and you guess last. Step three is what rescues the answer that starts with Sure here is the JSON. Step one is the single most common reason a first attempt at parsing model output fails.
Image: None. This slide is code.
---
## Slide 5: Three details in nine lines that are load bearing
```python
FENCE_PATTERN = re.compile(r"[FENCE][a-zA-Z0-9_-]*\n(.*?)[FENCE]", re.DOTALL)

def find_json_object(text):
    candidate = strip_fences(text)
    for attempt in (candidate, widest_braced_run(candidate)):
        if attempt is None: continue
        try: data = json.loads(attempt)
        except (json.JSONDecodeError, ValueError): continue
        if isinstance(data, dict): return data
    return None
```
Speaker notes: FENCE in that pattern stands for three backticks again. Three things here carry weight. The language tag after the backticks is optional, so this matches a fence tagged json, a fence tagged JSON, and a bare fence. The isinstance check for dict is there because json dot loads of the text four five succeeds and gives you an integer. And the loop tries two candidates in order, first one that works wins, rather than an if else ladder.
Image: None. This slide is code.
---
## Slide 6: The model sent a sentence where you asked for a number
- You asked for minutes. It sent "about 25 minutes".
- Pull the first run of digits out. Use 25.
- Check isinstance bool before isinstance int
- In Python, True is an int
Speaker notes: Here is a real captured answer with about twenty five minutes in the minutes field. Refusing that throws away a usable answer, so you pull the digits out. And the bool check on the first line is not paranoia. In Python True is an int, so without it, minutes true becomes one minute, one minute is inside your allowed range, validation passes, and somebody gets a one minute study session with no error anywhere.
Image: A JSON snippet with the string value highlighted, an arrow to the integer 25, and a small warning marker on a boolean case.
---
## Slide 7: Trimming is not failing. Inventing is failing.
- Six bullets, limit five: cut to five and use it
- A 400 character bullet: shorten it and use it
- A label the model made up: refuse it
- The trimmed bullet still means what the model meant
Speaker notes: Where do you stop coercing. Here is the rule. Trimming keeps what the model meant, so six bullets becomes five and a long bullet becomes a short one, and both get used. An invented category does not mean anything the rest of your system can act on. It gets refused even though it is a perfectly good string, because your database, your report, and your filters have never heard of it.
Image: Two panels, one showing a list being trimmed in accent blue, one showing an invented value being rejected in accent red.
---
## Slide 8: Watch this regex throw away good answers
```
parse_plan uses one pattern: a fence, the word json, then the body

  mode fenced_json:  source='model'  error=None
  mode bare_json:    source='model'  error='plan_validation_failed'
  mode prose:        source='model'  error='plan_validation_failed'
```
Speaker notes: This is a real defect from this week's Gate two. It looks careful. It handles the fence. And it throws away every bare JSON answer and every prose answer, silently, and reports validation failed, which sends whoever reads that log looking at the model instead of at the regex. Two perfectly good answers destroyed by one pattern that only ever met the happy path.
Image: None. This slide is code.
---
## Slide 9: Why the happy path regex is tempting
- It worked on the first answer you tested with
- The model wrapped its JSON in a fence that day
- Models are not deterministic
- Capture answers. Keep them. Test against all of them.
Speaker notes: It is tempting because it worked. You wrote the prompt, you ran it once, the model used a fence, your regex matched, and everything you saw said it worked. The habit that prevents it is capturing answers and keeping them. Ten files in a folder. Every time the model does something new, save it next to the others and add a test. You did not have to imagine any of it.
Image: A folder of ten captured answer files with a green check beside each, navy and accent blue.
---
## Slide 10: What you are about to build
- Lab M05-02, ten captured answers, twenty tests
- The tests are written. Make them pass.
- parse returns a shape or None
- validate returns a sentence, never a boolean
Speaker notes: Build one is lab M zero five dash zero two. Ten real captured answers and twenty tests that are already written, and your job is to make them pass. Do not change the test file. Six of the ten answers carry a usable plan in six different wrappings. Four of them must not reach the rest of the program, and each of the four fails for a different reason.
Image: A terminal split between a failing test run on the left and a folder of ten answer files on the right.
