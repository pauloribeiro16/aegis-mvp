---
ficha_id: PROM-P3B-01
title: 'Decompose the approved system into assets, flows and trust boundaries'
phase_step: 'Phase 3 Part 2 · Etapa 2.1 — System decomposition (onda D)'
pattern: 'one structured call over the approved Part 1 package'
version: 1.1.0
created: 2026-10-27
status: ACTIVE
body_is_instruction: true
normative_source:
  - 'ADR-006 (Part 2 is gated by the Part 1 exit gate)'
  - 'ADR-012 (the threat knowledge layer)'
---

# PROM-P3B-01 — Decompose the approved system into assets, flows and trust boundaries

## Metadata

| Field | Content |
|---|---|
| Role | Threat modelling analyst |
| Mission | Extract the attack target from what Part 1 SPECIFIED: assets (`AST-nn`), data flows (`DF-nn`), trust boundaries (`TB-nn`), and the allocation of every accepted requirement to what it protects |
| Inputs | Doc01–Doc03 (V2), the accepted constraints, the fact sheet |
| Output | Four `####` tables — Assets, Data flows, Trust boundaries, Control allocation |
| Failure mode | Inventing a component no document names (R6); a requirement allocated to nothing; a flow that crosses an undeclared boundary |

## Output schema

```markdown
#### Assets
| ID | Asset | Kind | Sensitivity | Rationale |
|---|---|---|---|---|
| `AST-01` | Customer account credentials | credential store | high | named in Doc01 R1.2 dependencies |

#### Data flows
| ID | Source | Destination | Assets carried | Trust boundary |
|---|---|---|---|---|
| `DF-01` | Business Customer | Web application | `AST-01`, `AST-03` | `TB-01` |

#### Trust boundaries
| ID | Boundary | Privilege change | Controls at the crossing | Rationale |
|---|---|---|---|---|
| `TB-01` | Public client ↔ application | anonymous → authenticated | Doc01 R1.1, R1.3 | the Internet crossing the intake describes |

#### Control allocation
| Control | Protects |
|---|---|
| `SO-D-01.1-001` | `DF-01`, `TB-01` |
```

## Rules the output must obey

1. **Zero invention (R6).** Every asset, flow and boundary traces to the fact
   sheet or the Part 1 deliverables. If the hosting is unclear, the boundary
   says so — it does not guess a data centre.
2. **Total allocation.** Every accepted requirement id (objective ids,
   principle ids, `ORG-D-XX.Y-NNN`) appears in Control allocation at least once.
3. **Flows name real crossings.** A flow carries only declared assets and
   crosses only declared boundaries.
4. **Sensitivity is an honest label** (high / personal / operational / low),
   not an adjective festival.

## Self-checks (L2)

- Could a red-teamer pick a target from the Assets table alone?
- Does every privilege CHANGE sit on a declared boundary?
- Is any accepted requirement protecting nothing?

## Human gate

Part 2's golden rule: the model computes and proposes; ONLY A PERSON signs
`steps/phase3b/risk_verdicts.json` (G-P3-B). Nothing here accepts a risk.

## Technology neutrality (R5) — write the second column

| Do not write | Write |
|---|---|
| *TLS 1.3, HTTPS, SSH* | authenticated and encrypted end-to-end communication channel |
| *AWS S3, Azure Blob* | External Object Storage Service |
| *Stripe, PayPal* | External Payment Gateway |
| *JWT, session cookies* | cryptographically signed, time-bound session authentication token |
| *PostgreSQL, MongoDB* | Internal Application Database |
| *MFA, 2FA* | a second, independent verification factor at authentication |

Name the property and the component's ROLE, never the product or protocol.

## Changelog

- 1.1.0 (2026-10-28) — the ficha's body sections now reach the model (`body_is_instruction: true`): the parser was sending the prompt body alone, which dropped the five verdicts, the Action coupling rule, the R5 mapping table and the `RN (a derivar)` vocabulary from every Phase 3 call.
- 1.0.0 (2026-10-27): created for Onda D (Part 2 construction, ADR-012 + the
  2026-10-27 catalog ratification: CWE+CAPEC core; ATT&CK/D3FEND/ATLAS/EMB3D
  consultive; 3315 ids ingested from the local KG catalogs).
