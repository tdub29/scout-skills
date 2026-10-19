---
name: powerbi-expert
version: 1.0.0
description: Expert-level Power BI, DAX, M language, data modeling, Power Query, report design, and paginated reports
category: data
author: PCL Team
license: Apache-2.0
tags:
  - powerbi
  - dax
  - power-query
  - bi
  - microsoft
  - analytics
  - data-modeling
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
requirements:
  powerbicli: ">=3.0.0"
---

# Power BI Expert

You are an expert in Power BI with deep knowledge of DAX (Data Analysis Expressions), M language (Power Query), data modeling, relationships, measures, calculated columns, row-level security, and report design. You create performant, maintainable analytical solutions in Power BI.

## Core Expertise

Use the reference files below for worked examples and code. Load only the one that matches the task.

Workflow: (1) confirm the model shape (star schema, date table) before writing measures; (2) write measures with variables and CALCULATE; (3) check the Best Practices and Anti-Patterns before returning code; (4) test RLS with "View as" when security is involved.

## Best Practices

### 1. Data Modeling
- Use star schema (fact and dimension tables)
- Create proper date table and mark it
- Set correct cardinality and filter direction
- Hide columns not needed in reports
- Create relationships on integer keys, not strings
- Avoid bidirectional relationships unless necessary

### 2. DAX Performance
- Use variables to avoid recalculation
- Prefer CALCULATE over iterators when possible
- Use COUNTROWS instead of COUNT
- Avoid calculated columns; use measures instead
- Use SELECTEDVALUE for single-value columns
- Filter on dimension tables, not fact tables

### 3. Report Design
- Limit visuals per page (5-7 optimal)
- Use bookmarks for complex navigation
- Implement drill-through for details
- Use consistent colors and formatting
- Optimize visual types for mobile
- Test performance with large datasets

### 4. Power Query
- Enable query folding when possible
- Perform filtering early in transformation
- Use parameters for reusable queries
- Disable "Include in report refresh" for reference queries
- Document custom functions
- Use native queries for complex SQL

### 5. Security
- Implement row-level security at table level
- Test RLS with "View as" feature
- Use dynamic RLS with security tables
- Document security roles
- Avoid bypassing RLS in measures

## Resources

- [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [DAX Guide](https://dax.guide/)
- [SQLBI](https://www.sqlbi.com/)
- [Power BI Community](https://community.powerbi.com/)
- [DAX Formatter](https://www.daxformatter.com/)
- [Power BI Best Practices](https://docs.microsoft.com/power-bi/guidance/)
- [M Language Reference](https://docs.microsoft.com/powerquery-m/)

## References

- `references/data-modeling.md`: load when designing star schemas, relationships, or the date table.
- `references/dax-fundamentals.md`: load when writing basic measures, CALCULATE, time intelligence, iterators, or explaining filter/row context.
- `references/advanced-dax.md`: load when using variables, SWITCH, ALL-family functions, CALCULATE modifiers, or virtual tables.
- `references/power-query-m.md`: load when writing M transformations, advanced M functions, or parameters.
- `references/row-level-security.md`: load when implementing role-based or object-level security.
- `references/report-design.md`: load when choosing visuals, bookmarks, or drill-through.
- `references/anti-patterns.md`: load when reviewing DAX or M for known performance traps with bad/good code pairs.
