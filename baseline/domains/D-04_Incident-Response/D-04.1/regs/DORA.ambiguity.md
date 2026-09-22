# D-04.1 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
## DORA v0.2 — Chapter II Section I + Art. 4: Governance and Proportionality (Art. 4–6)
> **Source.** OJ L 333, 27.12.2022, p. 29–32. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **1635–1789**.
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending`, `scope`.
>
> **Why these three articles together (umbrella file `02a`).** Art. 4 is in Ch. I (General Provisions) but the proportionality principle it establishes **propagates to every clause in Ch. II–V Sec. I**. Art. 5 (governance) and Art. 6 (framework chapeau) are the structural anchors to which Art. 4 attaches. Grouping them in `02a` lets the reader see the **proportionality overlay + management-body liability + framework chapeau** as a single conceptual block. The remaining 10 articles of Ch. II Sec. II (Art. 7–16, the operational risk-management provisions) are analysed in `02b_DORA_Ch2Sec2_Framework.md`.
>
> **Articles in this file:** 3 articles, 17 paragraphs (Art. 4: 3; Art. 5: 4 + 9 sub-points; Art. 6: 10 + 8 sub-points), 13 atomic clauses (CL4-1 … CL6-5).
---
### 1. Articles covered
| Article | Title | Paragraphs | T3 clause | New in v0.2? |
|---|---|---|---|---|
| Art. 4 | Proportionality principle | 3 | **C01** (proportionality) | No (extended — T3 had a single clause; v0.2 has 3) |
| Art. 5 | Governance and organisation | 4 + 9 sub-points (a)–(i) | **C02** (governance), **C03** (management body), **C04** (board training) | No (extended — T3 had 3 clauses; v0.2 has 5) |
| Art. 6 | ICT risk management framework (chapeau) | 10 + 8 sub-points (a)–(h) | **C05** (framework chapeau), **C06** (control function), **C07** (audit), **C08** (resilience strategy) | No (extended — T3 had 4 clauses; v0.2 has 5) |
**Note on Art. 4 (Proportionality):** the three paragraphs of Art. 4 attach proportionality to (i) Ch. II as the default; (ii) Ch. III, IV, V Sec. I by specific reference; (iii) competent-authority review under Art. 6(5) and Art. 16(2). Each clause card in the rest of v0.2 carries a `proportionality-status: Art. 4 applies` flag (per pilot convention).
**Note on RTS-pending:** no RTS mandate in this article range. Art. 15 (RTS mandate to ESAs on Art. 9–11 elements) is meta-procedural; the substantive impact lives in Art. 9–11, not in this file. The Art. 4 proportionality principle is **self-implementing** — no RTS/ITS specifies the criteria.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL4-1 | Art. 4(1) | Proportionality chapeau (Ch. II) | **S3** | Implement Ch. II per proportionality (size, risk profile, nature/scale/complexity). |
| CL4-2 | Art. 4(2) | Proportionality propagation (Ch. III, IV, V Sec. I) | **S3** | Application proportionate to size/risk/nature/scale/complexity. |
| CL4-3 | Art. 4(3) | CA review of proportionality | **S2** | Competent authorities consider proportionality in framework review. |
| CL5-1 | Art. 5(1) | Internal governance and control framework chapeau | **S3** | Internal governance framework ensuring effective and prudent ICT risk management. |
| CL5-2 | Art. 5(2) chapeau | Management body 4-verb coordination | **S3** | Management body: `define, approve, oversee and be responsible for` ICT risk management framework. |
| CL5-3 | Art. 5(2)(a)–(d) | Management body sub-points (responsibility + standards + roles + strategy) | **S3** | Ultimate responsibility; high standards (availability, authenticity, integrity, confidentiality); clear roles; digital operational resilience strategy + risk tolerance. |
| CL5-4 | Art. 5(2)(e)–(i) | Management body sub-points (continuity + audit + budget + ICT-TPP + reporting) | **S3** | ICT business continuity; ICT internal audit plans; budget; ICT-TPP policy; reporting channels. |
| CL5-5 | Art. 5(3)+(4) | Designation + training | **S3** | Designate monitoring role (other than microenterprises); management body training. |
| CL6-1 | Art. 6(1) chapeau | Framework chapeau | **S3** | `Sound, comprehensive and well-documented` ICT risk management framework. |
| CL6-2 | Art. 6(2)+(3) | Framework content + minimise impact | **S3** | Strategies, policies, procedures, ICT protocols, tools; minimise impact; CA info. |
| CL6-3 | Art. 6(4)+(6) | Independence + 3 lines of defence + internal audit | **S3** | Control function independence; three lines of defence; internal audit by auditors with ICT expertise. |
| CL6-4 | Art. 6(5)+(7) | Documentation + review + follow-up | **S3** | Documented and reviewed at least yearly (or periodically for microenterprises); major-incident triggers; formal follow-up. |
| CL6-5 | Art. 6(8)+(9)+(10) | Digital operational resilience strategy + multi-vendor + outsourcing | **S3** | 8-point strategy; optional multi-vendor strategy; outsourcing of compliance verification. |
**Total: 13 atomic clauses (Art. 4: 3; Art. 5: 5; Art. 6: 5).**
---
### 3. Verbatim OJ text — Art. 4–6
#### 4.13 CL6-5 — Art. 6(8)+(9)+(10) — Digital operational resilience strategy + multi-vendor + outsourcing
**Source locus:** Art. 6(8), 6(9), 6(10).
> 8. The ICT risk management framework shall include a **digital operational resilience strategy** setting out how the framework shall be implemented. To that end, the digital operational resilience strategy shall include methods to address ICT risk and attain specific ICT objectives, by:
>
> (a) explaining how the ICT risk management framework supports the financial entity's business strategy and objectives;
>
> (b) establishing the **risk tolerance level for ICT risk, in accordance with the risk appetite of the financial entity, and analysing the impact tolerance for ICT disruptions**;
>
> (c) setting out clear information security objectives, including key performance indicators and key risk metrics;
>
> (d) explaining the ICT reference architecture and any changes needed to reach specific business objectives;
>
> (e) outlining the different mechanisms put in place to detect ICT-related incidents, prevent their impact and provide protection from it;
>
> (f) evidencing the current digital operational resilience situation on the basis of the number of major ICT-related incidents reported and the effectiveness of preventive measures;
>
> (g) implementing digital operational resilience testing, in accordance with Chapter IV of this Regulation;
>
> (h) outlining a communication strategy in the event of ICT-related incidents the disclosure of which is required in accordance with Article 14.
>
> 9. Financial entities may, in the context of the digital operational resilience strategy referred to in paragraph 8, define a **holistic ICT multi-vendor strategy**, at group or entity level, showing key dependencies on ICT third-party service providers and explaining the rationale behind the procurement mix of ICT third-party service providers.
>
> 10. Financial entities may, in accordance with Union and national sectoral law, **outsource the tasks of verifying compliance with ICT risk management requirements** to intra-group or external undertakings. In case of such outsourcing, the financial entity remains **fully responsible for the verification of compliance with the ICT risk management requirements**.
**Instance 1 — POLY — S3 — Art. 6(8)(a)–(h) — 8-point strategy enumeration**
The strategy content list. **Open or closed**?
- **R1:** Closed (the 8 are exhaustive; the strategy must contain all of them).
- **R2:** Open (the 8 are illustrative; additional elements may be added).
- **R3:** Floor (the 8 are minimum; additional elements required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed | None in OJ |
| R2 | Open | In-Directive: literal `include … by` (open-list) |
| R3 | Floor | None in OJ |
R2 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`include … by`); §5.4.7 (8-way enumeration).
**Instance 2 — VAG — S3 — `risk tolerance level for ICT risk, in accordance with the risk appetite of the financial entity` (Art. 6(8)(b))**
`risk tolerance` and `risk appetite` are **case-law-laden banking-supervision terms** (Basel Committee, EBA guidelines). Three materially distinct readings:
- **R1:** Risk tolerance = quantitative limit; risk appetite = qualitative board statement.
- **R2:** Risk tolerance = qualitative; risk appetite = quantitative.
- **R3:** Synonymous (both refer to the same concept).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Tolerance-quant, Appetite-qual | In-Directive: EBA Guidelines on ICT and Security Risk Management |
| R2 | Tolerance-qual, Appetite-quant | None in OJ |
| R3 | Synonymous | None in OJ |
R1 is the dominant EBA-aligned reading. S3.
*Berry anchor:* §3.3.1 (`risk tolerance`, `risk appetite`); §5.1 (`in accordance with`).
**Instance 3 — VAG — S3 — `key performance indicators and key risk metrics` (Art. 6(8)(c))**
The KPI/KRM pair. Three readings:
- **R1:** KPIs (forward-looking performance) AND KRMs (backward-looking risk).
- **R2:** Two labels for the same metrics.
- **R3:** Either, per entity choice.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct (forward vs. backward) | None in OJ |
| R2 | Synonymous | None in OJ |
| R3 | Either | In-Directive: literal `and` |
R1 is the conventional reading. S3.
*Berry anchor:* §3.3.1 (`key performance indicators`, `key risk metrics`); §5.4.7 (AND).
**Instance 4 — POLY — S2 — `major ICT-related incidents reported and the effectiveness of preventive measures` (Art. 6(8)(f))**
Two evidence sources (AND). The clause does not specify **how many** major incidents or **what** effectiveness threshold. S2.
*Berry anchor:* §3.3.1 (`major ICT-related incidents`, `effectiveness`).
**Instance 5 — VAG — S3 — `holistic ICT multi-vendor strategy` (Art. 6(9))**
The multi-vendor strategy. `holistic` is Berry-flagged. Three readings:
- **R1:** Multi-vendor for all ICT services (no single-vendor dependencies).
- **R2:** Multi-vendor for critical services (CTPPs may still be single-vendor for non-critical).
- **R3:** Documented strategy (any structure; the entity is its own judge of "holistic").
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All-services | None in OJ |
| R2 | Critical-only | None in OJ |
| R3 | Documented | In-Directive: literal `holistic` (entity judgment) |
R3 is the literal reading. S3 (R1 vs R3 admit materially distinct compliance populations: R1 requires vendor diversification; R3 requires only documentation).
*Berry anchor:* §3.3.1 (`holistic`); §3.3.1 (`multi-vendor`).
**Instance 6 — POLY — S3 — `outsource the tasks of verifying compliance with ICT risk management requirements to intra-group or external undertakings` (Art. 6(10))**
The outsourcing permission. Two paths (OR): intra-group OR external. Three readings:
- **R1:** Outsourcing permitted under any of (a) Union sectoral law, (b) national sectoral law, (c) both.
- **R2:** Outsourcing permitted only if both Union and national law allow.
- **R3:** Outsourcing permitted under either Union or national law.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either (Union OR national) | In-Directive: literal `in accordance with Union and national sectoral law` |
| R2 | Both required | None in OJ |
| R3 | Either | In-Directive: literal |
R1 is the literal reading (the `and` in `Union and national sectoral law` is conjunctive but each is independently sufficient — see also Art. 28 outsourcing provisions). S3.
*Berry anchor:* §5.4.7 (AND/OR in `Union and national`); §3.3.1 (`intra-group`, `external undertakings`).
**Instance 7 — VAG — S3 — `fully responsible for the verification of compliance with the ICT risk management requirements` (Art. 6(10))**
The non-delegable responsibility. `fully` admits three readings:
- **R1:** Absolute (no derogation even from gross negligence of outsourcee).
- **R2:** Standard (ordinary liability for own acts and those of the outsourcee).
- **R3:** Strict (joint-and-several liability with the outsourcee).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Absolute | None in OJ |
| R2 | Standard | None in OJ |
| R3 | Strict | In-Directive: literal `fully responsible` + non-delegable principle |
R3 is the literal reading (consistent with the management-body non-delegable responsibility in CL5-5 Instance 1). S3.
*Berry anchor:* §3.3.1 (`fully responsible`); cf. CL5-5 Instance 1 `ultimate responsibility`.
**Definitional anchor:** DORA Art. 3(1) `digital operational resilience` (DORA-D01, S3 `build, assure and review`); DORA Art. 3(10) `major ICT-related incident` (DORA-D10, S3 `high adverse impact`); DORA Art. 3(8) `ICT-related incident` (DORA-D08); DORA Art. 3(22) `critical or important function` (S3 tautology); DORA Art. 3(19) `ICT third-party service provider` (DORA-D19); DORA Art. 3(20) `ICT intra-group service provider` (DORA-D20).
**Proportionality-status:** Art. 4 applies (Art. 6(8)(b) `risk appetite` and Art. 6(9) `multi-vendor strategy` are both proportionality-sensitive).
**Scope:** financial entity.
---
### 5. T3-vs-text gaps
This section catalogues **inconsistencies between the v0.1 T3 mapping** and the OJ text. Per pilot convention, T3-vs-text gaps are flagged separately from linguistic ambiguities of the regulation (they are inconsistencies of the mapping layer, not of the text).
#### 6.1 Art. 4 propagation pattern — three distinct proportionality regimes
Art. 4 establishes **three distinct proportionality regimes** that operate simultaneously:
- **Art. 4(1) — Ch. II proportionality** (CL4-1): default for the ICT risk management framework.
- **Art. 4(2) — Ch. III, IV, V Sec. I proportionality** (CL4-2): default for incident reporting, testing, and third-party risk.
- **Art. 4(3) — CA-review proportionality** (CL4-3): meta-provision requiring CAs to consider proportionality when reviewing the framework.
The three regimes are **not symmetric**: Art. 4(1) is self-implementing (the entity applies it directly); Art. 4(2) defers to chapter-specific clauses (Art. 16 simplification, Art. 25(3) microenterprise exception); Art. 4(3) is addressed to CAs.
- **Berry anchor:** §3.3.1 (`principle of proportionality`); §5.1 (`proportionate`).
- **Structural implication:** the proportionality overlay is **inherited by every Ch. II–V Sec. I clause** in v0.2. Every clause card in `02b`–`05a` carries `proportionality-status: Art. 4 applies`. The v0.2 convention was established in the pilot file (`01_DORA_Art3_Definitions.md` §2 note on Art. 4).
#### 6.3 Art. 6 chapeau — the framework's three-attribute triad
Art. 6(1) opens with `sound, comprehensive and well-documented` (three attributes, AND). This is the **framework-level analog** of:
- **Art. 24(1) `sound and comprehensive`** (testing programme, two attributes; CL24-1)
- **Berry anchor:** §5.1 (`sound`, `comprehensive`, `well-documented`); §5.4.7 (AND); §5.5 (parallelism).
- **Structural implication:** the framework's three attributes set the bar for every Ch. II–V Sec. I clause. Any clause that fails one of the three (e.g. a framework that is `comprehensive and well-documented` but not `sound`) would be non-compliant.
#### 6.6 Art. 6(8) — the 8-point resilience strategy
Art. 6(8) enumerates **8 strategy elements** (open list: `include … by`). The 8 elements cover the strategy's full lifecycle: (a) business alignment, (b) risk tolerance, (c) KPIs/KRMs, (d) reference architecture, (e) detection/prevention, (f) current state evidence, (g) testing, (h) communication.
- **Berry anchor:** §3.3.1 (`include … by`); §5.4.7 (8-way enumeration).
- **Structural implication:** the 8-point strategy is the **operational mirror** of the framework's three-attribute triad (CL6-1 Instance 1). Where the triad describes the framework's qualities, the 8 elements describe its **contents**. A framework that is `sound, comprehensive and well-documented` and contains all 8 elements satisfies the chapeau.
## DORA v0.2 — Chapter III: ICT-Related Incident Management, Classification, and Reporting (Art. 17–23)
> **Source.** OJ L 333, 27.12.2022, p. 39–44. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **2275–2591**.
>
> **Pattern.** Each article quoted in full (paragraph by paragraph), then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 18(3) | Art. 20` (the defining characteristic of Ch. III — hard deadlines and classification thresholds live in RTS, not OJ), `scope: regulator→financial-entity` (for client-notification and CA-routing clauses).
>
> **Chapter III is the operational reporting arm of DORA.** It operationalises the Art. 3(8) `ICT-related incident` and Art. 3(10) `major ICT-related incident` definitions. Art. 17 establishes the management process. Art. 18 enumerates 6 multiplicative criteria for classifying incidents (and 3 for cyber threats) and delegates the **combination rule + materiality thresholds** to an ESA RTS (Art. 18(3)). Art. 19 mandates reporting of major ICT-related incidents in 3 tiers (initial / intermediate / final), plus voluntary cyber-threat notification and mandatory client notification. Art. 20 is a pure RTS/ITS delegation — content, time limits, and templates are **wholly dependent** on the ESAs Joint Committee output (deadline 17 July 2024). Art. 21 is a feasibility-report mandate on centralisation (a single EU Hub). Art. 22 specifies supervisory feedback. Art. 23 extends Ch. III to operational/security payment-related incidents for credit institutions, payment institutions, AISPs, and EMIs.
>
> **Articles in this file:** 7 articles, ~30 paragraphs, **31 atomic clauses** (CL17-1 … CL23-1).
---
### 1. Articles covered
| Article | Title (OJ) | Paragraphs | New in v0.2? | T3 clause |
|---|---|---|---|---|
| Art. 17 | **ICT-related incident management process** | 3 (1, 2, 3 with 6 sub-points (a)–(f)) | No (extended) | **C29** |
| Art. 18 | **Classification of ICT-related incidents and cyber threats** | 4 (1 with 6 sub-points (a)–(f), 2, 3 with 3 sub-points (a)–(c), 4) | No (extended) | **C30** |
| Art. 19 | **Reporting of major ICT-related incidents and voluntary notification of significant cyber threats** | 8 (1, 2, 3, 4 with 3 sub-points (a)–(c), 5, 6 with 5 sub-points (a)–(e), 7, 8) | No (extended) | **C31** |
| Art. 20 | **Harmonisation of reporting content and templates** | 1 (RTS+ITS) | No (extended) | — (RTS meta — T3 omitted) |
| Art. 21 | **Centralisation of reporting of major ICT-related incidents** (single EU Hub feasibility) | 3 (1, 2 with 7 sub-points (a)–(g), 3) | **YES** | — (not in T3) |
| Art. 22 | **Supervisory feedback** | 2 (1, 2) | **YES** | — (not in T3) |
| Art. 23 | **Operational or security payment-related incidents concerning credit institutions, payment institutions, account information service providers, and electronic money institutions** (extension of Ch. III to payment-sector entities) | 1 | **YES** | — (not in T3) |
**Note on Art. 4 (Proportionality):** every clause card in this file carries `proportionality-status: Art. 4 applies`. Art. 18(4) explicitly names microenterprises and SMEs.
**Note on Art. 20 (RTS-pending — THE defining characteristic of Ch. III):** Ch. III is structurally dependent on RTS/ITS acts. The hard reporting deadlines and classification thresholds do not live in OJ text — they are mandated to the ESAs Joint Committee. As of mid-2025:
| RTS/ITS | Mandate locus | OJ deadline | Status (mid-2025) |
|---|---|---|---|
| Art. 18(3) RTS (criteria + materiality thresholds) | Art. 18(3)(a)–(c) | **17 January 2024** | Deadline **passed**; ESAs Joint Committee RTS in adoption pipeline. Implementing Regulation (EU) 2024/2956 of 18 July 2024 partially addresses content. |
| Art. 20 RTS (content + time limits) | Art. 20(a)(i)–(iii) | **17 July 2024** | Deadline **passed**; partly addressed by Reg. (EU) 2024/2956. |
| Art. 20 ITS (forms, templates, procedures) | Art. 20(b) | **17 July 2024** | **Adopted** as Implementing Regulation (EU) 2024/2956 (Annex I–IV templates). |
| Art. 21(3) joint report (single EU Hub) | Art. 21(1)–(3) | **17 January 2025** | Deadline **passed**; ESAs Joint Committee report published in Q1 2025. |
**Note on v0.2 expansion:** T3 (T4 taxonomy) covered Ch. III as 3 clauses (C29, C30, C31) corresponding to Arts 17, 18, 19 in compressed form. v0.2 expands this to 31 atomic clauses and **adds 4 articles** (Art. 20, 21, 22, 23) that T3 entirely omitted (T3 dropped them as "procedural" or "payment-specific").
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL17-1 | Art. 17(1) | Process establishment | **S2** | `define, establish and implement` an ICT-related incident management process. |
| CL17-2 | Art. 17(2) | Recording + follow-up | **S2** | Record all incidents and significant cyber threats; identify root causes. |
| CL17-3 | Art. 17(3)(a) | Early warning indicators | **S2** | Put in place early warning indicators. |
| CL17-4 | Art. 17(3)(b) | Classification procedures | **S3** | `identify, track, log, categorise and classify` per Art. 18(1) criteria. |
| CL17-5 | Art. 17(3)(c) | Roles and responsibilities | **S2** | Assign roles for different incident types and scenarios. |
| CL17-6 | Art. 17(3)(d) | Communication plans | **S3** | Plans for staff/media/client notification (Art. 14 cross-ref). |
| CL17-7 | Art. 17(3)(e) | Senior management escalation | **S3** | Major incidents → senior mgmt + management body (impact, response, controls). |
| CL17-8 | Art. 17(3)(f) | Response procedures | **S3** | `timely manner` services become operational and secure. |
| CL18-1 | Art. 18(1)(a) | Criterion 1 of 6 | **S3** | Clients/counterparts/transactions/reputational impact. |
| CL18-2 | Art. 18(1)(b) | Criterion 2 of 6 | **S3** | Duration including service downtime. |
| CL18-3 | Art. 18(1)(c) | Criterion 3 of 6 | **S3** | Geographical spread, particularly >2 Member States. |
| CL18-4 | Art. 18(1)(d) | Criterion 4 of 6 | **S3** | Data losses (4 CIA+A dimensions). |
| CL18-5 | Art. 18(1)(e) | Criterion 5 of 6 | **S3** | Criticality of services including transactions/operations. |
| CL18-6 | Art. 18(1)(f) | Criterion 6 of 6 | **S3** | Economic impact (direct/indirect, absolute/relative). |
| CL18-7 | Art. 18(2) | Significant cyber threats classification | **S3** | 3 sub-criteria for significant cyber threats. |
| CL18-8 | Art. 18(3) | ESAs RTS mandate | **S3** | RTS specifying criteria + materiality thresholds (3 sub-points). |
| CL18-9 | Art. 18(4) | RTS development considerations + deadline | **S3** | Proportionality; microenterprise/SME consideration; 17 January 2024 deadline. |
| CL19-1 | Art. 19(1) | Major incident reporting | **S3** | Report to relevant CA per Art. 46; single-CA designation; significant CIs → ECB. |
| CL19-2 | Art. 19(2) | Voluntary cyber-threat notification | **S2** | Voluntary notification by entity; CA may forward. |
| CL19-3 | Art. 19(3) | Client notification | **S3** | `without undue delay` notify clients + protection measures. |
| CL19-4 | Art. 19(4) | Three-tier reporting | **S3** | Initial notification + intermediate + final report. |
| CL19-5 | Art. 19(5) | Outsourcing of reporting | **S2** | May outsource; financial entity remains responsible. |
| CL19-6 | Art. 19(6) | CA→other authorities forwarding | **S3** | 5 recipient categories (EBA/ESMA/EIOPA, ECB, NIS 2 CAs/SPOCs/CSIRTs, resolution authorities, other public authorities). |
| CL19-7 | Art. 19(7) | ESAs/ECB cross-MS assessment | **S3** | ESAs/ECB assess cross-MS relevance; ESAs notify other MS CAs. |
| CL19-8 | Art. 19(8) | ESMA + host MS transmission | **S2** | ESMA transmission to host MS CAs; CSD cross-border activity carve-out. |
| CL20-1 | Art. 20 | ESAs RTS/ITS mandate | **S3** | RTS content (a)(i)–(iii) + ITS forms/templates/procedures (b). |
| CL21-1 | Art. 21(1)+(2) | Single EU Hub feasibility mandate | **S3** | Joint ESA report (in consultation with ECB, ENISA); 7 enumerated elements (a)–(g). |
| CL21-2 | Art. 21(3) | Report submission deadline | **S2** | Submission to EP/Council/Commission by 17 January 2025. |
| CL22-1 | Art. 22(1) | Supervisory feedback | **S3** | CA feedback on receipt of notification/reports; anonymised threat intel; remedies discussion. |
| CL22-2 | Art. 22(2) | ESAs yearly aggregated report | **S3** | Yearly anonymised-aggregated ESA report; warnings + high-level statistics. |
| CL23-1 | Art. 23 | Ch. III extension to payment-sector entities | **S3** | Ch. III applies to operational/security payment incidents for CIs, PIs, AISPs, EMIs. |
**Total: 31 atomic clauses (Art. 17: 8; Art. 18: 9; Art. 19: 8; Art. 20: 1; Art. 21: 2; Art. 22: 2; Art. 23: 1).**
---
### 3. Verbatim OJ text — Art. 17–23
#### 4.1 CL17-1 — Art. 17(1) — Process establishment
**Source locus:** Art. 17(1).
> Financial entities shall **define, establish and implement** an ICT-related incident management process to detect, manage and notify ICT-related incidents.
**Instance 1 — COORD — S2 — `define, establish and implement`**
Three coordinated verbs; the standard for each is undefined. Same pattern as DORA-D01 `build, assure and review` and Art. 24(1) `establish, maintain and review` (CL24-1 in Ch. IV file).
- **R1:** Three discrete lifecycle phases (define-then-establish-then-implement).
- **R2:** Three aspects of a single continuous process.
- **R3:** Three independent control families (define policy, establish system, implement operationally).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Discrete phases | In-Directive: literal three-verb coordination |
| R2 | Continuous | None in OJ |
| R3 | Independent families | None in OJ |
R1 vs R3 admit materially distinct compliance populations. S2.
*Berry anchor:* §5.4.7 (three-way coordination).
**Instance 2 — COORD — S2 — `detect, manage and notify`**
Three coordinated purposes of the process. Same Berry pattern.
*Berry anchor:* §5.4.7 (three-way coordination).
---
#### 4.27 CL21-1 — Art. 21(1)+(2) — Single EU Hub feasibility mandate
**Source locus:** Art. 21(1) and 21(2).
> 1. The ESAs, through the Joint Committee, and in consultation with the ECB and ENISA, shall prepare a joint report assessing the **feasibility of further centralisation of incident reporting through the establishment of a single EU Hub for major ICT-related incident reporting** by financial entities. The joint report shall explore ways to facilitate the flow of ICT-related incident reporting, reduce associated costs and underpin thematic analyses with a view to enhancing supervisory convergence.
>
> 2. The joint report referred to in paragraph 1 shall comprise at least the following elements:
>
> (a) prerequisites for the establishment of a single EU Hub;
>
> (b) benefits, limitations and risks, including risks associated with the high concentration of sensitive information;
>
> (c) the necessary capability to ensure interoperability with regard to other relevant reporting schemes;
>
> (d) elements of operational management;
>
> (e) conditions of membership;
>
> (f) technical arrangements for financial entities and national competent authorities to access the single EU Hub;
>
> (g) a preliminary assessment of financial costs incurred by setting-up the operational platform supporting the single EU Hub, including the requisite expertise.
**Instance 1 — VAG — S3 — `single EU Hub`**
`single` + `Hub` — the architectural choice is undefined.
- **R1:** Single centralised data platform (one location, all CAs access).
- **R2:** Single API gateway (each CA holds data, common API).
- **R3:** Single standard (distributed but interoperable).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Centralised platform | In-Directive: literal `single EU Hub` |
| R2 | API gateway | None in OJ |
| R3 | Single standard | None in OJ |
S3.
*Berry anchor:* §3.3.1 (`single`, `Hub`); §5.1 (`single`).
**Instance 2 — VAG — S3 — `feasibility`**
`feasibility` of centralisation is broad — technical + legal + operational + financial + governance. S3.
*Berry anchor:* §5.1 (`feasibility`).
**Instance 3 — VAG — S3 — `thematic analyses with a view to enhancing supervisory convergence`**
`thematic analyses` + `supervisory convergence` — undefined. S3.
*Berry anchor:* §3.3.1 (`thematic analyses`, `supervisory convergence`).
**Instance 4 — VAG — S2 — `high concentration of sensitive information`**
`high concentration` is undefined. Same Berry pattern as DORA-D29 `ICT concentration risk`. S2.
*Berry anchor:* §5.1 (`high concentration`); cf. DORA-D29.
**Instance 5 — POLY — S2 — 7 enumerated elements**
Each element admits its own internal ambiguity:
| Element | Key ambiguity | Berry anchor |
|---|---|---|
| (a) `prerequisites` | Hard vs. soft preconditions | §3.3.1 (`prerequisites`) |
| (b) `benefits, limitations and risks` | Three-way comparison standard | §5.4.7 (three-way) |
| (c) `interoperability` | Technical vs. semantic | §3.3.1 (`interoperability`) |
| (d) `operational management` | Undefined scope | §3.3.1 (`operational management`) |
| (e) `conditions of membership` | Who becomes a member? | §3.3.1 (`membership`) |
| (f) `technical arrangements` | Read-only vs. write access | §3.3.1 (`technical arrangements`) |
| (g) `preliminary assessment of financial costs` | Method-based vs. estimate-based | §3.3.1 (`preliminary`) |
S2 (per-element); aggregate S3 due to the open-ended `at least` qualifier.
*Berry anchor:* §5.4.5 (illustrative use — `at least`); §3.3.1.
**Definitional anchor:** DORA-D29 `ICT concentration risk`; DORA Art. 50 (administrative penalties context).
**Scope:** regulator-internal (between ESAs and NCA institutional architecture, not directly entity-facing).
**Proportionality-status:** Art. 4 applies.
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in this file inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; Art. 3(5) `ICT risk`; Art. 3(30) `management body` (composite cross-reference, see pilot file §2.10). The Art. 3(22) `critical or important function` (S3 tautology, see pilot file §2.7) propagates to Art. 6(8)(f).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** Art. 4's proportionality pattern mirrors **NIS 2 Art. 1(2)** (proportionality in scope) and **CRA Art. 1(2)** (proportionality for microenterprises and SMEs). DORA Art. 4 is more elaborate than either, providing explicit CA-review (CL4-3) that NIS 2 and CRA do not have.


### from regs/DORA.ambiguity.md

- **CRA Annex I Part I §1 chapeau** `products with digital elements shall be designed, developed and produced …` (manufacturing lifecycle, three verbs; CRA-CL14)

### from regs/DORA.ambiguity.md

- **NIS 2 Art. 21(1) `appropriate and proportionate technical, operational and organisational measures`** (measures chapeau)


### from regs/DORA.ambiguity.md

The 3-attribute triad (`sound, comprehensive and well-documented`) is **the most demanding framework chapeau in the 5-regulation corpus** — it requires three distinct qualities (effectiveness, completeness, traceability). CRA Annex I Part I §1 has three verbs (design, develop, produce) but they describe **processes** not qualities. DORA's triad describes **qualities of an artifact** (the framework itself), which is a different kind of obligation.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the triad is the most explicit framework-quality specification in the corpus. NIS 2 Art. 21(1) uses `appropriate and proportionate` (2 qualifiers); CRA Annex I Part I uses process verbs; GDPR Art. 24 uses `appropriate` (1 qualifier). DORA's 3-attribute triad is the most demanding.


### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the open-list pattern is the **regulatory-drafting convention** shared with CRA Annex I Part I (multiple open enumerations) and NIS 2 Art. 21(2) (10 sub-points). DORA's 8 elements are **more strategic** (KPIs, risk tolerance, communication) than CRA's (technical requirements) and **more operational** than NIS 2's (governance policies).


### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in Ch. III inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) (`network and information system`). Major-incident classification inherits from Art. 3(10) `major ICT-related incident` (DORA-D10, S3 regress — see pilot file §2.4), which inherits from Art. 3(22) `critical or important function` (DORA-D22 tautology, S3).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA Art. 3(8) `ICT-related incident`.
**Proportionality-status:** Art. 4 applies.

<!-- aegis:purity: own_reg=DORA; demoted=9; core_cross_mentions=0 -->