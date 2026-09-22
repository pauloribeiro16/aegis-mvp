# D-08.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SG-DORA-015 | ICT security awareness programmes and digital operational resilience training as compulsory modules in staff training schemes, with complexity commensurate to the remit of staff functions (Art. 13(6)). | Entity-level compulsory training; awareness + digital operational resilience training combined. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity staff with `commensurate to the remit of their functions` complexity (workforce training across all staff functions) | financial entity establishes training schemes (Art. 13(6) `compulsory modules in their staff training schemes`) — continuous obligation | `compulsory` (Art. 13(6) — completion-mandatory per SR-DORA-025 ambiguity reading) + `commensurate to the remit of their functions` (function-specific calibration per the OJ literal) — qualitative + `level of complexity` qualitative; no quantitative cadence | competent authority (national financial supervisory authority) + management body — Art. 13(6) `compulsory modules` training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` + Art. 5(2) management-body responsibility + EBA Guidelines on ICT and security risk management |

## Sub-SO (DORA)

#### D-08.1.4 — Sub-SO for DORA

```yaml
id: SG-D-08.1.DORA
subdomain: D-08.1
applies_to: [DORA]
inherits_from: SG-DORA-015
source_SR: SR-DORA-025
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions (Art. 13(6) DORA).

**Considerations.**
- The Art. 13(6) workforce training duty is the workforce-scale counterpart to Art. 5(4) management-body training (governance track, mapped to D-08.3) and to the digital operational resilience testing duty at Chapter IV.
- The chosen reading of `compulsory` is completion-mandatory (not mere attendance) per SR-DORA-025 ambiguity_notes; the chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation.
- PR.AT-01 anchors the baseline awareness layer that closes the human-factor gap — phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes — and converts the OJ `ICT security awareness programmes` from an opt-in CPD activity into a compulsory training-module floor across the workforce.
- PR.AT-02 layers the role-specific depth dimension for staff in security-critical roles (incident response, ICT operations, fraud investigation, third-party governance) — distinct from the uniform baseline.
**CSF anchors (from `SR-DORA-025` v0.3 security_rationale):**
PR.AT-01, PR.AT-02.
*(PR.AT-01 anchors the baseline awareness layer that closes the human-factor gap — phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes — and converts the OJ `ICT security awareness programmes` from an opt-in continuing-professional-development activity into a compulsory training-module floor across the workforce. PR.AT-02 layers the role-specific depth dimension that the OJ `commensurate to the remit of their functions` qualifier demands, ensuring that staff in security-critical roles (incident response, ICT operations, fraud investigation, third-party governance) receive calibrated depth rather than a uniform baseline. Together these two subcategories operationalise both the `compulsory` and the `commensurate` axes of Art. 13(6), and an entity evidencing PR.AT-01 coverage plus PR.AT-02 role-calibrated depth can demonstrate ex-post to supervisory review that the Art. 13(6) workforce-training obligation was met at both the universal-awareness floor and the role-specific depth required by the staff function taxonomy, and that completion thresholds were documented as a condition of employment rather than as optional professional development.)*

---


## Security Requirements (DORA)

#### 8.1.4 — Financial-entity compulsory-modules-led ICT security awareness and resilience training

```yaml
- req_id: 8.1.4
  volere_section: 15
  volere_subtype: immunity

  title: "ICT security awareness programmes and digital operational resilience training as compulsory modules in financial-entity staff training schemes"

  derives_from:
    hso_sub_so: SO-8.1.DORA
    per_reg_so: SG-DORA-015
    source_sr: SR-DORA-025
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md
    objective_ref_section: "### 8.1.4"

  description: |
    The product shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in the financial-entity's staff training schemes (Art. 13(6) DORA), with a level of complexity commensurate to the remit of staff functions, on the financial-entity's workforce audience, with a digital-operational-resilience-testing-aligned syllabus and Art. 5(2) management-body oversight.

  fit_criterion: |
    A financial-entity compulsory-modules-led staff training scheme is operated covering PR.AT-01 baseline awareness (phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes, removable-media hygiene, disciplined use of administrative privileges) + PR.AT-02 role-specific depth calibrated to the remit of staff functions (incident response, ICT operations, fraud investigation, third-party governance — 8.2 layer 8.2.4); the training modules are `compulsory` (completion-mandatory per SR-DORA-025 ambiguity reading — not mere attendance); the level of complexity is calibrated to the remit of staff functions per the OJ-literal `commensurate to the remit of their functions` formulation (T4-vs-text gap: T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit` — the Executor keeps the OJ-literal locus per SR-DORA-025 ambiguity_notes); completion thresholds (completion percentages, assessment-pass thresholds) are documented as a condition of employment rather than as optional professional development; the DORA Art. 13(6) programme is co-existent with GDPR Art. 39 staff-awareness duties for personal-data processing and NIS 2 Art. 21(2)(g) basic security training baselines (EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration); the DORA Art. 13(6) programme is the carrier programme and the GDPR content is a sub-component for a DORA financial entity that is a controller processing personal data over its own staff (per CRDA-deep §8.1 GDPR↔DORA verified relationship); the DORA Art. 13(6) `compulsory modules` exceeds NIS 2 `basic cyber hygiene` and discharges the NIS 2 workforce-awareness obligation for DORA financial entities (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs); for DORA financial entities deploying high-risk AI, the DORA programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) 5-element + 4-element AND human-overseer competence is a sub-component (8.2 layer 8.2.4 + 8.2.5 — cross-ref); for DORA financial entities deploying/manufacturing CRA products, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator); Art. 5(2) management-body oversight is documented; verified by Art. 13(6) `compulsory modules` training-records inspection + completion-thresholds documentation + EBA Guidelines supervisory baseline review + Art. 5(2) management-body oversight records + national CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.1 (when DORA-controller — DORA Art. 13(6) is carrier; GDPR content is sub-component), 8.1.2 (DORA Art. 13(6) `compulsory modules` discharges NIS 2 `basic cyber hygiene` for DORA financial entities = NSIEs), 8.2.4 (role-specific `commensurate to the remit` depth), 8.2.5 (when DORA FE deploys high-risk AI — DORA carrier + AI Act 5-element sub-component)]

  nist_csf: [PR.AT-01, PR.AT-02]

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

**DORA article (verbatim, Art. 13(6)):**
> "Financial entities shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions." — Art. 13(6) DORA (per SR-DORA-025)

**DORA article (verbatim, Art. 13(6)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.1: GDPR↔DORA = COMPLEMENTARY (SAME — controller-side data-protection awareness overlay on financial-entity compulsory-modules-led programme; DORA programme as carrier + GDPR content as module); NIS2↔DORA = EQUAL (SAME — both regulations impose workforce awareness programmes at entity level; DORA-dominant for financial entities); CRA↔DORA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; end-user instructions vs internal staff training))
```

### from regs/DORA.md body

- The clause co-exists with GDPR Art. 39 staff-awareness duties for personal-data processing and with NIS 2 Art. 21(2)(g) first-clause basic security training baselines. EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration.

### from regs/DORA.md body

- For an integrated financial-entity-controller, the DORA programme is the carrier and the GDPR data-protection awareness is the module (per CRDA-deep §D-08.1 GDPR↔DORA verified relationship).

### from regs/DORA.md body

- For DORA financial entities that are also NSIEs, DORA-dominant for the workforce awareness dimension (Art. 13(6) `compulsory modules` is more prescriptive than NIS 2 Art. 21(2)(g) first clause `basic cyber hygiene` which is entity-discretionary under Recital 56 — per CRDA-deep §D-08.1 NIS2↔DORA EQUAL classification).

### from regs/DORA.md body

- For a DORA financial entity that is also a CRA manufacturer, the DORA workforce training is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — internal staff vs external end-user — no consolidation rule applies).


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Y (financial-entity-controller; DORA carrier + GDPR module); DORA↔NIS2 = Y (cross-sector; DORA-NSIE; DORA-dominant for financial entities); DORA↔CRA = N (typically) substantively scope-disjoint (internal staff vs B2B integrator); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA general-awareness obligation is the **financial-entity-side compulsory-modules-led workforce training programme** — Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions`. The chosen reading of `compulsory` is completion-mandatory (not mere attendance) per SR-DORA-025 ambiguity reading; the chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation. **T4-vs-text gap awareness:** T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit of their functions` — the Executor keeps the OJ-literal locus. PR.AT-01 anchors the baseline awareness layer that closes the human-factor gap (phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes) and converts the OJ `ICT security awareness programmes` from an opt-in continuing-professional-development activity into a compulsory training-module floor across the workforce. PR.AT-02 layers the role-specific depth dimension that the OJ `commensurate to the remit of their functions` qualifier demands (8.2 layer — 8.2.4), ensuring staff in security-critical roles receive calibrated depth rather than a uniform baseline. The DORA programme co-exists with GDPR Art. 39 staff-awareness duties for personal-data processing and with NIS 2 Art. 21(2)(g) basic security training baselines — EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration. For DORA financial entities that are controllers processing personal data over their own staff, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is a sub-component. The DORA `compulsory modules` exceeds NIS 2 `basic cyber hygiene` and discharges the NIS 2 obligation for DORA financial entities; for pure-financial NIS 2 §9 fall-back does not apply — DORA is lex specialis; for non-financial NSIEs, NIS 2 is the authority. For DORA financial entities deploying high-risk AI, the DORA programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) 5-element + 4-element AND competence is a sub-component (8.2 layer — 8.2.5 cross-ref). For DORA financial entities deploying/manufacturing CRA products, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences). The recipient is the competent authority (national financial supervisory authority) + management body — Art. 13(6) `compulsory modules` training records + Art. 5(2) management-body oversight + EBA Guidelines supervisory baseline. (Copied from the HSO Considerations block of `### 8.1.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=2 -->