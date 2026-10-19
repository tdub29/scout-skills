# Inicializar archivos de planificaciÃ³n para una nueva sesiÃ³n
# Uso: .\init-session.ps1 [nombre_del_proyecto]

param(
    [string]$ProjectName = "project"
)

$DATE = Get-Date -Format "yyyy-MM-dd"

Write-Host "Inicializando archivos de planificaciÃ³n: $ProjectName"

# Crear task_plan.md si no existe
if (-not (Test-Path "task_plan.md")) {
    @"
# Plan de Tarea: [descripciÃ³n breve]

## Objetivo
[describir el estado final en una frase]

## Fase Actual
Fase 1

## Fases

### Fase 1: Requisitos y Descubrimiento
- [ ] Comprender la intenciÃ³n del usuario
- [ ] Identificar restricciones y requisitos
- [ ] Documentar hallazgos en findings.md
- **Status:** in_progress

### Fase 2: PlanificaciÃ³n y Estructura
- [ ] Definir enfoque tÃ©cnico
- [ ] Crear estructura de proyecto si es necesario
- **Status:** pending

### Fase 3: ImplementaciÃ³n
- [ ] Ejecutar paso a paso segÃºn el plan
- [ ] Escribir cÃ³digo en archivos antes de ejecutar
- **Status:** pending

### Fase 4: Pruebas y ValidaciÃ³n
- [ ] Verificar que todos los requisitos estÃ¡n satisfechos
- [ ] Documentar resultados de pruebas en progress.md
- **Status:** pending

### Fase 5: Entrega
- [ ] Revisar todos los archivos de salida
- [ ] Entregar al usuario
- **Status:** pending

## Decisiones Tomadas
| DecisiÃ³n | JustificaciÃ³n |
|------|------|

## Errores Encontrados
| Error | SoluciÃ³n |
|------|---------|
"@ | Out-File -FilePath "task_plan.md" -Encoding UTF8
    Write-Host "Creado task_plan.md"
} else {
    Write-Host "task_plan.md ya existe, omitiendo"
}

# Crear findings.md si no existe
if (-not (Test-Path "findings.md")) {
    @"
# Hallazgos y Decisiones

## Requisitos
-

## Hallazgos de InvestigaciÃ³n
-

## Decisiones TÃ©cnicas
| DecisiÃ³n | JustificaciÃ³n |
|------|------|

## Problemas Encontrados
| Problema | SoluciÃ³n |
|------|---------|

## Recursos
-
"@ | Out-File -FilePath "findings.md" -Encoding UTF8
    Write-Host "Creado findings.md"
} else {
    Write-Host "findings.md ya existe, omitiendo"
}

# Crear progress.md si no existe
if (-not (Test-Path "progress.md")) {
    @"
# Registro de Progreso

## SesiÃ³n: $DATE

### Estado Actual
- **Fase:** 1 - Requisitos y Descubrimiento
- **Inicio:** $DATE

### Acciones Realizadas
-

### Resultados de Pruebas
| Prueba | Resultado esperado | Resultado real | Estado |
|------|---------|---------|------|

### Errores
| Error | SoluciÃ³n |
|------|---------|
"@ | Out-File -FilePath "progress.md" -Encoding UTF8
    Write-Host "Creado progress.md"
} else {
    Write-Host "progress.md ya existe, omitiendo"
}

Write-Host ""
Write-Host "Â¡Archivos de planificaciÃ³n inicializados!"
Write-Host "Archivos: task_plan.md, findings.md, progress.md"
