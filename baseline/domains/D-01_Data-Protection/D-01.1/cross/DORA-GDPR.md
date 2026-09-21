# D-01.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim — SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(b) "ongoing confidentiality, integrity, availability and resilience"):**
> Art. 5(1)(f) integrity and confidentiality … appropriate security of the personal data. Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

**DORA article (verbatim from SR-DORA-001, Art. 9(2)):**
> Art. 9(2) ICT security policies, procedures, protocols and tools that aim to ensure the resilience, continuity and availability of ICT systems and to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- GDPR scope: personal data.
- DORA scope: "data" of the financial entity (4×3 CIA+A matrix; the OJ does not say "personal data"; this is all ICT-supported data including non-personal).
- Scope overlap: Y (conditional) when the financial entity processes personal data — typically true.

**Trigger comparison:**
- GDPR trigger: continuous + on material change.
- DORA trigger: continuous + annual scenario review (Art. 7(2) sentence 2 "at least yearly" hard anchor; Art. 9(4) chapeau continuous).
- Trigger alignment: PARTIAL (DORA adds the annual scenario-review trigger; GDPR adds the Art. 35(11) DPIA-on-change trigger).

**Threshold/timeline comparison:**
- GDPR: "appropriate" / risk-based.
- DORA: "high standards" (VAG-S3; R1 best practice / R2 published standards / R3 frontier research; reading chosen in SR-DORA-001: R1 with R2 dominant EU supervisory reading).
- Tension: NONE on the substantive threshold — both are risk-anchored; DORA's "high standards" anchor is qualitatively similar but OJ-text softer than CRA's "state-of-the-art". The temporal anchor divergence (GDPR "regularly" vs DORA "continuous" + "at least yearly") is in D-02.1, not D-01.1.

**Recipient comparison:**
- GDPR: supervisory authority.
- DORA: competent authority (national CA, ESAs depending on entity type).

**Content template comparison:**
- GDPR: technical-and-organis measures + DPIA.
- DORA: ICT risk-management framework under Art. 6(8) + classification-driven cipher strength under Art. 9(4)(d) (relevant for D-01.3).

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two obligations are the same on the at-rest dimension: high-standards/at-appropriate-level encryption of data at rest. The principal divergence (DORA 4×3 CIA+A vs GDPR 3×CIA) is in scope dimensions, not in the at-rest/encryption cell where they overlap. Both share the same OJ reality: a single at-rest control deployed on a DORA financial entity that is a GDPR controller satisfies both, with the classification-driven overlay from DORA adding cipher-strength tiering.

**Scope-disjoint test:** Y — the DORA financial entity is the GDPR controller on the same data assets.

**Downstream implication:** Stack-merge with overlay: DORA's classification-driven cipher-strength tiering (PR.DS-01 + GV.RM-04 per SR-DORA-003) sits on top of the joint at-rest encryption; for a DORA financial entity that is also a GDPR controller, a tiered key-management architecture addresses both.

---


## Summary (Domain Analysis)

| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-001, Art. 32(1)(a)/(b)) | Personal data confidentiality at rest with risk-anchored baseline | Personal-data scope; risk-based + state-of-the-art |
| **DORA** (SR-DORA-001, Art. 9(2)) | Cross-state CIA+A matrix (4×3) maintained at "high standards" | Financial entity; ICT-system scope; explicit at-rest, in-use, in-transit enumeration; "high standards" OJ-literal |

**Why Complementary**: DORA's CIA+A at-rest obligation is broader in dimensions (4 vs GDPR's 3) and broader in scope (ICT system vs personal data), but DORA's "high standards" anchor is qualitatively softer than GDPR's Art. 32 risk-based floor. A DORA financial entity processing personal data is doubly bound; the stricter of the two (typically GDPR's data-minimisation + accuracy overlay) governs when the regulations overlap. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-001; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

