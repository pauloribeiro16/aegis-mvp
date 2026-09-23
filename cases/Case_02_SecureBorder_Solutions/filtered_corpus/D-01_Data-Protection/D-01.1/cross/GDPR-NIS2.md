# D-01.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim from SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(a)/(b)):**
> Art. 5(1)(f) integrity and confidentiality … processed in a manner that ensures appropriate security of the personal data … protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures. Art. 32(1)(b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

**NIS 2 article (verbatim from SR-NIS2-001, Art. 21(2)(h)):**
> Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption.

**Scope comparison:**
- GDPR scope: "personal data" (Art. 4(1) identifiability; pseudonymised data still in scope per CJEU Breyer and IAB Europe C-604/22).
- NIS 2 scope: "network and information systems" holding data that is "stored, transmitted or otherwise processed" (Art. 6(1)+(2)) — broader than personal data; includes operational, ICT-telemetry, business-confidential, and machine-generated data.
- Scope overlap: Y when the at-rest datastore holds personal data; Y (conditional) — typically the same storage holds both personal and non-personal data in modern stacks.

**Trigger comparison:**
- GDPR trigger: continuous obligation under Art. 5(1)(f) + Art. 32(1) (no event trigger; risk-anchored floor).
- NIS 2 trigger: continuous obligation under Art. 21(2)(h) + Art. 21(1) appropriate-and-proportionate.
- Trigger alignment: SAME (both continuous, both risk-anchored; no event-trigger divergence).

**Threshold/timeline comparison:**
- GDPR: "appropriate" anchored to the five Art. 32(1) preamble factors (state of the art, costs, nature, scope, context, purposes, risks).
- NIS 2: "where appropriate" anchored to the same Art. 21(1) preamble plus the "appropriate and proportionate" qualifier (state of the art, standards, cost, exposure, size, likelihood, severity).
- Tension: NONE — the two thresholds converge on risk-anchored proportionality; the NIS 2 "where appropriate" hedge admits a narrower scope than GDPR's "appropriate", but where NIS 2 is narrower, GDPR is stricter (always applicable to personal data).

**Recipient comparison:**
- GDPR: supervisory authority (Art. 58 enforcement); data subjects are notified on breach if Art. 34(1) high-risk threshold met (or carve-out under Art. 34(3)(a)).
- NIS 2: CSIRT or competent authority (Art. 23 reporting cascade); no direct data-subject notification.

**Content template comparison:**
- GDPR: technical-and-organis measures + accountability demonstrability under Art. 5(2).
- NIS 2: documented cryptography policy (SR-NIS2-001 title), with risk-anchored policy-and-procedure evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — terminology only, not substance).

**Reasoning (1-2 paragraphs):**
The OJ texts impose the same substantive obligation (encryption of data at rest where the risk assessment indicates) anchored to the same proportionality test (state of the art, risk factors). The two differ in (a) scope qualifier ("personal data" vs "network and information systems") — which makes NIS 2 broader; (b) anchor qualifier ("appropriate" vs "where appropriate") — which makes GDPR stricter for personal data; and (c) the GDPR-only existence of the Art. 34(3)(a) unintelligibility carve-out from data-subject notification. These are scope-depth and wording differences on a common obligation, not fundamentally different regulatory framings. CRDA's COMPLEMENTARY is consistent with this reading but understates the convergence: the two are best described as EQUIVALENT obligations on the same event (encryption at rest of personal data on a NIS 2 essential entity that is also a GDPR controller). The compliance population is the same party on the same artefact.

**Scope-disjoint test:** Y — the GDPR controller that is also a NIS 2 essential entity bears both obligations on the same datastore.

- If Y: the COMPLEMENTARY classification is correct; the practical reconciliation is stacked documentation (the GDPR Article 32 risk assessment doubles as the NIS 2 cryptography-policy risk rationale).

**Downstream implication (1-2 sentences):** For Phase 1C Doc 07, D-01.1 is a **stack-merge with documentation** sub-domain: a single at-rest encryption deployment (e.g. approved symmetric cipher with appropriate key custody under separate logical access) plus the joint Article 32 / Art. 21(2)(h) risk-assessment artefact discharges both obligations on a NIS 2 essential entity that is a GDPR controller.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-001, Art. 32(1)(a)/(b)) | Personal data confidentiality at rest with risk-anchored baseline; pseudonymisation renders data unintelligible on breach | Art. 5(1)(f) CIA; Art. 32 risk-based; data subject to GDPR scope (personal data) |
| **NIS2** (SR-NIS2-001, Art. 21(2)(h)) | Cryptography-policy obligation; "where appropriate" hedge for encryption; covers stored + transmitted + processed | Art. 6(2) CIA-A; appropriate-and-proportionate qualifier; scope = NIS (broader than personal data) |

**Why Complementary**: GDPR anchors at-rest encryption to a personal-data scope with a strict risk-based floor; NIS 2 anchors to a network-and-information-system scope with a "where appropriate" hedge. A DORA financial entity processing personal data is jointly bound by both: GDPR personal-data scope (narrower) plus NIS 2 system scope (broader). The two are compatible because GDPR's stricter floor (state-of-the-art via harmonised standards) satisfies NIS 2's "where appropriate" test. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-001; `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-001



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
46 lines — see ../../_migration_report.md)_