# D-10.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-006 | Policies and procedures are established to assess the effectiveness of cybersecurity risk-management measures, as part of the all-hazards risk-management framework (Art. 21(2)(f) NIS 2 per `SR-NIS2-037`/`SR-NIS2-038`). | Entity-level effectiveness-assessment of cybersecurity risk-management measures; cadence entity-discretionary under Recital 56; feeds the Art. 21(2)(a)–(j) risk-management cycle. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | entity-level effectiveness-assessment of cybersecurity risk-management measures | Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` | entity (essential / important entity) on network and information systems | management body + competent authority — Art. 21(2)(f) effectiveness-assessment outputs as part of all-hazards risk-management framework | cadence entity-discretionary under Recital 56 (no quantitative threshold); content not codified (policies-and-procedures POLY); feeds Art. 21(2)(a)–(j) risk-management cycle |

## Sub-SO (NIS 2)

#### D-10.3.2 — Sub-SO for NIS 2

```yaml
id: SO-D-10.3.NIS2
subdomain: D-10.3
applies_to: [NIS2]
inherits_from: SO-NIS2-006
source_SR: SR-NIS2-037 + SR-NIS2-038
activation: if NIS2 in applicable_regs
phase_1A_role: 2_of_5
```

**Objective.** Essential and important entities establish **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f) NIS 2) as part of the all-hazards risk-management framework; the cadence is entity-discretionary under Recital 56 (no quantitative threshold in the OJ).

**CSF anchors (from `SR-NIS2-037` + `SR-NIS2-038` v0.3 security_rationale):**
ID.IM-03 (primary), ID.RA-05, GV.OV-03, DE.AE-02.
*(ID.IM-03 — Configuration change control processes are in place — anchors the NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` mapped to NIST CSF 2.0 ID.IM-03; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the effectiveness-assessment feedback loop into the risk-management framework; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 21(2)(f) effectiveness-assessment feedback into the all-hazards risk-management strategy outcomes; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-assessment input to the incident-handling chain. The four subcategories together enable the NSIE to demonstrate ex post, against the competent authority (CSIRT), that the Art. 21(2)(f) effectiveness-assessment policies and procedures were operational with `policies and procedures to assess the effectiveness` cadence + methodology + evidence templates.)*

---


## Security Requirements (NIS 2)

#### 10.3.2 — Entity-level policies and procedures to assess effectiveness of cybersecurity risk-management measures (partial coverage)

```yaml
- req_id: 10.3.2
  volere_section: 15
  volere_subtype: audit

  title: "Essential and important entities establish policies and procedures to assess the effectiveness of cybersecurity risk-management measures as part of the all-hazards risk-management framework"

  derives_from:
    hso_sub_so: SO-D-10.3.NIS2
    per_reg_so: SO-NIS2-006
    source_sr: SR-NIS2-037 + SR-NIS2-038
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/D-10.3.md
    objective_ref_section: "### D-10.3.2"

  description: |
    The product shall establish policies and procedures to assess the effectiveness of cybersecurity risk-management measures (per NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures`) as part of the all-hazards risk-management framework; the cadence is entity-discretionary under Recital 56 (no quantitative threshold in the OJ).

  fit_criterion: |
    Effectiveness-assessment policies and procedures are established per Art. 21(2)(f) (SR-NIS2-037 + SR-NIS2-038) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the effectiveness-assessment feedback loop into the risk-management framework) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 21(2)(f) effectiveness-assessment feedback into the all-hazards risk-management strategy outcomes) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-assessment input to the incident-handling chain); the Art. 21(2)(f) cadence is entity-discretionary under Recital 56 (no quantitative threshold); the content is not codified (policies-and-procedures POLY); the policies and procedures feed the Art. 21(2)(a)–(j) risk-management cycle; the effectiveness-assessment inputs feed the incident-handling chain (4.1) via DE.AE-02; the recipient is the **management body + competent authority (CSIRT — Computer Security Incident Response Team or national competent authority)** on the Art. 21(2)(f) effectiveness-assessment outputs as part of the all-hazards risk-management framework; verified by CSIRT audit pack (policies and procedures content + cadence + effectiveness-assessment outputs + Art. 21(2)(a)–(j) risk-management cycle integration + incident-handling chain inputs) + automated policy-and-procedure test (policies exist in writing + procedures exist for execution + cadence operational + evidence templates defined) + manual effectiveness-assessment review (policies and procedures executed + evidenced + fed into risk-management cycle).

  priority: MUST
  verification_method: TEST
  dependencies: [10.3.1 (Y — when controller = NSIE; GDPR Art. 32(1)(d) effectiveness-evaluation of security measures + NIS 2 Art. 21(2)(f) effectiveness-assessment of risk-management measures; different scopes but same effectiveness objective; partial trigger alignment; entity-discretionary cadence alignment; the two regimes stack on the all-hazards risk-management framework + the Art. 32(1)(d) security measures), 10.3.3 (Conditional — Y when NSIE procures CRA-conformant products; NIS 2 Art. 21(2)(f) effectiveness-assessment + CRA Annex I Part II (3) effective/regular tests + Annex VIII modules; CRA conformity-assessment is a specific dimension of NIS 2 effectiveness-assessment; the two regimes stack on the entity-level + product-level), 10.3.4 (**EQUAL on testing-programme dimension, DORA-dominant for significant financial entities under Art. 26(1) TLPT**; for DORA significant financial entities, DORA Art. 24(1) testing programme discharges both DORA's dedicated testing obligation and NIS 2's Art. 21(2)(f) partial-coverage effectiveness-assessment; for non-financial NSIEs, NIS 2 is the authority; the EQUAL pair discharges both obligations on the DORA-led stack), 10.3.5 (Conditional — Y when NSIE deploys high-risk AI; NIS 2 Art. 21(2)(f) effectiveness-assessment + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing + Art. 15(1) baseline testing; AI Act adds real-world-conditions dimension; the two regimes stack without consolidation)]

  nist_csf: [ID.IM-03, ID.RA-05, GV.OV-03, DE.AE-02]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(f)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures." — Art. 21(2)(f) NIS 2 (per SR-NIS2-037/038)

**NIS2 article (verbatim, Art. 21(2)(f)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.3: GDPR↔NIS2 = COMPLEMENTARY (SAME — effectiveness-evaluation vs. risk-management-measure effectiveness-assessment); NIS2↔CRA = COMPLEMENTARY (SAME — effectiveness-assessment + conformity-assessment stack); NIS2↔DORA = EQUAL (SAME — both impose testing obligations; DORA-dominant for significant financial entities under Art. 26(1) TLPT); NIS2↔AI_Act = COMPLEMENTARY (SAME — effectiveness-assessment + AI Act real-world-conditions testing stack; AI Act adds real-world-conditions dimension))
```

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # NIS2↔GDPR = Y (controller = NSIE); NIS2↔CRA = Conditional (Y when NSIE procures CRA-conformant products); NIS2↔DORA = Y (DORA financial entity = NSIE; **EQUAL on testing-programme dimension, DORA-dominant for significant financial entities**); NIS2↔AI_Act = Conditional (Y when NSIE deploys high-risk AI); HL engages when the NIS 2 sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 compliance-testing obligation at D-10.3 is the **entity-level policies and procedures to assess effectiveness of cybersecurity risk-management measures** per Art. 21(2)(f) (per SR-NIS2-037 + SR-NIS2-038) — **partial coverage**. Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` — the `policies and procedures` POLY (entity-discretionary content) + the `effectiveness` anchor (effectiveness-assessment dimension); cadence entity-discretionary under Recital 56 (no quantitative threshold). The policies and procedures feed the Art. 21(2)(a)–(j) risk-management cycle. The effectiveness-assessment inputs feed the incident-handling chain (4.1) via DE.AE-02. The recipient is the **management body + competent authority (CSIRT or NCA)** on the Art. 21(2)(f) effectiveness-assessment outputs. **NIS 2 ↔ DORA EQUAL on testing-programme dimension** discharges both obligations on the DORA-led stack for significant financial entities (NIS 2 Art. 21(2)(f) is partial coverage); for DORA significant financial entities, the DORA Art. 24(1) testing programme discharges both obligations; for non-financial NSIEs, NIS 2 is the authority. The EQUAL classification preserves the OJ literal parallel between the two regimes on the testing-programme dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry. **NO OJ-level consolidation rule for testing** — even on the NIS 2 ↔ DORA EQUAL pair, the EQUAL classification discharges both obligations on the DORA-led stack without OJ-level consolidation with the other 3 regulators (GDPR / CRA / AI Act).
```

<!-- aegis:purity: own_reg=NIS2; demoted=3; core_cross_mentions=1 -->