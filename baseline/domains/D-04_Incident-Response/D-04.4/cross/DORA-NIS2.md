# D-04.4 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2)(c) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management (OJ L 333, 27.12.2022, p. 127).

**DORA article (verbatim):**
> Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a) continue critical operations, (b) recover from ICT-related incidents, (c) manage crises, (d) protect stakeholders, and (e) comply with regulatory obligations.
> [OJ-corrective note (v0.2 audit, material): Art. 11(2)(c)/(d)/(e) — BCP objectives mislabelled. OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) (manage crises, protect stakeholders, comply with regulatory obligations) do NOT match the OJ items.]

**Scope comparison:**
- NIS2 scope: generic BC/backup/DR/crisis-management measures for essential/important entities.
- DORA scope: financial-entity ICT business continuity, response/recovery plans, audit review, backup policies and restoration methods.
- Scope overlap: Conditional where both apply to the same financial entity and function.

**Trigger comparison:**
- NIS2 trigger: continuous BC/DR/CM obligation.
- DORA trigger: continuous ICT BC obligation plus incident-driven response/recovery activation.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate BC/DR/CM, no detailed backup frequency formula in the quoted clause.
- DORA: documented arrangements and plans; backup scope/frequency based on criticality or confidentiality; independent audit review for non-microenterprises.
- Tension: NONE.

**Recipient comparison:**
- NIS2: NIS competent authority/CSIRT evidence path.
- DORA: financial competent authority evidence path.

**Content template comparison:**
- NIS2: BC, backup, disaster recovery and crisis management evidence.
- DORA: ICT BC policy, response/recovery plans, audit reviews, backup policies and restoration methods.

**Classified relationship (from CRDA):** EQUAL

**Verified relationship (after OJ-text analysis):** CORRECTED — COMPLEMENTARY, DORA-specific overlay

**Reasoning (1-2 paragraphs):** The OJ text and DORA corrective note show that equality is too strong. DORA is not merely the same BC/DR obligation as NIS2; it has a financial-sector-specific BC architecture with explicit arrangements, response/recovery plans, backup-frequency criteria and audit expectations. It also contains material source-file caveats on the correct Art. 11(2)(a)–(e) objective list.

The verified relationship is complementary: NIS2 provides the generic entity BC/DR/CM floor; DORA adds a more detailed financial-sector layer. A DORA-compliant programme may satisfy NIS2 for the overlapping ICT subset, but that is not equality of obligations.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: equality as a baseline is overbroad; overlap must be established by entity and sector scope.

**Downstream implication (1-2 sentences):** Doc 07 should use DORA as the detailed financial-sector implementation layer, while preserving NIS2 as the broader BC/DR/CM requirement where it remains applicable.


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-019, Art. 21(2)(c)) | BC + backup + DR + CM triad |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-019 |
| **DORA** (SR-DORA-013 + SR-DORA-014 + SR-DORA-015, Art. 11(1)–(3) + Art. 12(1)) | Comprehensive BC policy + dedicated arrangements + backup policies with criticality/confidentiality basis + restoration procedures |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-014, SR-DORA-015 |

**Why equal (DORA exceeds)**: DORA's BC framework is the NIS2 BC triad with an additional specificity layer (independent internal audit for non-microenterprises; criticality/confidentiality-basis backup scoping). A financial entity implementing DORA exceeds NIS2's BC requirement.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_