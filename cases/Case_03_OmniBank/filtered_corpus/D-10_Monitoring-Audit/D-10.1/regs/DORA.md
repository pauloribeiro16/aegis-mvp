# D-10.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SG-DORA-018 + SG-DORA-007 + SG-DORA-003 | ICT systems and tools are continuously monitored and controlled for security and functioning (Art. 8(1) per `DORA-C07` — OJ-literal locus Art. 9(1)) + anomalous activities promptly detected through multi-layered controls (Art. 10(1)+(2)) + ICT risk identified on a continuous basis (Art. 7(2)). | Financial-entity continuous monitoring + control of ICT-system security and functioning (CIA+A); prompt detection of anomalous activities; continuous ICT risk identification. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-level continuous monitoring of ICT-system security and functioning + prompt anomalous-activity detection + continuous ICT risk identification | Art. 8(1) `Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures` per `SR-DORA-030` (OJ-literal locus Art. 9(1)) + Art. 10(1) `promptly detect anomalous activities` + Art. 7(2) continuous ICT risk identification | entity (financial entity under DORA scope per Art. 2) | NCA + management body — Art. 8(1) continuous monitoring + Art. 10(1)+(2) multi-layered controls + EBA Guidelines supervisory baseline | Art. 8(1) per `SR-DORA-030` (OJ-literal locus Art. 9(1)) + Art. 10(1) + Art. 10(2) multiple layers + alert thresholds + auto-alert + Art. 7(2) continuous basis + yearly review + Art. 4 proportionality |

## Sub-SO (DORA)

#### D-10.1.4 — Sub-SO for DORA

```yaml
id: SG-D-10.1.DORA
subdomain: D-10.1
applies_to: [DORA]
inherits_from: SG-DORA-018 + SG-DORA-007 + SG-DORA-003
source_SR: SR-DORA-030 + SR-DORA-011 + SR-DORA-012 + SR-DORA-004
activation: if DORA in applicable_regs
phase_1A_role: 4_of_5
```

**Objective.** Financial entities **continuously monitor and control the security and functioning of ICT systems and tools** and **minimise the impact of ICT risk on ICT systems** (Art. 8(1) DORA per SR-DORA-030; OJ-literal locus Art. 9(1)); **anomalous activities are promptly detected** through multi-layered controls, alert thresholds, incident response triggers, and identification of single points of failure (Art. 10(1)+(2) DORA), with sources of ICT risk **identified on a continuous basis** and risk scenarios reviewed on a regular basis, at least yearly (Art. 7(2) DORA).

**CSF anchors (from `SR-DORA-030` + `SR-DORA-011` + `SR-DORA-012` + `SR-DORA-004` v0.3 security_rationale):**
DE.CM-01, DE.CM-09, PR.PS-04, DE.AE-02, RS.MA-01, ID.RA-01, ID.RA-03, PR.PS-02.

---


## Security Requirements (DORA)

#### 10.1.4 — Financial-entity continuous monitoring of ICT-system security and functioning + prompt anomalous-activity detection + continuous ICT risk identification (DORA-led stack)

```yaml
- req_id: 10.1.4
  volere_section: 15
  volere_subtype: audit

  title: "Financial entity continuously monitors and controls the security and functioning of ICT systems and tools, with prompt anomalous-activity detection through multi-layered controls and continuous ICT risk identification"

  derives_from:
    hso_sub_so: SO-10.1.DORA
    per_reg_so: SG-DORA-018 + SG-DORA-007 + SG-DORA-003
    source_sr: SR-DORA-030 + SR-DORA-011 + SR-DORA-012 + SR-DORA-004
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.1.md
    objective_ref_section: "### 10.1.4"

  description: |
    The product shall continuously monitor and control the security and functioning of ICT systems and tools and minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures (per DORA Art. 8(1) per SR-DORA-030; OJ-literal locus Art. 9(1) `continuously monitor and control the security and functioning of ICT systems and tools`), with anomalous activities promptly detected through multi-layered controls, alert thresholds, incident response triggers, and identification of single points of failure (per Art. 10(1) `promptly detect anomalous activities` + Art. 10(2) multiple layers + alert thresholds + auto-alert to relevant staff), and sources of ICT risk identified on a continuous basis and risk scenarios reviewed on a regular basis, at least yearly (per Art. 7(2)).

  fit_criterion: |
    Continuous monitoring of ICT systems and tools is operational per Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) `Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures` (SR-DORA-030) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the DORA Art. 8(1) `continuously monitor and control` mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the financial-entity ICT-systems monitoring per DomainAnalysis cross-validation) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 8(1) `tools, policies and procedures` 3-way AND) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 10(1) prompt anomalous-activity detection) + ID.RA-01 (Asset vulnerabilities are identified, validated, and recorded — anchors the Art. 7(2) continuous ICT risk identification + yearly review) + ID.RA-03 (Threats to assets are identified and recorded — anchors the Art. 7(2) `cyber threats and ICT vulnerabilities`); the Art. 10(1) + Art. 10(2) prompt anomalous-activity detection is operational through multi-layered controls (network layer + system layer + application layer + data layer), alert thresholds, identification of single points of failure, and auto-alert to relevant staff; the Art. 7(2) continuous ICT risk identification is operational on a continuous basis with risk scenarios reviewed on a regular basis, at least yearly; the recipient is the **NCA (national competent authority) + management body** on the Art. 8(1) continuous monitoring + Art. 10(1)+(2) multi-layered detection + Art. 7(2) continuous ICT risk identification; verified by NCA + EBA Guidelines supervisory baseline audit pack (continuous monitoring evidence, prompt anomalous-activity detection evidence with multi-layered controls, alert thresholds, identification of single points of failure, auto-alert evidence, Art. 7(2) continuous ICT risk identification evidence with yearly review documentation). **DORA-led stack for financial entities**: DORA Art. 8(1) continuous monitoring is broader (security AND functioning) than GDPR Art. 32(2) 5-risk-type detection. For DORA financial entities that are also controllers, the DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack. **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension**: both regulations impose continuous-monitoring obligations (NIS 2 Art. 21(2)(b) detection capability vs. DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) `continuously monitor and control`); for DORA financial entities that are also NSIEs, the DORA Art. 9(1) continuous monitoring discharges both obligations — DORA-dominant; for non-financial NSIEs, NIS 2 is the authority. The proportionality factors per Art. 4 `in relation to the size, nature, scale and complexity of the financial entity's activities` calibrate the depth of the continuous monitoring + multi-layered detection + continuous ICT risk identification. **CRDA-flagged GENUINE TENSION with CRA (propagated)**: CRA Annex I Part I (2)(l) user opt-out vs. DORA Art. 8(1) mandatory continuous monitoring — Layer 2 OJ-level resolution required.

  priority: MUST
  verification_method: TEST
  dependencies: [10.1.1 (when DORA-controller — DORA Art. 8(1) / Art. 9(1) continuous monitoring is broader than GDPR Art. 32(2); DORA-led stack with GDPR detection as sub-component), 10.1.2 (when DORA-NSIE — **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**; DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges both DORA's dedicated monitoring obligation and NIS 2's Art. 21(2)(b) partial-coverage detection dimension; for non-financial NSIEs, NIS 2 detection capability operates on the all-hazards basis without DORA), 10.1.3 (when DORA entity deploys CRA-regulated products — **CRDA-flagged GENUINE TENSION (propagated)**: CRA user opt-out vs. DORA mandatory monitoring; Layer 2 OJ-level resolution required), 10.1.5 (when DORA financial entity deploys high-risk AI — DORA continuous monitoring + AI Act post-market monitoring stack; DORA-led stack with AI Act as AI-system-level overlay)]

  nist_csf: [DE.CM-01, DE.CM-09, PR.PS-04]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 8(1) per SR-DORA-030; OJ-literal locus Art. 9(1) per the v0.2 audit):**
> "Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures." — DORA Art. 8(1) per SR-DORA-030 (OJ-literal locus Art. 9(1))


**DORA article (verbatim, Art. 9(1)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.1: GDPR↔DORA = COMPLEMENTARY (SAME — DORA broader than GDPR; DORA-led stack with GDPR detection as sub-component); NIS2↔DORA = EQUAL (SAME — both impose continuous-monitoring obligations; DORA-dominant for financial entities under DORA's direct scope); CRA↔DORA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION propagated** — CRA user opt-out vs. DORA mandatory monitoring); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA continuous monitoring + AI Act post-market monitoring stack for DORA financial entities deploying high-risk AI))
```

### from regs/DORA.md body

*(DE.CM-01 — Networks and network services are monitored to find potentially adverse events — anchors the DORA Art. 8(1) `continuously monitor and control` mapped to NIST CSF 2.0 DE.CM-01; DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored — anchors the financial-entity ICT-systems monitoring per DomainAnalysis cross-validation; PR.PS-04 — Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 8(1) `tools, policies and procedures` 3-way AND; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 10(1) prompt anomalous-activity detection; ID.RA-01 — Asset vulnerabilities are identified, validated, and recorded — anchors the Art. 7(2) continuous ICT risk identification + yearly review; ID.RA-03 — Threats to assets are identified and recorded — anchors the Art. 7(2) `cyber threats and ICT vulnerabilities`. The six subcategories together enable the financial entity to demonstrate ex post, against the NCA + EBA Guidelines supervisory baseline, that the Art. 8(1) continuous monitoring + Art. 10(1)+(2) multi-layered detection + Art. 7(2) continuous ICT risk identification were operational in light of the proportionality factors (size, nature, scale, complexity per Art. 4). For DORA financial entities that are also NIS 2 NSIEs, the DORA Art. 9(1) continuous monitoring discharges both obligations — DORA-dominant. For DORA financial entities that are also controllers, the GDPR Art. 32(2) 5-risk-type monitoring becomes a sub-component within the DORA-led stack. **CRDA-flagged GENUINE TENSION with CRA (propagated)**: CRA Annex I Part I (2)(l) user opt-out vs. DORA Art. 8(1) mandatory continuous monitoring — Layer 2 OJ-level resolution required.)*

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Y (DORA financial entity = controller; DORA-led stack with GDPR 5-risk-type as sub-component); DORA↔NIS2 = Y (DORA financial entity = NSIE; **EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**); DORA↔CRA = Conditional (Y when DORA entity deploys CRA-regulated products; **CRDA-flagged GENUINE TENSION propagated** — CRA user opt-out vs. DORA mandatory monitoring); DORA↔AI_Act = Y (DORA financial entity deploys high-risk AI; DORA continuous monitoring + AI Act post-market monitoring stack); HL engages when the DORA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA continuous-monitoring obligation at 10.1 is the **financial-entity continuous monitoring of ICT-system security and functioning** + **prompt anomalous-activity detection** + **continuous ICT risk identification** per Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) + Art. 10(1) + Art. 10(2) + Art. 7(2). Art. 8(1) `Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures` (per SR-DORA-030; OJ-literal locus Art. 9(1) per the SR clarification) — the `tools, policies and procedures` 3-way AND + the `continuously monitor and control` 2-verb AND + the `security and functioning` 2-AND are S2 VAG + POLY + COORD ambiguities. Art. 10(1) `promptly detect anomalous activities` (per SR-DORA-011) + Art. 10(2) multiple layers + alert thresholds + auto-alert to relevant staff (per SR-DORA-012). Art. 7(2) continuous ICT risk identification on a continuous basis + yearly review (per SR-DORA-004). The recipient is the **NCA + management body** on the Art. 8(1) continuous monitoring + Art. 10(1)+(2) multi-layered detection + Art. 7(2) continuous ICT risk identification. **DORA-led stack for financial entities** — for DORA financial entities that are also controllers, the DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack. **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension** — DORA-dominant for financial entities. **CRDA-flagged GENUINE TENSION with CRA (propagated)**: CRA user opt-out vs. DORA mandatory monitoring — Layer 2 OJ-level resolution required. Proportionality factors per Art. 4 `in relation to the size, nature, scale and complexity of the financial entity's activities` calibrate the depth.
```

### from regs/DORA.md body

**DORA article (verbatim, Art. 9(1)):**

> [as quoted in GDPR ↔ DORA above]

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=2 -->
