# Step 4 — Absorption & Traceability Weaving (V1, 2.0.0)

> **Accepted set:** 20 constraints (RN11–RN30) + 51 chain bindings · `part1_security_privacy/v0_functional_baseline/` untouched.

## 1. Doc01 absorption

- **In-card `Security & Privacy Constraints` rows** added to 27 of the 28 requirement cards (`R2.2` has no direct card-level surface — its security behavior binds at `{U.C. 2.2}` via RN18 preconditions): 18 cards carry `NFR-RNxx` lines, 9 carry chain-only lines (`**Chain** …`), several carry both. Every line keeps the full 4-element chain.
- **Table 7** gains the cross-cutting transport row **RN13** (alongside V0 RN1–RN10).
- **No functional change** to the elicited set: no D1/D2/D3/D4 change was required — the V0 elicitation already covered the functional scope; see STEP5.
- Version History **2.0.0**.

## 2. Doc02 weaving

- All **28 use cases elaborated to the fully-dressed Cockburn anatomy** (preconditions, trigger, MSS, extensions, success & minimal guarantees).
- Security behavior woven from the accepted set: biometric protections in {U.C. 1.x} (RN11–RN14), oversight in {U.C. 2.x} (RN19, RN29), access in {U.C. 3.x} (RN17–RN19), rights in {U.C. 4.x} (RN16, RN28 + T-002 token-only leg), incidents/continuity in {U.C. 5.x} (RN22, RN23, RN25, RN26 + resilience chains), the **unified notification clock** in {U.C. 6.1} (RN21, T-001), update channel in {U.C. 7.2} (RN27), pipeline defaults in {U.C. 8.1} (RN20), AI rollback in {U.C. 8.3}/{U.C. 9.2} (RN15), AI governance in {U.C. 9.x} (RN24, RN25, RN30), unified assessments and vendor pass in {U.C. 10.x} (T-003/T-004 chains), oversight competence in {U.C. 11.2} (RN29).
- Traceability matrix (§3.2) carries the bound NFRs per requirement.
- Version History **2.0.0**.

## 3. Matrix synchronization

- `OBJECTIVE_MAPPING.md`: 71 proposal states → **Accepted R1**; totals 92 covered (39 RN-carried + 51 chain + 2 transversal) / 2 organizational / 6 N/A = 100.
- `PRINCIPLE_MAPPING.md`: proposed → Bound (7/7 followed); §2 per-requirement check updated.
- `UC_OBJECTIVE_CORRESPONDENCE.md`: all bindings marked accepted; 28/28 cards, 101 bindings.

## 4. Folder placement

Approved pair stored in `part1_security_privacy/v1_security_privacy_synthesis/` (Doc01 + Doc02 + README, uniform with v0); top-level `Doc01`/`Doc02` remain the synced active copies.
