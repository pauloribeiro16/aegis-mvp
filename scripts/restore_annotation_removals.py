#!/usr/bin/env python3
"""
restore_annotation_removals.py
==============================
Repairs a pre-existing loss from the tag-annotation step (annotate_baseline_
domains.py): when the aegis semantic tags were inserted into the corpus, the
annotator also DELETED 321 original lines — the 160 old-style
``<!-- pair: REG1,REG2 -->`` / ``<!-- /pair -->`` markers (Part 2 pair tables)
plus the D-06.4 "Conventions" line (it contained the same marker syntax
inline, as documentation).

This script reconstructs the correct annotated input M0' = original ∪ tags by
aligning each ORIGINAL merged file with its M0 (annotated snapshot) counterpart
via difflib.SequenceMatcher:
  - 'equal' blocks align line-for-line;
  - 'delete' blocks (lines present in the original, absent from M0) are
    re-inserted at their aligned position;
  - 'insert' blocks (M0-only) are the aegis tag lines — kept.

The result is written to a staging directory (--stage) mirroring the domains
layout, and optionally copied over the working baseline (--install).

Post-condition (asserted): every original line is present in the staged file
and the only staged-only lines are aegis tag lines.

Usage:
  python scripts/restore_annotation_removals.py \
      --original "../methodology-main/00_METHODOLOGY/PREPROCESSING_by_domain/domains" \
      --annotated _m0_tmp/baseline/domains \
      --stage _restore_stage --install baseline/domains
"""

import argparse
import difflib
import re
import shutil
import sys
from pathlib import Path

import time
import subprocess


def robust_rmtree(path, retries=4, delay=1.0):
    """rmtree that survives OneDrive/dir-handle locks (Windows)."""
    path = Path(path)
    if not path.exists():
        return
    for k in range(retries):
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            time.sleep(delay)
    subprocess.run(["cmd", "/c", "rd", "/s", "/q", str(path)], check=False)
    if path.exists():
        raise PermissionError(f"could not remove {path}")

RE_TAG_LINE = re.compile(r"^<!--\s*/?aegis:")


def read_lines(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    return [ln.replace("\r", "") for ln in text.splitlines()]


def restore_lines(orig_lines, ann_lines, log, name):
    sm = difflib.SequenceMatcher(a=orig_lines, b=ann_lines, autojunk=False)
    out = []
    restored = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            out.extend(ann_lines[j1:j2])
        elif tag == "delete":
            # original-only lines removed by the annotator -> re-insert
            out.extend(orig_lines[i1:i2])
            restored += i2 - i1
        elif tag == "insert":
            out.extend(ann_lines[j1:j2])  # aegis tags
        elif tag == "replace":
            # The annotator substituted old-style markers with aegis tags 1:1.
            # Keep BOTH: annotated tag lines first (routing boundaries), then
            # the original lines (content, e.g. <!-- pair: X,Y --> markers).
            block_o = orig_lines[i1:i2]
            block_a = ann_lines[j1:j2]
            tag_lines = [l for l in block_a if RE_TAG_LINE.match(l.strip())]
            non_tag_a = [l for l in block_a if l.strip() and not RE_TAG_LINE.match(l.strip())]
            if non_tag_a:
                log.append(f"{name}: REPLACE block contains {len(non_tag_a)} non-tag "
                           f"annotated lines (unexpected) — keeping original side")
            out.extend(tag_lines)
            out.extend(block_o)
            restored += i2 - i1
    return out, restored


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--original", required=True)
    ap.add_argument("--annotated", required=True, help="annotated snapshot dir (e.g. _m0_tmp/baseline/domains)")
    ap.add_argument("--stage", default="_restore_stage")
    ap.add_argument("--install", default=None, help="also copy staged files over this domains dir")
    args = ap.parse_args()

    orig_root = Path(args.original)
    ann_root = Path(args.annotated)
    stage_root = Path(args.stage)
    if stage_root.exists():
        robust_rmtree(stage_root)
    stage_root.mkdir(parents=True)

    log = []
    total_restored = 0
    n_files = 0
    for merged in sorted(orig_root.glob("D-*/D-*/D-*.?*.md")):
        if not re.fullmatch(r"D-\d+\.\d+", merged.stem):
            continue
        rel = merged.relative_to(orig_root)
        ann = ann_root / rel
        if not ann.exists():
            log.append(f"MISSING annotated counterpart: {rel.as_posix()}")
            continue
        orig_lines = read_lines(merged)
        ann_lines = read_lines(ann)
        out, restored = restore_lines(orig_lines, ann_lines, log, rel.as_posix())
        total_restored += restored
        n_files += 1

        # post-condition A: no original line lost in the staged file
        from collections import Counter
        missing = Counter(l for l in orig_lines if l.strip()) - Counter(l for l in out if l.strip())
        if missing:
            log.append(f"{rel.as_posix()}: POST-CONDITION FAIL, {sum(missing.values())} original lines still missing")
            for l in list(missing)[:3]:
                log.append(f"    - {l[:90]}")
        # post-condition B: staged-only lines are aegis tags or blank/format
        extra = Counter(out) - Counter(orig_lines)
        bad_extra = [l for l in extra if l.strip() and not RE_TAG_LINE.match(l.strip())]
        if bad_extra:
            log.append(f"{rel.as_posix()}: staged adds {len(bad_extra)} non-tag lines")
            for l in bad_extra[:3]:
                log.append(f"    + {l[:90]}")

        dst = stage_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

    print(f"files processed: {n_files}; original lines restored: {total_restored}")
    for l in log:
        print("LOG:", l)
    if args.install:
        installed = 0
        for f in stage_root.rglob("D-*.?*.md"):
            if not re.fullmatch(r"D-\d+\.\d+", f.stem):
                continue
            dst = Path(args.install) / f.relative_to(stage_root)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
            installed += 1
        print(f"installed {installed} restored merged files into {args.install}")
    fails = [l for l in log if "FAIL" in l or "MISSING" in l or "non-tag" in l]
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
