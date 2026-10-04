#!/usr/bin/env python3
"""controls.py — deterministic control derivation for the Phase 1 deliverable.

Resolves the chain  Sub-SO -> source_SR -> mapping store -> CONTROLS JSONs
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
from functools import lru_cache
from pathlib import Path

from compose import (REGULATIONS, anchor_slice, carries_reg_card, domain_dir,
                     reg_module_path)

REF_DIRS = {"nist_csf": "NIST_CSF_2.0", "nist_pf": "NIST_PF", "nist_airmf": "NIST_AI_RMF"}
PATH_ALIAS = {"NIST_CSF_2.0": "NIST_CSF", "NIST_PF": "NIST_PF", "NIST_AI_RMF": "NIST_AI_RMF"}
DESC_MAX = 90

# Track B tier matrix — the observable rules of the golden case (Doc02 §5.1/§5.2):
# tier = matrix[scale][priority][inheritability]; SHOULD/COULD drop one tier.
# Scales beyond the observed rows fail loudly until the researcher extends the
# matrix (flag-not-drop: never invent a tier).
TRACK_B_MATRIX = {
    "MICRO": {
        "MUST": {"BUILD_REQUIRED": "LIGHTWEIGHT", "INHERITABLE": "MINIMAL"},
        "SHOULD": {"BUILD_REQUIRED": "DEFERRED", "INHERITABLE": "DEFERRED"},
        "COULD": {"BUILD_REQUIRED": "DEFERRED", "INHERITABLE": "DEFERRED"},
    },
    # LARGE — derived from the researcher's own proportionality statement in
    # cases/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md
    # (§2 Size framing: "450-person workforce, ~EUR 120M revenue ... tiers
    # RIGOROUS/STANDARD ... DEFERRED unavailable at security staffing > 1 FTE").
    # That deliverable describes a 450-employee company, which this module's
    # threshold (line 219: <50 MICRO, <250 MEDIUM, else LARGE — the EU
    # 2003/361 bands) classifies as LARGE, so RIGOROUS/STANDARD are the LARGE
    # tier names. Case_02's prose says "MEDIUM scale"; the intake calls it
    # "Medium-Large (MEDIUM scale band for proportionality)" while its own
    # threshold check reads "450 | >250 = Large". The band and the word disagree
    # — flagged for the researcher; the CODE'S threshold wins here, so both
    # Case_02 and Case_03 resolve to LARGE.
    # The read: at this scale the organisation can BUILD controls outright
    # (RIGOROUS for must-haves), an inherited capability is a STANDARD
    # responsibility, the should/could tail thins to LIGHTWEIGHT/MINIMAL, and
    # deferral stops being proportionate once there is a real security team.
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
            f"traceability chain (R2/R2b).")
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
        raise ValueError(f"{sd_id}/regs/{reg}.md: Sub-SO id SG-{sd_id}.{reg} cited "
                         f"but its yaml card block is missing — fix the corpus module")
    m = re.search(rf"source_SR:\s*([^\n]*)", block)
    if not m:
        raise ValueError(f"{sd_id}/regs/{reg}.md: source_SR missing from the "
                         f"Sub-SO card SG-{sd_id}.{reg}")
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
    # the corpus renders source_SR as scalar, [inline], comma-, plus- or
    # block-separated — extract every well-formed id regardless of separator.
    # The token comes from the mapping store, not from the regulation name:
    # the store renders the AI Act series as SR-AIACT-NNN (Case_02).
    token = _sr_token(str(repo), reg)
    ids = re.findall(rf"{re.escape(token)}-[\w.]+", blob)
    if not ids:
        raise ValueError(f"{sd_id}/regs/{reg}.md: source_SR {rest!r} contains no "
                         f"{token}-NNN id (fix the corpus module)")
    if set(re.findall(r"SR-[A-Za-z0-9]+-[\w.]+", blob)) - set(ids):
        raise ValueError(f"{sd_id}/regs/{reg}.md: source_SR {rest!r} cites an id "
                         f"of another regulation's SR series (corpus error)")
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
    """The SR-id token the corpus and the store actually use for `reg`.

    It is NOT always the regulation name. The mapping store renders the AI Act
    series as `SR-AIACT-NNN` (no underscore) while the regulation is named
    `AI_Act` everywhere else, and the corpus modules are consistent with the
    store. Deriving the token from the store removes that assumption: the code
    stops relying on a regulation NAME being a valid identifier, which held for
    GDPR / CRA / NIS2 / DORA and broke the moment AI_Act was confirmed
    (Case_02, 203 references across 8 modules).
    """
    idx = _store_index(repo_str, reg)
    for sr_id in idx:
        m = re.match(r"(SR-[A-Za-z0-9]+)-\d", sr_id)
        if m:
            return m.group(1)
    # empty store: fall back to the name, so the error stays a corpus error
    return f"SR-{reg}"


def _sr(repo: Path, reg: str, sr_id: str) -> dict:
    idx = _store_index(str(repo), reg)
    if sr_id not in idx:
        raise ValueError(f"{sr_id} not found in the mapping store {reg}.json")
    return idx[sr_id]


def goal_anchors(repo: Path, sd_id: str, baseline_sources: list[str]) -> list[str]:
    """CSF 2.0 anchors for one goal row (§3 column): ordered union of the
    nist_csf sets of the source_SRs of each cited Sub-SO (dedup, stable)."""
    out: list[str] = []
    for bs in baseline_sources:
        reg = bs.rsplit(".", 1)[1].strip("` ")
        if reg not in REGULATIONS:
            raise ValueError(f"{sd_id}: Baseline source {bs!r} ends in unknown "
                             f"regulation {reg!r}")
        for sr_id in sources_of(repo, sd_id, reg):
            for c in _sr(repo, reg, sr_id).get("nist_csf") or []:
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
    return {"function": d.get("function", "—"), "text": text,
            "path": f"{PATH_ALIAS[ref]}/{d.get('function', '—')}/{cid}.json"}


def sd_control_sections(repo: Path, sd_id: str, confirmed: list[str]) -> list[dict]:
    """§6 tables for one sub-domain: per axis, the ordered union of control ids
    over (a) ALL SRs the mapping store binds to this sub-domain for the
    confirmed regulations (applicability filters the whole control set) and
    (b) the source_SRs cited by the sub-domain's Sub-SO cards (covers store
    rows whose sub_domain tagging is missing), resolved against the CONTROLS
    referential."""
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
    # A confirmed regulation is confirmed for the COMPANY; a sub-domain only
    # carries the cards that actually reach it. D-06.4 has no AI_Act card even
    # though Case_02 confirms AI_Act, and asking for its source_SRs raised
    # FileNotFoundError on a path the corpus never promised (p5 of
    # run_sec02_p1_1979370, job 1979980). Skipping here is the correct semantic:
    # the module asserts no AI_Act baseline goal, so it contributes no AI_Act
    # control rows and the §6 table stays a union over what the module cites.
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
            rows.append({"function": meta["function"], "id": cid,
                         "text": meta["text"], "path": meta["path"]})
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
        raise ValueError("fact sheet size_employees is not an integer — Track B "
                         "scale cannot be derived (R6: no invention)")
    scale = "MICRO" if n_emp < 50 else "MEDIUM" if n_emp < 250 else "LARGE"
    if scale not in TRACK_B_MATRIX:
        raise ValueError(f"no Track B matrix rows defined for scale {scale} — "
                         f"extend TRACK_B_MATRIX before running this company")
    rows = []
    for sd in sorted(selected):
        ov = overrides.get(sd, {})
        inh = ov.get("inheritability", "BUILD_REQUIRED")
        pri = ov.get("priority", "MUST")
        tier = TRACK_B_MATRIX[scale].get(pri, {}).get(inh)
        if tier is None:
            raise ValueError(f"Track B: no matrix cell for {scale} × {pri} × {inh} "
                             f"({sd}) — extend TRACK_B_MATRIX")
        rows.append({"subdomain": sd, "scale": scale, "inheritability": inh,
                     "priority": pri, "tier": tier,
                     "rationale": f"matrix row {scale} × {pri} × {inh} = {tier}"
                                  + (" (case override)" if ov else "")})
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
