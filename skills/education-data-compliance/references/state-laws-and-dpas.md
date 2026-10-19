# State student-privacy laws & Data Privacy Agreements

*Federal law is the floor; **state laws are stricter and are what you sign contracts against.** 100+ state student-data-privacy laws exist.*

**Use this when:** scoping which states you serve, signing district contracts, or answering "what do we have to put in the agreement / how do we satisfy this district?"

## The model law and the patchwork
- **SOPIPA (California)** â€” *Student Online Personal Information Protection Act* â€” the template most states copied. Bans selling student data, targeted advertising to students, and non-educational profiling.
- **Other strict/cited regimes:** California **AB 1584** (vendor contract requirements), **New York Ed Law Â§ 2-d + Part 121** (strict; Parents' Bill of Rights; breach-notice teeth), **Illinois SOPPA**, **Colorado**, **Connecticut**. Each has its own contract clauses, breach-notification timelines, and parent-rights provisions.

## The operational reality: you sign DPAs district-by-district
- You won't negotiate 50 statutes â€” you'll sign **Data Privacy Agreements** with each district.
- The de facto national standard is the **SDPC National Data Privacy Agreement (NDPA)** from the **Student Data Privacy Consortium** (latest **v2.2, Nov 2025**), aligned with most state + federal law and backed by ~28 state alliances. The SDPC registry hosts **130,000+ signed DPAs**.

> **Engineering translation:** Treat **"sign the NDPA" as a product requirement.** Pre-fill the NDPA exhibits (data elements collected, sub-processors, retention/destruction). Maintain a public **trust/privacy page** + **sub-processor list** (every cloud/LLM vendor in the data path). Register signed DPAs in the SDPC registry where applicable.

## How to satisfy a specific district fast
1. Identify the **state** â†’ pull that state's student-privacy statute + breach-notification timeline.
2. Check whether the state/district uses the **SDPC NDPA** (most do) and grab their template + state addendum.
3. Fill the **data inventory** (exact elements collected) and **sub-processor list**.
4. Confirm your stance on the SOPIPA throughline: **no sale, no targeted ads, no non-educational profiling, no training on student data.**
5. Map your security controls + breach-response timeline to the state's requirement.

## Artifact to produce
For the target state(s): the applicable law(s), breach-notice timeline, the DPA template to use (usually SDPC NDPA + state addendum), and the filled data-inventory/sub-processor exhibits. Flag any clause the product can't currently satisfy.

## Sources
- SDPC National DPA: https://privacy.a4l.org/national-dpa/
- SDPC registry & state alliances: https://privacy.a4l.org/
- Future of Privacy Forum â€” student privacy: https://studentprivacycompass.org/
