---
name: explore-data
description: "Profile a new dataset: shape, nulls, distributions"
argument-hint: "<table or file>"
---

# /explore-data - Profile and Explore a Dataset

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate a comprehensive data profile for a table or uploaded file. Understand its shape, quality, and patterns before diving into analysis.

## Usage

```
/explore-data <table_name or file>
```

## Workflow

### 1. Access the Data

**If a data warehouse MCP server is connected:**

1. Resolve the table name (handle schema prefixes, suggest matches if ambiguous)
2. Query table metadata: column names, types, descriptions if available
3. Run profiling queries against the live data

**If a file is provided (CSV, Excel, Parquet, JSON):**

1. Read the file and load into a working dataset
2. Infer column types from the data

**If neither:**

1. Ask the user to provide a table name (with their warehouse connected) or upload a file
2. If they describe a table schema, provide guidance on what profiling queries to run

### 2. Understand Structure

Before analyzing any data, understand its structure:

**Table-level questions:**
- How many rows and columns?
- What is the grain (one row per what)?
- What is the primary key? Is it unique?
- When was the data last updated?
- How far back does the data go?

**Column classification** â€” categorize each column as one of:
- **Identifier**: Unique keys, foreign keys, entity IDs
- **Dimension**: Categorical attributes for grouping/filtering (status, type, region, category)
- **Metric**: Quantitative values for measurement (revenue, count, duration, score)
- **Temporal**: Dates and timestamps (created_at, updated_at, event_date)
- **Text**: Free-form text fields (description, notes, name)
- **Boolean**: True/false flags
- **Structural**: JSON, arrays, nested structures

### 3. Generate Data Profile

Run the following profiling checks:

**Table-level metrics:**
- Total row count
- Column count and types breakdown
- Approximate table size (if available from metadata)
- Date range coverage (min/max of date columns)

**All columns:**
- Null count and null rate
- Distinct count and cardinality ratio (distinct / total)
- Most common values (top 5-10 with frequencies)
- Least common values (bottom 5 to spot anomalies)

**Numeric columns (metrics):**
```
min, max, mean, median (p50)
standard deviation
percentiles: p1, p5, p25, p75, p95, p99
zero count
negative count (if unexpected)
```

**String columns (dimensions, text):**
```
min length, max length, avg length
empty string count
pattern analysis (do values follow a format?)
case consistency (all upper, all lower, mixed?)
leading/trailing whitespace count
```

**Date/timestamp columns:**
```
min date, max date
null dates
future dates (if unexpected)
distribution by month/week
gaps in time series
```

**Boolean columns:**
```
true count, false count, null count
true rate
```

**Present the profile as a clean summary table**, grouped by column type (dimensions, metrics, dates, IDs).

### 4. Identify Data Quality Issues

Apply the quality assessment framework below. Flag potential problems:

- **High null rates**: Columns with >5% nulls (warn), >20% nulls (alert)
- **Low cardinality surprises**: Columns that should be high-cardinality but aren't (e.g., a "user_id" with only 50 distinct values)
- **High cardinality surprises**: Columns that should be categorical but have too many distinct values
- **Suspicious values**: Negative amounts where only positive expected, future dates in historical data, obviously placeholder values (e.g., "N/A", "TBD", "test", "999999")
- **Duplicate detection**: Check if there's a natural key and whether it has duplicates
- **Distribution skew**: Extremely skewed numeric distributions that could affect averages
- **Encoding issues**: Mixed case in categorical fields, trailing whitespace, inconsistent formats

### 5. Discover Relationships and Patterns

After profiling individual columns:

- **Foreign key candidates**: ID columns that might link to other tables
- **Hierarchies**: Columns that form natural drill-down paths (country > state > city)
- **Correlations**: Numeric columns that move together
- **Derived columns**: Columns that appear to be computed from others
- **Redundant columns**: Columns with identical or near-identical information

### 6. Suggest Interesting Dimensions and Metrics

Based on the column profile, recommend:

- **Best dimension columns** for slicing data (categorical columns with reasonable cardinality, 3-50 values)
- **Key metric columns** for measurement (numeric columns with meaningful distributions)
- **Time columns** suitable for trend analysis
- **Natural groupings** or hierarchies apparent in the data
- **Potential join keys** linking to other tables (ID columns, foreign keys)

### 7. Recommend Follow-Up Analyses

Suggest 3-5 specific analyses the user could run next:

- "Trend analysis on [metric] by [time_column] grouped by [dimension]"
- "Distribution deep-dive on [skewed_column] to understand outliers"
- "Data quality investigation on [problematic_column]"
- "Correlation analysis between [metric_a] and [metric_b]"
- "Cohort analysis using [date_column] and [status_column]"

## Output Format

```
## Data Profile: [table_name]

### Overview
- Rows: 2,340,891
- Columns: 23 (8 dimensions, 6 metrics, 4 dates, 5 IDs)
- Date range: 2021-03-15 to 2024-01-22

### Column Details
[summary table]

### Data Quality Issues
[flagged issues with severity]

### Recommended Explorations
[numbered list of suggested follow-up analyses]
```

## Tips

- For very large tables (100M+ rows), profiling queries use sampling by default -- mention if you need exact counts
- If exploring a new dataset for the first time, this command gives you the lay of the land before writing specific queries
- The quality flags are heuristic -- not every flag is a real problem, but each is worth a quick look

## References

- `references/quality_assessment.md`: load in step 4 to score completeness, consistency, accuracy and timeliness
- `references/pattern_discovery.md`: load in step 5 for distribution, temporal, segmentation and correlation checks
- `references/schema_documentation.md`: load when documenting a table, running schema discovery queries or tracing lineage
