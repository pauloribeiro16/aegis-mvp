# D-06.3 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 28(3)(a)–(h)):**
> (See GDPR↔NIS2 pair above for the verbatim 8-element list.)

**DORA article (verbatim, Art. 30(1)+(2)):**
> "The rights and obligations of the financial entity and of the ICT third-party service provider shall be clearly allocated and set out in writing … The contractual arrangements shall include, at least, the following elements: (a) a clear description of all functions and ICT services to be provided by the ICT third-party service provider … (b) the locations where the contracted and subcontracted functions and ICT services are to be provided and where the data are to be processed, including the storage location, and an obligation for the ICT third-party service provider to notify the financial entity in advance if it intends to change those locations; (c)) provisions on the availability, authenticity, integrity and confidentiality of the data, including the protection of data during transmission and processing; (d) provisions on ensuring access, recovery and return of the personal and non-personal data of the financial entity in the case of insolvency, resolution or termination of the ICT third-party service provider; (e) service level descriptions, including updates and revisions thereto; (f) the obligation of the ICT third-party service provider to provide assistance to the financial entity in the event of an ICT-related incident … at no extra cost or at a cost determined ex ante; (g) the obligation of the ICT third-party service provider to cooperate fully with the competent authority and the resolution authorities of the financial entity; (h) termination rights and related minimum notice periods for the financial entity … (i) conditions for participation of the ICT third-party service provider in the ICT security awareness programmes and digital operational resilience training of the financial entity …" — DORA Art. 30(1)+(2)(a)–(i)

(OJ-corrective note: per DORA validation report v0.2 F-10, the `audit rights` and `exit strategies` clauses that were originally attributed to Art. 30(2) are in fact in Art. 30(3)(e)(i) (audit rights) and Art. 30(3)(f) (exit strategies), both CIF-only. The Art. 30(2) closed list is the 9 elements (a)–(i) quoted above.)

**Scope comparison:**
- GDPR scope: processor contract (controller ↔ processor).
- DORA scope: ICT third-party contract (financial entity ↔ ICT provider).
- Scope overlap: **Y when the financial entity is also a controller and the ICT provider is also a processor**.

**Trigger comparison:**
- GDPR trigger: per-processor contract.
- DORA trigger: per-ICT-third-party contract.
- Trigger alignment: **PARTIAL** — both per-contract; DORA adds explicit CIF-only clauses at Art. 30(3).

**Threshold/timeline comparison:**
- GDPR: closed 8-element list.
- DORA: closed 9-element list (Art. 30(2)) + CIF-only clauses (Art. 30(3)).
- Tension: **GENUINE OVERLAP, NO CONTRADICTION** — the two lists overlap but are not identical. The closed AND-list reading of both lists means the union of all required clauses must appear in the contract. There is no clause in either list that contradicts a clause in the other — they are additive.

**Recipient comparison:**
- GDPR: DPA.
- DORA: competent authority.

**Content template comparison:**
- GDPR: 8-element DPA.
- DORA: 9-element Art. 30(2) contract + CIF-only Art. 30(3) clauses (audit rights, exit strategies).

**Classified relationship (from CRDA):** CONTRADICTORY (overlap)
**Verified relationship (after OJ-text analysis):** **CORRECTED — COMPLEMENTARY** (clause-list union)
**Reasoning:** GDPR Art. 28(3) has 8 mandatory elements; DORA Art. 30(2) has 9 minimum elements. The two lists overlap but are not identical. The CRDA reasoning itself acknowledges this: "the contract must satisfy both sets" — which is the textbook union pattern. There is no mutually exclusive obligation. The "contradictory" label is scope-incorrect; the correct label is "complementary" with consolidation requirement (union of clauses). When a financial entity contracts with a processor that is also an ICT third-party service provider, the contract must satisfy both sets — the union is the operative rule. Phase 2 must produce a consolidated clause matrix that satisfies the union without conflict.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the financial entity is also a controller and the ICT provider is also a processor — both apply on the same supplier relationship.** The union rule applies.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a consolidated clause matrix. The intersection of GDPR Art. 28(3) and DORA Art. 30(2) is the operational hinge: financial entities that process personal data via ICT third-party providers must satisfy both clause sets. Phase 3 case generation must validate that supplier contracts in case companies include all required elements per the consolidated matrix. The CRDA "contradictory" label should be corrected to "complementary" with union rule.

---


## Summary (Domain Analysis)

| GDPR ↔ DORA | **contradictory** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-034, Art. 28(3)(a)–(h)) | Eight-element processor contract |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-034 |
| **DORA** (SR-DORA-021 + SR-DORA-022, Art. 30(1)–(3)) | Minimum 9 contractual elements (a)–(i) + unrestricted audit rights |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-021, SR-DORA-022 |

**Why contradictory (overlap)**: GDPR Art. 28(3) has 8 mandatory elements (subject-matter, type of data, obligations, rights, deletion/return, audit, sub-processor, confidentiality); DORA Art. 30(2) has 9 minimum elements. The two lists overlap but are not identical. When a financial entity contracts with a processor that is also an ICT third-party service provider, the contract must satisfy both sets. Phase 2 must produce a consolidated clause matrix that satisfies the union of GDPR + DORA elements without conflict.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

