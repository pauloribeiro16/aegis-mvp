---
document_id: AEGIS-PREPROC-CRA-ART-8
title: CRA Art. 8 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 8
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# CRA Art. 8

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-052 | A product with digital elements is presumed to be in conformity with the essential cybersecurity requirements set out in Annex I where the product and the manufacturer's processes conform to harmonised standards, common specifications, or European cybersecurity certification schemes adopted pursuant to Regulation (EU) 2019/881 at the assurance level specified by Art. 8(1) or Art. 32(2)/(3). | `CRA-CL108` (Art. 27(1) — presumption of conformity (harmonised standards)); `CRA-CL109` (Art. 27(2) — common specifications); `CRA-CL110` (Art. 27(5) — common-specs presumption); `CRA-CL111` (Art. 27(8) — CSA-certification presumption); `CRA-CL112` (Art. 27(9) — delegated acts specifying CSA schemes) | D-09.1 |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-078
  title: "CSA certification presumption at substantial assurance level"
  source_clauses:
    - { clause_id: CRA-CL111, article_ref: "Art. 27(8) — CSA-certification presumption" }
    - { clause_id: CRA-CL112, article_ref: "Art. 27(9) — delegated acts specifying CSA schemes" }
    - { clause_id: CRA-CL10, article_ref: "Art. 8(1) — assurance level at least `substantial`" }
  linked_objectives: [SO-CRA-052]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 27(8) presumes that a product with digital elements and the
    manufacturer's processes for which the manufacturer has obtained an EU
    statement of conformity or an EU certificate under a European
    cybersecurity certification scheme adopted pursuant to Regulation (EU)
    2019/881 — at assurance level at least "substantial" — are in
    conformity with the Annex I cybersecurity requirements, to the extent
    that the certification covers those requirements [Recital 53]. Article
    27(9) authorises the Commission to adopt delegated acts specifying which
    CSA schemes and which product categories are eligible to demonstrate
    Annex I conformity through this route. Article 8(1) sets the assurance-
    level floor for critical-product certification at "at least substantial".
  security_rationale: |
    The Art. 27(8) certification-presumption is operationalised in NIST CSF
    2.0 through GV.OC-03 and GV.SC-04. GV.OC-03 anchors the manufacturer's
    duty to identify which CSA scheme, which assurance level (at least
    "substantial" per Art. 8(1)), and which Annex I requirements are
    actually covered by the issued certificate, and to keep that mapping
    current against the Commission's Art. 27(9) delegated acts. GV.SC-04
    (Suppliers and other third parties are routinely assessed using audits,
    test results, or other forms of evaluation to confirm they are meeting
    their contractual obligations) extends the third-party-assessment
    posture to the certification body itself, treating the CSA certificate
    as ongoing auditable evidence rather than a one-time artefact. Together,
    GV.OC-03 and GV.SC-04 let the manufacturer document ex post that the
    Art. 27(8) presumption covers each Annex I requirement it claims
    coverage for, and that the certificate is renewed within the scheme's
    surveillance window.
  ambiguity_notes: |
    The qualifier "at least substantial" is a floor that higher assurance
    levels (e.g. "high") satisfy automatically, but the practical
    availability of CSA schemes that cover CRA critical-product categories
    is the hard constraint. As of mid-2025, no CSA scheme has been adopted
    under Article 27(9) that covers the Annex IV critical-product
    catalogue, so the certification-presumption path is effectively dormant
    for critical products. The text directs such products to the Article
    32(4) fallback — the substantial-level certificate of Regulation (EU)
    2019/881 or, in its absence, the Article 32(3) third-party route of
    Module B+C, H, or certification. The open operational question is
    whether ENISA will deliver a critical-product CSA scheme aligned with
    Regulation (EU) 2019/881 before the Commission's delegated acts under
    Article 27(9) materially shape the certification landscape.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-098
  title: "Critical-product certification and FOSS simplified assessment"
  source_clauses:
    - { clause_id: CRA-CL126, article_ref: "Art. 32(4) — critical products: certification or B+C/H fallback" }
    - { clause_id: CRA-CL127, article_ref: "Art. 32(5) — FOSS simplified CA (Module A when tech docs are public)" }
  linked_objectives: [SO-CRA-066]
  sub_domain: [D-09.4, D-10.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 32(4) routes critical products (Annex IV) to European
    cybersecurity certification under Article 8(1) — at assurance level
    at least "substantial", and to higher levels where so determined by
    delegated act — or, where the relevant delegated acts have not been
    adopted, to the Article 32(3) fallback (Module B+C, Module H, or
    substantial-level certification). Article 32(5) separately provides a
    simplified conformity-assessment route for free and open-source
    software products in Annex III categories: the manufacturer may use
    Module A, provided the Annex VII technical documentation is made
    available to the public at the time of placing on the market.
  security_rationale: |
    The Art. 32(4)/(5) critical-product and FOSS-simplified routes are
    operationalised in NIST CSF 2.0 through GV.OC-03. GV.OC-03
    (Legal, regulatory, and contractual requirements regarding
    cybersecurity are understood and managed) anchors the
    highest-class procedure selection — the manufacturer identifies
    Annex IV critical products, evaluates the availability of
    Art. 8(1) certification at substantial or higher, and falls back
    to the Art. 32(3) routes when the relevant delegated acts are
    not yet adopted. GV.OC-03 also anchors the FOSS-simplified path:
    the manufacturer documents the public-availability of the Annex VII
    technical documentation and applies Module A. The single-Subcategory
    mapping reflects that both routes are procedure-selection controls,
    not new technical surfaces. GV.OC-03 lets the manufacturer
    demonstrate ex post that the correct high-class or FOSS-simplified
    procedure was chosen.
  ambiguity_notes: |
    "Made available to the public" reads as any form of public access —
    a project website, a code repository, a standards-trust
    publication — rather than MSA-on-request. The threshold is whether
    the documentation is reachable without a privileged channel at the
    time the product is placed on the market.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

