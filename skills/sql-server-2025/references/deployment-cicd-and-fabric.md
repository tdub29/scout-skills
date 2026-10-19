# Deployment, CI/CD and Fabric

## Contents

- [Deployment to SQL Server 2025](#deployment-to-sql-server-2025)
- [CI/CD Best Practices 2025](#cicd-best-practices-2025)
- [New SqlPackage Diagnostic Features](#new-sqlpackage-diagnostic-features)
- [Microsoft Fabric Data Warehouse Support](#microsoft-fabric-data-warehouse-support)

## Deployment to SQL Server 2025

### Using SqlPackage

```bash
# Publish with 2025 features
sqlpackage /Action:Publish \
  /SourceFile:Database.dacpac \
  /TargetConnectionString:"Server=tcp:server2025.database.windows.net;Database=MyDb;Authentication=ActiveDirectoryManagedIdentity;" \
  /p:BlockOnPossibleDataLoss=True \
  /p:IncludeCompositeObjects=True \
  /p:DropObjectsNotInSource=False \
  /p:DoNotDropObjectTypes=Users;RoleMembership \
  /p:GenerateSmartDefaults=True \
  /DiagnosticsFile:deploy.log
```

### Using MSBuild

```xml
<!-- Database.publish.xml -->
<Project>
  <PropertyGroup>
    <TargetConnectionString>Server=tcp:server2025.database.windows.net;Database=MyDb;Authentication=ActiveDirectoryManagedIdentity;</TargetConnectionString>
    <BlockOnPossibleDataLoss>True</BlockOnPossibleDataLoss>
    <TargetDatabaseName>MyDatabase</TargetDatabaseName>
    <ProfileVersionNumber>1</ProfileVersionNumber>
  </PropertyGroup>

  <ItemGroup>
    <SqlCmdVariable Include="Environment">
      <Value>Production</Value>
    </SqlCmdVariable>
  </ItemGroup>
</Project>
```

```bash
# Deploy using MSBuild
msbuild Database.sqlproj \
  /t:Publish \
  /p:PublishProfile=Database.publish.xml \
  /p:TargetPlatform=SqlServer2025
```

## CI/CD Best Practices 2025

### Key Principles

**State-Based Deployment (Recommended):**
- Source code represents current database state
- All objects (procedures, tables, triggers, views) in separate .sql files
- SqlPackage generates incremental scripts automatically
- Preferred over migration-based approaches

**Testing & Quality:**
- **tSQLt** - Unit testing for SQL Server stored procedures and functions
- Tests produce machine-readable results
- Abort pipeline on test failure with immediate notifications
- Never continue deployment if tests fail

**Security:**
- **Windows Authentication preferred** for CI/CD (avoid plain text passwords)
- Never commit credentials to source control
- Use Azure Key Vault or GitHub Secrets for connection strings

**Version Control:**
- All database objects in source control
- Test scripts versioned and executed in Build step
- Require comments on check-ins
- Configure custom check-in policies

### GitHub Actions (2025 Pattern)

```yaml
name: Deploy to SQL Server 2025

on:
  push:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Setup .NET 8
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: '8.0.x'

    - name: Install SqlPackage 170.2.70
      run: dotnet tool install -g Microsoft.SqlPackage --version 170.2.70

    - name: Build DACPAC
      run: dotnet build Database.sqlproj -c Release

    - name: Run tSQLt Unit Tests
      run: |
        # Run unit tests and capture results
        # Abort if tests fail
        echo "Running tSQLt unit tests..."
        # Add your tSQLt test execution here

    - name: Generate Deployment Report
      run: |
        sqlpackage /Action:DeployReport \
          /SourceFile:bin/Release/Database.dacpac \
          /TargetConnectionString:"${{ secrets.SQL_CONNECTION_STRING }}" \
          /OutputPath:deploy-report.xml \
          /p:BlockOnPossibleDataLoss=True

    - name: Publish to SQL Server 2025
      run: |
        sqlpackage /Action:Publish \
          /SourceFile:bin/Release/Database.dacpac \
          /TargetConnectionString:"${{ secrets.SQL_CONNECTION_STRING }}" \
          /p:TargetPlatform=SqlServer2025 \
          /p:BlockOnPossibleDataLoss=True \
          /DiagnosticsFile:publish.log \
          /DiagnosticsLevel:Verbose

    - name: Upload Artifacts
      if: always()
      uses: actions/upload-artifact@v4
      with:
        name: deployment-logs
        path: |
          publish.log
          deploy-report.xml
```

### Azure DevOps

```yaml
trigger:
- main

pool:
  vmImage: 'windows-2022'

steps:
- task: MSBuild@1
  displayName: 'Build Database Project'
  inputs:
    solution: 'Database.sqlproj'
    configuration: 'Release'

- task: SqlAzureDacpacDeployment@1
  displayName: 'Deploy to SQL Server 2025'
  inputs:
    azureSubscription: 'Azure Subscription'
    authenticationType: 'servicePrincipal'
    serverName: 'server2025.database.windows.net'
    databaseName: 'MyDatabase'
    deployType: 'DacpacTask'
    deploymentAction: 'Publish'
    dacpacFile: '$(Build.SourcesDirectory)/bin/Release/Database.dacpac'
    additionalArguments: '/p:TargetPlatform=SqlServer2025'
```

## New SqlPackage Diagnostic Features

```bash
# Enable detailed diagnostics
sqlpackage /Action:Publish \
  /SourceFile:Database.dacpac \
  /TargetServerName:server2025.database.windows.net \
  /TargetDatabaseName:MyDatabase \
  /DiagnosticsLevel:Verbose \
  /DiagnosticPackageFile:diagnostics.zip

# Creates diagnostics.zip containing:
# - Deployment logs
# - Performance metrics
# - Error details
# - Schema comparison results
```

## Microsoft Fabric Data Warehouse Support

**New in SqlPackage 162.5+:** Full support for SQL database in Microsoft Fabric.

**Fabric Deployment:**
```bash
# Deploy to Fabric Warehouse
sqlpackage /Action:Publish \
  /SourceFile:Warehouse.dacpac \
  /TargetConnectionString:"Server=tcp:myworkspace.datawarehouse.fabric.microsoft.com;Database=mywarehouse;Authentication=ActiveDirectoryInteractive;" \
  /p:DatabaseEdition=Fabric \
  /p:DatabaseServiceObjective=SqlDbFabricDatabaseSchemaProvider

# Extract from Fabric
sqlpackage /Action:Extract \
  /SourceConnectionString:"Server=tcp:myworkspace.datawarehouse.fabric.microsoft.com;Database=mywarehouse;Authentication=ActiveDirectoryInteractive;" \
  /TargetFile:Fabric.dacpac

# New permission: ALTER ANY EXTERNAL MIRROR (Fabric-specific)
GRANT ALTER ANY EXTERNAL MIRROR TO [FabricAdmin];
```
