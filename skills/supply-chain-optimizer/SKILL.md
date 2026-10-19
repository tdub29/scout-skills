---
name: supply-chain-optimizer
description: "Inventory levels, vendors, demand forecasting"
---

# Supply Chain Optimizer

Comprehensive frameworks for supply chain analysis, inventory management, logistics optimization, and vendor evaluation.

Moved to `references/supply-chain-mapping.md`: end-to-end supply chain map template.

## Inventory Optimization

### Economic Order Quantity (EOQ)

```
EOQ = sqrt(2DS / H)

Where: D = Annual demand, S = Ordering cost/order, H = Holding cost/unit/year
Total Cost = (D/Q)S + (Q/2)H + DC

Example: D=10,000, S=$50, H=$5 â†’ EOQ = 447 units, 22.4 orders/year
```

### Safety Stock & Reorder Point

```
SAFETY STOCK: SS = z x sigma_dLT
REORDER POINT: ROP = (Avg Daily Demand x Lead Time) + Safety Stock

SERVICE LEVEL FACTORS:
| Service Level | z-Score | Use Case          |
| ------------- | ------- | ----------------- |
| 90.0%         | 1.28    | Basic coverage    |
| 95.0%         | 1.65    | Standard          |
| 99.0%         | 2.33    | High service      |
| 99.9%         | 3.09    | Critical items    |
```

### Inventory KPI Dashboard

| Metric                | Formula                                  | Target          |
| --------------------- | ---------------------------------------- | --------------- |
| Inventory Turns       | COGS / Average Inventory                 | Industry-specific |
| Days of Supply        | Average Inventory / (COGS / 365)         | Minimize        |
| Fill Rate             | Orders Filled Complete / Total Orders    | 97%+            |
| Stockout Rate         | Stockout Events / Total Demand Events    | < 2%            |
| Carrying Cost %       | Holding Costs / Average Inventory Value  | 15-30%          |
| Dead Stock %          | No-movement Items / Total SKUs           | < 5%            |
| Inventory Accuracy    | Correct Counts / Total Counts            | 99%+            |
| GMROI                 | Gross Margin / Average Inventory Cost    | > 2.0           |

Moved to `references/segmentation-vendors-tco.md`: ABC-XYZ, vendor scorecard and TCO.

Moved to `references/forecasting-and-logistics.md`: forecasting methods, accuracy metrics, transport and warehouse.

Moved to `references/lead-time-and-risk.md`: lead time analysis and risk assessment.

## KPI Dashboard Template

| Category   | KPI                      | Target          |
| ---------- | ------------------------ | --------------- |
| Cost       | SC Cost as % of Revenue  | 5-10%           |
| Cost       | Cost per Order           | Minimize        |
| Service    | Perfect Order Rate       | 95%+            |
| Service    | On-Time In-Full (OTIF)   | 98%+            |
| Service    | Customer Fill Rate       | 97%+            |
| Efficiency | Inventory Turns          | Industry-specific|
| Efficiency | Cash-to-Cash Cycle       | Minimize        |
| Efficiency | Warehouse Utilization    | 85%             |
| Efficiency | Forecast Accuracy (MAPE) | < 20%           |

## See Also

- [Operations](../operations/SKILL.md)
- [Finance](../finance/SKILL.md)
- [Risk Management](../risk-management/SKILL.md)

## References

- `references/supply-chain-mapping.md`: load when mapping the chain end to end
- `references/segmentation-vendors-tco.md`: load for item segmentation, supplier evaluation or cost comparison
- `references/forecasting-and-logistics.md`: load for forecasts, accuracy metrics, mode selection or warehouse layout
- `references/lead-time-and-risk.md`: load for lead time variability or risk matrices
