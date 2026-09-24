# Synthesis Rounds — TinyTask SaaS (Iterative Risk-Acceptance Cycle)

> **Purpose:** Working folder for the Phase 3 iterative synthesis cycle (ADR-005): round proposals and the client's per-item risk verdicts.
> **Register:** [`RISK_ACCEPTANCE_REGISTER.md`](RISK_ACCEPTANCE_REGISTER.md) · template: `templates/phase3_risk_acceptance_register.md`.
> **Process:** manual Step 3 (Iterative Synthesis & Risk-Acceptance Rounds) — propose (EARS constraint + addressed risk + altitude + chain) → client verdict per item (**Accept / Reject = explicit risk acceptance / Adjust**) → iterate to convergence → only then do `Doc01`/`Doc02` versions evolve, followed by control selection (Step 4).

## Current state

- The APPROVED V1 baseline (`../v1_security_privacy_synthesis/`, 19 requirement cards) was consolidated on 2026-09-23/24, **before** the round cycle was introduced (ADR-005, 2026-09-24). It stands as the accepted starting position: absorbed constraints are treated as **Accepted** for the purposes of future rounds unless the client revisits them (recorded as Round 0 in the register).
- Future baseline revisions — including the chain-recalibration backlog (`../analysis_v0_to_v1/STEP6_SPECIFICITY_MATCHING_AUDIT.md` §7) and any Phase 4 treatment proposals — are negotiated through the register.
