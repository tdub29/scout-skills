---
name: sql-query-optimization
description: "Rewrite one slow SQL query. Postgres, MySQL"
---

# SQL Query Optimization

## Overview

Analyze SQL queries to identify performance bottlenecks and implement optimization techniques. Includes query analysis, indexing strategies, and rewriting patterns for improved performance.

## When to Use

- Slow query analysis and tuning
- Query rewriting and refactoring
- Index utilization verification
- Join optimization
- Subquery optimization
- Query plan analysis (EXPLAIN)
- Performance baseline establishment

## Query Analysis Framework

### 1. Analyze Current Performance

**PostgreSQL:**

```sql
-- Analyze query plan with execution time
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '1 year'
GROUP BY u.id, u.email;

-- Check table statistics
SELECT * FROM pg_stats
WHERE tablename = 'users' AND attname = 'created_at';
```

**MySQL:**

```sql
-- Analyze query plan
EXPLAIN FORMAT=JSON
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > DATE_SUB(NOW(), INTERVAL 1 YEAR)
GROUP BY u.id, u.email;

-- Check table size
SELECT table_name, ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size_MB'
FROM information_schema.tables WHERE table_schema = 'database_name';
```

### 2. Common Optimization Patterns

**PostgreSQL - Index Optimization:**

```sql
-- Create indexes for frequently filtered columns
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at DESC)
WHERE status != 'cancelled';

-- Partial indexes for filtered queries
CREATE INDEX idx_active_products
ON products(category_id)
WHERE active = true;

-- Multi-column covering indexes
CREATE INDEX idx_users_email_verified_covering
ON users(email, verified)
INCLUDE (id, name, created_at);
```

**MySQL - Index Optimization:**

```sql
-- Create composite index for multi-column filtering
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at DESC);

-- Use FULLTEXT index for text search
CREATE FULLTEXT INDEX idx_products_search
ON products(name, description);

-- Prefix indexes for large VARCHAR
CREATE INDEX idx_large_text
ON large_table(text_column(100));
```

### 3. Query Rewriting Techniques

**PostgreSQL - Window Functions:**

```sql
-- Inefficient: multiple passes
SELECT p.id, p.name,
  (SELECT COUNT(*) FROM orders o WHERE o.product_id = p.id) as order_count,
  (SELECT SUM(quantity) FROM order_items oi WHERE oi.product_id = p.id) as total_sold
FROM products p;

-- Optimized: single pass with window functions
SELECT DISTINCT p.id, p.name,
  COUNT(*) OVER (PARTITION BY p.id) as order_count,
  SUM(oi.quantity) OVER (PARTITION BY p.id) as total_sold
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id;
```

**MySQL - JOIN Optimization:**

```sql
-- Inefficient: JOIN after aggregation
SELECT user_id, name, total_orders
FROM (
  SELECT u.id as user_id, u.name, COUNT(o.id) as total_orders
  FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  GROUP BY u.id, u.name
) subquery
WHERE total_orders > 5;

-- Optimized: aggregate with HAVING clause
SELECT u.id, u.name, COUNT(o.id) as total_orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;
```

## Key Optimization Checklist

- Use EXPLAIN/EXPLAIN ANALYZE before and after optimization
- Add indexes to columns in WHERE, JOIN, and ORDER BY clauses
- Use LIMIT when exploring large result sets
- Avoid SELECT * when only specific columns needed
- Use database functions instead of application-level processing
- Batch operations to reduce network round trips
- Partition large tables for improved query performance
- Update statistics regularly with ANALYZE

## Common Pitfalls

âŒ Don't create indexes without testing impact
âŒ Don't use LIKE with leading wildcard without full-text search
âŒ Don't JOIN unnecessary tables
âŒ Don't ignore ORDER BY performance impact
âŒ Don't skip EXPLAIN analysis

âœ… DO test query changes in development first
âœ… DO monitor query performance after deployment
âœ… DO update table statistics regularly
âœ… DO use appropriate data types for columns
âœ… DO consider materialized views for complex aggregations

## Resources

- [PostgreSQL EXPLAIN Documentation](https://www.postgresql.org/docs/current/sql-explain.html)
- [MySQL EXPLAIN Documentation](https://dev.mysql.com/doc/refman/8.0/en/explain.html)
- [pgBadger - PostgreSQL log analyzer](https://pgbadger.darold.net/)
- [MySQL Workbench Query Analyzer](https://www.mysql.com/products/workbench/)

## References

- `references/batch_operations.md`: load when replacing row-by-row inserts or updates with batched statements
- `references/performance_monitoring.md`: load when finding slow queries (pg_stat_statements, MySQL slow log)
