# D-06.4 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 27(1)):**
> (See GDPR↔CRA pair above for the verbatim text.)

**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> "Where the contractual arrangements concern critical or important functions, the contractual arrangements shall, in addition to the elements set out in paragraph 2, include the following: … (e) the rights of the financial entity and the competent authority to obtain, from the ICT third-party service provider, unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … including the right to take copies of relevant documentation on-site if critical to the operations of the ICT third-party service provider, the effective exercise of which is not impeded or limited by other contractual arrangements or implementation policies. The right to agree on alternative assurance levels if other clients' rights are affected shall be allowed." — DORA Art. 30(3)(e)(i)+(ii)

**Scope comparison:**
- GDPR scope: EU representative designation for non-EU controller / processor.
- DORA scope: audit rights over critical ICT third-party providers (CIF-only).
- Scope overlap: **N — different mechanisms (legal-address vs audit rights).** They overlap when a non-EU ICT third-party provider is critical / important for a financial entity.

**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- DORA: CIF-only.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA.
- DORA: financial entity + competent authority.

**Content template comparison:**
- GDPR: written representative designation.
- DORA: Art. 30(3)(e)(i) audit-rights clause in CIF-supporting contracts.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR Art. 27 is a *legal-address* obligation (representative must be EU-based, mandate in writing); DORA Art. 30(3)(e) is a *rights* obligation (audit + inspection + on-site copy rights). Different mechanisms: GDPR = designate, DORA = assert audit rights. Both apply when a non-EU ICT third-party provider is critical / important for a financial entity.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms.** Conditional overlap when a non-EU ICT third-party provider is critical / important for a financial entity.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) GDPR Art. 27 representative designation; (2) DORA Art. 30(3)(e) audit-rights clause for CIF contracts. The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

| GDPR ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-038, Art. 27) | EU representative for non-EU controllers/processors |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-038 |
| **DORA** (SR-DORA-022, Art. 30(3)(e)) | Unrestricted audit rights over critical ICT third-party providers |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-022 |

**Why different-perspective**: GDPR Art. 27 is a *legal-address* obligation (representative must be EU-based, mandate in writing); DORA Art. 30(3)(e) is a *rights* obligation (audit + inspection + on-site copy rights). Different mechanisms: GDPR = designate, DORA = assert audit rights. Both apply when a non-EU ICT third-party provider is critical/important for a financial entity.



