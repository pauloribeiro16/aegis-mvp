# D-09.3 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
## DORA v0.2 — Chapter II Section II: ICT Risk Management Framework (Art. 7–16)
---
### 1. Articles covered
| Article | Title | Paragraphs | Cross-references | Compacted clauses |
|---|---|---|---|---|
| Art. 7 | ICT systems, protocols and tools | chapeau + 4 sub-points (a)–(d) | Art. 4 proportionality | **CL7-1** |
| Art. 8 | Identification | 7 paragraphs | Art. 6(1) framework, Art. 3(5)/(8) ICT risk and incident | **CL8-1, CL8-2, CL8-3** |
| Art. 9 | Protection and prevention | 4 paragraphs; **9(4) is the HINGE** with 6 sub-points (a)–(f) | Art. 3(2) network and information system, Art. 4 proportionality, Art. 6(1) | **CL9-1, CL9-2, CL9-3, CL9-4** |
| Art. 10 | Detection | 4 paragraphs | Art. 17, Art. 25 testing | **CL10-1, CL10-2, CL10-3** |
| Art. 11 | Response and recovery | 11 paragraphs | Art. 6(1), Art. 8, Art. 12, Art. 14, Art. 19, Art. 25 | **CL11-1, CL11-2, CL11-3, CL11-4** |
| Art. 12 | Backup policies and procedures, restoration and recovery procedures and methods | 7 paragraphs | Art. 3(2) network and information system | **CL12-1, CL12-2, CL12-3, CL12-4** |
| Art. 13 | Learning and evolving | 7 paragraphs | Art. 6(8), Art. 11, Art. 25, Art. 30(2)(i) | **CL13-1, CL13-2** |
| Art. 14 | Communication | 3 paragraphs | Art. 6(1) | **CL14-1, CL14-2** |
| Art. 15 | Further harmonisation of ICT risk management tools, methods, processes and policies | chapeau + 7 sub-points (a)–(g) | Art. 9(2), Art. 9(4)(c), Art. 10, Art. 11, Art. 6(5) | **CL15-1** |
| Art. 16 | Simplified ICT risk management framework | 3 paragraphs; **16(1) second sub-paragraph** = 8 sub-points (a)–(h) parallel to Art. 9(4) | Art. 5–15 (exemption scope) | **CL16-1, CL16-2** |
**Note on Art. 4 (Proportionality):** every operative clause card in this file carries `proportionality-status: Art. 4 applies` (per pilot convention). Art. 4 propagates to Ch. II Sec. II clauses; Art. 16(1) second sub-paragraph explicitly references `size and overall risk profile` (Art. 16(3) RTS preamble) and is itself the **proportionality-output clause** for exempted entities.
**Note on Art. 15 (RTS-pending):** Art. 15 mandates ESAs to develop draft RTS by **17 January 2024** (the deadline has passed; as of mid-2025, RTS adopting acts are either adopted or in the final adoption pipeline — **Delegated Regulation (EU) 2024/1774** of 31 May 2024 supplements DORA with the regulatory technical standards for Art. 15(a)–(g), adopted by the Commission on the basis of ESA Joint Committee draft). The RTS mandate covers 7 areas: Art. 9(2) ICT security policies (sub-point a); Art. 9(4)(c) access-control rights (sub-point b); Art. 10(1)+(2) detection mechanisms (sub-point c); Art. 11(1) ICT business continuity policy (sub-point d); Art. 11(6) BCP testing (sub-point e); Art. 11(3) ICT response and recovery plans (sub-point f); Art. 6(5) ICT risk management framework review report (sub-point g). Every flagged instance in this file tagged `RTS-pending: Art. 15` is materially constrained by the eventual RTS content.
**Compaction note (D1 / D5 / D3):** the compaction consolidates atomic clauses where two or more sub-clauses address the same operational concern (e.g. Art. 11(1)+(2) chapeau+objectives → CL11-1; Art. 11(7)+(8)+(9) crisis+records+CSD → CL11-3). Variant readings are consolidated to 2 (instead of 3) where 2 of 3 readings yield materially similar compliance obligations — `[no third reading identified]` is flagged explicitly. The full Art. 9(4) hinge is preserved at full density (15 instances within one card) because the 6 sub-points (a)–(f) are the operational core of DORA's protection regime. **D3 invariant: no Layer 2 normative force introduced** — the catalogue remains Layer 1 (ambiguity description); the resolution/adjudication is deferred to Layer 2 (cross-regulation synthesis) and to the entity (P7).
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL7-1 | Art. 7 chapeau + (a)–(d) | ICT systems baseline | **S3** | 4 baseline requirements (appropriateness, reliability, capacity, technological resilience). |
| CL8-1 | Art. 8(1)+(2) | Identification chapeau | **S3** | Identify/classify ICT-supported business functions, assets; continuous risk-source identification. |
| CL8-2 | Art. 8(3)+(7) | Major-change + legacy ICT | **S3** | Risk assessment upon each major change; legacy ICT risk assessment (non-micro). |
| CL8-3 | Art. 8(4)+(5)+(6) | Critical-asset mapping + inventory + TPP deps | **S3** | Map critical assets + links/interdeps; inventory; ICT-TPP dependency mapping. |
| CL9-1 | Art. 9(1) | Continuous monitoring | **S3** | Continuously monitor/control ICT systems security + functioning. |
| CL9-2 | Art. 9(2) | ICT security policies/procedures/protocols/tools | **S3** | Design/procure/implement for resilience + AAA of data. |
| CL9-3 | Art. 9(3)(a)–(d) | ICT solutions and processes (data security) | **S3** | Four sub-requirements for data confidentiality and integrity. |
| CL9-4 | Art. 9(4)(a)–(f) | **THE HINGE** | **S3** | Six sub-points: (a) info-security policy; (b) network/infrastructure mgmt; (c) physical+logical access control; (d) strong auth + crypto keys + encryption; (e) ICT change management (6-way AND); (f) patches and updates (3-way AND). |
| CL10-1 | Art. 10(1) | Detection mechanisms | **S3** | Mechanisms to promptly detect anomalous activities and SPOFs. |
| CL10-2 | Art. 10(2)+(3) | Multi-layer controls + sufficient monitoring resources | **S3** | Multi-layer controls, alert thresholds, sufficient resources for monitoring. |
| CL10-3 | Art. 10(4) | DRSP additional requirement | **S2** | Effective check of trade reports; identify omissions + errors; request re-transmission. |
| CL11-1 | Art. 11(1)+(2) chapeau + (a)–(e) | ICT business continuity policy + 5 objectives | **S3** | Comprehensive ICT BCP; 5 enumerated aims (continuity, response, containment, impact estimation, communication). |
| CL11-2 | Art. 11(3)+(4)+(5) | Recovery plans + BCP for outsourced CIFs + BIA | **S3** | Recovery plans (non-micro internal-audit); BCP for outsourced/contracted critical functions; BIA. |
| CL11-3 | Art. 11(6)+(7)+(8)+(9) | BCP testing + crisis management + records + CSD reporting | **S3** | Yearly BCP testing; crisis-comm plans testing; crisis mgmt function (non-micro); records; CSD reporting to CAs. |
| CL11-4 | Art. 11(10)+(11) | Cost reporting + ESA guidelines | **S3** | Annual cost/loss estimation reporting to CAs (non-micro); ESA guidelines by 17 July 2024. |
| CL12-1 | Art. 12(1)+(2) | Backup policies chapeau | **S3** | Documented backup policies + restoration/recovery procedures. |
| CL12-2 | Art. 12(3)+(4) | Restoration + redundant ICT capacities | **S3** | Physically/logically segregated restoration systems; redundant ICT capacities (non-micro). |
| CL12-3 | Art. 12(5) | CSD secondary processing site | **S3** | At least one secondary processing site with distinct risk profile. |
| CL12-4 | Art. 12(6)+(7) | RTO/RPO + data integrity checks | **S3** | Recovery time and point objectives; integrity checks including multiple checks/reconciliations. |
| CL13-1 | Art. 13(1)+(2)+(3) | Threat-intel + post-incident reviews + lessons propagation | **S3** | Threat-intel capability; post-incident reviews; lessons-learned into ICT risk-assessment. |
| CL13-2 | Art. 13(4)+(5)+(6)+(7) | Effectiveness monitoring + training + tech developments | **S3** | Cyber maturity mapping; senior-ICT yearly reporting; awareness programmes + training (non-micro). |
| CL14-1 | Art. 14(1) | Crisis communication plans | **S3** | Crisis comms plans; responsible disclosure of major ICT-related incidents/vulnerabilities. |
| CL14-2 | Art. 14(2)+(3) | Internal + external communication policies + designated person | **S2** | Differentiate internal staff; designated person for public/media. |
| CL15-1 | Art. 15 chapeau + (a)–(g) | ESAs RTS mandate | **S3** | ESAs through JC, in consultation with ENISA, develop draft RTS specifying further: ICT security policies (a), access-control rights (b), detection mechanisms (c), BCP (d), BCP testing (e), response/recovery (f), review report format (g). Deadline 17 January 2024. |
| CL16-1 | Art. 16(1) first sub-paragraph + (2) | Simplified framework scope + documentation/review | **S3** | Exemption scope (5 entity categories); documented + reviewed periodically and upon major ICT-related incidents; report to CA upon request. |
| CL16-2 | Art. 16(1) second sub-paragraph (a)–(h) + (3) | Simplified obligations (parallel to Art. 9(4)) + ESA RTS | **S3** | 8 obligations parallel to Art. 9(4) but at simplified granularity; ESA RTS mandate. |
**Total: 26 atomic clauses (Art. 7: 1; Art. 8: 3; Art. 9: 4; Art. 10: 3; Art. 11: 4; Art. 12: 4; Art. 13: 2; Art. 14: 2; Art. 15: 1; Art. 16: 2). Compaction: 34 → 26 (−8, −24%).**
---
### 3. Verbatim OJ text — Art. 7–16
#### 3.1 Article 7 — ICT systems, protocols and tools
> **Article 7**
>
> **ICT systems, protocols and tools**
>
> In order to address and manage ICT risk, financial entities shall use and maintain updated ICT systems, protocols and tools that are:
>
> (a) <mark>appropriate to the magnitude of operations supporting the conduct of their activities</mark>, in accordance with the proportionality principle as referred to in Article 4;
>
> (b) reliable;
>
> (c) <mark>equipped with sufficient capacity to accurately process the data necessary for the performance of activities and the timely provision of services, and to deal with peak orders, message or transaction volumes, as needed, including where new technology is introduced</mark>;
>
> (d) <mark>technologically resilient in order to adequately deal with additional information processing needs as required under stressed market conditions or other adverse situations</mark>.
#### 3.2 Article 8 — Identification
> **Article 8**
>
> **Identification**
>
> 1. As part of the ICT risk management framework referred to in Article 6(1), financial entities shall <mark>identify, classify and adequately document</mark> all ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk. Financial entities shall <mark>review as needed, and at least yearly</mark>, the adequacy of this classification and of any relevant documentation.
>
> 2. Financial entities shall, on a continuous basis, identify all sources of ICT risk, in particular the risk exposure to and from other financial entities, and assess <mark>cyber threats and ICT vulnerabilities</mark> relevant to their ICT supported business functions, information assets and ICT assets. Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them.
>
> 3. Financial entities, other than microenterprises, shall perform a risk assessment upon <mark>each major change</mark> in the network and information system infrastructure, in the processes or procedures affecting their ICT supported business functions, information assets or ICT assets.
>
> 4. Financial entities shall identify all information assets and ICT assets, including those on remote sites, network resources and hardware equipment, and shall <mark>map those considered critical</mark>. They shall map the configuration of the information assets and ICT assets and the links and interdependencies between the different information assets and ICT assets.
>
> 5. Financial entities shall identify and document all processes that are dependent on ICT third-party service providers, and shall identify interconnections with ICT third-party service providers that provide services that support critical or important functions.
>
> 6. For the purposes of paragraphs 1, 4 and 5, financial entities shall maintain relevant inventories and update them <mark>periodically and every time any major change as referred to in paragraph 3 occurs</mark>.
>
> 7. Financial entities, other than microenterprises, shall on a regular basis, and at least yearly, conduct a specific ICT risk assessment on <mark>all legacy ICT systems</mark> and, in any case before and after connecting technologies, applications or systems.
#### 3.3 Article 9 — Protection and prevention
> **Article 9**
>
> **Protection and prevention**
>
> 1. For the purposes of adequately protecting ICT systems and with a view to organising response measures, financial entities shall <mark>continuously monitor and control</mark> the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures.
>
> 2. Financial entities shall <mark>design, procure and implement</mark> ICT security policies, procedures, protocols and tools that aim to ensure the resilience, continuity and availability of ICT systems, in particular for those supporting critical or important functions, and to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.
>
> 3. In order to achieve the objectives referred to in paragraph 2, financial entities shall use ICT solutions and processes that are <mark>appropriate in accordance with Article 4</mark>. Those ICT solutions and processes shall:
>
> (a) ensure the security of the means of transfer of data;
>
> (b) minimise the risk of corruption or loss of data, unauthorised access and technical flaws that may hinder business activity;
>
> (c) prevent the lack of availability, the impairment of the authenticity and integrity, the breaches of confidentiality and the loss of data;
>
> (d) ensure that data is protected from risks arising from data management, including poor administration, processing-related risks and human error.
>
> 4. As part of the ICT risk management framework referred to in Article 6(1), financial entities shall:
>
> (a) develop and document an <mark>information security policy</mark> defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable;
>
> (b) following a risk-based approach, establish a <mark>sound network and infrastructure management structure</mark> using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks;
>
> (c) implement policies that limit the <mark>physical or logical access</mark> to information assets and ICT assets to <mark>what is required for legitimate and approved functions</mark> and activities only, and establish to that end a set of policies, procedures and controls that address access rights and ensure a sound administration thereof;
>
> (d) implement policies and protocols for <mark>strong authentication mechanisms</mark>, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes;
>
> (e) implement <mark>documented policies, procedures and controls for ICT change management</mark>, including changes to software, hardware, firmware components, systems or security parameters, that are based on a risk assessment approach and are an integral part of the financial entity's overall change management process, in order to ensure that <mark>all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified</mark> in a controlled manner;
>
> (f) have <mark>appropriate and comprehensive documented policies for patches and updates</mark>.
>
> For the purposes of the first subparagraph, point (b), financial entities shall design the network connection infrastructure in a way that allows it to be <mark>instantaneously severed or segmented</mark> in order to minimise and prevent contagion, especially for interconnected financial processes.
>
> For the purposes of the first subparagraph, point (e), the ICT change management process shall be approved by appropriate lines of management and shall have <mark>specific protocols in place</mark>.
#### 3.4 Article 10 — Detection
> **Article 10**
>
> **Detection**
>
> 1. Financial entities shall have in place mechanisms to <mark>promptly detect anomalous activities</mark>, in accordance with Article 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure.
>
> All detection mechanisms referred to in the first subparagraph shall be regularly tested in accordance with Article 25.
>
> 2. The detection mechanisms referred to in paragraph 1 shall enable <mark>multiple layers of control</mark>, define <mark>alert thresholds and criteria</mark> to trigger and initiate ICT-related incident response processes, including automatic alert mechanisms for relevant staff in charge of ICT-related incident response.
>
> 3. Financial entities shall devote <mark>sufficient resources and capabilities</mark> to monitor user activity, the occurrence of ICT anomalies and ICT-related incidents, in particular cyber-attacks.
>
> 4. Data reporting service providers shall, in addition, have in place systems that can effectively check trade reports for completeness, identify omissions and obvious errors, and request re-transmission of those reports.
#### 3.5 Article 11 — Response and recovery
> **Article 11**
>
> **Response and recovery**
>
> 1. As part of the ICT risk management framework referred to in Article 6(1) and based on the identification requirements set out in Article 8, financial entities shall put in place a <mark>comprehensive ICT business continuity policy</mark>, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity.
>
> 2. Financial entities shall implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to:
>
> (a) ensure the continuity of the financial entity's critical or important functions;
>
> (b) <mark>quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents</mark> in a way that limits damage and prioritises the resumption of activities and recovery actions;
>
> (c) <mark>activate, without delay</mark>, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident and prevent further damage, as well as tailored response and recovery procedures established in accordance with Article 12;
>
> (d) estimate preliminary impacts, damages and losses;
>
> (e) <mark>set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders</mark> in accordance with Article 14, and report to the competent authorities in accordance with Article 19.
>
> 3. As part of the ICT risk management framework referred to in Article 6(1), financial entities shall implement associated ICT response and recovery plans which, in the case of financial entities other than microenterprises, shall be subject to independent internal audit reviews.
>
> 4. Financial entities shall put in place, maintain and periodically test appropriate ICT business continuity plans, notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers.
>
> 5. As part of the overall business continuity policy, financial entities shall conduct a <mark>business impact analysis (BIA)</mark> of their exposures to severe business disruptions. Under the BIA, financial entities shall assess the potential impact of severe business disruptions by means of quantitative and qualitative criteria, using internal and external data and scenario analysis, as appropriate. The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies. Financial entities shall ensure that ICT assets and ICT services are <mark>designed and used in full alignment with the BIA</mark>, in particular with regard to adequately ensuring the redundancy of all critical components.
>
> 6. As part of their comprehensive ICT risk management, financial entities shall:
>
> (a) <mark>test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly</mark>, as well as in the event of any substantive changes to ICT systems supporting critical or important functions;
>
> (b) test the crisis communication plans established in accordance with Article 14.
>
> For the purposes of the first subparagraph, point (a), financial entities, other than microenterprises, shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities necessary to meet the obligations set out in Article 12.
>
> Financial entities shall regularly review their ICT business continuity policy and ICT response and recovery plans, taking into account the results of tests carried out in accordance with the first subparagraph and recommendations stemming from audit checks or supervisory reviews.
>
> 7. Financial entities, other than microenterprises, shall have a <mark>crisis management function</mark>, which, in the event of activation of their ICT business continuity plans or ICT response and recovery plans, shall, inter alia, set out clear procedures to manage internal and external crisis communications in accordance with Article 14.
>
> 8. Financial entities shall keep readily accessible records of activities before and during disruption events when their ICT business continuity plans and ICT response and recovery plans are activated.
>
> 9. Central securities depositories shall provide the competent authorities with copies of the results of the ICT business continuity tests, or of similar exercises.
>
> 10. Financial entities, other than microenterprises, shall report to the competent authorities, upon their request, an estimation of aggregated annual costs and losses caused by major ICT-related incidents.
>
> 11. In accordance with Article 16 of Regulations (EU) No 1093/2010, (EU) No 1094/2010 and (EU) No 1095/2010, the ESAs, through the Joint Committee, shall by 17 July 2024 develop common guidelines on the estimation of aggregated annual costs and losses referred to in paragraph 10.
#### 3.6 Article 12 — Backup policies and procedures, restoration and recovery procedures and methods
> **Article 12**
>
> **Backup policies and procedures, restoration and recovery procedures and methods**
>
> 1. For the purpose of ensuring the restoration of ICT systems and data with <mark>minimum downtime, limited disruption and loss</mark>, as part of their ICT risk management framework, financial entities shall develop and document:
>
> (a) backup policies and procedures specifying the <mark>scope of the data that is subject to the backup and the minimum frequency of the backup</mark>, based on the criticality of information or the confidentiality level of the data;
>
> (b) restoration and recovery procedures and methods.
>
> 2. Financial entities shall set up backup systems that can be activated in accordance with the backup policies and procedures, as well as restoration and recovery procedures and methods. The activation of backup systems shall <mark>not jeopardise the security of the network and information systems or the availability, authenticity, integrity or confidentiality of data</mark>. Testing of the backup procedures and restoration and recovery procedures and methods shall be undertaken periodically.
>
> 3. When restoring backup data using own systems, financial entities shall use ICT systems that are <mark>physically and logically segregated from the source ICT system</mark>. The ICT systems shall be securely protected from any unauthorised access or ICT corruption and allow for the timely restoration of services making use of data and system backups as necessary.
>
> For central counterparties, the recovery plans shall enable the recovery of all transactions at the time of disruption to allow the central counterparty to continue to operate with certainty and to complete settlement on the scheduled date.
>
> Data reporting service providers shall additionally maintain adequate resources and have back-up and restoration facilities in place in order to offer and maintain their services at all times.
>
> 4. Financial entities, other than microenterprises, shall maintain redundant ICT capacities equipped with resources, capabilities and functions that are adequate to ensure business needs. Microenterprises shall assess the need to maintain such redundant ICT capacities based on their risk profile.
>
> 5. Central securities depositories shall maintain at least one <mark>secondary processing site</mark> endowed with adequate resources, capabilities, functions and staffing arrangements to ensure business needs.
>
> The secondary processing site shall be:
>
> (a) located at a geographical distance from the primary processing site to ensure that it bears a <mark>distinct risk profile</mark> and to prevent it from being affected by the event which has affected the primary site;
>
> (b) capable of ensuring the continuity of critical or important functions identically to the primary site, or providing the level of services necessary to ensure that the financial entity performs its critical operations within the recovery objectives;
>
> (c) <mark>immediately accessible</mark> to the financial entity's staff to ensure continuity of critical or important functions in the event that the primary processing site has become unavailable.
>
> 6. In determining the <mark>recovery time and recovery point objectives</mark> for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency. Such time objectives shall ensure that, in extreme scenarios, the agreed service levels are met.
>
> 7. When recovering from an ICT-related incident, financial entities shall perform necessary checks, including any <mark>multiple checks and reconciliations</mark>, in order to ensure that the highest level of data integrity is maintained. These checks shall also be performed when reconstructing data from external stakeholders, in order to ensure that all data is consistent between systems.
#### 3.7 Article 13 — Learning and evolving
> **Article 13**
>
> **Learning and evolving**
>
> 1. Financial entities shall have in place <mark>capabilities and staff to gather information on vulnerabilities and cyber threats</mark>, ICT-related incidents, in particular cyber-attacks, and analyse the impact they are likely to have on their digital operational resilience.
>
> 2. Financial entities shall put in place <mark>post ICT-related incident reviews</mark> after a major ICT-related incident disrupts their core activities, analysing the causes of disruption and identifying required improvements to the ICT operations or within the ICT business continuity policy referred to in Article 11.
>
> Financial entities, other than microenterprises, shall, upon request, communicate to the competent authorities, the changes that were implemented following post ICT-related incident reviews as referred to in the first subparagraph.
>
> The post ICT-related incident reviews referred to in the first subparagraph shall determine whether the established procedures were followed and the actions taken were effective, including in relation to the following:
>
> (a) the promptness in responding to security alerts and determining the impact of ICT-related incidents and their severity;
>
> (b) the quality and speed of performing a forensic analysis, where deemed appropriate;
>
> (c) the effectiveness of incident escalation within the financial entity;
>
> (d) the effectiveness of internal and external communication.
>
> 3. Lessons derived from the digital operational resilience testing carried out in accordance with Articles 26 and 27 and from real life ICT-related incidents, in particular cyber-attacks, along with challenges faced upon the activation of ICT business continuity plans and ICT response and recovery plans, together with relevant information exchanged with counterparts and assessed during supervisory reviews, shall be <mark>duly incorporated on a continuous basis into the ICT risk assessment process</mark>. Those findings shall form the basis for appropriate reviews of relevant components of the ICT risk management framework referred to in Article 6(1).
>
> 4. Financial entities shall monitor the effectiveness of the implementation of their digital operational resilience strategy set out in Article 6(8). They shall map the evolution of ICT risk over time, analyse the frequency, types, magnitude and evolution of ICT-related incidents, in particular cyber-attacks and their patterns, with a view to understanding the level of ICT risk exposure, in particular in relation to critical or important functions, and <mark>enhance the cyber maturity and preparedness</mark> of the financial entity.
>
> 5. Senior ICT staff shall report at least yearly to the management body on the findings referred to in paragraph 3 and put forward recommendations.
>
> 6. Financial entities shall develop ICT security awareness programmes and digital operational resilience training as <mark>compulsory modules in their staff training schemes</mark>. Those programmes and training shall be applicable to all employees and to senior management staff, and shall have a level of complexity <mark>commensurate to the remit of their functions</mark>. Where appropriate, financial entities shall also include ICT third-party service providers in their relevant training schemes in accordance with Article 30(2), point (i).
>
> 7. Financial entities, other than microenterprises, shall monitor <mark>relevant technological developments</mark> on a continuous basis, also with a view to understanding the possible impact of the deployment of such new technologies on ICT security requirements and digital operational resilience. They shall keep up-to-date with the latest ICT risk management processes, in order to effectively combat current or new forms of cyber-attacks.
#### 3.8 Article 14 — Communication
> **Article 14**
>
> **Communication**
>
> 1. As part of the ICT risk management framework referred to in Article 6(1), financial entities shall have in place <mark>crisis communication plans</mark> enabling a responsible disclosure of, at least, <mark>major ICT-related incidents or vulnerabilities</mark> to clients and counterparts as well as to the public, as appropriate.
>
> 2. As part of the ICT risk management framework, financial entities shall implement communication policies for internal staff and for external stakeholders. Communication policies for staff shall take into account the need to <mark>differentiate between staff involved in ICT risk management</mark>, in particular the staff responsible for response and recovery, and staff that needs to be informed.
>
> 3. At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents and fulfil the <mark>public and media function</mark> for that purpose.
#### 3.9 Article 15 — Further harmonisation of ICT risk management tools, methods, processes and policies
> **Article 15**
>
> **Further harmonisation of ICT risk management tools, methods, processes and policies**
>
> The ESAs shall, through the Joint Committee, in consultation with the European Union Agency on Cybersecurity (ENISA), develop common draft regulatory technical standards in order to:
>
> (a) <mark>specify further elements to be included in the ICT security policies, procedures, protocols and tools</mark> referred to in Article 9(2), with a view to ensuring the security of networks, enable adequate safeguards against intrusions and data misuse, preserve the availability, authenticity, integrity and confidentiality of data, including cryptographic techniques, and guarantee an accurate and prompt data transmission without major disruptions and undue delays;
>
> (b) develop further components of the controls of <mark>access management rights referred to in Article 9(4), point (c)</mark>, and associated human resource policy specifying access rights, procedures for granting and revoking rights, monitoring anomalous behaviour in relation to ICT risk through appropriate indicators, including for network use patterns, hours, IT activity and unknown devices;
>
> (c) develop further the mechanisms specified in <mark>Article 10(1)</mark> enabling a prompt detection of anomalous activities and the criteria set out in Article 10(2) triggering ICT-related incident detection and response processes;
>
> (d) specify further the components of the <mark>ICT business continuity policy referred to in Article 11(1)</mark>;
>
> (e) specify further the testing of ICT business continuity plans referred to in <mark>Article 11(6)</mark> to ensure that such testing duly takes into account scenarios in which the quality of the provision of a critical or important function deteriorates to an unacceptable level or fails, and duly considers the potential impact of the insolvency, or other failures, of any relevant ICT third-party service provider and, where relevant, the political risks in the respective providers' jurisdictions;
>
> (f) specify further the components of the <mark>ICT response and recovery plans referred to in Article 11(3)</mark>;
>
> (g) specifying further the content and format of the <mark>report on the review of the ICT risk management framework</mark> referred to in Article 6(5).
>
> When developing those draft regulatory technical standards, the ESAs shall take into account the size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations, while duly taking into consideration any specific feature arising from the distinct nature of activities across different financial services sectors.
>
> The ESAs shall submit those draft regulatory technical standards to the Commission by <mark>17 January 2024</mark>.
>
> Power is delegated to the Commission to supplement this Regulation by adopting the regulatory technical standards referred to in the first paragraph in accordance with Articles 10 to 14 of Regulations (EU) No 1093/2010, (EU) No 1094/2010 and (EU) No 1095/2010.
#### 3.10 Article 16 — Simplified ICT risk management framework
> **Article 16**
>
> **Simplified ICT risk management framework**
>
> 1. Articles 5 to 15 of this Regulation shall not apply to <mark>small and non-interconnected investment firms, payment institutions exempted pursuant to Directive (EU) 2015/2366</mark>; institutions exempted pursuant to Directive 2013/36/EU in respect of which Member States have decided not to apply the option referred to in Article 2(4) of this Regulation; electronic money institutions exempted pursuant to Directive 2009/110/EC; and small institutions for occupational retirement provision.
>
> Without prejudice to the first subparagraph, the entities listed in the first subparagraph shall:
>
> (a) put in place and maintain a <mark>sound and documented ICT risk management framework</mark> that details the mechanisms and measures aimed at a quick, efficient and comprehensive management of ICT risk, including for the protection of relevant physical components and infrastructures;
>
> (b) <mark>continuously monitor the security and functioning of all ICT systems</mark>;
>
> (c) <mark>minimise the impact of ICT risk</mark> through the use of sound, resilient and updated ICT systems, protocols and tools which are appropriate to support the performance of their activities and the provision of services and adequately protect availability, authenticity, integrity and confidentiality of data in the network and information systems;
>
> (d) allow <mark>sources of ICT risk and anomalies in the network and information systems to be promptly identified and detected and ICT-related incidents to be swiftly handled</mark>;
>
> (e) identify <mark>key dependencies on ICT third-party service providers</mark>;
>
> (f) ensure the continuity of critical or important functions, through <mark>business continuity plans and response and recovery measures, which include, at least, back-up and restoration measures</mark>;
>
> (g) <mark>test, on a regular basis, the plans and measures referred to in point (f), as well as the effectiveness of the controls</mark> implemented in accordance with points (a) and (c);
>
> (h) implement, as appropriate, relevant operational conclusions resulting from the tests referred to in point (g) and from post-incident analysis into the ICT risk assessment process and develop, according to needs and ICT risk profile, ICT security awareness programmes and digital operational resilience training for staff and management.
>
> 2. The ICT risk management framework referred to in paragraph 1, second subparagraph, point (a), shall be <mark>documented and reviewed periodically and upon the occurrence of major ICT-related incidents</mark> in compliance with supervisory instructions. It shall be continuously improved on the basis of lessons derived from implementation and monitoring. A report on the review of the ICT risk management framework shall be submitted to the competent authority upon its request.
>
> 3. The ESAs shall, through the Joint Committee, in consultation with the ENISA, develop common draft regulatory technical standards in order to:
>
> (a) specify further the elements to be included in the ICT risk management framework referred to in paragraph 1, second subparagraph, point (a);
>
> (b) specify further the elements in relation to systems, protocols and tools to minimise the impact of ICT risk referred to in paragraph 1, second subparagraph, point (c), with a view to ensuring the security of networks, enabling adequate safeguards against intrusions and data misuse and preserving the availability, authenticity, integrity and confidentiality of data;
>
> (c) specify further the components of the ICT business continuity plans referred to in paragraph 1, second subparagraph, point (f);
>
> (d) specify further the rules on the testing of business continuity plans and ensure the effectiveness of the controls referred to in paragraph 1, second subparagraph, point (g) and ensure that such testing duly takes into account scenarios in which the quality of the provision of a critical or important function deteriorates to an unacceptable level or fails;
>
> (e) specify further the content and format of the report on the review of the ICT risk management framework referred to in paragraph 2.
>
> When developing those draft regulatory technical standards, the ESAs shall take into account the size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations.
>
> The ESAs shall submit those draft regulatory technical standards to the Commission by <mark>17 January 2024</mark>.
---
### 4. Detailed cards
#### 4.1 CL7-1 — Art. 7 chapeau + (a)–(d) — ICT systems baseline
`[scope: all financial entities — chapeau; Art. 4 proportionality applies per sub-point (a)]`
**Source locus:** Art. 7 chapeau and sub-points (a)–(d).
> In order to address and manage ICT risk, financial entities shall use and maintain updated ICT systems, protocols and tools that are:
>
> (a) **appropriate to the magnitude of operations supporting the conduct of their activities**, in accordance with the proportionality principle as referred to in Article 4;
>
> (b) reliable;
>
> (c) **equipped with sufficient capacity to accurately process the data necessary for the performance of activities and the timely provision of services, and to deal with peak orders, message or transaction volumes, as needed, including where new technology is introduced**;
>
> (d) **technologically resilient in order to adequately deal with additional information processing needs as required under stressed market conditions or other adverse situations**.
**Instance 1 — VAG — S3 — `appropriate to the magnitude of operations` (sub-point a)**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Size-driven | In-Directive: literal `magnitude of operations` |
| R2 | Risk-driven | In-Directive: Art. 4(2) reference |
R2 is the literal reading (Art. 4 is referenced explicitly). R1 vs R2 admit materially distinct compliance populations: a small entity with high-risk profile must comply differently under R1 vs R2. S3.
*Berry anchor:* §5.1 (`appropriate`); §5.4.6 (proportionality operator).
**Instance 2 — VAG — S3 — `reliable` (sub-point b)**
Single-word qualifier.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | SLA-defined (entity targets) | None in OJ |
| R2 | RTS-defined | In-Directive: Art. 15(a) |
R2 is the structural-rationale reading (RTS will specify). S3 (unresolved until RTS adoption).
*Berry anchor:* §5.1 (`reliable`); §3.3.1.
**Instance 3 — VAG — S3 — `sufficient capacity` (sub-point c)**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Qualitative (entity-calibrated resilience) | In-Directive: literal `sufficient` |
| R2 | Stress-tested (entity conducts stress testing) | In-Directive: literal `peak … as needed` |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations. `[no third reading identified]` — the original R3 (quantitative threshold) is operationally subsumed by R1 (qualitative adequacy + stress-test). S3.
*Berry anchor:* §5.1 (`sufficient`, `timely`, `as needed`); §5.4.6 (catch-all scope).
**Instance 4 — VAG — S3 — `technologically resilient` (sub-point d)**
`technologically resilient` is undefined. Three readings collapsed to 2: R1 (stack-specific) subsumed into R2 (architecture) — both are technical-design choices; R3 (outcome) is materially distinct.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technology-stack / architecture-specific (entity chooses stack) | None in OJ |
| R2 | Outcome-specific (measured recovery + continuity metrics) | In-Directive: literal `stressed market conditions` |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §3.3.1 (`technologically resilient`); §5.4.6 (`stressed market conditions`, `other adverse situations`).
---
#### 4.2 CL8-1 — Art. 8(1)+(2) — Identification chapeau + continuous risk-source identification
`[scope: identification; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 8(1) and 8(2).
> As part of the ICT risk management framework referred to in Article 6(1), financial entities shall **identify, classify and adequately document** all ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk. Financial entities shall **review as needed, and at least yearly**, the adequacy of this classification and of any relevant documentation.
>
> Financial entities shall, on a continuous basis, identify all sources of ICT risk, in particular the risk exposure to and from other financial entities, and assess **cyber threats and ICT vulnerabilities** relevant to their ICT supported business functions, information assets and ICT assets. Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them.
**Instance 1 — COORD — S3 — `identify, classify and adequately document`**
Three coordinated verbs (Berry §5.5 — three-way coordination).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete lifecycle phases (each verb = separate obligation) | In-Directive: literal `identify, classify and adequately document` |
| R2 | Composite process (one workflow, three aspects) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R2 admits a single integrated exercise; R1 requires three discrete artefacts). `[no third reading identified]` — R3 (discrete phases that must be repeated) is operationally subsumed by R1 + the `at least yearly` review trigger (Instance 2). S3.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 2 — VAG — S3 — `review as needed, and at least yearly`**
Catch-all + hard numeric anchor. The compound `as needed AND at least yearly`:
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Yearly review only (hard anchor) | In-Directive: literal `at least yearly` |
| R2 | Both (cumulative — whenever needed, in addition to yearly) | In-Directive: literal `as needed, AND at least yearly` |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance obligations (R1 review schedule is fixed; R2 admits additional reviews when triggers emerge). S3.
*Berry anchor:* §5.7 (`at least yearly`); §5.1 (`as needed`).
**Instance 3 — POLY — S3 — `the risk exposure to and from other financial entities`**
Bidirectional exposure scope (counterparty concentration risk + sectoral contagion).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exposure TO only (this entity is exposed to others) | In-Directive: literal `exposure to … other financial entities` |
| R2 | Both directions (TO and FROM) | In-Directive: literal `to and from` |
R2 is the literal reading. `[no third reading identified]` — the R3 (from only) was a misreading of the literal `from`; the `to and from` formulation is unambiguous on R2. R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.4.7 (`to and from`); §3.3.1 (`other financial entities`).
---
#### 4.3 CL8-2 — Art. 8(3)+(7) — Major-change risk assessment + legacy ICT (non-microenterprises)
`[scope: non-microenterprises; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 8(3) and 8(7).
> Financial entities, other than microenterprises, shall perform a risk assessment upon **each major change** in the network and information system infrastructure, in the processes or procedures affecting their ICT supported business functions, information assets or ICT assets.
>
> Financial entities, other than microenterprises, shall on a regular basis, and at least yearly, conduct a specific ICT risk assessment on **all legacy ICT systems** and, in any case before and after connecting technologies, applications or systems.
**Instance 1 — VAG — S3 — `each major change`**
The threshold for triggering re-assessment is undefined.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Structural change only (new system, new infra component) | None in OJ |
| R2 | Materiality-based (any change material to risk profile) | In-Directive: literal `major change` (materiality) |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations (a purely configurable change would not trigger under R1 but might trigger under R2). S3.
*Berry anchor:* §5.1 (`major`); §3.3.1 (`major change`).
**Instance 2 — POLY — S3 — `network and information system infrastructure, … processes or procedures affecting their ICT supported business functions, information assets or ICT assets`**
Four scope categories (OR). Three readings collapsed to 2: R1 (infra only) and R2 (processes only) are operationally similar (both are change-triggers); consolidated to **R1 = any one of the four categories**; **R2 = any combination of the four** (the `or` is inclusive).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any one category | None in OJ |
| R2 | Any combination of the four | In-Directive: literal `infrastructure, … processes or procedures … ICT assets` (OR-inclusive) |
R2 is the literal reading. S3 (combinations are open-ended). `[no third reading identified]` — the original R3 (information assets only) is subsumed by R2.
*Berry anchor:* §5.4.7 (4-way OR-inclusive).
**Instance 3 — VAG — S3 — `legacy ICT systems` (Art. 8(7))**
`legacy ICT systems` — DORA-D03 definition: `an ICT system that has reached the end of its life cycle, that is no longer supported or maintained by its vendor or provider, or that, for any other reasons, cannot be patched or updated by its vendor or provider, but which is still in use and supports the financial entity's functions`. The definition supplies its own disambiguation (end-of-life OR unsupported OR unable-to-patch — three-way OR).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict: only end-of-life systems (Berry-flagged `end-of-life` undefined) | In-Directive: DORA Art. 3(43) `legacy ICT system` |
| R2 | Broad: any system under any of the three conditions (EoL OR unsupported OR unable-to-patch) | In-Directive: DORA Art. 3(43) three-way OR |
R2 is the literal reading per Art. 3(43). Same Berry pattern as DORA-D03. S3. `[no third reading identified]` — R3 (substance: any system the entity cannot keep current) is operationally indistinguishable from R2 for compliance purposes.
*Berry anchor:* §3.3.1 (`legacy ICT systems`); DORA-D03.
**Definitional anchor:** DORA-D60 `microenterprise` (S2 — `fewer than 10 persons`, per pilot §2.12); DORA Art. 3(43) `legacy ICT system`.
**Proportionality-status:** Art. 4 applies; clause is itself a **carve-out FOR non-microenterprises** (Art. 8(3) and 8(7) do not bind microenterprises at all).
---
#### 4.4 CL8-3 — Art. 8(4)+(5)+(6) — Critical-asset mapping + inventory + TPP dependencies
`[scope: identification artefacts; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 8(4), 8(5), and 8(6).
> Financial entities shall identify all information assets and ICT assets, including those on remote sites, network resources and hardware equipment, and shall **map those considered critical**. They shall map the configuration of the information assets and ICT assets and the **links and interdependencies** between the different information assets and ICT assets.
>
> Financial entities shall identify and document all processes that are dependent on ICT third-party service providers, and shall identify interconnections with ICT third-party service providers that provide services that support critical or important functions.
>
> For the purposes of paragraphs 1, 4 and 5, financial entities shall maintain relevant inventories and update them **periodically and every time any major change as referred to in paragraph 3 occurs**.
**Instance 1 — VAG — S3 — `map those considered critical`**
The criticality threshold. `considered critical` is undefined (Berry classic — propagates from DORA-D22 tautology).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity-determined criticality | In-Directive: literal `considered` (entity judgment) |
| R2 | Regulator-determined (NCA guidance) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations. **Same S3 regress as DORA-D22 (tautological definition).** `[no third reading identified]` — R3 (standard-determined) is operationally subsumed by R1 (entity may invoke standards as evidence for its judgment). S3.
*Berry anchor:* §3.3.1 (`critical`).
**Instance 2 — POLY — S3 — `links and interdependencies`**
Two relationship types (AND). Two readings collapsed to 2: R1 (linear) vs R2 (both required). The R3 (network only / interdependencies only) is operationally incomplete.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Linear relationships only (links) | In-Directive: literal `links` |
| R2 | Both required (links map topology; interdependencies map causal chains) | In-Directive: literal `links and interdependencies` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`interdependencies`).
**Instance 3 — POLY — S3 — `interconnections with ICT third-party service providers that provide services that support critical or important functions` (Art. 8(5))**
The scope of `interconnections` and the substantive threshold `critical or important functions`.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All interconnections (any contact point) | In-Directive: literal `interconnections` (broad) |
| R2 | Interconnections to providers of CIF only (substantive scope) | In-Directive: literal `that support critical or important functions` |
R2 is the literal reading for the substantive scope. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — R3 (material interconnections) is operationally a sub-set of R2 (CIF-supporting) for compliance purposes.
*Berry anchor:* §3.3.1 (`interconnection`, `critical or important functions`).
**Instance 4 — VAG — S3 — `periodically and every time any major change as referred to in paragraph 3 occurs` (Art. 8(6))**
Compound temporal trigger: `periodically` + `every time any major change`. Inherits `major change` from CL8-2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Periodically only (no event-driven obligation) | None in OJ |
| R2 | Both (periodic + event-driven) | In-Directive: literal `periodically AND every time … major change` |
R2 is the literal reading. S3. `[no third reading identified]` — R3 (event-driven only) operationally defeats the `periodically` mandate.
*Berry anchor:* §5.4.7 (AND); §5.1 (`periodically`); §3.3.1 (`major change`).
**Definitional anchor:** DORA-D22 `critical or important function` (S3 tautology); DORA-D14 `cyber-attack` (inherited via `ICT assets`); DORA Art. 3(19) `ICT third-party service provider`.
**Proportionality-status:** Art. 4 applies (no carve-out).
---
#### 4.5 CL9-1 — Art. 9(1) — Continuous monitoring and control
**Source locus:** Art. 9(1).
> For the purposes of adequately protecting ICT systems and with a view to organising response measures, financial entities shall **continuously monitor and control** the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures.
**Instance 1 — COORD — S3 — `continuously monitor and control`**
Two verbs coordinated; the `continuously` adverb applies to both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Monitoring is continuous; control is event-driven | None in OJ |
| R2 | Both monitoring and control are continuous (the `continuously` distributes to both) | In-Directive: literal `continuously monitor AND control` |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — R3 (broad Art. 4 proportionality) is captured at the clause level via the `proportionality-status` field, not as an independent reading.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`continuously`).
**Instance 2 — VAG — S3 — `appropriate ICT security tools, policies and procedures`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Tools + policies only (technical + governance, no operational procedures) | In-Directive: literal `tools, policies` |
| R2 | All three (tools + policies + procedures) | In-Directive: literal `tools, policies AND procedures` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (3-way AND); §5.1 (`appropriate`).
---
#### 4.6 CL9-2 — Art. 9(2) — Design/procure/implement ICT security policies, procedures, protocols and tools
**Source locus:** Art. 9(2).
> Financial entities shall **design, procure and implement** ICT security policies, procedures, protocols and tools that aim to ensure the resilience, continuity and availability of ICT systems, in particular for those supporting critical or important functions, and to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.
**Instance 1 — COORD — S3 — `design, procure and implement`**
Three coordinated verbs (Berry §5.5 — three-way coordination).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete lifecycle phases (design → procure → implement) | In-Directive: literal `design, procure and implement` |
| R2 | Three independent obligations (any of which may be delegated to third parties) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R2 admits procurement delegation; R1 requires entity-side design control). S3. `[no third reading identified]` — the original R3 (composite process) is operationally indistinguishable from R1 for compliance purposes (each verb still requires an action).
*Berry anchor:* §5.5 (three-way coordination).
**Instance 2 — POLY — S3 — `availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All four dimensions (cumulative) | In-Directive: literal `availability, authenticity, integrity and confidentiality` (NIS 2 Art. 6(2) D02 analogue) |
| R2 | All four in all three states (cumulative × cumulative) | In-Directive: literal combined |
R2 is the literal reading; R1 admits subsets within dimensions. S3.
*Berry anchor:* §5.4.7 (4-way OR + 3-way OR); §3.3.1 (`at rest`, `in use`, `in transit`).
**Instance 3 — POLY — S3 — `policies, procedures, protocols and tools` (the 4-category scope)**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Documents only (policies + procedures) | None in OJ |
| R2 | All four required (cumulative) | In-Directive: literal `policies, procedures, protocols and tools` |
R2 is the literal reading. S3. `[no third reading identified]` — the original R3 (all four required) is identical to R2.
*Berry anchor:* §5.4.7 (4-way coordination).
---
#### 4.7 CL9-3 — Art. 9(3)(a)–(d) — ICT solutions and processes (data security baseline)
`[scope: ICT solutions and processes; multi-instance within one card per Q6=a convention; do not split into 4 sub-clauses]`
**Source locus:** Art. 9(3) chapeau and sub-points (a)–(d).
> In order to achieve the objectives referred to in paragraph 2, financial entities shall use ICT solutions and processes that are **appropriate in accordance with Article 4**. Those ICT solutions and processes shall:
>
> (a) ensure the security of the means of transfer of data;
>
> (b) minimise the risk of corruption or loss of data, unauthorised access and technical flaws that may hinder business activity;
>
> (c) prevent the lack of availability, the impairment of the authenticity and integrity, the breaches of confidentiality and the loss of data;
>
> (d) ensure that data is protected from risks arising from data management, including poor administration, processing-related risks and human error.
**Instance 1 — VAG — S3 — chapeau: `appropriate in accordance with Article 4`**
`appropriate` + Art. 4 reference. Same Berry-flagged combination as CL9-2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Size-driven proportionality | In-Directive: literal `appropriate` |
| R2 | Risk-driven proportionality (per Art. 4(2) criteria) | In-Directive: Art. 4(2) criteria |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — R3 (sectoral calibration) is captured via Art. 15 RTS, not as an independent reading.
*Berry anchor:* §5.1 (`appropriate`).
**Instance 2 — POLY — S3 — sub-points (a)+(b)+(c)+(d): four data-security objectives**
The four sub-points (a)–(d) constitute a cumulative 4-way AND. Three readings collapsed to 2: R1 (each independent) and R2 (any combination) are operationally indistinguishable; both collapse to **R2 (all four required, cumulative)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each sub-point is independent (any one suffices) | None in OJ |
| R2 | All four required (cumulative, each is a separate `prevent`/`ensure`/`minimise` clause) | In-Directive: literal four coordinated sub-clauses |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (4-way AND); §5.5 (four sub-clauses enumeration).
**Instance 3 — POLY — S3 — sub-point (a): `security of the means of transfer of data` (scope) + sub-point (b): four failure modes**
Combined analysis. R1 (network) vs R2 (all means of transfer) is materially distinct.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Network transfer only (TCP/IP) | None in OJ |
| R2 | All means of transfer (network + physical) | In-Directive: literal `means of transfer` (broad) |
R2 is the literal reading. Sub-point (b) three failure modes (corruption, loss, access, flaws) — same Berry pattern, all four required. S3. `[no third reading identified]` for sub-point (a) — physical-only and partial-coverage readings are operationally subsumed by R2.
*Berry anchor:* §3.3.1 (`means of transfer`); §5.4.7 (4-way OR for failure modes).
---
#### 4.8 CL9-4 — Art. 9(4)(a)–(f) — THE HINGE
`[scope: ICT risk-management framework core requirements; multi-instance within one card per Q6=a convention; 6 sub-points (a)-(f) NOT split into 6 cards]`
**Source locus:** Art. 9(4) chapeau, sub-points (a)–(f), and two clarifying sub-paragraphs for (b) and (e).
> As part of the ICT risk management framework referred to in Article 6(1), financial entities shall:
>
> (a) develop and document an **information security policy** defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable;
>
> (b) following a risk-based approach, establish a **sound network and infrastructure management structure** using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks;
>
> (c) implement policies that limit the **physical or logical access** to information assets and ICT assets to **what is required for legitimate and approved functions** and activities only, and establish to that end a set of policies, procedures and controls that address access rights and ensure a sound administration thereof;
>
> (d) implement policies and protocols for **strong authentication mechanisms**, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes;
>
> (e) implement **documented policies, procedures and controls for ICT change management**, including changes to software, hardware, firmware components, systems or security parameters, that are based on a risk assessment approach and are an integral part of the financial entity's overall change management process, in order to ensure that **all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified** in a controlled manner;
>
> (f) have **appropriate and comprehensive documented policies for patches and updates**.
>
> For the purposes of the first subparagraph, point (b), financial entities shall design the network connection infrastructure in a way that allows it to be **instantaneously severed or segmented** in order to minimise and prevent contagion, especially for interconnected financial processes.
>
> For the purposes of the first subparagraph, point (e), the ICT change management process shall be approved by appropriate lines of management and shall have **specific protocols in place**.
**Instance 1 — POLY — S3 — sub-point (a): `availability, authenticity, integrity and confidentiality`**
Four data-security dimensions (OR — same as CL9-2).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All four required (cumulative) | In-Directive: literal four-way coordination |
| R2 | Risk-based subset (entity selects per data classification) | None in OJ |
*Berry anchor:* §5.4.7 (4-way coordination).
**Instance 2 — VAG — S3 — sub-point (b) chapeau: `sound network and infrastructure management structure`**
`sound` is undefined. Same Berry pattern as CL8-3 `considered critical` (vague structural qualifier).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Documented structure (process-based) | In-Directive: literal `sound` |
| R2 | Outcome-based (results-based) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — original R3 (standards-based) is captured as R1 with an industry-standard reference.
*Berry anchor:* §3.3.1 (`sound`, `network and infrastructure management structure`).
**Instance 3 — POLY — S3 — sub-point (b): `techniques, methods and protocols` (3-way AND)**
Three categories of network controls. Three readings collapsed to 2: R1 (each independent) and R2 (any one suffices) are operationally similar; consolidated to **R1 = any one suffices** and **R2 = all three required (cumulative)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any one (each is independently selected) | None in OJ |
| R2 | All three required (cumulative) | In-Directive: literal `techniques, methods and protocols` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (3-way AND).
**Instance 4 — VAG — S3 — sub-point (b) clarifying sub-paragraph: `instantaneously severed or segmented`**
`instantaneously` is Berry-flagged. The temporal qualifier for sever/segment:
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Within seconds (sub-minute) | In-Directive: literal `instantaneously` |
| R2 | As fast as possible (general duty) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (an entity that severs within minutes does not meet R1). S3. `[no third reading identified]` — R3 (within minutes) is operationally below R1.
*Berry anchor:* §5.1 (`instantaneously`); §5.4.7 (`severed or segmented`).
**Instance 5 — POLY — S3 — sub-point (c): `physical or logical access`**
Two access-control dimensions (OR). R3 (logical only) is operationally incomplete (no physical control); collapsed.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Physical only | None in OJ |
| R2 | Both (physical AND logical) | In-Directive: literal `physical or logical` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`physical access`, `logical access`).
**Instance 6 — VAG — S3 — sub-point (c): `what is required for legitimate and approved functions and activities`**
**T3 imposed `need-to-know` and `least privilege` per C14; OJ says only `what is required for legitimate and approved functions`.** Two readings retained as materially distinct (R1 is OJ-literal; R2 is T3-imposed). R3 (least privilege) operationally indistinguishable from R2 (need-to-know) for compliance purposes — collapsed.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Functional necessity (only those required to perform a defined function) | In-Directive: literal `what is required for legitimate and approved functions` |
| R2 | Need-to-know (information compartmentation) | None in OJ — T3-imposed (gap from C14 mapping) |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (need-to-know is information-scoped; functional necessity is role-scoped). **T3's `least privilege / need-to-know` mapping is unsubstantiated by the OJ text — flag in §5.** S3.
*Berry anchor:* §3.3.1 (`legitimate and approved functions`); §5.1 (`required for`); §5.4.6.
**Instance 7 — POLY — S3 — sub-point (c): `policies, procedures and controls that address access rights`**
Three governance artefacts (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All three required (cumulative) | In-Directive: literal `policies, procedures and controls` |
| R2 | Any one suffices | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (3-way AND).
**Instance 8 — VAG — S3 — sub-point (d): `strong authentication mechanisms`**
**T3 imposed `Multi-Factor Authentication (MFA)` per C16; OJ says only `strong authentication`.** Two readings retained as materially distinct (R1 is OJ-literal; R2 is T3-imposed). R3 (two-factor) is operationally a sub-set of R2 (MFA) — collapsed.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strong single-factor (e.g. FIDO2/cryptographic token) | None in OJ — literal `strong authentication` admits strong single-factor |
| R2 | MFA (≥2 factors) | None in OJ — T3-imposed (gap from C16 mapping) |
The OJ uses `strong authentication` without mandating MFA. **Recital 64 mentions `strong authentication means`; the substantive thresholds vary by risk-based approach.** R1 (FIDO2 cryptographic single-factor) is widely accepted as strong; R2 (MFA) is one operationalisation but not the only one. S3 (the readings are operationally distinct).
*Berry anchor:* §3.3.1 (`strong authentication`); §5.1 (`strong`).
**Instance 9 — POLY — S3 — sub-point (d): `cryptographic keys … data is encrypted based on results of approved data classification and ICT risk assessment processes`**
Two encryption preconditions (AND). Three readings collapsed to 2: R1 (classification alone) and R2 (risk assessment alone) are both incomplete; collapsed to **R1 = either alone suffices** vs **R2 = both required (cumulative)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either classification OR risk assessment alone suffices | None in OJ |
| R2 | Both required (cumulative) | In-Directive: literal `based on results of approved data classification AND ICT risk assessment processes` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`data classification`, `ICT risk assessment`).
**Instance 10 — COORD — S3 — sub-point (e) chapeau: `documented policies, procedures and controls for ICT change management`**
Three governance artefacts (AND — Berry §5.5). Same pattern as CL9-2 three-way. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete artefacts | In-Directive: literal |
| R2 | Three independent artefacts (any one suffices) | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 11 — POLY — S3 — sub-point (e): scope of `changes to software, hardware, firmware components, systems or security parameters`**
Five change categories (OR — very long enumeration). Three readings collapsed to 2: R1-R5 (single categories) are operationally similar; consolidated to **R1 = any one of the five** and **R2 = any combination of the five**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any one of the five categories | None in OJ |
| R2 | Any combination of the five (cumulative) | In-Directive: literal `software, hardware, firmware components, systems or security parameters` |
R2 is the literal reading. S3.
*Berry anchor:* §5.4.7 (5-way OR); §3.3.1 (`firmware components`, `security parameters`).
**Instance 12 — COORD — S3 — sub-point (e): the **6-way AND** — `recorded, tested, assessed, approved, implemented and verified`**
**This is one of the longest single coordinated obligations in DORA: six verbs joined by AND.** Each verb is a discrete lifecycle phase.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Six discrete phases (each verb is a separate check) | In-Directive: literal `recorded, tested, assessed, approved, implemented and verified` |
| R2 | Six discrete phases that may be delegated to third parties (e.g. CTPPs) | None in OJ |
R1 is the literal reading (Berry §5.5 + §5.6 — see `Building Blocks` chapter for 6-way coordination analysis). R1 vs R2 admit materially distinct compliance populations (R2 admits third-party-delegated change management; R1 requires entity-side verification of each phase). S3. `[no third reading identified]` — original R3 (composite process) is operationally indistinguishable from R1.
*Berry anchor:* §5.5 (six-way coordination); §5.6 (parallelism).
**Instance 13 — VAG — S3 — sub-point (e) clarifying sub-paragraph: `approved by appropriate lines of management and shall have specific protocols in place`**
`appropriate lines of management` — undefined. `specific protocols` — undefined. Three readings collapsed to 2: R1 (single-line) and R2 (multi-line) are operationally distinct; R3 (risk-tier-based) is a hybrid — collapsed to R2 with risk-tier allowance.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Single-line approval (one designated approver per change) | In-Directive: literal `lines of management` |
| R2 | Multi-line approval (technical + business + security) | In-Directive: literal `lines` (plural) |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §3.3.1 (`appropriate lines of management`); §3.3.1 (`specific protocols`).
**Instance 14 — POLY — S3 — sub-point (f): `appropriate and comprehensive documented policies for patches and updates`**
Two qualifiers (`appropriate AND comprehensive`).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both qualifiers must be met (cumulative) | In-Directive: literal `appropriate AND comprehensive` |
| R2 | Either qualifies (R1 admits a `comprehensive but inappropriate` policy or a `narrow but appropriate` policy) | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §5.1 (`appropriate`, `comprehensive`).
**Instance 15 — POLY — S2 — sub-point (f): `patches and updates` (scope)**
Two coverage categories (OR).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Patches only (security patches) | None in OJ |
| R2 | Both (patches AND updates) | In-Directive: literal `patches AND updates` |
R2 is the literal reading. S2 (the catalogue of patches vs updates is operational, not ambiguous). `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`patches`, `updates`).
**Layer 1 observation — Art. 9(4) is the operational core.** It establishes the **mandatory six control families** (info-security policy, network/infrastructure, access control, authentication+encryption, change management, patches/updates). The 6-way AND in 9(4)(e) and the hendiadys-style `appropriate and comprehensive` in 9(4)(f) are operationally consequential. **T3's C15/C16/C17 imposed extra-conjunctive terms (need-to-know, least privilege, MFA) not present in the OJ text — see §5.** The T3-imposed patterns narrow the entity's discretion in ways the regulator did not require; Layer 2 must adjudicate whether T3's narrowing is a security best practice or a CJEU-overreach artefact.
---
#### 4.9 CL10-1 — Art. 10(1) — Detection mechanisms
**Source locus:** Art. 10(1).
> Financial entities shall have in place mechanisms to **promptly detect anomalous activities**, in accordance with Article 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure.
>
> All detection mechanisms referred to in the first subparagraph shall be **regularly tested** in accordance with Article 25.
**Instance 1 — VAG — S3 — `promptly detect anomalous activities`**
The temporal qualifier `promptly`. Same Berry pattern as CL9-4(b) `instantaneously severed or segmented`.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Within minutes (operational) | None in OJ — operational practice converges |
| R2 | Real-time (streaming analysis) | None in OJ |
R1 is the literal reading (most operational practice converges on minutes for detection). R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — original R1 (sub-minute) is operationally below the practical `promptly` threshold; collapsed to R1 (operational) and R2 (real-time).
*Berry anchor:* §5.1 (`promptly`); §3.3.1 (`anomalous activities`).
**Instance 2 — POLY — S3 — `ICT network performance issues and ICT-related incidents`**
Two event types (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Performance only OR incidents only (either suffices) | None in OJ |
| R2 | Both required (AND) | In-Directive: literal `performance issues and ICT-related incidents` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`network performance issues`).
**Instance 3 — POLY — S3 — `material single points of failure`**
`material SPOFs` threshold. Three readings collapsed to 2: R1 (operational) and R2 (vendor) and R3 (process) are operationally similar (all are SPOF categories); consolidated to **R1 = operational/technical** and **R2 = process/vendor (non-technical)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational SPOFs (technical single points) | None in OJ |
| R2 | Process or vendor SPOFs (single supplier / single individual) | None in OJ |
R1 is the dominant reading (per recital context on operational resilience). S3. `[no third reading identified]` — vendor-only and process-only are sub-sets of R2.
*Berry anchor:* §3.3.1 (`single point of failure`); §5.1 (`material`).
---
#### 4.10 CL10-2 — Art. 10(2)+(3) — Multi-layer controls + alert thresholds + sufficient monitoring resources
**Source locus:** Art. 10(2) and 10(3).
> The detection mechanisms referred to in paragraph 1 shall enable **multiple layers of control**, define **alert thresholds and criteria** to trigger and initiate ICT-related incident response processes, including **automatic alert mechanisms** for relevant staff in charge of ICT-related incident response.
>
> Financial entities shall devote **sufficient resources and capabilities** to monitor user activity, the occurrence of ICT anomalies and ICT-related incidents, in particular cyber-attacks.
**Instance 1 — POLY — S3 — `multiple layers of control`**
`multiple layers` is undefined. Three readings collapsed to 2: R1 (two layers / dual control) is operationally below the literal `multiple`; collapsed to **R1 = three+ (defence in depth)** and **R2 = adaptive (per system)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three+ (defence in depth) | In-Directive: literal `multiple` |
| R2 | Adaptive (different layers per system) | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §3.3.1 (`multiple layers`); §5.1 (`multiple`).
**Instance 2 — POLY — S3 — `alert thresholds and criteria`**
Two alert configuration dimensions (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either thresholds OR criteria (one suffices) | None in OJ |
| R2 | Both required (AND) | In-Directive: literal `thresholds and criteria` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`alert thresholds`, `criteria`).
**Instance 3 — VAG — S3 — `sufficient resources and capabilities`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Qualitative judgment (entity-defined) | In-Directive: literal `sufficient` |
| R2 | Risk-based (per Art. 4) | In-Directive: Art. 4 proportionality |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations (resource audit reveals different gaps). S3. `[no third reading identified]`.
*Berry anchor:* §5.1 (`sufficient`); §5.4.6.
---
#### 4.11 CL10-3 — Art. 10(4) — DRSP additional requirement
**Source locus:** Art. 10(4).
> Data reporting service providers shall, in addition, have in place systems that can **effectively check trade reports for completeness, identify omissions and obvious errors, and request re-transmission** of those reports.
**Instance 1 — VAG — S3 — `effectively check trade reports for completeness`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Process-based (procedure exists) | In-Directive: literal `effectively` |
| R2 | Outcome-based (errors are caught) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — R3 (standards-based) is captured as R1 with industry-standard reference.
*Berry anchor:* §5.1 (`effectively`).
**Instance 2 — COORD — S3 — `identify omissions and obvious errors`**
Two error categories (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either suffices | None in OJ |
| R2 | Both required | In-Directive: literal `omissions AND obvious errors` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`omissions`, `obvious errors`).
**Definitional anchor:** DORA Art. 3(63) `data reporting service provider` (MiFIR Art. 2(1)(34)–(36) cross-ref).
**Proportionality-status:** Art. 4 does not apply (sectoral carve-out for DRSP — uniform obligation).
---
#### 4.12 CL11-1 — Art. 11(1)+(2) chapeau + (a)–(e) — ICT business continuity policy + 5 objectives
`[scope: BCP chapeau + 5 enumerated aims; multi-instance within one card per Q6=a convention; do not split into 5 sub-clauses]`
**Source locus:** Art. 11(1) and 11(2) chapeau and sub-points (a)–(e).
> As part of the ICT risk management framework referred to in Article 6(1) and based on the identification requirements set out in Article 8, financial entities shall put in place a **comprehensive ICT business continuity policy**, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity.
>
> Financial entities shall implement the ICT business continuity policy through **dedicated, appropriate and documented arrangements, plans, procedures and mechanisms** aiming to:
>
> (a) ensure the continuity of the financial entity's critical or important functions;
>
> (b) **quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents** in a way that limits damage and prioritises the resumption of activities and recovery actions;
>
> (c) **activate, without delay**, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident and prevent further damage, as well as tailored response and recovery procedures established in accordance with Article 12;
>
> (d) estimate preliminary impacts, damages and losses;
>
> (e) **set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders** in accordance with Article 14, and report to the competent authorities in accordance with Article 19.
**Instance 1 — VAG — S3 — `comprehensive ICT business continuity policy`**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exhaustive (every possible scenario) | None in OJ |
| R2 | Risk-proportional (per Art. 4) | In-Directive: Art. 4 |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]`.
*Berry anchor:* §5.1 (`comprehensive`).
**Instance 2 — POLY — S3 — chapeau: `dedicated, appropriate and documented` (3-way AND)**
Three qualifiers on the policy. Same pattern as CL9-4 chapeau. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete qualifiers (each required) | In-Directive: literal |
| R2 | Composite (one workflow) | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (3-way AND); §5.1 (`dedicated`, `appropriate`, `documented`).
**Instance 3 — POLY — S3 — sub-points (a)+(b)+(c)+(d)+(e): five BCP objectives**
Five discrete objectives, each with its own threshold. The compliance population is the union (per sub-point (a), the entity must aim at continuity AND at quick response AND at timely activation AND at impact estimation AND at communication). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each objective is independent (any one satisfied is partial compliance) | None in OJ |
| R2 | All five required (cumulative) | In-Directive: literal enumeration |
R2 is the literal reading. S3. `[no third reading identified]` — R3 (entity prioritises / risk-based subset) is captured via Art. 4 at the chapeau level, not as an independent reading.
*Berry anchor:* §5.4.7 (5-way AND); §5.5 (enumeration).
**Instance 4 — VAG — S3 — sub-point (b): `quickly, appropriately and effectively respond to, and resolve` + sub-point (c): `activate, without delay`**
The temporal operators. Three readings collapsed to 2 per operator: **sub-point (b)** — R1 (hendiadys / single concept) vs R2 (compound / cumulative). **sub-point (c)** — R1 (immediately) vs R2 (as soon as practicable).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Compound (three adverbs cumulative) | In-Directive: literal three adverbs (sub-b) |
| R2 | Hendiadys (single concept) | None in OJ (sub-b) |
| R1' | Immediately (within minutes) | In-Directive: literal `without delay` (sub-c) |
| R2' | As soon as practicable | None in OJ (sub-c) |
For sub-point (b), R1 is the literal reading. For sub-point (c), R1' is the literal reading. R1' vs R2' admit materially distinct compliance populations. S3. `[no third reading identified]` for both sub-points.
*Berry anchor:* §5.4.7 (3-way AND adverb); §5.1 (`without delay`).
**Instance 5 — POLY — S3 — sub-point (e): `internal staff and external stakeholders`**
Two audience categories (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Internal only OR external only (either suffices) | None in OJ |
| R2 | Both (internal AND external) | In-Directive: literal `internal staff and external stakeholders` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Definitional anchor:** DORA-D22 `critical or important function` (S3); DORA-D08 `ICT-related incident` (S3); cross-ref to Art. 8, Art. 12, Art. 14, Art. 19.
**RTS-pending:** Art. 15(d) specifies further the components of the ICT business continuity policy referred to in Art. 11(1). Art. 15(f) specifies further the components of Art. 11(3) ICT response and recovery plans (relevant for sub-point (c) activation).
**Proportionality-status:** Art. 4 applies.
---
#### 4.13 CL11-2 — Art. 11(3)+(4)+(5) — Recovery plans + BCP for outsourced CIFs + BIA
`[scope: recovery plans, outsourcing BCP, BIA; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 11(3), 11(4), and 11(5).
> As part of the ICT risk management framework referred to in Article 6(1), financial entities shall implement associated ICT response and recovery plans which, in the case of financial entities other than microenterprises, shall be subject to **independent internal audit reviews**.
>
> Financial entities shall put in place, maintain and periodically test appropriate ICT business continuity plans, notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers.
>
> As part of the overall business continuity policy, financial entities shall conduct a **business impact analysis (BIA)** of their exposures to severe business disruptions. Under the BIA, financial entities shall assess the potential impact of severe business disruptions by means of **quantitative and qualitative criteria**, using internal and external data and scenario analysis, as appropriate. The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies. Financial entities shall ensure that ICT assets and ICT services are **designed and used in full alignment with the BIA**, in particular with regard to adequately ensuring the redundancy of all critical components.
**Instance 1 — POLY — S2 — `response and recovery plans` (Art. 11(3))**
Two plan types (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either plan type (response OR recovery) | None in OJ |
| R2 | Both required (AND) | In-Directive: literal `response AND recovery plans` |
R2 is the literal reading. S2. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Instance 2 — VAG — S3 — `independent internal audit reviews` (Art. 11(3))**
`independent internal` is itself a hendiadys. The independence standard applied to internal audit.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Pure internal audit (no independence requirement) | None in OJ |
| R2 | Internal audit with independence safeguards (structural separation) | In-Directive: literal `independent internal` |
R2 is the literal reading. S3 (same `independent` Berry classic as CL24-3). `[no third reading identified]` — R3 (external audit) contradicts `internal`.
*Berry anchor:* §3.3.1 (`independent internal`).
**Instance 3 — VAG — S3 — `put in place, maintain and periodically test` (Art. 11(4))**
Three coordinated verbs. Same Berry pattern as CL9-2 and CL11-1. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete lifecycle phases | In-Directive: literal `put in place, maintain AND periodically test` |
| R2 | Three independent obligations | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 4 — POLY — S3 — `quantitative and qualitative criteria` (Art. 11(5)) + `designed and used in full alignment with the BIA`**
Two assessment-method classes (AND) + alignment requirement. Three readings collapsed to 2 per operator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either quantitative OR qualitative (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal `quantitative AND qualitative criteria` |
| R1' | Risk-based alignment (BIA informs ICT architecture) | None in OJ |
| R2' | Strict alignment (BIA dictates ICT architecture) | In-Directive: literal `in full alignment` |
R2 and R2' are the literal readings. S3 for both. `[no third reading identified]` — review-based alignment is captured as R1' (BIA as one input).
*Berry anchor:* §5.4.7 (AND on criteria; AND on alignment); §3.3.1 (`full alignment`).
---
#### 4.14 CL11-3 — Art. 11(6)+(7)+(8)+(9) — BCP testing + crisis management + records + CSD reporting
`[scope: BCP testing cadence, crisis mgmt, records, CSD reporting; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 11(6), 11(7), 11(8), and 11(9).
> As part of their comprehensive ICT risk management, financial entities shall:
>
> (a) **test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly**, as well as in the event of any substantive changes to ICT systems supporting critical or important functions;
>
> (b) test the crisis communication plans established in accordance with Article 14.
>
> For the purposes of the first subparagraph, point (a), financial entities, other than microenterprises, shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities necessary to meet the obligations set out in Article 12.
>
> Financial entities shall regularly review their ICT business continuity policy and ICT response and recovery plans, taking into account the results of tests carried out in accordance with the first subparagraph and recommendations stemming from audit checks or supervisory reviews.
>
> Financial entities, other than microenterprises, shall have a **crisis management function**, which, in the event of activation of their ICT business continuity plans or ICT response and recovery plans, shall, inter alia, set out clear procedures to manage internal and external crisis communications in accordance with Article 14.
>
> Financial entities shall keep readily accessible records of activities before and during disruption events when their ICT business continuity plans and ICT response and recovery plans are activated.
>
> Central securities depositories shall provide the competent authorities with copies of the results of the ICT business continuity tests, or of similar exercises.
**Instance 1 — VAG — S3 — `at least yearly` (sub-point a) + `substantive changes` (sub-point a)**
The temporal anchor + change threshold. Three readings collapsed to 2 per operator. **Temporal**: R1 (calendar year) vs R2 (rolling 12 months). **Change threshold**: R1 (same as `major change` from Art. 8(3)) vs R2 (test-materially broader).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Calendar year (yearly) | None in OJ |
| R2 | Rolling 12 months | None in OJ — operational practice converges |
| R1' | = `major change` (Art. 8(3) threshold) | None in OJ |
| R2' | Test-materially broader (substantive includes test-relevant) | In-Directive: literal `substantive changes` (broader than `major`) |
R2 is the dominant reading for `at least yearly`; R2' is the literal reading for `substantive changes`. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]` — anniversary-date reading is operationally a sub-set of R2 (rolling 12 months).
*Berry anchor:* §5.7 (temporal operator); §5.1 (`at least yearly`); §3.3.1 (`substantive`).
**Instance 2 — POLY — S3 — non-microenterprise additional scenarios (sub-paragraph for (a))**
`scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities` (3 scenario categories OR). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cyber-attacks only OR switchovers only (either suffices) | None in OJ |
| R2 | All three categories required (cumulative) | In-Directive: literal three categories |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (3-way AND); §3.3.1.
**Instance 3 — VAG — S3 — `crisis management function` (Art. 11(7)) + `readily accessible records` (Art. 11(8))**
Two governance qualifiers. Three readings collapsed to 2 per operator. **Crisis mgmt function**: R1 (organisational unit) vs R2 (both unit + procedure). **Records**: R1 (within 1 hour) vs R2 (within operational SLA).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Organisational unit only (a team/role) | None in OJ |
| R2 | Both (organisational unit + procedure) | In-Directive: literal `function` (broad) |
| R1' | Within 1 hour (fixed time) | None in OJ |
| R2' | Within operational SLA (entity-defined) | In-Directive: literal `readily accessible` |
R2 and R2' are the literal readings. S3 for both. `[no third reading identified]` for both.
*Berry anchor:* §3.3.1 (`crisis management function`); §5.1 (`readily accessible`).
**Definitional anchor:** DORA-D22 `critical or important function` (S3); DORA-D60 `microenterprise` (S2 — per pilot §2.12; clause excludes microenterprises for crisis mgmt); CSDs sectoral carve-out per Art. 2(1)(s) cross-ref.
**RTS-pending:** Art. 15(e) specifies further the testing of BCPs referred to in Art. 11(6), including scenarios of CIF deterioration or failure + CTPP insolvency + political risks.
**Proportionality-status:** Art. 4 applies; non-microenterprise additional scenarios carve-out + crisis-management function carve-out.
---
#### 4.15 CL11-4 — Art. 11(10)+(11) — Cost reporting + ESA guidelines
**Source locus:** Art. 11(10) and 11(11).
> Financial entities, other than microenterprises, shall report to the competent authorities, upon their request, an estimation of **aggregated annual costs and losses** caused by major ICT-related incidents.
>
> In accordance with Article 16 of Regulations (EU) No 1093/2010, (EU) No 1094/2010 and (EU) No 1095/2010, the ESAs, through the Joint Committee, shall by 17 July 2024 develop **common guidelines** on the estimation of aggregated annual costs and losses referred to in paragraph 10.
**Instance 1 — POLY — S3 — `aggregated annual costs and losses` + `upon their request` (reporting trigger)**
Two aggregate metrics (AND) + reporting trigger. Three readings collapsed to 2 per operator. **Metrics**: R1 (costs only) vs R2 (both). **Trigger**: R1 (reactive only) vs R2 (reactive + periodic).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Costs only (losses excluded) | None in OJ |
| R2 | Both (costs AND losses) | In-Directive: literal `costs and losses` |
| R1' | Reactive only (entity waits for CA request) | In-Directive: literal `upon their request` |
| R2' | Reactive + periodic (entity reports even without request) | None in OJ |
R2 and R1' are the literal readings. S3. `[no third reading identified]` — voluntary disclosure (R3) is captured by the `upon their request` literal as R1'.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`costs`, `losses`, `upon their request`).
**Instance 2 — POLY — S3 — `common guidelines` (Art. 11(11))**
The output type.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Non-binding (per Art. 16 ESA Regulations) | In-Directive: Art. 16 ESA Regulations (guidelines are non-binding) |
| R2 | Comply-or-explain | In-Directive: Art. 16 ESA Regulations `comply or explain` |
R2 is the operational reading (ESA guidelines carry comply-or-explain under Art. 16). S3. `[no third reading identified]` — binding reading is precluded by Art. 16.
*Berry anchor:* §3.3.1 (`common guidelines`).
**Definitional anchor:** DORA Art. 3(10) `major ICT-related incident` (DORA-D10, S3 — `high adverse impact`); DORA-D60 `microenterprise` carve-out.
**RTS-pending:** Art. 11(11) mandates ESA guidelines (separate from RTS) by 17 July 2024. **Note: guidelines ≠ RTS** — guidelines are non-binding per Art. 16 of the three ESA Regulations.
**Proportionality-status:** Art. 4 applies; non-microenterprise carve-out.
---
#### 4.16 CL12-1 — Art. 12(1)+(2) — Backup policies chapeau
**Source locus:** Art. 12(1) and 12(2).
> For the purpose of ensuring the restoration of ICT systems and data with **minimum downtime, limited disruption and loss**, as part of their ICT risk management framework, financial entities shall develop and document:
>
> (a) backup policies and procedures specifying the **scope of the data that is subject to the backup and the minimum frequency of the backup**, based on the criticality of information or the confidentiality level of the data;
>
> (b) restoration and recovery procedures and methods.
>
> Financial entities shall set up backup systems that can be activated in accordance with the backup policies and procedures, as well as restoration and recovery procedures and methods. The activation of backup systems shall **not jeopardise the security of the network and information systems or the availability, authenticity, integrity or confidentiality of data**. Testing of the backup procedures and restoration and recovery procedures and methods shall be undertaken periodically.
**Instance 1 — COORD — S3 — `minimum downtime, limited disruption and loss`**
Three restoration-quality qualifiers (AND). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete metrics (downtime + disruption + loss) | In-Directive: literal three-coordination |
| R2 | Composite (overall restoration quality) | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]` — R3 (three independent metrics) is operationally indistinguishable from R1.
*Berry anchor:* §5.5 (three-way coordination); §3.3.1 (`downtime`).
**Instance 2 — POLY — S3 — `scope of the data that is subject to the backup and the minimum frequency of the backup` (sub-point a) + `based on the criticality of information or the confidentiality level of the data`**
Two backup-policy dimensions (AND) + two backup-classification dimensions (OR). Three readings collapsed to 2 per operator. **Policy**: R1 (either scope or frequency) vs R2 (both required). **Classification**: R1 (criticality only) vs R2 (either classification).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either scope OR frequency (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal `scope AND frequency` |
| R1' | Criticality only (one dimension) | None in OJ |
| R2' | Either criticality OR confidentiality (OR) | In-Directive: literal `criticality … OR confidentiality` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (AND for policy; OR for classification); §3.3.1.
**Instance 3 — POLY — S3 — `availability, authenticity, integrity or confidentiality` (12(2) — backup-activation condition)**
Four data-security dimensions — same OR as CL9-2. The condition is the **non-jeopardise** clause. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cumulative (all four required to hold) | None in OJ |
| R2 | Cumulative (the activation must not jeopardise any of the four) | In-Directive: literal cumulative `availability AND authenticity AND integrity AND confidentiality` |
R2 is the literal reading (the activation must not jeopardise any of the four). S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (4-way AND); §3.3.1 (`jeopardise`).
---
#### 4.17 CL12-2 — Art. 12(3)+(4) — Restoration + redundant ICT capacities
**Source locus:** Art. 12(3) and 12(4).
> When restoring backup data using own systems, financial entities shall use ICT systems that are **physically and logically segregated from the source ICT system**. The ICT systems shall be securely protected from any unauthorised access or ICT corruption and allow for the timely restoration of services making use of data and system backups as necessary.
>
> For central counterparties, the recovery plans shall enable the recovery of all transactions at the time of disruption to allow the central counterparty to continue to operate with certainty and to complete settlement on the scheduled date.
>
> Data reporting service providers shall additionally maintain adequate resources and have back-up and restoration facilities in place in order to offer and maintain their services at all times.
>
> Financial entities, other than microenterprises, shall maintain **redundant ICT capacities** equipped with resources, capabilities and functions that are adequate to ensure business needs. Microenterprises shall assess the need to maintain such redundant ICT capacities based on their risk profile.
**Instance 1 — POLY — S3 — `physically and logically segregated`**
Two segregation dimensions (AND). The security pattern is **defence-in-depth segregation**. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Physical only OR logical only (either suffices) | None in OJ |
| R2 | Both required (physical AND logical) | In-Directive: literal `physically AND logically segregated` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`physically segregated`, `logically segregated`).
**Instance 2 — VAG — S3 — `timely restoration of services`**
`timely` — same Berry temporal operator as CL7-1(c) `timely provision of services`. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Within RTO defined in Art. 12(6) | In-Directive: Art. 12(6) reference |
| R2 | As soon as practicable | None in OJ |
R1 is the literal reading (Art. 12(6) supplies the temporal anchor). S3. `[no third reading identified]`.
*Berry anchor:* §3.3.1 (`timely`); §5.1.
**Instance 3 — POLY — S3 — `redundant ICT capacities … adequate to ensure business needs` (Art. 12(4))**
The adequacy threshold. Three readings collapsed to 2: R1 (quantitative N+1/N+2) and R3 (architecture-based) are operationally similar; consolidated to **R1 = quantitative** and **R2 = qualitative**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative redundancy (N+1, N+2) | None in OJ |
| R2 | Qualitative redundancy (backups + failover) | In-Directive: literal `redundant` |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]`.
*Berry anchor:* §3.3.1 (`redundant ICT capacities`); §5.1 (`adequate`).
**Definitional anchor:** DORA-D60 `microenterprise` (S2 — per pilot §2.12); CCP sectoral carve-out per Art. 2(1)(o) cross-ref; DRSP carve-out per Art. 2(1)(t).
**Proportionality-status:** Art. 4 applies; non-microenterprise obligation + microenterprise risk-profile assessment.
---
#### 4.18 CL12-3 — Art. 12(5) — CSD secondary processing site
**Source locus:** Art. 12(5) chapeau and sub-points (a)–(c).
> Central securities depositories shall maintain at least one **secondary processing site** endowed with adequate resources, capabilities, functions and staffing arrangements to ensure business needs.
>
> The secondary processing site shall be:
>
> (a) located at a geographical distance from the primary processing site to ensure that it bears a **distinct risk profile** and to prevent it from being affected by the event which has affected the primary site;
>
> (b) capable of ensuring the continuity of critical or important functions identically to the primary site, or providing the level of services necessary to ensure that the financial entity performs its critical operations within the recovery objectives;
>
> (c) **immediately accessible** to the financial entity's staff to ensure continuity of critical or important functions in the event that the primary processing site has become unavailable.
**Instance 1 — VAG — S3 — `geographical distance … distinct risk profile`**
The geographic distance is undefined. Three readings collapsed to 2: R1 (regional >100km) and R2 (country-level different country) are operationally similar; consolidated to **R1 = sufficient to survive regional disaster** and **R2 = entity-determined**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Regional (sufficient to survive a regional disaster) | None in OJ |
| R2 | Entity-determined (per risk profile) | In-Directive: literal `geographical distance` (broad) |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3. `[no third reading identified]`.
*Berry anchor:* §5.1 (`geographical distance`); §3.3.1 (`distinct risk profile`).
**Instance 2 — VAG — S3 — `immediately accessible` (sub-point c)**
Same Berry temporal operator as CL11-2 `without delay`. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Immediately (within minutes) | In-Directive: literal `immediately accessible` |
| R2 | Within operational SLA | None in OJ |
R1 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.1 (`immediately`); §3.3.1 (`accessible`).
**Definitional anchor:** DORA-D22 `critical or important function` (S3); CSD sectoral carve-out per Art. 2(1)(r).
**Proportionality-status:** Art. 4 applies (entity-type-specific: CSDs only).
---
#### 4.19 CL12-4 — Art. 12(6)+(7) — RTO/RPO + data integrity checks
**Source locus:** Art. 12(6) and 12(7).
> In determining the **recovery time and recovery point objectives** for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency. Such time objectives shall ensure that, in extreme scenarios, the agreed service levels are met.
>
> When recovering from an ICT-related incident, financial entities shall perform necessary checks, including any **multiple checks and reconciliations**, in order to ensure that the highest level of data integrity is maintained. These checks shall also be performed when reconstructing data from external stakeholders, in order to ensure that all data is consistent between systems.
**Instance 1 — COORD — S3 — `recovery time and recovery point objectives`**
Two objectives (AND). Berry-flagged hard metric (RTO + RPO). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either RTO OR RPO (one suffices) | None in OJ |
| R2 | Both required (RTO AND RPO for every function) | In-Directive: literal `recovery time AND recovery point objectives` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.5 (two-way AND); §3.3.1 (`recovery time objective`, `recovery point objective`).
**Instance 2 — VAG — S3 — `the highest level of data integrity` + `multiple checks and reconciliations`**
Two integrity-control qualifiers. Three readings collapsed to 2 per operator. **Highest**: R1 (industry-standard) vs R2 (strongest possible). **Multiple checks**: R1 (multiple only) vs R2 (both required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Industry-standard integrity (bit-for-bit) | None in OJ |
| R2 | Strongest possible integrity (checksum + reconciliation + comparison) | In-Directive: literal `highest level` |
| R1' | Multiple checks only (one type) | None in OJ |
| R2' | Both required (multiple checks AND reconciliations) | In-Directive: literal `multiple checks AND reconciliations` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.1 (`highest`); §3.3.1 (`data integrity`); §5.4.7 (AND for checks).
**Definitional anchor:** DORA Art. 3(8) `ICT-related incident` (DORA-D08); DORA-D22 `critical or important function` (S3).
**Proportionality-status:** Art. 4 applies.
---
#### 4.20 CL13-1 — Art. 13(1)+(2)+(3) — Threat-intel + post-incident reviews + lessons propagation
`[scope: learn-and-evolve cycle (1)-(3); multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 13(1), 13(2), 13(3).
> Financial entities shall have in place **capabilities and staff to gather information on vulnerabilities and cyber threats**, ICT-related incidents, in particular cyber-attacks, and analyse the impact they are likely to have on their digital operational resilience.
>
> Financial entities shall put in place **post ICT-related incident reviews** after a major ICT-related incident disrupts their core activities, analysing the causes of disruption and identifying required improvements to the ICT operations or within the ICT business continuity policy referred to in Article 11.
>
> Financial entities, other than microenterprises, shall, upon request, communicate to the competent authorities, the changes that were implemented following post ICT-related incident reviews as referred to in the first subparagraph.
>
> The post ICT-related incident reviews referred to in the first subparagraph shall determine whether the established procedures were followed and the actions taken were effective, including in relation to the following:
>
> (a) the promptness in responding to security alerts and determining the impact of ICT-related incidents and their severity;
>
> (b) the quality and speed of performing a forensic analysis, where deemed appropriate;
>
> (c) the effectiveness of incident escalation within the financial entity;
>
> (d) the effectiveness of internal and external communication.
>
> Lessons derived from the digital operational resilience testing carried out in accordance with Articles 26 and 27 and from real life ICT-related incidents, in particular cyber-attacks, along with challenges faced upon the activation of ICT business continuity plans and ICT response and recovery plans, together with relevant information exchanged with counterparts and assessed during supervisory reviews, shall be **duly incorporated on a continuous basis into the ICT risk assessment process**. Those findings shall form the basis for appropriate reviews of relevant components of the ICT risk management framework referred to in Article 6(1).
**Instance 1 — POLY — S3 — `vulnerabilities and cyber threats` + `ICT-related incidents, in particular cyber-attacks` (Art. 13(1))**
Two info categories (AND) + event categories (illustrative). Three readings collapsed to 2 per operator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either vulnerabilities OR cyber threats (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal `vulnerabilities AND cyber threats` |
| R1' | Only cyber-attacks (excludes other ICT incidents) | None in OJ |
| R2' | Any ICT-related incident (cyber-attacks illustrative) | In-Directive: literal `in particular` (illustrative) |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`vulnerabilities`, `cyber threats`, `in particular`).
**Instance 2 — VAG — S3 — `after a major ICT-related incident disrupts their core activities` (Art. 13(2) trigger) + four review dimensions (a)–(d)**
The post-incident-review trigger + four review dimensions. Three readings collapsed to 2 per operator. **Trigger**: R1 (strict / major only) vs R2 (entity-determined). **Dimensions**: R1 (each independent) vs R2 (all four required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Major only (strict per DORA-D10) | In-Directive: literal `major ICT-related incident` |
| R2 | Entity-determined (lower threshold) | None in OJ |
| R1' | Each dimension is independent (any one is partial compliance) | None in OJ |
| R2' | All four required (cumulative) | In-Directive: literal four-way enumeration |
R1 and R2' are the literal readings. S3 for both. `[no third reading identified]` for both.
*Berry anchor:* §3.3.1 (`major ICT-related incident`); §5.4.7 (4-way for dimensions); DORA-D10.
**Instance 3 — POLY — S3 — four input sources for lessons (Art. 13(3)) + `duly incorporated on a continuous basis`**
Four sources (AND) + `duly` + `continuously` compound. Three readings collapsed to 2 per operator. **Sources**: R1 (TLPT only or any single source) vs R2 (all four required). **Incorporation**: R1 (continuous per Art. 4) vs R2 (event-based).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any single source (TLPT, incidents, BCP activation, supervisory) | None in OJ |
| R2 | All four required (cumulative) | In-Directive: literal four-source enumeration |
| R1' | Continuously, in accordance with Art. 4 | In-Directive: literal `continuously` |
| R2' | Event-based (at management-body meetings) | None in OJ |
R2 and R1' are the literal readings. S3 for both. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (4-way AND for sources); §5.5; §5.1 (`duly`, `continuously`).
---
#### 4.21 CL13-2 — Art. 13(4)+(5)+(6)+(7) — Effectiveness monitoring + training + tech developments
`[scope: monitoring, reporting, training, technology monitoring; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 13(4), 13(5), 13(6), 13(7).
> Financial entities shall monitor the effectiveness of the implementation of their digital operational resilience strategy set out in Article 6(8). They shall map the evolution of ICT risk over time, analyse the frequency, types, magnitude and evolution of ICT-related incidents, in particular cyber-attacks and their patterns, with a view to understanding the level of ICT risk exposure, in particular in relation to critical or important functions, and **enhance the cyber maturity and preparedness** of the financial entity.
>
> Senior ICT staff shall report **at least yearly** to the management body on the findings referred to in paragraph 3 and put forward recommendations.
>
> Financial entities shall develop ICT security awareness programmes and digital operational resilience training as **compulsory modules in their staff training schemes**. Those programmes and training shall be applicable to all employees and to senior management staff, and shall have a level of complexity **commensurate to the remit of their functions**. Where appropriate, financial entities shall also include ICT third-party service providers in their relevant training schemes in accordance with Article 30(2), point (i).
>
> Financial entities, other than microenterprises, shall monitor **relevant technological developments** on a continuous basis, also with a view to understanding the possible impact of the deployment of such new technologies on ICT security requirements and digital operational resilience. They shall keep up-to-date with the latest ICT risk management processes, in order to effectively combat current or new forms of cyber-attacks.
**Instance 1 — VAG — S3 — `enhance the cyber maturity and preparedness` (Art. 13(4)) + `frequency, types, magnitude and evolution` (4 dimensions)**
Two effectiveness-monitoring qualifiers. Three readings collapsed to 2 per operator. **Maturity**: R1 (CMMI-style levels) vs R2 (documented preparedness). **Dimensions**: R1 (any one suffices) vs R2 (all four required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Mature cyber controls (CMMI-style levels) | None in OJ |
| R2 | Documented preparedness (BCP testing) | In-Directive: literal `preparedness` |
| R1' | Any one suffices | None in OJ |
| R2' | All four required | In-Directive: literal four-way enumeration |
R1 and R2' are the literal readings. S3 for both. `[no third reading identified]` for both.
*Berry anchor:* §3.3.1 (`cyber maturity`, `preparedness`); §5.4.7 (4-way AND); §5.5.
**Instance 2 — VAG — S3 — `at least yearly` (Art. 13(5))**
Same Berry temporal anchor as CL8-1(2) and CL24-5. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Calendar year | None in OJ |
| R2 | Rolling 12 months | None in OJ — operational practice converges |
R2 is the dominant reading. S3. `[no third reading identified]` — anniversary-date is operationally a sub-set of R2.
*Berry anchor:* §5.7; §5.1.
**Instance 3 — VAG — S3 — `commensurate to the remit of their functions` (Art. 13(6)) + `all employees and to senior management staff`**
**T3 imposed `role-specific training` per C28; OJ says only `commensurate to the remit of their functions`.** Three readings collapsed to 2: R1 (remit) is OJ-literal; R3 (function-specific) is operationally indistinguishable from R2 (role-specific) — collapsed to **R1 = remit-based** and **R2 = role-specific (T3-imposed)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Remit-scope only (the broader the remit, the deeper the training) | In-Directive: literal `commensurate to the remit of their functions` |
| R2 | Role-specific (each role has a defined training path) | None in OJ — T3-imposed (gap from C28) |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R2 admits pre-mapped role paths; R1 admits training tailored to the staff member's actual remit). S3. **T3's `role-specific` mapping is unsubstantiated by the OJ text — flag in §5.**
*Berry anchor:* §3.3.1 (`commensurate`, `remit of their functions`); §5.4.7 (AND for audience).
**Definitional anchor:** DORA Art. 3(30) `management body` (DORA-D30, composite cross-reference); DORA-D22 `critical or important function` (S3); cross-ref to Art. 30(2)(i) on including CTPPs in training.
**Proportionality-status:** Art. 4 applies; non-microenterprise carve-out for Art. 13(7) technology monitoring.
---
#### 4.22 CL14-1 — Art. 14(1) — Crisis communication plans
**Source locus:** Art. 14(1).
> As part of the ICT risk management framework referred to in Article 6(1), financial entities shall have in place **crisis communication plans** enabling a **responsible disclosure** of, at least, **major ICT-related incidents or vulnerabilities** to clients and counterparts as well as to the public, as appropriate.
**Instance 1 — VAG — S3 — `responsible disclosure`**
`responsible` is Berry-flagged. Three readings collapsed to 2: R3 (entity-determined) is captured by R1 with entity latitude; collapsed to **R1 = timely + accurate** and **R2 = CVD-style (coordinated disclosure process)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Timely + accurate (R1 is literal; entity latitude) | In-Directive: literal `responsible` |
| R2 | CVD-style (vulnerability-disclosure-ethic-driven) | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R2 admits a coordinated disclosure process; R1 admits ad-hoc statements). S3. `[no third reading identified]`.
*Berry anchor:* §3.3.1 (`responsible disclosure`).
**Instance 2 — POLY — S3 — `major ICT-related incidents or vulnerabilities` + `clients and counterparts as well as to the public` (3-way AND)**
Two disclosure-trigger categories (OR) + three audience categories (AND). Three readings collapsed to 2 per operator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Major incidents only (no vulnerabilities) | None in OJ |
| R2 | Either (incidents OR vulnerabilities) | In-Directive: literal `incidents OR vulnerabilities` |
| R1' | Single audience (any one of three) | None in OJ |
| R2' | All three audiences (cumulative) | In-Directive: literal `clients AND counterparts AND public` |
R2 and R2' are the literal readings. S3 for both. `[no third reading identified]` for both — vulnerability-only (R3) is captured by R2.
*Berry anchor:* §5.4.7 (OR for trigger; AND for audience); §3.3.1.
---
#### 4.23 CL14-2 — Art. 14(2)+(3) — Internal + external communication policies + designated person
`[scope: communication differentiation + designated spokesperson; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 14(2) and 14(3).
> As part of the ICT risk management framework, financial entities shall implement communication policies for internal staff and for external stakeholders. Communication policies for staff shall take into account the need to **differentiate between staff involved in ICT risk management**, in particular the staff responsible for response and recovery, and staff that needs to be informed.
>
> At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents and fulfil the **public and media function** for that purpose.
**Instance 1 — POLY — S3 — `internal staff and external stakeholders` (Art. 14(2))**
Two audience categories (AND). Same pattern as CL11-2(4). Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Internal only OR external only (either suffices) | None in OJ |
| R2 | Both (internal AND external) | In-Directive: literal `internal staff and external stakeholders` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Instance 2 — POLY — S3 — `staff involved in ICT risk management … staff that needs to be informed` + `public and media function` (Art. 14(3))**
Two staff categories (POLY) + function descriptor. Three readings collapsed to 2 per operator. **Staff differentiation**: R1 (involved only or informed only) vs R2 (differentiate). **Public/media function**: R1 (spokesperson only) vs R2 (combined PR + media).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Involved staff only OR informed staff only (one suffices) | None in OJ |
| R2 | Differentiate (entity categorises by access level) | In-Directive: literal `differentiate between … and …` |
| R1' | Spokesperson role only (speaks to media) | None in OJ |
| R2' | Combined (PR + media) | In-Directive: literal `public AND media` |
R2 and R2' are the literal readings. R2 is S3; R2' is S2. `[no third reading identified]` for both — R3 (PR function only) is captured by R2'.
*Berry anchor:* §3.3.1 (`differentiate`, `public and media function`); §5.4.7 (AND).
**Definitional anchor:** cross-ref to Art. 11(2)(e) on communication during incidents; DORA Art. 3(30) `management body` (DORA-D30).
**Proportionality-status:** Art. 4 applies.
---
#### 4.24 CL15-1 — Art. 15 chapeau + sub-points (a)–(g) — ESAs RTS mandate
`[scope: ESAs (Joint Committee + ENISA) → Commission; meta-procedural RTS mandate]`
**Source locus:** Art. 15 chapeau and sub-points (a)–(g).
> The ESAs shall, through the Joint Committee, in consultation with the European Union Agency on Cybersecurity (ENISA), develop common draft regulatory technical standards in order to:
>
> (a) **specify further elements to be included in the ICT security policies, procedures, protocols and tools** referred to in Article 9(2), with a view to ensuring the security of networks, enable adequate safeguards against intrusions and data misuse, preserve the availability, authenticity, integrity and confidentiality of data, including cryptographic techniques, and guarantee an accurate and prompt data transmission without major disruptions and undue delays;
>
> (b) develop further components of the controls of **access management rights referred to in Article 9(4), point (c)**, and associated human resource policy specifying access rights, procedures for granting and revoking rights, monitoring anomalous behaviour in relation to ICT risk through appropriate indicators, including for network use patterns, hours, IT activity and unknown devices;
>
> (c) develop further the mechanisms specified in **Article 10(1)** enabling a prompt detection of anomalous activities and the criteria set out in Article 10(2) triggering ICT-related incident detection and response processes;
>
> (d) specify further the components of the **ICT business continuity policy referred to in Article 11(1)**;
>
> (e) specify further the testing of ICT business continuity plans referred to in **Article 11(6)** to ensure that such testing duly takes into account scenarios in which the quality of the provision of a critical or important function deteriorates to an unacceptable level or fails, and duly considers the potential impact of the insolvency, or other failures, of any relevant ICT third-party service provider and, where relevant, the political risks in the respective providers' jurisdictions;
>
> (f) specify further the components of the **ICT response and recovery plans referred to in Article 11(3)**;
>
> (g) specifying further the content and format of the **report on the review of the ICT risk management framework** referred to in Article 6(5).
>
> When developing those draft regulatory technical standards, the ESAs shall take into account **the size and the overall risk profile** of the financial entity, and the nature, scale and complexity of its services, activities and operations, while duly taking into consideration any specific feature arising from the **distinct nature of activities across different financial services sectors**.
>
> The ESAs shall submit those draft regulatory technical standards to the Commission by **17 January 2024**.
**Instance 1 — VAG — S3 — `specify further` (verbatim from Art. 15 chapeau and sub-points) + `the size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations` (RTS-calibration factors)**
The RTS specification mandate. The verbs vary across sub-points (`specify further elements`, `develop further components`, `further develop`, etc.) but the operational meaning is the same: ESAs fill in details. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Detailed technical specifications (comprehensive) | In-Directive: literal `specify further` |
| R2 | Light-touch specifications (references to standards) | None in OJ |
| R1' | Any single calibration factor (size, risk, N/S/C) | None in OJ |
| R2' | All four required (cumulative) | In-Directive: literal four-factor enumeration |
R1 and R2' are the literal readings. S3. `[no third reading identified]` — R3 (hybrid specifications) is captured by R1 with reference to standards.
*Berry anchor:* §3.3.1 (`specify further`, `nature, scale and complexity`); §5.4.7 (AND for factors); §5.5.
**Instance 2 — POLY — S3 — seven RTS subject areas (sub-points a–g) + sectoral calibration**
The 7 RTS subjects map to 7 Art. 9-11-6 elements. The RTS is multi-component. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each RTS subject is independent (one RTS per subject) | None in OJ |
| R2 | Single joint RTS covering all seven subjects | In-Directive: literal `common draft regulatory technical standards` (joint) |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (7-way coordination); §3.3.1 (`common`, `distinct nature`).
**Definitional anchor:** cross-ref to Art. 9(2), 9(4)(c), 10(1), 10(2), 11(1), 11(3), 11(6), 6(5).
**RTS-pending:** **YES.** Art. 15 RTS deadline 17 January 2024 (passed); as of mid-2025, **Delegated Regulation (EU) 2024/1774** of 31 May 2024 supplements DORA with the regulatory technical standards for Art. 15(a)–(g), adopted by the Commission on the basis of ESA Joint Committee draft. The adopted RTS is binding and resolves many S3 instances flagged above (e.g. specifics of Art. 9(2) security controls, Art. 11(6) BCP testing scenarios).
**Proportionality-status:** Art. 4 does not apply (clause is addressed to ESAs, not financial entities).
---
#### 4.25 CL16-1 — Art. 16(1) first sub-paragraph + (2) — Simplified framework scope + documentation/review
`[scope: Art. 5–15 exemption; addressed to small/exempted entities; multi-instance within one card per Q6=a convention]`
**Source locus:** Art. 16(1) first sub-paragraph and Art. 16(2).
> Articles 5 to 15 of this Regulation shall not apply to **small and non-interconnected investment firms, payment institutions exempted pursuant to Directive (EU) 2015/2366**; institutions exempted pursuant to Directive 2013/36/EU in respect of which Member States have decided not to apply the option referred to in Article 2(4) of this Regulation; electronic money institutions exempted pursuant to Directive 2009/110/EC; and small institutions for occupational retirement provision.
>
> The ICT risk management framework referred to in paragraph 1, second subparagraph, point (a), shall be **documented and reviewed periodically and upon the occurrence of major ICT-related incidents** in compliance with supervisory instructions. It shall be **continuously improved on the basis of lessons derived from implementation and monitoring**. A report on the review of the ICT risk management framework shall be submitted to the competent authority upon its request.
**Instance 1 — POLY — S3 — five exempted entity categories + `Member States have decided not to apply the option referred to in Article 2(4)` (MS-discretion)**
Five entity categories + MS discretion. Three readings collapsed to 2: R1 (per-entity) and R2 (per-entity-type) are operationally similar; collapsed to **R1 = per-entity** and **R2 = at any time (broad MS discretion)**.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each MS decides per entity | None in OJ |
| R2 | MS decides at any time (broad MS discretion) | In-Directive: literal `decided not to apply the option` (broad) |
R2 is the literal reading. S3. `[no third reading identified]`. The five exempted entity categories (R1-R5) are operationally distinct — each defines a separate compliance population.
| Category | Cross-ref |
|---|---|
| (a) Small + non-interconnected investment firms | DORA Art. 2(1)(j) → IFR Art. 12(1) |
| (b) Payment institutions exempted | PSD2 Art. 32(1) |
| (c) CRD-exempted institutions (where MS chose not to apply Art. 2(4)) | DORA Art. 2(4) |
| (d) EMD-exempted e-money institutions | EMD Art. 9(1) |
| (e) Small IORPs | DORA-D53 |
*Berry anchor:* §3.3.1 (entity-type definitions; `decided not to apply the option`).
**Instance 2 — COORD — S3 — `documented AND reviewed` (Art. 16(2)) + `reviewed periodically AND upon the occurrence of major ICT-related incidents`**
Two governance duties + two review triggers. Three readings collapsed to 2 per operator. **Documented + reviewed**: R1 (either) vs R2 (both). **Triggers**: R1 (periodic only) vs R2 (both, cumulative).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either documented OR reviewed (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal |
| R1' | Periodic only (no event-driven) | None in OJ |
| R2' | Both triggers (periodic AND upon major ICT-related incident) | In-Directive: literal `periodically AND upon the occurrence of major ICT-related incidents` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (AND for duties; AND for triggers); §5.1 (`periodically`).
**Instance 3 — POLY — S3 — `continuously improved on the basis of lessons derived from implementation and monitoring` (Art. 16(2))**
The continuous-improvement mechanism. Three readings collapsed to 2.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either implementation OR monitoring (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal `implementation AND monitoring` |
R2 is the literal reading. S3. `[no third reading identified]`.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`continuously improved`).
**Definitional anchor:** DORA Art. 3(34) → IFR Art. 12(1); DORA-D53 `small institution for occupational retirement provision`; DORA Art. 2(4) (material scope carve-out); DORA-D10 `major ICT-related incident` (S3).
**Proportionality-status:** Art. 4 does not apply (Art. 5–15 do not apply to these entities — the simplified framework is INSTEAD).
---
#### 4.26 CL16-2 — Art. 16(1) second sub-paragraph (a)–(h) + (3) — Simplified obligations (parallel to Art. 9(4)) + ESA RTS
`[scope: simplified framework — small entities; multi-instance within one card per Q6=a convention; parallel to Art. 9(4) but at lower granularity; 8 sub-points (a)-(h) NOT split into 8 cards]`
**Source locus:** Art. 16(1) second sub-paragraph and sub-points (a)–(h) + Art. 16(3).
> Without prejudice to the first subparagraph, the entities listed in the first subparagraph shall:
>
> (a) put in place and maintain a **sound and documented ICT risk management framework** that details the mechanisms and measures aimed at a **quick, efficient and comprehensive management of ICT risk**, including for the protection of relevant physical components and infrastructures;
>
> (b) <mark>continuously monitor the security and functioning of all ICT systems</mark>;
>
> (c) <mark>minimise the impact of ICT risk</mark> through the use of sound, resilient and updated ICT systems, protocols and tools which are appropriate to support the performance of their activities and the provision of services and adequately protect availability, authenticity, integrity and confidentiality of data in the network and information systems;
>
> (d) allow <mark>sources of ICT risk and anomalies in the network and information systems to be promptly identified and detected and ICT-related incidents to be swiftly handled</mark>;
>
> (e) identify <mark>key dependencies on ICT third-party service providers</mark>;
>
> (f) ensure the continuity of critical or important functions, through <mark>business continuity plans and response and recovery measures, which include, at least, back-up and restoration measures</mark>;
>
> (g) <mark>test, on a regular basis, the plans and measures referred to in point (f), as well as the effectiveness of the controls</mark> implemented in accordance with points (a) and (c);
>
> (h) implement, as appropriate, relevant operational conclusions resulting from the tests referred to in point (g) and from post-incident analysis into the ICT risk assessment process and develop, according to needs and ICT risk profile, ICT security awareness programmes and digital operational resilience training for staff and management.
>
> 3. The ESAs shall, through the Joint Committee, in consultation with the ENISA, develop common draft regulatory technical standards in order to:
>
> (a) specify further the elements to be included in the ICT risk management framework referred to in paragraph 1, second subparagraph, point (a);
>
> (b) specify further the elements in relation to systems, protocols and tools to minimise the impact of ICT risk referred to in paragraph 1, second subparagraph, point (c), with a view to ensuring the security of networks, enabling adequate safeguards against intrusions and data misuse and preserving the availability, authenticity, integrity and confidentiality of data;
>
> (c) specify further the components of the ICT business continuity plans referred to in paragraph 1, second subparagraph, point (f);
>
> (d) specify further the rules on the testing of business continuity plans and ensure the effectiveness of the controls referred to in paragraph 1, second subparagraph, point (g) and ensure that such testing duly takes into account scenarios in which the quality of the provision of a critical or important function deteriorates to an unacceptable level or fails;
>
> (e) specify further the content and format of the report on the review of the ICT risk management framework referred to in paragraph 2.
>
> When developing those draft regulatory technical standards, the ESAs shall take into account **the size and the overall risk profile** of the financial entity, and the nature, scale and complexity of its services, activities and operations.
>
> The ESAs shall submit those draft regulatory technical standards to the Commission by **17 January 2024**.
**Instance 1 — COORD — S3 — chapeau: `quick, efficient and comprehensive management of ICT risk` (3-way AND) + sub-point (a): `put in place and maintain` (2-way AND) + `sound and documented ICT risk management framework`**
Three management qualifiers (AND) + two lifecycle phases + two framework qualifiers. Three readings collapsed to 2 per operator. **3-way**: R1 (composite) vs R2 (three discrete). **2-way put/maintain**: R1 (either) vs R2 (both). **Sound/documented**: R1 (either) vs R2 (both).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete metrics (for 3-way) | In-Directive: literal `quick, efficient AND comprehensive` |
| R2 | Composite (overall management quality) | None in OJ |
| R1' | Either put OR maintain (for 2-way) | None in OJ |
| R2' | Both required | In-Directive: literal |
| R1'' | Either sound OR documented (one suffices) | None in OJ |
| R2'' | Both qualifiers required | In-Directive: literal `sound AND documented` |
R1, R2', R2'' are the literal readings. S3. `[no third reading identified]` for all three operators.
*Berry anchor:* §5.5 (three-way coordination); §5.4.7 (AND); §5.1 (`sound`, `documented`).
**Instance 2 — POLY — S3 — sub-point (b): `continuously monitor the security and functioning of all ICT systems` + sub-point (c): `sound, resilient and updated ICT systems, protocols and tools`**
Two monitoring dimensions (AND) + three governance attributes (AND) applied to three categories. Three readings collapsed to 2 per operator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either security OR functioning (one suffices) | None in OJ |
| R2 | Both (security AND functioning) | In-Directive: literal |
| R1' | Either attribute (one suffices) | None in OJ |
| R2' | All three required | In-Directive: literal `sound, resilient AND updated` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (AND for monitoring); §5.4.7 (3-way AND for attributes); §3.3.1 (`functioning`, `resilient`).
**Instance 3 — VAG — S3 — sub-point (d): `promptly identified and detected … swiftly handled` + sub-point (f): `back-up and restoration measures`**
Two temporal qualifiers + two backup measures. Three readings collapsed to 2 per operator. **Temporal**: R1 (either) vs R2 (both). **Backup**: R1 (one suffices) vs R2 (both).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either temporal qualifier (one suffices) | None in OJ |
| R2 | Both required | In-Directive: literal `promptly AND swiftly` |
| R1' | Back-up only (restoration excluded) | None in OJ |
| R2' | Both required (back-up AND restoration) | In-Directive: literal `back-up AND restoration` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (AND); §5.1 (`promptly`, `swiftly`).
**Instance 4 — POLY — S3 — sub-point (g): `the plans and measures referred to in point (f), as well as the effectiveness of the controls` (3-way AND) + sub-point (h): three categories of follow-on action**
Three test dimensions (AND) + three categories of follow-on. Three readings collapsed to 2 per operator. **Test**: R1 (each independent) vs R2 (all three required). **Follow-on**: R1 (each independent) vs R2 (all three required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each dimension is independent | None in OJ |
| R2 | All three required | In-Directive: literal `plans AND measures AND effectiveness of controls` |
| R1' | Each follow-on category is independent | None in OJ |
| R2' | All three required | In-Directive: literal three-way enumeration |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (3-way AND).
**Instance 5 — POLY — S3 — five RTS subject areas (sub-points a–e, Art. 16(3)) + `duly takes into account scenarios in which the quality of the provision of a critical or important function deteriorates to an unacceptable level or fails`**
Five RTS subjects + scenario test. Three readings collapsed to 2 per operator. **RTS**: R1 (each independent) vs R2 (joint). **Scenario**: R1 (only decline) vs R2 (decline or fail).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Each RTS subject is independent | None in OJ |
| R2 | Single joint RTS covering all five | In-Directive: literal `common draft regulatory technical standards` |
| R1' | Only decline scenarios (excludes failure) | None in OJ |
| R2' | Decline or failure (OR) | In-Directive: literal `deteriorates to an unacceptable level or fails` |
R2 and R2' are the literal readings. S3. `[no third reading identified]` for both.
*Berry anchor:* §5.4.7 (5-way coordination); §3.3.1 (`common`, `deteriorates to an unacceptable level`).
**Layer 1 observation — Art. 16 simplified framework is structurally parallel to Art. 9(4) hinge but at lower operational granularity.** The simplification is **substantive, not nominal**: the simplified framework omits access control (9(4)(c)), change management (9(4)(e)), and patches (9(4)(f)) as **standalone control families**. Some of these are absorbed into sub-points (a), (c), and (g) (e.g. data protection under (c) implies some security controls), but the **structural alignment is incomplete**. This is a deliberate regulatory choice: small entities are exempted from the most operationally demanding controls. **Layer 2 must adjudicate whether the simplification is proportional to the risk profile of exempted entities or whether it introduces a security gap.**
---
### 5. T3-vs-text gaps
This section catalogues **inconsistencies between the v0.1 T3 mapping** (T3 clauses **C14**, **C15**, **C16**, **C17**, **C26**, **C27**, **C28**) and the OJ text. Per pilot convention, T3-vs-text gaps are flagged separately from linguistic ambiguities of the regulation (they are inconsistencies of the mapping layer, not of the text). **Every gap below is a T3-imposed mapping artefact, not an OJ-text artefact.**
#### 5.1 T3 coverage check
| T3 clause | OJ locus | v0.2 mapping | Gap |
|---|---|---|---|
| **C14** | Art. 9(4)(c) | CL9-4 Instance 6 | **Major distortion** (§5.2.1). |
| **C15** | Art. 9(4)(a), (e), (f) | CL9-4 Instances 1, 10-15 | v0.2 restores single hinge card. |
| **C16** | Art. 9(4)(d) | CL9-4 Instance 8 | **Major distortion** (§5.2.2). |
| **C17** | Art. 9(4)(b), (c), (d) | CL9-4 Instances 2-9 | Single-hinge-card pattern. |
| **C26** | Art. 9(4)(f) [correct] / Art. 13(6) [mis-mapped] | CL9-4 Instances 14-15 + CL13-2 Instance 3 | **Mis-mapping** (§5.2.3). |
| **C27** | Art. 13(2) | CL13-1 Instance 2 | No major gap. |
| **C28** | Art. 13(6) | CL13-2 Instance 3 | **Major distortion** (§5.2.4). |
| **— (NEW)** | Art. 7-12, 14, 15, 16 | CL7-1 … CL16-2 | T3 omitted 19 clauses; v0.2 adds them. |
#### 5.2 Major T3 distortion gaps (with OJ-text rebuttals)
#### 4.26 CL20-1 — Art. 20 — ESAs RTS/ITS mandate (whole article)
**Source locus:** Art. 20, in its entirety.
> The ESAs, through the Joint Committee, and in consultation with ENISA and the ECB, shall develop:
>
> (a) common draft regulatory technical standards in order to:
>
> (i) establish the content of the reports for major ICT-related incidents in order to reflect the criteria laid down in Article 18(1) and incorporate further elements, such as details for establishing the relevance of the reporting for other Member States and whether it constitutes a major operational or security payment-related incident or not;
>
> (ii) determine the time limits for the initial notification and for each report referred to in Article 19(4);
>
> (iii) establish the content of the notification for significant cyber threats.
>
> When developing those draft regulatory technical standards, the ESAs shall take into account the **size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations**, and in particular, with a view to ensuring that, for the purposes of this paragraph, point (a), point (ii), different time limits may reflect, as appropriate, specificities of financial sectors, without prejudice to maintaining a consistent approach to ICT-related incident reporting pursuant to this Regulation and to Directive (EU) 2022/2555. The ESAs shall, as applicable, provide justification when deviating from the approaches taken in the context of that Directive;
>
> (b) common draft implementing technical standards in order to establish the standard forms, templates and procedures for financial entities to report a major ICT-related incident and to notify a significant cyber threat.
>
> The ESAs shall submit the common draft regulatory technical standards referred to in the first paragraph, point (a), and the common draft implementing technical standards referred to in the first paragraph, point (b), to the Commission by **17 July 2024**.
**Instance 1 — VAG — S3 — `size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations`**
A four-factor proportionality formulation (size + risk profile + nature + scale + complexity, 5 adjectives actually). Same Berry pattern as Art. 4(2) chapeau. S3 (each factor admits S2 reading; the combination rule is itself undefined).
*Berry anchor:* §5.4.7 (5-way AND); §3.3.1 (`size`, `risk profile`, `nature, scale and complexity`); cf. DORA Art. 4(2).
**Instance 2 — VAG — S3 — `specificities of financial sectors`**
`specificities` undefined. Three readings:
- **R1:** Sectoral (banking vs. insurance vs. securities).
- **R2:** Sub-sectoral (retail banking vs. investment banking).
- **R3:** Business-model-specific.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sectoral | None in OJ |
| R2 | Sub-sectoral | In-Directive: recital 56 |
| R3 | Business-model | None in OJ |
S3.
*Berry anchor:* §5.1 (`specificities`); §3.3.1 (`financial sectors`).
**Instance 3 — VAG — S3 — `consistent approach … pursuant to this Regulation and to Directive (EU) 2022/2555`**
*Berry anchor:* §3.3.1 (`consistent approach`).
**Instance 4 — POLY — S2 — `standard forms, templates and procedures`**
Three operational artefacts (AND). S2.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`forms`, `templates`, `procedures`).
**Definitional anchor:** DORA-D10; DORA-D13.
**RTS-pending:** **YES — Art. 20 is the pure RTS+ITS delegation of Ch. III.** Both deadlines = 17 July 2024.
| Sub-act | Status (mid-2025) |
|---|---|
| RTS under (a)(i) (report content) | **Adopted** as Implementing Regulation (EU) 2024/2956 Annex II–IV. |
| RTS under (a)(ii) (time limits) | Per-sector time limits laid down in Reg. (EU) 2024/2956 Annex II. |
| RTS under (a)(iii) (cyber-threat notification content) | **Adopted** in Reg. (EU) 2024/2956 Annex III. |
| ITS under (b) (standard forms, templates, procedures) | **Adopted** in Reg. (EU) 2024/2956 Annex IV. |
Net: as of mid-2025, **the Art. 20 mandates are substantially implemented via Reg. (EU) 2024/2956** but Layer 1 catalogues the RTS-pending character because OJ Art. 20 is, by its own terms, an RTS delegation.
**Proportionality-status:** Art. 4 applies (explicit cross-reference).
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

> **Source.** OJ L 333, 27.12.2022, p. 31–39. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **1791–2272**.
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor: DORA Art. 3(2) → NIS 2 Art. 6(1)`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 15` (where applicable).
>
> **Chapter II Section II is the operational heart of DORA.** Art. 7–9 establish the *Identify–Protect–Detect* baseline (NIST CSF mapping). Art. 10–11 establish *Detect–Respond*. Art. 12 establishes *Recover* (backup). Art. 13 closes the loop with *Learn–Evolve*. Art. 14 mandates crisis communication. Art. 15 is the meta-procedural RTS mandate to ESAs further specifying Art. 9–11. Art. 16 is the **simplified framework for exempted entities** (small investment firms, exempted payment institutions, exempted e-money institutions, small IORPs) — structurally parallel to Art. 9(4) but lowered in operational granularity.
>
> **Articles in this file:** 10 articles (Art. 7–16), ~50 operative paragraphs, **26 atomic clauses** (CL7-1 … CL16-2). Compacted from v0.2-pre (34 clauses) per user direction: D1=compact heavily, D5=entity-facing + Q1=software architecture + reporting deadlines, D3=Layer 1 only (no Layer 2 normative force introduced). Variant readings consolidated to 2 where 2 of 3 readings converged to materially similar compliance practice.

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in Ch. II Sec. II inherits from **DORA Art. 3(2) → NIS 2 Art. 6(1)** (`network and information system`). Clauses hinging on `critical or important function` inherit from **DORA-D22** (the tautological definition flagged at pilot file §2.7; **S3 regress**).

### from regs/DORA.ambiguity.md

The appropriateness qualifier. Same pattern as CRA Annex I Part I (1) chapeau `appropriate`. R3 (sectoral calibration per ESA guidance) consolidated: `[no third reading identified]` — sectoral calibration is captured via Art. 15(a) RTS, not via an independent reading.

### from regs/DORA.ambiguity.md

Quantitative threshold combined with temporal qualifier (`timely`) and stress qualifier (`peak … as needed`). Same Berry pattern as CRA-CL129 (`appropriate`).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system` (covers `ICT systems`; `protocols` and `tools` are open-ended).
**Proportionality-status:** Art. 4 applies (explicit reference in sub-point (a)).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(7) `ICT asset`; DORA Art. 3(6) `information asset`; DORA Art. 3(5) `ICT risk` (DORA-D05, S3 — `reasonably identifiable`); DORA Art. 3(12) `cyber threat` (CSA Art. 2(8) cross-ref); DORA Art. 3(16) `vulnerability` (NIS 2 Art. 6(15) cross-ref).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

Same Berry pattern as CRA Annex I chapeau + DORA-D21 `ICT services` definitional scope. Three categories (AND):

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D21 `ICT services` (S2).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

Four data-security dimensions (OR — inherits Art. 3(4) NIS 2 cross-ref + DORA-D08); three data states (OR).

### from regs/DORA.ambiguity.md

Four categories coordinated. Same pattern as CRA Annex I chapeau (4 elements). Three readings collapsed to 2.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA-D22 `critical or important function` (S3 regress); DORA-D08 `ICT-related incident` (S3 regress); DORA Art. 3(4) NIS 2 Art. 6(2) cross-ref.
**RTS-pending:** Art. 15(a) explicitly specifies further elements to be included in the ICT security policies, procedures, protocols and tools referred to in Art. 9(2).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**Proportionality-status:** Art. 4 applies (explicit reference in chapeau).

### from regs/DORA.ambiguity.md

R1 is the literal reading. S3 (NIS 2 Art. 6(2) D02 analogue propagates). `[no third reading identified]` — original R2 (any one suffices) is operationally below the literal threshold.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1); DORA-D22 `critical or important function` (S3 regress); DORA-D08 `ICT-related incident` (S3 regress).
**RTS-pending:** Art. 15(b) explicitly specifies further components of access management rights referred to in Art. 9(4)(c). Art. 15(a) covers the Art. 9(2) chapeau.
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(8) `ICT-related incident` (DORA-D08, S3); DORA Art. 3(17) NIS 2 Art. 6(6) `incident` cross-ref.
**RTS-pending:** Art. 15(c) specifies further the Art. 10(1) detection mechanisms.
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

Same Berry-flagged vague quantitative term as Art. 10(1), CL24-3, CL27-1, CL27-2, CRA-CL129. Three readings collapsed to 2: R1 (quantified) and R2 (qualitative) are operationally distinct; R3 (risk-based) is captured via Art. 4.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**RTS-pending:** Art. 15(c) explicitly covers the Art. 10(2) criteria triggering ICT-related incident detection/response processes.
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

`effectively` — same Berry-flagged qualifier as CL24-4 `effective risk-mgmt controls`, CRA-CL129 `effective`. Three readings collapsed to 2.

### from regs/DORA.ambiguity.md

`comprehensive` — same Berry qualifier as DORA-D01 `digital operational resilience` + CRA Annex I. Three readings collapsed to 2: R1 (exhaustive) and R2 (standard-based) operationally similar; consolidated to **R1 = exhaustive** and **R2 = risk-proportional (per Art. 4)**.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(19) `ICT third-party service provider`; DORA-D22 `critical or important function` (S3); DORA Art. 3(8) NIS 2 Art. 6(6) `incident` cross-ref.
**RTS-pending:** Art. 15(f) specifies further the components of the Art. 11(3) ICT response and recovery plans.
**Proportionality-status:** Art. 4 applies; audit-review obligation excludes microenterprises (per `in the case of financial entities other than microenterprises`).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(12) `cyber threat` (CSA Art. 2(8) cross-ref); DORA Art. 3(16) `vulnerability` (NIS 2 Art. 6(15) cross-ref); DORA-D08 `ICT-related incident` (S3); DORA-D14 `cyber-attack` (S2); DORA-D10 `major ICT-related incident` (S3); DORA-D60 `microenterprise` carve-out.
**RTS-pending:** Art. 15(g) specifies further the content and format of the report on the review of the ICT risk management framework (Art. 6(5)) — relevant to the lessons-learned reporting dimension.
**Proportionality-status:** Art. 4 applies; non-microenterprise communication carve-out (post-incident review changes).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA-D10 `major ICT-related incident` (S3); DORA-D16 `vulnerability` (NIS 2 Art. 6(15) cross-ref).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1); DORA-D22 `critical or important function` (S3); DORA Art. 3(19) `ICT third-party service provider`.
**RTS-pending:** Art. 16(3) mandates ESA RTS for the simplified framework (deadline 17 January 2024); as of mid-2025, **Reg. (EU) 2024/2956** (implementing) + Delegated Reg. (EU) 2024/1772 (delegated) jointly specify the simplified framework.
**Proportionality-status:** Art. 4 does not apply (clause IS the proportionality provision).

### from regs/DORA.ambiguity.md

`consistent approach` between DORA reporting and NIS 2 reporting (NIS 2 Art. 23; cf. NIS 2 file §3.10). S3.

<!-- aegis:purity: own_reg=DORA; demoted=25; core_cross_mentions=0 -->

