# DAX Fundamentals

## Contents

- [Basic Measures](#basic-measures)
- [CALCULATE - The Most Important Function](#calculate---the-most-important-function)
- [Time Intelligence](#time-intelligence)
- [Iterator Functions](#iterator-functions)
- [Filter Context and Row Context](#filter-context-and-row-context)

## Basic Measures
```dax
// Simple aggregations
Total Sales = SUM(FactSales[Amount])

Total Quantity = SUM(FactSales[Quantity])

Average Sale = AVERAGE(FactSales[Amount])

Distinct Customers = DISTINCTCOUNT(FactSales[CustomerKey])

// Count rows
Total Orders = COUNTROWS(FactSales)

// Conditional sum
Sales Above 100 = SUMX(
    FILTER(FactSales, FactSales[Amount] > 100),
    FactSales[Amount]
)

// Alternative with CALCULATE
Sales Above 100 = CALCULATE(
    [Total Sales],
    FactSales[Amount] > 100
)
```

## CALCULATE - The Most Important Function
```dax
// Basic filter
Sales USA = CALCULATE(
    [Total Sales],
    DimCustomer[Country] = "USA"
)

// Multiple filters (AND logic)
Sales USA Electronics = CALCULATE(
    [Total Sales],
    DimCustomer[Country] = "USA",
    DimProduct[Category] = "Electronics"
)

// OR logic using ||
Sales USA or Canada = CALCULATE(
    [Total Sales],
    DimCustomer[Country] = "USA" || DimCustomer[Country] = "Canada"
)

// Using IN for multiple values
Sales North America = CALCULATE(
    [Total Sales],
    DimCustomer[Country] IN {"USA", "Canada", "Mexico"}
)

// Remove filters with ALL
Total Sales All Countries = CALCULATE(
    [Total Sales],
    ALL(DimCustomer[Country])
)

// Keep only specific filter
Sales Ignoring Other Filters = CALCULATE(
    [Total Sales],
    ALL(DimCustomer),
    DimCustomer[Country] = "USA"
)

// Remove all filters
Grand Total = CALCULATE(
    [Total Sales],
    ALL(FactSales)
)
```

## Time Intelligence
```dax
// Year to date
YTD Sales = TOTALYTD(
    [Total Sales],
    DimDate[Date]
)

// Quarter to date
QTD Sales = TOTALQTD(
    [Total Sales],
    DimDate[Date]
)

// Month to date
MTD Sales = TOTALMTD(
    [Total Sales],
    DimDate[Date]
)

// Previous year
Sales PY = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

// Year over year growth
YoY Growth =
VAR CurrentYearSales = [Total Sales]
VAR PreviousYearSales = [Sales PY]
RETURN
    DIVIDE(CurrentYearSales - PreviousYearSales, PreviousYearSales)

// Previous month
Sales PM = CALCULATE(
    [Total Sales],
    DATEADD(DimDate[Date], -1, MONTH)
)

// Month over month growth
MoM Growth =
DIVIDE(
    [Total Sales] - [Sales PM],
    [Sales PM]
)

// Last N days
Sales Last 30 Days = CALCULATE(
    [Total Sales],
    DATESINPERIOD(DimDate[Date], LASTDATE(DimDate[Date]), -30, DAY)
)

// Moving average
Sales MA 3 Months =
CALCULATE(
    [Total Sales],
    DATESINPERIOD(DimDate[Date], LASTDATE(DimDate[Date]), -3, MONTH)
) / 3

// Same period last year
Sales SPLY = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

// Parallel period (previous complete period)
Sales Previous Quarter = CALCULATE(
    [Total Sales],
    PARALLELPERIOD(DimDate[Date], -1, QUARTER)
)
```

## Iterator Functions
```dax
// SUMX - row by row calculation
Total Revenue = SUMX(
    FactSales,
    FactSales[Quantity] * FactSales[UnitPrice]
)

// AVERAGEX
Average Order Value = AVERAGEX(
    VALUES(FactSales[OrderID]),
    [Total Sales]
)

// COUNTX with condition
Orders Above 1000 = COUNTX(
    FILTER(FactSales, [Total Sales] > 1000),
    FactSales[OrderID]
)

// RANKX
Product Rank = RANKX(
    ALL(DimProduct[ProductName]),
    [Total Sales],
    ,
    DESC,
    DENSE
)

// MINX / MAXX
Lowest Product Price = MINX(
    DimProduct,
    DimProduct[Price]
)

// Combining iterators
Weighted Average =
DIVIDE(
    SUMX(DimProduct, DimProduct[Price] * DimProduct[Weight]),
    SUM(DimProduct[Weight])
)
```

## Filter Context and Row Context
```dax
// Understanding context
// Filter context: Applied by slicers, filters, rows/columns in visual

// This measure changes with filter context
Total Sales = SUM(FactSales[Amount])

// This measure ignores filter context on Country
Total Sales All Countries = CALCULATE(
    SUM(FactSales[Amount]),
    ALL(DimCustomer[Country])
)

// Row context: When iterating through rows
// Calculated column (has row context)
Profit = FactSales[Amount] - FactSales[Cost]

// To use measure in row context, use iterator
Total Profit = SUMX(
    FactSales,
    [Total Sales] - [Total Cost]
)

// Converting row context to filter context
// Calculated column
Customer Sales = CALCULATE(
    [Total Sales],
    ALLEXCEPT(FactSales, FactSales[CustomerKey])
)
```
