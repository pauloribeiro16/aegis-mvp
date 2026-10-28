# PREREG_P3_02 — Onda C: calibração multi-modelo das fichas da Fase 3 Parte 1

Version: 1.2.0
Status: FROZEN 2026-10-27, before the first `p3a_all` job of the calibration matrix is submitted. Adenda 1.2.0 (2026-10-28) after the first submission and before any job completed — see §5.
Frozen by: aegis-mvp executor, after the Onda A/B/C code landed (`f34b2bf`, `693779a`, `5b7dade`) and all 16 local test suites were green, and before any GPU time.
Upstream: [phase3_improvement_and_calibration_plan.md](../../../.gemini/antigravity/brain/be621b89-afc5-4c19-82cc-8acf552a9ede/phase3_improvement_and_calibration_plan.md) §Onda C (plano diretor; cópia das intenções em `docs/pipeline/03_PROMPT_CATALOG.md`) · [PREREG_P3_01.md](PREREG_P3_01.md) (a construção que esta calibração mede) · [METRICS.md](METRICS.md) M-26 (o limiar de colapso, incident-calibrated).
Model availability verified 2026-10-27: `qwen3.8:27b`, `muse-glimmer:30b`, `gemma4:31b` — os três manifestos presentes na cache partilhada do Deucalion (`ollama_data/models/manifests/registry.ollama.ai/library/`).

---

## 1. What this preregisters

A calibração multi-modelo das etapas 1.1–1.8 da Fase 3 Parte 1 sobre as
intervenções Onda C nas fichas (coluna `Action` enum pura com a regra de
acoplamento; fit criterion caixa-preta com o guard `check_fit_criterion_observable`;
SILENCE para princípios meta-metodológicos; identificadores só do vocabulário do
pack) e nos guards L0/L1, contra os modos de falha medidos em `run_p2enr_c1`
(52/65 objectivos despejados na organizacional; mecanismos pré-cozinhados no fit
criterion; permissões inventadas; fecho cosmético).

**Todos os jobs:** seed 42, temperature 0.2 (defaults medidos, AGENTS.md §-1),
`--v0-source frozen` (a baseline funcional do caso é idêntica em todos os braços
— a comparação é de modelo sobre a MESMA baseline, Onda A A.2).

## 2. Arms (congelados)

| Braço | Modelo | Casos | Tag | Orçamento |
|---|---|---|---|---|
| 1 (referência) | `qwen3.8:27b` | Case 01, Case 03, Case 02 | `exp_p3_02_qwen38_c1/c3/c2` | ~6–8 GPU-h (3 jobs `p3a_all`) |
| 2 (secundário) | `muse-glimmer:30b` | Case 01, Case 03 | `exp_p3_02_muse_c1/c3` | incluído acima (2 jobs) |
| 3 (contraste) | `gemma4:31b` | Case 01 | `exp_p3_02_gemma4_c1` | incluído acima (1 job) |

n = 6 corridas. Sem braço de prompt alternativo: as intervenções Onda C são a
ficha única; o que se compara são modelos. A ronda humana (Etapa 1.6) NÃO corre
nestes jobs: a cadeia pára em `p3a_round` PROPOSED (two-states), e os critérios
abaixo medem até ao estado proposto + a gate.

## 3. Hypotheses, predictions, falsifiers

### H1 — Passagem L0 à primeira tentativa

- **H1:** Com os guards Onda C nas fichas, ≥ 90% das chamadas de `qwen3.8:27b`
  e ≥ 85% das de `muse-glimmer:30b` passam L0 à primeira tentativa (sem ronda
  de reparo) nas etapas 1.2/1.3/1.4.
- **Predição:** qwen3.8 ≥ 0.90 em todos os casos; muse ≥ 0.85; gemma4 medido
  sem limiar (braço de contraste — serve de variabilidade, não de aprovação).
- **Falsificador:** qwen3.8 < 90% à 1.ª tentativa — a ficha ou o guard está
  errado, e o limiar NÃO se move (doc 08 §7); regista-se qual campo falhou
  (Action fora do enum? fit criterion com mecanismo? identificador inventado?)
  porque o campo da falha diz qual intervenção não ensinou o suficiente.

### H2 — Equilíbrio na triagem (fim do mode collapse)

- **H2:** Com a coluna `Action` enum + regra de acoplamento, a partição da
  Etapa 1.2 cai na banda `ROUTE_ORG` 25–60% com `PROPOSE_PRODUCT` ≥ 25%.
- **Predição:** qwen3.8 dentro da banda nos três casos; muse dentro da banda
  em dois de dois.
- **Falsificador:** `ROUTE_ORG` > 60% em qualquer caso de qwen3.8 — a regra de
  acoplamento não moveu o comportamento e o alerta M-26 dispara; a revisão é
  da ficha (o sinal reabre a decisão, não se defende). NOTA DE REGISTO: o
  alerta de gate fica em 65% (M-26); a banda 25–60% é o critério de aprovação
  deste experimento — um braço pode passar a gate e falhar o experimento.

### H3 — Fecho estrutural (a gate mede o conteúdo)

- **H3:** Cada corrida `p3a_all` termina com a gate no estado PROPOSED honesto
  e, aplicados os veredictos da ronda 1 nos jobs de calibração seguintes,
  `G1..G6 = CLOSED` e `T1..T6 = 0 findings` sobre as entregas geradas
  (`Doc00..Doc03` completos, não bullets).
- **Predição:** os 15 achados de integridade de `run_p2enr_c1` (2×T2, 13×T5)
  não se reproduzem nas corridas novas (a junção S20 e a citação de âncoras
  S5/S6 fecham-nos à nascença).
- **Falsificador:** qualquer corrida nova com achados T2/T5 — a reparação
  Onda A não cobriu a classe; o finding diz onde.

### H4 — Qualidade semântica (L2, dependente de sessão humana)

- **H4:** Na rubrica [`L2_RUBRIC_F3.md`](L2_RUBRIC_F3.md), a amostra de
  propostas da Onda C atinge média global ≥ 2.3/3.0 com 0 notas `1` na
  Dimensão 2 (testabilidade caixa-preta).
- **Dependência declarada:** a sessão de pontuação L2 do investigador
  (~2 h) é o instrumento — **este critério fica EM ABERTO até essa sessão**;
  os critérios H1–H3 são automáticos e não esperam por ela. O resultado do
  H4 entra no doc de resultados como secção própria, mesmo que chegue depois.

## 4. Procedure (as submissões, por ordem)

1. `sync_up` do repo para o cluster; `bash -n` nos scripts; preflight local.
2. Braço 1, um job de cada vez (sequencial — um Ollama por nó):
   `submit.sh --case Case_01_TinyTask_SaaS --stage p3a_all --model qwen3.8:27b
   --seed 42 --temp 0.2 --v0-source frozen --tag exp_p3_02_qwen38_c1`;
   depois c3, depois c2 (`--wall 08:00:00`).
3. Braço 2 (c1, c3) e braço 3 (c1) pela mesma ordem.
4. Watchers por job; `sync_down.sh` no fecho; cada corrida lida
   `AEGIS_P3_GATE state=...` no log do `p3a_gate`.
5. Análise em `EXP_P3_02_results.md` citando este preregisto (v1.0.0);
   entradas em `00_RESULTS.md` no dia da análise — resultado negativo é
   resultado.

## 5. Deviations

**Adenda 1.1.0 (2026-10-27, antes da 1.ª submissão) — fixação do upstream.**
`p3a_all` num run novo exigiria p1→fase2 primeiro, e cada modelo geraria o SEU
fact sheet e as SUAS entregas da fase 2 — a comparação ficaria confundida pelo
upstream. Todos os braços partilham assim o MESMO upstream qwen3.8:27b seed 42
por caso, copiado do run base enriquecido da P2-02 para o fork do braço
(`run_p302_<modelo>_<caso>`): `steps/{fact_sheet.yaml, selection.*, verdicts.*,
goals/, phase2/}` + `outputs/phase2/`. A V0 é a do caso (`--v0-source frozen`).
O que varia entre braços é SÓ o modelo das chamadas p3a — a mesma partição de
objectivos, as mesmas âncoras publicadas, a mesma baseline funcional.
Bases: Case 01 → `run_p2enr_c1` (270 RULE-*), Case 02 → `run_p2c2` (340),
Case 03 → `run_p2c3` (422), todas seed 42 / temp 0.2 / qwen3.8:27b.

Nenhum outro desvio à data do congelamento. Desvios registam-se AQUI por
adenda versionada (nunca em silêncio), e o doc de resultados cita a versão
que vigia quando cada job correu.

**Adenda 1.2.0 (2026-10-28, depois da 1.ª submissão, ANTES de qualquer job
concluir) — a ficha chega inteira ao modelo.** Os seis jobs da 1.ª submissão
(`2160106`–`2160111`) abortaram todos em `p3a_org_cluster` com
`ValueError: unknown step` — os construtores de pack das etapas novas
(Ondas B e D) tinham sido escritos em `compose_call` em vez de `build_pack`,
e nenhuma chamada chegou ao modelo (0 propostas). A auditoria achou a causa
raiz e mais duas, ambas measured na mesma sessão:

1. **O contrato da ficha não chegava ao modelo.** `parse_ficha` extraía só o
   `## Prompt body` (e exigia o marcador `>`), pelo que as secções
   normativas — os cinco verditos, a regra de acoplamento da coluna
   `Action`, a tabela de neutralidade R5, o vocabulário `RN (a derivar)` —
   ficavam na ficha de engenharia e nunca no prompt. Seis das quinze fichas
   da Fase 3 tinham `prompt_body` vazio: o modelo recebia um esquema de
   saída e zero instrução. **Medido:** `PROM-P3A-01` enviava 1 916 chars
   (17% da ficha); envia agora 8 253. **As fichas da Fase 1/2 não mudam
   (byte-idêntico) — os seus prompts são medidos e congelados**; só as
   fichas da Fase 3 declaram `body_is_instruction: true` e assim passam a
   ler o corpo inteiro. As fifteen fichas da Fase 3 subiram de versão
   (1.x.0 → 1.x+1.0) com linha de changelog, e o digest de prompts que cada
   corrida grava no `manifest.json` passa a reflectir a nova ficha.
2. **Os defeitos reparáveis do `p3a_map` eram medidos DEPOIS da chamada.**
   Uma linha sem âncora citada custava o sub-domínio inteiro (o estágio
   apanhava o achado e descartava-o). Passaram para dentro de `_validate()`,
   onde vive a ronda de reparo L0: o modelo é re-preguntado com o defeito
   nomeado, em vez de o sub-domínio ser descartado.

**Efecto sobre as hipóteses:** H1, H2 e H3 medem o comportamento do modelo
perante a **ficha** — e a ficha mudou (era o instrumento defeituoso). As
hipóteses, os limiares e o critério de aprovação (banda `ROUTE_ORG` 25–60%
global) **não mudam**; o que muda é o instrumento, e é isso que a calibração
deveria medir. O alerta M-26 fica **como está registado** (D-02..D-07): foi
medido contra os dados dos seis braços e **discrimina** — 68–78%
`ROUTE_ORG` nos braços colapsados (dispara) e 12–21% nos saudáveis (silêncio).
Um âmbito mais estreito (os domínios de produto D-01, D-03, D-05, D-07) foi
medido também e mediu **pior** (50–59% nos colapsados, porque o D-03 ficou
em 25%/0% enquanto o D-01 colapsava a 62–75%) — por isso **não foi adoptado**.

**Medição por domínio (a distribuição real do colapso, Caso 01 vs Caso 03):**
no Caso 01 o modelo despejou para a lane organizacional D-02 (100%), D-04
(88–100%), D-06 (100%), D-08/D-09 (100%), D-10 (83%), D-07 (80–100%) e **D-01
(62–75%, contra 0/7 no gabarito manual)**; no Caso 03, o mesmo código com a
mesma ficha dá D-01 0%, D-05 0%, D-07 0%, D-10 14%. O colapso é do **Caso 01**
(uma SaaS de 8 pessoas), não do código. Esta distribuição é o que a
calibração tem de reproduzir — e é o que a ficha reparada deve mudar.

**Nenhum job desta matriz chegou a correr uma chamada**: as seis submissões
abortaram antes da primeira chamada, pelo que não há resultado a reconciliar.
Nenhum resultado anterior é invalidado — nenhum existia.

## 6. What this does NOT claim

- Não compara prompts (uma ficha só); não mede a ronda humana (os jobs param
  em PROPOSED); não valida a Parte 2 (Onda D, `PREREG_P3_03.md`); o limiar
  L0 de `gemma4:31b` é descritivo, não critério de aprovação.
