# D-03.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-015 | Identities, credentials, and access entitlements for users, services, and integrated components managed in a verifiable manner | Manufacturer; Annex I Part I (2)(d) + Art. 13(15); product-side (user / service / integrated-component identities); PR.AA-01 + ID.AM-01 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product users + services + integrated components | continuous (throughout operational lifetime) + triggered (becoming aware of identity-vulnerability) | `verifiable manner` (Annex I Part I (2)(d)) | market surveillance authority (Annex VII technical documentation) + users (Annex II §3 unique identification) | Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3 |

## Sub-SO (CRA)

#### D-03.1.3 — Sub-SO for CRA

```yaml
id: SO-D-03.1.CRA
subdomain: D-03.1
applies_to: [CRA]
inherits_from: SO-CRA-015
source_SR: SR-CRA-023, SR-CRA-024
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Identities, credentials, and access entitlements for
users, services, and integrated components of the product with digital
elements are managed in a verifiable manner throughout the operational
lifetime of the product (Annex I Part I (2)(d) + Art. 13(15)
type/batch/serial unique identification + Art. 13(17) single point of
contact; backed by Annex II §3 unique-identification user information).

- The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.1.

**CSF anchors (from `SR-CRA-023` + `SR-CRA-024` v0.3 security_rationale):**
PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09.
*(`SR-CRA-023` covers the Annex I Part I (2)(d) + Art. 13(15) + Annex II
§3 identity-management and unique-product-identification architecture
anchored to PR.AA-01 (identities and credentials managed by the
organisation) + ID.AM-01 (hardware inventories — the
type/batch/serial marking backing the SBOM-correlated identity
register). `SR-CRA-024` covers the Annex I Part I (2)(d)+(j)
reporting-on-access and attack-surface-limitation duty anchored to
PR.AA-05 (access permissions per least privilege) + PR.AA-06 (access
limited to authorised users/services/hardware) + DE.CM-09 (monitoring
to detect attempted and successful unauthorised access — the
visibility leg that pairs with the preventive controls).)*

---


## Security Requirements (CRA)

#### 3.1.3 — Product-side identity management in verifiable manner

```yaml
- req_id: 3.1.3
  volere_section: 15
  volere_subtype: access

  title: "Product users, services, and integrated components identities managed in verifiable manner throughout operational lifetime"

  derives_from:
    hso_sub_so: SO-D-03.1.CRA
    per_reg_so: SO-CRA-015
    source_sr: SR-CRA-023, SR-CRA-024
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md
    objective_ref_section: "### D-03.1.3"

  description: |
    The product shall manage identities, credentials, and access entitlements for users, services, and integrated components of the product with digital elements in a verifiable manner throughout the operational lifetime of the product, with type/batch/serial unique identification per Art. 13(15) + Annex II §3 backing the SBOM-correlated identity register and a single point of contact per Art. 13(17) (CRA Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3).

  fit_criterion: |
    A product-side identity-management framework is maintained in verifiable manner throughout the operational lifetime, covering human users, service identities, and integrated-component identities; type/batch/serial unique-identification markings back the SBOM-correlated identity register (ID.AM-01 hardware-inventory substrate); reporting-on-access and attack-surface-limitation artefacts (PR.AA-05 + PR.AA-06) document least-privilege enforcement and authorised-only access to users/services/hardware; monitoring for attempted and successful unauthorised access (DE.CM-09) provides the visibility leg; the CRA `verifiable manner` reading is the strictest knowledge-test floor of the four participating regulators and discharges the GDPR `reasonable means proportionate to risk` when the same party operates both manufacturer-side and controller-side roles; verified by product-side identity-register audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + unique-identification marking review + SBOM format-validity check + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.2.3 (product-side identity substrate feeds the product-authentication mechanism choice)]

  nist_csf: [PR.AA-01, ID.AM-01]

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
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.1: GDPR↔CRA CORRECTED from DIFFERENT-PERSPECTIVE; NIS2↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

**Considerations.**

- The CRA `verifiable manner` threshold is stricter than GDPR's `reasonable means proportionate to risk` — the manufacturer must demonstrate that identities are managed verifiably throughout the operational lifetime, not merely that verification is proportional to a request risk; CRDA-deep verified the CRA "verifiable manner" reading as the strictest knowledge-test floor of the four participating regulators.

### from regs/CRA.md body

- The CRA identity-management framework is the upstream input to the controller / NIS 2 entity / DORA financial-entity identity-lifecycle programmes: the product-side identity register, the type/batch/serial marking, and the SBOM-correlated component identities feed downstream entity-side identity-management via published advisories and deployment documentation.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; disjoint in baseline); CRA↔NIS2 = Conditional (Y NIS 2 entity deploying CRA product); CRA↔DORA = Conditional (Y DORA financial entity deploying CRA product; disjoint baseline manufacturer ≠ financial entity); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA `verifiable manner` threshold is stricter than GDPR's `reasonable means proportionate to risk` — the manufacturer must demonstrate that identities (users, services, integrated components) are managed verifiably throughout the operational lifetime, not merely that verification is proportional to a request risk. The CRA identity-management framework is the upstream input to the controller / NIS 2 entity / DORA financial-entity identity-lifecycle programmes: the product-side identity register, the type/batch/serial marking, and the SBOM-correlated component identities feed downstream entity-side identity-management via published advisories and deployment documentation. The downstream AEV notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.1. (Copied from the HSO Considerations block of `### D-03.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=1 -->
