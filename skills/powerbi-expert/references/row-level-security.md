# Row-Level Security (RLS)

**Role-Based Security:**
```dax
// Create role: Sales_USA
[Country] = "USA"

// Create role: Regional_Manager
[Region] = USERPRINCIPALNAME()

// Dynamic RLS using security table
// SecurityTable: Email | Region
[Region] IN
    CALCULATETABLE(
        VALUES(SecurityTable[Region]),
        SecurityTable[Email] = USERPRINCIPALNAME()
    )

// Manager hierarchy
// EmployeeTable: EmployeeID | ManagerID
VAR CurrentUser = USERPRINCIPALNAME()
VAR CurrentEmployeeID =
    LOOKUPVALUE(
        EmployeeTable[EmployeeID],
        EmployeeTable[Email], CurrentUser
    )
RETURN
    PATHCONTAINS(
        EmployeeTable[Path],
        CurrentEmployeeID
    )

// Multiple conditions (OR)
[Region] = "North" || [Region] = "South"

// Exclude admin users
[Region] = "North" ||
USERPRINCIPALNAME() = "admin@company.com"
```

**Object-Level Security:**
```dax
// Hide entire table from role
// Manage Roles -> Advanced -> Object-level security
// Table: SensitiveData -> Unchecked for standard users

// Hide specific columns using RLS
// Can't directly hide columns, but can obfuscate values
SensitiveColumn =
IF(
    USERPRINCIPALNAME() IN {"admin@company.com", "manager@company.com"},
    [ActualSensitiveColumn],
    BLANK()
)
```
