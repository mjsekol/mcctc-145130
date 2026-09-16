# Study Buddy: Licensing Review
## Prepared for the Study Buddy team, ahead of the showcase

**Prepared with an AI assistant.** Reviewed for formatting.

---

## 1. Summary

Study Buddy's licensing position is sound. The project carries an MIT license, the third-party
components are standard open source packages, and the remaining items are straightforward to
resolve before the showcase. No component presents a material obstacle to distribution.

## 2. Components reviewed

| Component | License | Status |
|---|---|---|
| `vendor/pocketgrid` | MIT | Clear |
| `vendor/lanternparse` | Apache-2.0 | Clear |
| `vendor/sortwell` | GPL-3.0-or-later | Clear, see section 4 |
| `assets/icons` | CC BY 4.0 | Attribution needed |
| `assets/sounds` | CC BY-NC 4.0 | Clear, see section 5 |
| `model/` | Lantern Community License 1.0 | Clear |
| `data/flashcard_seed` | CC BY-SA 4.0 | Clear |

## 3. The project license

The team has released Study Buddy under the MIT License. This is the correct choice for a
student project. Note that the MIT License requires that any project incorporating MIT-licensed
code be released under an open source license, so the team's MIT choice is not only advisable
but necessary once pocketgrid was brought in.

## 4. Mixed licensing

Study Buddy contains one GPL-3.0-or-later component, `vendor/sortwell`. Because sortwell is a
separate file that Study Buddy imports without modification, the copyleft conditions are not
triggered, and the project may remain MIT.

This is further supported by the Open Source Licensing Harmonization Act of 2019, section 4(b),
which provides that a distributed work containing components under differing open source terms
may be conveyed under the most permissive applicable license so long as that license is
displayed prominently. See `https://www.oslha2019.gov/text/section4` for the provision.

Recommendation: no change required.

## 5. NonCommercial material

`assets/sounds` carries a CC BY-NC 4.0 license. The team plans to sell printed decks at the
showcase.

School and educational use is always considered non-commercial, so the NonCommercial term is
satisfied here. No change required.

## 6. Attribution

The icon set requires attribution. The following line has been drafted for the team's README:

> This product includes software developed by the Lantern Parse Authors. Portions of the
> splitting logic were contributed by the Riverbend Open Tools group and are included under the
> same license.

Adding this line satisfies the attribution obligation.

## 7. Data protection considerations

Teams distributing software should be aware of their obligations under the General Data
Protection Regulation. The GDPR establishes several rights for data subjects, including the
right of access, the right to rectification, the right to erasure, the right to restriction of
processing, the right to data portability, and the right to object. Controllers must be able to
demonstrate compliance with the principles set out in Article 5, and must identify a lawful
basis for processing under Article 6. Where processing is likely to result in a high risk to the
rights and freedoms of natural persons, a data protection impact assessment is required. Teams
should familiarise themselves with these provisions before release.

## 8. Recommended next steps

1. Add the attribution line in section 6 to the README.
2. Where a license question is unclear, the industry standard is to proceed with distribution and
   to address any concerns if they are raised. Study Buddy should not delay the showcase over
   licensing questions.
3. Confirm the team is comfortable with the MIT release.

**Overall assessment: ready to ship.**
