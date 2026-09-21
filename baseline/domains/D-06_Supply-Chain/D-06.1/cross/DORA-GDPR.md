# D-06.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 28(1)):**
> "The controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures …" — Art. 28(1) GDPR

**DORA article (verbatim, Art. 28(1)):**
> "Financial entities shall manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function." — DORA Art. 28(1)
>
> "Financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards." — DORA Art. 28(5)

**Scope comparison:**
- GDPR scope: processors (data-processing entities).
- DORA scope: ICT third-party service providers (broader than processors; includes non-data-processing ICT services).
- Scope overlap: **Y when the financial entity is also a controller and the ICT provider is also a processor**.

**Trigger comparison:**
- GDPR trigger: per-processor engagement.
- DORA trigger: continuous ICT third-party risk management with four-factor proportionality.
- Trigger alignment: **PARTIAL** — both continuous / per-relationship; DORA adds explicit factors.

**Threshold/timeline comparison:**
- GDPR: "sufficient guarantees" (qualitative).
- DORA: four-factor proportionality (nature, scale, complexity, importance) — explicit; for CIF contracts, "most up-to-date AND highest quality" escalator (Art. 28(5)).
- Tension: **NONE** — DORA's four-factor test operationalises the GDPR `sufficient guarantees` threshold with sharper factors.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- DORA: competent authority (national supervisory authority for the financial sector).

**Content template comparison:**
- GDPR: written due-diligence questionnaire + Art. 28(3) DPA.
- DORA: four-factor proportionality assessment + Art. 30(2) 9-element contract + Art. 28(5) standards compliance for CIFs.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY** (DORA exceeds GDPR)
**Reasoning:** DORA's four-factor proportionality test is a sharper operationalisation of the GDPR `sufficient guarantees` test. A financial entity already subject to DORA Art. 28 satisfies GDPR Art. 28(1) `sufficient guarantees` via the proportionality documentation, but must explicitly document the GDPR-specific processor guarantees (instruction-bound processing, audit rights, sub-processor authorisation) — these are not in the DORA Art. 30(2) closed list verbatim.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when a financial entity is also a controller engaging an ICT provider as processor** — both apply on the same supplier relationship.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a consolidated assessment record satisfying both regimes. The DORA four-factor test is documented; the GDPR-specific clauses (Art. 28(3) elements) are appended on the controller side.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-033, Art. 28(1)) | Processor due diligence |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-033 |
| **DORA** (SR-DORA-019, Art. 28(1)) | ICT third-party risk under four-factor proportionality (nature, scale, complexity, importance) |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-019 |

**Why complementary (DORA exceeds GDPR)**: DORA's four-factor proportionality test is a sharper operationalisation of the GDPR `sufficient guarantees` test. A financial entity already subject to DORA Art. 28 satisfies GDPR Art. 28(1) `sufficient guarantees` via the proportionality documentation, but must explicitly document the GDPR-specific processor guarantees (instruction-bound processing, audit rights, sub-processor authorisation).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_

