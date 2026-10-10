# L2_RUBRIC_F3 — the Phase 3 scoring instrument (draft, frozen before the rehearsal corpus)

Version: 0.1.0 DRAFT
Status: FROZEN as a draft 2026-10-10, before the first rehearsal artifact exists
(`PREREG_P3_01`). The unit definitions and dimensions below may not move after
the first scoring session; if they do, the instrument failed its own §6.1
discipline and the session is void.
Upstream: [L2_RUBRIC.md](L2_RUBRIC.md) §8 ("a Phase 3 batch needs the same
script and a Phase 3 corpus, not new machinery") · [PREREG_P3_01.md](PREREG_P3_01.md)

## 1. The batch

One scoring unit = **one requirement row**, from either surface:

| Surface | Unit id | Source |
|---|---|---|
| V0 functional card row | `card:R<n>.<m>` | the run's generated `Doc01_Requirements_Elicitation_and_PUC.md` (or the case's hand-written V0 for calibration) |
| Organizational requirement | `org:ORG-D-XX.Y-NNN` | the run's `Doc03_Organizational_Requirements.md` |
| Coverage verdict row | `verdict:<PO/SO-D-XX.Y-NNN>` | `synthesis_rounds/OBJECTIVE_MAPPING.md` |

Sampling: fixed seed, 8 rows per document, stratified so every package R<n>
appears at least once (same mechanics as the Phase 1 batch; the builder in
`scripts/build_scoring_pack.py` is corpus-agnostic — the Phase 3 corpus is a new
manifest, not new machinery).

## 2. Dimensions (0–2 each, the Phase 1 L2 scale)

| # | Dimension | 0 | 1 | 2 |
|---|---|---|---|---|
| D1 | **Altitude** (R13 §2.5) | L4 vocabulary or parameter values present | mechanism named, no L3 warrant | stays at the source's level; every descent carries a warrant |
| D2 | **Form** | not the artefact's grammar (no EARS `shall`, no 7-row anatomy) | grammar present, one defect | grammar exact and complete |
| D3 | **Fit criterion** | absent or unfalsifiable | falsifiable but compound (two tests in one) | binary, judgeable from named evidence |
| D4 | **Chain validity** | an anchor the source does not publish | published anchor, wrong function (GOVERN/PROTECT mismatch) | every leg inside the published set, right function |
| D5 | **Company grounding** (R6) | contradicts or invents company facts | generic — would read identically for another company | names this company's operational reality |

A verdict row is additionally scored on **D6 — verdict honesty**: the verdict
word matches the discharge (a `Fully covered` with carve-outs in the discharge
is 0; an `organizational` that names a technical leg is 0).

## 3. What this instrument does NOT decide

It scores artifacts; it does not re-decide verdicts (the round's), proportionality
(G-c), or threat models (Part 2). The gate machine (`p3a_gate`) stays structural.

## 4. Session plan (calendar)

1. **Session 1** — after the rehearsal completes: score the sampled rehearsal
   units blind (pack built with `_key.json` un-blinding deferred).
2. **Session 2** — ≥7 days later (§6.1 test–retest), same units re-scored.
   κ weighted ≥0.7 usable; 0.4–0.7 caveats; <0.4 the instrument fails.
3. Both sessions score with the rubric above unmodified; changes void the pair.

## 5. Open items (honest)

- The Phase 1 L2 batch (450 units) is still unscored, and its test–retest never
  ran — the precedent this instrument inherits, not escapes.
- The `check_no_technology` L4 list overlaps D1; the scorer may use it as a
  helper, not as the altitude judge (doc 08 wave 0: the ceiling is the
  instrument, never a word list).
