# D-03.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i); workforce-side (internal) joiner-mover-leaver; PR.AA-01 + PR.AA-05 + PR.AT-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | workforce (internal, joiner-mover-leaver) | continuous (provisioning on induction, review on role change, revocation on separation) | `appropriate and proportionate` (Art. 21(1)) | competent authority / CSIRT (entity governance audit) | Art. 21(2)(i) (HR-security dimension) |

## Sub-SO (NIS 2)

#### D-03.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-03.1.NIS2
subdomain: D-03.1
applies_to: [NIS2]
inherits_from: SO-NIS2-003
source_SR: SR-NIS2-003, SR-NIS2-004
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Identities of the workforce — employees, contractors and
other authorised personnel with access to network and information
systems — are managed throughout the employment lifecycle, with
provisioning on induction, entitlement review on role change, and
revocation on separation, integrated into the entity's access-control
policy and asset-management discipline (Art. 21(2)(i) HR-security
dimension, coordinated by the literal AND with access-control policies
and asset management).

**Considerations.**
- The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the lifecycle rigour: high-risk roles (privileged access, sensitive data exposure) trigger tighter verification and review cadences than low-risk roles.
- The vulnerability handling dimension of the same Art. 21(2)(e) clause captures the supplier-correspondence channel through which identity-related vulnerabilities (e.g. compromised credentials in published advisories) feed the workforce identity-lifecycle register.
- The disclosure dimension (Art. 12(1) CSIRT-coordinated) is part of D-04.3, not D-03.1.

**CSF anchors (from `SR-NIS2-003` + `SR-NIS2-004` v0.3 security_rationale):**
PR.AA-01, PR.AA-05, PR.AT-02.
*(`SR-NIS2-003` covers the Art. 21(2)(i) identity-and-access-control
policy foundation anchored to PR.AA-01 (identities and credentials
managed by the organisation) + PR.AA-05 (access permissions managed
per least privilege). `SR-NIS2-004` covers the Art. 21(2)(i)
HR-security dimension of the workforce identity-lifecycle anchored to
PR.AT-02 (workforce understands role-specific security
responsibilities) + PR.AA-01 (identity substrate that the HR process
executes against — provisioning, role-transition review, separation).)*

---


## Security Requirements (NIS 2)

#### 3.1.2 — Workforce joiner-mover-leaver lifecycle under HR-security discipline

```yaml
- req_id: 3.1.2
  volere_section: 15
  volere_subtype: access

  title: "Workforce identities managed throughout the employment lifecycle (joiner-mover-leaver)"

  derives_from:
    hso_sub_so: SO-D-03.1.NIS2
    per_reg_so: SO-NIS2-003
    source_sr: SR-NIS2-003, SR-NIS2-004
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md
    objective_ref_section: "### D-03.1.2"

  description: |
    The product shall manage identities of the workforce — employees, contractors and other authorised personnel with access to network and information systems — throughout the employment lifecycle, with provisioning on induction, entitlement review on role change, and revocation on separation, integrated into the entity's access-control policy and asset-management discipline; the `appropriate and proportionate` qualifier from Art. 21(1) operationalises the lifecycle rigour with high-risk roles triggering tighter verification and review cadences than low-risk roles (NIS 2 Art. 21(2)(i) HR-security dimension, coordinated by the literal AND with access-control policies and asset management).

  fit_criterion: |
    A joiner-mover-leaver (JML) register operates for the workforce with documented induction-provisioning tickets, role-transition review tickets, and separation-revocation tickets, each linked to the underlying personnel-record event; access-control policy and asset-management artefacts reference the JML register; risk-tiered verification and review cadences apply (privileged access and sensitive-data-exposure roles trigger tighter cadences than low-risk roles); the workforce identity-lifecycle discipline operates at the internal workforce boundary only, with the boundary hand-off to data-subject verification (GDPR leg) and product-user identity management (CRA leg) documented as the controlled interface at which the NIS 2 workforce discipline ends; verified by JML register audit + risk-tier mapping review + access-control policy inspection + asset-management cross-reference + competent authority / CSIRT inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.2.2 (workforce identity feeds the staff-authentication event at the entity-side boundary)]

  nist_csf: [PR.AA-01, PR.AA-05]

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
verified_relationship: SAME (CRDA-deep, D-03.1: GDPR↔NIS2 CORRECTED from DIFFERENT-PERSPECTIVE; NIS2↔CRA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/NIS2.md body

- The workforce identity object is distinct from the GDPR data subjects, CRA product users + services + components, and DORA staff + service identities — the workforce boundary is internal, and the identity-lifecycle discipline operates at that boundary only.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = N (workforce ↔ data subjects); NIS2↔CRA = Conditional (Y when NIS 2 essential entity deploys or manufactures CRA product); NIS2↔DORA = Conditional (Y for cross-sector entities, N pure-financial via lex specialis); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The workforce identity object is distinct from the GDPR data subjects, CRA product users + services + components, and DORA staff + service identities — the workforce boundary is internal, and the identity-lifecycle discipline operates at that boundary only. The `appropriate and proportionate` qualifier from Art. 21(1) propagates and operationalises the lifecycle rigour. The vulnerability handling dimension of the same Art. 21(2)(e) clause captures the supplier-correspondence channel through which identity-related vulnerabilities (e.g. compromised credentials in published advisories) feed the workforce identity-lifecycle register. For pure-financial entities, DORA absorbs the NIS 2 workforce-identity-lifecycle obligation via lex specialis; the HL does not aggregate across the lex-specialis boundary in that direction. The disclosure dimension (Art. 12(1) CSIRT-coordinated) is part of D-04.3, not D-03.1. (Copied from the HSO Considerations block of `### D-03.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=1 -->
