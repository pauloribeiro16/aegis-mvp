# D-08.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-014 | Members of the management body actively keep up to date with sufficient knowledge and skills, including by following specific training on a regular basis, commensurate to the ICT risk being managed (Art. 5(4)). | Direct entity-side obligation; OJ-literal anchor on `sufficient knowledge and skills` + `regular basis` + `commensurate to the ICT risk`; the literacy underpinning of Art. 5(2) management-body responsibility. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | members of the management body of the financial entity (the OJ does not provide a designation carve-out; the definition of `management body` is determined by the company-law / sectoral governance architecture and the EBA Guidelines on Internal Governance fit-and-proper framework) | direct entity-side obligation — Art. 5(4) `shall actively keep up to date` is the direct entity-side trigger; the literacy underpinning of Art. 5(2) management-body responsibility (define+approve+oversee+be responsible); the clause co-exists with EBA Guidelines on Internal Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference) | `sufficient knowledge and skills` (S2 VAG on `sufficient` — chosen reading at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier) + `regular basis` (S2 VAG — chosen reading is risk-driven cadence per the literal `actively keep up to date` formulation) + `commensurate to the ICT risk being managed` (S2 VAG — chosen reading is risk-proportional rather than risk-quantified); no quantitative cadence; the OJ does not enumerate the content — entity-internal programme with evidence forms for `actively keep up to date` (training-attendance logs, assessment scores, peer-benchmark exercises) remaining for entity policy | management body (Art. 5(2) define+approve+oversee+be responsible) + NCA (national financial supervisory authority) — Art. 5(4) `actively keep up to date` records + Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance fit-and-proper framework + Art. 91 CRD + Art. 4(1)(36)/(37) MiFID II cross-reference | Art. 5(4) `Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` + Art. 5(2) management-body responsibility (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) + EBA Guidelines on Internal Governance fit-and-proper + CRD Art. 91 + MiFID II Art. 4(1)(36)/(37) |

## Sub-SO (DORA)

#### D-08.3.2 — Sub-SO for DORA

```yaml
id: SO-D-08.3.DORA
subdomain: D-08.3
applies_to: [DORA]
inherits_from: SO-DORA-014
source_SR: SR-DORA-024
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed (Art. 5(4) DORA).

**Considerations.**
- The clause is the literacy underpinning of Art. 5(2) management-body responsibility (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) and defines the personal-capacity threshold for Art. 5(2) to operate meaningfully (per SR-DORA-024 regulatory_rationale).
- The clause co-exists with EBA Guidelines on Internal Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4 proportionality, training evidence can be proportionate to risk exposure.
- The OJ-literal anchor is direct (Art. 5(4) is the entity-side obligation — `shall actively keep up to date`); the binding force is on the financial entity, not on a Member State.
- S2 VAG on `sufficient` is read at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier (per SR-DORA-024 ambiguity_notes).
- S2 VAG on `regular basis` is read as risk-driven cadence per the literal `actively keep up to date` formulation (alternatives include scheduled or ongoing).
- S2 VAG on `commensurate to the ICT risk` — the chosen reading is risk-proportional rather than risk-quantified.
- S2 POLY on `actively keep up to date` — alternatives include self-study, formal training, or both; the chosen reading is the literal AND.
- PR.AT-02 (All senior executives understand their roles and responsibilities in achieving the organization's cybersecurity objectives) anchors the training-and-knowledge component — the `sufficient knowledge and skills` OJ phrase operationalised as documented role-and-responsibility literacy, evidence of `actively keep up to date`, and training records calibrated to the ICT risk being managed.
- GV.RR-01 (Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture) layers the accountability-and-culture dimension — the management body's literacy is not decorative but tied to the personal-capacity prerequisite for the Art. 5(2) oversight-and-liability regime and to the broader fit-and-proper expectations under EBA Guidelines on Internal Governance, CRD Art. 91, and MiFID II Art. 4(1)(36)/(37).
- For a DORA financial entity that is not an NSIE (DORA only), only the DORA sub-SO activates and the management-body training is discharged against the Art. 5(4) direct entity-side obligation with the NCA-supervised evidence trail.
**CSF anchors (from `SR-DORA-024` v0.3 security_rationale):**
PR.AT-02, GV.RR-01.
*(PR.AT-02 anchors the training-and-knowledge component — the `sufficient knowledge and skills` OJ phrase operationalised as documented role-and-responsibility literacy, evidence of `actively keep up to date`, and training records calibrated to the ICT risk being managed. GV.RR-01 layers the accountability-and-culture dimension, ensuring that the management body's literacy is not decorative but tied to the personal-capacity prerequisite for the Art. 5(2) oversight-and-liability regime and to the broader fit-and-proper expectations under EBA Guidelines on Internal Governance, CRD Art. 91, and MiFID II Art. 4(1)(36)/(37). Together these two subcategories close the gap between training-attendance evidence and demonstrable governance competence, and an entity evidencing PR.AT-02 senior-executive literacy plus GV.RR-01 leadership accountability can demonstrate ex-post to supervisory review that the Art. 5(4) `sufficient knowledge and skills` obligation was met at personal-capacity level and that the management body was structurally positioned to discharge Art. 5(2) oversight responsibilities with informed judgement rather than ceremonial sign-off.)*

---


## Security Requirements (DORA)

#### 8.3.2 — Members of the management body of financial entities actively keep up to date with sufficient knowledge and skills, commensurate to the ICT risk being managed

```yaml
- req_id: 8.3.2
  volere_section: 15
  volere_subtype: immunity

  title: "Members of the management body of financial entities actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk, commensurate to the ICT risk being managed"

  derives_from:
    hso_sub_so: SO-8.3.DORA
    per_reg_so: SO-DORA-014
    source_sr: SR-DORA-024
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.3.md
    objective_ref_section: "### 8.3.2"

  description: |
    The product shall ensure that members of the management body of the financial entity actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed (per DORA Art. 5(4)), on the financial-entity workforce audience, with the literacy underpinning the Art. 5(2) management-body responsibility.

  fit_criterion: |
    Each member of the management body has documented evidence of `actively keep up to date` against the Art. 5(4) threshold — `sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` — with PR.AT-02 training-and-knowledge component (the `sufficient knowledge and skills` OJ phrase operationalised as documented role-and-responsibility literacy, evidence of `actively keep up to date`, and training records calibrated to the ICT risk being managed) + GV.RR-01 accountability-and-culture component (the management body's literacy tied to the personal-capacity prerequisite for the Art. 5(2) oversight-and-liability regime and to the broader fit-and-proper expectations under EBA Guidelines on Internal Governance + CRD Art. 91 + MiFID II Art. 4(1)(36)/(37)); the `sufficient` threshold is read at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier (S2 VAG, per SR-DORA-024 ambiguity_notes); the `regular basis` is read as risk-driven cadence per the literal `actively keep up to date` formulation (S2 VAG — risk-driven cadence rather than scheduled or ongoing); the `commensurate to the ICT risk` is read as risk-proportional rather than risk-quantified (S2 VAG — the OJ does not impose a numeric floor); the `actively keep up to date` is read as the literal AND of self-study, formal training, or both (S2 POLY — chosen reading: literal AND, per SR-DORA-024 ambiguity_notes); evidence forms (training-attendance logs, assessment scores, peer-benchmark exercises) are documented under entity policy and remain for entity policy (per SR-DORA-024 ambiguity_notes remain-open); the programme co-exists with EBA Guidelines on Internal Governance and the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4 proportionality, training evidence is proportionate to risk exposure; the programme is the literacy underpinning of the Art. 5(2) management-body responsibility (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) and the personal-capacity threshold for Art. 5(2) to operate meaningfully, per SR-DORA-024 regulatory_rationale; the programme couples with 8.3.1 on a DORA-dominant stack for a DORA financial entity that is also an NSIE (DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` direct entity-side obligation discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities, per CRDA-deep §8.3 NIS2↔DORA verified relationship — DORA-dominant); the programme couples with 8.1.4 (workforce-scale compulsory-modules substrate) and 8.2.4 (workforce-scale role-specific depth) without collapsing the governance-track / workforce-scale track distinction (per CRDA-deep §8.3 scope caveat on management-body training as governance-track counterpart — DORA Art. 5(4) = governance track; DORA Art. 13(6) = workforce-scale track); the programme is documented under Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance fit-and-proper framework; verified by management-body training programme documentation review + per-individual-member training-completion records + Art. 5(4) supervisory-evidence pack + NCA (national financial supervisory authority) review on request + EBA Guidelines on Internal Governance fit-and-proper assessment where applicable.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.1 (when DORA-NSIE — DORA Art. 5(4) `actively keep up to date` discharges NIS 2 Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities; DORA-dominant stack), 9.1.4 (Art. 5(2) management-body responsibility as governance hook on the ICT risk-management framework), 8.1.4 (workforce-scale compulsory-modules upstream substrate), 8.2.4 (workforce-scale role-specific depth dimension per `commensurate to the remit of their functions`)]

  nist_csf: [PR.AT-02, GV.RR-01]

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

**DORA article (verbatim, Art. 5(4)):**
> "Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed." — Art. 5(4) DORA (per SR-DORA-024)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: EQUAL (CRDA-deep, D-08.3: NIS2↔DORA = EQUAL (SAME — both regulations impose management-body training with the same operative target — senior-executive literacy + governance competence — and the same CSF substrate — PR.AT-02 + GV.RR-01; the EQUAL classification reflects this parallel; the dominant-authority reading is DORA-dominant for DORA financial entities; NIS 2 is dominant for non-financial NSIEs, per the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry))
```

### from regs/DORA.md body

- For an integrated controller-NSIE with both NIS 2 and DORA applicability on the management-body-training substrate, the DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite, per CRDA-deep §D-08.3 NIS2↔DORA verified relationship and downstream implication.

### from regs/DORA.md body

- **The CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy for entities deploying high-risk AI in ICT-risk contexts) is preserved as a structural Layer 2 review item; the HSO does NOT collapse the CRDA-unresolved interplay into a presumed reclassification.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔NIS2 = Y (when DORA financial entity is also an NSIE; DORA Art. 5(4) discharges both; DORA-dominant for financial entities); for DORA financial entity not an NSIE (DORA only), the sub-SO discharges the obligation standalone and the NIS 2 sub-SO is NOT activated; for NIS 2 NSIE not a financial entity (NIS 2 only), the sub-SO is NOT activated and the NIS 2 sub-SO discharges the obligation

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA management-body training obligation is the **literacy underpinning of the Art. 5(2) management-body responsibility** (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) and defines the personal-capacity threshold for Art. 5(2) to operate meaningfully, per SR-DORA-024 regulatory_rationale. The clause co-exists with EBA Guidelines on Internal Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4 proportionality, training evidence can be proportionate to risk exposure. The OJ-literal anchor is direct — Art. 5(4) is the entity-side obligation `shall actively keep up to date`; the binding force is on the financial entity, not on a Member State. The `sufficient` S2 VAG is read at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier (per SR-DORA-024 ambiguity_notes). The `regular basis` S2 VAG is read as risk-driven cadence per the literal `actively keep up to date` formulation (alternatives include scheduled or ongoing). The `commensurate to the ICT risk` S2 VAG — chosen reading is risk-proportional rather than risk-quantified. The `actively keep up to date` S2 POLY — alternatives include self-study, formal training, or both; chosen reading is the literal AND. PR.AT-02 anchors the training-and-knowledge component — `sufficient knowledge and skills` operationalised as documented role-and-responsibility literacy, evidence of `actively keep up to date`, and training records calibrated to the ICT risk being managed. GV.RR-01 layers the accountability-and-culture dimension — the management body's literacy tied to the personal-capacity prerequisite for the Art. 5(2) oversight-and-liability regime and to the broader fit-and-proper expectations under EBA Guidelines on Internal Governance, CRD Art. 91, and MiFID II Art. 4(1)(36)/(37). For a DORA financial entity that is also an NSIE with both NIS 2 and DORA applicability on the management-body-training substrate, the DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite, per CRDA-deep §8.3 NIS2↔DORA verified relationship (DORA-dominant for financial entities). For a DORA financial entity that is not an NSIE (DORA only), only the DORA sub-SO activates and the management-body training is discharged against the Art. 5(4) direct entity-side obligation with the NCA-supervised evidence trail. The **CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy for entities deploying high-risk AI in ICT-risk contexts) is preserved as a structural Layer 2 review item. (Copied from the HSO Considerations block of `### 8.3.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=2 -->