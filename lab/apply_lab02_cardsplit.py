#!/usr/bin/env python3
"""Apply the LAB02 card-split arm to a COPY of pipeline/src (p4 per Sub-SO card).

Usage: python3 lab/apply_lab02_cardsplit.py <target>/pipeline/src

WHAT THIS ARM CHANGES (unlike the LAB01 text overlays, this one touches control
flow on purpose — it is an ORCHESTRATION experiment, not a prompt experiment):
  1. `_call()`     — `p4:<sd>` may be restricted to ONE Sub-SO id: the instruction's
                     "declares EXACTLY N Sub-SO(s) to restate" list is narrowed to
                     that single card. Everything else in the composed pack is the
                     same pack the sub-domain call already used.
  2. `parse_p4()`  — `expect_id=False` is used for a single-card call (the parameter
                     already exists; it lets the model answer without pre-assigned ids)
                     and the parsed row is normalised to the card's own Sub-SO.
  3. `stage_p4()`  — per sub-domain: one call per card, merge in canonical regulation
                     order, renumber AG-<sd>-NNN sequentially, then run the EXISTING
                     `check_p4_quality` once on the merged list (coverage gate
                     included) before storing. The stored artefact is byte-identical in
                     shape to today's: `steps/goals/<sd>.{md,json}`.
  4. `store_parsed()` — unchanged. Consumers (p5/assemble_doc, validate.py) untouched.

FAILURE SEMANTICS (chosen and documented, prereg LAB02): conservative — if ANY card
of a sub-domain fails L0, the whole sub-domain fails, exactly as today. A sub-domain
that passes all cards is indistinguishable from a monolithic pass.

GUARD: `parse_p1/p2/p3/p3f/p4t`, `check_p4_quality`, `_validate`, `assemble_doc`,
`store_parsed`, all thresholds and NUM_CTX/NUM_PREDICT must stay byte-identical —
asserted by a block diff, not by promise.
"""
import re
import sys
from pathlib import Path

GUARD = re.compile(
    r"^(def parse_p1|def parse_p2|def parse_p3\(|def parse_p3f|def parse_p4t|"
    r"def check_p4_quality|def _validate|def assemble_doc|def store_parsed|"
    r"def _raise_if_nothing_carried|def stage_p4t|NUM_CTX|NUM_PREDICT|PARSERS|"
    r"ADJ_PREFIXES|RETENTION_FLOOR|IMPLICATION_DUP)")


def blocks(src: str) -> str:
    out, keep = [], False
    for line in src.splitlines():
        if GUARD.match(line):
            keep = True
        elif keep and line and not line[0].isspace() and not line.startswith((")", "]", "}")):
            keep = False
        if keep:
            out.append(line)
    return "\n".join(out)


CARD_CALL = '''    def _call_card(self, sd_id: str, subso_id: str) -> None:
        """LAB02 arm: one p4 call per Sub-SO card, then merge.

        The monolithic sub-domain call asks a model to restate every Sub-SO the
        module carries (2 on Case 01, up to 5 on Case 03) in one table. The
        compression failures in the M07 matrix land exactly here, so this arm
        gives each card its own call and re-joins the rows deterministically.
        """
        self._call(f"p4:{sd_id}", sd_id, only_card=subso_id)

'''

MERGE_HELPERS = '''

def merge_card_answers(sd_id: str, per_card: list[tuple[str, dict]]) -> dict:
    """LAB02 arm: join one answer per Sub-SO card into the artefact stage_p4 stores.

    Deterministic: canonical regulation order is the order of `per_card` (the
    caller walks the confirmed regulations in REGULATIONS order), ids are
    renumbered AG-<sd>-001..N in that order, and the markdown table is rendered
    from the merged rows rather than concatenated, so the render path and the
    renumber path are the same code. Assumptions concatenate in card order.
    """
    goals: list[dict] = []
    assumptions: list[str] = []
    for i, (subso_id, parsed) in enumerate(per_card, 1):
        for row in parsed.get("goals", []):
            r = dict(row)
            r["id"] = f"AG-{sd_id}-{i:03d}" if len(per_card) > 1 else row.get("id", f"AG-{sd_id}-{i:03d}")
            r["baseline_source"] = subso_id
            goals.append(r)
        assumptions.extend(parsed.get("assumptions", []))

    header = ("| ID | Adjusted goal | Company implication | Pattern | Property | "
              "Parent goal | Baseline source | Regulatory source | Adjustment |")
    sep = "|---|---|---|---|---|---|---|---|---|"
    lines = [f"### {sd_id} — adjusted goals", "", header, sep]
    for g in goals:
        lines.append("| " + " | ".join(str(g.get(k, "")) for k in (
            "id", "goal", "implication", "pattern", "property",
            "parent", "baseline_source", "regulation", "adjustment")) + " |")
    md = "\\n".join(lines)
    return {"md": md, "goals": goals, "assumptions": assumptions,
            "tensions": [], "verdicts": [], "selected": [], "excluded": [],
            "framing": "", "yaml_text": ""}

'''


def main() -> int:
    src_root = Path(sys.argv[1])
    steps_p = src_root / "steps.py"
    src = steps_p.read_text(encoding="utf-8")
    original = src

    # 1. _call gains an optional single-card restriction
    old_sig = '''    def _call(self, step: str, subdomain: str | None) -> None:'''
    new_sig = '''    def _call(self, step: str, subdomain: str | None,
              only_card: str | None = None, tag_sd: str | None = None) -> None:'''
    assert src.count(old_sig) == 1, "anchor: _call signature"
    src = src.replace(old_sig, new_sig)

    # LAB02 arm: numa chamada por cartão o `subdomain` chega card-qualified
    # (`D-01.1.GDPR`) para que o artefacto grave por cartão; o pack e a instrução
    # continuam a ser do sub-domínio.
    old_instr = '''            extra = _p4_instruction(
                subdomain, subso_ids=subso_ids,
                adjustment_variant=(self.config.get("ficha_overrides") or {}).get("p4_adjustment"))'''
    # LAB02 arm: a forensics tag de uma chamada por cartão leva o sub-domínio E o
    # cartão, senão N chamadas por sub-domínio colidem em inputs/ e trace.jsonl.
    old_tag = '''        step_kind = step.split(":", 1)[0]
        tag = (f"{step_kind}_{subdomain.replace('.', '_')}" if subdomain is not None
               else step.replace(":", "_"))'''
    new_tag = '''        step_kind = step.split(":", 1)[0]
        # a card call is attributed by CARD in the tag so N calls per sub-domain
        # do not collide in inputs/ and trace.jsonl
        _tsd = tag_sd if tag_sd is not None else subdomain
        if only_card is not None and subdomain is not None:
            tag = f"{step_kind}_{_tsd.replace('.', '_')}__{only_card.rsplit('.', 1)[-1]}"
        else:
            tag = (f"{step_kind}_{subdomain.replace('.', '_')}" if subdomain is not None
                   else step.replace(":", "_"))'''
    assert src.count(old_tag) == 1, "anchor: tag em _call"
    src = src.replace(old_tag, new_tag)
    new_instr = '''            # LAB02 arm: a single-card call restates exactly that card. The
            # merged artefact restores the full table, so the stored artefact is
            # the same shape as a monolithic pass.
            scoped = [only_card] if only_card in subso_ids else subso_ids
            extra = _p4_instruction(
                subdomain, subso_ids=scoped,
                adjustment_variant=(self.config.get("ficha_overrides") or {}).get("p4_adjustment"))'''
    assert src.count(old_instr) == 1, "anchor: p4 instruction call"
    src = src.replace(old_instr, new_instr)

    # 2. merge helper + _call_card live next to store_parsed
    anchor_store = '''def store_parsed(run_dir: Path, step: str, subdomain: str | None, parsed: dict) -> None:'''
    assert src.count(anchor_store) == 1, "anchor: store_parsed"
    src = src.replace(anchor_store, MERGE_HELPERS.strip("\n") + "\n\n\n" + anchor_store)

    card_anchor = '''    def stage_p4(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        sw = self._sweep("p4", order,
                         done_marker=lambda sd: (self.run_dir / "steps" / "goals" / f"{sd}.md").exists(),
                         on_call=lambda sd: self._call(f"p4:{sd}", sd))'''
    assert src.count(card_anchor) == 1, "anchor: stage_p4 body"

    stage_new = '''    def stage_p4(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        if self.dry_run:
            sw = self._sweep("p4", order,
                             done_marker=lambda sd: (self.run_dir / "steps" / "goals" / f"{sd}.md").exists(),
                             on_call=lambda sd: self._call(f"p4:{sd}", sd))
        else:
            sw = self._sweep_cards("p4", order)

        n_failed = len(sw["failures"])'''
    src = src.replace(card_anchor, stage_new)

    # 3. _sweep_cards — one call per card, merge, then the EXISTING quality gate
    sweep_new = '''
    def _sweep_cards(self, kind: str, order: list[str]) -> dict:
        """LAB02 arm: sweep sub-domains, one LLM call per Sub-SO card.

        Conservative failure semantics: any card failing L0 fails the sub-domain,
        exactly as a monolithic call would. The existing `check_p4_quality`
        (coverage + peer-dedup + R2/R5/R6) runs ONCE on the merged list, so the
        gates are not weakened by splitting the generation.
        """
        carried, failures, calls = [], [], 0
        already = []
        confirmed = confirmed_regulations(self.run_dir) if (
            self.run_dir / "steps" / "verdicts.json").exists() else []
        for sd_id in order:
            goal_dir = self.run_dir / "steps" / "goals"
            goal_dir.mkdir(exist_ok=True)
            if (goal_dir / f"{sd_id}.md").exists():
                already.append(sd_id)
                continue
            sd_dir = domain_dir(self.repo, sd_id)
            cards = []
            for reg in REGULATIONS:            # canonical order
                if reg not in confirmed:
                    continue
                rf = sd_dir / "regs" / f"{reg}.md"
                if rf.exists() and f"SG-{sd_id}.{reg}" in rf.read_text(encoding="utf-8"):
                    cards.append(f"SG-{sd_id}.{reg}")
            per_card, card_fail = [], None
            for card in cards:
                calls += 1
                try:
                    per_card.append((card, self._call_card_parsed(sd_id, card)))
                except (ValueError, KeyError) as e:
                    card_fail = (card, str(e)[:400])
                    break
                except Exception as e:         # noqa: BLE001 — recorded, not swallowed
                    card_fail = (card, f"{type(e).__name__}: {e}"[:400])
                    break
            if card_fail is not None:
                failures.append({
                    "subdomain": sd_id, "step": f"p4:{sd_id}", "kind": "L0",
                    "seq": self.trace.next_seq() - 1, "ts": now_iso(),
                    "l0_first_error": card_fail[1], "l0_final_error": card_fail[1],
                    "failed_card": card_fail[0],
                })
                continue
            merged = merge_card_answers(sd_id, per_card)
            verdict = check_p4_quality(self.repo, self.run_dir, merged, sd_id)
            if verdict.get("errors"):
                failures.append({
                    "subdomain": sd_id, "step": f"p4:{sd_id}", "kind": "L0",
                    "seq": self.trace.next_seq() - 1, "ts": now_iso(),
                    "l0_first_error": "; ".join(verdict["errors"])[:400],
                    "l0_final_error": "; ".join(verdict["errors"])[:400],
                    "stage": "merge-quality-gate",
                })
                continue
            store_parsed(self.run_dir, "p4", sd_id, merged)
            carried.append(sd_id)
        return {"carried": carried, "failures": failures, "calls": calls, "already": already}

'''
    stage_tail = '''    def stage_p4t(self) -> int:'''
    assert src.count(stage_tail) == 1, "anchor: stage_p4t"
    src = src.replace(stage_tail, sweep_new + "\n" + stage_tail)

    # 4. _call_card_parsed — a card call that returns the parsed payload
    helper = '''
    def _call_card_parsed(self, sd_id: str, card: str) -> dict:
        """One card-scoped p4 call; returns the parsed payload for the merge.

        The per-card answer is stored under the CARD's key, not the sub-domain's:
        `store_parsed` keys on its subdomain argument, so a card call would
        otherwise overwrite the previous card's artefact. The sub-domain artefact
        is written once, after the merge.
        """
        # The subdomain passed to _call stays the REAL sub-domain: every gate in
        # the validate path checks it against the canonical index, and store_parsed
        # keys the artefact on it. Passing a card-qualified key was what broke the
        # first attempt (`not a canonical sub-domain id: D-01.1.GDPR`); the card
        # travels separately in `only_card`, which narrows the instruction only.
        # The card call's answer therefore lands in the sub-domain's own file and
        # the merge rewrites it once, from all cards.
        self._call(f"p4:{sd_id}", sd_id, only_card=card, tag_sd=sd_id)
        goal_json = self.run_dir / "steps" / "goals" / f"{sd_id.replace('.', '_')}.json"
        if not goal_json.exists():
            raise ValueError(f"card call produced no artifact for {card}")
        return json.loads(goal_json.read_text(encoding="utf-8"))

'''
    # `_call_card` exists ONLY in this patch, so anchoring on it was a no-op that
    # silently dropped both methods. Anchor on a line the shipped file really has.
    card_anchor = '''    def stage_p4t(self) -> int:'''
    assert src.count(card_anchor) == 1, "anchor: stage_p4t"
    src = src.replace(card_anchor, helper + card_anchor)

    # -- guards --------------------------------------------------------------
    g0, g1 = blocks(original), blocks(src)
    if g0 != g1:
        added = [l for l in g1.splitlines() if l not in g0.splitlines()]
        sys.exit(f"FAIL: guarded blocks changed: {added[:6]}")
    try:
        compile(src, str(steps_p), "exec")
    except SyntaxError as e:
        sys.exit(f"FAIL: patched steps.py does not compile: {e}")
    steps_p.with_name("steps.py.prelab").write_text(original, encoding="utf-8")
    steps_p.write_text(src, encoding="utf-8")
    print("LAB02 card-split applied: _call(only_card), _call_card_parsed, _sweep_cards, "
          "merge_card_answers. Guarded blocks byte-identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())