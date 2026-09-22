# D-03.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-005 | Identity of data subjects making rights-exercise requests verified using reasonable means proportionate to risk | Controller; Art. 12(6) + Art. 11(2); data-subject-side (external) identity verification; PR.AA-03 + PR.AA-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | data subjects (external, rights-exercise) | reasonable doubts concerning identity of requester (Art. 12(6)) | `reasonable means proportionate to risk` + Art. 5(1)(c) minimisation | supervisory authority (verification-evidence audit) | Art. 12(6) + Art. 11(2) |

## Sub-SO (GDPR)

#### D-03.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-03.1.GDPR
subdomain: D-03.1
applies_to: [GDPR]
inherits_from: SO-GDPR-005
source_SR: SR-GDPR-009, SR-GDPR-010
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The identity of a natural person making a rights-exercise
request under Art. 15–22 is verified using reasonable means proportionate
to the risk of mis-identification, before action is taken; the controller
may request additional information necessary to confirm the identity, and
the data subject must supply enough information to enable identification
if they wish to exercise the rights (Art. 12(6) + Art. 11(2); the
verification scope is constrained by Art. 5(1)(c) data minimisation).

**Considerations.**
- The operational substrate is a graduated verification standard (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk) plus an Art. 5(1)(c) minimisation register on the identity-verification artefacts.
- The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.1.

**CSF anchors (from `SR-GDPR-009` + `SR-GDPR-010` v0.3 security_rationale):**
PR.AA-03, PR.AA-02, ID.AM-08.
**PF 1.1 anchors (from `SR-GDPR-009`, `SR-GDPR-010` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
PR.AC-P6, PR.AC-P3, CT.DP-P4.
*(`SR-GDPR-009` covers the Art. 12(6) reasonable-doubts verification
trigger anchored to PR.AA-03 (users/services/hardware authenticated at
the rights-request endpoint) + PR.AA-02 (identities proofed and bound
to credentials proportionate to context). `SR-GDPR-010` covers the Art.
5(1)(c) minimisation of identity-verification data anchored to
PR.AA-02 + ID.AM-08 (data managed consistent with risk strategy).)*

---


## Security Requirements (GDPR)

#### 3.1.1 — Data-subject identity verification on rights-exercise endpoint

```yaml
- req_id: 3.1.1
  volere_section: 15
  volere_subtype: access

  title: "Data-subject identity verified using reasonable means proportionate to risk (rights-exercise endpoint)"

  derives_from:
    hso_sub_so: SO-D-03.1.GDPR
    per_reg_so: SO-GDPR-005
    source_sr: SR-GDPR-009, SR-GDPR-010
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md
    objective_ref_section: "### D-03.1.1"

  description: |
    The product shall verify the identity of a natural person making a rights-exercise request under Art. 15–22 using reasonable means proportionate to the risk of mis-identification, with the controller permitted to request additional information necessary to confirm the identity and the data subject supplying enabling information sufficient to confirm identification if they wish to exercise the rights; the verification scope is constrained by Art. 5(1)(c) data minimisation (GDPR Art. 12(6) + Art. 11(2) + Art. 5(1)(c)).

  fit_criterion: |
    A graduated verification standard operates at the rights-exercise endpoint (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk) with verification requests anchored to documented risk-classification criteria; an Art. 5(1)(c) minimisation register documents the identity-verification artefacts collected and the proportionality justification per request class; the verification policy applies at the controller-facing rights-exercise boundary only, with the boundary hand-off to staff authentication (D-03.2) and to product-user identity management (CRA leg) documented as the controlled interface at which the GDPR verification discipline ends; verified by verification-policy inspection + graduated-verification records audit + Art. 5(1)(c) minimisation register review + boundary hand-off-protocol documentation + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.2.1 (verification outcome feeds the staff-authentication event at the rights-exercise endpoint)]

  nist_csf: [PR.AA-03, PR.AA-02]
  nist_pf: [PR.AC-P6, PR.AC-P3]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim):**
> Art. 12(6) permits the controller, where the controller has reasonable doubts concerning the identity of the natural person making a request under Art. 15–22, to request the additional information necessary to confirm the identity of the data subject. Art. 11(2) preserves data-subject rights where the data subject provides additional information enabling identification, anchoring the reciprocal obligation: the data subject must supply enough information to be identified if they wish to exercise the rights.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.1: GDPR↔NIS2 CORRECTED from DIFFERENT-PERSPECTIVE; GDPR↔CRA CORRECTED from DIFFERENT-PERSPECTIVE; GDPR↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/GDPR.md body

- The data-subject identity object is distinct from the NIS 2 workforce, CRA product users + services + components, and DORA staff + service identities — the controller-facing rights-exercise endpoint is the boundary, and the identity-verification policy is applied at that boundary only.

### from regs/GDPR.md body

- For an organisation across multiple regulators, the GDPR leg documents the data-subject leg of the multi-boundary identity architecture rather than imposing a separate identity-management framework; the boundary hand-off to staff authentication (D-03.2) and to product-user identity management (CRA) is documented as the controlled interface at which the GDPR verification discipline ends.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = N (data subjects vs workforce are distinct identity objects); GDPR↔CRA = Conditional (Y when CRA product hosts data-subject rights endpoints); GDPR↔DORA = Conditional (Y when DORA financial entity is also controller); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The data-subject identity object is distinct from the NIS 2 workforce, CRA product users + services + components, and DORA staff + service identities — the controller-facing rights-exercise endpoint is the boundary, and the verification policy applies at that boundary only. For an organisation across multiple regulators, the GDPR leg documents the data-subject leg of the multi-boundary identity architecture rather than imposing a separate identity-management framework. The CRA `verifiable manner` floor discharges the GDPR `reasonable means proportionate to risk` when the same party operates both manufacturer-side and controller-side roles on the same identity substrate. The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.1. (Copied from the HSO Considerations block of `### D-03.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=1 -->
