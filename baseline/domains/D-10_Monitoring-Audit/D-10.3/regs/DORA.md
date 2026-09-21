# D-10.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-019 + SO-DORA-020 + SO-DORA-021 | Financial entities establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework; the testing programme uses a 12-way portfolio of testing methodologies; significant financial entities carry out advanced testing of their ICT systems using threat-led penetration testing on a regular basis (Art. 24(1) + Art. 25(1) + Art. 26(1) DORA per `SR-DORA-008`). | Financial-entity testing programme with 12-way testing modalities portfolio (Art. 25(1) enumerative list) + TLPT (Art. 26(1)) for significant entities; OJ-literal cadence `on a regular basis` for TLPT; programme is integral part of ICT risk-management framework. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-level digital operational resilience testing programme + 12-way testing modalities portfolio + TLPT for significant entities | Art. 24(1) `Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework` + Art. 25(1) 12-way testing modalities portfolio + Art. 26(1) `Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing` (TLPT) | entity (financial entity under DORA scope per Art. 2) | NCA — Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT reports | cadence Art. 24(1) `sound and comprehensive ... establish, maintain and review` (entity-discretionary under Art. 4 proportionality + programme-review cadence); Art. 26(1) TLPT `on a regular basis`; content partially codified for the Art. 25(1) 12-way enumerative list; TLPT per Regulatory Technical Standards under Art. 26(8) |

## Sub-SO (DORA)

#### D-10.3.4 — Sub-SO for DORA

```yaml
id: SO-D-10.3.DORA
subdomain: D-10.3
applies_to: [DORA]
inherits_from: SO-DORA-019 + SO-DORA-020 + SO-DORA-021
source_SR: SR-DORA-008 + SR-DORA-009 + SR-DORA-010
activation: if DORA in applicable_regs
phase_1A_role: 4_of_5
```

**Objective.** Financial entities **establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework** (Art. 24(1) DORA), using a 12-way portfolio of testing methodologies (Art. 25(1) DORA); **significant financial entities carry out advanced testing of their ICT systems using threat-led penetration testing (TLPT) on a regular basis** (Art. 26(1) DORA per the Regulatory Technical Standards under Art. 26(8)).

**CSF anchors (from `SR-DORA-008` + `SR-DORA-009` + `SR-DORA-010` v0.3 security_rationale):**
PR.IP-07 (primary), ID.RA-05, DE.AE-02, GV.OV-03, PR.PS-04.
*(PR.IP-07 — Configuration change control processes are in place — anchors the DORA Art. 24(1) `sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework` mapped to NIST CSF 2.0 PR.IP-07; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 25(1) 12-way modalities risk-input dimension; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 25(1) testing modalities input to the incident-handling chain; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 24(1) `establish, maintain and review` testing programme lifecycle feedback loop; PR.PS-04 — Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 25(1) testing modalities operational dimension + Art. 26(1) TLPT operational dimension. The five subcategories together enable the financial entity to demonstrate ex post, against the NCA + EBA Guidelines supervisory baseline, that the Art. 24(1) `sound and comprehensive` testing programme + Art. 25(1) 12-way modalities portfolio + Art. 26(1) TLPT for significant entities were operational on the financial-entity ICT systems with `on a regular basis` TLPT cadence + appropriate proportionality calibration per Art. 4.)*

---


## Security Requirements (DORA)

#### 10.3.4 — Financial-entity digital operational resilience testing programme + 12-way modalities + TLPT for significant entities

```yaml
- req_id: 10.3.4
  volere_section: 15
  volere_subtype: audit

  title: "Financial entity establishes, maintains and reviews a sound and comprehensive digital operational resilience testing programme with a 12-way testing modalities portfolio and TLPT for significant entities on a regular basis"

  derives_from:
    hso_sub_so: SO-D-10.3.DORA
    per_reg_so: SO-DORA-019 + SO-DORA-020 + SO-DORA-021
    source_sr: SR-DORA-008 + SR-DORA-009 + SR-DORA-010
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/D-10.3.md
    objective_ref_section: "### D-10.3.4"

  description: |
    The product shall establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework (per DORA Art. 24(1) `Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`), using a 12-way portfolio of testing methodologies (per Art. 25(1)); significant financial entities shall carry out advanced testing of their ICT systems using threat-led penetration testing (TLPT) on a regular basis (per Art. 26(1) `Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing`) per the Regulatory Technical Standards under Art. 26(8).

  fit_criterion: |
    A digital operational resilience testing programme is established, maintained, and reviewed per Art. 24(1) + Art. 25(1) + Art. 26(1) (SR-DORA-008 + SR-DORA-009 + SR-DORA-010) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the DORA Art. 24(1) `sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework` mapped to NIST CSF 2.0 PR.IP-07) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 25(1) 12-way modalities risk-input dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 25(1) testing modalities input to the incident-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 24(1) `establish, maintain and review` testing programme lifecycle feedback loop) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 25(1) testing modalities operational dimension + Art. 26(1) TLPT operational dimension); the Art. 24(1) `sound and comprehensive` testing programme is established, maintained, and reviewed as an integral part of the ICT risk-management framework; the Art. 25(1) 12-way testing modalities portfolio is operational (the 12-way enumerative list per Art. 25(1)); the Art. 26(1) TLPT for significant entities is operational `on a regular basis` per the Regulatory Technical Standards under Art. 26(8); the programme is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity); the recipient is the **NCA (national competent authority)** on the Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT reports; verified by NCA audit pack (Art. 24(1) testing programme content + Art. 25(1) 12-way modalities coverage + Art. 26(1) TLPT reports for significant entities + Art. 4 proportionality calibration + programme review cadence + EBA Guidelines supervisory baseline) + automated testing-programme test (programme exists in writing + programme is integral part of ICT risk-management framework + 12-way modalities coverage + TLPT cadence for significant entities) + manual programme-review review (programme established, maintained, reviewed + TLPT executed + evidenced + cadence operational + proportionality calibrated).

  priority: MUST
  verification_method: TEST
  dependencies: [10.3.1 (Conditional — Y when DORA financial entity is a controller; **DORA-led stack** with GDPR Art. 32(1)(d) effectiveness-evaluation as sub-component; DORA Art. 24(1) testing programme discharges the financial entity's testing obligation and the GDPR effectiveness-evaluation becomes a sub-component within the DORA-led stack), 10.3.2 (**EQUAL on testing-programme dimension, DORA-dominant for significant financial entities under Art. 26(1) TLPT**; for DORA significant financial entities, DORA Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT discharges both DORA's dedicated testing obligation and NIS 2's Art. 21(2)(f) partial-coverage effectiveness-assessment; for non-financial NSIEs, NIS 2 is the authority; the EQUAL pair discharges both obligations on the DORA-led stack), 10.3.3 (Conditional — Y when DORA entity procures CRA-conformant products; DORA Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT + CRA Annex VII §6 test reports + Annex VIII modules; product-level upstream vs. entity-level downstream; the two regimes stack without consolidation), 10.3.5 (Y — when DORA financial entity deploys high-risk AI; DORA Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) baseline testing `throughout their lifecycle`; the two regimes stack without consolidation)]

  nist_csf: [PR.IP-07, ID.RA-05, DE.AE-02, GV.OV-03, PR.PS-04]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 24 + Art. 25 + Art. 26):**
> "Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework." — Art. 24(1) DORA (per SR-DORA-008)
> "The testing programme shall provide for the use of appropriate testing methodologies, including vulnerability assessments and scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires and scanning software solutions, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing." — Art. 25(1) DORA (per SR-DORA-008)
> "Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing." — Art. 26(1) DORA (TLPT)

**DORA article (verbatim, Art. 24 + Art. 26):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.3: GDPR↔DORA = COMPLEMENTARY (SAME — DORA broader than GDPR; DORA-led stack with GDPR effectiveness-evaluation as sub-component); NIS2↔DORA = EQUAL (SAME — both impose testing obligations; DORA-dominant for significant financial entities under Art. 26(1) TLPT); CRA↔DORA = COMPLEMENTARY (SAME — product-level conformity-assessment + entity-level testing programme stack; CRA upstream, DORA downstream); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA testing programme + TLPT + AI Act real-world-conditions testing stack for DORA financial entities deploying high-risk AI))
```

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Conditional (Y when DORA financial entity is controller; DORA-led stack with GDPR effectiveness-evaluation as sub-component); DORA↔NIS2 = Y (DORA financial entity = NSIE; **EQUAL on testing-programme dimension, DORA-dominant for significant financial entities**); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant products); DORA↔AI_Act = Y (DORA financial entity deploys high-risk AI); HL engages when the DORA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA compliance-testing obligation at D-10.3 is the **financial-entity digital operational resilience testing programme** + **12-way testing modalities portfolio** + **TLPT for significant entities** per Art. 24(1) + Art. 25(1) + Art. 26(1) (per SR-DORA-008 + SR-DORA-009 + SR-DORA-010). Art. 24(1) `Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework` — the `sound and comprehensive` 2-way AND + the `establish, maintain and review` 3-way verb AND (programme lifecycle); the programme is an integral part of the ICT risk-management framework. Art. 25(1) 12-way testing modalities portfolio — the enumerative list (12 modalities) per Art. 25(1). Art. 26(1) `Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing` — TLPT for significant entities with `on a regular basis` cadence; TLPT per the Regulatory Technical Standards under Art. 26(8). The programme is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity). The recipient is the **NCA** on the Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT reports. **NIS 2 ↔ DORA EQUAL on testing-programme dimension** — both impose testing obligations; for DORA significant financial entities that are also NSIEs, the DORA Art. 24(1) testing programme discharges both obligations; for non-financial NSIEs, NIS 2 is the authority; the EQUAL classification preserves the OJ literal parallel between the two regimes on the testing-programme dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry; **NIS 2 Art. 21(2)(f) is partial coverage** — the NIS 2 testing programme dimension is not codified as a dedicated programme; the EQUAL relationship discharges NIS 2's effectiveness-assessment policy into the DORA-led testing programme for financial entities. **DORA-led stack for financial entities** — DORA Art. 24(1) testing programme is broader (digital operational resilience + 12-way modalities + TLPT) than GDPR Art. 32(1)(d) effectiveness-evaluation or NIS 2 Art. 21(2)(f) effectiveness-assessment; for DORA financial entities that are also controllers, the DORA Art. 24(1) testing programme discharges the financial entity's testing obligation and the GDPR effectiveness-evaluation becomes a sub-component within the DORA-led stack.
```

<!-- aegis:purity: own_reg=DORA; demoted=3; core_cross_mentions=1 -->

