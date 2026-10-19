# Verificar si todas las fases en task_plan.md estÃ¡n completas
# Siempre salir con cÃ³digo 0 â€” usar stdout para informar el estado
# Llamado por el hook Stop para informar el estado de finalizaciÃ³n de la tarea

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files-es] No se encontrÃ³ task_plan.md â€” no hay sesiÃ³n de planificaciÃ³n activa.'
    exit 0
}

# Leer contenido del archivo
$content = Get-Content $PlanFile -Raw

# Contar el total de fases
$TOTAL = ([regex]::Matches($content, "### Phase")).Count

# Primero verificar formato **Estado:**
$COMPLETE = ([regex]::Matches($content, "\*\*Estado:\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*Estado:\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*Estado:\*\* pending")).Count

# Alternativa: si no se encontrÃ³ **Estado:** verificar formato en lÃ­nea [complete]
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# Informar estado â€” siempre salir con cÃ³digo 0, tareas incompletas son estado normal
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files-es] Todas las fases completadas (' + $COMPLETE + '/' + $TOTAL + '). Si el usuario tiene trabajo adicional, aÃ±adir fases en task_plan.md antes de comenzar.')
} else {
    Write-Host ('[planning-with-files-es] Tarea en progreso (' + $COMPLETE + '/' + $TOTAL + ' fases completadas). Actualizar progress.md antes de detenerse.')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files-es] ' + $IN_PROGRESS + ' fases aÃºn en progreso.')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files-es] ' + $PENDING + ' fases pendientes.')
    }
}
exit 0
