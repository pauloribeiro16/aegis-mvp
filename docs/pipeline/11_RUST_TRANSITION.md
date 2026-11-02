# 11 — Plano de Transição Python→Rust

> **Estado:** PROPOSED (decisão em
> [`ADR-2026-11-02`](../decisions/ADR-2026-11-02_rust-cutover.md), aguarda
> aprovação). **Ramo de cutover:** `feat/rust-port-cutover`.
> **Repo do port:** `~/Work/aegis-rust` (git próprio; o repo-mãe é read-only
> durante o port — Regra 0 do AGENTS.md dele).

## 1. Onde estamos

| | Python (a substituir) | Rust (o substituto) |
|---|---|---|
| Onde vive | este repo (`pipeline/src`, `scripts/`, `scoring/`) | `~/Work/aegis-rust` |
| Volume | ≈ 29k LOC — `pipeline/src` 15.209 (67 ficheiros), `scripts/` 12.609 (~45 ferramentas), `scoring/`+`audit_runner.py` 1.194 | 3.755 LOC portados |
| Fechado com paridade provada | — | **M0** pyjson + SequenceMatcher (973 vectores, fuzz apanhou 1-ULP do serde_json; job 2173086 PASS no nó de compute) · **M1** CLI new-run/run (A/B ao byte 7/7, 29 vectores de erro argparse; auditoria exterior C1–C9 remediada, job 2173574 PASS) · **M2** compose completo (replay `run_p2enr_c1` 316/316 byte-idêntico vs Python vivo) |
| Pendente | tudo | **M3** llm client + builders de instrução + runner p1..p5 · **M4** guards + validate · **M5** phase2 · **M6** phase3 + weave (+13 branches deferidas de packs.rs) · **M7** phase3b · **M8** replay e2e + FakeOllama · **M9** `scripts/` · **M10** scoring/audit · **M11** deucalion + stubs sbatch |

**A barra é paridade byte-exacto** (os limiares 0.88/0.95 e os resultados
publicados EXP-02.. mantêm-se sem recalibração — `aegis-rust/AGENTS.md`).
O binário de cluster é musl static-pie (corre no glibc 2.28 do Deucalion).

## 2. Etapas

| Etapa | Onde | O quê | Oráculo de paridade |
|---|---|---|---|
| **T0** | `feat/rust-port-cutover` | ADR + este plano. Zero código. | — |
| **T1 = M3** | aegis-rust | `llm.py` (cliente Ollama), builders de instrução (`_p4_instruction`, `p4t_extra_instruction`, `EXTRA_INSTRUCTION` — a meia-parte em código que o oráculo M2 passa como ficheiro), runner p1..p5 (`phases/phase1/runner.py`, 2.887 LOC) | replay das respostas gravadas no `trace.jsonl` de um run real (mesmo padrão do subcomando `compose-call` do M2); o request JSON também se escreve via `pyjson` |
| **T2 = M4–M5** | aegis-rust | guards (`quality_gates` 459, `l1_validation` 453, `controls.py`) + `validate.py` + phase2 | replay determinístico pós-LLM de `run_p2enr_c1` (Fases 1–2) |
| **T3 = M6–M7** | aegis-rust | phase3 (as 13 branches deferidas de `packs.rs` fecham aqui) + weave + `doc_lint`/`check_traceability` nativos + phase3b | replay de `run_p302_qwen38_c1` (Fase 3) |
| **T4 = M8** | aegis-rust | replay e2e offline + FakeOllama — a prova ponta-a-ponta | `diff -r` entre o replay Python e o replay Rust sobre os DOIS runs gravados (padrão Regra 2 de paridade do port) |
| **T5 = Onda 1 do cutover** | este ramo | crate → `pipeline/rust/`; `aegis-rust` arquiva-se com ponteiro para o SHA de origem; sbatch/submit invocam o binário musl; `pipeline/src` Python sai do caminho de execução (fica em disco como oráculo de comparação) | gates G-R1..G-R3 abaixo |
| **T6 = M9–M11** | aegis-rust → este ramo | `scripts/` (12,6k LOC), scoring/audit, deucalion | vectores por ferramenta + replay das ferramentas sobre artefactos reais |
| **T7 = Onda 2 do cutover** | este ramo | apagar `pipeline/src` Python + ferramentas Python; Python resta só em `parity/` (oráculo congelado); atualizar AGENTS.md §-1/§0, docs e CI | gates G-R4..G-R5 |

## 3. Gates de aceitação do cutover

- **G-R1 (por milestone T1–T4):** vectores gerados contra o Python vivo +
  replay da fatia byte-idêntico (o padrão que fechou M0–M2).
- **G-R2 (T5, Onda 1):** A/B fresh-run no Deucalion — a cadeia
  `p1→all→phase2→p3a_all` (a da medição P2-03, `run_seqall_1793479203_2173045`)
  corrida nos dois runtimes com o mesmo modelo/seed: runs byte-idênticos
  excepto `run_id`/timestamps, medidos pelo instrumento A/B byte-exacto do port.
- **G-R3 (T5):** EXP-02 re-validado sob Rust — o seeded run continua
  bit-reproduzível (sd 0.0000) sem alteração de limiares.
- **G-R4 (T7):** zero invocações Python activas em sbatch/docs; `doc_lint`,
  `check_traceability` e `validate` correm como subcomandos do binário.
- **G-R5 (T7):** §-1 do AGENTS.md reescrito para o binário (o default
  seed=42/temperature=0.2 é medida e transporta-se — não se re-mediu).

## 4. Riscos e sinais

- **O runner é LLM-dependent** (T1): a paridade mede-se contra respostas
  gravadas, não ao vivo. O risco byte-level está no *request* (ordem de
  campos, floats) — coberto pelo `pyjson`, que já está provado.
- **Dois repositórios durante o port**: fonte de verdade = `aegis-rust` até
  T4; após T5 passa a ser `pipeline/rust/` e o repo do port arquiva-se
  (nunca duas fontes vivas — o padrão das duas cópias do Doc03 que matou o
  primeiro `p3b_model` é o anti-exemplo).
- **O corpus evolui durante o port**: o replay compara sempre contra o
  Python VIVO (o M2 viu 121/316 divergirem de gravações antigas porque o
  repo-mãe mudou desde 2026-10-09 — o instrumento certo evita o falso
  positivo).
- **Ritmo**: o M2 portou 1.668 LOC num milestone com subagente de briefing
  fechado; ≈ 29k LOC restantes ⇒ a sequência M3–M11 é a aposta. Sinal S2 do
  ADR (milestone a 2× a estimativa) reabre a ordem, não a barra.

## 5. O que NÃO muda

Corpus, baseline, cases, templates, fichas (prompts), limiares e resultados
publicados: o port substitui o *runtime*, não a metodologia. Os `*.sbatch`
continuam a ser stubs de shell mínimos (SLURM exige shell) — em Rust apenas
menores: deixam de sincronizar fonte e passam a trazer um binário.
