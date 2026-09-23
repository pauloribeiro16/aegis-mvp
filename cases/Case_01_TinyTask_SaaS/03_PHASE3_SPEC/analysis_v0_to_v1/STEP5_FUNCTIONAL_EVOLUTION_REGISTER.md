# STEP 5 — Functional Evolution Register (V1 Refinement Pass)

> **Case Study:** Case 01 — TinyTask SaaS  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Purpose:** Mandatory change register for the Step 4b Functional Refinement Pass: every functional change introduced in V1 relative to the locked V0 baseline, classified in the D1–D4 taxonomy, with its driving `RN`/`PO-`/`SO-`/regulation-article trace and rationale.  
> **Normative basis:** `../PHASE3_PROCESS_AND_METHODOLOGY.md` Step 4b; `templates/phase3_functional_spec_guidelines.md` §3.4.  
> **Baselines:** FROM `../v0_functional_baseline/` (V0, LOCKED, 18 R cards) · TO `../v1_security_privacy_synthesis/` (V1, 19 R cards).

---

## 1. Gap-Analysis Method

For every synthesized obligation (`RN9`–`RN26` and their upstream `PO-`/`SO-` drivers), the pass asks one question:

> *Does complying with this obligation require user-visible, Cockburn Sea-Level functionality that no V0 card covers?*

- **Yes** → the gap becomes a register entry: **D1** for a missing capability, **D2** for a binding-blocking ambiguity, **D3** for a priority conflict with a confirmed regulation, **D4** for a split.
- **No** → the obligation is recorded as `evaluated, no change` (the constraint binds inside existing cards and use case extensions).

---

## 2. Register of Applied Changes

| # | Type | From (V0) | To (V1) | Driving obligation | Rationale |
|---|---|---|---|---|---|
| CH-01 | **D1 — Derived requirement** | — (no card covers post-lockout recovery) | New `R1.3` Recover access to a locked user account (Must) + `PUC 1.3` + `{U.C. 1.3}` | `NFR-RN10`, `NFR-RN11` (CRA Annex I Part I (2)(d)+(2)(j)) — lockout behavior specified in `{U.C. 1.1}` extension 5c | The synthesized brute-force lockout (5 failures → 15-minute block) creates a user goal absent from pure business elicitation: a legitimate user facing the lockout (or a persistent failure counter) has no autonomous recovery path. The derived card restores availability without weakening the lockout — identity is re-proved via the registered email (single-use, time-limited link), the failure counter is cleared, and all active sessions are invalidated (RN11). |
| CH-02 | **D2 — Description refinement** | `R8.2` description | `R8.2` description + `{U.C. 8.2}` MSS step 3 + extension 3a | `NFR-RN21` (GDPR Art. 17), `NFR-RN20` (GDPR Art. 20 + Art. 15(3)) | Art. 17 erasure is irreversible; once erasure executes, the portability/access rights (Art. 20, Art. 15(3)) can no longer be served. The V0 description had no export offer inside the closure flow, so the combined obligation could not bind. The refinement inserts the final-export offer (card description + use case step + extension), preserving the card's ID, origin, and scope. |
| CH-03 | **D2 — Description refinement** | `R7.2` description | `R7.2` description + `{U.C. 7.2}` extension 6a1 | `NFR-RN15` (CRA Annex I Part I (2)(l)) + `PRIN-ENG-04` (Fail-Securely) | The V0 description ended at "before applying plan restrictions" — the restricted state was undefined, leaving the fail-securely translation of billing failure untestable. The refinement defines it: read-only project consultation and data export are preserved; content modification and member invitations are suspended until billing is rectified. |
| CH-04 | **D3 — Priority re-evaluation** | `R1.2` Should | `R1.2` Must (Table 6, card, traceability matrix) | `PO-D-01.4-001` (GDPR Art. 5(1)(d) + Art. 16 — accuracy & rectification; CSF PR.DS-01, PR.DS-10; verification `TEST`) | Profile editing is the mechanism through which the data subject obtains rectification of inaccurate personal data without undue delay. A `Should` priority permits a deferral incompatible with a GDPR data-subject right under a regulation confirmed applicable to this case. |

---

## 3. Evaluated, No Change

| Candidate | Type considered | Driving obligation | Decision & rationale |
|---|---|---|---|
| `Terminate active sessions` as standalone card | D1 | `NFR-RN11` | Rejected — company-scale discipline (R13). RN11 is satisfiable server-side within existing functions (`R1.1` password reset, `R8.2` closure) and use case extensions; a dedicated session-management screen would inflate an 8-person micro-SaaS scope. Session invalidation is already asserted in the guarantees of `{U.C. 1.3}`, `{U.C. 1.2}` (extension 4c), and `{U.C. 8.2}`. |
| `R2.3` Monitor workspace activity (Could) | D3 | `NFR-RN22` | No elevation — RN22 constrains the purpose limitation of the data the feature aggregates; it does not oblige the feature's existence. If the card is deferred, no aggregation occurs and no obligation is violated. |
| `R3.2` Archive completed projects (Should) | D3 | GDPR Art. 5(1)(e) (storage limitation) | No elevation — storage limitation constrains retention; it does not mandate an archiving feature. |
| `R6.2` Receive alerts and daily digests (Should) | D3 | `NFR-RN16` | No elevation — webhook origin verification constrains the integration channel; it does not oblige notifications. |
| Card split | D4 | — | None identified — no V0 card bundles capabilities with distinct security surfaces requiring separate lifecycle or priority. |

---

## 4. Coverage Recap

- Functional set: 18 (V0, locked) → **19** (V1): +1 derived (`R1.3`); 2 descriptions refined (`R7.2`, `R8.2`); 1 re-prioritized (`R1.2`).
- Priorities: 15 Must / 2 Should (`R3.2`, `R6.2`) / 2 Could (`R2.3`, `R4.3`).
- Use cases: 19 `{U.C.n.m}` (18 + `{U.C. 1.3}`); PUCs: 19 (18 + `PUC 1.3`).
- Every entry above is materialized in `../v1_security_privacy_synthesis/Doc01` (cards, Table 6, Table 8) and `Doc02` (traceability matrix, use cases) and recorded in the documents' Version History (`Doc01` 3.0.0; `Doc02` 3.2.0). `v0_functional_baseline/` is untouched.

---

## 5. Open Traceability Observations (pre-existing, outside this pass)

- The absorbed chains of `RN19`, `RN20`, `RN21`, `RN22`, and `RN25` cite `PO-D-06.1-001` / `PO-D-06.2-001`, but this case's Phase 2 deliverable (`../../02_PHASE2_RULES/Doc01_Operational_Objectives.md`) defines D-06 as Supply Chain & Third-Party Security (`SO-D-06.1-*`, `SO-D-06.2-*` only) and carries the data-subject-rights objectives under `PO-D-05.1`–`PO-D-05.4` (minimization, retention, erasure, portability) and `PO-D-01.4` (accuracy/rectification). The cited `PO-D-06.*-001` IDs do not exist in this case's Phase 2.
- Correction requires a dedicated chain-recalibration pass across the absorbed constraint rows, the STEP2/STEP4 dossiers, and the analysis tables; it is deliberately not mixed into the refinement pass. The CH-04 driver `PO-D-01.4-001` is verified directly against the Phase 2 deliverable.
