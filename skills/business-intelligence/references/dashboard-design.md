# Dashboard Design Principles

## Dashboard Design Principles

**Visual hierarchy:**
1. Most important metrics at top-left
2. Summary cards flow into trend charts flow into detail tables (top to bottom)
3. Related metrics grouped; white space separates logical sections
4. RAG status colors: Green `#28A745` | Yellow `#FFC107` | Red `#DC3545` | Gray `#6C757D`

**Chart selection matrix:**

| Data question | Chart type | Alternative |
|---------------|-----------|-------------|
| Trend over time | Line | Area |
| Part of whole | Donut / Treemap | Stacked bar |
| Comparison across categories | Bar / Column | Bullet |
| Distribution | Histogram | Box plot |
| Relationship | Scatter | Bubble |
| Geographic | Choropleth | Filled map |

## Executive Dashboard Example

```
+------------------------------------------------------------+
|                   EXECUTIVE SUMMARY                         |
| Revenue: $12.4M (+15% YoY)   Pipeline: $45.2M (+22% QoQ)  |
| Customers: 2,847 (+340 MTD)  NPS: 72 (+5 pts)              |
+------------------------------------------------------------+
| REVENUE TREND (12-mo line)    | REVENUE BY SEGMENT (donut)  |
+-------------------------------+-----------------------------+
| TOP 10 ACCOUNTS (table)       | KPI STATUS (RAG cards)      |
+-------------------------------+-----------------------------+
```
