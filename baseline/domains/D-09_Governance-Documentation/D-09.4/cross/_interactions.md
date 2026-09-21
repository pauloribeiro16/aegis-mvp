# D-09.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-09.4 Records of Processing](../../DomainAnalysis/D-09_Governance-Documentation/D-09.4.md)
#### D-09.4 Records of Processing
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority note (CRDA flag):** DORA is fully absent — no RoPA-equivalent. DORA BC/DR logging (Art. 12) is operational continuity, not processing-of-personal-data records. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The DORA Art. 12 logging obligation is a separate artefact.

## Part 1 §1 — Cross-Regulation Analysis context

### D-10 Monitoring & Audit

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-09.4 Records of Processing
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md)
> (10 pairs verified against OJ text — **5 participating regulations
> are GDPR, NIS 2, CRA, DORA, AI Act; all 5 participate** as noted by
> `DomainAnalysis/D-09_Governance-Documentation/D-09.4.md`
> line 27: "Participants: GDPR, NIS2, CRA, DORA, AI_Act" and line 104:
> "Four documentation regimes with overlapping but non-substitutable
> artefacts" — note: only 4 of the 5 participating regs have
> non-substitable documentation artefacts per DomainAnalysis; DORA is
> explicitly marked fully absent per CRDA-deep §D-09.4 line 29).
>
> **Critical note (CRDA flag — DORA fully absent for RoPA).** Per
> CRDA-deep §D-09.4 line 29: **"DORA is fully absent — no RoPA-
> equivalent. DORA BC/DR logging (Art. 12) is operational continuity,
> not processing-of-personal-data records. For DORA financial entities,
> the GDPR RoPA remains the dedicated authority for processing-
> activities documentation. The DORA Art. 12 logging obligation is a
> separate artefact."** This is the **DORA-absence flag** that
> distinguishes D-09.4 from the other D-09 sub-domains; although DORA
> is listed as a participant, **the DORA Art. 9(4)(a) information
> security policy is a different record type** (IS-policy
> documentation) serving a different audit purpose (NCA audit) than
> the GDPR RoPA-equivalent. **No CORRECTED, no CONTRADICTORY** pairs.
> The high-level SO surfaces the **common documentation regime**
> (records of processing activities + technical documentation +
> certification records + IS-policy documentation + QMS
> documentation), with the 5 distinct documentation regimes on
> parallel artefacts serving distinct audit purposes.
>
> **Critical note (CRDA flag — NO OJ-level consolidation rule at
> D-09.4).** Unlike D-09.2 where **CRA Art. 13(4) sentence 2**
> permits AI Act Art. 9 risk-management to substitute for CRA risk
> assessment (the only OJ-level cross-regulation consolidation rule
> in D-09.2), the documentation object at D-09.4 has **NO OJ-level
> cross-regulation consolidation rule**. The 5 documentation regimes
> operate in parallel; no OJ-permitted cross-substitution exists
> between them.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-09.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-029 (primary) + SO-GDPR-038 (data-subject transparency) | Records of processing activities per Art. 30(1)/(2); in writing or electronic form (Art. 30(3)); 250-employee exception per Art. 30(5); supervisory-authority on-request (Art. 30(4)); transparency to data subjects (Art. 12-14). | Controller/processor RoPA mandate; data-subject-rights + DPA audit purposes; substantively scope-disjoint from NIS 2 + CRA per CRDA `N (typically)` (different record types). |
| NIS2 | SO-NIS2-024 (partial) | Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems (Art. 24(1)); Commission delegated acts under Art. 24(2); ENISA candidate scheme request under Art. 24(3). | Certification-driven recordkeeping (Art. 24(1)/(2)/(3)), not a RoPA-equivalent; substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers). |
| CRA | SO-CRA-055 to SO-CRA-067 (many — D-09.4 is the densest CRA sub-domain) | Single point of contact (Art. 13(17)) + product identification (Art. 13(15)/(16) + Annex II §1/§3) + 10-year technical-documentation retention (Art. 13(13) + Art. 19(6) + Art. 23(2)) + EU declaration + CE marking (Art. 13(12) + Art. 28 + Art. 30) + Annex VII 8-item technical documentation + support-period determination (Art. 13(8) sentence 2 + Art. 13(19) + Annex II §7) + EU declaration provision (Art. 13(20) + Annex II §6) + immediate corrective measures (Art. 13(21)) + MSA cooperation (Art. 13(22) + Art. 13(4) sentence 2) + cessation of operations notification (Art. 13(23)) + conformity-assessment procedure selection (Art. 32) + Commission implementing/delegated acts (Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6)). | Product-level technical documentation regime; Annex VII 8-item content list; 10-year retention or support period (whichever longer); substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers). |
| DORA | (out-of-scope as RoPA-equivalent — partial via DORA Art. 9(4)(a) information-security policy) | DORA does **NOT** impose a RoPA obligation (no GDPR Art. 30 analogue). The DORA Art. 9(4)(a) information security policy defines rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets — different record type serving a different audit purpose than RoPA. DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents. | Entity-level IS-policy documentation serving NCA audit purposes — **partial coverage at D-09.4 (different record type, not RoPA-equivalent)**; CRDA explicitly classifies DORA as "fully absent" for D-09.4 per CRDA-deep §D-09.4 line 29. |
| AI_Act | SO-AIACT-009 (partial, primary) + SO-AIACT-010 (cross) + SO-AIACT-008 (logs) | Technical documentation (Annex IV via Art. 11/12) per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` + QMS documentation of 13 enumerated aspects (Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions`). | AI-system-specific technical documentation mandate (Annex IV) + QMS documentation + provider logs; partial coverage; GDPR Art. 30 is the dedicated authority for RoPA. |

## Validated relationships (from CRDA-deep §D-09.4)

#### Validated relationships (from CRDA-deep §D-09.4)
Of 10 pairs, **10 verified as SAME — no CORRECTED, no CONTRADICTORY**. The 10 verified relationships are distributed as **2 SAME — DIFFERENT-PERSPECTIVE (GDPR ↔ NIS 2, GDPR ↔ CRA — substantively scope-disjoint per CRDA `N (typically)` for both, different record types)**; **3 SAME — COMPLEMENTARY classified by CRDA (GDPR ↔ AI Act; NIS 2 ↔ CRA; CRA ↔ AI Act)**; **1 SAME — DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA (GDPR ↔ DORA — recommended DIFFERENT-PERSPECTIVE per CRDA §D-09.4 line 149; substantively scope-disjoint)**; **4 SAME — COMPLEMENTARY RECOMMENDED-by-CRDA (NIS 2 ↔ DORA, NIS 2 ↔ AI Act, CRA ↔ DORA, DORA ↔ AI Act — recommended COMPLEMENTARY per CRDA §D-09.4 lines 275, 318, 361, 445)**. **The architecture is legitimately diverse with 5 distinct documentation regimes + DORA fully absent for RoPA + no OJ-level cross-regulation consolidation rule** — the 2 SAME — DIFFERENT-PERSPECTIVE pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA) reflect the structural RoPA vs. certification/architecture documentation asymmetry; the 1 RECOMMENDED-DIFFERENT-PERSPECTIVE pair (GDPR ↔ DORA) reflects the RoPA vs. information-security-policy documentation asymmetry; the 7 SAME — COMPLEMENTARY pairs (3 CRDA-classified + 4 CRDA-recommended) reflect the parallel-documentation-regime structure with distinct record types and audit purposes:
- **GDPR ↔ NIS2** — DIFFERENT-PERSPECTIVE (SAME): GDPR RoPA is **processing-activities-focussed** (Art. 30(1) `record of processing activities under its responsibility` + Art. 30(1) content items + Art. 30(5) 250-employee exception + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request); NIS 2 Art. 24 is **certification-driven recordkeeping** (Art. 24(1) `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` + Art. 24(2) Commission delegated acts + Art. 24(3) ENISA candidate scheme request). Different record types (processing-activities-focused vs. certification-focused); no substantive overlap; substantively scope-disjoint per CRDA `N (typically)` per CRDA-deep §D-09.4 line 68. No reclassification required. The two regimes do not substitute — Phase 1 entities with both must maintain **two separate documentation regimes** (GDPR RoPA + NIS 2 Art. 24 certification-driven records).
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): GDPR RoPA covers **processing activities** (Art. 30(1) `(a) name and contact details of the controller … (b) purposes of the processing … (c) a description of the categories of data subjects and of the categories of personal data … (d) the categories of recipients to whom personal data have been or will be disclosed … (e) transfers of personal data to a third country … (f) where possible, the envisaged time limits for erasure of the different categories of data … (g) where possible, a general description of the technical and organisational security measures`); CRA technical documentation covers **product cybersecurity** (Annex VII §1-§8 8-item content list — general description, design, development, vulnerability-handling processes, risk assessment, support-period determination, standards applied, test reports, EU declaration copy, SBOM). Different record types serving different audit purposes (processing-activities-focused DPA audit vs. product-cybersecurity-focused MSA audit); substantively scope-disjoint per CRDA `N (typically)` per CRDA-deep §D-09.4 line 110. No reclassification required. **The two regimes do not cross-substitute** — Phase 1 entities with GDPR + CRA applicability must maintain **two separate documentation regimes** (GDPR RoPA + CRA Annex VII technical documentation + EU declaration + CE marking).
- **GDPR ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME) — **CRDA-recommended (NOT classified in CRDA table; recommended in Downstream-implication)**: GDPR RoPA covers **processing activities** (Art. 30(1)/(2)/(3)/(4)/(5)); DORA does **NOT** impose a RoPA-equivalent (per CRDA-deep §D-09.4 line 29 explicit "DORA is fully absent" — no analogue to GDPR Art. 30); the DORA Art. 9(4)(a) information security policy is a **different record type** (defines rules to protect availability, authenticity, integrity and confidentiality of data/information assets/ICT assets), serving a different audit purpose (NCA audit on IS policy, not DPA audit on processing activities). Different record types serving different audit purposes; substantively scope-disjoint per CRDA `N (typically)` (recommended) per CRDA-deep §D-09.4 line 153. No reclassification required — **CRDA omission flagged in derivation** (CRDA did not classify this pair in its classification table; the recommended DIFFERENT-PERSPECTIVE classification surfaces this in the Downstream-implication). Phase 1 entities with GDPR + DORA applicability must maintain **two separate documentation regimes** (GDPR RoPA + DORA Art. 9(4)(a) information-security policy documentation — no cross-substitution).
- **GDPR ↔ AI_Act** — COMPLEMENTARY (SAME): GDPR RoPA + AI Act Annex IV technical documentation (per Art. 11 + Art. 12(2) traceability) + AI Act Art. 17(1) QMS documentation of 13 enumerated aspects stack for providers/deployers that are controllers processing personal data via high-risk AI. AI Act Recital 78 preserves GDPR (`protection of natural persons in relation to the processing of personal data by Union institutions, bodies, offices and agencies … is governed by Regulation (EU) 2018/1725`; explicit Regulation (EU) 2016/679 preservation). No OJ-level consolidation rule for documentation (the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule does not extend to documentation). Scope-disjoint test: **Conditional (Y when the provider/deployer is a controller processing personal data via high-risk AI)** per CRDA-deep §D-09.4 line 195. No reclassification required. **Phase 1 entities with GDPR + AI Act applicability for a high-risk-AI controller must maintain a layered documentation stack** (GDPR RoPA + AI Act Annex IV technical documentation + AI Act Art. 17 QMS documentation — three parallel artefacts).
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 Art. 24 requires the use of certified ICT products, ICT services, and ICT processes (where Member State or Commission delegated act so requires); CRA Art. 27(8) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements` + Art. 27(9) provide the **CSA-certification presumption-of-conformity machinery**. The two regimes link at the certification boundary (CRA CSA certification substitutes for NIS 2 supplier-side certification assessment). Scope-disjoint test: **Conditional (Y when the NSIE procures CSA-certified CRA products; N otherwise)** per CRDA-deep §D-09.4 line 236. No reclassification required. **Phase 1 entities with NIS 2 + CRA applicability that procure CSA-certified CRA products must maintain a NIS 2 Art. 24 certification-driven record + CRA Art. 27 CSA-certification presumption-of-conformity as upstream gate for NSIE procurements** (Conditional-Y scope overlap).
- **NIS2 ↔ DORA** — COMPLEMENTARY (SAME) — **CRDA-recommended (NOT classified in CRDA table; recommended in Downstream-implication)**: NIS 2 Art. 24 certification-driven recordkeeping + DORA Art. 9(4)(a) information security policy stack for DORA financial entities that are also NSIEs. Different record types (certification-driven records vs. entity-level IS-policy documentation). Scope-disjoint test: **Conditional (Y when the DORA financial entity is also an NSIE)** per CRDA-deep §D-09.4 line 279. No reclassification required — **CRDA omission flagged in derivation** (CRDA did not classify this pair; recommended COMPLEMENTARY classification). Phase 1 entities with NIS 2 + DORA applicability that are also NSIEs + DORA financial entities must maintain **two separate documentation regimes** (NIS 2 Art. 24 certification-driven records + DORA Art. 9(4)(a) IS-policy documentation).
- **NIS2 ↔ AI_Act** — COMPLEMENTARY (SAME) — **CRDA-recommended (NOT classified in CRDA table; recommended in Downstream-implication)**: NIS 2 Art. 24 certification-driven recordkeeping + AI Act Art. 17(1) QMS documentation stack for NSIEs deploying high-risk AI. Different record types (certification-driven records vs. AI-system QMS documentation). Scope-disjoint test: **Conditional (Y when the NSIE deploys high-risk AI)** per CRDA-deep §D-09.4 line 322. No reclassification required — **CRDA omission flagged in derivation**. Phase 1 entities with NIS 2 + AI Act applicability for an NSIE deploying high-risk AI must maintain **two separate documentation regimes** (NIS 2 Art. 24 certification-driven records + AI Act Art. 17 QMS documentation).
- **CRA ↔ DORA** — COMPLEMENTARY (SAME) — **CRDA-recommended (NOT classified in CRDA table; recommended in Downstream-implication)**: CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) information security policy stack when a DORA financial entity procures CRA-conformant products. Different record types (product-level technical documentation vs. entity-level IS-policy documentation). Scope-disjoint test: **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)** per CRDA-deep §D-09.4 line 365. No reclassification required — **CRDA omission flagged in derivation**. Phase 1 entities with CRA + DORA applicability that procures CRA-conformant products must maintain **two separate documentation regimes** (CRA Annex VII technical documentation + DORA Art. 9(4)(a) IS-policy documentation).
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME): CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS stack for AI-enabled products that are both CRA-regulated and AI-Act high-risk. No OJ-level consolidation rule for documentation (unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2 — that rule covers the *risk-assessment object* not the *documentation object*). Scope-disjoint test: **Y (when the CRA-regulated product is also a high-risk AI system)** per CRDA-deep §D-09.4 line 406. No reclassification required. **Phase 1 entities with CRA + AI Act applicability for an AI-enabled product must maintain a layered documentation stack** (CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS — three parallel artefacts).
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME) — **CRDA-recommended (NOT classified in CRDA table; recommended in Downstream-implication)**: DORA Art. 9(4)(a) information security policy + AI Act Art. 17(1) QMS documentation stack when a DORA financial entity deploys high-risk AI. Different record types (entity-level IS-policy documentation vs. AI-system QMS documentation). Scope-disjoint test: **Conditional (Y when the DORA financial entity deploys high-risk AI)** per CRDA-deep §D-09.4 line 449. No reclassification required — **CRDA omission flagged in derivation**. Phase 1 entities with DORA + AI Act applicability for a DORA financial entity deploying high-risk AI must maintain **two separate documentation regimes** (DORA Art. 9(4)(a) IS-policy + AI Act Art. 17 QMS).
The records-of-processing architecture is **legitimately diverse with 5 distinct documentation regimes + DORA fully absent for RoPA + no OJ-level cross-regulation consolidation rule**. The 5 regulators impose documentation regimes from **5 distinct regulatory perspectives** under **5 distinct triggers**, at **5 distinct retention cadences**, and serving **5 distinct audit purposes**: **GDPR RoPA on processing activities** (per-controller / per-processor RoPA mandating Art. 30(1) content items; Art. 30(5) 250-employee exception; Art. 30(3) `in writing, including in electronic form`; Art. 12-14 transparency to data subjects; DPA audit; Art. 30(4) on-supervisory-authority-request); **NIS 2 Art. 24 certification-driven records** (per-Member-State certification requirements per Art. 24(1)/(2)/(3); not codified at OJ level for content — entity-discretionary under Member State transposition); **CRA Annex VII 8-item technical documentation** (per-product technical documentation with Annex VII §1 `general description` + §2 `design, development, production, and vulnerability-handling processes` + §3 `cybersecurity risk assessment` + §4 `support-period determination` + §5 `harmonised standards applied` + §6 `reports of tests carried out` + §7 `copy of the EU declaration of conformity` + §8 `SBOM on MSA reasoned request`; MSA audit; 10-year retention or support period (whichever longer) per Art. 13(13)); **DORA Art. 9(4)(a) information security policy** (per-entity IS policy defining rules to protect CIA+A of data/information assets/ICT assets; NCA audit; no OJ-quantified retention period); **AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs** (per-AI-system technical documentation + 13-element QMS documentation + high-risk-AI-system logs; MSA + AI Office audit; no OJ-quantified retention period for documentation). **No OJ-level cross-regulation consolidation rule for documentation at D-09.4** — the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2 does NOT extend to the documentation object (per CRDA-deep §D-09.4 line 392: "no OJ-level consolidation rule for documentation — unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation"). The 5 documentation regimes operate in parallel with distinct record types, distinct triggers, distinct retention cadences, and distinct recipients; **no OJ-permitted cross-substitution exists** between any pair. The **DORA-absence flag** is structurally significant: per CRDA-deep §D-09.4 line 29, DORA is fully absent for RoPA (no DORA Art. 30 analogue); the DORA Art. 9(4)(a) information security policy is a **different record type** serving a different audit purpose than RoPA. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA | AI_Act |
|---|---|---|---|---|---|
| **GDPR** | — | **N (typically)** — substantively scope-disjoint per CRDA; different record types (RoPA vs. certification-driven Art. 24); different triggers (processing of personal data vs. certification requirement where Member State or Commission delegated act so requires); different audit purposes (DPA audit on processing activities vs. Member-State-driven certification audit) | **N (typically)** — substantively scope-disjoint per CRDA; different record types (RoPA vs. CRA Annex VII 8-item technical documentation); different triggers (processing of personal data vs. product placement on market); different audit purposes (DPA audit on processing activities vs. MSA audit on product cybersecurity); no OJ-level consolidation rule | **N (typically) (CRDA-recommended DIFFERENT-PERSPECTIVE)** — substantively scope-disjoint; different record types (RoPA vs. DORA Art. 9(4)(a) IS-policy documentation); DORA fully absent for RoPA per CRDA explicit note; different audit purposes (DPA audit on processing activities vs. NCA audit on IS policy) | Conditional (Y when the provider/deployer is a controller processing personal data via high-risk AI; N otherwise — GDPR RoPA + AI Act Annex IV + Art. 17 QMS stack on three parallel artefacts; AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation rule for documentation** — the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule does not extend to documentation) |
| **NIS2** | **N (typically)** (same; reciprocal — substantively scope-disjoint per CRDA; RoPA vs. certification-driven records) | — | Conditional (Y when the NSIE procures CSA-certified CRA products; N otherwise — NIS 2 Art. 24 certification-driven records + CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery; two regimes link at the certification boundary) | Conditional (Y when the DORA financial entity is also an NSIE; N otherwise — CRDA-recommended COMPLEMENTARY; NIS 2 Art. 24 certification-driven records + DORA Art. 9(4)(a) IS-policy documentation stack) | Conditional (Y when the NSIE deploys high-risk AI; N otherwise — CRDA-recommended COMPLEMENTARY; NIS 2 Art. 24 certification-driven records + AI Act Art. 17 QMS documentation stack) |
| **CRA** | **N (typically)** (same; reciprocal — substantively scope-disjoint per CRDA; RoPA vs. CRA Annex VII technical documentation; no OJ-level consolidation rule) | Conditional (Y when NSIE procures CSA-certified CRA products; same; reciprocal — CRA Art. 27 CSA-certification presumption as upstream gate for NSIE procurements) | — | Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise — CRDA-recommended COMPLEMENTARY; CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy documentation stack) | Y (CRA-regulated product is also a high-risk AI system; CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS stack on three parallel artefacts; no OJ-level consolidation rule for documentation at D-09.4) |
| **DORA** | **N (typically) (CRDA-recommended)** (same; reciprocal — substantively scope-disjoint; RoPA vs. DORA Art. 9(4)(a) IS-policy documentation; DORA fully absent for RoPA per CRDA explicit note) | Conditional (Y when DORA financial entity is also an NSIE; same; reciprocal — CRDA-recommended COMPLEMENTARY) | Conditional (Y when DORA entity procures CRA-conformant products; same; reciprocal — CRDA-recommended COMPLEMENTARY) | — | Conditional (Y when the DORA financial entity deploys high-risk AI; N otherwise — CRDA-recommended COMPLEMENTARY; DORA Art. 9(4)(a) IS-policy + AI Act Art. 17 QMS stack) |
| **AI_Act** | Conditional (Y when provider/deployer is controller; same; reciprocal — AI Act Recital 78 explicit GDPR preservation; **no OJ-level consolidation rule for documentation**) | Conditional (Y when NSIE deploys high-risk AI; same; reciprocal — CRDA-recommended COMPLEMENTARY) | Y (same; reciprocal — CRA-regulated product is also high-risk AI system; CRA Annex VII + AI Act Annex IV + Art. 17 QMS stack on three parallel artefacts; no OJ-level consolidation rule) | Conditional (Y when DORA financial entity deploys high-risk AI; same; reciprocal — CRDA-recommended COMPLEMENTARY) | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **N (typically)** = substantively scope-disjoint per CRDA — no same-event overlap (high-level SO does **NOT** engage on this pair; the three N (typically) pairs are 3 of the 10 cells: GDPR↔NIS 2, GDPR↔CRA, GDPR↔DORA-recommended). **Conditional (Y/N)** = conditional overlap depending on entity-product combination — Y when the listed entity-product combination applies on a single party, N otherwise. **CRITICAL — DORA fully absent for RoPA per CRDA explicit note** — DORA does not impose a RoPA-equivalent; the DORA Art. 9(4)(a) IS-policy documentation is a different record type serving a different audit purpose. **CRITICAL — no OJ-level consolidation rule for documentation** at D-09.4 — unlike D-09.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *documentation object*. CRDA-deep scope-disjoint tests: GDPR↔NIS2 = **N (typically)** — substantively scope-disjoint; GDPR↔CRA = **N (typically)** — substantively scope-disjoint; GDPR↔DORA = **N (typically)** (CRDA-recommended) — substantively scope-disjoint; GDPR↔AI_Act = Conditional (Y when provider is controller); NIS2↔CRA = Conditional (Y when NSIE procures CSA-certified CRA products); NIS2↔DORA = Conditional (Y when DORA financial entity is also NSIE; CRDA-recommended); NIS2↔AI_Act = Conditional (Y when NSIE deploys high-risk AI; CRDA-recommended); CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products; CRDA-recommended); CRA↔AI_Act = Y (no OJ-level consolidation rule for documentation); DORA↔AI_Act = Conditional (Y when DORA financial entity deploys high-risk AI; CRDA-recommended).

## Cross-recipient map

#### Cross-recipient map
D-09.4 generates a **layered recipient set on the parallel-documentation-regimes evidence trail** but does **not generate a notification cascade of D-09.4 itself**. The recipient set is at the **parallel-documentation-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 30(1) RoPA content items + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency to data subjects; **NIS 2's management body + competent authority** on the Art. 24(1)/(2)/(3) certification-driven records (per-Member-State transposition); **CRA's market surveillance authority (MSA)** on the Annex VII §1-§8 8-item content list + Art. 13(12) pre-market documentation + Art. 13(13) `10-year technical-documentation retention` or support period (whichever longer) + Art. 13(15)/(16) product identification + manufacturer contact info + Art. 13(19) support-period end-date display + Art. 13(20) EU declaration provision + Art. 13(21) immediate corrective measures + Art. 13(22) MSA cooperation + Art. 13(23) cessation-of-operations notification + Art. 13(24)/(25) Commission implementing/delegated acts + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 technical-documentation drawing-up-before-placing + Art. 32 conformity-assessment procedure selection; **DORA's competent authority (NCA — national financial supervisory authority)** on the Art. 9(4)(a) `develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable`; **AI Act's market surveillance authority + AI Office + provider** on the Art. 11 Annex IV technical documentation (per Art. 12(2) traceability) + Art. 17(1) 13-element QMS documentation + Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control`. These are **distinct regulatory channels on the parallel-documentation-regimes artefacts** but they do not generate a notification cascade of D-09.4 itself — they are **compliance-evidence channels on the layered documentation architecture**. The **D-09.1 (Information Security Policies)** is the upstream policy artefact where the documentation regimes are governed by the documented policies; **D-09.3 (Asset Inventories)** is the inventory-evidence downstream artefact where the CRA Annex VII §1-§2 architecture documentation is a sub-register and the DORA Art. 7(1) ICT asset register documentation is the entity-level master record.
---

## HSO considerations (from D-09.4.0 — High-level SecurityObjective)

**Considerations.**
- **5 of 5 regulations participate** on **parallel artefacts** with distinct triggers, retention cadences, and recipients — GDPR Art. 30(1)/(2)/(3)/(4)/(5) RoPA (DPA audit); NIS 2 Art. 24(1)/(2)/(3) certification-driven records per Member State (Member State / competent authority audit); CRA Annex VII §1-§8 8-item technical documentation + Art. 13(12)/(13)/(15)-(25)/(28)/(30)/(31)/(32) (MSA audit, 10-year or support-period retention); DORA Art. 9(4)(a) information security policy (NCA audit — **different record type from RoPA, DORA is fully absent for RoPA-equivalent per CRDA explicit note**); AI Act Art. 11 + Art. 12(1)/(2) + Art. 17(1) 13-element QMS + Art. 19(1) provider logs (MSA + AI Office audit).
- **CRDA-deep verified (10 pairs: 2 SAME — DIFFERENT-PERSPECTIVE — GDPR ↔ NIS 2 + GDPR ↔ CRA — substantively scope-disjoint per CRDA `N (typically)`, different record types; + 3 SAME — COMPLEMENTARY classified by CRDA — GDPR ↔ AI Act, NIS 2 ↔ CRA, CRA ↔ AI Act; + 1 SAME — DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA — GDPR ↔ DORA substantively scope-disjoint; + 4 SAME — COMPLEMENTARY RECOMMENDED-by-CRDA — NIS 2 ↔ DORA, NIS 2 ↔ AI Act, CRA ↔ DORA, DORA ↔ AI Act)** — no CORRECTED, no CONTRADICTORY.
- **DORA-absence flag (CRDA-deep §D-09.4 line 29)**: DORA is fully absent for RoPA-equivalent — no analogue to GDPR Art. 30. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; DORA Art. 9(4)(a) IS-policy documentation is a separate artefact.
- **No OJ-level cross-regulation consolidation rule for documentation** — unlike D-09.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *documentation object*. The 5 documentation regimes operate in parallel; no OJ-permitted cross-substitution exists.
- **Scope caveats**: (a) 3 substantively scope-disjoint pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA) — different record types, different audit purposes; the high-level SO does NOT engage on these pairs alone; (b) the only cross-regulation link involving CRA + NIS 2 is the CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity as upstream gate for NSIE procurements; (c) the 5 documentation regimes must be maintained in parallel even when the product is CRA-conformant and the AI system is AI-Act high-risk.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-09.4 over a distinct **documentation artefact** of the entity's documentation regime; the anchor, governance body, trigger, threshold, retention cadence, recipient, and legal anchor all depend on which perspective the regulation takes on the documentation object.
| Axis (reg) | Documentation artefact | Anchor (OJ-literal) | Governance body | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | controller/processor records of processing activities (RoPA) + transparency to data subjects on processing operations (Art. 12-14) | Art. 30(1) `record of processing activities under its responsibility` + Art. 30(2) processor RoPA + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency | controller (Art. 4(7) `the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data`) + processor (Art. 4(8)) + DPO (Art. 37-39) | supervisory authority (DPA) + data subjects — Art. 30(1) content items (name/contact details of controller; purposes; categories of data subjects and of personal data; categories of recipients; transfers to third country; envisaged time limits for erasure; general description of technical and organisational security measures) + Art. 30(4) on-DPA-request + Art. 12-14 transparency | Art. 30(1) `(a) … (g)` 7-item content + Art. 30(2) processor RoPA content + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 5(2) accountability |
| **NIS 2** | certification-driven recordkeeping — Member-State-driven use of certified ICT products, ICT services, and ICT processes per Art. 24 | Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` + Art. 24(1) sentence 2 qualified trust services encouragement + Art. 24(2) Commission delegated acts + Art. 24(3) ENISA candidate scheme request — **not codified at OJ level for content — entity-discretionary under Member State transposition** | management body + Member State — Art. 24(1)/(2)/(3) per Member State | management body + competent authority — Art. 24(1)/(2)/(3) certification-driven records per Member State | Art. 24(1) sentence 1 + Art. 24(1) sentence 2 + Art. 24(2) + Art. 24(3) |
| **CRA** | product-level technical documentation: Annex VII 8-item content list (general description + design/development/vulnerability-handling processes + risk assessment + support-period determination + standards applied + test reports + EU declaration copy + SBOM on MSA reasoned request) + pre-market documentation + EU declaration + CE marking + product identification + manufacturer contact info + support-period end-date + EU declaration provision + immediate corrective measures + MSA cooperation + cessation-of-operations notification + Commission implementing/delegated acts + conformity-assessment procedure selection | Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` + Art. 13(12) sentence 2 EU declaration + CE marking + Art. 13(13) `10 years … or for the support period, whichever is longer` + Annex VII §1-§8 8-item content list (per SR-CRA-087 + SR-CRA-088) | manufacturer (Art. 13 manufacturer obligations owner — cross to D-09.1) + MSA oversight — distinct from data-protection governance body | market surveillance authority (MSA) — Art. 13(12)/(13) + Annex VII §1-§8 + Art. 13(15)/(16) + Art. 13(17) SPOC + Art. 13(19) + Art. 13(20) + Art. 13(21) + Art. 13(22) + Art. 13(23) + Art. 13(24)/(25) + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 technical-documentation drawing-up-before-placing + Art. 32 conformity-assessment procedure selection | Art. 13(12) + Art. 13(13) 10-year retention + Art. 13(15)/(16) + Art. 13(17) SPOC + Art. 13(19) + Art. 13(20) + Art. 13(21) + Art. 13(22) + Art. 13(23) + Art. 13(24)/(25) Commission acts + Annex II §1/§2/§3/§6/§7 + Annex VII §1-§8 + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 drawing-up-before-placing + Art. 32 conformity-assessment procedure |
| **DORA** | entity-level information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets — **different record type from GDPR RoPA; DORA is fully absent for RoPA-equivalent per CRDA explicit note** | Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` (per SR-DORA-031) | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible — cross to D-09.1) + control function with appropriate level of independence per three-lines-of-defence (Art. 6(4) — cross to D-09.3) | competent authority (NCA — national financial supervisory authority) + management body — Art. 9(4)(a) IS-policy documentation serving NCA audit purposes | Art. 9(4)(a) (per SR-DORA-031) + Art. 6(4) three-lines-of-defence + Art. 5(2) management-body oversight + Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities` |
| **AI Act** | AI-system-specific technical documentation (Annex IV via Art. 11/12 traceability) + QMS documentation of 13 enumerated aspects (Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions`) + high-risk-AI-system logs per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` | Art. 11 technical documentation + Art. 12(1) automatic recording of events + Art. 12(2) traceability + Art. 17(1) 13-element QMS closed list (a)-(m) + Art. 19(1) log retention (per SR-AIACT-008) | provider (high-risk AI system provider with Art. 17(1) QMS + Art. 11 technical documentation + Art. 19(1) log retention) — distinct from MSA / AI Office oversight | provider + deployer + MSA + AI Office — Art. 11 + Art. 12(1)/(2) + Art. 17(1) 13-element QMS + Art. 19(1) log retention | Art. 11 + Art. 12(1) + Art. 12(2) + Art. 17(1) + Art. 19(1) + Art. 13(1)+(3) transparency-to-deployers (cross) |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
(See the validated-relationships table above for the 5×5 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-09.4.HL`) engages on a given party **if and only if ≥2 applicable
regulations have ≥1 Y or Conditional-Y-scope-overlap pair on the same
party** where both regimens operate on the **same documentation object
serving the same audit purpose**. For an integrated AI-enabled CRA-
regulated product that is also a high-risk AI system (an AI provider
that is also a manufacturer + high-risk AI provider), the **CRA ↔ AI
Act Y pair** engages the high-level SO with the documentation stack
(CRA Annex VII + AI Act Annex IV + AI Act Art. 17 QMS — three parallel
artefacts serving distinct audit purposes: CRA MSA audit + AI Act MSA +
AI Office audit). For a DORA financial entity that is also an NSIE and
that procures CRA-conformant products (DORA financial entity + NSIE +
CRA-conformant-product procurements), the **NIS 2 ↔ DORA Conditional-Y
+ CRA ↔ DORA Conditional-Y** pairs engage the high-level SO with the
parallel documentation regimes (NIS 2 Art. 24 certification-driven
records + DORA Art. 9(4)(a) IS-policy + CRA Annex VII 8-item technical
documentation). For a controller that is also an NSIE and deploys
high-risk AI (a controller + NSIE + high-risk-AI deployer), the **GDPR
↔ AI Act Conditional-Y + NIS 2 ↔ AI Act Conditional-Y** pairs engage
the high-level SO with the parallel documentation regimes (GDPR RoPA +
AI Act Annex IV + AI Act Art. 17 QMS + NIS 2 Art. 24 certification
records). For a DORA financial entity that is also a controller
deploying high-risk AI (a DORA financial entity + controller + high-
risk-AI deployer/processor), the **DORA ↔ AI Act Conditional-Y + GDPR
↔ DORA N (typically)-recommended** pairs engage the high-level SO
with **specific scope** — GDPR RoPA as the dedicated authority for
processing-activities documentation (per CRDA explicit DORA-absence
flag) + DORA Art. 9(4)(a) IS-policy documentation as a separate
artefact + AI Act Annex IV + AI Act Art. 17 QMS. **The 3 substantively
scope-disjoint pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA) never
engage the high-level SO together** — different record types serving
different audit purposes; CRDA `different-perspective` is a taxonomy
artifact (per CRDA-deep §D-09.4 lines 68, 110, 153) for these three
pairs. The 5 documentation regimes are stacked in parallel, not
collapsed: GDPR Art. 30 RoPA (controller / processor RoPA); NIS 2
Art. 24 certification-driven records (per Member State); CRA Annex VII
8-item technical documentation + EU declaration + CE marking (per
manufacturer); DORA Art. 9(4)(a) IS-policy documentation (per financial
entity); AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs (per
provider). The high-level SO surfaces the **common documentation-regime
duty** but does **NOT** collapse the 5 documentation regimes into a
single artefact; the per-reg perspective on the artefact, anchor,
governance body, content template, retention cadence, recipient, and
evidence template is preserved verbatim.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **5 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA, AI Act —
  all five participate on the documentation object): GDPR (Art. 30(1)
  + Art. 30(2) + Art. 30(3) + Art. 30(4) + Art. 30(5) + Art. 12-14 as
  controller/processor RoPA mandating the 7-item content); NIS 2 (Art.
  24(1)/(2)/(3) as per-Member-State certification-driven recordkeeping
  — not a RoPA-equivalent); CRA (Annex VII §1-§8 8-item technical
  documentation + Art. 13(12) + Art. 13(13) 10-year retention +
  Art. 13(15)/(16) + Art. 13(17) + Art. 13(19) + Art. 13(20) +
  Art. 13(21) + Art. 13(22) + Art. 13(23) + Art. 13(24)/(25) +
  Art. 28 + Art. 30 + Art. 31 + Art. 32 as product-level technical
  documentation regime); DORA (Art. 9(4)(a) as entity-level
  information security policy — different record type, **fully absent
  for RoPA-equivalent** per CRDA explicit note); AI Act (Art. 11 +
  Art. 12(1)/(2) + Art. 17(1) + Art. 19(1) as AI-system-specific
  technical documentation + 13-element QMS + provider logs).
- **10 pairwise cells, verified by CRDA-deep**:
  GDPR↔NIS2 (SAME — DIFFERENT-PERSPECTIVE — substantively scope-
  disjoint per CRDA `N (typically)` — different record types, RoPA vs.
  certification-driven Art. 24; substantively scope-disjoint);
  GDPR↔CRA (SAME — DIFFERENT-PERSPECTIVE — substantively scope-
  disjoint per CRDA `N (typically)` — different record types, RoPA vs.
  CRA Annex VII 8-item technical documentation; substantively scope-
  disjoint);
  GDPR↔DORA (SAME — DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA —
  substantively scope-disjoint per CRDA `N (typically)`; RoPA vs.
  DORA Art. 9(4)(a) IS-policy documentation; DORA fully absent for
  RoPA per CRDA explicit note);
  GDPR↔AI_Act (SAME — COMPLEMENTARY — Conditional-Y when
  provider/deployer is controller processing personal data via high-
  risk AI; GDPR RoPA + AI Act Annex IV + AI Act Art. 17 QMS stack
  on three parallel artefacts; AI Act Recital 78 explicit GDPR
  preservation; **no OJ-level consolidation rule for documentation**);
  NIS2↔CRA (SAME — COMPLEMENTARY — Conditional-Y when NSIE procures
  CSA-certified CRA products; NIS 2 Art. 24 + CRA Art. 27(8)/(9)
  CSA-certification presumption-of-conformity machinery as upstream
  gate for NSIE procurements);
  NIS2↔DORA (SAME — COMPLEMENTARY RECOMMENDED-by-CRDA — Conditional-Y
  when DORA financial entity is also an NSIE);
  NIS2↔AI_Act (SAME — COMPLEMENTARY RECOMMENDED-by-CRDA —
  Conditional-Y when NSIE deploys high-risk AI);
  CRA↔DORA (SAME — COMPLEMENTARY RECOMMENDED-by-CRDA — Conditional-Y
  when DORA entity procures CRA-conformant products; CRA Annex VII
  8-item technical documentation + DORA Art. 9(4)(a) IS-policy
  documentation stack);
  CRA↔AI_Act (SAME — COMPLEMENTARY — Y when CRA-regulated product is
  also a high-risk AI system; CRA Annex VII + AI Act Annex IV + AI
  Act Art. 17 QMS stack on three parallel artefacts; **no OJ-level
  consolidation rule for documentation at D-09.4** — unlike the CRA
  Art. 13(4) sentence 2 risk-assessment consolidation rule at D-09.2,
  that rule covers the *risk-assessment object* not the *documentation
  object*);
  DORA↔AI_Act (SAME — COMPLEMENTARY RECOMMENDED-by-CRDA —
  Conditional-Y when DORA financial entity deploys high-risk AI; DORA
  Art. 9(4)(a) IS-policy + AI Act Art. 17 QMS stack).
- The **DORA-absence flag** is structurally significant: per CRDA-
  deep §D-09.4 line 29, **DORA is fully absent for RoPA-equivalent**
  — DORA does not impose a RoPA obligation (no analogue to GDPR Art.
  30). The DORA Art. 9(4)(a) information security policy is a
  **different record type** (entity-level IS-policy documentation)
  serving a different audit purpose (NCA audit on IS policy) than
  the GDPR RoPA (DPA audit on processing activities). **For DORA
  financial entities, the GDPR RoPA remains the dedicated authority
  for processing-activities documentation**; the DORA Art. 9(4)(a)
  IS-policy documentation is a separate artefact (cross to D-09.1).
- The **no OJ-level consolidation rule for documentation** is
  structurally significant: **unlike D-09.2** where **CRA Art.
  13(4) sentence 2** permits AI Act Art. 9 risk-management to
  substitute for CRA risk assessment (the only OJ-level cross-
  regulation consolidation rule in D-09.2), the documentation
  object at D-09.4 has **no OJ-level cross-regulation consolidation
  rule** (per CRDA-deep §D-09.4 line 392: "no OJ-level consolidation
  rule for documentation — unlike the CRA Art. 13(4) sentence 2
  risk-assessment consolidation"). The 5 documentation regimes
  operate in parallel; no OJ-permitted cross-substitution exists
  between any pair. Phase 1 entities with ≥2 of the 5 participating
  regs applicability must maintain parallel documentation regimes.
- The 5 participating regulators impose **distinct documentation
  artefacts** at **distinct anchors** with **distinct governance
  bodies**, **distinct content templates**, **distinct retention
  cadences**, and **distinct recipients**: GDPR (Art. 30(1) 7-item
  content; Art. 30(5) 250-employee exception; Art. 30(3) `in
  writing, including in electronic form`; DPA audit;
  substantively scope-disjoint from NIS 2 / CRA / DORA-recommended /
  DORA per CRDA explicit N (typically) for the first 3); NIS 2
  (Art. 24(1) per-Member-State certification-driven records; not
  codified at OJ level for content — entity-discretionary under
  Member State transposition); CRA (Annex VII §1-§8 8-item content;
  Art. 13(13) 10-year retention or support period (whichever
  longer); MSA audit; substantively scope-disjoint from GDPR per
  CRDA `N (typically)`); DORA (Art. 9(4)(a) IS-policy documentation;
  no OJ-quantified retention period; NCA audit; different record
  type from RoPA; DORA-absence flag); AI Act (Annex IV technical
  documentation + Art. 17(1) 13-element QMS + Art. 19(1) logs;
  no OJ-quantified retention period for documentation; MSA + AI
  Office audit). The thresholds/cadences align qualitatively (no
  regulation imposes a single retention period — GDPR until
  processing ceases + on-DPA-request; CRA 10 years or support
  period, whichever longer; AI Act no OJ-quantified retention for
  documentation; DORA no OJ-quantified retention; NIS 2 per Member
  State). The 5 anchors align in their direction-of-travel (records
  of processing + technical documentation + certification records +
  IS-policy + QMS) but the artefacts, governance bodies, content
  templates, retention cadences, recipients, evidentiary templates
  diverge.
- The high-level SO describes the **COMMON OBJECTIVE** (records of
  processing activities + technical documentation + certification
  records + IS-policy documentation + QMS documentation + provider
  logs on parallel artefacts); the **per-regulation perspective**
  (artefact, governance body, anchor, content template, retention
  cadence, recipient, evidence template) is preserved verbatim in
  the 5 sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the documentation duty
  itself**, because no pair was verified as CONTRADICTORY or
  CORRECTED (all 10 pairs are SAME — 2 SAME — DIFFERENT-PERSPECTIVE
  + 3 SAME — COMPLEMENTARY-classified-by-CRDA + 1 SAME — DIFFERENT-
  PERSPECTIVE-recommended-by-CRDA + 4 SAME — COMPLEMENTARY-
  recommended-by-CRDA). Phase 1C Doc 07 does not need to resolve a
  documentation-object contradiction because none exist by
  construction; however, **Phase 1C Doc 07 must perform the Layer 1
  cross-cutting documentation-architecture mapping** because the 5
  regulators impose 5 distinct documentation regimes with:
  (a) **3 substantively scope-disjoint pairs** (GDPR ↔ NIS 2 + GDPR
  ↔ CRA + GDPR ↔ DORA — substantively scope-disjoint per CRDA `N
  (typically)`; CRDA `different-perspective` is a taxonomy artifact
  for these three pairs);
  (b) **DORA fully absent for RoPA-equivalent** (DORA-absence flag);
  (c) **no OJ-level consolidation rule for documentation** at D-09.4
  (unlike D-09.2 where CRA Art. 13(4) sentence 2 consolidation rule
  covers the risk-assessment object).
- **Scope caveat (CRITICAL — DORA-absence flag)** — derived from
  CRDA-deep verified classifications: DORA is fully absent for
  RoPA-equivalent per CRDA-deep §D-09.4 line 29. The DORA Art.
  9(4)(a) information security policy is a different record type
  (entity-level IS-policy documentation) serving a different audit
  purpose (NCA audit on IS policy) than the GDPR RoPA (DPA audit on
  processing activities). **For DORA financial entities, the GDPR
  RoPA remains the dedicated authority for processing-activities
  documentation**; the DORA Art. 9(4)(a) IS-policy documentation is
  a separate artefact. Phase 1 entities with DORA + GDPR
  applicability must maintain parallel documentation regimes (GDPR
  RoPA + DORA Art. 9(4)(a) IS-policy documentation — no cross-
  substitution possible).
- **Scope caveat (CRITICAL — no OJ-level consolidation rule for
  documentation at D-09.4)** — derived from CRDA-deep verified
  classifications: per CRDA-deep §D-09.4 line 392, **unlike D-09.2**
  where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-
  management to substitute for CRA risk assessment, the documentation
  object at D-09.4 has no OJ-level consolidation rule. The 5
  documentation regimes operate in parallel; no OJ-permitted cross-
  substitution exists. Phase 1 entities with ≥2 of the 5
  participating regs applicability must maintain parallel
  documentation regimes even when the underlying product is CRA-
  conformant and the underlying AI system is AI-Act high-risk.
- **Scope caveat (CRITICAL — GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA
  substantive scope-disjoint flag)** — derived from CRDA-deep
  verified classifications: the **3 same-row pairs with `N
  (typically)`** (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA-
  recommended) are substantively scope-disjoint per CRDA — different
  record types (RoPA vs. certification-driven records + CRA Annex
  VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy
  documentation) serving different audit purposes (DPA audit on
  processing activities vs. Member-State-driven certification audit +
  MSA audit on product cybersecurity + NCA audit on IS policy). The
  three regimes meet at **no consolidation interface**; CRDA
  `different-perspective` is a taxonomy artifact (per CRDA-deep §D-
  09.4 lines 68, 110, 153) for these three pairs.
---

## Emergent tensions (from CRDA-deep §D-09.4)

#### Emergent tensions (from CRDA-deep §D-09.4)
**0 conditional emergent tensions** on the documentation duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 10 pairs are all SAME — 2 SAME — DIFFERENT-PERSPECTIVE + 3 SAME — COMPLEMENTARY-classified-by-CRDA + 1 SAME — DIFFERENT-PERSPECTIVE-recommended-by-CRDA + 4 SAME — COMPLEMENTARY-recommended-by-CRDA. **No CORRECTED, no CONTRADICTORY** pairs. **No scope-disjoint CONTRADICTORY** — the 3 `N (typically)` pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA-recommended) are substantively scope-disjoint on the documentation-object dimension, not on the policy-object dimension; the high-level SO does **NOT** engage on these pairs because no same-event overlap exists, but this is **not** an emergent tension requiring Phase 1C resolution.
The **DORA-absence flag (CRDA-deep §D-09.4 line 29)** is the structurally significant operational divergence — DORA is fully absent for RoPA-equivalent (no analogue to GDPR Art. 30); the DORA Art. 9(4)(a) information security policy is a **different record type** serving a **different audit purpose**. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact (cross to D-09.1 DORA sub-SO). Phase 1 entities with GDPR + DORA applicability must maintain both GDPR RoPA + DORA Art. 9(4)(a) IS-policy documentation on distinct artefacts that are not substitutable.
The **no OJ-level consolidation rule for documentation flag (CRDA-deep §D-09.4 line 392)** is the structurally significant operational divergence — unlike D-09.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management to substitute for CRA risk assessment (the only OJ-level cross-regulation consolidation rule in D-09.2), the documentation object at D-09.4 has **no OJ-level cross-regulation consolidation rule**. Phase 1 entities with ≥2 of the 5 participating regs applicability must maintain **parallel documentation regimes** even when the underlying product is CRA-conformant and the underlying AI system is AI-Act high-risk. **No cross-substitution is OJ-permitted**.
The **3 substantively scope-disjoint pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA-recommended)** are the structurally significant operational divergence — these 3 pairs operate on **different record types** (RoPA vs. certification-driven records + CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy documentation) serving **different audit purposes** (DPA audit on processing activities vs. Member-State-driven certification audit + MSA audit on product cybersecurity + NCA audit on IS policy). CRDA `different-perspective` is a taxonomy artifact (per CRDA-deep §D-09.4 lines 68, 110, 153) for these three pairs. Phase 1 entities with GDPR + CRA + NIS 2 applicability must maintain **three separate documentation regimes** (GDPR RoPA + CRA Annex VII technical documentation + NIS 2 Art. 24 certification-driven records on distinct artefacts serving distinct audit purposes).
The **5 parallel documentation regimes** are the structurally significant compliance-architecture: **GDPR Art. 30 RoPA on processing activities** + **NIS 2 Art. 24 certification-driven records** + **CRA Annex VII 8-item technical documentation + EU declaration + CE marking** + **DORA Art. 9(4)(a) IS-policy documentation** + **AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs**. The 5 regimes operate in parallel with distinct record types, distinct triggers, distinct retention cadences, and distinct recipients. **No OJ-level cross-substitution exists** between any pair. Phase 1 entities with all 5 participating regs applicability (a DORA financial entity that is also a controller + NSIE + manufacturer + high-risk-AI provider) must maintain **5 parallel documentation regimes** serving 5 distinct audit purposes.
The **CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery** is the **only cross-regulation link at D-09.4 involving CRA + NIS 2** — when an NSIE procures CSA-certified CRA products, the CRA Art. 27(8)/(9) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements` is the upstream gate for NIS 2 procurements.
The high-level SO surfaces the **common documentation-regime duty** (records of processing activities + technical documentation + certification records + IS-policy documentation + QMS documentation + provider logs) on **parallel artefacts** serving distinct audit purposes; the per-reg perspective on the artefact, anchor, governance body, content template, retention cadence, recipient, and evidence template is documented separately in the 5 sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 5-distinct-documentation-regimes structure (GDPR Art. 30 RoPA + NIS 2 Art. 24 + CRA Annex VII 8-item + DORA Art. 9(4)(a) + AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs) with **DORA-absence flag + no OJ-level consolidation rule for documentation + 3 substantively scope-disjoint pairs (GDPR ↔ NIS 2 / CRA / DORA-recommended)** is itself the structurally significant compliance-architecture that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-09.4 — with overlapping documentation scope-determiners on the same party — operates **5 parallel documentation regimes** (GDPR Art. 30 RoPA + NIS 2 Art. 24 + CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy documentation + AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs) on **distinct artefacts** serving **distinct audit purposes**. The high-level SO (`SO-D-09.4.HL`) describes the **common documentation-regime duty** (records of processing activities + technical documentation + certification records + IS-policy documentation + QMS documentation + provider logs) on parallel artefacts; the per-reg perspective is preserved in the 5 sub-SOs (artefact, governance body, anchor, content template, retention cadence, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 5-parallel-documentation-regimes operationalising the per-reg governance body on the integrated documentation architecture. The high-level SO does NOT collapse the 5 documentation regimes into a single artefact; the per-reg perspective on the artefact, governance body, anchor, content template, retention cadence, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **documentation-architecture strategy**: (1) a **5-parallel-documentation-regimes architecture** with explicit governance-body hand-offs (GDPR Art. 30(1) RoPA + Art. 12-14 transparency → NIS 2 Art. 24(1)/(2)/(3) certification-driven records → CRA Annex VII §1-§8 8-item technical documentation + Art. 13(12)/(13)/(15)/(16)/(17)/(19)/(20)/(21)/(22)/(23)/EU declaration/CE marking → DORA Art. 9(4)(a) IS-policy documentation → AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs); (2) the **DORA-absence flag** preserving GDPR RoPA as the dedicated authority for processing-activities documentation even for DORA financial entities (GDPR Art. 30 RoPA + DORA Art. 9(4)(a) IS-policy documentation on parallel artefacts serving distinct audit purposes); (3) the **no OJ-level consolidation rule for documentation** distinguishing D-09.4 from D-09.2 (the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule covers the *risk-assessment object* but not the *documentation object* at D-09.4); (4) the **3 substantively scope-disjoint pairs** (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA-recommended) preserving GDPR RoPA on processing activities from cross-substitution by NIS 2 Art. 24 + CRA Annex VII + DORA Art. 9(4)(a); (5) the **CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery** as the only cross-regulation link at D-09.4 involving CRA + NIS 2 — when an NSIE procures CSA-certified CRA products, the CRA Art. 27(8)/(9) is the upstream gate for NIS 2 procurements (Conditional-Y scope overlap); (6) the **5 distinct retention cadences** (GDPR until processing ceases + on-DPA-request; CRA 10 years or support period, whichever longer; AI Act no OJ-quantified retention for documentation; DORA no OJ-quantified retention; NIS 2 per Member State) — Phase 1C Doc 07 must perform the Layer 1 cross-cutting retention-cadence reconciliation; (7) the **CRDA NOT-CLASSIFIED pairs** (GDPR ↔ DORA, NIS 2 ↔ DORA, NIS 2 ↔ AI Act, CRA ↔ DORA, DORA ↔ AI Act) — 4 of 5 are recommended-COMPLEMENTARY + 1 is recommended-DIFFERENT-PERSPECTIVE per CRDA explicit Downstream-implication lines; Phase 1C Doc 07 documents the recommended classifications as the operational reading; (8) the **convergent NIST CSF 2.0 Subcategories** ID.AM-08 + PR.DS-12 anchor the data-lifecycle + risk-strategy consistency as the common documentation objective; GDPR additionally maps GV.PO-02 for demonstrable-compliance; CRA additionally maps ID.RA-05 for risk-assessment documentation.
---
**Document version:** 0.1 — initial derivation from CRDA-deep §D-09.4 (10 pairs verified; 5 pairs CRDA-classified + 5 pairs CRDA-recommended; 3 substantively scope-disjoint pairs surfaced + DORA-absence flag + no OJ-level consolidation rule for documentation at D-09.4).
**See also:** [`D-09.1.md`](D-09.1.md) (Information Security Policies — 5-reg participation with no OJ-level consolidation rule); [`D-09.2.md`](D-09.2.md) (Impact & Risk Assessments — 5-reg participation with the **only OJ-level cross-regulation consolidation rule** at CRA Art. 13(4) sentence 2 / AI Act Art. 9 risk-management system; the contrast with D-09.4 is significant — *risk-assessment object* cross-substitutes but *documentation object* does NOT); [`D-09.3.md`](D-09.3.md) (Asset Inventories — 3-reg participation with DORA Art. 7(1) as the **dedicated authority** per AEGIS taxonomy §4.1 + NIS 2 + CRA partial coverage; substantive NIS 2 ↔ CRA scope-disjoint); [`index.md`](../index.md); [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md) (CRDA-deep source).

## Part 1 §3 — context

### 3. Security Requirements
## 9.4 Records of Processing — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md`. See that file for the CRDA-deep verified classification (10 pairs: 2 SAME — DIFFERENT-PERSPECTIVE — GDPR ↔ NIS 2 + GDPR ↔ CRA — substantively scope-disjoint per CRDA `N (typically)`, different record types; + 3 SAME — COMPLEMENTARY classified by CRDA — GDPR ↔ AI Act, NIS 2 ↔ CRA, CRA ↔ AI Act; + 1 SAME — DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA — GDPR ↔ DORA substantively scope-disjoint; + 4 SAME — COMPLEMENTARY RECOMMENDED-by-CRDA — NIS 2 ↔ DORA, NIS 2 ↔ AI Act, CRA ↔ DORA, DORA ↔ AI Act) — no CORRECTED, no CONTRADICTORY; **5 of 5 regulations participate**; the **DORA-absence flag (CRDA-deep §9.4 line 29)** — DORA is fully absent for RoPA-equivalent (no GDPR Art. 30 analogue); DORA Art. 9(4)(a) information security policy is a different record type serving a different audit purpose (NCA audit on IS policy vs. DPA audit on processing activities); for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; **no OJ-level consolidation rule for documentation at 9.4** (the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at 9.2 covers the *risk-assessment object* not the *documentation object*); the per-reg 5-distinct-documentation-artefact architecture (GDPR Art. 30(1)/(2)/(3)/(4)/(5) RoPA + Art. 12-14 transparency; NIS 2 Art. 24(1)/(2)/(3) certification-driven records per Member State; CRA Annex VII §1-§8 8-item technical documentation + Art. 13(12)-(25)/(28)/(30)/(31)/(32) + 10-year or support-period retention; DORA Art. 9(4)(a) information security policy — different record type from RoPA; AI Act Art. 11 + Art. 12(1)/(2) + Art. 17(1) 13-element QMS + Art. 19(1) provider logs), the 3 substantively scope-disjoint pairs (GDPR ↔ NIS 2 / CRA / DORA-recommended) operating on different record types serving different audit purposes, the NIS 2 ↔ CRA CSA-certification presumption-of-conformity link via CRA Art. 27(8)/(9), the 5 parallel documentation regimes on distinct artefacts (no cross-substitution OJ-permitted), the per-reg documentation artefact / governance body / anchor / content template / threshold / retention cadence / recipient / evidence template, and the aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA, AI Act (ALL 5 participate on the documentation object). The five regulators each impose a **distinct documentation regime** under a **distinct anchor** at a **distinct trigger** with a **distinct retention cadence** and serving a **distinct audit purpose**: GDPR (Art. 30(1) `record of processing activities under its responsibility` + Art. 30(1) (a)-(g) 7-item content + Art. 30(2) processor RoPA + Art. 30(3) `in writing, including in electronic form` + Art. 30(4) on-supervisory-authority-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency to data subjects + Art. 5(2) accountability burden) — controller/processor RoPA mandating the 7-item content; DPA audit; substantively scope-disjoint from NIS 2 + CRA per CRDA `N (typically)`; NIS 2 (Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` + Art. 24(1) sentence 2 qualified trust services encouragement + Art. 24(2) Commission delegated acts + Art. 24(3) ENISA candidate scheme request) — certification-driven recordkeeping per Member State; not codified at OJ level for content — entity-discretionary under Member State transposition; substantively scope-disjoint from GDPR per CRDA `N (typically)`; CRA (Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` + Art. 13(12) sentence 2 EU declaration + CE marking + Art. 13(13) `10 years … or for the support period, whichever is longer` + Annex VII §1-§8 8-item content list + Art. 13(15)/(16)/(17)/(19)/(20)/(21)/(22)/(23)/(24)/(25) + Art. 28 EU declaration + Art. 30 CE marking + Art. 31 drawing-up-before-placing + Art. 32 conformity-assessment procedure selection) — product-level technical documentation; MSA audit; substantively scope-disjoint from GDPR per CRDA `N (typically)`; DORA (Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` + Art. 6(4) three-lines-of-defence + Art. 5(2) management-body oversight) — entity-level IS-policy documentation; NCA audit; **DORA is fully absent for RoPA-equivalent per CRDA explicit note**; AI Act (Art. 11 `technical documentation … in accordance with Annex IV` + Art. 12(1) automatic recording + Art. 12(2) traceability + Art. 17(1) `systematic and orderly manner in the form of written policies, procedures and instructions` 13-element closed list (a)-(m) + Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control`) — AI-system-specific technical documentation + 13-element QMS + provider logs; MSA + AI Office audit.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 9.4
  volere_section: 15
  volere_subtype: audit
  title: "Records of processing activities established through 5 parallel documentation regimes on distinct artefacts serving distinct audit purposes, with DORA fully absent for RoPA-equivalent and no OJ-level cross-substitution permitted"
  derives_from:
    hso_sub_so: SO-9.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.4.md
    objective_ref_section: "### 9.4.0"
  description: |
    The product shall establish records of processing activities through 5 parallel documentation regimes on distinct artefacts serving distinct audit purposes (GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records + CRA Annex VII 8-item technical documentation + DORA Art. 9(4)(a) IS-policy documentation + AI Act Annex IV + Art. 17(1) QMS + Art. 19(1) logs), where ≥2 of the participating regulations (GDPR, NIS 2, CRA, DORA, AI Act) have applicability with overlapping documentation scope-determiners on the same party, with the per-reg documentation artefact, governance body, anchor, content template, threshold, retention cadence, recipient, and evidence template preserved verbatim in the 5 sub-SOs, with DORA-absence flag preserved (GDPR RoPA remains the dedicated authority for processing-activities documentation even for DORA financial entities), and with no OJ-permitted cross-substitution between any pair.
  fit_criterion: |
    A 5-parallel-documentation-regimes architecture is established with explicit governance-body hand-offs at the documentation-evidence layer: (1) **GDPR Art. 30(1)/(2)/(3)/(4)/(5) RoPA** — controller/processor record of processing activities with the Art. 30(1) (a)-(g) 7-item content list (name/contact details of controller; purposes; categories of data subjects and personal data; categories of recipients; transfers to third country; envisaged time limits for erasure; general description of TOMs), in writing or electronic form per Art. 30(3), made available to the DPA on request per Art. 30(4), subject to the Art. 30(5) 250-employee exception; the DPA audit channel; substantively scope-disjoint from NIS 2 / CRA per CRDA `N (typically)`; (2) **NIS 2 Art. 24(1)/(2)/(3) certification-driven records** — Member-State-driven use of European or internationally accepted standards + qualified trust services encouragement + Commission delegated acts + ENISA candidate scheme request; entity-discretionary under Member State transposition; substantively scope-disjoint from GDPR per CRDA `N (typically)`; (3) **CRA Annex VII §1-§8 8-item technical documentation** — general description (§1) + design, development, production, vulnerability-handling processes (§2) + cybersecurity risk assessment (§3) + support-period determination (§4) + harmonised standards applied (§5) + reports of tests carried out (§6) + copy of EU declaration of conformity (§7) + SBOM on MSA reasoned request (§8); drawn up before placing on market per Art. 31(2); retained at MSA disposal for at least 10 years or the support period, whichever longer, per Art. 13(13); substantively scope-disjoint from GDPR per CRDA `N (typically)`; (4) **DORA Art. 9(4)(a) information security policy** — entity-level IS-policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets including those of customers where applicable; **different record type from GDPR RoPA**; DORA-absence flag preserved (per CRDA-deep §9.4 line 29, DORA is fully absent for RoPA-equivalent; for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation); (5) **AI Act Art. 11 + Art. 12(1)/(2) + Art. 17(1) + Art. 19(1)** — Annex IV technical documentation (per Art. 12(2) traceability) + Art. 17(1) 13-element QMS closed list (a)-(m) in systematic-and-orderly manner + Art. 19(1) provider logs under their control; MSA + AI Office audit. The 5 regimes operate in parallel with distinct record types, distinct triggers, distinct retention cadences, and distinct recipients. **No OJ-permitted cross-substitution exists** between any pair — the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at 9.2 covers the *risk-assessment object* not the *documentation object*. Verified by per-recipient evidence packs (DPA RoPA, Member State/competent authority certification records, MSA Annex VII technical file, NCA IS-policy documentation, MSA + AI Office Annex IV + QMS + logs) + automated artefact-distinctness test (no field-level overlap between RoPA Art. 30(1)(a)-(g) and Annex VII §1-§8 content lists; no field-level overlap between DORA Art. 9(4)(a) IS-policy and GDPR Art. 30(1) RoPA).
  priority: MUST
  verification_method: TEST
  dependencies: [9.4.1, 9.4.2, 9.4.3, 9.4.4, 9.4.5]
  nist_csf: [ID.AM-08, PR.DS-12, GV.PO-02]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: Conditional   # HL engages when ≥2 applicable regs have ≥1 Y or Conditional-Y-scope-overlap pair on the same party; for 9.4 the matrix shows 7 pairs with Y or Conditional-Y activation on the joint-condition operator (GDPR↔AI_Act = Conditional-Y when provider/deployer is controller; NIS2↔CRA = Conditional-Y when NSIE procures CSA-certified CRA products; NIS2↔DORA = Conditional-Y when DORA financial entity is also NSIE; NIS2↔AI_Act = Conditional-Y when NSIE deploys high-risk AI; CRA↔DORA = Conditional-Y when DORA entity procures CRA-conformant products; CRA↔AI_Act = Y when CRA-regulated product is also high-risk AI; DORA↔AI_Act = Conditional-Y when DORA financial entity deploys high-risk AI). The 3 substantively scope-disjoint pairs (GDPR↔NIS 2, GDPR↔CRA, GDPR↔DORA-recommended) are `N (typically)` — different record types serving different audit purposes; the HL does NOT engage on these pairs alone (no same-event overlap). The HL engages on the 7 same-event activation pairs and surfaces the common documentation-regime duty on parallel artefacts; the per-reg anchor, governance body, content template, threshold, retention cadence, recipient, and evidence template is preserved verbatim in the 5 sub-SOs.
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The high-level SO surfaces the **common documentation-regime duty** (records of processing activities + technical documentation + certification records + IS-policy documentation + QMS documentation + provider logs) on **parallel artefacts** serving **distinct audit purposes**. The 10 verified pairs are all SAME — 2 SAME — DIFFERENT-PERSPECTIVE (GDPR ↔ NIS 2 + GDPR ↔ CRA — substantively scope-disjoint per CRDA `N (typically)`, different record types, different audit purposes; CRDA `different-perspective` is a taxonomy artifact for these three pairs) + 3 SAME — COMPLEMENTARY classified by CRDA + 1 SAME — DIFFERENT-PERSPECTIVE RECOMMENDED-by-CRDA (GDPR ↔ DORA) + 4 SAME — COMPLEMENTARY RECOMMENDED-by-CRDA. No CORRECTED, no CONTRADICTORY. **DORA-absence flag (CRDA-deep §9.4 line 29)** distinguishes 9.4 from the other D-09 sub-domains — DORA does NOT impose a RoPA-equivalent; the DORA Art. 9(4)(a) information security policy is a different record type (entity-level IS-policy documentation) serving a different audit purpose (NCA audit on IS policy) than the GDPR RoPA (DPA audit on processing activities). For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. **No OJ-level consolidation rule for documentation at 9.4** — unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk-management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *documentation object*. The 5 documentation regimes operate in parallel; no OJ-permitted cross-substitution exists between any pair. Phase 1 entities with ≥2 of the 5 participating regs applicability must maintain **parallel documentation regimes** even when the underlying product is CRA-conformant and the underlying AI system is AI-Act high-risk. The **3 substantively scope-disjoint pairs (GDPR ↔ NIS 2 + GDPR ↔ CRA + GDPR ↔ DORA-recommended)** never engage the HL together — different record types serving different audit purposes; CRDA `different-perspective` is a taxonomy artifact for these three pairs. The **NIS 2 ↔ CRA CSA-certification link** is the only cross-regulation link at 9.4 involving CRA + NIS 2 — when an NSIE procures CSA-certified CRA products, CRA Art. 27(8)/(9) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881, at assurance level at least 'substantial', shall be presumed to be in conformity with the essential cybersecurity requirements` is the upstream gate for NIS 2 procurements (certification boundary). The HL does NOT collapse the 5 documentation regimes into a single artefact; the per-reg perspective on the artefact, anchor, governance body, content template, threshold, retention cadence, recipient, and evidence template is preserved verbatim. For a DORA financial entity that is also a controller + NSIE + manufacturer + high-risk-AI provider (all 5 participating regs applicable), the 5 regimes must all be maintained in parallel serving 5 distinct audit purposes.
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-09.4
title: D-09.4 Records of Processing — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.4 Records of Processing
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---
> **Deep analysis:** [D-09.4 Records of Processing](../../DeepAnalysis/D-09_Governance-Documentation/D-09.4.md)
#### D-09.4 Records of Processing
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-029 + SO-GDPR-038 | Records of processing activities per Art. 30(1)/(2); transparency to data subjects on processing operations (Art. 12/13/14). | Controller/processor RoPA mandate; 250-employee exception; data-subject-rights-supporting records. |
| NIS2 | SO-NIS2-024 (partial) | Use of certified ICT products/services/processes where required by Member State or Commission delegated act (Art. 24). | Certification-driven recordkeeping, not a RoPA-equivalent. |
| CRA | SO-CRA-055/056/057/058/059/061/062/063/064/065/066/067 (many) | Single point of contact + product identification + 10-year technical documentation retention + EU declaration + CE marking + Annex VII content + corrective measures + MSA cooperation + cessation of operations. | Product-level technical documentation regime; Annex VII 8-item content list; 10-year retention or support period (whichever longer). |
| DORA | (out-of-scope) | DORA does not impose a RoPA obligation (no GDPR Art. 30 analogue). | BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents. |
| AI_Act | SO-AIACT-009 + SO-AIACT-010 (partial) | Technical documentation (Annex IV via Art. 11/12) + QMS documentation of 13 enumerated aspects. | AI-system-specific documentation mandate; partial coverage. GDPR Art. 30 is the dedicated authority for RoPA. |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

##### Emergent tensions (4 regulations)
<!-- emergent: GDPR,NIS2,CRA,AI_Act -->
- **Four documentation regimes with overlapping but non-substitutable artefacts**: GDPR RoPA, NIS 2 certification-driven records (Art. 24), CRA Annex VII 8-item technical documentation + 10-year retention, AI Act Annex IV + Art. 17 QMS. All four apply to a DORA-excluded entity that processes personal data and ships AI-enabled CRA-regulated products and is an NSIE. No OJ-level consolidation rule exists (the CRA Art. 13(4) sentence 2 consolidation applies only to risk assessment, not documentation). Phase 1 entities must maintain four parallel documentation regimes.
- **DORA is fully absent**: DORA does not impose a RoPA-equivalent. DORA BC/DR logging (Art. 12) is operational continuity, not processing-of-personal-data records. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The DORA Art. 12 logging obligation is a separate artefact.
<!-- /emergent -->
##### SR cross-validation
The 4 applicable regulations map D-09.4 to the NIST CSF 2.0 Subcategories **ID.AM-08** (Systems, hardware, software, services, and data are managed throughout their life cycle) and **PR.DS-12** (Data managed consistent with risk strategy) as the convergent pair. GDPR additionally maps **GV.PO-02** (Cybersecurity processes and procedures established, communicated, enforced) for the demonstrable-compliance dimension; CRA additionally maps **ID.RA-05** for the risk-assessment documentation.
##### Downstream implication
Phase 1 entities must implement four parallel documentation regimes. The retention periods differ (GDPR until processing ceases + supervisory-authority request; CRA 10 years or support period, whichever longer; AI Act Art. 19(1) 6-month log retention; NIS 2 Art. 24 per Member State). The Layer 1 cross-cutting analysis is required to reconcile retention cadences.
---
### D-10 Monitoring & Audit
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-09.4
title: D-09.4 Records of Processing — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.4 Records of Processing
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---
> **Domain analysis:** [D-09.4 Records of Processing](../../DomainAnalysis/D-09_Governance-Documentation/D-09.4.md)
#### D-09.4 Records of Processing
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority note (CRDA flag):** DORA is fully absent — no RoPA-equivalent. DORA BC/DR logging (Art. 12) is operational continuity, not processing-of-personal-data records. For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The DORA Art. 12 logging obligation is a separate artefact.

## Part 3 — context

### D-10 Monitoring & Audit
---

