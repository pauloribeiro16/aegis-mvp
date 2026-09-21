# D-09.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-028 + SO-GDPR-036 + SO-GDPR-037 (cross-ref) | DPIA covering the four Art. 35(7) content items (systematic description, necessity & proportionality, risks, mitigation); reviewed on change of risk per Art. 35(11); joint-controller arrangement per Art. 26 (cross to D-06.3); DPO designation per Art. 37-39 cross-referenced from D-09.1. | Personal-data-rights impact; pre-launch for high-risk processing; reviewed on risk change. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data-subject rights and freedoms (risks to rights-and-freedoms dimension) — pre-launch DPIA on high-risk personal-data processing | high-risk-processing event (Art. 35(1) `likely to result in a high risk to the rights and freedoms of natural persons`) | 4-item Art. 35(7) closed list: (a) systematic description of the envisaged processing operations and the purposes of the processing, including where applicable the legitimate interest pursued by the controller; (b) assessment of the necessity and proportionality of the processing operations in relation to the purposes; (c) assessment of the risks to the rights and freedoms of data subjects; (d) measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation | pre-launch + on-change review per Art. 35(11) `review … where there has been a change of the risk represented by processing operations` | supervisory authority (DPA) — Art. 35(7) DPIA content + Art. 35(11) review records + Art. 36(1) prior consultation where residual risk is high (cross to D-04.3) + Art. 5(2) accountability burden + Art. 26(1) joint-controller arrangement (cross to D-06.3) | Art. 35(1) + Art. 35(4) (DPA consultation triggers) + Art. 35(7) 4-item content + Art. 35(11) review cadence + Art. 36(1) prior consultation + Art. 4(7) (controller/joint controllers) + Art. 26(1) joint-controller arrangement + Art. 5(2) accountability + Art. 24(1) appropriate measures |

## Sub-SO (GDPR)

#### D-09.2.1 — Sub-SO for GDPR

```yaml
id: SO-D-09.2.GDPR
subdomain: D-09.2
applies_to: [GDPR]
inherits_from: SO-GDPR-028 + SO-GDPR-036 + SO-GDPR-037 (cross-ref from D-09.1)
source_SR: SR-GDPR-045 + SR-GDPR-046 + SR-GDPR-047
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a **data-protection impact assessment** covering the four Art. 35(7) content items and reviewed on change of risk per Art. 35(11) (Art. 35(1) + Art. 35(7) GDPR).

**CSF anchors (from `SR-GDPR-045` + `SR-GDPR-046` + `SR-GDPR-047` v0.3 security_rationale):**
ID.RA-05 (primary), ID.RA-04.

---


## Security Requirements (GDPR)

#### 9.2.1 — Controller-side pre-launch DPIA on data-subject rights with 4-item Art. 35(7) content and Art. 35(11) on-change review

```yaml
- req_id: 9.2.1
  volere_section: 15
  volere_subtype: integrity

  title: "Controller carries out a pre-launch DPIA covering the four Art. 35(7) content items before high-risk personal-data processing, reviewed on change of risk per Art. 35(11) and submitted for prior consultation where residual risk is high"

  derives_from:
    hso_sub_so: SO-9.2.GDPR
    per_reg_so: SO-GDPR-028 + SO-GDPR-036 + SO-GDPR-037
    source_sr: SR-GDPR-045 + SR-GDPR-046 + SR-GDPR-047
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.1"

  description: |
    The product shall ensure that, prior to processing likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a data-protection impact assessment (DPIA) covering the four Art. 35(7) content items (systematic description of envisaged processing + necessity-and-proportionality assessment + risks to rights and freedoms + measures envisaged to address the risks), reviewed on change of risk per Art. 35(11), and submitted for prior consultation under Art. 36(1) where residual risk remains high.

  fit_criterion: |
    A pre-launch DPIA is documented and maintained under Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` (SR-GDPR-045) covering the 4-item Art. 35(7) content list (SR-GDPR-046) with ID.RA-04 impact-and-likelihood dimension (Art. 35(7)(c) `assessment of the risks to the rights and freedoms of data subjects` + Art. 35(7)(d) `measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation`) + ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 35(7)(c) impact on data-subject rights and freedoms under Art. 5(1) principles); the DPIA identifies whether the processing falls within Art. 35(3)(a)-(d) mandatory-DPIA cases (systematic + extensive evaluation + large-scale special-category / systematic monitoring on large scale / innovative use of new technologies / automated decision-making with legal/similar effect) or the DPA-published Art. 35(4) blacklist; the DPIA is reviewed on change of risk per Art. 35(11) `review … where there has been a change of the risk represented by processing operations`, with material-change-of-risk trigger supplemented by a documented periodic-review cadence; the DPIA is submitted for prior consultation under Art. 36(1) where the residual risk remains high, with the controller documenting the consultation outcome in the accountability records under Art. 5(2); the DPIA is one of the records to be retained per Art. 5(2) accountability burden and is made available on request to the supervisory authority (DPA) with the DPIA content demonstrable against the 4-item Art. 35(7) list; the Art. 26 joint-controller arrangement is reflected in the DPIA with the joint-controller roles allocated per Art. 26(1) (cross to D-06.3); the Art. 35(11) review records identify the trigger event, the date, the assessment of the change, the residual-risk recalculation, and any updated measures; the controller can demonstrate Art. 5(2) accountability for the DPIA process with continuity of evidence (DPIA + reviews + prior-consultation records preserved on a continuing basis, EDPB Guidelines on accountability 07/2019); the DPIA coordinates with the DPO per Art. 39(1)(c) advice obligation (cross to 9.1 GDPR sub-SO DPO anchor); **CRDA flag — GDPR DPIA does NOT address cybersecurity risk** (DomainAnalysis §9.2 line 175): the DPIA's risk object is data-subject rights and freedoms; the CRA Art. 13(3) cybersecurity risk assessment or the NIS 2 Art. 21(2)(a) risk-analysis policy or the DORA Art. 7(2) ICT risk framework discharges the cybersecurity-risk-assessment obligation on a **separate artefact** — the DPIA is stacked, not collapsed with the cybersecurity assessments.

  priority: MUST
  verification_method: TEST
  dependencies: [9.2.3 (when controller-manufacturer — DPIA on data-subject rights + CRA risk-assessment on product cybersecurity risk; DIFFERENT-PERSPECTIVE, distinct artefacts, no OJ-level consolidation), 9.2.4 (when DORA-controller — DPIA pre-launch + DORA continuous + yearly; DIFFERENT-PERSPECTIVE, distinct artefacts), 9.2.5 (when AI-system processes personal data — DPIA pre-launch + AI Act Art. 9 continuous iterative; DIFFERENT-PERSPECTIVE; AI Act Recital 78 explicit GDPR preservation), 9.2.2 (when controller-NSIE — DPIA pre-launch on-change + NIS 2 continuous operational; DIFFERENT-PERSPECTIVE, conditional-Y scope overlap when DPIA conducted for NSIE's processing)]

  nist_csf: [ID.RA-04, ID.RA-05]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> "Where a type of processing is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data …" — Art. 35(1) GDPR
> "The assessment shall contain at least: (a) a systematic description of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller; (b) an assessment of the necessity and proportionality of the processing operations in relation to the purposes; (c) an assessment of the risks to the rights and freedoms of data subjects; (d) the measures envisaged to address the risks …" — Art. 35(7) GDPR

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-09.2: GDPR↔NIS2 = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA on data-subject rights vs continuous operational risk-analysis on entity operational risk; Conditional-Y scope overlap when DPIA conducted for NSIE's processing); GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA on data-subject rights vs pre-market + support-period cybersecurity risk assessment on product cybersecurity risk; **no OJ-level consolidation rule** even when CRA risk assessment performed); GDPR↔DORA = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA vs continuous + at-least-yearly DORA risk framework; **no OJ-level consolidation**); GDPR↔AI_Act = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA vs continuous iterative AI Act Art. 9 risk management; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation**))
```

### from regs/GDPR.md body

*(ID.RA-05 — Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response — anchors the convergent D-09.2 assessment regime across the 5 regulators per DomainAnalysis §D-09.2 line 180 cross-validation; ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — anchors the DPIA-specific impact-and-likelihood dimension per DomainAnalysis §D-09.2 line 180 cross-validation. The DPIA object — risks to data-subject rights and freedoms — is captured by Art. 35(7)(c) `assessment of the risks to the rights and freedoms of data subjects`; the impact dimension is captured by Art. 35(7)(d) `measures envisaged to address the risks`. The two subcategories together enable the controller to demonstrate ex post, against the Art. 5(2) accountability burden, that the DPIA was carried out prior to processing with the 4-item Art. 35(7) content, reviewed on change of risk per Art. 35(11), and was submitted for prior consultation where the residual risk is high per Art. 36(1). **GDPR DPIA does NOT address cybersecurity risk** — for the cybersecurity dimension, the CRA Art. 13(2) risk assessment (Annex VII §3 risk-assessment record) or the NIS 2 Art. 21(2)(a) risk-analysis policy discharges the cybersecurity-risk-assessment obligation on a separate artefact.)*

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y when DPIA conducted for NSIE's processing; N otherwise — pre-launch vs continuous); GDPR↔CRA = Y (CRA-regulated product processes personal data; **no OJ-level consolidation rule** — GDPR DPIA must be a separate artefact even when CRA risk assessment performed; object differs — rights-and-freedoms vs cybersecurity); GDPR↔DORA = Y (DORA financial entity is controller; **no OJ-level consolidation** — DPIA pre-launch vs DORA continuous + yearly); GDPR↔AI_Act = Y (high-risk AI processes personal data; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation** — DPIA pre-launch vs AI Act continuous iterative); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR impact-and-risk-assessment obligation at 9.2 is the **pre-launch DPIA on data-subject rights** under Art. 35(1) + Art. 35(7) 4-item content + Art. 35(11) on-change review cadence. The Art. 35(3)(a)-(d) mandatory-DPIA cases and the Art. 35(4) DPA-published blacklist form the **triggering test**. Art. 35(7) 4-item content: (a) systematic description of the envisaged processing operations + purposes including legitimate interest; (b) assessment of necessity and proportionality; (c) assessment of risks to data-subject rights and freedoms; (d) measures envisaged to address the risks — the 4-item codification is the **full content template** (vs. NIS 2's entity-discretionary content under Recital 56). Art. 35(11) carries S2 VAG on `change of the risk represented by processing operations` — chosen reading: material-change-of-risk trigger supplemented by a documented periodic-review cadence. **CRDA flag — GDPR DPIA does NOT address cybersecurity risk** (DomainAnalysis §9.2 line 175): the DPIA's risk object is data-subject rights and freedoms under Art. 5(1); the CRA cybersecurity risk assessment, NIS 2 risk-analysis policy, DORA ICT risk framework, and AI Act Art. 9 risk-management system all operate on different objects — for a CRA-regulated product processing personal data, the GDPR DPIA must be a separate artefact even when the CRA cybersecurity risk assessment has been performed; the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) preserve this structural pre-launch DPIA vs operational-continuous asymmetry without OJ-level consolidation. Art. 36(1) prior consultation is the cross-to-4.3 layer where residual risk is high. Joint-controller arrangements per Art. 26 (cross to D-06.3) are reflected in the DPIA content. The recipient is the **DPA (supervisory authority)** on Art. 35(7) DPIA content + Art. 35(11) review records + Art. 36(1) prior-consultation records + Art. 5(2) accountability burden. The DPIA coordinates with the DPO per Art. 39(1)(c) advice obligation (cross to 9.1 GDPR sub-SO DPO anchor). For a controller-NSIE (vertically-integrated entity subject to both GDPR + NIS 2), the GDPR DPIA + NIS 2 risk-analysis policy stack without OJ-level consolidation; for a controller-manufacturer (GDPR + CRA), the GDPR DPIA + CRA cybersecurity risk assessment stack without OJ-level consolidation.
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=2 -->

