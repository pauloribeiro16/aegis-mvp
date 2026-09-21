# D-04.3 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 23(4)(b) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 72 hours of becoming aware of the significant incident, an incident notification which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise (OJ L 333, 27.12.2022, p. 129).

**CRA article (verbatim):**
> Art. 14(2)(b) requires the manufacturer to submit, unless the relevant information has already been provided, a vulnerability notification without undue delay and in any event within 72 hours of becoming aware of the actively exploited vulnerability, providing general information about the product, the nature of the exploit and vulnerability, the corrective or mitigating measures taken, and the actions users can take. Art. 14(2)(c) requires a final report no later than 14 days after a corrective or mitigating measure is available, including a description of the vulnerability (severity, impact), information on the malicious actor where available, and details of the security update or other corrective measures.

**Scope comparison:**
- NIS2 scope: entity-level significant incidents.
- CRA scope: manufacturer-level actively exploited vulnerabilities and severe product incidents.
- Scope overlap: Conditional, usually actor-split unless the NIS2 entity is also the manufacturer or the product incident creates a NIS2 significant incident for the same party.

**Trigger comparison:**
- NIS2 trigger: significant incident under Art. 23(3).
- CRA trigger: actively exploited vulnerability or severe incident under Art. 14.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: 24h early warning, 72h incident notification, 1-month final report.
- CRA: AEV 24h/72h/14d; severe incident 24h/72h/1m.
- Tension: NONE for severe-incident timeline alignment; GENUINE for AEV final-report 14-day tightening if the same party/event overlaps.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- CRA: CSIRT designated as coordinator and ENISA through the single reporting platform.

**Content template comparison:**
- NIS2: severity, impact, indicators of compromise, root cause and mitigation.
- CRA: affected product, exploit/vulnerability, corrective or mitigating measures, user actions and final remediation details.

**Classified relationship (from CRDA):** EQUAL

**Verified relationship (after OJ-text analysis):** CORRECTED — COMPLEMENTARY, not EQUAL

**Reasoning (1-2 paragraphs):** The OJ-derived timelines share a 24h/72h progressive-reporting structure, but equality is too strong. CRA has two tracks, and the AEV final report is 14 days after a corrective or mitigating measure is available, while NIS2 uses a 1-month final report from the 72h incident notification. The content templates and actors also differ.

The correct reading is complementary with partial alignment. For severe incidents, the timing is close; for AEVs, CRA is stricter at the final-report tier. The pair should not be collapsed into an equal obligation.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: an unconditional equality or contradiction is scope-incorrect; the baseline is actor-split unless same-party facts exist.

**Downstream implication (1-2 sentences):** Doc 07 should expose two product/entity columns and apply the stricter CRA 14-day AEV final tier where AEV facts are present.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-010–013, Art. 23(4)(a)–(e)) | 24h early warning + 72h incident + 1m final + ongoing progress + closing final |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-010, SR-NIS2-011, SR-NIS2-012, SR-NIS2-013 |
| **CRA** (SR-CRA-029–033 + SR-CRA-040, Art. 14(2)–(4) + Art. 16(2)) | AEV: 24h/72h/14d; SI: 24h/72h/1m; CSIRT dissemination via single platform |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-029, SR-CRA-030, SR-CRA-031, SR-CRA-032, SR-CRA-033, SR-CRA-040 |

**Why equal (with structural differences)**: Both NIS2 and CRA use a 24h/72h tiered structure with progressive content enrichment; both notify to CSIRT. Differences: (1) CRA's AEV final tier is 14d vs NIS2's 1m; (2) CRA's severe-incident tier is 1m final, matching NIS2; (3) CRA introduces two parallel tracks (AEV vs severe incident), while NIS2 has one track. The 14d AEV final is CRA-specific and shorter than NIS2's 1m. Phase 2 should treat CRA's 14d AEV final as the binding deadline for AEV-class events (stricter than NIS2's 1m).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

