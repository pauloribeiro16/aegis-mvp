"""
Generate an advisory control framework into baseline/CONTROLS/<FRAMEWORK_DIR>/.

This is a generic, data-driven generator that consumes a single YAML/JSON
specification of a framework and emits:

  baseline/CONTROLS/<FRAMEWORK_DIR>/
      _MANIFEST.json
      <framework_short>.json (authoritative ID list)
      <FUNCTION_DIR>/
          <control_id>.json  (one per leaf control)

Each leaf JSON follows the canonical 10-field schema shared with NIST_CSF_2.0,
NIST_PF and NIST_AI_RMF (R2b — Anchor integrity).

USAGE:
    python scripts/generate_advisory_framework.py --spec scripts/specs/<name>.yaml

The spec is a YAML file with this shape (see scripts/specs/nist_ssdf.yaml
for a worked example):

    framework: "NIST SSDF v1.1"
    framework_short: "NIST_SSDF"
    directory: "NIST_SSDF"
    version: "1.1 (2022-02-08)"
    source_url: "https://doi.org/10.6028/NIST.SP.800-218"
    fetched_date: "2026-09-22"
    families:
      - function: "PO"
        function_dir: "PO"
        category_name: "Practices for Organizations"
        practices:
          - id: "PO.1.1"
            category: "Define Security Requirements for Software Development"
            text: "..."
            informative_references: ["..."]
            examples: ["...", "..."]
            objectives: ["Determine whether ...", ...]

The script is idempotent: re-running it overwrites the same leaf JSONs.
It does NOT touch any file outside baseline/CONTROLS/<FRAMEWORK_DIR>/.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTROLS_ROOT = REPO_ROOT / "baseline" / "CONTROLS"

REQUIRED_LEAF_FIELDS = (
    "control_id",
    "framework",
    "function",
    "category",
    "subcategory_id",
    "subcategory_text",
    "informative_references",
    "implementation_examples",
    "assessment_objectives",
    "related_controls",
    "source_url",
    "source_version",
)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_leaf(
    spec: dict[str, Any],
    fam: dict[str, Any],
    practice: dict[str, Any],
    family_siblings: list[str],
) -> dict[str, Any]:
    """Build one per-control JSON object following the canonical 10-field schema."""
    cid = practice["id"]
    function = fam["function"]
    cat_name = practice.get("category", fam["category_name"])

    # If the spec doesn't supply explicit siblings, auto-populate with the
    # other practice IDs in the same family so related_controls is never empty.
    explicit = list(practice.get("related", []))
    if explicit:
        related = [f"{sib} ({spec['framework']} — same family)" for sib in explicit]
    else:
        related = [
            f"{sib} ({spec['framework']} — same family)"
            for sib in family_siblings
            if sib != cid
        ]
    return {
        "control_id": cid,
        "framework": spec["framework"],
        "function": function,
        "category": f"{cat_name} ({cid.split('.')[0]})",
        "subcategory_id": cid,
        "subcategory_text": practice["text"],
        "informative_references": list(practice.get("informative_references", [])),
        "implementation_examples": list(practice.get("examples", [])),
        "assessment_objectives": list(practice.get("objectives", [])),
        "related_controls": related,
        "source_url": spec["source_url"],
        "source_version": spec["version"],
    }


def write_framework(spec: dict[str, Any]) -> tuple[int, list[Path]]:
    target_dir = CONTROLS_ROOT / spec["directory"]
    target_dir.mkdir(parents=True, exist_ok=True)

    # Clear any prior leaf JSONs in family subdirectories (idempotent re-runs).
    for p in target_dir.rglob("*.json"):
        if p.name.startswith("_") or p.name == f"{spec['framework_short']}.json":
            continue
        p.unlink()

    all_ids: list[str] = []
    written: list[Path] = []

    for fam in spec["families"]:
        fam_dir = target_dir / fam["function_dir"]
        fam_dir.mkdir(parents=True, exist_ok=True)
        family_ids = [p["id"] for p in fam["practices"]]
        for practice in fam["practices"]:
            leaf = render_leaf(spec, fam, practice, family_ids)
            leaf_path = fam_dir / f"{practice['id']}.json"
            write_text(
                leaf_path,
                json.dumps(leaf, indent=2, ensure_ascii=False) + "\n",
            )
            all_ids.append(practice["id"])
            written.append(leaf_path)

    # Manifest
    manifest = {
        "referential": spec["framework"],
        "version": spec["version"],
        "source_urls": [spec["source_url"]],
        "fetched_date": spec.get("fetched_date", "2026-09-22"),
        "subcategories": len(all_ids),
        "expected_total": len(all_ids),
        "unverified_entries": [],
        "advisory": True,
        "enforced_by_verify_no_loss": False,
    }
    write_text(
        target_dir / "_MANIFEST.json",
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    )

    # Authoritative ID list
    id_list = {
        "framework": spec["framework"],
        "version": spec["version"],
        "note": "advisory referential; ids authoritative; not enforced by scripts/verify_no_loss.py",
        "subcategories": sorted(all_ids),
    }
    write_text(
        target_dir / f"{spec['framework_short']}.json",
        json.dumps(id_list, indent=2, ensure_ascii=False) + "\n",
    )

    return len(all_ids), written


def verify_framework(spec: dict[str, Any]) -> list[str]:
    """Sanity-check every emitted leaf: parses, has 12 fields, control_id matches stem."""
    target_dir = CONTROLS_ROOT / spec["directory"]
    errors: list[str] = []
    declared_ids = set()
    for fam in spec["families"]:
        for p in fam["practices"]:
            declared_ids.add(p["id"])

    found_ids: set[str] = set()
    for p in sorted(target_dir.rglob("*.json")):
        if p.name.startswith("_") or p.name == f"{spec['framework_short']}.json":
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p}: JSON parse error: {e}")
            continue
        missing = [f for f in REQUIRED_LEAF_FIELDS if f not in data]
        if missing:
            errors.append(f"{p}: missing fields {missing}")
        if data.get("control_id") != p.stem:
            errors.append(
                f"{p}: control_id {data.get('control_id')!r} != stem {p.stem!r}"
            )
        if data.get("subcategory_id") != p.stem:
            errors.append(
                f"{p}: subcategory_id {data.get('subcategory_id')!r} != stem {p.stem!r}"
            )
        found_ids.add(p.stem)

    missing_ids = declared_ids - found_ids
    extra_ids = found_ids - declared_ids
    if missing_ids:
        errors.append(f"declared IDs without file: {sorted(missing_ids)}")
    if extra_ids:
        errors.append(f"files without declared ID: {sorted(extra_ids)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path, help="YAML spec file")
    parser.add_argument("--no-verify", action="store_true", help="skip post-write verification")
    args = parser.parse_args()

    spec = yaml.safe_load(args.spec.read_text(encoding="utf-8"))
    n, written = write_framework(spec)
    print(f"[OK] wrote {n} controls under {spec['directory']}/ ({len(written)} files)")

    if not args.no_verify:
        errors = verify_framework(spec)
        if errors:
            print(f"[FAIL] {len(errors)} errors:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
            return 1
        print("[OK] verification passed")

    return 0


if __name__ == "__main__":
    sys.exit(main())