# D-10.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-071 + SO-CRA-072 | Products with digital elements undergo effective and regular tests and reviews; conformity is demonstrated via the conformity-assessment modules (Module A internal production control; Module B+C and H notified-body EU-type examination); test reports are part of the technical documentation (Annex I Part II (3) + Annex VII §6 + Annex VIII Part I + Annex VIII Part II per `SR-CRA-101`/`SR-CRA-103`/`SR-CRA-104`). | Product-level conformity-assessment via OJ-codified modules (Module A self-assessment / Module B+C and H notified body) + Annex I Part II (3) effective/regular tests; OJ-literal cadence `effective and regular`; Annex VII §6 test reports as evidence. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level conformity-assessment via OJ-codified modules + effective and regular tests + test reports | Annex I Part II (3) `carry out effective and regular tests and reviews of the product` + Annex VII §6 `reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I` + Annex VIII Part I (Module A internal production control self-assessment) + Annex VIII Part II (Module B+C and H notified-body EU-type examination certificate) | product (product with digital elements placed on the EU market) | MSA — Annex VII §6 test reports + Annex VIII Part I–IV conformity-assessment certificates | cadence OJ-literal `effective and regular` Annex I Part II (3) (entity-discretionary under proportionality); content partially codified for Annex VII §6 test reports + Annex VIII Part I–IV modules; depends on product classification (Class I/II/critical) per Art. 6 + Annex III |

## Sub-SO (CRA)

#### D-10.3.3 — Sub-SO for CRA

```yaml
id: SO-D-10.3.CRA
subdomain: D-10.3
applies_to: [CRA]
inherits_from: SO-CRA-071 + SO-CRA-072
source_SR: SR-CRA-101 + SR-CRA-103 + SR-CRA-104
activation: if CRA in applicable_regs
phase_1A_role: 3_of_5
```

**Objective.** Manufacturers of products with digital elements **carry out effective and regular tests and reviews of the product** (Annex I Part II (3) CRA), and the technical documentation shall contain **the reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I** (Annex VII §6 CRA); conformity is demonstrated via the Annex VIII Part I (Module A internal production control) or Part II (Module B+C and H notified-body EU-type examination) conformity-assessment modules depending on product classification (Class I / Class II / critical per Art. 6 + Annex III).

**CSF anchors (from `SR-CRA-101` + `SR-CRA-103` + `SR-CRA-104` v0.3 security_rationale):**
ID.RA-04, GV.OV-01, GV.PO-02, ID.RA-01, GV.OC-03, GV.SC-04.
*(ID.IM-03 — Configuration change control processes are in place — anchors the CRA Annex I Part II (3) `effective and regular tests and reviews` mapped to NIST CSF 2.0 ID.IM-03; ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Annex VII §6 test reports as input to the conformity-assessment risk dimension; DE.AE-02 — Adverse events are analyzed to identify or determine the scope of an incident — anchors the Annex I Part II (3) effective and regular tests as input to the vulnerability-handling chain; GV.OV-03 — Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Annex VIII Part I–IV modules feedback loop into the manufacturer's quality-management system (Art. 13(8) cross to D-09.1). The four subcategories together enable the manufacturer to demonstrate ex post, against the MSA, that the Annex I Part II (3) `effective and regular tests` + Annex VII §6 test reports + Annex VIII Part I–IV conformity-assessment modules were operational on the product layer with `effective and regular` cadence + appropriate Module selection (A vs. B+C and H) per product classification.)*

---


## Security Requirements (CRA)

#### 10.3.3 — Product-level conformity-assessment via OJ-codified modules + effective/regular tests + test reports

```yaml
- req_id: 10.3.3
  volere_section: 15
  volere_subtype: audit

  title: "Manufacturer carries out effective and regular tests of the product, demonstrates conformity via OJ-codified modules (Module A or Module B+C and H), and includes test reports in technical documentation"

  derives_from:
    hso_sub_so: SO-D-10.3.CRA
    per_reg_so: SO-CRA-071 + SO-CRA-072
    source_sr: SR-CRA-101 + SR-CRA-103 + SR-CRA-104
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/D-10.3.md
    objective_ref_section: "### D-10.3.3"

  description: |
    The product shall be subject to effective and regular tests and reviews (per CRA Annex I Part II (3) `carry out effective and regular tests and reviews of the product`), with conformity demonstrated via the OJ-codified modules — Annex VIII Part I (Module A internal production control — manufacturer self-assessment) or Annex VIII Part II (Module B+C and H notified-body EU-type examination certificate) depending on product classification (Class I / Class II / critical per Art. 6 + Annex III); the technical documentation shall contain reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I (per Annex VII §6).

  fit_criterion: |
    Product-level conformity-assessment is operational per Annex I Part II (3) + Annex VII §6 + Annex VIII Part I (Module A) + Annex VIII Part II (Module B+C and H) (SR-CRA-101 + SR-CRA-103 + SR-CRA-104) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the CRA Annex I Part II (3) `effective and regular tests and reviews` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Annex VII §6 test reports as input to the conformity-assessment risk dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Annex I Part II (3) effective and regular tests as input to the vulnerability-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Annex VIII Part I–IV modules feedback loop into the manufacturer's quality-management system (Art. 13(8) cross to 9.1)); the Annex I Part II (3) `effective and regular tests` cadence is entity-discretionary under proportionality; the Annex VIII Part I (Module A internal production control) is operational for Class I products (manufacturer self-assessment); the Annex VIII Part II (Module B+C and H notified-body EU-type examination certificate) is operational for Class II and critical products (per Art. 6 + Annex III); the Annex VII §6 test reports are part of the technical documentation and available to MSA on reasoned request per Art. 13(22); the manufacturer policies, processes, and procedures (Art. 13(8) — cross to 9.1) feed the conformity-assessment feedback loop; the recipient is the **MSA (market surveillance authority)** on the Annex VII §6 test reports + Annex VIII Part I–IV conformity-assessment certificates + Annex I Part II (3) effective/regular tests; verified by MSA audit pack (Annex VII §6 test reports + Annex VIII conformity-assessment certificates + Annex I Part II (3) effective/regular tests evidence + module selection per product classification + Art. 13(22) MSA cooperation evidence + Art. 13(8) manufacturer policies/processes/procedures feedback loop) + automated conformity-assessment test (Module A self-assessment operational for Class I / Module B+C and H notified-body EU-type examination operational for Class II and critical) + automated Annex VII §6 test-report test (test reports part of technical documentation) + manual Annex I Part II (3) effective/regular tests review (tests executed + evidenced + cadence operational).

  priority: MUST
  verification_method: TEST
  dependencies: [10.3.1 (Conditional — Y when controller deploys CRA-regulated products; GDPR Art. 32(1)(d) effectiveness-evaluation of security measures + CRA Annex I Part II (3) effective/regular tests + Annex VIII modules; entity-level vs. product-level; different testing purposes; the two regimes stack without consolidation — **NO OJ-level consolidation rule for testing**), 10.3.2 (Conditional — Y when NSIE procures CRA-conformant products; NIS 2 Art. 21(2)(f) effectiveness-assessment + CRA Annex I Part II (3) effective/regular tests + Annex VIII modules; CRA conformity-assessment is a specific dimension of NIS 2 effectiveness-assessment; the two regimes stack on the entity-level + product-level), 10.3.4 (Conditional — Y when DORA entity procures CRA-conformant products; CRA Annex VII §6 test reports + Annex VIII modules + DORA Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT for significant entities; product-level upstream vs. entity-level downstream; the two regimes stack without consolidation), 10.3.5 (**Y — when CRA-regulated product is also high-risk AI; CRA Annex I Part II (3) + Annex VII §6 + Annex VIII modules + AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) baseline testing `throughout their lifecycle` stack on the same product; NO OJ-level consolidation rule for testing** — CRDA-deep line 388: "Tension: NONE (no OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation)"; Phase 1 entities implement both regimes in parallel — the AI Act testing does NOT substitute for CRA testing and vice versa)]

  nist_csf: [ID.RA-04, GV.OV-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex VII §6 + Annex I Part II (3)):**
> "The technical documentation shall contain the reports of the tests carried out to verify the conformity of the product … and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I." — CRA Annex VII §6 (per SR-CRA-101)
> "Manufacturers of products with digital elements shall … carry out effective and regular tests and reviews of the product …" — CRA Annex I Part II (3) (per SR-CRA-101)
> "The manufacturer shall ensure that products with digital elements which are not subject to the conformity assessment procedures applicable to important products of class I or class II or to critical products may demonstrate conformity by using one of the following procedures: (a) Module A (internal production control) …" — CRA Annex VIII Part I (Module A) (per SR-CRA-103)
> "The notified body shall examine the design of the product and the vulnerability-handling processes … and issue an EU-type examination certificate …" — CRA Annex VIII Part II (Module B+C and H) (per SR-CRA-104)

**CRA article (verbatim, Annex VII §6 + Annex VIII Part I-IV):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.3: GDPR↔CRA = COMPLEMENTARY (SAME — effectiveness-evaluation vs. conformity-assessment; different testing purposes); NIS2↔CRA = COMPLEMENTARY (SAME — effectiveness-assessment + conformity-assessment stack; CRA conformity-assessment is a specific dimension of NIS 2 effectiveness-assessment); CRA↔DORA = COMPLEMENTARY (SAME — product-level conformity-assessment + entity-level testing programme stack; CRA upstream, DORA downstream); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act Art. 9(6)+(7) + Art. 15(1) stack for AI-enabled products; **NO OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation**))
```

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y when controller deploys CRA-regulated products); CRA↔NIS2 = Conditional (Y when NSIE procures CRA-conformant products); CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products); CRA↔AI_Act = Y (when CRA-regulated product is also high-risk AI; **NO OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation**); HL engages when the CRA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA compliance-testing obligation at D-10.3 is the **product-level conformity-assessment via OJ-codified modules** + **effective and regular tests** + **test reports** per Annex I Part II (3) + Annex VII §6 + Annex VIII Part I (Module A) + Annex VIII Part II (Module B+C and H) (per SR-CRA-101 + SR-CRA-103 + SR-CRA-104). Annex I Part II (3) `carry out effective and regular tests and reviews of the product` — the OJ-literal cadence `effective and regular`. Annex VII §6 `reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I`. Annex VIII Part I (Module A internal production control — manufacturer self-assessment for Class I) + Annex VIII Part II (Module B+C and H — notified-body EU-type examination certificate for Class II and critical) — the OJ-codified modules; module selection depends on product classification (Class I / Class II / critical per Art. 6 + Annex III). The recipient is the **MSA** on the Annex VII §6 test reports + Annex VIII Part I–IV conformity-assessment certificates + Annex I Part II (3) effective/regular tests. **NO OJ-level consolidation rule for testing** — even on the CRA↔AI_Act pair (CRDA-deep line 388: "Tension: NONE (no OJ-level consolidation rule for testing — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation)"), the CRA Annex I Part II (3) `effective and regular tests` + Annex VII §6 test reports + Annex VIII modules stack separately from the AI Act Art. 9(6) testing for risk management + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline; Phase 1 entities must implement both regimes in parallel — the AI Act testing does NOT substitute for CRA testing and vice versa. The CRA testing is upstream (product placement on EU market); the DORA testing is downstream (entity operational testing on the procured CRA-conformant product).
```

<!-- aegis:purity: own_reg=CRA; demoted=3; core_cross_mentions=1 -->
