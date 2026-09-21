# D-06.4 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 27(1)):**
> "Where Article 3(2) applies, the controller or the processor shall designate in writing a representative in the Union." — Art. 27(1) GDPR

**CRA article (verbatim, Art. 18(1)–(3)):**
> "A manufacturer established outside the Union may, by written mandate, appoint an authorised representative established in the Union to perform specified tasks on behalf of the manufacturer." — CRA Art. 18(1)
>
> "The mandate of the authorised representative shall not cover the obligations laid down in Article 13(1) to (11), Article 13(12) first subparagraph, point (a), and Article 13(14)." — CRA Art. 18(2)
>
> "The authorised representative shall perform the tasks specified in the mandate. The mandate shall allow the authorised representative to perform at least the following tasks: (a) keeping a copy of the EU declaration of conformity and the technical documentation at the disposal of the market surveillance authorities for the period referred to in Article 13(13); (b) providing the market surveillance authorities, on reasoned request, with all the information and documentation necessary to demonstrate the conformity of a product with digital elements with the essential cybersecurity requirements set out in Annex I; (c) cooperating with the market surveillance authorities, at their request, on any action taken to address non-compliance with the essential cybersecurity requirements set out in Annex I presented by a product with digital elements covered by the mandate of the authorised representative." — CRA Art. 18(3)

**Scope comparison:**
- GDPR scope: data-protection representative for non-EU controller / processor.
- CRA scope: product-compliance authorised representative for non-EU manufacturer.
- Scope overlap: **Y (when the same non-EU entity is both a non-EU controller and a non-EU CRA manufacturer)** — different objects, different mandates.

**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- CRA trigger: non-EU manufacturer placing CRA-classified product on the EU market.
- Trigger alignment: **PARTIAL** — both for non-EU entities, but addressing different objects.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- CRA: written mandate + non-delegable carve-out (Art. 18(2)).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA + data subject.
- CRA: MSA + national competent authority.

**Content template comparison:**
- GDPR: written representative designation.
- CRA: written AR mandate (Art. 18(1)).

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL** (different objects)
**Reasoning:** Both GDPR Art. 27 and CRA Art. 18 require a written EU-side representative for non-EU entities. Different objects: GDPR = data-protection representative; CRA = product-compliance authorised representative. When a non-EU manufacturer of CRA-classified products is also a non-EU controller, both representatives are required, with different mandates (Art. 27 representative handles data-subject requests and DPA liaison; Art. 18 AR retains technical documentation and cooperates with MSA). The label "equal" captures the same form (written EU-side representative) but the substance is layered, not redundant.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the same non-EU entity is both a non-EU controller and a non-EU CRA manufacturer — both apply on the same entity but address different obligations.**

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer representative architecture: (1) GDPR Art. 27 data-protection representative; (2) CRA Art. 18 product-compliance AR. The EQUAL label is preserved.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **equal** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-038, Art. 27) | EU representative for non-EU controllers/processors |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-038 |
| **CRA** (SR-CRA-059 + SR-CRA-060, Art. 18(1)–(3)) | Authorised representative appointment with non-delegable carve-out + EU-side compliance tasks |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-059, SR-CRA-060 |

**Why equal (different objects)**: Both GDPR Art. 27 and CRA Art. 18 require a written EU-side representative for non-EU entities. Different objects: GDPR = data-protection representative; CRA = product-compliance representative. When a non-EU manufacturer of CRA-classified products is also a non-EU controller, both representatives are required, with different mandates (Art. 27 representative handles data-subject requests and DPA liaison; Art. 18 AR retains technical documentation and cooperates with MSA).



