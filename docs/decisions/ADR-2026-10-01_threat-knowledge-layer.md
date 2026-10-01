---
document_id: AEGIS-MVP-ADR-012
title: 'Threat knowledge layer for Phase 3 Part 2 — CWE + CAPEC core, ATT&CK consultive, ATLAS/EMB3D per case; CVE/KEV excluded'
status: 'ACCEPTED — decided by the researcher, 2026-10-01'
date: 2026-10-01
phase: 'Phase 3 Part 2, pipeline layer'
author: 'Decision: PhD researcher; formalization + record: Executor session'
---

# ADR-012 — Threat knowledge layer (Phase 3 Part 2)

> Registered decision (2026-10-01): asked which threat knowledge bases Phase 3 Part 2 should adopt, the researcher selected **CWE + CAPEC (core), MITRE ATT&CK, and MITRE ATLAS + EMB3D** — and did **not** select CVE/KEV/EPSS.

## 1. Context

- Phase 3 Part 2 (ADR-006) catalogs technical (STRIDE) and privacy (LINDDUN) threats, attack vectors and defense trees, and a risk register. Cases so far used STRIDE/LINDDUN plus, ad hoc, MITRE ATLAS and EMB3D (Case_02); there is no ingested threat-knowledge layer and no anchoring rule for threat IDs.
- Altitude discipline (R13 §2.5) bans specificity beyond the source's level in Phases 0–3 deliverables; L4/instance vocabulary is out.
- Literature (docs/pipeline/04 §4): the CVE→CWE→CAPEC→ATT&CK chain is validated as an auditable mapping step against standard KBs (NEXUS NDSS 2026; CIRCL) — mapping, not free-text generation.

## 2. Decisions

- **D1 — Adopted set.** CWE and CAPEC are the core layers (mechanism altitude — weakness categories and attack patterns); ATT&CK is a consultive layer (adversary TTPs, detection-leaning vocabulary) for defense trees; ATLAS (ML threats) and EMB3D (embedded) activate **per case**, routed by the case profile (AI/ML or embedded components present).
- **D2 — CVE/KEV/EPSS excluded.** Instance-level vulnerability records are below the design altitude of Phase 3 deliverables; risk-register likelihood stays a reasoned estimate. They may be revisited only as risk-register evidence, never as anchors, by explicit new decision.
- **D3 — Ingestion target and pattern.** `baseline/THREATS/<CATALOG>/` following the advisory-framework pattern (`_MANIFEST.json` with `advisory: true`, source URLs, fetch date; flat ID list; per-entry JSON) — the `generate_advisory_framework.py` precedent. Ingestion is a registered future increment; until it lands, no threat-ID citations appear in deliverables.
- **D4 — Only-cite-what-resolves.** A cited threat ID must resolve to a JSON under `baseline/THREATS/`; unresolvable → dropped or `—`, never `?` (R12 discipline). Guard T8 (threat-ID resolution) joins `check_traceability.py` when ingestion lands.
- **D5 — Mapping pass, not generation.** Threat → CWE → CAPEC (→ ATT&CK) enrichment is a dedicated step (PROM-P3B-05) with explicit ledger columns (`cwe_id`, `capec_id`, `attack_id`); IDs are matched against the local store, never generated.
- **D6 — Scope.** K3 feeds Part 2 artifacts only; it never anchors Part 1 requirements (R8 analog).

## 3. Alternatives considered

- **Full MITRE stack including CVE/KEV** — rejected: instance-level records would drag L4/instance vocabulary into design deliverables and imply a vulnerability-management cadence the methodology does not have.
- **Status quo (ad hoc citations per case)** — rejected: unresolvable anchors and non-uniform threat vocabulary across cases; T6 debt showed the cost of anchor provenance without a local store.

## 4. Consequences

- **C1:** docs/pipeline/02 §5 is the policy of record; the ingestion increment implements it.
- **C2:** Part 2 fichas (PROM-P3B-*) cite threat IDs only after ingestion lands; until then they cite STRIDE/LINDDUN categories as today.
- **C3:** advisory status (R2b pattern) — citing K3 entries is agent discretion, never an obligation source.

## 5. Ratification checklist (P7)

1. D1/D2 (adopted set; CVE/KEV/EPSS excluded) — **decided by researcher** (2026-10-01).
2. D3–D5 (ingestion pattern, T8, mapping pass) — confirm: ______
