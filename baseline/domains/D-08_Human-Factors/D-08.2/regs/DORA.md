# D-08.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-015 (partial via Art. 13(6) `commensurate to the remit`) | Compulsory training with complexity commensurate to the remit of staff functions. T4-vs-text gap: T4 reads `role-specific training` but OJ text says `commensurate to the remit`. | Entity-level role-specific training; OJ-literal locus preserved. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity staff with function-specific complexity `commensurate to the remit of their functions` (workforce with function-specific depth) | financial entity establishes training schemes (Art. 13(6) `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions`) — continuous obligation | `compulsory` (Art. 13(6) — completion-mandatory per SR-DORA-025 ambiguity reading) + `commensurate to the remit of their functions` (function-specific calibration per the OJ literal — T4-vs-text gap: T4 reads `role-specific training` while the OJ Art. 13(6) uses only `commensurate to the remit of their functions`) — qualitative + `level of complexity` qualitative; no quantitative cadence | competent authority (national financial supervisory authority) + management body — Art. 13(6) `commensurate to the remit` training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 13(6) `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` + Art. 5(2) management-body responsibility + EBA Guidelines on ICT and security risk management |

## Sub-SO (DORA)

#### D-08.2.4 — Sub-SO for DORA

```yaml
id: SO-D-08.2.DORA
subdomain: D-08.2
applies_to: [DORA]
inherits_from: SO-DORA-015 (partial via Art. 13(6) `commensurate to the remit`)
source_SR: SR-DORA-025
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions (Art. 13(6) DORA).

**Considerations.**
- The role-specific layer of the Art. 13(6) workforce training duty is anchored on `commensurate to the remit of their functions` — function-specific depth on the workforce (D-08.2 layer), distinct from the baseline awareness programme at D-08.1.
- The chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation (per SR-DORA-025 ambiguity_notes).
- **T4-vs-text gap awareness:** T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit of their functions` (per SR-DORA-025 ambiguity_notes); the Executor keeps the OJ-literal locus.
- PR.AT-02 layers the role-specific depth dimension — staff in security-critical roles (incident response, ICT operations, fraud investigation, third-party governance) receive calibrated depth rather than a uniform baseline. Together with PR.AT-01 (the baseline awareness layer at D-08.1), the two operationalise both the `compulsory` and the `commensurate` axes of Art. 13(6).
**CSF anchors (from `SR-DORA-025` v0.3 security_rationale):**
PR.AT-01, PR.AT-02.
*(PR.AT-01 anchors the baseline awareness layer that closes the human-factor gap — phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes — and converts the OJ `ICT security awareness programmes` from an opt-in continuing-professional-development activity into a compulsory training-module floor across the workforce (D-08.1 layer). PR.AT-02 layers the role-specific depth dimension that the OJ `commensurate to the remit of their functions` qualifier demands (D-08.2 layer), ensuring that staff in security-critical roles (incident response, ICT operations, fraud investigation, third-party governance) receive calibrated depth rather than a uniform baseline. Together these two subcategories operationalise both the `compulsory` and the `commensurate` axes of Art. 13(6), and an entity evidencing PR.AT-01 coverage plus PR.AT-02 role-calibrated depth can demonstrate ex-post to supervisory review that the Art. 13(6) workforce-training obligation was met at both the universal-awareness floor (D-08.1) and the role-specific depth required by the staff function taxonomy (D-08.2), and that completion thresholds were documented as a condition of employment rather than as optional professional development.)*

---


## Security Requirements (DORA)

#### 8.2.4 — Financial-entity function-specific `commensurate to the remit` training

```yaml
- req_id: 8.2.4
  volere_section: 15
  volere_subtype: immunity

  title: "Financial-entity staff training modules with level of complexity commensurate to the remit of staff functions"

  derives_from:
    hso_sub_so: SO-8.2.DORA
    per_reg_so: SO-DORA-015 (partial via Art. 13(6) `commensurate to the remit`)
    source_sr: SR-DORA-025
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.4"

  description: |
    The product shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in the financial-entity's staff training schemes, with a level of complexity commensurate to the remit of staff functions (Art. 13(6) DORA), on the financial-entity's workforce audience, with function-specific depth calibrated to the staff function taxonomy (incident response, ICT operations, fraud investigation, third-party governance, and other security-critical roles).

  fit_criterion: |
    A financial-entity `commensurate to the remit` function-specific depth training programme is operated for staff in security-critical roles via PR.AT-02 role-specific depth (Workforce understands role-specific responsibilities) covering incident response (cross to D-04 layer — RS.MA-01 incident-management-plan-executed), ICT operations (cross to D-10 layer — DE.CM-01 networks-monitored + DE.CM-09 host-monitored), fraud investigation (cross to 4.4 detection + recovery), third-party governance (cross to D-06 supply-chain — GV.SC-04 supplier-assessment), and other security-critical roles receiving function-specific depth rather than a uniform baseline; the chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation per SR-DORA-025 ambiguity_notes; the chosen reading of `compulsory` is completion-mandatory (not mere attendance) per SR-DORA-025; **T4-vs-text gap awareness:** T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit of their functions` — the Executor keeps the OJ-literal locus per SR-DORA-025; the training modules are `compulsory` as a condition of employment rather than as optional professional development; completion thresholds (completion percentages, assessment-pass thresholds) are documented per the staff function taxonomy; the DORA Art. 13(6) `commensurate to the remit` programme is co-existent with GDPR Art. 39 staff-awareness duties for personal-data processing (EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration, AI Act Art. 4(2) provider-deployer literacy duties intersect where AI systems are in scope of the same staff training schemes); for an integrated financial-entity-controller with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair on the DORA financial entity = controller); for DORA financial entities that are also NSIEs, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification); for DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship); for a CRA-regulated manufacturer that is also a DORA financial entity, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator — per CRDA-deep §8.2 CRA↔DORA Executor-recommended SCOPE-DISJOINT pair); verified by per-role `commensurate to the remit` training-records inspection + completion-thresholds documentation per staff function taxonomy + EBA Guidelines supervisory baseline review + Art. 5(2) management-body oversight records + national CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.4 (8.1 `compulsory modules` is the upstream awareness programme substrate), 8.2.1 (when DORA-controller — DORA Art. 13(6) carrier + GDPR role-specific sub-component), 8.2.2 (DORA-dominant on role-specific training for DORA financial entities = NSIEs), 8.2.5 (when DORA FE deploys high-risk AI — DORA `commensurate to the remit` carrier + AI Act 5-element sub-component)]

  nist_csf: [PR.AT-01, PR.AT-02]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 13(6)):**
> "Financial entities shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions." — Art. 13(6) DORA (per SR-DORA-025 — `commensurate to the remit`)

**DORA article (verbatim, Art. 13(6)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.2: NIS2↔DORA = EQUAL (SAME — both regulations impose role-specific training; DORA-dominant for financial entities); DORA↔AI_Act = COMPLEMENTARY (SAME — DORA `commensurate to the remit` carrier + AI Act 5-element sub-component on DORA financial entity deploying high-risk AI); GDPR↔DORA = COMPLEMENTARY (recommended — DORA programme as carrier + GDPR role-specific module on DORA financial entity = controller); CRA↔DORA = SCOPE-DISJOINT (recommended — integrator-B2B vs internal staff audiences; different objects))
```

### from regs/DORA.md body

- For an integrated financial-entity-controller with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is the module (per CRDA-deep §D-08.2 GDPR↔DORA Executor-recommended COMPLEMENTARY classification).

### from regs/DORA.md body

- For DORA financial entities that are also NSIEs, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §D-08.2 NIS2↔DORA EQUAL classification).

### from regs/DORA.md body

- For DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is the sub-component (per CRDA-deep §D-08.2 DORA↔AI_Act verified relationship).

### from regs/DORA.md body

- For a CRA-regulated manufacturer that is also a DORA financial entity, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator — per CRDA-deep §D-08.2 CRA↔DORA Executor-recommended SCOPE-DISJOINT classification — no consolidation rule applies).


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Y (financial-entity-controller; DORA carrier + GDPR role-specific sub-component); DORA↔NIS2 = Y (cross-sector; DORA-NSIE; DORA-dominant on role-specific training); DORA↔AI_Act = Y (DORA FE deploys high-risk AI; DORA carrier + AI Act 5-element sub-component); DORA↔CRA = N substantively scope-disjoint (internal staff vs B2B integrator); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA role-specific competence obligation is the **function-specific depth layer of the Art. 13(6) workforce training duty** — anchored on `commensurate to the remit of their functions` — distinct from the baseline awareness programme at 8.1 layer. The chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation (per SR-DORA-025 ambiguity_notes). **T4-vs-text gap awareness:** T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit of their functions` (per SR-DORA-025 ambiguity_notes); the Executor keeps the OJ-literal locus. PR.AT-02 layers the role-specific depth dimension — staff in security-critical roles (incident response, ICT operations, fraud investigation, third-party governance) receive calibrated depth rather than a uniform baseline. Together with PR.AT-01 (the baseline awareness layer at 8.1 layer — 8.1.4), the two operationalise both the `compulsory` and the `commensurate` axes of Art. 13(6). For an integrated financial-entity-controller with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair). For DORA financial entities that are also NSIEs, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification). For DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship). For a CRA-regulated manufacturer that is also a DORA financial entity, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator — per CRDA-deep §8.2 CRA↔DORA Executor-recommended SCOPE-DISJOINT pair). The recipient is the competent authority (national financial supervisory authority) + management body — Art. 13(6) `commensurate to the remit` training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline. (Copied from the HSO Considerations block of `### 8.2.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=2 -->

