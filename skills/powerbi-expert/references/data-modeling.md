# Data Modeling

**Star Schema Design:**
```
Fact Tables:
  - FactSales (OrderID, ProductKey, CustomerKey, DateKey, Quantity, Amount)
  - FactInventory (ProductKey, DateKey, StockLevel, ReorderPoint)

Dimension Tables:
  - DimProduct (ProductKey, ProductName, Category, SubCategory, Price)
  - DimCustomer (CustomerKey, CustomerName, Segment, Region, Country)
  - DimDate (DateKey, Date, Year, Quarter, Month, MonthName, Week, Day)
  - DimStore (StoreKey, StoreName, Region, Manager)

Relationships:
  FactSales[ProductKey] -> DimProduct[ProductKey] (Many-to-One)
  FactSales[CustomerKey] -> DimCustomer[CustomerKey] (Many-to-One)
  FactSales[DateKey] -> DimDate[DateKey] (Many-to-One)
  FactSales[StoreKey] -> DimStore[StoreKey] (Many-to-One)

Cardinality: Many-to-One (*:1)
Cross Filter Direction: Single (default) or Both (use sparingly)
Active Relationship: Yes
```

**Relationship Types:**
```dax
// One-to-Many (most common)
DimProduct[ProductKey] (1) -> FactSales[ProductKey] (*)

// Many-to-Many (use carefully)
FactSales (*) <-> BridgeTable (*) <-> DimPromotion (*)

// Inactive relationships (use USERELATIONSHIP)
FactSales[OrderDateKey] -> DimDate[DateKey] (Active)
FactSales[ShipDateKey] -> DimDate[DateKey] (Inactive)

// Use inactive relationship in measure
Sales by Ship Date = CALCULATE(
    [Total Sales],
    USERELATIONSHIP(FactSales[ShipDateKey], DimDate[DateKey])
)
```

**Date Table (Essential):**
```dax
// Calendar table using DAX
DimDate =
ADDCOLUMNS(
    CALENDAR(DATE(2020, 1, 1), DATE(2025, 12, 31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "QuarterNum", QUARTER([Date]),
    "Month", FORMAT([Date], "MMMM"),
    "MonthNum", MONTH([Date]),
    "MonthYear", FORMAT([Date], "MMM YYYY"),
    "Week", WEEKNUM([Date]),
    "Day", DAY([Date]),
    "DayOfWeek", FORMAT([Date], "dddd"),
    "DayOfWeekNum", WEEKDAY([Date]),
    "IsWeekend", WEEKDAY([Date]) IN {1, 7},
    "FiscalYear", IF(MONTH([Date]) <= 6, YEAR([Date]), YEAR([Date]) + 1),
    "FiscalQuarter", IF(MONTH([Date]) <= 6, QUARTER([Date]) + 2, QUARTER([Date]) - 2)
)

// Mark as date table
// Table Tools -> Mark as Date Table -> Date column: [Date]

// Alternative: Auto date table (not recommended for production)
// File -> Options -> Data Load -> Auto Date/Time
```
