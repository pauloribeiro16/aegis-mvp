# Synthesis Rounds — OmniBank Financial Systems (Iterative Risk-Acceptance Cycle)

> **Purpose:** working folder for the Phase 3 Part 1 iterative synthesis cycle (ADR-005/006): the exhaustive objective mapping, the principle mapping, the round registers, and the sufficiency assessment.
> **Objective Mapping:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) — all 134 Phase 2 objectives (GDPR 29 · CRA 36 · NIS 2 24 · DORA 30 · AI Act 15) with explicit verdicts.
> **Principle Mapping:** [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) — §1 per principle, §2 per-requirement check, §3 totals.
> **UC Correspondence:** [`UC_OBJECTIVE_CORRESPONDENCE.md`](UC_OBJECTIVE_CORRESPONDENCE.md) — use-case-centric view with per-UC bindings and the regulation tag.
> **Round registers:** [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) (16/16 + 92/92 accepts by client directive, 2026-09-29) and [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md) (R3.3 elevation) — EARS formulations, fit criteria, control selections, convergence.
> **Sufficiency:** [`SUFFICIENCY_ASSESSMENT.md`](SUFFICIENCY_ASSESSMENT.md) — per-regulation verdict, explicit residuals, Part 2 trigger.

## Capability lane rule (technology vs process)

A capability is **technology + process**. Phase 3 Part 1 operates the TECHNOLOGY lane (ADR-002): only the technology leg becomes product requirements here. The process leg is **never silently dropped**: when an objective binds only on the process leg, the mapping records `No functional carrier (organizational/process control)` and routes it to the organizational lane (ADR-008), visible in every review. In this case: `PO-D-08.1-001`, `PO-D-08.2-001` (DPO activities).

## Current state

- **Round 0:** the APPROVED V0 functional baseline (43 cards) consolidated 2026-09-28.
- **Round 1 CONVERGED (2026-09-29):** 16/16 constraint accepts (RN11–RN26) + 92/92 chain-binding accepts by client directive after five plain-language batches; absorbed into V1 (2.0.0).
- **Round 2 CONVERGED (2026-09-29):** `R3.3` CVD elevated SHOULD → MUST (D3, CRA Annex I Part II (5)); V2 (3.0.0) is the active version.
- **Part 1 Exit Gate G1–G6 GREEN** — evidence in [`../analysis_v0_to_v1/README.md`](../analysis_v0_to_v1/README.md); Part 2 cleared, not started.
- **Referential-integrity repairs** (ADR-007 discharge semantics): chain re-anchoring to the compact Phase 2 numbering, recorded in [`../analysis_v0_to_v1/TRACEABILITY_REPAIR_LEDGER.md`](../analysis_v0_to_v1/TRACEABILITY_REPAIR_LEDGER.md); guards run via `python scripts/check_traceability.py --case Case_03_OmniBank --strict`.
