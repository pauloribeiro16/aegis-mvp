---
document_id: AEGIS-PREPROC-CRA-ART-33
title: CRA Art. 33 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 33
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---

# CRA Art. 33

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-010
  title: "Vulnerability remediation without delay after awareness"
  source_clauses:
    - { clause_id: CRA-CL144, article_ref: "Annex I Part II (2) — address and remediate without delay" }
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — vulnerabilities addressed through security updates" }
    - { clause_id: CRA-CL24, article_ref: "Art. 13(6) sentence 1 — component vulnerability address + remediate" }
  linked_objectives: [SO-CRA-008]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (2) requires manufacturers to address and remediate vulnerabilities without delay in relation to the risks posed to the product, including by providing security updates; the clause further specifies that, where technically feasible, security updates shall be provided separately from functionality updates. Annex I Part I (2)(c) carries the same address-via-updates duty into the part I properties and pairs it with user-facing update notification. Art. 13(6) sentence 1 applies the address-and-remediate duty to component vulnerabilities identified in integrated third-party components, so the obligation is not evaded by externalising components. For a compliance officer the operational reading is: a vulnerability, once identified, triggers a documented timeline running from awareness to remediation and to user-dissemination (the latter covered in SR-CRA-017), with the technical-feasibility carve-out logged in the conformity dossier.
  security_rationale: |
    The Annex I Part II (2) "address and remediate without delay" duty is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **ID.RA-06 (risk responses chosen, prioritised, planned, tracked, and communicated)**. PR.PS-02 captures the maintenance and replacement leg: software is maintained (patched, mitigated, or where necessary replaced) commensurate with the risk that the vulnerability poses, and the address-and-remediate timeline is a sub-stream of the broader software-maintenance lifecycle. ID.RA-06 anchors the response-management dimension: risk responses are chosen (patch versus mitigation), prioritised (by severity and exploit availability), planned (with milestone evidence), tracked (with progress records), and communicated (upstream to the SBOM owners, downstream to users under SR-CRA-017). Together PR.PS-02 and ID.RA-06 enable the manufacturer to demonstrate ex post, through documented remediation timelines, technical-feasibility carve-out records in the conformity dossier under Annex VII, and addressed-component evidence under Art. 13(6), that the "without delay" anchor has been exercised continuously from the awareness moment through to user-dissemination, and that the Art. 13(2) risk-assessment prioritisation remains in force as the pipeline progresses.
  ambiguity_notes: |
    The phrase "without delay" is VAG-S3 in the Berry-classic sense, structurally identical to "without undue delay" in GDPR Art. 33 and NIS 2 Art. 23(4)(a). Reading chosen: R1, where remediation action commences immediately on awareness and the ceiling is determined by the duration of the technical remediation pipeline, with record-keeping and advisory messages to users accompanying each remediation step. Alternative readings: R2 (delay permitted up to a calendar ceiling of N days regardless of pipeline duration) would risk creating a licence to delay beneath the headline obligation; R3 (subjective manufacturer discretion) is rejected as failing the inquiry-resistant test. An additional reading, R4, would characterise "without delay" as beginning at the moment of developer handoff rather than the moment of awareness, shifting the clock upstream to internal triage; R4 is rejected because the OJ text anchors the trigger at the manufacturer's knowledge rather than at developer assignment, but the operational consequence is identical where the manufacturer's process is tightly coupled. The COORD-S2 "address and remediate" conjunction is treated literally as both required, with "address" denoting the acknowledgement, triage, and communication step and "remediate" denoting the patch or mitigation. Remain open: (a) does the awareness clock pause while the manufacturer awaits confirmation from the reporter (CVD step), or does it run continuously from initial receipt; (b) when remediation requires changes that exceed a single release cycle (schema migration, dependency removal), does the literal "without delay" require partial mitigations to be deployed in the interim.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

