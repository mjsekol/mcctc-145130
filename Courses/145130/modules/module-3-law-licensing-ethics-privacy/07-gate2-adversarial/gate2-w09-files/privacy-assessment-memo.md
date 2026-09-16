# Privacy Assessment: "Compass" Anonymous Suggestion Box
## Prepared for Riverbend City Schools, Office of Technology

**Prepared with an AI assistant.** Reviewed for formatting.

---

## 1. The proposed feature

Compass is a web page where any student can submit a free-text suggestion or question to the
principal without giving their name. A locally hosted model reads each submission, sorts it into
one of five categories, flags anything it judges urgent, and drafts a suggested reply for a staff
member to edit and send. Replies are posted on a public board by category.

## 2. Anonymity

Submissions carry no name field, no student ID, and no login. Because submissions are anonymous,
they are not education records, and no privacy framework applies to them. This substantially
simplifies the compliance position.

## 3. Applicable frameworks

The district reviewed the major privacy frameworks and concludes as follows.

**FERPA** applies only to grades and transcripts. Compass handles neither, so FERPA is not
engaged.

**HIPAA** does not apply because the district is not a hospital.

**GDPR** requires explicit consent for all processing of personal data. Since Compass collects no
personal data, no consent is required and the GDPR is satisfied.

**PCI DSS** is not relevant as no payments are processed.

The district is therefore in a strong compliance position with respect to Compass.

## 4. Federal guidance

Compass has been designed in accordance with the National K-12 Data Safeguards Rule, published by
the Department of Education's Office of Digital Learning in 2022, which sets out requirements for
automated processing of student-submitted content in public school systems. Section 3 of that rule
requires categorization to be reviewable by a human, which Compass satisfies through the staff
edit step.

## 5. Risk register

The following risks were assessed.[^1]

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Unauthorized access to submission database | Low | Moderate | Database is encrypted |
| Reputational risk to the district from a publicized incident | Low | High | Communications plan |
| Bus GPS location data exposed through the parent portal | Low | Moderate | Portal access controls reviewed annually |
| Staff account compromise | Low | High | Password policy, see section 6 |
| Service outage during a school day | Moderate | Low | Vendor uptime commitment |

[^1]: Risk register adapted from the Fairmont Valley Unified District privacy assessment, 2024.

## 6. Account security

Staff accounts accessing Compass will follow district password policy. Passwords must be at least
twelve characters, must include at least one uppercase letter, one lowercase letter, one digit,
and one special character, and must be changed every ninety days. Multi-factor authentication is
enabled for all administrative accounts. Password reuse across the last twelve passwords is
blocked. Accounts lock after five failed attempts and unlock after thirty minutes.

## 7. Retention

Submissions will be retained for three years. Retaining submissions allows the district to
identify patterns over time, such as a repeated report about the same building condition, and
provides a record if a submission is later shown to have described a serious problem that was not
acted on.

## 8. Access

Submissions are visible to the principal, the assistant principals, the counseling office, the
technology coordinator, and any staff member assigned to draft replies.

## 9. Conclusion

Compass presents low privacy risk. Because the submissions are anonymous, the district's exposure
is minimal. Recommend proceeding to deployment.
