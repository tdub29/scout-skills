# PrÃ¼ft, ob alle Phasen in task_plan.md abgeschlossen sind
# Immer mit Exit-Code 0 beenden â€” Status Ã¼ber stdout melden
# Wird vom Stop-Hook aufgerufen, um Aufgabenabschlussstatus zu melden

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files-de] task_plan.md nicht gefunden â€” keine aktive Planungssitzung.'
    exit 0
}

# Dateiinhalt lesen
$content = Get-Content $PlanFile -Raw

# Gesamtzahl der Phasen zÃ¤hlen
$TOTAL = ([regex]::Matches($content, "### Phase")).Count

# Zuerst **Status:** Format prÃ¼fen
$COMPLETE = ([regex]::Matches($content, "\*\*Status:\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*Status:\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*Status:\*\* pending")).Count

# Fallback: Wenn **Status:** nicht gefunden, [complete] Inline-Format prÃ¼fen
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# Status melden â€” immer mit Exit-Code 0 beenden, unvollstÃ¤ndige Aufgaben sind normaler Zustand
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files-de] Alle Phasen abgeschlossen (' + $COMPLETE + '/' + $TOTAL + '). Wenn der Benutzer zusÃ¤tzliche Arbeit hat, neue Phasen in task_plan.md hinzufÃ¼gen, bevor du beginnst.')
} else {
    Write-Host ('[planning-with-files-de] Aufgabe lÃ¤uft (' + $COMPLETE + '/' + $TOTAL + ' Phasen abgeschlossen). progress.md vor dem Stoppen aktualisieren.')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files-de] ' + $IN_PROGRESS + ' Phasen noch in Bearbeitung.')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files-de] ' + $PENDING + ' Phasen ausstehend.')
    }
}
exit 0
