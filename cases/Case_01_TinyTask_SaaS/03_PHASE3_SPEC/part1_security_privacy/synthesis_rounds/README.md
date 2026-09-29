# Synthesis Rounds — TinyTask SaaS (Iterative Risk-Acceptance Cycle)

> **Purpose:** Working folder for the Phase 3 iterative synthesis cycle (ADR-005): the exhaustive objective mapping, the principle mapping, round proposals, and the client's per-item risk verdicts.
> **Objective Mapping:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) — Step 2 deliverable: all 62 Phase 2 objectives + 7 principles with explicit verdicts (applies — with skill — or no functional carrier).
> **Principle Mapping:** [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) — principle-centric mirror: for each `PRIN-ENG-01..07`, where it binds across the functional model, how it is realized, and its coverage state (gaps feed the open round).
> **UC Correspondence:** [`UC_OBJECTIVE_CORRESPONDENCE.md`](UC_OBJECTIVE_CORRESPONDENCE.md) — use-case-centric view: grid (objective × UC package, regulation-tagged) + 20 per-UC cards (what each objective demands there, regulation, skill, RN, post-Round-1 state).
> **Process:** manual Step 2 (exhaustive matrix) → Step 3 rounds — propose (EARS constraint + addressed risk + altitude + chain) → client verdict per item (**Accept / Reject = explicit risk acceptance / Adjust**), recorded in the round documentation → iterate to convergence → only then do `Doc01`/`Doc02` versions evolve, followed by control selection (Step 4). **Part 1 Exit Gate (G1–G6, ADR-006):** when all six are GREEN (evidenced in `../analysis_v1_to_v2/README.md`), Phase 3 Part 2 — Threat & Risk Analysis (`../../part2_threat_risk`) may launch.

## Capability lane rule (technology vs process)

A capability is **technology + process**. Phase 3 operates the TECHNOLOGY lane (ADR-002): only the technology leg of a capability becomes product requirements here. The process leg (organizational practices, policies, training, governance routines) is **never silently dropped**: when an objective binds only on the process leg, the mapping records the explicit verdict `No functional carrier (organizational/process control)`, and the need is routed to the PROCESS lane deliverable (`part1_security_privacy/Doc03_Organizational_Requirements.md`, ADR-008) — visible in every review, accepted or rejected like any other item.

## Current state

- The APPROVED V1 baseline (`../v1_security_privacy_synthesis/`, 19 requirement cards) was consolidated on 2026-09-23/24, **before** the round cycle was introduced (ADR-005, 2026-09-24). It stands as the accepted starting position: absorbed constraints are treated as **Accepted** for the purposes of future rounds unless the client revisits them (recorded as Round 0 in the round documentation).
- **Round 1 CONVERGED (verdicts 2026-09-28)**: 13/13 accepts — 9 chain re-drives (ADJ-1…ADJ-9) + 4 new constraints (P-01…P-04 → RN27, RN28, R8.3 D1, RN29). Verdicts, formulations and Step-4 control selections in [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md); the accepted set evolves `Doc01`/`Doc02` to 4.0.0.
- **Round 2 — baseline-change proposals (P1–P4)** tabled from the ADR-007 coverage discharge verification: per-objective verdicts and discharge records live in the `VC discharge` column of [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md); the proposals await client verdicts in [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md) — the accepted baseline (4.0.0) is unchanged by them.
- The chain-recalibration of phantom `PO-D-06.x`/`PO-D-03.1-001` drivers was executed directly — it corrected citations to already-accepted constraints and required no new client decision; driver re-assignments and new constraints did, and went to Round 1.
