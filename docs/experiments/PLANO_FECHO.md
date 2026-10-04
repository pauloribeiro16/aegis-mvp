---
document_id: AEGIS-EXP-PLAN
title: 'Plano de fecho do programa experimental — todos os modelos, todos os casos'
version: 1.0.0
created: 2026-10-04
status: ACTIVE — execução lançada
sources: 'docs/research/sources.yaml'
upstream: '[00_RESULTS.md](00_RESULTS.md) · [04_EXPERIMENT_BACKLOG.md](../research/04_EXPERIMENT_BACKLOG.md)'
---

# Plano de fecho — todos os modelos em todos os casos

**Decisões que fixam este plano (2026-10-04):**

1. **O braço agentic sai do programa.** O EXP-03 fica com o braço agente
   fechado em 7/15 terminações limpas, como está registado; nenhuma corrida
   agentic nova. O E-11 (compressão de contexto no agente) cai do backlog por
   ficar sem sujeito. O histórico agentic permanece no inspector como
   evidência — não se apaga.
2. **Todos os modelos correm todos os casos** — a matriz 7 modelos × 3 casos
   (M02 no caderno de modelos), semeada, `n=2` por célula na triagem.
3. **Fechar o backlog E** na ordem do valor, com o playbook da §4 para os
   contratempos.

## 1. Estado de partida (2026-10-04, medido)

| Item | Estado |
|---|---|
| Fila do cluster | **vazia** — zero jobs |
| Corridas | 150 directórios; 132 reais; 72 entregues, 60 abortadas |
| Caso 02 | **entregue** (rc=0, 4 regulamentos) |
| Caso 03 | **bloqueado no p4 D-04.3**: pack de 136 kB, 5 cartões; o modelo escreve as 5 filas certas + §5 e continua a escrever até ao cap de 16 384 tokens |
| Matriz m03 (pós-revisão do prompt) | gemma4 2/2, muse 2/2, glm47 0/2 (sobre-compressão no p4), nemotron 0/2 (linha de 10 colunas), qwen3.5 0/2 (p2 sem bloco), ornith 0/1 histórico (crash CUDA) |
| Pontuação cega L2 | pack pronto (30 docs, 450 linhas), **0 notas lançadas** |
| EXP-04 | código pronto, nunca lançado |
| Correcção do prompt de selecção | verificada no m03: falha de contrato 10/10 → 0/4 |

## 2. Fases

### Fase 0 — agora, custo zero (executada neste commit)

- Corrigir `sync_watch.sh`: considerava uma corrida terminada ao primeiro
  `stage finished rc=` — que aparece em TODAS as etapas — e por isso puxou 4
  corridas a meio. Passa a exigir a linha `END=…EXIT_CODE=` do trap do sbatch.
- Cláusula TERMINATION na instrução do p4 (o desbloqueio do Caso 03, §3.1).
- Este documento.

### Fase 1 — validações pequenas (1 corrida por braço, ~2 GPU-h)

| # | O quê | Critério de saída |
|---|---|---|
| 1.1 | Caso 03, qwen3.8, semente 42, retomando `run_sec03_p1_1979371` a partir do p4 (o `all` salta o que já está validado em disco) | `EXIT_CODE=0` e `doc02_adjusted_goals.md` escrito — o Caso 03 desbloqueia |
| 1.2 | EXP-04 braço `menu`: 1 corrida, Caso 01, semente 42 | L1 PASS; conta `narrowed` no relatório |
| 1.3 | EXP-04 braço `clarified`: 1 corrida, Caso 01, semente 42 | idem |

Se 1.1 falhar de novo: §4 linha "pack grande no p4" — a decomposição
por regulamento é a próxima medida, e é uma meia jornada de código.

### Fase 2 — a matriz M02 (todos os modelos × todos os casos, ~14 GPU-h)

7 modelos × 3 casos, **semeada (42)** — a semente torna cada falha
reproduzível e cada sucesso verificável, que é o que uma matriz de cobertura
precisa; a variância natural dos modelos já foi medida no m01 sem semente.

- **Triagem: `n=1` por célula primeiro (21 corridas).** Uma célula que aborta
  fica registada com a causa; só as células que passam recebem a 2.ª repetição
  (mais ~10 GPU-h). Isto segue a disciplina escalonada: nada de n=2 sobre uma
  célula que ainda não provou que corre.
- Cada célula é uma corrida completa (`p1` + `all` encadeados, gates
  pré-aprovados). Uma falha no p4 ainda entrega p1–p3 como evidência.
- **ornith**: 1 tentativa num nó diferente; se o crash CUDA se reproduzir,
  fica **runtime-incompatível** no `MODELS.yaml` com o job id, e a matriz
  efectiva é de 6 modelos. Não se persegue mais.
- **qwen3.5**: falha no p2 por classe de formato em 4/4 corridas. Corre-se
  mesmo assim e a célula regista `contract-fail at p2` — é o caso de teste
  vivo do E-01. Sem E-01, a linha do qwen3.5 na matriz é a coluna vazia que
  motiva o E-01.
- Os resultados entram no `aegis-models/results/` e no site (aba
  Experimentos → Rastreio de modelos, que passa a ter também o eixo dos casos).

### Fase 3 — profundidade nos sobreviventes (~25 GPU-h)

| # | O quê | Custo |
|---|---|---|
| 3.1 | Deep dive gemma4 e muse no Caso 01: estender m03 de r02 → r15 (o instrumento não mudou; é continuação, não tier nova) | 26 corridas ≈ 18 GPU-h |
| 3.2 | Referência qwen3.8 n=5 nos Casos 02 e 03 (a referência por caso, para as células dos modelos terem contra quem ser comparadas) | 8 corridas ≈ 6 GPU-h |
| 3.3 | 2.ª repetição das células da matriz que passaram a triagem | ~10 corridas |

### Fase 4 — o que não precisa de GPU, por ordem de desbloqueio

| # | O quê | Porquê primeiro |
|---|---|---|
| 4.1 | **Pontuação cega L2** (~2 h do investigador; 450 linhas esperam) | Sem ela, retenção não distingue restatement fiel de cópia. Bloqueia o veredicto do EXP-03 E a leitura da matriz |
| 4.2 | E-17 — auditoria do juiz L3 (temperatura/seed fixados) | Custo zero; sem o seu piso de ruído, nenhum resultado pontuado por juiz é interpretável |
| 4.3 | EXP-04 bateria (n=5 por braço, semeada) | Depois das validações 1.2/1.3; e o braço `menu` é o teste directo para a sobre-compressão do glm47 |
| 4.4 | E-19 + E-20 (mutação dos gates; cobertura dos packs) | Custo zero; o E-19 ficou mais urgente com os gates novos desta semana |
| 4.5 | E-01 — saída restringida por schema, protótipo no p2 | A classe de falha do qwen3.5 (e do nemotron no p4). Protótipo com 1 corrida; só se estende se provar |
| 4.6 | Relatórios: `EXP04_results.md`, matriz no `EXP03a` §7+, painel `00_RESULTS` | No fim de cada fase, não no fim do programa |

## 3. Orçamento e calendário

≈ **60 GPU-h** no total. A partição `dev-a100-80` corre 5–6 jobs em paralelo
sem pressão (havia 12 em simultâneo esta semana), logo **2–3 noites**. A fila
está vazia agora — é a altura de encher.

## 4. Playbook de contratempos

A regra que governa tudo: **uma falha do gate é um dado, não um contratempo.**
Registra-se a causa, repete-se uma vez com uma correcção dirigida, e NUNCA se
afrouxa uma validação para uma corrida passar (R10 — validação circular).

| Sintoma | Causa provável | Acção imediata | Nunca fazer |
|---|---|---|---|
| `FATAL: model manifest not in shared cache` | tag truncada (o `%%:*` clássico) ou pull em falta | o preflight do `submit.sh` já lista o que existe; fazer pull no login node com o binário 0.32.13 | — consertar a tag por inspecção de string |
| `no ```markdown fenced block found` (p2/p3) | a classe de formato; qwen3.5 é o caso sistemático | 1 retry (o repair já é restrito); se persistir, registar `contract-fail` e deixar a célula vazia | — reescrever o parser para aceitar prosa |
| p4: `keeps N of the Sub-SO's M obligation terms` | sobre-compressão (capacidade do modelo) | 1 tentativa com o braço `menu` do EXP-04; se falhar, corte registado com o job id | — baixar o limiar do gate |
| p4: `row has 10 columns, expected 9` | lapso de formatação | o repair cobre; se semeada e reproduzível, registar | — relaxar o parser de tabelas |
| `CUDA illegal memory access` (ornith) | runtime do modelo no cluster | 1 retry noutro nó; se reproduz, runtime-incompatível | — recompilar/re-puxar em loop |
| Pack grande no p4 (≥4 regulamentos): o modelo não para | a terminação, não o tamanho (D-02.1 com 125 kB respondeu limpo) | a cláusula TERMINATION (Fase 1.1); se falhar, **decomposição por regulamento** — uma chamada por cartão Sub-SO nos casos com ≥4 confirmados | — subir o `num_predict` para mascarar |
| Corrida sincronizada a meio aparece como abortada | o watcher marcava fim pela linha de stage | já corrigido (Fase 0): exige `END=…EXIT_CODE=` | — confiar numa corrida sem manifest completo |
| ssh drops / `MaxStartups` | demasiadas ligações concorrentes | submissões em série com `sleep 3`; um ssh por lote | — 20 ssh em paralelo |
| `Job dependency problem` no afterok | dependência sobre um job que o controller já esqueceu | submeter sem a dependência e encadear por artefacto | — reencadear sobre job terminado há dias |
| `done_reason=length` no trace | tecto de `num_predict` atingido | é um dado; ver linha "pack grande" se for o p4 dos casos grandes | — subir o cap antes de ver a causa |
| Contexto: escalada de `num_ctx` até 262144 e ainda trunca | pack fora de orçamento | registar a célula como `context-fail`; é input para o E-15 | — cortar o corpus à mão |

## 5. O que fica registado onde

- **Cortes e causas por modelo** → `aegis-models/MODELS.yaml` + `results/*.tsv`
- **Veredictos por experiência** → `docs/experiments/EXP0*_results.md` + painel
- **As corridas** → `$AEGIS_RUNS_DIR` (nunca no repo); o site é a vista
- **O pré-registo da matriz** → `aegis-models/PREREG-M02.md` (antes da Fase 2)

## 6. Fim do programa

O programa fecha quando: (a) a matriz M02 tem uma célula registada por
modelo × caso — entregue ou com causa; (b) o EXP-04 tem veredicto; (c) a
pontuação cega distingue os braços; (d) os E-17/E-19/E-20 têm relatório. Nessa
altura o painel `00_RESULTS.md` passa de "results so far" para conclusões, e o
backlog E-01..E-22 é reavaliado com o programa fechado.
