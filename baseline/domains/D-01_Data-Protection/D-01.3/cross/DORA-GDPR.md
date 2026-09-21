# D-01.3 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim — SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a)):**
> Art. 4(5) … additional information is kept separately and is subject to appropriate technical and organisational measures. Art. 32(1)(a) pseudonymisation and encryption of personal data.

**DORA article (verbatim — SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)):**
> Art. 9(4)(d) … strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- GDPR: personal data + key separation (Art. 4(5)).
- DORA: financial-entity ICT data + key-protection + classification-driven cipher strength (Art. 9(4)(d) 3-control AND of strong-auth, key protection, encryption).
- Scope overlap: Y (conditional) when the DORA financial entity processes personal data.

**Trigger comparison:**
- GDPR: continuous + breach-context.
- DORA: continuous + classification-driven.
- Trigger alignment: PARTIAL — DORA adds the classification-driven sub-trigger (data-classification changes drive re-tuning of cipher strength per Art. 9(4)(d)).

**Threshold/timeline comparison:**
- GDPR: "appropriate" + unintelligibility.
- DORA: classification-driven (the classification and risk assessment drive cipher strength; R1 entity-internal classification with R2 supervisory-recognised as expectation per SR-DORA-003 ambiguity_notes).
- Tension: NONE on substantive threshold; DORA adds the depth-over-classification axis that GDPR does not have.

**Recipient comparison:**
- GDPR: SA.
- DORA: CA.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** DORA's 3-control AND (strong auth + key protection + encryption, classification-driven) is the entity-level architecture; GDPR's key separation (Art. 4(5)) is the personal-data-side method that earns the Art. 34(3)(a) carve-out. A DORA financial entity processing personal data operates both: the strong-auth + key-protection + classification-driven tiering (DORA Art. 9(4)(d)) + the de-attribution test for personal data (GDPR Art. 4(5)).

**Scope-disjoint test:** Y for the DORA financial entity.

**Downstream implication:** Stack-merge with overlay. DORA's classification-driven tiering (PR.DS-01 + GV.RM-04) sits above GDPR's PR.DS-01 + PR.IR-03 de-attribution/resilience pair.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a)) | Key separation; de-attribution; unintelligibility carve-out | Personal-data scope; PR.DS-01 + PR.IR-03 (resilience) |
| **DORA** (SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)) | Strong authentication + cryptographic-key protection + encryption (3-control AND); classification-driven cipher strength | Financial entity; PR.AA-03 + PR.AA-04 (authentication layer) + PR.DS-01 + GV.RM-04 (key-management) |

**Why Complementary**: DORA's 3-control AND couples key protection with strong authentication and encryption — the key-management obligation is one leg of a wider authentication-and-cryptography architecture. GDPR's key-management obligation is paired with pseudonymisation/encryption and serves the Art. 34(3)(a) carve-out. A DORA financial entity processing personal data must operate both: GDPR's pseudonymisation-separation test + DORA's classification-driven cipher strength. The two obligations are compatible because DORA's classification-driven layer (PR.DS-01 + GV.RM-04) and GDPR's de-attribution test (PR.DS-01 + PR.IR-03) share the same PR.DS-01 anchor. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-003; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002 + SR-DORA-003



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
39 lines — see ../../_migration_report.md)_

