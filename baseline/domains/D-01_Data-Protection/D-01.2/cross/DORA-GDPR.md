# D-01.2 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim — SR-GDPR-002, Art. 32(1)(b)):**
> Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

**Scope comparison:**
- GDPR: personal data in transit.
- DORA: data in transit of the financial entity (4×3 cell).
- Scope overlap: Y (conditional) when financial entity transmits personal data — typical.

**Trigger comparison:**
- GDPR: continuous.
- DORA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- GDPR: "appropriate".
- DORA: "high standards".
- Tension: NONE.

**Recipient comparison:**
- GDPR: SA.
- DORA: CA + ESAs.

**Content template comparison:**
- GDPR: technical-and-organis measures.
- DORA: ICT security policies + protocols + tools.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two obligations are the same on the in-transit cell of DORA's 4×3 matrix. OJ-explicit "in transit" in DORA vs risk-anchored in GDPR, but the operational substrate (mutual TLS, authenticated channels, network segmentation) is identical. A single in-transit design discharges both.

**Scope-disjoint test:** Y for the DORA financial entity processing personal data.

**Downstream implication:** Single-control — a mutually-authenticated encrypted-channel architecture + documented network-segmentation policy satisfies both.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-002, Art. 32(1)(b)) | In-transit confidentiality with Art. 32(2) risk events | Personal-data scope; PR.DS-02 + PR.IR-01 |
| **DORA** (SR-DORA-001, Art. 9(2)) | CIA+A maintained across data states, including in-transit | Financial entity; CIA+A 4×3 matrix; "high standards" anchor |

**Why Complementary**: DORA's in-transit protection is one cell of the 4×3 CIA+A matrix, with OJ-explicit "in transit" language. A DORA financial entity processing personal data is jointly bound by GDPR's PR.DS-02 + PR.IR-01 (personal-data scope, risk-anchored) and DORA's in-transit cell (CIA+A scope, high-standards-anchored). The two are compatible because both converge on PR.DS-02 as the operational anchor. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-002; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_