#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.goals — Stage P4 goal derivation and content quality checks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import (
    REGULATIONS,
    carries_reg_card,
    confirmed_regulations,
    domain_dir,
    sub_so_objective,
)
import quality
from aegis_pipeline.phases.phase1.common import (
    canonical_reg,
    extract_fenced,
    one_reg,
    parse_md_table,
)

PATTERNS = {"achieve", "cease", "maintain", "avoid", "optimize"}

PROPERTY_ALIASES = {
    "confidentiality": "c",
    "integrity": "i",
    "availability": "a",
    "privacy right": "privacy-right",
    "privacy-right": "privacy-right",
    "accountability": "accountability",
    "c": "c",
    "i": "i",
    "a": "a",
}

PROPERTY_LONG = {
    "c": "Confidentiality",
    "i": "Integrity",
    "a": "Availability",
    "privacy-right": "Privacy Right",
    "accountability": "Accountability",
}

GOAL_COLUMNS_EMIT = (
    "ID",
    "Adjusted goal",
    "Company implication",
    "Pattern",
    "Property",
    "Parent goal",
    "Baseline source",
    "Regulatory source",
    "Adjustment",
)

GOAL_COLUMNS_DOC = (
    "AG ID",
    "Adjusted Goal",
    "Company implication",
    "Pattern",
    "Property",
    "Parent Goal",
    "Regulation",
    "Articles",
    "Control Anchors",
    "Adjustment",
)


def goal_table_header(columns: tuple[str, ...] = GOAL_COLUMNS_DOC) -> str:
    """A markdown table's header row plus its separator, from a column list."""
    return f"| {' | '.join(columns)} |\n" + f"|{'|'.join('---' for _ in columns)}|"


def parse_p4(answer: str, sd_id: str, expect_id: bool = True) -> dict:
    """Parse and validate stage P4 goal derivation table."""
    md = extract_fenced(answer, "markdown")
    m5 = re.search(r"^##\s+§5\b", md, re.M)
    if not m5:
        raise ValueError("P4 answer missing the '## §5' section (assumptions/open questions)")
    goals_part, assum_part = md[:m5.start()], md[m5.start():]

    rows = parse_md_table(goals_part)
    goals = []
    seq = 0
    last_reg_idx = -1
    for cells in rows:
        if not cells:
            continue
        idm = re.match(r"`?(AG-D-\d{2}\.\d-\d{3})`?", cells[0].replace("*", "").strip())
        if not idm:
            if expect_id:
                continue
            gid = f"AG-{sd_id}-NNN"
        else:
            gid = idm.group(1)
        if len(cells) != len(GOAL_COLUMNS_EMIT):
            raise ValueError(
                f"goal row {gid} has {len(cells)} columns, expected "
                f"{len(GOAL_COLUMNS_EMIT)} ({' | '.join(GOAL_COLUMNS_EMIT)}) — "
                "control anchors are derived by code, not emitted"
            )
        seq += 1
        if expect_id:
            gid = idm.group(1)
            expected = f"AG-{sd_id}-{seq:03d}"
            if gid != expected:
                raise ValueError(f"goal IDs must be sequential from 001: expected {expected}, got {gid}")
        if any("|" in c for c in cells):
            raise ValueError(
                f"{gid}: a cell contains a literal '|' — markdown tables cannot carry it; rephrase using commas or semicolons"
            )
        pattern = cells[3].strip().lower()
        if pattern not in PATTERNS:
            raise ValueError(f"invalid pattern {pattern!r} on {gid}")
        prop_raw = " ".join(cells[4].strip().lower().split())
        prop = PROPERTY_ALIASES.get(prop_raw) or PROPERTY_ALIASES.get(prop_raw.replace(" ", "-"))
        if prop is None:
            raise ValueError(f"invalid property {cells[4]!r} on {gid}")
        parent = cells[5].replace("`", "").strip()
        if not re.fullmatch(rf"SO-{re.escape(sd_id)}\.HL", parent):
            raise ValueError(f"invalid parent goal {parent!r} on {gid} (expected SO-{sd_id}.HL)")
        reg = one_reg(cells[6], sd_id)
        reg_idx = REGULATIONS.index(reg)
        if reg_idx < last_reg_idx:
            raise ValueError(
                f"{gid}: regulation slots must follow the canonical order "
                f"{' → '.join(REGULATIONS)} (got {REGULATIONS[last_reg_idx]} before {reg})"
            )
        last_reg_idx = reg_idx
        if not cells[7].strip():
            raise ValueError(f"empty regulatory source on {gid} (R2a)")
        if not cells[8].strip():
            raise ValueError(f"empty adjustment record on {gid} (R3/ADR-003 D1)")
        goals.append({
            "id": gid,
            "goal": cells[1],
            "implication": cells[2],
            "pattern": pattern,
            "property": prop,
            "parent": parent,
            "baseline_source": f"SG-{sd_id}.{reg}",
            "regulation": reg,
            "source": cells[7].strip(),
            "adjustment": cells[8].strip(),
        })
    if not goals:
        if re.search(r"(?i)none\s*[—-]\s*no sub-so", md):
            assumptions = []
            for line in assum_part.splitlines():
                s = line.strip()
                if s.startswith(">") or s.startswith("- "):
                    if s.lower().rstrip(".") not in ("- none", "> none"):
                        assumptions.append(s)
            return {"md": md, "goals": [], "assumptions": assumptions}
        raise ValueError(
            f"no AG-D-{sd_id}-NNN rows found in P4 answer (if this module "
            f"carries no Sub-SO for the confirmed regulations, answer with "
            f"the marker 'None — no Sub-SO for the confirmed regulations.')"
        )

    assumptions = []
    for line in assum_part.splitlines():
        s = line.strip()
        if s.startswith(">") or s.startswith("- "):
            if s.lower().rstrip(".") not in ("- none", "> none"):
                assumptions.append(s)

    return {"md": md, "goals": goals, "assumptions": assumptions}


def check_p4_quality(repo: Path, run_dir: Path, parsed: dict, sd_id: str) -> dict:
    """Content gates: Sub-SO restatements must retain obligation, stay grounded,
    avoid tech leakage, and provide specific implications."""
    goals = parsed["goals"]
    confirmed = confirmed_regulations(run_dir)
    expected_regs = [reg for reg in confirmed if carries_reg_card(repo, sd_id, reg)]
    coverage = quality.check_subso_coverage(goals, expected_regs)
    if coverage:
        raise ValueError("; ".join(coverage))

    baselines = {reg: sub_so_objective(repo, sd_id, reg) for reg in expected_regs}
    steps_dir = run_dir / "steps"
    sources = [baselines[r] for r in expected_regs]
    for name in ("fact_sheet.yaml", "framing.md"):
        f = steps_dir / name
        if f.exists():
            sources.append(f.read_text(encoding="utf-8"))
    other = [
        g["implication"]
        for jf in sorted((steps_dir / "goals").glob("*.json"))
        for g in json.loads(jf.read_text()).get("goals", [])
    ]
    all_findings = []
    for g in goals:
        peers = other + [o["implication"] for o in goals if o["id"] != g["id"]]
        findings = quality.run_row(g, baselines, sources, peers)
        if findings:
            all_findings.extend(f"{g['id']}: {m}" for m in findings)
    if all_findings:
        raise ValueError("; ".join(all_findings))
    coverage = quality.check_subso_coverage(goals, expected_regs)
    if coverage:
        raise ValueError("; ".join(coverage))
    return parsed


# --------------------------------------------------------------------------
# Prompt Wrap and Instructions
# --------------------------------------------------------------------------

def p4_extra_instruction(sd_id: str, subso_ids: list[str] | None = None) -> str:
    if subso_ids is None:
        subso_ids = []
    if not subso_ids:
        return (
            f"Wrap your answer: return ONLY one ```markdown fenced block containing "
            f"(a) the heading `### {sd_id} — <canonical name>` followed by the single line "
            f"`None — no Sub-SO for the confirmed regulations.`, and (b) a heading `## §5` "
            f"with `None.` READ THIS: the module header saying a regulation 'applies' means "
            f"the regulation is IN SCOPE for the company — NOT that this sub-domain restates "
            f"a duty under it. 11 of the 38 sub-domains carry such a module with NO Sub-SO "
            f"card (the file ends with '(no ... Sub-SO or requirements in this sub-domain)'). "
            f"Therefore this module has NO goal rows. Do not invent one, and do not cite "
            f"`SG-{sd_id}.HL` as a baseline source. Nothing else."
        )
    return (
        f"Wrap your answer: return ONLY one ```markdown fenced block containing "
        f"(a) the heading `### {sd_id} — <canonical name>` and the "
        f"{len(GOAL_COLUMNS_EMIT)}-column goal table "
        f"(`{' | '.join(GOAL_COLUMNS_EMIT)}`), and (b) a heading `## §5` "
        f"listing only `> ASSUMPTION:` blockquotes and open questions this sub-domain owes "
        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "
        f"TERMINATION: after the `## §5` section the answer is COMPLETE — emit the "
        f"closing fence on the next line and stop. No table continuation, no notes, no "
        f"second §5, no text of any kind after the closing fence; an answer that keeps "
        f"writing past §5 hits the output cap and is discarded whole. Column rules: this module "
        f"declares EXACTLY {len(subso_ids)} Sub-SO(s) to restate — "
        f"{', '.join(subso_ids)} — and no others; write one row per listed id, in that "
        f"order. A regulation NOT in that list has no duty here — EVEN IF it is confirmed "
        f"for the company and even if its module file exists: 28 of the 38 sub-domains "
        f"carry an AI_Act file that is only a stub, ending in '(no AI Act Sub-SO or "
        f"requirements in this sub-domain)'. A stub is not a card; writing a row citing "
        f"a regulation absent from the list above is a hard failure (R8), and the stub "
        f"is exactly the trap. Adjusted goal = a declarative, normative security goal restating that Sub-SO's "
        f"Objective (2+ sentences, same obligation content). DO NOT prepend the company name "
        f"(do NOT write '<Company> shall...' or '<Company> must...'). Do NOT paste or embed the "
        f"Sub-SO Objective verbatim as a sentence (do not copy the baseline and append company calibration) — "
        f"reformulate the duty in the company's sentence structure, keeping roughly half the Sub-SO's vocabulary. "
        f"Express the goal objectively and impersonally, as a property the system holds rather than as an instruction issued "
        f"by someone; "
        f"Company implication = what this duty concretely means for THIS company given "
        f"the §2 framing and fact sheet (1-2 sentences explaining operational impact, roles and scope); "
        f"Baseline source = the single corpus Sub-SO id the row restates "
        f"(e.g. `SG-{sd_id}.GDPR`); Property MUST be one of C, I, A, privacy-right, "
        f"accountability. Control anchors are derived by code — do NOT emit any. "
        f"ADJUSTMENT — provide the substantive proportionality justification for THIS duty "
        f"(e.g. 'inherited from supplier-managed hosting under shared responsibility', 'role separation "
        f"achieved via platform IAM roles rather than disjoint full-time personnel', 'minimum 5-year support "
        f"period applies unconditionally per statutory floor'), or use badge `proportional: <rationale>` / "
        f"`inherited: <supplier>` / `flagged: <question>` / '—' if it applies directly under the §2 general "
        f"framing without duty-specific deviations. Do not paste empty 'unchanged' labels without rationale. "
        f"Nothing else."
    )


P4_ADJUSTMENT_MENU = (
    "ADJUSTMENT — pick exactly one of three values: `unchanged — fits as stated` | "
    "`narrowed: <what> — because <company fact>` | `flagged: <open question>`. "
    "Choose the value that best describes this row. Nothing else."
)
P4_ADJUSTMENT_BADGES = (
    "ADJUSTMENT — choose exactly one classification badge: `verbatim` | `proportional` | `inherited` | `flagged`. "
    "Do NOT append explanations here — the justification belongs entirely in the Company implication column. Nothing else."
)
P4_ADJUSTMENT_VARIANTS = {"menu": P4_ADJUSTMENT_MENU, "badges": P4_ADJUSTMENT_BADGES}

P4_STYLE_MARKER = "Express the goal objectively and impersonally"
P4_STYLE_META = (
    "Express the goal objectively and impersonally: state the duty that must hold "
    "across this entity's operational scope, keeping the Sub-SO's own obligation "
    "vocabulary but rebuilt into this company's sentence structure. Do not paste the "
    "baseline — a goal that is a near-verbatim copy of the Sub-SO objective restates "
    "nothing about this company and is rejected. "
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences explaining operational impact, roles "
    "and scope); Baseline source = the single corpus Sub-SO id the row restates "
    "(e.g. `SG-{sd_id}.GDPR`); Property MUST be one of C, I, A, privacy-right, "
    "accountability. Control anchors are derived by code — do NOT emit any. "
    "ADJUSTMENT — record the decision this duty forces on THIS company and the reason "
    "behind it: whether the duty holds as the baseline states it, is narrowed by a "
    "company fact you can name, or cannot be decided from the input. Justify "
    "proportionality against the §2 framing — the company's scale, its operational "
    "roles, and which capabilities it inherits from others — and never paste a label "
    "without the reasoning behind it. Nothing else."
)
P4_STYLE_VARIANTS = {"meta": P4_STYLE_META}

P4_IMPLICATION_MARKER = (
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences explaining operational impact, "
    "roles and scope)"
)
P4_IMPLICATION_CONCRETE = (
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences). Name one checkable artefact "
    "that appears in the fact sheet — a named system, a named supplier, a named "
    "role, a named volume, a named site — and say what this duty does to it. "
    "\"Operational impact, roles and scope\" in the abstract is not an answer: a "
    "sentence that would read the same for a company of any size or sector has "
    "not been written. If no artefact in the fact sheet is touched by this duty, "
    "write that it is not, in one clause, and keep it short"
)
P4_IMPLICATION_VARIANTS = {"concrete": P4_IMPLICATION_CONCRETE}


def _p4_instruction(
    sd_id: str,
    subso_ids: list[str] | None = None,
    adjustment_variant: str | None = None,
    style_variant: str | None = None,
    implication_variant: str | None = None,
) -> str:
    base = p4_extra_instruction(sd_id, subso_ids)
    if implication_variant:
        replacement = P4_IMPLICATION_VARIANTS.get(implication_variant)
        if replacement is None:
            raise ValueError(
                f"p4 implication override: unknown variant {implication_variant!r} "
                f"(known: {sorted(P4_IMPLICATION_VARIANTS)})"
            )
        head, sep, _tail = base.partition(P4_IMPLICATION_MARKER)
        if not sep:
            raise ValueError(
                "p4 implication override: the shipped base instruction no longer "
                f"contains the expected marker ({P4_IMPLICATION_MARKER[:48]!r}…) — "
                "refusing to run with a variant that would be silently ignored"
            )
        base = f"{head}{replacement}" + _tail
    if style_variant:
        replacement = P4_STYLE_VARIANTS.get(style_variant)
        if replacement is None:
            raise ValueError(
                f"p4 instruction override: unknown style variant {style_variant!r} "
                f"(known: {sorted(P4_STYLE_VARIANTS)})"
            )
        head, sep, _tail = base.partition(P4_STYLE_MARKER)
        if not sep:
            raise ValueError(
                f"p4 style override: the shipped base instruction no longer contains "
                f"the expected marker {P4_STYLE_MARKER!r} — refusing to run with a "
                "variant that would be silently ignored"
            )
        base = f"{head}{replacement.format(sd_id=sd_id)}"
    if not adjustment_variant:
        return base
    replacement = P4_ADJUSTMENT_VARIANTS.get(adjustment_variant)
    if replacement is None:
        return base
    head, sep, _tail = base.partition("ADJUSTMENT — choose exactly one classification badge")
    if not sep:
        raise ValueError(
            "p4 adjustment override: the shipped base instruction no longer "
            "contains the expected ADJUSTMENT marker — refusing to run with a "
            "variant that would be silently ignored"
        )
    return f"{head}{replacement}"
