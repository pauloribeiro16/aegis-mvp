# D-04.2 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-005 | Six-action incident-handling capability (prevent, detect, analyse, contain, respond, recover) per Art. 21(2)(b) + Art. 6(8) `contain` action | Entity-level ICT systems; lifecycle-phase content; RC.RP-01 + RC.RP-04 + PR.IR-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | entity-level incident-handling `contain` phase | lifecycle-phase actions (the `contain` action within the 6-action Art. 6(8) incident-handling lifecycle) | `appropriate and proportionate` (Art. 21(1)) | CSIRT or competent authority (Art. 23(4)(b) notification; 1m final report) | Art. 21(2)(b) + Art. 6(8) (six-action `contain` phase) |

## Sub-SO (NIS 2)

#### D-04.2.2 — Sub-SO for NIS 2

```yaml
id: SO-D-04.2.NIS2
subdomain: D-04.2
applies_to: [NIS2]
inherits_from: SO-NIS2-005
source_SR: SR-NIS2-008
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The entity operates the incident-handling capability across all six actions of the Art. 6(8) `incident handling` lifecycle (prevent, detect, analyse, contain, respond, recover), with the `contain` action documented in the entity-level response plan as the lifecycle phase that isolates affected systems and prevents further damage (Art. 21(2)(b)).

**Considerations.**
- The NIS 2 containment-and-mitigation obligation is the entity-level incident-handling `contain` phase; the operational substrate is the entity-wide response plan with the `contain` action as one of the six Art. 6(8) incident-handling actions. The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the containment depth: high-impact incidents trigger deeper and more aggressive containment than low-impact ones.
- The downstream notification cascade (Art. 23(4)(b) incident notification + Art. 23(4)(d) 1m final report with mitigation measures) is part of D-04.3, not D-04.2.

**CSF anchors (from `SR-NIS2-008` v0.3 security_rationale):**
RS.MA-01, RS.AN-03.
*(PR.IR-03 anchors the network-resources-prioritised-based-on-importance
leg (the `contain` action isolates high-importance resources first);
PR.IR-04 anchors the adequate-resource-capacity leg; RC.RP-01 anchors
the recovery-plan-execution leg for the contain-then-recover
sequence.)*

---


## Security Requirements (NIS 2)

#### 4.2.2 — Entity-level incident-handling `contain` phase within the 6-action lifecycle

```yaml
- req_id: 4.2.2
  volere_section: 15
  volere_subtype: immunity

  title: "Entity-level `contain` action within the Art. 6(8) six-action incident-handling lifecycle; entity response plan as procedural wrapper"

  derives_from:
    hso_sub_so: SO-4.2.NIS2
    per_reg_so: SO-NIS2-005
    source_sr: SR-NIS2-008
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md
    objective_ref_section: "### 4.2.2"

  description: |
    The product shall operate the entity-level incident-handling capability across all six actions of the Art. 6(8) `incident handling` lifecycle (prevent, detect, analyse, contain, respond, recover), with the `contain` action documented in the entity-level response plan as the lifecycle phase that isolates affected systems and prevents further damage, and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the containment depth with high-impact incidents triggering deeper and more aggressive containment than low-impact ones (NIS 2 Art. 21(2)(b) + Art. 6(8) six-action `contain` action).

  fit_criterion: |
    The entity-level response plan documents the `contain` action as one of the six Art. 6(8) incident-handling actions (prevent, detect, analyse, contain, respond, recover) with explicit isolation procedures, system-segregation runbooks, blast-radius limitation protocols, and stakeholder-coordination steps for the `contain` phase; PR.IR-03 network-resources-prioritised-based-on-importance leg anchors the isolation of high-importance resources first; PR.IR-04 adequate-resource-capacity leg anchors the resource allocation for containment; RC.RP-01 recovery-plan-execution leg anchors the contain-then-recover sequence; risk-tiered containment depth (high-impact incidents trigger deeper and more aggressive containment) is documented per the Art. 21(1) `appropriate and proportionate` qualifier; the entity-level response plan is the procedural wrapper that hosts the GDPR Art. 33(3)(d) TOMs (controller/NSIE scenario — 4.2-GDPR cross-ref) and the CRA Annex I (2)(h)/(i)/(k) product-resilience evidence (NIS 2 deployer scenario — 4.2-CRA cross-ref); for multi-reg parties, the NIS 2 response plan hosts the GDPR personal-data measures and the CRA product-resilience evidence under explicit cross-references; the entity-level containment discipline operates at the entity boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), product-design availability (CRA leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by entity-level response plan inspection + six-action `contain` phase operational records review + risk-tier containment mapping review + CSIRT / competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.2 (containment triggered by prior entity-level all-hazards detection event), 4.2.1 (when controller-NSIE — GDPR TOMs inside NIS 2 plan), 4.2.3 (when NIS 2 entity deploys/manufactures CRA product — CRA product-resilience evidence feeds NIS 2 plan), 4.2.4 (when DORA + NIS 2 cross-sector — NIS 2 chapeau coverage is the additional layer for non-financial incidents; physical + operational hazards still bind via NIS 2)]

  nist_csf: [RS.MI-01, RS.MI-02, PR.IR-03, PR.IR-04, RC.RP-01]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process including `containing` as one of the six actions.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.2: GDPR↔NIS2 = COMPLEMENTARY; NIS2↔CRA = COMPLEMENTARY; NIS2↔DORA = COMPLEMENTARY)
```

### from regs/NIS2.md body

- The entity-level lifecycle-phase action object is distinct from the GDPR personal-data post-breach runbook, the CRA product-design availability choices, and the DORA BC arrangements — the entity response plan is the containment layer, and the lifecycle-phase discipline operates at that layer only.

### from regs/NIS2.md body

- For a multi-reg party, the NIS 2 response plan is the procedural wrapper that hosts the GDPR Art. 33(3)(d) TOMs (controller/NSIE scenario) and the CRA Annex I (2)(h)/(i)/(k) product-resilience evidence (NIS 2 deployer scenario).

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y controller-NSIE; NIS 2 plan is the procedural wrapper, GDPR measures inside); NIS2↔CRA = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint in baseline: entity-level phase ↔ product-level design; CRA evidence feeds NIS 2 plan); NIS2↔DORA = Conditional (Y cross-sector; N pure-financial via lex specialis — DORA BC exceeds NIS 2 `contain` for financial-services subset); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 containment-and-mitigation obligation is the entity-level incident-handling `contain` phase; the operational substrate is the entity-wide response plan with the `contain` action as one of the six Art. 6(8) incident-handling actions. The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the containment depth. The entity-level lifecycle-phase action object is distinct from the GDPR personal-data post-breach runbook, the CRA product-design availability choices, and the DORA BC arrangements — the entity response plan is the containment layer, and the lifecycle-phase discipline operates at that layer only. For a multi-reg party, the NIS 2 response plan is the procedural wrapper that hosts the GDPR Art. 33(3)(d) TOMs (controller/NSIE scenario) and the CRA Annex I (2)(h)/(i)/(k) product-resilience evidence (NIS 2 deployer scenario). For DORA + NIS 2 cross-sector entities, the DORA BC arrangements absorb the financial-services subset of incidents and the NIS 2 chapeau extends to non-financial incidents (physical + operational hazards beyond ICT). For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 `contain` obligation for the financial-services subset and the high-level SO does not aggregate across the lex-specialis boundary in that direction. The downstream notification cascade (Art. 23(4)(b) incident notification + Art. 23(4)(d) 1m final report with mitigation measures) is part of 4.3, not 4.2. (Copied from the HSO Considerations block of `### 4.2.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=2 -->
