---
document_id: AEGIS-MVP-ADR-001
title: 'What "best practice" means in AEGIS Phase 2 — grounding the good-practice layer'
status: 'PROPOSED — awaiting human ratification (P7)'
date: 2026-09-22
phase: 'Phase 2 (cross-repo: Methodology_compact + aegis-mvp future increment)'
author: 'Executor session (analysis + literature research); decision reserved to the PhD researcher'
---

# ADR-001 — What "best practice" means in AEGIS Phase 2

> **Why this document exists.** The researcher asked (2026-09-22): *"Na fase 2 da minha metodologia eu tenho as melhores práticas, mas será que faz sentido? O que são as melhores práticas de algo que ainda não sei o que vai ser para construir, em que só sei o contexto da empresa?"* This ADR records the state analysis, the literature findings, the proposed decision and **the reasoning behind it**, so the choice can be re-read and defended later (thesis-defence context). Nothing in the corpora is modified by this ADR.

---

## 1. Status

**PROPOSED** — per AEGIS design principle P7 (human final arbiter), this decision takes effect only after the researcher ratifies it. Ratification checklist in §9.

---

## 2. The question, stated precisely

Phase 1 output knows only the company context (profile, products/services, data, assumed infrastructure) and the applicable regulations. Phase 2 emits a rules catalog. One family of those rules — the "best practice" layer — feels paradoxical:

- A **best practice of a design** ("use TLS 1.3", "store keys in this KMS") cannot be asserted before the design exists. If Phase 2 contained such rules, the objection would be fatal.
- A **constraint on whatever gets designed** ("data at rest is encrypted", "releases block unresolved critical CVEs") and a **standing organizational ability** ("someone owns quarterly competence review") *can* be asserted before the design — they constrain the solution space instead of choosing inside it.

So the question decomposes into: (a) which kind of thing does the Phase 2 layer actually contain, (b) what legitimizes calling it "best", and (c) by what criterion are practices admitted when the only known input is company context?

---

## 3. Current state (evidence from the repositories)

Path shorthand: **MC** = `Methodology_compact/`, **MVP** = `aegis-mvp/`.

### 3.1 What Phase 2 is today

- Case deliverables: `MC/02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc16_Privacy_Security_Objectives.md` (31 PO/SO objectives) and `Doc18_Rules_Catalog.md` — **46 controls = 30 obligation controls (CR, MUST) + 16 best-practice controls (BPR, SHOULD)**, 26-field card schema (fields 25/26 = `realization_class` / `_secondary`, per `MC/00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.12).
- Two rule families with different provenance:
  - **Obligation rules (CR)**: chain Legal → Phase 1 (AG) → Obligation → Objective → Rule; every card cites statute articles + framework anchors. These do **not** have the "best practice of what?" problem — law binds whatever gets built.
  - **Best-practice rules (BPR)**: selected by LLM step **2C-3** (`MC/00_METHODOLOGY/diagrams/fluxdiagram/phase2/phase2c_goals_and_rules.md:190-202`) *from ISO 27001:2022 ("All cases"), NIST CSF 2.0 ("All cases"), NIST 800-53 R5 ("HIGH/MAX cases"), OWASP ASVS ("cases with web apps"), NIST SSDF ("cases with software development")*, with selection criterion *"applicable given the company's architecture, tech stack, and deployment model"*. Declared purpose: *"Best-practice rules fill coverage gaps where obligations don't reach"* (ibid., line 271).
- `realization_class {TECHNOLOGY, PROCESS, CAPABILITY}` already encodes design-independence: PROCESS and CAPABILITY rules depend only on organizational context (RUBRIC §2); a well-formed TECHNOLOGY rule is a verifiable property of the built state, not a design choice.
- The implementation posture model (`MC/00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` §2) already handles "control that does not exist yet": 3-state posture (IMPLEMENTED / PARTIAL / NOT IMPLEMENTED) with mandatory "What's Missing" notes and an anti-fabrication rule ("record any control that is not applicable **with a reason** rather than creating artificial evidence").

### 3.2 The three defects (why the discomfort is justified)

1. **"Best practice" is never defined nor grounded.** Three disconnected senses circulate: (a) a *label* for "not law" — the overlays are headed *"Camada 3 — NIST Frameworks Overlay (best practice, optional)"* (`MC/.../MAPPINGS/OVERLAYS/OVERLAY_NIST_CSF_2.0.md:3`); (b) an *interpretation variant* of the legal indeterminate "state of the art" (`MC/00_METHODOLOGY/AMBIGUITY_REGISTRY/registry.md:69-73`, variants R1/R2/R3); (c) an *operational mechanic* — "a rule is a best practice because it cites a framework" (class model `BestPracticeRule {frameworkReference, confidenceLevel}`). There is no Sources/Definition section anywhere; the catalogs are the de facto definition precisely because nothing else defines the term.
2. **Circular provenance, and availability without policy.** The overlays' declared source-of-truth is Case_02's own Phase 2 output (`OVERLAY_NIST_CSF_2.0.md:5`: `Source-of-truth: 02_CASES/Case_02_SecureBorder_Solutions/.../13_Framework_Mapping_Matrix.md`) — best practices grounded in a case that already consumed them. ISO 27001:2022 is the **first** BPR source ("All cases") yet the **frozen MC source corpus has no ISO or ENISA catalog** (7 referentials, 5 of them IDs-only). *(Update, later 2026-09-22: a parallel session committed C1–C10, materializing 11 additional **advisory** referentials under `MVP/baseline/CONTROLS/` — NIST_SP_800_53R5, NIST_SSDF, NIST_AI_SSDF, OWASP_ASVS, OWASP_SAMM, ISO_27001_2022, ISO_27701_2019, ISO_42001_2023, CIS_CONTROLS_V8, BSI_GRUNDSCHUTZ, and ENISA incl. the NIS2 Art. 21 baseline — all flagged `advisory: true, enforced_by_verify_no_loss: false`.)* This closes the **availability** gap in the MVP working corpus but not the **policy** gap: "advisory" says when a referential is *not enforced*, not *what a good practice is*, *which authority tier it occupies*, or *when a rule may be admitted from it*. The uniform NI=2 SHOULD for all 16 BPRs is attributed to a "**Bloco B policy**" (Doc18:2999, :4130) for which no defining document exists. MVP `README.md:18` still claims "**7 NIST/OWASP control referentials**" while the directory now holds 14 (C10 updated config.yaml/AGENTS.md/SPEC.md but not the README).
3. **The selection criterion presupposes the design that does not exist.** 2C-3 requires knowing *"the company's architecture, tech stack, and deployment model"* (phase2c:202). This is coherent for Case_01 (TinyTask is an **existing** 8-person company) but incoherent for the MVP scenario — bootstrapping a **new** company, where Phase 1 input is prose context only. The methodology currently works by implicitly assuming a designed system.

Note: the term "best practice" appears **zero times** in MVP's SPEC.md / AGENTS.md / README body prose — the MVP has not yet imported the problem. The decision is therefore timely: it defines the Phase 1 → Phase 2 contract **before** the MVP Phase 2 increment is built.

---

## 4. Literature findings (what "best practice" can honestly mean)

### 4.1 Evidence-based software engineering: "best" cannot mean "empirically best"

- **Dybå & Dingsøyr (2008)**, *"Strength of Evidence in Systematic Reviews in Software Engineering"* (ESEM '08), borrowing evidence-grading systems from evidence-based medicine (GRADE-style), and their landmark *"Empirical Studies of Agile Software Development: A Systematic Review"* (IST 50(9–10):833–859): the evidence behind widely recommended practices is **generally weak to moderate**. Even famous practices (pair programming, Scrum rituals) rest on thin evidence.
- **Kitchenham et al.** — the EBSE programme (guidelines 2007; Kitchenham & Budgen, *Evidence-Based Software Engineering and Systematic Reviews*): replaces the rhetorical "best" with **graded evidence**. Later reassessments (Pizard et al. 2024, *"Evidence-based Software Engineering Revisited"*) still find SR-based evidence limited.

**Implication for AEGIS:** a compliance methodology cannot honestly claim empirical superiority for its practice layer. "Best" must be re-grounded as **legitimization by a declared, versioned source hierarchy** — an auditable provenance property, not an effectiveness claim.

### 4.2 Security patterns: the context→problem→solution formalization

- **Schumacher**, *Security Engineering with Patterns* (PLoP 2001; book 2003) and **Schumacher et al. 2005** (Wiley): a security pattern is *"a particular recurring security problem that arises in specific contexts and presents a well-proven generic scheme for its solution"*; formally the triple **P := (C, P, S)** — context, problem, solution. Schumacher & Röhm (2003, *"Security Patterns and Security Standards"*) standardize the triple further.
- The pattern literature is exactly the academic answer to the researcher's paradox: a practice is not "how to build X" but a **structured statement of when (context) and why (problem) a proven generic scheme applies**. The unknown design does not invalidate the practice — the practice's *context slot* is what the company context fills.

### 4.3 Legal doctrine: "state of the art" already has an operationalized, tiered reading

- **GDPR Art. 32(1)** binds measures *"taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing"* — a **dynamic, risk-based** standard that forces continuous monitoring of technological developments. Art. 25(1) uses the same indeterminate for data protection by design.
- **EDPB Guidelines 4/2019** on Art. 25 interpret "state of the art" alongside effectiveness and cost; **ENISA** publishes dedicated operationalizations: *"What is 'state of the art' in IT security?"* and the **Online Platform for Security of Personal Data Processing** — a reference **catalogue of security measures** supporting Art. 32 compliance. An authoritative EU catalogue that operationalizes the indeterminate **already exists**.
- **German/EU legal-technical doctrine** distinguishes explicit tiers: *Stand von Wissenschaft und Technik* (state of science — broadest) < ***Stand der Technik*** (state of the art — advanced processes ensuring high protection, tested and accessible but **not necessarily widely adopted**; §3(6) BImSchG; EU analogue: BAT under the IED) vs. ***allgemein anerkannte Regeln der Technik*** (generally accepted rules of technology — **proven in practice and recognized by the expert community**). DIN's own explainer (2025) draws the distinction: the state of the art "has (not yet) proven itself in practice" to the degree the accepted rules have. **TeleTrusT** publishes a dedicated guideline operationalizing "state of the art (in IT security)"; **BSI** maintains Stand-der-Technik guidance and a public library.

**Implication for AEGIS:** a tier hierarchy of practice sources is not an invented device — it mirrors the established European legal-technical doctrine that GDPR's "state of the art" inherits, and it maps cleanly onto the methodology's own ambiguity registry: **R2 already recommends ENISA/EDPB guidance as the strictest ceiling and ISO 27001 + sector practices as the minimum** (registry.md:72-73), adopted by all three cases.

### 4.4 Provenance-model precedents

- **NIST SSDF (SP 800-218)**: a meta-framework of *"established practices"* whose every practice/task documents provenance via informative references to source frameworks (BSA, OWASP, SAFECode). A catalog can honestly be "borrowed with attribution".
- **ISO/IEC 27002:2022**: every one of the 93 controls carries a **5-attribute model** (Control Type; Information Security Properties; Cybersecurity Concepts — aligned to NIST CSF; Operational Capabilities; Security Domains), enabling derived views by filtering. Precedent for AEGIS's `realization_class` as an attribute with derived views rather than a catalog split.

### 4.5 Requirements engineering for not-yet-designed systems

- **ISO/IEC/IEEE 29148:2018** distinguishes: **requirement** ("an expression of one or more particular needs in a very specific, precise and unambiguous form" — states *what*, not *how*), **design constraint** ("a factor that is imposed on the solution by force or compulsion and may limit or modify the design"), and **assumption** (a statement taken as true without proof). Requirements engineering explicitly requires that requirements **not embed design decisions** for the system-of-interest.

**Implication for AEGIS:** asserting verifiable properties/constraints about an undesigned system is not a category error — it is the *definition* of a constraint in RE. The building-code analogy holds: the code prescribes stair dimensions and fire exits without knowing the house.

---

## 5. Decision (proposed)

### D1 — Definition of the Phase 2 good-practice layer

A **good practice in AEGIS Phase 2** is a **context-conditioned solution template**: a named, verifiable **property** (realization_class TECHNOLOGY), **coordinated activity sequence** (PROCESS), or **standing organizational ability** (CAPABILITY) such that:

| Slot | Pattern analogue (Schumacher) | AEGIS content |
|---|---|---|
| Context (C) | specific contexts | the **company context** from Phase 1 input (profile, products/services, data, assumed infrastructure) — never design decisions |
| Problem (P) | recurring security problem | the sub-domain's risk/obligation the practice addresses (D-XX.Y spine) |
| Solution (S) | well-proven generic scheme | the verifiable property/process/capability; its **realization is deferred to Phase 3** |

and that carries **documented legitimization**: source tier + reference + version + default normative intensity.

### D2 — Source tiers (the answer to "best relative to what?")

| Tier | Sources | Default intensity | Doctrinal reading |
|---|---|---|---|
| **T1 — Law** | GDPR, CRA, NIS2, DORA, AI Act (already the obligation layer) | MUST | not "practices" at all; binding whatever gets built |
| **T2 — Regulator operationalizations of open norms** | ENISA state-of-the-art guidance + ENISA Art. 32 security-measures catalogue; EDPB guidelines (4/2019, 7/2019) | SHOULD (ceiling; escalate when incorporated by reference) | the *Stand der Technik* direction — advanced, authority-published |
| **T3 — International consensus catalogs** | ISO 27001/27002, NIST CSF 2.0, NIST SP 800-53 R5, NIST SSDF, OWASP ASVS, OWASP SAMM | SHOULD (minimum) | *allgemein anerkannte Regeln der Technik* semantics — proven in practice and generally recognized |

Grounding: this mirrors the European legal-technical hierarchy (§4.3) and **ratifies the methodology's own registry R2** (ENISA/EDPB ceiling, ISO minimum) as the layer's legitimization policy. Honest caveat (EBSE, §4.1): tier membership means *authority/recognition*, **not** measured effectiveness; an optional future `evidence_grade` attribute may record empirical strength where it exists, without pretending it exists everywhere.

Substrate note (2026-09-22): the T2/T3 tiers already have material containers in the MVP working corpus — the 11 advisory referentials committed in C1–C10 (`baseline/CONTROLS/`: ENISA + EDPB-guidance-derived tracks = **T2**; ISO 27001/27701/42001, NIST 800-53 R5/SSDF/AI SSDF, OWASP ASVS/SAMM, CIS v8, BSI Grundschutz = **T3**). What this ADR adds is the **semantics** those directories currently lack: which tier each occupies, what citing one commits you to, and the admission gate. D2 is the policy the advisory flag presupposes.

### D3 — Admission gate (replaces the 2C-3 architecture criterion)

A candidate practice enters Phase 2 only if **all four** hold:

- **A1 — Context-derivability**: applicability follows from the company context alone (products, data, infrastructure, size, jurisdiction). Fixes the greenfield defect: "no physical controls for cloud-only" becomes derivable from *context*, not from knowing the architecture.
- **A2 — Design-agnostic form**: expressible without embedding a design decision (29148 what-not-how). If A2 fails, the candidate is **deferred to Phase 3 as design guidance** — it is recorded, not asserted as a rule.
- **A3 — Legitimization**: citable to a versioned source in T2/T3 (or a T1 obligation it supports).
- **A4 — Recurrence**: addresses a recurring problem of the sub-domain (non-idiosyncratic; the pattern-P test).

SHOULD-tier practices may be waived with a documented reason (contextual inapplicability) — the posture model's anti-fabrication rule already provides the mechanism. Normative intensity defaults by tier (D2), replacing the undocumented "Bloco B" uniform NI=2 with a stated rationale; escalation to MUST only where law incorporates a source by reference.

### D4 — Naming: drop the rhetorical "best"

The layer's canonical name becomes **"framework-derived good-practice rules"**. corr-008 already deprecates `BPR-D-` in favour of `RULE-D-XX.X-NNN` with framework-derived rows at `+100` (`MC/00_METHODOLOGY/dependency_graph.yaml:258-259`) — the de facto renaming has happened; this decision aligns the prose and removes a term the methodology never defined and the literature treats as contested.

### Why this decision (the rationale to re-read)

1. **The paradox dissolves, it is not argued away.** "Best practices of an undesigned system" is contradictory only for design-level prescriptions. The pattern literature (context→problem→solution) and RE (constraint vs design decision, ISO 29148) both formalize the other kind — constraints conditioned on context — and AEGIS's own `realization_class` already implements the trichotomy. The methodology was conceptually right before it could articulate why; this decision gives the layer its missing definition instead of a retreat.
2. **"Best" becomes auditable.** Since empirical superiority is unavailable in principle (weak evidence base, §4.1), the only honest reading of "best" is *legitimized by a declared, versioned, tiered source hierarchy* — a property one can verify mechanically (A3), which suits a methodology whose whole spine is verifiable traceability.
3. **The tiers are not an invention — they are ratification.** GDPR's "state of the art" forces operationalization; the EU already operationalizes it (ENISA catalogue); German doctrine supplies the tier grammar; and AEGIS's own ambiguity registry (R2, adopted by all cases) already chose this policy for the legal layer. The decision extends an existing, case-tested choice to the Phase 2 rule layer — consistency, not novelty.
4. **It fixes the greenfield defect at its root.** A1 makes context-derivability the admission test, which is exactly what the MVP scenario needs and what 2C-3 currently lacks (it assumes a known architecture/tech stack).
5. **It closes the interrupted Phase 1 thread.** The earlier undecided question — CSF-only anchors in Phase 1 vs. OWASP/ISO/800-53 — resolves consistently: those frameworks get their proper home here, in Phase 2, as T3 anchor vocabularies, keeping Phase 1 lean (CSF primary; PF/AI RMF where dashboards publish them).

---

## 6. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| **Status quo** — catalogs remain the de facto definition of "best practice" | Keeps the circular provenance (overlays from case output), leaves "best" undefined and unfalsifiable, breaks on greenfield contexts (2C-3 assumes a designed system). The three defects remain. |
| **EBSE-strict** — admit only practices with published empirical evidence | Doctrinally pure but impractical: the evidence base for most controls is weak/absent (even for famous practices, §4.1); would gut the layer precisely where obligations don't reach — the layer's declared purpose. Kept as the optional `evidence_grade` attribute instead. |
| **Defer all good practices to Phase 3** | Loses the legal operationalization of "state of the art": Art. 32 binds the *choice of measures*, not only designs — the practice layer is how the methodology answers a legal indeterminate (registry R2). Phase 3 would design into an unconstrained space, and obligations alone demonstrably don't cover all sub-domains (Case_01: 2.0 rules-per-obligation precisely because of coverage gaps, phase2c:271). |

---

## 7. Consequences — future campaigns (NOT executed by this ADR)

Ordered, each pending ratification and its own campaign (respecting P5 impact checks in MC):

- **C1 (MC)** — New normative document (e.g., `00_METHODOLOGY/GOOD_PRACTICE_LAYER.md`, sibling of REALIZATION_CLASS_RUBRIC): definition D1, tier register with source versions (D2), admission gate A1–A4 (D3), intensity defaults, waiver mechanics. Amend pointers in `phase2c_goals_and_rules.md` 2C-3 (selection criterion → context-derivability) and the RUBRIC cross-refs.
- **C2 (MC)** — Re-anchor `MAPPINGS/OVERLAYS/*`: either re-derive from T3 catalogs + frozen dashboards, or reclassify the four overlay files explicitly as case-derived examples (removing the circular source-of-truth claim).
- **C3 (MVP + MC)** — ~~CONTROLS gap decision: ingest ISO and ENISA catalogs~~ *(largely EXECUTED by the parallel C1–C10 campaign of 2026-09-22, commits 450e0da..c438723: 11 advisory referentials materialized in `MVP/baseline/CONTROLS/`)*. Residual work, all **policy wiring**: (a) assign each advisory referential its D2 tier in its `_MANIFEST.json` (ENISA → T2; ISO*/NIST*/OWASP*/CIS/BSI → T3) and define what citation of each tier commits a rule to; (b) decide whether MC's frozen CONTROLS gains the same referentials or MVP remains the working corpus (recommended: MVP only — MC is read-only provenance); (c) either remove ISO 27001 from the 2C-3 source table or align it with ALT_ANCHOR §2 (crosswalk-last-resort) until C1 lands; (d) fix MVP `README.md:18` (7 → 14 referentials, enforced/advisory split).
- **C4 (MC)** — NI policy: replace/document "Bloco B" — tier-derived defaults per D2, with the Case_01 uniform NI=2 recorded as the interim policy that preceded this ADR.
- **C5 (MVP)** — SPEC.md contract for the future Phase 2 increment: input = `phase1_output.md` + company context; admission gate A1–A4 as the Phase-2 pipeline gate; citation format `tier + reference + version`; Phase 3 handoff includes deferred design-guidance items (A2 failures) so nothing is silently dropped. *(Scope amendment, 2026-09-22: the MVP increment is **TECHNOLOGY-only** per [ADR-002](ADR-2026-09-22_mvp-technology-only-scope.md) — PROCESS/CAPABILITY rules and `PROC-*`/`CAP-*` artifacts stay out of MVP scope.)*
- **C6 (MC)** — Prose alignment where "best practice" survives in human-facing docs (Doc18 §1/§2 headers, flow-diagram stage names) — only when C1 lands; no ID changes (corr-008 already canonical).

## 8. What this ADR deliberately does not do

No edits to MC (read-only provenance source), none to `baseline/`, no new catalogs, no spec changes. Everything is recorded here as consequence campaigns. The MVP Phase 2 increment is not designed here.

## 9. Ratification checklist (P7)

1. Adopt D1 (definition) — yes / amend: ______
2. Adopt D2 (tiers, incl. ENISA/EDPB as T2 ceiling) — yes / amend: ______
3. Adopt D3 (admission gate; deference rule for A2 failures) — yes / amend: ______
4. Adopt D4 (naming "framework-derived good-practice rules") — yes / amend: ______
5. Sequencing of campaigns C1–C6 (recommendation: C1 → C3 → C5; C2/C4 can follow) — order: ______

## 10. References

**Academic:**
- Dybå, T. & Dingsøyr, T. (2008). *Strength of Evidence in Systematic Reviews in Software Engineering.* ESEM '08, ACM. — and — *Empirical Studies of Agile Software Development: A Systematic Review.* Information and Software Technology 50(9–10), 833–859.
- Kitchenham, B. et al. (2007). *Guidelines for performing Systematic Literature Reviews in Software Engineering.* EBSE Technical Report; Kitchenham, B. & Budgen, D., *Evidence-Based Software Engineering and Systematic Reviews.*
- Pizard, S. et al. (2024). *Evidence-based Software Engineering Revisited.*
- Schumacher, M. (2001/2003). *Security Engineering with Patterns.* PLoP / Springer; Schumacher, M. et al. (2005). *Security Patterns: Integrating Security and Systems Engineering.* Wiley; Schumacher, M. & Röhm, U. (2003). *Security Patterns and Security Standards.*

**Legal & regulatory:**
- [GDPR Art. 32 — Security of processing](https://gdpr-info.eu/art-32-gdpr) ("state of the art" wording).
- [EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default](https://www.edpb.europa.eu).
- [ENISA — "What is 'state of the art' in IT security?"](https://www.enisa.europa.eu/news/enisa-news/what-is-state-of-the-art-in-it-security); [ENISA — Online Platform for Security of Personal Data Processing (Art. 32 reference catalogue)](https://www.enisa.europa.eu/sites/default/files/publications/Online%20Platform%20for%20Security%20of%20Personal%20Data%20Processing.pdf).
- German doctrine *Stand der Technik* vs. *allgemein anerkannte Regeln der Technik*: [DIN explainer (2025)](https://www.din.de); [howtoregulate.org, "Referring to standards" (2019)](https://howtoregulate.org); [BSI — Stand der Technik](https://www.bsi.bund.de); TeleTrusT guideline *State of the art (in IT security)*; §3(6) BImSchG; EU IED/BAT analogue.

**Standards & frameworks:**
- [NIST SSDF (SP 800-218)](https://www.nist.gov) — "established practices" with provenance informative references (BSA, OWASP, SAFECode).
- ISO/IEC 27002:2022 — 93 controls, 5-attribute model (Control Type / InfoSec Properties / Cybersecurity Concepts / Operational Capabilities / Security Domains).
- ISO/IEC/IEEE 29148:2018 — requirement vs. design constraint vs. assumption ([ISO](https://www.iso.org)).

**Repository evidence:** §3 of this document, with file:line citations.

---

*Related: the interrupted 2026-09-22 Phase-1 anchoring thread (CSF primary; PF/AI RMF where dashboards publish them; OWASP/ISO/800-53 deferred to Phase 2) is resolved by D2/T3 — this ADR is where those frameworks land.*
