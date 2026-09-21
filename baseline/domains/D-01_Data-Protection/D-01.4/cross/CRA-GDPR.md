# D-01.4 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim — SR-GDPR-005, Art. 5(1)(d) + Art. 5(1)(f)):**
> Art. 5(1)(d) personal data must be accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay.

**CRA article (verbatim — SR-CRA-005, Annex I Part I (2)(f) + (l)):**
> Annex I Part I (2)(f) protect the integrity of stored, transmitted or otherwise processed data — personal or other — as well as the integrity of commands, programs and configuration against any manipulation or modification not authorised by the user. The manufacturer shall also report on corruptions.

**Scope comparison:**
- GDPR: accuracy (semantic) of personal data + integrity of personal data.
- CRA: integrity of data + commands + programs + configuration (technical, universal-quantifier "any manipulation").
- Scope overlap: Y when CRA product handles personal data; the GDPR accuracy leg (semantic) is a controller obligation beyond CRA's technical-integration scope.

**Trigger comparison:**
- GDPR: continuous + on data-subject request (Art. 16 rectification) + on material change.
- CRA: continuous + corruption-event reporting (triggered on corruption).
- Trigger alignment: PARTIAL — CRA's corruption-reporting is event-triggered; GDPR's rectification is event-triggered (Art. 16 request) and continuous (Art. 5(1)(d) accuracy duty).

**Threshold/timeline comparison:**
- GDPR: Art. 5(1)(d) "without delay" (VAG; reading chosen: harmonised with Art. 16 "without undue delay").
- CRA: "without delay" not explicit on data integrity; "report corruptions" timing depends on the corruption event.
- Tension: NONE on threshold; CRA's "report corruptions" introduces an event-driven cadence that GDPR's accuracy duty does not match.

**Recipient comparison:**
- GDPR: SA + data subject (Art. 16).
- CRA: user / administering party (per SR-CRA-005 R1 reading; not an external authority).

**Content template comparison:**
- GDPR: Art. 16 rectification cascade + Art. 19 cascade to recipients.
- CRA: corruption reporting in Annex VII + Annex I (2)(l) logging.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** CRA's technical-integrity universal quantifier is the storage/protection leg; GDPR's semantic-accuracy + Art. 16 rectification cascade is the workflow + downstream leg. The two complement each other on the same data asset: CRA's PR.DS-01 + PR.DS-10 + PR.PS-04 satisfies the storage/technical leg; GDPR's Art. 16 + Art. 19 cascade satisfies the workflow/semantic leg. They are layered on the same data asset but at different layers, with PARTIAL trigger overlap (CRA corruption-event vs GDPR rectification-request).

**Scope-disjoint test:** Y on the same product handling personal data.

**Downstream implication:** Stack-merge with two layers. A CRA-compliant integrity/logging stack (cryptographic hashes + write-audit logging + corruption reports) discharges the GDPR Art. 5(1)(f) integrity leg; the controller separately operates the Art. 5(1)(d) accuracy + Art. 16 rectification workflow + Art. 19 cascade.

---


## Summary (Domain Analysis)

| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-005 + SR-GDPR-006, Art. 5(1)(d) + Art. 16) | Accuracy of stored personal data; rectification workflow with cascade propagation | Personal-data scope; accuracy (semantic) + integrity (storage); PR.DS-01 + PR.DS-10 + PR.DS-12 |
| **CRA** (SR-CRA-005, Annex I Part I (2)(f)+(l)) | Integrity of data, commands, programs, configuration; corruption reported | Product-level; "personal or other"; integrity as the universal quantifier "any manipulation or modification not authorised by the user"; PR.DS-01 + PR.DS-10 + PR.PS-04 |

**Why Complementary**: GDPR anchors integrity to two distinct principles (Art. 5(1)(d) accuracy — semantic; Art. 5(1)(f) integrity — storage) and Art. 16 rectification (cascade workflow). CRA anchors to a single clause covering data + commands + programs + configuration with a universal-quantifier "any manipulation" and a corruption-reporting obligation. The two are complementary: GDPR's accuracy dimension is semantic; CRA's integrity dimension is technical. A CRA product handling personal data is jointly bound; the CRA universal-quantifier integrity protection satisfies GDPR's Art. 5(1)(f) integrity leg, while GDPR's Art. 5(1)(d) accuracy leg remains a controller obligation. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-005 + SR-GDPR-006; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-005



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

