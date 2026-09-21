# D-03.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-006 (cross-ref) / SO-GDPR-005 (cross-ref) | No explicit MFA mandate; staff-side via instructions + confidentiality (Art. 28(3)(b) + Art. 29); data-subject-side via Art. 12(6) verification | Controller/processor; no explicit MFA; PR.AA-05 + PR.AA-06 + PR.AT-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | silent | staff (authorised persons) + data subjects (rights-request endpoint) | continuous (Art. 32(1)(b) confidentiality) + triggered (Art. 12(6) verification on reasonable doubt) | (no MFA threshold; instructions + confidentiality on staff-side; reasonable-means-proportionate on requester-side) | supervisory authority (compliance-evidence audit) | Art. 28(3)(b) + Art. 29 + Art. 12(6) |

## Sub-SO (GDPR)

#### D-03.2.1 — Sub-SO for GDPR

```yaml
id: SO-D-03.2.GDPR
subdomain: D-03.2
applies_to: [GDPR]
inherits_from: SO-GDPR-006 (cross-ref), SO-GDPR-005 (cross-ref)
source_SR: SR-GDPR-011, SR-GDPR-012
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Persons authorised to process personal data act only on
documented instructions from the controller (or processor) and are
bound by confidentiality or an appropriate statutory obligation of
confidentiality (Art. 28(3)(b) + Art. 29 + Art. 32(4) instruction-only
processing); the identity of data subjects making rights-exercise
requests is verified using reasonable means proportionate to the risk
of mis-identification (Art. 12(6) + Art. 11(2)).

**Considerations.**
- GDPR is the silent-wrapper around authentication: the OJ Art. 28(3)(b) + Art. 29 obligations govern the authorisation and confidentiality of authenticated persons (staff), and Art. 12(6) governs the verification of the data-subject requester at the rights-exercise endpoint — neither clause imposes an authentication-strength threshold.
- The operational substrate is the chain-of-authority pattern (controller → processor → authorised persons, with documented instructions binding each link) and the verification pattern (data-subject → verification-on-reasonable-doubt → proportionate additional information).
- A controller selecting MFA at the staff-authentication endpoint satisfies Art. 32(1)(b) confidentiality; a controller selecting single-factor password authentication is not forbidden by GDPR but must satisfy the surrounding instruction + confidentiality + minimisation obligations.
- The downstream authentication failure notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.2.

**CSF anchors (from `SR-GDPR-011` + `SR-GDPR-012` v0.3 security_rationale):**
PR.AA-05, PR.AA-06, PR.AT-02.

---


## Security Requirements (GDPR)

#### 3.2.1 — Silent wrapper (instructions + confidentiality + verification) without authentication-strength threshold

```yaml
- req_id: 3.2.1
  volere_section: 15
  volere_subtype: access

  title: "Authentication governed by instructions + confidentiality + minimisation (no OJ authentication-strength threshold)"

  derives_from:
    hso_sub_so: SO-D-03.2.GDPR
    per_reg_so: SO-GDPR-006 (cross-ref), SO-GDPR-005 (cross-ref)
    source_sr: SR-GDPR-011, SR-GDPR-012
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md
    objective_ref_section: "### D-03.2.1"

  description: |
    The product shall ensure that persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality, and that the identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification; GDPR does not impose an authentication-strength threshold — the OJ Art. 28(3)(b) + Art. 29 obligations govern the authorisation and confidentiality of authenticated staff, and Art. 12(6) governs the verification of the data-subject requester at the rights-exercise endpoint (GDPR Art. 28(3)(b) + Art. 29 + Art. 32(4) + Art. 12(6) + Art. 11(2)).

  fit_criterion: |
    A chain-of-authority pattern operates (controller → processor → authorised persons, with documented instructions binding each link) and a verification pattern operates (data-subject → verification-on-reasonable-doubt → proportionate additional information); Art. 28(3)(b) processor-contract confidentiality is documented for all processors and sub-processors; Art. 5(1)(c) minimisation applies to authentication-verification artefacts; the authentication-strength selection is the controller's discretion — a controller selecting MFA at the staff-authentication endpoint satisfies Art. 32(1)(b) confidentiality, a controller selecting single-factor password authentication is not forbidden by GDPR but must satisfy the surrounding instruction + confidentiality + minimisation obligations; the GDPR silent-wrapper around authentication is the surrounding obligation that does not impose an authentication-strength threshold but does require the authorisation + verification architecture; verified by documented-instructions register audit + processor-contract confidentiality review + verification-policy inspection + minimisation register review + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.1 (data-subject verification outcome feeds the rights-exercise authentication event)]

  nist_csf: [PR.AA-05, PR.AA-06, PR.AT-02]

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
> Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality. Art. 29 reinforces this by binding natural persons acting under the authority of controller or processor to instruction-only processing.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.2: GDPR↔NIS2 CORRECTED from COMPLEMENTARY; GDPR↔CRA CORRECTED from COMPLEMENTARY; GDPR↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/GDPR.md body

*(`SR-GDPR-011` covers the Art. 28(3)(a)/(b) + Art. 29 + Art. 32(4)
instruction-only processing anchored to PR.AA-05 (access permissions
managed per least privilege) + PR.AA-06 (access limited to authorised
users/services/hardware). `SR-GDPR-012` covers the Art. 28(3)(b)
processor-contract confidentiality anchored to PR.AA-06 + PR.AT-02
(workforce understands role-specific security responsibilities). The
two SRs together cover the authorisation + confidentiality wrapper
without imposing an authentication-strength threshold; the
authentication-strength selection is the controller's discretion,
discharged by any NIS 2 / DORA / CRA authentication-strength obligation
when those regs apply on the same party.)*

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y when controller is also NIS 2 entity); GDPR↔CRA = Conditional (Y when CRA product hosts staff- or data-subject-authentication endpoints); GDPR↔DORA = Conditional (Y when DORA financial entity is also controller); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    GDPR is the silent-wrapper around authentication: the OJ Art. 28(3)(b) + Art. 29 obligations govern the authorisation and confidentiality of authenticated persons (staff), and Art. 12(6) governs the verification of the data-subject requester at the rights-exercise endpoint — neither clause imposes an authentication-strength threshold. The authentication-strength selection is the controller's discretion, discharged by any NIS 2 / DORA / CRA authentication-strength obligation when those regs apply on the same party. A controller selecting MFA at the staff-authentication endpoint satisfies Art. 32(1)(b) confidentiality; a controller selecting single-factor password authentication is not forbidden by GDPR but must satisfy the surrounding instruction + confidentiality + minimisation obligations. The downstream notification cascade (Art. 33 personal-data-breach notification) is part of D-04.3, not D-03.2. (Copied from the HSO Considerations block of `### D-03.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=0 -->

