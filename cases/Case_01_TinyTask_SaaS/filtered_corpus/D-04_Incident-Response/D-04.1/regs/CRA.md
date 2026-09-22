# D-04.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-020 + SO-CRA-068 | Recording and monitoring of product internal activity with user opt-out, corruption reporting | Product with digital elements; manufacturer perspective; Annex I Part I (2)(l); DE.CM-09 + PR.PS-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-internal state (intra-product state changes) | continuous recording and monitoring of relevant internal activity | continuous product monitoring with user opt-out where appropriate | CSIRT + ENISA (Art. 14(1)/(3) AEV/SI notification) | Annex I Part I (2)(l) |

## Sub-SO (CRA)

#### D-04.1.3 — Sub-SO for CRA

```yaml
id: SO-D-04.1.CRA
subdomain: D-04.1
applies_to: [CRA]
inherits_from: SO-CRA-020
source_SR: SR-CRA-027, SR-CRA-100
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported (Annex I Part I (2)(l)).

**Considerations.**
- The CRA detection-and-triage obligation is the product-internal state-change visibility; the operational substrate is an intra-product recording capability that captures state changes relevant to security, with a user-visible opt-out for events that are not security-critical. The recording-and-monitoring obligation is CRA-unique among the four D-04.1 regulators and provides the manufacturer's view inside the product boundary.
- The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification; Art. 14(1)/(3) AEV/SI notification) is part of D-04.3, not D-04.1.

**CSF anchors (from `SR-CRA-027` + `SR-CRA-100` v0.3 security_rationale):**
DE.CM-09, PR.PS-04, RS.MA-02.
*(DE.CM-09 anchors the computing-hardware-monitored leg (the
product-internal state-change visibility maps to hardware-level
monitoring per CSF 2.0); PR.PS-04 anchors the software-logs-recorded
leg (the Annex I (2)(l) recording obligation is the product-side
expression of this anchor); RS.MA-02 anchors the incident-management
executed leg for the corruption / unauthorised-modification reporting
pathway.)*

---


## Security Requirements (CRA)

#### 4.1.3 — Product-internal state-change recording with user opt-out

```yaml
- req_id: 4.1.3
  volere_section: 15
  volere_subtype: audit

  title: "Product-internal activity recorded and monitored with user opt-out where appropriate; corruption / unauthorised modification reported"

  derives_from:
    hso_sub_so: SO-4.1.CRA
    per_reg_so: SO-CRA-020
    source_sr: SR-CRA-027, SR-CRA-100
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md
    objective_ref_section: "### 4.1.3"

  description: |
    The product shall record and monitor relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — on a continuing basis throughout the support period under Art. 13(8), with a user-visible opt-out mechanism where appropriate for events that are not security-critical, and any corruption or unauthorised modification shall be reported to the user (CRA Annex I Part I (2)(l) + Part II (6) + Art. 13(8)).

  fit_criterion: |
    An intra-product recording capability is maintained on a continuing basis throughout the support period under Art. 13(8), capturing state changes relevant to security (access to or modification of data, services, or functions) via DE.CM-09 computing-hardware-monitored leg + PR.PS-04 software-logs-recorded leg + RS.MA-02 incident-reports-triaged leg; a user-visible opt-out mechanism operates where appropriate for events that are not security-critical (the opt-out is not a blanket opt-out of security-relevant events); corruption and unauthorised-modification events are reported to the user via the reporting mechanism under Annex I Part II (6); the recording-and-monitoring obligation is CRA-unique and provides the manufacturer's view inside the product boundary; the product-internal recording feeds the deployer's entity-level (NIS 2) and financial-entity (DORA) detection pipelines as a feed, not a substitute; the product-internal detection discipline operates at the product boundary only, with the boundary hand-off to data-flow detection (GDPR leg) and entity-level all-hazards monitoring (NIS 2 leg) documented as the controlled interfaces; verified by Annex I (2)(l) recording-coverage audit + Annex I Part II (6) reporting-mechanism inspection + user-opt-out mechanism review (events that are not security-critical) + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.2 (CRA product-internal recording feeds NIS 2 entity-level detection when NIS 2 entity deploys / manufactures CRA product), 4.1.4 (CRA product-internal recording feeds DORA financial-entity detection when DORA FE deploys CRA product)]

  nist_csf: [DE.CM-09, PR.PS-04, RS.MA-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim):**
> Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.1: GDPR↔CRA = DIFFERENT-PERSPECTIVE; NIS2↔CRA = COMPLEMENTARY; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/CRA.md body

- The product-internal detection object is distinct from the GDPR data-flow detection, the NIS 2 entity-level all-hazards detection, and the DORA anomalous-ICT-activity detection — the product boundary is internal to the product, and the intra-product recording discipline operates at that boundary only.

### from regs/CRA.md body

- The CRA product feeds detection signals into the deployer's entity-level (NIS 2) and financial-entity (DORA) detection pipelines via Annex I (2)(l); CRA detection does NOT substitute for entity-level detection (NIS 2 / DORA). For an integrated manufacturer-controller (manufacturer is also controller), the CRA product-internal recording feeds the GDPR `becoming aware` trigger for the personal-data subset; for a NIS 2 entity deploying CRA products, the Annex I (2)(l) recording feeds the NIS 2 entity-level detection.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; disjoint baseline: data-flow ↔ product-internal); CRA↔NIS2 = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint baseline: entity ↔ product); CRA↔DORA = Conditional (Y DORA FE deploys CRA product; disjoint baseline: product ↔ financial-entity ICT); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA detection-and-triage obligation is the product-internal state-change visibility; the operational substrate is an intra-product recording capability that captures state changes relevant to security, with a user-visible opt-out for events that are not security-critical. The recording-and-monitoring obligation is CRA-unique among the four 4.1 regulators and provides the manufacturer's view inside the product boundary. The product-internal detection object is distinct from the GDPR data-flow detection, the NIS 2 entity-level all-hazards detection, and the DORA anomalous-ICT-activity detection — the product boundary is internal to the product, and the intra-product recording discipline operates at that boundary only. The CRA product feeds detection signals into the deployer's entity-level (NIS 2) and financial-entity (DORA) detection pipelines via Annex I (2)(l); CRA detection does NOT substitute for entity-level detection (NIS 2 / DORA). For an integrated manufacturer-controller (manufacturer is also controller), the CRA product-internal recording feeds the GDPR `becoming aware` trigger for the personal-data subset; for a NIS 2 entity deploying CRA products, the Annex I (2)(l) recording feeds the NIS 2 entity-level detection. The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification; Art. 14(1)/(3) AEV/SI notification) is part of 4.3, not 4.1. (Copied from the HSO Considerations block of `### 4.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=2 -->