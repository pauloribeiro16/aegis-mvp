---
document_id: AEGIS-PREPROC-CRA-ART-30
title: CRA Art. 30 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 30
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

# CRA Art. 30

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-058 | The manufacturer draws up, before placing a product with digital elements on the market, the technical documentation referred to in Art. 31; carries out (or has carried out) the chosen conformity assessment procedure referred to in Art. 32; and — where compliance with the applicable cybersecurity requirements has been demonstrated — draws up the EU declaration of conformity in accordance with Art. 28 and affixes the CE marking in accordance with Art. 30. | `CRA-CL36` (Art. 13(12) sentence 1 — tech docs + conformity assessment before placing); `CRA-CL37` (Art. 13(12) sentence 2 — EU declaration + CE marking); `CRA-CL120` (Art. 31(1) — tech docs contain Annex I compliance evidence); `CRA-CL121` (Art. 31(2) — tech docs drawn up before placing and updated during support); `CRA-CL113` (Art. 28(1) — EU declaration content); `CRA-CL114` (Art. 28(2) — declaration format per Annex V/VI); `CRA-CL116` (Art. 28(4) — manufacturer's responsibility); `CRA-CL117` (Art. 30(1) — CE marking affixing); `CRA-CL118` (Art. 30(3) — CE marking before placing) | D-09.4 |
| SO-CRA-058 | D-09.4 | Art. 13(12) + Art. 31(1)/(2) + Art. 28(1)/(2)/(4) + Art. 30(1)/(3) | Pre-market technical documentation + EU declaration + CE marking |
| SO-CRA-067 | The Commission may adopt implementing acts specifying the format and elements of the software bill of materials referred to in Annex I Part II (1); ADCO may conduct a Union-wide dependency assessment on the Union's dependence on software components (in particular FOSS components) for specific categories of products with digital elements. | `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL50` (Art. 13(25) — Union-wide dependency assessment by ADCO); `CRA-CL67` (Art. 14(9) — delegated acts on delay-dissemination grounds); `CRA-CL68` (Art. 14(10) — implementing acts on notification format/procedures); `CRA-CL8` (Art. 7(3) — delegated acts amending Annex III); `CRA-CL9` (Art. 7(4) — implementing acts specifying technical descriptions); `CRA-CL119` (Art. 30(6) — implementing acts on labels/pictograms) | D-09.4 |
| SO-CRA-067 | D-09.4 | Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6) | Commission implementing / delegated acts (SBOM, delay grounds, labels, technical descriptions) |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-086
  title: "CE marking affixed and EU declaration accompanies product"
  source_clauses:
    - { clause_id: CRA-CL117, article_ref: "Art. 30(1) — CE marking affixing" }
    - { clause_id: CRA-CL118, article_ref: "Art. 30(3) — CE marking before placing on market" }
    - { clause_id: CRA-CL119, article_ref: "Art. 30(6) — implementing acts for labels/pictograms" }
    - { clause_id: CRA-CL45, article_ref: "Art. 13(20) — full or simplified EU declaration with product" }
  linked_objectives: [SO-CRA-058, SO-CRA-062]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 30(1) requires the CE marking to be affixed visibly, legibly,
    and indelibly to the product and its packaging; for software products
    and products supplied without packaging, the marking may be placed on
    the EU declaration or on a website accessible with the product.
    Article 30(3) requires the CE marking to be affixed before the product
    is placed on the market. Article 30(6) authorises the Commission to
    adopt implementing acts on labels and pictograms related to the
    security of products with digital elements. Article 13(20) requires
    the manufacturer to provide the EU declaration — full or simplified —
    with the product [Recital 47, Recital 49].
  security_rationale: |
    The Art. 30(1)/(3)/(6)/(13)(20) CE marking and EU-declaration
    accompaniment is operationalised in NIST CSF 2.0 through GV.OC-03.
    GV.OC-03 (Legal, regulatory, and contractual requirements regarding
    cybersecurity are understood and managed) anchors the manufacturer's
    standing duty to know the current CE-marking format requirements —
    visible/legible/indelible for physical products, declaration-or-
    website for software — and to keep the EU declaration accessible
    for the Art. 13(13) retention window. The single-Subcategory mapping
    reflects that the obligation is essentially a regulatory-evidence
    delivery duty, not a new control surface. GV.OC-03 gives the
    manufacturer a managed-requirements framework that can demonstrate
    ex post that the marking was affixed before the first placement and
    that the declaration remained available throughout the support
    period.
  ambiguity_notes: |
    "Visibly, legibly, indelibly" is a conjunctive stack: all three must
    hold for the affixed marking. "Simplified EU declaration" refers to
    the Annex VI template format — the same compliance claim, expressed
    in a short form intended for products where the full Annex V
    declaration would be disproportionate.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-099
  title: "Commission implementing and delegated acts operationalisation"
  source_clauses:
    - { clause_id: CRA-CL49, article_ref: "Art. 13(24) — SBOM implementing acts" }
    - { clause_id: CRA-CL67, article_ref: "Art. 14(9) — delegated acts on delay grounds" }
    - { clause_id: CRA-CL68, article_ref: "Art. 14(10) — implementing acts on notification format/procedures" }
    - { clause_id: CRA-CL8, article_ref: "Art. 7(3) — delegated acts amending Annex III" }
    - { clause_id: CRA-CL9, article_ref: "Art. 7(4) — implementing acts on technical descriptions" }
    - { clause_id: CRA-CL119, article_ref: "Art. 30(6) — implementing acts on labels/pictograms" }
    - { clause_id: CRA-CL50, article_ref: "Art. 13(25) — Union-wide dependency assessment by ADCO" }
  linked_objectives: [SO-CRA-067, SO-CRA-070]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(24), 13(25), 14(9), 14(10), 7(3), 7(4), and 30(6)
    collectively establish the Commission and ADCO implementing and
    delegated acts machinery that operationalises, refines, and
    supplements the body of the Regulation. Article 13(24) authorises
    implementing acts on the SBOM format and elements; Article 13(25)
    authorises ADCO to conduct a Union-wide dependency assessment on
    the dependence of Member States and the Union on software
    components, in particular on free and open-source software
    components [Recital 25]; Article 14(9) authorises delegated acts on
    cybersecurity-related grounds for delaying notification
    dissemination; Article 14(10) authorises implementing acts on
    notification format and procedures; Article 7(3) authorises
    delegated acts amending Annex III; Article 7(4) authorises
    implementing acts specifying the technical descriptions of Annex III
    and Annex IV product categories; Article 30(6) authorises
    implementing acts on labels and pictograms related to security.
  security_rationale: |
    The Art. 7(3)/(4), 13(24)/(25), 14(9)/(10), 30(6) Commission and ADCO
    acts machinery is operationalised in NIST CSF 2.0 through GV.PO-02
    and GV.OV-01. GV.PO-02 (Cybersecurity processes and procedures for
    implementing the cybersecurity policy are established, communicated,
    and enforced) anchors the process discipline of tracking Commission
    publication cadence and folding each act into the SDLC and
    documentation package as it is adopted. GV.OV-01 (Cybersecurity risk
    management strategy outcomes are reviewed and adjusted to ensure
    they adequately address organizational risks) anchors the
    review-and-adjust loop triggered by each new act. Together, GV.PO-02
    and GV.OV-01 give the manufacturer a tracking-and-incorporation
    control set that can demonstrate ex post that the body of
    implementing and delegated acts in force at the time of placing was
    correctly reflected in the technical documentation and conformity
    posture.
  ambiguity_notes: |
    The implementing acts referenced by Articles 7(4), 13(24), and 14(9)
    — together with the Art. 7(4) technical descriptions and the Art.
    14(9) delegated acts on delay grounds — are scheduled for adoption by
    11 December 2025. As of mid-2025, several of these acts remain
    unpublished. The standing compliance duty attaches once the acts are
    published; manufacturers that have discharged their pre-July
    obligations on the basis of draft technical descriptions should
    re-verify against the adopted text within a reasonable window after
    publication.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

