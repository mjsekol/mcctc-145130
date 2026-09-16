# Protecting Data You Hold, and Saying Only What Is True
---
## Slide 1: Your report names five people
- Every other section is counts and totals
- Section four is five names and something unflattering
- The handbook says board reports carry no names
- So that section must not leave the room
Speaker notes: Here is section four of the report you are building. It names five members and says each of them has not returned something. Every other section on that page names nobody. Your own handbook says the board report carries counts and no names. So you have built something correct that must not be pasted into an email.
Image: A report page with one section highlighted in red and the rest in grey.
---
## Slide 2: The sentence to learn to distrust
- The data is encrypted
- So member records are protected
- And access control is handled
- Three claims, one true
Speaker notes: You will meet this sentence next week in a Gate 2, in a document that gets several other things right. Three claims in one sentence. The first is true. The second is much weaker than it sounds. The third has not been addressed at all, and it is the only one that affects section four.
Image: The sentence in quotation marks with three numbered annotations underneath.
---
## Slide 3: Three controls, three questions
- At rest: unreadable to somebody holding the disk
- In transit: unreadable to somebody on the network
- Access control: who may open it at all
- The file decrypts automatically for anybody signed in
Speaker notes: Encryption at rest protects a stolen laptop. It does nothing about the twelve people who can already open that shared folder, because for them the file decrypts automatically. That is what at rest means. And encryption is not access control. They are different controls answering different questions.
Image: Three locks, each guarding a different door, with only one of the doors on the path a signed-in user takes.
---
## Slide 4: CIA, and the trade inside it
- Confidentiality: only the right people can read it
- Integrity: it is correct and unchanged
- Availability: it is there when somebody needs it
- The strongest confidentiality control is deletion
Speaker notes: Everything in this module so far has been integrity: keys, constraints, transactions, quarantine, fidelity. Today is mostly confidentiality. And notice they trade: the very strongest confidentiality control is to delete the data, and that is also the worst possible thing for availability.
Image: A triangle with the three words at the corners and a tension line between two of them.
---
## Slide 5: Go and find grade_level in your report
- It is in your members table
- The report never uses it
- It was there because it was in the source file
- A field you never read is pure cost
Speaker notes: Look for it. It is not there. It is in your schema because it was in the file you were given, and that is the most common reason a field exists anywhere. It can be leaked, it can be wrong, it can be used later for something nobody agreed to, and it protects nothing.
Image: A schema with one column greyed out and a report with no corresponding column.
---
## Slide 6: Three questions for every column
- What question does this answer
- What is the worst thing somebody could do with it
- How long does it have to exist
- If you cannot name the question, remove the column
Speaker notes: Three questions, and they go in your data protection document. The makerspace's own privacy page says every field had to earn its place by answering a question the makerspace actually has to answer. That is minimisation, and it is cheaper than every control you would otherwise need.
Image: A column header with three question marks below it, and a delete arrow on the third.
---
## Slide 7: FERPA, at the level this course teaches
- These records are the shape of a student record
- The framework exists to say who may see it
- This course states no threshold and gives no advice
- The skill is knowing who to ask, with a list
Speaker notes: Your fixture is invented so you can practise this analysis without holding anybody's record. Understand what the framework is for. Do not state a threshold or a penalty, and do not tell anybody their system is compliant. A developer who says I do not know, here is my field list, and here is who has to look at it, is the useful one.
Image: A field list on a clipboard being handed to a person, rather than a stamp saying compliant.
---
## Slide 8: Verify means a command, not a tick
```
PRAGMA foreign_keys            ->  (1,)
rows read = loaded + quarantined
scan every source file for credentials
```
Speaker notes: The competency says verify compliance, not assume it. Verification is a check somebody else could repeat. A checklist somebody ticked is not verification. A command anybody can run is, and so is a test that fails when the claim stops being true.
Image: None. This slide is code.
---
## Slide 9: Here is security theatre
```python
encoded = base64.b64encode(open("makerspace.db", "rb").read())
print("Database encrypted.")
```
```
b'SQLite format 3\x00'
```
Speaker notes: The program says encrypted. The second line is what comes back out with one call and no key. Base sixty four is an encoding, not a cipher. It exists to move binary through text channels. The output is unreadable, so it looks protected, and the word encoded is one letter away from the word people mean.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- data-protection.md, half a page, in your project
- What this data would be if it were real
- Which fields you would not collect
- Who sees the section that names people, and who to ask
Speaker notes: Build two starts the data protection document for your project. Half a page. What this dataset would be if it were real, which fields you would not collect, who should see section four of your report, and what you would have to ask and of whom before this ran on real students. No legal thresholds and no advice.
Image: A half page document with four headings visible.
---
