# D-03.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i) literal AND; entity-side model-agnostic access-control policy; PR.AA-01 + PR.AA-05 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | entity-side access-control policy (model-agnostic) | continuous (entity access-control duty) | `access control policies` model-agnostic (Art. 21(2)(i) literal AND with HR-security + asset-management) | `appropriate and proportionate` (Art. 21(1)) — T3-vs-text gap preserved | competent authority / CSIRT (entity governance audit) | access-control policy + role definitions + HR-lifecycle records + asset-management register, on PR.AA-01 + PR.AA-05 + ID.AM-01/02 anchors |

## Sub-SO (NIS 2)

#### D-03.3.2 — Sub-SO for NIS 2

```yaml
id: SO-D-03.3.NIS2
subdomain: D-03.3
applies_to: [NIS2]
inherits_from: SO-NIS2-003 (partial)
source_SR: SR-NIS2-003, SR-NIS2-005 (asset-management cross-ref), SR-NIS2-004 (HR-security cross-ref)
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Access-control policies are established and applied at
the entity level for the entity's network and information systems,
covering access limited to authorised users, services, and hardware on
a least-privilege basis, with the literal AND binding access-control +
HR-security + asset-management together (Art. 21(2)(i)).

**Considerations.**
- The access-control-policy reference is model-agnostic — the OJ text does not impose RBAC, ABAC, MAC or DAC — so any model that satisfies least-privilege is operative at the implementation layer (T3-vs-text gap preserved: T3 imports `RBAC + need-to-know + least privilege` vocabulary not present in the OJ; the SR preserves model-agnostic OJ language).
- The T3-vs-text gap is preserved verbatim from `SR-NIS2-003` `ambiguity_notes`; Member State transposition divergence may apply on national AC-model compatibility (e.g. French ANSSI classified-inventory expectations for essential sectors; German BSI authoritative-register expectations).
- The vulnerability handling dimension of the same Art. 21(2)(e) clause captures the supplier-correspondence channel through which authorisation-related vulnerabilities (e.g. compromised credentials in published advisories) feed the entity access-control register; the disclosure dimension (Art. 12(1) CSIRT-coordinated) is part of D-04.3, not D-03.3.

**CSF anchors (from `SR-NIS2-003` + `SR-NIS2-005` v0.3 security_rationale):**
PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02.
*(`SR-NIS2-003` covers the Art. 21(2)(i) entity-side access-control
policy foundation anchored to PR.AA-01 (identities and credentials
managed by the organisation) + PR.AA-05 (access permissions managed
per least privilege). The two anchors together provide the identity-
governance evidence base — joiner/mover/leaver records, privilege
reviews, role definitions — on which the entity demonstrates ex post
under Art. 21(1) that its access-control posture satisfies the
appropriate-and-proportionate qualifier. `SR-NIS2-005` covers the
Art. 21(2)(i) asset-management dimension anchored to ID.AM-01
(inventories of hardware managed by the organisation) + ID.AM-02
(inventories of software, services, and systems managed by the
organisation). The two inventories together constitute the asset
register against which access-control decisions, vulnerability
scanning, patch management, supply-chain assessment and incident-
response capabilities target their actions, and which the Art. 21(1)
appropriate-and-proportionate analysis presupposes as the precondition
for any technical-control decision.)*

---


## Security Requirements (NIS 2)

#### 3.3.2 — Entity-side access-control policy (model-agnostic) under Art. 21(2)(i) literal AND

```yaml
- req_id: 3.3.2
  volere_section: 15
  volere_subtype: access

  title: "Entity-side access-control policy established and applied to network and information systems on a model-agnostic least-privilege basis (Art. 21(2)(i) literal AND of AC + HR-security + asset-management)"

  derives_from:
    hso_sub_so: SO-D-03.3.NIS2
    per_reg_so: SO-NIS2-003 (partial)
    source_sr: SR-NIS2-003, SR-NIS2-005 (asset-management cross-ref), SR-NIS2-004 (HR-security cross-ref)
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md
    objective_ref_section: "### D-03.3.2"

  description: |
    The product shall establish and apply access-control policies at the entity level for the entity's network and information systems, covering access limited to authorised users, services, and hardware on a least-privilege basis, with the literal AND of the Art. 21(2)(i) sub-point binding access-control + HR-security + asset-management together and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the rigour (NIS 2 Art. 21(2)(i) literal AND with HR-security + asset-management; Art. 21(1) appropriate-and-proportionate propagates).

  fit_criterion: |
    A model-agnostic access-control policy (the OJ does not impose RBAC, ABAC, MAC or DAC — the policy can be implemented under any model that satisfies least-privilege; the T3-vs-text gap on `RBAC + need-to-know + least privilege` vocabulary not present in the OJ is preserved as model-agnostic) is established and applied with documented role definitions, PR.AA-01 identity-governance evidence base (joiner/mover/leaver records, privilege reviews, entitlement inventories) and PR.AA-05 least-privilege policy + entitlement assignments + access-review records + revocation tickets; the literal AND of the three Art. 21(2)(i) sub-domains is preserved — AC + HR-security (D-03.1) + asset-management (D-09.3 / D-03.3 cross) all three required in cumulative form, partial-compliance readings (two-of-three) rejected by the literal conjunction; the entity-side access-control policy discipline operates at the internal entity boundary only, with the boundary hand-off to GDPR personal-data-scope chain (D-03.3 GDPR sub-requirement) and to CRA product-side authenticated-and-authorised boundary documented as the controlled interfaces at which the NIS 2 model-agnostic discipline ends; Member State transposition divergence may apply on national AC-model compatibility (e.g. French ANSSI classified-inventory expectations for essential sectors, German BSI authoritative-register expectations); verified by access-control policy inspection + role-definition documentation review + HR-lifecycle records audit (D-03.1) + asset-management cross-reference (D-09.3 / D-03.3) + privilege-review records + competent authority / CSIRT inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.2 (workforce identity substrate feeds the role-definition entitlement inventory)]

  nist_csf: [PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02]

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
> Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: SAME — COMPLEMENTARY (CRDA-deep, D-03.3: GDPR↔NIS2 SAME — COMPLEMENTARY; NIS2↔CRA SAME — COMPLEMENTARY; NIS2↔DORA CORRECTED from CRDA EQUAL to COMPLEMENTARY)
```

### from regs/NIS2.md body

- The entity-side access-control policy is distinct from the GDPR personal-data-scope chain of authority, the CRA product-side authenticated-and-authorised boundary, and the DORA financial-entity-side legitimate-and-approved-only ICT-asset access — the entity-side boundary is internal, and the model-agnostic access-control policy discipline operates at that boundary only.

### from regs/NIS2.md body

- For an organisation across multiple regulators, the NIS 2 leg documents the entity-side leg of the multi-boundary authorisation architecture rather than imposing a separate authorisation framework; the boundary hand-off to GDPR personal-data-scope chain (D-03.3 GDPR sub-SO) and to CRA product-side authenticated-and-authorised boundary is documented as the controlled interface at which the NIS 2 model-agnostic discipline ends.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = N (workforce ↔ data subjects are distinct identity objects); NIS2↔CRA = Conditional (Y when NIS 2 essential entity deploys or manufactures CRA product); NIS2↔DORA = Conditional (Y cross-sector entities, N pure-financial via lex specialis); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The entity-side access-control policy is distinct from the GDPR personal-data-scope chain of authority, the CRA product-side authenticated-and-authorised boundary, and the DORA financial-entity-side legitimate-and-approved-only ICT-asset access — the internal entity boundary is its own surface, and the model-agnostic access-control policy discipline operates at that surface only. The T3-vs-text gap is preserved verbatim from `SR-NIS2-003` `ambiguity_notes` — T3 imports `RBAC + need-to-know + least privilege` vocabulary not in the OJ text; the SR preserves the model-agnostic OJ language. The vulnerability handling dimension of the same Art. 21(2)(e) clause captures the supplier-correspondence channel through which authorisation-related vulnerabilities (e.g. compromised credentials in published advisories) feed the entity access-control register. For pure-financial entities, DORA absorbs the NIS 2 entity-side-access-control obligation via lex specialis and the HL does not aggregate across the lex-specialis boundary in that direction. The disclosure dimension (Art. 12(1) CSIRT-coordinated) is part of D-04.3, not D-03.3. (Copied from the HSO Considerations block of `### D-03.3.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=1 -->