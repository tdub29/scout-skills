# Accessibility â€” Section 504, ADA Title II, Section 508, WCAG

Not "data" law, but a **hard procurement gate** for anything used in public schools.

**Use this when:** building any UI a student, parent, or staff member will use, or answering a district's accessibility/VPAT request.

## The obligations
- **Section 504 (Rehabilitation Act) & ADA Title II** require public schools' programs â€” including the digital tools they adopt â€” to be **accessible to people with disabilities**.
- **2024 DOJ ADA Title II web rule** sets a concrete bar: state/local government entities (incl. public school districts) must conform web content & mobile apps to **WCAG 2.1 Level AA**, due **April 26, 2027** (entities serving 50,000+ people) and **April 26, 2028** (smaller entities and special districts). A DOJ interim final rule of April 20, 2026 moved both dates back one year; the WCAG 2.1 AA standard did not change. Re-check for a final rule (verified 2026-10-08).
- **Section 508** governs federal procurement and is the de facto baseline many districts cite.

> **Engineering translation:** Build to **WCAG 2.2 AA** from day one â€” keyboard navigation, sufficient contrast, alt text, semantic markup, captions, focus management, ARIA where needed. Keep a **VPAT / Accessibility Conformance Report** ready; districts increasingly require it before purchase. Use the `accessibility-compliance` and `impeccable` / `frontend-design` skills when building.

## Artifact to produce
An accessibility gate result: does the UI meet WCAG 2.2 AA? List the specific gaps (contrast, keyboard traps, missing labels, uncaptioned media) and whether a VPAT exists. Treat unmet AA as a launch blocker for school sales.

## Sources
- DOJ ADA Title II web rule (2024): https://www.ada.gov/resources/2024-03-08-web-rule/
- DOJ interim final rule extending the compliance dates (Apr 20, 2026): https://public-inspection.federalregister.gov/2026-07663.pdf
- Plain-language summary of the new dates (University of Arizona): https://accessibility.arizona.edu/news/doj-issues-interim-final-rule-title-ii-digital-accessibility-compliance-dates
- WCAG (W3C): https://www.w3.org/WAI/standards-guidelines/wcag/
- Section 508: https://www.section508.gov/
