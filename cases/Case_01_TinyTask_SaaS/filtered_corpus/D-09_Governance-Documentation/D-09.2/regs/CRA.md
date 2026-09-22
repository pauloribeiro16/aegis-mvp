# D-09.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-053 + SO-CRA-054 | Cybersecurity risk assessment documented + updated during support period (Art. 13(3) sentence 1); covers intended purpose + reasonably foreseeable use including operational environment and assets to be protected (Art. 13(3) sentence 2); maps Annex I Part I (2) applicability and indicates how those requirements are implemented as informed by the risk assessment (Art. 13(3) sentence 3); documented in Annex VII §3 risk-assessment record; reviewed on material change of risk (Art. 13(3) sentence 1 `updated as appropriate`). | Product-level pre-market + support-period cybersecurity risk assessment; supports Annex I Part I (2) applicability mapping; **subject to CRA Art. 13(4) sentence 2 consolidation rule** with AI Act Art. 9 risk management. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product cybersecurity risk (product-side dimension) — pre-market + support-period cybersecurity risk assessment; Annex I Part I (2) applicability mapping | product placement on market (Art. 13(1) trigger) + support-period maintenance (Art. 13(8) — cross to D-09.4) + on-change review of risk | not codified for content template; substantively per Art. 13(2) `take into account the intended purpose and reasonably foreseeable use, including operational environment and assets to be protected` + Art. 13(3) sentence 3 `indicate whether and in what manner the Annex I Part I (2) requirements apply to the relevant product and how those requirements are implemented as informed by the risk assessment` + Annex VII §3 risk-assessment record | pre-market + on-change review of risk per Art. 13(3) sentence 1 `updated as appropriate` (material change of product, material change of threat landscape, or upon becoming aware of a previously unidentified vulnerability per SR-CRA-066) | market surveillance authority (MSA) — Art. 13(3) documented + updated + Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping + Art. 13(4) sentence 1 technical-documentation inclusion + Art. 13(4) sentence 2 unification with AI Act Art. 9 risk management | Art. 13(2) risk assessment (intended purpose + reasonably foreseeable use + operational environment + assets to be protected) + Art. 13(3) sentence 1 `documented and updated` + sentence 2 `intended purpose and reasonably foreseeable use` + sentence 3 `Annex I Part I (2) applicability mapping` + Art. 13(4) sentence 1 (technical-documentation inclusion) + Art. 13(4) sentence 2 (consolidation with AI Act Art. 9 risk management) + Art. 13(7) update on becoming aware of vulnerability + Art. 13(8) support period + Annex I Part I (2) applicability + Annex VII §3 risk-assessment record |

## Sub-SO (CRA)

#### D-09.2.3 — Sub-SO for CRA

```yaml
id: SO-D-09.2.CRA
subdomain: D-09.2
applies_to: [CRA]
inherits_from: SO-CRA-053 + SO-CRA-054
source_SR: SR-CRA-064 + SR-CRA-065 + SR-CRA-066 + SR-CRA-079 + SR-CRA-080 + SR-CRA-081
activation: if CRA in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2)** and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2) and indicating Annex I Part I (2) applicability (Art. 13(3) sentence 3) — documented in the **Annex VII §3 risk-assessment record** (Art. 13(4) sentence 1 + Annex VII §3 CRA).

**CSF anchors (from `SR-CRA-064` + `SR-CRA-065` + `SR-CRA-066` + `SR-CRA-079` v0.3 security_rationale):**
PR.PS-06, GV.PO-02, ID.RA-05 (primary), GV.OV-02.

---


## Security Requirements (CRA)

#### 9.2.3 — Manufacturer-side pre-market + support-period cybersecurity risk assessment with Annex VII §3 record + subject to CRA Art. 13(4) sentence 2 consolidation

```yaml
- req_id: 9.2.3
  volere_section: 15
  volere_subtype: integrity

  title: "Manufacturer documents the cybersecurity risk assessment referred to in Art. 13(2) covering intended purpose + reasonably foreseeable use + Annex I Part I (2) applicability, updated during support period and recorded in Annex VII §3"

  derives_from:
    hso_sub_so: SO-9.2.CRA
    per_reg_so: SO-CRA-053 + SO-CRA-054
    source_sr: SR-CRA-064 + SR-CRA-065 + SR-CRA-066 + SR-CRA-079 + SR-CRA-080 + SR-CRA-081
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.3"

  description: |
    The product shall ensure that the manufacturer documents and updates, during the support period, the cybersecurity risk assessment referred to in Art. 13(2) covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2), indicating how Annex I Part I (2) requirements apply and are implemented (Art. 13(3) sentence 3), with the assessment drawn up before placing the product on the market and updated during the support period (Art. 13(4) sentence 1 + Art. 31(2)) — documented in the Annex VII §3 risk-assessment record, and subject to the CRA Art. 13(4) sentence 2 consolidation rule where applicable.

  fit_criterion: |
    The cybersecurity risk assessment is documented under Art. 13(3) sentence 1 `documented and updated` (SR-CRA-064) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 13(2) `cybersecurity risk assessment … taking into account the intended purpose and reasonably foreseeable use, including operational environment and assets to be protected`) + GV.SC-07 suppliers-prioritised-by-criticality dimension (the supplier-side risk-assessment perspective informing the manufacturer risk assessment, cross to 6.1); the assessment covers per Art. 13(3) sentence 2 the intended purpose + reasonably foreseeable use including operational environment and assets to be protected, with reasonable foreseeability scoped to `intentional misuses … as well as in those uses which are reasonably foreseeable by the manufacturer`; the assessment indicates per Art. 13(3) sentence 3 `whether and in what manner the Annex I Part I (2) requirements apply to the relevant product and how those requirements are implemented as informed by the risk assessment` — the applicability mapping from Annex I Part I (2) to the product's circumstances; the assessment is documented in the Annex VII §3 risk-assessment record per Art. 13(4) sentence 1 `The product with digital elements shall be accompanied by the technical documentation referred to in Annex VII` + Annex VII §3 (per SR-CRA-066 ambiguity_notes); the assessment is drawn up before placing on the market and updated during the support period per Art. 13(3) sentence 1 `updated as appropriate` + Art. 13(7) `upon becoming aware of a previously unidentified vulnerability` + Art. 13(8) support period + Art. 31(2) `drawn up before placing on the market and updated during the support period`; the assessment is retained at the disposal of market surveillance authorities for at least 10 years after placement on the market or the support period, whichever is longer, per Art. 13(13); the assessment is subject to the presumption-of-conformity machinery per Art. 27(1)/(2)/(5)/(8)/(9) where harmonised standards / common specifications / European cybersecurity certification scheme under Regulation (EU) 2019/881 apply — the presumption discharges the CRA conformity-assessment obligation where alignment exists (per SR-CRA-066 ambiguity_notes); **CRITICAL consolidation rule — CRA Art. 13(4) sentence 2**: `The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements` — for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment on a single artefact (per SR-CRA-066 ambiguity_notes); this is the ONLY OJ-level cross-regulation consolidation rule in 9.2 and no other cross-regulation substitution is OJ-permitted (the GDPR DPIA on data-subject rights must be a separate artefact even when CRA cybersecurity risk assessment performed, per CRDA flag DomainAnalysis §9.2 line 175); the manufacturer can demonstrate ex post, against the market surveillance authority, that the Art. 13(3) sentence 1 documented-and-updated risk assessment was carried out with the Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping + on-material-change update per Art. 13(7) + 10-year retention per Art. 13(13).

  priority: MUST
  verification_method: TEST
  dependencies: [9.2.5 (when product is both CRA-regulated and AI-Act high-risk — CRA Art. 13(4) sentence 2 consolidation rule permits AI Act Art. 9 risk-management system to substitute for CRA Art. 13(3) cybersecurity risk assessment on a single artefact; the ONLY OJ-level cross-regulation consolidation rule in 9.2), 9.2.1 (when controller-manufacturer — CRA cybersecurity risk assessment on product cybersecurity risk + GDPR DPIA on data-subject rights; DIFFERENT-PERSPECTIVE, distinct artefacts, **no OJ-level consolidation rule** even when CRA risk assessment performed — GDPR DPIA must be a separate artefact), 9.2.4 (when DORA entity procures CRA-conformant — CRA product-level pre-market + DORA entity-level operational; COMPLEMENTARY, Conditional-Y scope overlap), 9.2.2 (when entity procures CRA-conformant — CRA product-level + NIS 2 entity-level operational; COMPLEMENTARY; CRA risk-assessment record is an input to NIS 2 entity's supplier-risk register, meet at supplier-customer interface)]

  nist_csf: [PR.PS-06, GV.PO-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 13(2) + Art. 13(3) + Art. 13(4) sentence 2):**
> [as quoted above]
> "The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements." — Art. 13(4) sentence 2 CRA

**CRA article (verbatim, Art. 13(2) + Art. 13(3)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.2: GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA on data-subject rights vs pre-market + support-period cybersecurity risk assessment on product cybersecurity risk; **no OJ-level consolidation rule** even when CRA risk assessment performed); NIS2↔CRA = COMPLEMENTARY (SAME — entity-level operational + product-level pre-market; meet at supplier-customer interface); CRA↔DORA = COMPLEMENTARY (SAME — CRA product-level pre-market + DORA entity-level operational; Conditional-Y scope overlap); **CRA↔AI_Act = COMPLEMENTARY (SAME) — CRITICAL CONSOLIDATION RULE**: CRA Art. 13(4) sentence 2 explicitly permits the AI Act Art. 9 risk-management system to substitute for the CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product (per SR-CRA-066 ambiguity_notes); **only OJ-level cross-regulation consolidation rule in D-09.2**)
```

### from regs/CRA.md body

*(ID.RA-05 — Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response — anchors the CRA Art. 13(3) documented-and-updated cybersecurity risk assessment mapped to NIST CSF 2.0 ID.RA-05. GV.SC-07 — Suppliers prioritised by criticality — anchors the supply-chain risk dimension per DomainAnalysis §D-09.2 line 180 cross-validation. The CRA risk assessment covers (1) intended purpose + reasonably foreseeable use (including operational environment and assets to be protected) per Art. 13(3) sentence 2; (2) Annex I Part I (2) applicability mapping per Art. 13(3) sentence 3; (3) technical-documentation inclusion per Art. 13(4) sentence 1; (4) Annex VII §3 risk-assessment record per the documentation requirement. The **CRA Art. 13(4) sentence 2 unification rule** permits the AI Act Art. 9 risk-management system to substitute for the CRA cybersecurity risk assessment when both apply to the same product — for AI-enabled CRA-regulated products, a unified AI Act Art. 9 risk-management system discharges both CRA Art. 13(3) cybersecurity risk assessment and AI Act Art. 9 risk management on a single artefact (per SR-CRA-066 ambiguity_notes). The two subcategories together enable the manufacturer to demonstrate ex post, against the market surveillance authority, that the Art. 13(3) sentence 1 documented-and-updated risk assessment was carried out with Annex VII §3 documentation, Annex I Part I (2) applicability mapping, and updated on material change of risk per Art. 13(3) sentence 1 `updated as appropriate` + Art. 13(7) update-on-becoming-aware-of-vulnerability. **Note — CRA risk assessment does NOT extend to data-subject rights**: per CRDA flag (DomainAnalysis §D-09.2 line 175), the GDPR DPIA on data-subject rights must be a separate artefact even when the CRA cybersecurity risk assessment has been performed.)*

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Y (CRA-regulated product processes personal data; **no OJ-level consolidation rule** — GDPR DPIA must be a separate artefact even when CRA risk assessment performed); CRA↔NIS2 = Y (entity procures CRA-conformant products; CRA product-level + NIS 2 entity-level operational; meet at supplier-customer interface); CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant; same; CRA product-level + DORA entity-level operational); CRA↔AI_Act = Y (**CRITICAL CONSOLIDATION RULE** — CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management system to substitute for CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product; only OJ-level cross-regulation consolidation rule in 9.2); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA impact-and-risk-assessment obligation at 9.2 is the **pre-market + support-period cybersecurity risk assessment** under Art. 13(3) sentence 1 `documented and updated` + sentence 2 `intended purpose and reasonably foreseeable use` + sentence 3 `Annex I Part I (2) applicability mapping` + Art. 13(4) sentence 1 technical-documentation inclusion + Art. 13(4) sentence 2 consolidation with AI Act Art. 9 + Art. 13(7) update on becoming aware of vulnerability + Art. 13(8) support period + Annex VII §3 risk-assessment record. The risk object is **product cybersecurity risk**, distinct from the GDPR DPIA's data-subject-rights object (per CRDA flag DomainAnalysis §9.2 line 175). The reasonable-foreseeability scoping under Art. 13(3) sentence 2 + the Annex I Part I (2) applicability mapping under sentence 3 are the **content template** for the assessment; the substantive risk-analysis methodology is entity-discretionary under CRA's OJ. The **support-period** is determined per Art. 13(8) sentence 2 with the listed factors (reasonable expected user lifetime + nature of product + intended purpose + relevant industry standards + vendor statements). The **presumption-of-conformity machinery** per Art. 27(1)/(2)/(5)/(8)/(9) discharges the CRA conformity-assessment obligation where the assessment aligns with harmonised standards / common specifications / European cybersecurity certification schemes — but the presumption is **rebuttable** and the MSA may verify Annex I compliance on substance. **CRITICAL consolidation rule — CRA Art. 13(4) sentence 2** (per SR-CRA-066 ambiguity_notes): for AI-enabled CRA-regulated products, the AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment on a single artefact; this is the ONLY OJ-level cross-regulation consolidation rule in 9.2. No other cross-regulation substitution is OJ-permitted — the GDPR DPIA on data-subject rights must be a separate artefact even when CRA risk assessment has been performed. The recipient is the **market surveillance authority (MSA)** on Art. 13(3) documented-and-updated risk assessment + Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping + Art. 13(4) sentence 1 technical-documentation inclusion + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records + Annex VII technical documentation (cross to 9.4 for the records-of-processing layer). The Art. 13(13) 10-year retention applies to the technical documentation including the risk-assessment record. For a controller-manufacturer (vertically-integrated entity processing personal data AND shipping CRA-regulated products), the CRA cybersecurity risk assessment on product cybersecurity risk and the GDPR DPIA on data-subject rights are **distinct artefacts** with no OJ-level consolidation (per CRDA DomainAnalysis §9.2 line 175).
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
