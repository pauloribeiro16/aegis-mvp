---
document_id: AEGIS-PREPROC-CRA-ART-7
title: CRA Art. 7 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 7
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 7

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-067 | The Commission may adopt implementing acts specifying the format and elements of the software bill of materials referred to in Annex I Part II (1); ADCO may conduct a Union-wide dependency assessment on the Union's dependence on software components (in particular FOSS components) for specific categories of products with digital elements. | `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL50` (Art. 13(25) — Union-wide dependency assessment by ADCO); `CRA-CL67` (Art. 14(9) — delegated acts on delay-dissemination grounds); `CRA-CL68` (Art. 14(10) — implementing acts on notification format/procedures); `CRA-CL8` (Art. 7(3) — delegated acts amending Annex III); `CRA-CL9` (Art. 7(4) — implementing acts specifying technical descriptions); `CRA-CL119` (Art. 30(6) — implementing acts on labels/pictograms) | D-09.4 |
| SO-CRA-067 | D-09.4 | Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6) | Commission implementing / delegated acts (SBOM, delay grounds, labels, technical descriptions) |

## Security Rules (from 02_SecurityRules_NIST.md)

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

