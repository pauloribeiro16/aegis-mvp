# D-09.4 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.1 NIS2-CL07 — Art. 21(1) sentence 1 — Risk-management core obligation
**Source locus:**
> Member States shall ensure that essential and important entities take **<mark>appropriate and proportionate technical, operational and organisational measures</mark>** to manage the risks posed to the security of network and information systems which those entities use for their operations or for the provision of their services, and to prevent or minimise the **impact** of incidents on recipients of their services and on other services.
**Instance 1 — VAG — S3 — `appropriate and proportionate`**
The opening qualifier. Three materially distinct readings:
- **R1:** `appropriate` and `proportionate` are independent (entity must satisfy both tests, separately).
- **R2:** `appropriate` modifies `proportionate` (entity must satisfy proportionality, with `appropriate` as a placeholder synonym).
- **R3:** `appropriate and proportionate` is a single compound qualifier (a fixed phrase).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent | None in OJ |
| R2 | Hierarchical | None in OJ |
| R3 | Compound | In-Directive: Art. 21(1) sentence 2 operationalises proportionality by specific factors (exposure, size, likelihood, severity) |
R1 and R3 produce materially distinct compliance obligations (R1 admits two separate failure modes; R3 admits one composite test). S3.
This is the dominant VAG trigger of NIS 2. **It propagates to all 10 sub-points of Art. 21(2)(a)–(j) and to Art. 21(3) and Art. 21(4).** Every measure listed in Art. 21(2) inherits the `appropriate and proportionate` qualifier by reference to "The measures referred to in paragraph 1".
*Berry anchor:* §5.1 (`appropriate`, `proportionate`).
**Instance 2 — POLY — S2 — `technical, operational and organisational measures`**
Three-term coordination. Three readings:
- **R1:** Three distinct categories of measures (entity must implement at least one of each).
- **R2:** Cumulative description (a measure is "technical, operational and organisational" if it has all three characteristics).
- **R3:** Open list (entity may add more categories).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct categories | In-Directive: literal `technical, operational and organisational` |
| R2 | Cumulative single measure | None in OJ |
| R3 | Open list | In-Directive: recital 56 (proportionality) |
R1 is the literal reading. R3 is the dominant reading (recital 56 implies entity-discretion on additional categories). S2.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 3 — VAG + POLY — S2 — `manage the risks`**
`manage the risks` — what counts as `management`? Reading:
- **R1:** Identify + assess + mitigate.
- **R2:** Treat (avoid, accept, transfer, mitigate).
- **R3:** Continuous monitoring + adjustment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Identify-assess-mitigate | None in OJ; ISO/IEC 27005 |
| R2 | ISO 27005 risk-treatment | None in OJ; ISO/IEC 27005 |
| R3 | Continuous monitoring | None in OJ; NIST RMF |
*Berry anchor:* §3.3.1 (`manage`).
**Instance 4 — POLY — S2 — `impact`**
`impact` — on recipients of services (downstream effect) or on other services (cascading effect)?
- **R1:** Impact on direct recipients.
- **R2:** Impact on other services (cascade).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Recipients | In-Directive: literal `recipients of their services` |
| R2 | Other services | In-Directive: literal `on other services` |
| R3 | Both | In-Directive: literal `recipients … and … other services` |
R3 is the literal reading (coordinated by `and`). The fact that the two objects are coordinated by AND rather than OR means the entity must consider impact on both. S2 because the surface ambiguity is between "focus on direct recipients" and "consider cascading effects".
*Berry anchor:* §3.3.1 (`impact`); §5.4.7 (AND).
---
#### 3.6 NIS2-CL12 — Art. 21(2)(c) — Business continuity, backup, disaster recovery, crisis management
**Source locus:**
> **(c)** business continuity, such as backup management and disaster recovery, and crisis management;
**Instance 1 — VAG + POLY — S2 — `business continuity`**
- **R1:** Service continuity (operational).
- **R2:** Data continuity (backup-restoration).
- **R3:** Organisational continuity (going-concern).
- **R4:** All three (cumulative).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Service | None in OJ |
| R2 | Data | None in OJ |
| R3 | Organisational | None in OJ |
| R4 | Cumulative | In-Directive: `such as backup management and disaster recovery` (R2 implied) + `crisis management` (R3 implied) |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`business continuity`).
**Instance 2 — COORD — S3 — `business continuity, such as backup management and disaster recovery, and crisis management`**
The structure is `BC, such as [examples], and CM`. The `such as` opens an illustrative list (Berry §5.1 `include` pattern) inside an AND of `business continuity` and `crisis management`. The nesting admits ≥3 parse trees:
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | BC + (examples) + CM, all required | In-Directive: literal reading |
| R2 | BC + (examples) are illustrative, CM is independent | None in OJ |
| R3 | BC and CM are the two required; examples are floor | None in OJ |
R1 and R3 produce materially distinct compliance obligations (R1 mandates all three; R3 admits partial compliance). S3.
*Berry anchor:* §5.1 (`such as`); §5.5 (nested coordination).
**Instance 3 — POLY — S2 — `crisis management`**
- **R1:** Strategic crisis management (executive-level coordination, communication).
- **R2:** Tactical crisis management (operational, technical).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strategic | None in OJ; ISO 22361 |
| R2 | Tactical | None in OJ; ISO 22361 |
| R3 | Both | None in OJ; recital 56 |
*Berry anchor:* §3.3.1 (`crisis management`).
**Instance 4 — POLY — S2 — `backup management`**
- **R1:** `backup management` = backup policy.
- **R2:** `backup management` = backup operations (tape rotation, offsite storage).
- **R3:** `backup management` = backup recovery testing.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Policy | None in OJ |
| R2 | Operations | None in OJ; ISO 22301 |
| R3 | Recovery testing | None in OJ; ISO 22301 |
*Berry anchor:* §3.3.1 (`backup management`).
**Instance 5 — POLY — S2 — `disaster recovery`**
- **R1:** `disaster recovery` = IT-DR (technical recovery of systems).
- **R2:** `disaster recovery` = site recovery (physical site restoration).
- **R3:** `disaster recovery` = both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | IT | None in OJ; ISO 24762 |
| R2 | Site | None in OJ; ISO 24762 |
| R3 | Both | None in OJ |
*Berry anchor:* §3.3.1 (`disaster recovery`).
---
#### 3.16 NIS2-CL22 — Art. 21(4) — Corrective measures
**Source locus:**
> Member States shall ensure that an entity that finds that it does not comply with the measures provided for in paragraph 2 takes, **<mark>without undue delay</mark>**, all **<mark>necessary, appropriate and proportionate corrective measures</mark>**.
**Instance 1 — VAG — S3 — `without undue delay`**
- **R1:** `without undue delay` = 24 hours.
- **R2:** `without undue delay` = 72 hours.
- **R3:** `without undue delay` = reasonable time considering the nature of the non-compliance.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 24 h | None in OJ |
| R2 | 72 h | None in OJ |
| R3 | Reasonable | In-Directive: standard EU drafting convention; recital 60 |
R3 is the dominant reading. R1 and R2 are Member-State-implementation divergences. S3.
*Berry anchor:* §5.1 (`undue`).
**Instance 2 — VAG — S3 — `necessary, appropriate and proportionate corrective measures`**
Triple-vague qualifier. The three adjectives (necessary/appropriate/proportionate) are coordinated by AND. The same Berry pattern as the opening of Art. 21(1). Each modifier is open; the combination admits ≥3 readings:
- **R1:** All three are independent (entity must satisfy all three tests).
- **R2:** All three are synonyms (compound description).
- **R3:** `necessary` is a floor, `appropriate` is a target, `proportionate` is a ceiling.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent | None in OJ |
| R2 | Synonyms | None in OJ |
| R3 | Floor/target/ceiling | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`necessary`, `appropriate`, `proportionate`).
**Instance 3 — POLY — S2 — `corrective measures`**
- **R1:** `corrective measures` = fixes to the non-compliant measure.
- **R2:** `corrective measures` = compensating controls.
- **R3:** `corrective measures` = root-cause remediation.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Fixes | In-Directive: literal |
| R2 | Compensating | None in OJ |
| R3 | Root-cause | None in OJ; ISO/IEC 27001 corrective-action concept |
*Berry anchor:* §3.3.1 (`corrective measures`).
---
### 4. Cross-clause structural observations (Art. 21)
3. **Three sub-points of Art. 21(2) coordinate three distinct security domains in a single phrase** ((c), (i), (j)). Berry §5.5 parallelism: the structural symmetry invites the reading that each domain is an independent obligation, but the clause does not signal whether partial compliance is acceptable. **This is the dominant S3 pattern in Art. 21.**
6. **`direct` in Art. 21(2)(d) is the single most consequential scope-limiter.** The reading determines whether the obligation reaches 1-hop, n-hop, or only contractual counter-parties. The Directive is silent; the Commission's 17 October 2024 implementing acts (Art. 21(5)) were expected to clarify this but as of mid-2025 are not yet published.
7. **T3-vs-text gaps are the most extensive in the corpus so far.** At least 6 sub-points (b, d, e, f, g, h, i, j) are split by T3 into multiple T3 clauses that the OJ text does not support. The at-rest/in-transit/key-management split (h) is the largest single gap: three T3 clauses on one OJ sub-point.
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| NIS2-C03 | Art. 21(2)(a) | NIS2-CL10 | Art. 21(2)(a) | Same locus. v0.2 adds propagated VAG from 21(1) opening. |
| NIS2-C04 | Art. 21(2)(a) | (merged into CL10) | Art. 21(2)(a) | T3 split risk-analysis from IS-security; v0.2 treats them as one composite clause. |
| NIS2-C05 | Art. 21(2)(b) | NIS2-CL11 | Art. 21(2)(b) | Same locus; v0.2 adds 6-action-list POLY from Art. 6(8). |
| NIS2-C29 | Art. 21(2)(b) | (merged into CL11) | Art. 21(2)(b) | T3 split "real-time" detection from incident handling; v0.2 rejects the split (T3-vs-text gap). |
| NIS2-C06 | Art. 21(2)(c) | NIS2-CL12 | Art. 21(2)(c) | Same locus; v0.2 expands 3-term coordination analysis. |
| NIS2-C07 | Art. 21(2)(c) | (merged into CL12) | Art. 21(2)(c) | T3 split BC and CM; v0.2 keeps them coordinated. |
| NIS2-C08 | Art. 21(2)(d) | NIS2-CL13 | Art. 21(2)(d) | Same locus; v0.2 expands `direct` SCOPE-Q analysis. |
| NIS2-C09 | Art. 21(2)(d) | (merged into CL13) | Art. 21(2)(d) | T3 split contractual security; v0.2 keeps one composite. |
| NIS2-C10 | Art. 21(2)(e) | NIS2-CL14 | Art. 21(2)(e) | Same locus; v0.2 expands 3-term coordination. |
| NIS2-C11 | Art. 21(2)(e) | (T3-vs-text gap noted in CL14) | Art. 21(2)(e) | T3 read "CI/CD Pipeline"; v0.2 rejects the reading. |
| NIS2-C12 | Art. 21(2)(e) | (merged into CL14) | Art. 21(2)(e) | T3 split vulnerability handling; v0.2 keeps it as a sub-phrase. |
| NIS2-C13 | Art. 21(2)(f) | NIS2-CL15 | Art. 21(2)(f) | Same locus. |
| NIS2-C14 | Art. 21(2)(g) | NIS2-CL16 | Art. 21(2)(g) | Same locus; v0.2 expands POLY. |
| NIS2-C15 | Art. 21(2)(g) | (T3-vs-text gap noted in CL16) | Art. 21(2)(g) | T3 read "role-specific"; v0.2 rejects. |
| NIS2-C16-18 | Art. 21(2)(h) | NIS2-CL17 | Art. 21(2)(h) | T3 split at-rest/in-transit/key-mgmt; v0.2 keeps as one composite. |
| NIS2-C19 | Art. 21(2)(i) | NIS2-CL18 | Art. 21(2)(i) | Same locus. |
| NIS2-C20 | Art. 21(2)(i) | (T3-vs-text gap noted in CL18) | Art. 21(2)(i) | T3 read RBAC/need-to-know/least-privilege; v0.2 rejects. |
| NIS2-C21 | Art. 21(2)(j) | NIS2-CL19 | Art. 21(2)(j) | Same locus; v0.2 expands 4-obligation coordination. |
| NIS2-C22 | Art. 21(2)(j) | (T3-vs-text gap noted in CL19) | Art. 21(2)(j) | T3 read "logging"; v0.2 rejects. |
| (none) | — | NIS2-CL20 | Art. 21(3) sentence 1 | T3 partially covered (NIS2-C23, C24); v0.2 keeps as one composite. |
| (none) | — | NIS2-CL21 | Art. 21(3) sentence 2 | T3 omitted Art. 22 propagation; v0.2 includes. |
| (none) | — | NIS2-CL22 | Art. 21(4) | T3 omitted the corrective-measures clause; v0.2 includes. |
| (none) | — | NIS2-CL07, CL08, CL09 | Art. 21(1), (2) chapeau | T3 omitted the 21(1) opening, factors, and all-hazards chapeau; v0.2 includes. |
**Net: 21 T3 clauses → 16 v0.2 clauses (T3 splits rejected; v0.2 adds 4 new clauses that T3 omitted).**
---
**End of Art. 21 file. Next: `04_NIS2_Art22_SupplyChain.md` (shorter — Art. 22 has 2 paragraphs).**
#### 3.3 NIS2-CL28 — Art. 23(1) ¶1 — Cross-border information
**Source locus:**
> Each Member State shall ensure that those entities report, inter alia, any information enabling the CSIRT or, where applicable, the competent authority to determine any cross-border impact of the incident.
**Instance 1 — VAG — S2 — `inter alia`**
`inter alia` — among other things. The reporting is non-exhaustive; the entity may report more than the listed items. Standard EU drafting; the cross-border-impact info is mandatory, but other info is permitted.
*Berry anchor:* §3.3.1 (`inter alia`).
**Instance 2 — VAG — S2 — `cross-border impact`**
`cross-border impact` — impact in how many Member States? Impact of what kind?
- **R1:** Impact in two or more Member States.
- **R2:** Impact on cross-border services (single MS but cross-border flow).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ≥2 MS | In-Directive: Art. 6(7) `large-scale cybersecurity incident` |
| R2 | Cross-border services | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`cross-border`); §5.2.1 (`cross-border`).
---
## NIS 2 v0.2 — Article 24 Use of European Cybersecurity Certification Schemes
> **Source.** OJ L 333, 27.12.2022, p. 130–131. `03_REFERENCE_MATERIAL/Regulatory_References/NIS2.txt`, lines ~3020–3050.
>
> **Pattern.** Article quoted in full, then per-clause analysis.
>
> **Article 24 has 3 paragraphs and is short.** It is the only provision in Chapter IV that allows Member States to *require* the use of European cybersecurity certification schemes — a binding-certification hook that integrates the Cybersecurity Act (Reg. 2019/881) into NIS 2 enforcement.
---
### 1. Article 24 — full text
> **Article 24 — Use of European cybersecurity certification schemes**
>
> **1.** In order to demonstrate compliance with particular requirements of Article 21, Member States **<mark>may require</mark>** essential and important entities to use particular ICT products, ICT services and ICT processes, developed by the essential or important entity or procured from third parties, that are **certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881**. Furthermore, Member States shall encourage essential and important entities to use **<mark>qualified trust services</mark>**.
> **2.** The Commission is empowered to adopt delegated acts, in accordance with Article 38, to supplement this Directive by specifying which categories of essential and important entities are to be required to use certain certified ICT products, ICT services and ICT processes or obtain a certificate under a European cybersecurity certification scheme adopted pursuant to Article 49 of Regulation (EU) 2019/881. Those delegated acts shall be adopted where insufficient levels of cybersecurity have been identified and shall include an implementation period.
>
> Before adopting such delegated acts, the Commission shall carry out an impact assessment and shall carry out consultations in accordance with Article 56 of Regulation (EU) 2019/881.
>
> **3.** Where no appropriate European cybersecurity certification scheme for the purposes of paragraph 2 of this Article is available, the Commission may, after consulting the Cooperation Group and the European Cybersecurity Certification Group, request ENISA to prepare a candidate scheme pursuant to Article 48(2) of Regulation (EU) 2019/881.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| NIS2-CL48 | Art. 24(1) sentence 1 (certification requirement) | Certification hook | **S2** | Member States may require entities to use certified ICT products/services/processes. |
| NIS2-CL49 | Art. 24(1) sentence 2 (qualified trust services) | Encouragement | **S2** | Member States shall encourage use of qualified trust services. |
| NIS2-CL50 | Art. 24(2) (Commission delegated acts) | Delegated acts | **S2** | Commission may specify which entities must use certified products. |
| NIS2-CL51 | Art. 24(3) (ENISA candidate scheme) | ENISA power | **S2** | Commission may request ENISA to prepare a candidate scheme. |
**Total: 4 atomic clauses.**
---
### 3. Detailed cards
#### 3.1 NIS2-CL48 — Art. 24(1) sentence 1 — Certification requirement
**Source locus:**
> In order to demonstrate compliance with particular requirements of Article 21, Member States **<mark>may require</mark>** essential and important entities to use particular ICT products, ICT services and ICT processes, developed by the essential or important entity or procured from third parties, that are **certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881**.
**Instance 1 — VAG — S2 — `may require`**
Member State discretion. Three readings:
- **R1:** Pure discretion — each MS decides.
- **R2:** Discretion conditioned on Art. 21 compliance — `In order to demonstrate compliance`.
- **R3:** Discretion conditioned on Commission delegated acts (Art. 24(2)).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Discretion | In-Directive: literal `may require` |
| R2 | Compliance-conditioned | In-Directive: literal `In order to demonstrate compliance` |
| R3 | Commission-conditioned | In-Directive: Art. 24(2) |
R1 is the literal reading; R2 and R3 are contextual modifiers. S2.
*Berry anchor:* §3.3.1 (`may require`).
**Instance 2 — VAG — S2 — `particular requirements of Article 21`**
`particular requirements` — which sub-points of Art. 21(2)(a)–(j)?
- **R1:** Any sub-point.
- **R2:** Only sub-points that are certification-relevant (e.g. cryptography (h), access control (i), MFA (j)).
- **R3:** Sub-points explicitly named in delegated acts.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any | In-Directive: literal |
| R2 | Certification-relevant | None in OJ |
| R3 | Delegated-act-named | In-Directive: Art. 24(2) |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`particular`).
**Instance 3 — POLY — S2 — `ICT products, ICT services and ICT processes`**
Three categories (AND). Same coordination pattern as Art. 22(1) (CL23) and Art. 21(2) (NIS2-CL07).
- **R1:** Three distinct categories (any of which may be required).
- **R2:** Composite (entity may use any of the three).
- **R3:** All three required cumulatively.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal |
| R2 | Composite | None in OJ |
| R3 | All | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`ICT products`/`ICT services`/`ICT processes`); §5.5 (three-way coordination).
**Instance 4 — POLY — S2 — `developed by the essential or important entity or procured from third parties`**
The OR between in-house and procured.
- **R1:** In-house or procured (entity's choice).
- **R2:** The certification requirement applies only to procured (third-party) products.
- **R3:** Applies to both equally.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity choice | In-Directive: literal |
| R2 | Procured only | None in OJ |
| R3 | Both equally | In-Directive: literal `or` |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 5 — VAG — S2 — `European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881`**
Cross-reference to the Cybersecurity Act. The schemes are defined and adopted by the CSA. The Directive imports the CSA's certification architecture.
*Berry anchor:* §3.3.1 (`European cybersecurity certification schemes`).
---
#### 3.2 NIS2-CL49 — Art. 24(1) sentence 2 — Qualified trust services
**Source locus:**
> Furthermore, Member States shall encourage essential and important entities to use **<mark>qualified trust services</mark>**.
**Instance 1 — VAG — S2 — `shall encourage`**
`shall encourage` — same as Art. 20(2) (NIS2-CL05). Discretionary encouragement; not binding.
*Berry anchor:* §3.3.1 (`shall encourage`).
**Instance 2 — POLY — S2 — `qualified trust services`**
Cross-reference to Art. 6(26) `qualified trust service` (Reg. 910/2014 / eIDAS). Inherits the eIDAS definition.
*Berry anchor:* §3.3.1 (`qualified trust services`).
---
#### 3.3 NIS2-CL50 — Art. 24(2) — Commission delegated acts
**Source locus:**
> The Commission is empowered to adopt delegated acts, in accordance with Article 38, to supplement this Directive by specifying which categories of essential and important entities are to be required to use certain certified ICT products, ICT services and ICT processes or obtain a certificate under a European cybersecurity certification scheme adopted pursuant to Article 49 of Regulation (EU) 2019/881. Those delegated acts shall be adopted where insufficient levels of cybersecurity have been identified and shall include an implementation period.
**Instance 1 — VAG — S2 — `insufficient levels of cybersecurity`**
`insufficient levels` — measured how? By what methodology?
- **R1:** Measured by CSA (ENISA threat landscape).
- **R2:** Measured by national CSAs.
- **R3:** Measured by incident statistics (Art. 23).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ENISA | In-Directive: ENISA is the closest authority |
| R2 | National CSA | None in OJ |
| R3 | Incidents | In-Directive: Art. 23 incident data |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`insufficient levels`).
**Instance 2 — VAG — S2 — `categories of essential and important entities`**
`categories` — by sector? By size? By risk profile?
- **R1:** Sector-based (Annex I/II).
- **R2:** Size-based (Rec. 2003/361/EC).
- **R3:** Risk-profile-based.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sector | In-Directive: Annex I/II |
| R2 | Size | In-Directive: Art. 3 cross-ref |
| R3 | Risk | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`categories`).
**Instance 3 — VAG — S2 — `shall include an implementation period`**
`implementation period` — undefined. How long?
- **R1:** 6 months.
- **R2:** 12 months.
- **R3:** 24 months.
- **R4:** Discretionary.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 6m | None in OJ |
| R2 | 12m | None in OJ |
| R3 | 24m | None in OJ |
| R4 | Discretionary | In-Directive: literal `shall include` but content undefined |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`implementation period`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 33/34 and CRA Art. 14. Three materially distinct readings:

### from regs/NIS2.ambiguity.md

1. **Art. 21(1) opening is the single most consequential VAG phrase.** `appropriate and proportionate` propagates to every sub-point of Art. 21(2)(a)–(j), to Art. 21(3), and to Art. 21(4). Every clause in Art. 21 inherits S3 VAG on this opening qualifier. **This is structurally identical to GDPR Art. 32(1) opening's propagation to Art. 32(1)(a)–(d), and to CRA Annex I Part I §2 opening.**

### from regs/NIS2.ambiguity.md

2. **Art. 21(2) is structured as a 10-item list, but each item is a single phrase or short clause.** The operational content is delegated almost entirely to standards and national implementation. This makes Layer 1 findings uniformly S2-S3 — the text is too thin to generate the dense coordination ambiguities seen in GDPR Art. 4 (which has 26 definitions) or in some CRA Annex I items (which have longer compound requirements).

### from regs/NIS2.ambiguity.md

4. **`state-of-the-art` propagation is the cross-regulation Berry-classic.** Same term in GDPR Art. 25(1) and Art. 32(1) and NIS 2 Art. 21(1) sentence 2. The three regulations have begun to diverge in national transposition: German BSI standardises the term, French ANSSI requires independent assessment, Italian ACN publishes annual guidance. The Directive's silence on the term is the **single most actionable gap for harmonisation**.

### from regs/NIS2.ambiguity.md

5. **`where appropriate` is the soft-hedge pattern of Art. 21.** Three sub-points are closed by `where appropriate` (h, j — and the chapeau of (j)). The hedge softens the obligation without specifying the threshold. **Cross-regulation comparison:** GDPR Art. 32(1) `where appropriate` and CRA Art. 13(5) `as appropriate` follow the same pattern.

### from regs/NIS2.ambiguity.md

8. **The "physical environment" scope extension is the most distinctive feature of NIS 2 vs other regulations in the corpus.** All other regulations (GDPR, CRA, DORA, AI Act) are software/cyber-focused. NIS 2's all-hazards + physical-environment coverage is the unique outlier. **For software-compliance analysis, the physical-environment dimension is out-of-scope** — it does not generate software requirements.

<!-- aegis:purity: own_reg=NIS2; demoted=6; core_cross_mentions=0 -->

