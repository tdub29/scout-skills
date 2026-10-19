---
name: te2-cli
version: 26.20
description: CLI syntax reference for Tabular Editor 2 (TabularEditor.exe); deployment, scripting, BPA analysis, and CI/CD integration. Automatically invoke when the user mentions "TabularEditor.exe", TE2 CLI flags (-D, -S, -A, -B, -TMDL, -O, -C), or asks to "deploy a model via CLI", "set up CI/CD for Power BI", "automate model deployment", "run BPA from command line", "save model as TMDL".
---

# Tabular Editor 2 CLI

Command-line interface for Tabular Editor 2 (TE2). This skill covers the `TabularEditor.exe` executable; TE3 has its own CLI and is a separate product.

## Installation

### Tabular Editor 2 (Free)
- Download: https://github.com/TabularEditor/TabularEditor/releases
- Extract to preferred location or use Chocolatey: `choco install tabulareditor2`

## Executable

`TabularEditor.exe` -- free, Windows-only. For Mac/Linux, run via a Windows VM or container.

## Connection Sources

### Local Files
```bash
# model.bim (JSON format)
TabularEditor.exe Model.bim

# TMDL folder
TabularEditor.exe definition/

# PBIP project
TabularEditor.exe MyReport.pbip
```

### Remote XMLA Endpoints
```bash
# Analysis Services
TabularEditor.exe "localhost\tabular" "AdventureWorks"

# Power BI Premium/Fabric
TabularEditor.exe "powerbi://api.powerbi.com/v1.0/myorg/WorkspaceName" "ModelName"
```

### Power BI Desktop
```bash
# Auto-detect running instance
TabularEditor.exe localhost:PORT DatabaseName
```
Note: Find the port in PBIDesktop diagnostic files or use tools like DAX Studio.

## Command-Line Reference

### Basic Syntax
```bash
TabularEditor.exe <source> [options]
```

### Script Execution
```bash
# Inline C# script
TabularEditor.exe Model.bim -S "Info(Model.Name);"

# Script file
TabularEditor.exe Model.bim -S script.csx

# Multiple scripts (executed in order)
TabularEditor.exe Model.bim -S script1.csx -S script2.csx
```

### Deployment
```bash
# Deploy to XMLA endpoint
TabularEditor.exe Model.bim -D "server" "database"

# Deploy with options
TabularEditor.exe Model.bim -D "server" "database" -O -C -P -R -M -E -V -W
```

## Authentication

For authentication methods (Windows, Service Principal, Interactive) and CI/CD integration (Azure DevOps, GitHub Actions), see **`references/auth-and-cicd.md`**.

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Any error-level output (script error, deployment failure, BPA violations at severity >= 3) |

## File Formats

### Input Formats
- `model.bim` - Tabular JSON (legacy)
- `definition/` - TMDL folder (modern)
- `*.pbip` - Power BI Project (TE3)

### Output Formats

| Flag | Format | Description |
|------|--------|-------------|
| `-B` | `.bim` | Tabular JSON |
| `-TMDL` | folder | TMDL |
| `-F` | folder | Legacy folder structure |

## Troubleshooting

For common errors (database not found, authentication failed, script execution failed), see **`references/auth-and-cicd.md`**.

## References

To retrieve current XMLA and deployment docs, use `microsoft_docs_search` + `microsoft_docs_fetch` (MCP) if available, otherwise `mslearn search` + `mslearn fetch` (CLI). Search based on the user's request and run multiple searches as needed to ensure sufficient context before proceeding.

- [TE2 CLI Documentation](https://docs.tabulareditor.com/features/Command-line-Options.html)
- [XMLA Endpoints](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)
- `references/command_flags.md`: load for deployment option flags, save-output flags, BPA and schema-check commands
- `references/common_operations.md`: load for ready-made deploy, script-and-save, BPA, refresh and export commands
- `references/quick_reference_card.md`: load for a one-screen flag cheat sheet
- `references/auth-and-cicd.md`: load for authentication methods, CI/CD pipelines and troubleshooting
