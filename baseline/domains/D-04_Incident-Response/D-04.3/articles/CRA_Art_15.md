---
document_id: AEGIS-PREPROC-CRA-ART-15
title: CRA Art. 15 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 15
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---

# CRA Art. 15

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-030 | Any natural or legal person may voluntarily notify vulnerabilities or incidents (including near misses) of products with digital elements to the CSIRT designated as coordinator or to ENISA, and a CSIRT initially receiving a notification that does not originate from the manufacturer informs the manufacturer; the mere act of notification does not subject the notifying natural or legal person to increased liability. | `CRA-CL69` (Art. 15(1) — voluntary AEV reporting); `CRA-CL70` (Art. 15(2) — voluntary SI / near-miss reporting); `CRA-CL72` (Art. 15(4) — third-party notification + CSIRT-informs-manufacturer); `CRA-CL81` (Art. 17(4) — liability shield) | D-04.3, D-09.4 |
| SO-CRA-030 | D-04.3, D-09.4 | Art. 15(1)/(2)/(4) + Art. 17(4) | Voluntary vulnerability/incident/near-miss reporting + liability shield |

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

