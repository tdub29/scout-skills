# IDEA & special education â€” the highest-sensitivity tier

*Individuals with Disabilities Education Act, 20 U.S.C. Â§ 1400 et seq.; confidentiality at 34 CFR Â§Â§ 300.610â€“300.627. Section 504 of the Rehabilitation Act; ADA.*

**Use this when:** a feature touches **IEPs, 504 plans, special-education evaluations, or disability data** â€” the most sensitive student data that exists.

## What's added on top of FERPA
IDEA's confidentiality provisions reinforce FERPA and add:
- **Parental consent** for disclosure of personally identifiable special-ed info.
- **Access rights** (parents may inspect/review records; the agency must respond).
- **Records destruction:** info must be destroyed at the parent's request when no longer needed; parents must be **notified before destruction**.
- Designation of an official responsible for confidentiality + staff training.

## Non-discrimination overlay
Section 504 and ADA prohibit disability discrimination. An automated tool that disadvantages students with disabilities (a biased grader, a placement/risk predictor, an inaccessible interface) isn't just a privacy issue â€” it's a **civil-rights** issue (Section 504 / ADA Title II).

> **Engineering translation:** IEP/504 tooling is high-value but **maximum sensitivity**. This is a **Phase-3 hardened build, not an MVP.** Requirements: granular role-based access control, full audit logging, encryption in transit + at rest, careful data residency, strict minimal retention with destruction workflows, **human-in-the-loop for every consequential output**, and counsel review. AI assistance must be transparent and overridable; never let a model make an unreviewed decision about a student with a disability.

## Artifact to produce
If the feature touches special-ed data: confirm it's deferred to a hardened phase (or stop). List the required controls (RBAC, audit log, encryption, retention/destruction, human-in-loop, counsel). For any AI element, document the bias-testing + human-override plan and the Section 504/ADA exposure.

## Sources
- IDEA: https://sites.ed.gov/idea/
- FERPA/PTAC: https://studentprivacy.ed.gov/
- OCR Section 504 guidance: https://www.ed.gov/about/ed-offices/ocr
