---
document_id: AEGIS-EXP-METRICS
title: 'Metrics — every enforced threshold with its GQM question and declared basis'
version: 1.0.0
created: 2026-10-04
status: ACTIVE
upstream: 'AGENTS.md §-2 (rule 2), AEGIS-RES-10'
---

# Metrics — thresholds, questions, and the basis of each floor

**What this is.** The GQM table the §-2 contract (rule 2) requires: every
numeric parameter applied by a gate in this pipeline, with the question it
serves, where it lives in code, and — the column that matters — the **basis**
of its value. Three basis tags exist:

- `measured: EXP-xx` — the value is a measured result (cite the experiment).
- `incident-calibrated: job-xxxx` — the value was set in response to a
  concrete observed failure (cite the run/job).
- `convention` — the value is a calibrated choice with **no distribution
  measurement behind it**. A convention is legitimate; citing it as evidence
  of quality is not. Where a backlog experiment would convert it into a
  measured value, the row names it (`→ E-xx`).

**Maintenance rule.** A new threshold without a row here is a violation of
§-2 rule 2. When an experiment measures a `convention` row, update the row
and the code comment in the same session.

## The table

| ID | Parâmetro | Valor | Onde (file:line) | Pergunta (GQM) | Base |
|---|---|---|---|---|---|
| M-01 | seed / temperature | 42 / 0.2 | `pipeline/src/runconfig.py:50-51` | A corrida é reprodutível sem variância de serving? | `measured: EXP-02` — 15 runs byte-idênticos, retention sd 0.0000; greedy custou retention (0.7159 vs 0.7171) |
| M-02 | retention floor (obligation terms) | 0.30 | `pipeline/src/quality.py:86` (`RETENTION_FLOOR`, quality.py:261) | O adjusted goal mantém a obrigação do Sub-SO? | `convention` — calibrada no golden case ("around that band, not around word counts", quality.py:74-79); nunca medida em distribuição → E-10 |
| M-03 | near-verbatim similarity limit | 0.88 | `pipeline/src/quality.py:114` (`NEAR_VERBATIM_LIMIT`, quality.py:262) | O goal é uma reformulação, não uma cópia? | `convention, unmeasured → E-10` — a taxa de disparo nunca foi medida (EXP-01 registou máx 0.79 à mão, 65 rows) |
| M-04 | verbatim-embedding rejection | ≥2.2× comprimento | `pipeline/src/quality.py:110` | O goal reformula ou apenas incorpora o baseline? | `convention` |
| M-05 | implication min words (content gate) | 5 | `pipeline/src/quality.py:177` | A implicação é específica deste duty? | `convention` |
| M-05b | implication min words (doc-diff gate) | 4 | `pipeline/src/validate.py:298-299` | (mesma) | `convention` — **INCONSISTÊNCIA REGISTADA**: quality.py pede ≥5, validate.py ≥4. Unificar é decisão comportamental (afecta abortos); fica registada aqui, não executada sem experimento |
| M-06 | goal min words | 6 | `pipeline/src/validate.py:298-299` | O goal é uma frase substancial? | `convention` |
| M-07 | implication near-duplicate limit | 0.95 | `pipeline/src/quality.py:184` (`IMPLICATION_DUP_LIMIT`, quality.py:263) | Cada implicação é específica da sua linha? | `convention` — sem salto de identidade entre pares ("probe-caught 2026-10-03", quality.py:179-182) |
| M-08 | num_ctx por etapa | p1/p2/p3f: 16384 · p3/p4/p4t: 32768 | `pipeline/src/steps.py:34-35` | O contexto cabe sem truncar? | `incident-calibrated` |
| M-09 | num_predict por etapa | p1: 4096 · p2/p3f/p4t: 2048 · p3: 12288 · p4: 16384 | `pipeline/src/steps.py:40-41` | A resposta cabe sem truncar a tabela? | `incident-calibrated` — p4 16384 existe porque a 8192 a tabela truncava e o repair batia no mesmo tecto (job 1969983, D-08.3) |
| M-10 | context escalation | ×1.15 + 2000 tokens → 65536 | `pipeline/src/steps.py:923-925` | O pack estimado cabe no num_ctx da etapa? | `convention` |
| M-11 | tension-section trigger | ≥2 regulações confirmadas | `pipeline/src/steps.py:721-726, 1139` | A corrida tem tensões multi-regulação a resolver? | `structural` (§4 do contract) |
| M-12 | max 2 anchors por goal | 2 | `SPEC.md` §7 R2 (linha ~261) | O goal fica ancorado sem sobrecarga de verificação? | `policy (SPEC §7)` — camada normativa, não gate de código; SPEC está congelado (R5) |
| M-13 | doc_lint / T1–T7 checks | sem thresholds numéricos | `scripts/doc_lint.py`, `scripts/check_traceability.py` | O documento e a cadeia referencial são íntegros? | `structural` — sem parâmetros sintonizáveis; **mutation-tested**: 36/36 falhas semeadas detectadas, 0 falsos positivos (EXP-05a) |

## Rows pending promotion

Rows M-02 e M-03 (e a escolha 0.30/0.88 em geral) aguardam **E-10** — medir a
taxa de disparo e a distribuição dos valores no corpus — que as converte de
`convention` para `measured` ou as recalibra. A inconsistência M-05/M-05b
aguarda decisão própria (regista-se; não se resolve por omissão).
