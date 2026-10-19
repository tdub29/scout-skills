# Power Query (M Language)

## Contents

- [Data Transformation](#data-transformation)
- [Advanced M Functions](#advanced-m-functions)
- [Parameters and Dynamic Queries](#parameters-and-dynamic-queries)

## Data Transformation
```m
// Basic transformations
let
    Source = Sql.Database("server", "database"),
    FactSales = Source{[Schema="dbo",Item="FactSales"]}[Data],

    // Remove columns
    RemovedColumns = Table.RemoveColumns(FactSales, {"UnneededColumn1", "UnneededColumn2"}),

    // Rename columns
    RenamedColumns = Table.RenameColumns(RemovedColumns, {
        {"old_name", "NewName"},
        {"order_date", "OrderDate"}
    }),

    // Change data types
    ChangedTypes = Table.TransformColumnTypes(RenamedColumns, {
        {"OrderDate", type date},
        {"Amount", type number},
        {"Quantity", Int64.Type}
    }),

    // Filter rows
    FilteredRows = Table.SelectRows(ChangedTypes, each [OrderDate] >= #date(2020, 1, 1)),

    // Add custom column
    AddedCustom = Table.AddColumn(FilteredRows, "Revenue",
        each [Quantity] * [UnitPrice], type number),

    // Replace values
    ReplacedValues = Table.ReplaceValue(FilteredRows, null, 0,
        Replacer.ReplaceValue, {"Discount"}),

    // Remove duplicates
    RemovedDuplicates = Table.Distinct(AddedCustom, {"OrderID"})
in
    RemovedDuplicates
```

## Advanced M Functions
```m
// Custom function
let
    GetSalesByDate = (startDate as date, endDate as date) as table =>
    let
        Source = Sql.Database("server", "database"),
        FactSales = Source{[Schema="dbo",Item="FactSales"]}[Data],
        FilteredRows = Table.SelectRows(FactSales,
            each [OrderDate] >= startDate and [OrderDate] <= endDate)
    in
        FilteredRows
in
    GetSalesByDate

// Invoke function
Sales2024 = GetSalesByDate(#date(2024, 1, 1), #date(2024, 12, 31))

// Conditional column
AddedConditional = Table.AddColumn(Source, "Segment",
    each if [Amount] >= 1000 then "High"
         else if [Amount] >= 500 then "Medium"
         else "Low")

// Group by (aggregation)
GroupedRows = Table.Group(Source, {"CustomerID"}, {
    {"TotalSales", each List.Sum([Amount]), type number},
    {"OrderCount", each Table.RowCount(_), Int64.Type},
    {"AvgAmount", each List.Average([Amount]), type number}
})

// Merge queries (joins)
Merged = Table.NestedJoin(
    FactSales, {"ProductKey"},
    DimProduct, {"ProductKey"},
    "Product",
    JoinKind.LeftOuter
)

// Expand merged table
Expanded = Table.ExpandTableColumn(Merged, "Product",
    {"ProductName", "Category"},
    {"ProductName", "Category"})

// Append queries (union)
Appended = Table.Combine({Sales2023, Sales2024})

// Pivot
Pivoted = Table.Pivot(Source,
    List.Distinct(Source[Category]),
    "Category",
    "Amount",
    List.Sum)

// Unpivot
Unpivoted = Table.UnpivotOtherColumns(Source,
    {"Date", "Product"},
    "Attribute",
    "Value")
```

## Parameters and Dynamic Queries
```m
// Parameter
EnvironmentParameter = "Production" meta [IsParameterQuery=true, Type="Text", AllowedValues={"Development", "Production"}]

// Use in connection string
let
    Server = if EnvironmentParameter = "Production"
             then "prod-server.database.windows.net"
             else "dev-server.database.windows.net",
    Source = Sql.Database(Server, "database")
in
    Source

// Date range parameters
StartDate = #date(2024, 1, 1) meta [IsParameterQuery=true, Type="Date"]
EndDate = #date(2024, 12, 31) meta [IsParameterQuery=true, Type="Date"]

// Query folding check
Table.View(null, [
    GetType = () => type table [OrderID = Int64.Type, Amount = number],
    GetRows = () => #table(
        {"OrderID", "Amount"},
        {{1, 100}, {2, 200}}
    ),
    OnTake = (count as number) => ...,
    OnSkip = (count as number) => ...
])
```
