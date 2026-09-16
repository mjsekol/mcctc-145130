# Additional Resources · Week 7
## 145130 Applications of AI · Module 3
### Topics: intellectual property, reading licenses, Creative Commons, and who owns AI output

**Every URL on this page is marked [VERIFY].** That is not hedging. This is the strand where being
confidently wrong does the most damage, government pages move, and a link that was live when this
was written may not be live when you assign it. **Click every one before class.**

**Nothing on this page is legal advice.** Every source below is named because it is the body that
publishes the material, not because anybody has vouched for what it says about your situation.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | U.S. Copyright Office, copyright basics and its material on AI | Mon, Thu | On-level | 40 min |
| 2 | The MIT license text, in your own fixture | Tue | Remediation | 2 min |
| 3 | Apache License 2.0, section 4, at the ASF's published text | Tue | On-level | 20 min |
| 4 | The GNU General Public License, at the FSF's published text | Tue | Extension | 30 min |
| 5 | Creative Commons licenses: deed and legal code | Wed | On-level | 30 min |
| 6 | The Open Source Definition, Open Source Initiative | Tue, Thu | On-level | 15 min |
| 7 | The SPDX license list | Tue | Extension | 10 min |
| 8 | choosealicense.com | Any | Remediation | 10 min |
| 9 | USPTO on trademarks and patents | Mon | On-level | 20 min |
| 10 | A free video on software licensing | Any | Remediation | under 20 min |
| 11 | SQ-19 The Bias Audit | Fri | Extension | two blocks |
| 12 | This module's lecture notes, self-check sections | Before the exit assessment | Review | 20 min |

---

## 1. The U.S. Copyright Office

`https://www.copyright.gov` **[VERIFY]**

**Why this one.** It is the source, and it publishes both the basics and its own registration
guidance on works containing AI-generated material. **Thursday's lesson turns on the Office's
stated position on human authorship**, and a student who has read the Office's words rather than a
summary of them is in a different position in that discussion.

**Assign a question, not the page:** *find where the Office says what it does with a work that
contains both human-authored and AI-generated material. What happens to each part?*

**Time.** 40 minutes. **Level.** On-level.

---

## 2. The MIT license text, in your own fixture

`05-labs/lab-m03-01-files/study-buddy/vendor/pocketgrid/LICENSE`

**Why this one.** 169 words, one condition, and it is on the student's own disk. **This is the
fastest remediation on the page** and it settles more arguments than anything else in this module.

**Assign a question:** *quote the one condition. Now say what it does not require.*

**Time.** 2 minutes. **Level.** Remediation.

---

## 3. Apache License 2.0

`https://www.apache.org/licenses/LICENSE-2.0` **[VERIFY]**

**Why this one.** Section 4 is a checklist, which is unusual and useful. It is the clearest example
in this module of an obligation you can literally tick off, and it is what the lanternparse row of
the audit depends on.

**Assign a question:** *section 4 lists things you must do when you redistribute. Write them out.
Then open `vendor/lanternparse/NOTICE` and say which one the Study Buddy README fails.*

**Time.** 20 minutes. **Level.** On-level.

---

## 4. The GNU General Public License

`https://www.gnu.org/licenses/` **[VERIFY]**

**Why this one.** It is the copyleft license the module's hardest finding turns on, and the Free
Software Foundation also publishes its own frequently-asked-questions material on what counts as a
combined work.

**Assign a question, and the framing matters:** *find what the license says about conveying. Then
find the FSF's position on linking. **Note that the FSF's position is one party's position**, and
write down what the answer appears to depend on rather than what the FSF concludes.*

**Time.** 30 minutes. **Level.** Extension. This is the reading for Lab M03-01 EXTENDED.

---

## 5. Creative Commons

`https://creativecommons.org/licenses/` **[VERIFY]**

**Why this one.** It is the best available lesson on the difference between a summary and a source,
because Creative Commons publishes both side by side and labels them. **Every license page has a
short deed and a link to the legal code.**

**Assign a question:** *open BY-NC 4.0. Find the definition of NonCommercial in the legal code, and
copy it out in the license's own words. Then say, in one sentence, what facts the Study Buddy
showcase question depends on.*

**Time.** 30 minutes. **Level.** On-level.

---

## 6. The Open Source Definition

`https://opensource.org/osd` **[VERIFY]** and `https://opensource.org/licenses` **[VERIFY]**

**Why this one.** Thursday's distinction between "open weights" and "open source" is only available
to a student who has read what "open source" means as a defined term. The Open Source Initiative
maintains the definition and the approved list, and has also published work on what an open source
AI definition should be. **[VERIFY]** whether that is still current before assigning it.

**Assign a question:** *read the definition, then read `study-buddy/model/LICENSE.txt` section 4.
Which clause of the definition does that section fail?*

**Time.** 15 minutes. **Level.** On-level.

---

## 7. The SPDX license list

`https://spdx.org/licenses/` **[VERIFY]**

**Why this one.** The identifiers in the manifest come from somewhere, and this is the somewhere.
It is also the fastest way to check whether an identifier a student wrote down is a real one.

**Assign a question:** *four of the ten Study Buddy components carry an SPDX tag. Look up all four.
Then say why the absence of a tag on pocketgrid is not a finding.*

**Time.** 10 minutes. **Level.** Extension.

---

## 8. choosealicense.com

`https://choosealicense.com` **[VERIFY]**

**Why this one, and the caveat matters more than the resource.** It is a well-made summary site and
**it is a summary site.** Assign it to a student who needs an orientation, and assign it with the
instruction that every claim on it has to be checked against the license text before it goes in a
manifest.

**Use it as a Gate 2 exercise instead:** open its MIT page, then open the MIT text, and list every
place the summary compresses a condition.

**Time.** 10 minutes. **Level.** Remediation, with the caveat attached.

---

## 9. The United States Patent and Trademark Office

`https://www.uspto.gov` **[VERIFY]**

**Why this one.** Monday's four-protections table has two rows most students have never thought
about. The USPTO publishes basics on both.

**Assign a question:** *what does a trademark protect, in the USPTO's own words? Now say why "Study
Buddy" printed on a poster is a trademark question and the code behind it is not.*

**Time.** 20 minutes. **Level.** On-level.

---

## 10. A free video

**[VERIFY]. No specific video is linked**, because a link to a video is the thing on this page most
likely to be dead, renamed, or replaced by something worse.

**What to look for:** a video under 20 minutes that explains permissive versus copyleft licensing
without telling you that the GPL forbids selling software. **Watch it yourself before assigning
it**, and if it makes that claim, that is a better Gate 2 artifact than a resource.

**Level.** Remediation.

---

## 11. Side quest

**SQ-19 The Bias Audit** unlocks with this module. Bundle:
`Courses/Misc/side-quests/SQ-19-The-Bias-Audit/`. ★★★, two blocks, and it runs entirely on locally
hosted models with no account and no key.

It is a natural BPA entry and it carries into Module 4.

---

## 12. The self-checks you already have

Every Module 3 lecture note ends with three self-check questions and worked answers, in
`03-lecture-notes/`. **Before the exit assessment, a student should be able to answer all 36
without reading the answers first.**

The four most worth the time from this week: What IP Protects question 3, Reading a License
question 2, Creative Commons question 2, and Who Owns AI Output question 1.

**Level.** Review.

---

## For the student who is behind

1. The MIT file, read once, out loud
2. Monday's worked examples 1 and 2, typed and run
3. Gate 1 Reps 01, 02, and 05
4. Before the exit assessment: the Reading a License notes and nothing else new

## For the student who is ahead

- Lab M03-01 EXTENDED, the sortwell compatibility memo, with resource 4
- The Open Source Definition against the model license, resource 6
- SQ-19
