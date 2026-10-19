# COPPA â€” children under 13

*15 U.S.C. Â§ 6501â€“6506; 16 CFR Part 312. **FTC-enforced, real monetary penalties.** Major 2025 amendments.*

**Use this when:** any student **under 13** can enter personal info into an online service.

## Baseline
COPPA applies to operators of online services **directed to children under 13**, or with **actual knowledge** they collect personal info from under-13s. A teacher-facing tool that under-13 students log into is in scope. Baseline duty: **Verifiable Parental Consent (VPC)** before collection, plus notice, data minimization, security, and parental access/deletion.

## The school-authorization mechanism (critical for EdTech)
FTC guidance lets a **school consent on parents' behalf in lieu of VPC** â€” **only when the use is strictly educational and stays in the educational context.**
- The moment data is used for a **commercial purpose â€” including contextual advertising, profile-building, or training AI models â€” the school CANNOT consent.** You need real VPC.
- In the 2025 rulemaking the FTC **declined to codify** this exception (to avoid conflict with possible FERPA changes), so it lives in **guidance, not regulation.** Design conservatively.

## The 2025 amended Rule (first update since 2013)
- **Effective June 23, 2025; compliance required since April 22, 2026 (no extension).** The FTC has said it will enforce the amended Rule actively (verified 2026-10-08).
- **Age-verification carve-out (FTC policy statement, Feb 25, 2026):** limited enforcement when a child's data is collected only for age verification without prior consent, and only for operators compliant with the Rule in every other respect.
- **Expanded "personal information":** now includes **biometric identifiers** and **government-issued identifiers**.
- **Separate parental consent** required to **disclose** a child's data to **third parties** for targeted advertising / non-integral purposes.
- **Data-retention limits:** written retention policy; keep only as long as needed; **no indefinite retention.**
- **Written information-security program** required.
- New explicit **"mixed audience"** definition; new Safe-Harbor transparency duties.

> **Engineering translation (AI):** You may **not** use children's data to train models, build profiles, or for ads under school authorization. A feature that sends student work to an LLM is a **third-party disclosure** â€” keep it to the educational purpose, cover it in the DPA, and require the LLM vendor to contractually **not train** on it (enterprise / zero-retention tier). **De-identify before the model call** wherever possible.

## Artifact to produce
Determine: (1) Is under-13 data collected? (2) School-authorization (educational-use-only) or VPC? (3) Confirm zero commercial use / no AI training / no ads. (4) Retention policy + deletion in place? (5) Compliant with the amended Rule (in force since **April 22, 2026**)? Output the consent path + the retention/security gaps to close.

## Sources
- FTC COPPA rule: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
- 2025 Final Rule (Federal Register): https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule
- FTC press release (Jan 2025): https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data
- Compliance date in force, FTC enforcement posture (Davis Polk, Apr 2026): https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect
- Age-verification policy statement, Feb 25, 2026 (Hunton): https://www.hunton.com/privacy-and-cybersecurity-law-blog/tag/coppa
