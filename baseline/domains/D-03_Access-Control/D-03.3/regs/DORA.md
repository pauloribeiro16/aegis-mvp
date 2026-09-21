# D-03.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-006 | ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only | Financial entity; Art. 9(4)(c) `legitimate and approved` AND + `only` qualifier (T4-vs-text gap: T4 reads RBAC + need-to-know + least privilege; OJ literal preserves "legitimate and approved functions and activities only"); PR.AA-05 + PR.AA-06 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | financial-entity-side ICT-asset access (physical or logical, both required per R1) | continuous (financial-entity ICT-access-policy duty) | `physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only` (Art. 9(4)(c); the literal `only` qualifies the limiting phrase) | `legitimate AND approved` + `only` qualifier (T4-vs-text gap preserved as OJ-literal — `need-to-know + least privilege` not in OJ) | national competent authority + ESAs (Art. 9(4)(c) policy evidence + access register audit) | entitlement inventory + access-review records + separation-of-duties attestation logs + physical-access audit trails, on PR.AA-05 + PR.AA-06 anchors with multi-party authorisation for privileged grants |

## Sub-SO (DORA)

#### D-03.3.4 — Sub-SO for DORA

```yaml
id: SO-D-03.3.DORA
subdomain: D-03.3
applies_to: [DORA]
inherits_from: SO-DORA-006
source_SR: SR-DORA-010
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** ICT security policies limit physical or logical access to
information assets and ICT assets to what is required for legitimate
and approved functions and activities only, with the literal `only`
qualifier (Berry §5.3.1 — correctly placed before the limiting phrase)
closing off any access that is not strictly tied to a legitimate and
approved function (Art. 9(4)(c) physical or logical access + `legitimate
AND approved` AND-coordinated + `only` qualifier).

**Considerations.**
- The OJ `legitimate AND approved` two-axis gating (function-aligned AND governance-approved) is operationalised through PR.AA-05's documented entitlement rationales and PR.AA-06's access-request approval workflows with multi-party authorisation for privileged grants.
- The T4-vs-text gap on `need-to-know + least privilege` (T4 imports best-practice vocabulary not in OJ; the SR preserves OJ-literal `legitimate and approved functions and activities only`) is preserved from `SR-DORA-010` `ambiguity_notes`.
- The downstream notification cascade (Art. 19 major ICT-related incident notification) is part of D-04.3, not D-03.3.

**CSF anchors (from `SR-DORA-010` v0.3 security_rationale):**
PR.AA-05, PR.AA-06.
*(PR.AA-05 anchors the permission-tier discipline: function-aligned
entitlements, role-based and attribute-based access control, JIT
elevation with documented business justification, separation-of-
duties enforcement on payment-authorisation workflows, and PAM
with session recording. PR.AA-06 enforces the physical-and-logical
twin layer — badge access, mantrap entry, secure-room zoning, and
CCTV coverage complementing logical controls — preventing physical-
bypass of logical controls. The OJ `legitimate AND approved` two-axis
gating is operationalised through PR.AA-05's documented entitlement
rationales and PR.AA-06's access-request approval workflows with
multi-party authorisation for privileged grants. The DORA `only`
qualifier is the binding floor across the four regulators on the
financial-sector overlap.)*

---


## Security Requirements (DORA)

#### 3.3.4 — Financial-entity-side ICT-asset access limited to `legitimate and approved functions and activities only`

```yaml
- req_id: 3.3.4
  volere_section: 15
  volere_subtype: access

  title: "Financial-entity ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only (literal `only` qualifier)"

  derives_from:
    hso_sub_so: SO-D-03.3.DORA
    per_reg_so: SO-DORA-006
    source_sr: SR-DORA-010
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md
    objective_ref_section: "### D-03.3.4"

  description: |
    The product shall ensure that ICT security policies of the financial entity limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only, with the literal `only` qualifier (Berry §5.3.1 — `only` correctly placed before the limiting phrase) closing off any access that is not strictly tied to a legitimate and approved function, anchored to PR.AA-05 + PR.AA-06 with the OJ `legitimate AND approved` two-axis gating operationalised through documented entitlement rationales and access-request approval workflows with multi-party authorisation for privileged grants (DORA Art. 9(4)(c) physical or logical access + `legitimate AND approved` AND-coordinated + `only` qualifier).

  fit_criterion: |
    A financial-entity-side ICT-asset access policy operates with the literal `only` qualifier enforced on every access grant — no access may be granted that is not tied to a documented legitimate and approved function; an entitlement inventory + access-review records + separation-of-duties attestation logs + physical-access audit trails (badge access, mantrap entry, secure-room zoning, CCTV) satisfy the PR.AA-05 + PR.AA-06 physical-and-logical twin layer; multi-party authorisation is enforced for privileged grants on the OJ `legitimate AND approved` two-axis gating (function-aligned entitlement rationale AND governance-approved access-request approval workflow); the T4-vs-text gap on `need-to-know + least privilege` vocabulary not present in the OJ literal is preserved as OJ-literal `legitimate and approved functions and activities only` — Layer 2/3 to adjudicate whether the T-imposed best practice survives as interpretive continuation; the DORA `only` qualifier is the binding authorisation floor where the financial-entity-side stacks up on the same artefact with CRA product-side `limited to authenticated and authorised` and NIS 2 model-agnostic `access control policies`, and discharges those obligations on the same access-control substrate when both apply; the financial-entity-side ICT-asset access discipline operates at the financial-entity boundary only, with the boundary hand-off to NIS 2 entity-side model-agnostic access-control policy (when the financial entity is also a NIS 2 essential entity, i.e. cross-sector) and to CRA product-side authenticated-and-authorised boundary (when a DORA financial entity deploys CRA products) documented as the controlled interfaces at which the DORA `legitimate and approved only` discipline ends; verified by entitlement inventory audit + access-review records + separation-of-duties attestation logs + physical-access audit trails + multi-party-authorisation log review + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.4 (staff + service identity substrate feeds the entitlement inventory), 3.2.4 (authentication-strength floor feeds the strong-authentication event at the financial-entity boundary)]

  nist_csf: [PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06]

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
> Art. 9(4)(c) requires financial entities to implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME — COMPLEMENTARY (CRDA-deep, D-03.3: GDPR↔DORA SAME — COMPLEMENTARY; NIS2↔DORA CORRECTED from CRDA EQUAL to COMPLEMENTARY; CRA↔DORA SAME — COMPLEMENTARY)
```

### from regs/DORA.md body

- The DORA `only` qualifier is the strictest authorisation floor across the four regulators and discharges the CRA `limited to authenticated and authorised` and the NIS 2 `access control policies` on the same access-control substrate when both apply.

### from regs/DORA.md body

- The financial-entity-side ICT-asset access is distinct from the GDPR personal-data-scope chain of authority, the NIS 2 entity-side access-control policy, and the CRA product-side authenticated-and-authorised boundary — the financial-entity boundary is internal/ICT-asset-side, and the `legitimate and approved only` discipline operates at that boundary only.

### from regs/DORA.md body

- For an organisation across multiple regulators, the DORA leg documents the financial-entity-side leg of the multi-boundary authorisation architecture rather than imposing a separate authorisation framework; the boundary hand-off to NIS 2 entity-side model-agnostic access-control policy and to CRA product-side authenticated-and-authorised boundary is documented as the controlled interface at which the DORA `legitimate and approved only` discipline ends.

### from regs/DORA.md body

- For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 entity-side-access-control obligation and the high-level SO does not aggregate across the lex-specialis boundary.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-controller; disjoint baseline financial-entity ICT-asset access ↔ personal-data-scope chain); DORA↔NIS2 = Conditional (Y cross-sector; N pure-financial lex specialis); DORA↔CRA = Conditional (Y deployer-side; disjoint baseline financial entity ↔ manufacturer); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The financial-entity-side ICT-asset access is distinct from the GDPR personal-data-scope chain of authority, the NIS 2 entity-side access-control policy, and the CRA product-side authenticated-and-authorised boundary — the financial-entity boundary is internal/ICT-asset-side, and the `legitimate and approved only` discipline operates at that boundary only. The T4-vs-text gap (T4 imports `need-to-know + least privilege` not in OJ literal) is preserved from `SR-DORA-010` `ambiguity_notes`. The DORA `only` qualifier is the strictest authorisation floor across the four regulators and discharges the CRA `limited to authenticated and authorised` and the NIS 2 `access control policies` on the same access-control substrate when both apply. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 entity-side-access-control obligation on the same artefact via lex specialis and the HL does not aggregate across the lex-specialis boundary. The downstream notification cascade (Art. 19 major ICT-related incident notification) is part of D-04.3, not D-03.3. (Copied from the HSO Considerations block of `### D-03.3.4`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=1 -->

