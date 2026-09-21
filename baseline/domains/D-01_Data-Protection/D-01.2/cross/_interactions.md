# D-01.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-01.2 Data in Transit Encryption](../../DomainAnalysis/D-01_Data-Protection/D-01.2.md)
#### D-01.2 Data in Transit Encryption
<!-- participants: GDPR, CRA, DORA; NIS2 partial via SR-NIS2-007; AI_Act absent -->
**Participants (from CRDA):** GDPR, CRA, DORA (NIS2 partially present via SR-NIS2-007 on secured voice/video/text communications — flagged as "out-of-scope for D-01.2 standalone" by the CRDA taxonomy; AI_Act not present per AEGIS taxonomy §4.1).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md`](../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md)
> (3 pairs verified against OJ text).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-01.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-001 (cross-ref) | Confidentiality, integrity, resilience of processing systems — covers in-transit via Art. 32(2) "transmitted" | Controller/processor; Art. 32(1)(b) + Art. 32(2); personal-data scope; risk-anchored; PR.DS-02 + PR.IR-01 substrate |
| CRA | SO-CRA-001 (cross-ref) / SO-CRA-003 | Confidentiality of data in transit via state-of-the-art encryption + attack-surface limitation | Manufacturer; Annex I Part I (2)(e) + (2)(j); product-level; state-of-the-art baseline + attack-surface-limitation |
| DORA | SO-DORA-001 | CIA+A maintained across data states, including in transit (4×3 matrix) | Financial entity; Art. 9(2); ICT-system-level; `high standards`; OJ-explicit `in transit` dimension |

## Validated relationships (from CRDA-deep §D-01.2)

#### Validated relationships (from CRDA-deep §D-01.2)
All 3 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial 3 COMPLEMENTARY classifications to SAME after OJ-text analysis).
The underlying obligation is the same (in-transit encryption to protect
confidentiality against network-position adversaries); the pairs differ
only in scope qualifier (`personal data` vs `product with digital
elements` vs `ICT of financial entity`) and threshold anchor
(`appropriate` vs `state of the art` vs `high standards`). The CRA
substrate is stricter (state-of-the-art + Annex I (2)(j)
attack-surface-limitation) than GDPR's risk-anchored layer; meeting CRA
discharges GDPR on the in-transit channel. CRDA-deep explicitly notes
(GDPR↔CRA pair) that a CRA-compliant TLS configuration +
network-segmentation profile discharges the GDPR Art. 32(1)(b)/(2)
in-transit control.
| | GDPR | CRA | DORA |
|---|---|---|---|
| **GDPR** | — | Y (CRA product transmits personal data — typical); disjoint in baseline (manufacturer ≠ controller) | Y (DORA financial entity transmits personal data — typical) |
| **CRA** | Y | — | Y (DORA financial entity uses CRA product; disjoint in baseline as manufacturer ≠ financial entity) |
| **DORA** | Y | Y | — |
Legend: **Y** = scope overlap on a single channel (high-level SO can
engage on a single channel); **disjoint in baseline** = manufacturer and
controller/financial entity are typically different parties.

## Cross-recipient map

#### Cross-recipient map
N/A — D-01.2 (data in transit encryption) does not involve distinct
recipient classes (same as D-01.1). The recipients are supervisory
authorities for compliance demonstration on inspection only. The
D-04.3 sub-domain is the canonical recipient-fragmentation locus for
the data-protection area.
---

## HSO considerations (from D-01.2.0 — High-level SecurityObjective)

**Considerations.**
- The three participating regulations converge on the same substantive
  obligation (in-transit confidentiality) but each anchors it to a distinct
  scope and threshold: GDPR's `appropriate` (risk-anchored, personal-data
  scope, five-event Art. 32(2) risk enumeration), CRA's `state of the art`
  (product-level, harmonised standards + attack-surface-limitation Annex I
  (2)(j)), and DORA's `high standards` (ICT-system-level, OJ-explicit `in
  transit` dimension).
- CRDA-deep verified all 3 pairs as SAME — a single in-transit design
  (mutual TLS, authenticated channels, network segmentation) discharges all
  three obligations on the same channel.
- D-01.2 is a single-control sub-domain — in-transit is the cheapest of the
  three encryption sub-domains and modern TLS configurations typically
  satisfy all three without dedicated additional investment.
- The high-level SO describes the common obligation; the per-regulation
  perspective is preserved in the sub-SOs.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + on material change | personal data transmitted across networks | supervisory authority (DPA) | Art. 32(1)(b) + Art. 32(2) |
| **CRA** | continuous product-side baseline | data transmitted by product with digital elements | MSA + ENISA | Annex I Part I (2)(e) + (2)(j) |
| **DORA** | continuous | data in transit of the financial entity | national CA + ESAs | Art. 9(2) |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-01.2.HL`) engages on a given channel **if and only if ≥2
applicable regulations' scopes overlap on the same channel** (e.g. a
mutual-TLS connection between a GDPR controller's service and a
CRA-regulated product backend deployed by a DORA financial entity —
typical in modern SaaS stacks). Pure co-applicability on disjoint
channels does **not** trigger cross-regulation aggregation. For a 5-FTE
SaaS startup with GDPR + CRA applicability, the high-level SO engages
on the same channel when both apply (typical); DORA's participation is
limited to financial entities.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 3 of 5 regulations participate (GDPR, CRA, DORA; NIS 2 is
  out-of-scope for D-01.2 standalone per CRDA taxonomy T3-vs-text gap —
  SR-NIS2-007 covers secured voice/video/text communications only; AI
  Act is out-of-scope per AEGIS taxonomy §4.1).
- 3 pairwise cells, verified by CRDA-deep as **all SAME** after
  OJ-text analysis: GDPR↔CRA (CORRECTED from COMPLEMENTARY),
  GDPR↔DORA (CORRECTED from COMPLEMENTARY), CRA↔DORA (CORRECTED from
  COMPLEMENTARY).
- The high-level SO describes the **COMMON OBJECTIVE** (in-transit
  cryptographic confidentiality + integrity); the **per-regulation
  perspective** (threshold anchor, scope qualifier, recipient, content
  template) is preserved verbatim in the three sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 3 pairs as SAME. Phase 1C Doc 07 does not
  need to resolve contradictions on D-01.2 because none exist; the
  task is to document the **single in-transit control** that
  discharges all three obligations.
- **Scope caveat (CRITICAL)** — derived from CRDA-deep verified
  classifications: the high-level SO does NOT aggregate across
  manufacturer/controller hands-offs. A SaaS-using-CRA-product
  scenario has disjoint baseline obligations (CRA manufacturer supplies
  transport-security profile in technical documentation; GDPR
  controller implements in-transit control on its own channels); the
  two are separate compliance tracks unless the same party is both
  manufacturer and controller. The CRA product baseline does not by
  itself discharge the GDPR controller's deployment-side responsibility.
---

## Emergent tensions (from CRDA-deep §D-01.2)

#### Emergent tensions (from CRDA-deep §D-01.2)
None — sub-domain is **all-SAME in baseline (3 pairs verified as SAME
after OJ-text analysis; CRDA initial 3 COMPLEMENTARY classifications
corrected to SAME)**. No conditional emergent tensions. The threshold
divergence (GDPR `appropriate`, CRA `state of the art`, DORA `high
standards`) is wording-only on a common substantive obligation; the
operational convergence is on **mutually-authenticated encrypted channels
with network segmentation + attack-surface discipline**, and the
strictest floor (CRA state-of-the-art + Annex I (2)(j)
attack-surface-limitation) discharges the others on a single channel.
CRDA-deep explicitly notes (in the GDPR↔CRA pair reasoning) that a
CRA-compliant TLS configuration + network-segmentation profile
discharges the GDPR Art. 32(1)(b)/(2) in-transit control.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-01.2 — with
overlapping scopes on the same channel — operates a **single in-transit
design (mutual TLS + network segmentation + attack-surface
discipline)** that discharges all obligations. The high-level SO
(`SO-D-01.2.HL`) describes the common obligation; the per-reg
perspective is preserved in the sub-SOs. **No conflict-resolution is
required on D-01.2 because CRDA-deep verified all 3 pairs as SAME.**
Phase 1C Doc 07 documents the **single-control strategy** — typically
satisfied with no additional investment for a company with modern TLS
configurations. For proportionality, in-transit is the cheapest of the
three encryption sub-domains; the 5-FTE SaaS default already covers
the three regulators without dedicated additional investment.

## Part 1 §3 — context

### 3. Security Requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.2.md`. See that file for cross-reg verified relationships, scope overlap matrix, Objective/Considerations content, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA, DORA (3 of 5 regs; NIS 2 out-of-scope per T3-vs-text gap; AI Act out-of-scope per AEGIS taxonomy §4.1). CRDA-deep verified 3 pairs as all-SAME (3 corrected from COMPLEMENTARY after OJ-text analysis).
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 1.2
  volere_section: 15
  volere_subtype: integrity
  title: "Data in transit is protected by cryptographic confidentiality and integrity (multi-reg aggregation)"
  derives_from:
    hso_sub_so: SO-D-01.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.2.md
    objective_ref_section: "### D-01.2.0"
  description: |
    The product shall protect data in transit — across network paths, inter-service calls, and third-party APIs — against unauthorised disclosure and alteration through cryptographic confidentiality and integrity controls (mutual authentication, encryption, integrity verification), as the common substantive obligation converging across GDPR Art. 32(1)(b) + Art. 32(2), CRA Annex I Part I (2)(e) + (2)(j), and DORA Art. 9(2) where ≥2 of these scopes overlap on the same channel.
  fit_criterion: |
    TLS 1.3 (or stronger) is applied to all in-transit channels; mutual authentication (mTLS) is enforced where both channel endpoints authenticate to each other; certificate validation (chain, revocation, expiry) is configured to fail closed; network segmentation policy is documented; the strictest applicable floor (CRA state-of-the-art + Annex I (2)(j) attack-surface-limitation) discharges GDPR and DORA on a single channel; verified by automated network scan (cipher-suite enumeration + protocol-version probe) + manual configuration review + joint risk-assessment artefact citing all three legal anchors when scopes overlap.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-02]
  applicable_if:
    regs: [GDPR, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs overlap on same channel (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The three participating regulations converge on the same substantive obligation
    (in-transit confidentiality) but each anchors it to a distinct scope and
    threshold: GDPR's `appropriate` (risk-anchored, personal-data scope, five-event
    Art. 32(2) risk enumeration), CRA's `state of the art` (product-level, harmonised
    standards + attack-surface-limitation Annex I (2)(j)), and DORA's `high standards`
    (ICT-system-level, OJ-explicit `in transit` dimension). CRDA-deep verified all
    3 pairs as SAME — a single in-transit design (mutual TLS, authenticated channels,
    network segmentation) discharges all three obligations on the same channel.
    D-01.2 is a single-control sub-domain — in-transit is the cheapest of the three
    encryption sub-domains and modern TLS configurations typically satisfy all three
    without dedicated additional investment. The high-level SO describes the common
    obligation; the per-regulation perspective is preserved in the sub-SOs. (Copied
    from the HSO Considerations block of `### D-01.2.0`; preserved here for
    self-contained traceability.)
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-01.2
title: D-01.2 Data in Transit Encryption — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.2 Data in Transit Encryption
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-01_Data-Protection/D-01.2.md
status: DRAFT
---
> **Deep analysis:** [D-01.2 Data in Transit Encryption](../../DeepAnalysis/D-01_Data-Protection/D-01.2.md)
#### D-01.2 Data in Transit Encryption
<!-- participants: GDPR, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-001 (cross-ref) | Confidentiality, integrity, resilience of processing systems/services — implicitly covers data in transit via "processing systems" | Controller/processor; Art. 32(1)(b); risk-anchored |
| CRA | SO-CRA-001 (cross-ref) / SO-CRA-003 | Confidentiality of data in transit across network paths via state-of-the-art encryption | Manufacturer; Annex I Part I (2)(e); product-level; both internal east-west and external-boundary |
| DORA | SO-DORA-001 | CIA+A maintained across data states, including in transit | Financial entity; Art. 9(2); OJ-explicit in-transit dimension |
| AI_Act | — | Out-of-scope (no in-transit mandate; CRA/NIS 2/DORA sole authorities) | n/a |
| NIS2 | — | Out-of-scope for D-01.2 standalone (T3-vs-text gap per `99_NIS2_Synthesis.md` §8; in-transit covered by SR-NIS2-001 cryptography policy + SR-NIS2-007 secured communications) | n/a |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,CRA,DORA -->
- All three regulations converge on PR.DS-02 as the operational anchor for in-transit confidentiality, but the **scope-determiner** diverges: GDPR (personal data), CRA (personal or other, product-stored/transmitted), DORA (ICT-supported data, financial-entity scope). A CRA-regulated product transmitting mixed personal + telemetry data to a DORA financial entity host running a GDPR-scoped controller processing the personal-data subset creates a three-way layered obligation with no clean joint-decision-rule; the Layer 1/2 synthesis should establish whether the CRA state-of-the-art in-transit primitive is automatically sufficient for the other two (likely yes for confidentiality; the integrity + authenticity layers of DORA require entity-level additional controls).
<!-- /emergent -->
##### SR cross-validation
All three regulations map to PR.DS-02 (Data-in-transit protected) + PR.IR-01 (Networks protected from unauthorized logical access / usage). The shared anchor means a single network-security design typically discharges the three obligations. CRA additionally maps to PR.IR-01 for the Annex I (2)(j) attack-surface-limitation leg; GDPR additionally maps to PR.IR-01 for the Art. 32(1)(b) network-layer support. No contradictory mappings observed.
##### Downstream implication
For Phase 1C Doc 07, D-01.2 is a **single-control** sub-domain: a mutual-TLS + network-segmentation design typically satisfies all three regulators for an in-scope company. Proportionality: in-transit is universally the cheapest of the three encryption sub-domains; a 5-FTE SaaS with modern TLS configurations will satisfy all three without dedicated additional investment.
---
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-01.2
title: D-01.2 Data in Transit Encryption — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.2 Data in Transit Encryption
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-01_Data-Protection/D-01.2.md
status: DRAFT
---
> **Domain analysis:** [D-01.2 Data in Transit Encryption](../../DomainAnalysis/D-01_Data-Protection/D-01.2.md)
#### D-01.2 Data in Transit Encryption
<!-- participants: GDPR, CRA, DORA; NIS2 partial via SR-NIS2-007; AI_Act absent -->
**Participants (from CRDA):** GDPR, CRA, DORA (NIS2 partially present via SR-NIS2-007 on secured voice/video/text communications — flagged as "out-of-scope for D-01.2 standalone" by the CRDA taxonomy; AI_Act not present per AEGIS taxonomy §4.1).

