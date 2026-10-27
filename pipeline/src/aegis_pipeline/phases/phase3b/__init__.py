"""aegis_pipeline.phases.phase3b — Phase 3 Part 2: threat modelling and the
human acceptance of risk.

Modules: schemas (vocabularies, risk bands, T8), system_model (Etapa 2.1),
threats (Etapa 2.2 — STRIDE/LINDDUN + the Python risk arithmetic), adtrees
(Etapa 2.3 — broken-path proofs), risk_governance (Etapa 2.4 — the model
proposes, a person decides), threat_gate (Etapa 2.5 — G7–G12).
"""
from aegis_pipeline.phases.phase3b.schemas import (  # noqa: F401
    LINDDUN,
    MITIGATION,
    RISK_DECISIONS,
    RE_THREAT_IDS,
    STATUTORY_FORBIDDEN,
    STRIDE,
    check_threat_ids,
    residual_from_mitigation,
    risk_level,
    threat_index,
)
