# ABC-XYZ, Vendor Scorecard and TCO

## Contents

- [ABC-XYZ Analysis Framework](#abc-xyz-analysis-framework)
- [Vendor Scorecard](#vendor-scorecard)
- [Total Cost of Ownership (TCO)](#total-cost-of-ownership-tco)

## ABC-XYZ Analysis Framework

```
ABC CLASSIFICATION (Value):
A Items: Top 20% of SKUs = ~80% of annual consumption value
  â†’ Tight control, frequent review, accurate forecasts
B Items: Next 30% of SKUs = ~15% of value
  â†’ Moderate control, periodic review
C Items: Bottom 50% of SKUs = ~5% of value
  â†’ Minimal control, simple replenishment rules

XYZ CLASSIFICATION (Demand Variability):
X: Coefficient of Variation < 0.5 â†’ Stable, predictable demand
Y: CV between 0.5 and 1.0 â†’ Some variation, trend/seasonal
Z: CV > 1.0 â†’ Highly irregular, sporadic demand

COMBINED MATRIX:
| Class | AX         | AY           | AZ            |
| ----- | ---------- | ------------ | ------------- |
| Strat | JIT/Kanban | Forecast     | Order on demand|
| Class | BX         | BY           | BZ            |
| Strat | Reorder pt | Buffer stock | Min/Max       |
| Class | CX         | CY           | CZ            |
| Strat | Bulk buy   | Periodic rev | Eliminate?     |
```

## Vendor Scorecard

### Supplier Evaluation Matrix

| Criteria           | Weight | Score (1-5) | Weighted Score | Notes |
| ------------------ | ------ | ----------- | -------------- | ----- |
| Quality (PPM)      | 25%    |             |                |       |
| Delivery (OTIF)    | 20%    |             |                |       |
| Pricing            | 20%    |             |                |       |
| Responsiveness     | 10%    |             |                |       |
| Financial Health   | 10%    |             |                |       |
| Innovation         | 5%     |             |                |       |
| Sustainability     | 5%     |             |                |       |
| Risk Profile       | 5%     |             |                |       |
| **Total**          | 100%   |             | **__ / 5.0**   |       |

```
RATING SCALE:
4.5-5.0  Strategic Partner â€” expand relationship
3.5-4.4  Preferred Supplier â€” maintain, develop
2.5-3.4  Approved Supplier â€” improvement plan required
< 2.5    Probation / Exit â€” find alternative
```

### Supplier Performance Tracking

| KPI                 | Target  | Q1 Actual | Q2 Actual | Q3 Actual | Q4 Actual | Trend |
| ------------------- | ------- | --------- | --------- | --------- | --------- | ----- |
| On-Time Delivery    | 98%+    |           |           |           |           |       |
| Quality (PPM)       | < 500   |           |           |           |           |       |
| Lead Time (days)    |         |           |           |           |           |       |
| Price Variance      | +/- 2%  |           |           |           |           |       |
| Response Time (hrs) | < 24    |           |           |           |           |       |
| Corrective Actions  | < 2/qtr |           |           |           |           |       |

## Total Cost of Ownership (TCO)

```
TCO = Acquisition Costs + Operating Costs + Disposal Costs

ACQUISITION COSTS:
  Purchase price
+ Shipping / freight
+ Customs / duties / tariffs
+ Procurement labor
+ Quality inspection
+ Supplier qualification
= Total Acquisition

OPERATING COSTS (over useful life):
  Maintenance & repair
+ Inventory carrying cost
+ Warranty claims
+ Downtime cost (if component fails)
+ Training / support
+ Quality failures (scrap, rework)
= Total Operating

DISPOSAL COSTS:
  Decommissioning
+ Recycling / disposal fees
+ Environmental compliance
= Total Disposal

TCO = Total Acquisition + Total Operating + Total Disposal
```

### TCO Comparison Template

| Cost Element         | Supplier A | Supplier B | Supplier C |
| -------------------- | ---------- | ---------- | ---------- |
| Unit Price           |            |            |            |
| Shipping             |            |            |            |
| Duties / Tariffs     |            |            |            |
| Quality Cost (est.)  |            |            |            |
| Inventory Carry Cost |            |            |            |
| Lead Time Cost       |            |            |            |
| Risk Premium         |            |            |            |
| **Total TCO/Unit**   |            |            |            |
| **Annual TCO**       |            |            |            |
