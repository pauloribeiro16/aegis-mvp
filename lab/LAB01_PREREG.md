---
document_id: AEGIS-LAB-PREREG-01
title: 'Pré-registo LAB01 — um braço por modelo falhante, gates intactos'
version: 1.0.0
created: 2026-10-05
status: REGISTERED — before any run
upstream: 'lab/README.md · lab/BRIEFS.md · PREREG-M07 (aegis-models) · docs/experiments/00_RESULTS.md §M07'
---

# Prer-registo LAB01 — ajustes por modelo, gates intactos

## Questão

Cada modelo falha a pipeline de forma diferente (M07). Um ajuste de prompt/orquestração
dirigido à classe de falha de cada um consegue fazê-lo atravessar os MESMOS gates?

## Desenho

| Braço | Modelo | Caso | Variável isolada | Baseline (M07) |
|---|---|---|---|---|
| `lab01-qwen35-fence` | qwen3.5:27b | C1 | instrução p2: fence-first (o primeiro carácter da resposta é a abertura do bloco) | p2 contract-fail 3/3 (7/7 histórico) |
| `lab01-qwen35-demo` | qwen3.5:27b | C1 | instrução p2: demo de formato (header + linhas de exemplo com empresa fictícia) | idem |
| `lab01-glm47-substance` | glm-4.7-flash:latest | C1 | instrução p4: scaffolding de profundidade (pernas do dever: quem/o quê/medida/limiar) + §5 sempre | p4 20/38 carried |
| `lab01-nemotron-substance` | nemotron-3.5-lightning:30b | C1 | instrução p4: idem + quantidades só do fact sheet + 9 colunas exactas | p4 31/38 carried |
| `lab01-gemma4-precision` | gemma4:31b | C3 | instrução p4: ordem canónica das slots + R6 (quantidades do intake) + R8 (stub ≠ cartão) | p4 37/38 carried, p5 abort |

Tudo o resto constante: gates, parsers, packs, corpus, seed 42, temperature 0.2,
n=1 por braço, `MVP_PREAPPROVE_GATES=1`. **Predição nenhuma sobre os braços
qwen3.5** (primeira medição da classe); para os outros três, as previsões abaixo.

## Hipóteses e falsificadores

- **H-L2 (glm-4.7).** A sobre-compressão é instrução-endereçável.
  **Predição:** p4 carried ≥ 36/38 (o p5 monta). **Falsificador:** carried ≤ 20/38
  (nível M07) — a classe é de capacidade; o próximo braço é orquestração
  (decomposição por cartão Sub-SO, wave 2), não mais texto.
- **H-L3 (nemotron).** Idem com o reforço de quantidades/colunas.
  **Predição:** p4 carried ≥ 36/38. **Falsificador:** ≤ 31/38 (nível M07).
- **H-L4 (gemma4).** As 1–2 falhas residuais são endereçáveis por ênfase.
  **Predição:** 38/38 → deliverable. **Falsificador:** nova falha noutro
  sub-domínio — a resiliência é aleatória, não instrutível.
- **H-L1 (qwen3.5) — sem predição registada.** Desfecho medido: p2 passa em
  qualquer braço ⇒ a classe é instrução-endereçável; ambos falharem ⇒ é de
  capacidade e o caminho é o E-01 (saída schema-constrained), não texto.

## Custos

≈ 6–9 GPU-h (4 corridas C1 ~2h; 1 corrida C3 ~2.5h; as do qwen3.5 morrem cedo
se falharem).

## O que esta wave não é

Não compara braços do p4 (isso é EXP-04). Não valida o limiar 0,70 do M-14
(isso é a L2). Não promove nada para produção sem decisão do investigador
(lab/README.md §Constituição, regra 4).
