# D-06.3 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 28(3)(a)–(h)):**
> "Processing by a processor … be governed by a contract … that sets out … the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects, and the obligations and rights of the controller. That contract or other legal act shall stipulate, in particular, that the processor: (a) processes the personal data only on documented instructions from the controller …; (b) ensures that persons authorised to process the personal data have committed themselves to confidentiality …; (c) implements all the measures required pursuant to Article 32; (d) engages another processor only with the prior specific or general written authorisation of the controller …; (e) assists the controller in fulfilling its obligation to respond to requests for exercising the data subject's rights …; (f) assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36; (g) at the choice of the controller, deletes or returns all the personal data to the controller after the end of the provision of services relating to processing … and deletes existing copies; (h) makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller." — Art. 28(3)(a)–(h) GDPR

**NIS 2 article (verbatim, Art. 21(2)(d) + Art. 21(3) sentence 1):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)
>
> "When considering which of the measures referred to in the first subparagraph are appropriate, essential and important entities shall take into account the vulnerabilities specific to each direct supplier and service provider, the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures, and the results of coordinated security risk assessments of critical supply chains …" — NIS 2 Art. 21(3)

**Scope comparison:**
- GDPR scope: processor contract (controller ↔ processor).
- NIS 2 scope: direct supplier contract + supplier assessment (entity ↔ direct supplier).
- Scope overlap: **Y when the supplier is both a processor and a supplier**.

**Trigger comparison:**
- GDPR trigger: per-processor contract.
- NIS 2 trigger: continuous supply-chain security + per-supplier assessment.
- Trigger alignment: **PARTIAL** — GDPR is per-contract; NIS 2 is continuous + per-supplier.

**Threshold/timeline comparison:**
- GDPR: closed 8-element list (Art. 28(3)(a)–(h)).
- NIS 2: "security-related contractual aspects" (no closed list at OJ level).
- Tension: **NONE** — GDPR's 8-element list operationalises the NIS 2 `security-related contractual aspects` open-texture with specific clauses.

**Recipient comparison:**
- GDPR: DPA.
- NIS 2: CSIRT / competent authority.

**Content template comparison:**
- GDPR: 8-element DPA.
- NIS 2: security-related supplier-contract terms + Art. 21(3) supplier assessment.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 28(3) contract elements are on the *processor* (data-processing actor); NIS 2 Art. 21(3) supplier-assessment obligations are on the *direct supplier* (broader scope, not limited to processors). When the supplier is both a processor and a supplier, both contracts apply; GDPR is data-protection-specific, NIS 2 is cybersecurity-specific. The GDPR Art. 28(3)(c) reference to Art. 32 measures is the operational hinge where the two contractual obligations intersect.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the controller and the essential / important entity is the same party** — both apply on the same supplier relationship.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a layered supplier-contract template: GDPR Art. 28(3) DPA + NIS 2 supplier-security terms. Phase 3 case generation must validate that supplier contracts include the GDPR 8-element list + the NIS 2 security-related terms.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-034 + SR-GDPR-036, Art. 28(3)(a)–(h) + Art. 28(2)) | Eight-element processor contract with audit and instruction clauses + sub-processor authorisation with controller change-notification |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-034, SR-GDPR-036 |
| **NIS2** (SR-NIS2-020 + SR-NIS2-022, Art. 21(2)(d) + Art. 21(3)) | Direct supplier security by contract + per-supplier vulnerability intelligence for risk prioritisation |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-020, SR-NIS2-022 |

**Why complementary**: GDPR Art. 28(3) contract elements are on the *processor* (data-processing actor); NIS2 Art. 21(3) supplier-assessment obligations are on the *direct supplier* (broader scope, not limited to processors). When the supplier is both a processor and a supplier, both contracts apply; GDPR is data-protection-specific, NIS2 is cybersecurity-specific. The GDPR Art. 28(3)(c) reference to Art. 32 measures is the operational hinge where the two contractual obligations intersect.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_