# D-10.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-020 + SG-CRA-068 | Relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate; manufacturer enables continuous security-relevant internal-activity monitoring such that security-relevant events are observable by the manufacturer and (where appropriate) reportable to the user (Annex I Part I (2)(l) + Annex I Part II (6)). | Product-level on-device internal-activity monitoring with **user opt-out** + vulnerability-reporting mechanism; manufacturer-side observability. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-level on-device internal-activity monitoring with user opt-out + vulnerability-reporting mechanism | Annex I Part I (2)(l) `provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user` + Annex I Part II (6) `facilitate the sharing of information about potential vulnerabilities of the product with digital elements` | product (product with digital elements placed on the market) | MSA + users — Annex I Part I (2)(l) on-device monitoring + Annex I Part II (6) vulnerability-reporting contact address | Annex I Part I (2)(l) + Annex I Part II (6) + Art. 13(8) manufacturer policies/processes/procedures (cross to D-09.1) + Annex VII §2(b) CVD policy (cross to D-02.3) + Annex VII §6 test reports (cross to D-10.3) |

## Sub-SO (CRA)

#### D-10.1.3 — Sub-SO for CRA

```yaml
id: SG-D-10.1.CRA
subdomain: D-10.1
applies_to: [CRA]
inherits_from: SG-CRA-020 + SG-CRA-068
source_SR: SR-CRA-100 + SR-CRA-101
activation: if CRA in applicable_regs
phase_1A_role: 3_of_5
```

**Objective.** A product with digital elements **provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provides an opt-out mechanism for the user** (Annex I Part I (2)(l) CRA); the manufacturer **facilitates the sharing of information about potential vulnerabilities** through a single contact address (Annex I Part II (6) CRA).

**CSF anchors (from `SR-CRA-100` + `SR-CRA-101` v0.3 security_rationale):**
DE.CM-09, DE.CM-01 (primary), ID.RA-04, GV.OV-01.

---


## Security Requirements (CRA)

#### 10.1.3 — Product-level on-device internal-activity monitoring with user opt-out + vulnerability-reporting mechanism

```yaml
- req_id: 10.1.3
  volere_section: 15
  volere_subtype: audit

  title: "Product with digital elements records and monitors relevant internal activity (access to or modification of data, services or functions) with a user opt-out mechanism, and enables vulnerability sharing through a single contact address"

  derives_from:
    hso_sub_so: SO-10.1.CRA
    per_reg_so: SG-CRA-020 + SG-CRA-068
    source_sr: SR-CRA-100 + SR-CRA-101
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.1.md
    objective_ref_section: "### 10.1.3"

  description: |
    The product shall provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user (per CRA Annex I Part I (2)(l) `provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user`); the manufacturer shall facilitate the sharing of information about potential vulnerabilities of the product with digital elements through a single contact address (per Annex I Part II (6) `facilitate the sharing of information about potential vulnerabilities of the product with digital elements`).

  fit_criterion: |
    Product-level on-device internal-activity monitoring is operational per Annex I Part I (2)(l) + Annex I Part II (6) (SR-CRA-100 + SR-CRA-101) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the CRA Annex I Part I (2)(l) on-device internal-activity monitoring mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the product-level on-device monitoring per DomainAnalysis cross-validation) + ID.IM-04 (Adequate resource capacity — anchors the manufacturer-side observability dimension); the on-device monitoring records and monitors access to or modification of data, services, or functions; the user opt-out mechanism is operational with a clear opt-out interface (UI surface) + opt-out state preservation across product restarts; the vulnerability-reporting contact address is operational per Annex I Part II (6) — single contact address (email or web form) for the sharing of information about potential vulnerabilities of the product with digital elements, integrated with the manufacturer's CVD policy per Annex I Part II §5 (cross to 2.3 Vulnerability Management + 9.1 CRA sub-SO); the recipient is the **MSA (market surveillance authority) + users** on the Annex I Part I (2)(l) on-device monitoring with user opt-out + Annex I Part II (6) vulnerability-reporting contact address; verified by MSA audit pack (on-device monitoring evidence, user opt-out mechanism evidence, vulnerability-reporting contact address operational evidence) + automated on-device monitoring coverage test (access to data + access to services + access to functions + modification of data + modification of services + modification of functions are all monitored) + automated user opt-out mechanism test (opt-out interface accessible + opt-out state preserved across product restarts) + automated vulnerability-reporting contact address test (single contact address operational and responsive). **IMPORTANT — CRDA-flagged GENUINE TENSION (primary flag, GDPR↔CRA)**: CRA Annex I Part I (2)(l) user opt-out vs. mandatory-monitoring regimes (GDPR Art. 32(2), NIS 2 Art. 21(2)(b), DORA Art. 8(1)) — the OJ does not resolve this conflict. The tension propagates to 3 of 10 pairs (GDPR↔CRA primary, NIS2↔CRA propagated, CRA↔DORA propagated). Phase 1 entities with this conflict must (a) maintain the mandatory monitoring under GDPR / NIS 2 / DORA on the entity layer regardless of the CRA opt-out at the product layer, and (b) escalate to Layer 2 OJ-level resolution for the cross-layer conflict. The two regimes can stack on the layered monitoring architecture (entity-layer mandatory + product-layer with opt-out), but the user's opt-out from CRA monitoring does not legally exempt the controller / NSIE / DORA entity from the respective mandatory-monitoring regime. **IMPORTANT — CRA opt-out mechanism is the origin of the 1 CRDA-flagged GENUINE TENSION**: CRA is the only regulator that explicitly permits user opt-out from monitoring (Annex I Part I (2)(l)); the opt-out mechanism is structurally significant and propagates against any mandatory-monitoring regime.

  priority: MUST
  verification_method: TEST
  dependencies: [10.1.1 (when controller-manufacturer — **CRDA-flagged GENUINE TENSION (primary)**: CRA user opt-out vs. GDPR mandatory monitoring; the OJ does not resolve; Layer 2 OJ-level resolution required; the two regimes stack on the layered monitoring architecture — entity-layer mandatory + product-layer with opt-out), 10.1.2 (when NSIE deploys CRA-regulated products — **CRDA-flagged GENUINE TENSION (propagated)**: CRA user opt-out vs. NIS 2 mandatory monitoring; same structural conflict as GDPR↔CRA), 10.1.4 (when DORA entity deploys CRA-regulated products — **CRDA-flagged GENUINE TENSION (propagated)**: CRA user opt-out vs. DORA mandatory monitoring; same structural conflict as GDPR↔CRA), 10.1.5 (when CRA-regulated product is also high-risk AI — CRA Annex I conformity + AI Act post-market monitoring stack for AI-enabled products; the AI Act adds the feedback-loop dimension; the CRA opt-out tension does NOT extend to the AI Act pair — the AI Act Art. 72 monitoring is provider-side, not subject to user opt-out)]

  nist_csf: [DE.CM-09, DE.CM-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part I (2)(l) + Part II (6)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (l) provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user." — CRA Annex I Part I (2)(l) (per SR-CRA-100)
> "The manufacturer shall … (6) facilitate the sharing of information about potential vulnerabilities of the product with digital elements …" — CRA Annex I Part II (6)

**CRA article (verbatim, Annex I Part I (2)(l)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.1: GDPR↔CRA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION** on CRA user opt-out vs. GDPR mandatory monitoring); NIS2↔CRA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION propagated**); CRA↔DORA = COMPLEMENTARY (SAME — **CRDA-flagged GENUINE TENSION propagated**); CRA↔AI_Act = COMPLEMENTARY (SAME — CRA Annex I conformity + AI Act post-market monitoring stack for AI-enabled products; AI Act adds feedback-loop dimension))
```

### from regs/CRA.md body

*(DE.CM-01 — Networks and network services are monitored to find potentially adverse events — anchors the CRA Annex I Part I (2)(l) on-device internal-activity monitoring mapped to NIST CSF 2.0 DE.CM-01; DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored — anchors the product-level on-device monitoring per DomainAnalysis cross-validation; ID.IM-04 — Adequate resource capacity — anchors the manufacturer-side observability dimension. The three subcategories together enable the manufacturer to demonstrate ex post, against the MSA, that the Annex I Part I (2)(l) on-device monitoring was operational with the user opt-out mechanism in place, and that the Annex I Part II (6) vulnerability-reporting contact address was functional. **IMPORTANT — CRA opt-out vs. mandatory-monitoring conflict**: per CRDA-deep §D-10.1 lines 29, 94, 106, 217, 340, the CRA Annex I Part I (2)(l) user opt-out conflicts with GDPR Art. 32(2) mandatory monitoring, NIS 2 Art. 21(2)(b) mandatory detection capability, and DORA Art. 8(1) mandatory continuous monitoring. The OJ does not resolve this conflict. Phase 1 entities with this conflict must (a) maintain the mandatory monitoring under GDPR / NIS 2 / DORA on the entity layer regardless of the CRA opt-out at the product layer, and (b) escalate to Layer 2 OJ-level resolution for the cross-layer conflict.)*

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Y (**CRDA-flagged GENUINE TENSION** — controller-manufacturer; CRA opt-out vs. GDPR mandatory monitoring; conflict requires Layer 2 OJ-level resolution); CRA↔NIS2 = Conditional (Y when NSIE deploys CRA-regulated products; **CRDA-flagged GENUINE TENSION propagated**); CRA↔DORA = Conditional (Y when DORA entity deploys CRA-regulated products; **CRDA-flagged GENUINE TENSION propagated**); CRA↔AI_Act = Conditional (Y when CRA-regulated product is also high-risk AI; CRA Annex I conformity + AI Act Art. 72 post-market monitoring stack — no OJ-level consolidation; the CRA opt-out tension does NOT extend to the AI Act pair); HL engages when the CRA sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA continuous-monitoring obligation at 10.1 is the **product-level on-device internal-activity monitoring** with **user opt-out** + **vulnerability-reporting mechanism** per Annex I Part I (2)(l) + Annex I Part II (6). Annex I Part I (2)(l) `provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user` (per SR-CRA-100) — the `opt-out mechanism for the user` clause is VAG-3 (Berry §5.1 — OJ does not anchor the opt-out mechanism's form factor or scope); chosen reading: opt-out interface (UI surface) + opt-out state preservation across product restarts. The monitoring scope covers access to or modification of data, services, or functions. Annex I Part II (6) `facilitate the sharing of information about potential vulnerabilities of the product with digital elements` (per SR-CRA-101) — the vulnerability-reporting contact address is integrated with the manufacturer's CVD policy per Annex I Part II §5 (cross to 2.3 + 9.1). The recipient is the **MSA (market surveillance authority) + users** on the Annex I Part I (2)(l) on-device monitoring with user opt-out + Annex I Part II (6) vulnerability-reporting contact address. **CRDA-flagged GENUINE TENSION (primary flag, GDPR↔CRA)**: CRA user opt-out vs. mandatory-monitoring regimes (GDPR Art. 32(2), NIS 2 Art. 21(2)(b), DORA Art. 8(1)) — the OJ does not resolve this conflict. The tension propagates to 3 of 10 pairs (GDPR↔CRA primary, NIS2↔CRA propagated, CRA↔DORA propagated). Phase 1 entities with this conflict must (a) maintain the mandatory monitoring under GDPR / NIS 2 / DORA on the entity layer regardless of the CRA opt-out at the product layer, and (b) escalate to Layer 2 OJ-level resolution. The two regimes can stack on the layered monitoring architecture (entity-layer mandatory + product-layer with opt-out), but the user's opt-out from CRA monitoring does not legally exempt the controller / NSIE / DORA entity from the respective mandatory-monitoring regime.
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
