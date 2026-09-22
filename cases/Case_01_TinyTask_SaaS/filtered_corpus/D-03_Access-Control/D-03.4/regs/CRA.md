# D-03.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-018 + SO-CRA-019 | Product made available with secure-by-default configuration + reset to original state + automatic security updates default + opt-out + postponement | Manufacturer; Annex I Part I (2)(b) + (2)(c); product-level; "tailor-made" carve-out for business users; reset capability; auto-update default; PR.PS-01 + ID.AM-08 + GV.SC-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-centric secure-by-default (product configuration) | continuous (Annex I Part I (2)(b) configuration + (2)(c) auto-update at market placement + reset capability) | `secure-by-default configuration` + `reset to original state` + tailor-made carve-out (Annex I Part I (2)(b)); `automatic security updates enabled by default` + `opt-out mechanism` + `notification of available updates` + `option to postpone` (Annex I Part I (2)(c)) | `secure by default` R1 features-enabled-on-default + reset capability R1 factory-reset-no-user-data + tailor-made R1 business-user-only + auto-update R1 enabled-by-default-with-opt-out | market surveillance authority (Annex VII technical documentation) + product users (Annex II §6 user-facing information on the secure default + reset capability) | secure-by-default configuration + reset procedure + tailor-made contractual records + auto-update default + opt-out mechanism discoverability + update-notification mechanism, on PR.PS-01 + ID.AM-08 + GV.SC-03 anchors |

## Sub-SO (CRA)

#### D-03.4.2 — Sub-SO for CRA

```yaml
id: SO-D-03.4.CRA
subdomain: D-03.4
applies_to: [CRA]
inherits_from: SO-CRA-018 + SO-CRA-019
source_SR: SR-CRA-025, SR-CRA-026, SR-CRA-018 (auto-update cross-ref)
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Products with digital elements are made available on the
market with a secure-by-default configuration — including the possibility
for the user to reset the product to its original state — unless otherwise
agreed between manufacturer and business user in relation to a tailor-made
product with digital elements (Annex I Part I (2)(b)), and the
secure-by-default configuration ensures that vulnerabilities can be
addressed through security updates — automatic security updates installed
within an appropriate timeframe, enabled by default, with a clear and
easy-to-use opt-out mechanism, through notification of available updates
to users, and with the option to temporarily postpone them (Annex I Part I
(2)(c)).

**Considerations.**
- R1 features-enabled-on-default adopted on secure-by-default; R2 deny-all-initial and R3 zero-config security operationally convergent with R1 in many cases; R2 and R3 are alternative readings; R4 post-deployment-surface rejected where it would conflict with the tailor-made carve-out.
- R1 factory-reset-no-user-data on reset-to-original-state; R2 initial-config-preserving-user-data underweights the reset semantic.
- The tailor-made carve-out (R1 business-user-only; R2 any-customised rejected as overreach; consumer products cannot opt out of the default-secure floor) and the auto-update dimension (R1 enabled-by-default-with-opt-out adopted) are preserved from `SR-CRA-026` + `SR-CRA-018` `ambiguity_notes`.
- The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.4.

**CSF anchors (from `SR-CRA-025` + `SR-CRA-026` + `SR-CRA-018` v0.3 security_rationale):**
PR.PS-01, ID.AM-08, GV.SC-03.
*(`SR-CRA-025` covers the Annex I Part I (2)(b) + Art. 6(a) proviso +
Art. 3(23) intended-purpose secure-by-default obligation anchored to
PR.PS-01 (configuration management practices established, documented,
and applied) + ID.AM-08 (data managed consistent with the
organisation's risk strategy to protect confidentiality, integrity,
and availability). The two anchors together enable the manufacturer
to demonstrate ex post, through documented baseline-configuration
records, configuration-change audit trails, and reset-capability
evidence in the technical documentation under Annex VII sections 2/6,
that the secure-by-default floor has been applied at the point of
market placement and that the reset capability has been preserved as
the recovery path. `SR-CRA-026` covers the tailor-made carve-out and
reset-to-original-state obligation anchored to PR.PS-01 + GV.SC-03
(contracts with suppliers and other third parties used to implement
appropriate measures designed to meet the objectives of an
organisation's cybersecurity program and the Cybersecurity Supply
Chain Risk Management Plan). `SR-CRA-018` covers the Annex I Part I
(2)(c) auto-update default obligation.)*

---


## Security Requirements (CRA)

#### 3.4.2 — Product-centric secure-by-default configuration + reset + tailor-made carve-out + auto-update default

```yaml
- req_id: 3.4.2
  volere_section: 15
  volere_subtype: access

  title: "Products with digital elements made available with secure-by-default configuration + reset-to-original-state capability + auto-update default + opt-out + postponement (Annex I Part I (2)(b) + (2)(c) multi-leg product default)"

  derives_from:
    hso_sub_so: SO-D-03.4.CRA
    per_reg_so: SO-CRA-018, SO-CRA-019
    source_sr: SR-CRA-025, SR-CRA-026, SR-CRA-018 (auto-update cross-ref)
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.4.md
    objective_ref_section: "### D-03.4.2"

  description: |
    The product shall be made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements, and the secure-by-default configuration shall ensure that vulnerabilities can be addressed through security updates — automatic security updates installed within an appropriate timeframe, enabled by default, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them (CRA Annex I Part I (2)(b) + Art. 6(a) proviso + Art. 3(23) intended-purpose anchor + Annex I Part I (2)(c) + Annex II §8(e) opt-out discoverability).

  fit_criterion: |
    A product-centric secure-by-default configuration operates with PR.PS-01 configuration-management baseline applied at first power-up to every unit leaving the manufacturing pipeline (R1 features-enabled-on-default — security features including authentication, access control, audit logging, network segmentation, secure-update mechanism enabled by default at first power-up; R2 deny-all-initial state and R3 zero-config-security operationally-convergent alternative readings rejected where they would conflict with the tailor-made carve-out; R4 post-deployment-surface rejected where it would conflict with the tailor-made carve-out); the reset-to-original-state capability (R1 factory-reset-no-user-data as the literal reading; R2 initial-config-preserving-user-data underweights the reset semantic) provides the recovery path back to the secure baseline; the tailor-made carve-out (R1 business-user-only on the carve-out scope; R2 any-customised rejected as overreach; consumer products cannot opt out of the default-secure floor) is documented in tailor-made contractual records; the auto-update default (R1 enabled-by-default-with-opt-out adopted; R2 deny-all-initial state; R3 zero-config security; R2 and R3 operationally-convergent with R1 in many cases; R4 post-deployment-surface rejected where it would conflict with the tailor-made carve-out) is on by default at first power-up with a clear and easy-to-use opt-out mechanism (UI discoverable + single-click) per Annex II §8(e); notification of available updates is delivered to users; postponement is temporarily available; Annex I Part I (2)(c) `within an appropriate timeframe` is anchored to the severity of the addressed vulnerability and the user's operational environment per the Art. 13(2) risk assessment (R2 chosen; R1 single quantitative ceiling rejected because severity modulation is the operative sanity check; R3 manufacturer discretion rejected as failing the inquiry-resistant test); ID.AM-08 data-management risk strategy governs the configuration-management baseline policy; the CRA tailor-made carve-out does NOT propagate into GDPR scope — even a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side; verified by secure-by-default configuration audit + reset-capability evidence + tailor-made contractual records + auto-update default documentation + opt-out discoverability check + update-notification mechanism review + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + Annex II §8(e) user-facing-instructions inspection + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.3 (product-side identity substrate feeds the secure-by-default baseline)]

  nist_csf: [PR.PS-01, ID.AM-08, GV.SC-03]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim):**
> Annex I Part I (2)(b) requires products to be made available on the market with a secure-by-default configuration — including the possibility to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. Art. 6(a) proviso anchors the configuration to intended purpose and reasonably foreseeable use.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME DIFFERENT-PERSPECTIVE (CRDA-deep, D-03.4: GDPR↔CRA same DIFFERENT-PERSPECTIVE confirmed after OJ-text analysis)
```

### from regs/CRA.md body

- The CRA tailor-made carve-out does NOT propagate into GDPR scope: a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side.

### from regs/CRA.md body

- The product-centric secure-by-default is distinct from the GDPR data-centric by-default — the product configuration layer is product-side, and the configuration-management baseline discipline operates at that layer only.

### from regs/CRA.md body

- For an organisation across both regulators, the CRA leg documents the product-side leg of the two-layer default posture rather than imposing a separate framework; the boundary hand-off to GDPR data-centric four-dimension AND is documented as the controlled layer interface at which the product-secure-by-default ends.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y when CRA product processes personal data; tailor-made carve-out does NOT exempt from GDPR); HL engages on overlap; for parties that deploy a CRA product that does NOT process personal data, only the CRA sub-requirement activates; the GDPR sub-requirement does NOT activate on the product-side

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The product-centric secure-by-default is distinct from the GDPR data-centric by-default — the product configuration layer is product-side, and the configuration-management baseline discipline operates at that layer only. The R1 features-enabled-on-default reading is adopted on secure-by-default; R2 deny-all-initial and R3 zero-config-security are alternative readings; R4 post-deployment-surface is rejected where it would conflict with the tailor-made carve-out. The R1 factory-reset-no-user-data reading on reset-to-original-state; R2 initial-config-preserving-user-data underweights the reset semantic. The R1 business-user-only reading on tailor-made scope (R2 any-customised rejected as overreach; consumer products cannot opt out of the default-secure floor); and the R1 enabled-by-default-with-opt-out reading on auto-update are preserved from `SR-CRA-026` + `SR-CRA-018` + `SR-CRA-025` `ambiguity_notes`. The CRA tailor-made carve-out does NOT propagate into GDPR scope: a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side. For an organisation across both regulators, the CRA leg documents the product-side leg of the two-layer default posture rather than imposing a separate framework. The downstream notification cascade (Annex I Part II (4)/(5) CSIRT + ENISA CVD notification) is part of D-04.3, not D-03.4. (Copied from the HSO Considerations block of `### D-03.4.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=1 -->