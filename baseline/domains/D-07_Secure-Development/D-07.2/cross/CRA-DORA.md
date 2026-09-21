# D-07.2 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Annex I Part I (2)(j) + (2)(k)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (j) limit its attack surfaces, including attack surfaces of external interfaces … (k) reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques." — CRA Annex I Part I (2)(j)+(k)

**DORA article (verbatim, Art. 9(4)(e)):**
> [as quoted in NIS2 ↔ DORA above]

**Scope comparison:**
- CRA scope: product-level outcome mandates (limit attack surfaces, exploit mitigation).
- DORA scope: financial-entity ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified).
- Scope overlap: **N (typically)** — CRA addresses product-level coding outcomes; DORA addresses entity-level process.

**Trigger comparison:**
- CRA trigger: product design / development (Annex I Part I chapeau).
- DORA trigger: ICT change event (software/hardware/firmware/system/security parameter change).
- Trigger alignment: **DIFFERENT** (product design vs. entity change).

**Threshold/timeline comparison:**
- CRA: no quantitative threshold; Annex I (2)(j) `(k)` qualitative.
- DORA: no quantitative cadence; six-step mandatory.
- Tension: **NONE (scope-disjoint)**.

**Recipient comparison:**
- CRA: MSA.
- DORA: NCA, management body.

**Content template comparison:**
- CRA: Annex VII §2 design/development documentation + risk-assessment record (§3).
- DORA: documented change-management policy.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY** (CRDA classification preserved; but see P0 disagreement on DORA OJ-text support for D-07.2)
**Reasoning:** CRA Annex I Part I (2)(j)+(k) specifies product-level outcomes (attack-surface reduction, exploitation mitigation). DORA Art. 9(4)(e) specifies entity-level process (change-management six-step) but does not prescribe coding standards. The two regimes do not overlap substantively on coding practices — CRA covers the product, DORA covers the process. No DORA SR exists for D-07.2 from OJ-literal text (the SR-DORA-007 audit confirms Art. 9(4)(f) is patch-management policy, not coding standards).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different objects (product coding outcomes vs. entity change process), different actors (manufacturer vs. financial entity). Pair is scope-disjoint in the OJ-literal reading; CRDA's "complementary" label is more a taxonomy artifact than a substantive relationship.

**Downstream implication (Phase 1C Doc 07):** Phase 1 entities must NOT treat DORA as a coding-standards authority absent OJ-text evidence (see P0 disagreement). Coding-standards baseline must be built from industry frameworks (NIST SSDF, OWASP SAMM, ISO 27034) and demonstrated against each regulation's outcome (CRA) or process (DORA) requirement.

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-067, Annex I Part I (2)(j) attack-surface; SR-CRA-068, Annex I Part I (2)(k) exploitation mitigation) | Outcome-level: limit attack surfaces, deploy exploitation mitigation. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-067 / SR-CRA-068 |
| **DORA** (SR-DORA-023, Art. 9(4)(e) — partial, no OJ mandate for D-07.2) | Six-step change management; secure-coding coverage is by inference only. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-023 |

**Why complementary**: CRA specifies the product-level outcome (attack-surface limitation, exploitation mitigation); DORA specifies the entity-level process (change-management six-step) but does not prescribe coding standards. The two regimes do not overlap substantively on coding practices — CRA covers the product, DORA covers the process; no DORA SR exists for D-07.2 from OJ-literal text.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

