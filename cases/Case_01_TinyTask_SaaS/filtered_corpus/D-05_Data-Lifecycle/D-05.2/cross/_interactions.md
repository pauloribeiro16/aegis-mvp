<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-05.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-05.2 Retention & Archiving](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md)
#### D-05.2 Retention & Archiving
<!-- participants: GDPR, CRA, AI_Act -->
**Participants (from CRDA):** GDPR, CRA, AI_Act
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.2 per AEGIS taxonomy §4.1 — DORA Art. 12(1) backup policies specify scope and frequency but do not impose retention / archiving obligations as such. GDPR is the dedicated authority for retention; CRA addresses the distinct update-availability tail; AI Act addresses the distinct AI-log minimum floor.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-05.2 Retention & Archiving
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md`](../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md)
> (3 pairs verified against OJ text — **3 of 5 participating regulations
> are GDPR, CRA, AI_Act; NIS 2 and DORA are out-of-scope per AEGIS
> taxonomy §4.1** as noted by `DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md`
> line 36: "NIS2 and DORA are out-of-scope for D-05.2 per AEGIS taxonomy
> §4.1 — DORA Art. 12(1) backup policies specify scope and frequency but
> do not impose retention / archiving obligations as such. GDPR is the
> dedicated authority for retention; CRA addresses the distinct
> update-availability tail; AI Act addresses the distinct AI-log minimum
> floor").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-05.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-017 | Personal data kept no longer than necessary; longer only where lawful and Art. 89(1) safeguards in place (Art. 5(1)(e) storage limitation + Art. 30(1)(f) RoPA retention time-limits) | Personal data; storage limitation; controller/processor; Art. 5(1)(e) + Art. 30(1)(f) + Art. 89(1); PR.DS-12 + ID.AM-03 |
| CRA | SO-CRA-035 + SO-CRA-061 (cross-ref) | Security updates and supporting advisory messages remain available across support period + Art. 13(18) 10-year Annex II information accessibility | Update artefacts (firmware, patches, advisories) + Annex II information; manufacturer obligation; Annex I Part II (7)/(8) + Art. 13(9) 10-year tail + Art. 13(18) 10-year information accessibility + Art. 13(8) 5-year support-period floor; PR.PS-02 + GV.OC-04 (10-year tail SR) + PR.PS-02 + GV.OV-02 |
| AI_Act | SO-AIACT-006 | High-risk AI system logs retained for ≥6 months aligned with intended purpose, unless Union/national law provides otherwise (Art. 19(1); T5 mapping error on Art. 12(4) per `SR-AIACT-008` `ambiguity_notes`) | AI logs; minimum floor; provider obligation; Art. 19(1) 6-month floor + `under their control` POLY + GDPR escape clause; PR.PS-04 + GV.PO-02 |

## Validated relationships (from CRDA-deep §D-05.2)

#### Validated relationships (from CRDA-deep §D-05.2)
Of 3 pairs, **1 verified as SAME (DIFFERENT-PERSPECTIVE; CRDA initial classification held) and 2 CORRECTED** (GDPR ↔ CRA: CRDA `CONTRADICTORY (direction)` → verified `SCOPE-DISJOINT` — the CRDA reasoning itself concedes "CRA's 10-year tail is about *update availability*, not personal-data retention", making the contradictory label scope-incorrect, since two regulations imposing limits on different data classes at different actors are scope-disjoint not contradictory; GDPR ↔ AI_Act: CRDA `CONTRADICTORY (direction)` → verified `COMPLEMENTARY (floor-within-ceiling)` — the AI Act 6-month floor is a subset of GDPR's "as long as necessary" envelope, which the CRDA reasoning itself states "the two are reconcilable: the AI Act 6-month floor is a subset of GDPR's 'as long as necessary'", making the contradictory label scope-incorrect since two regulators setting the same boundary at different sides of an interval jointly bound the admissible range, which is the textbook complementary pattern not the prohibition-vs-prohibition pattern). **No SCOPE-DISJOINT pairs on the baseline; no CONTRADICTORY pairs on the retention duty itself** — the two CORRECTED pairs were relabelled from CONTRADICTORY to their correct classification, and the relabelling is preserved verbatim.
- **GDPR ↔ CRA** — **CORRECTED: CRDA `CONTRADICTORY (direction)` → verified `SCOPE-DISJOINT`**: GDPR Art. 5(1)(e) imposes an upper limit on personal-data retention ("no longer than is necessary"); CRA imposes a 10-year *minimum availability* of security updates (Art. 13(9)) and a 10-year Annex II information accessibility (Art. 13(18)) plus the Art. 13(8) 5-year support-period minimum. The CRDA reasoning itself states: "These are not on the same axis (CRA's 10-year tail is about *update availability*, not personal-data retention)". With that concession, the `CONTRADICTORY` label is internally inconsistent — a true contradiction requires mutually exclusive obligations on the same data at the same actor, and there is no such overlap here. GDPR Art. 5(1)(e) caps the retention of *personal data*; CRA Annex I Part II (7)/(8) and Art. 13(9) require *update artefact* availability. If a CRA product's update-distribution logs contain personal data, the controller must decouple the log retention from the update availability via separation architecture (pseudonymisation, separate retention rules) — but that is a **layering rule**, not a contradiction. The pair is **scope-disjoint in baseline** (different data classes — personal data vs update artefacts); the layering rule applies only in the narrow window where a CRA update-distribution log contains personal data (then both regimes apply, the CRA-side to the artefact and the GDPR-side to the personal-data subset, with separation architecture as the controlled hand-off).
- **GDPR ↔ AI_Act** — **CORRECTED: CRDA `CONTRADICTORY (direction)` → verified `COMPLEMENTARY (floor-within-ceiling)`**: GDPR imposes an upper limit on personal-data retention ("no longer than is necessary"); AI Act imposes a lower floor (≥6 months) for high-risk AI system logs. The two are **reconcilable**: the AI Act 6-month floor is a subset of GDPR's "as long as necessary" envelope — if the intended purpose requires 6+ months of logs, GDPR's "necessary" is satisfied for that period. The CRDA reasoning itself states: "The two are reconcilable: the AI Act 6-month floor is a subset of GDPR's 'as long as necessary'". A floor-within-ceiling relationship is the textbook **complementary** pattern — one regulation sets a hard floor (≥6 months), the other sets a qualitative ceiling (no longer than necessary), and the operative range is the intersection [6 months, "necessary"]. There is no contradiction. The CRDA `CONTRADICTORY` label is scope-incorrect. The pair is **substantive-complementary** (Y on the same event at the same controller/provider when the AI log contains personal data); the two obligations jointly bound the admissible range, with the AI Act setting the floor and the GDPR setting the cap.
- **CRA ↔ AI_Act** — DIFFERENT-PERSPECTIVE (SAME): CRA's update-availability tail is about *update artefact availability* (the user can fetch a security update for ≥10 years post-support per Art. 13(9) and the Annex II information remains accessible for ≥10 years per Art. 13(18)); AI Act's 6-month floor is about *log retention* (the provider must keep system-generated logs for at least 6 months per Art. 19(1)). Different objects (update artefacts vs AI-system logs), different actors (manufacturer vs provider), different purposes (user protection continuity vs post-market monitoring and incident reconstruction). Complementary, not overlapping. CRDA's label is correct.
The retention/archiving architecture is **legitimately diverse** — each regulator targets a distinct data class (personal data vs update artefacts vs AI logs) with a distinct obligation direction (GDPR ceiling: upper limit; CRA floor: lower bound for update artefacts; AI Act floor: lower bound for AI logs). The high-level SO surfaces the **common retention/archiving duty** as a **3-axis layering rule**: (1) GDPR Art. 5(1)(e) ceiling (upper limit, qualitative "no longer than is necessary"); (2) AI Act Art. 19(1) floor (≥6 months for high-risk AI logs containing personal data); (3) CRA Art. 13(9) + Art. 13(18) availability tail (≥10 years for update artefacts and Annex II information). The per-regulation perspective is preserved verbatim in the three sub-SOs (data class, obligation direction, trigger, anchor, evidence template).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (Y when a CRA update-distribution log contains personal data — GDPR applies to the personal-data subset, CRA applies to the artefact portion independently, separation architecture is the controlled hand-off; disjoint in baseline: personal data vs update artefacts)  |
|  **CRA**  |  Conditional (Y when CRA update-distribution log contains personal data; disjoint in baseline: update artefacts vs personal data)  |  —  |
Legend: **Conditional** = scope overlap only under specific circumstances (CRA update log contains personal data; AI log contains personal data; integrated manufacturer-controller / provider-controller). **N** = scope-disjoint in baseline (CRA update-availability tail vs AI Act log retention — different data classes at different actors with different purposes; the two obligations sit on different data flows). CRDA-deep scope-disjoint tests: GDPR↔CRA = Conditional (Y when CRA update log contains personal data; N pure update artefacts with no personal data); GDPR↔AI_Act = Conditional (Y when AI logs contain personal data; N pure technical logs with no personal data); CRA↔AI_Act = N (disjoint in baseline — different objects, different actors, different purposes).

## Cross-recipient map

#### Cross-recipient map
D-05.2 itself does **not** generate recipient asymmetry — the
retention/archiving process is **inward-looking** (the controller /
manufacturer / provider sets the retention boundary, then documents the
retention rationale and the erasure/cascade procedure, then propagates
the boundary to the data-inventory and operational evidence base).
The recipient fragmentation across the three regulators is at the
**downstream compliance-demonstration point**: GDPR's supervisory
authority (DPA) on the Art. 5(2) accountability evidence (Art. 30(1)(f)
RoPA retention time-limits + Art. 89(1) safeguards for the
public-interest carve-out + Art. 5(1)(e) `no longer than is necessary`
boundary); CRA's market surveillance authority (MSA) on the Annex VII
§3 risk-assessment record + the Annex II information deliverable
(support-period end-date + Annex II §7 type of technical security
support + the 10-year Annex II information accessibility per Art. 13(18)
+ the 10-year update-availability tail per Art. 13(9)); and AI Act's
market surveillance authority + national competent authority on the
Annex IV technical documentation (Art. 19(1) ≥6-month log retention
+ the "appropriate to the intended purpose" upward adjustment clause
+ the GDPR escape clause). These are distinct regulatory channels but
they do not generate a notification cascade of D-05.2 itself — they
are compliance-evidence channels on the same retention/archiving
architecture. **D-05.3 (Right to Erasure) and D-09.4 (Records of
Processing) are where the recipient asymmetry manifests operationally
on the GDPR side; D-04.3 (Regulatory Notification) and D-02.3
(Coordinated Vulnerability Disclosure) are where the recipient
asymmetry manifests operationally on the CRA side; D-04.3 (Regulatory
Notification) and D-10.2 (Audit Logging) are where the recipient
asymmetry manifests operationally on the AI Act side. D-05.2 is the
retention-boundary architecture that constrains the data-lifecycle
timeline and produces the retention-rationale evidence base.**
---

## HSO considerations (from D-05.2.0 — High-level SecurityObjective)

**Considerations.**
- Three participating regulations (GDPR, CRA, AI Act) each impose a retention/archiving duty on a distinct data class with a distinct obligation direction: GDPR Art. 5(1)(e) "no longer than is necessary" qualitative ceiling on personal data (controller-side, Art. 30(1)(f) RoPA time-limits + Art. 89(1) safeguards for the public-interest/research/statistical carve-out); CRA Art. 13(8) 5-year support period + Art. 13(9) 10-year update-availability tail + Art. 13(18) 10-year Annex II information accessibility on update artefacts (manufacturer-side, floor); AI Act Art. 19(1) ≥6-month floor on high-risk AI system logs (provider-side, "appropriate to the intended purpose" upward adjustment + GDPR escape clause).
- CRDA-deep verified relationships: GDPR↔CRA = CORRECTED from CONTRADICTORY (direction) to SCOPE-DISJOINT (the CRDA reasoning itself concedes CRA's 10-year tail is on update availability, not personal-data retention; the pair is scope-disjoint in baseline with separation architecture as the layering rule when the CRA update log contains personal data); GDPR↔AI_Act = CORRECTED from CONTRADICTORY (direction) to COMPLEMENTARY (floor-within-ceiling — the AI Act ≥6-month floor is a subset of GDPR's "as long as necessary" envelope, with operative range [6 months, "necessary"]); CRA↔AI_Act = SAME — DIFFERENT-PERSPECTIVE (update artefact availability vs AI log retention, different objects, actors, purposes).
- The 1 conditional emergent tension (3-way retention/obligation interaction on a single data flow when CRA update logs or AI logs contain personal data) is regulated by two layering rules: separation architecture (pseudonymisation, separate retention rules, separate storage paths) for the CRA↔GDPR overlap; floor-within-ceiling for the AI Act↔GDPR overlap.
- Implementation guidance: the three data classes are layered not collapsed — personal data is collected from data subjects (GDPR), update artefacts are produced by the manufacturer (CRA), AI logs are generated by the AI system (AI Act). A unified retention platform may serve the technical substrate but policy and evidence layers must remain class-segregated.
- Scope caveats: CRA 10-year tail is on update artefacts (firmware, patches, advisories — non-personal data) and Annex II information, NOT on personal data; AI Act 6-month floor is a floor not a ceiling — the upward adjustment clause permits retention beyond 6 months when intended purpose requires; the CRA Art. 13(9) 10-year-or-remainder is a twin-anchor pattern where the longer of the two applies per update (R2 reading).

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 3 participating regulations each define D-05.2 over a distinct
**data class** with a distinct **obligation direction** (ceiling or
floor); the trigger, the threshold anchor, the lifecycle stage, the
recipient, and the legal anchor all depend on which data class the
retention duty applies to.
| Axis (reg) | Data class | Obligation direction | Trigger | Threshold anchor | Lifecycle stage | Recipient | Legal anchor |
|---|---|---|---|---|---|---|---|
| **GDPR** | personal data (data-subject-identifiable) | ceiling (upper limit, qualitative) | continued storage of personal data beyond processing-purpose end | `no longer than is necessary for the purposes for which the personal data are processed` (Art. 5(1)(e) VAG) + Art. 30(1)(f) `envisaged time limits for erasure` + Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for the public-interest/scientific-research/statistical carve-out | collection → purpose end → erasure; Art. 89(1) carve-out for archiving/research/statistical | supervisory authority (DPA) — Art. 5(2) accountability + Art. 30(1) RoPA + Art. 17 erasure | Art. 5(1)(e) + Art. 30(1)(f) + Art. 89(1) + Art. 17 + Art. 19 cascade |
| **CRA** | update artefacts (security updates, firmware, patches, advisories) + Annex II information | floor (lower bound, support period + 10-year tail) | ongoing availability of security updates across support period + Annex II information accessibility | support period ≥5 years (Art. 13(8)) OR expected use time if shorter; update-availability tail ≥10 years from issue date OR remainder of support period, whichever is longer (Art. 13(9)); Annex II information accessibility ≥10 years from placing on market (Art. 13(18)) | support period (post-market, 5-year minimum) + 10-year availability tail | market surveillance authority (MSA) + users | Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge + Art. 13(8) support period + Art. 13(9) 10-year update-availability tail + Art. 13(18) 10-year Annex II information accessibility + Art. 13(19) support-period end-date display + Annex II §7 |
| **AI_Act** | AI logs (high-risk AI system auto-generated event logs) | floor (lower bound, 6 months) | high-risk AI system log generation (Art. 12(1) lifetime automatic event recording) | `at least six months, unless provided otherwise in the applicable Union or national law` (Art. 19(1)) + `appropriate to the intended purpose of the high-risk AI system` (upward adjustment clause) + `under their control` (responsibility-allocation) + GDPR escape clause (when log contains personal data) | log generation → 6-month minimum retention → erasure at the `necessary` boundary | market surveillance authority + national competent authority — Annex IV technical documentation + Art. 19(1) log-retention records | Art. 19(1) 6-month floor (cf. T5 mapping error: AIA-C11 cited Art. 12(4) which does not exist in OJ; substance is in Art. 19(1) per `SR-AIACT-008` `ambiguity_notes`) + Art. 12(1)/(2) lifetime log generation + Art. 72 post-market monitoring + Art. 6(2) high-risk classification + Art. 9(1)/(2) risk management |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-05.2.HL`) engages on a given party **if and only if ≥2 applicable
regulations' data-class scope-determiners overlap on the same party**
(e.g. a GDPR controller that also manufactures CRA-regulated products
and operates a high-risk AI system processing personal data in both
the CRA update log and the AI log — a vertically-integrated
manufacturer-controller-provider on a 3-axis retention/archiving
architecture with the GDPR ceiling, the CRA availability floor, and
the AI Act log-retention floor all simultaneously engaged). Pure
co-applicability of disjoint-data-class regulations on different data
objects does **not** trigger cross-regulation aggregation — see the
Activation logic in the file header. For a 5-FTE SaaS startup with
GDPR + CRA applicability but no AI Act applicability, only the GDPR
and CRA sub-SOs activate; the high-level SO engages on the same
party if both apply, with the boundary between GDPR personal-data
retention ceiling and CRA update-artefact availability floor
documented as the controlled hand-off (separation architecture when
the CRA update log contains personal data; pure parallel obligations
when the log is purely technical). **The three data classes are
layered, not collapsed**: personal data is collected from data
subjects (GDPR); update artefacts are produced by the manufacturer
(CRA); AI logs are generated by the AI system (AI Act). The
high-level SO surfaces the common retention/archiving duty as the
3-axis layering rule but does **NOT** aggregate the per-reg data
class, obligation direction, trigger, threshold anchor, lifecycle
stage, recipient, or evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 3 of 5 regulations participate (GDPR, CRA, AI_Act; NIS 2 and DORA
  are out-of-scope per AEGIS taxonomy §4.1 — DORA Art. 12(1) backup
  policies specify scope and frequency of backup but do not impose
  retention or archiving obligations as such; GDPR is the dedicated
  authority for retention; CRA addresses the distinct update-
  availability tail; AI Act addresses the distinct AI-log minimum
  floor).
- 3 pairwise cells, verified by CRDA-deep as **1 SAME + 2 CORRECTED**:
  CRA↔AI_Act (SAME — DIFFERENT-PERSPECTIVE, CRDA initial classification
  held); GDPR↔CRA (**CORRECTED** from CONTRADICTORY (direction) to
  SCOPE-DISJOINT — the CRDA reasoning itself concedes "CRA's 10-year
  tail is about *update availability*, not personal-data retention",
  making the contradictory label scope-incorrect; the pair is
  scope-disjoint in baseline with separation-architecture requirement
  as the layering rule where the CRA update log contains personal
  data); GDPR↔AI_Act (**CORRECTED** from CONTRADICTORY (direction) to
  COMPLEMENTARY (floor-within-ceiling) — the AI Act ≥6-month floor is
  a subset of GDPR's "no longer than is necessary" envelope, which
  the CRDA reasoning itself states is reconcilable, making the
  contradictory label scope-incorrect; the pair is substantive-
  complementary on the same data flow when the AI log contains
  personal data, with the operative range [6 months, "necessary"]).
- The three regulations impose **distinct data-class obligations on
  a common substantive retention/archiving duty** with three
  **distinct obligation directions**: GDPR's controller-side
  personal-data retention ceiling (Art. 5(1)(e) `no longer than is
  necessary` VAG upper limit); CRA's manufacturer-side update-artefact
  availability floor (Art. 13(8) 5-year support period + Art. 13(9)
  10-year update-availability tail + Art. 13(18) 10-year Annex II
  information accessibility); AI Act's provider-side AI-log retention
  minimum floor (Art. 19(1) ≥6 months). The three obligation
  directions jointly form the **3-axis layering rule** (ceiling +
  floor + floor) that constrains the retention/archiving
  architecture on a single party across all three regulators.
- The high-level SO describes the **COMMON OBJECTIVE** (retain data
  for a period that satisfies the 3-axis layering rule — GDPR
  ceiling on personal data + CRA availability tail on update
  artefacts + AI Act minimum floor on AI logs; document the
  retention rationale; apply the separation architecture when
  regimes overlap on a single data flow; deliver the evidence
  base); the **per-regulation perspective** (data class, obligation
  direction, trigger, anchor, lifecycle stage, evidence template)
  is preserved verbatim in the three sub-SOs.
- The high-level SO does **NOT** resolve the 1 conditional emergent
  tension — the **3-way retention/obligation interaction** (GDPR
  ceiling + AI Act floor + CRA availability tail on three different
  data flows, with potential overlap on a single data flow when
  CRA update logs or AI logs contain personal data). The pairwise
  readings (GDPR↔CRA, GDPR↔AI_Act, CRA↔AI_Act) each handle two of
  the three axes, but the *non-pairwise observation* is that a
  single data stream (e.g. update logs from a CRA-classified
  high-risk AI product) may need to satisfy all three axes
  simultaneously. The high-level SO codifies this as a **layering
  rule, not a contradiction**: (a) the AI Act ≥6-month floor applies
  to the AI-log portion; (b) the GDPR Art. 5(1)(e) `necessary`
  boundary applies to the personal-data portion; (c) the CRA
  update-availability tail applies to the update-artefact portion;
  (d) when regimes overlap on a single data flow, separation
  architecture (pseudonymisation, separate retention rules,
  separate storage paths) is the controlled hand-off. The tension
  is **conditional** (it engages only when a CRA update log or an
  AI log contains personal data) and is **regulated** by the
  separation-architecture requirement. Phase 1C Doc 07 documents
  the 3-axis layering architecture; Phase 3 case generation must
  surface the separation-architecture requirement explicitly when
  the case company's data flows cross regime boundaries.
- **Scope caveat (CRITICAL — data-class divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the three data classes into a single retention policy.
  Personal data, update artefacts, and AI logs are **distinct data
  objects** at **distinct lifecycle stages** (controller-side
  processing vs manufacturer-side product support vs provider-side
  AI system log generation), with distinct obligation directions
  (ceiling vs floor vs floor), distinct threshold anchors (GDPR VAG
  vs CRA hard 10-year tail vs AI Act hard 6-month floor), and
  distinct evidence templates (Art. 30(1)(f) RoPA time-limits +
  Art. 89(1) safeguards vs Annex VII §3 risk-assessment + Annex II
  information deliverable + Annex VII §4 support-period determination
  vs Annex IV technical documentation + Art. 19(1) log-retention
  records). A unified data-retention platform may serve the
  technical substrate (e.g. a unified retention policy engine with
  per-data-class rules), but the policy and evidence layers must
  remain **class-segregated** for compliance demonstration. Phase
  1A must therefore emit **three checks before applying the
  high-level SO** (one per participating regulation) to confirm that
  the per-reg data class, obligation direction, trigger, threshold
  anchor, lifecycle stage, recipient, and evidence template are
  documented separately; the high-level SO surfaces the common
  retention/archiving duty as the 3-axis layering rule but does NOT
  aggregate the per-reg data classes.
- **Scope caveat (CRITICAL — CRA 10-year tail is on update
  artefacts, NOT on personal data)** — derived from CRDA-deep
  verified classifications: CRA Annex I Part II (7)/(8) and
  Art. 13(9)/(18) are about update artefact availability and Annex II
  information accessibility, NOT about personal-data retention. If
  a CRA-compliant product's update-distribution logs contain
  personal data, the controller must **decouple** the log retention
  from the update availability via separation architecture. The CRA
  10-year tail does NOT extend to personal data; the GDPR Art. 5(1)(e)
  `necessary` boundary remains the operative ceiling on the
  personal-data portion. The "10-year tail" of CRA is on update
  artefacts (firmware, patches, advisories — non-personal data) and
  Annex II information (product documentation, support-period end-
  date, intended purpose — non-personal data). For a CRA product
  with personal-data-containing update logs, the separation
  architecture is the controlled hand-off: pseudonymise the
  personal-data portion of the log, retain the pseudonymised log
  for the GDPR `necessary` boundary, and retain the update artefact
  for the CRA 10-year tail.
- **Scope caveat (CRITICAL — AI Act 6-month floor is a floor, not
  a ceiling)** — derived from CRDA-deep verified classifications: the
  AI Act Art. 19(1) `at least six months` is a **floor**, not a
  ceiling — the upward adjustment clause `appropriate to the
  intended purpose of the high-risk AI system` permits the provider
  to retain logs longer than 6 months when the intended purpose
  requires. The GDPR escape clause `unless provided otherwise in the
  applicable Union or national law, in particular Union law on the
  protection of personal data` defers to GDPR Art. 5(1)(e) when the
  log contains personal data. The operative retention range is
  [6 months, "necessary"] — the AI Act sets the floor, the GDPR sets
  the cap, the provider chooses the actual retention within the
  range based on the intended purpose. The high-level SO does NOT
  default to the 6-month floor; the default is the intended-purpose-
  calibrated retention within the floor-within-ceiling range.
- **Scope caveat (CRITICAL — CRA Art. 13(9) 10-year tail
  interpretation)** — derived from CRDA-deep verified classifications:
  the CRA Art. 13(9) `at least 10 years or for the remainder of the
  support period, whichever is longer` is a **twin-anchor** pattern
  where the 10-year floor and the support-period remainder are
  compared, and the longer of the two applies in each case. The
  chosen reading is R2 — the calculation is performed case-by-case on
  a per-update basis. A long-support product may have many updates
  subject to the support-period remainder rather than the fixed
  10-year floor. R1 (always 10 years) is rejected because it ignores
  the "whichever is longer" qualifier; R3 (always the support-period
  remainder) is similarly rejected because it ignores the 10-year
  floor when the support period is shorter than 10 years. The
  Art. 13(18) `accessible for at least 10 years` is similarly
  structured: the conjunction `support period + at least 10 years`
  is preserved, with the longer of the two governing. R2 is the
  per-update / per-document basis; R1 (10 years full stop) is
  rejected as narrower than the literal.
---

## Emergent tensions (from CRDA-deep §D-05.2)

#### Emergent tensions (from CRDA-deep §D-05.2)
**1 conditional emergent tension** — the **3-way retention/obligation
interaction** (GDPR ceiling on personal data; AI Act floor on AI
logs; CRA availability tail on update artefacts — three different
data flows with three different obligation directions, with potential
overlap on a single data flow when CRA update logs or AI logs
contain personal data). The pairwise readings (GDPR↔CRA, GDPR↔AI_Act,
CRA↔AI_Act) each handle two of the three axes, but the *non-pairwise
observation* is that a single data stream (e.g. update logs from a
CRA-classified high-risk AI product) may need to satisfy all three
axes simultaneously: (a) the CRA update-availability tail applies
to the update-artefact portion of the log; (b) the AI Act ≥6-month
log-retention floor applies to the AI-system log portion; (c) the
GDPR Art. 5(1)(e) `necessary` boundary applies to the personal-data
portion. The high-level SO codifies this as a **layering rule, not a
contradiction**: (a) identify the data class on the single data flow
(update artefact vs AI log vs personal data); (b) apply the
corresponding obligation direction (CRA availability floor on update
artefacts; AI Act minimum floor on AI logs; GDPR ceiling on personal
data); (c) when regimes overlap on a single data flow, **separation
architecture** (pseudonymisation, separate retention rules, separate
storage paths) is the controlled hand-off. The tension is
**conditional** (it engages only when a CRA update log or an AI log
contains personal data, or when a single data flow crosses regime
boundaries) and is **regulated** by the separation-architecture
requirement. Phase 1C Doc 07 documents the 3-axis layering
architecture; Phase 3 case generation must surface the
separation-architecture requirement explicitly when the case
company's data flows cross regime boundaries.
**No SCOPE-DISJOINT baseline pairs** — the 3×3 matrix shows
**Conditional** scope overlap in baseline (Y or N depending on
whether the data flow contains personal data); the baseline is not
scope-disjoint across all three pairs. **No CONTRADICTORY pairs on
the retention duty itself** — the 2 CORRECTED pairs (GDPR ↔ CRA and
GDPR ↔ AI_Act) were relabelled from CONTRADICTORY to their correct
classifications, and the relabelling is preserved verbatim. The
**data-class divergence** (personal data / update artefacts / AI
logs) is the **legitimately diverse dimension**: each regulator
targets a distinct data class with a distinct obligation direction
(ceiling vs floor vs floor), and the operational convergence is on
the **3-axis layering rule** (GDPR ceiling + AI Act floor + CRA
availability tail) with explicit axis-segregated hand-offs and
separation-architecture requirement where regimes overlap on a single
data flow. The **CRA 10-year tail is on update artefacts and Annex
II information, NOT on personal data** — this is the rare-but-honest
distinction that prevents the retention duty from being conflated
across data classes; the controller-side GDPR `necessary` boundary
remains the operative ceiling on the personal-data portion. The
**AI Act 6-month floor is a floor-within-ceiling**, not a standalone
obligation — the GDPR `necessary` boundary is the cap, the AI Act
6-month floor is the floor, the provider chooses the actual retention
within the [6 months, "necessary"] range based on the intended
purpose. The **CRA ↔ AI Act pair is genuinely N in baseline**
(different objects, different actors, different purposes); the two
obligations sit on different data flows and do not interact unless
the same data flow is both a CRA update artefact and an AI Act log
(a narrow window). The high-level SO surfaces the common
retention/archiving duty as the 3-axis layering rule; the per-reg
data class, obligation direction, trigger, anchor, lifecycle stage,
recipient, and evidence template are documented separately in the
three sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-05.2 — with
overlapping data-class scope-determiners on the same party — operates
a **3-axis retention/archiving architecture** with explicit
axis-segregated hand-offs. The high-level SO (`SO-D-05.2.HL`)
describes the common retention/archiving duty as the 3-axis layering
rule (GDPR ceiling on personal data + AI Act minimum floor on AI
logs + CRA availability tail on update artefacts); the per-reg
perspective is preserved in the three sub-SOs (data class,
obligation direction, trigger, anchor, lifecycle stage, recipient,
evidence template). **The 1 conditional emergent tension on the
3-way retention/obligation interaction is documented as a layering-
rule architecture with separation-architecture requirement, not a
contradiction.** The high-level SO does NOT collapse the three data
classes into a single retention policy; the per-reg perspective on
data class, obligation direction, trigger, anchor, lifecycle stage,
recipient, and evidence template is preserved verbatim. Phase 1C
Doc 07 documents the **3-axis retention/archiving strategy**: (1) a
3-axis retention/archiving architecture with explicit axis hand-offs
at the data-class surfaces (personal data vs update artefacts vs AI
logs); (2) the **CRA 10-year tail is on update artefacts and Annex
II information, NOT on personal data** — separation architecture is
the controlled hand-off when a CRA update log contains personal
data; (3) the **AI Act ≥6-month floor is a subset of the GDPR
Art. 5(1)(e) `necessary` envelope** — the operative retention range
is [6 months, "necessary"] with the AI Act setting the floor and the
GDPR setting the cap (floor-within-ceiling); (4) the CRA ↔ AI Act
pair is genuinely N in baseline — the two obligations sit on
different data flows (update artefacts vs AI logs) at different
actors (manufacturer vs provider) with different purposes (user
protection continuity vs post-market monitoring), and do not interact
unless the same data flow is both a CRA update artefact and an AI
Act log (a narrow window where the AI Act log-retention floor and
the CRA update-availability tail both apply, with the longer of the
two governing); (5) the **GDPR Art. 89(1) safeguards** (pseudo-
nymisation, aggregation, access limitation) as the public-interest/
scientific-research/statistical carve-out for indefinite retention;
(6) the **CRA Art. 13(9) 10-year-or-remainder twin-anchor** as the
per-update basis (R2 reading — not always 10 years full stop, not
always the support-period remainder); (7) the **CRA Art. 13(18)
10-year Annex II information accessibility** as the durable
instruction layer; (8) the **AI Act T5 mapping error on AIA-C11 /
Art. 12(4) does not exist in the OJ** — the substance is in
Art. 19(1); T5 should be reconciled by removing AIA-C11 or remapping
it to Art. 19(1); (9) the **AI Act `under their control` POLY**
(cumulative reading — physical + legal + technical access) as the
responsibility-allocation hinge; (10) the **AI Act `appropriate to
the intended purpose`** as the upward adjustment clause for the
6-month floor. For proportionality (P2), a 5-FTE SaaS with GDPR + CRA
applicability may default to the CRA Art. 13(9) 10-year-or-remainder
update-availability tail plus the GDPR Art. 5(1)(e) controller-side
necessity assessment (AI Act log retention is out of scope unless
the SaaS operates a high-risk AI system); a mid-size AI-enabled
product company in scope of all three regulations must additionally
document the AI Act Art. 19(1) ≥6-month log-retention floor with
the upward adjustment justification, the separation-architecture
requirement where a CRA update log or AI log contains personal data,
and the GDPR escape clause application (Art. 5(1)(e) `necessary`
boundary as the cap on the personal-data portion).
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-05.2 Retention & Archiving — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.2.md`. See that file for cross-reg verified relationships (3 pairs verified: 1 SAME — CRA↔AI_Act = DIFFERENT-PERSPECTIVE on update-artefact availability vs AI-log retention, different objects/actors/purposes; 2 CORRECTED — GDPR↔CRA, was CONTRADICTORY (direction) → SCOPE-DISJOINT (CRDA reasoning itself concedes CRA's 10-year tail is about update availability, not personal-data retention, making the contradictory label scope-incorrect); GDPR↔AI_Act, was CONTRADICTORY (direction) → COMPLEMENTARY (floor-within-ceiling) — the AI Act ≥6-month floor is a subset of GDPR's "no longer than is necessary" envelope), scope overlap matrix, Objective/Considerations content, data-class divergence (personal data / update artefacts / AI logs), obligation-direction divergence (GDPR ceiling / CRA floor / AI Act floor), CRA 10-year tail is on update artefacts NOT on personal data (separation-architecture layering rule), AI Act 6-month floor is a floor-within-ceiling not a standalone obligation, CRA Art. 13(9) twin-anchor pattern, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA, AI Act (3 of 5 regs — NIS 2 and DORA are out-of-scope per AEGIS taxonomy §4.1 — DORA Art. 12(1) backup policies specify scope and frequency but do not impose retention/archiving obligations as such; GDPR is the dedicated authority for retention; CRA addresses the distinct update-availability tail; AI Act addresses the distinct AI-log minimum floor). CRDA-deep verified 3 pairs as 1 SAME (DIFFERENT-PERSPECTIVE) + 2 CORRECTED. The three regulators target **distinct data classes** with **distinct obligation directions** (ceiling vs floor vs floor), and the high-level SO surfaces the common retention/archiving duty as a **3-axis layering rule** — GDPR ceiling on personal data + AI Act ≥6-month floor on AI logs + CRA 10-year availability tail on update artefacts — with explicit axis-segregated hand-offs and separation-architecture requirement where regimes overlap on a single data flow.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 5.2
  volere_section: 15
  volere_subtype: privacy
  title: "Data retained for the period required to satisfy its declared purpose — 3-axis retention/archiving architecture (GDPR ceiling + AI Act floor + CRA availability tail) with separation architecture where regimes overlap"
  derives_from:
    hso_sub_so: SO-D-05.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.2.md
    objective_ref_section: "### D-05.2.0"
  description: |
    The product shall retain data — across the three in-scope data classes (personal data, update artefacts, AI logs) — for a period that satisfies the 3-axis layering rule: GDPR Art. 5(1)(e) `no longer than is necessary` qualitative ceiling on personal data (controller-side, Art. 30(1)(f) RoPA time-limits + Art. 89(1) safeguards for the public-interest/research/statistical carve-out); AI Act Art. 19(1) ≥6-month floor on high-risk AI system logs (provider-side, with `appropriate to the intended purpose` upward adjustment); CRA Art. 13(8) 5-year support-period floor + Art. 13(9) 10-year-or-remainder-of-support-period update-availability tail + Art. 13(18) 10-year Annex II information accessibility on update artefacts (manufacturer-side, floor), with documented retention rationale per data class and a separation-architecture requirement (pseudonymisation, separate retention rules, separate storage paths) where regimes overlap on a single data flow, as the common retention/archiving duty converging across GDPR Art. 5(1)(e) + Art. 89(1), CRA Annex I Part II (7)/(8) + Art. 13(8)/(9)/(18), and AI Act Art. 19(1), where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A 3-axis retention/archiving architecture is operated with explicit axis-segregated hand-offs at the personal-data / update-artefact / AI-log surfaces; each data class has a documented retention rationale (declared purpose + retention period + erasure trigger + safeguard posture) per ID.AM-03 data-inventory substrate + PR.DS-12 risk-strategy-bound retention schedules; the GDPR Art. 5(1)(e) `no longer than is necessary` ceiling is enforced on personal data with the Art. 30(1)(f) RoPA envisages-time-limits-for-erasure documented per category and the Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) applied when longer retention is permitted for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the AI Act Art. 19(1) ≥6-month floor is enforced on high-risk AI system logs with the `appropriate to the intended purpose` upward adjustment documented and justified beyond the 6-month floor (operative retention range is [6 months, "necessary"] with AI Act setting the floor and GDPR setting the cap when logs contain personal data); the CRA Art. 13(8) 5-year support-period floor and Art. 13(9) 10-year-or-remainder-of-support-period update-availability tail are enforced on update artefacts (firmware, patches, advisories) and Annex II information with the twin-anchor pattern (the longer of 10 years from issue date or the remainder of the support period applies per update — R2 reading); the CRA 10-year tail is on update artefacts and Annex II information NOT on personal data; where regimes overlap on a single data flow (a CRA update-distribution log containing personal data; an AI log containing personal data), separation architecture (pseudonymisation of the personal-data subset, separate retention rules, separate storage paths) is the controlled hand-off; verified by 3-axis retention-policy documentation review + per-class retention-rationale audit + Art. 5(1)(e) ceiling-enforcement records inspection... (line truncated to 2000 chars)
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-12, ID.AM-03, PR.PS-02, PR.PS-04, GV.PO-02, GV.OV-02, GV.OC-04]
  applicable_if:
    regs: [GDPR, CRA, AI_ACT]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping data classes on the same party AND the floor-within-ceiling or separation-architecture layering rule engages; see HSO scope-overlap principle
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The three participating regulations impose distinct data-class obligations on a common substantive retention/archiving duty with three distinct obligation directions: GDPR's controller-side personal-data retention ceiling (Art. 5(1)(e) `no longer than is necessary` VAG upper limit); CRA's manufacturer-side update-artefact availability floor (Art. 13(8) 5-year support period + Art. 13(9) 10-year update-availability tail + Art. 13(18) 10-year Annex II information accessibility); AI Act's provider-side AI-log retention minimum floor (Art. 19(1) ≥6 months). The three obligation directions jointly form the 3-axis layering rule (ceiling + floor + floor) that constrains the retention/archiving architecture on a single party across all three regulators. The 1 conditional emergent tension (3-way retention/obligation interaction when CRA update logs or AI logs contain personal data) is regulated by two layering rules: separation architecture for the CRA↔GDPR overlap; floor-within-ceiling for the AI Act↔GDPR overlap. The high-level SO surfaces the common retention/archiving duty as the 3-axis layering rule; the per-reg data class, obligation direction, trigger, anchor, lifecycle stage, recipient, and evidence template is preserved verbatim in the three sub-SOs. (Copied from the HSO Considerations block of `### D-05.2.0`; preserved here for self-contained traceability.)
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-05.2
title: D-05.2 Retention & Archiving — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.2 Retention & Archiving
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
status: DRAFT
---
> **Deep analysis:** [D-05.2 Retention & Archiving](../../DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md)
#### D-05.2 Retention & Archiving
<!-- participants: GDPR, CRA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-017 | Personal data kept no longer than necessary; longer only where lawful and Art. 89(1) safeguards in place (Art. 5(1)(e) + Art. 30(1)(f)) | Personal data; storage limitation |
| NIS2 | — | Out-of-scope (sole authority: GDPR) | n/a |
| CRA | SO-CRA-035 | Security updates and advisories remain available across support period + 10-year update-availability tail (Art. 13(9) + Annex I Part II (7)/(8)) | Product updates; support-period continuity |
| DORA | — | Out-of-scope (sole authority: GDPR) | n/a |
| AI_Act | SO-AIACT-006 | High-risk AI system logs retained for ≥6 months aligned with intended purpose, unless Union/national law provides otherwise (Art. 19(1)) | AI logs; minimum floor |
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.2 per AEGIS taxonomy §4.1 — DORA Art. 12(1) backup policies specify scope and frequency but do not impose retention/archiving obligations as such. GDPR is the dedicated authority for retention; CRA addresses the distinct update-availability tail; AI Act addresses the distinct AI-log minimum floor.
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,CRA,AI_Act -->
- **Three-direction retention/obligation interaction.** GDPR says *upper limit*; AI Act says *lower floor for AI logs*; CRA says *lower floor for update artefacts*. The pairwise readings (GDPR↔CRA, GDPR↔AI_Act, CRA↔AI_Act) each handle two of the three directions, but the *non-pairwise observation* is that a single data stream (e.g., update logs from a CRA-classified high-risk AI) may need to satisfy all three simultaneously. Phase 2 must produce a retention-policy template that: (1) sets the AI Act 6-month floor as a hard minimum for AI logs; (2) caps retention at the GDPR "necessary" boundary; (3) ensures CRA update artefact availability is decoupled from personal-data retention via separation architecture.
<!-- /emergent -->
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **PR.DS-12** (Data disposal managed) and **ID.AM-03** (Asset inventory prioritised). GDPR SR-GDPR-029 maps both. CRA SR-CRA-016 maps PR.PS-02 (Software is patched) and GV.OV-02 (Organisational priorities established). AI Act SR-AIACT-008 maps PR.PS-04 (Adequate resource capacity) and GV.PO-02 (Organisational policy established). The CSF 2.0 surface is consistent; the architectural separation (update artefact availability vs log retention vs personal-data retention) is not separately enumerated by CSF and is a regulatory-orchestration concern.
##### Downstream implication
Phase 2 obligation derivation must produce a 3-axis retention policy: (1) GDPR ceiling (upper limit, Art. 5(1)(e)), (2) AI Act floor (≥6 months for high-risk AI logs), (3) CRA availability tail (10 years for security updates). For high-risk AI products that are CRA-classified and process personal data, all three apply; the policy must explicitly decouple CRA update artefact availability from personal-data retention. Phase 3 case generation must validate the separation architecture in case companies.
---
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-05.2
title: D-05.2 Retention & Archiving — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.2 Retention & Archiving
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
status: DRAFT
---
> **Domain analysis:** [D-05.2 Retention & Archiving](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md)
#### D-05.2 Retention & Archiving
<!-- participants: GDPR, CRA, AI_Act -->
**Participants (from CRDA):** GDPR, CRA, AI_Act
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.2 per AEGIS taxonomy §4.1 — DORA Art. 12(1) backup policies specify scope and frequency but do not impose retention / archiving obligations as such. GDPR is the dedicated authority for retention; CRA addresses the distinct update-availability tail; AI Act addresses the distinct AI-log minimum floor.

