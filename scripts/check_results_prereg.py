#!/usr/bin/env python3
"""Results-doc preregistration checker (read-only, report-only).

Enforces AGENTS.md §-2 rule 3: a results document must cite the preregistration
it ran under, and the cited version must exist in that preregistration.

Two checks:

  R-A  every ``docs/experiments/EXP*results*.md`` carries frontmatter fields
       ``prereg:`` (a path that resolves to a PREREG*.md file) and
       ``prereg_version:`` (a version string that appears in that file).
  R-B  ``docs/experiments/00_RESULTS.md`` names, for every EXP-xx block it
       declares COMPLETE, the results document carrying that EXP id.

Scope: ``docs/experiments/`` only.

Usage::

    python scripts/check_results_prereg.py            # human report, exit 0
    python scripts/check_results_prereg.py --strict   # exit 1 on any finding
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXPERIMENTS = REPO / "docs" / "experiments"

RESULTS_RE = re.compile(r"^EXP\d.*results.*\.md$", re.IGNORECASE)
PREREG_RE = re.compile(r"^PREREG_\d+\.md$")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r"^(prereg(?:_version|_note)?):\s*'?\"?([^'\"\n]+)", re.MULTILINE)
VERSION_RE = re.compile(r"version:\s*'?\"?([0-9]+\.[0-9]+\.[0-9]+)")
EXP_BLOCK_RE = re.compile(r"^##\s+(EXP-\d+)", re.MULTILINE)
COMPLETE_RE = re.compile(r"##\s+(EXP-\d+)[^\n]*COMPLETE", re.IGNORECASE)


def findings_for(path: Path) -> list[str]:
    out: list[str] = []
    text = io.open(path, encoding="utf-8").read()
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return [f"{path.name}: no YAML frontmatter (prereg contract unreadable)"]
    fields = dict(FIELD_RE.findall(fm.group(1)))
    prereg = fields.get("prereg", "").strip()
    version = fields.get("prereg_version", "").strip()
    note = fields.get("prereg_note", "").strip()
    if prereg.lower() == "none":
        # Recorded exemption: the run predates the prereg contract. Allowed
        # only with a note saying why — silence is not an exemption.
        if not note:
            return [f"{path.name}: 'prereg: none' requires a 'prereg_note:'"]
        return []
    if not prereg:
        return [f"{path.name}: frontmatter missing 'prereg:'"]
    prereg_path = EXPERIMENTS / prereg
    if not prereg_path.exists() or not PREREG_RE.match(prereg):
        return [f"{path.name}: prereg '{prereg}' does not resolve to a PREREG_*.md"]
    prereg_text = io.open(prereg_path, encoding="utf-8").read()
    versions = set(VERSION_RE.findall(prereg_text))
    if not version:
        return [f"{path.name}: frontmatter missing 'prereg_version:'"]
    if version not in versions:
        return [
            f"{path.name}: prereg_version {version!r} not found in {prereg} "
            f"(has: {sorted(versions) or 'none'})"
        ]
    return out


def results_panel_findings() -> list[str]:
    out: list[str] = []
    panel = EXPERIMENTS / "00_RESULTS.md"
    if not panel.exists():
        return ["00_RESULTS.md missing"]
    text = io.open(panel, encoding="utf-8").read()
    for exp_id in COMPLETE_RE.findall(text):
        stem = exp_id.lower().replace("-", "")  # EXP-02 -> exp02 matches EXP02_results.md
        if not any(stem in p.name.lower() for p in EXPERIMENTS.glob("*.md")):
            out.append(
                f"00_RESULTS.md: block {exp_id} declared COMPLETE but no results "
                f"doc referencing it exists"
            )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    args = parser.parse_args()

    findings: list[str] = []
    results_docs = sorted(p for p in EXPERIMENTS.glob("*.md") if RESULTS_RE.match(p.name))
    for path in results_docs:
        findings.extend(findings_for(path))
    findings.extend(results_panel_findings())

    print(f"results-doc preregistration check — {len(results_docs)} results doc(s)")
    for f in findings:
        print(f"  ERROR {f}")
    if not findings:
        print("  PASS — every results doc cites a resolvable prereg + version")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
