#!/usr/bin/env python3
"""aegis_pipeline.phases.phase2.parsers — Parsers and metrics for Phase 2 operationalization."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

import quality
from aegis_pipeline.phases.phase1.common import extract_fenced

METHOD_VOCAB = {"TEST", "INSPECT", "DEMONSTRATE", "ANALYZE"}


def load_tensions(run_dir: Path) -> list[dict]:
    tfile = run_dir / "steps" / "tensions.json"
    if tfile.exists():
        try:
            return json.loads(tfile.read_text(encoding="utf-8")).get("tensions", [])
        except (OSError, ValueError):
            return []
    return []


def load_operationalizations(run_dir: Path) -> dict[str, dict]:
    """Load per-subdomain operationalization data from steps/phase2/*.json."""
    p2_dir = run_dir / "steps" / "phase2"
    if not p2_dir.is_dir():
        return {}
    out: dict[str, dict] = {}
    for jf in sorted(p2_dir.glob("*.json")):
        try:
            blob = json.loads(jf.read_text(encoding="utf-8"))
            sd = blob.get("subdomain")
            if sd:
                out[sd] = blob
        except (OSError, ValueError):
            continue
    return out


def _slot_of(objective_id: str) -> str | None:
    m = re.search(r"(D-\d{2}\.\d-\d{3})$", objective_id or "")
    return m.group(1) if m else None


def _ops_by_slot(op_data: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for o in op_data.get("objectives", []):
        s = _slot_of(str(o.get("objective_id", "")))
        if s:
            out[s] = o
    return out


def seam_fill(rows: list[dict], op_map: dict[str, dict]) -> tuple[int, int]:
    by_slot: dict[str, dict] = {}
    for blob in op_map.values():
        by_slot.update(_ops_by_slot(blob))
    filled = sum(1 for r in rows if by_slot.get(_slot_of(r["objective_id"]), {}).get("criteria"))
    return filled, len(rows)


def method_distribution(op_map: dict[str, dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for blob in op_map.values():
        for o in blob.get("objectives", []):
            m = str(o.get("method", ""))
            counts[m] = counts.get(m, 0) + 1
    return dict(sorted(counts.items()))


def method_diversity_findings(dist: dict[str, int]) -> list[str]:
    total = sum(dist.values())
    if total < 4:
        return []
    return [
        f"method {m}: {n}/{total} objectives ({n / total:.0%}) exceeds the "
        "60% mode-collapse ceiling (R10b) — the batch is collapsing to "
        "one default verification method"
        for m, n in dist.items() if n / total > 0.60
    ]


def parse_p2o(answer: str, subdomain: str | None = None) -> dict:
    """Parse and validate one sub-domain's operationalization answer."""
    raw = extract_fenced(answer, "json").strip()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("p2o: expected a JSON object")
    sd_raw = str(data.get("subdomain", "")).strip()
    m_sd_field = re.match(r"^[Dd][-_.]?(\d{2})[-_.](\d)$", sd_raw)
    sd = f"D-{m_sd_field.group(1)}.{m_sd_field.group(2)}" if m_sd_field else sd_raw.upper()
    if subdomain and sd != subdomain:
        raise ValueError(f"p2o: expected subdomain {subdomain!r}, got {sd!r}")
    data["subdomain"] = sd or subdomain
    op_trans = str(data.get("operational_translation", "")).strip()
    if not op_trans:
        raise ValueError("p2o: operational_translation cannot be empty")
    objs = data.get("objectives", [])
    if not isinstance(objs, list) or len(objs) == 0:
        raise ValueError("p2o: expected non-empty list under 'objectives'")

    normalized_objs = []
    seen_criteria: dict[str, str] = {}
    rule_seq = 0
    for idx, o in enumerate(objs):
        if not isinstance(o, dict):
            raise ValueError(f"p2o: objective {idx} is not an object")
        oid = str(o.get("objective_id") or o.get("id") or "").strip().upper()
        if oid.startswith("OBJ-"):
            oid = "SO-" + oid[4:]
        m_oid = re.match(r"^(?:PO|SO)-(D-\d{2}\.\d)-\d{3}$", oid)
        if not m_oid:
            raise ValueError(f"p2o: objective {idx} id {oid!r} is not a PO-/SO-D-XX.Y-NNN id")
        if subdomain and m_oid.group(1) != subdomain:
            raise ValueError(f"p2o: {oid} belongs to {m_oid.group(1)}, not to this sub-domain ({subdomain})")
        meth = str(o.get("method", "")).strip().upper()
        if meth not in METHOD_VOCAB:
            raise ValueError(f"p2o: {oid} invalid method {meth!r}, must be one of {sorted(METHOD_VOCAB)}")
        crit = str(o.get("criteria", "")).strip()
        if len(crit.split()) < 8:
            raise ValueError(
                f"p2o: {oid} criteria too thin to be falsifiable "
                f"({len(crit.split())} words) — name the verification "
                "artifact or test condition"
            )
        crit_key = re.sub(r"\W+", " ", crit.lower()).strip()
        if crit_key in seen_criteria:
            raise ValueError(
                f"p2o: {oid} criteria duplicates {seen_criteria[crit_key]}'s "
                "— a repeated template is not a per-objective criterion"
            )
        seen_criteria[crit_key] = oid
        own = str(o.get("owner", "")).strip()
        if not own:
            raise ValueError(f"p2o: {oid} owner cannot be empty")
        raw_rules = o.get("rules", [])
        if not isinstance(raw_rules, list) or len(raw_rules) == 0:
            raise ValueError(f"p2o: {oid} must carry at least one RULE-* rule")
        norm_rules = []
        for r in raw_rules:
            if isinstance(r, str):
                parts = r.split(":", 1)
                rid = parts[0].strip()
                stmt = parts[1].strip() if len(parts) > 1 else r.strip()
                r_dict = {"rule_id": rid, "statement": stmt, "verification_target": meth}
            elif isinstance(r, dict):
                vt = str(r.get("verification_target") or meth).strip().upper()
                r_dict = {
                    "rule_id": str(r.get("rule_id") or r.get("id") or "").strip(),
                    "statement": str(r.get("statement") or r.get("description") or r.get("rule") or "").strip(),
                    "verification_target": vt if vt in METHOD_VOCAB else meth,
                }
            else:
                raise ValueError(f"p2o: {oid} rule must be string or object")

            rule_seq += 1
            m_sd = re.search(r"D[-_.](\d{2})[-_.](\d)", r_dict["rule_id"], re.IGNORECASE)
            sd_norm = f"D-{m_sd.group(1)}.{m_sd.group(2)}" if m_sd else m_oid.group(1)
            r_dict["rule_id"] = f"RULE-{sd_norm}-{rule_seq:03d}"
            stmt = r_dict["statement"]
            if not ("SHALL" in stmt.upper() or "MUST" in stmt.upper()):
                raise ValueError(f"p2o: {r_dict['rule_id']} statement must contain SHALL or MUST (EARS/RFC2119)")
            tech_hits = quality.check_no_technology(stmt)
            if tech_hits:
                raise ValueError(f"p2o: {r_dict['rule_id']} {tech_hits[0]}")
            norm_rules.append(r_dict)

        normalized_objs.append({
            "objective_id": oid,
            "method": meth,
            "criteria": crit,
            "owner": own,
            "rules": norm_rules,
        })

    data["objectives"] = normalized_objs
    return data
