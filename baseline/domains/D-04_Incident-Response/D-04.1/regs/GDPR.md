# D-04.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-008 | Personal-data breach detection and triaging with documented "becoming aware" moment anchoring the 72h clock | Personal data; controller/processor; Art. 32(1)(b) + Art. 33(1) `becoming aware` + Art. 4(12) breach definition; PR.PS-04 + DE.AE-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data-flow boundary (controller-side, personal-data ingress/egress) | awareness of personal-data breach | `becoming aware` (Art. 33(1)) — document the trigger moment | supervisory authority (Art. 33 notification) | Art. 32(1)(b) + Art. 33(1) + Art. 4(12) |

## Sub-SO (GDPR)

#### D-04.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-04.1.GDPR
subdomain: D-04.1
applies_to: [GDPR]
inherits_from: SO-GDPR-008
source_SR: SR-GDPR-014
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal-data breaches are detected and triaged, and the moment of "becoming aware" is documented to anchor the 72-hour notification clock (Art. 33(1) + Art. 4(12) breach definition).

**Considerations.**
- The GDPR detection-and-triage obligation is the data-flow-boundary detection of the controller; the operational substrate is monitoring of the five Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), with a documented `becoming aware` moment that anchors the downstream Art. 33 notification. The awareness anchor is GDPR-unique among the four D-04.1 regulators and binds the notification pipeline in D-04.3.
- The downstream notification cascade (Art. 33 supervisory-authority notification + Art. 34 data-subject communication) is part of D-04.3, not D-04.1.

**CSF anchors (from `SR-GDPR-014` v0.3 security_rationale):**
DE.AE-02, PR.PS-04, DE.CM-01.
*(DE.AE-02 anchors the adverse-event analysis leg; PR.PS-04 anchors
the software-logs-recorded leg (relevant for the data-flow detection
evidence); DE.CM-01 anchors the networks-monitored leg for the
data-flow boundary.)*

---


## Security Requirements (GDPR)

#### 4.1.1 — Data-flow-boundary personal-data-breach detection with `becoming aware` documentation

```yaml
- req_id: 4.1.1
  volere_section: 15
  volere_subtype: audit

  title: "Personal-data breaches detected at the controller data-flow boundary with documented `becoming aware` moment anchoring the 72h clock"

  derives_from:
    hso_sub_so: SO-4.1.GDPR
    per_reg_so: SO-GDPR-008
    source_sr: SR-GDPR-014
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md
    objective_ref_section: "### 4.1.1"

  description: |
    The product shall detect personal-data breaches at the controller's data-flow boundary — covering the five Art. 4(12) breach types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed) — and shall document the moment of "becoming aware" by a controller employee with delegated breach-handling responsibility, with the awareness moment anchoring the Art. 33(1) 72-hour notification clock in 4.3 (GDPR Art. 32(1)(b) + Art. 33(1) `becoming aware` + Art. 4(12) breach definition).

  fit_criterion: |
    Continuous monitoring of the controller's data-flow boundary is operated covering the five Art. 4(12) breach types via DE.CM-01 networks-monitored leg (unauthorised disclosure / exfiltration vector) + DE.CM-09 host / runtime / data leg (alteration / access / loss vector) + PR.PS-04 log-records-generated leg; a designated breach-handling role receives validated incident reports under RS.MA-02 incident-reports-triaged; a documented `becoming aware` moment is timestamped at the moment the breach is captured by the controller's detection capability and recorded per EDPB Guidelines 9/2022 §3.4; the awareness moment anchors the Art. 33(1) 72h clock (4.3 cross-ref); the data-flow detection discipline operates at the controller boundary only, with the boundary hand-off to entity-level all-hazards monitoring (NIS 2 leg) and product-internal recording (CRA leg) documented as the controlled interfaces; verified by data-flow monitoring coverage audit + breach-detection log review + `becoming aware` timestamp records inspection + breach-handling role-designation documentation + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.2 (when controller is also NSIE — data-flow detection feeds entity detection), 4.1.3 (when integrated manufacturer-controller — CRA product-internal recording feeds data-flow awareness for personal-data subset)]

  nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, PR.PS-04, RS.MA-02]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim):**
> Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 33(1) creates the 72-hour clock from the moment of becoming aware; awareness requires detection capability. Art. 4(12) defines a personal data breach as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.1: GDPR↔NIS2 = COMPLEMENTARY; GDPR↔CRA = DIFFERENT-PERSPECTIVE; GDPR↔DORA = COMPLEMENTARY)
```

### from regs/GDPR.md body

- The data-flow detection object is distinct from the NIS 2 entity-level all-hazards detection, the CRA product-internal state-change recording, and the DORA anomalous-ICT-activity detection — the controller-facing data-flow boundary is the detection layer, and the awareness-anchoring discipline operates at that layer only.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-NSIE; data-flow detection feeds entity detection); GDPR↔CRA = Conditional (Y integrated manufacturer-controller; disjoint in baseline: data-flow ↔ product-internal); GDPR↔DORA = Conditional (Y DORA-controller; disjoint in baseline: data-flow ↔ financial-entity ICT); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR detection-and-triage obligation is the data-flow-boundary detection of the controller; the operational substrate is monitoring of the five Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), with a documented `becoming aware` moment that anchors the downstream Art. 33 notification. The awareness anchor is GDPR-unique among the four 4.1 regulators and binds the notification pipeline in 4.3. `Becoming aware` carries POLY-S3 (Berry §5.1 explicit ambiguous term); the chosen reading per SR-GDPR-014 is documented awareness by a controller employee with delegated breach-handling responsibility, the moment the breach is captured by the controller's detection capability — consistent with EDPB Guidelines 9/2022 §3.4. The data-flow detection object is distinct from the NIS 2 entity-level all-hazards detection, the CRA product-internal state-change recording, and the DORA anomalous-ICT-activity detection — the controller-facing data-flow boundary is the detection layer, and the awareness-anchoring discipline operates at that layer only. The downstream notification cascade (Art. 33 supervisory-authority notification + Art. 34 data-subject communication) is part of 4.3, not 4.1. (Copied from the HSO Considerations block of `### 4.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=2 -->