---
name: xlsx
description: "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path â€” even casually (like \"the xlsx in my downloads\") â€” and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved."
license: Proprietary. LICENSE.txt has complete terms
---

## Good360 / Trevor standing requirements (always apply)

These override the generic guidance below for any workbook produced on this machine.

### a. Font-color convention
Color cell text by role so a reviewer can audit the model quickly:
- **Blue (RGB 0,0,255 / `0000FF`)**: hardcoded inputs and scenario assumptions.
- **Black (RGB 0,0,0 / `000000`)**: formulas referencing cells on the same sheet.
- **Green (RGB 0,128,0 / `008000`)**: formulas linked from another sheet in the same workbook.
- **Red (RGB 192,0,0 / `C00000`)**: unusual items or items needing attention.

Add a small font key on the summary/model sheet when the workbook is meant for review.

### b. Text vs formulas
Any cell value beginning with `=` is a formula to Excel/openpyxl. Do not use a leading equals sign as prose, a visual marker, or a source-note prefix.

- Good text note: `orders x PE-per-order`
- Bad text note: `= orders x PE-per-order`
- Good formula: `=B9*B10`
- If a literal text cell truly must display a leading equals sign, prefix it with an apostrophe or explicitly set it as text and verify the worksheet XML has no `<f>` element for that cell.

Source/unit/commentary cells are text, not formulas. A workbook that makes Excel show "We found a problem with some content" is not deliverable.

### c. No em dashes
Do not put em dashes (U+2014) in workbook prose, headers, or cell text. Use a comma, colon, parenthesis, or sentence break.

### d. openpyxl empty cached formula values
openpyxl may write an empty cached value (`<v></v>` or `<v/>`) immediately after a formula cell's `<f>`. Excel can treat that as corrupt formula metadata. After saving any workbook with openpyxl, run:

```bash
python scripts/finalize_xlsx.py output.xlsx
```

The script removes empty cached formula values from worksheet XML so Excel recalculates formulas on open.

### e. Mandatory final integrity check
Before delivering any `.xlsx`, run:

```bash
python scripts/check_xlsx_integrity.py output.xlsx
```

This checks ZIP/XML health, empty cached formula values, em dashes, and suspicious formulas that look like prose accidentally serialized as formulas. Fix every error before delivery.

Then verify calculations by the strongest available route:
1. Open/recalculate/save through Excel automation when available.
2. Otherwise run `scripts/recalc.py` if LibreOffice is available.
3. If no recalc engine is available, reproduce key formula outputs in Python, set full-calc-on-open metadata, and clearly state that formulas are expected to calculate on user open.

### f. Durable source references for Good360 deliverables
Workbook-visible source references must be meaningful months later. Do not leave temporary numbered export filenames, generic export names, or absolute personal paths as the main source reference in a model or deliverable.

For project work:
- Copy or move source extracts into the project companion folder under `data/` with descriptive names before building the final workbook.
- Copy screenshots or visual references into `assets/` with descriptive names.
- In workbook cells, show project-relative paths such as `data/2025 Amazon Product Need FMV Mix.xlsx` plus a plain-English description of what the file contains.
- Preserve original export names only as secondary provenance in notes or artifact summaries when useful, never as the primary visible reference.
- If the source must stay outside the project, add a durable artifact summary or source note that explains what the external file is and why it was not copied.

### g. Main deliverable page layout
For stakeholder-facing Good360 workbooks, the first tab is the deliverable page, not the audit trail.

Default pattern:
- First sheet title should be the deliverable name. When helpful, add a short parenthetical such as `(Only this tab matters, rest for backup)`.
- Keep the first page compact and answer-first. Put only essential assumptions above the answer: total, weights, period/date, and business-readable source names.
- Put the final answer table immediately under those assumptions, usually within columns `A:E` or `A:F` when the output is a small allocation or summary.
- Use short, plain headers. Do not add a `Formula note` column, QA checks, font key, long source paths, or process notes on the main deliverable page unless the user explicitly asks for an audit/model tab as the first page.
- Put reproducibility material on backup tabs: source rows, category mapping, QA checks, font key, source paths, and technical notes.
- Main-page source labels should be business-readable names such as `2025 Amazon Product Category FMV Mix`, not project paths. Project-relative paths belong on backup/source tabs or artifact summary notes.
- Avoid frozen panes on the main deliverable page unless the user asks for them.
- Use restrained Excel-native formatting. The main page should be easy to send, screenshot, or review quickly, with minimal fills and no dashboard styling.

# Requirements for Outputs

## Contents

- [Good360 / Trevor standing requirements (always apply)](#good360--trevor-standing-requirements-always-apply)
- [All Excel files](#all-excel-files)
- [Financial models](#financial-models)
- [Overview](#overview)
- [Important Requirements](#important-requirements)
- [Reading and analyzing data](#reading-and-analyzing-data)
- [Excel File Workflows](#excel-file-workflows)
- [CRITICAL: Use Formulas, Not Hardcoded Values](#critical-use-formulas-not-hardcoded-values)
- [Common Workflow](#common-workflow)
- [Recalculating formulas](#recalculating-formulas)
- [Formula Verification Checklist](#formula-verification-checklist)
- [Best Practices](#best-practices)
- [Code Style Guidelines](#code-style-guidelines)


## All Excel files

### Professional Font
- Use a consistent, professional font (e.g., Arial, Times New Roman) for all deliverables unless otherwise instructed by the user

### Zero Formula Errors
- Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preserve Existing Templates (when updating templates)
- Study and EXACTLY match existing format, style, and conventions when modifying files
- Never impose standardized formatting on files with established patterns
- Existing template conventions ALWAYS override these guidelines

## Financial models

### Color Coding Standards
Unless otherwise stated by the user or existing template

#### Industry-Standard Color Conventions
- **Blue text (RGB: 0,0,255)**: Hardcoded inputs, and numbers users will change for scenarios
- **Black text (RGB: 0,0,0)**: ALL formulas and calculations
- **Green text (RGB: 0,128,0)**: Links pulling from other worksheets within same workbook
- **Red text (RGB: 255,0,0)**: External links to other files
- **Yellow background (RGB: 255,255,0)**: Key assumptions needing attention or cells that need to be updated

### Number Formatting Standards

#### Required Format Rules
- **Years**: Format as text strings (e.g., "2024" not "2,024")
- **Currency**: Use $#,##0 format; ALWAYS specify units in headers ("Revenue ($mm)")
- **Zeros**: Use number formatting to make all zeros "-", including percentages (e.g., "$#,##0;($#,##0);-")
- **Percentages**: Default to 0.0% format (one decimal)
- **Multiples**: Format as 0.0x for valuation multiples (EV/EBITDA, P/E)
- **Negative numbers**: Use parentheses (123) not minus -123

### Formula Construction Rules

#### Assumptions Placement
- Place ALL assumptions (growth rates, margins, multiples, etc.) in separate assumption cells
- Use cell references instead of hardcoded values in formulas
- Example: Use =B5*(1+$B$6) instead of =B5*1.05

#### Formula Error Prevention
- Verify all cell references are correct
- Check for off-by-one errors in ranges
- Ensure consistent formulas across all projection periods
- Test with edge cases (zero values, negative numbers)
- Verify no unintended circular references

#### Documentation Requirements for Hardcodes
- Comment or in cells beside (if end of table). Format: "Source: [System/Document], [Date], [Specific Reference], [URL if applicable]"
- Examples:
  - "Source: Company 10-K, FY2024, Page 45, Revenue Note, [SEC EDGAR URL]"
  - "Source: Company 10-Q, Q2 2025, Exhibit 99.1, [SEC EDGAR URL]"
  - "Source: Bloomberg Terminal, 8/15/2025, AAPL US Equity"
  - "Source: FactSet, 8/20/2025, Consensus Estimates Screen"

# XLSX creation, editing, and analysis

## Overview

A user may ask you to create, edit, or analyze the contents of an .xlsx file. You have different tools and workflows available for different tasks.

## Important Requirements

**Integrity and recalculation are required before delivery**: Run `scripts/finalize_xlsx.py` after openpyxl saves, run `scripts/check_xlsx_integrity.py`, then use the strongest available recalculation route (Excel automation, LibreOffice `scripts/recalc.py`, or Python mirror validation when no spreadsheet engine is available).

## Reading and analyzing data

### Data analysis with pandas
For data analysis, visualization, and basic operations, use **pandas** which provides powerful data manipulation capabilities:

```python
import pandas as pd

# Read Excel
df = pd.read_excel('file.xlsx')  # Default: first sheet
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets as dict

# Analyze
df.head()      # Preview data
df.info()      # Column info
df.describe()  # Statistics

# Write Excel
df.to_excel('output.xlsx', index=False)
```

## Excel File Workflows

## CRITICAL: Use Formulas, Not Hardcoded Values

**Always use Excel formulas instead of calculating values in Python and hardcoding them.** This ensures the spreadsheet remains dynamic and updateable.

### âŒ WRONG - Hardcoding Calculated Values
```python
# Bad: Calculating in Python and hardcoding result
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcodes 5000

# Bad: Computing growth rate in Python
growth = (df.iloc[-1]['Revenue'] - df.iloc[0]['Revenue']) / df.iloc[0]['Revenue']
sheet['C5'] = growth  # Hardcodes 0.15

# Bad: Python calculation for average
avg = sum(values) / len(values)
sheet['D20'] = avg  # Hardcodes 42.5
```

### âœ… CORRECT - Using Excel Formulas
```python
# Good: Let Excel calculate the sum
sheet['B10'] = '=SUM(B2:B9)'

# Good: Growth rate as Excel formula
sheet['C5'] = '=(C4-C2)/C2'

# Good: Average using Excel function
sheet['D20'] = '=AVERAGE(D2:D19)'
```

This applies to ALL calculations - totals, percentages, ratios, differences, etc. The spreadsheet should be able to recalculate when source data changes.

## Common Workflow
1. **Choose tool**: pandas for data, openpyxl for formulas/formatting
2. **Create/Load**: Create new workbook or load existing file
3. **Modify**: Add/edit data, formulas, and formatting
4. **Save**: Write to file
5. **Finalize and validate package integrity**: If openpyxl wrote the file, run `scripts/finalize_xlsx.py`, then run `scripts/check_xlsx_integrity.py`
   ```bash
   python scripts/finalize_xlsx.py output.xlsx
   python scripts/check_xlsx_integrity.py output.xlsx
   ```
6. **Recalculate formulas (MANDATORY IF USING FORMULAS)**: Use Excel automation when available, otherwise use the `scripts/recalc.py` script when LibreOffice is available
   ```bash
   python scripts/recalc.py output.xlsx
   ```
7. **Verify and fix any errors**: 
   - The script returns JSON with error details
   - If `status` is `errors_found`, check `error_summary` for specific error types and locations
   - Fix the identified errors and recalculate again
   - Common errors to fix:
     - `#REF!`: Invalid cell references
     - `#DIV/0!`: Division by zero
     - `#VALUE!`: Wrong data type in formula
     - `#NAME?`: Unrecognized formula name

### Creating new Excel files

```python
# Using openpyxl for formulas and formatting
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# Add data
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
sheet.append(['Row', 'of', 'data'])

# Add formula
sheet['B2'] = '=SUM(A1:A10)'

# Formatting
sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')

# Column width
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

### Editing existing Excel files

```python
# Using openpyxl to preserve formulas and formatting
from openpyxl import load_workbook

# Load existing file
wb = load_workbook('existing.xlsx')
sheet = wb.active  # or wb['SheetName'] for specific sheet

# Working with multiple sheets
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]
    print(f"Sheet: {sheet_name}")

# Modify cells
sheet['A1'] = 'New Value'
sheet.insert_rows(2)  # Insert row at position 2
sheet.delete_cols(3)  # Delete column 3

# Add new sheet
new_sheet = wb.create_sheet('NewSheet')
new_sheet['A1'] = 'Data'

wb.save('modified.xlsx')
```

## Recalculating formulas

Excel files created or modified by openpyxl contain formulas as strings but not calculated values. Prefer Excel automation when available because it is the target application. Otherwise use the provided `scripts/recalc.py` script with LibreOffice:

```bash
python scripts/recalc.py <excel_file> [timeout_seconds]
```

Example:
```bash
python scripts/recalc.py output.xlsx 30
```

The script:
- Automatically sets up LibreOffice macro on first run
- Recalculates all formulas in all sheets
- Scans ALL cells for Excel errors (#REF!, #DIV/0!, etc.)
- Returns JSON with detailed error locations and counts
- Works on both Linux and macOS

## Formula Verification Checklist

Quick checks to ensure formulas work correctly:

### Essential Verification
- [ ] **Test 2-3 sample references**: Verify they pull correct values before building full model
- [ ] **Column mapping**: Confirm Excel columns match (e.g., column 64 = BL, not BK)
- [ ] **Row offset**: Remember Excel rows are 1-indexed (DataFrame row 5 = Excel row 6)

### Common Pitfalls
- [ ] **NaN handling**: Check for null values with `pd.notna()`
- [ ] **Far-right columns**: FY data often in columns 50+ 
- [ ] **Multiple matches**: Search all occurrences, not just first
- [ ] **Prose-as-formula**: No explanatory/source/unit note starts with `=`; run `check_xlsx_integrity.py`
- [ ] **Division by zero**: Check denominators before using `/` in formulas (#DIV/0!)
- [ ] **Wrong references**: Verify all cell references point to intended cells (#REF!)
- [ ] **Cross-sheet references**: Use correct format (Sheet1!A1) for linking sheets

### Formula Testing Strategy
- [ ] **Start small**: Test formulas on 2-3 cells before applying broadly
- [ ] **Verify dependencies**: Check all cells referenced in formulas exist
- [ ] **Test edge cases**: Include zero, negative, and very large values
- [ ] **OpenXML sanity**: Confirm ZIP/XML clean and no suspicious formulas with `scripts/check_xlsx_integrity.py`

### Interpreting scripts/recalc.py Output
The script returns JSON with error details:
```json
{
  "status": "success",           // or "errors_found"
  "total_errors": 0,              // Total error count
  "total_formulas": 42,           // Number of formulas in file
  "error_summary": {              // Only present if errors found
    "#REF!": {
      "count": 2,
      "locations": ["Sheet1!B5", "Sheet1!C10"]
    }
  }
}
```

## Best Practices

### Library Selection
- **pandas**: Best for data analysis, bulk operations, and simple data export
- **openpyxl**: Best for complex formatting, formulas, and Excel-specific features

### Working with openpyxl
- Cell indices are 1-based (row=1, column=1 refers to cell A1)
- Use `data_only=True` to read calculated values: `load_workbook('file.xlsx', data_only=True)`
- **Warning**: If opened with `data_only=True` and saved, formulas are replaced with values and permanently lost
- For large files: Use `read_only=True` for reading or `write_only=True` for writing
- Formulas are preserved but not evaluated - use scripts/recalc.py to update values

### Working with pandas
- Specify data types to avoid inference issues: `pd.read_excel('file.xlsx', dtype={'id': str})`
- For large files, read specific columns: `pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
- Handle dates properly: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`

## Code Style Guidelines
**IMPORTANT**: When generating Python code for Excel operations:
- Write minimal, concise Python code without unnecessary comments
- Avoid verbose variable names and redundant operations
- Avoid unnecessary print statements

**For Excel files themselves**:
- Add comments to cells with complex formulas or important assumptions
- Document data sources for hardcoded values
- Include notes for key calculations and model sections
