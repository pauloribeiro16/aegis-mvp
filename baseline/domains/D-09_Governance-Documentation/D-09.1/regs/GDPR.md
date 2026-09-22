# D-09.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-026 + SO-GDPR-027 + SO-GDPR-037 | Appropriate data-protection policies reviewed and updated where necessary, with the controller responsibility-accountability chain (Art. 24(1)/(2) + Art. 5(2)) and DPO designation + independence (Art. 37/38/39), securing the controller-side policy architecture. | Process-oriented data-protection policies; DPO as governance anchor; accountability under Art. 5(2). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | controller-side data-protection policies, reviewed and updated where necessary in light of the nature, scope, context, and purposes of processing, the risks of varying likelihood and severity, and the cost of implementation | Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` + Art. 5(2) accountability + DPO (Art. 37-39) | DPO (designated individual with Art. 39(1) tasks reporting to the management body but not a member per Art. 38(6)) | supervisory authority (DPA) — Art. 5(2) accountability on Art. 24(1) policies + Art. 30(4) (cross to D-09.4) + Art. 35(7) (cross to D-09.2) | Art. 24(1) + Art. 24(2) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) chapeau + Art. 37(1) + Art. 38(1) + Art. 38(6) conflict of interests + Art. 39(1) DPO tasks |

## Sub-SO (GDPR)

#### D-09.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-09.1.GDPR
subdomain: D-09.1
applies_to: [GDPR]
inherits_from: SO-GDPR-026 + SO-GDPR-027 + SO-GDPR-037
source_SR: SR-GDPR-043 + SR-GDPR-044 + SR-GDPR-062 + SR-GDPR-063 + SR-GDPR-064
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_5
```

**Objective.** The controller implements **appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner** (Art. 24(1) GDPR), with the Art. 5(2) accountability burden and the DPO as the governance anchor (Art. 37-39).

**CSF anchors (from `SR-GDPR-043` + `SR-GDPR-044` v0.3 security_rationale):**
GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.OV-03.
**PF 1.1 anchors (from `SR-GDPR-043`, `SR-GDPR-044` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
GV.PO-P1, GV.PO-P6, GV.MT-P3, GV.PO-P5.
*(GV.PO-01 — Organizational cybersecurity policy established, communicated, enforced — anchors the GDPR data-protection policy artefact via the Art. 24(1) `policies … designed to implement data-protection principles … in an effective manner` mapped to NIST CSF 2.0 GV.PO-01; GV.RM-04 — Strategic direction for risk response — anchors the GDPR data-protection-policy anchor per DomainAnalysis §D-09.1 line 178 cross-validation; the GDPR data-protection policy is the controller-side policy artefact that operationalises the Art. 5(2) accountability burden. The two subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability burden shifted by Art. 24(1) chapeau, that the controller-side data-protection policies were adopted, reviewed, and updated in light of the four proportionality factors (nature, scope, context, purposes; risks of varying likelihood and severity). GV.RR-02 anchors the DPO role designation + independence — the DPO is the designated individual reporting to the management body but not a member per Art. 38(6). The DPO's Art. 39(1) tasks (inform and advise; monitor compliance with awareness-raising and training) are the operational evidence layer on the GDPR sub-SO.)*

---


## Security Requirements (GDPR)

#### 9.1.1 — Controller-side data-protection policies with DPO governance anchor and Art. 5(2) accountability

```yaml
- req_id: 9.1.1
  volere_section: 15
  volere_subtype: integrity

  title: "Controller implements appropriate data-protection policies reviewed and updated where necessary, with DPO designation, independence, and Art. 5(2) accountability"

  derives_from:
    hso_sub_so: SO-9.1.GDPR
    per_reg_so: SO-GDPR-026 + SO-GDPR-027 + SO-GDPR-037
    source_sr: SR-GDPR-043 + SR-GDPR-044 + SR-GDPR-063
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.1"

  description: |
    The product shall establish, document, review, and update appropriate data-protection policies designed to implement data-protection principles in an effective manner (per GDPR Art. 24(1) + Art. 24(2)), with the DPO designated per Art. 37(1) triggers and operating with the independence, resources, and expert-knowledge maintenance required by Art. 38 (per Art. 38(1) timely involvement + Art. 38(2) resources + Art. 38(3) direct reporting + Art. 38(6) conflict-of-interests prohibition), and with Art. 5(2) accountability burden demonstrating continuous compliance with the Art. 5(1) principles.

  fit_criterion: |
    Appropriate data-protection policies are documented and enforced under Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` (SR-GDPR-043) with GV.PO-01 policy-instrument discipline (every controller has a communicated, current, enforced cybersecurity-and-data-protection policy anchored on the Art. 24(2) proportionality test) + GV.PO-02 operational-procedure layer (each policy backed by documented processes — incident response, breach notification, data-subject rights, retention, processor onboarding — so the policy is real rather than paper) + GV.RM-04 strategic-direction and review-coupling (the controller communicates how it identifies and responds to risks, including the cadence and triggers for policy and procedure refresh, operationalising the Art. 24(1) `where necessary` review obligation on a material-change-of-risk trigger supplemented by annual periodic review per EDPB Guidelines 07/2019 on accountability); the policies are reviewed and updated `where necessary` against the material-change-of-risk trigger; the controller can demonstrate continuous compliance under Art. 5(2) accountability (SR-GDPR-044) with GV.PO-02 procedural-evidence backbone (RoPA entries, DPIA artefacts, audit logs, training records, breach-response records preserved on a continuous basis per EDPB Guidelines on accountability 07/2019) + GV.OV-03 evaluated-and-reviewed-correction dimension (controller's performance against cybersecurity and data-protection objectives measured and adjusted, with adjustments materialising as refreshed policies, processes, and procedures); a DPO is designated where any of the Art. 37(1) triggers applies (public authority + core-activity regular/systematic monitoring of data subjects on large scale + core-activity large-scale special-category or criminal-conviction processing), with Art. 37(7) publication of the designation (SR-GDPR-062), and operates with Art. 38 independence and resourcing (SR-GDPR-063): timely involvement in all Art. 38(1) issues relating to personal-data protection + Art. 38(2) resources necessary to carry out Art. 39 tasks + access to personal data and processing operations + expert-knowledge maintenance + Art. 38(3) direct reporting to highest management level with no instructions regarding exercise of Art. 39 tasks + Art. 38(4) protection against dismissal or penalty for performing tasks + Art. 38(6) conflict-of-interests prohibition (DPO may not hold roles with direct data-processing decision authority — head of marketing, head of IT operations, CISO where that role includes decisions about processing purposes or means — per EDPB Guidelines 3/2018 §6); the DPO performs the Art. 39(1) tasks with adequate independence, resources, and expert knowledge (advisory, monitoring, assurance); for an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance architecture extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair (NIS 2 management-body approval minute as governance hook on top of the GDPR policy artefact — policies are stacked not collapsed, per CRDA-deep §9.1 GDPR↔NIS2 verified relationship); for a DORA financial entity that is a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR Art. 24(1) data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair (DORA-dominant for financial entities, per CRDA-deep §9.1 GDPR↔DORA verified relationship); for a provider/deployer of high-risk AI that is also a controller, the AI Act QMS becomes a sub-policy of the GDPR data-protection policies on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation, per CRDA-deep §9.1 GDPR↔AI_Act verified relationship); verified by Art. 24(1) data-protection policy documentation review + Art. 24(1) `where necessary` review-cadence records + Art. 5(2) accountability evidence pack (RoPA + DPIA + audit logs + training records + breach-response records) + Art. 37(7) DPO designation publication + Art. 38(3) direct-reporting documentation + Art. 38(6) conflict-of-interests assessment + DPA supervisory review on request.

  priority: MUST
  verification_method: TEST
  dependencies: [9.1.2 (when controller = NSIE — NIS 2 management-body approval minute as governance hook on top of GDPR data-protection policies; policies stacked, not collapsed), 9.1.4 (when DORA-controller — DORA Art. 6(1) ICT risk-management framework as carrier + GDPR Art. 24(1) data-protection policies as module; DORA-dominant stack), 9.1.5 (when provider/deployer = controller — AI Act QMS as sub-policy of GDPR data-protection policies; AI Act Recital 78 explicit GDPR preservation)]

  nist_csf: [GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.RR-03, GV.OV-03]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 24(1) + Art. 5(2) + Art. 37-39):**
> "Taking into account the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller shall implement appropriate technical and organisational measures, such as … policies … which are designed to implement data-protection principles … in an effective manner." — Art. 24(1) GDPR
> "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 ('accountability')." — Art. 5(2) GDPR

**GDPR article (verbatim, Art. 24(1) + Art. 5(2)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-09.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — controller-side data-protection policies + NIS 2 management-body approve/oversee/liable governance act stack at controller-NSIE); GDPR↔CRA = COMPLEMENTARY (SAME — Conditional-Y scope overlap when controller is also manufacturer/OSS steward; controller policies + manufacturer policies are different artefacts coexisting without overlap); GDPR↔DORA = COMPLEMENTARY (SAME — DORA framework as carrier + GDPR data-protection policies as module for DORA financial entities that are controllers); GDPR↔AI_Act = COMPLEMENTARY (SAME — AI Act Recital 78 explicit GDPR preservation; AI Act QMS as sub-policy of GDPR controller policies for providers/deployers that are controllers processing personal data via high-risk AI))
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Y (controller-NSIE; NIS 2 management-body approve/oversee/liable governance extends to GDPR data-protection policies); GDPR↔CRA = Conditional (Y when controller is also manufacturer or OSS steward — different artefacts, different actors); GDPR↔DORA = Y (DORA financial entity = controller; DORA framework as carrier + GDPR data-protection policies as module; DORA-dominant for financial entities); GDPR↔AI_Act = Y (provider/deployer = controller; AI Act QMS as sub-policy of GDPR data-protection policies; AI Act Recital 78 explicit GDPR preservation); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR information-security-policy obligation at 9.1 is the **controller-side data-protection policies** with **DPO as governance anchor** under Art. 24(1) + Art. 24(2) + Art. 5(2) accountability + DPO designation per Art. 37-39. Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` + Art. 24(2) `appropriate data-protection policies` (the OJ's `such as` formulation admits a broader operational-measure cluster but `data-protection policies` are the named 9.1 anchor); Art. 5(2) accountability + Art. 30(4) RoPA (cross to 9.4) + Art. 35(7) DPIA content (cross to 9.2). The `where necessary` review cadence (Art. 24(1)) carries Berry-flagged VAG-S3 (Berry §5.1); reading adopted: material-change-of-risk trigger supplemented by annual periodic review (EDPB Guidelines 07/2019 on accountability). The DPO designation under Art. 37(1) fires on any of the three triggers (public authority + core-activity regular/systematic monitoring on large scale + core-activity large-scale special-category or criminal-conviction processing); the `core activities` (VAG-S3), `regular and systematic` + `large scale` (VAG-S3 + POLY-S3), and Berry-flagged `nature, scope and/or purposes` operator — chosen readings per EDPB Guidelines 3/2018 §3.1. The DPO operates with Art. 38(1)-(6) independence (timely involvement + resources + direct reporting + no instructions + protection against dismissal/penalty + conflict-of-interests prohibition); per EDPB Guidelines 3/2018 §6, the DPO cannot also hold roles with direct data-processing decision authority (head of marketing, head of IT operations, CISO where that role includes decisions about processing purposes or means). The recipient is the **DPA (supervisory authority)** on Art. 5(2) accountability + Art. 24(1) appropriate-measures demonstration + Art. 30(4) RoPA + Art. 35(7) DPIA content + DPO designation records. For an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair (per CRDA-deep §9.1 GDPR↔NIS2 verified relationship). For a DORA financial entity that is a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair (DORA-dominant for financial entities). For a provider/deployer of high-risk AI that is a controller, the AI Act QMS becomes a sub-policy of the GDPR data-protection policies on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation). (Copied from the HSO Considerations block of `### 9.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=2 -->
