# D-09.2 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SG-NIS2-022 + SG-NIS2-016 + SR-NIS2-028 (Art. 21(1)) | Policies on risk analysis + EU-level coordinated supply-chain risk assessments via Art. 22(1) Cooperation Group (cross to D-09.4); all-hazards methodology with appropriate-and-proportionate chapeau and state-of-the-art floor + cost factor per Recital 56 + entity-discretionary interpretation. | Entity-level operational continuous risk analysis + EU-level coordinated assessments; no pre-launch DPIA. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | entity operational cybersecurity risk (network-and-information-systems dimension) — continuous risk-analysis policy | entity-establishment / on-going operational | not codified for content — entity-discretionary under Recital 56 proportionality + Art. 21(1) chapeau `appropriate and proportionate … taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity` + state-of-the-art floor (Art. 21(1) sentence 2) + cost factor (Recital 56); all-hazards methodology per SR-NIS2-040 | continuous (no codified cadence); entity-discretionary under Recital 56 | management body + competent authority — Art. 21(2)(a) risk-analysis policy + Art. 22(1) Cooperation Group coordinated assessments + Art. 20(1) management-body approval; cross to D-09.4 for EU-level coordinated assessments | Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art (Art. 21(1) sentence 2) + Recital 56 cost factor + Art. 22(1) Cooperation Group coordinated supply-chain assessments + Art. 20(1) management-body approve/oversee/liable + SR-NIS2-028 Art. 21(1) state-of-the-art + cost factor + SR-NIS2-040 all-hazards methodology |

## Sub-SO (NIS 2)

#### D-09.2.2 — Sub-SO for NIS 2

```yaml
id: SG-D-09.2.NIS2
subdomain: D-09.2
applies_to: [NIS2]
inherits_from: SG-NIS2-022 + SG-NIS2-016 + SR-NIS2-028 (Art. 21(1))
source_SR: SR-NIS2-035 + SR-NIS2-039 + SR-NIS2-040
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** Essential and important entities establish **policies on risk analysis and information system security** (Art. 21(2)(a) NIS 2) on a continuous basis, taking into account the proportionality factors (degree of exposure, likelihood of incidents, severity, state of the art, costs of implementation per Recital 56); the Cooperation Group may carry out coordinated supply-chain risk assessments under Art. 22(1) NIS 2 that NSIEs take into account per Art. 21(3) sentence 2.

**CSF anchors (from `SR-NIS2-035` + `SR-NIS2-039` + `SR-NIS2-040` v0.3 security_rationale):**
ID.RA-05 (primary), GV.PO-01, GV.RM-06, ID.RA-06, PR.IR-01.
*(ID.RA-05 — Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response — anchors the NIS 2 Art. 21(2)(a) continuous operational risk-analysis policy mapped to NIST CSF 2.0 ID.RA-05. SR-NIS2-040 establishes the **all-hazards methodology** with the proportionality factors (degree of exposure; likelihood of incidents; severity; state of the art; cost of implementation per Recital 56) calibrating the depth. The Cooperation Group coordinated supply-chain assessments per Art. 22(1) are the EU-level coordinated-assessment substrate for NSIEs to incorporate via Art. 21(3) sentence 2. The two subcategories together enable the NSIE to demonstrate ex post, against the Member State transposition + competent authority, that the Art. 21(2)(a) risk-analysis policy is operational continuous with all-hazards methodology, calibrated by the proportionality factors, and incorporates the Art. 22(1) Cooperation Group coordinated assessments.)*


---


## Security Requirements (NIS 2)

#### 9.2.2 — Entity-level continuous operational risk-analysis policy with all-hazards methodology + Cooperation Group coordinated-assessments ingestion

```yaml
- req_id: 9.2.2
  volere_section: 15
  volere_subtype: integrity

  title: "Essential and important entities establish and maintain documented policies on risk analysis and information system security on a continuous basis with all-hazards methodology and Cooperation Group coordinated-assessments ingestion"

  derives_from:
    hso_sub_so: SO-9.2.NIS2
    per_reg_so: SG-NIS2-022 + SG-NIS2-016
    source_sr: SR-NIS2-035 + SR-NIS2-039 + SR-NIS2-040
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.2"

  description: |
    The product shall ensure that the essential or important entity establishes and maintains, on a continuous basis, documented policies on risk analysis and information system security (per NIS 2 Art. 21(2)(a)) with an all-hazards methodology calibrated by the Art. 21(1) `appropriate and proportionate` chapeau and the Recital 56 proportionality factors, ingesting the EU-level Cooperation Group coordinated supply-chain risk assessments per Art. 22(1) via Art. 21(3) sentence 2.

  fit_criterion: |
    Documented policies on risk analysis and information system security are established and maintained on a continuous basis under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems) + GV.OV-01 management-body oversight dimension (the policies are management-body-approved per Art. 20(1) sentence 1 first-clause `approve` + continuously-overseen per second-clause `oversees`); the policies apply an **all-hazards methodology** per SR-NIS2-040 covering cyber + non-cyber hazards (natural disasters + power failures + human errors + malicious acts + supply-chain disruptions + technical failures) with the depth calibrated by Art. 21(1) chapeau `appropriate and proportionate … taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity` + state-of-the-art floor per Art. 21(1) sentence 2 + Recital 56 cost factor; the entity incorporates the EU-level Cooperation Group coordinated supply-chain risk assessments per Art. 22(1) into its risk-analysis policy per Art. 21(3) sentence 2 (cross to 9.4); the management body formally approves the Art. 21(2)(a) policy through a documented approval minute; the policy is reviewed and updated on a material-change-of-risk trigger (e.g., new threat landscape, organisational change, new critical-asset class, Art. 22(1) coordinated-assessment publication) with cadence entity-discretionary under Recital 56; the policy identifies the risk-analysis scope (information systems supporting essential services + business processes + supporting assets), the risk methodology (asset-threat-vulnerability-impact combination scoring, or equivalent), the risk-treatment options (accept / mitigate / transfer / avoid), the residual-risk acceptance chain, and the responsible functions; for DORA financial entities under DORA's direct scope, the DORA Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 continuous + sentence 2 at-least-yearly discharge both DORA's dedicated continuous + at-least-yearly ICT risk-identification obligation and NIS 2's Art. 21(2)(a) continuous operational risk-analysis policy — DORA-dominant stack with EQUAL classification; the management body's Art. 20(2) sentence 1 training obligation (cross-ref 8.3.1) is the literacy prerequisite for the Art. 20(1) approve/oversee/liable architecture.

  priority: MUST
  verification_method: TEST
  dependencies: [8.3.1 (Art. 20(2) management-body training as literacy prerequisite for Art. 20(1) approve/oversee/liable), 9.2.4 (when DORA-NSIE — DORA continuous + yearly discharges both; EQUAL, DORA-dominant), 9.2.3 (when entity procures CRA-conformant — NIS 2 entity-level operational + CRA product-level pre-market; COMPLEMENTARY; meet at supplier-customer interface — CRA risk-assessment record is an input to the NIS 2 entity's supplier-risk register, cross to 6.1), 9.2.5 (when NSIE deploys high-risk AI — NIS 2 entity-level operational + AI Act AI-system-level continuous iterative; COMPLEMENTARY), 9.2.1 (when controller-NSIE — NIS 2 continuous + GDPR DPIA pre-launch on-change; DIFFERENT-PERSPECTIVE, conditional-Y scope overlap when DPIA conducted for NSIE's processing)]

  nist_csf: [ID.RA-05, GV.PO-01]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(a) + Art. 21(1) + Art. 22(1)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security …" — Art. 21(2)(a) NIS 2 (per SR-NIS2-035)
> "[Member States shall ensure that essential and important entities take appropriate and proportionate … measures to … ] taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity …" — Art. 21(1) NIS 2 (per SR-NIS2-039)

**NIS2 article (verbatim, Art. 21(2)(a)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE / COMPLEMENTARY / EQUAL (CRDA-deep, D-09.2: GDPR↔NIS2 = DIFFERENT-PERSPECTIVE (SAME — pre-launch DPIA on data-subject rights vs continuous operational risk-analysis on entity operational risk; Conditional-Y scope overlap); NIS2↔CRA = COMPLEMENTARY (SAME — entity-level operational + product-level pre-market; meet at supplier-customer interface); NIS2↔DORA = EQUAL (SAME — both regulations impose continuous operational risk-identification obligations; DORA-dominant for financial entities under DORA's direct scope); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 entity-level operational + AI Act AI-system-level continuous iterative; AI Act layer adds the AI-specific 4-step process))
```

### from regs/NIS2.md body

**Considerations.** For DORA financial entities under DORA's direct scope, the DORA Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 + sentence 2 discharges both DORA's dedicated continuous + at-least-yearly ICT risk-identification obligation and NIS 2's Art. 21(2)(a) continuous operational risk-analysis policy — DORA-dominant stack (EQUAL).

### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y when DPIA is conducted for NSIE's processing); NIS2↔CRA = Y (entity procures CRA-conformant products — meet at supplier-customer interface); NIS2↔DORA = Y (DORA financial entity is NSIE — EQUAL on continuous operational risk identification; DORA-dominant stack for financial entities); NIS2↔AI_Act = Y (NSIE deploys high-risk AI; AI Act layer adds the AI-specific 4-step process to the NIS 2 risk-analysis policy); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 impact-and-risk-assessment obligation at 9.2 is the **continuous operational risk-analysis policy** under Art. 21(2)(a) `policies on risk analysis and information system security` with the **all-hazards methodology** per SR-NIS2-040 and **state-of-the-art floor + cost factor proportionality calibration** per Art. 21(1) + Recital 56. Entity-discretionary content (no OJ-codified content list — vs. GDPR's 4-item Art. 35(7) or CRA's Annex VII §3) — chosen reading: the OJ-codified behaviour is the **continuous methodology** + **proportionality calibration** + **ingestion of Cooperation Group coordinated assessments** + **management-body approval**; the entity chooses the depth and the supporting methodology under Recital 56. The Art. 21(2)(a) policy is one of the Art. 21(2) sub-points established under the Art. 21(1) chapeau `appropriate and proportionate all-hazards approach`. The Art. 22(1) EU-level coordinated supply-chain risk assessments are the **Collaboration-Group-level coordinated-assessment substrate** for NSIEs to incorporate via Art. 21(3) sentence 2; the entity must document the incorporation step in the policy (cross to 9.4 for the records-of-processing layer). The **NIS 2 ↔ DORA EQUAL classification** on continuous operational risk identification discharges both obligations on the DORA-dominant stack for financial entities under DORA's direct scope; for non-financial NSIEs, NIS 2 is the authority. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on Art. 21(2)(a) policy + Art. 21(3) sentence 2 ingestion of Art. 22(1) coordinated assessments + Art. 20(1) management-body approval records. The **state-of-the-art floor** (Art. 21(1) sentence 2) and **cost factor** (Recital 56) constrain the entity's discretion: the methodology cannot be so lightweight that it fails to keep pace with state-of-the-art threat intelligence, and the cost factor adjusts the depth without lowering the state-of-the-art floor below the threshold of responsible practice. Member State transposition divergence may apply on the documentation expected to evidence the continuous methodology and the management-body approval.
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=2 -->
