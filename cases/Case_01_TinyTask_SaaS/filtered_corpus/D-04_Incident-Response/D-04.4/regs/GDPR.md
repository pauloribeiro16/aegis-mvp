# D-04.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-014 | Timely restoration of availability and access to personal data after physical or technical incident (with continuing confidentiality, integrity and resilience of processing systems) | Personal-data availability; controller/processor; Art. 32(1)(b)+(c) + Art. 5(1)(f) (cross) + Art. 32(2) risk-enumeration (cross); PR.IR-04 + PR.DS-11 + RC.RP-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data-availability outcome (controller-side, personal-data availability + integrity + resilience of processing systems) | `timely manner` (Art. 32(1)(c)) — VAG (resolved by layered BC framework cadence) | RTO/RPO defined per processing activity; tested recovery objectives | recovery-exercise records under Art. 5(2) + Art. 32 documentation; backup-test results | supervisory authority inspection (Art. 58) — not systematic | Art. 32(1)(c) + Art. 5(1)(f) (cross) + Art. 32(2) (cross) |

## Sub-SO (GDPR)

#### D-04.4.1 — Sub-SO for GDPR

```yaml
id: SO-D-04.4.GDPR
subdomain: D-04.4
applies_to: [GDPR]
inherits_from: SO-GDPR-014
source_SR: SR-GDPR-024
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(b) + Art. 32(1)(c); Art. 5(1)(f) integrity/confidentiality cross-reference; Art. 32(2) five-event risk-enumeration cross).

**Considerations.**
- The GDPR restoration-and-recovery obligation is the personal-data-availability outcome of the controller; the operational substrate is a tested recovery capability with per-processing-activity RTO/RPO targets, where tested backups (PR.DS-11) and recovery-execution evidence (RC.RP-04) are the verifiable artefacts the supervisory authority may inspect under Art. 58 to confirm Art. 5(2) accountability.
**CSF anchors (from `SR-GDPR-024` v0.3 security_rationale):**
PR.IR-04, PR.DS-11, RC.RP-04.
*(PR.IR-04 anchors the resource-capacity dimension — adequate
resource headroom to absorb incident and recover availability within
the documented RTO; PR.DS-11 anchors the backup-discipline foundation
— created, integrity-protected, maintained and tested; RC.RP-04 closes
the recovery-execution cycle — tested recovery plan with documented
Recovery Point Objectives per activity. The three subcategories
together operationalise the Art. 32(1)(c) `timely manner`
restoration duty via the capacity + backup + recovery-execution
triad; Art. 32(2) five-event risk-enumeration cross-anchors the
trigger assessment; Art. 5(2) accountability closes the
supervisory-authority evidence loop.)*

---


## Security Requirements (GDPR)

#### 4.4.1 — Personal-data availability restored in `timely manner` with tested recovery-exercise evidence

```yaml
- req_id: 4.4.1
  volere_section: 15
  volere_subtype: immunity

  title: "Personal data availability and access restored in `timely manner` after physical or technical incident, with tested recovery-exercise evidence discharging Art. 5(2) accountability"

  derives_from:
    hso_sub_so: SO-4.4.GDPR
    per_reg_so: SO-GDPR-014
    source_sr: SR-GDPR-024
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md
    objective_ref_section: "### 4.4.1"

  description: |
    The product shall ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (Art. 32(1)(b)) and shall restore the availability of and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(c)), with the recovery evidence produced by tested recovery exercises (PR.IR-04 adequate resource capacity + PR.DS-11 backup creation + protection + maintenance + testing + RC.RP-04 critical mission functions restored) supplying the Art. 5(2) accountability evidence the supervisory authority may inspect under Art. 58 (GDPR Art. 32(1)(b) + Art. 32(1)(c) + Art. 5(1)(f) integrity/confidentiality cross-reference + Art. 32(2) five-event risk-enumeration cross; `timely manner` VAG anchor resolved by per-reg operationalising framework — NIS 2 BC framework cadence for NIS 2 + GDPR parties; DORA Art. 12 backup-tiering for DORA + GDPR parties; per-activity RTO/RPO for GDPR-only parties).

  fit_criterion: |
    A tested-recovery-exercise capability is operated with documented per-processing-activity RTO/RPO targets under PR.IR-04 adequate-resource-capacity substrate (resource headroom to absorb incident and recover availability within the documented RTO) + PR.DS-11 backup-discipline substrate (backups created on defined cadence, integrity-protected, maintained across technology lifecycle, tested for restorability on a defensible schedule with ransomware-resistant retention and offsite replication with RPO alignment) + RC.RP-04 recovery-execution substrate (tested recovery plan with documented RTO/RPO per activity, critical-mission-function restoration discipline, restore-confidence integrity verification before restoration); the five-event risk-enumeration cross (Art. 32(2)) anchors the trigger assessment — accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data — and the recovery exercise demonstrates that each risk class can be remediated within the documented RTO/RPO; the Art. 32 documentation expectations provide the supervisory-authority evidence base (Art. 58 inspection); the BC framework documentation + recovery-exercise records + backup-test results are the audit-grade artefacts; for GDPR-only parties (no NIS 2 / DORA applicability), the controller documents `timely manner` via tested per-activity RTO/RPO targets; for NIS 2 + GDPR parties, the NIS 2 BC framework cadence (BC plan + backup records + DR tests + CM records) operationalises the GDPR `timely` VAG anchor with tested recovery evidence for the personal-data subset; for DORA + GDPR parties, the DORA Art. 12(1)(a) backup-scoping on criticality/confidentiality + Art. 12(1)(b) restoration/recovery procedures + Art. 11(3) independent internal audit on non-microenterprises supply the measurable implementation; verified by per-processing-activity RTO/RPO documentation review + PR.DS-11 backup-test results inspection + RC.RP-04 recovery-exercise records audit + Art. 32 documentation-records review + Art. 5(2) accountability evidence pack + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.2.1 (recovery depends on prior containment classification — the five-event risk class determines which recovery pipeline fires), 4.1.1 (recovery depends on prior `becoming aware` trigger feeding the recovery-event classification)]

  nist_csf: [PR.IR-04, PR.DS-11, RC.RP-04]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim):**
> Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.4: GDPR↔NIS2 = COMPLEMENTARY; GDPR↔CRA = DIFFERENT-PERSPECTIVE; GDPR↔DORA = COMPLEMENTARY)
```

### from regs/GDPR.md body

- The `timely manner` anchor (Art. 32(1)(c)) is VAG (Recital 49 reads "as soon as possible", non-binding); operationalised via (a) tested recovery exercises for non-financial parties — the controller documents RTO per processing activity consistent with the BC framework — or (b) NIS 2 BC framework cadence on NIS 2 + GDPR parties — the NIS 2 BC plan + backup records + DR tests + CM records supply the operationalised evidence base. For a financial-entity + GDPR party, DORA Art. 12(1)(a) backup-scoping on criticality/confidentiality + Art. 12(1)(b) restoration/recovery procedures and methods resolve the `timely` VAG via the Art. 11(3) independent internal audit floor on non-microenterprises.

### from regs/GDPR.md body

- The personal-data-outcome object is distinct from the NIS 2 entity-level BC framework, the CRA product-internal resilience, and the DORA financial-entity BC framework + backup-architecture — the data-availability outcome is verified at the processing-system layer, and the restoration-and-recovery discipline operates at that layer.

### from regs/GDPR.md body

- The controller is responsible for the personal-data-outcome verification, not for the upstream architecture (which is shared with NIS 2 / DORA where applicable) or for the product-resilience layer (which is shared with CRA where applicable). The Art. 32 documentation expectations + Art. 5(2) accountability provide the supervisory-authority evidence path; BC framework documentation + recovery-exercise records + backup-test results are the audit-grade evidence base.


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-NSIE; NIS 2 BC framework operationalises GDPR `timely` for personal-data subset); GDPR↔CRA = Conditional (Y integrated manufacturer-controller; disjoint baseline: data-outcome ↔ product-resilience — CRA reduces probability of recovery trigger; controller still owns the recovery outcome); GDPR↔DORA = Conditional (Y DORA-FE processes personal data; disjoint baseline: data-outcome ↔ backup/restore architecture — DORA Art. 12 backup-tiering operationalises GDPR `timely` for personal-data subset); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR restoration-and-recovery obligation is the personal-data-availability outcome of the controller; the operational substrate is a tested recovery capability with per-processing-activity RTO/RPO targets, where tested backups (PR.DS-11) and recovery-execution evidence (RC.RP-04) are the verifiable artefacts the supervisory authority may inspect under Art. 58 to confirm Art. 5(2) accountability. The `timely manner` anchor (Art. 32(1)(c)) is VAG (Recital 49 reads "as soon as possible", non-binding); operationalised via (a) tested recovery exercises for non-financial parties — the controller documents RTO per processing activity consistent with the BC framework — or (b) NIS 2 BC framework cadence on NIS 2 + GDPR parties — the NIS 2 BC plan + backup records + DR tests + CM records supply the operationalised evidence base — or (c) DORA Art. 12(1)(a) backup-scoping on criticality/confidentiality + Art. 12(1)(b) restoration/recovery procedures + Art. 11(3) independent internal audit on non-microenterprises for DORA + GDPR parties. The personal-data-outcome object is distinct from the NIS 2 entity-level BC framework, the CRA product-internal resilience, and the DORA financial-entity BC framework + backup-architecture — the data-availability outcome is verified at the processing-system layer, and the restoration-and-recovery discipline operates at that layer. The Art. 32 documentation expectations + Art. 5(2) accountability provide the supervisory-authority evidence path; BC framework documentation + recovery-exercise records + backup-test results are the audit-grade evidence base. (Copied from the HSO Considerations block of `### 4.4.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=2 -->