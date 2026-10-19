# FERPA & the school-official exception

*20 U.S.C. Â§ 1232g; 34 CFR Part 99. Enforced by the US Dept. of Ed Student Privacy Policy Office (SPPO). Applies to schools/districts receiving federal funds â€” effectively all public K-12.*

**Use this to:** decide whether an EdTech feature can legally receive/use student records, and what the contract must say.

## What FERPA protects
"Education records" â€” records directly related to a student, maintained by the school or a party acting for it: grades, transcripts, discipline, attendance, IEPs, contact info, student work, behavioral notes, biometrics â€” anything personally identifiable (PII).

## The rights (and who holds them)
Parents hold the rights until the student turns 18 or enters postsecondary, then they transfer to the **eligible student**:
- Inspect & review records
- Request correction
- Consent before PII is disclosed â€” **subject to exceptions**

## The "school official" exception â€” how EdTech operates
A school may share student PII with a vendor **without parental consent** if the vendor is a "school official with a legitimate educational interest." **All four prongs required** (34 CFR Â§ 99.31(a)(1)):
1. Performs an **institutional service/function** the school would otherwise do itself.
2. Has a **legitimate educational interest** in the records.
3. Is under the **direct control** of the school re: use and maintenance of the records.
4. Uses records **only for the authorized purpose** and **does not redisclose** PII without consent.

> **Engineering translation:** We're a contractor on the school's leash. Use student data **only** for the contracted task. **No selling, no ads, no profiling, no training models on it.** Delete on request. The DPA must say all of this. Sub-processors (cloud, LLM vendors) must be flowed-down the same obligations.

## Directory information
Schools *may* designate some fields (name, grade, photo) as shareable "directory information" after annual notice + opt-out. **Don't design products that rely on this** â€” treat all student data as protected.

## Health-records carve-out (commonly wrong)
K-12 **school** health/counseling/nurse records are generally **FERPA education records, NOT HIPAA**. Don't apply HIPAA frameworks to in-school health data. (HIPAA can attach to certain *external* providers â€” flag for counsel.)

## Enforcement reality
No private right of action. Ultimate federal penalty is funding withdrawal for a *policy or practice* of violations. The *practical* risk is bigger: **lost district contracts, reputational damage, and state-law liability** (state laws have real teeth â€” see `state-laws-and-dpas.md`).

## Artifact to produce
A verdict: **does the feature fit the four prongs?** If yes, list the DPA clauses needed (purpose limitation, direct control, no secondary use, no redisclosure, deletion, sub-processor flow-down). If no, redesign to a lower-PII shape (de-identify, aggregate, keep teacher-authored) or build a consent path. Cross-check `product-compliance-gate.md`.

## Sources
- studentprivacy.ed.gov â€” EdTech vendors hub: https://studentprivacy.ed.gov/audience/education-technology-vendors
- PTAC Written Agreement Checklist: https://studentprivacy.ed.gov/sites/default/files/resource_document/file/Written_Agreement_Checklist.pdf
- Vendor FAQ (third-party responsibilities): https://studentprivacy.ed.gov/sites/default/files/resource_document/file/Vendor%20FAQ.pdf
