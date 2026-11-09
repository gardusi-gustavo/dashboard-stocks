#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/database/data/stocks"
python3 - "$tmp/database/data/stocks/2026-11-08.json" <<'PY'
import json, sys
json.dump({"schema": 1, "domain": "stocks", "date": "2026-11-08",
           "generated_at": "2026-11-09T02:07:47Z", "source": {"provider": "ci"}, "items": []},
          open(sys.argv[1], "w"), indent=2)
PY
python3 scripts/build.py --database "$tmp/database" --out "$tmp/dist"
test -s "$tmp/dist/index.html"
