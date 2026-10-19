# Redshift Reference

### Redshift (Amazon)

**Date/time:**
```sql
-- Current date/time
CURRENT_DATE, GETDATE(), SYSDATE

-- Date arithmetic
DATEADD(day, 7, date_column)
DATEDIFF(day, start_date, end_date)

-- Truncate to period
DATE_TRUNC('month', created_at)

-- Extract parts
EXTRACT(YEAR FROM created_at)
DATE_PART('dow', created_at)
```

**String functions:**
```sql
-- Case-insensitive
column ILIKE '%pattern%'
REGEXP_INSTR(column, 'pattern') > 0

-- String manipulation
SPLIT_PART(str, delimiter, position)
LISTAGG(column, ', ') WITHIN GROUP (ORDER BY column)
```

**Performance tips:**
- Design distribution keys for collocated joins (DISTKEY)
- Use sort keys for frequently filtered columns (SORTKEY)
- Use `EXPLAIN` to check query plan
- Avoid cross-node data movement (watch for DS_BCAST and DS_DIST)
- `ANALYZE` and `VACUUM` regularly
- Use late-binding views for schema flexibility

---
