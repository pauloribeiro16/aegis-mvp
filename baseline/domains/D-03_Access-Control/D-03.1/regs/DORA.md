# D-03.1 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-002 (partial) | Strong authentication + key protection (Art. 9(4)(d) 3-control AND); identity-lifecycle is one dimension | Financial entity; Art. 9(4)(d); staff + service-to-service identities (financial-entity-side); PR.AA-03 + PR.AA-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity staff + service identities | continuous (strong-authentication under standards) | `strong authentication mechanisms based on relevant standards and dedicated control systems` + Art. 6(8) `appropriate level of independence` | national competent authority + ESAs | Art. 9(4)(d) (3-control AND: strong auth + key protection + encryption) |

## Sub-SO (DORA)

#### D-03.1.4 — Sub-SO for DORA

```yaml
id: SO-D-03.1.DORA
subdomain: D-03.1
applies_to: [DORA]
inherits_from: SO-DORA-002
source_SR: SR-DORA-002
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Identity assertions for financial-entity staff and
service-to-service identities are managed, protected, and conveyed in a
manner that verifies authenticity, as one dimension of the
strong-authentication + cryptographic-key-protection + risk-based
encryption 3-control AND in Art. 9(4)(d).

**Considerations.**
- The operational substrate is an identity provider with assertion-conveyance integrity (signed tokens, mutual transport authentication, PKI chain-of-trust), backed by authenticator inventories and AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 (per the EBA Guidelines on ICT and security risk management §145–§148 dominant supervisory expectation).
- The downstream notification cascade (Art. 19 major ICT-related incident notification) is part of D-04.3, not D-03.1

**CSF anchors (from `SR-DORA-002` v0.3 security_rationale):**
PR.AA-03, PR.AA-04.
*(PR.AA-03 anchors the strong-authentication event — users, services
and hardware authenticated at the financial-entity boundary with
calibrated authenticator strength (AAL2/AAL3, FIDO2/WebAuthn for
phishing-resistance, PKI for service-to-service). PR.AA-04 anchors the
identity-assertion conveyance integrity — managed, protected and
conveyed in a manner that verifies authenticity (signed federated-
identity tokens, mutual transport authentication, PKI chain-of-trust).
The two anchors together close the credential-compromise attack surface
that dominates financial-entity breach statistics.)*

---


## Security Requirements (DORA)

#### 3.1.4 — Financial-entity identity-assertion management under strong-authentication discipline

```yaml
- req_id: 3.1.4
  volere_section: 15
  volere_subtype: access

  title: "Staff + service identities managed with assertion-conveyance integrity under strong-authentication discipline"

  derives_from:
    hso_sub_so: SO-D-03.1.DORA
    per_reg_so: SO-DORA-002
    source_sr: SR-DORA-002
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md
    objective_ref_section: "### D-03.1.4"

  description: |
    The product shall manage, protect, and convey identity assertions for financial-entity staff and service-to-service identities in a manner that verifies authenticity, as one of the three coordinated controls in Art. 9(4)(d) (strong authentication + cryptographic-key protection + risk-based data encryption), backed by an authenticator-inventory register with AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 per the EBA Guidelines on ICT and security risk management §145–§148 dominant supervisory expectation (DORA Art. 9(4)(d)).

  fit_criterion: |
    An identity provider operates with assertion-conveyance integrity (signed federated-identity tokens, mutual transport authentication, PKI chain-of-trust) for staff and service-to-service identities at the financial-entity boundary; an authenticator-inventory register with AAL mappings (NIST SP 800-63B AAL2/AAL3, FIDO2/WebAuthn for phishing-resistance, PKI for service-to-service) is maintained and reviewed; the DORA identity-assertion discipline (PR.AA-04) is the strictest assertion-conveyance floor and supports the NIS 2 `where appropriate` test on authentication strength for financial-sector entities also within retained NIS 2 scope; for pure-financial entities, DORA absorbs the NIS 2 workforce-identity-lifecycle obligation via lex specialis and the HL does not aggregate across the lex-specialis boundary; verified by authenticator-inventory register audit + AAL-mapping documentation review + PKI chain-of-trust audit logs + identity-provider assurance records + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.2.4 (identity-assertion discipline feeds the strong-authentication event at the financial-entity boundary)]

  nist_csf: [PR.AA-03, PR.AA-04]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.1: GDPR↔DORA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/DORA.md body

- The staff + service identity object is distinct from the GDPR data subjects, NIS 2 workforce, and CRA product users + services + components — the financial-entity boundary is internal, and the assertion-management discipline operates at that boundary only.

### from regs/DORA.md body

- The `strong authentication mechanisms based on relevant standards and dedicated control systems` threshold is the strictest assertion-conveyance floor of the four participating regulators and discharges the NIS 2 `where appropriate` test on authentication strength for financial-sector entities also within retained NIS 2 scope.

### from regs/DORA.md body

- For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 workforce-identity-lifecycle obligation and the high-level SO does not aggregate across the lex-specialis boundary.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-controller; disjoint baseline service-auth ↔ data-subject-verification); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial lex specialis); DORA↔CRA = Conditional (Y deployer-side; disjoint baseline); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The staff + service identity object is distinct from the GDPR data subjects, NIS 2 workforce, and CRA product users + services + components — the financial-entity boundary is internal, and the assertion-management discipline operates at that boundary only. The DORA identity-assertion discipline (PR.AA-04) is the strictest assertion-conveyance floor of the four participating regulators; the OJ Art. 9(4)(d) text does NOT contain the phrase `multi-factor` — the T4-vs-text gap is P0-flagged in `SR-DORA-002` `ambiguity_notes` — but the dominant EBA Guidelines reading is MFA, with the chosen SR-DORA-002 reading mechanism-agnostic (R5) and R3 (MFA) as the dominant EU supervisory reading pending the ESAs Joint Committee RTS under Art. 15. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 workforce-identity-lifecycle obligation and the HL does not aggregate across the lex-specialis boundary. The downstream major ICT-related incident notification cascade (Art. 19) is part of D-04.3, not D-03.1. (Copied from the HSO Considerations block of `### D-03.1.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=6; core_cross_mentions=1 -->