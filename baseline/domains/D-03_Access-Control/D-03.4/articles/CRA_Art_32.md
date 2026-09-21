---
document_id: AEGIS-PREPROC-CRA-ART-32
title: CRA Art. 32 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 32
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
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# CRA Art. 32

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-052 | A product with digital elements is presumed to be in conformity with the essential cybersecurity requirements set out in Annex I where the product and the manufacturer's processes conform to harmonised standards, common specifications, or European cybersecurity certification schemes adopted pursuant to Regulation (EU) 2019/881 at the assurance level specified by Art. 8(1) or Art. 32(2)/(3). | `CRA-CL108` (Art. 27(1) — presumption of conformity (harmonised standards)); `CRA-CL109` (Art. 27(2) — common specifications); `CRA-CL110` (Art. 27(5) — common-specs presumption); `CRA-CL111` (Art. 27(8) — CSA-certification presumption); `CRA-CL112` (Art. 27(9) — delegated acts specifying CSA schemes) | D-09.1 |
| SO-CRA-058 | The manufacturer draws up, before placing a product with digital elements on the market, the technical documentation referred to in Art. 31; carries out (or has carried out) the chosen conformity assessment procedure referred to in Art. 32; and — where compliance with the applicable cybersecurity requirements has been demonstrated — draws up the EU declaration of conformity in accordance with Art. 28 and affixes the CE marking in accordance with Art. 30. | `CRA-CL36` (Art. 13(12) sentence 1 — tech docs + conformity assessment before placing); `CRA-CL37` (Art. 13(12) sentence 2 — EU declaration + CE marking); `CRA-CL120` (Art. 31(1) — tech docs contain Annex I compliance evidence); `CRA-CL121` (Art. 31(2) — tech docs drawn up before placing and updated during support); `CRA-CL113` (Art. 28(1) — EU declaration content); `CRA-CL114` (Art. 28(2) — declaration format per Annex V/VI); `CRA-CL116` (Art. 28(4) — manufacturer's responsibility); `CRA-CL117` (Art. 30(1) — CE marking affixing); `CRA-CL118` (Art. 30(3) — CE marking before placing) | D-09.4 |
| SO-CRA-066 | The manufacturer designates the conformity-assessment procedure applicable to the product with digital elements in accordance with Art. 32, choosing between Module A (internal production control, default), Modules B+C (EU-type examination + internal production control, for Class I/II important products when harmonised standards are not fully applied), Module H (full quality assurance), or — where available and applicable — a European cybersecurity certification scheme at assurance level at least 'substantial'. | `CRA-CL123` (Art. 32(1) — default CA: modules A / B+C / H / certification); `CRA-CL124` (Art. 32(2) — Class I CA: B+C or H); `CRA-CL125` (Art. 32(3) — Class II CA: B+C / H / certification at substantial); `CRA-CL126` (Art. 32(4) — critical products CA: certification or B+C/H fallback); `CRA-CL127` (Art. 32(5) — FOSS simplified CA: module A when tech docs are public) | D-09.4 |
| SO-CRA-066 | D-09.4 | Art. 32(1)/(2)/(3)/(4)/(5) | Conformity-assessment procedure selection (Module A / B+C / H / certification) |
| SO-CRA-071 | The manufacturer establishes and operates a conformity-assessment regime in line with the modules specified in Annex VIII (Module A internal production control as default; Modules B+C / Module H for Class I/II important and critical products) ensuring that the product's design, production, and vulnerability-handling processes meet the Annex I cybersecurity requirements on a continuing basis. | `CRA-CL123` (Art. 32(1) — default CA); `CRA-CL168` (Annex VIII Part I (1) — Module A); `CRA-CL169` (Annex VIII Part I (2) — Annex VII docs in Module A); `CRA-CL170` (Annex VIII Part I (3) — design/production/vuln for Module A); `CRA-CL171` (Annex VIII Part II (1) — Module B); `CRA-CL172` (Annex VIII Part II (3) — Module B application); `CRA-CL173` (Annex VIII Part II (6) — EU-type certificate); `CRA-CL174` (Annex VIII Part II (8) — Module B periodic audits); `CRA-CL175` (Annex VIII Part III (1) — Module C); `CRA-CL176` (Annex VIII Part IV (1) — Module H) | D-10.3, D-09.4 |
| SO-CRA-071 | D-10.3, D-09.4 | Art. 32(1) + Annex VIII Parts I–IV | Module A/B+C/H conformity-assessment regime |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-001
  title: "State-of-the-art cryptographic confidentiality baseline"
  source_clauses:
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — confidentiality + encryption" }
    - { clause_id: CRA-CL14, article_ref: "Art. 13(1) — design/development/production duty" }
  linked_objectives: [SO-CRA-001, SO-CRA-045]
  sub_domain: [D-01.1, D-01.2]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.DS-02, title: "The confidentiality, integrity, and availability of data-in-transit are protected" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(1) lays the umbrella design-and-development duty on manufacturers, executed in the three sequenced phases described in CRA-CL14 (designed, developed, produced) and tied to the Annex I risk-based baseline through Recital 49. On top of that umbrella, Annex I Part I (1) requires that products with digital elements ensure an appropriate level of cybersecurity based on the risks presented by the product across its life cycle, and Annex I Part I (2)(e) carries that umbrella into a concrete property: stored, transmitted, or otherwise processed data — personal or other — must be protected in its confidentiality by state-of-the-art mechanisms, illustrated as encrypting relevant data at rest or in transit, "or by using other technical means." The triangular architecture — chapeau, Art. 13 umbrella, sub-clause property — is what makes (2)(e) operationally actionable; the manufacturer cannot meet "appropriate cybersecurity" without addressing confidentiality, and cannot address confidentiality without choosing a recognised cryptographic baseline. For a compliance officer this means documenting the cryptographic choice and the underlying risk rationale in the conformity dossier under Annex VII §3, retaining that justification for the support period established under Art. 13(8)–(9) (cf. Recital 49 for the support-period rationale).
  security_rationale: |
    The obligation in Annex I Part I (1)+(2)(e) is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)** and **PR.DS-02 (data-in-transit confidentiality, integrity, and availability protected)**. PR.DS-01 anchors the cryptographic protection of stored data -- keys, certificates, key-management material -- so that an attacker who bypasses storage-layer controls (insider access, lost device, misconfigured bucket) still meets ciphertext without the corresponding key, the structural defence against offline exfiltration and ransomware plaintext-theft. PR.DS-02 anchors the in-transit leg: end-to-end confidentiality on data flowing across network paths, service-to-service calls, and external APIs, where network-position adversaries and misconfigured peering make the in-transit stratum the most frequently observed breach vector in published incident telemetry. Together PR.DS-01 and PR.DS-02 form the substrate on which every other Annex I Part I control is laid -- without them, authentication tokens can be intercepted, audit logs exfiltrated, and incident forensics become inadmissible -- and they enable the manufacturer to demonstrate ex post, through documented cipher-suite choices, key-handling evidence in the technical documentation under Annex VII sections 2/3, and conformity-assessment records under Art. 13, that the state-of-the-art baseline required by (2)(e) has been met across the support period under Art. 13(8).
  ambiguity_notes: |
    The source clause carries two distinct ambiguity stacks. First, the term state of the art is VAG-S3 in the Berry-classic sense — temporal and benchmark-relative, much like "state of the art" in GDPR Art. 32(1). Reading chosen: R2, anchoring the benchmark to harmonised standards adopted under Art. 27 (when present) and, in their absence, to industry-standard cryptographic mechanisms as of the product's support-period commencement date. Alternative readings: R1 would require continuous R&D reassessment on a literal "instant of evaluation" basis, generating unbounded compliance churn and effectively compelling a never-finished redesign cycle; R3 (any mechanism chosen by the manufacturer) would dilute the floor to "any algorithm that compiles," breaking the cross-Member-State level playing field that Annex I is designed to deliver. An additional reading, R0, would treat state-of-the-art as a forward-looking duty that anticipates the next regulatory or standards step beyond support-period commencement, structurally similar to R2 but materially more demanding; R0 is rejected on the literal bench-anchored reading preserved by Annex I. Second, the phrase at rest or in transit is POLY-S2 because the boundary between persistent storage, transient caches, and inter-process transfers is technical rather than legal; Reading chosen: R3 — both contexts are protected, with the Art. 13(2) risk assessment selecting the appropriate primitive for each technical layer. Remain open: (a) when harmonised cryptography standards under Art. 27 are slow to be adopted, can a manufacturer rely on industry-led profiles (NIST SP 800-131A, BSI TR-02102) without violating the "state of the art" baseline; (b) does post-quantum migration obligation attach to legacy products within their support period, or only to newly placed-on-the-market versions after a determined cut-over date?
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-018
  title: "Automatic security updates with user opt-out capability"
  source_clauses:
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — automatic security updates + opt-out + postponement" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8(e) — how the automatic-update default setting can be turned off" }
  linked_objectives: [SO-CRA-019, SO-CRA-009]
  sub_domain: [D-03.4, D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(c) requires vulnerabilities to be addressed through security updates, including — where applicable — through automatic security updates installed within an appropriate timeframe enabled as a default setting, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them. Annex II §8(e) obliges the manufacturer to inform the user how the automatic-update default can be turned off, lifting the user's path from implication (the setting exists) to discoverability (the setting is documented). For a compliance officer the operational consequence is: auto-update on by default, opt-out discoverable and single-click, postponement available, and Annex II §8(e) disclosure present in the user-facing materials.
  security_rationale: |
    The Annex I Part I (2)(c) + Annex II section 8(e) auto-update-default and opt-out architecture is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-management dimension: the auto-update default is itself a configuration baseline that must be established, documented (in the technical documentation and the Annex II section 8(e) user-facing materials), and applied consistently across deployed instances -- the secure-by-default principle operationalised at the update channel level. PR.DS-12 captures the data-management side: the auto-update mechanism exists to preserve data CIA over time, and the opt-out and postponement options are risk-modulated choices that allow enterprise users and regulated industries to operate within controlled update windows without sacrificing the baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented default configurations, configuration-change audit trails, and Annex II section 8(e) user-information records, that the auto-update default has been implemented consistent with Annex I Part I (2)(c) and that the user-autonomy safeguards (opt-out, postponement) have been preserved.
  ambiguity_notes: |
    The phrase "within an appropriate timeframe" in Annex I Part I (2)(c) is VAG-S3 in the Berry-classic "appropriate" sense (cf. GDPR Art. 32, NIS 2 Art. 21). Reading chosen: R2, anchoring the timeframe to the severity of the addressed vulnerability and the user's operational environment, modulated by the Art. 13(2) risk assessment. Alternative readings: R1 (a single quantitative ceiling for all vulnerabilities) is rejected because severity modulation is the operative sanity check; R3 (manufacturer discretion) is rejected as failing the inquiry-resistant test. The "clear and easy-to-use" qualifier is VAG-S2 with R1 (UI discoverable + single-click) as the literal reading, anchored in harmonised standards and Art. 7(4) Commission implementing acts. An additional reading, R5, would tie the timeframe to harmonised-standards baselines that specify a category-specific deployment window (industrial control, medical device, consumer IoT); R5 is admitted as the long-run consensus direction but is rejected for current OJ reading because Annex I Part I (2)(c) leaves the timeframe to the manufacturer's risk assessment, pending Art. 7(4) implementing acts that may specify defaults. Remain open: (a) does the opt-out obligation require that disabling auto-update also disable any active update channel that could silently re-enable, or merely that the toggle be respected once flipped; (b) when updates are bundled (security + functionality), must Annex I Part II (2)'s "where technically feasible" separation route the entire bundle through opt-in for the functionality part.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-095
  title: "Module A default self-declared conformity assessment"
  source_clauses:
    - { clause_id: CRA-CL123, article_ref: "Art. 32(1) — default conformity assessment" }
    - { clause_id: CRA-CL168, article_ref: "Annex VIII Part I (1) — Module A: sole responsibility" }
  linked_objectives: [SO-CRA-066]
  sub_domain: [D-09.4, D-10.3]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 32(1) provides that manufacturers of products with digital
    elements — for products that do not fall under Class I/II important
    products or critical products — may demonstrate conformity with the
    Annex I requirements by using one of the procedures specified in
    paragraphs (2), (3), or (4) of Article 32, including Module A
    (internal production control) under Annex VIII Part I. Module A
    places sole responsibility on the manufacturer for the design,
    development, production, and vulnerability-handling processes, and
    requires drawing up the Annex VII technical documentation. Module A
    is therefore the default route, but not the only option within
    Article 32(1) [Recital 58].
  security_rationale: |
    The Art. 32(1)/Annex VIII Part I Module A default route is
    operationalised in NIST CSF 2.0 through GV.PO-02 and GV.OC-03.
    GV.PO-02 (Cybersecurity processes and procedures for implementing
    the cybersecurity policy are established, communicated, and
    enforced) anchors the internal-production-control procedure —
    the manufacturer executes the SDLC controls, draws up the Annex VII
    documentation, and self-declares without a third-party check.
    GV.OC-03 anchors the legal-classification content: the
    manufacturer knows which products fall under the Module A default
    and which are escalated to Class I/II/critical procedures under
    Art. 32(2)/(3)/(4). Together, GV.PO-02 and GV.OC-03 give the
    manufacturer a class-identification and internal-execution control
    set that can demonstrate ex post that the correct procedure was
    chosen for the product's class.
  ambiguity_notes: |
    "May demonstrate … by using Module A" reads as manufacturer choice
    inside the Article 32(1) default set; Article 32(2), (3), and (4)
    impose Module B+C, H, or certification when class-driven. The
    choice among the Article 32(1) procedures is administrative; the
    Article 32(2)/(3)/(4) elevation is class-driven and outside the
    manufacturer's discretion.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-096
  title: "Class I notified-body conformity-assessment routes"
  source_clauses:
    - { clause_id: CRA-CL124, article_ref: "Art. 32(2) — Class I important products: Module B+C or H" }
    - { clause_id: CRA-CL171, article_ref: "Annex VIII Part II (1) — Module B: EU-type examination" }
    - { clause_id: CRA-CL175, article_ref: "Annex VIII Part III (1) — Module C: internal production control" }
    - { clause_id: CRA-CL176, article_ref: "Annex VIII Part IV (1) — Module H: full quality assurance" }
  linked_objectives: [SO-CRA-066]
  sub_domain: [D-09.4, D-10.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 32(2) routes Class I important products — those listed in
    Annex III Class I — to Module B+C (EU-type examination by a notified
    body followed by internal production control) or to Module H (full
    quality assurance by a notified body), where the manufacturer has
    not applied, or has applied only in part, harmonised standards,
    common specifications, or CSA schemes at assurance level at least
    "substantial"; or where such standards, specifications, or schemes do
    not exist. Where harmonised standards are fully applied, the
    presumption in Article 27 can in principle reduce the third-party
    assessment perimeter, but Article 32(2) still requires the
    manufacturer to follow the chosen procedure for the residual elements
    [Recital 58].
  security_rationale: |
    The Art. 32(2) Class I notified-body routes (Annex VIII Part II/III/IV
    — Modules B, C, H) are operationalised in NIST CSF 2.0 through
    GV.OC-03 and GV.SC-04. GV.OC-03 anchors the class-and-procedure
    selection content: the manufacturer identifies the Annex III Class I
    classification and selects the admissible procedure (B+C or H)
    consistent with the harmonised-standard application status. GV.SC-04
    (Suppliers and other third parties are routinely assessed using
    audits, test results, or other forms of evaluation to confirm they
    are meeting their contractual obligations) anchors the notified-body
    layer as a third-party evaluation of the manufacturer's
    design-and-vulnerability-handling processes. Together, GV.OC-03 and
    GV.SC-04 give the manufacturer a class-and-evaluation control set
    that the notified body can verify and that the manufacturer can
    demonstrate ex post was correctly chosen and correctly executed.
  ambiguity_notes: |
    The trigger "has not applied or has applied only in part" is a
    literal inclusive disjunction — both states trigger the third-party
    route. The coordination "harmonised standards, common specifications
    or European cybersecurity certification schemes" admits any
    combination of those three conformity routes; the test is whether
    the cumulative application covers each Annex I requirement, not
    whether a single instrument covers all. The structural ambiguity in
    practice is whether partial harmonised-standard coverage is a
    triggering state even when the design type is otherwise settled,
    and the literal reading says yes.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-097
  title: "Class II conformity routes including CSA certification"
  source_clauses:
    - { clause_id: CRA-CL125, article_ref: "Art. 32(3) — Class II important products: B+C / H / certification at substantial" }
  linked_objectives: [SO-CRA-066]
  sub_domain: [D-09.4, D-10.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 32(3) routes Class II important products — those listed in
    Annex III Class II — to Module B+C, Module H, or — where available
    and applicable — a European cybersecurity certification scheme
    pursuant to Article 27(9) at assurance level at least "substantial".
    The certification path is the third option in Article 32(3), in
    addition to the two notified-body routes inherited from Article 32(2)
    [Recital 58].
  security_rationale: |
    The Art. 32(3) Class II routes are operationalised in NIST CSF 2.0
    through GV.OC-03. GV.OC-03 (Legal, regulatory, and contractual
    requirements regarding cybersecurity are understood and managed)
    anchors the class-identification and procedure-selection content:
    the manufacturer identifies the Annex III Class II classification,
    evaluates whether an Art. 27(9) CSA scheme at "substantial" or
    higher covers the product category, and selects the admissible
    route — Module B+C, Module H, or CSA certification. The
    single-Subcategory mapping reflects that the addition over Class I
    is the certification path rather than a new control surface.
    GV.OC-03 gives the manufacturer a managed-requirements framework
    that can demonstrate ex post that the Class II procedure was
    correctly chosen from the three available options, including the
    CSA certification route when available.
  ambiguity_notes: |
    "At assurance level at least 'substantial'" reads literally: the
    assurance-level floor is "substantial". Higher levels (e.g. "high")
    satisfy the floor by definition. The structural constraint is the
    availability of CSA schemes covering the Class II product category;
    where no such scheme has been adopted under Article 27(9), the
    certification path collapses into the Article 32(2)-equivalent
    Module B+C / H routes.
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

