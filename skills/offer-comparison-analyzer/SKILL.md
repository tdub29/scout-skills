---
name: offer-comparison-analyzer
description: "Compare job offers on total comp"
---

# Offer Comparison Analyzer

## When to Use This Skill

Use this skill when the user:
- Has multiple job offers to compare
- Needs to evaluate total compensation
- Wants to make a data-driven job decision
- Is weighing different opportunities
- Mentions: "compare offers", "multiple offers", "which job", "offer comparison", "deciding between jobs"

## Core Capabilities

- Compare total compensation across offers
- Evaluate non-monetary factors
- Create weighted decision frameworks
- Calculate true offer value
- Identify hidden costs and benefits
- Guide the decision-making process

## The Comparison Challenge

**The Problem:** 
Comparing offers is hard because:
- Different compensation structures
- Non-monetary factors matter
- Hidden benefits and costs
- Emotional factors cloud judgment
- Information asymmetry

**The Solution:**
Systematic comparison framework that considers:
- Total compensation (not just salary)
- Career growth potential
- Work-life factors
- Risk assessment
- Personal values alignment

## Total Compensation Calculator

### Components to Include

**Cash Compensation:**
- Base salary
- Signing bonus (one-time)
- Annual bonus (target %)
- Commission (for sales roles)
- Relocation assistance

**Equity Compensation:**
- Stock options (value = current price - strike price)
- RSUs (value = current price Ã— shares)
- Vesting schedule
- Refresh grant expectations

**Benefits Value:**
- Health insurance (employer contribution)
- 401(k) match
- HSA/FSA contributions
- Life/disability insurance
- Other insurance benefits

**Perks Value:**
- Vacation days (can assign $ value)
- Remote work (saves commute costs)
- Professional development budget
- Equipment/office stipend
- Meals, gym, etc.

## Output Format

When comparing offers:

```markdown
# JOB OFFER COMPARISON

## Offers Being Compared
- **Offer A:** [Role] at [Company]
- **Offer B:** [Role] at [Company]

## Total Compensation Comparison

| Component | Offer A | Offer B | Difference |
|-----------|---------|---------|------------|
| Base | $X | $X | |
| Bonus | $X | $X | |
| Equity (annual) | $X | $X | |
| Benefits | $X | $X | |
| **Year 1 Total** | $X | $X | |
| **Ongoing Total** | $X | $X | |

## Non-Monetary Comparison

| Factor | Offer A | Offer B | Notes |
|--------|---------|---------|-------|
| Career Growth | X/10 | X/10 | |
| Work-Life | X/10 | X/10 | |
| Team/Culture | X/10 | X/10 | |
| Risk Level | X/10 | X/10 | |

## Weighted Analysis

Using your priorities:
- Offer A Score: X.XX
- Offer B Score: X.XX

## Key Differences
1. [Key difference 1]
2. [Key difference 2]
3. [Key difference 3]

## Recommendation

Based on your stated priorities of [X, Y, Z], **Offer [A/B]** appears to be the stronger choice because:
- [Reason 1]
- [Reason 2]
- [Reason 3]

## Things to Clarify Before Deciding
- [ ] [Question for Company A]
- [ ] [Question for Company B]

## Negotiation Opportunities
- [Opportunity 1]
- [Opportunity 2]
```

## Comparison Checklist

- âœ… Calculated total comp (not just base)
- âœ… Included equity with realistic valuation
- âœ… Factored in benefits value
- âœ… Considered tax implications
- âœ… Weighted non-monetary factors
- âœ… Assessed career growth potential
- âœ… Evaluated team and manager quality
- âœ… Checked company stability/risk
- âœ… Aligned with personal priorities
- âœ… Gut-checked the decision

## References

- `references/total_comp_calculation.md`: load when computing year 1 and ongoing total compensation for an offer
- `references/comparison_template.md`: load when laying offers out side by side
- `references/non_monetary_factors.md`: load when scoring career growth, work-life, team, culture or risk
- `references/weighted_decision_matrix.md`: load when weighting priorities and computing the weighted score
- `references/red_flags_and_gut_checks.md`: load when scanning offer, company and role red flags or running the gut-check questions
