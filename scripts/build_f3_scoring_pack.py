#!/usr/bin/env python3
"""build_f3_scoring_pack.py — the blind scoring pack for L2_RUBRIC_F3.md.

The Phase 3 instrument scores three SURFACES of the Part 1 package, not the
Phase 1 goal rows: a functional card row, an organizational requirement, and a
coverage verdict row. This builds the anonymised sheets for them.

What it emits:

  scoring/f3/pack/<doc_key>.md   one sheet per document (anonymous key)
  scoring/f3/_reference.md       the material the judgement needs and the
                                  pack must not repeat per sheet: the company
                                  intake, the objective statements and the
                                  published anchor sets
  scoring/f3/L2_F3_SCORES.csv     the file the researcher fills in
  scoring/f3/_manifest.json       which units each document exposes
  scoring/f3/_key.json            the un-blinding map — DO NOT OPEN before
                                  scoring

Blinding is mechanical: the sheet carries no run id, no model, no document
name; the keys are opaque and the presentation order is a seeded shuffle.
The key derivation is salted per build (secrets.token_hex); the salt lives
ONLY in _key.json, so the keys are not re-derivable from the pack's own
contents. _reference.md merges the runs' material by content (the pack is
for arms of the SAME case: same company facts, same objectives) and names
no run. Residual, stated honestly: the unit ids are the artefact's own
ids, so a reader with repository access could set-diff a sheet against a
candidate run — the blind holds for an honest scorer, not against an
adversary with repo access.

Sampling (L2_RUBRIC_F3 §1): 8 units per document, stratified so every
package R<n> (cards) and every domain D-XX (verdict rows) appears at least
once where there are enough units to do so.

Usage:
    python3 scripts/build_f3_scoring_pack.py --run <run_id> [--run <run_id> ...]
    python3 scripts/build_f3_scoring_pack.py --open     # reveal the key afterwards

Stdlib only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import secrets
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline" / "src"))

RUNS = Path(os.environ.get("AEGIS_RUNS_DIR") or (Path.home() / "Work" / "aegis-runs"))
OUT = REPO / "scoring" / "f3"

#: Registered seeds (L2_RUBRIC_F3 §1 asks for the Phase 1 mechanics).
SEED_ROWS = 20261030      # which units get sampled
SEED_ORDER = 20261031     # presentation order of the documents
N_ROWS = 8                # sampled units per document

#: The dimensions of L2_RUBRIC_F3 §2 (0–2 each). D6 applies to verdict rows.
DIMENSIONS = ["D1 altitude", "D2 form", "D3 fit criterion",
              "D4 chain validity", "D5 company grounding"]
CSV_COLUMNS = ["doc_key", "unit", "dimension", "score", "notes"]

RE_CARD = re.compile(r"^#### Card (R\d+\.\d+)\b", re.M)
RE_ORG = re.compile(r"^### (ORG-D-\d{2}\.\d-\d{3})\b", re.M)
RE_MATRIX_ROW = re.compile(r"^\|\s*`((?:PO|SO)-D-\d\d\.\d-\d{3})`\s*\|")
RE_OBJECTIVE = re.compile(r"\b(?:PO|SO)-D-\d\d\.\d-\d{3}\b")
RE_PACKAGE = re.compile(r"^###\s+Package\s+(\S+)", re.M)


def _blocks(text: str, pattern: re.Pattern) -> list[tuple[str, str]]:
    """(id, block) for every heading the pattern matches, in document order."""
    out: list[tuple[str, str]] = []
    matches = list(pattern.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1), text[m.start():end].rstrip()))
    return out


def _matrix_rows(mapping: str) -> list[tuple[str, str]]:
    out = []
    for line in mapping.splitlines():
        m = RE_MATRIX_ROW.match(line.strip())
        if m:
            out.append((m.group(1), line.strip()))
    return out


def _carrier_of(row: str) -> str:
    cells = [c.strip() for c in row.split("|")[1:-1]]
    return cells[2].strip("` ") if len(cells) > 2 else ""


def _objective_reference(phase2: str) -> dict[str, dict[str, str]]:
    """{objective id: {statement, anchors}} from the Phase 2 deliverable.

    The Phase 2 doc's table is the only place where an objective's published
    anchor set is written down; the rubric's D4 (chain validity) is judged
    against it.
    """
    out: dict[str, dict[str, str]] = {}
    for line in phase2.splitlines():
        m = RE_MATRIX_ROW.match(line.strip())
        if not m:
            continue
        cells = [c.strip() for c in line.strip().split("|")[1:-1]]
        anchors = ""
        for c in cells:
            if re.search(r"\b[A-Z]{2}\.[A-Z]{2}-\d{2}\b", c):
                anchors = c
                break
        statement = next((c for c in cells if len(c) > 40), "")
        out[m.group(1)] = {"statement": statement, "anchors": anchors}
    return out


def _sample(items: list[tuple[str, str]], strata: dict[str, list[int]],
            n: int, seed: int) -> list[int]:
    """`n` indices, stratified: one per stratum first, then a seeded fill."""
    rng = random.Random(seed)
    chosen: list[int] = []
    for key in sorted(strata):
        pool = strata[key]
        if pool and len(chosen) < n:
            chosen.append(rng.choice(pool))
    rest = [i for i in range(len(items)) if i not in chosen]
    rng.shuffle(rest)
    chosen += rest[: max(0, n - len(chosen))]
    return sorted(chosen[:n])


def build(run_ids: list[str]) -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    pack_dir = OUT / "pack"
    pack_dir.mkdir(parents=True, exist_ok=True)
    for old in pack_dir.glob("*.md"):
        old.unlink()

    documents: list[dict] = []
    reference: list[str] = ["# Reference material (the same for every document)", "",
                           "The rubric asks questions that need the baseline behind the "
                           "artefact: the objective's duty, the anchors the objective "
                           "publishes, and the company's own facts.", ""]
    fact_variants: list[str] = []
    run_facts_variant: dict[str, int] = {}
    merged_objs: dict[str, dict[str, str]] = {}
    for run_id in run_ids:
        run = RUNS / run_id
        phase2 = run / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        doc01 = run / "outputs" / "phase3" / "part1_security_privacy" / "v2_security_privacy_synthesis" / "Doc01_Requirements_Specification.md"
        doc03 = run / "outputs" / "phase3" / "part1_security_privacy" / "v2_security_privacy_synthesis" / "Doc03_Organizational_Requirements.md"
        mapping = run / "outputs" / "phase3" / "synthesis_rounds" / "OBJECTIVE_MAPPING.md"
        facts = run / "steps" / "fact_sheet.yaml"
        missing = [p for p in (phase2, doc01, doc03, mapping, facts) if not p.is_file()]
        if missing:
            print(f"skip {run_id}: missing {[p.name for p in missing]}", file=sys.stderr)
            continue

        objs = _objective_reference(phase2.read_text(encoding="utf-8"))
        fact_text = facts.read_text(encoding="utf-8")
        if fact_text not in fact_variants:
            fact_variants.append(fact_text)
        run_facts_variant[run_id] = fact_variants.index(fact_text)
        for oid, ref in objs.items():
            prev = merged_objs.get(oid)
            if prev and prev != ref:
                raise SystemExit(
                    f"objective {oid} differs between runs — this pack scores arms of "
                    "ONE case; mixed cases would attribute a document by its reference")
            merged_objs[oid] = ref

        cards = _blocks(doc01.read_text(encoding="utf-8"), RE_CARD)
        orgs = _blocks(doc03.read_text(encoding="utf-8"), RE_ORG)
        rows = _matrix_rows(mapping.read_text(encoding="utf-8"))

        # the mapping binds each objective to its carrier — the reference of a
        # card unit is the objective it carries.
        carrier_of = {oid: _carrier_of(row) for oid, row in rows}

        card_strata: dict[str, list[int]] = {}
        for i, (cid, _) in enumerate(cards):
            card_strata.setdefault(cid.split(".")[0], []).append(i)
        verdict_strata: dict[str, list[int]] = {}
        for i, (oid, _) in enumerate(rows):
            m = re.match(r"^(?:PO|SO)-(D-\d{2})\.", oid)
            if m:
                verdict_strata.setdefault(m.group(1), []).append(i)

        documents.append({
            "run_id": run_id, "kind": "cards", "units": cards,
            "picks": _sample(cards, card_strata, N_ROWS, SEED_ROWS),
            "reference_of": lambda cid, co=carrier_of: [o for o, c in co.items() if c == cid],
        })
        documents.append({
            "run_id": run_id, "kind": "organizational", "units": orgs,
            "picks": _sample(orgs, {}, N_ROWS, SEED_ROWS + 1),
            "reference_of": lambda oid, objs=objs: [oid] if oid in objs else [],
        })
        documents.append({
            "run_id": run_id, "kind": "verdicts", "units": rows,
            "picks": _sample(rows, verdict_strata, N_ROWS, SEED_ROWS + 2),
            "reference_of": lambda oid, objs=objs: [oid] if oid in objs else [],
        })

    if not documents:
        print("no documents — nothing to score", file=sys.stderr)
        return 2

    # The reference merges the runs' material by CONTENT and names no run:
    # the same-case arms share the company facts and the objective set.
    reference += ["## Company facts", ""]
    for i, fact_text in enumerate(fact_variants):
        label = "" if len(fact_variants) == 1 else f" (variant {chr(65 + i)})"
        reference += [f"### The company{label}", "", "```yaml", fact_text.rstrip(), "```", ""]
    reference += ["## Objectives and their published anchors", ""]
    for oid, ref in sorted(merged_objs.items()):
        reference += [f"- `{oid}` — {ref['statement']}", f"  - published anchors: {ref['anchors'] or '—'}"]

    # anonymised keys + a seeded presentation order
    rng = random.Random(SEED_ORDER)
    order = list(range(len(documents)))
    rng.shuffle(order)
    salt = secrets.token_hex(16)
    key_map: dict[str, dict] = {}
    manifest: list[dict] = []
    scores = []

    for slot, doc_index in enumerate(order, start=1):
        doc = documents[doc_index]
        key = "doc-" + hashlib.sha256(
            f"{salt}:{doc['kind']}:{slot}".encode()).hexdigest()[:10]
        key_map[key] = {"run_id": doc["run_id"], "kind": doc["kind"], "slot": slot}
        if len(fact_variants) > 1:
            key_map[key]["facts_variant"] = chr(65 + run_facts_variant[doc["run_id"]])
        units = doc["units"]
        sheet = [f"# Scoring sheet {key}", "",
                 f"This sheet shows {len(doc['picks'])} artefact rows from one document. "
                 "Score each row against the dimensions in L2_RUBRIC_F3.md §2 (0, 1 or 2):",
                 "",
                 "- **D1 altitude** — does the text stay at the level its source sets?",
                 "- **D2 form** — is it the artefact's grammar (EARS `shall`, the card anatomy)?",
                 "- **D3 fit criterion** — binary, judgeable from named evidence?",
                 "- **D4 chain validity** — every anchor inside the published set, right function?",
                 "- **D5 company grounding** — does it name THIS company's reality?",
                 "",
                 "A verdict row is scored on **D6 verdict honesty** as well: the verdict "
                 "word matches the discharge.", "",
                 "The objective behind each row, its published anchors and the company "
                 "facts are in `_reference.md`.", ""]
        for n, index in enumerate(doc["picks"], start=1):
            uid, body = units[index]
            sheet += [f"## Row {n} — `{uid}`", "", body, "",
                      "D1 (0-2): ______   D2 (0-2): ______   D3 (0-2): ______   "
                      "D4 (0-2): ______   D5 (0-2): ______", ""]
            if doc["kind"] == "verdicts":
                sheet += ["D6 verdict honesty (0-2): ______", ""]
            sheet += ["Notes:", "", "---", ""]
            scores.append({"doc_key": key, "unit": uid, "kind": doc["kind"]})
        (pack_dir / f"{key}.md").write_text("\n".join(sheet) + "\n", encoding="utf-8")
        manifest.append({
            "doc_key": key, "kind": doc["kind"],
            "units": [units[i][0] for i in doc["picks"]],
            "reference_units": {units[i][0]: doc["reference_of"](units[i][0]) for i in doc["picks"]},
        })

    (OUT / "_reference.md").write_text("\n".join(reference) + "\n", encoding="utf-8")
    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    with (OUT / "L2_F3_SCORES.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(CSV_COLUMNS)
        for row in scores:
            for dim in DIMENSIONS + (["D6 verdict honesty"] if row["kind"] == "verdicts" else []):
                writer.writerow([row["doc_key"], row["unit"], dim, "", ""])
    (OUT / "_key.json").write_text(json.dumps({"salt": salt, "documents": key_map}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"pack: {len(documents)} document(s), {len(scores)} unit(s) -> {OUT}")
    print("the key file names the runs — do not open it before scoring")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", action="append", default=[], help="run id under $AEGIS_RUNS_DIR")
    ap.add_argument("--open", action="store_true", help="reveal the key (only after scoring)")
    args = ap.parse_args()
    key_path = OUT / "_key.json"
    if args.open:
        if not key_path.is_file():
            print("no key file — run without --open first", file=sys.stderr)
            return 2
        print(json.dumps(json.loads(key_path.read_text()), indent=1))
        return 0
    runs = args.run or [p.name for p in sorted(RUNS.glob("run_*")) if (p / "steps" / "phase3" / "gate_report.md").is_file()]
    return build(runs)


if __name__ == "__main__":
    raise SystemExit(main())
