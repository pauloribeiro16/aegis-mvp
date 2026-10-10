# Proportionality audit — the organizational lane (TinyTask SaaS)

> **Scope.** The 32 objectives the coverage matrix verdicts `No functional carrier
> (organizational)` in [`synthesis_rounds/OBJECTIVE_MAPPING.md`](../synthesis_rounds/OBJECTIVE_MAPPING.md)
> are routed, by ADR-008 D4, to an organizational requirements document that this
> case does not have. This audit establishes, per objective, whether the verdict
> survives R3 proportionality at the case's actual size — **8 employees,
> micro-enterprise, GDPR + CRA confirmed, NIS2 below threshold**.
>
> **Status.** MEASUREMENT, acted on 2026-10-10. Ten requirements were specified
> in [`Doc03_Organizational_Requirements.md`](../Doc03_Organizational_Requirements.md)
> from the dispositions below; the six SCALE duties remain unspecifed pending the
> proportionality judgement, and the two CARRIED rows close against `ORG-INT-03`.
> Every disposition is a proposal carrying a warrant — the proportionality
> judgement is the researcher's; this document is the evidence it rests on.

## 1. The problem the audit answers

The matrix's verdict block names `part1_security_privacy/Doc03_Organizational_Requirements.md`
as "the input repertoire" for these 32 objectives. **That file did not exist** when this audit was written. It now does:
`Doc03_Organizational_Requirements.md`, specified 2026-10-10 from the dispositions
in §3. The matrix's normative preamble therefore points at a
document the case does not ship, and `check_traceability.py --case Case_01`
returns 0 findings across T1–T7 — T4 checks files cited as G1–G6 *evidence*, and
this citation sits in the verdict vocabulary instead, so no gate sees it.

Two facts follow, and they are the reason a routing rule cannot be written
before this audit:

1. A 1:1 rule ("every organizational verdict becomes an ORG requirement") would
   emit **32 requirements for an 8-person company**.
2. The two cases that *did* route, SecureBorder and OmniBank, emit **2 each** —
   against 100 and 134 objectives. The same ADR-007 classification produces 52%
   organizational in one case and 2% in the others.

## 2. Disposition vocabulary

| Disposition | Meaning | Effect |
|---|---|---|
| **ORG** | The obligation holds at micro scale and needs a named owner and a written artefact | Becomes an ORG requirement as stated |
| **SCALE** | The duty holds; the *form* the objective implies is disproportionate at 8 people | Reworded to the proportional form, then routed — or absorbed into the duty it duplicates |
| **CARRIED** | Proportionality is already settled by a recorded case decision; nothing to route | Closes against that decision |

## 3. The audit

| Objective | Duty | Disposition | Warrant / proportional form |
|---|---|---|---|
| `SO-D-02.1-001` | Process: regularly test effectiveness of measures | **SCALE** | Duplicates `SO-D-10.3-001`. A standing testing programme is an enterprise artefact; the proportional form is a written annual self-review by the founders |
| `SO-D-02.1-002` | Product free of known exploitable vulnerabilities | **ORG** | CRA Annex I(2)(b); a per-release dependency check is a build step, not a committee |
| `SO-D-02.2-002` | Vulnerabilities remediated via security updates | **SCALE** | Already settled by `ORG-INT-02` — a managed pull-request workflow satisfies the duty for B2B SaaS |
| `SO-D-02.3-002` | Coordinated vulnerability disclosure policy | **ORG** | CRA Art. 13(1); a one-page policy plus a contact address |
| `SO-D-03.2-001` | Authorized persons act on documented instructions | **ORG** | Merges with `SO-D-03.3-001` — one instruction set, two article anchors |
| `SO-D-03.3-001` | Processor-side documented instructions + confidentiality | **ORG** | Art. 28(3)(b),(f); this *is* the DPA |
| `SO-D-04.1-001` | Breach detection/triage; awareness moment documented | **ORG** | Art. 33(1); the clock start is already fixed by `ORG-INT-04` |
| `SO-D-04.2-001` | Breach containment/mitigation | **ORG** | Same runbook as the row above; merges |
| `SO-D-04.2-002` | Availability of essential functions after incident | **SCALE** | A standing resilience capability implies redundancy posture out of proportion at 8 people; the proportional form is managed-platform redundancy plus the RPO already carried by `RN5` |
| `SO-D-04.3-001` | Breach notified to the supervisory authority (72 h) | **ORG** | Art. 33(3); the duty is not scale-dependent |
| `SO-D-04.3-002` | Actively-exploited vulnerability notified | **ORG** | CRA Art. 14; same runbook, CRA reporting path |
| `SO-D-04.4-001` | Ongoing CIA + resilience of processing systems | **SCALE** | Third instance of the same duty (see `SO-D-10.1-001`); the proportional form at this scale is a managed-cloud responsibility split, per R3 |
| `SO-D-05.2-002` | Updates/advisories available across the support period | **SCALE** | Third instance of the update-distribution duty (see `SO-D-02.2-002`) |
| `SO-D-06.1-001` | Processors provide sufficient guarantees | **ORG** | Merges with `SO-D-06.3-001`; evidenced by `ORG-INT-01` |
| `SO-D-06.1-002` | Due diligence on third-party / open-source components | **ORG** | Same duty as the SBOM rows; one supply-chain requirement |
| `SO-D-06.2-002` | SBOM maintained, machine-readable | **ORG** | CRA Annex I(2)(a); a build artefact, merges with the supply-chain requirement |
| `SO-D-06.3-001` | Art. 28(3)(a)–(h) contract floor + sub-processor chain | **ORG** | Merges with `SO-D-06.1-001` |
| `SO-D-07.3-002` | Secure, timely update distribution | **SCALE** | Third instance of the update-distribution duty |
| `SO-D-08.1-001` | DPO informs and advises | **CARRIED** | `ORG-INT-03` already accepts a proportional dual-hat advisory role at MICRO scale; a DPO *function* is not what the objective needs here |
| `SO-D-08.2-001` | DPO monitors compliance, awareness, training | **CARRIED** | Same decision; the monitoring leg collapses into the founders' annual review |
| `PO-D-09.1-001` | Accountability policies implementing data-protection principles | **ORG** | Art. 5(2)/24; anticipated by `ORG-INT-03`'s own pointer to D-09.1 governance policies |
| `SO-D-09.1-002` | Product-security policies, processes, procedures | **SCALE** | A standing policy *system* is disproportionate at 8 people; the proportional form is the runbook + DPA + CVD policy already counted above |
| `PO-D-09.2-001` | DPIA before high-risk processing | **ORG** | Art. 35; a conditional duty, not a standing programme |
| `SO-D-09.2-002` | Cybersecurity risk assessment documented and updated | **SCALE** | A periodic assessment *cadence* is disproportionate; the proportional form is a written assessment owned by the founders, reviewed on change |
| `SO-D-09.3-002` | Technical documentation (general + design description) | **SCALE** | CRA Annex II; for a SaaS product the design description is the product — the proportional form is a short architecture note, not Annex II |
| `PO-D-09.4-001` | Art. 30 records of processing activities | **ORG** | A RoPA is a spreadsheet at this scale; the named carriers are `R1.2`/`R6.1` |
| `SO-D-09.4-002` | Technical documentation + conformity assessment before market | **SCALE** | Same artefact as `SO-D-09.3-002`; merges |
| `SO-D-10.1-001` | Ongoing CIA + resilience | **SCALE** | Second instance of the CIA/resilience duty |
| `SO-D-10.2-001` | Compliance records with integrity and traceability | **ORG** | Merges with the row below; the technical leg is already carried by `RN18` |
| `SO-D-10.2-002` | Technical and risk-assessment documentation preserved | **ORG** | Merges with the row above |
| `SO-D-10.3-001` | Regular testing of measures' effectiveness | **SCALE** | Second instance of the testing-of-measures duty |
| `SO-D-10.3-002` | Effective, regular product testing; reports in documentation | **SCALE** | A standing product-testing regime with written reports is an enterprise QA artefact; merges with the annual self-review |

## 4. What the audit found

**32 rows are 16 obligations.** The taxonomy organises by sub-domain and the
obligations cut across it, so the same duty appears in two or three places:

| Duty | Rows | Where |
|---|---|---|
| Update / advisory distribution | 3 | D-02.2, D-05.2, D-07.3 |
| Supply-chain due diligence + SBOM | 3 | D-02.1, D-06.1, D-06.2 |
| Breach runbook (detect → contain → notify) | 4 | D-04.1, D-04.2, D-04.3 ×2 |
| Ongoing CIA + resilience | 2 | D-04.4, D-10.1 |
| Testing of measures' effectiveness | 2 | D-02.1, D-10.3 |
| Technical documentation | 2 | D-09.3, D-09.4 |
| Processor guarantees / Art. 28 contract floor | 2 | D-06.1, D-06.3 |
| Documented instructions | 2 | D-03.2, D-03.3 |
| Policy set | 2 | D-09.1, D-09.2 |
| Risk assessment (DPIA / Art. 32) | 2 | D-09.2 |
| Records retention | 2 | D-10.2 |
| DPO advisory | 2 | D-08.1, D-08.2 |
| Availability after incident | 1 | D-04.2 |
| Product-testing reports | 1 | D-10.3 |
| Art. 30 RoPA | 1 | D-09.4 |
| CVD policy | 1 | D-02.3 |

A routing rule that counts verdicts rather than duties would triple the
requirement count on the three-row duties before writing a single EARS sentence.

**The proportional load is 15 requirements, not 32 — and 8 of the 15 are not yet
writable.** The dispositions are **17 ORG · 13 SCALE · 2 CARRIED**. Collapsed to
duties, and separating the two clusters whose rows fall on both sides of the line:

| | Requirements | Why |
|---|---|---|
| Organizational, as stated | **7** | The lane is already proportional at this scale — breach runbook, RoPA, DPA, CVD, supply chain, records retention, documented instructions |
| Straddling clusters | **2** | `PO-D-09.1-001`/`SO-D-09.1-002` (policy set) and `PO-D-09.2-001`/`SO-D-09.2-002` (risk assessment) each split one ORG row against one SCALE row, so one requirement carries both dispositions |
| Organizational, needs the SCALE rewording first | **6** | CIA/resilience, testing of measures, update distribution, availability after incident, product-testing reports, technical documentation |
| Closes with nothing to write | **1** | DPO advisory, settled by `ORG-INT-03` |

The SCALE items are the expensive half: an EARS statement with a Volere fit
criterion cannot be drafted for "regularly test the effectiveness of measures" at
this scale without first deciding what the proportional form *is* — and 6 of the
15 requirements cannot start until that decision is made per duty.

**Two of the three cases may be classifying, not disagreeing.** If SecureBorder's
2 organizational verdicts and OmniBank's 2 are correct, then Case 01's 32 reflect a
different application of the same rule rather than a different company. That is
testable — re-run this audit's dispositions against the other two matrices — and
it should be run before any pipeline encodes the classification. If the three
cases still disagree by more than ~3× after disposition, the finding is that
`realization_class` (ADR-003) is not stable across cases, and that is the result
to record, not a number to pick.

## 5. Open for the researcher

1. **The proportionality judgement is not mine.** The warrants above are
   proposals. The disposition that matters is whether a given duty is *out of
   scale* for an 8-person company, and R3 is the rule it turns on.
2. **Backfill or re-verdict.** If the dispositions hold, Case 01 needs either a
   `Doc03` with ~16 requirements or a re-verdict of the 32 rows against this
   audit. ADR-008 says no backfill by default; this audit is the evidence for
   revisiting that, not a decision to revisit it.
3. **The dangling citation.** The matrix's preamble names a file the case does
   not ship, and no gate sees it. Either the file appears or the preamble stops
   naming it.