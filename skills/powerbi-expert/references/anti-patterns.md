# Anti-Patterns

### 1. Calculated Columns vs Measures
```dax
// Bad: Calculated column (stored, consumes memory)
TotalRevenue = FactSales[Quantity] * FactSales[UnitPrice]

// Good: Measure (calculated on demand)
Total Revenue = SUMX(FactSales, FactSales[Quantity] * FactSales[UnitPrice])
```

### 2. Bidirectional Relationships
```dax
// Bad: Bidirectional filter on all relationships
// Can cause ambiguity and performance issues

// Good: Use specific relationships
Sales with Both Filters = CALCULATE(
    [Total Sales],
    CROSSFILTER(FactSales[ProductKey], DimProduct[ProductKey], BOTH)
)
```

### 3. Not Using Variables
```dax
// Bad: Repeated calculation
Margin % = ([Total Sales] - [Total Cost]) / [Total Sales]

// Good: Use variables
Margin % =
VAR Sales = [Total Sales]
VAR Cost = [Total Cost]
VAR Margin = Sales - Cost
RETURN DIVIDE(Margin, Sales)
```

### 4. Ignoring Query Folding
```m
// Bad: Filtering after loading all data
Source = Sql.Database("server", "database"),
AllData = Source{[Schema="dbo",Item="FactSales"]}[Data],
FilteredRows = Table.SelectRows(AllData, each [Year] = 2024)

// Good: Filter at source (query folding)
Source = Sql.Database("server", "database"),
FilteredData = Table.SelectRows(Source{[Schema="dbo",Item="FactSales"]}[Data],
    each [Year] = 2024)
```
