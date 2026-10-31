---
prereg: PREREG_P3_03.md
prereg_version: 1.0.0
status: H1 SUPPORTED · H2 SUPPORTED · H3 SUPPORTED (medição corrigida 2026-10-31) · H4 holds structurally · H5 SUPPORTED — a Parte 2 corre nas duas armas; o registo fica PROPOSED até a ronda humana assinar
---

# EXP_P3_03 results — a Parte 1 da Onda E: ameaças, árvores e o registo que não fecha sem pessoas

Prereg: [PREREG_P3_03.md](PREREG_P3_03.md) **v1.0.0** (congelado 2026-10-27,
antes do primeiro `p3b_all`).

## O que correu

Dois braços sobre pacotes Parte 1 CONCLUDED (o `p3b_all` recusa o contrário —
two-states):

- **`run_p302_muse_c1`** (muse-glimmer:30b, Case 01): 21 ameaças (16 STRIDE +
  5 LINDDUN), 16 árvores (11 com caminho aberto), registo PROPOSED. Gate
  G8–G12 CLOSED, G7 OPEN (as 21 assinaturas humanas). **7/21 ameaças ficaram
  com mapeamento K3 vazio** (as 5 LINDDUN + `T-STR-008`/`T-STR-013`; o qwen3.8
  preencheu 31/31) — diferença real de qualidade entre armas, registada para
  a pontuação L2.
- **`run_p302_qwen38_c1`** (qwen3.8:27b, Case 01): 31 ameaças (só STRIDE), 17
  árvores, registo PROPOSED. Gate G8–G12 CLOSED, G7 OPEN (31 assinaturas).
  **O LINDDUN deste braço falhou por CONTEÚDO** (L0 recusou duas vezes: o
  modelo citou `SO-D-01.1-001` como mitigador fora do conjunto aceite) — a via
  de privacidade falta no braço e fica registada como diferença real de
  qualidade entre modelos. 1 árvore falhou (`T-STR-013`: resposta sem bloco
  cercado e a reparação L0 truncou no teto `num_predict=8192`), registada no
  stage result.

## H1 — L0 à primeira tentativa: SUPPORTED (com a base honesta)

Das 59 chamadas `p3b_*` que chegaram ao modelo com o ambiente certo, 57
passaram L0 **à primeira tentativa** (96,6%: muse 30/30; qwen3.8 **27/29 =
93,1%** — as duas falhas são de conteúdo: o LINDDUN recusado duas vezes pela
L0 e a árvore `T-STR-013`, sem bloco cercado e com a reparação truncada no
teto `num_predict`); **zero rejeições T8 com o catálogo presente**. O
falsificador formal (>15% de falhas L0 ou qualquer rejeição T8) disparou
APENAS enquanto o ambiente estava errado: o catálogo `baseline/THREATS` nunca
entrou no payload do `sync_up.sh` (job 2168367 — o fallback é um índice VAZIO
que recusa todos os ids, reais inclusive), e as restantes falhas run-level
foram contratos de código nunca antes exercitados (`domain_dir("DF-01")` no
despacho, `.get()` numa lista no renumerador, stores com ids locais pré-
renumeração, árvores com chave velha) — **cada um fixado em código com
commit e teste**; a cascata integral está registada em
[00_RESULTS.md](00_RESULTS.md) §P3-02/P3-04. A leitura de H1: o pack ensina o
contrato (a ficha LINDDUN sem esquema próprio foi o contra-exemplo — v1.2.0
inlineou-o e o mesmo modelo passou à primeira).

## H2 — a aritmética é do código: SUPPORTED

13 ameaças `UNMITIGATED_GAP` nas duas armas; **0** com residual diferente do
inerente. O registo não reduz um risco que nada mitiga.

## H3 — a árvore tem dentes: SUPPORTED (medição corrigida 2026-10-31)

A primeira análise declarou o falsificador disparado com
`residual_floored_by_tree` = 0 nas duas armas — e a medição estava errada duas
vezes (correcção registada no fim da página): o `compose_risk_register()`
deixava a flag nas stores de ameaças (o registo nunca a soube — bug corrigido
com teste), e a procura de residuais baixos usou a palavra portuguesa "Baixo"
sobre um campo que guarda `Low`. A medição correcta, sobre as stores e o
registo re-composto:

- **qwen3.8: o chão mordeu 2 ameaças** — `T-STR-001` (FULL_MITIGATION,
  inerente 3x4=12 High → residual 1x5=5 **Medium**) e `T-STR-006` (3x5=15
  High → 1x5=5 Medium): ambas liam residual Low pela prosa do modelo e a
  árvore prova caminho aberto — o piso levantou um veredicto que a prosa
  teria deixado passar. A predição (≥1 por corrida) cumpre-se neste braço.
- **muse: 0 pisos, com a causa distinguida** — as 2 ameaças com residual Low
  (`T-STR-003`, `T-STR-013`) têm árvores com caminho **quebrado**; as 11
  árvores com caminho aberto cavam todas ameaças Medium/High. O chão
  manteve-se vago (held vacuously) — honesto, não morto.
- O falsificador ("zero corrigidos em **todas** as corridas") **não
  disparou**. Nota de instrumento: a primeira análise do muse media o chão
  sobre árvores introuváveis (drift de ids pré-renumeração — corrigido em
  `505ad90`; as árvores foram re-derivadas sob os ids renumerados no job
  2169496). A discriminação fina (o chão deve ALGUMA vez corrigir? é sinal de
  honestidade ou de ameaças mal escolhidas?) fica para o investigador — é
  decisão de método, não de código.

## H4 — a regra de ouro: mantém-se estrutural

Nenhum gate chegou a CLOSED sem `risk_verdicts.json`: ambos os gates ficaram
`state: PROPOSED` com G7 OPEN sobre as ameaças não assinadas. G9 (estatutário
não mitigado): fechou com 4 (muse) e 2 (qwen3.8) obrigações estatutárias sem
FULL_MITIGATION — registadas no registo para a decisão humana, nunca aceites
em silêncio.

## H5 — reconciliação e catálogo: SUPPORTED

G11 CLOSED nas duas armas depois do renumber-on-carry (`44f78bd`): o registo é
a união STRIDE ∪ LINDDUN e os mitigadores citados são ids reais. G12 CLOSED
(catálogo íntegro, 3315 ids no cluster desde `ee67af2`).

## O que falta para CONCLUDED (e é por desenho)

A ronda humana de risco (G-P3-B): 21 + 31 decisões, uma por ameaça, com nome,
papel, justificação e sinal de revisão — os endpoints do inspector
(`POST /runs/:id/phase3b/verdicts`) assinam pelo browser. Uma recusa reabre a
Parte 1 com a instrução escrita (o loop reverso G10, cuja fechadura já foi
exercida em teste). Só depois o gate fecha, o export Parte 2 aterra em
`output/`, e a comparação entre armas fica completa para a pontuação L2 cega
([`scoring/f3/`](../../scoring/f3/)).

## Armadilha de instrumento registada

O pack do K3 envia id + nome truncado (158k chars ≈ 39,5k tokens) — a
estimativa de tokens do pack mede-se no que o builder ENVIA, não no ficheiro
fonte (o 265 KB era o JSON em disco). A escada de contexto não subiu
(needed 55,7k < num_ctx 65536) e o H1 foi medido nesse pack.

## Correcção de medição (2026-10-31, mesma sessão da auditoria)

A primeira versão desta página continha três erros de medição, apanhados na
auditoria física dos artefactos; o desvio regista-se aqui (§-2.3), e os
números das secções H1/H3 já são os corrigidos:

1. **H3 estava invertido.** `compose_risk_register()` não copiava
   `residual_floored_by_tree` das stores para o registo — a medição leu um
   artefacto que o código esvaziara. Corrigido em `risk_governance.py` com
   teste de regressão; o `risk_register.json` do qwen3.8 foi re-composto
   localmente pelo mesmo caminho do estágio (zero chamadas LLM; o delta são
   as 2 flags), e o do muse regenera byte-idêntico. H3: FALSIFICADOR →
   **SUPPORTED**.
2. **"Baixo" vs `Low`.** A procura de residuais baixos usou a palavra
   portuguesa sobre um campo que guarda o enum inglês (muse: 2; qwen3.8: 19).
3. **H1 com denominador omissivo.** O qwen3.8 tinha 2 falhas L0 de conteúdo
   fora da conta: a taxa é 27/29 = 93,1%, não 27/27 — o limiar de 85%
   continua cumprido. A muse 30/30 mantém-se (as 5 falhas do trace são da era
   de ambiente partido: catálogo vazio a recusar CWEs reais, espelho Doc03
   velho, campos em falta).

Adicionalmente registado na auditoria: as 16 árvores do muse (não 13) e os
7/21 mapeamentos K3 vazios do muse — ver "O que correu".
