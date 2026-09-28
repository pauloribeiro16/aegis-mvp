# D-04.4 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.

**DORA article (verbatim):**
> Art. 12(1)(a) requires financial entities to develop and document backup policies and procedures specifying the scope of the data subject to backup and the minimum frequency of backup, based on the criticality of information or the confidentiality level of the data. Art. 12(1)(b) requires restoration and recovery procedures and methods.

**Scope comparison:**
- GDPR scope: personal-data restoration.
- DORA scope: financial-entity backup, restoration and recovery procedures for ICT data and critical functions.
- Scope overlap: Conditional where the financial entity processes personal data.

**Trigger comparison:**
- GDPR trigger: physical or technical incident affecting personal-data availability/access.
- DORA trigger: continuous BC/backup duty and incident-driven restoration process.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: timely manner.
- DORA: documented backup scope and minimum frequency based on criticality or confidentiality, plus restoration/recovery procedures.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority evidence if inspected.
- DORA: financial competent authority evidence.

**Content template comparison:**
- GDPR: recovery capability and timely restoration evidence.
- DORA: backup policy, minimum frequency, restoration/recovery methods and test evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** DORA is more specific operationally, but it does not contradict GDPR. For financial entities, DORA supplies the concrete backup and restoration architecture that can operationalise GDPR's open-textured timely-restoration requirement.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradiction claim would be scope-incorrect; CRDA classified this pair as complementary.

**Downstream implication (1-2 sentences):** Doc 07 should allow DORA Art. 12 backup tiers to serve as the measurable implementation of GDPR Art. 32(1)(c) where personal data are in scope.


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-024, Art. 32(1)(c)) | Timely availability restoration |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-024 |
| **DORA** (SR-DORA-013 + SR-DORA-014 + SR-DORA-015, Art. 11(1)–(3) + Art. 12(1)) | BC policy + dedicated arrangements + backup policies (scope and frequency on criticality/confidentiality) + restoration procedures |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-014, SR-DORA-015 |

**Why complementary (DORA exceeds GDPR)**: DORA explicitly specifies the BC framework (Art. 11), the backup scope/frequency on criticality/confidentiality (Art. 12(1)(a)), and the restoration procedures (Art. 12(1)(b)). For a financial entity, DORA's Art. 12 supersedes GDPR's VAG `timely` anchor with a concrete backup-and-restore architecture.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_