# D-05.1 — Relevant Ambiguity (AI Act)

> Part 4 ambiguity analysis for AI Act, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## AI_Act
#### 2.5 AIA-C05 — Art. 10(1) Data governance scope
**Source locus:** `High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used`.
* **VAG — S2** — `quality criteria` (deferred to paragraphs 2–5, themselves VAG-loaded).
* **POLY — S2** — `techniques involving the training of AI models` — does it include fine-tuning? Transfer learning? Reinforcement learning from human feedback? The clause does not enumerate.
* **COORD — S2** — `training, validation AND testing data sets` — 3-way AND of dataset categories.
**Berry anchor:** §5.1 (`quality`), §3.3.1 (`training`), §5.4.7.
#### 2.6 AIA-C06 — Art. 10(2) Data governance practices
**Source locus:** 8-element list (a)–(h) of data governance practices, including `(f) examination in view of possible biases … (g) appropriate measures to detect, prevent and mitigate possible biases`.
* **VAG — S2** — `appropriate`.
* **POLY — S3** — `biases` — statistical bias (sampling error) vs. algorithmic bias (unequal performance) vs. societal bias (discriminatory outcome). The clause does not differentiate; the three senses drive distinct detection methods.
* **COORD — S3** — 8-element closed list (a)–(h) AND-coordinated; within (g), `detect, prevent AND mitigate` is a 3-way AND of distinct activities. The cumulative obligation requires all 8 practices and all 3 bias activities.
**Berry anchor:** §5.1 (`appropriate`), §3.3.1 (`biases`), §5.4.7 (8-element list + nested 3-way AND).
#### 2.7 AIA-C07 — Art. 10(3) Dataset quality criteria
**Source locus:** `Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose`.
* **VAG — S3** — `relevant`, `sufficiently representative`, `to the best extent possible`, `free of errors`, `complete`. Five vague determiners in one sentence.
* **POLY — S2** — `representative` — demographically representative vs. statistically representative vs. contextually representative.
* **COORD — S3** — `relevant, sufficiently representative, AND to the best extent possible, free of errors AND complete`. The third coordinator (`and to the best extent possible`) introduces a soft hedge on what would otherwise be hard requirements (`free of errors`, `complete`). Berry §5.4.7: the parse tree admits distinct readings (are all five criteria hedged, or only the last two?).
**Berry anchor:** §5.1 (`relevant`, `sufficiently`, `free of errors`, `complete`), §5.4.7 (hedge-AND interaction).
#### 2.8 AIA-C08 — Art. 10(5) Special category data processing
**Source locus:** `To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction … the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards … In addition … all the following conditions must be met: (a) … (b) … (c) … (d) … (e) … (f)`.
* **VAG — S3** — `strictly necessary`, `appropriate safeguards`, `state-of-the-art security and privacy-preserving measures`.
**Berry anchor:** §5.1 (`strictly necessary`, `state-of-the-art`, `appropriate`), §5.4.7 (6-element AND-list).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.ambiguity.md

* **POLY — S2** — `state-of-the-art` — Berry §5.1 classic vague term (cf. GDPR C09, CRA C07). Time-dependent, jurisdiction-dependent.

### from regs/AI_Act.ambiguity.md

* **COORD — S3** — Six cumulative conditions (a)–(f) all required (closed AND-list); the exception to GDPR Art. 9 prohibition is narrow in theory but each condition is qualitatively specified, leaving wide practical discretion.


<!-- aegis:purity: own_reg=AI_Act; demoted=2; core_cross_mentions=0 -->