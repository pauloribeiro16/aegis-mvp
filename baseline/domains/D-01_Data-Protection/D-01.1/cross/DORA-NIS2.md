# D-01.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS 2 article (verbatim — SR-NIS2-001, Art. 21(2)(h)):**
> Article 21(2)(h) … establish policies and procedures regarding the use of cryptography and, where appropriate, encryption.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) ICT security policies, procedures, protocols and tools … to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- NIS 2 scope: entity-level "network and information systems".
- DORA scope: entity-level ICT of financial entities; "data" (no personal-data qualifier).
- Scope overlap: Y — a DORA financial entity that is also a NIS 2 essential entity (per NIS 2 §9 fall-back clause, DORA is lex specialis in the financial sector, so this only applies to non-financial-sector NSIEs that fall under DORA-fall-back or to entities in adjacent sectors).

**Trigger comparison:**
- NIS 2: continuous + Art. 21(1) framework review.
- DORA: continuous + annual scenario review.
- Trigger alignment: SAME on substance; PARTIAL on temporal cadence.

**Threshold/timeline comparison:**
- NIS 2: "where appropriate" on encryption + "state of the art" on cryptography policy.
- DORA: "high standards" on the CIA+A matrix (no explicit cipher-strength measurement; pending ESAs RTS under Art. 15).
- Tension: NONE on the substantive baseline; DORA's OJ is explicit on the 3-way data-state OR (at-rest/in-use/in-transit — all required for cross-state coverage per SR-DORA-001 R1 reading), while NIS 2 is silent on the in-use dimension.

**Recipient comparison:**
- NIS 2: CSIRT or CA.
- DORA: national CA + ESAs.

**Classified relationship (from CRDA):** EQUAL.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — no change).

**Reasoning:** Both impose an entity-level cryptography-policy obligation anchored to a risk-based test. The principal OJ-level divergence is DORA's explicit enumeration of three data states (at-rest / in-use / in-transit) where NIS 2 is silent on in-use; this is a **scope dimension difference, not a substantive threshold difference on the at-rest cell**. CRDA's EQUAL is sustained as the classification, with the qualifier that DORA is **more demanding by inclusion** (the in-use dimension) but **not more demanding on the at-rest anchor**.

**Scope-disjoint test:** Y for the DORA financial entity that is also a NIS 2 essential entity; N (disjoint in baseline) for the NIS 2 essential entity in the financial sector (DORA is lex specialis).

**Downstream implication:** Stack-merge for the cross-sector entity; lex specialis for the financial entity (DORA absorbs the NIS 2 obligation).

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **Equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-001, Art. 21(2)(h)) | Cryptography policy + "where appropriate" encryption | Entity-level; "where appropriate" hedge + appropriate-and-proportionate |
| **DORA** (SR-DORA-001, Art. 9(2)) | CIA+A 4×3 matrix; at-rest/in-use/in-transit all required | Financial entity; OJ-explicit 3-state OR (all required for the protection to be effective across the data lifecycle) |

**Why Equal (with scope qualifier)**: both regulations are entity-level cryptography-policy obligations; the principal difference is the OJ explicitness on data states (DORA explicit 3-state; NIS 2 silent on the in-use dimension) and the threshold anchor (NIS 2 appropriate-and-proportionate; DORA "high standards"). A DORA financial entity that is also a NIS 2 NSIE (e.g. a large credit institution designated as essential entity of a specific type) is jointly bound; the DORA "high standards" anchor and NIS 2 appropriate-and-proportionate filter operate in parallel. → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-001; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
39 lines — see ../../_migration_report.md)_