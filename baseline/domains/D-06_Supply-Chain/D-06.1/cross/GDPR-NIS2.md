# D-06.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 28(1) + Art. 28(2) + Art. 4(7)/(8)):**
> "The controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing will meet the requirements of this Regulation and ensure the protection of data subjects' rights." — Art. 28(1) GDPR
>
> "The processor shall not engage another processor without prior specific or general written authorisation of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of other processors, thereby giving the controller the opportunity to object to such changes." — Art. 28(2) GDPR

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems which those entities use for their activities or for the provision of their services, and to prevent or minimise the impact of incidents on recipients of their services and on other services. Taking into account the state of the art … those measures shall include, in particular … supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(1) + Art. 21(2)(d)

**Scope comparison:**
- GDPR scope: processors (data-processing entities).
- NIS 2 scope: direct suppliers and service providers (broader, includes non-data-processing suppliers).
- Scope overlap: **Y when the supplier is both a processor and a service provider** (typical in ICT outsourcing).

**Trigger comparison:**
- GDPR trigger: per-processor engagement.
- NIS 2 trigger: continuous supply-chain security.
- Trigger alignment: **PARTIAL** — GDPR is per-processor; NIS 2 is continuous + per-supplier.

**Threshold/timeline comparison:**
- GDPR: qualitative "sufficient guarantees" — EDPB Guidelines 07/2020 factors.
- NIS 2: "appropriate and proportionate" (Art. 21(1) chapeau); "direct" scope-limiter (Art. 21(2)(d)).
- Tension: **NONE** — both are risk-anchored; GDPR's `sufficient guarantees` is a sharper threshold on the same risk substrate.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- NIS 2: CSIRT or competent authority.

**Content template comparison:**
- GDPR: written due-diligence questionnaire, certifications review, Art. 28(3) clauses.
- NIS 2: documented supply-chain security programme; Member State transposition may specify minimum-clause catalogues.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR due diligence is on the *processor* (data-processing entity); NIS 2 supply chain security is on *direct suppliers and service providers* (broader scope, includes non-data-processing suppliers). When the supplier is both a processor and a service provider, both apply; the GDPR `sufficient guarantees` test and the NIS 2 `direct` scope-limiter are layered, not overlapping. The NIS 2 `direct` SCOPE-Q S3 ambiguity (R1 Tier-1 / R2 technically integrated / R3 operationally dependent) is the key operational handle — see SR-NIS2-020 `ambiguity_notes` for the full 3-reading discussion.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the controller and the essential / important entity is the same party** (typical for financial entities that are also essential entities under NIS 2). The two obligations stack on the same supplier relationship.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered supplier-assessment matrix: (1) GDPR processor due diligence (Art. 28(1)) covering all 4 EDPB Guidelines 07/2020 factors; (2) NIS 2 direct-supplier security under Art. 21(2)(d) with the chosen `direct` reading documented. Phase 3 case generation must validate the dual-layer assessment in case companies.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-033, Art. 28(1) + Art. 28(2) + Art. 4(7)/(8)) | Processor due diligence with documented sufficient guarantees |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-033 |
| **NIS2** (SR-NIS2-020, Art. 21(2)(d) + Art. 21(1)) | Direct supplier and service-provider security by contract |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-020 |

**Why complementary**: GDPR due diligence is on the *processor* (data-processing entity); NIS2 supply chain security is on *direct suppliers and service providers* (broader scope, includes non-data-processing suppliers). When the supplier is both a processor and a service provider, both apply; the GDPR `sufficient guarantees` test and the NIS2 `direct` scope-limiter are layered, not overlapping.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

