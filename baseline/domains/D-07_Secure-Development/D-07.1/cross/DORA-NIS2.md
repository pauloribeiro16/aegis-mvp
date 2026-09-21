# D-07.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim, Art. 21(2)(e)):**
> [as quoted above]

**DORA article (verbatim, Art. 9(4)(e)):**
> "Financial entities shall … (e) implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … that are based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner." — Art. 9(4)(e) DORA

**Scope comparison:**
- NIS 2 scope: entity-level security of NIS across acquisition, development, maintenance.
- DORA scope: financial-entity ICT change management (six-step process).
- Scope overlap: **Y (when a DORA financial entity is also an NSIE — both apply).**

**Trigger comparison:**
- NIS 2 trigger: lifecycle activity on NIS.
- DORA trigger: ICT change event (software/hardware/firmware/system/security-parameter change).
- Trigger alignment: **PARTIAL** (NIS 2 development/maintenance phase overlaps DORA change-management six-step).

**Threshold/timeline comparison:**
- NIS 2: no quantitative threshold.
- DORA: no quantitative threshold for change cadence; six-step process mandatory.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- DORA: management body, competent authority.

**Content template comparison:**
- NIS 2: not codified for content.
- DORA: documented change-management policy with six-step process.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 mandates lifecycle security as a continuous obligation; DORA mandates the change-management six-step that operationalises the maintenance phase. NIS 2 financial-entity coverage is light in this domain (financial entities under DORA are NSIEs partially, but DORA's dedicated obligations dominate). The two regimes meet at the maintenance phase: NIS 2 Art. 21(2)(e) maintenance-phase security requirements are operationalised through DORA Art. 9(4)(e) six-step process.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when a DORA financial entity is also an NSIE applying maintenance-phase controls)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 9(4)(e) six-step process discharges both DORA's dedicated change-management obligation and NIS 2's maintenance-phase security requirement.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-026, Art. 21(2)(e) acquisition; SR-NIS2-027, Art. 21(2)(e) development; SR-NIS2-028, Art. 21(2)(e) maintenance) | Entity-level lifecycle security. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-026 / SR-NIS2-027 / SR-NIS2-028 |
| **DORA** (SR-DORA-004, Art. 9(4)(b)+(f) — partial; SR-DORA-023, Art. 9(4)(e) — D-07.4) | Network/infrastructure mgmt + change-management operationalises secure-by-design dimension. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-004 / SR-DORA-023 |

**Why complementary**: NIS 2 mandates lifecycle security as a continuous obligation; DORA mandates the change-management six-step process (recorded/tested/assessed/approved/implemented/verified) that operationalises the maintenance phase. NIS 2 financial-entity coverage is light in this domain (financial entities under DORA are NSIEs partially, but DORA's dedicated obligations dominate).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

