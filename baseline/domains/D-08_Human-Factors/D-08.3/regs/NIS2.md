# D-08.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-020 | Members of the management bodies of essential and important entities follow cybersecurity training, gaining sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by entity (Art. 20(2) sentence 1). | Management-body training mandatory (Member-State-imposed — the binding force is on the MS, with the entity-side SR applying only where the MS has transposed); literacy prerequisite for Art. 20(1) approve+oversee+liable governance duties. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | members of the management bodies of essential and important entities (every member individually — the OJ does not provide a designation carve-out; the definition of `management body` is Member-State-determined under Article 6 / Recital 75) | Member-State obligation — the binding force of Art. 20(2) sentence 1 is on the Member State (`Member States shall ensure`); the entity-side SR applies only where the Member State has transposed, per SR-NIS2-031 ambiguity_notes (chosen reading: both reading — statute mandates, entity operationalises) | `sufficient knowledge and skills` (cybersecurity-specific reading dominant per the OJ's coordination with `cybersecurity risk-management practices`) + `required to follow training` (S3 ambiguity on the binding-force locus — statutory reading, entity-internal reading, or both reading; chosen reading: both reading); no quantitative cadence; the OJ does not enumerate the content — entity-internal programme with the chosen reading being entity-discretionary (formal certified training preferred where the entity seeks documented compliance evidence) | management body (Art. 20(1) approve+oversee+liable) + competent authority (national NIS 2 supervisory authority) — Art. 20(2) sentence 1 management-body training records + Art. 20(1) management-body approval minute + Member State supervisory review | Art. 20(2) sentence 1 `Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` + Art. 20(1) sentence 1 first/second/third clause approve+oversee+liable (literacy prerequisite) + Recital 75 (management-body engagement as a strategic discipline) + Art. 6 (definition of `management body` is Member-State-determined) |

## Sub-SO (NIS 2)

#### D-08.3.1 — Sub-SO for NIS 2

```yaml
id: SO-D-08.3.NIS2
subdomain: D-08.3
applies_to: [NIS2]
inherits_from: SO-NIS2-020
source_SR: SR-NIS2-031
activation: if NIS2 in applicable_regs  # entity-side SR applies to entities that have an MS-transposed Member-State obligation under Art. 20(2) sentence 1; the standard MS-implementation pattern is the both reading (statute mandates, entity operationalises), per SR-NIS2-031 ambiguity_notes
phase_1A_role: 1_of_N
```

**Objective.** Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity (Art. 20(2) sentence 1 NIS 2).

**Considerations.**
- The training obligation is structurally the literacy prerequisite for the Article 20(1) management-body obligations (approve, oversee, can be held liable under SR-NIS2-032/033/034): without trained members, the management body cannot meaningfully discharge the approve-and-oversee obligations or be held accountable for infringements (per SR-NIS2-031 regulatory_rationale).
- The purpose clause anchors two distinct knowledge objects (identify risks; assess cybersecurity risk-management practices) and a third impact object (impact on the services provided), which together define the syllabus scope without prescribing specific content.
- The Member-State implementation determines whether the training is statutory (statute-imposed curriculum), entity-internal (entity's own programme), or both; the chosen reading is the both reading as the standard MS-implementation pattern (per SR-NIS2-031 ambiguity_notes).
- The binding force of Art. 20(2) sentence 1 is on the Member State (`Member States shall ensure`); the entity-side SR applies only where the Member State has transposed.
- The construction `are required to follow training` carries an S3 ambiguity on the binding-force locus — a statutory reading, an entity-internal reading, or a both reading — with the chosen reading being the both reading since the OJ's literal `are required to follow` is compatible with either locus.
- The compound `training` admits three operative readings (formal certified programme, awareness briefing, or tabletop exercise), with the chosen reading being entity-discretionary, with formal certified training preferred where the entity seeks documented compliance evidence (per SR-NIS2-031 ambiguity_notes).
- The scope `members of the management bodies` admits three readings (every member individually, the body collectively, or a designated subset), with the literal reading being every member individually because the OJ does not provide a designation carve-out; the definition of `management body` is Member-State-determined under Article 6 (Recital 75).
- The qualifier `sufficient knowledge and skills` admits a general-management or cybersecurity-specific reading, with the cybersecurity-specific reading being dominant because the OJ coordinates it with `cybersecurity risk-management practices`.
- PR.AT-03 (All senior executives understand their roles and responsibilities in achieving the organization's cybersecurity objectives) anchors the executive-literacy substrate: management-body members individually possess sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion.
- GV.RR-01 (Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture) anchors the leadership-culture substrate: trained members exercise the approve-and-oversee obligations of Article 20(1) with informed judgement and accept personal liability exposure under Article 20(1) sentence 1 third clause on a substantively-informed basis.
- For a non-financial NSIE that is not a financial entity (NIS 2 only), only the NIS 2 sub-SO activates and the management-body training is discharged against the Art. 20(2) sentence 1 Member-State-imposed literacy prerequisite with the MS-supervised evidence trail.
**CSF anchors (from `SR-NIS2-031` v0.3 security_rationale):**
PR.AT-03, GV.RR-01.

---


## Security Requirements (NIS 2)

#### 8.3.1 — Members of management bodies of essential and important entities follow cybersecurity training (Member-State-imposed literacy prerequisite)

```yaml
- req_id: 8.3.1
  volere_section: 15
  volere_subtype: immunity

  title: "Members of management bodies of essential and important entities follow cybersecurity training to gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices"

  derives_from:
    hso_sub_so: SO-8.3.NIS2
    per_reg_so: SO-NIS2-020
    source_sr: SR-NIS2-031
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.3.md
    objective_ref_section: "### 8.3.1"

  description: |
    The product shall ensure that members of the management bodies of essential and important entities follow cybersecurity training gaining sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity (per NIS 2 Art. 20(2) sentence 1), where the entity-side SR applies where the Member State has transposed the literacy prerequisite for the Art. 20(1) approve+oversee+liable governance duties.

  fit_criterion: |
    Each member of the management body individually (the OJ does not provide a designation carve-out — the literal `members of the management bodies` reads as every member individually, per SR-NIS2-031 ambiguity_notes) has documented evidence of cybersecurity training completion covering the OJ purpose-clause objects — `sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` — with PR.AT-03 executive-literacy substrate (each member individually possesses sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion) + GV.RR-01 leadership-culture substrate (trained members exercise the Art. 20(1) approve+oversee+liable obligations with informed judgement and accept personal liability exposure under Art. 20(1) sentence 1 third clause on a substantively-informed basis); the binding-force locus is the both reading (statute mandates, entity operationalises) under the standard MS-implementation pattern, with Member State transposition divergence preserved (the chosen reading is the both reading since the OJ literal `are required to follow` is compatible with either locus, per SR-NIS2-031 ambiguity_notes); the `training` content is entity-discretionary (formal certified programme preferred where the entity seeks documented compliance evidence, with awareness-briefing and tabletop-exercise readings admitted, per SR-NIS2-031 ambiguity_notes); the `sufficient knowledge and skills` threshold is read in the cybersecurity-specific dominant sense because the OJ coordinates it with `cybersecurity risk-management practices`; the programme couples with 8.3.2 on a DORA-dominant stack for a DORA financial entity that is also an NSIE (DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities, per CRDA-deep §8.3 NIS2↔DORA verified relationship); the Art. 20(2) sentence 1 training obligation is the literacy prerequisite for the Art. 20(1) approve+oversee+liable obligations (cross-ref 9.1.2 for the management-body approval minute + Art. 21(2)(a) policy artefact) — without trained members, the management body cannot meaningfully discharge the approve-and-oversee obligations or be held accountable for infringements, per SR-NIS2-031 regulatory_rationale; the programme is documented under Art. 21(1) NIS 2 chapeau with the management-body approval minute as governance hook (cross-ref 9.1.2); the workforce-scale upstream substrate (8.1 general awareness — 8.1.2) and the workforce-scale depth dimension (8.2 role-specific competence — 8.2.2) feed the management-body literacy substrate without collapsing the governance-track / workforce-scale track distinction; verified by management-body training programme documentation review + per-individual-member training-completion records + Art. 20(2) sentence 1 supervisory-evidence pack + competent-authority (national NIS 2 supervisory authority) review on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.2 (when DORA-NSIE — DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges NIS 2 Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities; DORA-dominant stack), 9.1.2 (management-body approval minute as governance hook on Art. 21 measures), 9.1.4 (when DORA-NSIE — DORA framework as carrier on the DORA-dominant stack)]

  nist_csf: [PR.AT-03, GV.RR-01]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 20(2) sentence 1):**
> "Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity." — Art. 20(2) sentence 1 NIS 2 (per SR-NIS2-031)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: EQUAL (CRDA-deep, D-08.3: NIS2↔DORA = EQUAL (SAME — both regulations impose management-body training with the same operative target — senior-executive literacy + governance competence — and the same CSF substrate — PR.AT-03 + GV.RR-01; the EQUAL classification reflects this parallel; the dominant-authority reading is DORA-dominant for DORA financial entities; NIS 2 is dominant for non-financial NSIEs, per the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry))
```

### from regs/NIS2.md body

- For an integrated controller-NSIE with both NIS 2 and DORA applicability on the management-body-training substrate, the DORA Art. 5(4) programme is the dominant authority (per CRDA-deep §D-08.3 NIS2↔DORA verified relationship: "DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities").

### from regs/NIS2.md body

- **The CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy for entities deploying high-risk AI in NIS-critical contexts) is preserved as a structural Layer 2 review item; the HSO does NOT collapse the CRDA-unresolved interplay into a presumed reclassification.


### from regs/NIS2.md body

*(PR.AT-03 anchors the executive-literacy substrate: management-body members individually possess sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion — a board that has completed formal certified training in cybersecurity risk identification and assessment can demonstrate ex-post, against the Art. 20(1) governance duties and the Art. 5(2) DORA-equivalent, that the management body's approve-and-oversee obligations were exercised with informed judgement. GV.RR-01 anchors the leadership-culture substrate: trained members exercise the approve-and-oversee obligations of Article 20(1) with informed judgement and accept personal liability exposure under Article 20(1) sentence 1 third clause on a substantively-informed basis — the literacy substrate converts the upstream approve+oversee+liable architecture from procedural compliance into substantively-informed decision-making. Together, PR.AT-03 and GV.RR-01 connect management-body literacy to the wider accountability architecture; the control set enables ex-post demonstration that the management body could meaningfully interrogate the CISO's risk register, ask the right questions, and weight competing strategic trade-offs.)*

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔DORA = Y (when DORA financial entity is also an NSIE; DORA Art. 5(4) discharges both); for non-financial NSIE only, the sub-SO discharges the obligation standalone; for DORA-only financial entity (not an NSIE), the sub-SO is NOT activated and the DORA sub-SO discharges the obligation

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 management-body training obligation is structurally the **literacy prerequisite for the Art. 20(1) approve+oversee+liable governance duties** (SR-NIS2-031 regulatory_rationale): without trained members, the management body cannot meaningfully discharge the approve-and-oversee obligations or be held accountable for infringements. The purpose clause anchors two distinct knowledge objects (`identify risks`; `assess cybersecurity risk-management practices`) and a third impact object (`impact on the services provided`), which together define the syllabus scope without prescribing specific content. The `required to follow training` construction carries an S3 ambiguity on the binding-force locus (statutory reading / entity-internal reading / both reading) with the chosen reading being the both reading as the standard MS-implementation pattern (per SR-NIS2-031 ambiguity_notes). The binding force of Art. 20(2) sentence 1 is on the Member State (`Member States shall ensure`); the entity-side SR applies only where the Member State has transposed. The `members of the management bodies` scope admits three readings (every member individually / the body collectively / a designated subset) with the literal reading being every member individually because the OJ does not provide a designation carve-out; the definition of `management body` is Member-State-determined under Article 6 (Recital 75). PR.AT-03 anchors the executive-literacy substrate — management-body members individually possess sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion — and GV.RR-01 anchors the leadership-culture substrate — trained members exercise the approve-and-oversee obligations of Art. 20(1) with informed judgement and accept personal liability exposure under Art. 20(1) sentence 1 third clause on a substantively-informed basis. For a DORA financial entity that is also an NSIE, the DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` direct entity-side obligation discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite, per CRDA-deep §8.3 NIS2↔DORA verified relationship (DORA-dominant for financial entities). For a non-financial NSIE that is not a financial entity (NIS 2 only), only the NIS 2 sub-SO activates and the management-body training is discharged against the Art. 20(2) sentence 1 Member-State-imposed literacy prerequisite with the MS-supervised evidence trail. The **CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy for entities deploying high-risk AI in NIS-critical contexts) is preserved as a structural Layer 2 review item. (Copied from the HSO Considerations block of `### 8.3.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=6; core_cross_mentions=2 -->

