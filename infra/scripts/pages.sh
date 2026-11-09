#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
DATABASE_DIR="${DATABASE_DIR:-$ROOT/../database}"
OUT_DIR="${OUT_DIR:-$ROOT/dist}"
python3 scripts/build.py --database "$DATABASE_DIR" --out "$OUT_DIR"
