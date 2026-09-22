# D-07.4 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-013 | Documented policies, procedures and controls for ICT change management — covering changes to software, hardware, firmware components, systems or security parameters — ensure that all changes are recorded, tested, assessed, approved, implemented and verified in a controlled manner, based on a risk assessment approach (Art. 9(4)(e) 5-way OR of change-targets + 6-way AND of change-management steps: recorded/tested/assessed/approved/implemented/verified + `controlled manner`). | **Entity-level change management**; **explicit OJ-mandate** under Art. 9(4)(e) (DORA is the only OJ-mandated dedicated authority for entity-level change-management-controls). The 6-step process is mandatory; the 5 change-target categories (software + hardware + firmware + systems + security parameters) are cumulative (S3 COORD). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-level change management — explicit OJ-mandate six-step process (recorded/tested/assessed/approved/implemented/verified in a controlled manner based on a risk-assessment approach) | financial-entity ICT change event (continuous — every software/hardware/firmware/systems/security-parameter change goes through the six-step process) | 5-way OR change-targets (software + hardware + firmware + systems + security parameters — R1 all five in scope per S3 COORD) + 6-way AND change-management steps (recorded + tested + assessed + approved + implemented + verified — R1 cumulative all six required per S3 COORD; partial-process compliance is non-compliance) + `controlled manner` (R1 documented procedure + segregated approval R3 both per S2 VAG) + `risk assessment approach` (qualitative); no quantitative cadence; no quantitative six-step cadence | competent authority (national financial supervisory authority) — Art. 9(4)(e) change-management policy + the six-step change-management record; management body on the Art. 5(2) management-body responsibility for all arrangements related to the ICT risk-management framework | Art. 9(4)(e) 5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate + EBA Guidelines on ICT and security risk management supervisory baseline + Art. 6(1) ICT risk-management framework + Art. 5(2) management-body responsibility |

## Sub-SO (DORA)

#### D-07.4.2 — Sub-SO for DORA

```yaml
id: SO-D-07.4.DORA
subdomain: D-07.4
applies_to: [DORA]
inherits_from: SO-DORA-013
source_SR: SR-DORA-023
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner (Art. 9(4)(e) DORA — 5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate).

**Considerations.**
- The 6-step change-management process is operationalised as: (1) recorded — every change to ICT systems is recorded; (2) tested — every change is tested before implementation (with documented test results); (3) assessed — every change is assessed for risk and impact (with documented assessment); (4) approved — every change is approved by an appropriate authority before implementation (with documented approval); (5) implemented — every change is implemented with documented implementation record; (6) verified — every change is verified post-implementation with documented verification.
- The 6 steps are cumulative (R1 all six required per S3 COORD) — partial-process compliance is non-compliance.
- The `controlled manner` qualifier (R1 documented procedure + segregated approval R3 both per S2 VAG) is read as the combination of documented procedure and segregated approval.
- The 5 change-target categories (software + hardware + firmware components + systems + security parameters) are cumulative (R1 all five in scope per S3 COORD).
- The `based on a risk assessment approach` is the operational anchor — the change-management six-step is calibrated by the risk assessment under Art. 6(1) + Art. 7(2) + Art. 8(2) + EBA Guidelines on ICT and security risk management supervisory baseline.
- For a 5-FTE DORA financial entity, the change-management obligation is the Art. 9(4)(e) six-step process with EBA Guidelines supervisory baseline + the Art. 6(1) ICT risk-management framework.
- **Caveat (D-07.2 cross-references via SR-DORA-023 partial):** the change-management six-step's `tested` + `assessed` legs + Art. 25 testing modalities (source-code reviews where feasible as one of 12 modalities) imply a secure-coding dimension (D-07.2 cross-reference partial); no OJ-mandated coding-standards prescription. Layer 2 review item preserved at D-07.2: AEGIS-taxonomy §4.1 DORA sole-authority disagreement has no OJ-text support.

**CSF anchors (from `SR-DORA-023` v0.3 security_rationale):**
PR.PS-01, PR.PS-02, PR.PS-06.
*(The Art. 9(4)(e) change-management duty is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** + **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** + **PR.PS-06 (secure software development practices integrated and monitored throughout the SDLC)**. PR.PS-01 anchors the documented-policy substrate (golden baselines, drift detection, configuration-as-code) that operationalises the `controlled manner` qualifier across the 5 change-target categories. PR.PS-02 supplies the commensurate-with-risk axis that the OJ `risk assessment approach` demands — change decisions are weighted by impact and likelihood rather than treated uniformly. PR.PS-06 closes the SDLC integration loop (the `tested, assessed, approved` stages of the six-step process tie back to secure-development practices upstream + verified-deployment evidence downstream). The three subcategories together convert a paper change-approval workflow into an evidence-backed governance discipline covering the full change-target surface, and an entity documenting PR.PS-01 + PR.PS-02 + PR.PS-06 coverage can demonstrate ex post that the Art. 9(4)(e) six-step process — recorded, tested, assessed, approved, implemented, verified — was anchored in platform-security configuration practice and proportionate to risk across the SDLC. The DORA-side CSF mapping is dual-mapping on PR.PS-02 (cross to D-07.4) + cross to D-07.2 partial via SR-DORA-023 inference (P0 DORA-taxonomy-disagreement preserved at D-07.2 per `CRDA/D-07_Secure-Development/D-07.2.md` line 54).)*

---


## Security Requirements (DORA)

#### 7.4.2 — Entity-side ICT change-management records

```yaml
- req_id: 7.4.2
  volere_section: 15
  volere_subtype: audit

  title: "Entity-side ICT change records demonstrate controlled, risk-based change execution"

  derives_from:
    hso_sub_so: SO-D-07.4.DORA
    per_reg_so: SO-DORA-013
    source_sr: SR-DORA-023
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md
    objective_ref_section: "### D-07.4.2"

  description: |
    The product shall maintain auditable ICT change records showing that DORA-relevant changes to the entity's ICT environment follow the required risk-based change lifecycle from request through post-implementation verification.

  fit_criterion: |
    For 100% of in-scope ICT changes, the change ticket contains requester, affected asset or parameter, risk assessment, test evidence, approver, implementation evidence, verification result, emergency-change flag if applicable, segregation-of-duty check, rollback decision, and immutable audit timestamp.

  priority: MUST
  verification_method: INSPECT
  dependencies: [7.3]

  nist_csf: [PR.PS-01, PR.PS-02, PR.PS-06]

  applicable_if:
    regs: [DORA]
    scope_overlap: conditional

  satisfaction:
    controls: []
    nodes: []

  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md` and `../../Regulation/DORA/02_SecurityRules_NIST.md` for the DORA-side target object, caveats, and inherited SR rationale; not duplicated here.
```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 9(4)(e)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (SAME) with Conditional Y scope overlap on the substantial-modification trigger event (CRDA-deep, D-07.4: CRA↔DORA = COMPLEMENTARY (SAME — entity-level change-management six-step via Art. 9(4)(e) 5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate vs product-level series-production conformity via Art. 13(14) + substantial-modification = manufacturer via Art. 21-22; Conditional Y scope overlap on the substantial-modification trigger event when a DORA financial entity customises a CRA-conformant product — Art. 22 third-party substantial-modification = manufacturer; N (typically) on the simple supplier-customer boundary; **AEGIS taxonomy §4.1 sole-authority disagreement**: AEGIS marks DORA as SOLE AUTHORITY; CRDA-deep finds CRA Art. 13(14) + Art. 21-22 constitute dedicated authorities for the substantial-modification trigger; preserved as co-equal participation)
```

### from regs/DORA.md body

- The DORA-side participation at D-07.4 is the unique OJ-mandated dedicated authority for entity-level change-management controls — Art. 9(4)(e) is the only OJ-verbatim dedicated change-management mandate (no equivalent OJ mandate in CRA on the entity-level change-management dimension).

### from regs/DORA.md body

- For a DORA financial entity that customises a CRA-conformant product (Conditional-Y substantial-modification trigger event), the entity-side six-step process operates on top of the CRA-side substantial-modification trigger (Art. 22 third-party substantial-modification = manufacturer — the DORA entity becomes a CRA-manufacturer-equivalent with the attendant obligations: Art. 13 conformity-assessment + Art. 14 AEV/SI notification + Annex I compliance + Annex VII technical documentation + Art. 13(8) support period) with layered documentation.

### from regs/DORA.md body

- For a DORA financial entity that does not customise CRA-conformant products (simple supplier-customer boundary), the entity-side six-step process operates on the financial-entity ICT-infrastructure changes with the DORA six-step documentation serving as the change-management evidence trail for the entity's CRA-conformant product procurements when substantively the same change event is recorded on both sides.

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=0 -->