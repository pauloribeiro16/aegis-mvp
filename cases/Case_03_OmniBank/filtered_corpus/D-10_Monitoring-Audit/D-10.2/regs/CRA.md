# D-10.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-069 + SG-CRA-070 | Test reports demonstrating verification of conformity of the product with digital elements and of the vulnerability-handling processes with the Annex I Part I and Part II cybersecurity requirements are part of the technical documentation and available on reasoned request from market surveillance authorities; the cybersecurity risk-assessment documentation is preserved, updated as appropriate during the support period, and made available — together with the technical documentation as a whole — to market surveillance authorities on reasoned request. | Product-level documentation traceability: Annex VII §6 test reports + Annex I Part II (3) effective/regular tests (SG-CRA-069) + Art. 13(4) sentence 1 + Annex VII §3 risk-assessment documentation + Art. 13(22) MSA cooperation (SG-CRA-070). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level documentation traceability: technical documentation (Annex VII §5–§8) + risk-assessment documentation (Annex VII §3) + test reports (Annex VII §6 + Annex I Part II (3) effective/regular tests) + SBOM on MSA reasoned request (Annex VII §8) + EU declaration of conformity (Annex VII §7) | Annex VII §5–§8 technical documentation content items (per `SR-CRA-088`) + Annex VII §3 risk-assessment documentation (per `SR-CRA-080`/`SR-CRA-102`) + Annex I Part II (3) effective and regular tests (per `SR-CRA-069`) + Art. 13(4) sentence 1 risk assessment in technical documentation + Art. 13(22) MSA cooperation | product (product with digital elements placed on the EU market) | MSA + users — Annex VII §5–§8 `on a reasoned request from a market surveillance authority, where necessary to check compliance, the software bill of materials` + Art. 13(22) MSA cooperation + Annex VII §3 risk-assessment documentation + Art. 13(8) manufacturer policies/processes/procedures (cross to D-09.1) | Annex VII §5–§8 + Annex VII §3 + Annex I Part II (3) + Art. 13(4) sentence 1 + Art. 13(22) + Art. 13(8) manufacturer policies/processes/procedures (cross to D-09.1) |

## Sub-SO (CRA)

#### D-10.2.2 — Sub-SO for CRA

```yaml
id: SG-D-10.2.CRA
subdomain: D-10.2
applies_to: [CRA]
inherits_from: SG-CRA-069 + SG-CRA-070
source_SR: SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102
activation: if CRA in applicable_regs
phase_1A_role: 2_of_4
```

**Objective.** The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmonised standards applied, test reports, copy of the EU declaration of conformity, SBOM on MSA reasoned request), **preserves the cybersecurity risk-assessment documentation** (Annex VII §3 + Art. 13(4) sentence 1) during the support period (10 years or support period, whichever longer) with updates as appropriate, and ensures **test reports demonstrating verification of conformity with Annex I Part I and Part II** are part of the technical documentation and available on reasoned request from market surveillance authorities (Annex VII §6 + Annex I Part II (3) + Art. 13(22) CRA).

**CSF anchors (from `SR-CRA-088` + `SR-CRA-080` + `SR-CRA-069` + `SR-CRA-070` + `SR-CRA-102` v0.3 security_rationale):**
GV.OC-03, ID.RA-04, GV.SC-04, ID.RA-05, GV.OV-01, GV.PO-02, PR.PS-02.
*(PR.DS-11 — Data are destroyed according to policy — anchors the CRA Annex VII §5–§8 technical documentation integrity mapped to NIST CSF 2.0 PR.DS-11; ID.AM-08 — Data are securely deleted or destroyed — anchors the support-period retention + updates-as-appropriate per DomainAnalysis cross-validation; GV.PO-02 — Information security policy is established, communicated, and maintained — anchors the Art. 13(8) manufacturer policies/processes/procedures + Annex VII §2(b) CVD policy; ID.RA-04 — Potential impacts and likelihoods of threats are identified — anchors the Annex VII §3 risk-assessment documentation + Art. 13(2) cybersecurity risk assessment per Art. 13(4) sentence 1. The four subcategories together enable the manufacturer to demonstrate ex post, against the MSA, that the Annex VII §5–§8 technical documentation + Annex VII §3 risk-assessment documentation + Annex I Part II (3) effective/regular tests were maintained with integrity + traceability during the support period and available on MSA reasoned request.)*

---


## Security Requirements (CRA)

#### 10.2.2 — Product-level technical documentation traceability + risk-assessment documentation + effective/regular tests + MSA cooperation

```yaml
- req_id: 10.2.2
  volere_section: 15
  volere_subtype: audit

  title: "Manufacturer maintains technical documentation + risk-assessment documentation + test reports + SBOM on MSA reasoned request during the support period with effective/regular tests of the product"

  derives_from:
    hso_sub_so: SO-10.2.CRA
    per_reg_so: SG-CRA-069 + SG-CRA-070
    source_sr: SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.2.md
    objective_ref_section: "### 10.2.2"

  description: |
    The product shall maintain technical documentation — including a general description of the product, design and development information, harmonised standards applied, test reports, a copy of the EU declaration of conformity, and the software bill of materials (SBOM) on reasoned request from a market surveillance authority (per CRA Annex VII §5–§8) — together with the cybersecurity risk-assessment documentation preserved during the support period (10 years or support period, whichever longer) with updates as appropriate (per Annex VII §3 + Art. 13(4) sentence 1) and the manufacturer's policies, processes, and procedures (per Art. 13(8) — cross to 9.1), and shall carry out effective and regular tests and reviews of the product (per Annex I Part II (3)) with the test reports part of the technical documentation and available on reasoned request from market surveillance authorities (per Annex VII §6 + Art. 13(22)).

  fit_criterion: |
    Product-level documentation traceability is operational per Annex VII §5–§8 + Annex VII §3 + Annex I Part II (3) + Art. 13(4) sentence 1 + Art. 13(22) (SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the CRA Annex VII §5–§8 technical documentation integrity mapped to NIST CSF 2.0 PR.DS-11) + ID.AM-08 (Data are securely deleted or destroyed — anchors the support-period retention + updates-as-appropriate per DomainAnalysis cross-validation) + GV.PO-02 (Information security policy is established, communicated, and maintained — anchors the Art. 13(8) manufacturer policies/processes/procedures + Annex VII §2(b) CVD policy) + ID.RA-04 (Potential impacts and likelihoods of threats are identified — anchors the Annex VII §3 risk-assessment documentation + Art. 13(2) cybersecurity risk assessment per Art. 13(4) sentence 1); the technical documentation content covers Annex VII §5 (general description of the product) + §6 (design and development information: harmonised standards applied + test reports) + §7 (copy of the EU declaration of conformity) + §8 (information on the software bill of materials — SBOM on MSA reasoned request); the risk-assessment documentation (Annex VII §3) is preserved during the support period (10 years or support period, whichever longer) with updates as appropriate per Art. 13(4) sentence 1; the effective and regular tests (Annex I Part II (3)) are operational with test reports available on reasoned request from MSA (Annex VII §6); the manufacturer policies, processes, and procedures (Art. 13(8) — cross to 9.1) are documented and operational; the MSA cooperation obligation (Art. 13(22)) is operationalised as: technical documentation + risk-assessment documentation + SBOM available to MSA on reasoned request `where necessary to check compliance`; the recipient is the **MSA (market surveillance authority) + users** on the Annex VII §5–§8 technical documentation + Annex VII §3 risk-assessment documentation + Annex I Part II (3) effective/regular tests + Art. 13(22) MSA cooperation; verified by MSA audit pack (technical documentation content items §5–§8 + risk-assessment documentation + Annex I Part II (3) test reports + Annex VII §6 test reports + Art. 13(8) manufacturer policies/processes/procedures + SBOM-on-request evidence) + automated documentation-integrity test (immutability / version control / cryptographic hash over technical documentation set) + automated support-period retention test (10 years or support period, whichever longer) + automated SBOM-on-request test (SBOM available to MSA on reasoned request within the Art. 13(22) window).

  priority: MUST
  verification_method: TEST
  dependencies: [10.2.1 (N (typically) — substantively scope-disjoint by record-type distinctness; CRA product documentation vs. GDPR compliance records; no joint condition on this pair alone; engages only via DORA or AI Act third-regulator joint-condition), 10.2.3 (Conditional — Y when DORA entity procures CRA-conformant products; CRA product documentation + DORA CIA+A information security policy stack; CRA product documentation feeds the DORA entity-level audit-records stack), 10.2.4 (Conditional — Y when CRA-regulated product is also high-risk AI; CRA Annex VII §5–§8 product documentation + Annex I Part II (3) effective/regular tests + AI Act Art. 12(1)+(2) automatic event logging + Art. 19(1) provider log retention stack; product documentation traceability feeds AI Act automatic event logging chain)]

  nist_csf: [GV.OC-03, ID.RA-04, GV.SC-04]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex VII §5-§8 + Annex VII §3):**
> "The technical documentation shall contain: (5) the list of the harmonised standards … applied in full or in part … (6) the reports of the tests carried out to verify the conformity of the product … (7) a copy of the EU declaration of conformity … (8) on a reasoned request from a market surveillance authority, where necessary to check compliance, the software bill of materials …" — CRA Annex VII §5-§8 (per SR-CRA-088)
> "The technical documentation shall contain an assessment of the cybersecurity risks against which the product with digital elements is designed, developed, produced, delivered and maintained pursuant to Article 13 …" — CRA Annex VII §3 (per SR-CRA-080)

**CRA article (verbatim, Annex VII §5-§8):**
> [as quoted above]

**CRA article (verbatim, Annex I Part I (2)(l)):**
> [as quoted in D-10.1 above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.2: GDPR↔CRA = COMPLEMENTARY (SAME — substantively scope-disjoint by record-type distinctness; N (typically) — different record types, different triggers); CRA↔DORA = COMPLEMENTARY (SAME — Conditional-Y when DORA entity procures CRA-conformant products; CRA product documentation + DORA CIA+A policy stack); CRA↔AI_Act = COMPLEMENTARY (SAME — Conditional-Y when CRA-regulated product is also high-risk AI; CRA product documentation + AI Act AI-system event logging stack))
```

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = N (typically) — substantively scope-disjoint by record-type distinctness; CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products); CRA↔AI_Act = Conditional (Y when CRA-regulated product is also high-risk AI); HL engages when the CRA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA documentation-traceability obligation at 10.2 is the **product-level technical documentation** + **risk-assessment documentation** + **effective/regular tests** + **MSA cooperation** per Annex VII §5–§8 + Annex VII §3 + Annex I Part II (3) + Art. 13(4) sentence 1 + Art. 13(22) (per SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102). Annex VII §5–§8 technical documentation content items (general description / design and development / harmonised standards applied + test reports / copy of EU declaration of conformity / SBOM on MSA reasoned request). Annex VII §3 risk-assessment documentation preserved during the support period (10 years or support period, whichever longer) with updates as appropriate per Art. 13(4) sentence 1. Annex I Part II (3) `carry out effective and regular tests and reviews of the product` — the OJ-literal cadence `effective and regular`. Annex VII §6 `reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I`. Art. 13(22) MSA cooperation — technical documentation + risk-assessment documentation + SBOM available to MSA on reasoned request `where necessary to check compliance`. Art. 13(8) manufacturer policies, processes, and procedures (cross to 9.1 Information Security Policies). The recipient is the **MSA + users** on the Annex VII §5–§8 technical documentation + Annex VII §3 risk-assessment documentation + Annex I Part II (3) effective/regular tests + Art. 13(22) MSA cooperation. **Substantively scope-disjoint GDPR ↔ CRA pair** (N (typically) — product documentation vs. compliance records; different record types at different triggers; no overlap on a single event at a single party; HL does NOT engage on GDPR ↔ CRA pair alone). **For DORA entities that procure CRA-conformant products**, the CRA documentation traceability (Annex VII §5–§8 + Annex VII §3) feeds the DORA entity-level audit-records stack; the CRA product documentation is upstream and the DORA CIA+A information security policy is downstream.
```

<!-- aegis:purity: own_reg=CRA; demoted=3; core_cross_mentions=1 -->
