# The Prompt Is the Whole Input
---
## Slide 1: You asked about your school and it answered about a school
- Six words in about equipment checkout
- A hundred and ten words back
- It names a sheet, a serial number, a repair shelf
- You never mentioned any of those
Speaker notes: You have been typing into chat boxes for years, and that taught you one habit, which is to keep rephrasing until something looks right. The habit works well enough that you have never had to know what is happening underneath. This week you get asked to explain why one version worked, so before anything else you need to know what the machine on the other end can see. Watch what comes back from six words.
Image: A six-word prompt on the left, a dense block of reply text on the right, deep navy and accent blue, with four specific nouns in the reply circled.
---
## Slide 2: Six words in, a hundred and ten out
```
python ask.py --prompt "How do you do equipment checkout?" --label demo1 --show

[demo1] 6 prompt words to http://127.0.0.1:11434
  110 reply words in 0.02s, recorded in runs\demo1.json

Open the checkout sheet before anyone lines up. Match the serial number on the
case to the number on the sheet. Write the borrower's grade level, not their
schedule. Photograph any damage before the item leaves the room.
```
Speaker notes: Read that first paragraph again. It named a checkout sheet, a serial number, a return slot and a repair shelf. Now tell me which of those is true about Room 214. Nobody in here knows, and that is the point. Nothing in the prompt mentioned a sheet or a shelf. Those are things checkout procedures usually have, which is a completely different claim from things your checkout has.
Image: None. This slide is the recorded run.
---
## Slide 3: What the machine can actually see
- It sees one thing: the text you sent
- It has never seen Room 214 or your club
- It does not look anything up
- It fills gaps with what is typical
- Nothing in the process checks whether the output is true
Speaker notes: Four things follow from that, and they explain most of what you will see for the next three weeks. It knows nothing about you. It has no search step unless somebody built one. It fills gaps with whatever is most common across everything it was trained on. And producing a true sentence and producing a false one are the same operation. Here is the sentence to carry all module. It is not lying to you, because lying requires knowing.
Image: A single box labelled context with one arrow going in labelled your text, and three crossed-out arrows labelled memory, search, and your files.
---
## Slide 4: The part of the reply that says nothing
```
It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule. Ultimately, the right approach
depends on your specific needs and goals. Studies have shown that small changes
can produce meaningful improvements.
```
Speaker notes: Four sentences, zero content. Read them and try to write down one thing you would do differently because of them. You cannot. Ask yourself why that paragraph is there at all. It is there because nothing in the prompt said what finished looks like, so the model kept producing plausible continuation until it ran out of plausible continuation. Padding is a symptom of a missing finish line, and you fix it tomorrow.
Image: None. This slide is the recorded run.
---
## Slide 5: Now put the facts it cannot know into the box
```
python ask.py --prompt "The Media Club checkout sheet is taped inside the door of Room 214, and the cameras live in the cabinet under the window. How do you run checkout?" --label demo2 --show

[demo2] 28 prompt words to http://127.0.0.1:11434
  59 reply words in 0.02s, recorded in runs\demo2.json
```
Speaker notes: Same question, with two facts added that the model could not have. Watch the numbers on the second line. The prompt went from six words to twenty-eight, and the reply went from a hundred and ten words down to fifty-nine. Before I show you the text, predict which parts of the original reply survived and which parts disappeared.
Image: None. This slide is the recorded run.
---
## Slide 6: Context narrowed the target
- A hundred and ten words became fifty-nine
- The material about return slots and repair shelves is gone
- Context did not add knowledge to the model
- It moved the reply towards what you supplied
- A real model will also quote your room back at you
Speaker notes: This is the sentence I want from you on the exit ticket. Context did not add knowledge. It narrowed the target. Everything left in that reply connects to the sheet, the case and the room you mentioned, and the generic filler is gone. Against our stub the narrowing is all you see. Against the lab's local model it will usually go further and hand your own door and cabinet back to you, and that difference is on the confirmation list.
Image: A dartboard with a wide scattered grouping labelled six words beside a tight grouping labelled twenty-eight words.
---
## Slide 7: Ask it something it could not possibly have
```
python ask.py --prompt "What time does the late bus leave from the Advanced Technology Wing on Thursday?" --label demo3 --show

[demo3] 14 prompt words to http://127.0.0.1:11434
  93 reply words in 0.02s, recorded in runs\demo3.json

Start by writing down what finished looks like. Write down what you decided and
why. Name the one thing that would make this fail.
```
Speaker notes: There is no version of this system that could know that time. It has no timetable, no network call, and no way of noticing that it has nothing to work from. So watch what it does instead of stopping. Ninety-three confident words, about a real wing of a real building, containing no information about any bus.
Image: None. This slide is the recorded run.
---
## Slide 8: Read what did not happen
- No error, no refusal, no question back to you
- Ninety-three confident words about a bus
- Zero information about any bus
- A real model often invents a specific time instead
Speaker notes: Notice what is absent. There is no error. There is no sentence saying I have no way to know that. There is no question asking you which bus. On a real local model this usually goes one step worse than our stub and produces a specific time, because a specific time is the shape of an answer to a question like that. That version is the one that catches careful people. Confident, specific, about a real place, and wrong.
Image: A terminal window with a clean reply and a large empty space beside it labelled where the error would be.
---
## Slide 9: The wrong way, and the thing it does not print
```
python ask.py --prompt "Use the checkout file I showed you earlier." --label wrong --show

[wrong] 8 prompt words to http://127.0.0.1:11434
  110 reply words in 0.03s, recorded in runs\wrong.json

Open the checkout sheet before anyone lines up. Match the serial number on the
case to the number on the sheet. Write the borrower's grade level, not their
schedule.
```
Speaker notes: There is no earlier. There is no file. Every call starts with a context that holds only what you sent this time. Look at what you did not get. You did not get an error saying there is no previous conversation. You got a hundred and ten words about a file that was never sent, and it is the same reply the six-word prompt produced, because both prompts carried the same amount of information about your file, which is none.
Image: None. This slide is the recorded run.
---
## Slide 10: The failure has no error message
- Both prompts carried the same amount about your file: none
- Chat interfaces resend your history, so earlier works there
- Call the model from a program and the resending is gone
- The belief that it remembers stays behind
- The dangerous outputs are the ones that look finished
Speaker notes: Here is why almost everyone makes this mistake in their first week. A chat interface quietly resends the earlier messages for you, so the word earlier does work there. That builds a belief that the model remembers. The moment you call it from your own program the interface is gone, the resending is gone, and the belief is still sitting there. Say the last line with me, because you will meet it eleven more times this module. The dangerous outputs are the ones that look finished.
Image: Two panels. A chat window with the history highlighted and resent, beside a program making one call with an empty box.
---
## Slide 11: What you are about to build
- Entry check first, fifteen minutes, not graded
- Then the toolkit: start the stub, run one prompt
- Cause two failures on purpose and read the exit codes
- Then Lab M02-01 steps one through five
- Five prompt files committed before any run
Speaker notes: Build one is the entry check and then the toolkit README worked all the way through. Acceptance is that test_toolkit dot py prints Ran twenty-nine tests and OK, you have one recorded run in your own runs folder, and you have caused at least two different failure modes on purpose and can tell me the exit code each one gave. Build two is the lab, steps one through five, and the requirement that matters is committing the prompt files before you run them. One hard rule, and it is not negotiable. Your prompt gets recorded verbatim into a file you commit, so no name, no ID, no grade and no schedule goes into a prompt. Invented people only.
Image: A repository tree showing a prompts folder and a runs folder side by side, with a commit marker between them.
---
