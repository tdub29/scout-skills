# Initialisiert Planungsdateien fÃ¼r eine neue Sitzung
# Verwendung: .\init-session.ps1 [Projektname]

param(
    [string]$ProjectName = "projekt"
)

$DATE = Get-Date -Format "yyyy-MM-dd"

Write-Host "Initialisiere Planungsdateien: $ProjectName"

# task_plan.md erstellen, wenn nicht vorhanden
if (-not (Test-Path "task_plan.md")) {
    @"
# Aufgabenplan: [Kurze Beschreibung]

## Ziel
[Ein-Satz-Beschreibung des Endzustands]

## Aktuelle Phase
Phase 1

## Phasen

### Phase 1: Anforderungen & Entdeckung
- [ ] Benutzerabsicht verstehen
- [ ] EinschrÃ¤nkungen und Anforderungen klÃ¤ren
- [ ] Erkenntnisse in findings.md dokumentieren
- **Status:** in_progress

### Phase 2: Planung & Struktur
- [ ] Technischen Ansatz festlegen
- [ ] Projektstruktur bei Bedarf erstellen
- **Status:** pending

### Phase 3: Implementierung
- [ ] Schrittweise gemÃ¤ÃŸ Plan ausfÃ¼hren
- [ ] Code zuerst in Dateien schreiben, dann ausfÃ¼hren
- **Status:** pending

### Phase 4: Test & Validierung
- [ ] Alle Anforderungen geprÃ¼ft
- [ ] Testergebnisse in progress.md dokumentieren
- **Status:** pending

### Phase 5: Auslieferung
- [ ] Alle Ausgabedateien geprÃ¼ft
- [ ] An Benutzer ausgeliefert
- **Status:** pending

## Getroffene Entscheidungen
| Entscheidung | BegrÃ¼ndung |
|------|------|

## Aufgetretene Fehler
| Fehler | LÃ¶sung |
|------|---------|
"@ | Out-File -FilePath "task_plan.md" -Encoding UTF8
    Write-Host "task_plan.md erstellt"
} else {
    Write-Host "task_plan.md existiert bereits, Ã¼berspringe"
}

# findings.md erstellen, wenn nicht vorhanden
if (-not (Test-Path "findings.md")) {
    @"
# Erkenntnisse & Entscheidungen

## Anforderungen
-

## Forschungsergebnisse
-

## Technische Entscheidungen
| Entscheidung | BegrÃ¼ndung |
|------|------|

## Aufgetretene Probleme
| Problem | LÃ¶sung |
|------|---------|

## Ressourcen
-
"@ | Out-File -FilePath "findings.md" -Encoding UTF8
    Write-Host "findings.md erstellt"
} else {
    Write-Host "findings.md existiert bereits, Ã¼berspringe"
}

# progress.md erstellen, wenn nicht vorhanden
if (-not (Test-Path "progress.md")) {
    @"
# Fortschrittsprotokoll

## Sitzung: $DATE

### Aktueller Status
- **Phase:** 1 - Anforderungen & Entdeckung
- **Startzeit:** $DATE

### AusgefÃ¼hrte Aktionen
-

### Testergebnisse
| Test | Erwartet | TatsÃ¤chlich | Status |
|------|---------|---------|------|

### Fehler
| Fehler | LÃ¶sung |
|------|---------|
"@ | Out-File -FilePath "progress.md" -Encoding UTF8
    Write-Host "progress.md erstellt"
} else {
    Write-Host "progress.md existiert bereits, Ã¼berspringe"
}

Write-Host ""
Write-Host "Planungsdateien initialisiert!"
Write-Host "Dateien: task_plan.md, findings.md, progress.md"
