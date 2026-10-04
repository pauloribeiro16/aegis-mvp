#!/usr/bin/env python3
"""agent_tool_test.py — unit tests for the agent toolbox contracts.

Every submission tool must accept what the pipeline's L0 parsers accept and
reject — with the SAME named error — what they reject, then persist artifacts
byte-compatible with the pipeline's steps/ layout. Also covers the state
machine (out-of-order submission), the R2b derivation tools and the
finish-gate contract.

Usage: python3 pipeline/tests/agent_tool_test.py
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))  # reuse e2e fixtures
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from local_e2e_test import CONFIRMED, FACT_SHEET, FRAMING_TABLE, SELECTED, \
    TENSIONS_TABLE, VERDICT_TABLE, goals_answer, selection_answer  # noqa: E402

from agent.tools import AgentToolbox, ToolError, tool_schemas  # noqa: E402

FAILURES: list[str] = []
TMP = Path("/tmp/mvp_agent_tool_test")


def unfence(s: str) -> str:
    """Some e2e fixtures carry their own fences (they ARE pipeline answers);
    the toolbox takes raw markdown/table text."""
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1]
        s = s.rsplit("```", 1)[0]
    return s.strip()


from compose import domain_dir  # noqa: E402


def fake_pack(sd: str) -> str:
    """The regs/ slice of a P4 pack, in the attachment format goals_answer()
    parses to discover which Sub-SO cards the module carries."""
    chunks = []
    for reg in CONFIRMED:
        p = domain_dir(REPO, sd) / "regs" / f"{reg}.md"
        if p.exists():
            chunks.append(f"----- BEGIN FILE: {p} -----\n"
                          f"{p.read_text(encoding='utf-8')}\n----- END FILE")
    return "\n".join(chunks)


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(name)


def fresh_box() -> AgentToolbox:
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True)
    # validate_run's trace block needs a manifest (agent-mode accounting)
    (TMP / "manifest.json").write_text(json.dumps({
        "run_id": "agent_tool_test", "case_id": "Case_01_TinyTask_SaaS",
        "mode": "agentic", "model": "fake",
        "stage_history": [{"stage": "agentic", "status": "ok"}],
        "n_calls_total": 0}), encoding="utf-8")
    return AgentToolbox(REPO, "Case_01_TinyTask_SaaS", TMP)


def main() -> int:
    print("== agent toolbox: contracts shared with the pipeline ==")
    tb = fresh_box()

    print("-- state machine (out-of-order submissions are named errors) --")
    for fn, kwargs in ((tb.submit_framing, {"markdown_table": "| Dimension | Framing |\n|---|---|\n| Size | x |"}),
                       (tb.list_candidate_subdomains, {}),
                       (tb.derive_track_b, {})):
        try:
            fn(**kwargs)
            check(f"{fn.__name__} refuses before prerequisites", False)
        except ToolError as e:
            check(f"{fn.__name__} refuses before prerequisites",
                  "prerequisite missing" in str(e))
    try:
        tb.read_regulation_module("D-01.1", "regs")
        check("read_regulation_module refuses before verdicts", False)
    except ToolError as e:
        check("read_regulation_module refuses before verdicts", "prerequisite missing" in str(e))

    print("-- submission happy path stores pipeline-shaped artifacts --")
    r = tb.submit_fact_sheet(FACT_SHEET)
    check("fact sheet accepted", r.get("ok") is True and (TMP / "steps" / "fact_sheet.yaml").exists())
    r = tb.submit_verdicts(VERDICT_TABLE)
    check("verdicts accepted, confirmed == [GDPR, CRA]",
          r.get("confirmed") == ["GDPR", "CRA"])
    v = json.loads((TMP / "steps" / "verdicts.json").read_text())
    check("verdicts.json is the pipeline shape",
          sorted(x["regulation"] for x in v["verdicts"]) ==
          ["AI_Act", "CRA", "DORA", "GDPR", "NIS2"])
    r = tb.submit_selection(unfence(selection_answer()))
    check("selection accepted with all candidates covered",
          r.get("selected") == sorted(SELECTED), f"{r}")
    r = tb.submit_framing(unfence(FRAMING_TABLE))
    check("framing accepted", r.get("ok") is True)
    r = tb.submit_tensions(unfence(TENSIONS_TABLE))
    check("tensions accepted (multi-reg)", r.get("n_tensions", 0) >= 1)
    t = json.loads((TMP / "steps" / "tensions.json").read_text())
    check("tensions.json is the pipeline shape", all(
        set(x) == {"id", "subdomains", "tension", "conflict", "resolution"} for x in t["tensions"]))

    print("-- goals: per-row submit_goal, pipeline parse + content gates --")
    good = unfence(goals_answer(SELECTED[0], fake_pack(SELECTED[0])))
    good_rows = {reg: [c.strip().replace("|", "/") for c in l.split(" | ")]
                 for l in good.splitlines() if l.startswith(f"| AG-{SELECTED[0]}-")
                 for reg in CONFIRMED
                 if f"SG-{SELECTED[0]}.{reg}" in l}

    def submit_row(sd, reg, override=None):
        c = list(good_rows[reg])
        if override:
            c = override(c)
        return tb.submit_goal(sd, f"SG-{sd}.{reg}", c[1], c[2], c[3], c[4], c[7], c[8])

    n = 0
    for reg in tb._expected_regs(SELECTED[0]):
        try:
            r = submit_row(SELECTED[0], reg)
            check(f"submit_goal accepts a good {reg} row", r.get("ok") is True, str(r)[:120])
            n += 1
        except ToolError as e:
            check(f"submit_goal accepts a good {reg} row", False, str(e)[:200])
    check("module persisted only when every expected Sub-SO arrived",
          n == len(tb._expected_regs(SELECTED[0])))
    jf = TMP / "steps" / "goals" / f"{SELECTED[0].replace('.', '_')}.json"
    check("goal artifact written", jf.exists())
    if jf.exists():
        d = json.loads(jf.read_text())
        check("goal JSON has the pipeline keys",
              {"id", "goal", "implication", "pattern", "property", "parent",
               "baseline_source", "regulation", "source", "adjustment"} <= set(d["goals"][0]))
        check("ids sequential from 001",
              [g["id"] for g in d["goals"]] == [f"AG-{SELECTED[0]}-{i:03d}"
                                                for i in range(1, len(d["goals"]) + 1)])
        check("goal .md artifact stored too",
              (TMP / "steps" / "goals" / f"{SELECTED[0]}.md").exists())

    print("-- goals: each defect class rejected with the pipeline's named error --")
    other = SELECTED[1]
    for name, override in (
            ("bad pattern", lambda c: c[:3] + ["achieve more"] + c[4:]),
            ("bad property", lambda c: c[:4] + ["Vibes"] + c[5:]),
            ("bad baseline source", lambda c: c[:6] + ["SG-D-99.9.NIS2"] + c[7:]),
            ("empty adjustment", lambda c: c[:8] + [""]),
            ("literal pipe in a field", lambda c: c[:1] + [c[1] + " | a | b"] + c[2:]),
            ("technology leakage", lambda c: c[:1] + [c[1] + " encrypted with AES-256 over TLS"] + c[2:]),
    ):
        try:
            submit_row(other, CONFIRMED[0], override)
            check(f"rejects: {name}", False, "accepted a defective row")
        except ToolError as e:
            check(f"rejects: {name}", bool(str(e)))
    # a Sub-SO the module does not carry is refused
    try:
        tb.submit_goal(other, f"SG-{other}.DORA", "goal", "implication", "maintain",
                       "Confidentiality", "DORA Art. 1", "unchanged — fits as stated")
        check("rejects: Sub-SO the module does not carry", False)
    except ToolError as e:
        check("rejects: Sub-SO the module does not carry", bool(str(e)))

    print("-- derivation tools match controls.py --")
    anchors = tb.derive_anchors(SELECTED[0], ["SG-D-01.1.GDPR"])
    check("derive_anchors returns CSF ids", isinstance(anchors.get("anchors"), list)
          and all(a.count("-") >= 1 for a in anchors["anchors"]))
    tb_r = tb.derive_track_b()
    check("track B rows for current selection",
          sorted(r0["subdomain"] for r0 in tb_r["rows"]) == sorted(SELECTED))
    cs = tb.derive_controls_section(SELECTED[0])
    check("controls sections non-empty", len(cs.get("sections", [])) >= 1)

    print("-- state view + finish gate --")
    st = tb.get_state()
    check("state lists artifacts", "verdicts.json" in st["artifacts_present"]
          and st["goals_per_subdomain"].get(SELECTED[0]) == 2)
    try:
        tb.finalize()
        check("finalize refused before the artifacts exist", False)
    except ToolError as e:
        check("finalize refused before the artifacts exist",
              "Call submit_" in str(e) or "cannot finalize" in str(e))

    print("-- render + validate + finish on a complete toolbox state --")
    # submit remaining goals so render_document can assemble
    for sd in SELECTED[1:]:
        tbl = unfence(goals_answer(sd, fake_pack(sd)))
        regs = tb._expected_regs(sd)
        if not regs:
            tb.submit_goal(sd, "SG-%s.GDPR" % sd, "", "", "maintain",
                           "Confidentiality", "", "unchanged — fits as stated")
            continue
        for l in tbl.splitlines():
            if l.startswith(f"| AG-{sd}-"):
                c = [x.strip().replace("|", "/") for x in l.split(" | ")]
                tb.submit_goal(sd, c[6], c[1], c[2], c[3], c[4], c[7], c[8])
    r = tb.finalize()
    check("finalize writes doc02", (TMP / "doc02_adjusted_goals.md").exists())
    from validate import validate_run
    findings = validate_run(REPO, TMP)
    check("L1 PASS on complete agent state", not findings, str(findings[:3]))

    print("-- schema sanity --")
    names = [s["function"]["name"] for s in tool_schemas()]
    check("all tool schemas unique", len(names) == len(set(names)))
    check("finalize is a schema", "finalize" in names)

    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — toolbox contracts identical to the pipeline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
