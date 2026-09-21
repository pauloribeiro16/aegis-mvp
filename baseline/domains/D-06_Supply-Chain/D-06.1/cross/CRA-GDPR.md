# D-06.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 28(1)):**
> "The controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures …" — Art. 28(1) GDPR

**CRA article (verbatim, Art. 13(5) + Art. 3(48)):**
> "Manufacturers shall exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements." — CRA Art. 13(5) sentence 1
>
> "'free and open-source software' means software the source code of which is openly shared and which is made available under a free and open-source licence … for the study, modification and distribution by its users …" — CRA Art. 3(48)

**Scope comparison:**
- GDPR scope: processor as legal entity (data-processing counterparty).
- CRA scope: components as technical artefacts (including non-commercial OSS).
- Scope overlap: **Y (when the CRA product is integrated into a GDPR controller's processing — but the two objects remain distinct)**.

**Trigger comparison:**
- GDPR trigger: per-processor engagement.
- CRA trigger: continuous product-component integration.
- Trigger alignment: **DIFFERENT** — entity-level vs product-level.

**Threshold/timeline comparison:**
- GDPR: "sufficient guarantees" (qualitative).
- CRA: "due diligence" (VAG+POLY-S3, R3 procedural + substantive per SR-CRA-050).
- Tension: **NONE** — distinct objects, distinct triggers.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- CRA: market surveillance authority (MSA).

**Content template comparison:**
- GDPR: due-diligence record on processor + Art. 28(3) contract.
- CRA: Annex VII §2 technical-documentation record on integrated components; SBOM per Annex I Part II (1).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR due diligence is on the *processor as legal entity*; CRA due diligence is on *components as technical artefacts* (including non-commercial OSS, which GDPR does not separately contemplate). When a CRA-compliant product is integrated into a GDPR controller's processing, the manufacturer has already done CRA-level component due diligence; the controller still owes GDPR-level processor due diligence on the manufacturer. The two layers are different perspectives on the same supply chain.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the controller deploys a CRA-classified product — both apply to the same supply chain but at different layers.** The two obligations do not contradict; they layer.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a 2-layer due-diligence record: (1) controller-side processor due diligence on the manufacturer (GDPR Art. 28(1)); (2) manufacturer-side component due diligence on third-party components (CRA Art. 13(5)). The CRDA DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-033, Art. 28(1)) | Processor due diligence |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-033 |
| **CRA** (SR-CRA-050, Art. 13(5) + Art. 3(48)) | Third-party component due diligence including non-commercial OSS |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-050 |

**Why different-perspective**: GDPR due diligence is on the *processor as legal entity*; CRA due diligence is on *components as technical artefacts* (including non-commercial OSS, which GDPR does not separately contemplate). When a CRA-compliant product is integrated into a GDPR controller's processing, the manufacturer has already done CRA-level component due diligence; the controller still owes GDPR-level processor due diligence on the manufacturer.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

