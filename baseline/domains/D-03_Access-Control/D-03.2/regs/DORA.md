# D-03.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-002 | Strong authentication mechanisms (T4 reads MFA; OJ says "strong authentication") | Financial entity; Art. 9(4)(d); dominant EBA Guidelines reading is MFA but OJ has no "multi-factor" phrase (T4-vs-text gap); PR.AA-03 + PR.AA-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | demanding (`strong authentication`) | financial-entity staff + service identities + machine identities | continuous (financial-entity operation) | `strong authentication mechanisms based on relevant standards and dedicated control systems` + Art. 6(8) appropriate level of independence | national competent authority + ESAs (EBA Guidelines dominant MFA reading) | Art. 9(4)(d) |

## Sub-SO (DORA)

#### D-03.2.4 — Sub-SO for DORA

```yaml
id: SO-D-03.2.DORA
subdomain: D-03.2
applies_to: [DORA]
inherits_from: SO-DORA-002
source_SR: SR-DORA-002
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Strong authentication mechanisms (based on relevant
standards and dedicated control systems) are implemented as one of
three coordinated controls in Art. 9(4)(d), together with
cryptographic-key protection measures and risk-based data encryption.

**Considerations.**
- The operational substrate is an authenticator-inventory register, AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 (per the EBA Guidelines on ICT and security risk management §145–§148 dominant supervisory expectation), and authenticator-strength calibration by risk-tier under Art. 4 proportionality.
- DORA is the most demanding OJ-text anchor among the four participating regulators (the only one that names `relevant standards` and `dedicated control systems`); the OJ Art. 9(4)(d) text does NOT contain the phrase `multi-factor` — the T4-vs-text gap is P0-flagged — but the dominant EBA Guidelines reading is MFA. The chosen reading in `SR-DORA-002` is mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory reading, pending the ESAs Joint Committee RTS under Art. 15 that may eventually name specific authentication-strength standards.
- The downstream major ICT-related incident notification cascade (Art. 19) is part of D-04.3, not D-03.2.

**CSF anchors (from `SR-DORA-002` v0.3 security_rationale):**
PR.AA-03, PR.AA-04.
*(PR.AA-03 anchors the strong-authentication event — users, services
and hardware authenticated at the financial-entity boundary with
calibrated authenticator strength (AAL2/AAL3, FIDO2/WebAuthn for
phishing-resistance, PKI for service-to-service, certificate-based
authentication in service-to-service flows). PR.AA-04 anchors the
identity-assertion conveyance integrity — managed, protected and
conveyed in a manner that verifies authenticity (signed federated-
identity tokens, mutual transport authentication, PKI chain-of-trust).
The two anchors together close the credential-compromise attack surface
that dominates financial-entity breach statistics and produce the
authenticator-inventory registers + AAL-mapping documentation + PKI
chain-of-trust audit logs + identity-provider assurance records that
constitute the Art. 5(2) accountability evidence.)*

---


## Security Requirements (DORA)

#### 3.2.4 — Strong authentication mechanisms (T4 reads MFA; OJ says `strong authentication`)

```yaml
- req_id: 3.2.4
  volere_section: 15
  volere_subtype: access

  title: "Strong authentication mechanisms based on relevant standards (Art. 9(4)(d); dominant EBA MFA reading)"

  derives_from:
    hso_sub_so: SO-D-03.2.DORA
    per_reg_so: SO-DORA-002
    source_sr: SR-DORA-002
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md
    objective_ref_section: "### D-03.2.4"

  description: |
    The product shall implement strong authentication mechanisms based on relevant standards and dedicated control systems, as one of three coordinated controls in Art. 9(4)(d), together with cryptographic-key protection measures and risk-based data encryption; the OJ Art. 9(4)(d) text does NOT contain the phrase `multi-factor` — the T4-vs-text gap is P0-flagged in `SR-DORA-002` `ambiguity_notes` — but the dominant EBA Guidelines on ICT and security risk management §145–§148 reading is MFA (DORA Art. 9(4)(d)).

  fit_criterion: |
    An authenticator-inventory register with AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 (per the EBA Guidelines §145–§148 dominant supervisory expectation) is maintained for financial-entity staff, service identities, and machine identities; the strong-authentication architecture includes FIDO2/WebAuthn for phishing-resistance, PKI for service-to-service, certificate-based authentication in service-to-service flows, signed federated-identity tokens, mutual transport authentication, and PKI chain-of-trust for identity-assertion integrity (PR.AA-04); the DORA strong-authentication floor discharges the NIS 2 `where appropriate` test (when NIS 2 also applies — typically only on cross-sector entities), exceeds the CRA `may include` permissive baseline, and provides the strong-authentication substrate that the GDPR silent-wrapper surrounds with instructions + confidentiality; for pure-financial entities, DORA absorbs the NIS 2 authentication-strength obligation via lex specialis; the T4-vs-text gap on `strong authentication` vs MFA is documented as the chosen reading (mechanism-agnostic R5 with R3 MFA as the dominant EU supervisory reading, pending the ESAs Joint Committee RTS under Art. 15); verified by authenticator-inventory register audit + AAL-mapping documentation review + PKI chain-of-trust audit logs + identity-provider assurance records + chosen-reading rationale records + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.4 (identity-assertion discipline feeds the strong-authentication event at the financial-entity boundary)]

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
verified_relationship: SAME (CRDA-deep, D-03.2: GDPR↔DORA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/DORA.md body

- DORA is the strictest floor; when DORA applies on the same party as the other three regulators, the DORA strong-authentication architecture discharges the NIS 2 `where appropriate` test (when NIS 2 also applies — typically only on cross-sector entities), exceeds the CRA "may include" permissive baseline, and provides the strong-authentication substrate that the GDPR silent-wrapper surrounds with instructions + confidentiality.

### from regs/DORA.md body

- For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 authentication-strength obligation and the high-level SO does not aggregate across the lex-specialis boundary.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-controller); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial lex specialis); DORA↔CRA = Conditional (Y DORA deployer-side + CRA product-side); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    DORA is the most demanding OJ-text anchor among the four participating regulators (the only one that names `relevant standards` and `dedicated control systems`); the OJ Art. 9(4)(d) text does NOT contain the phrase `multi-factor` — the T4-vs-text gap is P0-flagged — but the dominant EBA Guidelines reading is MFA. The chosen SR-DORA-002 reading is mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory reading, pending the ESAs Joint Committee RTS under Art. 15 that may eventually name specific authentication-strength standards. The DORA strong-authentication architecture discharges the NIS 2 `where appropriate` test on the same authentication event when NIS 2 also applies (typically only on cross-sector entities), exceeds the CRA `may include` permissive baseline, and provides the strong-authentication substrate that the GDPR silent-wrapper surrounds with instructions + confidentiality. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 authentication-strength obligation and the HL does not aggregate across the lex-specialis boundary. The downstream major ICT-related incident notification cascade (Art. 19) is part of D-04.3, not D-03.2. (Copied from the HSO Considerations block of `### D-03.2.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=1 -->

