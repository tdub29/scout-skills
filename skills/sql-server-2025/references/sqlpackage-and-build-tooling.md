# SqlPackage and Build Tooling

## Contents

- [SqlPackage 170.x Series (2025 Releases)](#sqlpackage-170x-series-2025-releases)
- [ScriptDom Version 170.0.64](#scriptdom-version-170064)
- [Microsoft.Build.Sql 2.0.0 GA (2025)](#microsoftbuildsql-200-ga-2025)
- [SQL Server 2025 Release Status](#sql-server-2025-release-status)

## SqlPackage 170.x Series (2025 Releases)

### Latest Version: 170.2.70 (October 14, 2025)

Three major 2025 releases:
- **170.2.70** - October 14, 2025 (Current)
- **170.1.61** - July 30, 2025 (Data virtualization)
- **170.0.94** - April 15, 2025 (SQL Server 2025 initial support)

### Key 2025 Features

**Data Virtualization (170.1.61+)**:
- Support for Azure SQL Database data virtualization objects
- Import/export/extract/publish operations for external data sources
- Parquet file support for Azure SQL Database with Azure Blob Storage
- Automatic fallback to BCP for CLR types and LOBs > 1MB

**New Data Types**:
- **VECTOR** - Up to 3,996 dimensions with half-precision (2-byte) floating-point
- **JSON** - Native JSON data type for Azure SQL Database

**New Permissions (170.0+)**:
- `ALTER ANY INFORMATION PROTECTION` - SQL Server 2025 & Azure SQL
- `ALTER ANY EXTERNAL MIRROR` - Azure SQL & SQL database in Fabric
- `CREATE/ALTER ANY EXTERNAL MODEL` - AI/ML model management

**Deployment Options**:
- `/p:IgnorePreDeployScript=True/False` - Skip pre-deployment scripts
- `/p:IgnorePostDeployScript=True/False` - Skip post-deployment scripts

### SqlPackage Commands

```bash
# Publish to SQL Server 2025
sqlpackage /Action:Publish \
  /SourceFile:Database.dacpac \
  /TargetServerName:server2025.database.windows.net \
  /TargetDatabaseName:MyDatabase \
  /TargetDatabaseEdition:Premium \
  /p:TargetPlatform=SqlServer2025  # New target platform

# Extract from SQL Server 2025
sqlpackage /Action:Extract \
  /SourceServerName:server2025.database.windows.net \
  /SourceDatabaseName:MyDatabase \
  /TargetFile:Database.dacpac \
  /p:ExtractAllTableData=False \
  /p:VerifyExtraction=True

# Export with SQL Server 2025 features
sqlpackage /Action:Export \
  /SourceServerName:server2025.database.windows.net \
  /SourceDatabaseName:MyDatabase \
  /TargetFile:Database.bacpac
```

## ScriptDom Version 170.0.64

New ScriptDom version for SQL Server 2025 syntax parsing:

```csharp
// Package: Microsoft.SqlServer.TransactSql.ScriptDom 170.0.64

using Microsoft.SqlServer.TransactSql.ScriptDom;

// Parse SQL Server 2025 syntax
var parser = new TSql170Parser(true);
IList<ParseError> errors;
var fragment = parser.Parse(new StringReader(sql), out errors);

// Supports SQL Server 2025 new T-SQL features
```

## Microsoft.Build.Sql 2.0.0 GA (2025)

**MAJOR MILESTONE:** Microsoft.Build.Sql SDK entered General Availability in 2025!

### Latest Version: 2.0.0 (Production Ready)

**Breaking Change from Preview:**
- SDK is now production-ready and recommended for all new database projects
- No longer in preview status
- Full cross-platform support (Windows/Linux/macOS)
- Requires .NET 8+ (was .NET 6+ in preview)

### SQL Server 2025 Support

**Current Status:** SQL Server 2025 target platform support coming in future Microsoft.Build.Sql release (post-2.0.0).

**Workaround for SDK-Style Projects:**
```xml
<!-- Database.sqlproj (SDK-style with SQL Server 2025 compatibility) -->
<Project Sdk="Microsoft.Build.Sql/2.0.0">
  <PropertyGroup>
    <Name>MyDatabase</Name>
    <!-- Use SQL Server 2022 (160) provider until 2025 provider available -->
    <DSP>Microsoft.Data.Tools.Schema.Sql.Sql160DatabaseSchemaProvider</DSP>
    <TargetFramework>net8.0</TargetFramework>
    <SqlServerVersion>Sql160</SqlServerVersion>

    <!-- SQL Server 2025 features will still work in runtime database -->
    <!-- Only build-time validation uses Sql160 provider -->
  </PropertyGroup>

  <ItemGroup>
    <Folder Include="Tables\" />
    <Folder Include="Views\" />
    <Folder Include="StoredProcedures\" />
  </ItemGroup>
</Project>
```

### Visual Studio 2022 Support

**Requirement:** Visual Studio 2022 version 17.12 or later for SDK-style SQL projects.

**Note:** Side-by-side installation with original SQL projects (legacy SSDT) is NOT supported.

## SQL Server 2025 Release Status

**Current Status**: SQL Server 2025 (17.x) is in **Release Candidate (RC1)** stage as of October 2025. Public preview began May 2025.

**Predicted GA Date**: November 12, 2025 (based on historical release patterns - SQL Server 2019: Nov 4, SQL Server 2022: Nov 16). Expected announcement at Microsoft Ignite conference (November 18-21, 2025).

**Not Yet Production**: SQL Server 2025 is not yet generally available. All features described are available in RC builds for testing purposes only.
