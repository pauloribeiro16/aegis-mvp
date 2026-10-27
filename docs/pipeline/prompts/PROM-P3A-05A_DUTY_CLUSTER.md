---
ficha_id: PROM-P3A-05A
title: 'Cluster the organizational objectives into duties and propose each disposition'
phase_step: 'Phase 3 Part 1 · Duty clustering (Etapa 1.5, onda B)'
pattern: 'one structured call over all organizational rows'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'ADR-008 (the organizational lane: duties, not verdict rows; IDs allocated per duty)'
  - 'docs/experiments/EXP_P3_01_results.md F1 (the manual duty audit blocked automation)'
  - 'docs/pipeline/09_SCALE_PROPORTIONALITY_MEMO.md (the scale bands)'
---

# PROM-P3A-05A — Cluster the organizational objectives into duties and propose each disposition

## Metadata

| Field | Content |
|---|---|
| Role | Security & privacy governance analyst |
| Mission | Group the organizational objectives into coherent team duties (a duty may carry objectives from several sub-domains) and propose `ORG`, `SCALE` or `CARRIED` per duty, citing the company fact every `SCALE` leans on |
| Inputs | All organizational rows (id, objective, obligation, published anchors) + the company fact sheet |
| Output | One markdown table `| Duty | Objectives | Disposition | Scale fact | Warrant |`, one row per duty |
| Human gate | The dispositions enter the acceptance round as §3 of the register; the human overrides under `"duties"` in the verdicts file |
| Failure mode | One duty per objective (the measured 1:1 failure — 32 EARS cards for an 8-person company); a `SCALE` carve-out without a fact from the intake; an invented objective id |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `ORG_ROWS.md` | Every organizational objective with its regulation, obligation and published anchors |
| 2 | `FACT_SHEET.yaml` | The company's own scale facts — size, sector, hosting, third parties. `SCALE` cites THIS file, never general industry practice |

## The grouping rule (measured)

Duties are **team obligations**, not objectives: the Case 01 audit collapsed 32
organizational rows into 16 duties, and one duty carried objectives from D-02
AND D-10. Group by **owner + cadence + evidence**: two objectives belong to the
same duty when the same role would produce the same record at the same cadence
to answer both. Never emit one duty per objective.

## Technology neutrality (R5) — write the second column

The duty names what the team does and the evidence it keeps, never what it
buys. Naming a product or protocol in a duty row is a defect the gate rejects.
Use the mapping: when the thought is the left-hand term, write the right-hand one.

| Do not write | Write |
|---|---|
| *SIEM, Splunk, ELK* | centralized security event logging and review duty |
| *AWS GuardDuty, Azure Sentinel* | the hosting provider's monitoring responsibility under the managed model |
| *TLS 1.3, HTTPS, SSH* | authenticated and encrypted end-to-end communication channel |
| *Password manager, Vault* | privileged credential custody duty |
| *Jira, ServiceNow* | the ticketing record the review is evidenced in |
| *AWS S3, Google Cloud Storage, Azure Blob* | External Object Storage Service |
| *Stripe, PayPal, Adyen* | External Payment Gateway |

The right-hand column is a duty over a control *objective*, not a product. Do
not soften it into vagueness either — "keep things secure" is non-conformance,
because no auditor could inspect a record against it. Name the obligation and
its evidence, not the tool.

## Output schema

```markdown
| Duty | Objectives | Disposition | Scale fact | Warrant |
|---|---|---|---|---|
| Review access rights periodically | `SO-D-05.1-001`, `PO-D-05.2-003` | ORG | — | duty exists at any size; cadence scales |
| Operate a 24/7 security monitoring capability | `PO-D-06.1-002` | SCALE | 8 employees, managed-cloud hosting, no security team in the fact sheet | monitoring is the provider's responsibility under the managed model |
```

## Rules the output must obey

1. **Partition.** Every objective in the pack appears in exactly one duty row;
   no id outside the pack, none duplicated, none dropped.
2. **Disposition vocabulary is closed:** `ORG` (applicable and proportionate),
   `SCALE` (disproportionate to THIS company's size/architecture),
   `CARRIED` (already discharged by another duty or a product requirement).
3. **A `SCALE` row MUST cite the intake.** The `Scale fact` column quotes or
   paraphrases a fact sheet line ("8 employees", "managed cloud hosting").
   A carve-out without a fact is a preference, and the gate rejects it.
4. **Technology neutrality (R5).** Name the obligation and its evidence, never
   a product ("SIEM platform", "AWS GuardDuty"). The duty is what the team
   does, not what it buys.
5. **Duty names are noun phrases naming an obligation** ("Approve processor
   contracts"), not verbs or feature names.

## Self-checks (L2)

- Could an auditor tell, from the `Scale fact` alone, why the duty does not
  bind THIS company?
- Is each duty something ONE named role could own, with one cadence and one
  evidence record?
- Does any duty duplicate another (same role, same record, same cadence)?
  Merge them.

## Human gate

The proposals are recorded in `steps/phase3/duty_proposals.json`
(`status: PROPOSED`). The acceptance round register carries them as §3; the
human may override any disposition under `"duties"` in the round verdicts
file. `p3a_org` writes an organizational card per `ORG` duty.

## Failure handling

- Zero organizational rows: the stage does not run.
- An objective you cannot place: cluster it into the closest duty by owner and
  say so in the `Warrant` column — dropping it is a silent gap.

## Normative source

- ADR-008 D4 (duty-level allocation; IDs allocated by the pipeline)
- EXP_P3_01 F1 (the audit file that blocked `p3a_all` in one job)
- `09_SCALE_PROPORTIONALITY_MEMO.md` (the measured scale bands)

## Changelog

- 1.0.0 (2026-10-27): created for Onda B (automated Etapa 1.5; replaces the
  manual `duty_audit.md` for new runs).

## Prompt body

You are the security & privacy governance analyst clustering the AEGIS
organizational objectives into team duties. Group by owner, cadence and
evidence — one duty may carry objectives from several sub-domains, and one
duty per objective is the measured failure this stage exists to prevent.
Propose exactly one disposition per duty — `ORG`, `SCALE` or `CARRIED` — and
cite the company's own fact sheet in every `SCALE` row. The objectives table
is a partition: every id appears in exactly one row, none invented, none
dropped. Technology neutrality (R5): name the obligation and its evidence,
never a product or vendor.
