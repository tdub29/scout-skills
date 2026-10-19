---
name: resume-quantifier
description: "Adds numbers to bullets, estimating when exact data is missing"
---

# Resume Quantifier

## When to Use This Skill

Use this skill when the user:
- Needs to add metrics and numbers to their resume
- Has bullets without quantifiable results
- Doesn't know what numbers to include
- Says they "don't have metrics" or "can't measure impact"
- Mentions: "add metrics", "quantify", "add numbers", "measure impact", "no data"

## Core Capabilities

- Find hidden metrics in any experience
- Estimate numbers when exact data unavailable
- Create before/after comparisons
- Identify measurable impact points
- Transform vague statements into quantified achievements
- Guide users to discover their metrics

## Why Quantification Matters

**The Problem:**
- "Managed projects" vs "Managed 12 projects worth $2M"
- "Improved processes" vs "Reduced cycle time by 40%"
- "Helped customers" vs "Resolved 50+ tickets daily with 98% satisfaction"

**Studies Show:**
- Resumes with numbers get 30% more attention
- Quantified bullets are 40% more memorable
- Numbers provide credibility and scale

## The Quantification Framework

### Categories of Metrics

**1. Money**
- Revenue generated
- Costs reduced/saved
- Budget managed
- Deal sizes closed
- Profit margins improved

**2. Time**
- Hours saved
- Cycle time reduced
- Project duration
- Response times
- Time to market

**3. Percentages**
- Growth rates
- Improvement percentages
- Efficiency gains
- Error reduction
- Conversion rates

**4. Volume/Scale**
- Number of customers/users
- Projects managed
- Team size
- Transactions processed
- Items produced

**5. Quality**
- Satisfaction scores
- Error rates
- Accuracy rates
- Compliance rates
- SLA adherence

**6. Frequency**
- Per day/week/month
- Annual totals
- Meeting cadences
- Report cycles

Moved to `references/finding-hidden-metrics.md`: discovery questions and role-specific metric prompts.

Moved to `references/estimation-techniques.md`: conservative, range, minimum-bound and time-based estimates.

Moved to `references/templates-and-no-numbers-situations.md`: quantification templates and the five common no-numbers situations.

## Output Format

When quantifying a resume:

```markdown
# RESUME QUANTIFICATION

## Analysis Summary
**Bullets without numbers:** X
**Bullets with numbers:** Y
**Target:** 100% of bullets should have at least one metric

## Quantified Bullets

### Original Bullet #1:
"Managed customer accounts"

### Questions to Find Metrics:
- How many accounts? â†’ [User answer: ~40]
- What was the revenue? â†’ [User answer: ~$2M]
- What results did you achieve? â†’ [User answer: retained most]

### Quantified Version:
"Managed portfolio of 40 enterprise accounts representing $2M ARR, achieving 95% retention rate"

### Metrics Added:
- Account count: 40
- Revenue: $2M ARR
- Retention: 95%

---

### Original Bullet #2:
[Continue for each bullet]

## Estimation Notes
- [Metric]: Estimated based on [reasoning]
- [Metric]: Conservative estimate using [method]

## Remaining Questions
- [Questions to ask user for missing information]
```

## Quantification Quality Checklist

For each bullet:
- âœ… Has at least ONE number
- âœ… Number is relevant (not just any number)
- âœ… Scale is clear (what does the number mean?)
- âœ… Estimation is conservative and defensible
- âœ… Number adds credibility, not confusion
- âœ… You can explain the number in an interview

## Numbers to Avoid

- âŒ Numbers that make you look bad
- âŒ Numbers you can't explain or defend
- âŒ Numbers that reveal confidential information
- âŒ Exaggerated or inflated numbers
- âŒ Numbers without context (e.g., "increased by 300%" without baseline)
- âŒ Too many numbers in one bullet (2-3 max)

## Key Principle

**Every bullet can be quantified.** If you think your work can't be measured, you haven't asked the right questions yet.

The goal isn't to have impressive numbersâ€”it's to have SPECIFIC numbers that show the scope and impact of your work.

## References

- `references/finding-hidden-metrics.md`: load when the user says they have no metrics, to ask discovery questions
- `references/estimation-techniques.md`: load when a number must be estimated
- `references/templates-and-no-numbers-situations.md`: load when phrasing the quantified bullet or handling a no-numbers objection
