# D-07.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | (no OJ-mandated D-07.3 SO; partial via SG-CRA-009 cross-ref to Annex I Part II (7)+(8)) | Annex I Part II (7) `securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates` + Annex I Part II (8) `ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take` — **delivery path only**, **not** CI/CD build-time controls (signed artefacts, build-agent integrity). | **Product-level delivery path** at the manufacturer side — the maker-side update distribution obligation that meets the user-side (NIS 2) maintenance dimension at the supplier-customer boundary. AEGIS taxonomy §4.1 marks NIS 2 as sole authority; CRA participation is preserved as partial-coverage cross-ref only. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-side update delivery path (manufacturer securely distributes + disseminates updates free of charge + with advisory messages describing user-actionable security improvements) | manufacturer places product on market (Annex I Part I chapeau) + ongoing during support period per Art. 13(8) (5-year floor + 10-year update-availability tail per Art. 13(9)) | `without delay` (Annex I Part II (8)) — qualitative, no quantitative cadence; 5-year support-period floor (Art. 13(8) sentence 3); 10-year update-availability tail (Art. 13(9)); free-of-charge + clearly-described + information on security-improvements + actions-the-user-should-take (Annex I Part II (8)) | market surveillance authority (MSA) — Annex VII §2 design/development documentation (covering the secure-update-distribution mechanism) + Annex I Part II (7)+(8) update-distribution evidence + the user/customer as direct recipient of the update + the Article 14 actively-exploited-vulnerability / severe-incident flow when an update-distribution compromise is material | Annex I Part II (7) + Annex I Part II (8) + Art. 13(8) sentence 3 (support-period floor) + Art. 13(9) (10-year update-availability tail) + Annex VII §2 |

## Sub-SO (CRA)

#### D-07.3.2 — Sub-SO for CRA

```yaml
id: SG-D-07.3.CRA
subdomain: D-07.3
applies_to: [CRA]
inherits_from: SG-CRA-009 (partial cross-ref via Annex I Part II (7) — secure update distribution; SG-CRA-009 primary sub-domain is D-02.2 patch management with cross-ref to D-07.3 partial)
source_SR: SR-CRA-009
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The manufacturer of a product with digital elements shall securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates (Annex I Part II (7) CRA), and ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take (Annex I Part II (8) CRA).

**Considerations.**
- The product-side update delivery path is the operational heart of the CRA-side participation at D-07.3: the manufacturer-side distribution mechanism that securely delivers security updates to users — including, where appropriate, through automatic updates — across the support period (5-year floor from Art. 13(8) sentence 3) + the 10-year update-availability tail (Art. 13(9)).
- The Annex I Part II (7) + (8) text together constitute the OJ-mandated product-side update-delivery-path obligation — a partial-coverage cross-ref from SG-CRA-009 (D-02.2 patch management primary) to D-07.3 CI/CD Pipeline Security partial.
- **Coverage-scope caveat (CRITICAL):** CRA covers product-side update delivery path only, not CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments). The manufacturer-side CI/CD-pipeline compliance is demonstrated through: (a) CRA-side Annex I Part II (7)+(8) update-delivery-path evidence (Annex VII §2 design/development documentation covering the secure-update-distribution mechanism + advisory messages describing user-actionable security improvements); (b) the industry-framework CI/CD build-time baseline (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA); (c) the support-period operational implementation (5-year support-period floor + 10-year update-availability tail).
- The `without delay` (Annex I Part II (8)) qualitative threshold on update dissemination — no quantitative cadence — is calibrated by the Annex I Part II risk-assessment propagation across the 6 lifecycle phases (planning + design + development + production + delivery + maintenance) per Art. 13(2).
**CSF anchors (from `SR-CRA-009` v0.3 security_rationale — Annex I Part II (7) routing):**
ID.AM-02, GV.SC-03.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the CRA Annex I Part II (7) `securely distribute updates … in a timely manner, including, where appropriate, through automatic updates` + the cross-reference to the Annex I Part I (2)(c) automatic-security-updates default (SG-CRA-019 D-03.4 secure system defaults) form the SDLC-side update-distribution mechanism — the secure-update-distribution mechanism is a SDLC-coordinated operational instrument. PR.PS-02 anchors the software-maintenance dimension — software is maintained, replaced, and removed commensurate with risk; the CRA Annex I Part II (7) + (8) update-distribution obligation is realised across the support period (5-year floor from Art. 13(8) sentence 3) + the 10-year update-availability tail (Art. 13(9)) — the support-period tail establishes the duration over which the secure-update-distribution mechanism must remain operational. The two subcategories together enable the manufacturer to demonstrate ex post, through the documented Annex VII §2 design/development documentation covering the secure-update-distribution mechanism + the Annex I Part I (2)(c) automatic-security-updates default + Art. 13(8) support-period record + Art. 13(9) 10-year update-availability record + advisory messages describing user-actionable security improvements, that the Annex I Part II (7)+(8) update-delivery-path duty has been exercised with the `without delay` qualitative threshold + free-of-charge + clearly-described + information-on-security-improvements + actions-the-user-should-take dimensions. The **CI/CD build-time control dimension** (signed artefacts, build-agent integrity, ephemeral build environments) is documented via the industry-framework build-time baseline (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA) without an OJ-mandated CI/CD build-time control prescription.)*

---


## Security Requirements (CRA)

#### 7.3.2 — Product-side secure-update delivery evidence

```yaml
- req_id: 7.3.2
  volere_section: 15
  volere_subtype: immunity

  title: "Product-side secure-update delivery evidence for CRA-regulated products"

  derives_from:
    hso_sub_so: SG-D-07.3.CRA
    per_reg_so: SG-CRA-009
    source_sr: SR-CRA-009
    source_sr_current_file_refs: [SR-CRA-011, SR-CRA-017, SR-CRA-018, SR-CRA-047]
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md
    objective_ref_section: "### D-07.3.2"

  description: |
    The product shall maintain secure-update delivery evidence showing that CRA-regulated product updates are integrity-protected, disseminated through an approved channel, accompanied by release metadata, and retained as technical-documentation evidence for the support period.

  fit_criterion: |
    For 100% of security updates, the update-delivery record contains artefact identifier, signature or equivalent integrity proof, distribution-channel identifier, advisory-message reference, user-action metadata, publication timestamp, support-period applicability, and technical-documentation retention reference.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.3]

  nist_csf: [ID.AM-02, GV.SC-03]

  applicable_if:
    regs: [CRA]
    scope_overlap: conditional

  satisfaction:
    controls: []
    nodes: []

  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md` and `../../Regulation/CRA/02_SecurityRules_NIST.md` for the partial-coverage caveat and inherited SR rationale; not duplicated here.
```


---


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part II (7)+(8)):**
> "The manufacturer shall … (7) securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates; (8) ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take." — CRA Annex I Part II (7)+(8)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (SAME) with substantial scope-disjoint qualifier (CRDA-deep, D-07.3: NIS2↔CRA = COMPLEMENTARY (SAME — entity-side deployment-and-maintenance pipeline partial-coverage via the maintenance dimension vs product-side update delivery path via Annex I Part II (7)+(8); substantively scope-disjoint in baseline; Conditional Y on the supplier-customer boundary when an NIS 2 entity procures a CRA-conformant product; **T3-vs-text gap on NIS 2 side** — AEGIS taxonomy §4.1 marks NIS 2 as SOLE AUTHORITY with T3-vs-text caveat; **partial coverage on CRA side** — CRA Annex I Part II (7)+(8) covers product-side update delivery path, not CI/CD build-time controls)
```

### from regs/CRA.md body

- For an integrated manufacturer-controller-deployer stack (CRA manufacturer + NIS 2 entity + GDPR controller + DORA financial entity + AI Act provider/deployer), the CRA-side Annex I Part II (7)+(8) update-delivery-path discharges the NIS 2-side supplier-side patch pathway on the supplier-customer boundary of the Conditional-Y integrated stack.


<!-- aegis:purity: own_reg=CRA; demoted=2; core_cross_mentions=0 -->
