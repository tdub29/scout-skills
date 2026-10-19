# The AI overlay â€” using AI on/about students

AI gets no single federal statute for schools â€” it **amplifies the existing laws** (student data flowing to models; automated decisions about kids) and adds a layer of **guidance + civil-rights scrutiny**.

**Use this when:** a feature uses an LLM/model on student data or to make/inform decisions about students.

## Federal guidance & posture (mid-2026)
- **US Dept. of Ed â€” "Designing for Education with AI: An Essential Guide for Developers"** (July 2024): the developer playbook. Five areas that double as a trust/compliance checklist: (1) design for teaching & learning; (2) provide evidence of impact; (3) advance equity & protect civil rights; (4) ensure safety & security; (5) promote transparency & earn trust.
- **US Dept. of Ed â€” "AI and the Future of Teaching and Learning"** (2023): emphasizes **humans in the loop**.
- **Shifting federal politics:** Biden's **EO 14110** (which tasked Ed with this work) was **rescinded Jan 2025**; the current administration issued **EO 14179** (pro-innovation) and **EO 14277, "Advancing AI Education for American Youth"** (Apr 2025, pushes K-12 AI literacy). Net: federal posture is **pro-adoption, lighter on mandates** â€” but the **2023/2024 guidance is still published** and the **privacy statutes (FERPA/COPPA/PPRA) are unchanged and fully in force.**
- **NIST AI Risk Management Framework** â€” voluntary; good scaffolding for documenting governance + bias testing.

## Civil-rights overlay (where AI bias becomes illegal)
Tools that affect students can trigger **Title VI** (race/national origin), **Title IX** (sex), **Section 504/ADA** (disability), and **FERPA**. A biased grader, risk-flagger, or discipline predictor can be a **civil-rights violation**, not just a quality bug.

## The AI rules that actually bind a product
1. **No training on student data** without explicit written district authorization (FERPA + COPPA + SOPIPA-style laws converge). Use LLM vendor tiers that contractually **don't train** on your data (enterprise / zero-retention).
2. **Third-party LLM calls = disclosures** â†’ must be within the contracted educational purpose, in the DPA, and flowed-down to the LLM sub-processor.
3. **Minimize & de-identify** â€” strip PII before the model call wherever the task allows; aggregate/anonymize for analytics.
4. **Human-in-the-loop** for consequential decisions (grades, discipline, placement, special ed). AI assists; humans decide. Document it.
5. **Transparency** â€” disclose AI use, what it does, limits, and how to contest/override.
6. **Bias & accessibility testing** as a release gate.
7. **Retention limits & deletion on request.**

## International note
**EU AI Act** classifies AI in education (admissions, scoring, proctoring) as **"high-risk"** â†’ heavy obligations; GDPR also attaches. **Out of scope for US K-12** â€” flag before any international expansion.

## Artifact to produce
For the AI feature: (a) the data-flow with the de-identification point marked; (b) confirmation the LLM vendor doesn't train on inputs + is in the DPA; (c) the human-in-the-loop + transparency design; (d) the bias-test plan if it evaluates/sorts students; (e) mapping to the Dept-of-Ed 5 areas.

## Sources
- "Designing for Education with AI" / Office of Ed Tech: https://tech.ed.gov/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- State AI guidance tracker (AI for Education): https://www.aiforeducation.io/ai-resources/state-ai-guidance
