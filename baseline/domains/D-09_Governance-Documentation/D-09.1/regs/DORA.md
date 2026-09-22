# D-09.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-016 + SO-DORA-017 | Management body defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework (Art. 5(2)), supported by a sound, comprehensive and well-documented framework (Art. 6(1)); ICT risk assigned to a control function with appropriate level of independence according to three lines of defence model + identification/classification/documentation of ICT supported business functions and information/ICT assets (Art. 6(4) + Art. 7(1)). | Financial-entity ICT risk-management framework; three-lines-of-defence + asset identification/classification as governance anchor. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | sound, comprehensive, well-documented ICT risk-management framework comprising 5-artefact types (strategies, policies, procedures, ICT protocols, tools) + three-lines-of-defence model + ICT supported business functions / information assets / ICT assets identified, classified, documented | Art. 5(2) `The management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` + Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively` + Art. 6(4) `three lines of defence model` | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible + `all arrangements`) — corporate-governance body | competent authority (NCA — national financial supervisory authority) + management body — Art. 6(1) ICT risk-management framework + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 5(2) + Art. 6(1) + Art. 6(2) 5-artefact closed list (`strategies, policies, procedures, ICT protocols and tools`) + Art. 6(4) three-lines-of-defence + Art. 7(1) asset identification/classification + Art. 4 proportionality |

## Sub-SO (DORA)

#### D-09.1.4 — Sub-SO for DORA

```yaml
id: SO-D-09.1.DORA
subdomain: D-09.1
applies_to: [DORA]
inherits_from: SO-DORA-016 + SO-DORA-017
source_SR: SR-DORA-026 + SR-DORA-027 + SR-DORA-028
activation: if DORA in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The management body of the financial entity **defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework** (Art. 5(2) DORA), supported by a **sound, comprehensive and well-documented ICT risk management framework** (Art. 6(1)) with a three-lines-of-defence model (Art. 6(4)).

**CSF anchors (from `SR-DORA-026` + `SR-DORA-027` + `SR-DORA-028` v0.3 security_rationale):**
GV.PO-01 (primary), GV.RR-02, GV.RM-04.

---


## Security Requirements (DORA)

#### 9.1.4 — Financial-entity ICT risk-management framework with management-body define/approve/oversee/be-responsible and three-lines-of-defence

```yaml
- req_id: 9.1.4
  volere_section: 15
  volere_subtype: integrity

  title: "Financial entity operates a sound, comprehensive, well-documented ICT risk-management framework with three-lines-of-defence and identified, classified, documented ICT supported business functions and assets"

  derives_from:
    hso_sub_so: SO-9.1.DORA
    per_reg_so: SO-DORA-016 + SO-DORA-017
    source_sr: SR-DORA-026 + SR-DORA-027
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.4"

  description: |
    The product shall establish and maintain a sound, comprehensive, and well-documented ICT risk-management framework comprising strategies, policies, procedures, ICT protocols, and tools, with the management body defining, approving, overseeing, and being responsible for its implementation (per DORA Art. 5(2) four-verb coordination + Art. 6(1) framework + Art. 6(2) 5-artefact closed list), with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence according to the three lines of defence model (per Art. 6(4)), and with ICT supported business functions, information assets, and ICT assets identified, classified, and adequately documented (per Art. 7(1)).

  fit_criterion: |
    A sound, comprehensive, and well-documented ICT risk-management framework is established under Art. 6(1) `which enables them to address ICT risk quickly, efficiently and comprehensively` (SR-DORA-027) with GV.PO-01 + GV.PO-02 + GV.RM-04 (the framework documents the entity's approach to ICT risk, supports the operational-procedure layer with documented processes and procedures, and couples policy formulation to strategic-direction and update-coupling); the framework comprises the Art. 6(2) 5-artefact closed list `strategies, policies, procedures, ICT protocols and tools`; the management body discharges the Art. 5(2) four-verb coordination (SR-DORA-026) `define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` with GV.RR-01 leadership accountability + GV.RR-02 approval as documented governance act (the approval minute records the management body's reading of the framework, acceptance of residual risk, and resource commitment, creating executive sponsorship) + GV.OC-03 standing duty to track the full set of legal, regulatory, and contractual obligations that DORA adds on top of CRA, NIS 2, GDPR, and AI Act; the `define, approve, oversee and be responsible for` (S2 VAG + POLY + COORD per SR-DORA-026 ambiguity_notes) four-verb coordination carries the ambiguity on whether the four verbs are four distinct obligations or a composite — chosen reading: four distinct obligations (the OJ coordinates four verbs with commas and the conjunction `and`); the responsibility for managing and overseeing ICT risk is assigned to a control function with appropriate level of independence according to the three lines of defence model (or an internal risk management and control model) per Art. 6(4) (SR-DORA-027) with GV.RR-02 + GV.OC-03 (the three-lines-of-defence model is operationalised as a documented control-function independence architecture, with the operational-management function as first line, the risk-management and compliance function as second line, and the internal-audit function as third line, each with documented independence and reporting lines); ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk are identified, classified and adequately documented per Art. 7(1) (SR-DORA-027 cross) with GV.OC-04 critical-objectives-and-capabilities understanding (the entity understands and communicates the ICT-supported business functions, the assets supporting those functions, and their roles and dependencies in relation to ICT risk) + GV.RM-05 upward-channel substrate (the CISO and relevant functions have documented escalation paths to the management body, including exception and incident reporting); the framework is documented under Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance supervisory baseline + EBA Guidelines on ICT and security risk management; for smaller entities under Art. 4 proportionality, the framework is proportionate to the entity's risk exposure, size, and complexity; for a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities, per CRDA-deep §9.1 NIS2↔DORA verified relationship); for a DORA financial entity that is also a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR Art. 24(1) data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair (DORA-dominant for financial entities, per CRDA-deep §9.1 GDPR↔DORA verified relationship); for a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair (Conditional Y when DORA entity procures CRA-conformant products, per CRDA-deep §9.1 CRA↔DORA verified relationship); for a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component, per CRDA-deep §9.1 DORA↔AI_Act verified relationship); verified by Art. 6(1) framework documentation review + Art. 5(2) management-body oversight records + Art. 6(2) 5-artefact closed-list records + Art. 6(4) three-lines-of-defence model documentation + Art. 7(1) ICT asset register + asset classification records + EBA Guidelines on ICT and security risk management supervisory-baseline documentation + NCA (national financial supervisory authority) review on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.2 (Art. 5(4) management-body training as literacy prerequisite for Art. 5(2) define/approve/oversee/be-responsible), 9.1.2 (when DORA-NSIE — DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act; EQUAL classification, DORA-dominant stack for financial entities), 9.1.1 (when DORA-controller — DORA framework as carrier + GDPR data-protection policies as module; DORA-dominant stack), 9.1.3 (when DORA entity procures CRA-conformant — CRA presumption discharges parts of DORA supplier-assessment evidence but not DORA framework obligation), 9.1.5 (when DORA FE deploys high-risk AI — DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack; three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component)]

  nist_csf: [GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.OC-03, GV.OC-04, GV.RM-05]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 5(2) + Art. 6(1) + Art. 6(4)):**
> "The management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework." — Art. 5(2) DORA (per SR-DORA-026)
> "Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively." — Art. 6(1) DORA (per SR-DORA-027)
> "Financial entities shall assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … in accordance with the three lines of defence model, or an internal risk management and control model." — Art. 6(4) DORA (per SR-DORA-028)

**DORA article (verbatim, Art. 5(2) + Art. 6(1) + Art. 6(4)):**
> [as quoted above]

**DORA article (verbatim, Art. 6(1)):**
> "Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively." — Art. 6(1) DORA (per SR-DORA-027)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.1: GDPR↔DORA = COMPLEMENTARY (SAME — DORA framework as carrier + GDPR data-protection policies as module for DORA financial entities that are controllers); NIS2↔DORA = EQUAL (SAME — both regulations impose policy + governance architecture; DORA-dominant for financial entities under DORA's direct scope; NIS 2 applies to the financial entity only insofar as it is an NSIE outside DORA); CRA↔DORA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when DORA entity procures CRA-conformant products; CRA presumption discharges parts of DORA supplier-assessment evidence but not DORA framework obligation); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack for DORA financial entities deploying high-risk AI))
```

### from regs/DORA.md body

*(GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the DORA Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework` mapped to NIST CSF 2.0 GV.PO-01; GV.RR-02 — Roles/responsibilities/accountabilities established — anchors the DORA Art. 6(4) `three lines of defence model` per DomainAnalysis §D-09.1 line 178 cross-validation; the management-body define/approve/oversee/be-responsible architecture (Art. 5(2) four-verb coordination) extends to all arrangements related to the ICT risk-management framework, with the management body collectively responsible for the framework's implementation. The three subcategories together enable the financial entity to demonstrate ex post, against the national competent authority + EBA supervisory baseline, that the Art. 6(1) ICT risk-management framework + Art. 5(2) management-body oversight + Art. 6(4) three-lines-of-defence architecture were established and maintained in light of the proportionality factors (size, nature, scale, complexity per Art. 4). For DORA financial entities that are also NIS 2 NSIEs, the DORA ICT risk-management framework discharges both obligations — DORA-dominant under DORA's direct scope (EQUAL classification). For DORA financial entities that are also controllers, the GDPR Art. 24(1) data-protection policies become a module within the DORA framework — DORA-led stack with GDPR as module.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔NIS2 = Y (DORA financial entity = NSIE; DORA-dominant stack for financial entities — EQUAL on policy + governance dimension); DORA↔GDPR = Y (DORA financial entity = controller; DORA framework as carrier + GDPR data-protection policies as module; DORA-dominant for financial entities); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant products); DORA↔AI_Act = Y (DORA FE deploys high-risk AI; DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack; three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA information-security-policy obligation at 9.1 is the **financial-entity ICT risk-management framework** with the **management-body define/approve/oversee/be-responsible architecture** (Art. 5(2) four-verb coordination) + **three-lines-of-defence** (Art. 6(4)) + **ICT asset identification / classification / documentation** (Art. 7(1)) as governance anchor. Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework` carries S2 VAG + POLY + COORD on `sound, comprehensive and well-documented` (three vague adjectives — operational thresholds supplied by EBA Guidelines on ICT and security risk management) and on `quickly, efficiently and comprehensively` (S3 VAG + POLY + COORD per SR-DORA-027 ambiguity_notes); Art. 6(2) 5-artefact closed list `strategies, policies, procedures, ICT protocols and tools` — full content codification (vs GDPR's entity-discretionary content under Art. 24(2) or NIS 2's entity-discretionary content under Recital 56 proportionality); Art. 5(2) four-verb coordination `define, approve, oversee and be responsible for` carries S2 VAG + POLY + COORD ambiguity on whether the four verbs are four distinct obligations, one composite obligation, or other combinations — chosen reading: four distinct obligations (per SR-DORA-026 ambiguity_notes, the OJ coordinates four verbs with commas and the conjunction `and`); Art. 6(4) `three lines of defence model` carries S2 VAG + POLY + COORD on `appropriate level of independence` (chosen reading: operational-management as first line, risk-management and compliance as second line, internal-audit as third line); Art. 7(1) `identify, classify and adequately document` 3-verb + long AND chain of asset classes (ICT supported business functions + roles and responsibilities + information assets + ICT assets + their roles and dependencies in relation to ICT risk). The `actively keep up to date` training obligation for the management body (Art. 5(4), cross-ref 8.3.2) is the literacy underpinning of Art. 5(2) management-body responsibility and the personal-capacity threshold for Art. 5(2) to operate meaningfully. For smaller entities under Art. 4 proportionality, the framework is proportionate to the entity's risk exposure. The recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on Art. 6(1) ICT risk-management framework + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline. For a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities). For a DORA financial entity that is also a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR Art. 24(1) data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair. For a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair. For a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures). (Copied from the HSO Considerations block of `### 9.1.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=2 -->