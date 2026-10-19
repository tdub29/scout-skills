#!/usr/bin/env bash
# Inicializar archivos de planificaciÃ³n para una nueva sesiÃ³n
# Uso: ./init-session.sh [nombre_del_proyecto]

set -e

PROJECT_NAME="${1:-project}"
DATE=$(date +%Y-%m-%d)

echo "Inicializando archivos de planificaciÃ³n: $PROJECT_NAME"

# Crear task_plan.md si no existe
if [ ! -f "task_plan.md" ]; then
    cat > task_plan.md << 'EOF'
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
EOF
    echo "Creado task_plan.md"
else
    echo "task_plan.md ya existe, omitiendo"
fi

# Crear findings.md si no existe
if [ ! -f "findings.md" ]; then
    cat > findings.md << 'EOF'
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
EOF
    echo "Creado findings.md"
else
    echo "findings.md ya existe, omitiendo"
fi

# Crear progress.md si no existe
if [ ! -f "progress.md" ]; then
    cat > progress.md << EOF
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
EOF
    echo "Creado progress.md"
else
    echo "progress.md ya existe, omitiendo"
fi

echo ""
echo "Â¡Archivos de planificaciÃ³n inicializados!"
echo "Archivos: task_plan.md, findings.md, progress.md"
