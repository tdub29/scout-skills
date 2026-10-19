# Maturity Model and Performance Checklist

## Self-Service BI Maturity Model

| Level | Capability | Users can... |
|-------|-----------|-------------|
| 1 - Consumers | View & filter | Open dashboards, apply filters, export data |
| 2 - Explorers | Ad-hoc queries | Write simple queries, create basic charts, share findings |
| 3 - Builders | Design dashboards | Combine data sources, create calculated fields, publish reports |
| 4 - Modelers | Define data models | Create semantic models, define metrics, optimize performance |

## Performance Optimization Checklist

- [ ] Limit visualizations per page (5-8 max)
- [ ] Use data extracts or materialized views instead of live connections for heavy dashboards
- [ ] Minimize calculated fields in the visualization layer; push logic to the semantic layer or warehouse
- [ ] Apply context filters to reduce query scope
- [ ] Aggregate at source when granularity allows
- [ ] Schedule data refreshes during off-peak hours
- [ ] Monitor and log query execution times; target < 5 s per dashboard load

**Query optimization example:**
```sql
-- Before: full table scan
SELECT * FROM large_table WHERE date >= '2024-01-01';

-- After: partitioned, filtered, and column-pruned
SELECT order_id, customer_id, amount
FROM large_table
WHERE partition_date >= '2024-01-01'
  AND status = 'active'
LIMIT 10000;
```
