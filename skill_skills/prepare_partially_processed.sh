#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$SCRIPT_DIR/scan_skills.py"

if [ ! -f "$PY" ]; then
  echo "Missing scanner: $PY" >&2
  exit 1
fi

if [ -n "$TARGET" ]; then
  DIR="$TARGET"
else
  # fallback candidates (tolerant of common typos)
  ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
  for c in $SCRIPT_DIR; do
    if [ -d "$ROOT_DIR/$c" ]; then
      DIR="$ROOT_DIR/$c"
      break
    fi
  done
  done
fi

if [ -z "${DIR:-}" ]; then
  echo "No target directory found. Provide as first arg." >&2
  exit 1
fi

cd "$DIR"
echo "Scanning .md files in: $(pwd)"
python3 "$PY" --dir "$(pwd)" --output "skills.json"
echo "Done. Outputs: skills.json, summary.json"
