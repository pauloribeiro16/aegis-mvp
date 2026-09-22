# D-04.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-010 | Comprehensive ICT business continuity policy operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms (incl. response and recovery plans subject to independent internal audit for non-microenterprises; backup policies; restoration and recovery procedures) | Financial entity; BC arrangements under Art. 11 + Art. 12; RC.RP-01 + RC.RP-04 + PR.IR-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity BC arrangements | BC policy + dedicated arrangements (response + recovery plans + backup policies + restoration procedures) — 4-way AND of artefacts | `dedicated, appropriate and documented` (Art. 11(2)); independent internal audit for non-microenterprises (Art. 11(3)) | competent authority + clients (Art. 19(1)+(3) notification); internal audit function (Art. 11(3)) | Art. 11(1)/(2)/(3) + Art. 12(1) |

## Sub-SO (DORA)

#### D-04.2.4 — Sub-SO for DORA

```yaml
id: SO-D-04.2.DORA
subdomain: D-04.2
applies_to: [DORA]
inherits_from: SO-DORA-010
source_SR: SR-DORA-013, SR-DORA-014, SR-DORA-016
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms — including ICT response and recovery plans (subject to independent internal audit for non-microenterprises), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup based on criticality or confidentiality, and restoration and recovery procedures and methods (Art. 11(1) + Art. 11(2) + Art. 11(3) + Art. 12(1)).

**Considerations.**
- The DORA containment-and-mitigation obligation is the financial-entity BC arrangements architecture; the operational substrate is a comprehensive BC policy with dedicated, appropriate and documented arrangements including response and recovery plans, backup policies, and restoration procedures; the BC arrangements are subject to independent internal audit for non-microenterprises (the audit requirement is DORA-unique — no other participating regulator imposes an audit obligation on the containment architecture).
- The downstream notification cascade (Art. 19(1) competent-authority + Art. 19(3) client notification) is part of D-04.3, not D-04.2.

**CSF anchors (from `SR-DORA-013` + `SR-DORA-014` + `SR-DORA-016` v0.3 security_rationale):**
RC.RP-01, PR.IR-03, RC.RP-04, PR.IR-04, RS.MA-01, RS.AN-03.
*(RC.RP-01 anchors the recovery-plan-execution leg (Art. 11(2)/(3)
response and recovery plans); RC.RP-04 anchors the recovery-plans-
executed leg (Art. 12(1) restoration procedures + backup policies);
PR.IR-04 anchors the adequate-resource-capacity leg for backup
frequency and scope; PR.IR-03 anchors the network-resources-
prioritised leg for criticality-based backup scope.)*

---


## Security Requirements (DORA)

#### 4.2.4 — Financial-entity BC arrangements with response/recovery plans, backup policies, restoration procedures, and independent internal audit

```yaml
- req_id: 4.2.4
  volere_section: 15
  volere_subtype: immunity

  title: "Financial-entity BC arrangements: dedicated, appropriate and documented response/recovery plans + backup policies + restoration procedures; independent internal audit for non-microenterprises"

  derives_from:
    hso_sub_so: SO-4.2.DORA
    per_reg_so: SO-DORA-010
    source_sr: SR-DORA-013, SR-DORA-014, SR-DORA-016
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md
    objective_ref_section: "### 4.2.4"

  description: |
    The product shall operate a comprehensive ICT business continuity policy operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms — including ICT response and recovery plans (subject to independent internal audit for non-microenterprises per Art. 11(3)), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup based on criticality or confidentiality (per Art. 12(1)), and restoration and recovery procedures and methods (DORA Art. 11(1) + Art. 11(2) + Art. 11(3) + Art. 12(1)).

  fit_criterion: |
    A comprehensive ICT business continuity policy is established and implemented as an integral part of the overall business continuity policy of the financial entity; the BC arrangements are operationalised through a 4-way AND of artefacts per Art. 11(2) — response and recovery plans (RC.RP-01 recovery-plan-execution leg + RC.RP-04 recovery-plans-executed leg), backup policies and procedures (PR.IR-04 adequate-resource-capacity leg + PR.IR-03 network-resources-prioritised leg for criticality-based backup scope), restoration and recovery procedures and methods (RC.RP-04), and crisis-management actions; the `dedicated, appropriate and documented` qualifier from Art. 11(2) is operationalised as artefacts registered in the BC arrangements registry; for non-microenterprises, an independent internal audit of the BC arrangements (Art. 11(3)) is conducted and the audit records are inspection-ready; backup policies specify scope of data subject to backup and minimum frequency of backup based on criticality or confidentiality (Art. 12(1)); restoration and recovery procedures and methods are documented and tested; the DORA BC arrangements are the strictest containment-architecture floor in the AEGIS corpus (4-way AND of artefacts + independent internal audit for non-microenterprises); the DORA BC arrangements exceed the NIS 2 `contain` requirement for the financial-services subset of incidents; the GDPR Art. 33(3)(d) personal-data TOMs are documented as a section within the DORA BC arrangements (4.2-GDPR cross-ref), not as a separate runbook; for pure-financial entities, DORA absorbs the NIS 2 `contain` obligation for the financial-services subset via lex specialis; the BC arrangements discipline operates at the financial-entity boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), entity-level `contain` phase (NIS 2 leg) and product-design availability (CRA leg) documented as the controlled interfaces; verified by BC arrangements registry audit + Art. 11(2) 4-way AND artefact review + Art. 11(3) independent internal audit records (when non-microenterprise) + Art. 12(1) backup-policy + restoration-procedure documentation review + BC arrangements testing records inspection + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.4 (containment triggered by prior multi-layer detection event), 4.2.1 (when DORA-controller — GDPR Art. 33(3)(d) TOMs documented as section within DORA BC arrangements), 4.2.3 (when DORA FE deploys CRA product — CRA Annex I (2)(h)/(i)/(k) resilience design feeds DORA BC arrangements), 4.2.2 (when DORA + NIS 2 cross-sector — NIS 2 chapeau coverage is the additional layer for non-financial incidents; physical + operational hazards still bind via NIS 2)]

  nist_csf: [RC.RP-01, RC.RP-04, PR.IR-04, PR.IR-03, PR.DS-11, RC.RP-03]

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

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy forming an integral part of the overall business continuity policy of the financial entity. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19.

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.2: GDPR↔DORA = COMPLEMENTARY; NIS2↔DORA = COMPLEMENTARY; CRA↔DORA = COMPLEMENTARY)
```

### from regs/DORA.md body

- The BC arrangements measure object is distinct from the GDPR personal-data post-breach runbook, the NIS 2 entity-level lifecycle-phase actions, and the CRA product-design availability choices — the financial-entity BC boundary is internal to the ICT estate, and the BC arrangements discipline operates at that boundary only.

### from regs/DORA.md body

- For a multi-reg party, the DORA BC arrangements exceed the NIS 2 `contain` requirement for the financial-services subset of incidents; the GDPR Art. 33(3)(d) personal-data TOMs are documented as a section within the DORA BC arrangements (Doc 07 downstream implication), not as a separate runbook. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 `contain` requirement for the financial-services subset; the high-level SO does not aggregate across the lex-specialis boundary in that direction.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-controller; disjoint baseline: runbook ↔ BC arrangements; GDPR TOMs documented as section within DORA BC arrangements); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial lex specialis — DORA BC exceeds NIS 2 `contain` for financial-services subset); DORA↔CRA = Conditional (Y DORA FE deploys CRA product; disjoint baseline: BC arrangements ↔ product-level design); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA containment-and-mitigation obligation is the financial-entity BC arrangements architecture; the operational substrate is a comprehensive BC policy with dedicated, appropriate and documented arrangements including response and recovery plans, backup policies, and restoration procedures; the BC arrangements are subject to independent internal audit for non-microenterprises (the audit requirement is DORA-unique — no other participating regulator imposes an audit obligation on the containment architecture). The BC arrangements measure object is distinct from the GDPR personal-data post-breach runbook, the NIS 2 entity-level lifecycle-phase actions, and the CRA product-design availability choices — the financial-entity BC boundary is internal to the ICT estate, and the BC arrangements discipline operates at that boundary only. For a multi-reg party, the DORA BC arrangements exceed the NIS 2 `contain` requirement for the financial-services subset of incidents; the GDPR Art. 33(3)(d) personal-data TOMs are documented as a section within the DORA BC arrangements, not as a separate runbook. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 `contain` obligation for the financial-services subset; the high-level SO does not aggregate across the lex-specialis boundary in that direction. The downstream notification cascade (Art. 19(1) competent-authority + Art. 19(3) client notification) is part of 4.3, not 4.2. (Copied from the HSO Considerations block of `### 4.2.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=2 -->
