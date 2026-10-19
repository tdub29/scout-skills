# TE2 Quick Reference Card

## Quick Reference Card

```
+---------------------------------------------------------+
| TABULAR EDITOR CLI QUICK REFERENCE                      |
+---------------------------------------------------------+
| SOURCES                                                 |
|   Model.bim           Local JSON model                  |
|   definition/         TMDL folder                       |
|   "server" "db"       XMLA connection                   |
+---------------------------------------------------------+
| SCRIPTS                                                 |
|   -S "code"           Inline C# script                  |
|   -S file.csx         Script file                       |
+---------------------------------------------------------+
| DEPLOYMENT                                              |
|   -D "server" "db"    Deploy to target                  |
|   -O                  Overwrite existing                |
|   -C                  Create if not exists              |
+---------------------------------------------------------+
| OUTPUT                                                  |
|   -B output.bim       Save as JSON                      |
|   -TMDL folder/       Save as TMDL                      |
+---------------------------------------------------------+
| BPA                                                     |
|   -A rules.json       Run BPA analysis                  |
|   -G results.sarif    Output BPA results                |
+---------------------------------------------------------+
```
