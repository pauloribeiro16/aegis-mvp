# Traceability index — regulation -> article -> objective -> requirement -> control

- Generated: 2026-09-22 by `scripts/build_traceability.py` (re-run after any `uniformize_control_anchors.py --apply`).
- Chain per row: regulation -> article(s) -> ambiguity clause(s) -> HSO `SO-D-XX.Y.HL` -> `SO-<REG>-NNN` -> Sub-SO `SO-D-XX.Y.<REG>` -> requirement (`req_id` + `SR`) -> CSF 2.0 | PF 1.1 | AI RMF.
- Baseline-only: per-company adjusted objectives (`AG-D-XX.Y-NNN`) are recorded in each Phase 1 output (`templates/phase1_output.md` §4.1).
- Control values are the module YAML sets, guaranteed equal to the dashboard crosswalk (check H of `scripts/verify_no_loss.py`).

| Regulation | Sub-domains | Requirements | Articles | Clauses | Reqs with PF 1.1 | Reqs with AI RMF |
|---|---|---|---|---|---|---|
| GDPR | 38 | 29 | 29 | 29 | 29 | 0 |
| CRA | 38 | 36 | 36 | 36 | 0 | 0 |
| NIS2 | 38 | 24 | 24 | 24 | 0 | 0 |
| DORA | 38 | 30 | 30 | 30 | 0 | 0 |
| AI_Act | 37 | 15 | 15 | 15 | 0 | 15 |
