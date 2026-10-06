#!/usr/bin/env python3
"""Apply one lab overlay to a COPY of pipeline/src/steps.py — with a guard.

Usage: python3 lab/apply_overlay.py lab/overlays/<variant>.py <target>/pipeline/src/steps.py

An overlay declares REPLACEMENTS = [(old, new), ...] as exact strings. Each
`old` must occur exactly once in the target. Guards, in order:
1. anchor count == 1 (no silent mis-targeting);
2. no replacement may introduce a guarded token (gates, parsers, thresholds,
   stage logic stay byte-identical — the lab varies instructions, never rules);
3. the patched file must import (syntax check via compile());
4. backup kept at <target>.prelab, restored on any refusal.
"""
import sys
from pathlib import Path

BANNED = (
    "def parse_", "def check_", "def stage_", "def _sweep", "def _validate",
    "def assemble_doc", "def store_parsed", "PARSERS", "RETENTION_FLOOR",
    "IMPLICATION_DUP", "NUM_CTX", "NUM_PREDICT", "ELIDE_THRESHOLD",
)


def banned_in(s: str) -> str | None:
    for tok in BANNED:
        if tok in s:
            return tok
    return None


def main() -> int:
    overlay_path, target = Path(sys.argv[1]), Path(sys.argv[2])
    original = target.read_text(encoding="utf-8")
    src = original

    ns: dict = {}
    exec(compile(overlay_path.read_text(encoding="utf-8"), str(overlay_path), "exec"), ns)
    replacements: list[tuple[str, str]] = ns["REPLACEMENTS"]

    for old, new in replacements:
        n = src.count(old)
        if n != 1:
            sys.exit(f"FAIL: anchor occurs {n}x (expected exactly 1): {old[:90]!r}…")
        if banned_in(new) and not banned_in(old):
            sys.exit(f"FAIL: replacement introduces a guarded token: {new[:90]!r}…")
        src = src.replace(old, new)

    try:
        compile(src, str(target), "exec")
    except SyntaxError as e:
        sys.exit(f"FAIL: patched file does not compile: {e}")

    backup = target.with_name(target.name + ".prelab")
    backup.write_text(original, encoding="utf-8")
    target.write_text(src, encoding="utf-8")
    delta = len(src.splitlines()) - len(original.splitlines())
    print(f"overlay applied: {overlay_path.name} — {len(replacements)} replacement(s), "
          f"net {delta:+d} lines; backup at {backup.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
