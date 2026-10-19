# Advanced DAX

## Contents

- [Variables (VAR)](#variables-var)
- [SWITCH and Complex Logic](#switch-and-complex-logic)
- [ALL Family Functions](#all-family-functions)
- [CALCULATE Modifiers](#calculate-modifiers)
- [Virtual Tables](#virtual-tables)

## Variables (VAR)
```dax
// Using variables for clarity and performance
Sales vs Target =
VAR ActualSales = [Total Sales]
VAR TargetSales = [Sales Target]
VAR Variance = ActualSales - TargetSales
VAR VariancePct = DIVIDE(Variance, TargetSales)
RETURN
    IF(
        ISBLANK(TargetSales),
        BLANK(),
        VariancePct
    )

// Variables are evaluated once
Customer Lifetime Value =
VAR FirstPurchase =
    CALCULATE(
        MIN(FactSales[Date]),
        ALLEXCEPT(FactSales, FactSales[CustomerKey])
    )
VAR LastPurchase =
    CALCULATE(
        MAX(FactSales[Date]),
        ALLEXCEPT(FactSales, FactSales[CustomerKey])
    )
VAR DaysBetween = DATEDIFF(FirstPurchase, LastPurchase, DAY)
VAR TotalSpend =
    CALCULATE(
        [Total Sales],
        ALLEXCEPT(FactSales, FactSales[CustomerKey])
    )
RETURN
    DIVIDE(TotalSpend, DIVIDE(DaysBetween, 365), 0)
```

## SWITCH and Complex Logic
```dax
// SWITCH for multiple conditions
Metric Selector =
SWITCH(
    SELECTEDVALUE(MetricParameter[Metric]),
    "Revenue", [Total Sales],
    "Profit", [Total Profit],
    "Quantity", [Total Quantity],
    "Orders", [Total Orders],
    BLANK()
)

// Nested IF vs SWITCH
Customer Tier =
VAR LTV = [Customer Lifetime Value]
RETURN
    SWITCH(
        TRUE(),
        LTV >= 10000, "VIP",
        LTV >= 5000, "Gold",
        LTV >= 1000, "Silver",
        "Bronze"
    )

// Complex business logic
Sales Performance =
VAR CurrentSales = [Total Sales]
VAR TargetSales = [Sales Target]
VAR GrowthRate = [YoY Growth]
RETURN
    SWITCH(
        TRUE(),
        ISBLANK(CurrentSales), "No Data",
        CurrentSales >= TargetSales && GrowthRate >= 0.1, "Exceeding",
        CurrentSales >= TargetSales, "Meeting Target",
        CurrentSales >= TargetSales * 0.9, "Close to Target",
        "Below Target"
    )
```

## ALL Family Functions
```dax
// ALL - removes all filters
All Sales = CALCULATE([Total Sales], ALL(FactSales))

// ALLSELECTED - removes filters but keeps external filters
Sales % of Selected =
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALLSELECTED())
)

// ALLEXCEPT - removes all filters except specified
Sales Same Customer = CALCULATE(
    [Total Sales],
    ALLEXCEPT(FactSales, FactSales[CustomerKey])
)

// REMOVEFILTERS (modern alternative to ALL)
Sales All Products = CALCULATE(
    [Total Sales],
    REMOVEFILTERS(DimProduct)
)

// VALUES vs ALL
// VALUES - returns filtered distinct values
// ALL - returns all distinct values (ignores filters)

Filtered Product Count = COUNTROWS(VALUES(DimProduct[ProductName]))
All Product Count = COUNTROWS(ALL(DimProduct[ProductName]))
```

## CALCULATE Modifiers
```dax
// KEEPFILTERS - adds filter without removing existing
Sales With Filter = CALCULATE(
    [Total Sales],
    KEEPFILTERS(DimProduct[Category] = "Electronics")
)

// USERELATIONSHIP - activate inactive relationship
Sales by Ship Date = CALCULATE(
    [Total Sales],
    USERELATIONSHIP(FactSales[ShipDateKey], DimDate[DateKey])
)

// CROSSFILTER - change relationship direction
Sales Both Ways = CALCULATE(
    [Total Sales],
    CROSSFILTER(FactSales[ProductKey], DimProduct[ProductKey], BOTH)
)

// ALL - remove filter
Sales All Regions = CALCULATE(
    [Total Sales],
    ALL(DimCustomer[Region])
)
```

## Virtual Tables
```dax
// SUMMARIZE - create virtual summary table
Sales by Category =
SUMX(
    SUMMARIZE(
        FactSales,
        DimProduct[Category],
        "CategorySales", [Total Sales]
    ),
    [CategorySales]
)

// ADDCOLUMNS - add calculated columns to table
Top Customers =
TOPN(
    10,
    ADDCOLUMNS(
        VALUES(DimCustomer[CustomerName]),
        "CustomerSales", [Total Sales]
    ),
    [CustomerSales],
    DESC
)

// SELECTCOLUMNS - select specific columns
Customer List =
SELECTCOLUMNS(
    DimCustomer,
    "Name", DimCustomer[CustomerName],
    "Country", DimCustomer[Country]
)

// GENERATE - cartesian product
Date Product Combinations =
GENERATE(
    VALUES(DimDate[Date]),
    VALUES(DimProduct[ProductName])
)
```
