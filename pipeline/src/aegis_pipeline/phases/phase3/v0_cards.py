"""aegis_pipeline.phases.phase3.v0_cards — candidate functional card loader.

V0 is a human input and this module never writes it. Only the id, name and
description are read, because that is all a verdict needs: whether a card can
carry an objective.
"""
from __future__ import annotations

import re
from pathlib import Path


def load_v0_cards(doc01: Path) -> list[dict]:
    """The candidate carrier pool, read from the frozen V0 deliverable.

    Constraints live in V1/V2 and are deliberately not shown — a verdict that can
    see the security constraints it is judging has already been anchored, and the
    question being asked is whether the functional card covers the obligation at all.
    """
    cards, current = [], None
    for line in doc01.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\*\*ID:\*\*\s*(R\d+\.\d+)\s*\*\*Name:\*\*\s*(.+?)\s*\|", line)
        if m:
            current = {"id": m.group(1), "name": m.group(2), "description": ""}
            cards.append(current)
            continue
        if current is not None:
            d = re.match(r"^\|\s*\*\*Description:\*\*\s*(.+?)\s*\|", line)
            if d:
                current["description"] = d.group(1)
    return cards
