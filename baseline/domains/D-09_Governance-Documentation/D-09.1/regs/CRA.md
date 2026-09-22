# D-09.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-049 + SO-CRA-050 + SO-CRA-051 + SO-CRA-052 | OSS-steward cybersecurity policy fostering the development of a secure product with digital elements and effective vulnerability handling (Art. 24(1)); OSS-steward cooperation with market surveillance authorities (Art. 24(2)); manufacturer policies/processes/procedures for CRA cybersecurity obligations including CVD policy + secure-update distribution + support-period factors + cessation-of-operations procedure (Art. 13(8) + Annex I Part II §5 + Art. 13(23)); presumption of conformity via harmonised standards / common specifications / CSA certification (Art. 27(1)/(2)/(5)/(8)/(9)). | Product-level policy framework + standards-presumption machinery + OSS-steward cybersecurity policy. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | OSS-steward cybersecurity policy (Art. 24(1) 4-element: documenting, addressing, remediating vulnerabilities; sharing information within the open-source community) + manufacturer policies/processes/procedures including CVD policy, secure-update distribution, support-period determination methodology, cessation-of-operations communication + presumption of conformity via harmonised standards / common specifications / CSA certification | Art. 24(1) `Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product` + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1) `Products with digital elements and the processes put in place by the manufacturer shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I where those products and processes conform to harmonised standards` + Art. 27(8) CSA certification | OSS steward (Art. 24(1) OSS-steward policy owner) + manufacturer (Art. 13(8) manufacturer policies/processes/procedures owner) — distinct from data-protection governance body | market surveillance authority (MSA) — Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records + Annex VII technical documentation (cross to D-09.4) | Art. 24(1) + Art. 24(2) + Art. 13(8) + Art. 13(8) sentence 6 CVD policy + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation of operations + Art. 27(1) + Art. 27(2) + Art. 27(5) + Art. 27(8) + Art. 27(9) + Recital 25 (Annex II scope) |

## Sub-SO (CRA)

#### D-09.1.3 — Sub-SO for CRA

```yaml
id: SO-D-09.1.CRA
subdomain: D-09.1
applies_to: [CRA]
inherits_from: SO-CRA-049 + SO-CRA-050 + SO-CRA-051 + SO-CRA-052
source_SR: SR-CRA-072 + SR-CRA-073 + SR-CRA-075 + SR-CRA-077 + SR-CRA-078
activation: if CRA in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** An open-source software steward **puts in place and documents in a verifiable manner a cybersecurity policy** (Art. 24(1) CRA) covering vulnerability documentation, remediation, and information-sharing within the open-source community; a manufacturer **establishes policies, processes and procedures necessary to implement its CRA cybersecurity obligations** (Art. 13(8) CRA) including CVD policy, secure-update distribution, support-period determination, and cessation-of-operations communication.

**CSF anchors (from `SR-CRA-072` + `SR-CRA-075` + `SR-CRA-077` v0.3 security_rationale):**
GV.PO-01 (primary), GV.SC-01, GV.PO-02, GV.OC-03.

---


## Security Requirements (CRA)

#### 9.1.3 — Manufacturer / OSS-steward policies with presumption-of-conformity machinery via harmonised standards / common specifications / CSA certification

```yaml
- req_id: 9.1.3
  volere_section: 15
  volere_subtype: integrity

  title: "Manufacturer and OSS-steward cybersecurity policies with verifiable documentation, CVD, support-period, and presumption of conformity via harmonised standards, common specifications, or CSA certification"

  derives_from:
    hso_sub_so: SO-9.1.CRA
    per_reg_so: SO-CRA-049 + SO-CRA-050 + SO-CRA-051 + SO-CRA-052
    source_sr: SR-CRA-072 + SR-CRA-073 + SR-CRA-075 + SR-CRA-077
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.3"

  description: |
    The product shall establish manufacturer policies/processes/procedures necessary to implement CRA cybersecurity obligations — including the CVD policy under Annex I Part II §5 + Art. 13(8) sentence 6, the secure-update distribution mechanism under Annex I Part II §7, the support-period determination methodology under Art. 13(8) sentence 2, and the cessation-of-operations communication procedure under Art. 13(23) (per CRA Art. 13(8)) — and where applicable, OSS-steward cybersecurity policy fostering secure development and effective vulnerability handling (per Art. 24(1) 4-element (i)-(iv)) with verifiable documentation + cooperation with market surveillance authorities (per Art. 24(2)), with the presumption-of-conformity machinery via harmonised standards / common specifications / CSA certification (per Art. 27(1)/(2)/(5)/(8)/(9)).

  fit_criterion: |
    Manufacturer policies/processes/procedures are documented under Art. 13(8) sentence 6 `appropriate policies including a CVD policy` + Annex I Part II §5 CVD policy + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation-of-operations communication procedure (SR-CRA-075) with GV.PO-01 policy-instrument layer (CVD policy + support-period-determination methodology established, communicated to security researchers, users, and other stakeholders via publication and promotion, and enforced through the documented policy framework) + GV.PO-02 implementation-process layer (policies operationalised through documented processes — CVD coordination workflow + support-period calculation procedure + policy-update mechanism — with implementation evidence recorded in technical documentation under Annex VII §2(b)); for OSS-steward entities, an Art. 24(1) cybersecurity policy is put in place and documented in a verifiable manner fostering the secure development of products with digital elements and effective vulnerability handling (SR-CRA-072) with GV.PO-01 policy-instrument layer (cybersecurity policy established, communicated across the steward's maintainer base + contributors + downstream dependents, and enforced through the documented 4-element (i)-(iv) `documenting, addressing, remediating vulnerabilities; sharing of information concerning discovered vulnerabilities within the open-source community`) + GV.SC-01 supply-chain-risk-management dimension (policy positioned as the entry point of the steward's SCRM programme, with upstream-coverage of OSS contributors and downstream-coverage of dependents integrated into the programme); the OSS-steward verifiable-documentation character of the policy supplies the auditability anchor under Art. 24(2) MSA cooperation (SR-CRA-073) — upon reasoned request the steward provides documentation of the cybersecurity policy and the relevant security aspects of the products they steward, with GV.SC-04 third-party-assessment dimension (MSA treated as a regulated assessor; cooperation duty operationalises the third-party-assessment-on-request function with documentation of policy + security aspects supplying the assessment record) + GV.OC-03 legal-and-regulatory-requirements-managed dimension (steward's regulatory requirements managed, with the request-triggered nature of the duty preserved — no standing reporting or audit); the presumption-of-conformity machinery is tracked at the conformity-assessment evidence layer via Art. 27(1) harmonised standards (SR-CRA-077) + Art. 27(2)/(5) common specifications via implementing acts + Art. 27(8) CSA certification at the assurance level specified by Art. 8(1) `substantial` or Art. 32(2)/(3) `high`, with GV.OC-03 standing duty to track the Official Journal list of harmonised standards and know which Annex I requirements each cited standard covers + GV.PO-02 common-specification fallback as documented process (the SDLC executes when no harmonised standard exists, and records the alternative solution adopted); the presumption is rebuttable — the OJ literal `presumed` signals a rebuttable presumption rather than a binding acquittal per general EU product-safety case law — and the coverage qualifier `to the extent that the standards cover those requirements` means that an Annex I requirement not addressed by the cited standard is not swept into the presumption and must be demonstrated by the manufacturer (partial-standard coverage shifts the burden back onto the manufacturer for un-addressed elements); for a controller-manufacturer (vertically-integrated entity that processes personal data AND ships CRA-regulated products), the CRA manufacturer-side policies and the GDPR controller-side data-protection policies coexist on different artefacts (manufacturer-side policies for product cybersecurity + controller-side data-protection policies for personal-data processing) on the GDPR↔CRA SAME — COMPLEMENTARY pair (different artefacts, different actors — no OJ-level consolidation rule, per CRDA-deep §9.1 GDPR↔CRA verified relationship); for a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair (Conditional Y when DORA entity procures CRA-conformant products, per CRDA-deep §9.1 CRA↔DORA verified relationship); for AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (CRA on the product cybersecurity requirements + AI Act on the AI-system quality-management system; no OJ-level consolidation rule at 9.1 — unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*, per CRDA-deep §9.1 CRA↔AI_Act verified relationship); verified by manufacturer policies/processes/procedures documentation review + Annex VII technical documentation (cross to 9.4) + Art. 24(2) OSS-steward cooperation-on-request records + Annex II §8(a)-(f) instruction-set review (when product-side applies, cross to 8.1 partial) + Annex I Part I + Part II conformity-assessment records + Official Journal harmonised-standards list tracking + common-specification fallback procedure documentation + CSA certification records at the assurance level specified + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [9.1.1 (when controller-manufacturer — manufacturer-side CRA policies coexist with controller-side GDPR data-protection policies on different artefacts; policies stacked, not collapsed), 9.1.2 (when entity procures CRA-conformant — CRA presumption substitutes for parts of NIS 2 supplier-assessment evidence but not NIS 2 entity-level policy architecture), 9.1.4 (when DORA entity procures CRA-conformant — CRA presumption discharges parts of DORA supplier-assessment evidence but not DORA framework obligation), 9.1.5 (when product is both CRA-regulated and AI-Act high-risk — CRA Annex I conformity + AI Act QMS stack; no OJ-level consolidation rule at 9.1)]

  nist_csf: [GV.PO-01, GV.SC-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 24(1) + Art. 13(8) + Art. 27(1)/(2)/(5)/(8)/(9)):**
> "Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product." — Art. 24(1) CRA (per SR-CRA-072)
> "Products with digital elements and the processes put in place by the manufacturer shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I where those products and processes conform to harmonised standards …" — Art. 27(1) CRA
> "The Commission may adopt implementing acts establishing common specifications …" — Art. 27(2) CRA
> "Common specifications … shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I …" — Art. 27(5) CRA
> "A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881 … shall be presumed to be in conformity with the essential cybersecurity requirements …" — Art. 27(8) CRA

**CRA article (verbatim, Art. 27(1)/(2)/(5)/(8)/(9)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.1: GDPR↔CRA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when controller is also manufacturer/OSS steward; controller policies + manufacturer policies are different artefacts); NIS2↔CRA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when entity procures CRA-conformant products; NIS 2 entity-side policy artefact + CRA presumption-of-conformity machinery); CRA↔DORA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when DORA entity procures CRA-conformant products; CRA presumption discharges parts of DORA supplier-assessment evidence but not DORA framework obligation); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act QMS stack for products that are both CRA-regulated and AI-Act high-risk; **no OJ-level consolidation rule at D-09.1** — unlike D-09.2 CRA Art. 13(4) sentence 2 which permits AI Act Art. 9 to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*))
```

### from regs/CRA.md body

*(GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the OSS-steward cybersecurity policy (Art. 24(1)) + manufacturer policies/processes/procedures (Art. 13(8)) mapped to NIST CSF 2.0 GV.PO-01. The presumption-of-conformity machinery (Art. 27(1)/(2)/(5)/(8)/(9)) is the upstream gate for the policy object's evidence trail — a CRA-conformant product is presumed to meet the Annex I essential cybersecurity requirements when the manufacturer's processes conform to harmonised standards (Art. 27(1)) or common specifications (Art. 27(2)/(5)) or European cybersecurity certification schemes (Art. 27(8)/(9)). The OSS-steward policy is the workforce-level policy anchor for OSS projects under the steward's umbrella; the manufacturer policies/processes/procedures are the operational policy artefacts for the manufacturer's Annex I compliance chain. The two subcategories together enable the OSS steward / manufacturer to demonstrate ex post, against the market surveillance authority, that the Art. 24(1) OSS-steward policy or Art. 13(8) manufacturer policies were adopted, reviewed, and updated during the support period, with the Art. 27(1)/(2)/(5)/(8)/(9) presumption-of-conformity machinery as the upstream gate. **IMPORTANT — CRA presumption does not extend cross-regulation**: per DomainAnalysis §D-09.1 line 173, CRA presumption of conformity discharges the CRA conformity-assessment obligation only and does not substitute for the GDPR Art. 24(1) appropriate-measures obligation, NIS 2 Art. 21(2)(a)+(f) policy obligation, or DORA Art. 6(1) ICT risk-management framework obligation. Phase 1 entities must discharge each regime's policy obligation separately even when the underlying product is CRA-conformant.)*

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y when controller is also manufacturer or OSS steward — different artefacts, different actors); CRA↔NIS2 = Conditional (Y when entity procures CRA-conformant products); CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products); CRA↔AI_Act = Y (same product is both CRA-regulated and AI-Act high-risk; CRA Annex I conformity + AI Act QMS stack — no OJ-level consolidation rule at 9.1); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA information-security-policy obligation at 9.1 is the **manufacturer-side / OSS-steward-side policies** with **presumption-of-conformity machinery** via harmonised standards / common specifications / CSA certification. The manufacturer policies cluster (Art. 13(8) + Annex I Part II §5 CVD policy + Annex I Part II §7 secure-update distribution + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation-of-operations) is the operational-instrument layer; the OSS-steward policy under Art. 24(1) has 4-element partial content codification (i)-(iv) per the OJ — voluntary-reporting enablement (i), nature-aware proportionality (ii), documenting/addressing/remediating vulnerabilities (iii), sharing of information within the open-source community (iv) — and the `documented in a verifiable manner` (VAG-S3) is read at the R1 literal — `verifiable manner` = the steward can demonstrate the policy on request, with Art. 24(2) MSA cooperation providing external verification on demand (per SR-CRA-072 ambiguity_notes). The Art. 24(2) cooperation duty is request-triggered — no standing reporting or audit obligation (per SR-CRA-073 regulatory_rationale). The Art. 27 presumption-of-conformity machinery is rebuttable — a market-surveillance authority remains free to verify Annex I compliance on substance — and partial-standard coverage shifts the burden back onto the manufacturer for un-addressed elements (per SR-CRA-077 ambiguity_notes). The recipient is the **MSA (market surveillance authority)** on Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records + Annex VII technical documentation (cross to 9.4). For a controller-manufacturer (vertically-integrated entity that processes personal data AND ships CRA-regulated products), the CRA manufacturer-side policies and the GDPR controller-side data-protection policies coexist on different artefacts on the GDPR↔CRA SAME — COMPLEMENTARY pair (different artefacts, different actors — no OJ-level consolidation rule). For an NSIE that procures CRA-conformant products, the CRA presumption-of-conformity machinery substitutes for parts of the NIS 2 supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the NIS 2 entity-level policy architecture on the NIS2↔CRA SAME — COMPLEMENTARY pair. For a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair. For AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (no OJ-level consolidation rule at 9.1 — unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*). (Copied from the HSO Considerations block of `### 9.1.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
