---
document_id: AEGIS-PREPROC-CRA-ART-3
title: CRA Art. 3 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 3
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
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.2.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 3

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-027 | An incident having an impact on the security of a product with digital elements is considered severe where it negatively affects (or is capable of negatively affecting) the ability of the product to protect the availability, authenticity, integrity, or confidentiality of sensitive or important data or functions; OR where it has led (or is capable of leading) to the introduction or execution of malicious code in the product or in the network and information systems of a user of the product. | `CRA-CL61` (Art. 14(5)(a) — SI test A: CIA of sensitive/important data/functions); `CRA-CL62` (Art. 14(5)(b) — SI test B: malicious code); `CRA-CL44` (Art. 3(44) — incident definition) | D-04.3 |
| SO-CRA-031 | An open-source software steward shall — to the extent the steward is involved in the development of the products with digital elements — notify actively exploited vulnerabilities of such products to the CSIRT designated as coordinator and to ENISA via the single reporting platform; and — to the extent severe incidents affect network and information systems provided by the steward for the development of such products — apply the severe-incident and user-notification obligations of Art. 14(3)/(8). | `CRA-CL103` (Art. 24(3) — OSS steward Art. 14(1)/(3)/(8) extension); `CRA-CL44` (Art. 3(44) — incident definition) | D-04.3, D-09.1 |
| SO-CRA-034 | Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (data minimisation). | `CRA-CL136` (Annex I Part I (2)(g) — adequate, relevant, necessary); `CRA-CL19` (Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use); `CRA-CL3` (Art. 3(23) — intended purpose definition) | D-05.1 |
| SO-CRA-034 | D-05.1 | Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) | Data minimisation: adequate, relevant, necessary for intended purpose |
| SO-CRA-038 | The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements. | `CRA-CL39` (Art. 3(39) — SBOM definition); `CRA-CL143` (Annex I Part II (1) — SBOM); `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL159` (Annex II §9 — SBOM location for user); `CRA-CL161` (Annex VII §2(b) — SBOM in technical documentation); `CRA-CL167` (Annex VII §8 — SBOM on MSA request) | D-06.2 (CRA sole authority per taxonomy §4.1), D-02.1 |
| SO-CRA-038 | D-06.2 (CRA sole authority), D-02.1 | Art. 3(39) + Annex I Part II (1) + Annex II §9 + Art. 13(24) + Annex VII §2(b)/§8 | SBOM content + format + on-request |
| SO-CRA-041 | A manufacturer established outside the Union may appoint an authorised representative established in the Union by written mandate to perform specified tasks on behalf of the manufacturer; the manufacturer's obligations under Art. 13(1)–(11), Art. 13(12) first subparagraph, and Art. 13(14) are not delegable to the authorised representative, who retains the technical documentation and cooperates with market surveillance authorities. | `CRA-CL84` (Art. 18(1) — AR appointment); `CRA-CL85` (Art. 18(2) — AR carve-out of non-delegable obligations); `CRA-CL86` (Art. 18(3) — AR tasks); `CRA-CL13` (Art. 3(13) — manufacturer definition) | D-06.4, D-09.4 |
| SO-CRA-041 | D-06.4, D-09.4 | Art. 18(1)/(2)/(3) + Art. 3(13) | Authorised representative appointment + non-delegable obligations |
| SO-CRA-042 | An importer or distributor who places a product with digital elements on the market under its own name or trademark, or who carries out a substantial modification of a product with digital elements already placed on the market, is considered to be the manufacturer for the purposes of the Regulation and assumes the manufacturer's obligations under Arts. 13 and 14. | `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL30` (Art. 3(30) — substantial modification definition) | D-06.4, D-07.4 |
| SO-CRA-042 | D-06.4, D-07.4 | Art. 21 + Art. 3(30) | Manufacturer-equivalent trigger (own name/trademark or substantial mod) |
| SO-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations. | `CRA-CL39` (Art. 13(14) — series-of-production conformity); `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL97` (Art. 22(1) — third-party substantial modification = manufacturer); `CRA-CL30` (Art. 3(30) — substantial modification definition); `CRA-CL34` (Art. 13(10) — substantial modification compliance for the last-placed version) | D-07.4, D-06.4 |
| SO-CRA-047 | D-07.4, D-06.4 | Art. 13(14) + Art. 21 + Art. 22(1) + Art. 3(30) + Art. 13(10) | Series-production conformity + substantial-modification consequences |
| SO-CRA-049 | An open-source software steward puts in place and documents in a verifiable manner a cybersecurity policy fostering the secure development of products with digital elements and the effective handling of vulnerabilities by the developers of those products, including aspects related to documenting, addressing, and remediating vulnerabilities, and the sharing of information concerning discovered vulnerabilities within the open-source community; the policy takes into account the specific nature of the open-source software steward and the legal and organisational arrangements to which it is subject. | `CRA-CL101` (Art. 24(1) — OSS steward policy); `CRA-CL14` (Art. 3(14) — open-source software steward definition); `CRA-CL48` (Art. 3(48) — free and open-source software definition) | D-09.1 |
| SO-CRA-049 | D-09.1 | Art. 24(1) + Art. 3(14)/(48) | OSS steward cybersecurity policy (verifiable) |

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

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-008
  title: "Machine-readable SBOM format for supply-chain transparency"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — SBOM format" }
    - { clause_id: CRA-CL39, article_ref: "Art. 3(39) — SBOM definition (details and supply chain relationships)" }
  linked_objectives: [SO-CRA-007, SO-CRA-038]
  sub_domain: [D-06.2, D-02.1]
  nist_csf_mapping:
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (1) requires the SBOM to be drawn up in a commonly used and machine-readable format covering at least the top-level dependencies. The CRA-defined SBOM artefact under Art. 3(39) is a formal record containing details and supply-chain relationships of the components included in the software elements of the product, so the format obligation in Annex I Part II (1) sits downstream of the definitional anchor in Art. 3(39). Art. 13(24) authorises the Commission to adopt implementing acts further specifying the format and elements of the SBOM, providing the formal route by which the "commonly used and machine-readable" floor will become binding. For a compliance officer this means selecting a format that supports automated downstream consumption, documenting the choice in the conformity dossier, and being prepared to migrate when the implementing acts specify a baseline.
  security_rationale: |
    The SBOM-format obligation in Annex I Part II (1) is operationalised in NIST CSF 2.0 through **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)** and **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply-chain risk-management process)**. ID.AM-02 captures the format-side leg: the inventory must be queryable and automatable -- a "commonly used and machine-readable format" is the structural requirement that turns the inventory from a static artefact into an input to vulnerability-management automation, CVE matching, and downstream supply-chain risk assessment. GV.SC-02 anchors the supply-chain dimension: the format must encode supplier and supply-chain relationships (per the Art. 3(39) definition), so that the SBOM supports both vulnerability lookup and supplier-prioritisation under the broader cybersecurity supply-chain risk-management process. Together ID.AM-02 and GV.SC-02 enable the manufacturer to demonstrate ex post, through a queryable SBOM artefact, format-choice documentation in the conformity dossier, and supplier-prioritisation records, that the Annex I Part II (1) format obligation has been met in a manner interoperable with the CSIRT-side and MSA-side verification workflow.
  ambiguity_notes: |
    The phrase "commonly used and machine-readable format" is POLY+VAG S3 and admits three materially distinct readings tied to format families. Reading chosen: R3, treating the obligation as "any commonly-used machine-readable format that supports automated component identification," pending the Commission implementing acts under Art. 13(24). Alternative readings: R1 (a specific sector format such as SPDX or CycloneDX) and R2 (a different specific sector format) are both currently common in the market but neither is OJ-mandated at present; the executing-acts-dependent choice lets manufacturers pick what interoperates best with their tooling while preparing for the eventual binding specification. An additional reading, R5, would set the format floor to a domain-agnostic cryptographic manifest that any SBOM-aware toolchain can ingest regardless of origin sector, achieving interoperability through shared primitives rather than shared schemas; R5 is admitted as the long-run consensus direction but rejected for current OJ reading because Annex I does not specify such a manifest, leaving the implementing-acts route to harmonise rather than the SR body to import. Format names are intentionally not introduced into the SR body to honour the V12 tech-stack denylist. Remain open: (a) when the implementing acts specify a single binding format, does the choice bind retroactively across previously-published SBOMs or only prospectively for new releases; (b) does Annex I Part II (1) require that the SBOM be human-readable in addition to machine-readable, or is the format-agnostic floor purely automated.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-015
  title: "Migration-only remediation carve-out for substantially modified versions"
  source_clauses:
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification compliance scope (last version)" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification" }
  linked_objectives: [SO-CRA-060, SO-CRA-047]
  sub_domain: [D-02.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 13(10) provides that, where a manufacturer has placed subsequent substantially modified versions of a software product on the market, the manufacturer may ensure compliance with the Annex I Part II (2) vulnerability remediation requirement only for the version last placed on the market — provided that users of previously placed versions have access to the last-placed version free of charge and do not incur additional costs to adjust the hardware and software environment in which they use the original version. Art. 3(30) defines substantial modification through a disjunctive test covering both compliance impact and intended-purpose modification. For a compliance officer the carve-out permits a "migration-only" remediation strategy but the free-of-charge / no-adjustment-required constraint protects users from being coerced into migration, so the practical scope of the carve-out is narrower than the headline suggests.
  security_rationale: |
    The Art. 13(10) + Art. 3(30) substantial-modification carve-out is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)**. PR.PS-02 captures the migration-only remediation strategy: rather than maintaining N parallel versions in parallel, the manufacturer consolidates remediation effort on the latest version and offers migration as the protection path for users on earlier versions -- the "replacement" leg of the Subcategory applies at the version level rather than the patch level. GV.SC-04 anchors the free-of-charge and no-adjustment-required dimension: third-party assessment (and self-assessment against the same standard) verifies that the migration offer is genuinely low-friction and that no user is operationally coerced into migration through hidden cost or hardware-software-environment adjustment burdens. Together PR.PS-02 and GV.SC-04 enable the manufacturer to demonstrate ex post, through documented version-management records, free-migration-offer evidence, and third-party assessment records, that the substantial-modification carve-out has been applied within its protective scope and that the user-coercion safeguard has been honoured.
  ambiguity_notes: |
    The phrase "substantial modification" inherits the Art. 3(30) definition, which is VAG+POLY S3 with three materially distinct readings. Reading chosen: R1 combined with R3, treating the Art. 3(30) literal disjunctive "affects compliance OR modifies intended purpose" as the operative test, so any change that crosses either threshold is substantial. Alternative readings: R1 alone (compliance impact only) would miss the intended-purpose dimension, where R3 alone (intended-purpose only) would miss the compliance dimension. An additional reading, R5, would apply "substantial modification" only at the boundary where compliance verification triggers anew under Annex VIII, importing the conformity-assessment notion into the modification definition; R5 reads the Art. 3(30) disjunction through a conformity lens and is admitted as a non-strict equivalent to R1+R3 when the implementation of substantial-modification checks already runs through conformity re-verification. The "free of charge" qualifier is POLY-S2 with R1 (no monetary cost) as the literal reading, which the SR preserves without imported carve-outs. Remain open: (a) how ADCO and the Commission interpret "additional costs to adjust the hardware and software environment" when a migration imposes modest operational friction that is hard to monetise; (b) whether the free-migration access must be perpetual or only for the residual support period of the original version.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-025
  title: "Secure-by-default configuration with reset capability"
  source_clauses:
    - { clause_id: CRA-CL131, article_ref: "Annex I Part I (2)(b) — secure by default configuration" }
    - { clause_id: CRA-CL2, article_ref: "Art. 6(a) proviso — properly installed, intended purpose, reasonably foreseeable" }
    - { clause_id: CRA-CL3, article_ref: "Art. 3(23) — intended purpose" }
  linked_objectives: [SO-CRA-018, SO-CRA-045]
  sub_domain: [D-03.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part I (2)(b) requires products to be made available on the market with a secure-by-default configuration — including the possibility to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. Art. 6(a) proviso anchors the configuration to intended purpose and reasonably foreseeable use, framing "secure" against the operational context the manufacturer reasonably anticipated. Art. 3(23) defines the intended purpose, providing the lexical anchor for what counts as "use" in the proviso. The combination addresses three obligations in one clause: default configuration, reset capability, and tailor-made carve-out.
  security_rationale: |
    The Annex I Part I (2)(b) + Art. 6(a) + Art. 3(23) secure-by-default obligation is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-baseline leg: the secure-by-default configuration is itself a documented configuration baseline, applied at first power-up to every unit leaving the manufacturing pipeline, with the configuration-change history auditable as part of the broader configuration-management practice. PR.DS-12 captures the data-management side: the secure-by-default configuration is the protective posture that determines which data CIA properties hold by default, with the reset-to-original-state capability providing the recovery path when a user has driven the configuration away from the secure baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented baseline-configuration records, configuration-change audit trails, and reset-capability evidence in the technical documentation under Annex VII sections 2/6, that the secure-by-default floor has been applied at the point of market placement and that the reset capability has been preserved as the recovery path.
  ambiguity_notes: |
    The phrase "secure by default configuration" is VAG-S3 because three materially distinct configurations produce materially different compliance populations. Reading chosen: R2 — the security features (authentication, access control, audit logging, network segmentation, secure-update mechanism) are enabled by default at first power-up. Alternative readings: R1 (deny-all initial state, with the user explicitly enabling required services) and R3 (zero-config security, the product works securely without any user configuration) are operationally convergent with R2: all three require security features on at delivery, and only the configuration-management user-experience differs. An additional reading, R4, would extend the "secure by default" floor to the post-deployment configuration surface: any change the user makes from the default is documented and reversible through the reset mechanism; R4 is admitted as a strengthening of the chosen R2 reading and is rejected where it would conflict with the tailor-made carve-out, which permits negotiated non-default configurations in business-user settings. Remain open: (a) when a user explicitly changes a setting from the secure default and a subsequent vulnerability surfaces, does the manufacturer retain responsibility for the as-configured state or does the configuration shift break the Art. 13(2) risk-assessment chain; (b) does the "reset to original state" obligation require preserving user data through the reset (R3) or wiping it (R1/R2).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-028
  title: "Simultaneous AEV notification to CSIRT and ENISA"
  source_clauses:
    - { clause_id: CRA-CL51, article_ref: "Art. 14(1) sentence 1 — AEV notification to CSIRT + ENISA" }
    - { clause_id: CRA-CL64, article_ref: "Art. 14(7) — routing through CSIRT of MS of main establishment" }
    - { clause_id: CRA-CL52, article_ref: "Art. 14(1) sentence 2 — single reporting platform" }
    - { clause_id: CRA-CL44, article_ref: "Art. 3(44) — incident definition (imported from Art. 6(6) NIS 2 + CRA add-on)" }
    - { clause_id: CRA-CL42, article_ref: "Art. 3(42) — actively exploited vulnerability" }
  linked_objectives: [SO-CRA-023]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(1) requires a manufacturer to notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) — the CSIRT of the Member State where the manufacturer has its main establishment in the Union — and to ENISA, via the single reporting platform established under Art. 16. Art. 3(44) imports the incident definition from NIS 2 Art. 6(6) with a CRA add-on, and Art. 3(42) defines actively exploited vulnerability. For a compliance officer the operational reading is: an AEV, once known, triggers a same-timestamp dual-channel notification routed through the single platform to the correct CSIRT and ENISA.
  security_rationale: |
    The Art. 14(1) AEV notification obligation is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident management plan executed in coordination with relevant third parties once an incident is declared)** and **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)**. RS.MA-01 captures the third-party-coordination leg: once an AEV is identified and declared, the manufacturer executes its incident-management plan in concert with the CSIRT coordinator (the CSIRT of the Member State where the manufacturer has its main establishment), ENISA, and downstream market-surveillance authorities in other Member States -- the orchestrator-coordination role is the operative duty, and the single reporting platform under Art. 14(1) sentence 2 + Art. 16 is the instrument through which the coordination is delivered. RS.CO-04 anchors the rule-consistent coordination dimension: the simultaneity requirement (Art. 14(1) sentence 1) prevents asymmetric early disclosure where one authority hears first and the other hears later, leaving an information window that adversaries can exploit, and the Subcategory anchors the cross-Member-State coordination in documented platform-mediated records. Together RS.MA-01 and RS.CO-04 enable the manufacturer to demonstrate ex post, through single-platform submission timestamps, dual-channel acknowledgement records, and incident-management plan execution evidence in the technical documentation under Annex VII, that the Art. 14(1) AEV notification has been delivered within the regulatory envelope and that ENISA's biennial synthesis pipeline receives consistent input.
  ambiguity_notes: |
    The phrase "simultaneously" is VAG-S3 because temporal precision is left to interpretation. Reading chosen: R1, treating "simultaneously" as same-timestamp on the single platform under Art. 16, because the platform enforces simultaneity architecturally. R2 (same day) and R3 (short window) are rejected as failing the simultaneity requirement. The "becomes aware of" trigger inherits the GDPR Art. 33 / NIS 2 Art. 23 ambiguity (cf. CJEU IAB Baltic C-394/21 on reasonable certainty of harm), with R1 (actual knowledge) literal and R2 (constructive knowledge through due diligence) admissible. The "actively exploited vulnerability" definition under Art. 3(42) admits R3/R4 (publicly available exploit / researcher-published PoC) as the dominant readings. An additional reading, R3-as-window, would treat "simultaneously" as occurring within a tightly bounded time window (a few hours) rather than at the literal same timestamp, accommodating the practical realities of single-platform queueing; R3-as-window is rejected because the single platform architecture under Art. 16 enforces same-timestamp submission architecturally, making the literal reading the operational reality. Remain open: (a) does a published PoC alone (without observed exploitation) qualify as an AEV, or does the manufacturer require evidence of exploitation in the wild; (b) does constructive knowledge extend to threats described in confidential channels (vendor-to-vendor vulnerability programmes) that the manufacturer has not joined.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-034
  title: "Severe-incident CIA-of-sensitive-data categorisation test"
  source_clauses:
    - { clause_id: CRA-CL61, article_ref: "Art. 14(5)(a) — severe-incident test A: CIA of sensitive/important data/functions" }
    - { clause_id: CRA-CL45, article_ref: "Art. 6(2) of NIS 2 (cross-ref via CRA Art. 3(43) `incident`) — availability, authenticity, integrity, confidentiality" }
  linked_objectives: [SO-CRA-027]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, validated, and recorded" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(5)(a) provides that an incident having an impact on the security of the product shall be considered severe where it negatively affects — or is capable of negatively affecting — the ability of the product to protect the availability, authenticity, integrity, or confidentiality of sensitive or important data or functions. The four CIA dimensions (availability, authenticity, integrity, confidentiality) are inherited from NIS 2 via the CRA Art. 3(43) incident cross-reference, with authenticity being the NIS-2/CRA-unique addition over the classical CIA triad. The "or is capable of" gate establishes forward-looking severity rather than strictly materialised harm. For a compliance officer the rule provides the categorisation test A under Art. 14(5), which is satisfied if any one CIA dimension is materially impacted on a sensitive or important data or function category.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — The four CIA dimensions (confidentiality, integrity, availability, authenticity) are listed explicitly in CRA Art. 3(44) `incident` definition. Art. 3(43) imports `incident` from NIS 2 Art. 6(6), not from Art. 6(2).]
  security_rationale: |
    The Art. 14(5)(a) severe-incident categorisation test (CIA of sensitive or important data or functions) is operationalised in NIST CSF 2.0 through **ID.RA-04 (potential impacts and likelihoods of threats exploiting vulnerabilities are identified, validated, and recorded)** and **RS.MA-03 (incidents categorised, prioritised, and scoped)**. ID.RA-04 captures the impact-estimation leg: the four CIA dimensions (availability, authenticity, integrity, confidentiality) inherited from the NIS 2 Art. 6(6) cross-reference must be evaluated for impact on sensitive or important data or functions, and the "capable of" gate requires forward-looking severity assessment even when harm has not materialised. RS.MA-03 anchors the categorisation-and-scoping dimension: the incident is categorised as severe under the Art. 14(5)(a) test when any one CIA dimension is materially impacted on a sensitive or important data or function category, with the Subcategory's scoping leg capturing the territorial and data-class scope. Together ID.RA-04 and RS.MA-03 enable the manufacturer to demonstrate ex post, through documented CIA-impact assessments, threshold-of-sensitivity evidence, and categorisation records, that the Art. 14(5)(a) test was applied with the disjunctive-inclusion reading preserved (any CIA dimension triggering severity) and that the "capable of" gate was exercised with appropriate forward-looking rigour.
  ambiguity_notes: |
    The phrase "negatively affects OR is capable of negatively affecting" is VAG+POLY S3 with R3 (literal inclusive OR) as the chosen reading, so capability is sufficient without materialisation. The phrase "sensitive OR important data or functions" is POLY+COORD S3 with materially distinct populations across the OR chain; Reading chosen: R5, treating the qualifier as broadly inclusive (any data or function significant to user operations), anchored in the harmonised-standards layer under Art. 27. An additional alternative reading, R4-closed, would limit "sensitive or important" to a closed list enumerated in the Annex or implementing acts, restoring a positive enumeration that the current OJ leaves open; R4-closed is admitted as the long-run consensus direction through harmonised standards and ADCO guidance and is rejected for current OJ reading because Annex I plus Art. 14(5) do not provide the enumeration, leaving the determination to the risk assessment until the standardisation layer matures. Remain open: (a) what evidential threshold converts "capable of affecting" into a categorisable severity claim when no harm has materialised; (b) does "sensitive" align with sector-specific legal definitions (GDPR special-category data, NIS 2 essential-services data) or is it CRA-autonomous.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-038
  title: "Voluntary third-party vulnerability reporting with CSIRT bridge"
  source_clauses:
    - { clause_id: CRA-CL69, article_ref: "Art. 15(1) — voluntary AEV reporting by any person" }
    - { clause_id: CRA-CL70, article_ref: "Art. 15(2) — voluntary SI / near-miss reporting by any person" }
    - { clause_id: CRA-CL72, article_ref: "Art. 15(4) — third-party notification + CSIRT informs manufacturer" }
    - { clause_id: CRA-CL81, article_ref: "Art. 17(4) — no increased liability for mere notification" }
  linked_objectives: [SO-CRA-030]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 15(1) and Art. 15(2) allow any natural or legal person to voluntarily notify vulnerabilities or incidents (including near misses) to the CSIRT designated as coordinator or to ENISA. Art. 15(4) requires that, where a third party notifies the CSIRT of an AEV or severe incident, the CSIRT informs the manufacturer concerned, closing the loop. Art. 17(4) provides that the mere act of notification does not subject the notifying natural or legal person to increased liability — a structural shield against chilling effects. For a compliance officer the rule sets up the regulator-side intake from non-manufacturer parties (researchers, integrators, users) and the CSIRT-side bridge back to the manufacturer.
  security_rationale: |
    The Art. 15 voluntary-reporting architecture is operationalised in NIST CSF 2.0 through **RS.CO-03 (information shared with designated internal and external stakeholders consistent with established information-sharing rules)** and **GV.SC-01 (a cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders)**. RS.CO-03 captures the upstream-input leg: any natural or legal person -- researchers, integrators, users, journalists -- may voluntarily notify vulnerabilities or incidents (including near misses) to the CSIRT designated as coordinator or to ENISA, and the Subcategory's voluntary-shared-rules framework supplies the interpretive context for what counts as "voluntary" under Art. 15. GV.SC-01 anchors the supply-chain-risk-management-program dimension: the manufacturer-side mirror of the reporting architecture must integrate the third-party intake under Art. 15(4) (CSIRT informs manufacturer concerned) and the Art. 17(4) liability shield into the supply-chain risk-management programme so that downstream vulnerability research is not chilled by disclosure-risk concerns. Together RS.CO-03 and GV.SC-01 enable the manufacturer and the wider reporting ecosystem to demonstrate ex post, through documented third-party-intake records, CSIRT-bridge evidence under Art. 15(4), and supply-chain risk-management programme records, that the voluntary-reporting architecture has remained viable and that the liability-shield under Art. 17(4) has been honoured as a structural feature of the policy regime.
  ambiguity_notes: |
    The phrase "any natural or legal person" is SCOPE-Q S2 with R1 (anyone who has information, including researchers, journalists, concerned users) as the literal reading. The phrase "near miss" inherits the Art. 3(45) definition, which in turn imports from NIS 2 Art. 6(5) — POLY+S2 with R1 (event that could have caused harm), R2 (event that caused no harm), and R3 (partial-success event) as the three admissible readings; the Annex level reading does not pick one and lets the harmonised-standards layer modulate.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-039
  title: "OSS steward actively-exploited-vulnerability reporting extension"
  source_clauses:
    - { clause_id: CRA-CL103, article_ref: "Art. 24(3) — OSS steward Art. 14(1) extension (with involvement threshold)" }
    - { clause_id: CRA-CL14, article_ref: "Art. 3(14) — open-source software steward definition" }
  linked_objectives: [SO-CRA-031]
  sub_domain: [D-04.3, D-09.1]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 24(3) of the Cyber Resilience Act extends the actively-exploited-vulnerability notification architecture of Article 14(1) to open-source software stewards — defined in Article 3(14) as legal persons — other than manufacturers — that systematically provide support on a sustained basis for the development of specific products with digital elements that are intended for commercial use, whether or not they have a commercial interest in those products. The extension operates to the extent that the steward is involved in the development of the products with digital elements, and the steward is treated, for the purposes of Article 14(1), as a manufacturer for the triggering condition. Article 24(3) further provides that — where a severe incident affects network and information systems provided by the steward for the development of such products — the obligations of Article 14(3) (severe-incident notification) and of Article 14(8) (user notification) apply to the steward in respect of those systems. The territorial scope of the Act (Article 2) and the steward definition (Article 3(14)) together define when this extension is operatively engaged — most notably the `systematically … on a sustained basis` requirement, which is the upstream gate for whether the entity is a steward at all. The recitals (notably Recital 18 on OSS) clarify that the steward is not subject to manufacturer obligations beyond the enumerated Article 14 extensions, preserving the proportionality principle articulated across the Regulation.
  security_rationale: |
    The Article 24(3) reporting extension is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident-management plan executed in coordination with relevant third parties)** and **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)**. RS.MA-01 captures the upstream-coordination function the steward is being asked to perform: once an actively-exploited vulnerability is identified, the steward must execute its incident-management plan in concert with the manufacturer, the CSIRT coordinator, and the wider OSS community that depends on the affected component — the orchestrator-coordination role is the operative duty. GV.PO-01 anchors the documentary foundation: the Article 24(1) cybersecurity policy (see SR-CRA-072) is the policy instrument without which the Article 14(1) extension discharge is procedurally incomplete, and the steward's organisational policy must be auditable on a reasoned MSA request. Together RS.MA-01 and GV.PO-01 enable the steward to demonstrate ex post, through documented coordination logs and policy-evidence records, that the Article 24(3) extension duty has been discharged consistent with the proportionality principle preserved by Recital 18.
  ambiguity_notes: |
    The phrase `to the extent that they are involved in the development of the products with digital elements` carries VAG-S3 ambiguity and exposes three live readings: R1 (commit access to a relevant repository — a strict operational threshold), R2 (maintainer or co-maintainer role in the project — an organisational role threshold), R3 (advisory or review contribution without commit rights — a contribution-volume threshold), and R4 (any involvement in the product's software supply chain — the broad literal reading captured by the words `involved` and `development`). The reading chosen is R4 — the literal text `involved` carries the broadest reasonable construction consistent with the OJ-literal purpose of catching supply-chain-attributable incidents at the upstream end. The qualifier `steward's NIS for the development of such products` is SCOPE-Q-S2: R1 (the steward's own network and information systems only — literal scope). The Article 3(14) `systematically providing support on a sustained basis` threshold, inherited from the steward definition, carries a Berry-classic POLY+COORD signature and is treated in SR-CRA-072's record. Remain open: (a) whether the European Commission's forthcoming guidance on Article 24 (signalled in Recital 18) will supply a narrower reading of `involved in the development` than the R4 literal; (b) whether stewards that monetise upstream components via SaaS, dual-licensing, or sponsored-development arrangements are exposed to dual classification — both as stewards under Article 3(14) and as de facto manufacturers under Article 3(13) — and which obligation set governs.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-045
  title: "Non-conformity corrective measures, withdrawal, or recall"
  source_clauses:
    - { clause_id: CRA-CL46, article_ref: "Art. 13(21) — corrective measures on non-conformity" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification (cross-ref for trigger)" }
  linked_objectives: [SO-CRA-063]
  sub_domain: [D-04.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(21) requires manufacturers — from the placing on the market of the product and for the support period — who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the Annex I cybersecurity requirements to immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product, as appropriate. The text expressly covers both product-side and process-side non-conformity, recognising that a product can be Annex-I-conformant on its own merits even where the manufacturer's vulnerability-handling processes are deficient, and vice versa. The `know or have reason to believe` trigger mirrors the Article 14(1) awareness trigger language (cf. SR-CRA-039) — the same constructive-knowledge debate applies. The `or withdraw or recall` formulation gives the manufacturer the choice of remedy, but the choice is governed by the proportionality principle articulated across the Regulation.
  security_rationale: |
    The Article 13(21) non-conformity corrective-measures duty is operationalised in NIST CSF 2.0 through **RS.MI-01 (incidents contained)**, **RS.MI-02 (incidents mitigated)**, and **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes in the risk landscape)**. RS.MI-01 captures the immediate-containment response: once non-conformity is known, the manufacturer isolates the affected product or process from further exposure, applying the corrective measure that brings the product or process back to conformity or removes it from the market. RS.MI-02 captures the mitigation dimension: the corrective measure is applied, and the residual risk is brought within acceptable bounds — fix, withdraw, or recall as appropriate, with the proportionality principle setting the choice. GV.OV-02 closes the strategic loop: the manufacturer's risk-management strategy is reviewed and adjusted against the change in circumstances that triggered the non-conformity, ensuring the same root cause does not recur. Together RS.MI-01, RS.MI-02, and GV.OV-02 enable the manufacturer to demonstrate ex post, through documented containment records, mitigation evidence, and strategy-review minutes, that the Article 13(21) duty has been discharged and that the proportionality of the chosen remedy (fix vs. withdraw vs. recall) is evidentially supported.
  ambiguity_notes: |
    `Immediately take the corrective measures necessary` is VAG+POLY-S2 — R1 (`immediately` = upon knowledge of non-conformity, in line with Article 14 awareness trigger; `corrective measures necessary` = the minimum set needed to restore conformity). `Withdraw or recall` is POLY-S2 — R1 (literal OR — either is admissible; the choice is the manufacturer's, governed by proportionality). The cross-reference to Article 3(30) substantial modification is significant: if the corrective measure requires a substantial modification, the Art. 22(1) third-party-modifier trigger may engage as well, transferring liability downstream. Remain open: (a) what regulatory practice crystallises around `have reason to believe` — i.e. whether constructive knowledge attaches upon receipt of an upstream-CVD report from a component supplier (per Article 13(6) in SR-CRA-051) or only upon internal verification of the non-conformity; (b) whether withdrawal versus recall is itself a proportionality determination that must be evidenced ex ante in the technical documentation under Annex VII.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-046
  title: "Product-design data minimisation adequate to intended purpose"
  source_clauses:
    - { clause_id: CRA-CL136, article_ref: "Annex I Part I (2)(g) — adequate, relevant, necessary = data minimisation" }
    - { clause_id: CRA-CL19, article_ref: "Art. 13(3) sentence 2 — intended purpose + reasonably foreseeable use" }
    - { clause_id: CRA-CL3, article_ref: "Art. 3(23) — intended purpose" }
  linked_objectives: [SO-CRA-034, SO-CRA-072]
  sub_domain: [D-05.1, D-07.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: ID.AM-03, title: "Inventories of data and corresponding metadata for designated data types are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(g) requires products with digital elements to process only data — personal or other — that are adequate, relevant, and limited to what is necessary in relation to the intended purpose of the product with digital elements. This is the CRA's data-minimisation principle, borrowing the GDPR Article 5(1)(c) language (`adequate, relevant and limited to what is necessary`) and applying it at the product-design level rather than at the controller-side processing level. Article 13(3) sentence 2 anchors the minimisation to the intended purpose (Article 3(23)) and to the reasonably foreseeable use derived from the cybersecurity risk assessment. Article 13(3) sentence 3 (cf. SR-CRA-066) requires the assessment to indicate whether and how the Annex I Part I (2) requirements apply and how they are implemented — providing the documented basis for the `necessary in relation to the intended purpose` determination.
  security_rationale: |
    The Annex I Part I (2)(g) data-minimisation principle is operationalised in NIST CSF 2.0 through **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect confidentiality, integrity, and availability)** and **ID.AM-03 (inventories of data and corresponding metadata for designated data types maintained)**. PR.DS-12 captures the strategic-posture dimension: data is managed consistent with the manufacturer's risk strategy, with the Article 13(2) risk assessment supplying the proportionality bar that determines which data classes are adequate, relevant, and necessary for the product's intended purpose. ID.AM-03 anchors the operational-traceability dimension: inventories of data and corresponding metadata for designated data types are maintained, providing the demonstrable record that the manufacturer knows which data classes are present in the product and on what basis each class was admitted under the minimisation principle. Together PR.DS-12 and ID.AM-03 enable the manufacturer to demonstrate ex post, through risk-strategy alignment and data-inventory records in the technical documentation under Annex VII §2, that the (2)(g) minimisation principle has been discharged and that the product's data footprint is no broader than its intended purpose requires.
  ambiguity_notes: |
    The three coordinated adjectives — `adequate, relevant and limited to what is necessary` — carry VAG+POLY+COORD-S3 ambiguity. Reading chosen: R2 (proportionate to purpose, demonstrable ex ante via the Annex VII §3 risk-assessment record). R1 (literal reading of each adjective as an independent gate) and R3 (any single reading satisfies all three) are the alternative readings. The `intended purpose` term inherits the Article 3(23) D23 POLY-S2 classification — the intended purpose is a product-class-relative determination that the manufacturer documents in the technical documentation (Annex VII §3). Remain open: (a) whether the EDPB's forthcoming guidance on the CRA's intersection with GDPR Article 25 (data protection by design and by default) will supply a harmonised reading of `necessary in relation to intended purpose`; (b) the operational handling of minimisation when downstream integrators extend the intended purpose (e.g. via third-party plugins or configuration) — i.e. whether the manufacturer's documented minimisation suffices, or whether the integrator inherits a re-evaluation duty.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-050
  title: "Third-party component due diligence including non-commercial OSS"
  source_clauses:
    - { clause_id: CRA-CL23a, article_ref: "Art. 13(5) — due diligence on third-party components" }
    - { clause_id: CRA-CL48, article_ref: "Art. 3(48) — free and open-source software definition" }
  linked_objectives: [SO-CRA-037]
  sub_domain: [D-06.1, D-07.1]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: ID.RA-02, title: "Threat and vulnerability information received from internal and external sources is collected and used to support risk identification" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(5) requires manufacturers to exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements. The phrase `due diligence` is a Berry-classic: it is a case-law-laden term imported from company law and M&A practice, and its operational content is supplied by the Annex VII §2 technical-documentation record and by the Article 13(2) risk assessment. The CRA's express inclusion of non-commercial OSS in the due-diligence scope — Article 3(48) — closes the largest supply-chain risk gap in modern software products: an upstream OSS dependency that is maintained by volunteers on a non-commercial basis is still subject to the manufacturer's due-diligence exercise, without converting the maintainer into a manufacturer. This is the key CRA-Unique reading: the OSS community's non-commercial posture does not transfer risk to the community; it transfers the duty to assess to the integrating manufacturer.
  security_rationale: |
    The Article 13(5) due-diligence duty is operationalised in NIST CSF 2.0 through **GV.SC-01 (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed)**, **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)**, and **ID.RA-02 (threat and vulnerability information received from internal and external sources collected and used to support risk identification)**. GV.SC-01 captures the programme-governance layer: the manufacturer establishes and maintains a documented supply-chain risk management programme covering commercial and non-commercial OSS components. GV.SC-02 anchors the supplier-prioritisation and assessment process: components are inventoried, prioritised by criticality, and assessed against documented cybersecurity criteria. ID.RA-02 closes the threat-intelligence loop: external vulnerability information (CVE feeds, advisories, OSS-security mailing lists) is collected and used to refresh the risk picture for integrated components. Together GV.SC-01, GV.SC-02, and ID.RA-02 enable the manufacturer to demonstrate ex post, through documented programme governance, supplier-assessment records, and threat-intelligence feeds, that the (5) due-diligence duty has been discharged for both commercial and non-commercial OSS components.
  ambiguity_notes: |
    `Due diligence` carries VAG+POLY-S3 ambiguity. The reading chosen is R3 — both procedural (a documented vetting process, evidenced in Annex VII §2) and substantive (positive verification of supplier / component security posture). R1 (procedural only — paper-based) is rejected as insufficient; R2 (substantive only, without documentation) is rejected as falling short of the conformity-assessment evidentiary requirements. The Article 7 reference to OSS in Article 3(48) — and the Article 24 steward provisions (SR-CRA-072 to SR-CRA-074) — together draw the perimeter at which due-diligence gives way to the steward-policy interface. Remain open: (a) whether the implementing acts under Article 13(24) (cf. SR-CRA-052) will specify minimum due-diligence evidentiary content — e.g. signed attestations of CVE-monitoring posture, vulnerability-handling SLA disclosure — beyond what is recorded in Annex VII §2 today; (b) the operational status of `due diligence` for indirect dependencies (transitive depth beyond the SBOM top-level floor) where the manufacturer has no visibility — pending implementing-acts guidance.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-061
  title: "Manufacturer-equivalent status on own-name placement or substantial modification"
  source_clauses:
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger (own name/trademark or substantial modification)" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification" }
  linked_objectives: [SO-CRA-042, SO-CRA-047]
  sub_domain: [D-06.4, D-07.4]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 21 provides that an importer or distributor shall be considered to be a manufacturer for the purposes of this Regulation — and shall be subject to the obligations of Articles 13 and 14 — where that importer or distributor places a product with digital elements on the market under its own name or trademark, or carries out a substantial modification of a product with digital elements already placed on the market. The provision is the accountability transfer at the supply-chain boundary: re-branding or substantially modifying a product makes the economic operator the manufacturer, regardless of their underlying supply relationship. Article 3(30) — cross-referenced — defines `substantial modification` as a modification occurring after the product has been placed on the market, where the manufacturer has not considered it in the conformity assessment, and which affects the compliance of the product with the essential cybersecurity requirements set out in Annex I or which modifies the intended purpose of the product.
  security_rationale: |
    The Article 21 manufacturer-equivalent trigger is operationalised in NIST CSF 2.0 through **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.SC-02 captures the supplier-prioritisation dimension: an importer or distributor that re-brands or substantially modifies a product transitions from being a downstream economic operator to being the manufacturer of record, and the supply chain risk management process re-categorises the entity accordingly. GV.SC-04 anchors the contractual-obligation-confirmation layer: the trigger condition (own-name placement OR substantial modification) is itself a contractual-and-procedural test that the importer/distributor documents in the operational record, with the Article 3(30) substantial-modification test supplying the operative criterion. Together GV.SC-02 and GV.SC-04 enable the importer or distributor to demonstrate ex post, through documented re-branding-decision records and substantial-modification assessments, that the Article 21 trigger has been correctly applied and that the accountability transfer has been executed where the trigger fires.
  ambiguity_notes: |
    `Under its name or trademark` carries VAG+POLY-S3: R3 (either — white-label, co-brand, or repackaged under a distinct trademark). R1 (strictly under one's own trademark) is rejected as narrower than the literal; R2 (only when both name and trademark diverge) is rejected as cumulatively restrictive. `Substantial modification` inherits Article 3(30) D30 — VAG+POLY+COORD-S3 (cf. SR-CRA-061/R-CRA-015 for the full reading). Reading chosen for this SR: R1 + R3 (Article 3(30) disjunctive `affects compliance OR modifies intended purpose` — literal). The interaction with Article 22 (SR-CRA-062) is significant: where the modifier is neither manufacturer nor importer nor distributor, Article 22 applies the manufacturer-equivalent status to that other person — closing a critical loophole. Remain open: (a) the operational demarcation between `intended-purpose modification` (Article 3(30) limb b) and intended-purpose-preserving configuration changes — i.e. whether adding optional features that do not affect Annex I compliance is `substantial`; (b) whether the harmonised standards under Article 27 will specify a baseline technical-modification catalogue for the most common product categories.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-070
  title: "Substantial-modification compliance scope across supply chain"
  source_clauses:
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification compliance scope" }
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger" }
    - { clause_id: CRA-CL97, article_ref: "Art. 22(1) — third-party substantial modification" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification definition" }
  linked_objectives: [SO-CRA-047, SO-CRA-060]
  sub_domain: [D-07.4, D-06.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    The Articles 13(10), 21, and 22 architecture treats substantial modification as the trigger for manufacturer-equivalent status, with the Article 13(10) carve-out allowing compliance with Annex I Part II (2) for the last-placed version of the product where the user-migration conditions are met (i.e. the user is given the choice to migrate to the modified product or to retain the last-placed version). Article 21 (SR-CRA-061) addresses the importer/distributor trigger; Article 22 (SR-CRA-062) addresses the third-party modifier trigger; Article 13(10) provides the manufacturer's own substantial-modification compliance scope.
  security_rationale: |
    The Article 13(10) + 21 + 22 substantial-modification architecture is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. PR.PS-02 captures the version-management dimension: the substantial-modification threshold is the boundary between normal-version-update and manufacturer-equivalent liability transfer, and PR.PS-02 supplies the risk-commensurate maintenance discipline that distinguishes the two. GV.SC-04 anchors the supply-chain-coordination dimension: the importer, distributor, and third-party modifier assessments (Articles 21, 22) are operationalised through the supply-chain contractual-and-procedural tests that determine when the manufacturer-equivalent status fires. Together PR.PS-02 and GV.SC-04 enable the manufacturer, importer, distributor, or third-party modifier to demonstrate ex post, through documented version-management records and supply-chain assessment evidence, that the substantial-modification boundary has been correctly applied and that the manufacturer-equivalent status has been appropriately assumed or retained.
  ambiguity_notes: |
    `Substantial modification` inherits Article 3(30) D30 — VAG+POLY+COORD-S3. See SR-CRA-061/R-CRA-015 for the full reading across this threshold. R1 (any non-compliance change) + R3 (intended-purpose modification) admitted as the disjunctive literal reading. The Article 13(10) carve-out — allowing Annex I Part II (2) compliance for the last-placed version subject to user-migration — is POLY-S2 — R1 (the carve-out is conditional on user choice; the manufacturer cannot unilaterally apply it). Remain open: (a) the operational demarcation between security updates (which rarely meet the substantial-modification threshold) and security features whose modification would meet the substantial-modification threshold — pending harmonised practice; (b) whether the substantial-modification test must be re-run at every release (formal), or only at material risk-relevant changes (substantive) — the BERs harmonised standards under Article 27 will likely converge on the latter.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-072
  title: "OSS steward verifiable cybersecurity policy and CVD enablement"
  source_clauses:
    - { clause_id: CRA-CL101, article_ref: "Art. 24(1) — OSS steward cybersecurity policy" }
    - { clause_id: CRA-CL14, article_ref: "Art. 3(14) — open-source software steward definition" }
    - { clause_id: CRA-CL48, article_ref: "Art. 3(48) — free and open-source software definition" }
  linked_objectives: [SO-CRA-049]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 24(1) requires open-source software stewards to put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product. The policy shall: (i) foster the voluntary reporting of vulnerabilities as laid down in Article 15 by the developers of that product; (ii) take into account the specific nature of the open-source software steward and the legal and organisational arrangements to which it is subject; (iii) include aspects related to documenting, addressing, and remediating vulnerabilities; (iv) promote the sharing of information concerning discovered vulnerabilities within the open-source community. The four sub-elements together define the minimum content of the cybersecurity policy — verifiable documentation, voluntary-reporting enablement, nature-aware proportionality, and remediation-practice coverage.
  security_rationale: |
    The Article 24(1) OSS-steward cybersecurity policy duty is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.SC-01 (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed)**. GV.PO-01 captures the policy-instrument layer: the cybersecurity policy is established, communicated (across the steward's maintainer base, contributors, and downstream dependents), and enforced through the documented four sub-elements (i)–(iv), with the verifiable-documentation character of the policy supplying the auditability anchor under Article 24(2) MSA cooperation (SR-CRA-073). GV.SC-01 anchors the supply-chain-risk-management dimension: the policy is positioned as the entry point of the steward's supply-chain risk management programme, with the upstream-coverage of OSS contributors and the downstream-coverage of dependents integrated into the programme. Together GV.PO-01 and GV.SC-01 enable the steward to demonstrate ex post, through the documented policy and the supply-chain-programme evidence, that the Article 24(1) duty has been discharged consistent with the proportionality principle preserved by Recital 18 and the steward definition under Article 3(14).
  ambiguity_notes: |
    `Documented in a verifiable manner` carries VAG-S3 ambiguity — the operational threshold is supplied by Article 24(2) (cf. SR-CRA-073): R1 (self-verification — the steward can demonstrate the policy on request), R2 (third-party-attested), R3 (MSA-verified on demand). Reading chosen: R1 (literal — `verifiable manner` = the steward can demonstrate the policy on request, with Article 24(2) MSA cooperation providing external verification on demand). R2 (third-party attestation) is rejected as over-prescriptive for OSS stewards; R3 (MSA-verified) is rejected as over-restrictive, since Article 24(2) only triggers on reasoned request. `Foster` (VAG+POLY-S3): R1 (encourage — literal). `Systematically providing support on a sustained basis` inherits Article 3(14) D14 — R3 (both — regular + ongoing). Remain open: (a) whether the voluntary-reporting enablement under (i) requires a published CVD coordinator email / signed PGP key / security.txt — analogous to RFC 9116 — or whether softer enablement suffices; (b) the operational handling of `verifiable` at enforcement — i.e. whether MSAs will accept a steward's self-attestation or will look for an external anchor.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

