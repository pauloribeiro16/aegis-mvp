---
document_id: AEGIS-PREPROC-GDPR-ART-20
title: GDPR Art. 20 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 20
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md
status: DRAFT
---

# GDPR Art. 20

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-020 | Where processing is based on consent (Art. 6(1)(a)) or on a contract (Art. 6(1)(b)) and carried out by automated means, the data subject receives the personal data concerning him or her in a structured, commonly used, machine-readable format and can transmit those data to another controller. | `GDPR-RT10` (Art. 15(3) — copy); `GDPR-CP09` (Art. 28(3)(g) — return/deletion); informed by Art. 20 (cross-chapter inheritance) | D-05.4 |
| SO-GDPR-020 | D-05.4 | Art. 20, Art. 15(3) | Portable data in commonly used machine-readable form |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-032
  title: "Structured electronic access copy in commonly used format"
  source_clauses:
    - { clause_id: GDPR-RT09, article_ref: "Art. 15(1)/(3) — copy provision and format" }
    - { clause_id: GDPR-RT10, article_ref: "Art. 15(3) — commonly used electronic form" }
  linked_objectives: [SO-GDPR-020]
  sub_domain: [D-05.4]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 15(1) grants the data subject the right to obtain from the
    controller confirmation as to whether personal data concerning them
    is being processed and access to that data. Art. 15(3) requires the
    controller to provide a copy of the personal data undergoing
    processing and, where the request is by electronic means, to provide
    the information in a commonly used electronic form unless the data
    subject requests otherwise. The controller may charge a reasonable
    fee based on administrative costs for any further copies. The
    provision is the data-subject-facing access right; the Art. 20
    portability right is distinct and broader in scope.
  security_rationale: |
    The obligation in Art. 15(1) and Art. 15(3) to deliver a copy of personal data undergoing processing in a commonly used electronic form, on request and without undue delay, is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.DS-10 captures the runtime integrity posture: any export pipeline must be able to read live data under controlled exposure so that the copy delivered reflects current processing truth rather than stale snapshot drift, with proper handling for partial-views derived from the same in-use data set.
    PR.DS-12 captures the data-management posture: the export pipeline is governed by the same risk strategy as the data it is exposing, with structured, commonly used formats (JSON, CSV, XML) layered into the data-handling substrate rather than treated as ad-hoc report outputs, ensuring the copy is machine-readable and downstream-tool-friendly without sacrificing security classification discipline.
    A controller that documents PR.DS-10 in-use export controls and PR.DS-12 format-selection policy can demonstrate ex post, against the Art. 5(2) accountability duty, that any Art. 15(3) export request was honoured at the data-handling quality and at the format-quality the provision requires on the day of any data-subject complaint or supervisory inspection.
  ambiguity_notes: |
    `commonly used electronic form` carries Berry-flagged VAG-S3 on
    format open-texture. The reading adopted for this SR is the
    structured-interoperable reading: JSON, CSV or XML, in line with
    EDPB Guidelines 06/2020 on data portability (which interpret the
    parallel Art. 20 phrase). The structured-interoperable reading is
    preferred over a PDF-style free-text rendering because it preserves
    machine-readability and aligns with the practical purpose of
    cross-provider migration. Two alternative readings remain. First, a
    print-ready rendering (PDF or scanned image) of the data would
    satisfy the literal text but defeat the purpose of the access right
    and the EDPB guidance. Second, a controller-preferred proprietary
    format that the data subject cannot easily open would technically
    comply but functionally obstruct; EDPB Guidelines 06/2020 reject
    this. Remain open: (a) whether open formats like Parquet or NDJSON
    count as `commonly used` for non-technical data subjects; (b) whether
    the obligation extends to inferred data (scores, profiles) or only to
    data the data subject explicitly provided.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

