# D-06.3 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS 2 article (verbatim, Art. 21(3) sentence 1):**
> "When considering which of the measures referred to in the first subparagraph are appropriate, essential and important entities shall take into account the vulnerabilities specific to each direct supplier and service provider, the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures …" — NIS 2 Art. 21(3)

**CRA article (verbatim, Art. 13(6) sentence 1):**
> "Upon identifying a vulnerability in a component integrated in the product with digital elements, the manufacturer shall report the vulnerability to the person or entity manufacturing or maintaining that component, and address and remediate the vulnerability in accordance with the vulnerability handling requirements set out in Annex I, Part II." — CRA Art. 13(6) sentence 1

**Scope comparison:**
- NIS 2 scope: supplier assessment (entity-side, ex-ante).
- CRA scope: component vulnerability reporting, remediation, and OSS sharing (manufacturer-side, post-contract).
- Scope overlap: **N (typically) — different lifecycle stages.** NIS 2 is ex-ante (before contracting); CRA is post-contract (during product lifecycle).

**Trigger comparison:**
- NIS 2 trigger: per-supplier assessment.
- CRA trigger: per-component vulnerability identification.
- Trigger alignment: **DIFFERENT** — ex-ante vs post-contract.

**Threshold/timeline comparison:**
- NIS 2: "appropriate and proportionate" (Art. 21(1)).
- CRA: "without delay" (Art. 13(6) — vulnerability reporting).
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- CRA: component supplier + MSA.

**Content template comparison:**
- NIS 2: supplier-assessment record (vulnerabilities + quality + secure-development procedures).
- CRA: Annex VII §2 component-vulnerability handling record + upstream reporting.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 supplier-assessment obligations are *ex-ante* (before contracting); CRA component-vulnerability reporting is *post-contract* (during the product lifecycle). Layered: NIS 2 determines whether to contract; CRA governs what happens to the components during the product life.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — different lifecycle stages.** Conditional overlap when a NIS 2 entity deploys a CRA-classified product: the entity does NIS 2 assessment before contracting; the manufacturer does CRA reporting throughout the lifecycle.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer record: (1) NIS 2 supplier-assessment ex ante; (2) CRA component-vulnerability reporting post-contract. The COMPLEMENTARY label is preserved.

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-023 + SR-NIS2-024, Art. 21(3)) | Supplier product quality + secure-development procedures assessed per criticality |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-023, SR-NIS2-024 |
| **CRA** (SR-CRA-051, Art. 13(6)) | Component vulnerability reporting, remediation, and OSS sharing |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-051 |

**Why complementary**: NIS2 supplier-assessment obligations are *ex-ante* (before contracting); CRA component-vulnerability reporting is *post-contract* (during the product lifecycle). Layered: NIS2 determines whether to contract; CRA governs what happens to the components during the product life.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

