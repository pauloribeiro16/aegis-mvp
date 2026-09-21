# D-07.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-024 | Personal-data processing implements data-protection principles (data minimisation) in an effective manner at means-determination and processing time, integrating necessary safeguards (pseudonymisation, encryption, by-default limits) at state-of-the-art level (Art. 25(1)+(2)). | Privacy-by-design as controller obligation; minimisation/pseudonymisation/encryption as canonical by-design techniques; qualitative proportionality anchored in state-of-the-art + cost + nature/scope/context/purposes/risks. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data-protection properties via pseudonymisation + minimisation + by-default limits | controller's means-determination (Art. 25(1)) + processing time (Art. 25(1)) | `state of the art` + `cost of implementation` + `nature, scope, context and purposes of processing` + `risks of varying likelihood and severity` — 4-factor qualitative proportionality (no quantitative threshold) + Art. 25(2) by-default on amount/extent/period/access | supervisory authority (DPA) — Art. 5(2) accountability (documented necessity assessment, often via DPIA per Art. 35 — cross to D-09.2) | Art. 25(1) + Art. 25(2) + Art. 5(1)(f) + Art. 5(2) + Art. 24(1) + Art. 32(1)(a) + Art. 35(7) + Art. 4(5) pseudonymisation definition |

## Sub-SO (GDPR)

#### D-07.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-07.1.GDPR
subdomain: D-07.1
applies_to: [GDPR]
inherits_from: SO-GDPR-024
source_SR: SR-GDPR-039
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The controller implements appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing (Art. 25(1) GDPR), and ensures that by default only personal data which are necessary for each specific purpose are processed (Art. 25(2) GDPR).

**Considerations.**
- The design anchor is 4-factor qualitative proportionality: state of the art, cost of implementation, nature/scope/context/purposes of processing, and risks of varying likelihood and severity (Art. 25(1)).
- The by-default leg (Art. 25(2)) covers amount of data collected, extent of processing, period of storage, and accessibility — implies by-default minimal-data-collection pipelines, minimal-access, minimal-storage periods, and minimal-scope-of-processing.
- The by-design + by-default pair forms a 2-tier architecture: by-design is the architectural decision record; by-default is the operational implementation. Decisions are documented in a necessity assessment often via DPIA (Art. 35(7)) and demonstrated to the supervisory authority (DPA) under Art. 5(2) accountability.
- The pseudonymisation + minimisation + by-default triad propagates downstream to D-07.2 (Secure Coding Practices) as the code-level instruction and D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction.

**CSF anchors (from `SR-GDPR-039` v0.3 security_rationale):**
PR.PS-06, PR.DS-12.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the GDPR Art. 25(1) by-design at the time of means-determination + processing-time by-default forms the SDLC anchor on the controller side. PR.DS-12 anchors the data-management-consistent-with-risk-strategy dimension — data are managed consistent with the risk strategy; the GDPR Art. 25(1) `data-protection principles such as data minimisation` + Art. 25(2) by-default on amount/extent/period/access maps to PR.DS-12 directly. The two subcategories together enable the controller to demonstrate ex post, through documented Art. 25(1) by-design necessity assessment + Art. 25(2) by-default operational implementation + Art. 5(2) accountability record + Art. 30 RoPA on processing purposes and safeguards + Art. 35(7) DPIA content items, that the Art. 25(1)+(2) by-design + by-default duty has been exercised with the 4-factor qualitative proportionality calibration.)*

---


## Security Requirements (GDPR)

#### 7.1.1 — Controller-side data-protection by-design and by-default

```yaml
- req_id: 7.1.1
  volere_section: 15
  volere_subtype: integrity

  title: "Personal-data processing implements data-protection principles via appropriate technical and organisational measures designed into the means of processing, with by-default limits on amount, extent, storage period and accessibility"

  derives_from:
    hso_sub_so: SO-D-07.1.GDPR
    per_reg_so: SO-GDPR-024
    source_sr: SR-GDPR-039
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.1"

  description: |
    The product shall implement appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles (such as data minimisation) in an effective manner and to integrate the necessary safeguards into the processing at the time of means-determination and at the time of the processing itself, and shall ensure that by default only personal data which are necessary for each specific purpose are processed (GDPR Art. 25(1) + Art. 25(2)).

  fit_criterion: |
    A documented Art. 25(1) by-design necessity assessment is maintained for each processing activity, applying the 4-factor qualitative proportionality (state of the art + cost of implementation + nature/scope/context/purposes of processing + risks of varying likelihood and severity); the by-design decisions include pseudonymisation, minimisation, encryption, and by-default safeguards integrated at the time of means-determination; an Art. 25(2) by-default operational implementation is maintained covering the amount of personal data collected, the extent of processing, the period of storage, and the accessibility of the data — operationalised through minimal-data-collection pipelines, minimal-access, minimal-storage-periods, and minimal-scope-of-processing controls; the by-design and by-default pair forms a 2-tier architecture: by-design is the architectural decision record; by-default is the operational implementation; decisions are documented in a necessity assessment often via DPIA per Art. 35(7) and demonstrated to the DPA under Art. 5(2) accountability + Art. 30 RoPA on processing purposes and safeguards + Art. 24(1) responsibility of the controller; for an integrated manufacturer-controller-deployer, the controller-side GDPR Art. 25(1) by-design sits on top of the upstream CRA-side Annex I Part I product-cybersecurity by-design (the manufacturer has done CRA Art. 13(1) product by-design); the GDPR Art. 25(1) by-design outputs (pseudonymised-by-default pipelines, minimisation-by-default) are propagated downstream to D-07.2 (Secure Coding Practices) as the code-level instruction and D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction; verified by Art. 25(1) necessity-assessment records review + Art. 25(2) by-default operational-implementation evidence inspection + 4-factor proportionality calibration records review + Art. 30 RoPA entries + Art. 35(7) DPIA content items (when DPIA required) + Art. 5(2) accountability record + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.2 (when controller is also NSIE — GDPR by-design outputs realised through NIS 2 acquisition + development gates per SR-NIS2-026/027), 7.1.3 (when integrated manufacturer-controller — CRA Annex I Part I engineering substrate + GDPR Art. 25(1) personal-data overlay stack vertically), 7.1.4 (when DORA financial entity is also controller — GDPR overlay on DORA change-mgmt six-step + testing), 7.1.5 (when high-risk AI system processes personal data — Recital 78 preservation, GDPR by-design overlay on AI Act by-design + QMS)]

  nist_csf: [PR.PS-06, PR.DS-12]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 25(1)):**
> "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller shall … implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing in order to meet the requirements of this Regulation and protect the rights of data subjects." — Art. 25(1) GDPR


**GDPR article (verbatim, Art. 25(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-07.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — controller-NSIE stack, `what` data-protection by-design outputs realised through `that` NIS 2 acquisition gate + development gate); GDPR↔CRA = COMPLEMENTARY (SAME — controller-side personal-data by-design overlay on manufacturer-side product by-design, integrated-stack manufacturer-controller-deployer); GDPR↔DORA = COMPLEMENTARY (SAME — controller-side data-protection by-design overlay on financial-entity change-mgmt six-step + testing); GDPR↔AI_Act = COMPLEMENTARY (SAME — privacy-by-design overlay on AI-system-accuracy+robustness+cybersecurity + QMS, Recital 78 preservation))
```

### from regs/GDPR.md body

- For an integrated manufacturer-controller-deployer, CRA-side Annex I Part I product-cybersecurity by-design discharges the engineering substrate (the manufacturer has done CRA Art. 13(1) product by-design) while GDPR Art. 25(1) data-protection by-design discharges the personal-data overlay — the two stack vertically on the same product-lifecycle with distinct design outputs.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Y (controller-NSIE); GDPR↔CRA = Y (integrated manufacturer-controller-deployer); GDPR↔DORA = Conditional Y (financial-entity-controller combined stack); GDPR↔AI_Act = Y (provider/deployer-controller-processing-personal-data-via-AI); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR secure-by-design obligation is the controller-side data-protection by-design and by-default architecture; the operational substrate is the 4-factor qualitative proportionality (Art. 25(1)) + the by-default leg on amount/extent/period/access (Art. 25(2)). The by-design + by-default pair forms a 2-tier architecture: by-design is the architectural decision record; by-default is the operational implementation. Decisions are documented in a necessity assessment often via DPIA (Art. 35(7)) and demonstrated to the DPA under Art. 5(2) accountability. The data-protection properties designed into the means of processing are distinct from the CRA product-cybersecurity properties, the NIS 2 NIS-lifecycle-security properties, the DORA infrastructure-management properties, and the AI Act AI-system-accuracy+robustness+cybersecurity properties — the controller-facing data-protection overlay is the GDPR target object. The pseudonymisation + minimisation + by-default triad propagates downstream to D-07.2 (Secure Coding Practices) as the code-level instruction and D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction. (Copied from the HSO Considerations block of `### D-07.1.1`; preserved here for self-contained traceability.)
```

### from regs/GDPR.md body

**GDPR article (verbatim, Art. 25(1)):**

> [as quoted in GDPR ↔ NIS2 above]

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=2 -->

