# Step 3 — EARS Formulation & Client Acceptance (Round 1)

> **Ledger:** [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) — authoritative per-constraint formulations (EARS, risk, fit criterion, verification method, chain) and control selections.

## 1. Formulation discipline

All 20 constraints (RN11–RN30) were formulated at altitude L2 (technology-neutral control objectives) in EARS syntax, each with a binary Volere fit criterion, an ISO 29148 verification method (`TEST` ×15, `INSPECT` ×4, `DEMONSTRATE` ×1 — RN29), and the full chain `regulation article → Phase 2 objective(s) → PRIN-ENG → published control anchors`. The Specificity Matching rule was applied during derivation: no mechanism categories or parameters beyond the W2-warranted wording (e.g., "state-of-the-art", "statutory floor").

## 2. Presentation and verdicts

The 71 Round-1 items were presented to the client in **five plain-language batches** (business substance, not internal IDs):

| Batch | Content | Items | Verdict |
|---|---|---|---|
| 1 | "Contabilidade" — attach the legal citation to each function the product already has (51 chain bindings) | 51 | **Accept** |
| 2 | Cryptographic protection of biometric data (RN11 at-rest, RN12 key separation, RN13 transit, RN14 integrity) | 4 | **Accept** |
| 3 | High-risk AI obligations (RN15 resilience/rollback, RN24 logging, RN25 post-market, RN29 oversight, RN30 transparency) | 5 | **Accept** |
| 4 | Identities & access (RN16 identity verification, RN17 lifecycle, RN18 MFA, RN19 role mediation, RN20 secure defaults) | 5 | **Accept** |
| 5 | Incidents, notifications, updates & rights (RN21 unified timelines, RN22 recording, RN23 lifecycle closure, RN26 awareness, RN27 updates, RN28 erasure/portability) | 6 | **Accept** |

## 3. Convergence

**20/20 constraint accepts + 51/51 chain-binding accepts — 0 Rejects (= no explicit risk acceptances), 0 Adjusts — Round 1 converged on 2026-09-28 with no Round 2 required.** No `Doc01`/`Doc02` version evolved before convergence.

## 4. Control Selection (Step 4, executed with the proposals)

Per-constraint selections with source surfaces and rationale are in [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) §3: published sets of the driver objectives (all four ambits publish CSF 2.0 anchors) plus one store-flagged selection (RN28 ← `SR-GDPR-030`, since the erasure driver `PO-D-05.3-001` publishes no anchors). PF anchors accompany GDPR-derived constraints only; AI RMF axes were reviewed for AI-Act constraints and the selected sets follow the published CSF sets (AI RMF available in the store where needed by verification tooling). No out-of-set anchor without W4.
