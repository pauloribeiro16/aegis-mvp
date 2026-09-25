# Synthesis Rounds — TinyTask SaaS (Iterative Risk-Acceptance Cycle)

> **Purpose:** Working folder for the Phase 3 iterative synthesis cycle (ADR-005): the exhaustive objective mapping, round proposals, and the client's per-item risk verdicts.
> **Objective Mapping:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) — Step 2 deliverable: all 62 Phase 2 objectives + 7 principles with explicit verdicts (applies — with skill — or no functional carrier).
> **UC Correspondence:** [`UC_OBJECTIVE_CORRESPONDENCE.md`](UC_OBJECTIVE_CORRESPONDENCE.md) — use-case-centric view: grid (objective × UC package) + 19 per-UC cards (what each objective demands there, skill, RN, state incl. pending Round-1 items).
> **Register:** [`RISK_ACCEPTANCE_REGISTER.md`](RISK_ACCEPTANCE_REGISTER.md) · template: `templates/phase3_risk_acceptance_register.md`.
> **Process:** manual Step 2 (exhaustive matrix) → Step 3 rounds — propose (EARS constraint + addressed risk + altitude + chain) → client verdict per item (**Accept / Reject = explicit risk acceptance / Adjust**) → iterate to convergence → only then do `Doc01`/`Doc02` versions evolve, followed by control selection (Step 4).

## Current state

- The APPROVED V1 baseline (`../v1_security_privacy_synthesis/`, 19 requirement cards) was consolidated on 2026-09-23/24, **before** the round cycle was introduced (ADR-005, 2026-09-24). It stands as the accepted starting position: absorbed constraints are treated as **Accepted** for the purposes of future rounds unless the client revisits them (recorded as Round 0 in the register).
- **Round 1 is open (2026-09-24)**: 13 items awaiting client verdicts — 9 chain re-drives to their natural objectives (ADJ-1…ADJ-9) + 4 new constraints from the exhaustive mapping (P-01…P-04). Verdicts are recorded in the register; only after convergence do the deliverables evolve.
- The chain-recalibration of phantom `PO-D-06.x`/`PO-D-03.1-001` drivers was executed directly (STEP7) — it corrected citations to already-accepted constraints and required no new client decision; driver re-assignments and new constraints did, and went to Round 1.
