# Product compliance gate (pre-ship sign-off)

Run this on every feature before a pilot. If a box can't be checked, **redesign to remove the student PII** (de-identify, aggregate, keep teacher-authored) rather than bolting on consent machinery. Lower PII = faster to ship + easier to sell.

## Step 0 â€” Classify
- [ ] **Whose data?** Staff-only Â· De-identified/aggregated student Â· Identifiable student PII Â· **Under-13** student PII
- [ ] **Sensitivity:** None (no student PII) Â· Standard Â· **High** (IEP/504, health, behavior, discipline, SEL/protected-category)
- [ ] **Does any student data leave our system** (LLM API, analytics, email, cloud)? List every destination.

> Staff-only or no-student-PII â†’ light load; document and proceed. Otherwise continue. (See `ferpa-school-official-exception.md`.)

## Step 1 â€” FERPA
- [ ] Data used **only** for the contracted educational purpose
- [ ] **No** selling / ads / profiling / model-training on student data
- [ ] **No redisclosure**; sub-processors flowed-down in contract
- [ ] Deletion/export on district request implemented
- [ ] Access & correction path exists

## Step 2 â€” COPPA (if under-13 data)  â†’ `coppa-children-under-13.md`
- [ ] School authorization (educational use only) **or** verifiable parental consent
- [ ] Zero commercial use of children's data (no ads, profiles, **AI training**)
- [ ] Written retention policy; no indefinite retention
- [ ] Written security program
- [ ] Compliant with 2025 amended Rule (**in force since April 22, 2026**)

## Step 3 â€” Surveys / sensitive (PPRA, IDEA, health)  â†’ `ppra-surveys.md`, `idea-special-education.md`
- [ ] No PPRA protected-category collection without consent/opt-out
- [ ] Survey data never used for marketing
- [ ] IEP/504/health data â†’ hardened controls (don't ship as MVP)

## Step 4 â€” AI specifics  â†’ `ai-in-education.md`
- [ ] Student PII de-identified/aggregated before the model call where possible
- [ ] LLM vendor contractually does **not** train on our data (zero-retention/enterprise)
- [ ] LLM vendor on the sub-processor list + in the DPA
- [ ] Human-in-the-loop for consequential decisions
- [ ] Transparency: users told AI is involved, limits, override path
- [ ] Bias check for anything that evaluates/sorts students

## Step 5 â€” Accessibility  â†’ `accessibility-wcag.md`
- [ ] Meets WCAG 2.2 AA
- [ ] VPAT / conformance statement available

## Step 6 â€” Contracts & trust  â†’ `state-laws-and-dpas.md`
- [ ] Can sign the SDPC NDPA (v2.2)
- [ ] Public privacy/trust page + sub-processor list
- [ ] Breach-response plan with state-law timelines
- [ ] Counsel review if identifiable student PII is involved

---
**Verdict format:** PASS / REDESIGN / BLOCK, plus the specific unchecked boxes and the cheapest path to green (usually: remove the PII).
