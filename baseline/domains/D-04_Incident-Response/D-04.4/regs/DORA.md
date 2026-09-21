# D-04.4 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-010 | Comprehensive ICT BC policy with dedicated arrangements/plans/procedures/mechanisms including ICT response and recovery plans (independent internal audit for non-microenterprises), backup policies with criticality/confidentiality-graded scope and minimum frequency, and restoration and recovery procedures and methods | Financial entity; BC framework + backup architecture + audit-verified arrangements; Art. 11(1)–(3) + Art. 12(1); RC.RP-01 + PR.IR-03 + RC.RP-04 + PR.IR-04 + PR.DS-11 + RC.RP-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity ICT BC framework + backup-architecture on criticality/confidentiality + restoration methods | `comprehensive ICT business continuity policy` (Art. 11(1)) + `dedicated, appropriate and documented arrangements, plans, procedures and mechanisms` (Art. 11(2)) + `backup policies and procedures … based on the criticality of information or the confidentiality level of the data` (Art. 12(1)(a)) | risk-based via criticality or confidentiality tiering; tiered backup cadences (Tier 1 critical, Tier 2 standard, Tier 3 reporting) | BC policy + recovery plans + backup-and-restoration documentation + audit-review records | **independent internal audit (Art. 11(3) — non-microenterprises)** — systematic second-line / third-line assurance floor | Art. 11(1)–(3) + Art. 12(1) |

## Sub-SO (DORA)

#### D-04.4.4 — Sub-SO for DORA

```yaml
id: SO-D-04.4.DORA
subdomain: D-04.4
applies_to: [DORA]
inherits_from: SO-DORA-010
source_SR: SR-DORA-013, SR-DORA-014, SR-DORA-015
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms, including ICT response and recovery plans (subject to independent internal audit review for non-microenterprises, Art. 11(3)), backup policies and procedures specifying the scope of the data subject to backup and the minimum frequency of the backup, based on the criticality of information or the confidentiality level of the data (Art. 12(1)(a)), and restoration and recovery procedures and methods (Art. 12(1)(b)).

**Considerations.**
- The DORA restoration-and-recovery obligation is the financial-entity ICT BC framework with backup-architecture on criticality/confidentiality + restoration/recovery procedures + audit verification on non-microenterprises; the operational substrate is a comprehensive BC policy (Art. 11(1)) operationalised via dedicated-and-documented arrangements, plans, procedures and mechanisms (Art. 11(2) 3-way AND of adjectives + 4-way AND of artefact types), with response and recovery plans as distinct artefacts (Art. 11(3); independent internal audit review for non-microenterprises), backup policies on criticality or confidentiality (Art. 12(1)(a) — the measurable backup-tier calibration), and restoration and recovery procedures and methods (Art. 12(1)(b) — the technical-and-service coordination).

**CSF anchors (from `SR-DORA-013` + `SR-DORA-014` + `SR-DORA-015`
v0.3 security_rationale):**
RC.RP-01, PR.IR-03, RC.RP-04, PR.IR-04, PR.DS-11, RC.RP-03.
*(From `SR-DORA-013` (Art. 11(1) BC policy): RC.RP-01 anchors the
recovery-execution dimension — the BC policy specifies the criteria
under which recovery transitions from incident-response to recovery-mode;
PR.IR-03 supplies the broader resilience-mechanism substrate.
From `SR-DORA-014` (Art. 11(2)+(3) implementation arrangements +
independent audit review): RC.RP-04 anchors the recovery-execution
layer — the documented arrangements/plans/procedures/mechanisms
(4-way AND) operationalise the five-objective Art. 11(2)(a)–(e) list
into concrete recovery capability; PR.IR-04 supplies the
resource-capacity substrate — redundant compute, storage, network,
alternative-site capacity. From `SR-DORA-015` (Art. 12(1) backup +
restoration procedures): PR.DS-11 anchors the backup-creation and
protection layer — encryption-at-rest, immutable storage for
ransomware-resistant retention, offsite replication with RPO alignment;
RC.RP-03 closes the restore-confidence dimension — integrity
verification before restoration (Recital 57's testing-not-merely-
writing principle); RC.RP-04 anchors the service-restoration layer —
recovery plan operationalises restored data into running services.
The six subcategories together operationalise the DORA BC framework
+ backup-architecture + audit-verified arrangements + restoration
procedures as the financial-sector recovery strictest-floor in the
AEGIS corpus. The OJ Art. 12(1)(a) `based on criticality or
confidentiality` risk-based proportionality is operationalised through
tiered backup cadences — Tier 1 critical trading books synchronously
replicated, Tier 2 settlement data at high cadence, Tier 3 reporting
data at standard cadence.)*

---


## Security Requirements (DORA)

#### 4.4.4 — Comprehensive ICT BC policy + arrangements + backup-scoping + restoration procedures + OJ-corrected Art. 11(2)(a)–(e) objectives

```yaml
- req_id: 4.4.4
  volere_section: 15
  volere_subtype: immunity

  title: "Comprehensive ICT BC policy with dedicated appropriate documented arrangements + response/recovery plans + backup-scoping on criticality/confidentiality + restoration procedures; OJ-corrected Art. 11(2)(a)–(e) BC-policy objectives preserved verbatim"

  derives_from:
    hso_sub_so: SO-4.4.DORA
    per_reg_so: SO-DORA-010
    source_sr: SR-DORA-013, SR-DORA-014, SR-DORA-015
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md
    objective_ref_section: "### 4.4.4"

  description: |
    The product shall operationalise a comprehensive ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms (Art. 11(2) 3-way AND of adjectives + 4-way AND of artefact types = `arrangements, plans, procedures, mechanisms`), including ICT response and recovery plans (Art. 11(3); subject to independent internal audit review for non-microenterprises), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup, based on the criticality of information or the confidentiality level of the data (Art. 12(1)(a) — `criticality or confidentiality` basis), and restoration and recovery procedures and methods (Art. 12(1)(b)) (DORA Art. 11(1)–(3) + Art. 12(1); the OJ-corrected Art. 11(2)(a)–(e) objective list per `SR-DORA-014` v0.2 audit applies — (a) continuity of critical or important functions; (b) quick+appropriate+effective response/resolution; (c) without-delay activation of dedicated plans with containment measures; (d) preliminary impact/damage/loss estimation; (e) communication + crisis-management per Art. 14 + CA reporting per Art. 19).

  fit_criterion: |
    A comprehensive ICT BC framework is operated at the financial-entity ICT-infrastructure layer with the DORA `dedicated, appropriate and documented` 3-way AND + `arrangements + plans + procedures + mechanisms` 4-way AND + Art. 11(3) independent internal audit on non-microenterprises as the audit-verification floor; the Art. 11(2)(a)–(e) objective list is implemented with the OJ-corrected labels — (a) ensure the continuity of the financial entity's critical or important functions (continuity-of-critical-functions / operational continuity); (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions (response-and-resolution / rapid incident handling); (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident (plan-activation / without-delay containment per type of incident); (d) estimate preliminary impacts, damages and losses (impact-and-loss-estimation / preliminary, near-real-time); (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19 (communication-and-CA-reporting / per Art. 14 + Art. 19); a BC policy specifies the criteria under which recovery transitions from incident-response to recovery-mode (RC.RP-01); the documented arrangements/plans/procedures/mechanisms (4-way AND) operationalise the five-objective Art. 11(2)(a)–(e) list into concrete recovery capability (RC.RP-04); resource-capacity substrate (PR.IR-04 redundant compute + storage + network + alternative-site capacity); backup policies and procedures (Art. 12(1)(a)) specify the scope of data subject to backup and the minimum frequency, calibrated to the `criticality of information or the confidentiality level of the data` VAG with tiered backup cadences per `SR-DORA-015` — Tier 1 critical trading books synchronously replicated; Tier 2 settlement data at high cadence; Tier 3 reporting data at standard cadence; restoration and recovery procedures and methods (Art. 12(1)(b)) specify how restored data is operationalised into running services (RC.RP-04 service-restoration) with integrity verification before restoration (RC.RP-03 restore-confidence per Recital 57's testing-not-merely-writing principle); on GDPR + DORA parties, the DORA Art. 12(1)(a) backup-tiering on criticality/confidentiality + Art. 12(1)(b) restoration procedures + Art. 11(3) independent internal audit for non-microenterprises supply the measurable implementation of the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for the personal-data subset; on NIS 2 + DORA parties (cross-sector or pure-financial via lex specialis), the DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset, with the NIS 2 all-hazards chapeau extending beyond ICT (operational + physical-environment hazards); the DORA BC framework does NOT make DORA co-extensive with NIS 2 — the financial-sector overlay is material (response and recovery plans as distinct artefacts; risk-calibrated backup scoping; audit-verified BC arrangements); verified by Art. 11(1) BC policy review + Art. 11(2) arrangements + plans + procedures + mechanisms (4-way AND) arrangements registry audit + Art. 11(3) response-and-recovery-plans documentation + independent internal audit review records on non-microenterprises + Art. 12(1)(a) backup-scoping records on criticality/confidentiality + tiered-backup-cadence evidence + Art. 12(1)(b) restoration procedures inspection + Art. 11(2)(a)–(e) OJ-corrected objective-mapping documentation review + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.2.4 (recovery depends on prior BC-arrangements containment discipline from 4.2 leg), 4.1.4 (recovery depends on prior multi-layer detection + SPOF identification feeding recovery-event classification)]

  nist_csf: [RC.RP-01, RC.RP-03, RC.RP-04, PR.IR-03, PR.IR-04, PR.DS-11]

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
> Art. 12(1)(a) requires financial entities to develop and document backup policies and procedures specifying the scope of the data subject to backup and the minimum frequency of backup, based on the criticality of information or the confidentiality level of the data. Art. 12(1)(b) requires restoration and recovery procedures and methods.

**DORA article (verbatim):**
> Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a) continue critical operations, (b) recover from ICT-related incidents, (c) manage crises, (d) protect stakeholders, and (e) comply with regulatory obligations.
> [OJ-corrective note (v0.2 audit, material): Art. 11(2)(c)/(d)/(e) — BCP objectives mislabelled. OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) (manage crises, protect stakeholders, comply with regulatory obligations) do NOT match the OJ items.]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.4: GDPR↔DORA = COMPLEMENTARY; **NIS2↔DORA = CORRECTED — was EQUAL → COMPLEMENTARY (DORA-specific overlay)**; CRA↔DORA = COMPLEMENTARY)
```

### from regs/DORA.md body

- The DORA BC-framework object is distinct from the GDPR personal-data-availability outcome, the NIS 2 entity-level BC framework, and the CRA product-internal resilience — the financial-entity ICT-infrastructure boundary is internal to the ICT estate, and the BC-framework discipline operates at that boundary.

### from regs/DORA.md body

- A DORA-compliant BC framework discharges the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for the personal-data subset via the Art. 12(1)(a) backup-tier calibration + Art. 12(1)(b) restoration/recovery procedures + Art. 11(3) independent internal audit floor on non-microenterprises (the audit-verification dimension is material — the recovery arrangements are demonstrably operational, not merely aspirational).

### from regs/DORA.md body

- A DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset on DORA + NIS 2 parties (DORA is lex specialis on pure-financial entities); the DORA overlayer is material (response and recovery plans as distinct artefacts; risk-calibrated backup scoping; audit-verified BC arrangements — see DORA-correction flag below) and NOT co-extensive with NIS 2. For pure-financial entities (NIS 2 §9 fall-back does not apply), DORA absorbs the NIS 2 BC/DR/CM obligation for the ICT-hazard subset; the high-level SO does NOT aggregate across the lex-specialis boundary in that direction.


### from regs/DORA.md body

> **DORA-correction flag (preserved from CRDA-deep).** CRDA classified
> this pair as **EQUAL** (NIS 2 ↔ DORA on D-04.4). CRDA-deep verified
> the relationship as **COMPLEMENTARY (DORA-specific overlay)** because
> DORA is not merely the same BC obligation as NIS 2; DORA carries a
> financial-sector BC architecture with explicit `dedicated, appropriate
> and documented` arrangements/plans/procedures/mechanisms (Art. 11(2)
> 3-way AND + 4-way AND); response and recovery plans (Art. 11(3);
> independent internal audit review for non-microenterprises); backup-
> frequency criteria calibrated to `criticality of information or the
> confidentiality level of the data` (Art. 12(1)(a)); restoration and
> recovery procedures and methods (Art. 12(1)(b)); and audit expectations.
> A DORA-compliant programme satisfies NIS 2 for the overlapping ICT
> subset, but is not equal-to NIS 2.
>
> **OJ-corrective note (v0.2 audit, material) on DORA Art. 11(2)(c)/(d)/(e)**
> — preserved verbatim from `SR-DORA-014` `regulatory_rationale` and
> propagated from CRDA-deep §D-04.4 pair `NIS2 ↔ DORA`:
> OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the
> continuity of the financial entity's critical or important
> functions; (b) quickly, appropriately and effectively respond to,
> and resolve, all ICT-related incidents in a way that limits damage
> and prioritises the resumption of activities and recovery actions;
> (c) activate, without delay, dedicated plans that enable
> containment measures, processes and technologies suited to each
> type of ICT-related incident; (d) estimate preliminary impacts,
> damages and losses; (e) set out communication and crisis
> management actions that ensure that updated information is
> transmitted to all relevant internal staff and external stakeholders
> in accordance with Article 14, and report to the competent
> authorities in accordance with Article 19. The SR's labels for
> (c)/(d)/(e) as `manage crises`, `protect stakeholders`, `comply with
> regulatory obligations` (per the broader BC three-Cs reading) do NOT
> match the OJ items; the substantive classification (COMPLEMENTARY)
> is unaffected; the mapping between BC-policy objectives and the
> DORA sub-SO language must use the OJ-corrected (a)–(e) labels.
> **Furthermore**, this means the DORA BC objectives are operationalised
> as:
> - (a) → continuity-of-critical-functions (operational continuity)
> - (b) → response-and-resolution (rapid incident handling with damage
>   limitation and recovery-action prioritisation)
> - (c) → plan-activation (without delay, per type of incident)
> - (d) → impact-and-loss-estimation (preliminary, near-real-time)
> - (e) → communication-and-CA-reporting (per Art. 14 + Art. 19).
>
> The high-level SO surfaces the common restoration duty across all
> four regulators; the DORA-specific overlay is preserved verbatim in
> the audit-verification floor + Art. 12 backup-scoping on criticality
> or confidentiality + Art. 11(3) independent internal audit review
> for non-microenterprises + the OJ-corrected Art. 11(2)(a)–(e)
> objective list above.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-FE processes personal data; DORA Art. 12 backup-tiering operationalises GDPR `timely manner` for personal-data subset); DORA↔NIS2 = CORRECTED (was EQUAL → COMPLEMENTARY (DORA-specific overlay); pure-financial entities: DORA absorbs NIS 2 BC/DR/CM for ICT subset via lex specialis; cross-sector: DORA BC framework + NIS 2 all-hazards chapeau parallel fires; DORA strict BC overlay is material and preserved); DORA↔CRA = Conditional (Y DORA FE deploys/manufactures CRA products; disjoint baseline: financial-entity ICT ↔ product; both required, neither substitutes); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA restoration-and-recovery obligation is the financial-entity ICT BC framework with backup-architecture on criticality/confidentiality + restoration/recovery procedures + audit verification on non-microenterprises; the operational substrate is a comprehensive BC policy (Art. 11(1)) operationalised via dedicated-and-documented arrangements, plans, procedures and mechanisms (Art. 11(2) 3-way AND of adjectives + 4-way AND of artefact types), with response and recovery plans as distinct artefacts (Art. 11(3); independent internal audit review for non-microenterprises), backup policies on criticality or confidentiality (Art. 12(1)(a) — the measurable backup-tier calibration), and restoration and recovery procedures and methods (Art. 12(1)(b) — the technical-and-service coordination). The DORA BC-framework object is distinct from the GDPR personal-data-availability outcome, the NIS 2 entity-level BC framework, and the CRA product-internal resilience — the financial-entity ICT-infrastructure boundary is internal to the ICT estate, and the BC-framework discipline operates at that boundary. **DORA-correction flag (preserved from CRDA-deep):** CRDA classified this pair as EQUAL (NIS 2 ↔ DORA on 4.4); CRDA-deep verified the relationship as COMPLEMENTARY (DORA-specific overlay) because DORA is not merely the same BC obligation as NIS 2; DORA carries a financial-sector BC architecture with explicit `dedicated, appropriate and documented` arrangements + response/recovery plans as distinct artefacts + backup-frequency criteria on criticality or confidentiality + audit expectations. A DORA-compliant programme satisfies NIS 2 for the overlapping ICT subset, but is not equal-to NIS 2. **OJ-corrective note (v0.2 audit, material) on DORA Art. 11(2)(c)/(d)/(e)** — preserved verbatim from `SR-DORA-014` `regulatory_rationale` and propagated from CRDA-deep §4.4 pair NIS 2 ↔ DORA: OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) as `manage crises`, `protect stakeholders`, `comply with regulatory obligations` do NOT match the OJ items; the substantive classification (COMPLEMENTARY) is unaffected; the mapping between BC-policy objectives and the DORA sub-SO language uses the OJ-corrected (a)–(e) labels — (a) → continuity-of-critical-functions; (b) → response-and-resolution; (c) → plan-activation; (d) → impact-and-loss-estimation; (e) → communication-and-CA-reporting. A DORA BC framework discharges the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for the personal-data subset via the Art. 12(1)(a) backup-tier calibration + Art. 12(1)(b) restoration/recovery procedures + Art. 11(3) independent internal audit floor on non-microenterprises. A DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset on DORA + NIS 2 parties (DORA is lex specialis on pure-financial entities); the DORA overlayer is material and NOT co-extensive with NIS 2; the NIS 2 all-hazards chapeau still binds for operational + physical-environment hazards beyond ICT. (Copied from the HSO Considerations block of `### 4.4.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=1 -->

