```markdown
### D-07.2 — Secure Coding Practices

| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |
|---|---|---|---|---|---|---|---|
| AG-D-07.2-001 | The product with digital elements is designed, developed, and produced to limit its attack surfaces, including external interfaces, and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques, demonstrated through the design/development documentation and risk-assessment record | achieve | I | SO-D-07.2.HL | CRA Annex I Part I (2)(j); CRA Annex I Part I (2)(k); CRA Art. 13(1); CRA Art. 13(2) | PR.PS-01, PR.PS-02 | Restated for 8-FTE rule-based SaaS manufacturer (no AI/ML, no DORA, no AI Act); CRA participation is partial (outcome-level mandates only, no coding-standard prescription in OJ); coding-practices baseline from industry frameworks demonstrated against Annex I Part I (2)(j)+(k) via Annex VII §2/§3 records; HL SO not activated (single-regulation scope, no Conditional-Y overlap) |

## §4.1 Control Anchor Mapping

| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |
|---|---|---|---|---|---|
| AG-D-07.2-001 | CRA | PR.PS-01, PR.PS-02 | — | — | SR-CRA-067 |

## §5

> ASSUMPTION: GDPR is confirmed as an applicable regulation for TinyTask Lda. (controller/processor for EU personal data), but the D-07.2 GDPR module explicitly states "(no GDPR Sub-SO or requirements in this sub-domain)" — GDPR is process- and outcome-oriented and does not specify secure-coding practices. No GDPR-derived goal is produced for D-07.2; this is a scope-exclusion by the OJ text, not a silent drop.

> ASSUMPTION: The high-level SO (SG-D-07.2.HL) is not activated for TinyTask Lda. per the objective.md activation rule: the company has CRA applicability only (no DORA, no AI Act), so no ≥2-regulation Conditional-Y scope overlap exists on a single coding event. The CRA Sub-SO (SG-D-07.2.CRA) applies independently and is restated as AG-D-07.2-001.

> ASSUMPTION: DORA and AI Act are excluded per the fact sheet (not a financial entity; no AI/ML systems developed, deployed, or integrated). Their D-07.2 modules are not confirmed and are not restated.
```