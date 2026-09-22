# D-04.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-021 + SG-CRA-022 | Product availability preserved post-incident via resilience and DoS-resistance + cascading-impact minimisation + exploitation mitigation | Product with digital elements; manufacturer design; Annex I Part I (2)(h)/(i)/(k); PR.IR-04 + PR.IR-03 + DE.CM-09 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level post-incident availability + cross-product impact + exploitation mitigation | product-design choices (Annex I Part I (2)(h) DoS resilience; (2)(i) cross-product impact; (2)(k) exploitation mitigation) | continuous product design + post-incident availability preservation | CSIRT + ENISA (Art. 14 AEV/SI notification); product users (Art. 14(8) mitigation measures) | Annex I Part I (2)(h) + (2)(i) + (2)(k); Art. 13(21) corrective measures |

## Sub-SO (CRA)

#### D-04.2.3 — Sub-SO for CRA

```yaml
id: SG-D-04.2.CRA
subdomain: D-04.2
applies_to: [CRA]
inherits_from: SG-CRA-021
source_SR: SR-CRA-043, SR-CRA-044
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The availability of essential and basic functions of a product with digital elements is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer minimises the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)). Where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer takes the corrective measures necessary to bring the product into conformity, or to withdraw or recall the product (Art. 13(21)).

**Considerations.**
- The CRA containment-and-mitigation obligation is the product-level post-incident availability + cross-product impact + exploitation mitigation architecture; the operational substrate is a product-design framework that combines DoS resilience (Annex I Part I (2)(h)), cascading-impact minimisation (Annex I Part I (2)(i)), and exploitation-mitigation mechanisms (Annex I Part I (2)(k)). The three-clause constellation is CRA-unique and operates at the product-design level — the containment happens inside the product boundary.
- The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification; Art. 14(1)/(3) AEV/SI notification including corrective measures) is part of D-04.3, not D-04.2.

**CSF anchors (from `SR-CRA-043` + `SR-CRA-044` v0.3 security_rationale):**
PR.IR-03, ID.AM-08, GV.SC-04.
*(PR.IR-04 anchors the adequate-resource-capacity leg for DoS
resilience; PR.IR-03 anchors the network-resources-prioritised leg
for cross-product impact minimisation; DE.CM-09 anchors the
computing-hardware-monitored leg for exploitation-mitigation
mechanism effectiveness.)*

---


## Security Requirements (CRA)

#### 4.2.3 — Product-level post-incident availability + cross-product impact minimisation + exploitation mitigation

```yaml
- req_id: 4.2.3
  volere_section: 15
  volere_subtype: immunity

  title: "Product availability preserved after incident via resilience + DoS resistance + cross-product impact minimisation + exploitation mitigation; Art. 13(21) corrective measures on non-conformity"

  derives_from:
    hso_sub_so: SO-4.2.CRA
    per_reg_so: SG-CRA-021
    source_sr: SR-CRA-043, SR-CRA-044
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md
    objective_ref_section: "### 4.2.3"

  description: |
    The product shall protect the availability of essential and basic functions also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer shall minimise the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer shall reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)); where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer shall immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product (Art. 13(21) + Annex I Part I (2)(h) + (2)(i) + (2)(k)).

  fit_criterion: |
    A product-design framework is maintained combining DoS resilience (Annex I Part I (2)(h)) + cross-product impact minimisation (Annex I Part I (2)(i)) + exploitation-mitigation mechanisms (Annex I Part I (2)(k)) via PR.IR-04 adequate-resource-capacity leg (DoS resilience) + PR.IR-03 network-resources-prioritised leg (cross-product impact minimisation) + DE.CM-09 computing-hardware-monitored leg (exploitation-mitigation mechanism effectiveness); the post-incident availability preservation is the design-time commitment that the essential and basic functions remain available after an incident; the exploitation-mitigation mechanisms and techniques reduce the impact of an incident when one occurs; the cascading-impact-minimisation design limits the negative impact by the product on the availability of services provided by other devices or networks; where non-conformity is identified, Art. 13(21) corrective measures are taken immediately — including conformity-restoration, withdrawal or recall; the three-clause Annex I Part I (2)(h)/(i)/(k) constellation is CRA-unique and operates at the product-design level — the containment happens inside the product boundary, pre-event design + post-incident preservation (temporally distinct from GDPR's post-event reaction); for a DORA financial entity deploying CRA products, the CRA resilience design feeds the DORA BC arrangements (4.2-DORA cross-ref); the product-design containment discipline operates at the product boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), entity-level `contain` phase (NIS 2 leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by Annex VII §2(b) + §3 + §6 + §8 design-documentation inspection (DoS resilience, cross-product impact minimisation, exploitation mitigation) + Art. 13(21) corrective-measures records review (when non-conformity occurs) + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.3 (containment design at product-internal state level feeds from prior product-internal detection events), 4.2.2 (CRA product-resilience evidence feeds NIS 2 entity-level plan when NIS 2 entity deploys / manufactures CRA product), 4.2.4 (CRA product-resilience design feeds DORA BC arrangements when DORA FE deploys CRA product)]

  nist_csf: [PR.IR-03, ID.AM-08]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks. Annex I Part I (2)(i) requires products to minimise the negative impact by the products themselves or connected devices on the availability of services provided by other devices or networks. Annex I Part I (2)(k) requires reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.2: GDPR↔CRA = DIFFERENT-PERSPECTIVE; NIS2↔CRA = COMPLEMENTARY; CRA↔DORA = COMPLEMENTARY)
```

### from regs/CRA.md body

- The product-design measure object is distinct from the GDPR personal-data post-breach runbook (post-event reaction), the NIS 2 entity-level lifecycle-phase actions (entity boundary), and the DORA BC arrangements (financial-entity infrastructure) — the product boundary is internal to the product, and the design-level resilience discipline operates at that boundary only.

### from regs/CRA.md body

- The CRA product's Annex I (2)(h)/(i)/(k) architecture supports entity-level NIS 2 containment by reducing blast radius; for a DORA financial entity deploying CRA products, the CRA resilience design feeds the DORA BC arrangements. The CRA containment is pre-event design + post-incident availability preservation, temporally distinct from GDPR's post-event reaction; the high-level SO does not collapse the temporal distinction.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; disjoint in baseline: post-breach runbook ↔ product-design; CRA pre-event design + GDPR post-event reaction are temporally distinct); CRA↔NIS2 = Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint baseline: entity-level phase ↔ product-level design); CRA↔DORA = Conditional (Y DORA FE deploys CRA product; disjoint baseline: product ↔ BC arrangements); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA containment-and-mitigation obligation is the product-level post-incident availability + cross-product impact + exploitation mitigation architecture; the operational substrate is a product-design framework that combines DoS resilience (Annex I Part I (2)(h)), cascading-impact minimisation (Annex I Part I (2)(i)), and exploitation-mitigation mechanisms (Annex I Part I (2)(k)). The three-clause constellation is CRA-unique and operates at the product-design level — the containment happens inside the product boundary. The product-design measure object is distinct from the GDPR personal-data post-breach runbook (post-event reaction), the NIS 2 entity-level lifecycle-phase actions (entity boundary), and the DORA BC arrangements (financial-entity infrastructure) — the product boundary is internal to the product, and the design-level resilience discipline operates at that boundary only. The CRA product's Annex I (2)(h)/(i)/(k) architecture supports entity-level NIS 2 containment by reducing blast radius; for a DORA financial entity deploying CRA products, the CRA resilience design feeds the DORA BC arrangements. The CRA containment is pre-event design + post-incident availability preservation, temporally distinct from GDPR's post-event reaction; the high-level SO does not collapse the temporal distinction. The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification; Art. 14(1)/(3) AEV/SI notification including corrective measures) is part of 4.3, not 4.2. (Copied from the HSO Considerations block of `### 4.2.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=2 -->
