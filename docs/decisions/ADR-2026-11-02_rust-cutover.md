# ADR-2026-11-02 — Cutover Python→Rust em duas ondas, com gates de paridade byte-exacto

**Data:** 2026-11-02 · **Estado:** PROPOSED (aguarda aprovação do investigador)
**Âmbito:** substituição integral do runtime Python da pipeline pelo port Rust
(`~/Work/aegis-rust`, milestones M0–M2 fechados com paridade provada).

## Contexto

O port Rust existe desde 2026-10-31 num repo próprio, com a barra de
**paridade byte-exacto**: os artefactos escritos pelo binário Rust têm de ser
idênticos byte-a-byte aos do Python, para os limiares medidos (0.88/0.95,
EXP-02) e os resultados publicados continuarem válidos sem recalibração.
Já provado: M0 (pyjson + SequenceMatcher, 973 vectores, job 2173086 PASS no
nó de compute), M1 (CLI A/B ao byte 7/7 + 29 vectores de erro argparse;
auditoria exterior cética C1–C9 remediada, job 2173574 PASS), M2 (compose
completo, replay de `run_p2enr_c1` 316/316 byte-idêntico vs Python vivo).
Faltam M3–M11 (≈ 29k LOC Python: `pipeline/src` 15,2k + `scripts/` 12,6k +
`scoring/`+`audit_runner.py` 1,2k).

## Decisão

1. **O port continua no `aegis-rust` até M8** (Regra 0 do AGENTS.md dele: o
   repo-mãe é read-only durante o port). Nenhuma linha de código de transição
   entra no `aegis-mvp` antes da paridade ponta-a-ponta estar provada.
2. **O cutover entra neste repo em duas ondas**, no ramo
   `feat/rust-port-cutover`, cada uma com gates de aceitação e rollback de um
   `git revert`:
   - **Onda 1 (runtime, após M8):** o crate Rust move-se para
     `pipeline/rust/` (fonte de verdade muda; `aegis-rust` arquiva-se com
     ponteiro para o SHA de origem); `phase1.sbatch`/`submit.sh` passam a
     invocar o binário musl static-pie; `pipeline/src` Python fica em disco
     mas fora do caminho de execução. Python sobrevive como **oráculo**
     (`parity/`) — é o que gera os vectores de paridade.
   - **Onda 2 (ferramentas, após M9–M11):** `scripts/`, `scoring/`,
     `audit_runner.py` e a lógica deucalion em Rust; `pipeline/src` Python
     é **apagado**. Python resta só em `parity/` (oráculo congelado, nunca
     executado em produção).
3. **A barra não baixa:** nenhum gate de cutover aceita "divergência
   documentada". Divergência byte ⇒ cutover bloqueado e corrigido no port,
   nunca recalibração de limiares.

## Consequências previstas (falsificáveis)

- **C1:** a cadeia `p1→all→phase2→p3a_all` com seed/modelo fixados produz
  runs byte-idênticos Python vs Rust (excepto `run_id` e timestamps), medida
  pelo instrumento A/B byte-exacto já existente no port.
- **C2:** a propriedade do §-1 (seeded run bit-reproduzível, EXP-02,
  sd 0.0000) repete-se sob o binário Rust sem alteração de limiares.
- **C3:** a classe de falhas de cluster "sync de fonte + `.pyc` stale"
  (auditoria do port, job 2173574; registo no skill hpc-deucalion) desaparece
  — o sync passa a enviar um binário.

**Sinais de revisão (reabrem esta decisão):**
- S1: qualquer divergência byte não explicável por `run_id`/timestamp num
  replay das fatias M0–M8 ⇒ o padrão de port (subagente por módulo com
  briefing fechado + vectores gerados) reverte-se para port manual módulo a
  módulo.
- S2: um milestone estourar 2× a estimativa de LOC/tempo ⇒ revê-se a ordem
  M3→M11 (possível antecipação do M9 para as ferramentas que o cutover da
  Onda 1 precisa, ex. `doc_lint`).
- S3: descoberta de dependência Python que o âmbito "tudo em Rust" não
  cobriu (ex. ferramenta externa chamada por `scripts/`) ⇒ o âmbito revê-se
  caso a caso no plano, nunca por exclusão silenciosa.

## Ligação ao plano operacional

As etapas T0–T7, oráculos por milestone, gates G-R1..G-R5 e riscos estão em
[`docs/pipeline/11_RUST_TRANSITION.md`](../pipeline/11_RUST_TRANSITION.md).
