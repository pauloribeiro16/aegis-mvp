# Synthesis Rounds — SecureBorder eGate (Iterative Risk-Acceptance Cycle)

> **Purpose:** working folder for the Phase 3 Part 1 iterative synthesis cycle (ADR-005/006): the exhaustive objective mapping, the principle mapping, the round registers, and the sufficiency assessment.
> **Objective Mapping:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) — all 100 Phase 2 objectives (GDPR 29 · CRA 32 · NIS 2 22 · AI Act 15, plus 2 recorded N/A) with explicit verdicts.
> **Principle Mapping:** [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) — §1 per principle, §2 per-requirement check, §3 totals.
> **UC Correspondence:** [`UC_OBJECTIVE_CORRESPONDENCE.md`](UC_OBJECTIVE_CORRESPONDENCE.md) — use-case-centric view with per-UC bindings and the regulation tag.
> **Round registers:** [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) (20/20 constraints + 51/51 chain bindings, 2026-09-28) and [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md) (R9.3 elevation, 2026-09-29) — EARS formulations, fit criteria, control selections, convergence.
> **Sufficiency:** [`SUFFICIENCY_ASSESSMENT.md`](SUFFICIENCY_ASSESSMENT.md) — per-regulation verdict, explicit residuals, Part 2 trigger.
> **Organizational lane:** [`../Doc03_Organizational_Requirements.md`](../Doc03_Organizational_Requirements.md) — PROCESS-lane carrier of the objectives verdicted `No functional carrier (organizational)` (ADR-008).

## Capability lane rule (technology vs process)

A capability is **technology + process**. Phase 3 Part 1 operates the TECHNOLOGY lane (ADR-002): only the technology leg becomes product requirements here. The process leg is **never silently dropped**: when an objective binds only on the process leg, the mapping records `No functional carrier (organizational/process control)` and routes it to the organizational lane, visible in every review. In this case: `PO-D-08.1-001`, `PO-D-08.2-001` (DPO activities) — carried in `Doc03_Organizational_Requirements.md`.

## Current state

- **Round 0:** the APPROVED V0 functional baseline (28 cards) consolidated 2026-09-28.
- **Round 1 CONVERGED (2026-09-28):** 20/20 constraint accepts (RN11–RN30) + 51/51 chain-binding accepts, absorbed into V1 (2.0.0).
- **Round 2 CONVERGED (2026-09-29):** `R9.3` AI adversarial testing elevated SHOULD → MUST (D3, AI Act Art. 9(6)-(7)) and the Doc02 matrix `R7.3` aligned; V2 (3.0.0) is the active version.
- **Part 1 Exit Gate G1–G6 GREEN** — evidence in [`../analysis_v0_to_v1/README.md`](../analysis_v0_to_v1/README.md); Part 2 cleared, not started.
