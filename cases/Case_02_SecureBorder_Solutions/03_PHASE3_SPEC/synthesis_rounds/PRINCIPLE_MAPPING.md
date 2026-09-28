# Principle Mapping — Functional Requirements Analyzed Against the 7 Secure Design Principles (SecureBorder eGate)

> **Purpose:** the principle-centric mirror of [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md): for **each secure-design principle** (`PRIN-ENG-01`..`07`, Phase 2 `Doc02`), where it binds across the functional model (requirement cards `R<n.m>` and use cases `{U.C.n.m}`), how it is realized there, and its coverage state.
> **Sources:** `../../02_PHASE2_RULES/Doc02_Secure_Design_Principles.md` (principle definitions) · `../analysis_v0_to_v1/STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md` (derivation) · [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) (proposed constraints).
> **State legend:** `Proposed (RNx)` = realized by a Round-1 constraint proposal, awaiting client verdict · `Bound (functional)` = realized directly in the V0 requirement's functional description · `Cross-cutting` = binds via shared rows/preconditions. **All RN bindings are Round-1 proposals pending verdicts.**
> **Skills (analysis lens):** AS = attack-surface-analysis · TB = trust-boundary-analysis · LP = least-privilege-analysis · FS = fail-safe-defaults-analysis · V = verifiability-analysis · DM = data-minimization-analysis · LE = lifecycle-erasure-analysis.

---

## §1 Principle ↔ Functional Model Matrix (principle-centric)

### `PRIN-ENG-01` — Explicit Trust Boundaries & Complete Mediation

| Where | Realization | RN | State |
|---|---|---|---|
| `R1.1`/`R1.2`/`R1.3` (gate↔back-office↔authority flows) | Every biometric and record flow authenticated and encrypted at the boundary; templates protected within it | RN11, RN13 | Proposed |
| `R3.2`, `R3.3` | Strong authentication and role mediation before every operator action | RN18, RN19 | Proposed |
| `R4.1` | Rights execution mediated by verified requester identity | RN16 | Proposed |
| `R2.1`/`R11.2` | Oversight authority and competence demarcated (who may intervene) | RN29 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-02` — Attack Surface Minimization & Peripheral Resilience

| Where | Realization | RN | State |
|---|---|---|---|
| `R7.2` | Updates via a single secure, separated channel with advisories | RN27 | Proposed |
| `R5.2`/`R5.3` | Incident handling closed across the six lifecycle actions | RN23 | Proposed |
| `R9.2`/`R5.1` | Post-market monitoring data continuously feeds the risk system | RN25 | Proposed |
| `R8.1` | Pipeline gates limit surfaces of release artefacts (chain row) | chain | Proposed (chain row) |

**Verdict: followed (pending R1).**

### `PRIN-ENG-03` — Least Privilege & Mechanism Isolation

| Where | Realization | RN | State |
|---|---|---|---|
| `R3.1`, `R3.3` | Identity lifecycle + role entitlements reviewed on change | RN17, RN19 | Proposed |
| `R1.1`/`R1.2` | De-linking keys never bundled with the operational environment | RN12 | Proposed |
| Per-country deployment isolation | V0 `RN10` quality attribute (W1) | — | Bound (functional) |

**Verdict: followed (pending R1).**

### `PRIN-ENG-04` — Fail-Safe Defaults & Closed Failure States

| Where | Realization | RN | State |
|---|---|---|---|
| `R1.2`/`R8.1` | New deployments and artifacts born restrictive; resettable | RN20 | Proposed |
| `R1.2`/`R8.3` | AI fault → safe closed gate state + rollback to last verified model | RN15 | Proposed |
| `R1.2` | V0 description: gate decisions fail closed on verification failure (W1) | — | Bound (functional) |

**Verdict: followed (pending R1).**

### `PRIN-ENG-05` — Requirement Verifiability & Atomicity

| Where | Realization | RN | State |
|---|---|---|---|
| All RN cards + every Round-1 proposal | Volere fit criterion + empirical method on each requirement | global | Bound (recorded once) |

**Verdict: followed** (structural — enforced by the card anatomy and the proposal template).

### `PRIN-ENG-06` — Proactive Data Minimization & Scoped Projection

| Where | Realization | RN | State |
|---|---|---|---|
| `R1.1` | Raw captures discarded on template extraction; templates de-linked (V0, W1) + chain rows | chain | Proposed (chain rows) |
| `R4.1` | Exports limited to the requester's own data (T-002: token-only records) | RN28 | Proposed |

**Verdict: followed (pending R1).**

### `PRIN-ENG-07` — End-to-End Lifecycle Security & Irreversible Erasure

| Where | Realization | RN | State |
|---|---|---|---|
| `R5.1`/`R1.2` | Tamper-evident activity recording across fleet and gate | RN22 | Proposed |
| `R1.2`/`R9.2` | AI events logged over the lifetime; authority access on demand | RN24 | Proposed |
| `R4.1` | Erasure destroys biometric content including key material; token-only records survive | RN28 | Proposed |
| `R6.1` | Notification dossiers integrity-protected (RN14 chain) | RN14 | Proposed |

**Verdict: followed (pending R1).**

---

## §2 Per-Requirement Principle Check (R1.1–R11.2)

One row per (requirement × principle) binding with the concrete mechanism and carrier. A requirement without a binding row has no direct security surface of its own and says so explicitly.

| Req | Principle | How it is upheld here | Carrier | State |
|---|---|---|---|---|
| `R1.1` | `PRIN-ENG-06` Minimization | Raw capture discarded on extraction; template de-linked (V0 functional + chain rows) | functional + RN11 | Proposed |
| `R1.1` | `PRIN-ENG-01` Trust Boundaries | Templates encrypted at rest; flows mediated | RN11, RN13 | Proposed |
| `R1.1` | `PRIN-ENG-03` Least Privilege | De-linking keys under separated custody | RN12 | Proposed |
| `R1.2` | `PRIN-ENG-04` Fail-Safe | Fault → safe closed state; secure-by-default config | RN15, RN20 | Proposed |
| `R1.2` | `PRIN-ENG-07` Observability | AI event logging; activity recording | RN22, RN24 | Proposed |
| `R1.2` | `PRIN-ENG-01` Trust Boundaries | Transit protection on every boundary flow | RN13 | Proposed |
| `R1.3` | `PRIN-ENG-07` Observability | Decision records integrity-protected and tamper-evident | RN11, RN14 | Proposed |
| `R2.1` | `PRIN-ENG-01` Trust Boundaries | Oversight authority mediated by role and instruction | RN19, RN29 | Proposed |
| `R3.1` | `PRIN-ENG-03` Least Privilege | Lifecycle provisioning/review/revocation of entitlements | RN17 | Proposed |
| `R3.2` | `PRIN-ENG-01` Trust Boundaries | Strong/multi-factor authentication per policy | RN18 | Proposed |
| `R3.3` | `PRIN-ENG-03` Least Privilege | Role assignments and instruction mediation | RN17, RN19 | Proposed |
| `R4.1` | `PRIN-ENG-01` Trust Boundaries | Requester identity verified before execution | RN16 | Proposed |
| `R4.1` | `PRIN-ENG-07` Erasure | Erasure destroys biometric content incl. key material; portability scoped | RN28 | Proposed |
| `R5.1` | `PRIN-ENG-07` Observability | Fleet event collection with tamper evidence | RN22, RN25 | Proposed |
| `R5.2` | `PRIN-ENG-02` Resilience | Incident lifecycle closure with CSIRT-ready evidence | RN23, RN26 | Proposed |
| `R5.3` | `PRIN-ENG-04` Fail-Safe | Continuity/backup/disaster-recovery state (chain rows) | chain | Proposed (chain row) |
| `R6.1` | `PRIN-ENG-05` Verifiability | One clock-start, four statutory timelines enforced | RN21, RN14 | Proposed |
| `R7.2` | `PRIN-ENG-02` Attack Surface | Single secure separated update channel | RN27 | Proposed |
| `R8.1` | `PRIN-ENG-02` Attack Surface | Pipeline security gates; secure defaults on artifacts (chain row) | chain + RN20 | Proposed |
| `R8.3` | `PRIN-ENG-04` Fail-Safe | Model versioning with rollback to last verified version | RN15 | Proposed |
| `R9.2` | `PRIN-ENG-07` Observability | Accuracy/drift/bias monitoring feeding post-market loop | RN24, RN25 | Proposed |
| `R9.3` | `PRIN-ENG-05` Verifiability | Adversarial testing + deployer interpretability | RN30 | Proposed |
| `R10.1` | `PRIN-ENG-05` Verifiability | Unified assessment family with recorded updates (chain rows) | chain | Proposed (chain row) |
| `R10.2` | `PRIN-ENG-05` Verifiability | Vendor/provenance chain rows (T-004) | chain | Proposed (chain row) |
| `R10.3` | `PRIN-ENG-05` Verifiability | Documentation/compliance chain rows | chain | Proposed (chain row) |
| `R11.2` | `PRIN-ENG-01` Trust Boundaries | Oversight competence sustaining effective human mediation | RN29 | Proposed |

**Per-principle rollup (requirements realizing each principle):**

| Principle | Requirements realizing it | Cover |
|---|---|---|
| `PRIN-ENG-01` Trust Boundaries & Complete Mediation | R1.1, R1.2, R1.3, R2.1, R3.2, R3.3, R4.1, R11.2 (+RN13 cross-cutting) | 8 + cross-cutting |
| `PRIN-ENG-02` Attack Surface & Resilience | R5.2, R5.3, R7.2, R8.1, R9.2 | 5 |
| `PRIN-ENG-03` Least Privilege & Isolation | R1.1, R1.2, R3.1, R3.3 (+RN10 deployment isolation, V0) | 4 + V0 |
| `PRIN-ENG-04` Fail-Safe Defaults | R1.2, R5.3, R8.3 | 3 |
| `PRIN-ENG-05` Verifiability & Atomicity | all (structural) + R6.1, R9.3, R10.x chains | 28 + proposals |
| `PRIN-ENG-06` Minimization & Scoped Projection | R1.1, R4.1 | 2 |
| `PRIN-ENG-07` Lifecycle Security & Erasure | R1.2, R1.3, R4.1, R5.1, R6.1, R9.2 | 6 |

## §3 Coverage Totals & Gaps

| Surface | Count | Notes |
|---|---|---|
| Principles followed (pending R1) | 7/7 | every principle has ≥1 realization; none without a carrier |
| Requirements realizing ≥1 principle | 27/28 | `R11.1` realized via chain row (hygiene/training objectives) |
| Pending Round-1 items touching principle chains | 20 RNs | RN11–RN30 — see [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) |

**Read rule:** gaps are **principle gaps, not requirement defects** — they enter Round 1 as proposals; nothing is silently accepted.
