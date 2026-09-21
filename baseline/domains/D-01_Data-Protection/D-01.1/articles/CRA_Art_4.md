---
document_id: AEGIS-PREPROC-CRA-ART-4
title: CRA Art. 4 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 4
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
status: DRAFT
---

# CRA Art. 4

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-002
  title: "Confidentiality of stored data via state-of-the-art encryption"
  source_clauses:
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — at-rest encryption" }
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
  linked_objectives: [SO-CRA-002, SO-CRA-001]
  sub_domain: [D-01.1]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(e) requires that the confidentiality of stored data — personal or other — be protected by encrypting relevant data at rest using state-of-the-art mechanisms, illustrated together with the residual "or by using other technical means"; the data-scope qualifier "personal or other" ties back to the Art. 3(47) definition, which imports the GDPR Art. 4(1) notion of personal data and so extends the obligation to any non-personal data stored alongside. The Annex I Part I (1) chapeau fixes the baseline as an appropriate level of cybersecurity based on the risks, which sets the proportionality lever for choosing encryption coverage (which fields, what granularity, what key model). In practice the manufacturer documents a per-storage-class mapping — which logical stores hold which data categories, which cipher suites apply, and which keys protect which classes — in the technical documentation under Annex VII §2 and Annex VII §3.
    [OJ-corrective note (v0.2 audit, traceability): the OJ text reads verbatim — Definitions live in Article 3 of Regulation (EU) 2024/2847 (CRA). Annex II of CRA contains the information and instructions to the user (a documentary-scope annex), not definitions. Personal data is defined by Art. 3(47) (with the cross-reference to GDPR Art. 4(1)) — there is no `Annex II definitions` anchor.]
  security_rationale: |
    The at-rest branch of the Annex I Part I (2)(e) obligation is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)**. PR.DS-01 captures the structural defence against the persistent-attack-target pattern: backups, snapshots, lost disks, cloud-bucket misconfiguration -- all of which remain unreadable without the corresponding key, transforming a storage-layer bypass (insider with read access, stolen laptop, misconfigured access policy) into a ciphertext-only exposure rather than a plaintext disclosure. The encryption-at-rest control also functions as the upstream mitigation against the modern exfiltration-then-encrypt ransomware pattern, because ransomware that exfiltrates plaintext before encrypting depends directly on plaintext-at-rest exposures. PR.DS-01 feeds upward into the broader PR.DS family (integrity under PR.DS-10, access-control under PR.AA-05), and together with the manufacturer's documented per-storage-class mapping -- cipher suite, key custodian, granularity decisions -- it enables the manufacturer to demonstrate ex post, in the conformity dossier under Annex VII sections 2/3 and the Annex I Part I (1) risk assessment under Art. 13(2), that the chosen at-rest cryptographic mechanisms satisfy the state-of-the-art baseline across the support period under Art. 13(8).
  ambiguity_notes: |
    The phrase relevant data in the literal Annex I Part I (2)(e) text — "encrypting relevant data at rest or in transit" — is POLY-S2 because "relevant to what?" admits at least two materially distinct populations. Reading chosen: R2, where "relevant" means data tied to the product's intended purpose plus any data classified by the manufacturer as in-scope under the cybersecurity risk assessment conducted under Art. 13(2). Alternative reading: R1 would limit relevance strictly to data declared in the intended-purpose statement, leaving residual classes (telemetry, logs, derived metadata) outside the obligation and creating an enforcement gap. The state-of-the-art S3 ambiguity on the encryption primitive itself is carried by the umbrella SR-CRA-001 and not duplicated here.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

