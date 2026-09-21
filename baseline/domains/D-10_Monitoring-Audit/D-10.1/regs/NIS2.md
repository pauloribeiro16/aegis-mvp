# D-10.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-005 (partial) | An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents, including those with significant impact on the provision of services (Art. 21(2)(b) — incident handling). | All-hazards detection capability as a partial-coverage dimension of the incident-handling obligation; no dedicated continuous-monitoring mandate; D-10.1 partial coverage. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | all-hazards detection capability as incident-handling dimension (partial coverage — no dedicated continuous-monitoring mandate) | Art. 21(2)(b) `incident handling` detection capability | entity (essential / important entity) on network and information systems | management body + competent authority (CSIRT) — Art. 21(2)(b) detection capability + incident-handling 6-action lifecycle per SR-NIS2-008 (prevent, detect, analyse, contain, respond, recover) | Art. 21(2)(b) + Art. 21(1) chapeau all-hazards + Art. 21(9) significant-incident notification chain (cross to D-04.3) |

## Sub-SO (NIS 2)

#### D-10.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-10.1.NIS2
subdomain: D-10.1
applies_to: [NIS2]
inherits_from: SO-NIS2-005
source_SR: SR-NIS2-009 + SR-NIS2-014
activation: if NIS2 in applicable_regs
phase_1A_role: 2_of_5
```

**Objective.** Essential and important entities establish an **incident-handling capability** covering prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) NIS 2); the detection dimension is the partial-coverage dimension of D-10.1, operating on an all-hazards basis and feeding the Art. 23(1) significant-incident notification chain.

**CSF anchors (from `SR-NIS2-009` + `SR-NIS2-014` v0.3 security_rationale):**
DE.CM-01 (primary), DE.CM-09, DE.AE-02, ID.IM-04.

---


## Security Requirements (NIS 2)

#### 10.1.2 — Entity-level all-hazards detection capability as incident-handling dimension with 6-action lifecycle (partial coverage)

```yaml
- req_id: 10.1.2
  volere_section: 15
  volere_subtype: audit

  title: "Essential and important entities establish an incident-handling capability with 6-action lifecycle (prevent, detect, analyse, contain, respond, recover) covering detection of all-hazards incidents"

  derives_from:
    hso_sub_so: SO-10.1.NIS2
    per_reg_so: SO-NIS2-005
    source_sr: SR-NIS2-009 + SR-NIS2-014
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.1.md
    objective_ref_section: "### 10.1.2"

  description: |
    The product shall establish an incident-handling capability covering prevention, detection, analysis, containment, response, and recovery of incidents (per NIS 2 Art. 21(2)(b) `incident handling`), including those with significant impact on the provision of services, with the detection dimension operating on an all-hazards basis and feeding the Art. 23(1) significant-incident notification chain; the Art. 21(2)(b) detection capability is the **partial-coverage dimension** of 10.1 — NIS 2 does not impose a dedicated continuous-monitoring mandate beyond the detection dimension of incident handling.

  fit_criterion: |
    An incident-handling capability is established per Art. 21(2)(b) `incident handling` (SR-NIS2-009 + SR-NIS2-014) with the 6-action lifecycle (prevent, detect, analyse, contain, respond, recover — per SR-NIS2-008) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the NIS 2 Art. 21(2)(b) incident-handling detection capability mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the all-hazards network and information systems monitoring per DomainAnalysis cross-validation) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 23(1) significant-incident detection trigger) + ID.IM-04 (Adequate resource capacity — anchors the prevention+detection+response feedback loop); the detection dimension operates on an all-hazards basis (all sources of ICT risk + cyber threats + ICT vulnerabilities — Art. 21(1) chapeau `Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems … which those entities use for their activities or the provision of their services, and to prevent or minimise the impact of incidents on the recipients of their services`); the all-hazards detection capability feeds the Art. 23(1) significant-incident notification chain (cross to 4.3 Regulatory Notification) when an incident has a significant impact on the continuity of essential services; the recipient is the **management body + competent authority (CSIRT — Computer Security Incident Response Team or national competent authority)** on the Art. 21(2)(b) detection capability + incident-handling 6-action lifecycle; verified by CSIRT audit pack (incident-handling 6-action lifecycle evidence, Art. 21(2)(b) all-hazards detection capability, Art. 23(1) significant-incident notification chain). **IMPORTANT — NIS 2 partial coverage at 10.1**: NIS 2 does NOT impose a dedicated continuous-monitoring mandate beyond the detection dimension of incident handling (Art. 21(2)(b)); the 10.1 coverage on the NIS 2 side is partial via the SO-NIS2-005 incident-handling detection capability. For DORA financial entities under DORA's direct scope, the **DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) continuous monitoring is the dominant authority** and discharges both DORA's dedicated monitoring obligation and NIS 2's Art. 21(2)(b) partial-coverage detection dimension for DORA financial entities that are also NSIEs — **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**; for non-financial NSIEs, NIS 2 Art. 21(2)(b) detection capability operates on the all-hazards basis without a dedicated continuous-monitoring mandate.

  priority: MUST
  verification_method: TEST
  dependencies: [10.1.1 (when controller = NSIE — GDPR detection capability + NIS 2 all-hazards detection capability on overlapping detection capability with different triggering frameworks — risk-type-triggered vs. incident-triggered; partial trigger alignment), 10.1.3 (when NSIE deploys CRA-regulated products — **CRDA-flagged GENUINE TENSION propagated**: CRA user opt-out vs. NIS 2 mandatory monitoring; the OJ does not resolve; Layer 2 OJ-level resolution required; the two regimes stack on the layered monitoring architecture — entity-layer mandatory + product-layer with opt-out), 10.1.4 (when DORA-NSIE — **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**; DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges both DORA's dedicated monitoring obligation and NIS 2's Art. 21(2)(b) partial-coverage detection dimension; for non-financial NSIEs, NIS 2 detection capability operates on the all-hazards basis without DORA), 10.1.5 (when NSIE deploys high-risk AI — NIS 2 entity-level operational monitoring + AI Act AI-system lifecycle monitoring; different trigger alignment; the two regimes stack without overlap)]

  nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(b) detection dimension):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (b) incident handling …" — Art. 21(2)(b) NIS 2 (per SR-NIS2-009)

**NIS2 article (verbatim, Art. 21(2)(b)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — risk-type-triggered vs. incident-triggered); NIS2↔CRA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION propagated** — CRA user opt-out vs. NIS 2 mandatory monitoring); NIS2↔DORA = EQUAL (SAME — both impose continuous-monitoring obligations; DORA-dominant for financial entities under DORA's direct scope); NIS2↔AI_Act = COMPLEMENTARY (SAME — entity-level operational vs. AI-system lifecycle; different trigger alignment))
```

### from regs/NIS2.md body

*(DE.CM-01 — Networks and network services are monitored to find potentially adverse events — anchors the NIS 2 Art. 21(2)(b) incident-handling detection capability mapped to NIST CSF 2.0 DE.CM-01; DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored — anchors the all-hazards network and information systems monitoring per DomainAnalysis cross-validation; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 23 significant-incident detection trigger; ID.IM-04 — Adequate resource capacity — anchors the prevention+detection+response feedback loop. The four subcategories together enable the NSIE to demonstrate ex post, against the competent authority (CSIRT), that the Art. 21(2)(b) detection capability was operational on the all-hazards basis and that the Art. 23(1) significant-incident notification was correctly triggered. For DORA financial entities, the DORA Art. 9(1) continuous monitoring discharges both obligations — DORA-dominant.)*

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # NIS2↔GDPR = Y (controller = NSIE; detection capability overlaps); NIS2↔CRA = Conditional (Y when NSIE deploys CRA-regulated products; **CRDA-flagged GENUINE TENSION propagated** — CRA user opt-out vs. NIS 2 mandatory monitoring); NIS2↔DORA = Y (DORA financial entity = NSIE; **EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**); NIS2↔AI_Act = Conditional (Y when NSIE deploys high-risk AI); HL engages when the NIS 2 sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 continuous-monitoring obligation at 10.1 is the **entity-level all-hazards detection capability** as incident-handling dimension per Art. 21(2)(b) — **partial coverage, no dedicated continuous-monitoring mandate**. The 6-action incident-handling lifecycle per SR-NIS2-008 (prevent, detect, analyse, contain, respond, recover) is the operational backbone; the detection dimension is the partial-coverage dimension of 10.1 on the NIS 2 side. Art. 21(2)(b) `incident handling` (per SR-NIS2-009) is the partial-coverage obligation; the all-hazards basis derives from Art. 21(1) chapeau `appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems`. The detection capability feeds the Art. 23(1) significant-incident notification chain (cross to 4.3 Regulatory Notification) when an incident has a significant impact on the continuity of essential services. The recipient is the **management body + competent authority (CSIRT or national competent authority)** on the Art. 21(2)(b) detection capability. **For DORA financial entities that are also NSIEs**, the **DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges both obligations** — DORA-dominant. **CRDA-flagged GENUINE TENSION with CRA (propagated)**: CRA user opt-out vs. NIS 2 mandatory monitoring — Layer 2 OJ-level resolution required.
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=2 -->

