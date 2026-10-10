#!/usr/bin/env python3
"""aegis_pipeline.core.trace — call ledger and run manifest."""

from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Trace:
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.path = run_dir / "trace.jsonl"
        self.seq = self._max_seq()

    def _max_seq(self) -> int:
        if not self.path.exists():
            return 0
        last = 0
        for line in self.path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    last = max(last, int(json.loads(line).get("seq", 0)))
                except json.JSONDecodeError:
                    continue
        return last

    def next_seq(self) -> int:
        self.seq += 1
        return self.seq

    def append(self, record: dict) -> None:
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def update_manifest(run_dir: Path, **updates) -> dict:
    path = run_dir / "manifest.json"
    manifest: dict = {}
    if path.exists():
        manifest = json.loads(path.read_text(encoding="utf-8"))
    for key, value in updates.items():
        if key == "stage_history" and key in manifest and isinstance(manifest[key], list):
            manifest[key].append(value)
        else:
            manifest[key] = value
    manifest["updated"] = now_iso()
    path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    return manifest


def count_calls(run_dir: Path) -> int:
    path = run_dir / "trace.jsonl"
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
