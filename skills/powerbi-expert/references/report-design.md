# Report Design

**Visualizations:**
```
// KPI Cards
Card: Total Sales
- Format: $#,##0.0K
- Conditional formatting based on target

// Charts
Line chart: Sales trend by month
- X-axis: Date (month)
- Y-axis: Total Sales
- Legend: Category
- Tooltips: Custom with additional metrics

Bar chart: Sales by product
- Y-axis: Product Name
- X-axis: Total Sales
- Data labels: On
- Top N filter: 10

// Matrix
Rows: Category, SubCategory, Product
Columns: Year, Quarter, Month
Values: Sales, Profit, Margin %
Conditional formatting: Data bars, color scales

// Map
Map: Sales by country
- Location: Country
- Bubble size: Total Sales
- Color: Profit Margin

// Decomposition Tree
Decomp: Analyze sales
- Root: Total Sales
- Explain by: Category, Region, Product

// Key Influencers
Influencers: What drives high sales
- Analyze: Total Sales
- Explain by: Product, Region, Customer Segment
```

**Bookmarks and Drill-Through:**
```
// Bookmarks
Bookmark 1: Sales View
- Visible: Sales chart, Sales KPIs
- Hidden: Profit details

Bookmark 2: Profit View
- Visible: Profit chart, Profit KPIs
- Hidden: Sales details

// Drill-through page
Page: Product Details
- Drillthrough from: Sales by Category
- Required fields: Product Name
- Content: Product metrics, related products, trend

// Buttons with actions
Button: Show Profit Details
- Action: Bookmark -> Profit View
- Tooltip: "Click to see profit analysis"
```
