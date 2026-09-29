# Sufficiency Assessment — Phase 3 v2 (TinyTask SaaS): does the accepted baseline suffice for compliance and security?

> **Question:** with Round 1 converged and the deliverables at 4.0.0 (`Doc01`/`Doc02`), does the Phase 3 output already suffice — in compliance and in security — or does something remain open?
> **Basis:** `../Doc01`/`../Doc02` (v2) · [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (62/62 objectives placed) · [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) (7/7 principles bound) · [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) (13/13 accepts + Step-4 control selections) · [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md) (ADR-007 discharge re-audit — record corrections; P1–P4 pending) · Phase 2 spine (`02_PHASE2_RULES/Doc01`: 28 GDPR rows / 34 CRA rows).
> **Role:** per ADR-005 this assessment also feeds the **Phase 4 trigger decision** (formal threat analysis over the accepted baseline).

---

## §1 Compliance sufficiency (per regulation)

| Regulation | Obligation rows | Functional carrier (v2) | Organizational lane (recorded decision) | Design guidance | N/A (inapplicable to SaaS) |
|---|---|---|---|---|---|
| GDPR | 28 | **10** | 17 | 1 | 0 |
| CRA | 34 | **15** | 15 | 1 | 3 |
| **Total** | **62** | **25** | **32** | **2** | **3** |

**Reading.**

1. **Zero product-lane gaps.** Every obligation that binds on the *product* (the technology lane Phase 3 operates, ADR-002) carries a chain-complete carrier: `article → Phase 2 objective → requirement card / use case → selected control anchor`. After the Round 2 discharge re-audit (ADR-007) the matrix verdicts **6 fully covered / 19 partially covered** — every partial row naming its carried legs, the discharging fit criteria, and the explicit carve-out route — with zero silent objectives: 62/62 explicitly placed. Improvement proposals P1–P4 are pending client verdicts in [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md); the accepted constraint set is unchanged.
2. **The 32 organizational rows are not specification gaps.** They bind on process/organization (breach notification 72 h GDPR / 24 h CRA, DPIA, Art. 30 records, vulnerability management / SBOM / coordinated disclosure, Art. 28 processor contracts, DPO awareness & training, technical documentation & conformity) — including `PO-D-09.4-001`, re-verdicted in Round 2 (the Art. 30 register is documentary; RN26 remains a supporting privacy event trail). They are recorded decisions (`No functional carrier (organizational)`), remain obligations of the company, and have owners assigned in Phase 2 `Doc01` §13; they form the input repertoire of `part1_security_privacy/Doc03_Organizational_Requirements.md` (ADR-008). Total compliance is **conditional on operating the process lane** — now with a designated derived deliverable.
3. **3 N/A rows** (economic-operator distribution duties, series-production conformity, integration information for integrating products) are inapplicable to an 8-person B2B SaaS micro-enterprise — recorded, not deferred.
4. **2 design-guidance rows** (D-01.3 key/custody separation, both regulations): realized at design time; carried into Phase 4/design context per the mapping.
5. **One SHOULD stands out:** RN29 (secure-use instructions) is the only accepted carrier not at MUST; if not delivered, it becomes a recorded compliance residual (CRA Annex II §8).

**Compliance verdict:** the v2 baseline is **sufficient as the technical-compliance specification** for the MVP lane — traceable article-by-article for GDPR and CRA, proportionate to scale (R3). It is **not, by itself, total compliance**: the organizational lane (31 rows) must be operated, and that is a company/process responsibility, not missing specification.

---

## §2 Security sufficiency

**Selected control surface (post-Round 1, all copied from pre-verified surfaces):**

- **NIST CSF 2.0 — 18 distinct subcategories across 4 of 6 functions:**
  - *Govern:* GV.OC-03
  - *Identify:* ID.AM-03, ID.AM-08
  - *Protect:* PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-10, PR.PS-01, PR.PS-02, PR.PS-06, PR.IR-01
  - *Detect:* DE.CM-01, DE.CM-09
  - *Respond / Recover:* no product-level anchors — the functional recoverability slice is carried by RN2/RN5 (quality attributes); incident response belongs to the organizational lane.
- **NIST Privacy Framework — 8 anchors, GDPR-derived only:** CT.DP-P2, CT.DM-P1, CT.DM-P3, CM.AW-P2, CM.PO-P2, PR.DS-P1, PR.DS-P2, PR.AC-P6.
- **Chain integrity:** every anchor belongs to the published control set of the objective it cites (Round-0 recalibration + Round-1 realignment); no invented anchors.
- **Principles 7/7 bound; analysis skills 7/7 in use** across the coverage matrix.
- **Residual risks from verdicts: zero.** Round 1 closed with 13 accepts and no rejections — there are no explicit risk-acceptance entries; nothing was silently dropped (the organizational lane is a lane decision, not a rejection). Round 2 (2026-09-28) applied coverage-record corrections only — no new risk acceptances; improvement proposals P1–P4 pending (baseline unchanged).

**Security verdict:** the baseline is **sufficient as a preventive/detective control specification** proportional to an 8-person micro-SaaS (tenant isolation, access control, transport/at-rest protection, auditability, secure defaults, minimization, lifecycle erasure). It is **not yet threat-validated** — no attack scenarios have been exercised against it. That is not an omission: formal threat analysis is Phase 4 by charter (ADR-005).

---

## §3 Overall verdict & Phase 4 trigger

**Does v2 suffice?**

- **As the Phase 3 deliverable (specification): YES.** Compliance-traceable (GDPR + CRA), security-complete for its lane, fully client-accepted, with zero silent objectives and discharge-verified coverage (6 fully / 19 partially covered with explicit carve-outs — ADR-007).
- **As total compliance/security assurance: NO — and not expected.** Three standing conditions: (1) the 32 organizational controls must be operated in the process lane (owners in Phase 2 §13; derived specification: `Doc03`, ADR-008); (2) RN29 is SHOULD — a deferral would be a recorded residual; (3) the accepted baseline has not been exercised under attack scenarios.

**Phase 4 trigger (ADR-005): RECOMMENDED — GO.** The trigger condition ("the accepted baseline is robust and concrete") is met: the baseline is chain-complete, control-anchored, converged with the client, and the asset/trust-boundary statements of the functional model are in place. Fase 4 — Threat Analysis (STRIDE/LINDDUN over the accepted baseline) is the correct next step and is where security sufficiency gets tested under adversarial pressure.

---

## §4 Data-quality flags (for the record)

- Phase 2 `Doc01` personal-data rows carry the operational-scope label `Patient & Staff Data` — foreign to TinyTask's domain (likely template vocabulary from another case). Decision owner: researcher; does not affect the verdicts above.
- `SO-D-05.3-002` published anchor set lists `PR.DS-10` twice in Phase 2 `Doc01`; selections cite the unique value.
- Round 2 re-audit (ADR-007): 19 of the 25 product-covered rows are partially covered with explicit organizational carve-outs; the Art. 30 register objective (`PO-D-09.4-001`) is organizational. Four improvement proposals (P1–P4) await client verdicts in [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md); none alters the accepted constraint set.
