#!/usr/bin/env python3
"""Document hygiene lint (read-only, report-only) — enforces AGENTS.md R11/R12.

Closes the two gaps that let document junk through (2026-09-22):

  1. R12 — unresolved placeholders: ``?`` table cells, ``?`` path segments
     (e.g. ``NIST_CSF/?/RS.CO-04.json``), TODO/FIXME markers, and unfilled
     ``<slot>`` template escapes outside ``templates/``.
  2. R11 — editorial meta-commentary in document bodies: legacy-name glosses,
     ``formerly``/``deprecated``/``retired`` remarks, ``corr-NNN`` references.
     Suppressed inside Version History / CHANGELOG / Approval sections, where
     such history belongs.
  3. Anchor-path resolution: every cited control-referential path
     (``NIST_CSF/<FUNCTION>/<ID>.json`` and sibling referentials) must exist
     under ``baseline/CONTROLS/`` (``NIST_CSF/`` resolves to ``NIST_CSF_2.0/``).

Scope: ``cases/``, ``example/``, ``output/`` get full checks; ``templates/``
gets the placeholder and path checks only (its ``<slot>`` escapes are the
template's purpose). The governance layer (``AGENTS.md``, ``SPEC.md``,
``README.md``, ``docs/``, ``baseline/``) is intentionally out of scope — it is
the legitimate home for alias glosses and decision history.

Usage::

    python scripts/doc_lint.py                # human report, exit 0
    python scripts/doc_lint.py --strict       # exit 1 on any finding
    python scripts/doc_lint.py --report _doc_lint.md

Idempotent: reads the tree; writes nothing unless ``--report`` is given.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path
from typing import Iterator

REPO = Path(__file__).resolve().parent.parent
CONTROLS = REPO / "baseline" / "CONTROLS"

FULL_SCOPES = ["cases", "example", "output"]
TEMPLATE_SCOPES = ["templates"]

# Referential directory alias: cited prefix -> directory under baseline/CONTROLS/.
REFERENTIALS = {
    "NIST_CSF": "NIST_CSF_2.0",
    "NIST_PF": "NIST_PF",
    "NIST_AI_RMF": "NIST_AI_RMF",
    "NIST_SP_800_53R5": "NIST_SP_800_53R5",
    "NIST_SSDF": "NIST_SSDF",
    "NIST_AI_SSDF": "NIST_AI_SSDF",
    "OWASP_ASVS": "OWASP_ASVS",
    "OWASP_SAMM": "OWASP_SAMM",
    "ISO_27001_2022": "ISO_27001_2022",
    "ISO_27701_2019": "ISO_27701_2019",
    "ISO_42001_2023": "ISO_42001_2023",
    "CIS_CONTROLS_V8": "CIS_CONTROLS_V8",
    "BSI_GRUNDSCHUTZ": "BSI_GRUNDSCHUTZ",
    "ENISA": "ENISA",
}
RE_REF_ALT = "|".join(REFERENTIALS)
RE_REF_PATH = re.compile(rf"\b({RE_REF_ALT})/([A-Za-z0-9_./-]+\.json)\b")
RE_PLACEHOLDER_CELL = re.compile(r"\|\s*\?\s*(\||$)")
RE_PLACEHOLDER_PATH = re.compile(r"/\?/")
# TODO/FIXME not inside quotes (a checklist asserting 'no "TODO" remains' is content).
RE_TODO = re.compile(r'(?<!["\'])\b(?:TODO|FIXME)\b(?!["\'])')
RE_TEMPLATE_SLOT = re.compile(r"<([A-Za-z][A-Za-z0-9 _.\-]{0,30})>")
# Real leftover slots are multi-token lowercase ("canonical name") or SHOUTY
# ("YYYY-MM-DD"). Single short tokens (<REG>, <id>) are path/field notation.
def _is_leftover_slot(inner: str) -> bool:
    if re.fullmatch(r"[a-z]+(?:[ _\-][a-z0-9]+)+", inner):
        return True
    return bool(re.fullmatch(r"[A-Z]{4,}[A-Z0-9\-]*", inner))
# HTML markup allowed inside verbatim corpus content.
HTML_TAGS = {"details", "summary", "mark", "br", "b", "i", "em", "strong", "code", "sub", "sup"}
RE_META = re.compile(
    r"(legacy expansion|formerly_known_as|formerly known as|\bcorr-\d+\b"
    r"|deprecated|retired)",
    re.IGNORECASE,
)
RE_SECTION = re.compile(r"^##\s+(.*)$")
HISTORY_SECTION = re.compile(r"version history|changelog|document approval", re.IGNORECASE)


class Finding:
    __slots__ = ("path", "line_no", "check", "text")

    def __init__(self, path: Path, line_no: int, check: str, text: str) -> None:
        self.path, self.line_no, self.check, self.text = path, line_no, check, text


def iter_markdown(scopes: list[str]) -> Iterator[Path]:
    for scope in scopes:
        root = REPO / scope
        if root.is_dir():
            yield from sorted(root.rglob("*.md"))


def check_file(path: Path, full: bool) -> list[Finding]:
    findings: list[Finding] = []
    section = ""
    rel = path.relative_to(REPO).as_posix()
    composed_corpus = "filtered_corpus/" in rel
    lines = io.open(path, encoding="utf-8", errors="replace").read().splitlines()
    # YAML frontmatter: functional counters/contract ids live here; the R11
    # meta-commentary check applies to bodies, not to these fields.
    in_frontmatter = len(lines) > 1 and lines[0].strip() == "---"
    frontmatter_end = 1 if in_frontmatter else -1
    if in_frontmatter:
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                frontmatter_end = idx
                break
    for line_no, line in enumerate(lines, 1):
        heading = RE_SECTION.match(line)
        if heading:
            section = heading.group(1)
        in_history = bool(HISTORY_SECTION.search(section))

        if RE_PLACEHOLDER_CELL.search(line):
            findings.append(Finding(path, line_no, "R12 placeholder-cell", line))
        if RE_PLACEHOLDER_PATH.search(line):
            findings.append(Finding(path, line_no, "R12 placeholder-path", line))
        if RE_TODO.search(line):
            findings.append(Finding(path, line_no, "R12 todo-fixme", line))
        if full and not composed_corpus:
            # Slots inside `code spans` are path/field notation, not leftovers.
            prose = re.sub(r"`[^`]*`", "", line)
            for match in RE_TEMPLATE_SLOT.finditer(prose):
                inner = match.group(1)
                if inner.lower() in HTML_TAGS:
                    continue
                if _is_leftover_slot(inner):
                    findings.append(
                        Finding(path, line_no, "R12 template-slot", line)
                    )
                    break
        if full and not in_history and line_no > frontmatter_end and RE_META.search(line):
            findings.append(Finding(path, line_no, "R11 meta-commentary", line))
        for match in RE_REF_PATH.finditer(line):
            directory = CONTROLS / REFERENTIALS[match.group(1)] / match.group(2)
            if not directory.exists():
                findings.append(
                    Finding(
                        path,
                        line_no,
                        "R12 unresolved control path",
                        f"{match.group(0)}  (missing: {directory.relative_to(REPO)})",
                    )
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    parser.add_argument("--report", type=Path, help="write the findings to this markdown ledger")
    args = parser.parse_args()

    findings: list[Finding] = []
    checked = 0
    for path in iter_markdown(FULL_SCOPES):
        findings.extend(check_file(path, full=True))
        checked += 1
    for path in iter_markdown(TEMPLATE_SCOPES):
        results = check_file(path, full=False)
        findings.extend(f for f in results if not f.check.startswith("R12 template-slot"))
        checked += 1

    findings.sort(key=lambda f: (str(f.path), f.line_no))
    for finding in findings:
        text = finding.text if len(finding.text) <= 120 else finding.text[:117] + "..."
        print(f"{finding.path.relative_to(REPO)}:{finding.line_no}: [{finding.check}] {text}")
    print(
        f"\n{checked} files checked, {len(findings)} findings"
        f" ({len({str(f.path) for f in findings})} files affected)"
    )

    if args.report:
        rows = "\n".join(
            f"| `{f.path.relative_to(REPO)}:{f.line_no}` | {f.check} | "
            f"`{f.text.strip()[:100]}` |"
            for f in findings
        ) or "| — | — | — |"
        args.report.write_text(
            "# Document hygiene lint report\n\n"
            f"Findings: {len(findings)} over {checked} markdown files.\n\n"
            "| Location | Check | Line |\n|---|---|---|\n" + rows + "\n",
            encoding="utf-8",
        )
        print(f"report written: {args.report}")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
