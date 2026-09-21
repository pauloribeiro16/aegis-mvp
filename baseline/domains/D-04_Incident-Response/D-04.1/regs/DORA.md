# D-04.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-007 + SO-DORA-008 | Multi-class anomalous-activity detection with SPOF identification (Art. 10) + ICT-related incident management process (Art. 17(1)) | Financial-entity ICT; performance + incidents + SPOFs; DE.CM-01 + DE.CM-09 + RS.MA-01 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity ICT infrastructure | detection of anomalous ICT activity, performance issues, SPOFs meeting Art. 10 thresholds | multi-layer + alert thresholds + auto-alert to relevant staff + SPOF identification | competent authority + clients (Art. 19(1)+(3) notification) | Art. 10(1) + Art. 10(2); Art. 17(1) incident-management-process `detect/manage/notify` 3-way |

## Sub-SO (DORA)

#### D-04.1.4 — Sub-SO for DORA

```yaml
id: SO-D-04.1.DORA
subdomain: D-04.1
applies_to: [DORA]
inherits_from: SO-DORA-007
source_SR: SR-DORA-011, SR-DORA-012
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Anomalous activities — including ICT network performance issues and ICT-related incidents — are promptly detected through detection mechanisms that enable multiple layers of control, define alert thresholds and criteria, trigger and initiate ICT-related incident response processes, and identify potential material single points of failure (Art. 10(1) + Art. 10(2)). An ICT-related incident management process is defined, established and implemented to detect, manage and notify ICT-related incidents (Art. 17(1)).

**Considerations.**
- The DORA detection-and-triage obligation is the financial-entity ICT infrastructure detection with SPOF identification and threshold-driven escalation; the operational substrate is a multi-layer detection architecture with explicit alert thresholds, automatic escalation to relevant ICT-incident-response staff, and SPOF identification. The multi-layer + auto-alert + SPOF pattern is DORA-unique and the strictest detection-architecture floor in the AEGIS corpus.
- The downstream notification cascade (Art. 19(1) competent-authority + Art. 19(3) client notification) is part of D-04.3, not D-04.1.

**CSF anchors (from `SR-DORA-011` + `SR-DORA-012` v0.3 security_rationale):**
DE.CM-01, DE.CM-09, DE.AE-02, RS.MA-01.
*(DE.CM-01 anchors the networks-monitored leg; DE.CM-09 anchors the
computing-hardware-monitored leg (SPOF identification); DE.AE-02
anchors the adverse-event analysis leg for threshold-driven
escalation; RS.MA-01 anchors the incident-management-executed leg
from Art. 17(1) `detect/manage/notify` 3-way.)*

---


## Security Requirements (DORA)

#### 4.1.4 — Multi-class anomalous-activity detection with SPOF identification and threshold-driven escalation

```yaml
- req_id: 4.1.4
  volere_section: 15
  volere_subtype: audit

  title: "Multi-class anomalous-activity detection with SPOF identification, alert thresholds, automatic escalation, and Art. 17(1) `detect` leg of incident management process"

  derives_from:
    hso_sub_so: SO-4.1.DORA
    per_reg_so: SO-DORA-007
    source_sr: SR-DORA-011, SR-DORA-012
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md
    objective_ref_section: "### 4.1.4"

  description: |
    The product shall operate a financial-entity ICT infrastructure detection capability that promptly detects anomalous activities — including ICT network performance issues and ICT-related incidents — through detection mechanisms that enable multiple layers of control, define alert thresholds and criteria to trigger and initiate ICT-related incident response processes (including automatic alert mechanisms for relevant staff in charge of ICT-related incident response), and identify potential material single points of failure; an ICT-related incident management process shall be defined, established and implemented to detect, manage and notify ICT-related incidents (DORA Art. 10(1) + Art. 10(2) + Art. 17(1) `detect` leg).

  fit_criterion: |
    A multi-layer detection architecture is operated on the financial-entity ICT infrastructure with DE.CM-01 networks-monitored leg + DE.CM-09 computing-hardware-monitored leg (SPOF identification substrate) + DE.AE-02 adverse-event analysis leg for threshold-driven escalation; the architecture defines explicit alert thresholds and criteria (Art. 10(2)) and includes automatic alert mechanisms for relevant staff in charge of ICT-related incident response; an SPOF register (Art. 10(1) `identify potential material single points of failure`) is maintained and reviewed with material-SPOF remediation tracking; the Art. 17(1) ICT-related incident management process is defined, established and implemented, with the `detect` leg wired into the multi-layer detection architecture under RS.MA-01 incident-management-plan-executed; the DORA detection architecture is the operational source of GDPR awareness events (Art. 33(1) `becoming aware` — 4.3 cross-ref) when personal data are involved on the same party; for pure-financial entities, DORA absorbs the NIS 2 detection obligation for the ICT-hazard subset via lex specialis; the financial-entity detection discipline operates at the financial-entity boundary only, with the boundary hand-off to data-flow detection (GDPR leg) and entity-level all-hazards monitoring (NIS 2 leg) documented as the controlled interfaces; verified by multi-layer detection-architecture documentation audit + alert-threshold definitions review + auto-alert mechanism operational-test evidence + SPOF register audit + Art. 17(1) incident-management-process inspection + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.1 (when DORA financial entity is also controller — DORA detection architecture feeds GDPR `becoming aware` for personal-data subset), 4.1.2 (when DORA + NIS 2 cross-sector — DORA Art. 10 satisfies NIS 2 ICT-hazard detection; NIS 2 chapeau extends to physical + operational hazards)]

  nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, RS.MA-01, RS.MA-02, RS.MA-03]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim):**
> Art. 10(1) requires financial entities to have in place mechanisms to promptly detect anomalous activities, in accordance with Art. 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure. Art. 10(2) requires detection mechanisms to enable multiple layers of control, define alert thresholds and criteria to trigger and initiate ICT-related incident response processes, including automatic alert mechanisms for relevant staff in charge of ICT-related incident response.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.1: GDPR↔DORA = COMPLEMENTARY; NIS2↔DORA = DIFFERENT-PERSPECTIVE; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/DORA.md body

- The DORA detection object is distinct from the GDPR data-flow detection, the NIS 2 entity-level all-hazards detection, and the CRA product-internal state-change recording — the financial-entity infrastructure boundary is internal to the ICT estate, and the multi-layer detection discipline operates at that boundary only.

### from regs/DORA.md body

- A DORA Art. 10 detection event automatically feeds the GDPR Art. 33(1) `becoming aware` trigger when personal data are involved; the DORA detection architecture is the operational source of GDPR awareness events for the personal-data subset on the same party. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 detection obligation for the ICT-hazard subset; the high-level SO does not aggregate across the lex-specialis boundary in that direction.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-controller; disjoint baseline: data-flow ↔ financial-entity ICT); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial lex specialis — DORA Art. 10 satisfies NIS 2 ICT-hazard detection); DORA↔CRA = Conditional (Y DORA FE deploys CRA product; disjoint baseline: financial-entity ICT ↔ product); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA detection-and-triage obligation is the financial-entity ICT infrastructure detection with SPOF identification and threshold-driven escalation; the operational substrate is a multi-layer detection architecture with explicit alert thresholds, automatic escalation to relevant ICT-incident-response staff, and SPOF identification. The multi-layer + auto-alert + SPOF pattern is DORA-unique and the strictest detection-architecture floor in the AEGIS corpus. The DORA detection object is distinct from the GDPR data-flow detection, the NIS 2 entity-level all-hazards detection, and the CRA product-internal state-change recording — the financial-entity infrastructure boundary is internal to the ICT estate, and the multi-layer detection discipline operates at that boundary only. A DORA Art. 10 detection event automatically feeds the GDPR Art. 33(1) `becoming aware` trigger when personal data are involved; the DORA detection architecture is the operational source of GDPR awareness events for the personal-data subset on the same party. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 detection obligation for the ICT-hazard subset; the high-level SO does not aggregate across the lex-specialis boundary in that direction. The downstream notification cascade (Art. 19(1) competent-authority + Art. 19(3) client notification) is part of 4.3, not 4.1. (Copied from the HSO Considerations block of `### 4.1.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=2 -->

