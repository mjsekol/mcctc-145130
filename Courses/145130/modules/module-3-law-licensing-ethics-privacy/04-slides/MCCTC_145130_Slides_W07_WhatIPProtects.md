# What Intellectual Property Actually Protects
---
## Slide 1: Your poster goes up in front of strangers
- The competition deadline is next week
- Your project leaves the room
- Somebody asks: is all of this yours to use
- You have never been asked that before
Speaker notes: Next week your work goes somewhere a stranger can see it. And the question that has never mattered in twelve years of school suddenly matters. Not did it work. Not did anybody notice. Is every piece of this yours to use. Today you get the four systems that answer that question, and you find out that the project on your screen right now already fails it.
Image: A showcase table with a poster behind it, seen from a visitor's side.
---
## Slide 2: Four systems, not one
- Copyright protects expression, automatically, on fixation
- Trademark protects the badge on the product
- Patent protects an invention, only if granted
- Trade secret protects what you keep secret
Speaker notes: These are four separate systems. Different things, different starting moments, different lengths. Mixing them up is the most common error in this whole area, including in every AI-written summary you will read this week. Learn the four rows and you can catch most of those errors on sight.
Image: Four columns, navy headers, each with one icon and one starting moment.
---
## Slide 3: Copyright starts the moment you save
- No notice required. No registration required
- The commit you pushed this morning is protected
- So is the photo a stranger posted
- Registration is a separate step with separate benefits
Speaker notes: Protection is automatic on fixation. That is worth saying twice because it cuts both ways. Your work is protected without you doing anything, and so is everybody else's, including the person whose image came up in your search. There is no step where somebody had to claim it.
Image: A file being saved, with a copyright mark appearing at the moment of save.
---
## Slide 4: The line the whole system runs on
- Copyright covers expression, not the idea
- Not procedures, processes, systems, or methods
- Read the blog post, close the tab, write your own
- Copy and paste is a different act
Speaker notes: The statute says this directly. Copyright does not extend to any idea, procedure, process, system, or method of operation. So the idea of a flashcard app is not protected and the particular code somebody wrote for theirs is. That distinction is not a technicality, it is the thing that lets you learn from anybody.
Image: Two panels: a described algorithm on the left, a specific code file on the right.
---
## Slide 5: How most people look for licenses
```python
import os

for folder, subfolders, filenames in os.walk("study-buddy"):
    if "LICENSE" in filenames:
        print("licensed:", folder)

print("Scan complete. Everything above is licensed.")
```
Speaker notes: Here is how a project gets checked in practice. Walk the tree, look for a file called LICENSE, print what you find. I am going to run it on the Study Buddy project. Predict how many lines come out before I press enter.
Image: None. This slide is code.
---
## Slide 6: Three clean lines
```
licensed: study-buddy
licensed: study-buddy\vendor\lanternparse
licensed: study-buddy\vendor\pocketgrid
Scan complete. Everything above is licensed.
```
Speaker notes: Three components. No errors. A confident closing sentence. This is the output a team pastes into a competition submission when a judge asks about licensing. Everything on this screen is true and the conclusion a reader draws from it is false.
Image: None. This slide is code.
---
## Slide 7: The same project, looked at properly
```
vendor/pocketgrid                file: LICENSE
vendor/lanternparse              file: LICENSE
vendor/sortwell                  header in sortwell.py
snippets/shuffle_from_blog.py    NOTHING FOUND
assets/fonts                     NOTHING FOUND
assets/icons                     file: LICENSE.txt
assets/images                    NOTHING FOUND
assets/sounds                    file: LICENSE.txt
model                            file: LICENSE.txt
data/flashcard_seed              file: LICENSE.txt
```
Speaker notes: Ten components. Three with nothing at all. One whose license lives in a source header the first scan never opened. The difference between the two programs is not cleverness. The second one starts by naming what has to be accounted for, then goes looking. The first one looks, then reports what it happened to find.
Image: None. This slide is code.
---
## Slide 8: Public is not public domain
- Publicly available means you can see it
- Public domain means nobody holds a copyright
- A file you can download is not a file you can use
- Study Buddy's poster image is exactly this mistake
Speaker notes: These two phrases share a word and share nothing else. This is the single most expensive misunderstanding in the module and it is sitting in your fixture right now, in a file whose recorded source is found it in image search, looked good.
Image: A search results grid, with one image highlighted and no license anywhere on the page.
---
## Slide 9: Your app is not one work
- Code you wrote, code you copied, icons, font
- Sound, text, the name, the model, the dataset
- Different owners, different terms, one window
- Each can be fine and still not ship together
Speaker notes: An app is a stack of works owned by different people under terms that do not automatically agree with each other. This is what makes interactive media its own competency. Count the layers in your own project tonight and write the number down.
Image: An app window drawn as stacked transparent layers, each labelled with an owner.
---
## Slide 10: The pattern has repeated for a century
- Player pianos, photocopiers, cassettes, the web
- A copying technology arrives, rules get rewritten
- 1976 Act, Berne in 1989, the DMCA in 1998
- You are living inside the next turn
Speaker notes: The useful history is not a list of dates, it is one pattern. A copying technology arrives, does something the rules did not anticipate, courts and legislatures fight, the rules get rewritten, it becomes ordinary. Generative models are the current turn, and the rules are being written right now while you sit here. That is Thursday.
Image: A timeline wheel, each spoke a copying technology, the last one unlabelled.
---
## Slide 11: What you are about to build
- Run both scans against the Study Buddy tree
- Write down all ten components and what you found
- Three of them have nothing. Name them
- That list becomes your licensing audit
Speaker notes: Build one is both scans, with the output pasted into your notes. Build two starts the manifest that becomes your licensing audit, and the requirement that matters is that you list the components first and then go looking. Start from the tree, not from the files you happen to find.
Image: A ten-row table with three rows highlighted in accent red.
---
