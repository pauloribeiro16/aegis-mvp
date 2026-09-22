# D-07.1 — Relevant Ambiguity (AI Act)

> Part 4 ambiguity analysis for AI Act, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## AI_Act
#### 2.14 AIA-C14 — Art. 14(1) Human oversight design
**Source locus:** `High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use`.
* **VAG — S2** — `appropriate`, `effectively overseen`.
* **POLY — S2** — `effectively overseen` — supervisor-can-intervene vs. supervisor-does-intervene vs. supervisor-understands. The three senses drive different design choices (stop-button vs. dashboard vs. explanation-panel).
**Berry anchor:** §5.1 (`appropriate`, `effectively`), §3.3.1 (`overseen`).
#### 2.16 AIA-C16 — Art. 15(1) Accuracy, robustness, cybersecurity
**Source locus:** `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle`.
* **VAG — S3** — `appropriate level of accuracy, robustness, and cybersecurity`. The three AI-technical properties are each inquiry-resistant: `accuracy` (against which metric? at what threshold?), `robustness` (against which perturbations?), `cybersecurity` (against which threat model?).
* **COORD — S2** — `accuracy, robustness AND cybersecurity` (3-way AND of distinct properties). Partial compliance (2 of 3) is undefined.
**Berry anchor:** §5.1 (`appropriate level`), §3.3.1 (`accuracy`, `robustness`, `cybersecurity`), §5.4.7.
#### 2.21 AIA-C21 — Art. 17(1)(c) Design control
**Source locus:** `techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system`.
* **POLY — S2** — `design` vs. `design control` vs. `design verification` — three engineering terms with overlapping but distinct industry meanings.
* **COORD — S2** — `design, design control AND design verification` (3-way AND of near-synonyms); `techniques, procedures AND systematic actions` (3-way AND of artefact types).
**Berry anchor:** §3.3.1 (`design`/`control`/`verification`), §5.5 (twin 3-way AND).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.ambiguity.md

* **POLY — S3** — `accuracy` (precision vs. recall vs. F1 vs. calibration), `robustness` (distributional shift vs. adversarial vs. operational), `cybersecurity` (cf. CRA C07 — undefined at the EU level).

<!-- aegis:purity: own_reg=AI_Act; demoted=1; core_cross_mentions=0 -->