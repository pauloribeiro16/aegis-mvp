# D-03.2 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-004 | MFA or continuous authentication solutions "where appropriate" + secured voice/video/text + secured emergency | Essential/important entity; Art. 21(2)(j) first clause; "where appropriate" hedge; OR of MFA and continuous authentication (not redundant); PR.AA-03 + PR.AA-05 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | explicit (MFA or continuous) | staff + privileged access (entity workforce) | continuous (Art. 21(2) all-hazards) | `where appropriate` + Art. 21(1) factors (state of the art, costs, exposure, size, risk) | competent authority / CSIRT (entity governance audit) | Art. 21(2)(j) first clause |

## Sub-SO (NIS 2)

#### D-03.2.2 — Sub-SO for NIS 2

```yaml
id: SO-D-03.2.NIS2
subdomain: D-03.2
applies_to: [NIS2]
inherits_from: SO-NIS2-004
source_SR: SR-NIS2-006, SR-NIS2-007
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Multi-factor authentication or continuous authentication
solutions are used where appropriate, and secured voice, video and text
communications as well as secured emergency communication systems are
deployed within the entity (Art. 21(2)(j)).

**Considerations.**
- The OR admits both MFA and continuous-authentication as alternative authentication paradigms — they are not redundant — and the `where appropriate` hedge closes the sub-point.
- ENISA's 2022 baseline security recommendations list MFA as a default for all administrative and privileged access.
- The mechanism selection (FIDO2 / WebAuthn vs SMS-OTP vs TOTP vs hardware-token) is at the entity's discretion under the mechanism-agnostic R5 reading; the SMS-OTP reading is rejected for new deployments given the SS7 / SIM-swap attack surface.
- NIS 2 is the most explicit OJ-text anchor among the four participating regulators (the only one with an explicit `multi-factor authentication` phrase in OJ text).
- The second and third clauses of Art. 21(2)(j) (secured voice/video/text + secured emergency communication systems) are addressed separately by `SR-NIS2-007` and are partially routed to D-01.2 (data-in-transit channel protection) and D-04.4 (resilience under crisis); the D-03.2 leg of NIS 2 is focused on the MFA / continuous-authentication first clause only.

**CSF anchors (from `SR-NIS2-006` + `SR-NIS2-007` v0.3 security_rationale):**
PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03.
*(`SR-NIS2-006` covers the Art. 21(2)(j) first clause MFA or continuous
authentication obligation anchored to PR.AA-03 (users/services/hardware
authenticated — at session establishment the principal must present
evidence bound to multiple factors, or where continuous authentication
is chosen, session-risk signals feed re-validation) + PR.AA-05 (access
permissions managed per least privilege — the post-authentication
surface). `SR-NIS2-007` covers the Art. 21(2)(j) second-and-third
clauses secured-communications obligation anchored to PR.DS-02
(data-in-transit protected) + PR.IR-03 (mechanisms to achieve
resilience requirements in normal and adverse situations — the
secured-emergency channel-survival dimension). The two SRs together
cover the authentication-strength first clause and the
secured-communications second/third clauses of Art. 21(2)(j).)*

---


## Security Requirements (NIS 2)

#### 3.2.2 — MFA or continuous authentication `where appropriate`

```yaml
- req_id: 3.2.2
  volere_section: 15
  volere_subtype: access

  title: "Multi-factor or continuous authentication `where appropriate` (Art. 21(2)(j) first clause)"

  derives_from:
    hso_sub_so: SO-D-03.2.NIS2
    per_reg_so: SO-NIS2-004
    source_sr: SR-NIS2-006, SR-NIS2-007
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md
    objective_ref_section: "### D-03.2.2"

  description: |
    The product shall use multi-factor authentication or continuous authentication solutions where appropriate, and deploy secured voice, video and text communications and secured emergency communication systems within the entity; the OR admits both MFA and continuous-authentication as alternative authentication paradigms — they are not redundant — and the `where appropriate` hedge closes the sub-point (NIS 2 Art. 21(2)(j)).

  fit_criterion: |
    An authentication-mechanism choice (MFA or continuous-authentication) is documented with risk-tier mapping anchored to Art. 21(1) factors (state of the art, costs of implementation, exposure, size, risk) and a documented `where appropriate` justification per authentication surface; ENISA 2022 baseline security recommendations (MFA as default for all administrative and privileged access) are reflected in the risk-tier mapping; the mechanism selection (FIDO2 / WebAuthn vs TOTP vs hardware-token) is at the entity's discretion under the mechanism-agnostic R5 reading; the SMS-OTP reading is rejected for new deployments given the SS7 / SIM-swap attack surface; the DORA strong-authentication floor (≈ MFA via EBA reading) discharges the `where appropriate` test when DORA applies on the same party; the second and third clauses of Art. 21(2)(j) (secured voice/video/text + secured emergency) are routed to D-01.2 (data-in-transit) and D-04.4 (resilience) and are out of scope of this D-03.2 leg; verified by risk-tier mapping review + mechanism-selection rationale records + ENISA-baseline gap assessment + competent authority / CSIRT inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.2 (workforce identity substrate feeds the staff-authentication event)]

  nist_csf: [PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03]

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
> Article 21(2)(j) of Directive (EU) 2022/2555, in its first clause, requires essential and important entities to use multi-factor authentication or continuous authentication solutions, where appropriate.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.2: GDPR↔NIS2 CORRECTED from COMPLEMENTARY; NIS2↔CRA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/NIS2.md body

- The `where appropriate` test discharges under the strictest applicable floor (DORA `strong authentication` ≈ MFA via EBA reading) when DORA applies on the same party.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y when controller is also NIS 2 entity); NIS2↔CRA = Conditional (Y when NIS 2 entity deploys or manufactures CRA product); NIS2↔DORA = Conditional (Y cross-sector entities; N pure-financial via lex specialis); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    NIS 2 is the most explicit OJ-text anchor among the four participating regulators (the only one with an explicit `multi-factor authentication` phrase in OJ text). The OR admits both MFA and continuous-authentication as alternative authentication paradigms; the `where appropriate` hedge closes the sub-point and discharges under the strictest applicable floor (DORA `strong authentication` ≈ MFA via EBA reading) when DORA applies on the same party. The second and third clauses of Art. 21(2)(j) (secured voice/video/text + secured emergency communication systems) are addressed separately by `SR-NIS2-007` and are partially routed to D-01.2 (data-in-transit channel protection) and D-04.4 (resilience under crisis); the D-03.2 leg of NIS 2 is focused on the MFA / continuous-authentication first clause only. For pure-financial entities, DORA absorbs the NIS 2 authentication-strength obligation via lex specialis; the HL does not aggregate across the lex-specialis boundary in that direction. (Copied from the HSO Considerations block of `### D-03.2.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=1 -->

