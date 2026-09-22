<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-01.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-01.1 Data at Rest Encryption](../../DomainAnalysis/D-01_Data-Protection/D-01.1.md)
#### D-01.1 Data at Rest Encryption
<!-- participants: GDPR, NIS2, CRA, DORA; AI_Act absent -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA (AI_Act is not present; AI Act §D-01.1 marks CRA Annex I (2)(e) as sole authority per taxonomy §4.1).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md`](../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md)
> (6 pairs verified against OJ text).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-01.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-001 | CIA + resilience for personal data processing | Controller/processor; Art. 5(1)(f) + Art. 32(1)(a)/(b); personal-data scope; risk-anchored `appropriate` |
| NIS 2 | SO-NIS2-001 | Cryptography policies and procedures covering CIA of stored, transmitted, processed data | Essential/important entity; Art. 21(2)(h); NIS scope (broader than personal data); `where appropriate` hedge |
| CRA | SO-CRA-001 / SO-CRA-002 | State-of-the-art encryption of stored data (personal or other) | Manufacturer; Annex I Part I (1) + (2)(e); product-level; state-of-the-art baseline + harmonised-standards floor |
| DORA | SO-DORA-001 | CIA+A maintained across data states (at-rest, in-use, in-transit) | Financial entity; Art. 9(2); ICT-system-level; `high standards` anchor |

## Validated relationships (from CRDA-deep §D-01.1)

#### Validated relationships (from CRDA-deep §D-01.1)
All 6 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial classifications — 5 pairs initially marked COMPLEMENTARY and 1
EQUAL were all verified as SAME after OJ-text analysis). The underlying
obligation is the same (encryption of data at rest to protect
confidentiality); the pairs differ only in scope qualifier (`personal
data` vs `network and information systems` vs `product with digital
elements` vs `ICT of financial entity`) and threshold anchor
(`appropriate` vs `where appropriate` vs `state of the art` vs `high
standards`). These are scope-depth and wording differences on a common
obligation, not fundamentally different regulatory framings. CRA-deep
explicitly notes (GDPR↔CRA pair) that meeting the CRA state-of-the-art
floor discharges the GDPR `appropriate` obligation on the at-rest
dimension for that product — the convergence is not just nominal.
The scope-overlap column in the matrix below indicates whether the same
artefact can trigger both regulations on a single party; this is the
gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (disjoint in baseline; Y on integrated manufacturer-controller)  |
|  **CRA**  |  Conditional  |  —  |
Legend: **Y** = scope overlap on a single artefact (high-level SO can
engage on a single party); **Conditional** = disjoint in baseline case, Y
on integrated-stack or vertical-integration scenario. CRDA-deep
scope-disjoint tests: GDPR↔NIS2 = Y; GDPR↔CRA = Conditional (disjoint in
baseline; Y on integrated manufacturer-controller); GDPR↔DORA = Y;
NIS2↔CRA = Y; NIS2↔DORA = Y for cross-sector, N (disjoint in baseline)
for financial sector (DORA is lex specialis); CRA↔DORA = Conditional
(disjoint in baseline as manufacturer ≠ financial entity; Y when DORA
financial entity deploys CRA product).

## Cross-recipient map

#### Cross-recipient map
N/A — D-01.1 (data at rest encryption) does not involve distinct recipient
classes. The recipients are supervisory authorities for compliance
demonstration (GDPR SA, NIS 2 CSIRT/CA, CRA MSA + ENISA, DORA CA + ESAs)
on inspection, but there is no notification or reporting trigger;
the recipients only inspect compliance evidence. The D-04.3 sub-domain
is the canonical recipient-fragmentation locus for the data-protection
area.
---

## HSO considerations (from D-01.1.0 — High-level SecurityObjective)

**Considerations.**
- The four participating regulations converge on the same substantive obligation
  (risk-anchored encryption of data at rest) but each anchors it to a distinct
  threshold: GDPR's `appropriate` (risk-based, personal-data scope), NIS 2's
  `where appropriate` (broader NIS scope), CRA's `state of the art` (product-
  level, harmonised-standards floor — the strictest), and DORA's `high standards`
  (ICT-system-level).
- CRDA-deep verified all 6 pairs as SAME — a single encryption deployment with
  a joint risk-assessment artefact (joint Article 32 / Art. 21(2)(h) / Annex I
  (2)(e) / Art. 9(2) coverage) discharges all four obligations on the same
  datastore.
- For artefacts touching only one regulatory scope, only the triggered sub-SO
  applies.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-01.1 over a distinct
material scope; the trigger and threshold anchor depend on which scope
the data falls into.
| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous risk-anchored | personal data | supervisory authority (DPA) | Art. 5(1)(f) + Art. 32(1)(a)/(b) |
| **NIS 2** | continuous (Art. 21(1) appropriate-and-proportionate) | network and information systems | CSIRT or CA | Art. 21(2)(h) |
| **CRA** | continuous product-side baseline | product with digital elements | market surveillance authority + ENISA | Annex I Part I (1) + (2)(e) |
| **DORA** | continuous + annual scenario review | ICT-supported data of financial entity | national CA + ESAs | Art. 9(2) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-01.1.HL`) engages on a given datastore **if and only if ≥2
applicable regulations' scopes overlap on the same storage object**
(e.g. personal data on a CRA-regulated product deployed by a NIS 2
essential entity that is also a DORA financial entity — a
vertically-integrated manufacturer-controller on a financial-services
stack). Pure co-applicability of disjoint-scope regulations on different
artefacts does **not** trigger cross-regulation aggregation — see the
Activation logic in the file header. For a 5-FTE SaaS startup with
GDPR + CRA applicability but no NIS 2 / DORA applicability, only the
GDPR and CRA sub-SOs activate; the high-level SO engages on the same
artefact if both apply.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4.1 — CRA Annex I (2)(e) is the
  sole authority).
- 6 pairwise cells, verified by CRDA-deep as **all SAME** after
  OJ-text analysis: GDPR↔NIS2 (CORRECTED from COMPLEMENTARY),
  GDPR↔CRA (CORRECTED from COMPLEMENTARY), GDPR↔DORA (CORRECTED from
  COMPLEMENTARY), NIS2↔CRA (CORRECTED from COMPLEMENTARY), NIS2↔DORA
  (CORRECTED from EQUAL), CRA↔DORA (CORRECTED from COMPLEMENTARY).
- The four regulations impose the **same substantive obligation**
  (encryption of data at rest) with different anchors (threshold
  wording, scope qualifier, technical baseline). CRA is the strictest
  (state-of-the-art + harmonised standards); GDPR is calibrated by risk
  on personal data; NIS 2 adds the `where appropriate` hedge over a
  broader NIS scope; DORA specifies `high standards` over ICT-supported
  data.
- The high-level SO describes the **COMMON OBJECTIVE** (encryption of
  data at rest to protect confidentiality against unauthorised
  access); the **per-regulation perspective** (threshold anchor, scope
  qualifier, recipient, content template) is preserved verbatim in the
  four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 6 pairs as SAME. Phase 1C Doc 07 does not
  need to resolve contradictions on D-01.1 because none exist; the task
  is to **stack the documentation** so that a single at-rest
  deployment discharges all four obligations.
- **Scope caveat (CRITICAL)** — derived from CRDA-deep verified
  classifications: the high-level SO does NOT aggregate across
  manufacturer/controller hands-offs. A SaaS-using-CRA-product
  scenario has disjoint baseline obligations (CRA manufacturer supplies
  product baseline; GDPR controller implements at-rest control on its
  own deployment; the two are separate compliance tracks unless the
  same party is both manufacturer and controller). The CRA baseline met
  at the product level does not by itself discharge the GDPR
  controller's deployment-side responsibility — the controller's risk
  assessment and cipher-strength selection remain its own. Similarly,
  the NIS 2 ↔ DORA pair is disjoint in the financial sector (DORA is
  lex specialis) and the high-level SO does not aggregate there.
---

## Emergent tensions (from CRDA-deep §D-01.1)

#### Emergent tensions (from CRDA-deep §D-01.1)
None — sub-domain is **all-SAME in baseline (6 pairs verified as SAME
after OJ-text analysis; CRDA initial 5 COMPLEMENTARY + 1 EQUAL
classifications corrected to SAME)**. No conditional emergent tensions.
The threshold divergence (GDPR `appropriate`, NIS 2 `where appropriate`,
CRA `state of the art`, DORA `high standards`) is wording-only on a
common substantive obligation; the operational convergence is on
**encryption of data at rest using approved mechanisms with appropriate
key custody**, and the strictest floor (CRA state-of-the-art) discharges
the others on a single artefact. CRDA-deep explicitly notes (in the
GDPR↔CRA pair reasoning) that meeting CRA discharges GDPR on the at-rest
dimension for that product — the convergence is not just nominal.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-01.1 — with
overlapping scopes on the same datastore — operates a **single at-rest
encryption control + a joint risk-assessment artefact** that discharges
all obligations. The high-level SO (`SO-D-01.1.HL`) describes the
common obligation; the per-reg perspective is preserved in the sub-SOs
(threshold anchor, scope qualifier, recipient for compliance
demonstration). **No conflict-resolution is required on D-01.1 because
CRDA-deep verified all 6 pairs as SAME.** Phase 1C Doc 07 documents
the **stacked documentation** strategy: (1) a single at-rest deployment
(symmetric cipher with separate logical access on key custody); (2) a
joint risk assessment citing all four legal anchors; (3) per-recipient
evidence packs for SA / CSIRT or CA / MSA / DORA CA on request. For
proportionality, a 5-FTE SaaS with GDPR + CRA applicability may default
to the CRA state-of-the-art floor as the highest common denominator; a
500-FTE financial entity must additionally document the DORA
classification-driven cipher-strength overlay (SR-DORA-003 per
`GV.RM-04`) and the key-custody architecture.

## Part 1 §3 — context

### 3. Security Requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md`. See that file for cross-reg verified relationships, scope overlap matrix, Objective/Considerations content, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs; AI Act is out-of-scope per AEGIS taxonomy §4.1 — CRA Annex I (2)(e) is the sole authority). CRDA-deep verified 6 pairs as all-SAME (5 corrected from COMPLEMENTARY + 1 corrected from EQUAL after OJ-text analysis).
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 1.1
  volere_section: 15
  volere_subtype: integrity
  title: "Data at rest is protected by appropriate technical measures (multi-reg aggregation)"
  derives_from:
    hso_sub_so: SO-D-01.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md
    objective_ref_section: "### D-01.1.0"
  description: |
    The product shall protect data held at rest against unauthorised access through appropriate technical measures — primarily encryption with separate key custody — calibrated to the risk of processing and commensurate with the state of the art, as the common substantive obligation converging across GDPR Art. 32(1)(a)/(b), NIS 2 Art. 21(2)(h), CRA Annex I Part I (2)(e), and DORA Art. 9(2) where ≥2 of these scopes overlap on the same datastore.
  fit_criterion: |
    AES-256 (or stronger) symmetric encryption is applied to all data-at-rest storage volumes holding the in-scope data class (personal data, NIS data, CRA product data, or DORA ICT-supported data, as triggered); key custody is logically or physically separated from data access via role-based access control on key-material vs operational-environment credentials; cipher strength meets or exceeds the strictest applicable floor (CRA state-of-the-art discharges GDPR, NIS 2, DORA on a single artefact); verified by automated configuration audit (FIPS 140-3 / NIST SP 800-131A reference) + manual key-custody review + joint risk-assessment artefact citing all four legal anchors when scopes overlap.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-01]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs overlap on same datastore (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations converge on the same substantive obligation
    (risk-anchored encryption of data at rest) but each anchors it to a distinct
    threshold: GDPR's `appropriate` (risk-based, personal-data scope), NIS 2's
    `where appropriate` (broader NIS scope), CRA's `state of the art` (product-
    level, harmonised-standards floor — the strictest), and DORA's `high standards`
    (ICT-system-level). CRDA-deep verified all 6 pairs as SAME — a single encryption
    deployment with a joint risk-assessment artefact (joint Article 32 / Art.
    21(2)(h) / Annex I (2)(e) / Art. 9(2) coverage) discharges all four obligations
    on the same datastore. For artefacts touching only one regulatory scope,
    only the triggered sub-requirement applies. (Copied from the HSO
    Considerations block of `### D-01.1.0`; preserved here for self-contained
    traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-01.1
title: D-01.1 Data at Rest Encryption — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.1 Data at Rest Encryption
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-01_Data-Protection/D-01.1.md
status: DRAFT
---
> **Deep analysis:** [D-01.1 Data at Rest Encryption](../../DeepAnalysis/D-01_Data-Protection/D-01.1.md)
#### D-01.1 Data at Rest Encryption
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-001 / SO-GDPR-002 | Personal data confidentiality at rest, with pseudonymisation/encryption rendering breached data unintelligible | Controller/processor; Art. 5(1)(f) + Art. 32(1)(a); risk-anchored, scope = personal data |
| NIS2 | SO-NIS2-001 | Cryptography policies and procedures covering confidentiality, integrity, authenticity of stored, transmitted, and processed data | Essential/important entity; Art. 21(2)(h); "where appropriate" hedge, scope = network and information systems |
| CRA | SO-CRA-001 / SO-CRA-002 | Confidentiality of stored data (personal or other) protected by state-of-the-art encryption or other technical means | Manufacturer; Annex I Part I (1)+(2)(e); product-level, scope = data stored by product with digital elements |
| DORA | SO-DORA-001 | CIA + Authenticity maintained at high standards across at rest, in use, in transit (4×3 matrix) | Financial entity; Art. 9(2); ICT-system-level, scope = ICT-supported data |
| AI_Act | — | Out-of-scope (AI Act does not impose a data-at-rest mandate; CRA Annex I §2(c) is sole authority per taxonomy §4) | n/a |
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
- All four regulations impose an at-rest confidentiality obligation, but the **threshold anchor** diverges: GDPR `appropriate` (risk-based), NIS 2 `where appropriate` (with appropriate-and-proportionate), CRA `state of the art` (harmonised-standards floor), DORA `high standards` (OJ-literal, no measurement criterion pending ESAs RTS). A DORA financial entity that is a NIS 2 essential entity AND processes personal data AND uses CRA-regulated products must reconcile four parallel thresholds; a Layer 2/3 analysis should establish whether the CRA state-of-the-art floor is automatically sufficient for the other three (likely yes for the at-rest dimension).
- **CRA "personal or other" scope extension** beyond GDPR's personal-data scope creates a compliance-population gap: a CRA manufacturer protecting non-personal data (e.g. sensor telemetry) may not be in GDPR scope, but a NIS 2 entity that ingests the same data is in scope. A CRA baseline met at the product level does not by itself discharge the NIS 2 entity's deployment-side responsibility.
<!-- /emergent -->
##### SR cross-validation
CSF mappings converge on PR.DS-01 (Data-at-rest protected) for all four regulations, with CRA additionally mapping to PR.DS-02 (in-transit) per the SR-CRA-001 umbrella and DORA additionally mapping to PR.DS-02/PR.DS-10/ID.AM-08 for the in-transit/in-use/risk-strategy dimensions. The shared PR.DS-01 anchor is the operational pivot; divergence is at the supplementary layer (CRA: harmonised standards; DORA: classification-driven key protection; GDPR: pseudonymisation/Art. 4(5) de-attribution; NIS 2: appropriate-and-proportionate). No contradictory CSF mappings observed.
##### Downstream implication
For Phase 1C Doc 07 (cross-regulation consolidation in the company profile), D-01.1 is a **stack-merge** sub-domain: a single at-rest control (e.g. disk encryption with key custody) typically satisfies all four regulators when documentation links each one. Proportionality: a 5-FTE SaaS may default to the CRA state-of-the-art floor as the highest common denominator; a 500-FTE financial entity must additionally document the DORA classification-driven cipher strength overlay.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-01.1
title: D-01.1 Data at Rest Encryption — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.1 Data at Rest Encryption
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-01_Data-Protection/D-01.1.md
status: DRAFT
---
> **Domain analysis:** [D-01.1 Data at Rest Encryption](../../DomainAnalysis/D-01_Data-Protection/D-01.1.md)
#### D-01.1 Data at Rest Encryption
<!-- participants: GDPR, NIS2, CRA, DORA; AI_Act absent -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA (AI_Act is not present; AI Act §D-01.1 marks CRA Annex I (2)(e) as sole authority per taxonomy §4.1).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
