"""aegis_pipeline.phases.phase3b.threats — Etapa 2.2: STRIDE, LINDDUN, and the
risk arithmetic that lives in PYTHON.

The model identifies threats and classifies the mitigation Part 1 provides;
the CODE computes the residual. The measured way a register lies is a risk
that drops without a requirement behind it — `residual_from_mitigation` makes
that unreachable: an UNMITIGATED_GAP lowers nothing.
"""
from __future__ import annotations

import re

from aegis_pipeline.guards.quality_gates import check_no_technology
from aegis_pipeline.phases.phase3b.schemas import (
    LINDDUN,
    MITIGATION,
    STRIDE,
    check_threat_ids,
    residual_from_mitigation,
    risk_level,
)

FIELDS = ("Threat", "Category", "Inherent likelihood", "Inherent impact",
          "Mitigating requirements", "Mitigation assessment", "Defense mechanism or gap",
          "Statutory obligation")

RE_SCORE = re.compile(r"^[1-5]$")


def near_miss_ids(bad: str, accepted: set[str]) -> str:
    """The accepted Part 1 ids in the same D-XX.Y domain as a stray citation.
    The repair round learns the CONTRACT (which ids are legal) — which
    requirement actually mitigates the threat stays the model's call."""
    m = re.search(r"D-\d+\.\d+", bad)
    if not m:
        return ""
    same = sorted(x for x in accepted if m.group(0) in x)
    if not same:
        return ""
    return (f"; accepted Part 1 ids in {m.group(0)}: {', '.join(same[:5])}"
            + ("…" if len(same) > 5 else ""))


def _parse_blocks(answer: str) -> list[tuple[str, str]]:
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown")
    sections: list[tuple[str, str]] = []
    current: tuple[str, list[str]] | None = None
    for line in block.splitlines():
        if line.startswith("###"):
            if current:
                sections.append((current[0], "\n".join(current[1])))
            current = (line.lstrip("#").strip().strip("`"), [])
        elif current is not None:
            current[1].append(line)
    if current:
        sections.append((current[0], "\n".join(current[1])))
    return sections


def _fields(body: str, where: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in body.splitlines():
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line.strip())
        if m and m.group(1) in FIELDS:
            current = m.group(1)
            fields[current] = m.group(2).strip()
        elif current is not None and line.strip():
            fields[current] = (fields[current] + " " + line.strip()).strip()
    missing = [f for f in FIELDS if f not in fields]
    if missing:
        raise ValueError(f"{where}: missing field(s) {missing}")
    return fields


def parse_threats(answer: str, kind: str, accepted_ids: set[str],
                  index: dict) -> list[dict]:
    """L0 for a STRIDE (`kind='stride'`) or LINDDUN (`kind='linddun'`) call.

    One `### <DF-id | AST-id> T-n` section per threat. The category must be in
    the method's vocabulary; the scores are 1..5 ints the CODE re-reads; the
    mitigating requirements must be Part 1 ids; the assessment is the closed
    3-value enum; cited K3 ids must exist in the catalog (T8).
    """
    vocab = STRIDE if kind == "stride" else LINDDUN
    out = []
    for header, body in _parse_blocks(answer):
        m = re.match(r"^([\w.-]+)\s+(T-\d+)$", header)
        if not m:
            raise ValueError(f"threats: section header {header!r} is not `<target> T-<n>`")
        target, tid = m.group(1), m.group(2)
        f = _fields(body, f"threats [{tid}]")
        category = f["Category"]
        if category not in vocab:
            raise ValueError(f"threats [{tid}]: category {category!r} outside the {kind} vocabulary")
        l_inh, i_inh = f["Inherent likelihood"], f["Inherent impact"]
        if not RE_SCORE.match(l_inh) or not RE_SCORE.match(i_inh):
            raise ValueError(f"threats [{tid}]: inherent scores must be integers 1..5, got {l_inh!r}/{i_inh!r}")
        mitigators = [x.strip().strip("`") for x in f["Mitigating requirements"].split(",") if x.strip()]
        stray = [x for x in mitigators if x not in accepted_ids]
        if stray:
            hint = "".join(near_miss_ids(x, accepted_ids) for x in stray[:4])
            raise ValueError(f"threats [{tid}]: mitigating requirement(s) {stray[:4]} "
                             f"are not Part 1 ids{hint}")
        assessment = f["Mitigation assessment"]
        if assessment not in MITIGATION:
            raise ValueError(f"threats [{tid}]: assessment {assessment!r} outside {MITIGATION}")
        if assessment != "UNMITIGATED_GAP" and not mitigators:
            raise ValueError(f"threats [{tid}]: {assessment} with no mitigating requirement named")
        statutory = f["Statutory obligation"].strip().lower()
        if statutory not in ("yes", "no"):
            raise ValueError(f"threats [{tid}]: statutory obligation must be yes/no, got {statutory!r}")
        l_res, i_res = residual_from_mitigation(int(l_inh), int(i_inh), assessment)
        threat = {
            "id": tid, "target": target, "method": kind,
            "threat": f["Threat"], "category": category,
            "l_inh": int(l_inh), "i_inh": int(i_inh),
            "inherent_score": int(l_inh) * int(i_inh),
            "inherent_level": risk_level(int(l_inh) * int(i_inh)),
            "mitigating_requirements": mitigators,
            "mitigation_assessment": assessment,
            "defense": f["Defense mechanism or gap"],
            "statutory_obligation": statutory == "yes",
            "l_res": l_res, "i_res": i_res,
            "residual_score": l_res * i_res,
            "residual_level": risk_level(l_res * i_res),
            "k3_ids": sorted({x for rx in
                              (r"\bCWE-\d+\b", r"\bCAPEC-\d+\b", r"\bT\d{4}(?:\.\d{3})?\b",
                               r"\bD3-[A-Z]{2,6}\b", r"\bAML\.T\d{4}", r"\bTID-\d+\b")
                              for x in re.findall(rx, f"{f['Threat']} {f['Defense mechanism or gap']}")}),
        }
        t8 = check_threat_ids(f"{threat['threat']} {threat['defense']}", index)
        if t8:
            raise ValueError(f"threats [{tid}]: {t8[0]}")
        out.append(threat)
    if not out:
        raise ValueError("threats: zero threat sections parsed")
    return out


def parse_k3_mapping(answer: str, threats: list[dict], index: dict) -> dict[str, list[str]]:
    """L0 for the MITRE K3 mapping call: `### T-n` → comma-separated K3 ids."""
    threat_ids = {t["id"] for t in threats}
    mapping: dict[str, list[str]] = {}
    for header, body in _parse_blocks(answer):
        tid = header.strip().strip("`")
        if tid not in threat_ids:
            raise ValueError(f"K3 mapping: block {tid!r} is not a threat of this model")
        ids = sorted({x.strip().strip("`") for x in body.replace("\n", ",").split(",") if x.strip()})
        t8 = [f for f in check_threat_ids(" ".join(ids), index)]
        if t8:
            raise ValueError(f"K3 mapping [{tid}]: {t8[0]}")
        mapping[tid] = ids
    missing = [t["id"] for t in threats if t["id"] not in mapping]
    if missing:
        raise ValueError(f"K3 mapping: no block for {len(missing)} threat(s): {missing[:8]}")
    return mapping


def render_threats(threats: list[dict], kind: str, company: str,
                   k3: dict[str, list[str]] | None = None) -> str:
    """02_STRIDE / 03_LINDDUN — the deliverable, one table, risk computed."""
    title = ("02 — Technical Threat Analysis (STRIDE)" if kind == "stride"
             else "03 — Privacy Threat Analysis (LINDDUN)")
    lines = [
        "---",
        f"title: '{title} ({company})'",
        "generated_by: 'p3b_threats (onda D) — residual computed in Python'",
        "---",
        "",
        "| ID | Target | Category | Threat | L×I inherent | Level | Mitigating requirements | Assessment | L×I residual | Level |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for t in threats:
        lines.append(
            f"| `{t['id']}` | `{t['target']}` | {t['category']} | {t['threat'][:160]} "
            f"| {t['l_inh']}×{t['i_inh']}={t['inherent_score']} | {t['inherent_level']} "
            f"| {', '.join(f'`{r}`' for r in t['mitigating_requirements']) or '—'} "
            f"| {t['mitigation_assessment']} "
            f"| {t['l_res']}×{t['i_res']}={t['residual_score']} | {t['residual_level']} |")
    if k3 is not None:
        lines += ["", "## MITRE knowledge mapping (T8-verified)", "",
                  "| Threat | CWE | CAPEC | ATT&CK | D3FEND |", "|---|---|---|---|---|"]
        for t in threats:
            ids = k3.get(t["id"], [])
            by = {fam: ", ".join(i for i in ids if i.startswith(p))
                  for fam, p in (("CWE", "CWE-"), ("CAPEC", "CAPEC-"),
                                 ("ATT&CK", "T"), ("D3FEND", "D3-"))}
            lines.append(f"| `{t['id']}` | {by['CWE'] or '—'} | {by['CAPEC'] or '—'} "
                         f"| {by['ATT&CK'] or '—'} | {by['D3FEND'] or '—'} |")
    lines += ["", "## Residues (explicit)", ""]
    gaps = [t for t in threats if t["mitigation_assessment"] == "UNMITIGATED_GAP"]
    if gaps:
        for t in gaps:
            lines.append(f"- `{t['id']}` ({t['target']}): {t['defense'][:200]}")
    else:
        lines.append("- None — every threat names the requirement that mitigates it.")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_k3_mapping(threats: list[dict], k3: dict[str, list[str]], company: str) -> str:
    lines = [
        "---",
        f"title: '06 — MITRE Knowledge Mapping ({company})'",
        "generated_by: 'p3b_threats (onda D)'",
        "---",
        "",
        "Every identifier below resolves in `baseline/THREATS/_index.json` (guard T8).",
        "",
        "| Threat | K3 identifiers |",
        "|---|---|",
    ]
    for t in threats:
        ids = k3.get(t["id"], [])
        lines.append(f"| `{t['id']}` | {', '.join(f'`{i}`' for i in ids) or '—'} |")
    lines.append("")
    return "\n".join(lines) + "\n"
