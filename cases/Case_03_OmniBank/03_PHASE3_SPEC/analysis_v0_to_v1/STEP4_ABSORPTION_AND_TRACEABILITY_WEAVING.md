# Step 4 — Absorption & Traceability Weaving (V1, 2.0.0)

> **Accepted set:** 16 constraints (RN11–RN26) + 92 chain bindings · `v0_functional_baseline/` untouched.

## 1. Doc01 absorption

- **In-card `Security & Privacy Constraints` rows** on 36 of the 43 requirement cards (the operating-model cards without a direct security surface stay clean): 16 cards carry `NFR-RNxx` lines, 10 carry chain-only lines, several carry both. Multi-regulation chains cite all demanding objectives on one line.
- **Table 7** gains the cross-cutting transport row **RN13** (alongside V0 RN1–RN10).
- **No functional-set change** — see STEP5.
- Version History **2.0.0**.

## 2. Doc02 weaving

All **43 use cases elaborated to the fully-dressed Cockburn anatomy** with the accepted security behavior: cryptographic protections (RN13–RN15), OmniScore integrity/oversight/logging (RN11, RN22–RN25), access mediation (RN16, RN19–RN21), the unified notification clock (RN18, T-001), token-only retention (RN17, T-002), and the register/resilience families (RN26 + chains). Traceability matrix carries the bound NFRs.

## 3. Matrix synchronization

- `OBJECTIVE_MAPPING.md`: 128 covered (36 RN-carried + 92 chain) / 2 organizational / 4 N/A = 134.
- `PRINCIPLE_MAPPING.md`: 7/7 Bound. `UC_OBJECTIVE_CORRESPONDENCE.md`: all bindings Accepted R1.

## 4. Folder placement

Approved pair stored in `v1_security_privacy_synthesis/`; top-level `Doc01`/`Doc02` remain the synced active copies.
