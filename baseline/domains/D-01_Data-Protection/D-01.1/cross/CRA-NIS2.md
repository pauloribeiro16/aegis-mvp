# D-01.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS 2 article (verbatim — SR-NIS2-001, Art. 21(2)(h)):**
> Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption.

**CRA article (verbatim — SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (1) ensure an appropriate level of cybersecurity based on the risks presented by the product. Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms.

**Scope comparison:**
- NIS 2 scope: network and information systems (entity-level).
- CRA scope: products with digital elements (product-level).
- Scope overlap: Y (conditional) when a NIS 2 essential entity uses a CRA-regulated product that processes data at rest.

**Trigger comparison:**
- NIS 2: continuous.
- CRA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- NIS 2: "where appropriate" (hedge) on encryption; "state of the art" on cryptography policy.
- CRA: "state-of-the-art mechanisms" on encryption primitives.
- Tension: NONE on substantive floor — both anchor to state-of-the-art; NIS 2's policy obligation admits the CRA product-side baseline as evidence of compliance, with the entity-side key-management, cipher-suite selection and access-control architecture remaining NIS 2's own.

**Recipient comparison:**
- NIS 2: CSIRT or CA.
- CRA: market surveillance authority.

**Content template comparison:**
- NIS 2: documented cryptography policy + Art. 21(1) framework.
- CRA: technical documentation (Annex VII §2/§3) + Annex I risk assessment.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two are layered obligations on the same artefact: CRA is the product-side state-of-the-art baseline; NIS 2 is the entity-side policy + appropriate-and-proportionate deployment. A NIS 2 essential entity using a CRA-regulated product inherits CRA's product-side floor and operates the entity-side policy layer above it. The pair is structurally COMPLEMENTARY (different layers of the same stack) but operationally joint — meeting both is a stack-merge, not a choice.

**Scope-disjoint test:** Y — the NIS 2 essential entity bears both obligations on the same artefact.

**Downstream implication:** Stack-merge. A CRA-compliant product used by a NIS 2 essential entity discharges the product-side encryption floor; the entity adds the policy/appropriate-and-proportionate layer per Art. 21(1).

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-001, Art. 21(2)(h)) | Cryptography policy; encryption "where appropriate" | Entity-level (essential/important); "where appropriate" hedge; appropriate-and-proportionate |
| **CRA** (SR-CRA-001, Annex I Part I (1)+(2)(e)) | State-of-the-art encryption of stored data; "personal or other" | Product-level; state-of-the-art baseline; harmonised-standards anchor |

**Why Complementary**: NIS 2's entity-level policy obligation is met by the cryptography policy a manufacturer supplies with a CRA-regulated product, but the entity remains responsible for deployment-side cryptography choices (key management, cipher-suite selection) that CRA does not cover. CRA's product-level state-of-the-art baseline is the floor; NIS 2's policy + appropriate-and-proportionate filter applies above it. A CRA product used by a NIS 2 entity is jointly bound: product-side state-of-the-art (CRA) + entity-side appropriate-and-proportionate deployment (NIS 2). → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-001; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

