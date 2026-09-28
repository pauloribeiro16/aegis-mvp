# Principle Mapping — Functional Requirements Analyzed Against the 7 Secure Design Principles (OmniBank Financial Systems)

> **Purpose:** the principle-centric mirror of [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md).
> **State legend:** `Proposed (RNx)` = realized by a Round-1 constraint proposal, awaiting client verdict · `Bound (functional)` = realized directly in the V0 functional description · structural = enforced by the card anatomy.
> **Skills (analysis lens):** AS = attack-surface-analysis · TB = trust-boundary-analysis · LP = least-privilege-analysis · FS = fail-safe-defaults-analysis · V = verifiability-analysis · DM = data-minimization-analysis · LE = lifecycle-erasure-analysis.

## §1 Principle ↔ Functional Model Matrix (principle-centric)

### `PRIN-ENG-01` — Explicit Trust Boundaries & Complete Mediation

Every boundary flow authenticated/encrypted (RN13); rights execution mediated (RN16); privileged access mediated (RN19); oversight authority demarcated (RN22).

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Every boundary flow authenticated/encrypted (RN13); rights execution mediated (RN16); privileged access mediated (RN19); oversight authority demarcated (RN22). | RN13, RN16, RN19, RN22 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-02` — Attack Surface Minimization & Peripheral Resilience

Post-market feedback loop (RN24); adversarial robustness measures (RN25); testing programmes reduce exploitable surface (chain rows R3.4/R11.3).

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Post-market feedback loop (RN24); adversarial robustness measures (RN25); testing programmes reduce exploitable surface (chain rows R3.4/R11.3). | RN24, RN25 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-03` — Least Privilege & Mechanism Isolation

Key custody separated from operations (RN15); AI platform least-privilege mediation (RN21); V0 RN10 architectural isolation.

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Key custody separated from operations (RN15); AI platform least-privilege mediation (RN21); V0 RN10 architectural isolation. | RN15, RN21 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-04` — Fail-Safe Defaults & Closed Failure States

Born-restrictive configurations with reset (RN20); fail-closed decision and gate defaults (V0 functional).

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Born-restrictive configurations with reset (RN20); fail-closed decision and gate defaults (V0 functional). | RN20 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-05` — Requirement Verifiability & Atomicity

Structural: Volere fit criterion + ISO 29148 method on every RN and proposal (recorded once).

| Where | Realization | RN | State |
|---|---|---|---|
| All RN cards + every Round-1 proposal | Volere fit criterion + empirical method on each requirement | global | Bound (recorded once) |

**Verdict: followed (structural).**

### `PRIN-ENG-06` — Proactive Data Minimization & Scoped Projection

Scoring purpose binding (RN12); token-only retention after erasure (RN17); V0 collection minimization (R6.1).

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Scoring purpose binding (RN12); token-only retention after erasure (RN17); V0 collection minimization (R6.1). | RN12, RN17 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-07` — End-to-End Lifecycle Security & Irreversible Erasure

Decision/model integrity (RN11); at-rest protection (RN14); non-repudiable notification clock (RN18); lifetime AI logging (RN23); immutable audit fabric (R11.2).

| Where | Realization | RN | State |
|---|---|---|---|
| Requirement cards and use cases per [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) | Decision/model integrity (RN11); at-rest protection (RN14); non-repudiable notification clock (RN18); lifetime AI logging (RN23); immutable audit fabric (R11.2). | RN11, RN14, RN18, RN23 | Proposed |

**Verdict: followed (pending R1).**

## §3 Coverage Totals & Gaps

| Surface | Count | Notes |
|---|---|---|
| Principles followed (pending R1) | 7/7 | every principle has ≥1 realization; none without a carrier |
| Pending Round-1 items touching principle chains | 16 RNs | RN11–RN26 — see [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) |

**Read rule:** gaps are **principle gaps, not requirement defects** — they enter Round 1 as proposals; nothing is silently accepted.
