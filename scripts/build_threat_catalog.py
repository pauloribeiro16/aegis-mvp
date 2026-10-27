#!/usr/bin/env python3
"""build_threat_catalog.py — ingest the local threat catalogs into baseline/THREATS.

Source: the KG repo's local catalogs (`~/Work/aegis-mvp-kg/catalogs/`, fetched
2026-10-05, no egress needed). Families and their status per ADR-012 + the
2026-10-27 ratification:

  CWE, CAPEC           core      — the only families a threat MUST cite from
  ATT&CK, D3FEND       consultive — adversary tactics / defensive countermeasures
  ATLAS, EMB3D         consultive — AI-system threats, embedded-device threats

Output: `baseline/THREATS/_index.json` — one entry per id with name +
description, family metadata, and the source manifest. This is the universe
guard T8 checks against: a threat id a Part 2 deliverable cites and the index
does not contain is a fabrication.

The write lands in `baseline/`, which AGENTS.md §3 keeps read-only — this
script is the ADR-012 governance pass, run deliberately, never as a side
effect of a stage. Re-runnable and idempotent.

Usage: python3 scripts/build_threat_catalog.py [--kg PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_KG = Path.home() / "Work" / "aegis-mvp-kg" / "catalogs"

FAMILIES = {
    "CWE": {"core": True, "prefix": "CWE-"},
    "CAPEC": {"core": True, "prefix": "CAPEC-"},
    "ATTACK": {"core": False, "prefix": "T"},
    "D3FEND": {"core": False, "prefix": "D3-"},
    "ATLAS": {"core": False, "prefix": "AML.T"},
    "EMB3D": {"core": False, "prefix": "TID-"},
}


def build(kg: Path) -> dict:
    manifest = json.loads((kg / "_MANIFEST.json").read_text(encoding="utf-8"))
    index: dict[str, dict] = {}
    families: dict[str, dict] = {}
    for family, meta in FAMILIES.items():
        entries = sorted(kg.glob(f"{family}/*.json"))
        ids = []
        for path in entries:
            try:
                blob = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"  [skip] {family}/{path.name}: {e}", file=sys.stderr)
                continue
            tid = blob.get("id") or path.stem
            index[tid] = {
                "family": family,
                "name": blob.get("name", ""),
                "description": (blob.get("description") or "")[:600],
            }
            ids.append(tid)
        declared = (manifest.get("catalogs") or {}).get(family, {}).get("entries")
        families[family] = {
            "core": meta["core"],
            "ids": ids,
            "count": len(ids),
            "manifest_count": declared,
            "url": (manifest.get("catalogs") or {}).get(family, {}).get("url"),
        }
        print(f"  {family}: {len(ids)} ids (manifest declares {declared})")
    return {
        "built": date.today().isoformat(),
        "source": str(kg),
        "source_manifest": {"fetched": manifest.get("fetched"), "advisory": manifest.get("advisory")},
        "families": families,
        "entries": index,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kg", type=Path, default=DEFAULT_KG, help="the catalogs dir")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not (args.kg / "_MANIFEST.json").is_file():
        print(f"FATAL: no _MANIFEST.json under {args.kg}", file=sys.stderr)
        return 2
    catalog = build(args.kg)
    total = len(catalog["entries"])
    core = sum(f["count"] for f in catalog["families"].values() if f["core"])
    print(f"total: {total} ids ({core} core)")
    if args.dry_run:
        return 0
    out = REPO / "baseline" / "THREATS"
    out.mkdir(parents=True, exist_ok=True)
    (out / "_index.json").write_text(
        json.dumps(catalog, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out / '_index.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
