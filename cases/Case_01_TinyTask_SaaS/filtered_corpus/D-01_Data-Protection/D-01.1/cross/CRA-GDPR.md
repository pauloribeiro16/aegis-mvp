# D-01.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim from SR-GDPR-001, Art. 5(1)(f) + Art. 32(1)(a)):**
> Art. 32(1)(a) pseudonymisation and encryption of personal data … as appropriate technical measures.

**CRA article (verbatim from SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (1) ensure an appropriate level of cybersecurity based on the risks presented by the product. Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms, "or by using other technical means."

**Scope comparison:**
- GDPR scope: personal data.
- CRA scope: "personal or other" data stored by a product with digital elements (Art. 3(47) cross-references GDPR Art. 4(1) personal-data definition; Annex I extends to non-personal data).
- Scope overlap: Y when the CRA-regulated product processes personal data; Y (conditional).

**Trigger comparison:**
- GDPR trigger: continuous risk-anchored.
- CRA trigger: continuous product-side baseline (Art. 13 umbrella + Annex I chapeau).
- Trigger alignment: SAME (continuous on both legs).

**Threshold/timeline comparison:**
- GDPR: "appropriate" (risk-based).
- CRA: "state-of-the-art mechanisms" (R2 — harmonised-standards floor per SR-CRA-001 ambiguity_notes; bench-anchored to support-period commencement date).
- Tension: NONE — the CRA state-of-the-art baseline is **stricter** than GDPR's risk-based "appropriate" once harmonised standards are present; in their absence, the SR-CRA-001 reading imports ISO/NIST-published standards at support-period commencement.

**Recipient comparison:**
- GDPR: supervisory authority.
- CRA: market surveillance authority + ENISA (Ancillary — not a recipient per se).

**Content template comparison:**
- GDPR: risk assessment + accountability.
- CRA: technical documentation under Annex VII §2/§3 + conformity assessment (Module B or H depending on criticality).

**Classified relationship (from CRDA):** COMPLEMENTARY.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two are the same substantive obligation (encryption at rest to protect personal data) with different anchors: GDPR Art. 32(1)(a) is risk-based; CRA Annex I (2)(e) is state-of-the-art + harmonised-standards. Where the two apply on the same artefact (a CRA-regulated product that processes personal data), the CRA baseline is stricter; meeting the CRA floor discharges the GDPR obligation on the at-rest dimension for that product. CRDA's COMPLEMENTARY is correct in framing but the practical effect on a single product is that CRA is the floor and GDPR is automatically satisfied; COMPLEMENTARY slightly understates that the two converge.

**Scope-disjoint test:** Conditional — disjoint in the baseline case (CRA manufacturer is not the GDPR controller; the SaaS deployer is the GDPR controller inheriting CRA's product-side baseline). Y when the same party is both manufacturer and controller (integrated vendors).

- **P0 note:** This is the pattern the Orchestrator should flag. For the SaaS-using-CRA-product case, the CRDA "C" classification is technically correct on the underlying concern but **does not produce a single compliance task** for either party. Phase 1C Doc 07 should treat this pair as **scope-disjoint in baseline; Y on integrated-stack**.

**Downstream implication:** For Phase 1C Doc 07, this is a **disjoint baseline / scope-conditional** pair: a non-integrated SaaS-uses-CRA-product company has separate compliance tracks (CRA SBOM intake from vendor + GDPR at-rest implementation by controller); an integrated manufacturer-controller has one combined documentation pack.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **Complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-001, Art. 32(1)(a)/(b)) | Personal data confidentiality at rest with risk-anchored baseline | Controller/processor; personal data scope; risk-based + state-of-the-art |
| **CRA** (SR-CRA-001 + SR-CRA-002, Annex I Part I (1)+(2)(e)) | Confidentiality of stored data (personal or other) via state-of-the-art encryption | Manufacturer; product-level; "personal or other" extends beyond GDPR scope; Annex I baseline |

**Why Complementary**: CRA explicitly extends encryption to "personal or other" data (Annex I Part I (2)(e) + Art. 3(47) cross-ref to GDPR Art. 4(1)) and imposes a state-of-the-art baseline. GDPR's risk-based "appropriate" is a softer anchor; CRA's state-of-the-art + harmonised-standards anchor (Art. 27) is stricter. A product manufacturer placing a CRA-regulated product on the market satisfies GDPR's at-rest floor for personal data processed by that product if the CRA baseline is met. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-001; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-001 + SR-CRA-002



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_

