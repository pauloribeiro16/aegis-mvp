# D-04.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-021 (cross-ref) | Preservation of availability of essential and basic functions of a product with digital elements *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and reduced incident impact via exploitation-mitigation mechanisms | Product with digital elements; manufacturer perspective; Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21); PR.IR-03 + ID.AM-08 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-internal resilience + exploitation mitigation (intra-product availability after incident) | `also after an incident` (Annex I Part I (2)(h)) — design-time and runtime resilience | risk-based per Article 13(2) risk assessment + product support period | resilience architecture + exploitation-mitigation evidence in Annex VII §2 technical documentation | market-surveillance authority (Annex VII) — not systematic; manufacturer self-attestation by default | Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) |

## Sub-SO (CRA)

#### D-04.4.3 — Sub-SO for CRA

```yaml
id: SG-D-04.4.CRA
subdomain: D-04.4
applies_to: [CRA]
inherits_from: SG-CRA-021
source_SR: SR-CRA-043
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The availability of essential and basic functions of a product with digital elements is protected *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques and minimises the negative impact on services of other devices and networks (Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) corrective measures).

**Considerations.**
- The CRA restoration-and-recovery obligation (which overlaps D-04.2 + D-04.4 in the source SO/SR) is the product-internal resilience + exploitation-mitigation architecture; the operational substrate is an intra-product resilience mechanism (engineered pre-incident so that essential and basic functions survive an attack) plus an exploitation-mitigation mechanism (operating at the binary layer + runtime layer — rate-limiting, ASLR/DEP, control-flow integrity, configuration hardening) plus a cross-product impact containment (minimising negative impact on services of other devices or networks, the (2)(i) CRA-unique cross-boundary responsibility), all risk-calibrated via the Art. 13(2) risk assessment.
- The CRA `also after an incident` anchor (Annex I Part I (2)(h)) is design-time and runtime — the resilience mechanism must be in place before the incident, not bolted on after. The Annex VII §6 test-reports demonstrating verification of conformity with Annex I Part I and Part II cybersecurity requirements (including the post-incident-availability obligation of (2)(h)) are the market-surveillance evidence base on a reasoned request.

**CSF anchors (from `SR-CRA-043` v0.3 security_rationale):**
PR.IR-03, ID.AM-08.
*(PR.IR-03 anchors the resilience pillar — mechanisms in place to
achieve resilience requirements in normal and adverse situations;
the post-incident availability reading is supplied by the literal
`also after an incident` qualifier — resilience mechanisms must be
in place before the incident, not bolted on after. ID.AM-08 captures
the CIA-availability leg and the data-management dimension of
impact-mitigation — data is managed consistent with the manufacturer's
risk strategy, with exploitation-mitigation controls (rate-limiting,
ASLR/DEP, control-flow integrity, configuration hardening) at the
binary + runtime layers, calibrated by the Art. 13(2) risk assessment.
The two subcategories together enable the manufacturer to demonstrate
ex post, through documented resilience architecture and
exploitation-mitigation evidence in the technical documentation under
Annex VII §2, that the combined (2)(h)+(2)(k) duty has been discharged
and that essential and basic functions will survive an incident. The
SR also covers D-04.2 (containment) and D-07.1 (secure-by-design);
the D-04.4 dimension in this HSO focuses on the post-incident
availability + exploitation-mitigation recovery-architecture aspect.)*

---


## Security Requirements (CRA)

#### 4.4.3 — Product-internal availability preserved `also after an incident` with exploitation-mitigation

```yaml
- req_id: 4.4.3
  volere_section: 15
  volere_subtype: immunity

  title: "Product with digital elements preserves essential and basic functions `also after an incident` through resilience and exploitation-mitigation architecture (intra-product recovery, layered not substituted)"

  derives_from:
    hso_sub_so: SO-4.4.CRA
    per_reg_so: SG-CRA-021
    source_sr: SR-CRA-043
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md
    objective_ref_section: "### 4.4.3"

  description: |
    The product with digital elements shall preserve the availability of essential and basic functions *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, with the manufacturer reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (binary + runtime layers — rate-limiting, ASLR/DEP, control-flow integrity, configuration hardening) and minimising the negative impact on services of other devices and networks (cross-product impact containment) (CRA Annex I Part I (2)(h) `also after an incident` + (2)(k) exploitation-mitigation + (2)(i) cross-product impact minimisation + Art. 13(21) corrective measures; the Annex I (2)(h) anchor is design-time and runtime — resilience must be in place before the incident, not bolted on after).

  fit_criterion: |
    An intra-product resilience architecture is engineered pre-incident so that essential and basic functions survive an attack (Annex I Part I (2)(h) `also after an incident`) — the resilience mechanism is in place before the incident, not bolted on after; an exploitation-mitigation mechanism operates at the binary layer + runtime layer — rate-limiting, ASLR/DEP, control-flow integrity (CFI), configuration hardening, sandboxing, secure enclaves, principle of least privilege at process level — via ID.AM-08 data-management-discipline substrate (Annex I Part I (2)(k)); cross-product impact containment minimises the negative impact on services of other devices or networks via Annex I Part I (2)(i) cross-boundary responsibility (the (2)(i) CRA-unique reading); the (2)(h)+(2)(k)+(2)(i) triad is risk-calibrated via the Art. 13(2) risk assessment; the Annex VII §2 technical-documentation evidence demonstrates the resilience architecture (general description §1 + design / vuln-handling processes §2 + SBOM §2 + risk-assessment §3); the Annex VII §6 test-reports demonstrate verification of conformity with Annex I Part I and Part II cybersecurity requirements (including the post-incident-availability obligation of (2)(h)); the product-internal resilience feeds the deployer's entity-level (NIS 2) and financial-entity (DORA) BC frameworks via deployment (CRA products reduce the load on the entity's BC framework by continuing to function during/after attack); for an integrated manufacturer-controller (manufacturer is also controller), the CRA product-internal resilience feeds the controller-side recovery-evidence base via Annex VII technical documentation; the CRA product-internal resilience does NOT replace the deployer's entity-level BC framework for cases where the product itself fails or the attack propagates beyond the product boundary (CRA is a layered-not-substituted caveat — structurally different from 4.1 where CRA `verifiable manner` is the strictest knowledge-test floor; here, CRA is a layered prevention/mitigation); verified by Annex I (2)(h) resilience architecture review + (2)(k) exploitation-mitigation evidence inspection + (2)(i) cross-product impact-containment evidence review + Annex VII §2 technical-documentation review + Annex VII §6 test-reports review (including post-incident-availability verification) + Art. 13(2) risk-calibration documentation + MSA reasoned-request inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.2.3 (recovery depends on prior exploitation-mitigation + impact-containment discipline from 4.2 leg), 4.1.3 (recovery depends on prior product-internal recording feeding the awareness trigger)]

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
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.4: GDPR↔CRA = DIFFERENT-PERSPECTIVE; NIS2↔CRA = COMPLEMENTARY; CRA↔DORA = COMPLEMENTARY)
```

### from regs/CRA.md body

- The product-resilience object is distinct from the GDPR personal-data-availability outcome, the NIS 2 entity-level BC framework, and the DORA financial-entity BC framework + backup-architecture — the product boundary is internal to the product, and the intra-product resilience discipline operates at that boundary.

### from regs/CRA.md body

- The CRA product reduces the probability that an entity-level recovery event materialises (the product continues to function during/after attack), but does NOT replace the deployer's entity-level BC framework for cases where the product itself fails or the attack propagates beyond the product boundary. For an integrated manufacturer-controller (manufacturer is also controller), the CRA product-internal resilience feeds the controller-side recovery-evidence base via the technical documentation under Annex VII (general description §1 + design / vuln-handling processes §2 + SBOM §2 + risk-assessment §3); for a NIS 2 entity deploying CRA products, the Annex I Part I (2)(h) resilience reduces the load on the entity-level BC framework via deployment.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; disjoint baseline: data-outcome ↔ product-resilience — CRA product-internal resilience reduces probability of GDPR restoration trigger; controller still owns recovery outcome); CRA↔NIS2 = Conditional (Y NIS 2 entity deploys/manufactures CRA products; disjoint baseline: entity ↔ product — CRA product-internal resilience reduces load on NIS 2 BC framework); CRA↔DORA = Conditional (Y DORA FE deploys/manufactures CRA products; disjoint baseline: product ↔ financial-entity ICT — CRA product-internal resilience reduces load on DORA BC framework; both required, neither substitutes); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA restoration-and-recovery obligation (which overlaps 4.2 + 4.4 in the source SO/SR) is the product-internal resilience + exploitation-mitigation architecture; the operational substrate is an intra-product resilience mechanism (engineered pre-incident so that essential and basic functions survive an attack) plus an exploitation-mitigation mechanism (operating at the binary + runtime layers) plus a cross-product impact containment (minimising negative impact on services of other devices or networks, the (2)(i) CRA-unique cross-boundary responsibility), all risk-calibrated via the Art. 13(2) risk assessment. The product-resilience object is distinct from the GDPR personal-data-availability outcome, the NIS 2 entity-level BC framework, and the DORA financial-entity BC framework + backup-architecture — the product boundary is internal to the product, and the intra-product resilience discipline operates at that boundary. The CRA product reduces the probability that an entity-level recovery event materialises (the product continues to function during/after attack), but does NOT replace the deployer's entity-level BC framework for cases where the product itself fails or the attack propagates beyond the product boundary. The CRA `also after an incident` anchor (Annex I Part I (2)(h)) is design-time and runtime — the resilience mechanism must be in place before the incident, not bolted on after. The (2)(h)+(2)(k)+(2)(i) triad is risk-calibrated via Art. 13(2) — the risk assessment drives the depth of each pillar. The Annex VII §6 test-reports demonstrating verification of conformity with Annex I Part I and Part II cybersecurity requirements (including the post-incident-availability obligation of (2)(h)) are the market-surveillance evidence base on a reasoned request. The CRA product-resilience as a layered-not-substituted caveat is structurally different from 4.1 (where CRA `verifiable manner` is the strictest knowledge-test floor); here, CRA product resilience is layered *above* the entity-level BC framework as a prevention/mitigation layer, with the entity-level BC framework remaining the operational floor when the CRA product fails. (Copied from the HSO Considerations block of `### 4.4.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=1 -->