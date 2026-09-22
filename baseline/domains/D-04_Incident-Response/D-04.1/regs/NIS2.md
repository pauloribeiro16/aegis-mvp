# D-04.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-005 | Six-action incident-handling capability (prevent, detect, analyse, contain, respond, recover) per Art. 21(2)(b) + Art. 6(8) definition | Entity-level ICT systems; all-hazards approach (Art. 21(2) chapeau); PR.PS-04 + DE.CM-01 + DE.AE-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | entity boundary (entity ICT systems, all-hazards) | detection of adverse event affecting service continuity | `appropriate and proportionate` (Art. 21(1)); all-hazards coverage (Art. 21(2) chapeau + Recital 56) | CSIRT or competent authority (Art. 23(4) notification) | Art. 21(2)(b) + Art. 6(8) (six-action `detect` phase) |

## Sub-SO (NIS 2)

#### D-04.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-04.1.NIS2
subdomain: D-04.1
applies_to: [NIS2]
inherits_from: SO-NIS2-005
source_SR: SR-NIS2-008, SR-NIS2-009
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) + Art. 6(8) six-action `incident handling` definition), with the detection dimension operationalised as all-hazards entity-level monitoring that surfaces adverse events affecting service continuity (Art. 21(2) chapeau + Recital 56).

**Considerations.**
- The NIS 2 detection-and-triage obligation is the entity-level all-hazards detection; the operational substrate is an entity-wide monitoring capability covering cybersecurity, operational, and physical-environment hazards (Recital 56 all-hazards approach), with the `detect` action as one of the six Art. 6(8) incident-handling actions. The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the detection depth: high-risk roles and systems trigger deeper detection coverage than low-risk ones.
- The downstream notification cascade (Art. 23(4) 24h early warning + 72h incident notification + 1m final report) is part of D-04.3, not D-04.1.

**CSF anchors (from `SR-NIS2-008` + `SR-NIS2-009` v0.3 security_rationale):**
RS.MA-01, RS.AN-03, DE.CM-01, DE.CM-09.
*(DE.CM-01 anchors the networks-monitored leg (entity-level
monitoring is the NIS 2 detection backbone); DE.AE-02 anchors the
adverse-event analysis leg (the detection-triage threshold); PR.PS-04
anchors the software-logs-recorded leg for the entity-level
detection evidence.)*

---


## Security Requirements (NIS 2)

#### 4.1.2 — Entity-level all-hazards detection with the six-action `detect` leg

```yaml
- req_id: 4.1.2
  volere_section: 15
  volere_subtype: audit

  title: "Entity-level all-hazards detection operating the Art. 6(8) six-action `detect` leg of incident handling"

  derives_from:
    hso_sub_so: SO-4.1.NIS2
    per_reg_so: SO-NIS2-005
    source_sr: SR-NIS2-008, SR-NIS2-009
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md
    objective_ref_section: "### 4.1.2"

  description: |
    The product shall operate entity-level all-hazards monitoring covering cybersecurity, operational, and physical-environment hazards affecting network and information systems (per Art. 21(2) chapeau + Recital 56), with the `detect` action as one of the six Art. 6(8) `incident handling` actions (prevent, detect, analyse, contain, respond, recover) under Art. 21(2)(b), and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the detection depth with high-risk roles and systems triggering deeper detection coverage than low-risk ones (NIS 2 Art. 21(2)(b) + Art. 6(8) six-action definition + Art. 21(2) chapeau all-hazards + Recital 56).

  fit_criterion: |
    An entity-wide monitoring capability is operated covering cybersecurity + operational + physical-environment hazards via DE.CM-01 networks-monitored leg (entity-level network telemetry, flow analytics, north-south and east-west monitoring) + DE.CM-09 host / runtime / data leg (endpoint telemetry, process-level behavioural signals, runtime-environment integrity monitoring) + DE.AE-02 adverse-event analysis leg (detection-triage threshold); the `detect` action of the six Art. 6(8) incident-handling actions is documented in the entity-level incident-response procedure (RS.MA-01 incident-management-plan-executed) with explicit coordination discipline with CSIRT, competent authority, single point of contact and sectoral peers; the detection capability produces the awareness event on which the Art. 23(4)(a) 24-hour clock trigger (4.3 cross-ref) is built; risk-tiered detection depth (high-risk roles / systems trigger deeper coverage) is documented per the Art. 21(1) `appropriate and proportionate` qualifier; the entity-level detection discipline operates at the entity boundary only, with the boundary hand-off to data-flow detection (GDPR leg), product-internal recording (CRA leg) and financial-entity multi-layer detection (DORA leg) documented as the controlled interfaces; verified by entity-level monitoring coverage audit + risk-tier mapping review + six-action incident-handling procedure inspection + adverse-event analysis records review + CSIRT / competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.3 (when NIS 2 entity deploys / manufactures CRA product — CRA product-internal recording feeds entity-level detection), 4.1.4 (when DORA + NIS 2 cross-sector — DORA Art. 10 satisfies NIS 2 detection for ICT-hazard subset; NIS 2 chapeau extends to physical + operational hazards)]

  nist_csf: [RS.MA-01, RS.AN-03]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process anchored in the Article 21(2) all-hazards approach.

**NIS2 article (verbatim):**
> Article 21(2) chapeau introduces the all-hazards approach, which requires the detection capability to cover cybersecurity, operational, and physical-environment hazards affecting network and information systems (Recital 56). Article 21(2)(b) requires the detection dimension of incident handling.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.1: GDPR↔NIS2 = COMPLEMENTARY; NIS2↔CRA = COMPLEMENTARY; NIS2↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/NIS2.md body

- The entity-level detection object is distinct from the GDPR data-flow detection, the CRA product-internal state-change recording, and the DORA anomalous-ICT-activity detection — the entity boundary is internal, and the all-hazards detection discipline operates at that boundary only.

### from regs/NIS2.md body

- A DORA Art. 10 detection event satisfies the NIS 2 detection obligation for the ICT-hazard subset, but the entity must extend detection to physical and operational hazards per the NIS 2 chapeau; a CRA product's Annex I (2)(l) recording feeds detection signals into the NIS 2 entity-level pipeline.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y controller-NSIE); NIS2↔CRA = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint baseline: entity ↔ product); NIS2↔DORA = Conditional (Y cross-sector; N pure-financial via lex specialis — DORA Art. 10 satisfies NIS 2 ICT-hazard subset; NIS 2 chapeau extends to physical + operational hazards); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 detection-and-triage obligation is the entity-level all-hazards detection; the operational substrate is an entity-wide monitoring capability covering cybersecurity, operational, and physical-environment hazards (Recital 56 all-hazards approach), with the `detect` action as one of the six Art. 6(8) incident-handling actions. The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the detection depth. A DORA Art. 10 detection event satisfies the NIS 2 detection obligation for the ICT-hazard subset, but the entity must extend detection to physical and operational hazards per the NIS 2 chapeau; a CRA product's Annex I (2)(l) recording feeds detection signals into the NIS 2 entity-level pipeline. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 detection obligation for the ICT-hazard subset; the high-level SO does not aggregate across the lex-specialis boundary in that direction for the ICT-hazard scope, but does aggregate for the physical/operational hazards where NIS 2 still binds. The software-compliance track the cybersecurity and operational dimensions are in scope; the physical-environment dimension is captured by SR-NIS2-041 (out-of-scope flag for software-compliance). The downstream notification cascade (Art. 23(4) 24h early warning + 72h incident notification + 1m final report) is part of 4.3, not 4.1. (Copied from the HSO Considerations block of `### 4.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=2 -->
