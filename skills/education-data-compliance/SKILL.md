---
name: education-data-compliance
description: Apply US K-12 student-data and AI-in-education law when building, scoping, reviewing, or selling EdTech for schools, teachers, or principals. Use whenever a feature, product, contract, or data flow could touch student data or use AI on/about students, to answer "is this compliant?", "can we send student data to an LLM?", "do we need parental consent?", "what goes in the DPA?", "can the school consent for parents?", "can we train on this data?", or to review an EdTech feature for legal/privacy risk before shipping. Covers FERPA (education records, the "school official" exception, directory information, no-redisclosure), COPPA (under-13 online data, verifiable parental consent, the school-authorization mechanism, the 2025 amended Rule in force since April 22, 2026, no training/ads on kids' data), PPRA (student surveys + protected categories), IDEA + Section 504 (IEP/special-education records, the highest-sensitivity tier), state student-privacy laws (SOPIPA model, NY Ed Law 2-d, etc.) and the SDPC National Data Privacy Agreement (NDPA), accessibility (Section 504/ADA Title II/Section 508/WCAG 2.2 AA as a procurement gate), the AI overlay (US Dept of Ed developer guidance, civil-rights/bias exposure under Title VI/IX/504, human-in-the-loop, data minimization), and a pre-ship product compliance gate. Triggers: FERPA, COPPA, PPRA, IDEA, student data privacy, education records, school official exception, directory information, EdTech compliance, student data, K-12 data, parental consent, verifiable parental consent, school authorization, Data Privacy Agreement, DPA, SDPC, NDPA, SOPIPA, student online personal information, NY Ed Law 2-d, AI in education, AI in schools, can we train on student data, send student data to LLM, de-identify student data, classroom AI, teacher tool, principal tool, IEP, 504 plan, special education records, WCAG for schools, VPAT, accessibility compliance for education. NOT for: general (non-education) GDPR/CCPA work, HIPAA/healthcare (school health records are usually FERPA, not HIPAA; note the carve-out), or non-US jurisdictions (flag EU AI Act / GDPR as a separate module).
---

# education-data-compliance

US **K-12** student-data and AI-in-education compliance, distilled into a routing hub for builders. Route to **one** reference per task, read it fully, then produce its artifact (a decision, a checklist verdict, contract clauses, or a redesign). Verified against authoritative sources (FERPA/PTAC, FTC COPPA, US Dept of Ed) as of mid-2026; COPPA and ADA Title II dates re-checked 2026-10-08. Re-check time-sensitive items (ADA Title II interim rule status, federal AI EO status, NDPA version).

> **Not legal advice.** This guides engineering and product decisions. Anything touching identifiable student PII goes past counsel and a signed district Data Privacy Agreement before it ships.

## The mental model (read this first, every time)

1. **Whose data?** Staff-only or **de-identified/aggregated** student data â†’ light load. **Identifiable** student data â†’ the full regime. **Under-13** student data â†’ COPPA on top.
2. **The spine is FERPA.** EdTech vendors operate under the **"school official exception"**: we're a contractor doing the school's job, on its leash, using data only for the contracted purpose, with **no secondary use and no redisclosure**. Everything else layers on this.
3. **The governing rule for AI:** student PII may **not** be used to train models, build profiles, or for advertising without explicit written authorization. A third-party LLM call is a *disclosure* â€” it must be inside the contracted purpose, in the DPA, and flowed down to the LLM vendor (no-training / zero-retention terms).
4. **The cheat code:** legal load scales with student-PII exposure. **De-identify, aggregate, or keep it teacher-authored** and most rules relax. Ship the no-PII workflows first.

## Quick routing

| User cue / task | Reference |
|---|---|
| "Is this compliant?", general EdTech feature review, education records, the school-official exception, directory info, redisclosure, HIPAA-vs-FERPA for school health records | `references/ferpa-school-official-exception.md` |
| Under-13 students entering data, parental consent, verifiable parental consent, the school-authorization mechanism, the 2025 amended COPPA Rule (in force since April 22, 2026), no ads/profiling/training on kids' data, retention limits | `references/coppa-children-under-13.md` |
| Student surveys, SEL/wellness/climate screeners, protected categories, marketing use of student data | `references/ppra-surveys.md` |
| IEP / 504 / special-education records, the highest-sensitivity tier, hardened-build requirements, disability non-discrimination | `references/idea-special-education.md` |
| State laws (SOPIPA, NY 2-d, IL SOPPA, etc.), signing DPAs, the SDPC National Data Privacy Agreement (NDPA), breach-notification timelines, how to satisfy a specific district | `references/state-laws-and-dpas.md` |
| Using AI on/about students, US Dept of Ed developer guidance, bias/civil-rights (Title VI/IX/504), human-in-the-loop, de-identifying before LLM calls, transparency, federal AI EO posture | `references/ai-in-education.md` |
| Accessibility, WCAG 2.2 AA, Section 504/ADA Title II/Section 508, VPAT, procurement gate, deadlines | `references/accessibility-wcag.md` |
| "Can we ship this?", pre-launch sign-off, what to check before a pilot | `references/product-compliance-gate.md` |

## How to apply

1. Match the request to a routing row.
2. Read that reference in full.
3. Produce its artifact: a **compliance verdict + the specific gate(s) the feature must pass**, a **redesign** to a lower-PII shape if it can't pass, or the **contract clauses / consent flow** required.
4. If the task spans regimes (e.g., an under-13 AI tutor), read the relevant references and combine â€” COPPA + FERPA + the AI overlay commonly travel together.
5. Default to the **PII-minimizing** option. When in doubt, recommend de-identification/aggregation over building consent machinery.

## Common failure modes this skill prevents

- Treating school authorization as a blanket COPPA waiver (it covers *educational use only* â€” not ads, profiling, or AI training).
- Sending raw student work to an LLM that trains on inputs (a redisclosure + secondary-use violation).
- Assuming school health/counseling records are HIPAA (they're usually FERPA education records).
- Shipping an inaccessible product into a district (WCAG/VPAT is a procurement gate).
- Building IEP/504 or discipline-prediction features as an MVP (highest-sensitivity + civil-rights exposure â€” harden first, or don't).
- Forgetting the operational reality: you sign **DPAs district-by-district** (use the SDPC NDPA).
