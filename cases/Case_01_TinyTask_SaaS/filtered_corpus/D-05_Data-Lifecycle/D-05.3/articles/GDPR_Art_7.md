---
document_id: AEGIS-PREPROC-GDPR-ART-7
title: GDPR Art. 7 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 7
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# GDPR Art. 7

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-032 | Consent to personal-data processing is freely given, specific, informed, and unambiguous; the controller demonstrates the data subject's consent on request; withdrawal of consent is as easy as giving; bundled consent requests are presented in a clearly distinguishable form; conditional consent (bundled with contract) is presumed non-compliant unless processing is strictly necessary for contract performance; special-category consent is at the higher `explicit` standard; child consent (information-society services) is gated by Art. 8 age thresholds and parental-responsibility verification; transfer consent (Art. 49(1)(a)) is `explicit` and risk-informed. | `GDPR-C05` (Art. 4(11) — consent definition); `GDPR-CL08` (Art. 6(1)(a)); `GDPR-CL15` (Art. 7(1)); `GDPR-CL16` (Art. 7(2)); `GDPR-CL17` (Art. 7(3)); `GDPR-CL18` (Art. 7(4)); `GDPR-CL19` (Art. 8(1) — age threshold); `GDPR-CL20` (Art. 8(2) — reasonable verification); `GDPR-CL22` (Art. 9(2)(a) — explicit consent for special categories); `GDPR-TR08` (Art. 49(1)(a) — explicit transfer consent) | D-09.1, D-03.1 |
| SO-GDPR-032 | D-09.1, D-03.1 | Art. 4(11), Art. 6(1)(a), Art. 7, Art. 8, Art. 9(2)(a), Art. 49(1)(a) | Consent lifecyle: specific, informed, demonstrable, withdrawable |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-022
  title: "Downstream-recipient cascade for rectification and erasure"
  source_clauses:
    - { clause_id: GDPR-RT15, article_ref: "Art. 19 — cascade notification" }
    - { clause_id: GDPR-RT12, article_ref: "Art. 16 — rectification" }
    - { clause_id: GDPR-RT11, article_ref: "Art. 15(4) — third-party-rights limit" }
    - { clause_id: GDPR-CL26, article_ref: "Art. 11(2) — identification-exemption (cross)" }
  linked_objectives: [SO-GDPR-012]
  sub_domain: [D-04.3, D-05.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 19 requires the controller to communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Art. 16, Art. 17(1) or Art. 18 to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller must inform the data subject about those recipients if the data subject requests it. Art. 16 supplies the rectification mechanism, Art. 15(4) caps the disclosure obligation to recipients known to the controller, and Art. 11(2) preserves the identification precondition for the data-subject rights endpoint. Read together, the provisions establish a downstream-integrity obligation: when the controller corrects, erases, or restricts personal data, the correction must propagate to all known recipients or the controller must demonstrate that propagation is impossible or disproportionate, and the controller must be able to enumerate those recipients on request.
  security_rationale: |
    The obligation in Art. 19, read with Art. 16 and Art. 15(4), to cascade rectifications and erasures to every recipient of the personal data is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.DS-12 anchors the data-management foundation that the cascade requires: a recipient register mapping each processing activity to its known recipients, including processors and joint controllers, and a propagation procedure that issues the rectification or erasure event through that register, satisfying the Art. 19 downstream-integrity duty at the policy layer.
    RS.CO-02 captures the reporting dimension that gives the cascade operational force: routing each correction event to the internal stakeholders responsible for recipient notification, documenting the impossible-or-disproportionate justifications where propagation fails, and retaining the evidence needed to answer a data-subject recipient-list request under Art. 19.
    The two subcategories together operationalise the propagation chain that prevents the rectification right from becoming illusory across a distributed processing ecosystem.
    A controller documenting PR.DS-12 recipient register, RS.CO-02 propagation logs and the per-event justification evidence can demonstrate ex post, under Art. 5(2), that corrections reached every known recipient or that the documented exception genuinely applied.
  ambiguity_notes: |
    `impossible` OR `disproportionate effort` (Art. 19) carries COORD-S3. Reading chosen: either escape clause suffices, as a logical inclusive OR. An alternative reading requiring both to hold is rejected: the stricter reading would impose undue compliance burden without policy justification. The OJ text uses `or`, the English-language UN-style drafting convention for an inclusive disjunction; EDPB Guidelines treat this consistently. On the Art. 15(4) cap (third-party-rights limit), the disclosure to the data subject about recipients is bounded to recipients known to the controller; the controller is not required to investigate recipients beyond its own records. Remain open: (a) whether the `recipient` definition includes processors (under Art. 28) and joint controllers (under Art. 26) or only independent third-party controllers, pending EDPB Guidelines 5/2019 revision; and (b) how the recipient-list request interacts with confidentiality obligations (e.g. trade-secret-protected recipients), pending alignment with Charter Art. 7 and CJEU jurisprudence on commercial confidentiality.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-051
  title: "Demonstrable consent with equally accessible withdrawal path"
  source_clauses:
    - { clause_id: GDPR-C05, article_ref: "Art. 4(11) — consent definition" }
    - { clause_id: GDPR-CL08, article_ref: "Art. 6(1)(a) — consent as lawfulness base" }
    - { clause_id: GDPR-CL15, article_ref: "Art. 7(1) — demonstrability" }
    - { clause_id: GDPR-CL17, article_ref: "Art. 7(3) — withdrawal" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CONSENT-COLLECTION, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(11) defines consent as any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. Art. 6(1)(a) anchors that consent as one of six alternative lawfulness bases, meaning that any single processing operation relying on consent must satisfy the Art. 4(11) elements in full. Art. 7(1) shifts the evidentiary burden onto the controller, which must be able to demonstrate that the data subject has consented. Art. 7(3) then grants the data subject the right to withdraw consent at any time, requires withdrawal to be as easy as giving consent, requires the data subject to be informed of that right before giving consent, and obliges the controller to cease processing based on consent upon withdrawal without affecting the lawfulness of processing carried out before withdrawal (Recital 65).
  security_rationale: |
    The obligation in Art. 4(11), Art. 6(1)(a), Art. 7(1) and Art. 7(3) is
    operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and
    bound to credentials based on the context of interactions)** and **GV.OC-03
    (Legal, regulatory, and contractual requirements regarding cybersecurity —
    including privacy and civil liberties obligations — are understood and
    managed)**.

    PR.AA-02 controls the binding of the data subject's identity to the consent
    artefact: because the consent act functions as an authentication of intent,
    the controller must proof the identity of the consenting party and bind that
    proof to a credential-like consent record that is reproducible on demand.
    GV.OC-03 captures the broader legal-basis frame: the controller's
    organisation must understand and manage the conditions under which consent
    remains valid, the demonstrability threshold imposed by Art. 7(1), and the
    operational withdrawal mechanism that Art. 7(3) requires to be as accessible
    as the original consent collection.

    Together the two subcategories give the controller an auditable consent
    ledger (identity-bound artefacts under PR.AA-02) embedded in a managed
    regulatory-compliance process (under GV.OC-03), enabling ex-post
    demonstration to the supervisory authority that each Art. 4(11) qualifier was
    satisfied and that withdrawal was honoured without retroactive lawfulness
    collapse.
  ambiguity_notes: |
    The four Art. 4(11) qualifiers — freely given, specific, informed, unambiguous — are each open-textured and together carry the highest coordination risk because they are conjunctive, so failure of any one defeats the consent. Reading chosen: the four qualifiers must all be present simultaneously, as anchored by EDPB Guidelines 05/2020 §3.1 (consent must be a freely given, specific, informed and unambiguous indication, with each element assessed independently). An alternative reading limits the assessment to the absence of clear duress or deception, treating specific and unambiguous as formal rather than substantive qualifiers; this narrower reading is plausible for low-risk processing but is inconsistent with EDPB §3.1 and with CJEU Planet49 (C-673/17 §73), which held that pre-ticked boxes do not constitute unambiguous consent. A second alternative would treat specific as a granularity requirement separate from informed, requiring a separate consent per processing purpose even where the data subject is fully informed of all purposes, which is consistent with EDPB §3.4 but operationally costly and not always demanded by supervisory authorities in practice. Remain open: (a) whether the four qualifiers admit a sliding-scale intensity test proportionate to the sensitivity of the data and the purpose, or whether each must always be satisfied at uniform intensity; (b) whether Art. 7(3) as easy as giving consent applies only to the withdrawal mechanism proper, or extends to the procedural difficulty of locating that mechanism within the wider user interface.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-052
  title: "Unbundled and non-conditional consent collection"
  source_clauses:
    - { clause_id: GDPR-CL16, article_ref: "Art. 7(2) — bundled consent" }
    - { clause_id: GDPR-CL18, article_ref: "Art. 7(4) — conditional consent" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CONSENT-COLLECTION]
  regulatory_rationale: |
    Art. 7(2) requires that, if the data subject's consent is given in the context of a written declaration which also concerns other matters, the request for consent shall be presented in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language. Recital 32 reinforces this by requiring the request to be unambiguous. Art. 7(4) then states that when assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is not necessary for the performance of that contract (Recital 43). The two articles together form the unbundling rule: separate consent UI for separate processing purposes, and no conditioning of contract performance on consent for unrelated processing. Recital 43 anchors the practical effect by clarifying that consent should not provide a blanket gateway to all processing the controller may wish to perform.
  security_rationale: |
    The obligation in Art. 7(2) and Art. 7(4) is operationalised in NIST CSF 2.0
    through **GV.PO-02 (Cybersecurity processes and procedures established,
    communicated, and enforced)** and **PR.AA-02 (Identities proofed and bound to
    credentials based on the context of interactions)**.

    GV.PO-02 controls the documented consent-flow process: the controller must
    establish and enforce a written consent-collection procedure that physically
    or logically separates each purpose's consent UI, uses plain-language
    labelling, and prohibits the conditioning of contract performance on consent
    for processing that is not strictly necessary to the contract. The CJEU
    Bundeskartellamt line (C-252/21) and Planet49 (C-673/17) confirm that this
    process discipline is the principal defence against consent-coercion
    patterns. PR.AA-02 captures each consent act as an authentication of intent,
    with the consent artefact treated like a credential whose issuance is
    purpose-scoped and whose withdrawal path mirrors the issuance path in
    accessibility.

    Together the two subcategories translate the Art. 7 unbundling rule into a
    documented, enforced process (GV.PO-02) backed by identity-bound consent
    records (PR.AA-02), enabling the controller to demonstrate ex-post at
    supervisory-authority review that no consent was coerced, bundled, or
    improperly conditioned.
  ambiguity_notes: |
    Clearly distinguishable, intelligible and easily accessible, and clear and plain language carry VAG-S3 because none of them specifies an objective threshold that an auditor or supervisory authority could apply uniformly. Reading chosen: a visible, separate consent UI per purpose, with no pre-ticked boxes and layered notices following EDPB Guidelines 05/2020 §3.6, which treats physical separation of consent from other matters as a condition for the consent to be clearly distinguishable. The Art. 7(4) reading chosen: bundling per se is non-compliant unless the unrelated processing is strictly necessary for the contract, per the CJEU Bundeskartellamt ruling (C-252/21), which treated Facebook's combined-terms consent as coercive. An alternative reading would permit softer bundling where the data subject can in practice decline without losing access to the core service, on the rationale that effective choice rather than physical separation is the substance of the requirement; this conditional-permissibility reading is inconsistent with the Bundeskartellamt precedent but has been raised in national-court proceedings and remains litigated. A second alternative would treat the requirement as satisfied by any technically distinguishable mechanism, including a default-accept button paired with an opt-out link, which is rejected by supervisory practice because default-accept configurations cannot satisfy the freely-given qualifier of Art. 4(11). Remain open: (a) whether Art. 7(2) requires physical separation (separate button or checkbox on the same screen) or merely logical separation (same screen, clearly labelled section) when consent is collected in a multi-purpose form; (b) whether a single consent artefact that bundles consent for a core service with consent for an ancillary feature (analytics, personalisation) is per se non-compliant under Art. 7(4) when the ancillary feature is genuinely optional and not technically integrated with the core.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

