# D-05.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 5(1)(e) + Art. 30(1)(f)):**
> "Personal data shall be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed ('storage limitation'). Personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89(1) subject to implementation of the appropriate technical and organisational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject." — Art. 5(1)(e) GDPR
>
> "Each controller … shall maintain a record of processing activities under its responsibility … that contains … where possible, the envisaged time limits for erasure of the different categories of data." — Art. 30(1)(f) GDPR

**CRA article (verbatim, Annex I Part II (7)/(8) + Art. 13(8)/(9)):**
> "Securely distribute updates … to the users of products with digital elements, in a timely manner, including, where appropriate, through automatic updates." — CRA Annex I Part II (7)
>
> "Ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take." — CRA Annex I Part II (8)
>
> "Where, after placing a product with digital elements on the market, the manufacturer becomes aware of a vulnerability affecting the security of the product, the manufacturer shall, without delay, disclose the vulnerability and any associated mitigations to the person or entity maintaining the product, where applicable, and to the market surveillance authorities, as well as, where the manufacturer becomes aware of an actively exploited vulnerability, to the users of the product." — CRA Art. 13(9) (vulnerability disclosure — adjacent but distinct from update availability)

(Note: the CRDA reasoning invokes a "10-year update-availability tail" derived from CRA Art. 13(18) + Annex I Part II (7)/(8) supporting-period accessibility, while the OJ literal anchor is the support-period floor of Art. 13(8) (5-year minimum) + the 10-year accessibility for Annex II information under Art. 13(18). The substantive distinction is that CRA's obligation is on *update artefacts* (firmware, patches, advisories) made available by the manufacturer — not on personal-data retention.)

**Scope comparison:**
- GDPR scope: personal data held by the controller.
- CRA scope: security-update artefacts (firmware, patches, advisories) made available by the manufacturer.
- Scope overlap: **N (typically)** — different data classes (personal data vs update artefacts).

**Trigger comparison:**
- GDPR trigger: continued storage of personal data beyond processing-purpose end.
- CRA trigger: ongoing availability of security updates across support period.
- Trigger alignment: **DIFFERENT** — retention vs availability.

**Threshold/timeline comparison:**
- GDPR: no quantitative upper bound; "no longer than is necessary" is qualitative.
- CRA: support period is at least 5 years (Art. 13(8) CRA — the OJ-literal anchor); Annex II information must remain accessible for at least 10 years after placing on the market (Art. 13(18)). CRDA's "10-year tail" reading collapses these two provisions; the operative substance is "support period + 10-year information accessibility".
- Tension: **NONE — the scopes are disjoint.** The CRDA reasoning itself notes: "CRA's 10-year tail is about *update availability*, not personal-data retention … if a CRA-compliant product retains update-related logs containing personal data for 10 years, the GDPR retention ceiling may be violated."

**Recipient comparison:**
- GDPR: data subject + supervisory authority (DPA).
- CRA: market surveillance authority (MSA) + users.

**Content template comparison:**
- GDPR: not codified; documented in RoPA (Art. 30(1)(f) "envisaged time limits for erasure").
- CRA: not codified; documented in Annex VII §3 risk-assessment record + Annex II information deliverable.

**Classified relationship (from CRDA):** CONTRADICTORY (direction)
**Verified relationship (after OJ-text analysis):** **CORRECTED — SCOPE-DISJOINT**
**Reasoning:** The CRDA reasoning explicitly concedes: "These are not on the same axis (CRA's 10-year tail is about *update availability*, not personal-data retention)." With that concession, the "contradictory" label is internally inconsistent. Two regulations imposing limits on different data classes at different actors are **scope-disjoint**, not contradictory. A true contradiction requires mutually exclusive obligations on the same data at the same actor. There is no such overlap here: GDPR Art. 5(1)(e) caps the retention of *personal data*; CRA Annex I Part II (7)/(8) requires *update artefact* availability. If a CRA product's update-distribution logs contain personal data, the controller must decouple the log retention from the update availability via separation architecture — but that is a layering rule, not a contradiction.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when a CRA update-distribution log contains personal data, the controller must apply GDPR Art. 5(1)(e) to the personal data portion; CRA Annex I Part II (7)/(8) applies to the artefact portion independently).** In the typical case (pure update artefacts with no personal data), there is no overlap. The pair is therefore scope-disjoint in baseline.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must correct CRDA's "contradictory" label to "scope-disjoint" with separation-architecture requirement. The 3-axis retention policy (GDPR ceiling + CRA availability + AI Act floor) is correct as a *layering* rule, but the CRDA label "contradictory" is scope-incorrect. Phase 3 case generation must validate that CRA-regulated products with personal-data-containing update logs apply separation architecture (pseudonymisation, separate retention rules) to honour both regimes.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-029, Art. 5(1)(e) + Art. 30(1)(f)) | Documented retention limits with erasure at purpose end |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-029 |
| **CRA** (SR-CRA-016 + SR-CRA-047, Art. 13(9) + Annex I Part II (7)/(8)) | 10-year update-availability tail beyond support period + free timely dissemination |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-016, SR-CRA-047 |

**Why contradictory (direction)**: GDPR imposes an upper limit on retention (no longer than necessary); CRA imposes a 10-year *minimum* availability of security updates. These are not on the same axis (CRA's 10-year tail is about *update availability*, not personal-data retention), but if a CRA-compliant product retains update-related logs containing personal data for 10 years, the GDPR retention ceiling may be violated. Phase 2 must surface this tension: CRA's 10-year tail applies to *update artefact availability*; GDPR's ceiling applies to *personal-data retention*. The intersection (update logs containing personal data) requires a separation architecture.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
49 lines — see ../../_migration_report.md)_