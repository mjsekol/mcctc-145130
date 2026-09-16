# Data Minimization, and the Assessment You Write Before You Build
---
## Slide 1: One control cannot be misconfigured
- Encryption, access control, logging, audits, retention
- All real, all necessary, all able to fail
- Each one needs somebody doing it right forever
- Except the one where you never held the field
Speaker notes: A field you never collected cannot leak, cannot be subpoenaed, cannot be sold in a breach, cannot end up in a prompt, and needs no retention rule. That asymmetry is why this lesson comes before the assessment instead of after it.
Image: A row of locks beside one empty shelf.
---
## Slide 2: Three ideas, one checklist
- Purpose limitation: write the purpose down first
- Data minimisation: adequate, relevant, limited
- Storage limitation: deletion is a feature you build
- Every field on a form was somebody's decision
Speaker notes: These are the clearest published statement of the idea, from the GDPR's Article five, which is why this course uses them as a design checklist even though the GDPR does not govern your school. Most forms have fields on them because somebody thought they might be interesting one day.
Image: Three principles as three gates a field has to pass.
---
## Slide 3: Minimization as a data structure
```python
PURPOSES = {
    "attendance_letter": ["student_id", "first_name", "last_name",
                          "guardian_name", "guardian_email",
                          "absences_this_term"],
    "bus_route_count": ["bus_route"],
    "ai_hint_request": [],
}
```
Speaker notes: A policy that says we minimize data is a sentence. This is the same idea as a program. The list is per purpose, not per program, which is purpose limitation expressed as a data structure. And the empty list is the course rule as code.
Image: None. This slide is code.
---
## Slide 4: Sixteen fields in, one field out
```
Fields the roster carries: 16
 attendance_letter: 6 field(s)
   bus_route_count: 1 field(s)
   ai_hint_request: 0 field(s)

Riders per route, from records holding one field each: {'12': 3, '7': 2}
```
Speaker notes: The count is still correct. That is the argument for minimization in one line of output: the job got done with one field, and every other field would have been a field at risk for no benefit. The route count is the purpose that looks too small to be right.
Image: None. This slide is code.
---
## Slide 5: Fail closed, not open
- An unknown purpose raises instead of returning everything
- Returning everything would be shorter
- And every future typo would get the whole record
- Loud on the first run beats quiet forever
Speaker notes: This is the security decision in the lab and the self-check tests for it. A permissive default at the data layer is the most durable design mistake in this whole module, because the next team inherits it and builds everything on top of it.
Image: Two doors, one refusing, one wide open with everything behind it.
---
## Slide 6: The names are gone. Is anybody anonymous
```
grade                                 0 of 5 alone in their group
grade + bus_route                     0 of 5 alone in their group
grade + bus_route + meal_status       5 of 5 alone in their group
grade + bus_route + meal + services    5 of 5 alone in their group
```
Speaker notes: Watch the third line. Grade and route together identify nobody. Add one more ordinary field and every single record is unique. No name, no ID, no address, no birthday anywhere in those groupings.
Image: None. This slide is code.
---
## Slide 7: Quasi-identifiers
- Fields that identify nobody alone
- And somebody in combination
- Anybody who knows a few facts can find the row
- And that row holds the services plan
Speaker notes: At a school, everybody knows a few facts about everybody. We removed the names is not an answer and it is not evidence. If somebody claims data is anonymous, that claim has to be measured, every time, and the burden is on whoever made it.
Image: Three plain field tiles combining into one identified person.
---
## Slide 8: The two sections that carry the document
- Section 6: what this feature refuses to collect
- Section 11: the recommendation and every UNKNOWN
- Anybody can list the fields they collected
- Listing what you rejected proves a decision happened
Speaker notes: Section six reads as empty work because a refusal leaves nothing behind. Write it down, or in six months somebody adds the field back and nobody remembers why it was out. And section eleven has to make a call, in one of three exact wordings.
Image: An eleven-section outline with two sections highlighted.
---
## Slide 9: Where retention plans actually fail
- Draft files on a workstation
- Application logs, and the model server's own log
- Cached responses and one-off exports
- Backups, which exist to outlive deletion
Speaker notes: Ask a team where the data lives and they say the database. None of these are in the database that the retention policy was written about. Derived material is the answer to how did this still exist two years later.
Image: A database icon surrounded by five files nobody listed.
---
## Slide 10: The design note that works and is wrong
- Pull the full record, we already have access
- Pass it to the model with the template
- In case we want personalization later
- Strip names before logging
Speaker notes: Nothing errors and this design would pass a demo. Four problems. The whole record is in the prompt. In case we want it later is the purpose limitation failure word for word. Stripping names is the anonymization failure you disproved two slides ago. And the data layer decision will outlive everybody in the room.
Image: A short design note with four separate underlines.
---
## Slide 11: What you are about to build
- Fill the field list for three purposes
- Make the unknown purpose refuse
- Rewrite the log line and salt the reference
- Write section 6 of your assessment: what you refused
Speaker notes: Build one is the lab, ten checks. Build two is section six of your own assessment, which is the section that separates a real assessment from a filled-in form. Every field you considered and rejected, with a reason each. Nobody will see the counselor note you did not send. Write it down anyway.
Image: A refused-fields table with seven rows and a reason on each.
---
