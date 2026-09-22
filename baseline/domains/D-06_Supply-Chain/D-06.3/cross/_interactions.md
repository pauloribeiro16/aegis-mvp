# D-06.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-06.3 Contractual Security Obligations](../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md)
#### D-06.3 Contractual Security Obligations
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.3 per AEGIS taxonomy §4.1. DORA is the sole authority for ICT-services contractual-security architecture (Art. 30 minimum elements + audit rights).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-06.3 Contractual Security Obligations
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md`](../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md)
> (6 pairs verified against OJ text — **4 of 5 participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope per AEGIS taxonomy §4.1**).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-06.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-022; SG-GDPR-033; SG-GDPR-035 | Processor contracts contain the eight Art. 28(3)(a)–(h) mandatory clauses; third-country transfers use Art. 46 safeguards where no adequacy decision exists; third-country court or administrative requests are recognised only through an international-agreement basis | Controller/processor personal-data contract; transfer-safeguard contractual layer; DPA-facing accountability |
| NIS2 | SG-NIS2-015; SG-NIS2-016 | Direct suppliers and service providers are assessed on supplier-specific vulnerabilities, product/service quality, cybersecurity practices, secure-development procedures, and EU-level coordinated supply-chain risk-assessment outputs | Entity-side direct-supplier contractual and assessment layer; Member-State-transposition-sensitive `direct` scope-limiter |
| CRA | SG-CRA-039; SG-CRA-040 | Importers perform pre-market checks and escalation; distributors act with due care, verify CE/documentation/manufacturer/importer compliance, and escalate non-conformity or vulnerabilities | Product market-access layer; importer/distributor obligations to manufacturer and market surveillance authority (MSA), imposed by regulation rather than negotiated as a DPA |
| DORA | SG-DORA-012; SG-DORA-011 (standards link) | ICT third-party contractual arrangements clearly allocate rights and obligations in writing, include the Art. 30(2) minimum elements, and comply with Art. 28(5) information-security standards; CIF contracts add Art. 30(3) clauses | Financial-entity ICT third-party contractual layer; competent-authority-facing evidence; CIF escalator |

## Validated relationships (from CRDA-deep §D-06.3)

#### Validated relationships (from CRDA-deep §D-06.3)
Of 6 pairs, **5 verified as SAME and 1 verified as CORRECTED — COMPLEMENTARY**. There are **no verified CONTRADICTORY pairs** after OJ-text analysis. The one correction is material: GDPR↔DORA was initially classified as CONTRADICTORY in CRDA, but CRDA-deep corrected it to **COMPLEMENTARY** because the operative rule is a **clause-list union**, not a mutually exclusive conflict.
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR Art. 28(3) contracts govern the controller↔processor relationship with an eight-element closed list. NIS 2 Art. 21(2)(d)/(3) governs direct supplier and service-provider relationships, including vulnerabilities, quality, cybersecurity practices, and secure-development procedures. When the supplier is both a processor and a direct supplier, both apply on the same relationship; GDPR adds data-protection-specific clauses and NIS 2 adds cybersecurity supplier-assessment evidence.
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): GDPR contracts are controller↔processor legal instruments. CRA importer/distributor duties are market-surveillance-facing regulatory obligations, not DPA-style negotiated contracts. They overlap conditionally when a GDPR controller deploys a CRA-compliant product and the manufacturer/importer/distributor is in the supply chain; the duties remain different mechanisms on different actors.
- **GDPR ↔ DORA** — CORRECTED — COMPLEMENTARY (clause-list union): GDPR Art. 28(3) has eight mandatory clauses; DORA Art. 30(2) has nine minimum ICT-contract elements, with CIF-only clauses at Art. 30(3). The two lists overlap but are not mutually exclusive. When a financial entity is also a controller and the ICT third-party provider is also a processor, the operative rule is the **union of all applicable clauses**.
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 supplier assessment is ex ante and entity-side; CRA component-vulnerability reporting/remediation and importer/distributor obligations are product-lifecycle and market-access mechanisms. Conditional overlap exists when a NIS 2 entity deploys a CRA-classified product.
- **NIS2 ↔ DORA** — EQUAL (SAME) (DORA exceeds NIS 2): DORA's Art. 30 contractual elements operationalise NIS 2's open-textured `security-related contractual aspects` in the financial-services subset. A financial entity implementing DORA Art. 30 exceeds the NIS 2 contractual-security floor for the same supplier relationship.
- **CRA ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME): CRA obligations are market-surveillance-facing importer/distributor duties; DORA Art. 30 is a financial-entity ICT-service contract duty. They overlap conditionally when a CRA-classified product is procured by a financial entity, but the regulatory direction and evidence recipient remain distinct.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Y (controller is also an essential/important entity; processor is also a direct supplier) | Conditional (Y when a CRA-compliant product is deployed by a GDPR controller; N when importer/distributor duties sit only at market-access layer) | Y (financial entity is controller and ICT provider is processor; clause-list union applies) |
| **NIS2** | Y (same supplier relationship with processor/direct-supplier dual role) | — | Conditional (N in baseline because NIS 2 is ex-ante entity-side and CRA component/product duties are lifecycle/market-side; Y when a NIS 2 entity deploys a CRA product) | Y (financial entity is also NIS 2 essential/important entity; DORA contract list satisfies NIS 2 floor) |
| **CRA** | Conditional (same chain, different actors and mechanisms) | Conditional (same as NIS2↔CRA) | — | Conditional (N in baseline because CRA is regulatory market access and DORA is contract; Y when CRA product is procured as financial-entity ICT service) |
| **DORA** | Y (same ICT provider can be processor and DORA ICT third party) | Y (same financial-entity supplier relationship) | Conditional (same chain, different regulatory direction) | — |
Legend: **Y** = scope overlap on a single event at a single party. **Conditional** = overlap only under specific factual circumstances. **N in baseline** = the pair is typically scope-disjoint as to actors/triggers, even if CRDA-deep preserves the SAME taxonomy label because the obligations layer within the same supply-chain sub-domain.

## Cross-recipient map

#### Cross-recipient map
D-06.3 generates recipient fragmentation at the **contractual evidence** layer. **GDPR** evidence is addressed to the supervisory authority (DPA) through Art. 5(2) accountability, Art. 28(3) DPA contracts, and Chapter V transfer safeguards. **NIS 2** evidence is addressed to the competent authority or CSIRT through the supplier-risk register, direct-supplier contract terms, Art. 21(3) three-prong supplier assessment, and Art. 22 coordinated-assessment ingestion. **CRA** evidence is addressed to market surveillance authorities through importer/distributor pre-market verification, non-conformity escalation, and conformity-documentation retention. **DORA** evidence is addressed to the competent authority and, where applicable, resolution authorities through the Art. 28(5) standards record, Art. 30(2) contract elements, and CIF-only Art. 30(3) clauses.
---

## HSO considerations (from D-06.3.0 — High-level SecurityObjective)

**Considerations.**
- Four participating regulations (GDPR, NIS 2, CRA, DORA) each use a distinct legal instrument: GDPR uses processor contracts and transfer safeguards; NIS 2 uses direct-supplier contractual security and a supplier-assessment evidence chain; CRA uses importer/distributor market-access duties and component-vulnerability escalation; DORA uses ICT third-party written contractual arrangements, Art. 28(5) standards compliance, and CIF-specific audit/exit clauses where applicable.
- CRDA-deep verified relationships (6 pairs: 5 SAME + 1 CORRECTED — GDPR↔DORA from CRDA CONTRADICTORY to COMPLEMENTARY because both clause sets add rather than conflict; the operative rule is clause-list union when the same contract is in scope). No verified CONTRADICTORY pairs.
- Where the same real-world supplier relationship is covered by multiple regulations, the organisation implements a consolidated contractual-security matrix that preserves all applicable mandatory clauses and evidence recipients; the high-level SO does not collapse the regimes into one generic supplier contract — it preserves the per-reg target object, trigger, actor, evidence template, and recipient.
- The 1 conditional emergent tension (4-track contract architecture — GDPR 8 DPA elements + DORA 9 ICT-contract elements + NIS 2 supplier-assessment + CRA importer/distributor market-access duties) is regulated by preserving the multi-track matrix rather than choosing a single stricter regime.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
| Axis (reg) | Target object | Trigger | Contract/evidence instrument | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | processor and transfer recipient handling personal data | per-processor contract; per-transfer safeguard; per-third-country legal request | Art. 28(3) DPA 8-element list; Art. 46 safeguards; Art. 48 legal-request filter | DPA; controller; processor | Art. 28(3)(a)–(h); Art. 46; Art. 48 |
| **NIS2** | direct supplier/service-provider relationship | continuous supply-chain security; per-supplier assessment; availability of Art. 22 coordinated assessment | supplier-risk register; security-related contract terms; three-prong assessment evidence | CSIRT or competent authority | Art. 21(2)(d); Art. 21(3); Art. 22 |
| **CRA** | importer/distributor market-access chain and component-vulnerability hand-off | before market placement; reason to believe non-conformity; vulnerability identified | pre-market check record; CE/documentation verification; non-conformity/corrective-measures record | MSA; manufacturer; component supplier | Art. 19; Art. 20; Art. 13(6) |
| **DORA** | ICT third-party contractual arrangement | per-ICT-service contract; CIF support; standards compliance | Art. 30(2) 9-element contract; Art. 28(5) standards record; CIF clauses under Art. 30(3) | competent authority; financial entity; resolution authorities where applicable | Art. 28(1); Art. 28(5); Art. 30(1)–(3) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
| | GDPR | NIS 2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Y (controller is also an essential/important entity; processor is also a direct supplier) | Conditional (Y when a CRA-compliant product is deployed by a GDPR controller; N when importer/distributor duties sit only at market-access layer) | Y (financial entity is controller and ICT provider is processor; clause-list union applies) |
| **NIS 2** | Y (same supplier relationship with processor/direct-supplier dual role) | — | Conditional (N in baseline because NIS 2 is ex-ante entity-side and CRA component/product duties are lifecycle/market-side; Y when a NIS 2 entity deploys a CRA product) | Y (financial entity is also NIS 2 essential/important entity; DORA contract list satisfies NIS 2 floor) |
| **CRA** | Conditional (same chain, different actors and mechanisms) | Conditional (same as NIS2↔CRA) | — | Conditional (N in baseline because CRA is regulatory market access and DORA is contract; Y when CRA product is procured as financial-entity ICT service) |
| **DORA** | Y (same ICT provider can be processor and DORA ICT third party) | Y (same financial-entity supplier relationship) | Conditional (same chain, different regulatory direction) | — |
Legend: **Y** = scope overlap on a single event at a single party. **Conditional** = overlap only under specific factual circumstances. **N** = scope-disjoint in baseline.
(See the validated-relationships table above for the per-cell notes.)

## Scope-overlap principle (operational)

#### Scope-overlap principle (operational)
The high-level SO (`SG-D-06.3.HL`) engages when ≥2 participating regulations apply to the same supplier relationship or to a single integrated supply-chain event. The dominant high-overlap scenario is a financial entity that is also a GDPR controller and a NIS 2 entity contracting with an ICT provider that processes personal data: GDPR Art. 28(3), NIS 2 Art. 21(2)(d)/(3), and DORA Art. 30 all apply, and the contract must satisfy the union of clauses. CRA usually operates on the product-market-access side rather than the contract itself; it joins the same architecture when the ICT service includes a CRA-classified product supplied through importer/distributor channels or when a component vulnerability is identified during the lifecycle.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate: GDPR, NIS 2, CRA, DORA. AI Act is out-of-scope for D-06.3 per AEGIS taxonomy §4.1.
- The verified profile is **5 SAME + 1 CORRECTED** across 6 pairwise cells. The correction is GDPR↔DORA from CONTRADICTORY to **COMPLEMENTARY** because the clause sets add rather than conflict.
- The high-level SO describes the **COMMON OBJECTIVE**: make third-party security duties enforceable through the correct contractual or regulatory evidence instrument, with a consolidated matrix where multiple instruments apply.
- The **single emergent tension** is not a substantive contradiction; it is a **4-track contract architecture** tension: GDPR 8 DPA elements, DORA 9 ICT-contract elements plus CIF clauses, NIS 2 supplier-assessment and contractual aspects, and CRA importer/distributor market-access duties must be sequenced without flattening actors or recipients.
- DORA exceeds NIS 2 only in the financial-services subset. It does not replace NIS 2 for non-financial essential/important entities, nor does it replace GDPR-specific processor clauses when the ICT provider is also a processor.
- CRA remains market-surveillance-facing in baseline. It is not converted into a negotiated supplier contract merely because it maps to D-06.3; its obligations are imposed on economic operators by regulation.
---

## Emergent tensions (from CRDA-deep §D-06.3)

#### Emergent tensions (from CRDA-deep §D-06.3)
**1 conditional emergent tension**: the **4-track contract architecture**. GDPR Art. 28(3) imposes an eight-element processor-contract list; DORA Art. 30(2) imposes a nine-element ICT-contract list and CIF-only Art. 30(3) clauses; NIS 2 imposes direct-supplier security and a three-prong supplier assessment; CRA imposes importer/distributor pre-market and non-conformity obligations through a market-surveillance channel. CRDA-deep confirms that this is not a true contradiction. The Phase 1C/Phase 2 implementation task is to build a consolidated matrix that applies the union where the same contract is in scope, and a two-layer or four-layer evidence pack where actors/triggers are conditional or typically separate.
The GDPR↔DORA pair is the only corrected pair: CRDA-deep corrects the initial CONTRADICTORY label to **COMPLEMENTARY** because both clause sets can be satisfied simultaneously. The correct operational rule is clause-list union, with CIF-only DORA clauses scoped to critical or important functions and with GDPR-specific processor clauses retained whenever the ICT provider processes personal data.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in D-06.3 must maintain a contractual-security matrix keyed by party, role, product/service, and trigger. For a financial-entity-controller contracting with an ICT provider that is also a processor, the matrix includes GDPR Art. 28(3) + DORA Art. 30(2) + applicable Art. 30(3) CIF clauses, with NIS 2 satisfied by reference only where the financial entity is also a NIS 2 entity and the supplier is within the `direct` scope. For a CRA product supply chain, the matrix includes importer/distributor verification and escalation records rather than treating CRA as a DPA-like contract. The one emergent tension is resolved by preserving this multi-track matrix rather than by choosing a single stricter regime.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-06.3 Contractual Security Obligations — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md`. See that file for cross-reg verified relationships (6 pairs: 5 SAME + 1 CORRECTED — GDPR↔DORA corrected from CRDA CONTRADICTORY to COMPLEMENTARY clause-list union because Art. 28(3) 8-element DPA + DORA Art. 30(2) 9-element ICT-contract lists add rather than conflict; no verified CONTRADICTORY pairs after OJ-text verification), scope overlap matrix, Objective/Considerations content, the 1 emergent tension (the 4-track contract architecture — GDPR 8 DPA elements + DORA 9 ICT-contract elements + NIS 2 supplier-assessment evidence + CRA importer/distributor market-access duties must be sequenced without flattening actors or recipients), the GDPR↔DORA clause-list-union resolution (the operative rule when same contract is in scope is union of all applicable clauses, NOT mutual exclusivity), the CRA market-surveillance-facing non-conversion to DPA-style negotiated contract (CRA obligations remain imposed by regulation on economic operators), and DORA-exceeds-NIS 2 in the financial-services subset (DORA Art. 30 operationalises the NIS 2 open-textured `security-related contractual aspects` floor). **Scope-title note (P0):** the index.md row used the placeholder `D-06.3 Third-party Risk (PENDING Batch 11)` label; this file uses the CRDA-deep source-of-truth title `D-06.3 Contractual Security Obligations` per Batch 11 critical-rule #6 + #8 (the Batch 12 HSO file already documented the divergence). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1). CRDA-deep verified 6 pairs as **5 SAME + 1 CORRECTED — COMPLEMENTARY** (2 COMPLEMENTARY + 1 CORRECTED + 1 DIFFERENT-PERSPECTIVE + 1 COMPLEMENTARY + 1 EQUAL — wait, re-checking: GDPR↔NIS2 = COMPLEMENTARY, GDPR↔CRA = DIFFERENT-PERSPECTIVE, GDPR↔DORA = CORRECTED — COMPLEMENTARY (clause-list union), NIS2↔CRA = COMPLEMENTARY, NIS2↔DORA = EQUAL with DORA exceeding NIS 2, CRA↔DORA = DIFFERENT-PERSPECTIVE). The four regulators each use a distinct legal instrument: GDPR uses Art. 28(3) processor contracts and Art. 46/48 transfer safeguards; NIS 2 uses Art. 21(2)(d)/(3) direct-supplier contractual security and a supplier-assessment evidence chain; CRA uses Art. 19/20 importer/distributor market-access duties and Art. 13(6) component-vulnerability escalation; DORA uses Art. 28(5) standards + Art. 30(1)+(2) 9-element contract + Art. 30(3) CIF-only clauses. The high-level SO surfaces the **common contractual-security objective** — making third-party security duties enforceable through the correct contractual or regulatory evidence instrument — while preserving per-reg target object, trigger, actor, evidence template, and recipient. The 1 emergent tension (the 4-track contract architecture) is resolved by a consolidated contractual-security matrix rather than by collapsing regimes into one generic supplier contract.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 6.3
  volere_section: 15
  volere_subtype: immunity
  title: "Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, with a consolidated 4-track contractual-security matrix where multiple regulations apply to the same supplier relationship (GDPR Art. 28(3) 8-element DPA + DORA Art. 30(2) 9-element ICT-contract + NIS 2 supplier-assessment + CRA importer/distributor market-access)"
  derives_from:
    hso_sub_so: SG-D-06.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md
    objective_ref_section: "### D-06.3.0"
  description: |
    The product shall make third-party security obligations enforceable through the correct contractual or regulatory evidence instrument — GDPR Art. 28(3) DPA + transfer safeguards + Art. 48 international-agreement filter for controllers/processors; NIS 2 Art. 21(2)(d) direct-supplier contracts + Art. 21(3) three-prong assessment + Art. 22 coordinated-assessment inputs for essential/important entities; CRA Art. 19/20 importer/distributor market-access duties + Art. 13(6) component-vulnerability reporting for products with digital elements; DORA Art. 28(5) standards + Art. 30(1)+(2) 9-element ICT-contract + Art. 30(3) CIF-only clauses for financial entities — preserving per-reg target object, trigger, actor, evidence template, and recipient and assembling the union of mandatory clauses when the same supplier relationship is covered by ≥2 of these regimes.
  fit_criterion: |
    A 4-track contractual-security matrix is maintained keyed by supplier / regulator / instrument / actor / recipient, with explicit instrument separation (processor-DPA / supplier-contract / economic-operator-mandate / ICT-contract) and documented track hand-offs at instrument boundaries; each of the four tracks records its target object (processor-as-legal-entity / direct-supplier-as-relationship / importer-or-distributor-as-economic-operator / ICT-third-party-as-financial-entity-counterparty), its trigger gate (per-processor engagement / continuous supplier-security / pre-market placement + non-conformity / per-ICT-service contract + CIF support), its closed-list clause inventory (GDPR Art. 28(3)(a)–(h) 8-element DPA / NIS 2 Art. 21(2)(d) security-related contractual aspects + Art. 21(3) three-prong assessment evidence / CRA Art. 19(2) importer-verification + Art. 19(3) measures records + Art. 20(2) distributor-due-care + Art. 20(3) non-conformity measures / DORA Art. 30(2)(a)–(i) 9-element ICT-contract + Art. 30(3)(a)–(f) CIF-only clauses), and its recipient (DPA / CSIRT-or-competent-authority / MSA / national-financial-supervisory-authority-or-competent-authority); when ≥2 tracks overlap on the same supplier relationship, the matrix applies the **clause-list union** rule (GDPR↔DORA correction resolves to UNION, NOT mutual exclusivity) with DORA-exceeds-NIS 2 discharge in the financial-services subset and CRA duties retained as regulatory (non-DPA-converted); verified by contractual-security matrix documentation review + per-track closed-list clause-inventory inspection + instrument-boundary hand-off records audit + DPA/CSIRT/MSA/National-Competent-Authority inspection-ready evidence pack on request + GDPR Art. 5(2) accountability Art. 28(3) DPA inspection + NIS 2 Art. 21(3) three-prong assessment records review (when NIS 2 in scope) + CRA Annex VII §2 technical-documentation reference (when CRA product procured) + DORA Art. 30 CIF-clause attestation review (when CIF support).
  priority: MUST
  verification_method: TEST
  dependencies: [6.1 (vendor-risk-assessment findings feed the contractual-security matrix parties/clauses; CRA component-due-diligence shapes NIS 2 supplier-contract annexes; DORA four-factor scales Art. 30 contract depth)]
  nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, PR.PS-06]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping supplier relationships (see HSO scope-overlap principle); AI Act out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Four participating regulations (GDPR, NIS 2, CRA, DORA) each use a distinct legal instrument: GDPR Art. 28(3) DPA 8-element list + Art. 46 transfer safeguards + Art. 48 international-agreement filter; NIS 2 Art. 21(2)(d) supplier contracts + Art. 21(3) three-prong assessment + Art. 22 coordinated-assessment inputs; CRA Art. 19/20 importer/distributor market-access duties + Art. 13(6) component-vulnerability escalation; DORA Art. 30(1)+(2) ICT-contract 9-element list + Art. 28(5) standards + Art. 30(3) CIF-only clauses. CRDA-deep verified relationships (6 pairs: 5 SAME + 1 CORRECTED — GDPR↔DORA from CRDA CONTRADICTORY to COMPLEMENTARY clause-list union; no verified CONTRADICTORY pairs after OJ-text verification). The 1 conditional emergent tension is the **4-track contract architecture** — the four instrument tracks (processor-DPA / supplier-contract / economic-operator-mandate / ICT-contract) must be sequenced in a consolidated matrix without flattening actors or recipients. The GDPR↔DORA CORRECTED pair is resolved as clause-list union (NOT mutually exclusive) — when the same contract is in scope, the operative rule is the union of all applicable clauses, with CIF-only DORA clauses scoped to critical or important functions and GDPR-specific processor clauses retained whenever the ICT provider processes personal data. DORA Art. 30 exceeds NIS 2 `security-related contractual aspects` in the financial-services subset only — it does not replace NIS 2 for non-financial essential/important entities nor GDPR-specific processor clauses when the ICT provider is also a processor. CRA obligations are imposed by regulation on economic operators (importer, distributor, manufacturer-equivalent); they are NOT converted into DPA-style negotiated contracts merely because they map to D-06.3. The high-level SO does not collapse these regimes — it builds a consolidated matrix that preserves all applicable mandatory clauses and evidence recipients, layered not flattened. (Copied from the HSO Considerations block of `### D-06.3.0`; preserved here for self-containment per Volere shell `considerations` field definition; the substantive content lives in HSO.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-06.3
title: D-06.3 Contractual Security Obligations — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.3 Contractual Security Obligations
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-06_Supply-Chain/D-06.3.md
status: DRAFT
---
> **Deep analysis:** [D-06.3 Contractual Security Obligations](../../DeepAnalysis/D-06_Supply-Chain/D-06.3.md)
#### D-06.3 Contractual Security Obligations
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-022, SG-GDPR-033, SG-GDPR-035 | Eight-element DPA per Art. 28(3)(a)–(h) + sufficient-guarantees processor selection + Art. 46 appropriate safeguards + Art. 47 BCR + Art. 48 third-country request filter | Personal data processing contracts; controller/processor |
| NIS2 | SG-NIS2-015, SG-NIS2-016 | Supplier three-prong assessment (vulnerabilities + quality + secure-development) + EU-level coordinated supply-chain risk-assessment integration (Art. 21(3) + Art. 22) | Direct supplier contractual obligations; per-supplier |
| CRA | SG-CRA-039, SG-CRA-040 | Importer pre-market verification + 10-year conformity retention + distributor due-care + non-conformity escalation (Art. 19 + Art. 20) | Economic operator (importer/distributor) contractual obligations; market access |
| DORA | SG-DORA-012 | Rights and obligations clearly allocated + 9 minimum elements (a)–(i) + unrestricted audit rights (Art. 30(1)–(3)) | ICT third-party contractual arrangements; financial entity |
| AI_Act | — | Out-of-scope (sole authority: DORA) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-06.3 per AEGIS taxonomy §4.1. DORA is the sole authority for ICT-services contractual-security architecture (Art. 30 minimum elements + audit rights).
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,NIS2,CRA,DORA -->
- **4-track contract architecture with overlapping but non-identical clause lists.** GDPR Art. 28(3) = 8 elements; DORA Art. 30(2) = 9 elements; NIS2 Art. 21(3) = 3-prong supplier assessment; CRA Art. 19/20 = importer/distributor pre-market verification. The pairwise readings surface specific overlaps (GDPR↔DORA clause-list overlap, GDPR↔NIS2 processor-vs-supplier distinction), but the *non-pairwise observation* is that a single supplier relationship (e.g., a CRA-compliant product supplied to a financial entity that processes personal data) must satisfy all four tracks simultaneously. Phase 2 must produce a consolidated supplier-contract template that operationalises the union of all four clause sets.
<!-- /emergent -->
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **GV.SC-03** (Contracts with suppliers and third-party partners) and **GV.SC-04** (Suppliers and third-party partners are routinely assessed). GDPR maps both via SR-GDPR-034. NIS2 maps GV.SC-02 + GV.SC-04 via SR-NIS2-020. CRA maps GV.SC-02 + GV.SC-04 via SR-CRA-054 + SR-CRA-057. DORA maps GV.SC-03 + GV.SC-04 via SR-DORA-021. The CSF 2.0 surface is consistent. The clause-list overlap (GDPR 8 elements vs DORA 9 elements) is a regulatory-orchestration concern, not a CSF construct.
##### Downstream implication
Phase 2 obligation derivation must produce a consolidated contract-clause matrix. The intersection of GDPR Art. 28(3) and DORA Art. 30(2) is the operational hinge: financial entities that process personal data via ICT third-party providers must satisfy both clause sets. Phase 3 case generation must validate that supplier contracts in case companies include all required elements per the consolidated matrix.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-06.3
title: D-06.3 Contractual Security Obligations — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.3 Contractual Security Obligations
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-06_Supply-Chain/D-06.3.md
status: DRAFT
---
> **Domain analysis:** [D-06.3 Contractual Security Obligations](../../DomainAnalysis/D-06_Supply-Chain/D-06.3.md)
#### D-06.3 Contractual Security Obligations
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.3 per AEGIS taxonomy §4.1. DORA is the sole authority for ICT-services contractual-security architecture (Art. 30 minimum elements + audit rights).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)