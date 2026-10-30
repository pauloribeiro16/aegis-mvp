# PREREG_P3_04 — Onda C-2: re-calibração do braço qwen38 c1 com a ficha revista (sinal H2)

Version: 1.2.0
Status: FROZEN 2026-10-29, before the re-calibration job is submitted.
Adenda 1.1.0 (2026-10-30): the H1/H2 falsifiers FIRED on the counted run (job 2165434: global 68%, D-05 4/7, D-07 4/5 — identical to v1.3.0). The falsifier's own contingency (structural revision, not more prose) is the next run, frozen in §5 addendum below BEFORE that run.
Adenda 1.2.0 (2026-10-30): the structural revision was implemented and MEASURED INERT — the diagnosis and the two corrections (granularity, threshold) are in §5 below. The next run is the third attempt on the same instrument, and it is the last: if it does not move the routing, the conclusion is that the routing is a STABLE PRIOR of the model and the instrument has to change the decision procedure (a worked example in the pack, or a derived routing), not the prompt.
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

**Adenda 1.1.0 (2026-10-30) — a revisão estrutural que o falsificador obriga.**
O job 2165434 mediu o instrumento v1.4.0 e o falsificador disparou outra vez:
global **68%** (v1.3.0: 66%), D-05 **4/7** e D-07 **4/5** — **uma linha
inalterada** em todos os domínios-alvo. Conclusão: a prosa da regra de
acoplamento não é o mecanismo; o modelo tem um juízo prévio sobre que
obrigações são organizacionais e uma frase mais longa não o move. É
exactamente a condição escrita no falsificador do §H1 ("a revisão seguinte tem
de ser estrutural… não mais uma extensão de lista").

**O que muda: uma guarda de reparo L0** (`verdict_defects`, chamada de dentro
de `_validate`), que devolve um defeito de reparo quando um sub-domínio
recebe mais de 65% de `ROUTE_ORG` — pedindo ao modelo que reavalie quais
dessas obrigações regulam dados, estado, sessões, pacotes ou artefactos de
release do software descrito no V0.

**Âmbito da guarda — medido, não escolhido.** A guarda aplica-se **apenas** a
D-01, D-03, D-05 e D-07: os quatro domínios onde a matriz manual do Caso 01
diz que a obrigação é do produto (0%, 25%, 14%, 20% organizacional). **Não**
se aplica a D-02 (100% organizacional no gabarito), D-04 (75%), D-06 (80%),
D-08 (67%), D-09 (100%) nem D-10 (83%): lá o veredicto organizacional é a
resposta certa, e uma guarda que os empurrasse para produto seria o mesmo
erro pelo lado oposto. (O texto do plano director nomeava "D-02..D-05 ou D-07";
incluir D-02 seria contrariar o gabarito — é uma correcção deliberada, com a
base indicada.)

**Caracterização do guard: suave.** A guarda dispara **uma vez**: se a
re-pedida ao modelo não resolver, a resposta do modelo é aceite e o achado
fica registado como aviso na corrida. Perder o sub-domínio inteiro (11
objectivos sem veredicto) seria pior do que um mau encaminhamento visível.

**Adenda 1.2.0 (2026-10-30) — a revisão estrutural foi medida INERTE, e o
diagnóstico é de granularidade.** O job 2166542 (`run_p304b_qwen38_c1`, a
revisão estrutural tal como foi congelada na Adenda 1.1.0) mediu routing
**bit-idêntico** ao run sem guarda (68%; D-05 4/7; D-07 4/5) e a trace
registou **zero re-pedidas L0** — a guarda nunca disparou. Duas causas, ambas
medidas:

1. **Granularidade.** A chamada (e portanto a reparação L0) é por
   **sub-domínio**: `verdicts_D-07_1.json` tem 2 linhas, `_2` tem 1. O
   colapso é um padrão de **domínio** (D-07 é 4/5Across D-07.1..4). A guarda
   via 1–2 linhas e o seu mínimo de 3 nunca era atingido. **Correcção:** a
   guarda passa a ver o domínio (as linhas já julgadas dos sub-domínios
   irmãos entram na contagem).
2. **Limiar.** 65% ficava **acima** do D-05 colapsado (57%) — nunca o
   desafiava. **Base medida** (os seis braços da calibração): os braços
   saudáveis medem no máximo 28% organizacional nestes domínios (Caso 02
   D-05 2/7; Caso 03 D-01 1/14, D-03 0/14, D-05 0/7, D-07 1/10) e os
   braços colapsados do Caso 01 medem 57% (D-05) e 80% (D-07). **Limiar
   novo: 40%**, que separa com margem dos dois lados (M-27 actualizado).

**Previsão e falsificador desta adenda** (re-submissão `run_p304c_qwen38_c1`,
mesmo upstream, mesma seed):
- **H4:** a guarda move D-05 e D-07 para ≤ 29% e ≤ 35% e o global para ≤ 60%.
  - **Falsificador:** D-05 ou D-07 inalterados ⇒ o modelo ignora também a
    instrução de reavaliação, e a lacuna é de JUÍZO (o modelo tem uma crença
    estável sobre organização) — a revisão seguinte tem de ser de outra
    natureza (exemplar no pack, ou a triagem passa a ser derivada do V0 e
    não de uma leitura do modelo). **Este é o ÚLTIMO teste do instrumento
   actual**: se falhar, a conclusão é científica e fecha a via da prosa.
- **H5 (regressão):** L0 1.ª tentativa ≥ 90%, 65/65 objectivos com veredicto,
  e **zero sub-domínios descartados** (a guarda não pode custar objectivos).

## 5. What this does NOT claim

- Não compara modelos (um braço, um modelo);
- não reabre a banda 25–60% para os Casos 02/03 (registada no P3_02 como
  Case-01-shaped, convenção por calibrar);
- não valida a qualidade das propostas (a ronda e o L2 são os instrumentos).
