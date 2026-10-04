#!/usr/bin/env python3
"""Research reference checker (read-only, report-only) — anchors docs/research/ to its sources.

docs/research/sources.yaml is the single registry of external sources for
AEGIS-RES-01..04. Every factual claim in those documents carries an ``[S-nnn]``
token. This script is the mechanical guard that keeps the research layer honest
over time — it is the answer to "will this drift away from the source?".

Seven checks:

  R1  every ``[S-nnn]`` token in the research documents resolves to a registry entry
  R2  every registry entry is cited at least once (or is explicitly ``status: unused``)
  R3  every repo-relative path cited in the research documents exists on disk
  R4  no source is past its ``recheck_after`` date (the drift alarm)
  R5  every registry entry is well-formed (required fields, parseable dates, https url)
  R6  every ``status: superseded`` entry names a valid ``superseded_by`` target
  R7  no ``evidence: UNVERIFIED`` entry carries a ``quote`` (an unread source may
      not gain the authority of a citation)

Why R7 is the important one: this registry deliberately records sources that
could not be opened during the survey pass. Those entries are allowed to exist so
the gap is visible, but they must never be quotable, or a reader has no way to
tell a verified claim from a plausible-looking one.

Scope: ``docs/research/`` only. The governance layer is not a research document
and is not scanned.

Usage::

    python scripts/check_research_refs.py                # human report, exit 0
    python scripts/check_research_refs.py --strict       # exit 1 on any finding
    python scripts/check_research_refs.py --report _research_refs.md
    python scripts/check_research_refs.py --now 2026-10-03   # test the drift alarm

Idempotent: reads the tree; writes nothing unless ``--report`` is given.

See docs/research/README.md for the field contract and the maintenance rule.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from datetime import date
from pathlib import Path
from typing import Iterator, NamedTuple

REPO = Path(__file__).resolve().parent.parent
RESEARCH = REPO / "docs" / "research"
REGISTRY = RESEARCH / "sources.yaml"
DOC_GLOB = "*.md"

# Citation token as it appears in prose: [S-042].
CITE_RE = re.compile(r"\[(S-\d{3})\]")
# Bare registry id, used only inside sources.yaml itself and in the checker output.
ID_RE = re.compile(r"^S-\d{3}$")
# A backticked span that could plausibly be a repo-relative path.
SPAN_RE = re.compile(r"`([^`\n]+)`")
# Partial dates accepted in `published`.
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")

REQUIRED_FIELDS = [
    "id",
    "key",
    "title",
    "org",
    "kind",
    "evidence",
    "url",
    "published",
    "retrieved",
    "recheck_after",
    "status",
]

VALID_EVIDENCE = {"PRIMARY", "PEER", "PRACTITIONER", "CONTESTED", "UNVERIFIED"}
VALID_KIND = {
    "vendor-primary",
    "standard",
    "preprint",
    "framework-doc",
    "practitioner",
    "infrastructure-doc",
    "prior-review",
}
VALID_STATUS = {"active", "superseded", "unverified", "unused"}

# Repo top-level names a cited path may start with. A backticked span is only
# treated as a path if it starts with one of these, which keeps `num_ctx`,
# `D-01.1`, `PP-001` and `qwen3.8:27b` from being mistaken for files.
REPO_ROOTS = (
    "AGENTS.md",
    "SPEC.md",
    "README.md",
    "config.yaml",
    "baseline/",
    "cases/",
    "docs/",
    "example/",
    "input/",
    "output/",
    "pipeline/",
    "scripts/",
    "templates/",
)
FILE_SUFFIXES = (".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".sh", ".sbatch", ".txt")

# A path that is being described rather than pointed at.
NOT_A_PATH = (" ", "*", "…", "...", "<", ">", "(", ")")

# Relative markdown links, e.g. [01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md)
# or [pipeline/](../pipeline/README.md). External links are skipped.
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


class Finding(NamedTuple):
    check: str
    severity: str  # "ERROR" | "WARN"
    where: str  # file, or "sources.yaml:<id>"
    message: str

    def render(self) -> str:
        return f"{self.severity:<5} {self.check:<3} {self.where}: {self.message}"


# --------------------------------------------------------------------------
# Minimal YAML subset reader
# --------------------------------------------------------------------------
#
# sources.yaml deliberately uses a narrow subset — plain scalars, inline
# flow lists, and `>-` folded block scalars — so this reader has no corner
# cases to get wrong. Mirrors the stdlib-only constraint the rest of the repo
# works under (compute nodes have no pip egress).


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_registry(text: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Return (entries keyed by id, parse problems).

    Entries are dicts of field name -> string value. ``supports`` is stored as
    its raw inline-list text; the caller decides how to interpret it.
    """
    entries: dict[str, dict[str, str]] = {}
    problems: list[str] = []
    lines = text.splitlines()

    in_header = True
    current: dict[str, str] | None = None
    field_indent = 0
    block_field: str | None = None
    block_parts: list[str] = []

    def close_block() -> None:
        nonlocal block_field, block_parts
        if block_field is not None and current is not None:
            current[block_field] = " ".join(p for p in block_parts if p).strip()
        block_field = None
        block_parts = []

    def flush() -> None:
        nonlocal current
        close_block()
        if current is not None:
            sid = current.get("id", "")
            if not sid:
                problems.append("an entry has no id")
            elif sid in entries:
                problems.append(f"duplicate id {sid}")
            else:
                entries[sid] = current
        current = None

    for lineno, raw in enumerate(lines, start=1):
        if in_header:
            if raw.strip() == "sources:":
                in_header = False
            continue

        if block_field is not None:
            indent = len(raw) - len(raw.lstrip())
            # A block scalar continues while lines stay more indented than the
            # field that opened it, or while the line is blank.
            if not raw.strip() or indent > field_indent:
                block_parts.append(raw.strip())
                continue
            close_block()

        if not raw.strip() or raw.strip().startswith("#"):
            continue

        item = re.match(r"^(\s*)-\s+(\w+):\s*(.*)$", raw)
        if item:
            flush()
            field_indent = len(item.group(1)) + 2
            current = {item.group(2): _unquote(item.group(3))}
            continue

        field_match = re.match(r"^(\s+)(\w+):\s*(.*)$", raw)
        if field_match:
            indent, field, value = (
                len(field_match.group(1)),
                field_match.group(2),
                field_match.group(3),
            )
            if current is None:
                problems.append(f"line {lineno}: field {field!r} outside any entry")
            elif indent < field_indent:
                problems.append(f"line {lineno}: unexpected indentation for {field!r}")
                current = None
            elif value.strip() in (">-", "|", ">", "|-"):
                block_field = field
                block_parts = []
            else:
                current[field] = _unquote(value)
            continue

        problems.append(f"line {lineno}: unparseable line {raw!r}")

    flush()
    return entries, problems


def supports_list(fields: dict[str, str]) -> list[str]:
    raw = fields.get("supports", "").strip()
    if not raw.startswith("[") or not raw.endswith("]"):
        return []
    inner = raw[1:-1].strip()
    if not inner:
        return []
    return [part.strip() for part in inner.split(",") if part.strip()]


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def check_forms(entries: dict[str, dict[str, str]], today: date) -> Iterator[Finding]:
    """R5 + R7 — entry well-formedness, and the no-quote-without-reading rule."""
    for sid, fields in sorted(entries.items()):
        where = f"sources.yaml:{sid}"
        for name in REQUIRED_FIELDS:
            if not fields.get(name, "").strip():
                yield Finding("R5", "ERROR", where, f"missing required field {name!r}")

        evidence = fields.get("evidence", "")
        if evidence and evidence not in VALID_EVIDENCE:
            yield Finding(
                "R5", "ERROR", where,
                f"evidence {evidence!r} not in {sorted(VALID_EVIDENCE)}",
            )

        kind = fields.get("kind", "")
        if kind and kind not in VALID_KIND:
            yield Finding("R5", "ERROR", where, f"kind {kind!r} not in {sorted(VALID_KIND)}")

        status = fields.get("status", "")
        if status and status not in VALID_STATUS:
            yield Finding(
                "R5", "ERROR", where, f"status {status!r} not in {sorted(VALID_STATUS)}"
            )

        url = fields.get("url", "")
        if url and not url.startswith("https://"):
            yield Finding("R5", "ERROR", where, f"url {url!r} is not https")

        published = fields.get("published", "")
        if published and not DATE_RE.match(published):
            yield Finding("R5", "ERROR", where, f"published {published!r} is not YYYY[-MM[-DD]]")

        retrieved = fields.get("retrieved", "")
        if retrieved and not DATE_RE.match(retrieved):
            yield Finding("R5", "ERROR", where, f"retrieved {retrieved!r} is not a date")
        elif retrieved:
            if _to_date(retrieved) > today:
                yield Finding(
                    "R5", "ERROR", where,
                    f"retrieved {retrieved} is in the future (now {today})",
                )

        recheck = fields.get("recheck_after", "")
        if recheck and recheck != "never":
            if not DATE_RE.match(recheck):
                yield Finding(
                    "R5", "ERROR", where, f"recheck_after {recheck!r} is not a date or 'never'"
                )
            else:
                when = _to_date(recheck)
                if when < today:
                    yield Finding(
                        "R4", "ERROR", where,
                        f"stale: recheck_after {recheck} has passed (now {today}) — "
                        f"re-read the source and bump retrieved + recheck_after",
                    )

        if evidence == "UNVERIFIED" and fields.get("quote", "").strip():
            yield Finding(
                "R7", "ERROR", where,
                "entry is evidence: UNVERIFIED but carries a quote — an unread "
                "source may not be quotable",
            )


def _to_date(value: str) -> date:
    parts = [int(p) for p in value.split("-")]
    while len(parts) < 3:
        parts.append(1)
    return date(parts[0], parts[1], parts[2])


def check_supersession(entries: dict[str, dict[str, str]]) -> Iterator[Finding]:
    """R6 — a superseded entry must name a live replacement."""
    for sid, fields in sorted(entries.items()):
        if fields.get("status") != "superseded":
            continue
        where = f"sources.yaml:{sid}"
        target = fields.get("superseded_by", "").strip()
        if not target:
            yield Finding(
                "R6", "ERROR", where,
                "status: superseded but no superseded_by — the replacement is unrecorded",
            )
        elif target not in entries:
            yield Finding("R6", "ERROR", where, f"superseded_by {target!r} is not a registry entry")


def check_citations(
    entries: dict[str, dict[str, str]], docs: dict[str, str]
) -> Iterator[Finding]:
    """R1 + R2 — every citation resolves; every entry earns its place."""
    cited: dict[str, int] = {}
    for path, text in sorted(docs.items()):
        for sid in CITE_RE.findall(text):
            cited[sid] = cited.get(sid, 0) + 1
            if sid not in entries:
                yield Finding(
                    "R1", "ERROR", f"docs/research/{path}",
                    f"[{sid}] does not resolve to any registry entry",
                )

    for sid, fields in sorted(entries.items()):
        if fields.get("status") == "unused":
            continue
        if cited.get(sid, 0) == 0:
            yield Finding(
                "R2", "WARN", f"sources.yaml:{sid}",
                "registry entry is cited nowhere (mark status: unused if deliberate)",
            )


def check_paths(docs: dict[str, str]) -> Iterator[Finding]:
    """R3 — a cited repo path must exist, and a relative link must resolve.

    Two distinct citation styles are checked, because the documents use both: a
    repo-relative path in backticks (``pipeline/src/steps.py``), and a relative
    markdown link (``[01_PIPELINE_PATTERNS.md](01_PIPELINE_PATTERNS.md)``).
    Anchors within a link target are stripped before resolving.
    """
    for path, text in sorted(docs.items()):
        where = f"docs/research/{path}"
        # The document's own directory, for resolving relative markdown links.
        doc_dir = (RESEARCH / path).parent

        for span in SPAN_RE.findall(text):
            if "://" in span or not span.startswith(REPO_ROOTS):
                continue
            if any(bad in span for bad in NOT_A_PATH):
                continue
            if "/" not in span and not span.endswith(FILE_SUFFIXES):
                continue
            if not (REPO / span).exists():
                yield Finding("R3", "ERROR", where, f"cited path {span!r} does not exist")

        for label, target in MD_LINK_RE.findall(text):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (doc_dir / target.split("#")[0]).resolve()
            if not resolved.exists():
                yield Finding(
                    "R3", "ERROR", where,
                    f"link [{label}]({target}) does not resolve to a file",
                )


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------


def load_docs() -> dict[str, str]:
    if not RESEARCH.is_dir():
        return {}
    return {p.name: p.read_text(encoding="utf-8") for p in sorted(RESEARCH.glob(DOC_GLOB))}


def build_report(findings: list[Finding], entries: dict, docs: dict, today: date) -> str:
    out = io.StringIO()
    out.write("AEGIS research reference report\n")
    out.write("=" * 72 + "\n")
    out.write(f"generated for  : {today.isoformat()}\n")
    out.write(f"registry       : docs/research/sources.yaml ({len(entries)} entries)\n")
    out.write(f"documents      : {len(docs)}\n")
    citations = sum(len(CITE_RE.findall(t)) for t in docs.values())
    unique = {s for t in docs.values() for s in CITE_RE.findall(t)}
    out.write(f"citations      : {citations} ({len(unique)} distinct sources)\n")
    out.write(f"findings       : {len(findings)}\n")
    out.write("\n")

    if not findings:
        out.write("RESULT: PASS — every citation resolves, every path exists,\n")
        out.write("               no source is past its recheck date.\n")
        return out.getvalue()

    by_check: dict[str, list[Finding]] = {}
    for f in findings:
        by_check.setdefault(f.check, []).append(f)
    for check in sorted(by_check):
        out.write(f"{check} ({len(by_check[check])})\n")
        for f in by_check[check]:
            out.write(f"  {f.severity:<5} {f.where}: {f.message}\n")
        out.write("\n")

    errors = sum(1 for f in findings if f.severity == "ERROR")
    warns = sum(1 for f in findings if f.severity == "WARN")
    out.write("RESULT: " + ("PASS" if not errors else "FAIL"))
    out.write(f" — {errors} error(s), {warns} warning(s)\n")
    return out.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--strict", action="store_true", help="exit 1 on any ERROR finding")
    ap.add_argument("--report", metavar="PATH", help="also write the report to PATH")
    ap.add_argument(
        "--now",
        metavar="YYYY-MM-DD",
        help="treat this date as today (default: the system date)",
    )
    args = ap.parse_args()

    if not REGISTRY.is_file():
        print(f"registry not found: {REGISTRY}", file=sys.stderr)
        return 2

    today = _to_date(args.now) if args.now else date.today()

    text = REGISTRY.read_text(encoding="utf-8")
    entries, problems = parse_registry(text)
    docs = load_docs()

    findings: list[Finding] = []
    for problem in problems:
        findings.append(Finding("R5", "ERROR", "sources.yaml", problem))
    findings.extend(check_forms(entries, today))
    findings.extend(check_supersession(entries))
    findings.extend(check_citations(entries, docs))
    findings.extend(check_paths(docs))

    report = build_report(findings, entries, docs, today)
    print(report)

    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")

    if args.strict and any(f.severity == "ERROR" for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
