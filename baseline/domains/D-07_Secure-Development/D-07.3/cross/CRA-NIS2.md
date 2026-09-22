# D-07.3 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(e) third clause):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (e) … security in the maintenance of network and information systems, including vulnerability handling and disclosure." — Art. 21(2)(e) third clause NIS 2 (per SR-NIS2-028)

**CRA article (verbatim, Annex I Part II (7)+(8)):**
> "The manufacturer shall … (7) securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates; (8) ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take." — CRA Annex I Part II (7)+(8)

**Scope comparison:**
- NIS 2 scope: entity-level maintenance-phase security including vulnerability handling (partial coverage of CI/CD via maintenance dimension).
- CRA scope: product-level update-distribution delivery path (Part II (7)+(8)) — not CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments).
- Scope overlap: **N (typically)** — NIS 2 covers entity-side CI/CD pipeline; CRA covers product-side update delivery path.

**Trigger comparison:**
- NIS 2 trigger: NIS maintenance activity.
- CRA trigger: manufacturer update distribution.
- Trigger alignment: **DIFFERENT** (entity side vs. maker side).

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- CRA: `without delay` (Part II (8)) — qualitative.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: MSA, users.

**Content template comparison:**
- NIS 2: not codified for content.
- CRA: Annex VII §2 design/development documentation.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 covers the entity-side CI/CD pipeline (entity deploying NIS into production); CRA covers the product-side update delivery path (manufacturer distributing security updates). The two regimes meet at the supplier-customer interface — NIS 2 procurement gate (SR-NIS2-026) references CRA-conformant products, and CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway. The CI/CD pipeline security sub-domain has no dedicated OJ mandate in any of the 5 regulations.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different objects (entity-side CI/CD pipeline vs. product-side update delivery path), different actors. Pair is substantively scope-disjoint; CRDA "complementary" is a taxonomy artifact.

**Downstream implication (Phase 1C Doc 07):** Phase 1 entities must construct CI/CD baseline from industry frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA). Pipeline-architecture controls (signed artefacts, build-agent integrity, ephemeral build environments) are industry best-practice, not regulatory mandate.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-028, Art. 21(2)(e) maintenance — partial coverage) | Maintenance-phase security including vulnerability handling and disclosure; partial coverage of CI/CD via maintenance dimension. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-028 |
| **CRA** (SR-CRA-009 / Annex I Part II (7)+(8) — partial coverage of delivery path) | Secure update distribution (Part II (7)) + update dissemination (Part II (8)) — delivery path only, not build-time controls. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-009 (cross-ref to D-07.3 partial) |

**Why complementary**: NIS 2 covers the entity-side CI/CD pipeline (entity deploying NIS into production); CRA covers the product-side update delivery path (manufacturer distributing security updates). The two regimes meet at the supplier-customer interface — NIS 2 procurement gate (SR-NIS2-026) references CRA-conformant products, and CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway.



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(e) third clause):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (e) … security in the maintenance of network and information systems, including vulnerability handling and disclosure." — Art. 21(2)(e) third clause NIS 2 (per SR-NIS2-028)

**CRA article (verbatim, Annex I Part II (7)+(8)):**
> "The manufacturer shall … (7) securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates; (8) ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take." — CRA Annex I Part II (7)+(8)

**Scope comparison:**
- NIS 2 scope: entity-level maintenance-phase security including vulnerability handling (partial coverage of CI/CD via maintenance dimension).
- CRA scope: product-level update-distribution delivery path (Part II (7)+(8)) — not CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments).
- Scope overlap: **N (typically)** — NIS 2 covers entity-side CI/CD pipeline; CRA covers product-side update delivery path.

**Trigger comparison:**
- NIS 2 trigger: NIS maintenance activity.
- CRA trigger: manufacturer update distribution.
- Trigger alignment: **DIFFERENT** (entity side vs. maker side).

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- CRA: `without delay` (Part II (8)) — qualitative.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: MSA, users.

**Content template comparison:**
- NIS 2: not codified for content.
- CRA: Annex VII §2 design/development documentation.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 covers the entity-side CI/CD pipeline (entity deploying NIS into production); CRA covers the product-side update delivery path (manufacturer distributing security updates). The two regimes meet at the supplier-customer interface — NIS 2 procurement gate (SR-NIS2-026) references CRA-conformant products, and CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway. The CI/CD pipeline security sub-domain has no dedicated OJ mandate in any of the 5 regulations.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different objects (entity-side CI/CD pipeline vs. product-side update delivery path), different actors. Pair is substantively scope-disjoint; CRDA "complementary" is a taxonomy artifact.

**Downstream implication (Phase 1C Doc 07):** Phase 1 entities must construct CI/CD baseline from industry frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA). Pipeline-architecture controls (signed artefacts, build-agent integrity, ephemeral build environments) are industry best-practice, not regulatory mandate.

---


---
