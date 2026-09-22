# D-08.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations and on the controller's or processor's data-protection policies applicable to their role (Art. 39(1)(a)+(b)). | DPO-driven; workforce awareness on data-protection obligations specific to processing role. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | DPO-catalysed processing staff with data-subject-facing or access-management responsibilities (internal workforce) | DPO-catalysed awareness/training activity per Art. 39(1)(b) `awareness-raising and training of staff involved in processing operations` + Art. 39(1)(a) `inform and advise the controller or the processor and the employees who carry out processing of their obligations` | no quantitative cadence (DPO-discretionary under Recital 56); `awareness-raising` implies ongoing reinforcement not one-off induction; Art. 5(2) accountability burden shifts demonstration duty to the controller | supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) DPO-catalysed awareness/training records + Art. 30(4) staff awareness record + Art. 47(2)(n) BCR training (cross to D-09.2 via Art. 35 DPIA necessary-assessment chain) | Art. 39(1)(a) + Art. 39(1)(b) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) + Art. 30(4) + Art. 47(2)(n) BCR |

## Sub-SO (GDPR)

#### D-08.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-08.1.GDPR
subdomain: D-08.1
applies_to: [GDPR]
inherits_from: SO-GDPR-025
source_SR: SR-GDPR-042
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The data protection officer informs and advises the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions (Art. 39(1)(a) GDPR), and monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR).

**Considerations.**
- The DPO is the catalyst for the controller-side awareness programme — distinct from the controller's substantive training obligation — operating as the internal advisor and awareness-raising/training agent for staff involved in processing.
- The design-anchor is DPO-discretionary cadence (no quantitative cadence in Art. 39(1)(b); the OJ is silent on training-frequency or completion-thresholds); `awareness-raising` implies ongoing reinforcement rather than one-off induction (per SR-GDPR-042 ambiguity reading).
- The DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and changing data flows (PR.AT-01 anchor).
- The role-specific layer (PR.AT-02) covers personnel with data-subject-facing, access-management, breach-response, or DPO-deputy responsibilities — distinct from the general awareness programme.
- The DPO's awareness function is documented under Art. 5(2) accountability on the controller side — the controller must demonstrate that the Art. 39(1)(a)+(b) DPO-catalysed awareness function was operationally exercised and recorded on the day of any supervisory inspection.
**CSF anchors (from `SR-GDPR-042` v0.3 security_rationale):**
PR.AT-01, PR.AT-02.
*(PR.AT-01 anchors the broad-coverage discipline: the DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and the changing data flows of the organisation — phishing awareness, social-engineering recognition, password discipline, removable-media hygiene, incident-reporting reflexes. PR.AT-02 anchors the role-specific layer that PR.AT-01 cannot cover: personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme. The two subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 39(1) DPO mandate, that the DPO's awareness-and-training function was operationally exercised and recorded on the day of any supervisory inspection.)*

---


## Security Requirements (GDPR)

#### 8.1.1 — DPO-catalysed workforce data-protection awareness with Art. 39(1)(a)+(b) documentation

```yaml
- req_id: 8.1.1
  volere_section: 15
  volere_subtype: immunity

  title: "Personnel authorised to process personal data receive DPO-catalysed awareness-raising and training on GDPR obligations applicable to their role"

  derives_from:
    hso_sub_so: SO-8.1.GDPR
    per_reg_so: SO-GDPR-025
    source_sr: SR-GDPR-042
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md
    objective_ref_section: "### 8.1.1"

  description: |
    The product shall operate a DPO-catalysed data-protection awareness programme covering personnel authorised to process personal data, with the DPO informing and advising the controller or processor and the employees who carry out processing of their obligations (Art. 39(1)(a) GDPR) and monitoring compliance including assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR), where the controller is the data-protection awareness anchor on the controller-side processing-staff audience.

  fit_criterion: |
    A DPO-catalysed data-protection awareness programme is operated covering all personnel authorised to process personal data via PR.AT-01 broad-coverage leg (phishing, social-engineering, password-discipline, removable-media, incident-reporting reflexes as they apply to data-protection obligations) on a recurring cadence with content that updates to reflect emerging threats and the changing data flows of the organisation; the DPO inform-and-advise obligation under Art. 39(1)(a) is documented with documented advisory records (DPO briefs + induction material + privacy-notice change advisory); the DPO awareness-raising and training obligation under Art. 39(1)(b) is documented with annual induction-completion records + periodic reinforcement records (DPO-discretionary cadence under Recital 56 — no quantitative OJ cadence; `awareness-raising` implies ongoing reinforcement rather than one-off induction per SR-GDPR-042 ambiguity reading); personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities receive role-specific reinforcement of their GDPR and cybersecurity obligations under PR.AT-02 (8.2 layer — cross-ref 8.2.1); the programme is documented under Art. 5(2) accountability so the controller can demonstrate on the day of any supervisory inspection that the Art. 39(1)(a)+(b) DPO-catalysed awareness function was operationally exercised and recorded; for an integrated controller-NSIE workforce the GDPR data-protection module combines with the NIS 2 entity-wide basic-hygiene module into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship — separate evidence trails on the controller side vs the entity side); for a DORA financial entity that is a controller processing personal data over its own staff, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is a sub-component of the carrier (per CRDA-deep §8.1 GDPR↔DORA verified relationship — DORA programme as carrier + GDPR content as module); for a CRA-regulated manufacturer that is also a controller, the GDPR workforce awareness obligation is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs external end-user — per CRDA-deep §8.1 GDPR↔CRA verified relationship — no consolidation rule applies); verified by DPO-catalysed awareness-records inspection + DPO inform-and-advise records review + Art. 5(2) accountability evidence pack + training-cadence documentation + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.2 (when controller = NSIE — GDPR data-protection module combines with NIS 2 hygiene module into single curriculum), 8.1.4 (when DORA-controller — DORA Art. 13(6) is the carrier programme; GDPR content is a sub-component)]

  nist_csf: [PR.AT-01, PR.AT-02]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 39(1)(a)+(b)):**
> "The data protection officer shall … (a) inform and advise the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions; (b) monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations …" — Art. 39(1)(a)+(b) GDPR

**GDPR article (verbatim, Art. 39(1)(a)+(b)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — DPO data-protection vs hygiene baseline stack at controller-NSIE; combined curriculum); GDPR↔DORA = COMPLEMENTARY (SAME — controller-side data-protection awareness overlay on financial-entity compulsory-modules-led programme; DORA programme as carrier + GDPR content as module); GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; workforce vs end-user audiences; no consolidation rule))
```

### from regs/GDPR.md body

- For an integrated controller-NSIE workforce, the GDPR data-protection awareness module combines with the NIS 2 entity-wide hygiene baseline into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation (per CRDA-deep §D-08.1 GDPR↔NIS2 verified relationship).

### from regs/GDPR.md body

- For a DORA financial entity that is a controller processing personal data over its own staff, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is the module (per CRDA-deep §D-08.1 GDPR↔DORA verified relationship).

### from regs/GDPR.md body

- For a CRA-regulated manufacturer that is also a controller, the GDPR workforce awareness obligation is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule applies).


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Y (controller-NSIE; data-protection module + hygiene module combined); GDPR↔CRA = N (typically) substantively scope-disjoint (workforce vs end-user audiences); GDPR↔DORA = Y (financial-entity-controller; DORA programme as carrier + GDPR content as module); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR general-awareness obligation is the **DPO-driven catalyst for the controller-side awareness programme**, distinct from the controller's substantive training obligation — the DPO operates as the internal advisor and awareness-raising/training agent for staff involved in processing (Art. 39(1)(a) + Art. 39(1)(b)). The design-anchor is DPO-discretionary cadence (no quantitative cadence in Art. 39(1)(b); the OJ is silent on training-frequency or completion-thresholds); `awareness-raising` implies ongoing reinforcement rather than one-off induction (per SR-GDPR-042 ambiguity reading). The DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and the changing data flows of the organisation (PR.AT-01 anchor). The role-specific layer (PR.AT-02) covers personnel with data-subject-facing, access-management, breach-response, or DPO-deputy responsibilities — distinct from the general awareness programme and discharged at the 8.2 layer (8.2.1). The DPO's awareness function is documented under Art. 5(2) accountability on the controller side — the controller must demonstrate that the Art. 39(1)(a)+(b) DPO-catalysed awareness function was operationally exercised and recorded on the day of any supervisory inspection. **8.2 layer (RE...-8.2-GDPR)** adds the role-specific depth on the same workforce. For an integrated controller-NSIE workforce, the GDPR data-protection module combines with the NIS 2 entity-wide hygiene baseline into a single curriculum (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship). For a DORA financial entity that is a controller processing personal data over its own staff, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is the module (per CRDA-deep §8.1 GDPR↔DORA verified relationship). For a CRA-regulated manufacturer that is also a controller, the GDPR workforce awareness obligation is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule applies). The recipient is the supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) DPO-catalysed awareness/training records + Art. 30(4) staff awareness record + Art. 47(2)(n) BCR training (cross to 9.2 via Art. 35 DPIA necessary-assessment chain). (Copied from the HSO Considerations block of `### 8.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=2 -->