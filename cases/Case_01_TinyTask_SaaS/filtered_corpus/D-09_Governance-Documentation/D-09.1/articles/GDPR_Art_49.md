---
document_id: AEGIS-PREPROC-GDPR-ART-49
title: GDPR Art. 49 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 49
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# GDPR Art. 49

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-033 | Cross-border transfer of personal data takes place only where the conditions laid down in Chapter V are complied with (Art. 44); where no Commission adequacy decision exists (Art. 45), appropriate safeguards (Art. 46) are in place; absent both, derogations under Art. 49 are used only as narrowly-defined conditions, with the catch-all applying only when transfers are not repetitive, concern a limited number of data subjects, are necessary for compelling legitimate interests, and are accompanied by suitable safeguards. | `GDPR-TR01` (Art. 44); `GDPR-TR02` (Art. 45(1)); `GDPR-TR03` (Art. 45(3) — periodic review); `GDPR-TR04` (Art. 46(1)); `GDPR-TR05` (Art. 46(2)); `GDPR-TR08`–`GDPR-TR10` (Art. 49(1)(a)/(d) and catch-all); `GDPR-C07` (Art. 4(16) — main establishment) | D-06.3, D-09.1, D-05.1 |
| SO-GDPR-033 | D-06.3, D-09.1, D-05.1 | Art. 44, Art. 45, Art. 46, Art. 49, Art. 4(16) | Cross-border transfers maintain GDPR protection level |
| SO-GDPR-032 | Consent to personal-data processing is freely given, specific, informed, and unambiguous; the controller demonstrates the data subject's consent on request; withdrawal of consent is as easy as giving; bundled consent requests are presented in a clearly distinguishable form; conditional consent (bundled with contract) is presumed non-compliant unless processing is strictly necessary for contract performance; special-category consent is at the higher `explicit` standard; child consent (information-society services) is gated by Art. 8 age thresholds and parental-responsibility verification; transfer consent (Art. 49(1)(a)) is `explicit` and risk-informed. | `GDPR-C05` (Art. 4(11) — consent definition); `GDPR-CL08` (Art. 6(1)(a)); `GDPR-CL15` (Art. 7(1)); `GDPR-CL16` (Art. 7(2)); `GDPR-CL17` (Art. 7(3)); `GDPR-CL18` (Art. 7(4)); `GDPR-CL19` (Art. 8(1) — age threshold); `GDPR-CL20` (Art. 8(2) — reasonable verification); `GDPR-CL22` (Art. 9(2)(a) — explicit consent for special categories); `GDPR-TR08` (Art. 49(1)(a) — explicit transfer consent) | D-09.1, D-03.1 |
| SO-GDPR-032 | D-09.1, D-03.1 | Art. 4(11), Art. 6(1)(a), Art. 7, Art. 8, Art. 9(2)(a), Art. 49(1)(a) | Consent lifecyle: specific, informed, demonstrable, withdrawable |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-054
  title: "Verified consent for child and transfer-risk contexts"
  source_clauses:
    - { clause_id: GDPR-CL19, article_ref: "Art. 8(1) — age threshold" }
    - { clause_id: GDPR-CL20, article_ref: "Art. 8(2) — reasonable verification efforts" }
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit transfer consent" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-OFFERING, PER-TRANSFER]
  regulatory_rationale: |
    Art. 8(1) sets a default age of 16 for consent in information-society services offered directly to a child, with Member States permitted to lower the threshold by law provided it is not below 13 (Recital 38); the threshold governs only consent and not the other Art. 6 lawfulness bases. Art. 8(2) requires the controller to make reasonable efforts to verify that parental responsibility is held in respect of any child below the threshold, taking into consideration available technology, which is a process obligation rather than an outcome guarantee. Art. 49(1)(a) requires, as a derogation for international transfers in the absence of adequacy and appropriate safeguards, that the data subject has explicitly consented to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and of appropriate safeguards (Recital 49). The three articles together form a single rule on consent validity for vulnerable contexts: child consent requires parental verification (Art. 8) and transfer consent requires informed risk acknowledgement (Art. 49(1)(a)), both layered on top of the Art. 4(11) baseline.
  security_rationale: |
    The obligation in Art. 8(1)–(2) and Art. 49(1)(a) is operationalised in NIST
    CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials based
    on the context of interactions)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    PR.AA-02 controls the identity-proofing step that Art. 8(2) requires: the
    controller must make reasonable efforts to verify that the consenting party
    holds parental responsibility for a child below the age threshold, and the
    available-technology standard operates as a rolling baseline that the
    proofing mechanism must track. The same subcategory controls the stronger
    transfer-risk-informed consent that Art. 49(1)(a) requires, layered on top of
    the Art. 4(11) baseline with explicit risk acknowledgement. GV.OC-03 captures
    the wider regulatory frame across Member-State age-threshold variations
    (which span 13 to 16) and across the transfer-restriction regime under which
    Art. 49(1)(a) sits as a narrow derogation rather than a general mechanism.

    Together the two subcategories embed age and transfer-risk verification in a
    documented identity-proofing process (PR.AA-02) within a managed
    regulatory-compliance frame (GV.OC-03), enabling the controller to
    demonstrate ex-post that the Art. 8 verification effort was reasonable in its
    technological context and that Art. 49(1)(a) consent was collected with
    informed risk acknowledgement.
  ambiguity_notes: |
    Art. 8(1) parental-responsibility carries POLY-S3 because Member State legal definitions diverge (some treat only biological parents as holders of parental responsibility, others include guardians and educational institutions). Art. 8(2) reasonable efforts carries VAG-S3 because the available-technology standard is a rolling benchmark and no supervisory authority has published a hard test. Art. 49(1)(a) explicitly consented carries POLY-S3 against the Art. 4(11) unambiguous standard and the Art. 9(2)(a) explicit standard. The rule preserves the EDPB Guidelines 05/2020 reading that the derogation consent must be explicit, specific to the transfer, and documented as risk-informed, so the controller cannot rely on the same consent artefact used for the underlying Art. 6(1)(a) basis. An alternative reading confines Art. 8(2) reasonable efforts to a one-time check at the moment of consent collection; this reading is rejected because EDPB Guidelines on Art. 8(2) treat the obligation as continuing for as long as the child uses the service. A second alternative reading treats the Art. 49(1)(a) explicit consent as a one-time event that survives subsequent changes in the destination regime; this reading is rejected because the risk-informed nature of the consent requires re-confirmation when the destination regime materially changes. Remain open: (a) whether reasonable efforts under Art. 8(2) includes reliance on the data subject's self-declaration of age or whether a positive verification step (credit-card verification, ID upload, knowledge-based authentication) is required; (b) whether Art. 49(1)(a) explicit consent can be combined with Art. 6(1)(a) consent in a single transaction or must be collected through a separate user journey that highlights the transfer-risk information.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-057
  title: "Derogation-based transfer fallback under strict preconditions"
  source_clauses:
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit consent" }
    - { clause_id: GDPR-TR09, article_ref: "Art. 49(1)(d) — important public interest" }
    - { clause_id: GDPR-TR10, article_ref: "Art. 49(1) second subparagraph — catch-all" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: UNMAPPED_CSF, title: "Derogation under Art. 49 is GDPR-specific with no clean CSF 2.0 mapping" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER, ONE_TIME]
  regulatory_rationale: |
    Art. 49 derogations apply only in the absence of an adequacy decision under Art. 45(3) and of appropriate safeguards under Art. 46, including binding corporate rules. Art. 49(1) lists seven disjunctive grounds: explicit consent after being informed of possible risks; necessity for the performance of a contract between the data subject and the controller or implementation of pre-contractual measures at the data subject's request; necessity for a contract concluded in the interest of the data subject between the controller and another natural or legal person; important reasons of public interest; establishment, exercise or defence of legal claims; protection of the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent; transfer from a register intended to provide information to the public (Recital 111–115). The second subparagraph of Art. 49(1) adds a catch-all: transfers may take place where the transfer is not repetitive, concerns a limited number of data subjects, is necessary for compelling legitimate interests of the controller which are not overridden by the interests, rights or freedoms of the data subject, and the controller has assessed all the circumstances and put in place suitable safeguards (Recital 113).
  security_rationale: |
    The obligation in Art. 49(1)(a), Art. 49(1)(d) and Art. 49(1) second
    subparagraph has no clean NIST CSF 2.0 subcategory and is anchored on the
    closest fit **GV.OC-03 (Legal, regulatory, and contractual requirements
    regarding cybersecurity — including privacy and civil liberties obligations —
    are understood and managed)** within the broader **GV.OC — Organizational
    Context** category; the residual gap is noted as UNMAPPED_CSF.

    GV.OC-03 controls the controller's understanding of the regulatory
    preconditions on which any Art. 49 derogation depends — absence of an
    adequacy decision under Art. 45(3), absence of Art. 46 appropriate
    safeguards, and satisfaction of one of the seven enumerated grounds or the
    catch-all (not repetitive, limited number of data subjects, compelling
    legitimate interests, suitable safeguards). CSF 2.0 does not enumerate
    derogation-availability analysis and GV.OC-03 is a poor fit because it is
    designed for ongoing regulatory understanding rather than exception-
    availability gating, but it is the closest available anchor.

    Because the CSF gap is documented, the controller must supplement GV.OC-03
    with a GDPR-specific derogation-use register that records each catch-all
    reliance, the compelling-interests analysis, and the suitable safeguards
    deployed. Accountability is sustained through the documented gap
    (UNMAPPED_CSF + unmapped_csf_justification) and through GV.OC-03's
    regulatory-understanding trail that demonstrates the derogation fallback was
    used only where adequacy and Art. 46 safeguards were unavailable.
  ambiguity_notes: |
    Explicitly (Art. 49(1)(a)) carries POLY-S3 against the specific qualifier of Art. 4(11) and the explicit qualifier of Art. 9(2)(a); reading chosen: the strongest consent form, risk-informed and documented, building on EDPB Guidelines 05/2020 §3.4 and the Schrems II framing of risk disclosure. The catch-all qualifiers not repetitive, limited number, compelling legitimate interests, suitable safeguards carry VAG-S3 and SCOPE-Q-S3 because none of them is quantitatively bounded in the OJ text; compelling in particular carries POLY-S3 across Art. 21(1) and Art. 49(1) (Recital 47 cross-reference), and the EDPB Guidelines 2/2018 emphasise that compelling means more than legitimate and approaches necessity. An alternative reading confines the catch-all to transfers that are truly exceptional and treats recurring or systematic reliance on it as a structural misuse of the derogation; this reading is consistent with that framing and operationally shifts the burden onto the controller to demonstrate the exceptional nature of each catch-all reliance. A second alternative reading treats not repetitive as a per-data-subject test rather than per-data-flow; this reading is harder to operationalise and is inconsistent with the structural purpose of the catch-all. Remain open: (a) whether repetitive in the catch-all should be measured per data subject, per transfer, or per data flow, given that no OJ anchor specifies the unit; (b) whether suitable safeguards in the catch-all may be purely contractual or must include technical measures (encryption, pseudonymisation) per Schrems II §134.
  unmapped_csf_justification: |
    The four Art. 49 catch-all conjunctive qualifiers and the
    `compelling legitimate interests` qualifier have no clean CSF 2.0
    Subcategory. The closest mapping GV.OC-03 is a poor fit.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-059
  title: "Third-country legal-request recognition filter via international agreements"
  source_clauses:
    - { clause_id: GDPR-TR07, article_ref: "Art. 48 — third-country legal-request filter" }
  linked_objectives: [SO-GDPR-035]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-REQUEST]
  regulatory_rationale: |
    Art. 48 provides that judgments or administrative decisions of third countries requiring a controller or processor to transfer or disclose personal data may only be recognised or enforced in any manner on the basis of an international agreement, such as a mutual legal assistance treaty (MLAT), in force between the requesting third country and the Union or a Member State, without prejudice to other grounds for transfer pursuant to Chapter V. The provision is the GDPR's response to the risk of extra-territorial legal-process demands that bypass the EU's cooperation regime, and it does not preclude transfers under the Chapter V mechanisms but rather adds a recognition-and-enforcement filter on the receiving-side process (Recital 6 on international cooperation). The scope of Art. 48 extends to any third-country administrative or judicial decision that compels transfer or disclosure, regardless of whether the decision names the controller or addresses it indirectly, so the controller cannot rely on a narrow reading that excludes indirect orders. The interplay with the U.S. CLOUD Act is the canonical operational example: an MLAT-based request from a U.S. authority is enforceable on Art. 48 grounds, while an extraterritorial CLOUD Act order directed at an EU-headquartered provider is not.
  security_rationale: |
    The obligation in Art. 48 is operationalised in NIST CSF 2.0 through
    **GV.OC-03 (Legal, regulatory, and contractual requirements regarding
    cybersecurity — including privacy and civil liberties obligations — are
    understood and managed)** and **GV.SC-03 (Contracts with suppliers and other
    third parties used to implement appropriate measures)**.

    GV.OC-03 controls the controller's understanding of the international-
    agreement filter that Art. 48 imposes: third-country judgments or
    administrative decisions compelling transfer or disclosure may be recognised
    or enforced only on the basis of a binding international agreement (such as a
    mutual legal assistance treaty) in force between the requesting third country
    and the Union or a Member State. GV.SC-03 controls the contractual
    articulation of this filter in processor agreements, requiring that any
    third-country legal request be escalated to the controller before disclosure
    and that the recognition-and-enforcement gate be documented in the
    data-processing agreement.

    Together the two subcategories embed extra-territorial legal-request
    resistance in a managed regulatory-understanding frame (GV.OC-03) backed by
    contractual escalation clauses (GV.SC-03), enabling ex-post demonstration to
    the supervisory authority that no third-country order was honoured without an
    international-agreement basis and that the refusal-and-escalation chain is
    auditable through a designated accountable owner.
  ambiguity_notes: |
    Such as a mutual legal assistance treaty carries POLY-S3 because the OJ text uses a non-exemplifying list and the term itself is undefined in GDPR. Reading chosen: the broad reading, in which any binding international agreement between the third country and the EU or a Member State qualifies, on the practical ground that the CLOUD Act conflict demonstrates that formal MLATs are too narrow a vehicle for the volume and velocity of contemporary cross-border legal-process traffic; EDPB Guidelines 5/2022 on the interplay with the CLOUD Act adopt a similar practical reading. An alternative reading limits the qualifier to formal MLATs and excludes unilateral instruments such as executive agreements or executive orders; this reading is rejected because it would render Art. 48 largely ineffective against the practical pattern it was meant to address. A second alternative reading treats Art. 48 as covering only the recognition and enforcement of foreign judgments, not the underlying transfer obligation; this reading is consistent with the text of Art. 48 but operationally creates a loophole where a transfer can occur in compliance with Chapter V while the third-country legal-process filter applies only to recognition of the resulting judgment. Remain open: (a) whether a transfer pursuant to a valid Chapter V mechanism (adequacy, Art. 46 safeguards, Art. 49 derogation) is itself the relevant compliance anchor even where the third-country request lacks an international-agreement basis, on the view that Art. 48 regulates recognition and enforcement of the request rather than the underlying transfer; (b) whether the controller must challenge the third-country legal request in the third-country courts before refusing disclosure, or whether refusal grounded in Art. 48 alone discharges the obligation.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

