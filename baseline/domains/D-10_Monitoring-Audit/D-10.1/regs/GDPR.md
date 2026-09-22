# D-10.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-030 + SO-GDPR-008 | Personal-data processing systems and services are monitored for adverse events covering the five Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), with a clear definition of the moment of "becoming aware of" a breach to anchor the Art. 33(1) 72-hour notification clock. | Entity-level monitoring of personal-data processing systems; 5-risk-type trigger (Art. 32(2) chapeau `a process for regularly testing, assessing and evaluating`); `becoming-aware` clock for breach notification. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | entity-level 5-risk-type detection (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data) + breach-`becoming-aware` clock for Art. 33(1) 72-hour notification | Art. 32(2) chapeau `the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services` + Art. 32(1)(d) `a process for regularly testing, assessing and evaluating` + Art. 33(1) `without undue delay and, where feasible, not later than 72 hours after having become aware of it` | entity (controller / processor) on personal-data processing systems | data subject + DPA — Art. 32(2) detection evidence + Art. 33(1) notification | Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2)(b)(c)(d) + Art. 33(1) `becoming aware` |

## Sub-SO (GDPR)

#### D-10.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-10.1.GDPR
subdomain: D-10.1
applies_to: [GDPR]
inherits_from: SO-GDPR-030 + SO-GDPR-008
source_SR: SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The controller and processor implement appropriate technical and organisational measures to ensure the **ongoing confidentiality, integrity, availability and resilience of processing systems and services** (Art. 32(1)(b) GDPR) and **regularly test, assess and evaluate their effectiveness** (Art. 32(1)(d) GDPR); personal-data processing systems and services are monitored for the five Art. 32(2) risk types, with a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock.

**CSF anchors (from `SR-GDPR-019` + `SR-GDPR-020` v0.3 security_rationale):**
DE.CM-01 (primary), DE.CM-09, DE.AE-02, ID.IM-04.
*(DE.CM-01 — Networks and network services are monitored to find potentially adverse events — anchors the GDPR Art. 32(2) 5-risk-type monitoring mapped to NIST CSF 2.0 DE.CM-01; DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored — anchors the personal-data processing systems monitoring per DomainAnalysis cross-validation; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the breach-`becoming-aware` clock per Art. 33(1); ID.IM-04 — Adequate resource capacity to ensure availability is maintained — anchors the Art. 32(1)(b) ongoing availability dimension. The four subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability burden, that the 5-risk-type monitoring was operational and that the breach-`becoming-aware` clock was correctly anchored for Art. 33(1) notification.)*

---


## Security Requirements (GDPR)

#### 10.1.1 — Entity-level 5 Art. 32(2) risk-type detection with breach-`becoming-aware` clock anchoring the Art. 33(1) 72-hour notification

```yaml
- req_id: 10.1.1
  volere_section: 15
  volere_subtype: audit

  title: "Controller and processor monitor personal-data processing systems for the 5 Art. 32(2) risk types, with breach-`becoming-aware` clock anchoring the Art. 33(1) 72-hour notification"

  derives_from:
    hso_sub_so: SO-10.1.GDPR
    per_reg_so: SO-GDPR-030 + SO-GDPR-008
    source_sr: SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.1.md
    objective_ref_section: "### 10.1.1"

  description: |
    The product shall implement appropriate technical and organisational measures to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (per GDPR Art. 32(1)(b)) and regularly test, assess and evaluate their effectiveness (per Art. 32(1)(d) `a process for regularly testing, assessing and evaluating`), with personal-data processing systems and services monitored for the 5 Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), and a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock `without undue delay and, where feasible, not later than 72 hours after having become aware of it`.

  fit_criterion: |
    Entity-level monitoring of personal-data processing systems is operational per Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) (SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — the controller demonstrates ex post that the 5-risk-type monitoring is operational on personal-data processing systems per DomainAnalysis cross-validation) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the personal-data processing systems monitoring dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the breach-`becoming-aware` clock per Art. 33(1) `the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of it, notify the personal data breach to the supervisory authority`) + ID.IM-04 (Adequate resource capacity to ensure availability is maintained — anchors the Art. 32(1)(b) ongoing availability dimension); the 5 Art. 32(2) risk types are: (i) accidental or unlawful destruction, (ii) loss, (iii) alteration, (iv) unauthorised disclosure of, (v) access to personal data; the breach-`becoming-aware` clock is operationalised with a clear definition of the moment of `becoming aware of` (per EDPB Guidelines 9/2022 on personal data breach notification under Regulation 2016/679 §3.2 — the controller has a high degree of certainty that a security incident has occurred that has led to personal data being compromised) and an audit trail that documents the moment-of-becoming-aware timestamp + the Art. 33(1) 72-hour notification timestamp; the recipient is the **data subject + DPA (supervisory authority)** on the Art. 32(2) detection evidence + Art. 33(1) notification; verified by DPA audit pack (5-risk-type monitoring evidence, breach-`becoming-aware` clock evidence, Art. 33(1) notification log, Art. 5(2) accountability burden evidence) + automated 5-risk-type coverage test (each of the 5 risk types is covered by the monitoring evidence) + automated breach-`becoming-aware` clock test (Art. 33(1) 72-hour notification triggered within 72h of moment-of-becoming-aware). **For DORA financial entities**, the **DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) continuous monitoring is broader (security AND functioning) than GDPR Art. 32(2) 5-risk-type detection; the DORA-led stack discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack (DORA-led stack for financial entities — cross to 10.1.4).

  priority: MUST
  verification_method: TEST
  dependencies: [10.1.2 (when controller = NSIE — GDPR detection capability + NIS 2 all-hazards detection capability on overlapping detection capability with different triggering frameworks — risk-type-triggered vs. incident-triggered; partial trigger alignment), 10.1.3 (when controller-manufacturer — **CRDA-flagged GENUINE TENSION**: CRA user opt-out vs. GDPR mandatory monitoring; the OJ does not resolve; Layer 2 OJ-level resolution required; the two regimes stack on the layered monitoring architecture — entity-layer mandatory + product-layer with opt-out), 10.1.4 (when DORA-controller — DORA Art. 8(1) / Art. 9(1) continuous monitoring is broader than GDPR Art. 32(2); DORA-led stack with GDPR detection as sub-component; for DORA financial entities, the DORA-led stack discharges the GDPR continuous-monitoring obligation), 10.1.5 (when provider/deployer = controller — GDPR pre-breach detection + AI Act lifecycle monitoring on different trigger alignment; pre-breach vs. lifecycle; the two regimes stack)]

  nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 32(2) + Art. 33(1)):**
> "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing, as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures … such as … (b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services; (c) the ability to restore the availability and access to personal data in a timely manner … (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures …" — Art. 32(1)+(2) GDPR

**GDPR article (verbatim, Art. 32(2) + Art. 33(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — risk-type-triggered vs. incident-triggered; partial trigger alignment); GDPR↔CRA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION** on CRA user opt-out vs. GDPR mandatory monitoring — Layer 2 OJ-level resolution required); GDPR↔DORA = COMPLEMENTARY (SAME — DORA broader than GDPR; DORA-led stack with GDPR detection as sub-component); GDPR↔AI_Act = COMPLEMENTARY (SAME — pre-breach detection vs. lifecycle; different trigger alignment))
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR↔NIS2 = Y (controller = NSIE; detection capability overlaps with different triggering frameworks); GDPR↔CRA = Y (CRDA-flagged GENUINE TENSION — controller-manufacturer; CRA user opt-out vs. GDPR mandatory monitoring; conflict requires Layer 2 OJ-level resolution); GDPR↔DORA = Y (DORA financial entity = controller; DORA-led stack with GDPR 5-risk-type as sub-component); GDPR↔AI_Act = Conditional (Y when high-risk AI processes personal data — provider is controller); HL engages when the GDPR sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR continuous-monitoring obligation at 10.1 is the **entity-level 5 Art. 32(2) risk-type detection** + **breach-`becoming-aware` clock** anchoring the Art. 33(1) 72-hour notification. Art. 32(1)(b) `the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services` + Art. 32(1)(d) `a process for regularly testing, assessing and evaluating` + Art. 32(2) 5-risk-type trigger `the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident` (chapeau) + Art. 33(1) `the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of it, notify the personal data breach to the supervisory authority` (per SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021). The 5 Art. 32(2) risk types: (i) accidental or unlawful destruction, (ii) loss, (iii) alteration, (iv) unauthorised disclosure of, (v) access to personal data. The `becoming aware` clock is operationalised per EDPB Guidelines 9/2022 §3.2 — the controller has a high degree of certainty that a security incident has occurred that has led to personal data being compromised; the `without undue delay and, where feasible, not later than 72 hours` is a dual qualifier — `without undue delay` is immediate, `where feasible, not later than 72 hours` is the soft ceiling; the 72-hour clock starts at the moment-of-becoming-aware and ends at the DPA notification. The recipient is the **data subject + DPA (supervisory authority)** on the Art. 32(2) detection evidence + Art. 33(1) notification. **For DORA financial entities**, the DORA Art. 8(1) / Art. 9(1) continuous monitoring is broader than GDPR Art. 32(2) 5-risk-type; the DORA-led stack discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack. **CRDA-flagged GENUINE TENSION with CRA**: CRA Annex I Part I (2)(l) user opt-out vs. GDPR Art. 32(2) mandatory monitoring — Layer 2 OJ-level resolution required.
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=2 -->