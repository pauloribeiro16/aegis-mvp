# D-03.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-017 + SO-CRA-024 | Access to product with digital elements limited to authenticated and authorised users, services, hardware; possible unauthorised access reported; attack-surface limitation | Manufacturer; Annex I Part I (2)(d) + (2)(j); product-side access boundary + reporting + attack-surface-reduction; PR.AA-05 + PR.AA-06 + DE.CM-09 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-side authenticated-and-authorised product access + reporting + attack-surface limitation | continuous (product access-control duty + triggered on detection of unauthorised access) | `limited to authenticated and authorised users, services and hardware` + `possible unauthorised access reported` + `limit attack surfaces including external interfaces` (Annex I Part I (2)(d) + (2)(j)) | R1 inclusive on `possible` + state-of-the-art (Annex I (2)(e) `commensurate with the identified cybersecurity risk`) | market surveillance authority (Annex VII technical documentation) + product users (Annex II §8 user-facing instructions on monitoring + opt-out) | access-control records + attack-surface-reduction evidence + runtime-monitoring logs (DE.CM-09) + reporting evidence, on PR.AA-05 + PR.AA-06 + DE.CM-09 anchors |

## Sub-SO (CRA)

#### D-03.3.3 — Sub-SO for CRA

```yaml
id: SO-D-03.3.CRA
subdomain: D-03.3
applies_to: [CRA]
inherits_from: SO-CRA-017
source_SR: SR-CRA-024, SR-CRA-017 (update dissemination cross-ref)
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Access to the product with digital elements, its data,
services, and functions is limited to authenticated and authorised users,
services, and hardware, with possible unauthorised access reported
(Annex I Part I (2)(d) `protection from unauthorised access through
appropriate control mechanisms` + `possible unauthorised access reported`
— R1 inclusive reading on `possible`) and attack surfaces including
external interfaces limited (Annex I Part I (2)(j)).

**Considerations.**
- The `possible unauthorised access` polysemy (R1 inclusive — any successful + any detected-but-failed attempt; R2 overreaches the literal; R3 under-reaches because successful breaches must also be reported) is preserved from `SR-CRA-024` `ambiguity_notes`.
- The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.3.

**CSF anchors (from `SR-CRA-024` v0.3 security_rationale):**
PR.AA-05, PR.AA-06, DE.CM-09.
*(`SR-CRA-024` covers the Annex I Part I (2)(d) + (2)(j)
reporting-on-access and attack-surface-limitation duty anchored to
PR.AA-05 (access permissions managed per least privilege) + PR.AA-06
(access limited to authorised users/services/hardware) + DE.CM-09
(monitoring to detect attempted and successful unauthorised access).
The three anchors together enable the manufacturer to demonstrate ex
post, through documented access-control records, attack-surface-
reduction evidence, and runtime-monitoring logs, that the (2)(d)+(j)
combined duty has been exercised across the deployed product
population and that bypass attempts become observable events rather
than silent failures. The `possible unauthorised access` R1 inclusive
reading is the strictest visibility floor across the four regulators.)*

---


## Security Requirements (CRA)

#### 3.3.3 — Product-side authenticated-and-authorised boundary + reporting + attack-surface-limitation

```yaml
- req_id: 3.3.3
  volere_section: 15
  volere_subtype: access

  title: "Access to product with digital elements limited to authenticated and authorised users, services, and hardware; possible unauthorised access reported; attack surfaces including external interfaces limited (multi-leg product-side authorisation framework)"

  derives_from:
    hso_sub_so: SO-D-03.3.CRA
    per_reg_so: SO-CRA-017
    source_sr: SR-CRA-024, SR-CRA-023 (product identification cross-ref)
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md
    objective_ref_section: "### D-03.3.3"

  description: |
    The product shall limit access to the product with digital elements, its data, services and functions to authenticated and authorised users, services, and hardware, with possible unauthorised access reported (R1 inclusive reading on `possible` — any successful + any detected-but-failed attempt) and attack surfaces including external interfaces limited (CRA Annex I Part I (2)(d) `protection from unauthorised access through appropriate control mechanisms` + `possible unauthorised access reported` + Annex I Part I (2)(j) `limit attack surfaces including external interfaces`).

  fit_criterion: |
    A product-side authenticated-and-authorised boundary operates with PR.AA-05 + PR.AA-06 least-privilege entitlement baseline + boundary-enforcement on physical and logical assets; a reporting-and-monitoring substrate under PR.PS-04 + DE.CM-09 captures attempted and successful unauthorised access and surfaces it as observable events; type/batch/serial unique-identification markings per Art. 13(15) + Annex II §3 back the SBOM-correlated identity register (ID.AM-01) on which the (2)(d) control mechanisms rely; Annex I Part I (2)(j) attack-surface-reduction evidence documents least-privilege enforcement at external interfaces (network ingress, exposed APIs, hardware ports); the `possible unauthorised access` R1 inclusive reading is the strictest visibility floor across the four regulators — R2 (any access attempt at all) overreaches the literal, R3 (failed-but-detected subset only) under-reaches because successful breaches must also be reported; the product-side authorisation framework operates at the product boundary only, with the boundary hand-off to GDPR personal-data-scope chain (when the CRA product hosts data-subject rights endpoints) and to NIS 2 entity-side access-control policy (when a CRA manufacturer is also a NIS 2 essential entity) and to DORA financial-entity-side ICT-asset access (when a DORA financial entity deploys the CRA product) documented as the controlled interfaces at which the CRA product-side discipline ends; verified by product-side identity-register audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + attack-surface-reduction evidence + runtime-monitoring logs + Annex II §8 user-facing instructions on monitoring + opt-out + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.3 (product-side identity substrate feeds the authenticated-and-authorised boundary), 3.3.3 cross-ref to 10.1 / 10.2 (monitoring substrate under SR-CRA-027 feeds the (2)(d) reporting leg)]

  nist_csf: [PR.AA-01, PR.AA-05, PR.AA-06, PR.PS-04, ID.AM-01, DE.CM-09]

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
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms — and the clause's broader scope in the OJ covers both the control itself and the visibility into access events, supporting the manufacturer-side reporting on possible unauthorised access. Annex I Part I (2)(j) limits attack surfaces, including external interfaces, in support of this access-control posture by reducing the number of contact points an adversary could probe.

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access through appropriate control mechanisms. Annex I Part I (2)(j) limits attack surfaces, including external interfaces.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME — COMPLEMENTARY (CRDA-deep, D-03.3: GDPR↔CRA SAME — COMPLEMENTARY; NIS2↔CRA SAME — COMPLEMENTARY; CRA↔DORA SAME — COMPLEMENTARY)
```

### from regs/CRA.md body

- The CRA product authorisation framework is the upstream input to the controller / NIS 2 entity / DORA financial-entity authorisation programmes: the product-side access boundary feeds downstream entity-side access-control policy via deployment documentation and the product's reporting mechanism (under Annex I Part II (6) + Art. 13(17) per `SR-CRA-019`).

### from regs/CRA.md body

- The reporting dimension is the strictest visibility floor across the four regulations and is not mirrored in GDPR / NIS 2 / DORA's authorisation obligations; a party in CRA + GDPR + NIS 2 + DORA scope has the CRA visibility floor as the operative ceiling on the overlap surface.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; disjoint in baseline); CRA↔NIS2 = Conditional (Y NIS 2 entity deploying CRA product); CRA↔DORA = Conditional (Y DORA financial entity deploying CRA product; disjoint baseline manufacturer ≠ financial entity); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA product authorisation framework is the upstream input to the controller / NIS 2 entity / DORA financial-entity authorisation programmes: the product-side access boundary, the type/batch/serial marking, the SBOM-correlated component identities, and the (2)(d) reporting mechanism feed downstream entity-side access-control policy via deployment documentation and the Annex I Part II (6) + Art. 13(17) vulnerability-reporting channel per `SR-CRA-019`. The reporting dimension (DE.CM-09 monitoring + (2)(d) reporting) is **CRA-specific** and is not mirrored in GDPR / NIS 2 / DORA's authorisation obligations; a party in CRA + GDPR + NIS 2 + DORA scope has the CRA visibility floor as the operative ceiling on the overlap surface. The (2)(j) attack-surface-limitation dimension is the CRA-specific reporting lever not mirrored in the other three regulations' authorisation obligations (the cross-validation report flags VAG-S2 on `possible unauthorised access` with R1 inclusive chosen). For pure-financial entities, DORA absorbs the CRA product-side authorisation obligation on the financial-entity-side via lex specialis and the HL does not aggregate across the lex-specialis boundary. The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.3. (Copied from the HSO Considerations block of `### D-03.3.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=1 -->