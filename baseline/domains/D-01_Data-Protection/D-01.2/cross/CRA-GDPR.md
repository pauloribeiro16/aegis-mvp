# D-01.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim — SR-GDPR-002, Art. 32(1)(b) + Art. 32(2)):**
> Art. 32(1)(b) the ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 32(2) in assessing the appropriate level of security account shall be taken in particular of the risks … from accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed.

**CRA article (verbatim — SR-CRA-003, Annex I Part I (2)(e) + (2)(j)):**
> Annex I Part I (2)(e) … by encrypting relevant data at rest or in transit using state-of-the-art mechanisms. Annex I Part I (2)(j) limit attack surfaces … including external interfaces.

**Scope comparison:**
- GDPR: personal data in transit (Art. 32(2) "transmitted").
- CRA: data in transit through product with digital elements (personal or other).
- Scope overlap: Y when the CRA product transmits personal data.

**Trigger comparison:**
- GDPR: continuous + on material change.
- CRA: continuous.
- Trigger alignment: SAME.

**Threshold/timeline comparison:**
- GDPR: "appropriate" anchored to Art. 32(2) risk events.
- CRA: "state-of-the-art mechanisms".
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- CRA: MSA + ENISA.

**Content template comparison:**
- GDPR: technical-and-organis measures + risk assessment of the five-event enumeration.
- CRA: transport-security profile in technical documentation (Annex VII §2(b)).

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two impose the same in-transit confidentiality obligation on the same artefacts (channels transmitting personal data), with the same PR.DS-02 + PR.IR-01 CSF anchors. The CRA substrate is stricter (state-of-the-art) than GDPR's risk-anchored layer; meeting CRA discharges GDPR on the in-transit channel. The Annex I (2)(j) attack-surface-limitation leg is the additional CRA primitive (the in-transit control + surface limitation as a pair) that GDPR does not separately require.

**Scope-disjoint test:** Y when the same product transmits personal data; disjoint in baseline (CRA manufacturer ≠ GDPR controller).

**Downstream implication:** Stack-merge on the same channel; a CRA-compliant TLS configuration + network-segmentation profile discharges the GDPR Art. 32(1)(b)/(2) in-transit control.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-002, Art. 32(1)(b) + Art. 32(2)) | In-transit confidentiality across networks and inter-service channels | Risk-anchored; personal-data scope; 5-event Art. 32(2) risk enumeration |
| **CRA** (SR-CRA-003, Annex I Part I (2)(e)+(j)) | Confidentiality of data in transit; in-transit = one channel of Annex I (2)(e) broader obligation | State-of-the-art; product-level; "personal or other"; attack-surface-limitation (2)(j) supports the in-transit scope |

**Why Complementary**: GDPR anchors in-transit protection to the Art. 32(2) 5-event risk enumeration (destruction, loss, alteration, unauthorised disclosure, access on transit), with PR.DS-02 + PR.IR-01 as the operational substrate. CRA anchors to the same Annex I (2)(e) umbrella as D-01.1 (the at-rest / in-transit separation is OJ-literal but operationally continuous), with PR.DS-02 + PR.IR-01 also as the substrate. The two are complementary because CRA's product-level state-of-the-art is the floor; GDPR's risk-anchored layer applies above it for personal data. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-002; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-003



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

