#!/usr/bin/env bash
# Initialisiert Planungsdateien fÃ¼r eine neue Sitzung
# Verwendung: ./init-session.sh [Projektname]

set -e

PROJECT_NAME="${1:-projekt}"
DATE=$(date +%Y-%m-%d)

echo "Initialisiere Planungsdateien: $PROJECT_NAME"

# task_plan.md erstellen, wenn nicht vorhanden
if [ ! -f "task_plan.md" ]; then
    cat > task_plan.md << 'EOF'
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
EOF
    echo "task_plan.md erstellt"
else
    echo "task_plan.md existiert bereits, Ã¼berspringe"
fi

# findings.md erstellen, wenn nicht vorhanden
if [ ! -f "findings.md" ]; then
    cat > findings.md << 'EOF'
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
EOF
    echo "findings.md erstellt"
else
    echo "findings.md existiert bereits, Ã¼berspringe"
fi

# progress.md erstellen, wenn nicht vorhanden
if [ ! -f "progress.md" ]; then
    cat > progress.md << EOF
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
EOF
    echo "progress.md erstellt"
else
    echo "progress.md existiert bereits, Ã¼berspringe"
fi

echo ""
echo "Planungsdateien initialisiert!"
echo "Dateien: task_plan.md, findings.md, progress.md"
