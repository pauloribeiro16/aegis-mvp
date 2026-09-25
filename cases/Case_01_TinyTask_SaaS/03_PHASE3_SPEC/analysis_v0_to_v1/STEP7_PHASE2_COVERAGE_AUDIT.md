# STEP 7 — Phase 2 Coverage Audit (exhaustive objective ↔ functionality mapping)

> **Case Study:** Case 01 — TinyTask SaaS  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Purpose:** Verify that **every** Phase 2 objective (`PO-`/`SO-`) and engineering principle (`PRIN-ENG-*`) is applied to the Phase 3 requirements (R/RN) and use cases — in both directions — and that requirements are informed by the controls each objective publishes.  
> **Bar (researcher rule):** the mapping must be exhaustive, with every objective placed where a person can judge whether it makes sense — an objective with no functional carrier is a *recorded decision*, never an omission.  
> **Scope:** V0 and the V0→V1 transition (as-is state, before the conformant mapping of `../../synthesis_rounds/OBJECTIVE_MAPPING.md`).

---

## 1. Inventories

| Layer | Count | Detail |
|---|---|---|
| Phase 1 scope | 35 sub-domains / 62 AGs | the full canonical selection (`01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md`) |
| Phase 2 objectives | **62** (12 PO + 50 SO) | `02_PHASE2_RULES/Doc01_Operational_Objectives.md` |
| Phase 2 principles | **7** | `PRIN-ENG-01`–`07` (`Doc02_Secure_Design_Principles.md`) |
| Analysis skills available | **7** | `baseline/skills/`: attack-surface, trust-boundary, least-privilege, fail-safe-defaults, verifiability, data-minimization, lifecycle-erasure |
| Phase 3 V1 | 19 R cards, 26 RNs, 19 UCs | `v1_security_privacy_synthesis/` |

## 2. Forward coverage (objective → requirement/UC)

| Verdict | Count | Detail |
|---|---|---|
| **Applied** | 10 | SO-D-01.1-002, 02.1-002, 02.2-002, 03.1-002, 05.1-002, 07.1-002, 08.1-002; PO-D-01.1-001, 01.2-001, 01.4-001 |
| **Cited but nonexistent (phantom)** ⚠ | 3 | PO-D-06.1-001 (×17), PO-D-06.2-001 (×10), PO-D-03.1-001 (×6) — 33 chain citations point to objectives that do not exist in this case's Phase 2 |
| **Never applied** | **49** | zero mentions across requirements, RNs, use cases, and the dossier (e.g., all of D-04 Incident Response, D-06 Supply Chain, D-09 Governance product rows, SO-D-03.1-001 identity verification for rights requests, SO-D-05.3-002 permanent data removal, SO-D-07.2-002 attack-surface limitation) |

**Coverage: 10/62 real objectives ≈ 16%.** Whether each of the 49 is genuinely carrier-less (organizational/process control per ADR-002) or a missed constraint is *undecidable from the current documents* — they are simply absent, which is the defect this audit records. The conformant mapping (`../../synthesis_rounds/OBJECTIVE_MAPPING.md`) gives every one of the 62 an explicit verdict.

## 3. Reverse coverage (requirement/UC → objective)

- Every absorbed constraint chain cites objectives — but the 6 GDPR-derived RNs (19, 20, 21, 22, 25, 26) cite the phantom POs, so their upstream warrants are unverifiable.
- **Principles:** 6/7 bind in chains; **PRIN-ENG-05 (Atomic Verifiability)** appears only in STEP2's listing box — it never binds anything (ironic, since the fit-criteria practice realizes it).
- **Use cases:** inherit 1:1 from R cards via the traceability matrix — internally consistent, but they inherit exactly the same 16%.
- **V0:** zero objectives — correct by design (pure functional baseline).

## 4. Skills application

**0/7 skills referenced anywhere in the Phase 3 lane.** The guidelines designate the functional cards as the anchor canvas for skill-driven analysis, but the Case_01 derivation never invoked a skill as its analysis lens.

## 5. Control influence on requirements (the decisive test)

Per the researcher's model, each objective/publishes a control set (final column of the Phase 2 deliverable), and requirements should be written *against* those controls. Comparison of published sets vs the anchors actually cited by the chains:

| Objective | Published controls (Phase 2) | Anchors cited by RN chains | Verdict |
|---|---|---|---|
| PO-D-01.1-001 | PR.DS-01, PR.DS-10 | PR.DS-01, PR.DS-10 (RN23) | ✅ |
| PO-D-01.2-001 | PR.DS-02, PR.IR-01 | PR.DS-02, PR.IR-01 (RN24) | ✅ |
| PO-D-01.4-001 | PR.DS-01, PR.DS-10 | (no anchors — D3 elevation, STEP5 CH-04) | ✅ n/a |
| SO-D-01.1-002 | PR.DS-01 | PR.DS-01 ✔ + PR.AA-03 ✗ (RN10) | ⚠ partial |
| SO-D-02.1-002 | PR.PS-02, PR.IR-03, ID.RA-01, PR.PS-01 | PR.AA-05, PR.DS-01 (RN9); PR.AA-03 (RN10); PR.AA-05/06 (RN12); PR.AA-01 (RN17) | ❌ systematic |
| SO-D-02.2-002 | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | PR.AA-03, PR.DS-02 (RN11) | ❌ |
| SO-D-03.1-002 | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | PR.PS-04, DE.AE-02 (RN18) | ❌ |
| SO-D-05.1-002 | PR.DS-10, ID.AM-03 | PR.DS-02, PR.AA-05 (RN16); PR.AA-01 (RN17) | ❌ |
| SO-D-07.1-002 | PR.PS-06, PR.PS-01 | PR.PS-06 ✔, PR.PS-02 ✗ (RN13); PR.PS-06 ✔ (RN14) | ⚠ partial |
| SO-D-08.1-002 | PR.AT-01 | PR.DS-02, PR.AA-05 (RN15/16) | ❌ |

**Only RN23 and RN24 are built from the controls their objectives publish.** The CRA-derived chains cite anchors that do not belong to the cited objective's set — several actually belong to *other* objectives (e.g., RN12's PR.AA-05/PR.AA-06 belong to SO-D-02.2-002/SO-D-03.x, not SO-D-02.1-002), indicating ad-hoc anchor selection rather than control-driven derivation.

**Additional driver-integrity finding:** several objectives are cited for constraints outside their subject matter — SO-D-02.2-002 (*security updates*) drives RN11 *session management*; SO-D-03.1-002 (*identity/credential management*) drives RN18 *audit logging*; SO-D-08.1-002 (*user instructions*) drives RN15/16 *billing/webhooks*. The natural drivers exist in Phase 2 (e.g., SO-D-03.2-002/SO-D-03.3-002 for isolation and access, SO-D-04.1-002/SO-D-10.1-002 for activity recording, SO-D-07.2-002 for attack surface, SO-D-01.4-002 for integrity) but were never used.

## 6. Verdict

The process described by the researcher — exhaustive objective↔functionality mapping in the early steps, skill-driven analysis per applicable objective, and requirements derived from the controls each objective publishes — **was not followed**. What exists is internally consistent but covers ~16% of the objective set, uses no skills, and derives anchors ad hoc for most CRA chains.

## 7. Conformance actions (executed in `../../synthesis_rounds/OBJECTIVE_MAPPING.md` + Register Round 1)

1. Exhaustive 62-objective + 7-principle mapping with per-objective verdicts (applies / no functional carrier — recorded decision).
2. Skill citation per applicable objective.
3. Chain recalibration: phantom POs remapped to real objectives (PO-D-05.1/05.2/05.3/05.4-001, PO-D-09.4-001); anchors corrected to the cited objective's published set.
4. Driver-integrity re-assignments proposed through the round cycle (Round 1 adjustments) — the client accepts or rejects them.
5. Anchor-integrity rule codified in the manual (chain anchors ∈ published set of the cited objective; extras need W4 rationale).
