# D-07.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations (Art. 13(14) + Art. 21-22 + Art. 3(30) + Art. 13(10)). | **Product-level change management across series production** + **substantial-modification trigger with manufacturer-equivalent consequences** (Art. 22 third-party substantial-modification = manufacturer). The substantial-modification trigger (Art. 3(30) D30 — VAG+POLY+COORD-S3) fires the manufacturer-equivalent status transfer when a third party carries out a substantial modification and makes that product available on the market (Art. 22(1)) or when an importer/distributor places a product on the market under its own name/trademark or carries out a substantial modification (Art. 21). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level change management across series production (Art. 13(14) continuous) + substantial-modification consequences (Art. 21-22 TRIGGERED) + substantial-modification compliance scope (Art. 13(10) TRIGGERED) + immediate corrective measures (Art. 13(21) TRIGGERED) | manufacturer series-production event (continuous) + substantial-modification event (TRIGGERED — Art. 3(30) substantial-modification definition) + manufacturer-equivalent trigger (Art. 21 importer/distributor trigger + Art. 22(1) third-party substantial-modification = manufacturer) + correction-event trigger (Art. 13(21) where manufacturer knows/has-reason-to-believe non-conformity) | `procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation` (Art. 13(14)) + `substantial modification` (Art. 3(30) D30 — VAG+POLY+COORD-S3: R1 (any non-compliance change) + R3 (intended-purpose modification) disjunctive literal reading) + `where the manufacturer knows or has reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity` (Art. 13(21)) — qualitative thresholds; no quantitative cadence | market surveillance authority (MSA) — Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record + Art. 13(22) MSA cooperation + Art. 14(1)/(3)/(8) AEV/SI/user-notification flows when a substantial modification creates an actively-exploited-vulnerability or severe-incident event; the user/customer as direct recipient of the change-management-related outputs (CRA-side documentation) | Art. 13(14) series-of-production conformity + Art. 3(30) substantial-modification definition + Art. 21 manufacturer-equivalent trigger + Art. 22(1) third-party substantial-modification = manufacturer + Art. 22(2) scope of obligations + Art. 13(10) substantial-modification compliance scope + Art. 13(21) immediate corrective measures + Annex VII §2 + Annex VII §3 + Art. 13(22) MSA cooperation |

## Sub-SO (CRA)

#### D-07.4.1 — Sub-SO for CRA

```yaml
id: SG-D-07.4.CRA
subdomain: D-07.4
applies_to: [CRA]
inherits_from: SG-CRA-047
source_SR: SR-CRA-069 (Art. 13(14) series-production + SR-CRA-070 Art. 13(10) + 21-22 substantial-modification)
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The manufacturer of a product with digital elements that is part of a series of production ensures that procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation (Art. 13(14) CRA).

**Considerations.**
- An importer or distributor who places a product with digital elements on the market under its own name or trademark, or who carries out a substantial modification of a product with digital elements already placed on the market, is considered to be the manufacturer for the purposes of the Regulation and assumes the manufacturer's obligations under Arts. 13 and 14 (Art. 21 CRA).
- A natural or legal person, other than the manufacturer, importer, or distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market, is considered to be the manufacturer for the purposes of the Regulation, with obligations attaching to the affected part or — where the substantial modification has an impact on the cybersecurity of the product as a whole — to the entire product (Art. 22(1)+(2) CRA).
- The substantial-modification definition under Art. 3(30) (D30 — VAG+POLY+COORD-S3) is the boundary between normal-version-update and manufacturer-equivalent liability transfer.
- Art. 13(10) substantial-modification compliance scope carve-out allows the manufacturer to ensure Annex I Part II (2) compliance for the version last placed on the market subject to user-migration conditions (user is given the choice to migrate to the modified product or retain the last-placed version, with access to the last-placed version free of charge + no additional costs to adjust the hardware/software environment).
- Art. 13(21) immediate corrective measures duty requires the manufacturer to immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product (cross to D-04.2 — `SG-CRA-063`).
**CSF anchors (from `SR-CRA-069` v0.3 security_rationale — Art. 13(14) series-production + `SR-CRA-070` v0.3 security_rationale — Art. 13(10) + 21-22 substantial-modification + `SR-CRA-081` v0.3 security_rationale — Art. 13(7)/(14) always-current record):**
GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04.

---


## Security Requirements (CRA)

#### 7.4.1 — Product-side series-production and substantial-modification records

```yaml
- req_id: 7.4.1
  volere_section: 15
  volere_subtype: audit

  title: "Product-side change records preserve series-production conformity and substantial-modification decisions"

  derives_from:
    hso_sub_so: SG-D-07.4.CRA
    per_reg_so: SG-CRA-047
    source_sr: SR-CRA-069, SR-CRA-070, SR-CRA-081
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md
    objective_ref_section: "### D-07.4.1"

  description: |
    The product shall maintain auditable product-side change records that preserve series-production conformity decisions, substantial-modification assessments, and manufacturer-equivalent status determinations for CRA-regulated products.

  fit_criterion: |
    For 100% of product changes, the change record contains product/version identifier, change classification, substantial-modification decision, conformity-impact assessment, affected technical-documentation reference, responsible role, approval decision, corrective-action link where applicable, and retention location for market-surveillance inspection.

  priority: MUST
  verification_method: INSPECT
  dependencies: [7.3.2]

  nist_csf: [GV.OV-01, GV.PO-02]

  applicable_if:
    regs: [CRA]
    scope_overlap: conditional

  satisfaction:
    controls: []
    nodes: []

  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md` and `../../Regulation/CRA/02_SecurityRules_NIST.md` for the CRA-side target object, caveats, and inherited SR rationale; not duplicated here.
```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 13(14) + Art. 21-22):**
> "Manufacturers of products with digital elements that are part of a series of production shall ensure that … such products remain in conformity with this Regulation. The manufacturer shall also ensure that procedures are in place for series of production to remain in conformity, including, where applicable, procedures for …" — Art. 13(14) CRA (per SR-CRA-069 reading; SR-CRA-070 covers substantial-modification)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (SAME) with Conditional Y scope overlap on the substantial-modification trigger event (CRDA-deep, D-07.4: CRA↔DORA = COMPLEMENTARY (SAME — product-level series-production conformity via Art. 13(14) + substantial-modification = manufacturer via Art. 21-22 + substantial-modification compliance scope via Art. 13(10) + immediate corrective measures via Art. 13(21) vs entity-level change-management six-step via Art. 9(4)(e) 5-way OR change-targets + 6-way AND change-management steps; Conditional Y scope overlap on the substantial-modification trigger event when a DORA financial entity customises a CRA-conformant product — Art. 22 third-party substantial-modification = manufacturer; N (typically) on the simple supplier-customer boundary)
```

### from regs/CRA.md body

- The CRA-side participation at D-07.4 is preserved as co-equal participation rather than as partial-coverage cross-ref per CRA `03_validation_report.md` line 177 — the substantial-modification trigger with manufacturer-equivalent consequences (Art. 22 third-party substantial modification = manufacturer) is a dedicated authority for the substantial-modification dimension that complements the DORA-side entity-level change-management six-step.

### from regs/CRA.md body

- For an integrated manufacturer that is also a DORA financial entity (Conditional-Y substantial-modification trigger event), the manufacturer-equivalent status transfer (Art. 22) applies on top of the DORA-side six-step process (Art. 9(4)(e)) with layered documentation (DORA six-step record + CRA Art. 13(14) series-production record + substantial-modification assessment per Art. 13(10) + Annex VII technical-documentation update). On the simple supplier-customer boundary (no substantial modification), the DORA-side six-step record can serve as the evidence trail for CRA Art. 13(14) series-production conformity when substantively the same change event is recorded on both sides.


### from regs/CRA.md body

*(The Art. 13(14) series-of-production conformity duty is operationalised in NIST CSF 2.0 through **GV.OV-01 (cybersecurity risk management strategy outcomes reviewed and adjusted to ensure they adequately address organisational risks)** + **GV.PO-02 (cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** — GV.OV-01 anchors the strategy-outcomes-review dimension (series-production conformity procedure reviewed and adjusted); GV.PO-02 anchors the process layer (series-production conformity procedure implemented as a documented process with operational discipline, evidence in Annex VII §2). The Art. 13(10) + 21-22 substantial-modification architecture is operationalised through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** + **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)** — PR.PS-02 captures the version-management dimension (substantial-modification threshold is the boundary between normal-version-update and manufacturer-equivalent liability transfer); GV.SC-04 anchors the supply-chain-coordination dimension (importer/distributor/third-party modifier assessments via Art. 21-22). The Art. 13(7)/(14) always-current record is operationalised through **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes)** + **ID.IM-04 (cybersecurity risk management improvements informed by awareness of related developments)** — GV.OV-02 anchors the periodic re-baselining of the risk assessment when the threat/regulatory/standards landscape shifts; ID.IM-04 anchors the intake of new third-party information (vulnerability advisories, OSS-steward disclosures, CSIRT alerts, CVD reports) into the record. The four pairs of subcategories together enable the manufacturer to demonstrate ex post, through documented series-production conformity procedure + substantial-modification assessment record + Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record + Art. 13(10) compliance-scope record + Art. 13(21) immediate-corrective-measures record + the always-current record that the (14) + (10) + (21) + (7) series-production conformity + substantial-modification + always-current duties have been discharged in coordination with the DORA-side six-step on the Conditional-Y substantial-modification trigger event.)*

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=0 -->
