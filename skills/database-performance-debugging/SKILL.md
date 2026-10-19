---
name: database-performance-debugging
description: "Whole DB is slow. Indexes, plans, hot queries"
---

# Database Performance Debugging

## Overview

Database performance issues directly impact application responsiveness. Debugging focuses on identifying slow queries and optimizing execution plans.

## When to Use

- Slow application response times
- High database CPU
- Slow queries identified
- Performance regression
- Under load stress

## Instructions

### 1. **Identify Slow Queries**

```sql
-- Enable slow query log (MySQL)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.5;

-- View slow queries
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SELECT * FROM mysql.slow_log;

-- PostgreSQL slow queries
CREATE EXTENSION pg_stat_statements;
SELECT mean_exec_time, calls, query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;

-- SQL Server slow queries
SELECT TOP 10
  execution_count,
  total_elapsed_time,
  statement_text
FROM sys.dm_exec_query_stats
ORDER BY total_elapsed_time DESC;

-- Query profiling
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 123;
-- Slow: Seq Scan (full table scan)
-- Fast: Index Scan
```

### 2. **Common Issues & Solutions**

Five patterns with before and after fixes (N+1, missing index, inefficient JOIN, large table scan, slow aggregation) are in `references/common-issues.md`.

### 3. **Execution Plan Analysis**

How to read scan types, join methods and EXPLAIN ANALYZE rows and timings is in `references/execution-plan-reading.md`.

### 4. **Debugging Process**

```yaml
Steps:

1. Identify Slow Query
  - Enable slow query logging
  - Run workload
  - Review slow log
  - Note execution time

2. Analyze with EXPLAIN
  - Run EXPLAIN ANALYZE
  - Look for Seq Scan
  - Check estimated vs actual rows
  - Review join methods

3. Find Root Cause
  - Missing index?
  - Inefficient join?
  - Missing WHERE clause?
  - Outdated statistics?

4. Try Fix
  - Add index
  - Rewrite query
  - Update statistics
  - Archive old data

5. Measure Improvement
  - Run query after fix
  - Compare execution time
  - Before: 5000ms
  - After: 100ms (50x faster!)

6. Monitor
  - Track slow queries
  - Set baseline
  - Alert on regression
  - Periodic review

---

Checklist:

[ ] Slow query identified and logged
[ ] EXPLAIN ANALYZE run
[ ] Estimated vs actual rows analyzed
[ ] Seq Scans identified
[ ] Indexes checked
[ ] Join strategy reviewed
[ ] Statistics updated
[ ] Query rewritten if needed
[ ] Index created if needed
[ ] Fix verified
[ ] Performance baseline established
[ ] Monitoring configured
[ ] Documented for team
```

## Key Points

- Enable slow query logging in production
- Use EXPLAIN ANALYZE to investigate
- Look for Seq Scan = missing index
- Add indexes to WHERE/JOIN columns
- Monitor query statistics
- Update table statistics regularly
- Rewrite queries to avoid inefficiencies
- Use pagination for large result sets
- Measure before and after optimization
- Track slow query trends

## References

- `references/common-issues.md`: load when diagnosing a slow query pattern (N+1, missing index, bad JOIN, large scan, slow aggregation) and you need the before and after fix
- `references/execution-plan-reading.md`: load when reading EXPLAIN or EXPLAIN ANALYZE output or comparing join methods
