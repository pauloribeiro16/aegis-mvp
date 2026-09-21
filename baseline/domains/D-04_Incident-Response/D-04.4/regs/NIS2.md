# D-04.4 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-013 | Business-continuity triad (BC + backup + DR + crisis management) ensuring the ability to restore availability and integrity of network and information systems and manage crises arising from significant incidents | Entity ICT systems; all-hazards approach (Art. 21(2) chapeau + Recital 56); Art. 21(2)(c); RC.RP-04 + PR.DS-11 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | entity-level BC framework (entity ICT systems, all-hazards; backup + DR + CM triad) | `business continuity, such as backup management and disaster recovery, and crisis management` (Art. 21(2)(c)) | `appropriate and proportionate` (Art. 21(1)) + all-hazards chapeau + Recital 56; BC plan + backup records + DR tests + CM records | BC plan + backup records + DR test results + CM records | Member State competent authority / CSIRT audit (no systematic internal-audit floor) | Art. 21(2)(c) + Art. 21(1) + Recital 56 |

## Sub-SO (NIS 2)

#### D-04.4.2 — Sub-SO for NIS 2

```yaml
id: SO-D-04.4.NIS2
subdomain: D-04.4
applies_to: [NIS2]
inherits_from: SO-NIS2-013
source_SR: SR-NIS2-019
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Business continuity, backup management, disaster recovery, and crisis management capabilities are maintained, ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents (Art. 21(2)(c); the `business continuity, such as backup management and disaster recovery, and crisis management` structure imposes an AND chain across the BC + backup + DR + CM triad).

**Considerations.**
- The NIS 2 restoration-and-recovery obligation is the entity-level BC triad (BC + backup + DR + CM, with `business continuity` and `crisis management` as the outer AND and `backup management` and `disaster recovery` as inner pillars per the `such as` opening); the operational substrate is a tested BC framework with the all-hazards chapeau extending the recovery envelope to operational + physical-environment + cyber hazards (Recital 56), and the `appropriate and proportionate` qualifier (Art. 21(1)) calibrates the recovery depth to the entity's risk classification.
**CSF anchors (from `SR-NIS2-019` v0.3 security_rationale):**
RC.RP-04, PR.DS-11.
*(RC.RP-04 anchors the recovery-execution substrate — recovery plan
with documented RTO/RPO calibrated to the Art. 21(1) `appropriate and
proportionate` analysis, with critical-mission-function restoration
discipline; PR.DS-11 anchors the backup-discipline substrate — backups
created on a defined cadence, protected against threats (including
ransomware), maintained across the technology lifecycle, and tested
for restorability on a defensible schedule. The two subcategories
together address the recovery-execution dimension and the
backup-discipline dimension of the BC/DR/CM triad; the BC plan +
backup records + DR test results + CM records supply the operational-
continuity evidence base and the Art. 21(1) accountability artefact.
ISO 22301 (BCMS) and ISO 22361 (crisis management) are the recognised
methodological anchors cross-referenced in the SR's `regulatory_rationale`.)*

---


## Security Requirements (NIS 2)

#### 4.4.2 — Entity-level BC + backup + DR + CM triad with all-hazards scope

```yaml
- req_id: 4.4.2
  volere_section: 15
  volere_subtype: immunity

  title: "Entity-level business continuity, backup management, disaster recovery, and crisis management triad maintained with all-hazards scope and risk-tiered depth"

  derives_from:
    hso_sub_so: SO-4.4.NIS2
    per_reg_so: SO-NIS2-013
    source_sr: SR-NIS2-019
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md
    objective_ref_section: "### 4.4.2"

  description: |
    The product shall maintain business continuity, backup management, disaster recovery, and crisis management capabilities — ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents — under the `appropriate and proportionate` qualifier (Art. 21(1)) with the all-hazards chapeau (Art. 21(2) + Recital 56) extending the recovery envelope to operational + physical-environment + cyber hazards, and the BC + backup + DR + CM triad documented in BC plan + backup records + DR test results + CM records (NIS 2 Art. 21(2)(c) + Art. 21(1) `appropriate and proportionate` + all-hazards chapeau + Recital 56; the `such as backup management and disaster recovery, and crisis management` structure imposes an AND chain across the four pillars).

  fit_criterion: |
    An entity-level BC framework is maintained with the four-pillar BC + backup + DR + CM triad as the operational vehicle; a tested BC plan is produced documenting scenarios (operational + physical-environment + cyber hazards per Recital 56 all-hazards); backup records demonstrate PR.DS-11 backup creation (defined cadence), protection (encryption-at-rest + immutable storage + ransomware-resistant retention + offsite replication with RPO alignment), maintenance across the technology lifecycle, and tested restorability on a defensible schedule; DR test results demonstrate RC.RP-04 critical-mission-function restoration with documented RTO/RPO per activity calibrated to the Art. 21(1) `appropriate and proportionate` analysis; CM records demonstrate crisis-management discipline for incidents beyond ICT (operational + physical-environment hazards); high-risk roles / systems trigger deeper recovery depth per risk-tier mapping; the BC framework cadence operationalises the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) on non-financial parties — the tested recovery-exercise records are the measurable implementation; on DORA + NIS 2 parties, the DORA Art. 11–12 BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset (DORA is lex specialis on pure-financial entities) but the NIS 2 all-hazards chapeau extends beyond ICT (operational + physical-environment hazards), with the high-level SO not aggregating across the lex-specialis boundary in the ICT-hazard direction; on CRA + NIS 2 parties, CRA Annex I Part I (2)(h) product-internal resilience reduces the load on the NIS 2 entity-level BC framework via deployment (the product continues to function during/after attack); ISO 22301 (BCMS) and ISO 22361 (crisis management) are recognised methodological anchors cross-referenced in the `SR-NIS2-019` `regulatory_rationale`; verified by BC plan + backup records + DR test results + CM records review + Art. 21(1) `appropriate and proportionate` calibration documentation + all-hazards scenario coverage audit + risk-tier mapping review + MS competent-authority / CSIRT inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.2.2 (recovery depends on prior containment discipline feeding BC framework invocation), 4.1.2 (recovery depends on prior awareness event from 4.1 detection leg)]

  nist_csf: [RC.RP-04, PR.DS-11]

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
> Article 21(2)(c) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management (OJ L 333, 27.12.2022, p. 127).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.4: GDPR↔NIS2 = COMPLEMENTARY; NIS2↔CRA = COMPLEMENTARY; NIS2↔DORA = CORRECTED — was EQUAL → COMPLEMENTARY (DORA-specific overlay))
```

### from regs/NIS2.md body

- The BC-framework object is distinct from the GDPR personal-data-availability outcome, the CRA product-internal resilience, and the DORA financial-entity BC framework + backup-architecture — the entity-boundary BC framework is the operational vehicle that delivers the recovery cadence; on a NIS 2 + DORA party, the DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT-hazard subset (DORA is lex specialis on pure-financial entities); the NIS 2 all-hazards chapeau extends beyond ICT (operational + physical-environment hazards).

### from regs/NIS2.md body

- A NIS 2 BC framework operationalises the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for non-financial parties — the BC framework cadence + tested recovery-exercise records supply the measurable evidence base. CRA Annex I Part I (2)(h) product-internal resilience feeds into the NIS 2 BC framework via deployment (CRA products instrument their intra-product resilience to reduce the load on the entity's BC framework).

### from regs/NIS2.md body

- The NIS 2 BC framework does NOT have a dedicated independent-internal-audit floor (the supervisory authority / CSIRT evidence path is the audit channel; Member State transposition may add internal-audit obligations on a national basis); for DORA + NIS 2 cross-sector parties, DORA Art. 11(3) independent internal audit for non-microenterprises operates as the verification floor on the joint BC framework.


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y controller-NSIE; NIS 2 BC framework operationalises GDPR `timely`); NIS2↔CRA = Conditional (Y NIS 2 entity deploys/manufactures CRA products; disjoint baseline: entity ↔ product; CRA product-internal resilience feeds NIS 2 BC framework via deployment, reduces load); NIS2↔DORA = CORRECTED (was EQUAL → COMPLEMENTARY (DORA-specific overlay); on DORA + NIS 2 parties, DORA Art. 11–12 BC framework absorbs NIS 2 BC/DR/CM for ICT subset via lex specialis on pure-financial entities, with NIS 2 all-hazards chapeau extending beyond ICT; cross-sector: parallel tracks with NIS 2 chapeau + DORA-specific overlay); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 restoration-and-recovery obligation is the entity-level BC triad (BC + backup + DR + CM, with `business continuity` and `crisis management` as the outer AND and `backup management` and `disaster recovery` as inner pillars per the `such as` opening); the operational substrate is a tested BC framework with the all-hazards chapeau extending the recovery envelope to operational + physical-environment + cyber hazards (Recital 56), and the `appropriate and proportionate` qualifier (Art. 21(1)) calibrates the recovery depth to the entity's risk classification. The BC-framework object is distinct from the GDPR personal-data-availability outcome, the CRA product-internal resilience, and the DORA financial-entity BC framework + backup-architecture — the entity-boundary BC framework is the operational vehicle that delivers the recovery cadence; on a NIS 2 + DORA party, the DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT-hazard subset (DORA is lex specialis on pure-financial entities); the NIS 2 all-hazards chapeau extends beyond ICT (operational + physical-environment hazards). The NIS 2 BC framework does NOT have a dedicated independent-internal-audit floor (the supervisory authority / CSIRT evidence path is the audit channel; Member State transposition may add internal-audit obligations on a national basis); for DORA + NIS 2 cross-sector parties, DORA Art. 11(3) independent internal audit for non-microenterprises operates as the verification floor on the joint BC framework (the DORA-specific overlay is material and means DORA is NOT co-extensive with NIS 2 — the correction from EQUAL to COMPLEMENTARY captures this). The NIS 2 BC framework is the operational vehicle that discharges the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for non-financial parties and the CRA Annex I (2)(h) product-internal resilience feeds into the NIS 2 BC framework via deployment. (Copied from the HSO Considerations block of `### 4.4.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=6; core_cross_mentions=1 -->

