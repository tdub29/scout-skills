# PPRA â€” surveys & protected categories

*Protection of Pupil Rights Amendment, 20 U.S.C. Â§ 1232h.*

**Use this when:** a product surveys students (SEL check-ins, climate/wellness/needs surveys, screeners) or collects student info for marketing.

## The rule
Requires **parental opt-in consent** before a student takes a US-DoE-funded survey revealing any of **8 protected categories**:
1. Political affiliations/beliefs
2. Mental/psychological problems
3. Sex behavior or attitudes
4. Illegal, antisocial, self-incriminating behavior
5. Critical appraisals of family members
6. Legally privileged relationships (lawyers, physicians, clergy)
7. Religious practices/affiliations/beliefs
8. Income (other than for program eligibility)

Also gives parents **opt-out** rights for other surveys and for the collection/use/disclosure of student info for **marketing** purposes.

> **Engineering translation:** If a feature surveys students, the protected categories trigger consent flows â€” build them or avoid collecting those categories. **Never** use survey responses for marketing. SEL/mental-wellness tools are especially exposed (category 2) and are high-sensitivity overall.

## Artifact to produce
Classify the survey content against the 8 categories. If any are hit â†’ require an opt-in consent flow (or redesign to avoid them). Confirm no marketing use of any student-collected data. Flag SEL/mental-health features for the high-sensitivity path (`idea-special-education.md` patterns + counsel).

## Sources
- studentprivacy.ed.gov (PPRA overview): https://studentprivacy.ed.gov/
- 20 U.S.C. Â§ 1232h
