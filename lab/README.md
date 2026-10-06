# lab/ — a banca de ensaios (per-model prompt & orchestration experiments)

> **O que é:** uma lane separada para descobrir, por modelo, que ajustes de
> prompt/orquestração o fazem atravessar a MESMA pipeline que a referência
> (qwen3.8) e o muse atravessam. Nasce da matriz M07 (2026-10-05): 7/18
> células entregues, e cada modelo falha de forma diferente.
> **O que nunca é:** parte da pipeline de produção.

## Constituição (regras duras da lane)

1. **A pipeline de produção não é tocada.** Nada em `pipeline/src/`, `pipeline/deucalion/`,
   fichas, gates ou parsers muda por causa desta lane. Os ajustes vivem em
   `lab/overlays/*.py` e aplicam-se apenas a uma CÓPIA do payload no cluster
   (`$PROJ/mvp-lab/<variant>/`).
2. **Gates e parsers são byte-idênticos aos de produção.** O que se varia são
   instruções (texto do prompt), composição do pack e topologia de chamadas —
   nunca um limiar, um parser ou um gate. `apply_overlay.py` recusa qualquer
   alteração fora das regiões de instrução (guard de linhas).
3. **Corridas lab vivem separadas:** runs root `$PROJ/mvp-lab/aegis-runs/` no
   cluster, `~/Work/aegis-runs-lab/` local, tags `lab_<variant>`. Nunca entram
   na matriz M02 nem no painel sem promoção explícita.
4. **Promoção tem processo:** um overlay que funcione não se copia para produção
   na hora — o investigador decide, a mudança entra como instrumento com
   preregisto próprio, e a matriz é re-corrida limpa.
5. **Pré-registo antes da primeira corrida** de cada wave (`LAB0n_PREREG.md`),
   com hipótese, predição e falsificador por braço (§-2.3).
6. **Seed 42, temperature 0.2, n=1 por braço** nas waves de triagem.

## Uso

```bash
# submeter um braço: lab/run_lab.sh <variant> <model> <case>
bash lab/run_lab.sh lab01-qwen35-fence qwen3.5:27b Case_01_TinyTask_SaaS

# puxar os resultados quando terminarem
bash lab/run_lab.sh pull lab01-qwen35-fence
```

## Estado

- **LAB01** (2026-10-05): 5 braços, 5 corridas — ver `LAB01_PREREG.md` e `BRIEFS.md`.
