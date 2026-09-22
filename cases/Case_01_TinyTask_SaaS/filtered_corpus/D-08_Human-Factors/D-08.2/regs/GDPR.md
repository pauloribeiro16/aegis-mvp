# D-08.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-025 (cross-ref at D-08.2) | DPO monitors assignment of responsibilities, awareness-raising, training of staff involved in processing (Art. 39(1)(b)). | Role-specific training for staff with data-subject-facing or access-management responsibilities. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | DPO-catalysed processing staff with data-subject-facing or access-management responsibilities (role-specific layer of the Art. 39(1)(b) duty) | DPO-catalysed role-specific training (Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations`) | no quantitative cadence (DPO-discretionary under Recital 56); `awareness-raising` implies ongoing reinforcement not one-off induction; role-specific depth on data-subject-facing and access-management responsibilities | supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) role-specific training records (cross to D-09.2 via Art. 35 DPIA necessary-assessment chain) | Art. 39(1)(a) + Art. 39(1)(b) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) + Art. 30(4) + Art. 47(2)(n) BCR |

## Sub-SO (GDPR)

#### D-08.2.1 — Sub-SO for GDPR

```yaml
id: SO-D-08.2.GDPR
subdomain: D-08.2
applies_to: [GDPR]
inherits_from: SO-GDPR-025 (cross-ref at D-08.2)
source_SR: SR-GDPR-042
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The data protection officer monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR) — the role-specific layer of the DPO-catalysed awareness function.

**Considerations.**
- The role-specific dimension targets staff with data-subject-facing or access-management responsibilities — distinct from the general awareness programme at D-08.1.
- The chosen reading of `awareness-raising` (per SR-GDPR-042 ambiguity_notes) splits the obligation into two: (1) general awareness training on GDPR for all personnel involved in processing, on an annual basis (D-08.1 layer); (2) role-specific training for personnel with data-subject-facing or access-management responsibilities, on a quarterly or event-triggered basis (D-08.2 layer).
- PR.AT-02 anchors the role-specific layer — personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme.
- The role-specific depth is documented under Art. 5(2) accountability on the controller side — the controller must demonstrate that the Art. 39(1)(b) DPO-catalysed role-specific training was operationally exercised and recorded on the day of any supervisory inspection.
**CSF anchors (from `SR-GDPR-042` v0.3 security_rationale):**
PR.AT-01, PR.AT-02.
*(PR.AT-01 captures the broad-coverage discipline (D-08.1 layer) — the DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and the changing data flows of the organisation. PR.AT-02 captures the role-specific layer (D-08.2 layer) that PR.AT-01 cannot cover: personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme. The two subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 39(1) DPO mandate, that the DPO's awareness-and-training function — both the general-awareness layer and the role-specific layer — was operationally exercised and recorded on the day of any supervisory inspection.)*

---


## Security Requirements (GDPR)

#### 8.2.1 — DPO-catalysed role-specific training for processing staff with data-subject-facing or access-management responsibilities

```yaml
- req_id: 8.2.1
  volere_section: 15
  volere_subtype: immunity

  title: "Role-specific training for processing staff with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities"

  derives_from:
    hso_sub_so: SO-8.2.GDPR
    per_reg_so: SO-GDPR-025 (cross-ref)
    source_sr: SR-GDPR-042
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.1"

  description: |
    The product shall provide role-specific training for personnel with data-subject-facing, access-management, breach-response, or DPO-deputy responsibilities (the role-specific layer of the Art. 39(1)(b) DPO-catalysed awareness function), with quarterly or event-triggered cadence and content covering GDPR-specific and cybersecurity-specific obligations for the assigned role (GDPR Art. 39(1)(a) + Art. 39(1)(b)).

  fit_criterion: |
    A DPO-catalysed role-specific training programme is operated for personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities via PR.AT-02 role-understanding dimension (Workforce understands role-specific responsibilities) on a quarterly cadence or event-triggered cadence (whichever is sooner — material change of role, material change of processing profile, material change of risk, post-incident); the chosen reading per SR-GDPR-042 ambiguity_notes splits the obligation into (1) general awareness training on GDPR for all personnel involved in processing, on an annual basis (8.1 layer — 8.1.1 cross-ref) + (2) role-specific training for personnel with the four responsibility-types above, on a quarterly or event-triggered basis (this layer); the role-specific training covers: data-subject-rights handling (Arts. 12–22), access-management including privileged-access review (Art. 25 + Art. 32), breach-response including notification timelines (Art. 33 + Art. 34 — D-04 cross-references), DPO-deputy capacity when the primary DPO is unavailable (Art. 38–39), and updated content reflecting emerging threats + the changing data flows of the organisation; the role-specific training is documented under Art. 5(2) accountability so the controller can demonstrate on the day of any supervisory inspection that the Art. 39(1)(b) DPO-catalysed role-specific training was operationally exercised and recorded; for an integrated controller-NSIE adopting Member-State encouragement, the GDPR role-specific layer stacks with the NIS 2 Member-State-encouraged employee risk-identification training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship — joint curriculum on the Y-pair); for a DORA financial entity that is a controller processing personal data with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair on the DORA financial entity = controller); for an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified DIFFERENT-PERSPECTIVE pair); verified by role-specific training records inspection (per responsibility-type — four-way review) + DPO-catalysed training-completion records inspection + Art. 5(2) accountability evidence pack + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.1 (8.1 awareness substrate is upstream governance input — annual general awareness + this quarterly role-specific), 8.2.2 (Conditional Y on controller-NSIE adopting Member-State encouragement — GDPR role-specific + NIS 2 employee risk-identification stack), 8.2.4 (when DORA-controller — DORA Art. 13(6) carrier + GDPR role-specific sub-component)]

  nist_csf: [PR.AT-02, PR.AT-01]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 39(1)(b)):**
> "The data protection officer shall … monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations …" — Art. 39(1)(b) GDPR

**GDPR article (verbatim, Art. 39(1)(b)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.2: GDPR↔NIS2 = COMPLEMENTARY (SAME — Conditional Y on controller-NSIE adopting Member-State encouragement); GDPR↔DORA = COMPLEMENTARY (recommended — DORA programme as carrier + GDPR role-specific module on DORA financial entity = controller); GDPR↔AI_Act = DIFFERENT-PERSPECTIVE (SAME — Conditional Y on same natural person as both data-processing staff and AI human overseer); GDPR↔CRA = SCOPE-DISJOINT (recommended — workforce vs integrator-B2B audiences; different objects))
```

### from regs/GDPR.md body

- For an integrated controller-NSIE adopting Member-State encouragement, the GDPR role-specific layer stacks with the NIS 2 Member-State-encouraged employee risk-identification training on the same workforce (Conditional Y per CRDA-deep §D-08.2 GDPR↔NIS2 verified relationship).

### from regs/GDPR.md body

- For a DORA financial entity that is a controller processing personal data with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is the module (per CRDA-deep §D-08.2 GDPR↔DORA Executor-recommended COMPLEMENTARY classification).

### from regs/GDPR.md body

- For an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §D-08.2 GDPR↔AI_Act verified relationship).

### from regs/GDPR.md body

- For a CRA-regulated manufacturer that is also a controller, the GDPR role-specific workforce training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §D-08.2 GDPR↔CRA Executor-recommended SCOPE-DISJOINT classification — no consolidation rule applies).


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Y (Cond on controller-NSIE adopting encouragement); GDPR↔DORA = Y (DORA financial entity = controller); GDPR↔AI_Act = Y (Cond on same natural person as both data-processing staff and AI human overseer); GDPR↔CRA = N substantively scope-disjoint (workforce vs integrator-B2B); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR role-specific competence obligation is the **role-specific layer of the Art. 39(1)(b) DPO-catalysed awareness function** — distinct from the general awareness programme at 8.1 layer. The chosen reading of `awareness-raising` (per SR-GDPR-042 ambiguity_notes) splits the obligation into two: (1) general awareness training on GDPR for all personnel involved in processing, on an annual basis (8.1 layer — 8.1.1); (2) role-specific training for personnel with data-subject-facing or access-management responsibilities, on a quarterly or event-triggered basis (this 8.2 layer). PR.AT-02 anchors the role-specific layer — personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme. The role-specific depth is documented under Art. 5(2) accountability on the controller side — the controller must demonstrate that the Art. 39(1)(b) DPO-catalysed role-specific training was operationally exercised and recorded on the day of any supervisory inspection. For an integrated controller-NSIE adopting Member-State encouragement, the GDPR role-specific layer stacks with the NIS 2 Member-State-encouraged employee risk-identification training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship). For a DORA financial entity that is a controller processing personal data with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair). For an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified relationship — same natural person — AND-stack). For a CRA-regulated manufacturer that is also a controller, the GDPR role-specific workforce training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §8.2 GDPR↔CRA Executor-recommended SCOPE-DISJOINT pair — no consolidation rule applies). The recipient is the supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) role-specific training records (cross to 9.2 via Art. 35 DPIA necessary-assessment chain). (Copied from the HSO Considerations block of `### 8.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=7; core_cross_mentions=2 -->