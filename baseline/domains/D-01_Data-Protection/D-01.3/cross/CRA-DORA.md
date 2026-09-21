# D-01.3 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-004, Annex I Part I (2)(d) + (2)(e)):**
> Annex I Part I (2)(e) … by encrypting … and by using other technical means. Annex I Part I (2)(d) protect from unauthorised access by appropriate control mechanisms.

**DORA article (verbatim — SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)):**
> Art. 9(4)(d) … strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA: product-level key separation (functional RBAC).
- DORA: entity-level key protection (HSM-anchored custodianship + split-knowledge + rotation cadence scaled to criticality).
- Scope overlap: Y (conditional) when a DORA financial entity deploys a CRA-regulated product.

**Trigger comparison:**
- CRA: design-time.
- DORA: continuous + classification-driven re-tuning.
- Trigger alignment: PARTIAL (DORA adds the classification-driven sub-trigger).

**Threshold/timeline comparison:**
- CRA: functional RBAC separation.
- DORA: HSM + split-knowledge + classification-tiered cipher strength + quorum-based key recovery.
- Tension: NONE — CRA is the necessary-but-not-sufficient product-side floor; DORA is the entity-side depth layer.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA floor + DORA overlay. The CRA product-level RBAC separation is necessary but not sufficient for DORA; DORA requires HSM-anchored custodianship, split-knowledge ceremonies, classification-tiered rotation, and quorum-based recovery. The pair is genuinely layered in depth, not scope-disjoint.

**Scope-disjoint test:** Y (DORA financial entity deploying CRA product).

**Downstream implication:** Stack-merge with depth-layer overlay. CRDA's depth framing is correct; the proportional cost is materially higher for the DORA layer (small SaaS in CRA scope only meets the floor with HSM-anchored custodianship + rotation; DORA financial entity requires the full split-knowledge + quorum-recovery stack).

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-004, Annex I Part I (2)(d)+(e)) | Cryptographic key separation from operational environment | Product-level; functional RBAC separation |
| **DORA** (SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)) | Cryptographic-key protection with classification-driven cipher strength + HSM/split-knowledge | Financial entity; entity-level key-custodian + classification-driven |

**Why Complementary**: CRA's product-level key-separation invariant is a necessary but not sufficient condition for DORA's entity-level key-management architecture. A DORA financial entity deploying a CRA-regulated product inherits the product-side separation, but must additionally operate entity-level HSM-anchored custodianship, split-knowledge ceremonies, rotation cadences scaled to data criticality, and quorum-based key-recovery procedures. The CRA floor + the DORA classification-driven overlay are the Layer 2/3 reconciliation point. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-004; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002 + SR-DORA-003



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim — SR-CRA-004, Annex I Part I (2)(d) + (2)(e)):**
> Annex I Part I (2)(e) … by encrypting … and by using other technical means. Annex I Part I (2)(d) protect from unauthorised access by appropriate control mechanisms.

**DORA article (verbatim — SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)):**
> Art. 9(4)(d) … strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- CRA: product-level key separation (functional RBAC).
- DORA: entity-level key protection (HSM-anchored custodianship + split-knowledge + rotation cadence scaled to criticality).
- Scope overlap: Y (conditional) when a DORA financial entity deploys a CRA-regulated product.

**Trigger comparison:**
- CRA: design-time.
- DORA: continuous + classification-driven re-tuning.
- Trigger alignment: PARTIAL (DORA adds the classification-driven sub-trigger).

**Threshold/timeline comparison:**
- CRA: functional RBAC separation.
- DORA: HSM + split-knowledge + classification-tiered cipher strength + quorum-based key recovery.
- Tension: NONE — CRA is the necessary-but-not-sufficient product-side floor; DORA is the entity-side depth layer.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA floor + DORA overlay. The CRA product-level RBAC separation is necessary but not sufficient for DORA; DORA requires HSM-anchored custodianship, split-knowledge ceremonies, classification-tiered rotation, and quorum-based recovery. The pair is genuinely layered in depth, not scope-disjoint.

**Scope-disjoint test:** Y (DORA financial entity deploying CRA product).

**Downstream implication:** Stack-merge with depth-layer overlay. CRDA's depth framing is correct; the proportional cost is materially higher for the DORA layer (small SaaS in CRA scope only meets the floor with HSM-anchored custodianship + rotation; DORA financial entity requires the full split-knowledge + quorum-recovery stack).

---


---


