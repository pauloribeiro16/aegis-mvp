# D-01.4 — Relevant Ambiguity (DORA)

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
#### 4.1 CL4-1 — Art. 4(1) — Proportionality chapeau (Ch. II)
**Source locus:** Art. 4(1).
> Financial entities shall implement the rules laid down in Chapter II in accordance with the principle of proportionality, taking into account their size and overall risk profile, and the nature, scale and complexity of their services, activities and operations.
**Instance 1 — VAG — S3 — `principle of proportionality`**
The proportionality principle is a **general principle of EU law** (case-law-laden: Cassis de Dijon, Lange, Schwarz, etc.) but Art. 4(1) makes it the **specific override for Ch. II implementation**. Three materially distinct readings:
- **R1:** Quantitative (proportional to size: headcount, balance-sheet total, turnover).
- **R2:** Risk-based (proportional to the ICT risk profile of the entity).
- **R3:** Combined: size, risk profile, AND nature/scale/complexity (literal reading).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative (size) | None in OJ |
| R2 | Risk-based | In-Directive: literal `overall risk profile` |
| R3 | Combined (size + risk + nature/scale/complexity) | In-Directive: literal `taking into account their size and overall risk profile, and the nature, scale and complexity` |
R1 vs R3 admit materially distinct compliance populations (R1: small entity is automatically exempted; R3: a small entity with high risk profile may still need to comply fully). S3.
*Berry anchor:* §5.1 (`proportionality`); §3.3.1 (`principle of proportionality`).
**Instance 2 — VAG — S3 — `nature, scale and complexity`**
The three-factor qualifier. Each term admits its own ambiguity.
| Sub-factor | Key ambiguity | Berry anchor |
|---|---|---|
| `nature` | Sectoral (banking vs. insurance vs. asset management) vs. operational (online vs. branch) | §3.3.1 (`nature`) |
| `scale` | Volume of operations, number of clients, geographic spread | §3.3.1 (`scale`) |
| `complexity` | Organisational (group structure) vs. technical (legacy systems, multi-vendor) | §3.3.1 (`complexity`) |
S3 (the three sub-factors are not formally weighted; an entity may emphasise one over another).
*Berry anchor:* §3.3.1 (`nature, scale and complexity`).
---
#### 4.4 CL5-1 — Art. 5(1) — Internal governance and control framework chapeau
**Source locus:** Art. 5(1).
> Financial entities shall have in place an **internal governance and control framework** that ensures an **effective and prudent** management of ICT risk, in accordance with Article 6(4), in order to achieve a high level of digital operational resilience.
**Instance 1 — VAG — S3 — `internal governance and control framework`**
The framework chapeau. Three materially distinct readings:
- **R1:** Three lines of defence model (per Art. 6(4) cross-reference).
- **R2:** Two lines of defence (business + control, common in some Member States).
- **R3:** Composite: any recognised internal-control model.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three lines of defence | In-Directive: Art. 6(4) `according to the three lines of defence model` |
| R2 | Two lines of defence | None in OJ |
| R3 | Any model | In-Directive: Art. 6(4) `or an internal risk management and control model` |
R3 is the literal reading (Art. 6(4) gives the option). S3 (the choice between R1 and R3 yields materially distinct control populations).
*Berry anchor:* §3.3.1 (`governance and control framework`); §5.4.7 (AND/OR structure).
**Instance 2 — VAG — S3 — `effective and prudent`**
Two vague qualifiers (AND). Both are Berry classics.
- **R1:** Effective (outcome-based) AND prudent (process-based, conservative).
- **R2:** Hendiadys (single concept: risk-management discipline).
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct qualifiers | In-Directive: literal `and` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations (R1 requires both outcome and process; R3 allows either). S3.
**Instance 3 — POLY — S2 — `a high level of digital operational resilience`**
The target standard. Inherits DORA-D01 `digital operational resilience` (S3 `build, assure and review`).
- **R1:** All three lifecycle phases per R1 of DORA-D01.
- **R2:** Continuous process per R2 of DORA-D01.
- **R3:** All three control families per R3 of DORA-D01.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Lifecycle phases | In-Directive: DORA-D01 |
| R2 | Continuous process | In-Directive: DORA-D01 |
| R3 | Control families | In-Directive: DORA-D01 |
S2 (the target is propagated from the definition).
*Berry anchor:* §3.3.1 (`high level`); §3.3.1 (`digital operational resilience`).
**Definitional anchor:** DORA Art. 3(1) `digital operational resilience` (DORA-D01); DORA Art. 3(5) `ICT risk` (DORA-D05).
**Proportionality-status:** Art. 4 applies.
**Scope:** financial entity.
---
#### 6.1 Art. 4 propagation pattern — three distinct proportionality regimes
Art. 4 establishes **three distinct proportionality regimes** that operate simultaneously:
- **Art. 4(1) — Ch. II proportionality** (CL4-1): default for the ICT risk management framework.
- **Art. 4(2) — Ch. III, IV, V Sec. I proportionality** (CL4-2): default for incident reporting, testing, and third-party risk.
- **Art. 4(3) — CA-review proportionality** (CL4-3): meta-provision requiring CAs to consider proportionality when reviewing the framework.
The three regimes are **not symmetric**: Art. 4(1) is self-implementing (the entity applies it directly); Art. 4(2) defers to chapter-specific clauses (Art. 16 simplification, Art. 25(3) microenterprise exception); Art. 4(3) is addressed to CAs.
- **Berry anchor:** §3.3.1 (`principle of proportionality`); §5.1 (`proportionate`).
- **Structural implication:** the proportionality overlay is **inherited by every Ch. II–V Sec. I clause** in v0.2. Every clause card in `02b`–`05a` carries `proportionality-status: Art. 4 applies`. The v0.2 convention was established in the pilot file (`01_DORA_Art3_Definitions.md` §2 note on Art. 4).
#### 4.21 CL19-4 — Art. 19(4) — Three-tier reporting (initial/intermediate/final)
**Source locus:** Art. 19(4).
> Financial entities shall, **within the time limits to be laid down in accordance with Article 20, first paragraph, point (a), point (ii)**, submit the following to the relevant competent authority:
>
> (a) an **initial notification**;
>
> (b) an **intermediate report** after the initial notification referred to in point (a), **as soon as the status of the original incident has changed significantly or the handling of the major ICT-related incident has changed based on new information available**, followed, as appropriate, by updated notifications every time a relevant status update is available, as well as upon a specific request of the competent authority;
>
> (c) a **final report**, when the **root cause analysis has been completed**, regardless of whether mitigation measures have already been implemented, and when the **actual impact figures are available to replace estimates**.
**Instance 1 — VAG + CROSS — S3 — `time limits to be laid down in accordance with Article 20(a)(ii)`**
The OJ article **does not specify the hard timestamps**. Each tier's time limit is delegated to the Art. 20 RTS. As of mid-2025, the Implementing Regulation (EU) 2024/2956 (Annex II initial-notification content + Annex IV templates) partially fills the gap, but the OJ-level obligation is fully RTS-dependent. S3.
*Berry anchor:* §5.1 (`time limits`); §5.7 (temporal); §3.3.1 (`in accordance with`).
**Instance 2 — VAG — S3 — `initial notification`**
*Berry anchor:* §3.3.1 (`initial notification`); §5.1 (`initial`).
**Instance 3 — VAG — S3 — `status of the original incident has changed significantly`**
`significantly` undefined. Three readings:
- **R1:** Material change in impact.
- **R2:** Material change in operational state.
- **R3:** Material change in any dimension.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Impact | None in OJ |
| R2 | Operational | None in OJ |
| R3 | Any | None in OJ |
S3.
*Berry anchor:* §5.1 (`significantly`); §3.3.1 (`status`).
**Instance 4 — VAG — S3 — `handling of the major ICT-related incident has changed based on new information available`**
Two layered Berry terms (`handling` + `changed` + `new information`). S3.
*Berry anchor:* §3.3.1 (`handling`, `new information`); §5.1 (`changed`).
**Instance 5 — VAG — S3 — `root cause analysis has been completed`**
`completed` undefined — strict completion (full report filed) vs. substantive completion (root cause identified, follow-up ongoing)?
- **R1:** Strict (formal report).
- **R2:** Substantive (cause identified).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict | None in OJ |
| R2 | Substantive | None in OJ |
S2 (R1 vs R2 affect the timing of the final report).
*Berry anchor:* §3.3.1 (`completed`); §3.3.1 (`root cause analysis`).
**Instance 6 — VAG — S3 — `actual impact figures are available to replace estimates`**
`actual impact figures` vs. `estimates` — the distinction is operationally standard but the threshold for replacement is undefined. S3.
*Berry anchor:* §5.1 (`actual`, `available`); §3.3.1 (`impact figures`, `estimates`).
**Definitional anchor:** DORA-D10 `major ICT-related incident`.
**RTS-pending:** **YES** — Art. 20(a)(ii) (time limits). Initial-notification time limit addressed in **Implementing Regulation (EU) 2024/2956** Annex II but OJ-level time limits still RTS-dependent.
**Proportionality-status:** Art. 4 applies.
---
#### 4.24 CL19-7 — Art. 19(7) — ESAs/ECB cross-MS assessment + notification
**Source locus:** Art. 19(7).
> Following receipt of information in accordance with paragraph 6, **EBA, ESMA or EIOPA and the ECB**, in consultation with ENISA and in cooperation with the relevant competent authority, shall assess whether the major ICT-related incident is relevant for competent authorities in other Member States. Following that assessment, EBA, ESMA or EIOPA shall, **as soon as possible**, notify relevant competent authorities in other Member States accordingly. **The ECB shall notify the members of the European System of Central Banks** on issues relevant to the payment system. Based on that notification, the competent authorities shall, where appropriate, take all of the necessary measures to protect the immediate stability of the financial system.
**Instance 1 — VAG — S3 — `shall assess whether the major ICT-related incident is relevant for competent authorities in other Member States`**
The relevance assessment is delegated to ESAs/ECB. The criteria live in Art. 18(3)(b) RTS. S3 (the OJ-level cross-MS relevance is framework-only).
*Berry anchor:* §3.3.1 (`relevance`); §5.1 (`relevant for competent authorities in other Member States`).
**Instance 2 — VAG — S2 — `as soon as possible`**
Stronger than `without undue delay` but weaker than `immediately`. S2.
*Berry anchor:* §5.1 (`as soon as possible`); §5.7 (temporal operator).
**Instance 3 — COORD — S2 — `the necessary measures to protect the immediate stability of the financial system`**
`necessary` + `immediate stability` — two layered Berry terms. S2.
*Berry anchor:* §5.1 (`necessary`, `immediate`); §3.3.1 (`stability`, `financial system`).
**Definitional anchor:** DORA-D10.
**RTS-pending:** Art. 18(3)(b) (cross-MS relevance criteria).
**Scope:** regulator→regulator.
**Proportionality-status:** Art. 4 applies.
---
#### 4.25 CL19-8 — Art. 19(8) — ESMA + host-MS transmission (CSD carve-out)
**Source locus:** Art. 19(8).
> The notification to be done by ESMA pursuant to paragraph 7 of this Article shall be without prejudice to the responsibility of the competent authority to **urgently transmit the details of the major ICT-related incident** to the relevant authority in the host Member State, where a central securities depository has significant cross-border activity in the host Member State, the major ICT-related incident is **likely to have severe consequences for the financial markets of the host Member State** and where there are cooperation arrangements among competent authorities related to the supervision of financial entities.
**Instance 1 — VAG — S2 — `urgently transmit`**
Stronger than `as soon as possible`. S2.
*Berry anchor:* §5.1 (`urgently`); §5.7 (temporal operator).
**Instance 2 — POLY — S3 — `likely to have severe consequences for the financial markets of the host Member State`**
*Berry anchor:* §5.1 (`likely`, `severe`); §3.3.1 (`consequences`, `financial markets`); §5.4.7 (literal).
**Instance 3 — COORD — S2 — Three trigger conditions AND'd**
(a) CSD has significant cross-border activity in host MS; (b) major incident likely to have severe consequences for host MS markets; (c) cooperation arrangements exist. All three required. S2.
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Definitional anchor:** DORA Art. 3(43) `trading venue` and CSDR Reg. 909/2014 Art. 2(1)(1) `central securities depository` (cross-references).
**Scope:** regulator→regulator.
**Proportionality-status:** Art. 4 applies.
---
#### 6.3 Art. 19 reporting timeline — RTS-dependent 3-tier (initial/intermediate/final)
Art. 19(4) establishes a **3-tier reporting timeline**:
| Tier | Trigger | OJ time limit |
|---|---|---|
| (a) Initial notification | After awareness of major incident | RTS (Art. 20(a)(ii)) |
| (b) Intermediate report | Status change / new information / CA request | RTS (Art. 20(a)(ii)) |
| (c) Final report | Root cause analysis completed + actual impact figures available | RTS (Art. 20(a)(ii)) |
**None of these time limits live in OJ.** The literal Art. 19(4) chapeau says `within the time limits to be laid down in accordance with Article 20, first paragraph, point (a), point (ii)` — the OJ text references an RTS that was not in force at the time the regulation was adopted. As of mid-2025, **Reg. (EU) 2024/2956 Annex II** addresses the initial-notification content and Annex IV addresses the templates, but the per-tier time limits are layered with sectoral differentiation (Art. 20 chapeau: `different time limits may reflect, as appropriate, specificities of financial sectors`).
- **Berry anchor:** §3.3.1 (`time limits`); §5.7 (temporal); §5.1 (`specificities`).
#### 6.8 Art. 19 — voluntary cyber-threat notification vs. mandatory incident reporting
Ch. III distinguishes **mandatory** incident reporting (Art. 19(1), 19(4)) from **voluntary** cyber-threat notification (Art. 19(2)). The voluntary notification is at entity discretion and for significant cyber threats (DORA-D13, defined per Art. 18(2)).
The asymmetry is:
| Trigger | Mandatory? |
|---|---|
| Major ICT-related incident | **Yes** — Art. 19(1)+(4) |
| Significant cyber threat | **No** — Art. 19(2) voluntary |
- **Berry anchor:** §3.3.1 (`may, on a voluntary basis`); §5.1 (`deem`).
- **Structural implication:** the asymmetry preserves entity discretion on **pre-incident** intelligence but mandates **post-incident** reporting.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in this file inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; Art. 3(5) `ICT risk`; Art. 3(30) `management body` (composite cross-reference, see pilot file §2.10). The Art. 3(22) `critical or important function` (S3 tautology, see pilot file §2.7) propagates to Art. 6(8)(f).

### from regs/DORA.ambiguity.md

**Proportionality-status:** **THIS IS ART. 4** — the clause is the proportionality chapeau.
**Scope:** financial entity.
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system` (Ch. II is ICT-risk-management chapter).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`effective`, `prudent`); §5.4.7 (AND); cf. CRA-CL27 `handled effectively` (same pattern).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** Art. 4's proportionality pattern mirrors **NIS 2 Art. 1(2)** (proportionality in scope) and **CRA Art. 1(2)** (proportionality for microenterprises and SMEs). DORA Art. 4 is more elaborate than either, providing explicit CA-review (CL4-3) that NIS 2 and CRA do not have.


### from regs/DORA.ambiguity.md

The content of the initial notification is undefined. Same Berry `notification` pattern as GDPR Art. 33(1), CRA Art. 14, NIS 2 Art. 23(4)(a). S3 (content + format + time limit all depend on RTS).

### from regs/DORA.ambiguity.md

`likely` undefined; `severe consequences` undefined; `financial markets` undefined. Same Berry cluster as NIS 2 CL27 (`likely to adversely affect`). S3.

### from regs/DORA.ambiguity.md

- **Structural implication:** the Ch. III timeline is **functionally identical to NIS 2 Art. 23(4)** (24h/72h/1-month triple tier) and **GDPR Art. 33** (72h notification) in spirit, but the **specific hour-anchors are sector-differentiated** rather than uniform. This is a deliberate DORA design choice (per recital 56: `duly consideration to any specific feature arising from the distinct nature of activities across different financial services sectors`).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the NIS 2 24h/72h/1-month trio is the **uniform template**; DORA adopts a **sector-differentiated template** that is more flexible but less predictable. **Layer 2 must surface this design divergence.**


### from regs/DORA.ambiguity.md

This is **structurally different** from the NIS 2 model (where significant cyber threats are part of Art. 23(11) implementing-acts scope and Art. 23(2) voluntary cyber-threat communication to recipients only). DORA's Art. 19(2) is **CA-directed** (the entity notifies the CA, not the recipients); NIS 2's Art. 23(2) is **recipient-directed**.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the closest parallel is **NIS 2 Art. 23(2)** (recipients-communication of cyber threats) — but NIS 2 only requires entity-to-recipient communication; DORA Art. 19(2) only requires entity-to-CA communication. **The two are not strictly equivalent.** Layer 2 must adjudicate the divergence.


<!-- aegis:purity: own_reg=DORA; demoted=10; core_cross_mentions=0 -->