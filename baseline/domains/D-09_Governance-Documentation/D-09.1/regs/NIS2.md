# D-09.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SG-NIS2-021 + SG-NIS2-022 + SG-NIS2-023 | Management body of essential/important entities approves the cybersecurity risk-management measures, oversees their implementation, and can be held liable (Art. 20(1)); policies on risk analysis + IS security (Art. 21(2)(a)) and policies/procedures to assess effectiveness of cybersecurity risk-management measures (Art. 21(2)(f)). | Governance-first with policy artefact; management-body approve/oversee/liable architecture on top of three policy artefacts. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | entity-level policies on risk analysis + IS security + policies and procedures to assess effectiveness of cybersecurity risk-management measures | Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` | management body (Art. 20(1) sentence 1 `management bodies … approve the cybersecurity risk-management measures … oversee their implementation and can be held liable for infringements`) | management body + competent authority — Art. 21(2)(a)+(f) policy records + Art. 21(1) documented policies on risk analysis + IS security + Art. 20(1) management-body approval records | Art. 20(1) sentence 1 + Art. 21(2)(a) + Art. 21(2)(f) + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Recital 56 proportionality |

## Sub-SO (NIS 2)

#### D-09.1.2 — Sub-SO for NIS 2

```yaml
id: SG-D-09.1.NIS2
subdomain: D-09.1
applies_to: [NIS2]
inherits_from: SG-NIS2-021 + SG-NIS2-022 + SG-NIS2-023
source_SR: SR-NIS2-032 + SR-NIS2-033 + SR-NIS2-034 + SR-NIS2-035 + SR-NIS2-036 + SR-NIS2-037
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The management body of essential and important entities **approves the cybersecurity risk-management measures, oversees their implementation, and can be held liable for infringements** (Art. 20(1) sentence 1 NIS 2); the entity adopts **policies on risk analysis and information system security** (Art. 21(2)(a)) and **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f)).

**CSF anchors (from `SR-NIS2-035` + `SR-NIS2-036` + `SR-NIS2-037` v0.3 security_rationale):**
ID.RA-05, GV.PO-01 (primary), PR.PS-01, ID.IM-01, GV.OV-03.
*(GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the NIS 2 Art. 21(2)(a)+(f) policy artefacts mapped to NIST CSF 2.0 GV.PO-01; GV.OV-01 — Risk management strategy outcomes reviewed — anchors the NIS 2 management-body approve/oversee/liable governance act per DomainAnalysis §D-09.1 line 178 cross-validation; the management body's liability exposure for NIS 2 infringements (Art. 20(1) sentence 1) is the operational evidence layer for the governance hook. The three subcategories together enable the entity to demonstrate ex post, against the Member State transposition, that the Art. 21(2)(a)+(f) policies + Art. 20(1) management-body approval records were established, reviewed, and updated in light of the proportionality factors (degree of exposure; likelihood of incidents; severity of incidents).)*


---


## Security Requirements (NIS 2)

#### 9.1.2 — Entity-level risk-analysis + IS-security + effectiveness-assessment policy artefacts with management-body approve/oversee/liable architecture

```yaml
- req_id: 9.1.2
  volere_section: 15
  volere_subtype: integrity

  title: "Essential and important entities establish policies on risk analysis, information system security, and effectiveness assessment, approved and overseen by the management body"

  derives_from:
    hso_sub_so: SO-9.1.NIS2
    per_reg_so: SG-NIS2-021 + SG-NIS2-022 + SG-NIS2-023
    source_sr: SR-NIS2-032 + SR-NIS2-035 + SR-NIS2-036
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.2"

  description: |
    The product shall establish and maintain documented policies on risk analysis and information system security (per NIS 2 Art. 21(2)(a)) and policies and procedures to assess the effectiveness of cybersecurity risk-management measures (per NIS 2 Art. 21(2)(f)), with the management body approving the Art. 21 measures and overseeing their implementation (per Art. 20(1) sentence 1 first-clause `approve` + second-clause `oversees`) and bearing personal liability for infringements (per Art. 20(1) sentence 1 third-clause `can be held liable`).

  fit_criterion: |
    Documented policies are established and maintained under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) documenting the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems, and under Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` (SR-NIS2-036) with results feeding back into the risk-management cycle, with the depth calibrated by Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor (Art. 21(1) sentence 2) + Recital 56 proportionality (nature/size/risk profile/cost of implementation); the management body formally approves the Art. 21 measures through a documented approval minute (SR-NIS2-032) with GV.RR-02 approval as documented governance act (the approval minute records the management body's reading of the measures, acceptance of residual risk, and resource commitment, creating executive sponsorship) + GV.PO-01 downstream enforceability (the approved measures become the binding organisational cybersecurity policy); the management body continuously oversees the implementation (SR-NIS2-033) with GV.OV-01 active-monitoring dimension (management body reviews implementation status, receives exception reports, interrogates the CISO on residual-risk drift, authorises adjustments to the Art. 21 measures as the threat landscape and entity exposure evolve) + GV.RM-05 upward-channel substrate (the CISO and relevant functions have documented escalation paths to the management body, including exception and incident reporting); the management body bears personal liability for Art. 21 infringements (SR-NIS2-034) under Art. 20(1) sentence 1 third-clause `can be held liable` — the literacy prerequisite is the Art. 20(2) sentence 1 training obligation (cross-ref 8.3.1) which makes the management body structurally positioned to discharge Art. 20(1) oversight responsibilities with informed judgement; the policy artefact is layered under Art. 21(1) chapeau with the three policy records (Art. 21(2)(a) risk-analysis + IS-security policies + Art. 21(2)(f) effectiveness-assessment policies + procedures) and the management-body approval minute as governance hook; the policy content is entity-discretionary under Recital 56 proportionality — the OJ does not enumerate specific content; for an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance architecture extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair (NIS 2 management-body approval minute as governance hook on top of the GDPR policy artefact — policies are stacked not collapsed, per CRDA-deep §9.1 GDPR↔NIS2 verified relationship); for a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities, per CRDA-deep §9.1 NIS2↔DORA verified relationship); for an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair (the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy, per CRDA-deep §9.1 NIS2↔AI_Act verified relationship); for an entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery substitutes for parts of the NIS 2 supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the NIS 2 entity-level policy architecture on the NIS2↔CRA SAME — COMPLEMENTARY pair (Conditional Y when entity procures CRA-conformant products, per CRDA-deep §9.1 NIS2↔CRA verified relationship); verified by Art. 21(2)(a) + Art. 21(2)(f) policy-records review + Art. 20(1) management-body approval minute + Art. 20(1) oversight records (board minutes + dashboard reviews + exception registers) + Art. 21(1) chapeau documented-policies evidence + Member State supervisory review (national NIS 2 supervisory authority) on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.1 (Art. 20(2) sentence 1 management-body training as literacy prerequisite for Art. 20(1) approve/oversee/liable), 9.1.1 (when controller-NSIE — NIS 2 management-body approval minute as governance hook on top of GDPR data-protection policies; policies stacked, not collapsed), 9.1.4 (when DORA-NSIE — DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act; EQUAL classification, DORA-dominant stack for financial entities), 9.1.5 (when NSIE deploys high-risk AI — AI Act QMS as sub-policy of NIS 2 entity-level governance), 9.1.3 (when entity procures CRA-conformant — CRA presumption substitutes for parts of NIS 2 supplier-assessment evidence but not NIS 2 entity-level policy architecture)]

  nist_csf: [GV.RR-02, GV.PO-01]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 20(1) sentence 1 + Art. 21(2)(a) + Art. 21(2)(f)):**
> "Member States shall ensure that the management bodies of essential and important entities approve the cybersecurity risk-management measures taken by those entities in order to comply with Article 21, oversee their implementation and can be held liable for infringements by the entities of that Article." — Art. 20(1) sentence 1 NIS 2 (per SR-NIS2-032/033/034)
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security; … (f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures." — Art. 21(2)(a)+(f) NIS 2

**NIS2 article (verbatim, Art. 21(2)(a) + Art. 21(2)(f) + Art. 24):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security; … (f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures." — Art. 21(2)(a)+(f) NIS 2
> "Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems …" — Art. 24(1) NIS 2 (per SR-NIS2-043)

**NIS2 article (verbatim, Art. 20(1) + Art. 21(2)(a) + Art. 21(2)(f)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — controller policies + NIS 2 management-body approve/oversee/liable governance act stack); NIS2↔CRA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when entity procures CRA-conformant products; NIS 2 policy artefact + CRA presumption-of-conformity machinery); NIS2↔DORA = EQUAL (SAME — both regulations impose policy + governance architecture; DORA-dominant for financial entities under DORA's direct scope); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 entity-level governance + AI Act QMS as sub-policy for NSIEs deploying high-risk AI))
```

### from regs/NIS2.md body

**Considerations.** For DORA financial entities under DORA's direct scope, the DORA Art. 6(1) + Art. 5(2) + Art. 6(4) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's policy + governance obligation — DORA-dominant stack.

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Y (controller-NSIE; NIS 2 management-body approve/oversee/liable governance extends to GDPR data-protection policies); NIS2↔CRA = Conditional (Y when entity procures CRA-conformant products); NIS2↔DORA = Y (DORA financial entity = NSIE; DORA-dominant stack for financial entities — EQUAL on policy + governance dimension); NIS2↔AI_Act = Y (NSIE deploys high-risk AI; AI Act QMS as sub-policy of NIS 2 entity-level governance); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 information-security-policy obligation at 9.1 is the **entity-level policy artefacts** (Art. 21(2)(a) risk-analysis + IS-security policies + Art. 21(2)(f) effectiveness-assessment policies and procedures) with the **management-body approve/oversee/liable architecture** as governance hook (Art. 20(1) sentence 1 three-verb coordination `approve, oversee, and can be held liable` — three distinct obligations per Recital 75, per SR-NIS2-032/033/034 ambiguity readings). The `cybersecurity risk-management measures` (SR-NIS2-032) carry an S3 ambiguity on the approval object — an Art. 21(2)(a)-(j) sub-point list reading, an Art. 21(1) chapeau-and-Art. 21(5) implementing-act reading, or a free-standing entity-cybersecurity-strategy reading — chosen reading: literal-and-broad interpretation that `measures` covers both the Art. 21(2) sub-points and any entity-discretionary measures adopted under Art. 21(1). The `in order to comply with Article 21` qualifier carries an indicative-vs-restrictive ambiguity on whether the approval is for Art. 21 measures specifically or for any measures contributing to compliance — indicative reading dominant since the OJ uses the qualifier to anchor the approval object rather than constrain it. The `oversees` obligation is continuous by construction (no terminal-event qualifier) — the management body reviews implementation status and adjusts as needed on entity-discretionary cadence. The three-verb S3 COORD ambiguity (`approve, oversee, and can be held liable`) — chosen reading: three-distinct-obligations reading per Recital 75. Member State transposition divergence may apply on documentation expected to evidence oversight (board minutes, dashboard reviews, exception registers). The policy content is entity-discretionary under Recital 56 proportionality — OJ does not enumerate specific content. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on Art. 21(2)(a)+(f) policy records + Art. 21(1) documented policies + Art. 20(1) management-body approval + oversight records. For an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair. For a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities). For an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair. For an entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery substitutes for parts of the NIS 2 supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the NIS 2 entity-level policy architecture on the NIS2↔CRA SAME — COMPLEMENTARY pair. (Copied from the HSO Considerations block of `### 9.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=2 -->
