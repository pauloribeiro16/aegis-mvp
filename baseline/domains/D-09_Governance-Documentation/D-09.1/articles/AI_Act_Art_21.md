---
document_id: AEGIS-PREPROC-AI_Act-ART-21
title: AI_Act Art. 21 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 21
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# AI_Act Art. 21

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-019
  title: "Deployer measures aligned with provider instructions for use"
  source_clauses:
    - { clause_id: AIA-C23, article_ref: "Art. 26(1) — `Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use`" }
  linked_objectives: [SO-AIACT-011]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g., recognition of phishing, social engineering, and other relevant risks)" }
  applies_to_role: [DEPLOYER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 26(1) of Regulation (EU) 2024/1689 requires deployers
    of high-risk AI systems to take appropriate technical and
    organisational measures to ensure they use the system in
    accordance with the provider's instructions for use. This
    is the deployer-side mirror of the provider's QMS
    obligation under Art. 17: the deployer cannot rely on the
    provider's design-time safeguards to discharge its own
    duty. The phrase `technical and organisational measures`
    uses the same AND/OR pattern as GDPR Art. 5(1)(f) (security
    of processing, `C04`) and as NIS 2 Art. 21(1) (C18), so
    the provider-deployer interface inherits the consolidated
    cross-regulation reading. A compliance officer at the
    deployer should treat the instructions for use as the
    binding use-case specification.
  security_rationale: |
    The Art. 26(1) deployer duty is operationalised in NIST CSF
    2.0 through **GV.PO-01 (Organisational cybersecurity policy
    established, communicated, enforced)**, **GV.OC-03 (Legal,
    regulatory, contractual requirements understood and
    managed)**, and **PR.AT-01 (User awareness and training)**,
    with supplementary alignment to **GV.RR-01 (Leadership
    accountability for cybersecurity risk)**, **GV.RR-02 (Roles,
    responsibilities, authorities, accountabilities established
    and communicated)**, and **PR.AT-03 (Senior executive
    understanding of cybersecurity roles)**. GV.PO-01 anchors
    the deployer's own organisational policy — the deployer
    cannot satisfy Art. 26(1) by merely adopting the
    provider's policy unchanged; it must have a deployer-side
    policy that maps to the provider's instructions for use.
    GV.OC-03 ensures the deployer understands and manages the
    full set of legal (Art. 26 + Art. 27), regulatory (NIS 2 +
    DORA + CRA), and contractual (Art. 26 provider-deployer
    agreement) obligations layered on top of the AI Act.
    PR.AT-01 binds the technical-and-organisational measures
    to user awareness and training, so that deployer staff
    recognise AI-specific risks (data poisoning, model
    evasion, automation bias). Supplementary GV.RR-01 and
    GV.RR-02 reinforce accountability by requiring leadership
    ownership and explicit RACI for the AI system, and
    PR.AT-03 ensures the deployer's executives understand
    their role. The combined control set yields a documented
    deployer cybersecurity policy, an obligations register,
    a training programme, an executive accountability
    statement, and a RACI matrix — the evidentiary substrate
    for the deployer to demonstrate ex post that its use of
    the high-risk AI system complied with the provider's
    instructions and with Art. 26 (deployer obligations)
    under the Art. 17 QMS + Art. 26 deployer + Art. 27
    fundamental-rights impact assessment + GDPR Art. 5(1)(f)
    + NIS 2 Art. 21 accountability chain.
  ambiguity_notes: |
    Source clause AIA-C23 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.23). `appropriate` is VAG-2 (Berry
    §5.1 — the legal-hedge vs. technical-recommendation
    distinction is material; reading chosen: R3 cumulative —
    `appropriate` is read as `proportionate to the risk`,
    not as a soft floor). The AND of `technical AND
    organisational` is COORD-2 (Berry §5.4.7 — same pattern
    as GDPR C04 and NIS 2 C18; reading chosen: R1 inclusive
    — both dimensions required, exclusive readings not
    accommodated by the OJ). Remain open: (a) whether a
    deployer can satisfy `appropriate` by adopting the
    provider's TOMs unchanged, or must adapt them to the
    deployer's own risk profile; (b) whether the deployer's
    `appropriate` threshold is a separate assessment or
    inherits the provider's `appropriate` ceiling.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

