---
document_id: AEGIS-PREPROC-CRA-ART-28
title: CRA Art. 28 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 28
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 28

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-058 | The manufacturer draws up, before placing a product with digital elements on the market, the technical documentation referred to in Art. 31; carries out (or has carried out) the chosen conformity assessment procedure referred to in Art. 32; and — where compliance with the applicable cybersecurity requirements has been demonstrated — draws up the EU declaration of conformity in accordance with Art. 28 and affixes the CE marking in accordance with Art. 30. | `CRA-CL36` (Art. 13(12) sentence 1 — tech docs + conformity assessment before placing); `CRA-CL37` (Art. 13(12) sentence 2 — EU declaration + CE marking); `CRA-CL120` (Art. 31(1) — tech docs contain Annex I compliance evidence); `CRA-CL121` (Art. 31(2) — tech docs drawn up before placing and updated during support); `CRA-CL113` (Art. 28(1) — EU declaration content); `CRA-CL114` (Art. 28(2) — declaration format per Annex V/VI); `CRA-CL116` (Art. 28(4) — manufacturer's responsibility); `CRA-CL117` (Art. 30(1) — CE marking affixing); `CRA-CL118` (Art. 30(3) — CE marking before placing) | D-09.4 |
| SO-CRA-058 | D-09.4 | Art. 13(12) + Art. 31(1)/(2) + Art. 28(1)/(2)/(4) + Art. 30(1)/(3) | Pre-market technical documentation + EU declaration + CE marking |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-085
  title: "Pre-market documentation, declaration, and CE marking chain"
  source_clauses:
    - { clause_id: CRA-CL36, article_ref: "Art. 13(12) sentence 1 — technical documentation + conformity assessment before placing" }
    - { clause_id: CRA-CL37, article_ref: "Art. 13(12) sentence 2 — EU declaration + CE marking" }
    - { clause_id: CRA-CL113, article_ref: "Art. 28(1) — EU declaration content" }
    - { clause_id: CRA-CL114, article_ref: "Art. 28(2) — declaration format per Annex V/VI" }
    - { clause_id: CRA-CL116, article_ref: "Art. 28(4) — manufacturer responsibility" }
  linked_objectives: [SO-CRA-058, SO-CRA-063]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(12) sentence 1 requires the manufacturer — before placing
    the product on the market — to draw up the technical documentation
    referred to in Article 31, carry out (or have carried out) the
    conformity-assessment procedure referred to in Article 32, and, where
    compliance has been demonstrated, draw up the EU declaration of
    conformity in accordance with Article 28 and affix the CE marking in
    accordance with Article 30. Article 28(1) sets the declaration content
    (statement of Annex I fulfilment). Article 28(2) sets the format:
    Annex V model for the full declaration, Annex VI template for the
    simplified form. Article 28(4) attributes sole responsibility for the
    compliance claim to the entity that drew up the declaration.
  security_rationale: |
    The Art. 13(12)/(28) pre-market chain is operationalised in NIST CSF
    2.0 through GV.PO-02 and GV.OC-03. GV.PO-02 anchors the procedural
    discipline of executing the four sequential gates (technical
    documentation, conformity assessment, EU declaration, CE marking) in
    the correct order, with a process artefact produced at each gate.
    GV.OC-03 anchors the legal-claim content of the EU declaration — the
    Annex I fulfilment statement and the Annex V/VI format selection —
    as a managed regulatory requirement. Together, GV.PO-02 and GV.OC-03
    give the manufacturer a single, end-to-end control set that the SDLC
    can be audited against, and that the manufacturer can demonstrate
    ex post cleared every gate before the first placement, with no gate
    compressed or skipped.
  ambiguity_notes: |
    "Before placing on the market" is a temporal anchor: every gate must
    be cleared before the first placement, not after the fact. Article
    28(4) — "the manufacturer assumes responsibility for the compliance
    of the product with digital elements" by virtue of drawing up the
    declaration — reads literally as the entity that signed the
    declaration bears the obligation; if a third party draws up the
    declaration on the manufacturer's behalf without becoming a
    manufacturer under Articles 21–22, the underlying responsibility
    chain remains with the manufacturer [Art. 13(12) literal].
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

