# TE2 Command Flags

### Deployment Options

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-O` | `-OVERWRITE` | Overwrite existing database |
| `-C` | `-CONNECTIONS` | Deploy/overwrite data sources (supports connection string placeholder substitution) |
| `-P` | `-PARTITIONS` | Deploy/overwrite existing table partitions |
| `-R` | `-ROLES` | Deploy roles |
| `-M` | `-MEMBERS` | Deploy role members |
| `-S` | `-SHARED` | Deploy shared expressions (within `-D` context; note: `-S` also means script outside `-D`) |
| `-E` | `-ERR` | Return non-zero exit code if AS returns error messages after deployment |
| `-V` | `-VSTS` | Output Azure DevOps logging commands |
| `-W` | `-WARN` | Output warnings for unprocessed objects |
| `-F` | `-FULL` | Full deployment (equivalent to `-O -C -P -S -R -M`) |
| `-X` | `-XMLA` | Generate XMLA/TMSL script instead of deploying |
| `-L` | `-LOGIN` | Disable integrated security for deployment |
| `-Y` | `-SKIPPOLICY` | Skip incremental refresh policy partitions |

### Save Output
```bash
# Save to model.bim
TabularEditor.exe Model.bim -S script.csx -B Output.bim

# Save to TMDL folder
TabularEditor.exe Model.bim -S script.csx -TMDL output/

# Save to legacy folder structure
TabularEditor.exe Model.bim -S script.csx -F output/
```

### Best Practice Analyzer
```bash
# Run BPA rules
TabularEditor.exe Model.bim -A rules.json

# Run BPA with Azure DevOps logging output
TabularEditor.exe Model.bim -A rules.json -V

# Run BPA with GitHub Actions logging output
TabularEditor.exe Model.bim -A rules.json -G

# Analyze excluding rules embedded in model annotations
TabularEditor.exe Model.bim -AX rules.json
```

### Schema Check
```bash
# Validate data source schemas against the model
TabularEditor.exe Model.bim -SC
```
