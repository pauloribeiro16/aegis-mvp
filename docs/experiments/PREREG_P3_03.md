# PREREG_P3_03 — Onda D: a Parte 2 (ameaças e aceitação humana de risco) na pipeline

Version: 1.0.0
Status: FROZEN 2026-10-27, before the first `p3b_all` job is submitted.
Frozen by: aegis-mvp executor, after the Part 2 code landed (catálogo 3315 ids em `baseline/THREATS/_index.json`; módulos `phase3b/`; estágios `p3b_*`; 17 testes em `phase3b_test.py`) e a bateria local completa estava verde.
Upstream: [PREREG_P3_02.md](PREREG_P3_02.md) (a Onda C cujo pacote aceite a Parte 2 julga) · ADR-012 (a camada de conhecimento de ameaças) + ratificação 2026-10-27 (CWE+CAPEC núcleo; ATT&CK/D3FEND/ATLAS/EMB3D consultivos; ingestão do KG local) · ADR-005 (o loop reverso) · ADR-006 (a Parte 2 é gated pela Parte 1).

---

## 1. What this preregisters

A primeira execução na pipeline das etapas 2.1–2.5 (`p3b_model`, `p3b_threats`,
`p3b_trees`, `p3b_risk_round`, `p3b_gate`) sobre o pacote aceite da Parte 1 de
um braço da Onda C, com a aritmética de risco em Python, provas de caminho
quebrado, e a ronda humana de risco (`G-P3-B`) — o modelo propõe, uma pessoa
assina.

**Dependência humana declarada (não é desvio, é o desenho):** a Parte 2 julga
o pacote CONVERGIDO da Parte 1 (two-states). Os runs da Onda C terminam
PROPOSED — a ronda de veredictos (`Accept/Reject/Adjust` por item em
`round1_verdicts.json` + marcador `G-P3-A`) é do investigador. O 1.º `p3b_all`
só corre depois dessa assinatura; o pré-registo mede a partir daí.

## 2. Arms (congelados)

| Braço | Modelo | Caso | Tag | Nota |
|---|---|---|---|---|
| 1 | `qwen3.8:27b` | Case 01 | `exp_p3_03_p3b_qwen38_c1` | sobre o run da Onda C com a ronda assinada |
| 2 | `muse-glimmer:30b` | Case 01 | `exp_p3_03_p3b_muse_c1` | mesmo upstream da Onda C, Parte 2 própria |

n = 2 corridas `p3b_all` + as rondas humanas de risco que se seguiram. As
decisões de risco são do investigador e entram no doc de resultados como
estão — um registo de risco sem assinatura é um estado, não uma falha.

## 3. Hypotheses, predictions, falsifiers

### H1 — L0 da Parte 2 à primeira tentativa

- **H1:** ≥ 85% das chamadas `p3b_*` (modelo, fluxos, árvores, K3) passam L0 à
  primeira tentativa com o catálogo no pack.
- **Predição:** o T8 não rejeita nenhum id (o catálogo completo de 3315 ids
  está no pack do K3); as violações L0 concentram-se no formato das tabelas,
  não no conteúdo.
- **Falsificador:** > 15% de falhas L0, ou qualquer rejeição T8 — o pack não
  ensina o contrato, e o campo da falha diz qual.

### H2 — A aritmética é do código (zero redução mágica)

- **H2:** Em todas as ameaças `UNMITIGATED_GAP` (ou sem mitigadores), o risco
  residual é IGUAL ao inerente — medido sobre `risk_register.json`.
- **Predição:** 100% dos gaps preservam L×I; nenhuma redução sem requisito.
- **Falsificador:** um único gap com residual abaixo do inerente — o código
  mentiu, e a correção é do código, nunca do prompt.

### H3 — A árvore tem dentes

- **H3:** Pelo menos uma ameaça Critical/High tem o residual ELEVADO pelo
  chão da árvore (caminho aberto ⇒ residual nunca Low) — i.e., a prova de
  caminho quebrado muda um veredicto que a prosa teria deixado passar.
- **Predição:** ≥ 1 `residual_floored_by_tree: true` por corrida com árvores.
- **Falsificador:** zero corrigidos em todas as corridas — ou as árvores não
  estão a ser honestas (marcaram DEF sem requisito), ou o chão nunca dispara;
  o registo distingue os dois casos.

### H4 — A regra de ouro (structural, não estatística)

- **H4:** Nenhum run chega a `G7..G12 = CLOSED` sem assinatura humana; G9
  recusa aceitação de estatutário não mitigado; G10 abre o loop reverso com
  gatilho escrito.
- **Falsificador:** qualquer estado CONCLUDED com `risk_verdicts.json`
  vazio/ausente — o two-states quebrou.

### H5 — Reconciliação e catálogo (T7/T8 = 0 findings)

- **H5:** `G11` fecha (STRIDE ∪ LINDDUN == registo; mitigadores reais) e
  `G12` fecha (0 ids fora do catálogo) nas corridas concluídas.
- **Falsificador:** qualquer finding T7/T8 no `gate_report.md` da Parte 2.

## 4. Procedure

1. Assinada a ronda da Parte 1 do braço escolhido (pré-requisito humano),
   fork de execução: o MESMO run dir continua (`p3b_all` no run `run_p302_*`
   cuja Parte 1 concluiu).
2. `submit.sh --stage p3b_all` com `MVP_RUN_ID` do run; watchers; `sync_down`.
3. A ronda humana de risco: o investigador assina `steps/phase3b/risk_verdicts.json`;
   se houver `Reject_Risk_Require_Mitigation`, o gatilho reabre a Parte 1
   (nova ronda) e a Parte 2 re-avalia depois.
4. Análise em `EXP_P3_03_results.md` citando este preregisto; entrada em
   `00_RESULTS.md` no dia da análise.

## 5. Deviations

Nenhum à data do congelamento.

## 6. What this does NOT claim

- Não compara modelos na Parte 2 (n=2, fases diferentes do mesmo caso);
- não mede a qualidade das decisões humanas de risco (mede que EXISTEM e são
  assinadas — a qualidade é da pessoa, e o signpost é o instrumento);
- não valida a Onda E (o site) nem a exportação final para além do gate.
