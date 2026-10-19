#requires -Version 5.1
<#
.SYNOPSIS
  Find the biggest code files in a repo (god-file candidates) by line count.
.EXAMPLE
  pwsh scripts/find-god-files.ps1 -Root . -Min 800 -Top 30
# ponytail: line-count is a good-enough proxy for "too big". Not cyclomatic
# complexity; add that only if line-count ever picks the wrong targets.
#>
param(
  [string]$Root = ".",
  [int]$Min = 800,      # ignore files under this many lines
  [int]$Top = 30,       # show this many
  [string[]]$Ext = @("js","jsx","ts","tsx","py","rb","html","vue","svelte","css","php","go","java","cs")
)

$prune = @("node_modules",".venv","venv",".git","repos","dist","build",".next","vendor","__pycache__",".wrangler",".cache",".agents",".claude",".cursor",".codex","skills","generated")
$extSet = @{}; foreach ($e in $Ext) { $extSet["." + $e.ToLower()] = $true }

$results = Get-ChildItem -Path $Root -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
  $extSet.ContainsKey($_.Extension.ToLower()) -and
  ($_.FullName -split '[\\/]' | Where-Object { $prune -contains $_ }).Count -eq 0
} | ForEach-Object {
  $n = 0
  try { $n = (Get-Content -LiteralPath $_.FullName -ErrorAction Stop | Measure-Object -Line).Lines } catch {}
  if ($n -ge $Min) { [pscustomobject]@{ Lines = $n; Path = (Resolve-Path -Relative $_.FullName) } }
} | Sort-Object Lines -Descending | Select-Object -First $Top

if (-not $results) { Write-Host "No files >= $Min lines under $Root (checked: $($Ext -join ', '))."; exit 0 }
$results | Format-Table -AutoSize
Write-Host ""
Write-Host "Top candidate: $($results[0].Path) ($($results[0].Lines) lines). Point refactor-god-file at it."
