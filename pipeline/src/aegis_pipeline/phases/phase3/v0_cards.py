"""aegis_pipeline.phases.phase3.v0_cards — candidate functional card loader.

V0 is a human input and this module never writes it. Only the id, name and
description are read, because that is all a verdict needs: whether a card can
carry an objective.
"""
from __future__ import annotations

import re
from pathlib import Path


def load_v0_cards(doc01: Path) -> list[dict]:
    """The candidate carrier pool, read from the frozen V0 deliverable.

    Constraints live in V1/V2 and are deliberately not shown — a verdict that can
    see the security constraints it is judging has already been anchored, and the
    question being asked is whether the functional card covers the obligation at all.
    """
    cards, current = [], None
    for line in doc01.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\*\*ID:\*\*\s*(R\d+\.\d+)\s*\*\*Name:\*\*\s*(.+?)\s*\|", line)
        if m:
            current = {"id": m.group(1), "name": m.group(2), "description": ""}
            cards.append(current)
            continue
        if current is not None:
            d = re.match(r"^\|\s*\*\*Description:\*\*\s*(.+?)\s*\|", line)
            if d:
                current["description"] = d.group(1)
    return cards


def resolve_v0_doc(run_dir: Path, repo: Path, case_id: str | None = None,
                   source: str | None = None) -> Path:
    """Resolve the path to the V0 Doc01 deliverable.

    `source` selects the baseline explicitly instead of by accident:

    * `None` (auto) — run-local first, frozen case baseline as fallback;
    * `"frozen"` — the case baseline always, even when a generated one exists
      (model comparisons must run on the identical functional baseline);
    * `"generated"` — the run-local deliverable only; a missing one is an
      error at the caller, never a silent fall back to the frozen corpus
      (mixing baselines inside one run is the defect this flag exists to
      make unreachable).
    """
    local_v0 = run_dir / "outputs" / "phase3" / "v0_functional_baseline" / "Doc01_Requirements_Elicitation_and_PUC.md"
    if source != "frozen":
        if local_v0.is_file():
            return local_v0

        local_spec = run_dir / "outputs" / "phase3" / "v0_functional_baseline" / "Doc01_Requirements_Specification.md"
        if local_spec.is_file():
            return local_spec

    if source != "generated" and case_id:
        case_v0 = (
            repo / "cases" / case_id / "03_PHASE3_SPEC"
            / "part1_security_privacy" / "v0_functional_baseline"
            / "Doc01_Requirements_Elicitation_and_PUC.md"
        )
        if case_v0.is_file():
            out_dir = run_dir / "outputs" / "phase3" / "v0_functional_baseline"
            out_dir.mkdir(parents=True, exist_ok=True)
            copied_doc = out_dir / "Doc01_Requirements_Elicitation_and_PUC.md"
            if not copied_doc.is_file():
                import shutil
                shutil.copy2(case_v0, copied_doc)
                companion = case_v0.parent / "Doc02_System_Use_Cases.md"
                if companion.is_file() and not (out_dir / "Doc02_System_Use_Cases.md").is_file():
                    shutil.copy2(companion, out_dir / "Doc02_System_Use_Cases.md")
            return copied_doc

    return local_v0


def v0_source(run_dir: Path) -> str | None:
    """The run's declared V0 source from config.json (`None` = auto)."""
    from aegis_pipeline.core.config import load

    value = load(run_dir).get("v0_source")
    return str(value) if value in ("frozen", "generated") else None


def ensure_v0_pool(run_dir: Path, repo: Path, case_id: str | None = None,
                   source: str | None = None, seed: bool = True) -> list[dict]:
    """The one V0 reader: seed `steps/phase3/cards/` once, then always read it.

    Every Phase 3 consumer (map, propose, gate, weave) goes through here, so a
    run cannot read the frozen corpus in one stage and the generated baseline
    in the next. Returns the candidate cards. `seed=False` is the read-only
    variant the exit gate uses — the gate is a pure function of the disk and
    must not create state as a side effect of judging it.
    """
    import json
    cards_dir = run_dir / "steps" / "phase3" / "cards"
    existing_cards = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(cards_dir.glob("R*.json"))] \
        if cards_dir.is_dir() else []
    if existing_cards:
        return [c["card"] if "card" in c else c for c in existing_cards]

    v0_doc = resolve_v0_doc(run_dir, repo, case_id, source=source)
    if not v0_doc.is_file():
        if source == "generated":
            raise ValueError(
                "v0-source=generated but the run has no V0 deliverable — "
                "run --stage p3a_cards first (falling back to the frozen "
                "baseline here would mix baselines inside one run)"
            )
        return []
    cards = load_v0_cards(v0_doc)
    if not seed:
        return cards
    cards_dir.mkdir(parents=True, exist_ok=True)
    for c in cards:
        cid = c["id"]
        c_path = cards_dir / f"{cid.replace('.', '_')}.json"
        if not c_path.is_file():
            c_path.write_text(json.dumps({"card": c}, indent=2), encoding="utf-8")
    return cards

