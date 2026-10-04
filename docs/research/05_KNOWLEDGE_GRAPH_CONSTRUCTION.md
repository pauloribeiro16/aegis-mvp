---
document_id: AEGIS-RES-05
title: 'Knowledge-graph construction — building a cyber KG, and knowing when it is wrong'
version: 0.1.0
created: 2026-10-04
status: ACTIVE
survey_date: 2026-10-04
sources: 'docs/research/sources.yaml'
---

# Knowledge-graph construction — an annotated catalogue

**What this document is.** A catalogue of `KG-001`..`KG-010`: how knowledge graphs
are actually built, in cybersecurity and in general, and — the part that matters
more — the named ways the built thing turns out to be wrong. It is a *reference*,
not a recommendation. What AEGIS should do with it is
[09_KG_PATTERN_MAPPING.md](09_KG_PATTERN_MAPPING.md).

**Method.** Web survey, 2026-10-04, one pass over primary sources. Preference for
standards bodies and machine-readable artefacts over prose, and for measurement
over assertion. Every factual claim carries an `[S-nnn]` token resolving into
[sources.yaml](sources.yaml); verify with `python scripts/check_research_refs.py
--strict`.

**A methodological note that shapes this whole document.** Three independent
findings in this survey say that the *scorer*, not the extractor, determines what
a published KG number means. The sharpest is [S-202]: re-scoring ten CTI
extraction systems on shared documents under eight matching protocols **reversed
eleven of forty-five pairwise orderings**, and one fixed prediction set spans F1
0.1577 to 0.6994 depending on the matcher. Read that before any number in §3.
The consequence for this catalogue: patterns whose *mechanism* is documented are
recorded at high confidence; patterns whose *score* is documented are recorded
with the scorer attached.

**Evidence grades.** `PRIMARY` (standards body or vendor spec read directly) ·
`PEER` (preprint or paper; peer status not established) · `PRACTITIONER` (named
expert from experience) · `CONTESTED` (credible sources disagree; both recorded).

---

## 1. Substrate: what already exists as a machine-readable graph

### KG-001 — Standards as the substrate: STIX 2.1 + TAXII 2.1

**Definition.** Rather than designing a node/edge schema, adopt a standard object
model that the domain already converges on. In cyber threat intelligence that
object model is **STIX 2.1** (Structured Threat Information Expression) with
**TAXII 2.1** as its transport.

**Sources.** [S-183] is the OASIS Standard, read in full: 19 Domain Objects, 2
SROs (`relationship`, `sighting`), 18 SCOs, with every id typed as
`^<type>--<uuid>`. [S-184] is the normative JSON schema set that actually gets
loaded. [S-189] is TAXII 2.1, published by the same technical committee on the
same date (2021-06-10). MITRE's ATT&CK is distributed *as* STIX [S-186].

**The finding that makes this more than a checklist.** [S-187] records parsing
the full Enterprise 19.2 bundle: **26,086 objects of which 21,262 — 81% — are
`relationship` objects**, against 858 attack-patterns and 733 malware. The
analytic content of a mature cyber knowledge base lives in the edges, not the
node list. That is a direct, measured analogue of what
`baseline/MAPPINGS/traceability/traceability.csv` already is in this repo.

**Named limitations.** Two, both structural rather than fixable:

- The `vulnerability` SDO is deliberately thin — only `name` is required, and
  there is **no first-class CVE-ID field** [S-183]. Linking a STIX vulnerability
  to a CVE number is a convention via `external_references`, not a typed edge.
- ATT&CK's `x-mitre-*` custom types (`analytic`, `detection-strategy`,
  `data-component`, `data-source`, `tactic`) are **not** OASIS SDOs, so a
  strictly-validating STIX 2.1 consumer will reject or ignore them [S-187].

**For AEGIS.** There is no equivalent consensus standard for EU regulatory
compliance, and the absence is worth recording rather than working around: the
only machine-readable regulatory substrate in this survey is the one this repo
already maintains itself. The transferable move from [S-183] is not the schema —
it is the **`aliases` array on `attack-pattern`**, a first-class typed field for
alternative names, which is exactly what a canonical-ID scheme needs and what
hand-maintained prose usually lacks.

### KG-002 — Attack graphs: encode the rules, not the instances

**Definition.** For network-state reasoning, encode advisories, host and network
configuration, and interaction rules in a declarative language (Datalog, or a
constrained rule DSL) and let an engine derive the graph, rather than
materialising attack paths.

**Sources.** [S-191] is MulVAL (USENIX Security 2005) — read in full, and the
strongest quantitative evidence in the entire survey despite being 21 years old.
Everything is Datalog: advisories via OVAL, host and network configuration as
HACLs, principals, interaction rules. Measured runtime **0.08s at 1 host, 0.22s
at 200, 0.75s at 400, 3.85s at 1000, 15.8s at 2000**. The whole
reimplementation is ~1,000 lines (668 scanner + 393 rules) and the rules are
**vulnerability-definition-independent**. Coverage: 84% of Red Hat OVAL
definitions (169 of 202), reasoning about privilege escalation and DoS but
explicitly *not* confidentiality or integrity loss.

**The correction to a common framing.** Recent work [S-192] opens by saying
attack graphs "suffer from poor scalability due to their combinatorial
complexity" — which [S-191] contradicts for Datalog-based generation. The
sharper statement in [S-192] is that the defect is **temporal, not
combinatorial**: existing solutions permit analysis only *after* generation
completes, and long generation times mean "they poorly capture the dynamic
changes in the networks". The fix inverts the loop so the analyst queries during
generation and the analysis query *steers* it.

**Named limitation, from the source itself.** [S-191] documents hypothetical
("what if") analysis degrading as n^k over program kinds × injected bugs: **12s
at k=1, 273s at k=2**. The authors concede this is acceptable only because
counterfactual analysis runs offline before the bug is known. That remains the
binding constraint on counterfactual graph reasoning.

**Caveat carried forward.** [S-192]'s abstract reports no absolute node counts or
wall-clock numbers, and the full PDF was not read; its "networks of
unprecedented size" claim is unverified.

---

## 2. Taxonomy chaining: the most seductive and most dangerous construction

### KG-005 — Derive, do not chain: table expansion is an artefact, not a finding

**Definition.** The obvious way to build a cyber knowledge graph is to derive
edges transitively through the standard taxonomies — CVE → CWE → CAPEC → ATT&CK
— and inherit every mapping error at each hop. **This does not work, and the
magnitude of the failure is measured.**

**Sources.** [S-185] explains why the errors compound: `CVE → CWE` is an
*editable, declared* mapping inside each CVE record, not a computed one.
[S-188] supplies the structural amplifier — CAPEC is an explicit hierarchy that
itself concedes multi-parent membership: "There exists the potential for some
attack patterns to align with more than one category." [S-201] quantifies the
result, read in full.

**The measurement.** On CVE2CAPEC's CVE-2024 database (39,156 CVEs, 34,562
labelled), coverage looks excellent — 88.3% receive at least one ATT&CK
technique. But the **median labelled CVE receives 8 techniques, the mean 13.3,
and 19% receive twenty or more**. The most frequent derived technique, T1574.007
(Path Interception by PATH Environment Variable), is attached to **53% of all
labelled CVEs**; T1574.006 to 53%, T1562.003 to 52%, T1134.001 to 49%. The
authors' own words: "No plausible reading of the vulnerability landscape has
path-interception implicated in a majority of all disclosed CVEs; these
frequencies are artifacts of table expansion."

**The concrete failure.** CVE-2024-21732, a cross-site-scripting bug (CWE-79), is
mapped through 48 CAPECs to T1027 and T1574.006/007 — none of which relates to
XSS.

**What to do instead.** [S-201] trains a multi-label classifier on 1,207 CVEs
curated by the MITRE Center for Threat-Informed Defense, roughly doubling
recall@5 over a zero-shot baseline (0.322 → 0.686); the record figures are
recall@5 **0.673 ± 0.019**, macro-F1 0.177 ± 0.014. Crucially, they then try
LLM-generated label expansion as a cheap substitute for more expert curation and
show it fails: at ~0.39 agreement with expert annotation, "the apparent
improvement is an evaluation artifact", and **additional expert-curated data
consistently improves performance whereas LLM-labelled data does not** — "the
classifier is limited by label quality rather than dataset size."

**The transferable principle, and it is the strongest lesson in this
document.** *An edge derived by table expansion is an artefact of the tables, not
a statement about the subject.* This is precisely the failure mode rule R2
already guards against on the AEGIS side by forbidding the agent to re-derive
anchors: the discipline is to copy a verified anchor from a mapping surface, and
never to compute one by traversing taxonomies. [S-201] is the external,
measured confirmation that R2 is not over-cautious.

**Caveat.** [S-201] also demonstrates the evaluation trap that produces the
"artifact" verdict in the first place: "Selecting checkpoints on a small test
split effectively maximizes over many noisy evaluations, producing recall@5
differences of up to 0.05 between otherwise identical runs." Read with KG-009.

---

## 3. Building a graph from text

### KG-003 — The four-stage pipeline, reached independently three times

**Definition.** CTI graph construction converges on the same four stages —
**extract → ground/type → verify → curate/merge** — regardless of whether the
implementation is rules, an LLM, or a team of agents.

**Sources.** Four independently-authored systems decompose the same way, which is
the strongest kind of convergence signal available:

| System | Stages named | Source |
|---|---|---|
| AttacKG+ | rewriter, parser, **identifier**, summarizer | [S-194] |
| CTINexus | prompt construction, **hierarchical entity alignment**, long-distance relation prediction | [S-195] |
| TACTIC-KG | extraction, typing, verification, curation **agents** | [S-212] |
| BEACON | propose-then-verify extraction, then hierarchical merging | [S-197] |

The one substantive difference is whether *grounding to a canonical taxonomy* is
an explicit stage. All four make it one; only BEACON [S-197] states the insight
that makes the others coherent.

**The load-bearing insight (KG-003 proper).** [S-197]: "attack behaviors, once
mapped to MITRE ATT&CK (a standardized catalog of attack techniques), **can
anchor the rest of a report**. Attaching them to these anchors places every
per-report graph in one canonical space." ATT&CK is recast from a *label* into a
**join key** — the thing that makes two unrelated documents' graphs comparable
at all. This reframes the entire problem: extraction is not the bottleneck,
*grounding* is.

**Supporting evidence for that claim.** [S-193] (AttacKG, pre-LLM) reports F1
0.887 for attack-relevant entities, 0.896 for dependencies, but only **0.789 for
techniques** — the technique score sits ~10 points below the entity score even
with non-LLM extraction, in 2021. Technique identification was always the hard
sub-problem.

**Method note.** The multi-hop part is not the single-source problem it is often
posed as. [S-196] (MultiKG, same lead author as AttacKG) improves on
single-source text by adding **audit logs and static code analysis** as
finer-grained sources, processing each separately then merging.

### KG-004 — Entity resolution: a distinct stage, and the reference implementation does not do it

**Definition.** Mapping extracted surface names onto canonical identifiers is a
separate problem from extraction, and it is where curated graphs are won or lost.

**The uncomfortable starting point.** The reference GraphRAG implementation
resolves entities by **exact string matching**, and defends it [S-170]:
"GraphRAG is generally resilient to duplicate entities since duplicates are
typically clustered together for summarization in subsequent steps."

**Why that defence does not transfer.** In GraphRAG, cluster identity is an
intermediate artefact feeding a summarisation step, so duplicates wash out. In a
curated corpus, **cluster identity *is* the analytic output** — [S-197]'s
entire thesis is that the same threat is given unrelated names across sources,
and that ATT&CK anchors are what place the graphs in one canonical space. If the
duplicates are the signal, exact string matching is not a defensible default.

**The mechanism, reached three times independently.** Hierarchical, cluster-aware,
most-deterministic-signal-first merging:

- [S-197] applies signals "in decreasing order of determinism, from
  character-level and semantic similarity to overlapping technique
  neighborhoods", iterating as merges pool neighborhoods.
- [S-195] calls it "hierarchical entity alignment".
- [S-204] names the wrong primitive being used: "current LLM-based entity
  matching approaches typically follow a binary matching paradigm that **ignores
  the global consistency among record relationships**." An entity mentioned in
  three reports must be merged *consistently*, not by three independent binary
  calls. Across 8 ER datasets and 10 LLMs, the cluster-level **selecting**
  strategy wins.

**What general-domain SOTA says.** [S-203] (EDBT 2025): the best LLMs "require no
or only a few training examples to perform comparably to PLMs that were
fine-tuned using thousands of examples", and — the result that matters for a
growing corpus — "LLM-based matchers further exhibit higher robustness to unseen
entities." A newly admitted regulation is exactly the out-of-distribution case.
Two practical caveats from the same source: "**there is no single best prompt but
that the prompt needs to be tuned for each model/dataset combination**", so
prompt tuning is not optional; and GPT-4 can emit structured explanations of
*wrong* decisions, which makes error-class discovery automatable.

**The joint formulation.** [S-210] (ReLiK, ACL 2024) does entity linking and
relation extraction in **one forward pass** by placing candidate entities
alongside the text, rather than one pass per candidate — a retrieve-then-read
structure where a retriever proposes canonical ids and a reader aligns spans to
them, claiming in- and out-of-domain SOTA with "up to 40x inference speed
compared to competitors".

**Benchmark.** [S-198] (CTIConnect, KDD 2026) makes **Entity Linking a
first-class task category** — 1,860 expert-verified QA pairs across nine tasks
over five heterogeneous sources. Its finding is that the bottleneck "shifts
between retrieval infrastructure and evidence utilization depending on the task",
and that results are stable under temporal splits spanning 2008–2025, the only
temporal-split protocol found for CTI.

### KG-006 — Extraction: LLM, small encoder, or neither

**Definition.** Entity and relation extraction for graph construction. The choice
is between a general LLM, a small task-specific encoder with swappable schema, and
a rule/Datalog pipeline.

**The efficiency argument for small encoders.** [S-207] (GLiNER) takes entity
types **at inference time as natural-language labels**, so a taxonomy can be
swapped without retraining, and extracts in parallel rather than by the slow
sequential token generation of LLMs. [S-208] extends this to relation extraction
and QA in one small encoder, so a non-LLM path can cover both halves of
construction. **Both papers' headline claims are table-relative with no numbers
in the abstract, and [S-207] self-labels "Work in progress"** — cite [S-208] and
read the tables before treating either as a result.

**The seq2seq formulation.** [S-209] (REBEL, EMNLP 2021) reframes relation
extraction as seq2seq generation of triples, motivated by exactly the failure
mode these papers keep reporting: multi-step pipelines "propagate errors or are
limited to a small number of relation types". It is a *general-domain* model
whose 200 relation types are Wikipedia-ish, so applying it to STIX/ATT&CK types
requires fine-tuning. (Naming hazard: an unrelated 2026 preprint also called
REBEL exists — arXiv 2602.06248.)

**The ontology-conformance requirement.** [S-206] (Text2KGBench, ISWC 2023) is
the reference benchmark and states the task precisely: extract facts that
**conform to a given ontology's concepts, relations and domain/range
constraints** *and* are faithful to the input. Its verdict as of 2023 — "there is
room for improvement using both Semantic Web and Natural Language Processing
techniques" — is the statement that open 13B models had not solved it. It is
**not cyber-specific and no cyber-domain equivalent was found.**

**A reporting-hygiene data point, and a reusable asset.** [S-213] reports gains as
*deltas only* — "3-4% gains in NER and up to 8% in RE" — with no absolute
scores, which is itself a datum about this field (see KG-009). Its useful
contribution is the artefact rather than the result: **DNRTI-AUG-STIX2**, a
released dataset with 21 entity types aligned to STIX 2.1. For anyone building
against STIX, that is the one ready-made extraction corpus found in the survey.

**The best articulation of why schema-fixed pipelines break.** [S-211] (ANCHOR)
names three challenges directly: "(i) schema-specific pipelines that require
manual reconfiguration whenever the schema changes, (ii) prompt-based schema
inclusion that fails to scale on large ontologies such as UCO, and (iii)
reliance on enterprise LLM APIs that conflicts with privacy constraints." Its
answer pairs search-and-navigate ontology discovery with **SHACL-based
validation** of type assignments, evaluated on UCO, STIX and MALOnt — with the
practically important result that "ANCHOR with a local LLM closely matches
enterprise LLM typing performance". A corpus that must absorb a *new regulation*
hits challenge (i) exactly.

**The local-model result.** [S-212] (TACTIC-KG) decomposes construction into
specialised agents for extraction, typing, verification and curation, and reports
that with **3B–8B models** agent specialisation "consistently outperforms larger
monolithic in-context-learning baselines". No absolute F1 in the abstract — the
direction is the takeaway, and the direction is the one that matters for a
pipeline that runs a local model.

**The dissent worth knowing: less structure can be right.** [S-214] (KGV)
builds *paragraph-level* graphs where nodes are text segments linked by
similarity, and measures the trade against entity-based graphs: node count **down
nearly two-thirds, precision up 1.7%, response time down 46.7%**, with a 5.7% F1
gain on CTI-200. This is the only published measurement of the cost of
entity-centricity anywhere in the survey, and it is the one counterweight to the
premise that a richer typed graph is automatically better.

### KG-007 — Consolidation: merge hierarchically, and never pairwise

**Definition.** When several extracted graphs describe the same entity, merge them
by applying signals in decreasing order of determinism, iteratively, pooling
neighborhoods as merges proceed — rather than asking a model pairwise whether two
records match.

**Sources.** [S-204] establishes that pairwise binary matching is the wrong
primitive because it "ignores the global consistency among record relationships",
and that cluster-level *selecting* wins across 8 datasets and 10 LLMs. [S-197]
and [S-195] converge on the same hierarchical shape from the cyber side. [S-203]
supplies the per-comparison primitive.

**Why determinism order matters.** A character-level match is auditable and
reversible; an embedding similarity is neither. Applying them in that order means
the cheap, checkable signal fires first and the probabilistic one only resolves
what the deterministic pass could not — and every step remains inspectable, which
is the property a regulated corpus needs most.

### KG-008 — Incremental update beats rebuild

**Definition.** Absorb new documents into an existing graph rather than
regenerating it.

**Sources.** [S-228] measures the rebuild cost directly and it is severe: adding a
same-size corpus to a Microsoft-GraphRAG index forces the community structure to
be regenerated at roughly **1,399 × 2 × 5,000 ≈ 14M tokens**, where LightRAG
merges new entities and relations into the existing graph. [S-190] (FIRST EPSS)
supplies the discipline for *derived* values: retraining is "driven by evidence of
performance degradation, not a fixed calendar" — "Sustained drift toward the
random baseline triggers a retraining cycle… In practice, retraining has
occurred approximately annually."

**One trap in [S-190] worth flagging.** Exploitation activity does **not** feed
daily EPSS scores — "Exploitation data informs model training, not daily
scoring", because direct evidence would leak activity EPSS lacks rights to
publish. So a CVE-to-exploitation edge in a graph comes from *signals* (exploit
code, chatter, reference volume), not from confirmed exploitation; CISA KEV is
the confirmed-exploitation source. Building a graph that treats a modelled
probability as an observed fact is the same error as KG-005 in a different
register.

---

## 4. Knowing when the graph is wrong

### KG-009 — The matcher determines the number, and almost nobody specifies it

**Definition.** The most important methodological finding in the survey: for graph
construction, the *scoring rule* is an uncontrolled variable large enough to
reverse system rankings. Any published extraction F1 that does not name its
matcher is uninterpretable.

**Source.** [S-202] — read in full, and the paper this catalogue most needs to
exist. Findings in order of severity:

- Of **twelve** inspected CTI extraction systems, the stated matching rule was
  reimplementable for only **five**; three "named a family without fixing it, and
  four stated no criterion". The most consequential named case counts a
  prediction correct when it "semantically match[es]" without specifying
  encoder, threshold, or rule.
- Re-scoring **ten** systems on 50 shared documents under **eight** protocols
  **reversed eleven of forty-five pairwise orderings**; one fixed prediction set
  spans F1 **0.1577 to 0.6994**.
- Against a 378-item human-adjudicated calibration set, **no mechanical
  protocol agrees with reviewers more than 71%** (range 0.598–0.706) across
  lexical, embedding and NLI-entailment families. The strict protocol misses
  40.2% of matches humans credit. An LLM judge reaches 0.860.
- **Corpus-pooled matching inflates true positives by 6.4%.**

The framing to reuse: "a reader comparing a published 0.16 against a published
0.70 would infer a different system, not a different set of three decisions."

**The mechanism that matters most for a curated corpus.** [S-202] finds that a
canonicalization module "scores identically to four decimals" with and without
itself on every backbone, while the two prediction sets differ on **54 of 1,571
triples**. Soft name comparison absorbs every rewrite, so the metric is not
judging canonicalization to be neutral — **it cannot see it**. Also: the error
profile shifts with input granularity (long documents dominated by
confidence-lowering errors at 67.0%, short sentences by type misassignment at
29.5%), so a validator ported to a new corpus should expect the dominant error
category to follow granularity rather than stay fixed.

**A related trap that masquerades as a hallucination finding.** In financial
triplet extraction (S-244's sibling thread; see [S-202] on precision reporting),
hybrid regex plus LLM-judge verification cut apparent *subject* hallucination
from **65.2% to 1.6%** — i.e. roughly 64 points of the "hallucination" was
coreference false positives. Naive hallucination counting in an extraction
pipeline is dominated by coreference artefacts.

### KG-010 — Drift, staleness, and provenance are maintenance, not construction

**Definition.** A graph is a maintained artefact with a half-life, not a build
product. Provenance per edge is what makes maintenance tractable.

**Sources.** [S-190] is the best-documented drift discipline in the survey and
covers the derived-value case. [S-190]'s "why did my score change overnight"
framing is the right mental model for any graph whose nodes are refreshed from an
external feed.

**Provenance is captured more often than it is used.** [S-202] observes that
systems' triples and benchmark annotations routinely inherit a pointer to the
sentence and citation that produced them, yet "in the one systematic check
available, it was not used to filter or score anything." Captured provenance that
nothing reads is decoration.

**For a frozen-corpus pipeline, this inverts.** AEGIS's baseline is version-
controlled markdown with a documented source of truth per field. Its graphs would
be *regenerated from* that corpus rather than *refreshed from* a feed, so drift
is bounded by the corpus's own review cycle — a materially easier problem than
KG-010 as the literature poses it, and the reason KG-010 is a smaller concern
here than for the systems that produced it.

### KG-023 — LLM-built graphs: validity, and where they are measured

**Definition.** The controlled comparison of graph construction methods, and the
one number that reframes the whole thread.

**Source.** [S-205] (KGGen, with the MINE benchmark) — read in full. MINE-1: 100
articles × 15 manually verified facts, with an LLM inferability judge
**validated at 90.2% agreement and 0.80 correlation** against manual scoring of
60 fact-KG pairs. Results: **KGGen 66.07%, GraphRAG 47.80%, OpenIE 29.84%**. Per
model, KGGen scores Claude Sonnet 3.5 73%, GPT-4o 66%, Gemini 2.0 Flash 44%.

**The sharpest number in the survey.** From 100 hand-scored triples per method:
**KGGen 98% valid, OpenIE 55%, GraphRAG 0%.**

**How to reconcile 0% with GraphRAG's published wins.** The docs answer it:
GraphRAG's graph is designed for its own pipeline (entities carry
*descriptions*, not typed triples), and Microsoft itself says its FastGraphRAG
graph "is less directly relevant for use outside of GraphRAG". The fair reading
is that **GraphRAG's graph is a valid memory structure for its own summariser and
a poor KG substrate for reuse** — and for a project whose goal is an
interoperable knowledge graph rather than a question-answering index, that
distinction is decisive.

**KGGen's mechanism is entity clustering**, and it improves the metrics while
*shrinking* the graph: at 1M characters, entities 4,602 → 3,573 and edges 3,180
→ 2,448. It also reports relation-type reuse of ~10× for KGGen versus ~2× for
GraphRAG regardless of corpus size, concluding that "the relations in GraphRAG
do not generalize as the corpus grows". Cost on 1M characters: 5.37M tokens,
551s.

**Construction cost, officially attributed.** Microsoft's own docs state graph
extraction is "roughly 75% of indexing cost" and that for a curated corpus
"[i]ndexing is a relatively expensive operation… start small." Their shipped
example prompts are written for "people, places, organizations, or things" — the
wrong prior for a regulatory corpus, and their own transparency document names
prompt dependence as the main quality risk.

**Maintenance mode is a first-order fact.** [S-263]: the canonical
implementation is self-declared "largely in maintenance mode, and won't be
accepting new PRs or implementing new features", since its first release in July
2024. Operationally: the docs require re-init between minor version bumps and a
migration notebook between major bumps, "which will overwrite your configuration
and prompts" — so **prompt files are part of the system state** and must be
version-controlled, or the index is irreproducible.

---

## 5. What the survey could not establish

Recorded because absence is evidence here too.

| Sought | Result |
|---|---|
| Published, community-agreed benchmark of **cyber-KG extraction** precision/recall/F1 | **NOT FOUND.** Every benchmark is per-paper and private; [S-202] shows they are not commensurable. |
| Cyber Ontology (CSCO) primary source | **NOT FOUND** — all four canonical URLs 404/empty. |
| W3C or OGC standard for a cybersecurity ontology | **NOT FOUND.** |
| TVA (Tenable) construction documentation or underlying paper | **NOT FOUND.** The GitHub page renders empty; the raw README is 14 bytes. |
| Microsoft Security Copilot / Google GUCC graph data model | **NOT FOUND** — no primary or peer-reviewed description exists. No claim is made about how these products build their graphs. |
| Content of the most-cited LLM CTI-KG paper (LLM-TIKG, 141 citations) | **NOT ACCESSIBLE** — closed access, no abstract in the bibliographic record, publisher behind a captcha. Its prominence rests on something unverifiable, which is a structural weakness of the field, not a fetch failure. |

**Caveats on this pass.** The knowledge-graph survey could not use a general web
search interface; discovery ran through the arXiv API, OpenAlex, Semantic
Scholar, and direct retrieval of standards, ACL Anthology, and official sites.
Coverage of arXiv is broad; coverage of vendor blogs and practitioner write-ups
is necessarily thin, and no practitioner post-mortem of a KG deployment that
failed was found. Roughly ten sources in the underlying survey were
bibliographic-only (paywalled or CDN-blocked) and are excluded from this
catalogue rather than registered as quotable.
