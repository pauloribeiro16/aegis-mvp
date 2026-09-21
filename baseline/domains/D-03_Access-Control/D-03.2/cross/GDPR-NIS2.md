# D-03.2 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality. Art. 29 reinforces this by binding natural persons acting under the authority of controller or processor to instruction-only processing.

**NIS2 article (verbatim):**
> Article 21(2)(j) of Directive (EU) 2022/2555, in its first clause, requires essential and important entities to use multi-factor authentication or continuous authentication solutions, where appropriate.

**Scope comparison:**
- GDPR scope: staff confidentiality/instructions and data-subject verification; no explicit MFA mandate.
- NIS2 scope: MFA or continuous authentication for essential/important entities where appropriate.
- Scope overlap: Conditional when a controller is also a NIS2 entity.

**Trigger comparison:**
- GDPR trigger: authorised-person processing and rights-request verification context.
- NIS2 trigger: continuous authentication-risk-management duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: no MFA timeline; confidentiality and instruction controls are continuous.
- NIS2: MFA or continuous authentication where appropriate.
- Tension: NONE.

**Recipient comparison:**
- GDPR: controller/processor accountability and data subjects indirectly.
- NIS2: entity governance and NIS competent-authority evidence.

**Content template comparison:**
- GDPR: authorised-person instruction and confidentiality records.
- NIS2: MFA/continuous-authentication policy and risk justification.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** GDPR does not impose MFA. NIS2 supplies the explicit authentication mechanism, while GDPR supplies the surrounding authority and confidentiality duties. The pair is complementary because NIS2 can satisfy authentication strength while GDPR requires processing discipline for those authenticated persons.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should not claim a GDPR MFA mandate; it should use NIS2 as the MFA source and GDPR as the authorisation/confidentiality wrapper.


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011 + SR-GDPR-012, Art. 28(3)(b) + Art. 29) | No explicit MFA; instructions + confidentiality for staff; verification for data subjects | Controller/processor; staff-side via confidentiality obligation; data-subject-side via verification; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| **NIS2** (SR-NIS2-006, Art. 21(2)(j) first clause) | MFA or continuous authentication "where appropriate" | Entity-level; OR of MFA and continuous; "where appropriate" hedge; PR.AA-03 + PR.AA-05 |

**Why Complementary**: GDPR has no explicit MFA mandate; NIS 2 imposes MFA or continuous authentication "where appropriate". A controller that is a NIS 2 essential entity is bound by the NIS 2 MFA/continuous-authentication obligation; the GDPR staff-side instructions + confidentiality (Art. 28(3)(b) + Art. 29) operate on top of the NIS 2 authentication baseline. The two are complementary, with NIS 2 supplying the authentication mechanism and GDPR supplying the instructions + confidentiality dimension. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011 + SR-GDPR-012; `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-006



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

