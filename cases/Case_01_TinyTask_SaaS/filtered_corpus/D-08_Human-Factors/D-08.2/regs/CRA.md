# D-08.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-048 (partial via SR-CRA-108 Annex II §8(f)) | Integrator-facing information delivery for compliance with Annex I + Annex VII. | Limited role-specific dimension aimed at integrators (B2B), not workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | integrator (B2B external party) receiving information necessary for compliance with Annex I + Annex VII (partial coverage per AEGIS taxonomy §4.1) | manufacturer ships integrator-facing information per Annex II §8(f) `where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` | `intended for integration` per the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4) — not as third-party speculation; where intended purpose does not include integration, §8(f) is not engaged; support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)) | integrator (B2B external party) + market surveillance authority (MSA) — Annex II §8(f) integrator information + Art. 13(18) support-period accessibility | Art. 13(1) + Annex II §8(f) + Art. 13(18) support-period accessibility + Recital 25 (Annex II scope) |

## Sub-SO (CRA)

#### D-08.2.3 — Sub-SO for CRA (partial)

```yaml
id: SO-D-08.2.CRA
subdomain: D-08.2
applies_to: [CRA]
inherits_from: SO-CRA-048 (partial via SR-CRA-108 Annex II §8(f))
source_SR: SR-CRA-108
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Where the product with digital elements is intended for integration into other products with digital elements, the manufacturer provides the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).

**Considerations.**
- The clause sits within the Annex II user-information package; it is the supply-chain-facing counterpart to the §8(a)–(e) user-facing instructions.
- The chosen PR.AT-02 mapping at SR-CRA-108 anchors the integrator's understanding of the upstream product's threat model, configuration constraints, and vulnerability-handling interface — the workforce-supplier analog for the integrator side.
- GV.SC-03 (per SR-CRA-108 security_rationale) anchors the contractual / information-disclosure layer: the §8(f) information is the information counterpart to a contractually-anchored SCRM commitment.
- The chosen reading of `intended for integration` is the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4), not third-party speculation about possible integration patterns. Where the intended purpose does not include integration, §8(f) is not engaged.
**CSF anchors (from `SR-CRA-108` v0.3 security_rationale):**
PR.AT-02, GV.SC-03.
*(PR.AT-02 anchors the integrator's understanding of the upstream product's threat model, configuration constraints, and vulnerability-handling interface — the workforce-supplier analog for the integrator side. GV.SC-03 anchors the contractual / information-disclosure layer: the §8(f) information is the information counterpart to a contractually-anchored SCRM commitment. Together, PR.AT-02 and GV.SC-03 give the manufacturer an integrator-engagement control set that the integrator can consume to discharge its own Annex I and Annex VII obligations, and that the manufacturer can demonstrate ex post was operative for products intended for integration.)*

---


## Security Requirements (CRA)

#### 8.2.3 — Integrator-facing upstream product information delivery for Annex I + Annex VII compliance

```yaml
- req_id: 8.2.3
  volere_section: 15
  volere_subtype: immunity

  title: "Where the product is intended for integration, information necessary for the integrator to comply with Annex I cybersecurity requirements and Annex VII documentation requirements is delivered"

  derives_from:
    hso_sub_so: SO-8.2.CRA
    per_reg_so: SO-CRA-048 (partial)
    source_sr: SR-CRA-108
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.3"

  description: |
    The product with digital elements shall, where intended for integration into other products with digital elements, be accompanied by information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (CRA Annex II §8(f)), on the B2B integrator audience — partial coverage per AEGIS taxonomy §4.1.

  fit_criterion: |
    Where the product with digital elements is `intended for integration` per the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4 — not third-party speculation about possible integration patterns), the product is accompanied by information via PR.AT-02 integrator's understanding of the upstream product's threat model, configuration constraints, and vulnerability-handling interface + GV.SC-03 contractual/information-disclosure layer (the §8(f) information is the information counterpart to a contractually-anchored SCRM commitment); the information covers the cybersecurity measures required for the integrator to maintain Annex I compliance + the documentation requirements set out in Annex VII; the information is provided in paper or electronic form and remains accessible for the support period ≥ 5 years under Art. 13(8) sentence 3 + 10-year Annex II information accessibility under Art. 13(18); the CRA participation at 8.2 is partial — Annex II §8(f) addresses the B2B integrator audience (not workforce) per AEGIS taxonomy §4.1; the asymmetry — workforce training (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is unique to 8.2 per DomainAnalysis §8.2 line 107; the Annex II §8(f) integrator-B2B audience operates on a substantively scope-disjoint audience from the GDPR / NIS 2 / DORA workforce programmes and the AI Act human-overseer role within the deployer organization — no consolidation rule applies on the 4 CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act — Executor-recommended SCOPE-DISJOINT per CRDA-deep §8.2); **8.1 layer (8.1.3)** adds the user-facing secure-use instructions (Annex II §8(a)–(e)) + the integrator-facing dimension (Annex II §8(f)) at the general-awareness level — this 8.2 layer adds the role-specific depth on the integrator-B2B audience (Annex II §8(f) only — the integrator's role-specific understanding of threat model + configuration + vulnerability-handling); verified by Annex II §8(f) integrator-information review (B2B integrators only — product intended for integration) + Art. 13(18) support-period accessibility audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + market surveillance authority (MSA) / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.3 (8.1 layer is the upstream Annex II §8(a)–(e) user-facing + §8(f) integrator-facing general-awareness substrate), 8.2.2 (substantively scope-disjoint — workforce vs B2B integrator — no consolidation rule), 8.2.4 (substantively scope-disjoint — B2B integrator vs internal staff — no consolidation rule), 8.2.5 (substantively scope-disjoint — B2B integrator vs AI-overseer role within deployer organization — no consolidation rule)]

  nist_csf: [PR.AT-02, GV.SC-03]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex II §8(f)):**
> "The product shall be accompanied by detailed instructions and information … including … (f) where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII." — CRA Annex II §8(f)

**CRA article (verbatim, Annex II §8(f)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SCOPE-DISJOINT (CRDA-deep, D-08.2 Executor-recommended: GDPR↔CRA = SCOPE-DISJOINT (workforce vs integrator-B2B audiences; different objects); NIS2↔CRA = SCOPE-DISJOINT (workforce vs integrator-B2B audiences; different objects); CRA↔DORA = SCOPE-DISJOINT (integrator-B2B vs internal staff audiences; different objects); CRA↔AI_Act = SCOPE-DISJOINT (integrator-B2B vs AI-overseer role within deployer organization; different objects))
```

### from regs/CRA.md body

- The CRA participation at D-08.2 is partial: Annex II §8(f) addresses the integrator-B2B audience — not the manufacturer's or operator's workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence.

### from regs/CRA.md body

- The asymmetry — workforce training (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is unique to D-08.2 (per DomainAnalysis §D-08.2 line 107).

### from regs/CRA.md body

- For an integrated manufacturer-controller-deployer, the CRA-side Annex II §8(f) integrator information is independent of the GDPR Art. 39(1)(b) DPO-catalysed workforce training, the NIS 2 employee risk-identification training, the DORA Art. 13(6) internal staff training, and the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (different audiences: integrator-B2B vs AI-overseer role within deployer organization) — substantively scope-disjoint across all four pairs.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: N   # CRA↔GDPR = N substantively scope-disjoint (workforce vs integrator-B2B); CRA↔NIS2 = N substantively scope-disjoint (workforce vs integrator-B2B); CRA↔DORA = N substantively scope-disjoint (integrator-B2B vs internal staff); CRA↔AI_Act = N substantively scope-disjoint (integrator-B2B vs AI-overseer role within deployer organization); HL does NOT engage on the 4 CRA-involving pairs; CRA sub-SO activates standalone when CRA in applicable_regs

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA role-specific competence obligation is the **Annex II §8(f) integrator-facing B2B information** — `where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII`. The clause sits within the Annex II user-information package; it is the supply-chain-facing counterpart to the §8(a)–(e) user-facing instructions (per Recital 25). The CRA participation at 8.2 is partial: Annex II §8(f) addresses the integrator-B2B audience — not the manufacturer's or operator's workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence. The asymmetry — workforce training (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is unique to 8.2 (per DomainAnalysis §8.2 line 107). The chosen PR.AT-02 mapping at SR-CRA-108 anchors the integrator's understanding of the upstream product's threat model, configuration constraints, and vulnerability-handling interface — the workforce-supplier analog for the integrator side. GV.SC-03 (per SR-CRA-108 security_rationale) anchors the contractual / information-disclosure layer: the §8(f) information is the information counterpart to a contractually-anchored SCRM commitment. The chosen reading of `intended for integration` is the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4), not third-party speculation about possible integration patterns. Where the intended purpose does not include integration, §8(f) is not engaged. For an integrated manufacturer-controller-deployer, the CRA-side Annex II §8(f) integrator information is independent of the GDPR Art. 39(1)(b) DPO-catalysed workforce training, the NIS 2 employee risk-identification training, the DORA Art. 13(6) internal staff training, and the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (different audiences: integrator-B2B vs AI-overseer role within deployer organization) — substantively scope-disjoint across all four pairs (Executor-recommended SCOPE-DISJOINT per CRDA-deep §8.2). The recipient is the integrator (B2B external party) + market surveillance authority (MSA) — Annex II §8(f) integrator information + Art. 13(18) support-period accessibility. (Copied from the HSO Considerations block of `### 8.2.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=1 -->