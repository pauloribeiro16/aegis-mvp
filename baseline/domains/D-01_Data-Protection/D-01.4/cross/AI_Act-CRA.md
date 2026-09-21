# D-01.4 — Pair analysis: CRA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim — SR-CRA-005, Annex I Part I (2)(f) + (l)):**
> Annex I Part I (2)(f) protect the integrity of stored, transmitted or otherwise processed data — personal or other — as well as the integrity of commands, programs and configuration against any manipulation or modification not authorised by the user.

**AI Act article (verbatim — SR-AIACT-015, Art. 15(3)):**
> Art. 15(3) … as resilient as possible regarding errors, faults or inconsistencies … technical redundancy solutions, which may include backup or fail-safe plans.

**Scope comparison:**
- CRA: integrity of data + commands + programs + configuration (universal).
- AI Act: AI-system resilience to errors/faults/inconsistencies (system-level).
- Scope overlap: Y when a CRA-regulated product is also a high-risk AI system (edge-AI device scenario).

**Trigger comparison:**
- CRA: continuous + corruption-event.
- AI Act: continuous + lifecycle.
- Trigger alignment: SAME on continuous.

**Threshold/timeline comparison:**
- CRA: "any manipulation" (universal).
- AI Act: "as resilient as possible" (state-of-the-art per SR-AIACT-015 R3).
- Tension: NONE — different objects (storage integrity vs system resilience).

**Recipient comparison:**
- CRA: user.
- AI Act: conformity-assessment body + MSA.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — no change).

**Reasoning:** CRA's universal-quantifier integrity protection is the storage/perimeter leg; AI Act's resilience is the AI-system leg above it. A CRA-regulated product that is also a high-risk AI system has both layers. The CRA-AI Act deemed-compliance bridge (CRA Art. 12) provides a one-way shortcut for high-risk AI satisfying CRA Annex I.

**Scope-disjoint test:** Y for the integrated edge-AI product.

**Downstream implication:** Stack-merge with CRA-AI Act deemed-compliance bridge. CRA-Compliant product + Art. 15(3) backup/fail-safe plans + Art. 15(1) accuracy/robustness/cybersecurity 3-way AND on the AI layer.

---


## Summary (Domain Analysis)

| CRA ↔ AI_Act | **Complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-005, Annex I Part I (2)(f)+(l)) | Integrity of data + commands + programs + configuration; corruption reported | Product-level; PR.DS-01 + PR.DS-10 + PR.PS-04 |
| **AI_Act** (SR-AIACT-014 + SR-AIACT-015, Art. 15(1)+(3)) | Accuracy + robustness + cybersecurity; resilience via backup/fail-safe | High-risk AI provider; AI-system-level; PR.IR-03 + PR.IR-04 + PR.DS-11 |

**Why Complementary**: CRA's integrity obligation is universal ("any manipulation"); AI Act's resilience obligation is AI-system-specific and uses different CSF anchors (PR.IR-03 + PR.IR-04 + PR.DS-11). A CRA-regulated product that is also a high-risk AI system (e.g. an edge-AI device) is jointly bound; the CRA integrity protection + AI Act resilience satisfy the 3-way AND of accuracy/robustness/cybersecurity at the system level, with the AI-specific accuracy and robustness dimensions remaining provider obligations under AI Act. → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-005; `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 + SR-AIACT-015



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
39 lines — see ../../_migration_report.md)_

