# D-05.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 17(1) + Art. 5(1)(c)/(e) + Art. 28(3)(g)):**
> "The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies: (a) the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed; (b) the data subject withdraws consent …; (c) the data subject objects …; (d) the personal data have been unlawfully processed; (e) the personal data have to be erased for compliance with a legal obligation …; (f) the personal data have been collected in relation to the offer of information society services …" — Art. 17(1) GDPR
>
> "Processing by a processor … be governed by a contract … that sets out … the obligation to … delete or return all the personal data to the controller after the end of the provision of services relating to processing … and delete existing copies." — Art. 28(3)(g) GDPR

**CRA article (verbatim, Annex I Part I (2)(m) + Annex II §8(d)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (m) allow users to securely and in a timely manner remove or transfer all of the data they have provided to, or generated through, the use of, the product with digital elements, and provide the user with information on how to do so, including for the purpose of switching to another product." — CRA Annex I Part I (2)(m)
>
> "The instructions and information referred to in paragraph 1 shall include … the secure decommissioning of the product with digital elements, including, where applicable, information on how user data can be securely removed." — CRA Annex II §8(d)

**Scope comparison:**
- GDPR scope: personal data held by the controller (data-subject-initiated right).
- CRA scope: all data provided to or generated through the product (user-initiated mechanism).
- Scope overlap: **Y (when the user is also a data subject and the data is personal)**.

**Trigger comparison:**
- GDPR trigger: data subject's Art. 17(1) request.
- CRA trigger: user's product-initiated removal request (manufacturer obligation to enable the mechanism).
- Trigger alignment: **PARTIAL** — both user-initiated but addressing different objects (data subject's erasure of personal data vs user's removal of all product data).

**Threshold/timeline comparison:**
- GDPR: "without undue delay" — qualitative.
- CRA: "in a timely manner" — qualitative, with explicit secure-removal semantics.
- Tension: **NONE** (both qualitative; the stricter "securely" qualifier of CRA does not contradict "without undue delay").

**Recipient comparison:**
- GDPR: data subject; downstream recipients per Art. 19 (when erasure is invoked).
- CRA: user (the user-facing interface of the removal mechanism).

**Content template comparison:**
- GDPR: Art. 12 transparency + Art. 17(2) confirmation of action.
- CRA: Annex II §8(h) user instructions on the removal procedure.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 17 is a data-subject right (controller-bound); CRA Annex I Part I (2)(m) is a user-facing mechanism (manufacturer-bound, embedded in product design). The two layers stack: the manufacturer enables the deletion mechanism (CRA), and the controller operationalises the data-subject right through that mechanism (GDPR). For the cryptographic-key-destruction deletion path specified by SR-GDPR-030, the CRA product design must support it. Both provisions converge on the operational aim (render the user's personal data inaccessible) while the mechanism layer (controller's policy execution) and the architectural layer (manufacturer's product design) are stacked.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the data subject invoking Art. 17(1) is also the user invoking the CRA (2)(m) removal mechanism on a CRA-classified product)**. The two obligations stack — they do not contradict.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer rule: (1) manufacturer-side design obligation (CRA Annex I Part I (2)(m) — the product must support secure, easy, permanent removal of all data on user election); (2) controller-side rights obligation (GDPR Art. 17 — the controller must operationalise the data-subject right through that mechanism). Phase 3 case generation must validate that CRA-classified products in case companies expose a deletion API aligned with GDPR Art. 17 obligations (cryptographic erasure per SR-GDPR-030's `deletes` POLY reading).

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-030 + SR-GDPR-031, Art. 17 + Art. 5(1)(c)/(e) + Art. 28(3)(g)) | Right-to-erasure with cryptographic key-destruction deletion path + processor erasure/return on contract end |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-030, SR-GDPR-031 |
| **CRA** (SR-CRA-048 + SR-CRA-049 + SR-CRA-111, Annex I Part I (2)(m) + Annex II §8(d)) | User-initiated secure data and settings removal + secure cross-product transfer + decommissioning instructions |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-048, SR-CRA-049, SR-CRA-111 |

**Why complementary**: GDPR Art. 17 is a data-subject-initiated right (controller-bound); CRA Annex I Part I (2)(m) is a user-initiated mechanism (manufacturer-bound, embedded in product design). When a user exercises both rights on the same product, the manufacturer-bound CRA obligation is operationalised through the controller-bound GDPR process. Phase 2 must surface that the CRA product design must support the GDPR Art. 17 deletion path (e.g., cryptographic key destruction as GDPR SR-GDPR-030 specifies).



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 17(1) + Art. 5(1)(c)/(e) + Art. 28(3)(g)):**
> "The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies: (a) the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed; (b) the data subject withdraws consent …; (c) the data subject objects …; (d) the personal data have been unlawfully processed; (e) the personal data have to be erased for compliance with a legal obligation …; (f) the personal data have been collected in relation to the offer of information society services …" — Art. 17(1) GDPR
>
> "Processing by a processor … be governed by a contract … that sets out … the obligation to … delete or return all the personal data to the controller after the end of the provision of services relating to processing … and delete existing copies." — Art. 28(3)(g) GDPR

**CRA article (verbatim, Annex I Part I (2)(m) + Annex II §8(d)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (m) allow users to securely and in a timely manner remove or transfer all of the data they have provided to, or generated through, the use of, the product with digital elements, and provide the user with information on how to do so, including for the purpose of switching to another product." — CRA Annex I Part I (2)(m)
>
> "The instructions and information referred to in paragraph 1 shall include … the secure decommissioning of the product with digital elements, including, where applicable, information on how user data can be securely removed." — CRA Annex II §8(d)

**Scope comparison:**
- GDPR scope: personal data held by the controller (data-subject-initiated right).
- CRA scope: all data provided to or generated through the product (user-initiated mechanism).
- Scope overlap: **Y (when the user is also a data subject and the data is personal)**.

**Trigger comparison:**
- GDPR trigger: data subject's Art. 17(1) request.
- CRA trigger: user's product-initiated removal request (manufacturer obligation to enable the mechanism).
- Trigger alignment: **PARTIAL** — both user-initiated but addressing different objects (data subject's erasure of personal data vs user's removal of all product data).

**Threshold/timeline comparison:**
- GDPR: "without undue delay" — qualitative.
- CRA: "in a timely manner" — qualitative, with explicit secure-removal semantics.
- Tension: **NONE** (both qualitative; the stricter "securely" qualifier of CRA does not contradict "without undue delay").

**Recipient comparison:**
- GDPR: data subject; downstream recipients per Art. 19 (when erasure is invoked).
- CRA: user (the user-facing interface of the removal mechanism).

**Content template comparison:**
- GDPR: Art. 12 transparency + Art. 17(2) confirmation of action.
- CRA: Annex II §8(h) user instructions on the removal procedure.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 17 is a data-subject right (controller-bound); CRA Annex I Part I (2)(m) is a user-facing mechanism (manufacturer-bound, embedded in product design). The two layers stack: the manufacturer enables the deletion mechanism (CRA), and the controller operationalises the data-subject right through that mechanism (GDPR). For the cryptographic-key-destruction deletion path specified by SR-GDPR-030, the CRA product design must support it. Both provisions converge on the operational aim (render the user's personal data inaccessible) while the mechanism layer (controller's policy execution) and the architectural layer (manufacturer's product design) are stacked.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the data subject invoking Art. 17(1) is also the user invoking the CRA (2)(m) removal mechanism on a CRA-classified product)**. The two obligations stack — they do not contradict.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer rule: (1) manufacturer-side design obligation (CRA Annex I Part I (2)(m) — the product must support secure, easy, permanent removal of all data on user election); (2) controller-side rights obligation (GDPR Art. 17 — the controller must operationalise the data-subject right through that mechanism). Phase 3 case generation must validate that CRA-classified products in case companies expose a deletion API aligned with GDPR Art. 17 obligations (cryptographic erasure per SR-GDPR-030's `deletes` POLY reading).

---


---
