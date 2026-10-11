#!/usr/bin/env python3
"""aegis_pipeline.guards.controls — deterministic control derivation for Phase 1 deliverable.

Resolves the chain: Sub-SO -> source_SR -> mapping store -> CONTROLS JSONs
with zero LLM involvement (R2b by construction):

    SG-D-XX.Y.<REG>  --regs/<REG>.md Sub-SO yaml `source_SR`-->  SR-<REG>-NNN
    SR-<REG>-NNN     --MAPPINGS/sr_control_mappings/<REG>.json--> NIST CSF 2.0 /
                     PF 1.1 / AI RMF control ids
    control id       --CONTROLS/<REF>/<FUNCTION>/<ID>.json--> function + text

Stdlib only (Deucalion compute nodes have no pip egress).
"""

from __future__ import annotations

import json
import re
import sys
from functools import lru_cache
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[2]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import (
    REGULATIONS,
    anchor_slice,
    carries_reg_card,
    domain_dir,
    reg_module_path,
)

REF_DIRS = {"nist_csf": "NIST_CSF_2.0", "nist_pf": "NIST_PF", "nist_airmf": "NIST_AI_RMF"}
PATH_ALIAS = {"NIST_CSF_2.0": "NIST_CSF", "NIST_PF": "NIST_PF", "NIST_AI_RMF": "NIST_AI_RMF"}
DESC_MAX = 90

TRACK_B_MATRIX = {
    "MICRO": {
        "MUST": {"BUILD_REQUIRED": "LIGHTWEIGHT", "INHERITABLE": "MINIMAL"},
        "SHOULD": {"BUILD_REQUIRED": "DEFERRED", "INHERITABLE": "DEFERRED"},
        "COULD": {"BUILD_REQUIRED": "DEFERRED", "INHERITABLE": "DEFERRED"},
    },
    "LARGE": {
        "MUST": {"BUILD_REQUIRED": "RIGOROUS", "INHERITABLE": "STANDARD"},
        "SHOULD": {"BUILD_REQUIRED": "STANDARD", "INHERITABLE": "LIGHTWEIGHT"},
        "COULD": {"BUILD_REQUIRED": "LIGHTWEIGHT", "INHERITABLE": "MINIMAL"},
    },
}


# --------------------------------------------------------------------------
# Sub-SO card -> source_SR
# --------------------------------------------------------------------------

def _module_text(repo: Path, sd_id: str, reg: str) -> str:
    path = reg_module_path(repo, sd_id, reg)
    if not carries_reg_card(repo, sd_id, reg):
        raise ValueError(
            f"{sd_id} carries no Sub-SO card for {reg}: {path.name} is absent or "
            f"declares no SG-{sd_id}.{reg}. There is no source_SR to map, and "
            f"inventing one would break the regulation→article→objective→control "
            f"traceability chain (R2/R2b)."
        )
    return path.read_text(encoding="utf-8")


def sources_of(repo: Path, sd_id: str, reg: str) -> list[str]:
    """The Sub-SO card's `source_SR` (scalar, inline list or block list) of
    regs/<REG>.md — the SRs this sub-domain's <REG> baseline rests on.
    Returns [] when the module legitimately carries no Sub-SO card for this
    regulation (e.g. D-02.2/GDPR: partial coverage via SG-D-02.1.GDPR)."""
    text = _module_text(repo, sd_id, reg)
    if not re.search(rf"id:\s*SG-{re.escape(sd_id)}\.{re.escape(reg)}\b", text):
        return []
    block = None
    for m in re.finditer(r"```yaml\n(.*?)```", text, re.S):
        if re.search(rf"id:\s*SG-{re.escape(sd_id)}\.{re.escape(reg)}\b", m.group(1)):
            block = m.group(1)
            break
    if block is None:
        raise ValueError(
            f"{sd_id}/regs/{reg}.md: Sub-SO id SG-{sd_id}.{reg} cited "
            f"but its yaml card block is missing — fix the corpus module"
        )
    m = re.search(rf"source_SR:\s*([^\n]*)", block)
    if not m:
        raise ValueError(
            f"{sd_id}/regs/{reg}.md: source_SR missing from the Sub-SO card SG-{sd_id}.{reg}"
        )
    rest = m.group(1).strip()
    if rest:
        blob = rest
    else:  # block list
        blob_lines = []
        for line in block[m.end():].splitlines():
            s = line.strip()
            if s.startswith("- "):
                blob_lines.append(s[2:])
            elif blob_lines:
                break
        blob = " ".join(blob_lines)
    token = _sr_token(str(repo), reg)
    ids = re.findall(rf"{re.escape(token)}-[\w.]+", blob)
    if not ids:
        raise ValueError(
            f"{sd_id}/regs/{reg}.md: source_SR {rest!r} contains no {token}-NNN id (fix the corpus module)"
        )
    if set(re.findall(r"SR-[A-Za-z0-9]+-[\w.]+", blob)) - set(ids):
        raise ValueError(
            f"{sd_id}/regs/{reg}.md: source_SR {rest!r} cites an id of another regulation's SR series (corpus error)"
        )
    return ids


# --------------------------------------------------------------------------
# mapping store -> control ids
# --------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _store_index(repo_str: str, reg: str) -> dict[str, dict]:
    path = Path(repo_str) / "baseline" / "MAPPINGS" / "sr_control_mappings" / f"{reg}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {sr["sr_id"]: sr for sr in data.get("srs", [])}


@lru_cache(maxsize=None)
def _sr_token(repo_str: str, reg: str) -> str:
    """The SR-id token the corpus and the store actually use for `reg`."""
    idx = _store_index(repo_str, reg)
    for sr_id in idx:
        m = re.match(r"(SR-[A-Za-z0-9]+)-\d", sr_id)
        if m:
            return m.group(1)
    return f"SR-{reg}"


def _sr(repo: Path, reg: str, sr_id: str) -> dict:
    idx = _store_index(str(repo), reg)
    if sr_id not in idx:
        raise ValueError(f"{sr_id} not found in the mapping store {reg}.json")
    return idx[sr_id]


def goal_anchors(repo: Path, sd_id: str, baseline_sources: list[str]) -> list[str]:
    """Published anchors for one goal row (§3 column): the ordered union of the
    nist_csf sets of the source_SRs of each cited Sub-SO, plus the nist_pf set
    of GDPR-derived sources (R8 — PF accompanies GDPR obligations only; the
    other regulations publish no PF, so nothing else may cite it)."""
    out: list[str] = []
    for bs in baseline_sources:
        reg = bs.rsplit(".", 1)[1].strip("` ")
        if reg not in REGULATIONS:
            raise ValueError(f"{sd_id}: Baseline source {bs!r} ends in unknown regulation {reg!r}")
        axes = ["nist_csf"] + (["nist_pf"] if reg == "GDPR" else [])
        for sr_id in sources_of(repo, sd_id, reg):
            sr = _sr(repo, reg, sr_id)
            for ax in axes:
                for c in sr.get(ax) or []:
                    if c not in out:
                        out.append(c)
    return out


# --------------------------------------------------------------------------
# CONTROLS JSONs -> §6 tables
# --------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _controls_index(repo_str: str, ref: str) -> dict[str, Path]:
    root = Path(repo_str) / "baseline" / "CONTROLS" / ref
    return {p.stem: p for p in root.rglob("*.json")}


def control_meta(repo: Path, axis: str, cid: str) -> dict[str, str]:
    ref = REF_DIRS[axis]
    p = _controls_index(str(repo), ref).get(cid)
    if p is None:
        raise ValueError(f"control {cid} not found under CONTROLS/{ref}/ (R2b)")
    d = json.loads(p.read_text(encoding="utf-8"))
    text = " ".join((d.get("subcategory_text") or "").split())
    if len(text) > DESC_MAX:
        text = text[:DESC_MAX].rstrip() + "…"
    return {
        "function": d.get("function", "—"),
        "text": text,
        "path": f"{PATH_ALIAS[ref]}/{d.get('function', '—')}/{cid}.json",
    }


def sd_control_sections(repo: Path, sd_id: str, confirmed: list[str]) -> list[dict]:
    """§6 tables for one sub-domain."""
    axes: list[tuple[str, str]] = [("nist_csf", "NIST CSF 2.0 controls")]
    if "GDPR" in confirmed:
        axes.append(("nist_pf", "NIST PF 1.0 controls"))
    if "AI_Act" in confirmed:
        axes.append(("nist_airmf", "NIST AI RMF controls"))
    confirmed_eff = [r for r in REGULATIONS if r in confirmed]
    per_axis: dict[str, list[str]] = {ax: [] for ax, _ in axes}

    def absorb(sr: dict) -> None:
        for ax, _ in axes:
            for c in sr.get(ax) or []:
                if c not in per_axis[ax]:
                    per_axis[ax].append(c)

    for sr in anchor_slice(repo, sd_id, confirmed_eff):
        absorb(sr)
    for reg in confirmed_eff:
        if not carries_reg_card(repo, sd_id, reg):
            continue
        for sr_id in sources_of(repo, sd_id, reg):
            absorb(_sr(repo, reg, sr_id))
    sections = []
    for ax, title in axes:
        rows = []
        for cid in per_axis[ax]:
            meta = control_meta(repo, ax, cid)
            rows.append({
                "function": meta["function"],
                "id": cid,
                "text": meta["text"],
                "path": meta["path"],
            })
        sections.append({"title": title, "rows": rows})
    return sections


# --------------------------------------------------------------------------
# Track B tier derivation (deterministic matrix + case overrides)
# --------------------------------------------------------------------------

def track_b_rows(fact: dict, selected: list[str], overrides: dict[str, dict]) -> list[dict]:
    """§5 rows: scale from the fact sheet, inheritability/priority from the
    defaults + per-sub-domain case overrides, tier from the matrix."""
    try:
        n_emp = int(fact.get("size_employees", 0))
    except (TypeError, ValueError):
        raise ValueError(
            "fact sheet size_employees is not an integer — Track B scale cannot be derived (R6: no invention)"
        )
    scale = "MICRO" if n_emp < 50 else "MEDIUM" if n_emp < 250 else "LARGE"
    if scale not in TRACK_B_MATRIX:
        raise ValueError(
            f"no Track B matrix rows defined for scale {scale} — extend TRACK_B_MATRIX before running this company"
        )
    rows = []
    for sd in sorted(selected):
        ov = overrides.get(sd, {})
        inh = ov.get("inheritability", "BUILD_REQUIRED")
        pri = ov.get("priority", "MUST")
        tier = TRACK_B_MATRIX[scale].get(pri, {}).get(inh)
        if tier is None:
            raise ValueError(
                f"Track B: no matrix cell for {scale} × {pri} × {inh} ({sd}) — extend TRACK_B_MATRIX"
            )
        rows.append({
            "subdomain": sd,
            "scale": scale,
            "inheritability": inh,
            "priority": pri,
            "tier": tier,
            "rationale": f"matrix row {scale} × {pri} × {inh} = {tier}" + (" (case override)" if ov else ""),
        })
    return rows


def parse_overrides(raw) -> dict[str, dict]:
    """case.yaml `track_b_overrides:` entries 'D-XX.Y: key=VALUE[, key=VALUE]'."""
    out: dict[str, dict] = {}
    for item in raw or []:
        m = re.match(r"\s*([A-Za-z0-9.\-]+)\s*:\s*(.+)", str(item))
        if not m:
            raise ValueError(f"unparseable Track B override: {item!r}")
        sd, rest = m.group(1), m.group(2)
        ov = out.setdefault(sd, {})
        for kv in rest.split(","):
            k, _, v = kv.partition("=")
            ov[k.strip()] = v.strip()
    return out
