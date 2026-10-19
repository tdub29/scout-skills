#!/usr/bin/env sh
# Find the biggest code files in a repo (god-file candidates) by line count.
# Usage: sh scripts/find-god-files.sh [root] [min-lines] [top]
#   root      default .        min-lines default 800     top default 30
# ponytail: line-count proxy for "too big"; add complexity metrics only if it
# ever picks the wrong target.
set -eu

ROOT="${1:-.}"
MIN="${2:-800}"
TOP="${3:-30}"

find "$ROOT" \
  \( -name node_modules -o -name .venv -o -name venv -o -name .git \
     -o -name repos -o -name dist -o -name build -o -name .next \
     -o -name vendor -o -name __pycache__ -o -name .wrangler -o -name .cache \
     -o -name .agents -o -name .claude -o -name .cursor -o -name .codex -o -name skills \
     -o -name generated \) -prune \
  -o -type f \( -name '*.js' -o -name '*.jsx' -o -name '*.ts' -o -name '*.tsx' \
     -o -name '*.py' -o -name '*.rb' -o -name '*.html' -o -name '*.vue' \
     -o -name '*.svelte' -o -name '*.css' -o -name '*.php' -o -name '*.go' \
     -o -name '*.java' -o -name '*.cs' \) -print 2>/dev/null \
| while IFS= read -r f; do
    n=$(wc -l < "$f" 2>/dev/null || echo 0)
    [ "$n" -ge "$MIN" ] && printf '%s\t%s\n' "$n" "$f"
  done \
| sort -rn | head -n "$TOP"
