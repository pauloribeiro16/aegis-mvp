# D-08.2 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-019 | Employees offered similar training on a regular basis to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2). | Entity-side, encouraged-not-mandatory (Member State obligation); employee training for risk-identification and assessment capability. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | Member-State-encouraged employee training on risk-identification and assessment capability (entity-side, encouraged-not-mandatory at OJ level) | Member State encouragement per Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis` — binding force on Member State, not on entity directly (Orchestrator-recommended treatment per SR-NIS2-030) | `on a regular basis` entity-discretionary under Recital 56; the OJ is silent on training-frequency; the entity-side SR activates when the entity adopts the encouragement | management body (Art. 20(1) approve+oversee+liability) + competent authority — Art. 20(2) sentence 2 employee-training records + Art. 20(1) management-body approval | Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices` + Art. 20(2) sentence 1 purpose clause cross + Art. 20(1) management-body approval + Recital 56 proportionality |

## Sub-SO (NIS 2)

#### D-08.2.2 — Sub-SO for NIS 2

```yaml
id: SO-D-08.2.NIS2
subdomain: D-08.2
applies_to: [NIS2]
inherits_from: SO-NIS2-019
source_SR: SR-NIS2-030
activation: if NIS2 in applicable_regs  # entity-side SR applies to entities that adopt the Member-State encouragement (Orchestrator-recommended treatment per SR-NIS2-030 ambiguity_notes)
phase_1A_role: 1_of_N
```

**Objective.** Member States shall encourage essential and important entities to offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2 NIS 2).

**Considerations.**
- The binding force of Art. 20(2) sentence 2 is on the Member State rather than directly on the entity (Orchestrator-recommended treatment per SR-NIS2-030 ambiguity_notes) — the entity-side SR applies to entities that adopt the encouragement.
- The cross-link to Art. 20(2) sentence 1 anchors the purpose clause: training must equip employees to identify risks and assess cybersecurity risk-management practices, the same purpose clause that governs the management-body training in SR-NIS2-031.
- The chosen reading of `shall encourage` is the cumulative reading (national policy + financial incentives + sectoral guidance + all) since the OJ is silent on the encouragement mechanism (per SR-NIS2-030 ambiguity_notes).
- The compound `similar training` admits a parallel-to-management-training reading — the chosen reading is literal (parallel-to-management-training because the OJ coordinates sentence 2 with sentence 1 within the same paragraph).
- The temporal anchor `on a regular basis` is entity-discretionary under Recital 56.
- PR.AT-01 anchors the recurring training content (phishing, social engineering, password discipline, threat-recognition capability — per SR-NIS2-030 security_rationale).
- PR.AT-02 anchors the role-specific dimension — each employee understands how their own role contributes to the entity's cybersecurity objectives — supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`.
**CSF anchors (from `SR-NIS2-030` v0.3 security_rationale):**
PR.AT-01, PR.AT-02.
*(PR.AT-01 anchors the recurring training content: phishing, social engineering, password discipline, and the threat-recognition capability that the OJ's purpose clause requires employees to possess. PR.AT-02 anchors the role-specific dimension: each employee understands how their own role contributes to the entity's cybersecurity objectives, supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`. Together, PR.AT-01 and PR.AT-02 operationalise the workforce-literacy substrate. The control set enables ex-post demonstration that the OJ's `regular basis` anchor is discharged against a documented training curriculum anchored in the NIST NICE Workforce Framework and proportionate to the entity's exposure.)*

---


## Security Requirements (NIS 2)

#### 8.2.2 — Member-State-encouraged employee risk-identification training on a regular basis

```yaml
- req_id: 8.2.2
  volere_section: 15
  volere_subtype: immunity

  title: "Employees gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Member-State-encouraged, entity-side on adoption)"

  derives_from:
    hso_sub_so: SO-8.2.NIS2
    per_reg_so: SO-NIS2-019
    source_sr: SR-NIS2-030
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.2"

  description: |
    The product shall offer employees training on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2 NIS 2), with the entity-side SR applying to entities that adopt the Member-State encouragement (binding force on the Member State rather than directly on the entity per SR-NIS2-030).

  fit_criterion: |
    A Member-State-encouraged employee risk-identification training programme is operated when the entity adopts the encouragement, covering PR.AT-01 recurring training content (phishing, social engineering, password discipline, threat-recognition capability) + PR.AT-02 role-specific dimension supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`; the temporal anchor `on a regular basis` is entity-discretionary under Recital 56 (annual, biannual, ad-hoc, or event-triggered cadence — entity choice); the compound `similar training` reads as parallel-to-management-training per SR-NIS2-030 (the OJ coordinates sentence 2 with sentence 1 within the same paragraph); the chosen reading of `shall encourage` is the cumulative reading (national policy + financial incentives + sectoral guidance + all) since the OJ is silent on the encouragement mechanism; the entity-side SR applies to entities that adopt the encouragement (Orchestrator-recommended treatment per SR-NIS2-030 — the Article 20(2) sentence 2 binding force is on the Member State rather than directly on the entity); the training is anchored in the NIST NICE Workforce Framework and proportionate to the entity's exposure; for an integrated controller-NSIE adopting Member-State encouragement, the NIS 2 Member-State-encouraged employee risk-identification training stacks with the GDPR Art. 39(1)(b) DPO-catalysed role-specific training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship — joint curriculum on the Y-pair); for DORA financial entities, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification); for NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship — NIS 2 risk-identification baseline + AI Act 5-element competence stack); for a CRA-regulated manufacturer that is also an NSIE, the NIS 2 employee risk-identification training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §8.2 NIS2↔CRA Executor-recommended SCOPE-DISJOINT pair); the training programme coordinates with the Art. 20(2) sentence 1 management-body training via SR-NIS2-031 (cross to 8.3); verified by employee training-records inspection + risk-identification competency assessment records + NIST NICE Workforce Framework curriculum anchor documentation + management body + competent authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.2 (8.1 hygiene baseline is the upstream substrate), 8.2.1 (Conditional Y on controller-NSIE adopting encouragement — GDPR role-specific + NIS 2 employee risk-identification stack), 8.2.4 (when DORA-NSIE — DORA-dominant on role-specific training), 8.2.5 (when NSIE deploys high-risk AI and assigns human oversight — NIS 2 risk-identification baseline + AI Act 5-element competence stack)]

  nist_csf: [PR.AT-01, PR.AT-02]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 20(2) sentence 2):**
> "Member States shall encourage essential and important entities to offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices." — Art. 20(2) sentence 2 NIS 2

**NIS2 article (verbatim, Art. 20(2) sentence 2):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.2: GDPR↔NIS2 = COMPLEMENTARY (SAME — Conditional Y on controller-NSIE adopting Member-State encouragement); NIS2↔DORA = EQUAL (SAME — both regulations impose role-specific training; DORA-dominant for financial entities); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 risk-identification baseline + AI Act 5-element competence on NSIE deploying high-risk AI); NIS2↔CRA = SCOPE-DISJOINT (recommended — workforce vs integrator-B2B audiences; different objects))
```

### from regs/NIS2.md body

- For an integrated controller-NSIE adopting Member-State encouragement, the NIS 2 Member-State-encouraged employee risk-identification training stacks with the GDPR Art. 39(1)(b) DPO-catalysed role-specific training on the same workforce (Conditional Y per CRDA-deep §D-08.2 GDPR↔NIS2 verified relationship).

### from regs/NIS2.md body

- For DORA financial entities, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §D-08.2 NIS2↔DORA EQUAL classification).

### from regs/NIS2.md body

- For NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §D-08.2 NIS2↔AI_Act verified relationship).

### from regs/NIS2.md body

- For a CRA-regulated manufacturer that is also an NSIE, the NIS 2 employee risk-identification training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §D-08.2 NIS2↔CRA Executor-recommended SCOPE-DISJOINT classification — no consolidation rule applies).


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Y (Cond on controller-NSIE adopting encouragement); NIS2↔DORA = Y (DORA financial entity = NSIE; DORA-dominant on role-specific training); NIS2↔AI_Act = Y (NSIE deploys high-risk AI and assigns human oversight); NIS2↔CRA = N substantively scope-disjoint (workforce vs integrator-B2B); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 role-specific competence obligation is the **Member-State-encouraged employee training on risk-identification and assessment capability** — Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`. The binding force of Art. 20(2) sentence 2 is on the Member State rather than directly on the entity (Orchestrator-recommended treatment per SR-NIS2-030 ambiguity_notes) — the entity-side SR applies to entities that adopt the encouragement. The cross-link to Art. 20(2) sentence 1 anchors the purpose clause: training must equip employees to identify risks and assess cybersecurity risk-management practices, the same purpose clause that governs the management-body training in SR-NIS2-031 (cross to 8.3 layer). The chosen reading of `shall encourage` is the cumulative reading (national policy + financial incentives + sectoral guidance + all) since the OJ is silent on the encouragement mechanism. The compound `similar training` admits a parallel-to-management-training reading — the chosen reading is literal (parallel-to-management-training because the OJ coordinates sentence 2 with sentence 1 within the same paragraph). The temporal anchor `on a regular basis` is entity-discretionary under Recital 56. PR.AT-01 anchors the recurring training content (phishing, social engineering, password discipline, threat-recognition capability — per SR-NIS2-030 security_rationale). PR.AT-02 anchors the role-specific dimension — each employee understands how their own role contributes to the entity's cybersecurity objectives — supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`. **8.1 layer (8.1.2)** establishes the entity-wide hygiene baseline. For an integrated controller-NSIE adopting Member-State encouragement, the NIS 2 Member-State-encouraged employee risk-identification training stacks with the GDPR Art. 39(1)(b) DPO-catalysed role-specific training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship). For DORA financial entities, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification). For NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship). For a CRA-regulated manufacturer that is also an NSIE, the NIS 2 employee risk-identification training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §8.2 NIS2↔CRA Executor-recommended SCOPE-DISJOINT pair). The recipient is the management body (Art. 20(1) approve+oversee+liability — 8.3 layer via SR-NIS2-031) + competent authority — Art. 20(2) sentence 2 employee-training records + Art. 20(1) management-body approval. (Copied from the HSO Considerations block of `### 8.2.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=7; core_cross_mentions=2 -->