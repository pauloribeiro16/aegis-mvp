# INSTRUMENT — Badge `adjustment_kind`: teste de resposta-conhecida + re-score offline M07/M09

> **Natureza:** medição de instrumento offline, executada 2026-10-09 (tarefa闲时 `offpeak-903db79d`).
> **NÃO registada como EXP e sem pré-registo** — registar é decisão do investigador (conduta científica §-2.3).
> Zero SSH/cluster, zero chamadas a modelos; leitura de `pipeline/src/quality.py`,
> `pipeline/src/steps.py`, `~/Work/aegis-runs/run_m07_*` (18), `~/Work/aegis-runs/run_m09_*` (4)
> e `~/Work/aegis-runs/_aggregate_cache.json`. Comando de re-score:
> `python3 scripts/aggregate_runs.py ~/Work/aegis-runs/run_m07_* ~/Work/aegis-runs/run_m09_* --json /tmp/rescore_m07m09.json`.

**Veredicto em duas linhas:** o classificador do badge é fiel (26/26 casos de resposta-conhecida) —
o defeito não está no classificador mas no **vocabulário que o prompt oferece**: 97,4% das linhas
declaradas `unchanged` descrevem goals que as gates obrigam a ser reescritas, e o menu
(steps.py:1162-1163) não oferece a classe `proportional` que o enum conhece (quality.py:441).
A hipótese estrutural "unchanged é correcto sob seleccionar-e-delimitar" é **refutada** para
estas corridas: linhas `unchanged` com similaridade média ao baseline de 0,248 — seleccionar-e-delimitar
previa ~1,0.

---

## (i) Inventário de corridas

18 × M07 (6 modelos × 3 casos) + 4 × M09 (qwen3.8 × 2 casos × braços ctrl/meta) = 22.
Job id no sufixo do directório; estado lido de `manifest.json` (`stage_history`/`stage_result`).

| Modelo | Caso | Job | Estágios | Deliverable | Bloco quality |
|---|---|---|---|---|---|
| gemma4:31b | C01 | 1983787 | 7 (p5 ok) | sim | sim |
| gemma4:31b | C02 | 1983789 | 7 | não | — |
| gemma4:31b | C03 | 1983791 | 7 | não | — |
| glm-4.7-flash | C01 | 1983799 | 7 | não | — |
| glm-4.7-flash | C02 | 1983801 | 7 | não | — |
| glm-4.7-flash | C03 | 1983804 | 7 | não | — |
| muse-glimmer:30b | C01 | 1983793 | 7 (p5 ok) | sim | sim |
| muse-glimmer:30b | C02 | 1983795 | 7 (p5 ok) | sim | sim |
| muse-glimmer:30b | C03 | 1983797 | 7 (p5 ok) | sim | sim |
| nemotron-3.5-lightning:30b | C01 | 1983807 | 7 | não | — |
| nemotron-3.5-lightning:30b | C02 | 1983809 | 7 | não | — |
| nemotron-3.5-lightning:30b | C03 | 1983811 | 7 | não | — |
| qwen3.5:27b | C01 | 1983813 | 2 (parou em p2) | não | — |
| qwen3.5:27b | C02 | 1983815 | 2 (parou em p2) | não | — |
| qwen3.5:27b | C03 | 1983817 | 2 (parou em p2) | não | — |
| qwen3.8:27b | C01 | 1983781 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b | C02 | 1983783 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b | C03 | 1983785 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b (ctrl) | C02 | 1991134 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b (meta) | C02 | 1991136 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b (ctrl) | C03 | 1991138 | 7 (p5 ok) | sim | sim |
| qwen3.8:27b (meta) | C03 | 1991140 | 7 (p5 ok) | sim | sim |

11 corridas entregues com bloco de qualidade (7 M07 + 4 M09); 11 sem deliverable
(`artefact.has_deliverable: false` — o resultado negativo M07 7/18 conhecido; qwen3.5 abortou em p2).

## (ii) Teste de resposta-conhecida do badge

Função sob teste: `adjustment_kind` (pipeline/src/quality.py:440-454). Enum documentado:
`unchanged | verbatim | proportional | inherited | narrowed | flagged | malformed`.
Mecânica: `norm()` (quality.py:64-65, lowercase + colapso de espaço) seguido de
**prefix match** pela ordem `verbatim → proportional → inherited → narrowed → flagged → unchanged`
(quality.py:451); vazio → `malformed` (quality.py:449-450); sem prefixo → `malformed` (quality.py:454).
Assinatura recebe **só a string de auto-declaração** — nunca o goal nem o baseline.

26 casos sintéticos (script `/tmp/badge_known_response_test.py`, fora do repo), 0 divergências
face às regras documentadas. Extracto:

| Caso | Entrada | Esperado | Obtido | Veredicto |
|---|---|---|---|---|
| V1–V2, P1–P2, I1–I2, N1–N2, F1–F2, U1–U2 (12) | palavra nua + frase por classe | classe respectiva | igual | PASS 12/12 |
| M1–M2 | `""`, `"   "` | malformed | malformed | PASS |
| X1 | `—` | malformed (sem prefixo) | malformed | PASS — **mas ver divergência D1** |
| X2–X3 | `-`, `--` | malformed | malformed | PASS — **D1** |
| S1–S6 | `Kept as is.`, `No adjustment needed.`, `Copied from baseline.`, `goal kept verbatim`, `Tailored to the 8-person team.`, `Recalibrated for micro-company scale.` | malformed (semântica óbvia fora do vocabulário) | malformed | PASS (regra) — **D2** |
| A1 | `proportionally recalibrated` | proportional (inflexão apanhada pelo prefixo) | proportional | PASS |
| A2 | `narrower than baseline` | malformed (`narrower` não começa por `narrowed`) | malformed | PASS |
| A3 | `Unchanged?` | unchanged | unchanged | PASS |

**Divergências de instrumento que o teste documenta (não são falhas do classificador):**

- **D1 — vocabulário legal desalinhado:** `check_adjustment_vocab` declara `—`/`-`/`--` legais e
  sem finding (quality.py:195-196, "badge, or '—'"), mas `adjustment_kind` faz-lhes bucket
  `malformed` (quality.py:449-454). Um registo honesto de "sem ajuste" polui a distribuição em
  `malformed` em vez de `unchanged`.
- **D2 — malformed conflate três animais diferentes:** registo vazio; dash legal-abençoado;
  veredicto semântico em prosa livre ("Kept as is."). Para análise de distribuição são categorias
  distintas que hoje partilham bucket.
- **D3 — a classe certa existe no enum mas não no menu:** o prompt oferece só
  `unchanged — fits as stated | narrowed: … — because … | flagged: …` (steps.py:1162-1163;
  verificado no prompt real do M07: `run_m07_qwen3_8_27b_c1_1983781/inputs/005_p4_D-01_1_user.md:593`).
  O enum conhece `proportional`/`inherited`/`verbatim` (quality.py:441,451) mas o modelo não os
  pode escolher. Nota: as memórias de 2026-10-08 diziam "a instrução nunca oferece `unchanged`" —
  **desactualado**: o menu com `unchanged` nasce em `3c11dc2` e está nos prompts do M07.
- **D4 — o badge mede a declaração, não a acção:** por construção (quality.py:440), um goal
  copiado verbatim com declaração "Proportional: …" fica `proportional`. O cruzamento
  declaração↔acção só existe na família delegação (quality.py:482-489).

## (iii) Re-score M07/M09 e comparação com a cache

**Reprodutibilidade: o re-score reproduz a cache byte-a-byte** nas 18 corridas sobrepostas em
todas as colunas comparadas (retenção, near_verbatim, adjustment_mix, calibration). As 4 corridas
M09 não estão na cache (foi construída antes delas) — entram como novos registos.

Colunas-chave das 11 corridas entregues (`near_verbatim` = similaridade ao baseline; limites em
quality.py:294-296 — piso de retenção 0,30; tecto de escape 0,88; duplicação de implication 0,95):

| Run | rows | ret média | ret mín | nv média | nv máx | mix | ratio_verbatim | alert | contradições |
|---|---|---|---|---|---|---|---|---|---|
| gemma4 c1 | 65 | 0.632 | 0.368 | 0.176 | 0.663 | unchanged:65 | 1.000 | True | 12 |
| muse c1 | 65 | 0.819 | 0.474 | 0.194 | 0.631 | unchanged:56, narrowed:8, flagged:1 | 0.862 | True | 8 |
| muse c2 | 99 | 0.792 | 0.389 | 0.176 | 0.722 | unchanged:98, flagged:1 | 0.990 | True | 39 |
| muse c3 | 129 | 0.804 | 0.333 | 0.230 | 0.842 | unchanged:122, narrowed:5, flagged:2 | 0.946 | True | 63 |
| qwen3.8 c1 | 65 | 0.707 | 0.316 | 0.144 | 0.750 | unchanged:64, flagged:1 | 0.985 | True | 19 |
| qwen3.8 c2 | 99 | 0.734 | 0.333 | 0.172 | 0.779 | unchanged:99 | 1.000 | True | 11 |
| qwen3.8 c3 | 129 | 0.747 | 0.310 | 0.207 | 0.847 | unchanged:128, flagged:1 | 0.992 | True | 17 |
| m09 c2 ctrl | 93 | 0.757 | 0.342 | 0.378 | 0.864 | unchanged:91, narrowed:1, flagged:1 | 0.978 | True | 10 |
| m09 c2 meta | 90 | 0.770 | 0.395 | 0.333 | 0.800 | unchanged:89, flagged:1 | 0.989 | True | 6 |
| m09 c3 ctrl | 112 | 0.763 | 0.432 | 0.354 | 0.875 | unchanged:108, narrowed:3, flagged:1 | 0.964 | True | 12 |
| m09 c3 meta | 125 | 0.778 | 0.333 | 0.362 | 0.854 | unchanged:123, narrowed:1, flagged:1 | 0.984 | True | 20 |

Agregado das 1071 linhas: **`unchanged` 1043 (97,4%) · `narrowed` 18 (1,7%) · `flagged` 10 (0,9%)
· `proportional`/`inherited`/`verbatim` 0.** `calibration_alert: True` em 11/11 corridas
(critério: ≥10 linhas e ratio_verbatim > 0,70 — quality.py:490); 217 contradições no total
(badge verbatim/unchanged + keyword de delegação na implication — quality.py:482-489).

## (iv) O que estes números fazem às hipóteses estruturais

**O falsificador disparou.** A hipótese estrutural restante (memória instrument-validity,
2026-10-08) dizia: a Fase 1 pode pedir *seleccionar-e-delimitar*, e nesse caso `unchanged` é a
declaração correcta. Sob essa hipótese, linhas `unchanged` deviam co-ocorrer com goals ≈ baseline
(similaridade próxima de 1,0 — é o que "seleccionar o texto tal como está" produz). Medido: as
linhas `unchanged` têm similaridade média 0,248 (0,144–0,378 por corrida) e retenção média
0,632–0,819 — os goals são reescritas com 18–37% do vocabulário do baseline alterado. Nenhuma
corrida entregue tem sequer UMA linha perto de verbatim (nv máx por corrida 0,631–0,875, todas
sob o tecto de 0,88 que as próprias gates impõem). Conclusão: ou `unchanged` é falso em 97,4%
das declarações (leitura textual), ou — se lido como "obrigação inalterada" — o badge não
distingue uma linha genuinamente inalterada de uma reescrita proporcional, e em qualquer das
leituras **não transporta sinal da acção**. As duas leituras são separáveis por código: o enum já
tem `verbatim` como classe distinta (quality.py:441), logo o vocabulário pretende distinguir
texto-copiado de obrigação-mantida — e não o consegue fazer sem olhar para o goal, que a função
não recebe (quality.py:440).

**O defeito é do menu, não do classificador.** O classificador é determinístico e fiel (26/26).
Mas as gates obrigam cada linha a ser uma reescrita (escape ≥ 1,27× — tecto 0,88, quality.py:295;
piso de retenção 0,30, quality.py:294) e o menu não oferece a classe que descreve o comportamento
exigido (`proportional` está no enum mas fora do menu, steps.py:1162-1163 — D3). O modelo escolhe
o rótulo menos-falso disponível e a distribuição colapsa: 97,4% > tecto de 60–70% do R10b
(invariante 3), alarme mecânico disparado em 11/11 (quality.py:490). A braço meta do M09 (mensagem
com banda-alvo, `b32bccc`) moveu a acção (nv média 0,33–0,38 vs 0,14–0,23 no M07) e **não moveu a
declaração** (~97% unchanged nos dois braços) — evidência directa de que o badge não segue a acção.

**Guard em falta:** o único cruzamento declaração↔acção que existe é o das keywords de delegação
(quality.py:482-489; 217 linhas apanhadas). Não existe o cruzamento geral "declara `unchanged` mas
similaridade < limiar" — é o guard que fecharia a classe de defeito observada. Junto com D1
(`—` abençoado por um checker e condenado pelo outro) e D3 (menu sem a classe certa), qualquer
correctivo passa por: (1) alinhar o menu com o enum (oferecer `proportional`); (2) decidir o
estatuto de `—` nos dois checkers; (3) cruzar badge↔similaridade no `score_run`.

**Âmbito:** estas medidas caracterizam o instrumento sobre os artefactos armazenados das 22
corridas; não reavalam as gates do p4 nem a qualidade dos deliverables. O registo como EXP
(pré-registo, falsificador formal) é decisão do investigador.
