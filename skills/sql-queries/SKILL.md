---
name: sql-queries
description: Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.
user-invocable: false
---

# SQL Queries Skill

Write correct, performant, readable SQL across all major data warehouse dialects.

## Dialect-Specific Reference

Identify the target dialect first, write with CTEs, then load only that dialect's reference.

- `references/dialect-postgresql.md`: PostgreSQL, Aurora, RDS, Supabase, Neon
- `references/dialect-snowflake.md`: Snowflake
- `references/dialect-bigquery.md`: BigQuery
- `references/dialect-redshift.md`: Redshift
- `references/dialect-databricks.md`: Databricks SQL
- `references/common-patterns.md`: window functions, CTEs, cohort retention, funnel, deduplication

## Common SQL Patterns

Load `references/common-patterns.md` when writing window functions, CTE chains, cohort retention, funnels, or dedup queries.

## Error Handling and Debugging

When a query fails:

1. **Syntax errors**: Check for dialect-specific syntax (e.g., `ILIKE` not available in BigQuery, `SAFE_DIVIDE` only in BigQuery)
2. **Column not found**: Verify column names against schema -- check for typos, case sensitivity (PostgreSQL is case-sensitive for quoted identifiers)
3. **Type mismatches**: Cast explicitly when comparing different types (`CAST(col AS DATE)`, `col::DATE`)
4. **Division by zero**: Use `NULLIF(denominator, 0)` or dialect-specific safe division
5. **Ambiguous columns**: Always qualify column names with table alias in JOINs
6. **Group by errors**: All non-aggregated columns must be in GROUP BY (except in BigQuery which allows grouping by alias)

## References

- `references/dialect-postgresql.md`: load when the target is PostgreSQL or a Postgres-compatible service
- `references/dialect-snowflake.md`: load when the target is Snowflake
- `references/dialect-bigquery.md`: load when the target is BigQuery
- `references/dialect-redshift.md`: load when the target is Redshift
- `references/dialect-databricks.md`: load when the target is Databricks SQL
- `references/common-patterns.md`: load when writing window functions, CTE chains, cohort retention, funnels, or dedup queries
