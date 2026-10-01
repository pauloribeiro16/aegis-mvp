```markdown
### D-04.3 — Regulatory Notification

**Framing (company context conditioning every goal below):**

> TinyTask Lda. is an 8-employee B2B SaaS company in Portugal (EU) developing rule-based productivity tools. It acts as GDPR controller for customer account data (names, emails, passwords) and processor for customer task data, and as CRA manufacturer of products with digital elements (SaaS + web/mobile interface, default product class, self-assessment conformity). No AI/ML systems are developed, deployed, or integrated. NIS 2, DORA, and AI Act are excluded per the fact sheet. The company operates on managed cloud hosting with individual customer logins and one external payment sub-processor.

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-04.3-001 | A personal data breach affecting customer account data or task data is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after TinyTask becomes aware of the breach, unless the breach is unlikely to result in a risk to data subjects' rights and freedoms, with the Art. 33(3) content template (nature, categories, approximate numbers, consequences, measures, DPO contact) filed. | achieve | accountability | SO-D-04.3.HL | GDPR Art. 33(1); Art. 33(3); Art. 4(12) | RS.CO-02; CM.AW-P7 | Restated for an 8-person B2B SaaS controller/processor; the `where feasible` softening and `unlikely risk` carve-out are preserved as GDPR-unique conditions per the corpus; the Art. 33(3) content template is the operative filing requirement; no mechanism or tool prescribed. |
| AG-D-04.3-002 | An actively-exploited vulnerability or severe incident in TinyTask's SaaS product with digital elements is notified to the designated CSIRT and ENISA on the three-tier temporal pattern — early warning within 24 hours, vulnerability or incident notification within 72 hours with progressive disclosure content, and final report within 14 days (AEV) or 1 month (SI) — with the Art. 15 coordinated vulnerability disclosure process operating in parallel without replacing the Art. 14 tiers. | achieve | accountability | SO-D-04.3.HL | CRA Art. 14(1); Art. 14(2)(a); Art. 14(2)(b); Art. 14(2)(c); Art. 14(3); Art. 14(4) | RS.MA-02; RS.CO-02 | Restated for an 8-person manufacturer of default-class SaaS products; the three-tier AEV pathway (24h/72h/14d) and parallel SI pathway (24h/72h/1m) are preserved verbatim from the corpus; the Art. 15 CVD process coordinates but does not replace the Art. 14 notification tiers; no mechanism or tool prescribed. |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-04.3-001 | GDPR | RS.CO-02, RS.MA-04, RS.MA-03 | CM.AW-P7, CM.PO-P2 | — | SR-GDPR-016 |
| AG-D-04.3-002 | CRA | RS.MA-02, RS.CO-02, RS.AN-03, RS.AN-07 | — | — | SR-CRA-029; SR-CRA-030 |

## §5

> ASSUMPTION: TinyTask's processor role for customer task data triggers GDPR Art. 33(2) (processor-to-controller notification without undue delay), which is a distinct obligation from the controller→DPA notification captured in AG-D-04.3-001. The D-04.3 module's requirement set (4.3.1) addresses only the controller→DPA leg; the processor→controller leg is outside this sub-domain's scope as defined in the corpus and is not restated here.

> ASSUMPTION: The fact sheet does not state a data-scale figure. The 72-hour GDPR clock and the CRA 24h/72h/14d tiers are absolute regulatory deadlines independent of data volume; no proportional relaxation is applied or assumed.

> OPEN QUESTION: When a single event simultaneously triggers both the GDPR personal-data-breach notification (AG-D-04.3-001) and the CRA AEV/SI notification (AG-D-04.3-002) — e.g., a vulnerability in the SaaS platform that also exposes customer personal data — the corpus (cross/_interactions.md) confirms the GDPR↔CRA relationship as SAME and mandates parallel notification to both DPA and CSIRT+ENISA on their respective clocks. The corpus defers the binding-procedure principle for simultaneous multi-recipient routing to Phase 1C Doc 07. No operationalisation principle is supplied at this step.
```