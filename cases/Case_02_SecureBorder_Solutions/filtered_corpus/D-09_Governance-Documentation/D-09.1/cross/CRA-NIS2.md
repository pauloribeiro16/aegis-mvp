# D-09.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(a) + Art. 21(2)(f) + Art. 24):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (a) policies on risk analysis and information system security; … (f) policies and procedures to assess the effectiveness of cybersecurity risk-management measures." — Art. 21(2)(a)+(f) NIS 2
> "Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems …" — Art. 24(1) NIS 2 (per SR-NIS2-043)

**CRA article (verbatim, Art. 27(1)/(2)/(5)/(8)/(9)):**
> [as quoted above]

**Scope comparison:**
- NIS 2 scope: entity-level risk-analysis policy + IS-security policy + effectiveness-assessment policy.
- CRA scope: manufacturer-side presumption-of-conformity machinery via harmonised standards / common specifications / CSA certification.
- Scope overlap: **N (typically)** — different actors (entity vs. manufacturer).

**Trigger comparison:**
- NIS 2 trigger: entity adoption of policies.
- CRA trigger: manufacturer conformity-assessment procedure.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- NIS 2: no quantitative cadence.
- CRA: support period + 10-year accessibility.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: MSA.

**Content template comparison:**
- NIS 2: not codified for content.
- CRA: presumption-of-conformity machinery.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 mandates the policy artefact; CRA provides the presumption-of-conformity machinery that the NIS 2 entity can rely on when procuring CRA-conformant products. The CRA presumption substitutes for parts of the NIS 2 supplier-assessment obligation.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the entity procures CRA-conformant products; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a NIS 2 entity-side stack with CRA presumption-of-conformity as upstream gate: NIS 2 Art. 21(2)(a)+(f) policy artefacts + CRA Art. 27 presumption-of-conformity as substitute for supplier-assessment evidence.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-035, Art. 21(2)(a); SR-NIS2-036, Art. 21(2)(a); SR-NIS2-037, Art. 21(2)(f)) | Risk-analysis policy + IS-security policy + effectiveness-assessment policy. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-035 / SR-NIS2-036 / SR-NIS2-037 |
| **CRA** (SR-CRA-077, Art. 27(1)/(2)/(5); SR-CRA-078, Art. 27(8)/(9)) | Presumption of conformity via harmonised standards / common specs / CSA certification. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-077 / SR-CRA-078 |

**Why complementary**: NIS 2 mandates the policy artefact; CRA provides the presumption-of-conformity machinery that the NIS 2 entity can rely on when procuring CRA-conformant products. The CRA presumption substitutes for parts of the NIS 2 supplier-assessment obligation.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_