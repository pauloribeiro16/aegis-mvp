# D-06.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 28(3)(a)–(h)):**
> (See GDPR↔NIS2 pair above for the verbatim 8-element list.)

**CRA article (verbatim, Art. 19 + Art. 20):**
> "An importer shall place on the market only products with digital elements that comply with Chapter II, Section 2 and where the relevant conformity assessment procedure has been carried out by the manufacturer or on behalf of the manufacturer … An importer shall, before placing a product with digital elements on the market, ensure that … the conformity assessment has been carried out, the technical documentation has been drawn up, the product bears the CE marking and is accompanied by the required documents … and the manufacturer has complied with the requirements set out in Article 13(5) and (7)." — CRA Art. 19(1)/(2)
>
> "A distributor shall act with due care in relation to the requirements of this Regulation when making a product with digital elements available on the market. Before making a product with digital elements available on the market, a distributor shall verify that … the CE marking has been affixed … the product is accompanied by the required documents … and the manufacturer and the importer have complied with the requirements set out in Article 13(5), (7) and (9) …" — CRA Art. 20(1)/(2)
>
> "Where a distributor has reason to believe that a product with digital elements is not in conformity with Chapter II, Section 2, the distributor shall not make the product available on the market until conformity has been restored, and shall inform the manufacturer and the market surveillance authority of the significant risk." — CRA Art. 20(3)
>
> "Where a vulnerability is identified in a product with digital elements that the distributor has made available on the market, the distributor shall inform the manufacturer and take immediate corrective measures necessary to bring the product into conformity, including, where appropriate, withdrawal or recall." — CRA Art. 20(4)

**Scope comparison:**
- GDPR scope: controller ↔ processor contract.
- CRA scope: importer / distributor ↔ market surveillance authority (imposed by regulation, not contract).
- Scope overlap: **N (typically) — different contracting parties, different contract objects.** They overlap when a CRA-compliant product is used by a GDPR controller: the controller is the data-protection-facing party; the manufacturer / importer / distributor is the market-surveillance-facing party.

**Trigger comparison:**
- GDPR trigger: per-processor contract.
- CRA trigger: continuous market-surveillance obligation (Art. 19 + Art. 20).
- Trigger alignment: **DIFFERENT** — contract vs regulatory obligation.

**Threshold/timeline comparison:**
- GDPR: closed 8-element list.
- CRA: "due care" + non-conformity escalation; no closed-list clause requirements at OJ level for distributor contracts.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA.
- CRA: MSA + manufacturer.

**Content template comparison:**
- GDPR: 8-element DPA.
- CRA: pre-market verification (Art. 19(2)) + pre-market checks (Art. 20(2)) + non-conformity escalation (Art. 20(3)) + corrective measures (Art. 20(4)).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR contracts are *controller ↔ processor* (Art. 28(3)); CRA obligations are *importer / distributor ↔ MSA* (market-surveillance direction). Different contracting parties, different contract objects. The CRA economic-operator obligations are imposed by regulation (not contract); the GDPR DPA elements are contractually negotiated. Both apply to the same chain when a CRA-compliant product is used by a GDPR controller.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct contracting parties, distinct obligations.** Conditional overlap only when the controller deploys a CRA-compliant product and the manufacturer / importer / distributor is in the chain.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer contract architecture: (1) GDPR DPA between controller and processor; (2) CRA economic-operator obligations between manufacturer / importer / distributor and MSA. The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-034, Art. 28(3)(a)–(h)) | Eight-element processor contract |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-034 |
| **CRA** (SR-CRA-054 + SR-CRA-055 + SR-CRA-057 + SR-CRA-058, Art. 19 + Art. 20) | Importer pre-market verification + non-conformity escalation + distributor due-care + corrective measures escalation |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-054, SR-CRA-055, SR-CRA-057, SR-CRA-058 |

**Why different-perspective**: GDPR contracts are *controller↔processor* (Art. 28(3)); CRA obligations are *importer/distributor↔MSA* (market-surveillance direction). Different contracting parties, different contract objects. The CRA economic-operator obligations are imposed by regulation (not contract); the GDPR DPA elements are contractually negotiated. Both apply to the same chain when a CRA-compliant product is used by a GDPR controller.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
47 lines — see ../../_migration_report.md)_

