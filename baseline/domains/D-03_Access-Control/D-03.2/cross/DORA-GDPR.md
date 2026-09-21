# D-03.2 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- GDPR scope: authorised-person confidentiality and instruction-bound processing.
- DORA scope: financial-entity strong authentication and key protection.
- Scope overlap: Conditional where a financial entity processes personal data.

**Trigger comparison:**
- GDPR trigger: personal-data processing by authorised persons.
- DORA trigger: continuous financial-entity ICT-control obligation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: no explicit MFA requirement.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- GDPR: controller/processor accountability and supervisory authority if audited.
- DORA: financial competent authority and management body accountability.

**Content template comparison:**
- GDPR: confidentiality undertakings and instruction records.
- DORA: strong-authentication standard, control-system and key-protection evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** DORA provides the stronger authentication floor; GDPR provides the staff-side legal authority and confidentiality layer. The source text also preserves the DORA gap: the OJ says strong authentication, not expressly multi-factor authentication. Doc 07 should not overstate the OJ wording.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should set DORA strong authentication as the operative financial-sector floor and cite GDPR only for authorised-person controls.


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-011 + SR-GDPR-012, Art. 28(3)(b) + Art. 29) | No explicit MFA; staff instructions + confidentiality | Controller/processor; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication mechanisms (T4 reads MFA; OJ says "strong authentication" — T4-vs-text gap) | Financial entity; PR.AA-03 + PR.AA-04 |

**Why Complementary**: DORA's strong-authentication obligation (Art. 9(4)(d)) is the principal financial-sector MFA anchor; the dominant EBA Guidelines reading is MFA but the OJ text says only "strong authentication mechanisms". A DORA financial entity processing personal data is bound by DORA's strong-authentication + GDPR's staff-side instructions + confidentiality. The two are compatible: DORA's strong-authentication is the authentication mechanism; GDPR's instructions + confidentiality are the surrounding obligations. **Caveat:** the T4-vs-text gap on DORA's "strong authentication" vs MFA creates a reading-choice risk; the SR-DORA-002 ambiguity notes preserve both the mechanism-agnostic literal reading and the dominant EBA MFA reading. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-011; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

