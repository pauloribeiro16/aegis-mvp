# D-07.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SG-NIS2-017 (partial via maintenance dimension — SG-NIS2-017 routes via Art. 21(2)(e) third clause) | Security in maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) third clause) — partial coverage of CI/CD via the maintenance dimension. T3-vs-text gap per `04_NIS2.md` line 29: OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`. | **Entity-level partial coverage** via the maintenance dimension; AEGIS taxonomy §4.1 marks NIS 2 as sole authority. The partial coverage is realised through the maintenance phase of the 3-phase coordinated lifecycle (acquisition/development/maintenance — `SR-NIS2-028` on the basis of Art. 21(2)(e) third clause); the CI/CD build-time control surface (signed artefacts, build-agent integrity, ephemeral build environments) is **industry best-practice, not regulatory mandate**. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | entity-side deployment-and-maintenance pipeline (partial coverage of CI/CD via maintenance dimension; AEGIS taxonomy §4.1 sole-authority assignment with T3-vs-text gap — OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`) | essential/important entity NIS deployment activity (Art. 21(2)(e) third clause trigger) | `appropriate and proportionate` (Art. 21(1) chapeau) + `state of the art` (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative cadence; no quantitative CI/CD-pipeline controls (T3-vs-text gap) | management body (Art. 20(1) approve + oversee + liability) + competent authority on the Art. 21 measures + the Art. 23 significant-incident reporting flow when a CI/CD pipeline compromise leads to a significant incident | Art. 21(2)(e) third clause + Art. 21(1) chapeau + sentence 2 + Art. 20(1) management-body approval |

## Sub-SO (NIS 2)

#### D-07.3.1 — Sub-SO for NIS 2

```yaml
id: SG-D-07.3.NIS2
subdomain: D-07.3
applies_to: [NIS2]
inherits_from: SG-NIS2-017 (partial via the maintenance dimension — `SG-NIS2-017` routes to D-07.3 via Art. 21(2)(e) third clause)
source_SR: SR-NIS2-028
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in the maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) third clause NIS 2).

**Considerations.**
- The partial coverage of CI/CD pipeline security via the maintenance dimension is the operational heart of the NIS 2-side participation at D-07.3: the entity-side deployment-and-maintenance pipeline — patch-management policies + vulnerability-handling-and-disclosure records + the 3-phase coordinated lifecycle of Art. 21(2)(e) (acquisition + development + maintenance) with the maintenance phase covering the delivery-path security dimension of the CI/CD pipeline.
- **T3-vs-text gap:** the OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`. AEGIS taxonomy §4.1 marks NIS 2 as the SOLE AUTHORITY for D-07.3 CI/CD Pipeline Security, but the OJ literal text is silent on CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments).
- The entity-side CI/CD-pipeline compliance is demonstrated through: (a) NIS 2-side partial-coverage via the maintenance dimension (3-phase coordinated lifecycle — patch-management policies + vulnerability-handling-and-disclosure records + the maintenance phase operational implementation); (b) the industry-framework CI/CD build-time baseline (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA); (c) the supplier-customer boundary evidence trail (NIS 2 procurement gate via `SR-NIS2-026` supplier-secure-development-procedures three-prong + Art. 21(3) sentence 1 supplier-vulnerability-intelligence three-prong) on the Conditional-Y integrated stack.
- Art. 21(1) chapeau `appropriate and proportionate` is read with Art. 21(1) sentence 2 state-of-the-art floor + Recital 56 cost-of-implementation qualifier + Member-State transposition divergence on the appropriateness test.
- For a 5-FTE essential entity, the NIS 2-side CI/CD-pipeline compliance is demonstrated through the maintenance-dimension partial-coverage + industry-framework CI/CD build-time baseline.

**CSF anchors (from `SR-NIS2-028` v0.3 security_rationale):**
PR.PS-02, ID.RA-01.
*(PR.PS-02 anchors the software-maintenance dimension — software is maintained, replaced, and removed commensurate with risk; the NIS 2 Art. 21(2)(e) third-clause maintenance phase + vulnerability-handling-and-disclosure leg maps to PR.PS-02 directly. ID.RA-01 anchors the vulnerabilities-identified-validated-recorded dimension — vulnerabilities in assets are identified, validated, and recorded; the NIS 2 Art. 21(2)(e) third-clause + fourth-clause vulnerability-handling-and-disclosure + CSIRT-coordinated disclosure pathway under Art. 12(1) maps to ID.RA-01 directly. The two subcategories together enable the essential / important entity to demonstrate ex post, through documented supplier-procurement records on the maintenance-dimension partial-coverage + industry-framework CI/CD build-time baseline + vulnerability-handling-and-disclosure records + Art. 20(1) management-body approval record, that the Art. 21(2)(e) third-clause security-in-maintenance + vulnerability-handling duty has been exercised with the `appropriate and proportionate` chapeau + state-of-the-art floor — the **CI/CD-pipeline dimension** is documented via the maintenance-dimension partial-coverage + industry-framework build-time baseline without an OJ-mandated CI/CD-pipeline control prescription.)*

---


## Security Requirements (NIS 2)

#### 7.3.1 — Entity-side maintenance pipeline evidence

```yaml
- req_id: 7.3.1
  volere_section: 15
  volere_subtype: immunity

  title: "Entity-side deployment and maintenance pipeline evidence for network and information systems"

  derives_from:
    hso_sub_so: SG-D-07.3.NIS2
    per_reg_so: SG-NIS2-017
    source_sr: SR-NIS2-028
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md
    objective_ref_section: "### D-07.3.1"

  description: |
    The product shall maintain release-path evidence showing that entity-side network-and-information-system maintenance releases are linked to vulnerability handling, disclosure intake, risk approval, deployment verification, and remediation tracking under the NIS2 maintenance perspective.

  fit_criterion: |
    For 100% of in-scope maintenance releases, the pipeline record links the release identifier to a vulnerability register entry or scheduled maintenance item, risk assessment, approval actor, build or package identifier, deployment timestamp, post-deployment verification result, rollback decision, and management-body or delegated-control evidence reference.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.2]

  nist_csf: [PR.PS-02, ID.RA-01]

  applicable_if:
    regs: [NIS2]
    scope_overlap: conditional

  satisfaction:
    controls: []
    nodes: []

  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md` and `../../Regulation/NIS2/02_SecurityRules_NIST.md` for the HSO caveat and inherited SR rationale; not duplicated here.
```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(e) third clause):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (e) … security in the maintenance of network and information systems, including vulnerability handling and disclosure." — Art. 21(2)(e) third clause NIS 2 (per SR-NIS2-028)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (SAME) with substantial scope-disjoint qualifier (CRDA-deep, D-07.3: NIS2↔CRA = COMPLEMENTARY (SAME — entity-side deployment-and-maintenance pipeline partial-coverage via the maintenance dimension vs product-side update delivery path via Annex I Part II (7)+(8); substantively scope-disjoint in baseline; Conditional Y on the supplier-customer boundary when an NIS 2 entity procures a CRA-conformant product)
```

### from regs/NIS2.md body

- The vulnerability-handling-and-disclosure leg (Art. 21(2)(e) fourth clause) is one of three coordinated legs — its operational implementation is the entity's coordinated vulnerability-handling capability (cross to D-02.3 — CRA is sole authority for the CVD-architecture, NIS 2 partial coverage per SG-NIS2-002).

<!-- aegis:purity: own_reg=NIS2; demoted=2; core_cross_mentions=0 -->