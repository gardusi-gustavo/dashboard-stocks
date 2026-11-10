#!/usr/bin/env python3
"""Build the static dashboard from a checked-out database."""
from __future__ import annotations

import argparse
import html
import json
import shutil
from pathlib import Path

DOMAIN = "stocks"
TITLE = "Stocks"


def latest(database: Path, domain: str, date: str | None = None) -> Path:
    root = database / "data" / domain
    files = sorted(root.glob("*.json"))
    if not files:
        raise SystemExit(f"no data for {domain} under {root}")
    if date:
        match = root / f"{date}.json"
        if not match.exists():
            raise SystemExit(f"missing {match}")
        return match
    return files[-1]


def render(dataset: dict) -> str:
    items = dataset.get("items")
    if items is None:
        items = []
        for collection, entries in (dataset.get("collections") or {}).items():
            items.extend(entries if isinstance(entries, list) else [entries])
    rows = "".join(
        f"<li><code>{html.escape(str(item.get('title') or item.get('name') or item.get('id') or 'item'))}</code></li>"
        for item in items[:500]
    ) or "<li>No records yet.</li>"
    payload = html.escape(json.dumps(dataset, ensure_ascii=False)[:200000])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<style>body{{font-family:system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1rem}}code{{background:#eee;padding:.1rem .3rem}}</style>
</head><body>
<h1>{TITLE}</h1>
<p>Built from <code>gardusi-gustavo/database-stocks</code>. Date: <code>{html.escape(str(dataset.get("date", "")))}</code>.</p>
<h2>Records</h2><ul>{rows}</ul>
<script id="dataset" type="application/json">{payload}</script>
</body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--database", required=True)
    ap.add_argument("--out", default="dist")
    ap.add_argument("--date")
    args = ap.parse_args()
    database = Path(args.database).resolve()
    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    source = latest(database, DOMAIN, args.date)
    dataset = json.loads(source.read_text(encoding="utf-8"))
    (out / "data").mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, out / "data" / f"{DOMAIN}.json")
    (out / "index.html").write_text(render(dataset), encoding="utf-8")
    front = Path(__file__).resolve().parent.parent / "src/frontend"
    if front.is_dir():
        for src in front.rglob("*"):
            if src.is_file():
                dest = out / src.relative_to(front)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
    print(f"built {out} from {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
