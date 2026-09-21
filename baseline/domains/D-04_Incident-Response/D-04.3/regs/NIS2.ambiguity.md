# D-04.3 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 2.2 Definition (2) `security of network and information systems` (NIS2-D02)
**Source text:**
> **(2)** **`'security of network and information systems'`** means the ability of network and information systems to resist, at a given level of confidence, any event that may compromise the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, those network and information systems;
**Analysis.**
- **VAG — S3** — `at a given level of confidence`: the modifier is open. The reading determines the threshold at which an entity's security measures are deemed sufficient. Three materially distinct readings:
  - **R1:** `level of confidence` is subjective/qualitative — management attestation.
  - **R2:** `level of confidence` is relative — comparable to peer entities or sector baseline.
  - **R3:** `level of confidence` is absolute — measurable (e.g. probability metric, sigma-level).
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Subjective/qualitative (management attestation) | None in OJ |
  | R2 | Relative (peer/sector baseline) | None in OJ; ENISA security-baseline guidance |
  | R3 | Absolute (probabilistic metric) | None in OJ; ISO/IEC 27004 measurement-of-security concept |
  R1 and R3 produce materially distinct compliance obligations (R1 admits paper exercises; R3 requires measurement). R2 is intermediate. S3.
  *Berry anchor:* §5.1 (`level of confidence`).
- **POLY — S2** — `ability … to resist`: the metaphor of "resistance" implies a binary (resists/does not resist), but security is a continuous variable. The reading:
  - **R1:** Binary — the system either resists or does not.
  - **R2:** Threshold — the system resists all events up to a defined threshold.
  - **R3:** Probabilistic — the system resists with a defined probability.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Binary resistance | None in OJ |
  | R2 | Threshold resistance | None in OJ; ISO/IEC 27005 risk-threshold concept |
  | R3 | Probabilistic resistance | None in OJ; FAIR / NIST 800-30 quantitative-risk concept |
  *Berry anchor:* §3.3.1 (`ability to resist`).
- **COORD — S2** — `availability OR authenticity OR integrity OR confidentiality` (OR of four CIA-triad dimensions plus authenticity). The reading:
  - **R1:** Compromise of any one dimension triggers the security obligation.
  - **R2:** The four dimensions are the full CIA-A set; an entity is "secure" only if all four are protected.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Any one compromise = security event | None in OJ; recital 32 (cybersecurity) |
  | R2 | All four must be protected | None in OJ; NIST CSF core functions |
  *Berry anchor:* §5.4.7 (OR across four sub-clauses).
- **Layer 1 observation** — The definition defines the **state of security**, not the **state of cybersecurity**. NIS 2(2) `security of network and information systems` is a broader concept than NIS 2(3) `cybersecurity`. (3) is a cross-reference to Reg. 2019/881. The boundary between "security of network and information systems" and "cybersecurity" in NIS 2 itself is not drawn in Art. 6 — the Directive uses both terms (e.g. Art. 1(2) "high common level of cybersecurity", Art. 21(1) "security of network and information systems"). A purely linguistic Layer 1 reading flags this terminological overlap for Layer 2 adjudication.
---
## NIS 2 v0.2 — Article 23 Reporting Obligations
---
### 1. Article 23 — full text
> **Article 23 — Reporting obligations**
>
> **1.** Each Member State shall ensure that essential and important entities notify, **<mark>without undue delay</mark>**, its CSIRT or, where applicable, its competent authority in accordance with paragraph 4 of any incident that has a **significant impact** on the provision of their services as referred to in paragraph 3 (significant incident). Where appropriate, entities concerned shall notify, **without undue delay**, the recipients of their services of significant incidents that are likely to adversely affect the provision of those services. Each Member State shall ensure that those entities report, inter alia, any information enabling the CSIRT or, where applicable, the competent authority to determine any cross-border impact of the incident. The mere act of notification shall not subject the notifying entity to increased liability.
>
> Where the entities concerned notify the competent authority of a significant incident under the first subparagraph, the Member State shall ensure that that competent authority forwards the notification to the CSIRT upon receipt.
>
> In the case of a cross-border or cross-sectoral significant incident, Member States shall ensure that their single points of contact are provided in due time with relevant information notified in accordance with paragraph 4.
>
> **2.** Where applicable, Member States shall ensure that essential and important entities communicate, **without undue delay**, to the recipients of their services that are potentially affected by a significant cyber threat any measures or remedies that those recipients are able to take in response to that threat. Where appropriate, the entities shall also inform those recipients of the significant cyber threat itself.
> **3.** An incident shall be considered to be significant if:
> **(a)** it has caused or is capable of causing **<mark>severe operational disruption</mark>** of the services or **financial loss** for the entity concerned;
> **(b)** it has affected or is capable of affecting other natural or legal persons by causing **<mark>considerable material or non-material damage</mark>**.
> **4.** Member States shall ensure that, for the purpose of notification under paragraph 1, the entities concerned submit to the CSIRT or, where applicable, the competent authority:
> **(a)** **<mark>without undue delay and in any event within 24 hours of becoming aware of the significant incident</mark>**, an early warning, which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact;
> **(b)** **<mark>without undue delay and in any event within 72 hours of becoming aware of the significant incident</mark>**, an incident notification, which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise;
> **(c)** upon the request of a CSIRT or, where applicable, the competent authority, an intermediate report on relevant status updates;
> **(d)** a final report **not later than one month** after the submission of the incident notification under point (b), including the following:
> (i) a detailed description of the incident, including its severity and impact;
> (ii) the type of threat or root cause that is likely to have triggered the incident;
> (iii) applied and ongoing mitigation measures;
> (iv) where applicable, the cross-border impact of the incident;
> **(e)** in the event of an ongoing incident at the time of the submission of the final report referred to in point (d), Member States shall ensure that entities concerned provide a progress report at that time and a final report within one month of their handling of the incident.
>
> By way of derogation from the first subparagraph, point (b), a trust service provider shall, with regard to significant incidents that have an impact on the provision of its trust services, notify the CSIRT or, where applicable, the competent authority, **without undue delay and in any event within 24 hours** of becoming aware of the significant incident.
>
> **5.** The CSIRT or the competent authority shall provide, **without undue delay and where possible within 24 hours** of receiving the early warning referred to in paragraph 4, point (a), a response to the notifying entity, including initial feedback on the significant incident and, upon request of the entity, guidance or operational advice on the implementation of possible mitigation measures. …
> **6.** Where appropriate, and in particular where the significant incident concerns two or more Member States, the CSIRT, the competent authority or the single point of contact shall inform, without undue delay, the other affected Member States and ENISA of the significant incident. …
> **7.** Where public awareness is necessary to prevent a significant incident or to deal with an ongoing significant incident, or where disclosure of the significant incident is otherwise in the public interest, a Member State's CSIRT or, where applicable, its competent authority, and, where appropriate, the CSIRTs or the competent authorities of other Member States concerned, may, after consulting the entity concerned, inform the public about the significant incident or require the entity to do so.
> **8.** At the request of the CSIRT or the competent authority, the single point of contact shall forward notifications received pursuant to paragraph 1 to the single points of contact of other affected Member States.
> **9.** The single point of contact shall submit to ENISA every three months a summary report, including anonymised and aggregated data on significant incidents, incidents, cyber threats and near misses notified in accordance with paragraph 1 of this Article and with Article 30. …
> **10.** The CSIRTs or, where applicable, the competent authorities shall provide to the competent authorities under Directive (EU) 2022/2557 information about significant incidents, incidents, cyber threats and near misses notified in accordance with paragraph 1 of this Article and with Article 30 by entities identified as critical entities under Directive (EU) 2022/2557.
> **11.** The Commission may adopt implementing acts further specifying the type of information, the format and the procedure of a notification submitted pursuant to paragraph 1 of this Article and to Article 30 and of a communication submitted pursuant to paragraph 2 of this Article. By 17 October 2024, the Commission shall, with regard to DNS service providers, TLD name registries, cloud computing service providers, data centre service providers, content delivery network providers, managed service providers, managed security service providers, as well as providers of online marketplaces, of online search engines and of social networking services platforms, adopt implementing acts further specifying the cases in which an incident shall be considered to be significant as referred to in paragraph 3. …
---
### 2. Atomic clause map (Art. 23)
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| NIS2-CL26 | Art. 23(1) ¶1 (notification to CSIRT) | Notification core | **S3** | Entities notify CSIRT of significant incidents without undue delay. |
| NIS2-CL27 | Art. 23(1) ¶1 (recipient notification) | Recipient comms | **S2** | Entities notify recipients of services of significant incidents affecting them. |
| NIS2-CL28 | Art. 23(1) ¶1 (cross-border info) | Cross-border info | **S2** | Report info enabling cross-border impact determination. |
| NIS2-CL29 | Art. 23(1) ¶1 (no-increased-liability) | Liability shield | **S2** | Notification does not subject entity to increased liability. |
| NIS2-CL30 | Art. 23(1) ¶2 (CA→CSIRT forwarding) | Routing | **S2** | Competent authority forwards notification to CSIRT upon receipt. |
| NIS2-CL31 | Art. 23(1) ¶3 (SPOC cross-border) | SPOC routing | **S2** | Cross-border/cross-sectoral: SPOC gets relevant info in due time. |
| NIS2-CL32 | Art. 23(2) (cyber threat comms to recipients) | Recipient comms (threat) | **S2** | Entities communicate to recipients measures/remedies against significant cyber threat. |
| NIS2-CL33 | Art. 23(3)(a) (significant-incident test A) | Significant-incident definition | **S3** | Severe operational disruption or financial loss. |
| NIS2-CL34 | Art. 23(3)(b) (significant-incident test B) | Significant-incident definition | **S3** | Considerable material or non-material damage to other persons. |
| NIS2-CL35 | Art. 23(4)(a) (early warning 24h) | Reporting tier 1 | **S3** | Early warning within 24h of becoming aware. |
| NIS2-CL36 | Art. 23(4)(b) (incident notification 72h) | Reporting tier 2 | **S3** | Incident notification within 72h, with severity/impact/IOC. |
| NIS2-CL37 | Art. 23(4)(c) (intermediate report) | Reporting tier 3 | **S2** | Intermediate report on CSIRT request. |
| NIS2-CL38 | Art. 23(4)(d) (final report 1m) | Reporting tier 4 | **S2** | Final report 1 month after (b), with 4 sub-points. |
| NIS2-CL39 | Art. 23(4)(e) (ongoing incident) | Reporting tier 5 | **S2** | Ongoing incident: progress report + 1-month final. |
| NIS2-CL40 | Art. 23(4) ¶2 (TSP derogation) | TSP-specific | **S2** | Trust service providers: 24h regardless of tier. |
| NIS2-CL41 | Art. 23(5) (CSIRT response 24h) | Authority response | **S2** | CSIRT responds within 24h with initial feedback. |
| NIS2-CL42 | Art. 23(6) (cross-border MS notification) | Cross-MS info | **S2** | Other affected MS + ENISA informed without undue delay. |
| NIS2-CL43 | Art. 23(7) (public disclosure) | Public disclosure | **S2** | Public disclosure of significant incident if in public interest. |
| NIS2-CL44 | Art. 23(8) (SPOC forwarding) | SPOC routing | **S2** | SPOC forwards to other MS SPOCs on request. |
| NIS2-CL45 | Art. 23(9) (ENISA quarterly) | Aggregation | **S2** | SPOC submits summary report to ENISA every 3 months. |
| NIS2-CL46 | Art. 23(10) (CER info-sharing) | CER cross-ref | **S2** | CSIRTs/CA provide info to CER Directive competent authorities. |
| NIS2-CL47 | Art. 23(11) (implementing acts) | Implementing acts | **S2** | Commission may adopt implementing acts further specifying notification. |
**Total: 22 atomic clauses for Art. 23.**
---
### 3. Detailed cards
#### 3.1 NIS2-CL26 — Art. 23(1) ¶1 — Notification to CSIRT (the core)
**Source locus:**
> Each Member State shall ensure that essential and important entities notify, **<mark>without undue delay</mark>**, its CSIRT or, where applicable, its competent authority in accordance with paragraph 4 of any incident that has a **significant impact** on the provision of their services as referred to in paragraph 3 (significant incident).
**Instance 1 — VAG — S3 — `without undue delay`**
- **R1:** `without undue delay` = 24 hours (matches Art. 23(4)(a) early-warning hard anchor).
- **R2:** `without undue delay` = reasonable time considering the nature of the incident.
- **R3:** `without undue delay` = as soon as technically feasible.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 24 h | In-Directive: Art. 23(4)(a) hard anchor |
| R2 | Reasonable | In-Directive: recital 60; standard EU drafting |
| R3 | Technically feasible | None in OJ |
R2 is the dominant reading. R1 is the practical baseline. S3.
*Berry anchor:* §5.1 (`undue`).
**Instance 2 — VAG — S3 — `significant impact`**
`significant impact` — the threshold term. Defined in Art. 23(3) (CL33 + CL34) but `significant impact` itself is shorthand for the test result. The reading:
- **R1:** `significant impact` = severe operational disruption (Art. 23(3)(a) test A).
- **R2:** `significant impact` = considerable damage to other persons (Art. 23(3)(b) test B).
- **R3:** Either test satisfied.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Test A only | In-Directive: Art. 23(3)(a) |
| R2 | Test B only | In-Directive: Art. 23(3)(b) |
| R3 | Either | In-Directive: literal `or` (Art. 23(3) chapeau) |
R3 is the literal reading (OR). S3 because R1/R2/R3 admit materially different compliance populations.
*Berry anchor:* §3.3.1 (`significant`); §5.4.7 (OR).
**Instance 3 — POLY — S2 — `incident`**
Inherits Art. 6(6) `incident` definition: `an event compromising the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, network and information systems`. Same POLY as Art. 6(6) and Art. 2 NIS 2 D02:
- **R1:** Security incident (intentional, malicious).
- **R2:** Operational incident (any disruption).
- **R3:** All-hazards (per Art. 21(2) chapeau).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Security | None in OJ; recital 32 |
| R2 | Operational | None in OJ |
| R3 | All-hazards | In-Directive: Art. 21(2) all-hazards approach |
R3 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`incident`).
**Instance 4 — POLY — S2 — `CSIRT or competent authority`**
Two alternative routing paths. Three readings:
- **R1:** CSIRT only (default).
- **R2:** Competent authority only (where no CSIRT).
- **R3:** Either (entity's choice).
- **R4:** Member State determines.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CSIRT default | In-Directive: literal `CSIRT or, where applicable, its competent authority` |
| R2 | CA fallback | In-Directive: `where applicable` |
| R3 | Entity choice | None in OJ |
| R4 | MS-determined | In-Directive: literal `where applicable` is MS-determined |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`CSIRT`/`competent authority`); §5.4.7 (OR).
**Instance 5 — SCOPE-Q — S2 — `provision of their services`**
`provision of their services` — what counts as a service? Same POLY as Art. 6(1) `network and information system` and Art. 2 NIS 2 D01.
- **R1:** Customer-facing service only.
- **R2:** Internal service (e.g. HR system).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Customer-facing | In-Directive: literal `provision of their services` |
| R2 | Internal | None in OJ |
| R3 | Both | In-Directive: recital 56 |
R3 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`services`).
---
#### 3.2 NIS2-CL27 — Art. 23(1) ¶1 — Recipient notification
**Source locus:**
> Where appropriate, entities concerned shall notify, **without undue delay**, the recipients of their services of significant incidents that are likely to adversely affect the provision of those services.
**Instance 1 — VAG — S2 — `Where appropriate`**
`Where appropriate` — soft hedge. Same readings as Art. 21(2)(h)/(j) hedge pattern.
*Berry anchor:* §5.1 (`where appropriate`).
**Instance 2 — VAG — S2 — `without undue delay` (recipient)**
Same Berry `undue` term as CL26. S2 (because the recipient-notification trigger is conditional on `Where appropriate` and the threshold is lower than CSIRT notification — the obligation is to inform, not to report with full data).
*Berry anchor:* §5.1 (`undue`).
**Instance 3 — VAG — S2 — `likely to adversely affect`**
`likely` — likelihood threshold undefined. `adversely affect` — affected how?
- **R1:** `likely` = more probable than not (>50%).
- **R2:** `likely` = non-trivial probability (>10%).
- **R3:** `likely` = any non-zero probability.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | >50% | None in OJ |
| R2 | >10% | None in OJ |
| R3 | Any | None in OJ |
R3 is the literal reading. S2.
*Berry anchor:* §5.1 (`likely`).
---
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
#### 3.4 NIS2-CL29 — Art. 23(1) ¶1 — No-increased-liability shield
**Source locus:**
> The mere act of notification shall not subject the notifying entity to increased liability.
**Instance 1 — VAG — S2 — `mere act of notification`**
`mere act` — what counts as the act? Filing the notification? Communicating with the CSIRT? Disclosing to recipients?
- **R1:** Filing the notification with CSIRT.
- **R2:** Communicating with the CSIRT.
- **R3:** Any of the above + recipient notification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Filing | In-Directive: literal `notification` |
| R2 | Communication | None in OJ |
| R3 | All | In-Directive: Art. 23(1) ¶1 covers both CSIRT and recipient notification |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`mere act`).
**Instance 2 — VAG — S2 — `increased liability`**
`increased liability` — increased relative to what baseline? Notified entity's liability if it had not notified? Peer-entity liability?
- **R1:** Increased relative to non-notifying baseline.
- **R2:** Increased relative to peer-entity liability.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Non-notifying | In-Directive: literal |
| R2 | Peer | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`increased liability`).
---
#### 3.5 NIS2-CL30 — Art. 23(1) ¶2 — CA→CSIRT forwarding
**Source locus:**
> Where the entities concerned notify the competent authority of a significant incident under the first subparagraph, the Member State shall ensure that that competent authority forwards the notification to the CSIRT upon receipt.
**Instance 1 — VAG — S2 — `upon receipt`**
`upon receipt` — immediate? Same-day? Within 24h? Same Berry `undue` family.
- **R1:** Immediate.
- **R2:** Same-day.
- **R3:** Within 24h.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Immediate | In-Directive: literal `upon receipt` |
| R2 | Same-day | None in OJ |
| R3 | 24h | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`upon receipt`).
---
#### 3.6 NIS2-CL31 — Art. 23(1) ¶3 — SPOC cross-border
**Source locus:**
> In the case of a cross-border or cross-sectoral significant incident, Member States shall ensure that their single points of contact are provided **<mark>in due time</mark>** with relevant information notified in accordance with paragraph 4.
**Instance 1 — VAG — S2 — `in due time`**
`in due time` — same Berry `undue`/`due` family but without the `undue` hedge. Slightly stronger than `without undue delay`?
- **R1:** Same as `without undue delay` (reasonable time).
- **R2:** Tighter than `without undue delay` (i.e. shorter).
- **R3:** Tied to the CSIRT/CA processing time.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Reasonable | None in OJ |
| R2 | Tighter | None in OJ |
| R3 | Tied to processing | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`in due time`).
**Instance 2 — VAG — S2 — `cross-border OR cross-sectoral`**
Two distinct trigger conditions. Three readings:
- **R1:** Cross-border (across MS).
- **R2:** Cross-sectoral (across sectors within or across MS).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cross-MS | In-Directive: literal `cross-border` |
| R2 | Cross-sector | In-Directive: literal `cross-sectoral` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.7 NIS2-CL32 — Art. 23(2) — Cyber-threat communication to recipients
**Source locus:**
> Where applicable, Member States shall ensure that essential and important entities communicate, **without undue delay**, to the recipients of their services that are potentially affected by a **significant cyber threat** any measures or remedies that those recipients are able to take in response to that threat. Where appropriate, the entities shall also inform those recipients of the significant cyber threat itself.
**Instance 1 — POLY — S2 — `significant cyber threat`**
Inherits Art. 6(11) `significant cyber threat` definition: `a cyber threat which, based on its technical characteristics, can be assumed to have the potential to have a severe impact on the network and information systems of an entity or the users of the entity's services by causing considerable material or non-material damage`. Same definitional regress as `significant incident` (Art. 23(3)).
*Berry anchor:* §3.3.1 (`significant cyber threat`).
**Instance 2 — VAG — S2 — `measures or remedies`**
`measures` (technical) + `remedies` (corrective) — same OR as Art. 21(3) supplier assessment (vulnerabilities OR quality OR procedures).
*Berry anchor:* §3.3.1 (`measures`/`remedies`); §5.4.7 (OR).
**Instance 3 — VAG — S2 — `that those recipients are able to take`**
`are able to take` — recipients' capacity? Recipients' technical capability? Recipients' contractual entitlement?
- **R1:** Technical capability.
- **R2:** Contractual entitlement.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | In-Directive: literal `are able to take` |
| R2 | Contractual | None in OJ |
| R3 | Both | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`are able to`).
---
#### 3.8 NIS2-CL33 — Art. 23(3)(a) — Significant-incident test A
**Source locus:**
> **(a)** it has caused or is capable of causing **<mark>severe operational disruption</mark>** of the services or **financial loss** for the entity concerned;
**Instance 1 — VAG — S3 — `severe operational disruption`**
`severe` — undefined; `operational disruption` — undefined. Three materially distinct readings:
- **R1:** `severe` = >X% of service capacity disrupted (e.g. >50% downtime).
- **R2:** `severe` = >X hours of downtime.
- **R3:** `severe` = qualitative judgment by management.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Capacity-based | None in OJ |
| R2 | Time-based | None in OJ |
| R3 | Qualitative | None in OJ; recital 56 |
R1 and R2 produce materially distinct compliance obligations (R1 requires capacity monitoring; R2 requires downtime tracking). R3 is rejected by Art. 23(11) implementing-acts. S3.
*Berry anchor:* §5.1 (`severe`).
**Instance 2 — VAG — S2 — `operational disruption`**
`operational` — what counts? Service outage? Performance degradation? Internal-process disruption?
- **R1:** Service outage.
- **R2:** Performance degradation.
- **R3:** Internal-process disruption.
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Outage | In-Directive: literal `disruption` |
| R2 | Degradation | None in OJ |
| R3 | Internal | None in OJ |
| R4 | All | In-Directive: recital 56 |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`operational`).
**Instance 3 — COORD — S2 — `caused OR is capable of causing`**
The OR between actual and potential.
- **R1:** Past tense only — incidents that already caused disruption.
- **R2:** Future-tense only — incidents with the *capability* to cause disruption (preventive reporting).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Past | None in OJ |
| R2 | Future-capable | None in OJ |
| R3 | Either | In-Directive: literal `caused or is capable of causing` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 4 — COORD — S2 — `severe operational disruption OR financial loss`**
The OR between operational and financial impact.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational only | In-Directive: literal `operational disruption` |
| R2 | Financial only | In-Directive: literal `financial loss` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.9 NIS2-CL34 — Art. 23(3)(b) — Significant-incident test B
**Source locus:**
> **(b)** it has affected or is capable of affecting other natural or legal persons by causing **<mark>considerable material or non-material damage</mark>**;
**Instance 1 — VAG — S3 — `considerable material or non-material damage`**
`considerable` — undefined; `material` — undefined; `non-material` — undefined. Three layered vague qualifiers. The same pattern as `severe operational disruption` (CL33) — and they are coordinated in the same definition.
- **R1:** `considerable` = quantitatively significant (e.g. >€X loss).
- **R2:** `considerable` = qualitatively significant (management judgment).
- **R3:** `considerable` = either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | None in OJ |
| R2 | Qualitative | None in OJ |
| R3 | Either | None in OJ |
S3.
*Berry anchor:* §5.1 (`considerable`).
**Instance 2 — POLY — S2 — `material damage`**
`material` — financial? Physical? Reputational? Regulatory?
- **R1:** Financial.
- **R2:** Physical.
- **R3:** Reputational.
- **R4:** Regulatory.
- **R5:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Financial | None in OJ; recital 56 |
| R2 | Physical | None in OJ |
| R3 | Reputational | None in OJ |
| R4 | Regulatory | None in OJ |
| R5 | All | In-Directive: recital 56 |
R5 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`material`).
**Instance 3 — POLY — S2 — `non-material damage`**
`non-material` — non-financial but still harm. Senses:
- **R1:** Reputational.
- **R2:** Psychological.
- **R3:** Privacy (loss of personal data).
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Reputational | None in OJ |
| R2 | Psychological | None in OJ |
| R3 | Privacy | In-Directive: GDPR Art. 2(12) personal data breach |
| R4 | All | In-Directive: recital 56 |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`non-material`).
**Instance 4 — COORD — S2 — `material OR non-material`**
The OR between damage types.
- **R1:** Material only.
- **R2:** Non-material only.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Material | In-Directive: literal |
| R2 | Non-material | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.10 NIS2-CL35 — Art. 23(4)(a) — Early warning 24h
**Source locus:**
> **(a)** **<mark>without undue delay and in any event within 24 hours of becoming aware of the significant incident</mark>**, an early warning, which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact;
**Instance 1 — VAG + COORD — S3 — `without undue delay AND in any event within 24 hours`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `without undue delay` is the primary trigger; 24h is the hard ceiling. | In-Directive: literal `without undue delay and in any event within 24 hours` |
| R2 | 24h is the primary trigger; `without undue delay` is a softer prior trigger. | None in OJ |
| R3 | Both are independent triggers (entity may satisfy either). | None in OJ |
R1 is the dominant reading (the `and in any event` conjunction binds both). S3 because R1 vs R3 admit materially distinct compliance populations (R3 admits later reporting if the entity is "without undue delay" but past 24h).
*Berry anchor:* §5.1 (`undue`); §5.7 (temporal operator); §5.4.7 (temporal AND).
**Instance 2 — SCOPE-Q + POLY — S3 — `becoming aware of the significant incident`**
- **R1:** `becoming aware` = actual knowledge (the entity knows).
- **R2:** `becoming aware` = constructive knowledge (the entity should have known).
- **R3:** `becoming aware` = either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Actual | In-Directive: literal `becoming aware` |
| R2 | Constructive | None in OJ; CJEU practice |
| R3 | Either | None in OJ |
R1 is the literal reading; R2 is the dominant judicial reading. S3 because R1 vs R2 admit materially distinct compliance populations (R2 attaches the 24h clock to incidents the entity "should have" known about).
*Berry anchor:* §3.3.1 (`becoming aware`).
**Instance 3 — VAG — S2 — `where applicable`**
`where applicable` — soft hedge on the unlawful/malicious + cross-border indications.
*Berry anchor:* §5.1 (`where applicable`).
**Instance 4 — POLY — S2 — `unlawful or malicious acts`**
Hendiadys or distinct?
- **R1:** Hendiadys.
- **R2:** Distinct (unlawful = illegal; malicious = intentional harm).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hendiadys | None in OJ |
| R2 | Distinct | In-Directive: literal `unlawful or malicious` |
R2 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.11 NIS2-CL36 — Art. 23(4)(b) — Incident notification 72h
**Source locus:**
> **(b)** **<mark>without undue delay and in any event within 72 hours of becoming aware of the significant incident</mark>**, an incident notification, which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise;
**Instance 1 — VAG + COORD — S3 — twin-trigger at 72h**
Same pattern as CL35 at 72h. S3.
*Berry anchor:* §5.1 (`undue`); §5.7 (temporal operator); §5.4.7 (temporal AND).
**Instance 2 — SCOPE-Q + POLY — S3 — `becoming aware`**
Same awareness trigger as CL35. S3.
**Instance 3 — VAG — S2 — `indicators of compromise`**
IoC — defined in cybersecurity vocabulary; the Directive does not import a definition.
- **R1:** IoC = technical indicator (IP, hash, domain).
- **R2:** IoC = behavioural indicator (TTP).
- **R3:** Any indicator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | None in OJ; MITRE ATT&CK |
| R2 | Behavioural | None in OJ; MITRE ATT&CK |
| R3 | Any | In-Directive: literal `indicators` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`indicators of compromise`).
**Instance 4 — VAG — S2 — `where available`**
Soft hedge on the IoC inclusion. The IoC is included only if the entity has it.
*Berry anchor:* §5.1 (`where available`).
---
#### 3.12 NIS2-CL37 — Art. 23(4)(c) — Intermediate report
**Source locus:**
> **(c)** upon the request of a CSIRT or, where applicable, the competent authority, an intermediate report on relevant status updates;
**Instance 1 — VAG — S2 — `upon the request`**
`upon the request` — on-demand. No temporal anchor.
*Berry anchor:* §3.3.1 (`upon the request`).
**Instance 2 — VAG — S2 — `relevant status updates`**
`relevant` — relevant to whom? Updates on what dimension?
- **R1:** Technical (containment, eradication).
- **R2:** Impact (services restored, data integrity).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | In-Directive: literal `status updates` |
| R2 | Impact | None in OJ |
| R3 | Both | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant status updates`).
---
#### 3.13 NIS2-CL38 — Art. 23(4)(d) — Final report 1m
**Source locus:**
> **(d)** a final report **not later than one month** after the submission of the incident notification under point (b), including the following:
> (i) a detailed description of the incident, including its severity and impact;
> (ii) the type of threat or root cause that is likely to have triggered the incident;
> (iii) applied and ongoing mitigation measures;
> (iv) where applicable, the cross-border impact of the incident;
**Instance 1 — VAG — S2 — `one month`**
- **R1:** Calendar month (1st to last day).
- **R2:** 30 days.
- **R3:** Working month (~22 working days).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Calendar | In-Directive: literal `one month` |
| R2 | 30 days | None in OJ |
| R3 | Working | None in OJ |
R1 is the literal reading. S2 (lower severity than CL35/CL36 because the hard anchor reduces temporal ambiguity).
*Berry anchor:* §5.7 (temporal operator).
**Instance 2 — VAG — S2 — `detailed description`**
- **R1:** `detailed` = comprehensive (full technical narrative).
- **R2:** `detailed` = sufficient for the CSIRT to act.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Comprehensive | None in OJ |
| R2 | Sufficient | None in OJ |
*Berry anchor:* §5.1 (`detailed`).
**Instance 3 — POLY — S2 — `root cause`**
`root cause` — same POLY as T3 NIS2-C27.
- **R1:** Technical root cause.
- **R2:** Organisational root cause.
- **R3:** Procedural root cause.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | None in OJ; ISO/IEC 27001 |
| R2 | Organisational | None in OJ |
| R3 | Procedural | None in OJ |
*Berry anchor:* §3.3.1 (`root cause`).
**Instance 4 — COORD — S2 — `applied AND ongoing`**
The cumulative-vs-temporal reading.
- **R1:** Cumulative (both applied-so-far and ongoing-from-now must be reported).
- **R2:** Temporal (applied-so-far, ongoing-from-now).
- **R3:** Single composite.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cumulative | In-Directive: literal `applied and ongoing` |
| R2 | Temporal | None in OJ |
| R3 | Composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND); §5.5 (parallelism).
---
#### 3.14 NIS2-CL39 — Art. 23(4)(e) — Ongoing incident
**Source locus:**
> **(e)** in the event of an ongoing incident at the time of the submission of the final report referred to in point (d), Member States shall ensure that entities concerned provide a **progress report at that time** and a **final report within one month of their handling of the incident**.
**Instance 1 — VAG — S2 — `ongoing incident`**
`ongoing` — at the time of the 1-month final report submission, the incident is still in progress.
- **R1:** `ongoing` = still under containment.
- **R2:** `ongoing` = recovery phase.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Containment | None in OJ |
| R2 | Recovery | None in OJ |
| R3 | Either | In-Directive: literal `ongoing` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`ongoing`).
**Instance 2 — VAG — S2 — `within one month of their handling of the incident`**
The 1-month clock restarts on `handling of the incident`. `handling` — POLY per Art. 6(8) (process/team/capability).
*Berry anchor:* §3.3.1 (`handling`).
---
#### 3.15 NIS2-CL40 — Art. 23(4) ¶2 — Trust service provider derogation
**Source locus:**
> By way of derogation from the first subparagraph, point (b), a trust service provider shall, with regard to significant incidents that have an impact on the provision of its trust services, notify the CSIRT or, where applicable, the competent authority, **without undue delay and in any event within 24 hours** of becoming aware of the significant incident.
**Instance 1 — POLY — S2 — `trust service`**
Inherits Art. 6(24) `trust service` (cross-reference to Reg. 910/2014 / eIDAS). The 24h hard anchor is the only anomaly: TSPs notify within 24h regardless of the (b)/(c)/(d)/(e) tier structure. TSP-specific.
*Berry anchor:* §3.3.1 (`trust service`).
**Instance 2 — VAG + COORD — S2 — `without undue delay and in any event within 24 hours` (TSP)**
Same twin-trigger as CL35/CL36 but at 24h for TSPs. S2.
---
#### 3.17 NIS2-CL42 — Art. 23(6) — Cross-MS notification
**Source locus:**
> Where appropriate, and in particular where the significant incident concerns two or more Member States, the CSIRT, the competent authority or the single point of contact shall inform, **without undue delay**, the other affected Member States and ENISA of the significant incident.
**Instance 1 — VAG — S2 — `Where appropriate`**
Soft hedge.
**Instance 2 — VAG — S2 — `in particular where the significant incident concerns two or more Member States`**
Indicator (not definition) of when cross-MS notification is appropriate.
*Berry anchor:* §5.2.1 (`two or more`).
**Instance 3 — VAG — S2 — `without undue delay` (cross-MS)**
Same Berry `undue` term. S2.
---
#### 3.19 NIS2-CL44 — Art. 23(8) — SPOC forwarding
**Source locus:**
> At the request of the CSIRT or the competent authority, the single point of contact shall forward notifications received pursuant to paragraph 1 to the single points of contact of other affected Member States.
**Instance 1 — VAG — S2 — `At the request`**
Same on-demand trigger as CL37.
*Berry anchor:* §3.3.1 (`at the request`).
---
#### 3.4 NIS2-CL51 — Art. 24(3) — ENISA candidate scheme
**Source locus:**
> Where no appropriate European cybersecurity certification scheme for the purposes of paragraph 2 of this Article is available, the Commission may, after consulting the Cooperation Group and the European Cybersecurity Certification Group, request ENISA to prepare a candidate scheme pursuant to Article 48(2) of Regulation (EU) 2019/881.
**Instance 1 — VAG — S2 — `no appropriate European cybersecurity certification scheme`**
`no appropriate` — when is a scheme not appropriate? Coverage gap? Granularity gap? Maturity gap?
- **R1:** Coverage gap (no scheme covers the entity/product type).
- **R2:** Granularity gap (scheme exists but at wrong assurance level).
- **R3:** Maturity gap (scheme exists but standards not yet harmonised).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Coverage | None in OJ |
| R2 | Granularity | None in OJ; CSA assurance levels |
| R3 | Maturity | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`no appropriate`).
**Instance 2 — VAG — S2 — `may … request ENISA`**
Discretionary. Same `may` pattern as Art. 22(1).
*Berry anchor:* §3.3.1 (`may … request`).
---
### 4. Cross-clause structural observations (Art. 24)
1. **Art. 24 is the only NIS 2 provision allowing MS to require certification.** This is the integration point with the Cybersecurity Act (Reg. 2019/881). The Directive is permissive (`may require`) but the Commission's delegated acts (Art. 24(2)) can convert permissibility into specificity.
2. **The `may require` + `shall encourage` asymmetry is deliberate.** The certification hook is permissive (Member State discretion); the trust services hook is encouragement-only (entity discretion). The asymmetry reflects the regulatory philosophy: certification is a market-instrument, trust services are a service-quality instrument.
4. **No direct entity-facing obligation in Art. 24 itself.** The entity's obligation is indirect: if the MS requires certification (Art. 24(1)) and the Commission specifies (Art. 24(2)), the entity must comply with the certification requirement to demonstrate Art. 21 compliance.
---
### 5. T3-to-v0.2 mapping
T3 had no clause for Art. 24 — it was outside the T3 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 24 with 4 atomic clauses (CL48–CL51).
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | NIS2-CL48 | Art. 24(1) sentence 1 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL49 | Art. 24(1) sentence 2 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL50 | Art. 24(2) | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL51 | Art. 24(3) | T3 omitted; v0.2 adds. |
---
**End of Art. 24 file. Next: `07_NIS2_Art25_Standardisation.md`.**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

- **VAG — S2** — `authenticity`: GDPR Art. 5(1)(d) and ISO/IEC 27000 define `authenticity`; NIS 2 does not. A reading of `authenticity` requires recourse to the broader cybersecurity-vocabulary ecosystem (ISO/IEC 27000, NIST Glossary). The Directive does not import any of these.

  *Berry anchor:* §5.1 (`authenticity` undefined).

### from regs/NIS2.ambiguity.md

> **Source.** OJ L 333, 27.12.2022, p. 128–130. `03_REFERENCE_MATERIAL/Regulatory_References/NIS2.txt`, lines ~2890–3020.
>
> **Pattern.** Article quoted in full (paragraph by paragraph), then per-clause analysis.
>
> **Article 23 is the operational consequence of Chapter IV.** It defines the 3-tier incident-reporting architecture (24h early warning / 72h incident notification / 1-month final report) that runs parallel to GDPR Art. 33/34 and CRA Art. 14. Article 23 is **the second-most-consequential article in NIS 2** (after Art. 21) for software-compliance: the reporting flow drives the entire evidence-collection and chain-of-custody apparatus that compliance-aware software must support.

### from regs/NIS2.ambiguity.md

The recurring Berry-classic vague term (GDPR Art. 33, CRA Art. 14, NIS 2 Art. 21(4)). Three materially distinct readings:

### from regs/NIS2.ambiguity.md

**Layer 1 observation — definitional regress.** Art. 23(3) defines `significant incident` using `severe` (CL33) and `considerable` (CL34), both undefined. The trigger term is therefore *less defined* than the term it purports to define. This is a definitional regress: every downstream obligation in Art. 23 (CL35–CL47) depends on resolving `severe` and `considerable`. The Art. 23(11) implementing acts (CL47) are expected to address this — but as of mid-2025 they have not been published. **The same pattern repeats in CRA Art. 14 (severe incident) and DORA Art. 18 (major ICT-related incident): three regulations, three different threshold terms, zero cross-referenced definitions.**

### from regs/NIS2.ambiguity.md

The twin-trigger temporal pattern. Same as GDPR Art. 33(1) (cross-regulation) and CRA Art. 14 (cross-regulation).

### from regs/NIS2.ambiguity.md

The awareness trigger. Same Berry pattern as GDPR Art. 33(1) and CRA Art. 14.

### from regs/NIS2.ambiguity.md

`one month` — calendar month or 30 days? Same Berry temporal question as GDPR Art. 33(4).

### from regs/NIS2.ambiguity.md

`detailed` — undefined. Same Berry VAG as GDPR Art. 33(4) `detailed`.

### from regs/NIS2.ambiguity.md

3. **`insufficient levels of cybersecurity` is the trigger for delegated acts.** Same definitional regress pattern as Art. 23(3) `significant incident`: the trigger is itself undefined, leaving Commission discretion to specify. This is structurally identical to the DORA Art. 26(11) TLPT normative-tension (binding obligation anchored to non-binding TIBER-EU).

<!-- aegis:purity: own_reg=NIS2; demoted=9; core_cross_mentions=0 -->

