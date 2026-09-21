# D-09.4 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 30(1)–(4) + Art. 12-14):**
> "Each controller … shall maintain a record of processing activities under its responsibility … Such record shall contain … where possible, the envisaged time limits for erasure of the different categories of data …" — Art. 30(1) GDPR
> "Each processor … shall maintain a record of all categories of processing activities carried out on behalf of a controller …" — Art. 30(2) GDPR
> "The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form …" — Art. 30(3) GDPR

**NIS2 article (verbatim, Art. 24(1)/(2)/(3)):**
> "Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems …" — Art. 24(1) NIS 2 (per SR-NIS2-043)

**Scope comparison:**
- GDPR scope: controller/processor RoPA mandate with 250-employee exception.
- NIS 2 scope: certification-driven recordkeeping (Art. 24) — not a RoPA-equivalent.
- Scope overlap: **N (typically)** — different record types.

**Trigger comparison:**
- GDPR trigger: processing of personal data.
- NIS 2 trigger: certification requirement (where Member State or Commission delegated act so requires).
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: 250-employee carve-out; retention until processing ceases + on SA request.
- NIS 2: per Member State.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: Art. 30(1)/(2) content items.
- NIS 2: not codified (certification-driven).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR RoPA is processing-activities-focussed; NIS 2 Art. 24 is certification-driven. Different record types; no substantive overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different record types, different triggers. Substantively scope-disjoint.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records. No OJ-level consolidation.

---


## Summary (Domain Analysis)

| GDPR ↔ NIS2 | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-048, Art. 30(1)-(4); SR-GDPR-050, Art. 30(3) integrity; SR-GDPR-065-068, Art. 12-14 transparency) | RoPA + supervisory-authority access + transparent privacy notices + data-subject rights. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-048 / SR-GDPR-050 / SR-GDPR-065-068 |
| **NIS2** (SR-NIS2-043, Art. 24(1)/(2)/(3) — partial) | Use of certified ICT products/services/processes. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-043 |

**Why different-perspective**: GDPR RoPA is processing-activities-focussed; NIS 2 Art. 24 is certification-driven. Different record types; no substantive overlap.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

