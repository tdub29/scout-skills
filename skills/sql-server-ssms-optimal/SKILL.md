---
name: sql-server-ssms-optimal
description: Optimal SQL development in SQL Server Management Studio (SSMS). Covers execution plans, Query Store, T-SQL batches and SET options, indexing and statistics, and SSMS workflows. Use when writing or tuning T-SQL in SSMS, analyzing execution plans, debugging slow queries, or working in SQL Server Management Studio.
---

# Optimal SQL Development in SQL Server Management Studio

Guidance for writing, tuning, and debugging T-SQL in SSMS with execution plans, Query Store, and best-practice workflows.

## When to Use This Skill

- Writing or editing T-SQL in SSMS
- Analyzing execution plans (estimated or actual)
- Tuning slow queries or stored procedures
- Using Query Store or Activity Monitor
- Designing indexes or updating statistics in SSMS
- Working with batches, temp tables, or SET options in SSMS

## Execution Plans in SSMS

### Enabling and Reading Plans

- **Estimated plan**: Ctrl+L (or Query â†’ Display Estimated Execution Plan). No execution; use for quick cost check.
- **Actual plan**: Ctrl+M toggles "Include Actual Execution Plan"; then run with F5. Use for real row counts and I/O.

**Key operators to watch:**

| Operator | Meaning |
|----------|---------|
| Table Scan / Clustered Index Scan | Full scan; consider index or narrower query |
| Index Seek | Good: using index |
| Key Lookup | Lookup from nonclustered index to heap/clustered; consider covering index |
| Sort | May spill to tempdb if memory grant too small |
| Nested Loops | Often good for small outer input |
| Hash Match | Good for larger joins without sorted input |
| Merge | Good when both inputs sorted on join key |

**High-cost focus:** Right-click plan â†’ "Show execution plan XML" or read subtree cost; tackle highest-cost operators first (usually scans, heavy sorts, or large joins).

### SET Options for Accurate Plans

Run before capturing plans so estimates match typical runtime:

```sql
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- Optional: capture XML plan for tools
SET SHOWPLAN_XML ON;  -- then run query; turn OFF after
SET SHOWPLAN_XML OFF;
```

## T-SQL Best Practices in SSMS

### Batches and GO

- Use `GO` to separate batches when you need a new parser/scope (e.g., after `CREATE VIEW`, `CREATE PROCEDURE`, or schema changes).
- Variables and temp tables are batch-scoped; `#temp` lives until the session or the batch that created it (depending on where GO is).

### Stored Procedures

```sql
CREATE OR ALTER PROCEDURE dbo.ExampleProc
  @Id INT
AS
SET NOCOUNT ON;
SET XACT_ABORT ON;

-- Use parameters for all inputs (avoid injection, help plan reuse)
SELECT ...
FROM dbo.MyTable
WHERE Id = @Id;
```

- **SET NOCOUNT ON**: Reduces network traffic and minor overhead.
- **SET XACT_ABORT ON**: Whole transaction rolls back on error.
- Always parameterize; never build SQL from string concatenation.

### Sargability and Indexes

- Avoid functions on columns in `WHERE`/`JOIN` (e.g., `WHERE YEAR(OrderDate) = 2024`). Use range instead: `WHERE OrderDate >= '20240101' AND OrderDate < '20250101'`.
- Prefer `EXISTS` over `IN` for subqueries when you only need existence.
- List columns explicitly; avoid `SELECT *` in production code.

## Query Store (SSMS)

Use when on SQL Server 2016+ and Query Store is enabled for the database.

- **Reports**: Right-click database â†’ Reports â†’ Query Store (e.g., "Top Resource Consuming Queries", "Regressed Queries").
- **Force plan**: For a known-good plan, use "Force Plan" from Query Store UI to reduce plan regression.
- **Clear cache for one query**: Prefer Query Storeâ€“based forcing or plan guides rather than clearing entire plan cache.

## Indexes and Statistics in SSMS

### Discovering Indexes

```sql
-- Indexes on a table (run from Object Explorer context or a query window)
SELECT i.name, i.type_desc, i.is_unique, i.is_primary_key,
       STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS key_columns
FROM sys.indexes i
JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.object_id = OBJECT_ID('dbo.YourTable')
  AND i.type > 0
GROUP BY i.name, i.type_desc, i.is_unique, i.is_primary_key;
```

### Updating Statistics

- After large data changes or before capturing execution plans: `UPDATE STATISTICS dbo.YourTable;` or table-level from SSMS (right-click table â†’ Statistics).
- Keep automatic statistics on; only disable for rare maintenance windows.

## SSMS Workflow Checklist

1. **Before tuning**: Turn on Actual Execution Plan (Ctrl+M), SET STATISTICS IO/TIME ON.
2. **Run query**: Note logical reads, elapsed time, and highest-cost operators.
3. **Identify bottleneck**: Usually scan vs seek, missing index, or oversized memory grant.
4. **Change one thing**: Add/change index, rewrite predicate for sargability, or simplify query.
5. **Re-run and compare**: Same SET options and plan; verify improvement before committing.

## Keyboard Shortcuts (SSMS)

| Shortcut | Action |
|----------|--------|
| F5 | Execute |
| Ctrl+L | Display estimated execution plan |
| Ctrl+M | Toggle include actual execution plan |
| Ctrl+R | Toggle results pane |
| Ctrl+T | Results to text |
| Ctrl+N | New query window |
| Ctrl+Shift+C | Copy with headers (grid) |

## Additional Resources

- For generic SQL optimization patterns (index types, join strategies), see the **sql-optimization-patterns** skill (PostgreSQL-oriented but many concepts apply).
- For T-SQL and dialect details, see the **sql-pro** skill references in this repo.
