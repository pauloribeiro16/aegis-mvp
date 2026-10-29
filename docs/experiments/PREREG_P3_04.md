# PREREG_P3_04 — Onda C-2: re-calibração do braço qwen38 c1 com a ficha revista (sinal H2)

Version: 1.0.0
Status: FROZEN 2026-10-29, before the re-calibration job is submitted.
Upstream: [PREREG_P3_02.md](PREREG_P3_02.md) v1.2.0 — cujo falsificador H2 disparou (qwen38 c1, 66% `ROUTE_ORG` global, tecto 60%) e cujo §H2 manda "a revisão é da ficha (o sinal reabre a decisão, não se defende)" · [EXP_P3_02_results.md](EXP_P3_02_results.md) (a medição por domínio que nomeia o alvo).

---

## 1. What this preregisters

UM braço: `qwen3.8:27b` × Case 01, a re-corrida do `p3a_all` com a ficha
[PROM-P3A-01 v1.4.0](../pipeline/prompts/PROM-P3A-01_VERDICT_COVERAGE.md)
(a regra de acoplamento alargada ao ciclo de vida do produto: retenção/backup/
eliminação/portabilidade dos dados; secure update/dependências/releases do
software — CRA). O mesmo upstream fixado da Adenda 1.1.0, a mesma seed 42 /
temp 0.2 / `v0_source=frozen`; fork limpo `run_p304_qwen38_c1`.

**O controlo é intra-braço:** o resultado v1.3.0 do MESMO braço (mesma seed,
mesmo upstream, jobs 2160543) já medido — 66% global, D-05 4/7 (57%), D-07
4/5 (80%). Uma diferença entre corridas é a ficha e só a ficha.

n=1: o falsificador é sobre ESTE braço e ESTA ficha. Casos 02/03 não
re-correm (não têm falsificador; a banda registada é Case-01-shaped).
muse c1 não re-corre (passou a banda em v1.3.0; re-corri-lo seria gastar
GPU num braço sem sinal).

## 2. Hypotheses, predictions, falsifiers

- **H1:** Com a regra de acoplamento estendida, o `ROUTE_ORG` global do braço
  cai para ≤ 60% (o tecto de aprovação do P3_02).
  - **Predição:** 50–60% global (o excesso v1.3.0 é de 6 pontos sobre o tecto
    e os alvos são ~10 linhas de 65; se a regra mover TODAS as linhas-alvo,
    cai ~15 pontos — se mover só metade, fica dentro por pouco).
  - **Falsificador:** `ROUTE_ORG` > 60% de novo ⇒ a lacuna NÃO é vocabulário
    da regra de acoplamento; a revisão seguinte é estrutural (exemplar no
    pack ou guard L0 na coluna Action), não mais uma extensão de lista.
- **H2 (alvo nomeado):** D-05 ≤ 29% org (gabarito 14% + 15pp) e D-07 ≤ 35%
  org (gabarito 20% + 15pp).
  - **Falsificador:** qualquer um acima do seu tecto ⇒ a regra não alcança
    esse domínio; regista-se qual.
- **H3 (regressão do contrato):** L0 à 1.ª tentativa ≥ 90% e 65/65 objectivos
  com veredicto — a ficha revista não fragiliza o contrato (o padrão do
  P3_02 foi: ficha maior, contrato mais forte).
  - **Falsificador:** L0 < 90% ou sub-domínio descartado.

## 3. Procedure

1. Fork limpo: `run_p304_qwen38_c1` = upstream do `run_p302_qwen38_c1`
   (`manifest.json` com run_id reescrito, `config.json`, `steps/{fact_sheet,
   selection.*, verdicts.*, goals/, phase2/}`, `outputs/phase2/`) — nada de
   `steps/phase3*`, `steps/phase3b*`, `outputs/phase3*`.
2. `sync_up` (transporta a ficha v1.4.0), `submit.sh p3a_all` com
   `MVP_RUN_ID=run_p304_qwen38_c1`; watcher compacto (agregação server-side,
   o contrato de custo do operador).
3. Análise em `EXP_P3_04_results.md` citando este pré-registo; entrada no
   `00_RESULTS.md` no dia da análise. Se H1 segurar, a ficha v1.4.0 é a
   candidata à Parte 2 (`PREREG_P3_03`) e às rondas G-P3-A.

## 4. Deviations

Nenhum à data do congelamento.

## 5. What this does NOT claim

- Não compara modelos (um braço, um modelo);
- não reabre a banda 25–60% para os Casos 02/03 (registada no P3_02 como
  Case-01-shaped, convenção por calibrar);
- não valida a qualidade das propostas (a ronda e o L2 são os instrumentos).
