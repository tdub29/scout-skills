---
name: sql-server-2025
description: SQL Server 2025 and SqlPackage 170.2.70 (October 2025) - Vector databases, AI integration, and latest features
---

## ðŸš¨ CRITICAL GUIDELINES

### Windows File Path Requirements

**MANDATORY: Always Use Backslashes on Windows for File Paths**

When using Edit or Write tools on Windows, you MUST use backslashes (`\`) in file paths, NOT forward slashes (`/`).

**Examples:**
- âŒ WRONG: `D:/repos/project/file.tsx`
- âœ… CORRECT: `D:\repos\project\file.tsx`

This applies to:
- Edit tool file_path parameter
- Write tool file_path parameter
- All file operations on Windows systems

### Documentation Guidelines

**NEVER create new documentation files unless explicitly requested by the user.**

- **Priority**: Update existing README.md files rather than creating new documentation
- **Repository cleanliness**: Keep repository root clean - only README.md unless user requests otherwise
- **Style**: Documentation should be concise, direct, and professional - avoid AI-generated tone
- **User preference**: Only create additional .md files when user specifically asks for documentation

---

# SQL Server 2025 & SqlPackage 170.2.70 Support

## Overview

**SQL Server 2025** is the enterprise AI-ready database with native vector database capabilities, built-in AI model integration, and semantic search from ground to cloud.

**SqlPackage 170.2.70** (October 14, 2025) - Latest production release with full SQL Server 2025 support, data virtualization, and parquet file enhancements.

## SqlPackage and Build Tooling

SqlPackage 170.x releases (latest 170.2.70) and commands, ScriptDom 170.0.64, Microsoft.Build.Sql 2.0.0 GA with the Sql160 provider workaround, Visual Studio 2022 requirement, and SQL Server 2025 release status are in `references/sqlpackage-and-build-tooling.md`.
## SQL Server 2025 New Features

Vector database and DiskANN, AI model integration, optimized locking, Fabric mirroring, native JSON, RegEx, REST API integration, OPPO, Entra managed identities and information protection are covered in `references/new-features.md`.
## Deployment, CI/CD and Fabric

SqlPackage and MSBuild deployment, GitHub Actions and Azure DevOps pipelines, diagnostics and Fabric warehouse support are in `references/deployment-cicd-and-fabric.md`.
## Best Practices for SQL Server 2025

1. **Use Target Platform Specification:**
```xml
<PropertyGroup>
  <TargetPlatform>SqlServer2025</TargetPlatform>
</PropertyGroup>
```

2. **Test Vector Operations:**
```sql
-- Verify vector support
SELECT SERVERPROPERTY('IsVectorSupported') AS VectorSupport;
```

3. **Monitor AI Model Performance:**
```sql
-- Track model execution
SELECT
    model_name,
    AVG(execution_time_ms) AS AvgExecutionTime,
    COUNT(*) AS ExecutionCount
FROM sys.dm_exec_external_model_stats
GROUP BY model_name;
```

4. **Implement Sensitivity Classification:**
```sql
-- Classify all PII columns
ADD SENSITIVITY CLASSIFICATION TO dbo.Customers.Email
WITH (LABEL = 'Confidential - GDPR', INFORMATION_TYPE = 'Email');
```

## Resources

- [SQL Server 2025 Preview](https://aka.ms/sqlserver2025)
- [SqlPackage Documentation](https://learn.microsoft.com/sql/tools/sqlpackage/)
- [SDK-Style Projects](https://learn.microsoft.com/sql/tools/sql-database-projects/concepts/sdk-style-projects)
- [Vector Database](https://learn.microsoft.com/sql/relational-databases/vectors/)

## References

- `references/sqlpackage-and-build-tooling.md`: load for SqlPackage 170.x versions and commands, ScriptDom, Microsoft.Build.Sql SDK projects, Visual Studio support or SQL Server 2025 release status
- `references/new-features.md`: load for a specific 2025 feature: vectors and DiskANN, AI models, optimized locking, Fabric mirroring, JSON, RegEx, REST, OPPO, Entra managed identities, information protection
- `references/deployment-cicd-and-fabric.md`: load when deploying a dacpac, building CI/CD pipelines (GitHub Actions, Azure DevOps), enabling SqlPackage diagnostics or targeting Fabric
