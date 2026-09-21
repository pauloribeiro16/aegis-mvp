# D-10.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-032 + SO-GDPR-009 | A process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures is established, with DPIA review on any change of the risk represented by processing operations (Art. 32(1)(d) + Art. 35(11) GDPR). | Entity-level effectiveness-evaluation of technical and organisational measures + DPIA review on risk change; cadence entity-discretionary under Art. 32(1)(d) `regularly testing`; Art. 35(11) `at least when there is a change of the risk` anchor. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | entity-level effectiveness-evaluation of technical and organisational measures + DPIA review on risk change | Art. 32(1)(d) `a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing` + Art. 35(11) `at least when there is a change of the risk represented by processing operations` | entity (controller / processor) on personal-data processing activities | data subject + DPA — Art. 32(1)(d) effectiveness-evaluation evidence + Art. 35(11) DPIA review | cadence entity-discretionary under Art. 32(1)(d) `regularly testing` + Art. 35(11) `at least when there is a change of the risk`; content not codified (entity-discretionary under Art. 24(1) chapeau) |

## Sub-SO (GDPR)

#### D-10.3.1 — Sub-SO for GDPR

```yaml
id: SO-D-10.3.GDPR
subdomain: D-10.3
applies_to: [GDPR]
inherits_from: SO-GDPR-032 + SO-GDPR-009
source_SR: SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The controller and processor implement appropriate technical and organisational measures including **a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing** (Art. 32(1)(d) GDPR); the DPIA is **reviewed at least when there is a change of the risk represented by processing operations** (Art. 35(11) GDPR).

**CSF anchors (from `SR-GDPR-019` + `SR-GDPR-021` + `SR-GDPR-022` v0.3 security_rationale):**
PR.IP-07 (primary), ID.RA-05, DE.AE-02, GV.OV-03.
*(PR.IP-07 — Configuration change control processes are in place — anchors the GDPR Art. 32(1)(d) `regularly testing, assessing and evaluating the effectiveness of technical and organisational measures` mapped to NIST CSF 2.0 PR.IP-07; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 35(11) DPIA review on risk change dimension; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-evaluation input to the incident-handling chain; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 35(11) DPIA review feedback loop into the risk-management strategy. The four subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability burden, that the Art. 32(1)(d) effectiveness-evaluation was operational with `regularly testing` cadence + Art. 35(11) DPIA review on risk change trigger.)*

---


## Security Requirements (GDPR)

#### 10.3.1 — Entity-level effectiveness-evaluation of security measures with `regularly testing` cadence + DPIA review on risk change

```yaml
- req_id: 10.3.1
  volere_section: 15
  volere_subtype: audit

  title: "Controller and processor establish a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures, with DPIA review at least when there is a change of the risk"

  derives_from:
    hso_sub_so: SO-D-10.3.GDPR
    per_reg_so: SO-GDPR-032 + SO-GDPR-009
    source_sr: SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/D-10.3.md
    objective_ref_section: "### D-10.3.1"

  description: |
    The product shall implement appropriate technical and organisational measures including a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing (per GDPR Art. 32(1)(d) `a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing`); the DPIA shall be reviewed at least when there is a change of the risk represented by processing operations (per Art. 35(11) `at least when there is a change of the risk represented by processing operations`).

  fit_criterion: |
    An effectiveness-evaluation process is established per Art. 32(1)(d) + Art. 35(11) (SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the GDPR Art. 32(1)(d) `regularly testing, assessing and evaluating the effectiveness of technical and organisational measures` mapped to NIST CSF 2.0 PR.IP-07) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 35(11) DPIA review on risk change dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-evaluation input to the incident-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 35(11) DPIA review feedback loop into the risk-management strategy); the Art. 32(1)(d) `regularly testing, assessing and evaluating` cadence is entity-discretionary under Art. 32(1)(d) `regularly` (DPO-discretionary); the Art. 35(11) DPIA review trigger is `at least when there is a change of the risk represented by processing operations` (event-triggered + minimum cadence on risk change); the Art. 32(1)(d) effectiveness-evaluation inputs feed the incident-handling chain (4.1) via DE.AE-02; the Art. 35(11) DPIA review feeds the risk-management strategy feedback loop (cross to 9.2) via GV.OV-03; the content of the effectiveness-evaluation is not codified (entity-discretionary under Art. 24(1) chapeau); the recipient is the **data subject + DPA (supervisory authority)** on the Art. 32(1)(d) effectiveness-evaluation evidence + Art. 35(11) DPIA review evidence; verified by DPA audit pack (effectiveness-evaluation cadence evidence + Art. 35(11) DPIA review on risk change evidence + Art. 5(2) accountability demonstrability burden + effectiveness-evaluation inputs to incident-handling chain + DPIA review feedback loop into risk-management strategy) + automated cadence test (regularly testing cadence operational + DPIA review trigger operational on risk change) + manual effectiveness-evaluation review (process for testing/assessing/evaluating is documented + executed + evidenced).

  priority: MUST
  verification_method: TEST
  dependencies: [10.3.2 (Y — when controller = NSIE; GDPR Art. 32(1)(d) effectiveness-evaluation of security measures + NIS 2 Art. 21(2)(f) effectiveness-assessment of risk-management measures; different scopes but same effectiveness objective; partial trigger alignment; entity-discretionary cadence alignment), 10.3.3 (Conditional — Y when controller deploys CRA-regulated products; GDPR Art. 32(1)(d) effectiveness-evaluation of security measures + CRA Annex I Part II (3) effective/regular tests of the product + Annex VIII modules; entity-level vs. product-level; different testing purposes stack without consolidation — **NO OJ-level consolidation rule for testing**), 10.3.4 (Conditional — Y when DORA financial entity is a controller; DORA-led stack with GDPR Art. 32(1)(d) effectiveness-evaluation as sub-component; DORA Art. 24(1) testing programme discharges the financial entity's testing obligation and the GDPR effectiveness-evaluation becomes a sub-component within the DORA-led stack), 10.3.5 (Conditional — Y when high-risk AI system processes personal data; GDPR Art. 32(1)(d) effectiveness-evaluation + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing + Art. 15(1) baseline testing; entity-level regular testing vs. AI-system-level testing; partial trigger alignment; the two regimes stack without consolidation)]

  nist_csf: [PR.IP-07, ID.RA-05, DE.AE-02, GV.OV-03]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 32(1)(d) + Art. 35(11)):**
> "[The controller and processor shall implement appropriate technical and organisational measures, such as … ] (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing." — Art. 32(1)(d) GDPR
> "[The controller shall carry out a review to assess whether the processing operations are performed in accordance with the data protection impact assessment] at least when there is a change of the risk represented by processing operations." — Art. 35(11) GDPR

**GDPR article (verbatim, Art. 32(1)(d) + Art. 35(11)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.3: GDPR↔NIS2 = COMPLEMENTARY (SAME — effectiveness-evaluation vs. risk-management-measure effectiveness-assessment; partial trigger alignment); GDPR↔CRA = COMPLEMENTARY (SAME — effectiveness-evaluation vs. conformity-assessment; different testing purposes); GDPR↔DORA = COMPLEMENTARY (SAME — DORA broader than GDPR; DORA-led stack with GDPR effectiveness-evaluation as sub-component); GDPR↔AI_Act = COMPLEMENTARY (SAME — entity-level regular testing vs. AI-system-level testing for risk management; partial trigger alignment))
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Y (controller = NSIE); GDPR↔CRA = Conditional (Y when controller deploys CRA-regulated products); GDPR↔DORA = Conditional (Y when DORA financial entity is controller); GDPR↔AI_Act = Conditional (Y when high-risk AI processes personal data); HL engages when the GDPR sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR compliance-testing obligation at D-10.3 is the **entity-level effectiveness-evaluation of technical and organisational measures** with `regularly testing` cadence + **DPIA review on risk change trigger** per Art. 32(1)(d) + Art. 35(11) (per SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022). Art. 32(1)(d) `a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing` — the 3-way verb AND `testing, assessing and evaluating`; the `regularly` cadence is entity-discretionary. Art. 35(11) `at least when there is a change of the risk represented by processing operations` — event-triggered DPIA review on risk change + minimum cadence on the trigger. The recipient is the **data subject + DPA** on the Art. 32(1)(d) effectiveness-evaluation evidence + Art. 35(11) DPIA review evidence. **NO OJ-level consolidation rule for testing** — the GDPR Art. 32(1)(d) effectiveness-evaluation is distinct from CRA Annex I Part II (3) effective/regular tests of the product (entity-level vs. product-level; different testing purposes); the AI Act Art. 9(6) testing for risk management is distinct from GDPR Art. 32(1)(d) effectiveness-evaluation (AI-system-level vs. entity-level); Phase 1 entities implement both regimes in parallel without OJ-level consolidation. **For DORA financial entities that are also controllers**, the DORA Art. 24(1) testing programme discharges the financial entity's testing obligation and the GDPR effectiveness-evaluation becomes a sub-component within the DORA-led stack. The Art. 32(1)(d) effectiveness-evaluation inputs feed the incident-handling chain (4.1) via DE.AE-02; the Art. 35(11) DPIA review feeds the risk-management strategy feedback loop (cross to 9.2) via GV.OV-03.
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=1 -->

