---
document_id: AEGIS-PREPROC-NIS2-ART-14
title: NIS2 Art. 14 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 14
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
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---

# NIS2 Art. 14

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-001
  title: "Documented cryptography and encryption governance baseline"
  source_clauses:
    - { clause_id: NIS2-CL17, article_ref: "Art. 21(2)(h) — cryptography and, where appropriate, encryption" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art + standards + cost" }
    - { clause_id: NIS2-D01, article_ref: "Art. 6(1) — network and information system (cross)" }
    - { clause_id: NIS2-D02, article_ref: "Art. 6(2) — security of network and information systems" }
  linked_objectives: [SO-NIS2-001]
  sub_domain: [D-01.1]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption. The opening qualifier of Article 21(1) — that the technical, operational and organisational measures taken must be appropriate and proportionate to the risks posed — propagates to this sub-point, and Article 21(1) sentence 2 anchors the baseline against the state of the art, relevant European and international standards, and the cost of implementation (OJ L 333, 27.12.2022, p. 127). The four CIA-A dimensions of Article 6(2) — availability, authenticity, integrity and confidentiality of stored, transmitted or processed data — define what cryptography is to protect. Article 6(1) provides the operational scope by defining network and information systems through three coordinated sub-clauses (electronic communications networks; interconnected devices; digital data stored, processed, retrieved or transmitted). The Directive deliberately fuses cryptography as a discipline (algorithm selection, key management, protocol design) with encryption as a sub-technique applied where the risk assessment demands it, and leaves the application thresholds to the entity under the appropriate-and-proportionate qualifier (Recital 56). For the software-compliance track this means a documented cryptography policy that maps algorithms to data classifications and references the European standards landscape (ETSI TS 103 744 series on quantum-safe migration, ISO/IEC 27001:2022 Annex A.10 Cryptographic controls).
  security_rationale: |
    The obligation in Article 21(2)(h) of Directive (EU) 2022/2555 to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)**, **PR.DS-02 (Data-in-transit protected)** and **GV.RM-04 (Strategic direction on identifying and responding to risks established and communicated)**. PR.DS-01 anchors the cryptographic protection of stored data — algorithm selection, key-management lifecycle (generation, distribution, storage, rotation, revocation, destruction), and decommissioning of deprecated primitives on a known schedule. PR.DS-02 extends the same discipline to data in motion, translating cryptographic policy into mutually-authenticated transport between services, between entity and recipient, and between the entity and the supervisory authority during incident reporting. GV.RM-04 supplies the governance superstructure that converts ad-hoc algorithm choice into a position the entity can defend at audit. Together the three subcategories generate the policy artefacts, key-management records and review-cadence evidence that the Article 21(1) risk-management framework requires an entity to assemble to demonstrate, ex post, that its cryptographic posture is appropriate, proportionate and state-of-the-art.
  ambiguity_notes: |
    Article 21(2)(h) carries two compounding S3 ambiguities that drive materially different compliance obligations. First, the `cryptography and, where appropriate, encryption` conjunction is a hierarchical AND-with-hedge: cryptography is always required (a policy must address cryptographic mechanisms as a discipline) but encryption is additionally required only where the entity's risk assessment indicates it; the alternative reading that cryptography and encryption are synonyms is rejected by the literal text and by the CRA parallel (CRA Art. 13(2) on default passwords, Art. 14(2) on vulnerability remediation, treat cryptography and encryption as distinct concepts). Second, `state of the art` in Article 21(1) sentence 2 admits three readings — current best practice (qualitative), published standards (e.g. ISO/IEC 27001:2022, NIST CSF 2.0), or cutting-edge frontier research — of which the third is rejected by Recital 56 (cost of implementation implies off-the-shelf); the chosen reading accepts both R1 best practice and R2 published standards as operative, with ENISA's 2022 baseline guidance as the practical floor. Member State transposition divergence may apply on `state of the art`: the German BSI standardises the term through BSI TR-02102; French ANSSI requires an independent assessment by a qualified body; Italian ACN publishes annual guidance. The substantive software-compliance consequence is that a 5-FTE SaaS entity and a 500-FTE operator may both satisfy Article 21(2)(h) with materially different documentation depth, provided each documents the proportionality decision. Remain open: (a) whether the European Commission implementing acts under Article 21(5) will specify a baseline cryptography standard or only methodological requirements (the 17 October 2024 deadline has slipped to mid-2025 without publication as of the current reference date); (b) whether Member State national transposition will impose sector-specific cryptography mandates beyond the Directive... (line truncated to 2000 chars)
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-027
  title: "Secure-by-design controls integrated across NIS development"
  source_clauses:
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in development" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-017]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-DEVELOPMENT]
  regulatory_rationale: |
    Article 21(2)(e) second clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding security in the development of network and information systems. The development phase is the second of three coordinated lifecycle phases in Article 21(2)(e), and applies whether development is performed in-house by the entity or outsourced to a third-party developer under the entity's responsibility. The Article 21(1) appropriate-and-proportionate qualifier governs both the depth of the development controls and the scope of in-house versus outsourced coverage.
  security_rationale: |
    The obligation in Art. 21(2)(e) second clause to take measures regarding security in the development of network and information systems is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated and monitored throughout the SDLC)** and **PR.PS-02 (Software is maintained, replaced, and removed commensurate with risk)**. PR.PS-06 anchors the design-time control set: threat modelling, secure-by-design choices, secure coding standards, code review, and security testing all operate before deployment and so before any operational control can compensate for design weaknesses. PR.PS-02 anchors the lifecycle consequence: development-time decisions about component selection, dependency hygiene and update channels determine what the entity must later maintain, replace or remove. Together, PR.PS-06 and PR.PS-02 connect the design-time control set to the maintenance-time residual-risk profile. The control set enables ex-post demonstration that development-time decisions were risk-informed and that the resulting maintenance burden was deliberately accepted under the Article 21(1) proportionality discipline, with CRA Art. 14 vulnerability-handling readiness built in.
  ambiguity_notes: |
    The same `security in` ambiguity as SR-NIS2-026 applies; the chosen reading is broad-cumulative covering both process and product security in development. The T3-vs-text gap awareness import warning applies with equal force: the OJ does not mention NIST SSDF, OWASP SAMM, ISO 27034, or specific secure-coding catalogues, and the SR preserves OJ-literal `development` language while mapping to PR.PS-06 by meaning-alignment (synthesis §8 T3 NIS2-C11). Member State transposition divergence may apply on whether national law distinguishes in-house versus outsourced development for the depth of the obligation. Remain open: whether the Commission will adopt a delegated act under Article 24(2) specifying that development-tooling categories fall within the European cybersecurity certification scheme, which would convert a procedural development-security obligation into a certification-conditional one.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

