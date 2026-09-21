# D-09.1 — Relevant Ambiguity (AI Act)

> Part 4 ambiguity analysis for AI Act, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## AI_Act
#### 2.12 AIA-C12 — Art. 13(1) Transparency
**Source locus:** `High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately. An appropriate type and degree of transparency shall be ensured`.
* **VAG — S3** — `sufficiently transparent`, `appropriate type and degree of transparency`. Two vague anchors in one sentence, both modifying the same concept (transparency).
* **POLY — S3** — `transparent` — three distinct AI-governance senses: (i) explainability (the deployer can understand why the system produced this output); (ii) disclosure (the deployer is told what the system does in general); (iii) interpretability (the deployer can map inputs to outputs). The three senses imply different technical implementations (XAI tooling vs documentation vs model-architecture disclosure).
**Berry anchor:** §5.1 (`sufficiently`, `appropriate`), §3.3.1 (`transparent` polysemy).
#### 2.13 AIA-C13 — Art. 13(3) Instructions for use
**Source locus:** `instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers`.
* **VAG — S2** — `appropriate`, `concise`, `complete`, `correct`, `clear`, `relevant`, `accessible`, `comprehensible`. Eight vague adjectives in one sentence.
* **POLY — S2** — `characteristics, capabilities and limitations of performance` — three near-synonyms for system properties.
* **COORD — S2** — `concise, complete, correct AND clear` (4-way adjective AND); `relevant, accessible AND comprehensible` (3-way adjective AND). Two separate AND-chains compounding in one sentence.
**Berry anchor:** §5.1 (8 vague adjectives), §5.4.7 (twin AND-chains).
#### 2.20 AIA-C20 — Art. 17(1) Quality management system
**Source locus:** `Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)`.
* **VAG — S2** — `systematic and orderly manner`.
* **POLY — S2** — `quality management system` — ISO 9001 vs. ISO/IEC 23053 vs. internal bespoke.
* **COORD — S2** — `written policies, procedures AND instructions` (3-way AND); 13-element closed list (a)–(m) AND-coordinated.
**Berry anchor:** §5.1 (`systematic`, `orderly`), §3.3.1 (`QMS`), §5.4.7 (13-element list).
#### 2.22 AIA-C22 — Art. 17(1)(g) Risk management documentation
**Source locus:** `the risk management system referred to in Article 9` — single cross-reference constitutes the entire sub-point.
* **POLY — S2** — `risk management system` (inherits from C01).
* **COORD — S2** — implicit; the cross-reference defers to Art. 9 structure.
**Berry anchor:** §3.3.1 (`risk management system`).
#### 2.23 AIA-C23 — Art. 26(1) Deployer measures
**Source locus:** `Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use`.
* **VAG — S2** — `appropriate`.
* **POLY — S2** — `appropriate` (legal hedge vs. technical recommendation).
**Berry anchor:** §5.1 (`appropriate`), §5.4.7 (`technical and organisational`).
#### 2.24 AIA-C24 — Art. 26(2) Deployer oversight assignment
**Source locus:** `Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support`.
* **VAG — S2** — `necessary`.
* **POLY — S2** — `competence`, `training`, `authority` — three near-synonyms for personnel qualifications.
* **COORD — S2** — `necessary competence, training AND authority` (3-way AND); `as well as the necessary support` adds a fourth element.
**Berry anchor:** §5.1 (`necessary`), §3.3.1 (`competence`/`training`/`authority`), §5.4.7.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.ambiguity.md

* **COORD — S2** — `technical AND organisational` — same AND/OR pattern as GDPR Art. 5(1)(f) (C04); inclusive vs. exclusive reading material.


<!-- aegis:purity: own_reg=AI_Act; demoted=1; core_cross_mentions=0 -->

