---
document_id: AEGIS-EXP-METRICS
title: 'Metrics — every enforced threshold with its GQM question and declared basis'
version: 1.1.0
created: 2026-10-04
status: ACTIVE
upstream: 'AGENTS.md §-2 (rule 2), AEGIS-RES-10, ADR-2026-10-05_pack-budget-and-context-policy'
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
| M-09b | num_predict p4 — distribuição real por chamada | 16384 reservado · 2762 média · 4059 máximo na corrida completa | `pipeline/src/steps.py:40-41`; medido em `run_m04_muse_c3_r01_1983144` (job 1983144, 39 chamadas p4, 107,753 tokens de saída) | O valor é dimensionado pela mediana da etapa ou pelo pior sub-domínio? | `convention` — o 16384 é um **pior caso por etapa carregado 38 vezes**, não uma medição: 5.9× a média e 4.0× o máximo desta corrida (638,976 tokens reservados contra 107,753 produzidos). A justificação upstream é honesta mas pontual: o máximo do programa é 15,733 tokens (`p4_D-09_3`, job 1978919), ou seja 1.04× do valor. Nenhuma distribuição por etapa foi medida → **ADR-012 D5** (right-sizing por medição) → E-15 |
| M-10 | context escalation | ×1.15 + 2000 tokens → 65536 | `pipeline/src/steps.py:935-938` | O pack estimado cabe no num_ctx da etapa? | `convention` — desdobrada em M-10b (divisor), M-10c (factor), M-10d (constante) e M-10e (tecto da escada), que registam a base de cada parcela |
| M-10b | divisor chars/token | `// 4` | `pipeline/src/steps.py:935` | A estimativa de tokens do pack é correcta para o modelo que a vai receber? | `convention` — o próprio comentário em `steps.py:929` admite "chars/4 underestimates the real tokenizer". Medido nas classes de pack p4/p4t (>100 kB, todas as corridas, `attempt1_prompt_tokens` vs `system_chars + user_chars`): gemma4:31b mediana 3.87 (n=53, 3.55–3.98), qwen3.8:27b mediana 3.89 (n=225, 3.62–4.05), muse-glimmer:30b mediana 4.18 (n=80, 3.91–4.27). As medianas diferem 8.0 % e o intervalo observado cobre 20.2 %; o código **não** modela a dependência do modelo → **ADR-012 D5** |
| M-10c | factor de segurança da estimativa | ×1.15 | `pipeline/src/steps.py:936` | A margem absorve o erro do divisor? | `convention` — com M-10b o factor efectivo é 0.2875·c: **1.021** a c=3.55 (2 % de folga) e **1.228** a c=4.27. Um escalar não cobre um tokenizer dependente do modelo → E-15 |
| M-10d | constante de folga | +2000 tokens | `pipeline/src/steps.py:936` | A margem absorve o resto do envelope da chamada? | `convention` — nunca medida contra uma distribuição de prompts; nenhum run chegou a demonstrá-la necessária ou suficiente → E-15 |
| M-10e | tecto da escada de contexto | 131072 | `pipeline/src/steps.py:937` | A escada para num tecto real ou numa política? | `convention` — **literal cru no código**, não lido de `aegis-models/MODELS.yaml` (que regista `native_ctx` 32768 para a referência qwen3.8, 16384 para várias candidatas e `unknown` para cinco) nem de qualquer manifest de modelo. Escada exercitada: o rung 131072 foi atingido pelo maior prompt já enviado (50,054 tokens reais, `p4_D-09_1`, `run_sec03_p1_1979371`); o rung 65536 absorveu o p4t aos 46,978 tokens reais. Nenhum run demonstrou que um rung acima seria necessário → **ADR-012 D1** |
| M-10f | exaustão da escada deixa rasto? | não (hoje) | `pipeline/src/steps.py:939-942` (o `raise` precede `inputs/` em `:944-948` e o record em `:950`) | Uma etapa abortada por orçamento é investigável como as outras? | `convention` — nenhum `inputs/`, nenhuma linha de `trace.jsonl`, nenhuma entrada de stage no manifest; só a string da excepção. **ADR-012 D5** move o `raise` para depois do rasto (adiciona forense, não um gate) |
| M-11 | tension-section trigger | ≥2 regulações confirmadas | `pipeline/src/steps.py:721-726, 1139` | A corrida tem tensões multi-regulação a resolver? | `structural` (§4 do contract) |
| M-12 | max 2 anchors por goal | 2 | `SPEC.md` §7 R2 (linha ~261) | O goal fica ancorado sem sobrecarga de verificação? | `policy (SPEC §7)` — camada normativa, não gate de código; SPEC está congelado (R5) |
| M-13 | doc_lint / T1–T7 checks | sem thresholds numéricos | `scripts/doc_lint.py`, `scripts/check_traceability.py` | O documento e a cadeia referencial são íntegros? | `structural` — sem parâmetros sintonizáveis; **mutation-tested**: 36/36 falhas semeadas detectadas, 0 falsos positivos (EXP-05a) |
| M-14 | calibration mix (anti-lazy-defaulting) | `(unchanged+verbatim)/n > 0.70` em runs com n ≥ 10 → WARN não bloqueante | `pipeline/src/quality.py` (`score_run` → `calibration`), `pipeline/src/validate.py:316-334` | O modelo calibrou os goals ou refugiou-se no valor por omissão? | `convention` — o 0.70 **não é medido**: é ancorado às duas corridas entregues com mix mais saudável (gemma4 C1 0.35, muse C3 0.45) e dispara em TODAS as corridas da referência medidas (0.91 menu/C1, 0.94 regra/C2, 0.92 ref/C3, 0.99 badge/C3 — job 1983666). Se 0.70 separa preguiça de deveres que genuinamente se aplicam tal como escritos é exactamente o que a **pontuação cega L2** (`PLANO_FECHO.md` 4.1, 450 linhas por lançar) tem de decidir — por isso é WARN e não gate. **Confound de vocabulário:** corridas anteriores à m06 não tinham as opções `proportional`/`inherited` (instrumento `unchanged/narrowed/flagged`), pelo que a sua quota de `unchanged` não é directamente comparável com corridas do instrumento badge; os digests `p4_instruction`/`p4t_instruction` (compose.py `prompt_digests`) distinguem os instrumentos a partir da m06+1 |
| M-15 | contradição implicação↔ajustamento | implication com delegação (`cloud provider\|managed service\|third-party\|vendor\|supplier\|managed\|delegat(ed?\\|ing)\|external host(ing)?\|saas provider`) + badge `unchanged`/`verbatim` → WARN com ids | `pipeline/src/quality.py` (`contradiction_rows`), `pipeline/src/validate.py:322-330` | A narrativa e a classificação dizem coisas incompatíveis? | `convention` — regex por palavras-chave, não NLI: é grosseira (o "managed" legítimo de "managed cloud encryption" conta) e só plenamente significativa sob o instrumento badge (onde `inherited` existe como saída correcta); nas corridas de vocabulário antigo as contagens (ex.: muse r02 29 hits) medem os limites do vocabulário antigo, não desleixo. A versão NLI do check é trabalho futuro (E-26Shape); sem base para threshold de severidade → WARN |

## Rows pending promotion

Rows M-02 e M-03 (e a escolha 0.30/0.88 em geral) aguardam **E-10** — medir a
taxa de disparo e a distribuição dos valores no corpus — que as converte de
`convention` para `measured` ou as recalibra. A inconsistência M-05/M-05b
aguarda decisão própria (regista-se; não se resolve por omissão).

Rows M-09b e M-10b..M-10f (o orçamento de entrada e o de saída, Added
2026-10-05) aguardam **E-15** — evidence-chain retention under the pack budget,
já preregistrado (`docs/research/04_EXPERIMENT_BACKLOG.md:704-750`), 0 GPU-h na
passagem por travessia, sem dependências. É o experimento que decide se a
escada de contexto é a restrição, e as cinco linhas foram acrescentadas com
`convention` declarada precisamente porque nenhuma tinha base. **Nenhuma delas
deve ser citada como evidência de qualidade até E-15 correr**; o que hoje
sustenta qualquer afirmação sobre contexto são as medições de run citadas em
cada linha, não os valores. Ver `docs/decisions/ADR-2026-10-05_pack-budget-and-context-policy.md`.

