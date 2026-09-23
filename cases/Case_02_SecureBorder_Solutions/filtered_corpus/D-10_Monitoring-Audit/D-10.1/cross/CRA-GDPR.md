# D-10.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 32(2) + Art. 33(1)):**
> [as quoted above]

**CRA article (verbatim, Annex I Part I (2)(l) + Part II (6)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (l) provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user." — CRA Annex I Part I (2)(l) (per SR-CRA-100)
> "The manufacturer shall … (6) facilitate the sharing of information about potential vulnerabilities of the product with digital elements …" — CRA Annex I Part II (6)

**Scope comparison:**
- GDPR scope: entity-level monitoring (5 Art. 32(2) risk types).
- CRA scope: product-level on-device activity monitoring with user opt-out + vulnerability-reporting contact address.
- Scope overlap: **Y (when the CRA-regulated product processes personal data)**.

**Trigger comparison:**
- GDPR trigger: 5 Art. 32(2) risk types.
- CRA trigger: access/modification of data/services/functions + vulnerability reporting.
- Trigger alignment: **PARTIAL**.

**Threshold/timeline comparison:**
- GDPR: breach-`becoming-aware` 72h clock.
- CRA: support-period obligation.
- Tension: **GENUINE (CRA user opt-out vs. GDPR mandatory monitoring — see CRDA Layer 2 review flag)**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- CRA: MSA, users.

**Content template comparison:**
- GDPR: not codified for content.
- CRA: Annex VII §6 test reports + Annex VII §2(b) CVD policy.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY** (with CRDA-flagged Layer 2 conflict on user opt-out vs. mandatory monitoring)
**Reasoning:** GDPR monitoring is entity-level; CRA monitoring is product-level with user opt-out. The two regimes meet at the controller-manufacturer interface. **CRITICAL CONFLICT (Layer 2 review):** CRA Annex I Part I (2)(l) allows user opt-out from on-device activity monitoring; GDPR Art. 32(2) monitoring is mandatory for the 5 risk types; DORA Art. 8(1) monitoring is mandatory. For a CRA-regulated product processing personal data, the CRA user opt-out conflicts with the GDPR mandatory monitoring. The OJ does not resolve this conflict.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the CRA-regulated product processes personal data)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must surface the CRA user opt-out vs. GDPR mandatory monitoring conflict for Layer 2 review. The two regimes can stack, but the user's opt-out from CRA monitoring may not legally exempt the controller from GDPR Art. 32(2) mandatory detection — the conflict requires OJ-level resolution.

---
