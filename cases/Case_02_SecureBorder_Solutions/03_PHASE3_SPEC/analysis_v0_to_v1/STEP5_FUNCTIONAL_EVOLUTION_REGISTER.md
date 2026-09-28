# Step 5 — Functional Evolution Register (V0 → V1)

> **Finding: evaluated, no change.** The Round-1 synthesis required **zero functional-set changes** — no D1 derived requirement, no D2 description refinement, no D3 priority re-evaluation, no D4 card split.

## 1. Evaluation pass

Every functional area was evaluated for functional gaps exposed by the accepted constraint set:

| Area | Candidates considered | Outcome |
|---|---|---|
| R1 biometric verification | recovery/rollback flows — already covered by `R8.3` (model rollback) and `R2.2` (manual lane) | evaluated, no change |
| R2 oversight | competence gating — covered by `R11.2` + {U.C. 2.1} preconditions | evaluated, no change |
| R3 identity | lifecycle events — already the card's function | evaluated, no change |
| R4 rights | erasure incl. key material — absorbed as RN28 constraint on the existing card | evaluated, no change |
| R5–R7 operations | lifecycle closure, secure channel — absorbed as constraints on existing cards | evaluated, no change |
| R8–R11 governance | documentation/oversight families — absorbed as chain rows | evaluated, no change |

## 2. Rationale

Unlike Case_01 (where the synthesis exposed a missing recovery requirement), the Case_02 V0 was elicited for a RIGOROUS-tier essential entity whose functional repertoire already spans the operational capabilities the four regulations demand of the *product and its operation*. The synthesis therefore proceeded by **constraint absorption and chain binding only**, and the functional baseline (28 cards, 28 PUCs) carries over unchanged.

## 3. Register entry

| # | Type | From (V0) | To (V1) | Driving obligation | Decision & rationale |
|---|---|---|---|---|---|
| CH-01 | — (evaluated) | 28 cards | 28 cards | all four ambits | **evaluated, no change** — functional set complete for the accepted constraint set; protections absorbed as RN11–RN30 and chain rows |

`v0_functional_baseline/` files untouched (verified byte-identical to the locked copies).
