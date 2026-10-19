# TE2 Common Operations

## Common Operations

### 1. Deploy Local Model to Service
```bash
TabularEditor.exe Model.bim ^
    -D "powerbi://api.powerbi.com/v1.0/myorg/Workspace" "SemanticModel" ^
    -O -C
```

### 2. Run Script and Save
```bash
TabularEditor.exe Model.bim -S format-dax.csx -B Model.bim
```

### 3. Run BPA Analysis
```bash
TabularEditor.exe Model.bim ^
    -A https://raw.githubusercontent.com/microsoft/Analysis-Services/master/BestPracticeRules/BPARules.json ^
    -V
```

### 4. Refresh Model Data
```bash
TabularEditor.exe "server" "database" ^
    -S "Model.RequestRefresh(RefreshType.Full);" ^
    -D "server" "database"
```

### 5. Export Model from Service
```bash
TabularEditor.exe "powerbi://api.powerbi.com/v1.0/myorg/Workspace" "Model" ^
    -TMDL output/definition
```
