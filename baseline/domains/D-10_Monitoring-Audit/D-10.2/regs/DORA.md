# D-10.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-031 (partial via Art. 9(4)(a)) | An information security policy is developed and documented defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable; logging is implicit in the CIA+A monitoring, not standalone. | Financial-entity information security policy with CIA+A rules; **partial coverage only** — no dedicated audit-logging mandate (no analogue to NIS 2 Art. 21(2)(j) per CRDA D-10.2 §CRA ↔ DORA pair); CRA Art. 13(11) is the dedicated authority for product-level logging requirements. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-level information security policy defining rules to protect CIA+A — logging is implicit in the CIA+A monitoring, not a standalone audit-logging mandate | Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` | entity (financial entity under DORA scope per Art. 2) | NCA — Art. 9(4)(a) information security policy + EBA Guidelines supervisory baseline | Art. 9(4)(a) + Art. 4 proportionality (size, nature, scale, complexity) + Art. 8(1) per `SR-DORA-030` (cross to D-10.1 continuous monitoring — logging implicit under CIA+A policy) |

## Sub-SO (DORA)

#### D-10.2.3 — Sub-SO for DORA

```yaml
id: SO-D-10.2.DORA
subdomain: D-10.2
applies_to: [DORA]
inherits_from: SO-DORA-031 (partial)
source_SR: SR-DORA-031
activation: if DORA in applicable_regs
phase_1A_role: 3_of_4
```

**Objective.** Financial entities **develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable** (Art. 9(4)(a) DORA); logging is **implicit in the CIA+A monitoring** under the Art. 8(1) continuous-monitoring mandate, not a standalone audit-logging obligation at D-10.2.

**CSF anchors (from `SR-DORA-031` v0.3 security_rationale):**
GV.PO-01 (primary), PR.DS-12, GV.OC-03.
*(GV.PO-01 — Organizational information security policy is established and communicated — anchors the DORA Art. 9(4)(a) information security policy mapped to NIST CSF 2.0 GV.PO-01; PR.DS-12 — Data assets are managed consistent with the organization's risk strategy — anchors the CIA+A 4-way of data/information assets/ICT assets 3-way per DomainAnalysis cross-validation; GV.OC-03 — Legal and regulatory requirements regarding cybersecurity are understood and managed — anchors the Art. 9(4)(a) CIA+A rules + EBA Guidelines supervisory baseline. The three subcategories together enable the financial entity to demonstrate ex post, against the NCA + EBA Guidelines supervisory baseline, that the Art. 9(4)(a) information security policy with CIA+A rules was developed and documented, and that the policy governs the entity-level audit-records stack under the Art. 4 proportionality factors.)*

---


## Security Requirements (DORA)

#### 10.2.3 — Entity-level information security policy with CIA+A rules (logging implicit, partial coverage)

```yaml
- req_id: 10.2.3
  volere_section: 15
  volere_subtype: audit

  title: "Financial entity develops and documents an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, with logging implicit in CIA+A monitoring"

  derives_from:
    hso_sub_so: SO-10.2.DORA
    per_reg_so: SO-DORA-031 (partial)
    source_sr: SR-DORA-031
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.2.md
    objective_ref_section: "### 10.2.3"

  description: |
    The product shall develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable (per DORA Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable`), with logging **implicit in the CIA+A monitoring under the Art. 8(1) continuous-monitoring mandate (cross to 10.1)**, not a standalone audit-logging obligation at 10.2.

  fit_criterion: |
    An information security policy is developed and documented per Art. 9(4)(a) (SR-DORA-031) verified by GV.PO-01 primary (Organizational information security policy is established and communicated — anchors the DORA Art. 9(4)(a) information security policy mapped to NIST CSF 2.0 GV.PO-01) + PR.DS-12 (Data assets are managed consistent with the organization's risk strategy — anchors the CIA+A 4-way of data/information assets/ICT assets 3-way per DomainAnalysis cross-validation) + GV.OC-03 (Legal and regulatory requirements regarding cybersecurity are understood and managed — anchors the Art. 9(4)(a) CIA+A rules + EBA Guidelines supervisory baseline); the information security policy defines rules to protect the CIA+A of data, information assets and ICT assets (the 3-way asset scope), including those of customers where applicable; the policy is documented, communicated, and maintained per GV.PO-01; the logging dimension is **implicit in the CIA+A monitoring under the Art. 8(1) OJ-literal locus Art. 9(1) continuous-monitoring mandate (cross to 10.1)** — **partial coverage only**, no standalone audit-logging obligation at 10.2; the policy is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity); the recipient is the **NCA (national competent authority)** on the Art. 9(4)(a) information security policy + EBA Guidelines supervisory baseline; verified by NCA audit pack (information security policy content + CIA+A rules + EBA Guidelines compliance + Art. 4 proportionality calibration + DORA-led audit-records stack governance) + automated policy-documentation test (policy exists in writing + policy content covers CIA+A 4-way + policy references the Art. 8(1) continuous-monitoring mandate + policy identifies the audit-records stack governance).

  priority: MUST
  verification_method: TEST
  dependencies: [10.2.1 (Conditional — Y when DORA financial entity is a controller; DORA Art. 9(4)(a) information security policy + GDPR Art. 30(3) compliance records stack; DORA-led CIA+A stack with GDPR compliance records as sub-component), 10.2.2 (Conditional — Y when DORA entity procures CRA-conformant products; DORA Art. 9(4)(a) CIA+A policy + CRA Annex VII §5–§8 product documentation stack; CRA product documentation feeds the DORA entity-level audit-records stack), 10.2.4 (Conditional — Y when DORA financial entity deploys high-risk AI; DORA Art. 9(4)(a) CIA+A policy + AI Act Art. 12(1)+(2) automatic event logging + Art. 19(1) provider log retention stack; DORA-led CIA+A policy with AI Act automatic event logging as AI-system-level overlay)]

  nist_csf: [GV.PO-01, PR.DS-12, GV.OC-03]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim, Art. 9(4)(a) per SR-DORA-031):**
> "Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable." — Art. 9(4)(a) DORA

**DORA article (verbatim, Art. 9(4)(a) per SR-DORA-031):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.2: GDPR↔DORA = COMPLEMENTARY (SAME — Conditional-Y when DORA financial entity is controller; GDPR compliance records + DORA CIA+A policy stack); CRA↔DORA = COMPLEMENTARY (SAME — Conditional-Y when DORA entity procures CRA-conformant products; CRA product documentation + DORA CIA+A policy stack); DORA↔AI_Act = COMPLEMENTARY (SAME — Conditional-Y when DORA financial entity deploys high-risk AI; DORA CIA+A policy + AI Act AI-system event logging stack))
```

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y when DORA financial entity is a controller); DORA↔CRA = Conditional (Y when DORA entity procures CRA-conformant products); DORA↔AI_Act = Conditional (Y when DORA financial entity deploys high-risk AI); HL engages when the DORA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA audit-logging obligation at 10.2 is the **entity-level information security policy with CIA+A rules** per Art. 9(4)(a) (per SR-DORA-031) — **partial coverage only**. Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` — the CIA+A 4-way of data/information assets/ICT assets 3-way. Logging is **implicit in the CIA+A monitoring** under the Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) continuous-monitoring mandate (cross to 10.1) — DORA does NOT impose a standalone audit-logging mandate at 10.2; the CRA Art. 13(11) is the dedicated authority for product-level logging requirements (cross to 10.1 continuous monitoring + 10.2 product documentation traceability). The recipient is the **NCA** on the Art. 9(4)(a) information security policy + EBA Guidelines supervisory baseline. The policy is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity). **For DORA financial entities that are also controllers**, the DORA Art. 9(4)(a) information security policy with CIA+A rules governs the entity-level audit-records stack under the Art. 4 proportionality factors, and the GDPR compliance records are maintained as a sub-component within the DORA-led CIA+A stack. **For DORA entities that procure CRA-conformant products**, the CRA documentation traceability (Annex VII §5–§8 + Annex VII §3) feeds the DORA entity-level audit-records stack; the CRA product documentation is upstream and the DORA CIA+A information security policy is downstream. **For DORA financial entities that deploy high-risk AI**, the AI Act Art. 12(1)+(2) automatic event logging + Art. 19(1) provider log retention feeds the DORA-led CIA+A stack with the AI Act automatic event logging as an AI-system-level overlay.
```

<!-- aegis:purity: own_reg=DORA; demoted=3; core_cross_mentions=1 -->

