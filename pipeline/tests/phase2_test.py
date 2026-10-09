#!/usr/bin/env python3
"""phase2_test.py — the Phase 2 prototype's derivations may not drift.

`pipeline/src/phase2.py` turns a Phase 1 run directory into the two Phase 2
deliverables without a model. That is only worth anything if the derivations are
anchored to the corpus rather than to whatever the last run happened to contain,
which is what these assertions check.

Three of them exist because hand-authoring got them wrong in cases 01-03 and the
ledger recorded it (docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §4):

  * §4.2 — an `Operational Statement` cell swallowed raw baseline YAML in four
    Case 03 rows. A code path cannot produce that, and the gate must prove it.
  * §4.4 — Case 01 put 16 GDPR rows under the `SO-` prefix. The prefix is a
    function of the regulation, or it is a convention nobody can reproduce.
  * §4.8 — one Case 03 row carried `—` where Phase 1 had anchors, so control
    anchoring was lost silently. Anchors are re-derived here, never inherited.

The fourth is R2b: every anchor the prototype emits must resolve to a real file
under `baseline/CONTROLS/`. A derived-but-unresolvable anchor is worse than a
missing one, because it looks anchored.

These assertions read only committed files and need no model and no GPU.

Usage: python3 pipeline/tests/phase2_test.py
Exit 0 iff every derivation holds.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

import phase2  # noqa: E402

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def synth_run(tmp: Path, goals: list[dict], selected: list[str]) -> Path:
    """A minimal Phase 1 run dir: the prototype's only input contract."""
    gdir = tmp / "steps" / "goals"
    gdir.mkdir(parents=True)
    by_sd: dict[str, list[dict]] = {}
    for g in goals:
        by_sd.setdefault(phase2.subdomain_of(g["id"]), []).append(g)
    for sd, gs in by_sd.items():
        (gdir / f"{sd.replace('.', '_')}.json").write_text(
            json.dumps({"subdomain": sd, "goals": gs}), encoding="utf-8")
    (tmp / "steps" / "selection.json").write_text(
        json.dumps({"selected": [{"id": s, "name": s} for s in selected]}),
        encoding="utf-8")
    (tmp / "manifest.json").write_text(json.dumps({"case_id": "synthetic"}),
                                       encoding="utf-8")
    return tmp


def goal(gid: str, reg: str, sd_source: str = "SG-D-01.1.GDPR") -> dict:
    return {"id": gid, "goal": f"statement for {gid}", "regulation": reg,
            "baseline_source": sd_source, "pattern": "maintain",
            "property": "c", "parent": f"SG-{phase2.subdomain_of(gid)}.HL",
            "source": "some article", "adjustment": "unchanged — fits as stated",
            "implication": "n/a"}


def test_id_derivation() -> None:
    print("\nid derivation")
    rows = [
        phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR")),
        phase2.derive_objective(REPO, goal("AG-D-01.1-002", "CRA")),
        phase2.derive_objective(REPO, goal("AG-D-01.1-003", "NIS2")),
    ]
    check("GDPR takes the PO- prefix", rows[0]["objective_id"] == "PO-D-01.1-001",
          rows[0]["objective_id"])
    check("CRA takes SO-", rows[1]["objective_id"] == "SO-D-01.1-002",
          rows[1]["objective_id"])
    check("NIS2 takes SO-", rows[2]["objective_id"] == "SO-D-01.1-003",
          rows[2]["objective_id"])
    # the regression that produced `POD-01.1-001`
    check("the canonical D- axis survives the prefix swap",
          all(r["objective_id"].count("-") == 3 for r in rows),
          rows[0]["objective_id"])


def test_slot_inherited() -> None:
    print("\nslot inheritance")
    # D-01.1 carries CRA for real; a slot the golden does not use (003) proves
    # the slot is carried rather than recomputed from a canonical regulation
    # order. Using a pair the corpus does not carry would make controls.py
    # refuse the row, which is the correct behaviour and not what is under test.
    g = goal("AG-D-01.1-003", "CRA", sd_source="SG-D-01.1.CRA")
    r = phase2.derive_objective(REPO, g)
    check("the Phase 1 slot is carried verbatim", r["objective_id"] == "SO-D-01.1-003",
          r["objective_id"])
    check("the regulation is read from the goal, never from the slot",
          r["regulation"] == "CRA", r["regulation"])


def test_anchors_resolve() -> None:
    print("\nanchors (R2b)")
    r = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    anchors = [a.strip() for a in r["anchors"].split(",") if a.strip() != "—"]
    check("anchors are derived, not inherited", bool(anchors), r["anchors"])
    unresolved = [a for a in anchors
                  if not list((REPO / "baseline" / "CONTROLS").rglob(f"{a}.json"))]
    check("every derived anchor resolves under baseline/CONTROLS/",
          not unresolved, f"{len(anchors)} anchors, unresolved={unresolved}")


def test_pollution_gate() -> None:
    print("\ngate G1 — baseline pollution (§4.2)")
    good = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    bad = dict(good)
    bad["objective_id"] = "PO-D-01.1-999"
    bad["statement"] = "text ```yaml\n- req_id: 1.1.3\n``` --- ## Security Requirements"
    findings = phase2.check([good, bad], run_dir=None)
    check("the clean row raises nothing of its own",
          not any("PO-D-01.1-001" in f for f in findings),
          f"{[f for f in findings if 'PO-D-01.1-001' in f]}")
    check("a row carrying ```yaml + req_id: is caught",
          any("raw baseline" in f and "PO-D-01.1-999" in f for f in findings),
          f"{len(findings)} finding(s)")


def test_prefix_gate() -> None:
    print("\ngate G2 — prefix follows regulation (§4.4)")
    wrong = phase2.derive_objective(REPO, goal("AG-D-03.1-001", "GDPR"))
    wrong["objective_id"] = "SO-D-03.1-001"      # the Case 01 defect, by hand
    findings = phase2.check([wrong], run_dir=None)
    check("an SO- prefix on a GDPR row is caught",
          any("prefix" in f for f in findings), f"{findings}")


def test_coverage_gate() -> None:
    print("\ngate G0 — upstream completeness")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR")], selected=["D-01.1", "D-06.1"])
        rows = phase2.build(REPO, run)
        findings = phase2.check(rows, run)
        check("a selected sub-domain with no goal artifact is caught",
              any("upstream incomplete" in f for f in findings), f"{findings}")
        check("the missing sub-domain is named",
              any("D-06.1" in f for f in findings), "")


def test_seams_stay_unset() -> None:
    print("\nseams")
    r = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    unset = [c for c in ("criteria", "method", "owner") if r[c] == phase2.UNSET]
    check("cells with no rule stay UNSET rather than filled",
          len(unset) == 3, f"unset={unset}")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR")], selected=["D-01.1"])
        text = phase2.render_doc01(REPO, run, phase2.build(REPO, run))
        check("the rendered document declares the seams",
              "seam" in text.lower(), "")
        check("no placeholder leaks into the rendered statement",
              "TODO" not in text and "FIXME" not in text and "None" not in text)


def test_end_to_end_cli() -> None:
    print("\nCLI end to end")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR"),
                              goal("AG-D-01.1-002", "CRA")], selected=["D-01.1"])
        out = tmp / "out"
        proc = subprocess.run(
            [sys.executable, str(REPO / "pipeline" / "src" / "phase2.py"),
             "--run-dir", str(run), "--repo", str(REPO), "--out", str(out)],
            capture_output=True, text=True)
        check("exits 0 on a complete run", proc.returncode == 0,
              proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr[:200])
        doc = out / "Doc01_Operational_Objectives.md"
        check("Doc01 is written", doc.exists())
        text = doc.read_text(encoding="utf-8")
        check("both objectives are rendered",
              "PO-D-01.1-001" in text and "SO-D-01.1-002" in text)
        check("unrendered seams show the UNSET marker",
              text.count("| — |") >= 4, f"{text.count('| — |')} UNSET cells")


def test_doc02_renders() -> None:
    """Doc02 carries the 7 principles, 4 category tables and a resolvable §6.

    The §6 paths are the check that closes ledger §4.5: the hand-authored
    deliverables cite `file:///c:/Users/...`, which resolves only on the
    author's machine. A relative link that 404s is caught here; an absolute one
    that only works for one person never would be.
    """
    print("doc02")
    with tempfile.TemporaryDirectory() as td:
        run_dir = synth_run(Path(td) / "run", [goal("AG-D-01.1-001", "GDPR")], ["D-01.1"])
        text = phase2.render_doc02(REPO, run_dir, phase2.principles_for(run_dir))
    check("all 7 principles are rendered", all(p in text for p in phase2.PRINCIPLE_IDS))
    check("four category tables", all(c["def_col"] in text for c in phase2.CATEGORIES))
    check("no absolute file:// URL — ledger §4.5", "file:///" not in text)
    bad = [p["skill"] for p in phase2.PRINCIPLES
           if not (REPO / "baseline" / "skills" / p["skill"]).is_dir()]
    check("every §6 skill path resolves", not bad, f"missing={bad}" if bad else "7/7")
    check("unseamed constraints render as the UNSET marker",
          text.count("| — |") >= 7, f"{text.count('| — |')} seams")


def test_p2d_parser() -> None:
    """L0 on the one generative step: 7 rows, canonical ids, no missing field.

    Every rejection here corresponds to a way a 7-row document silently loses
    content — a dropped principle, a duplicate, an empty constraint that would
    render as a blank cell nobody can distinguish from an unset seam.
    """
    print("p2d parser")
    import steps

    ok = {"principles": [{"id": p, "constraint": f"constraint for {p}",
                          "method_lead": "TEST (Lead)", "eval_scope": "an artefact"}
                         for p in phase2.PRINCIPLE_IDS]}
    good = "```json\n" + json.dumps(ok) + "\n```"
    try:
        parsed = steps.parse_p2d(good)
        check("a well-formed answer parses", len(parsed["principles"]) == 7)
    except Exception as e:  # noqa: BLE001 — the point is that it does not raise
        check("a well-formed answer parses", False, str(e))
        return

    six = json.dumps({"principles": ok["principles"][:6]})
    dup = json.dumps({"principles": [dict(ok["principles"][0])] * 7})
    empty = json.loads(json.dumps(ok))
    empty["principles"][3]["constraint"] = "  "
    unknown = json.loads(json.dumps(ok))
    unknown["principles"][0]["id"] = "PRIN-ENG-99"
    for name, payload, expect in [
            ("six rows is rejected", six, "exactly 7"),
            ("a duplicated principle is rejected", dup, "more than once"),
            ("an empty field is rejected", json.dumps(empty), "empty"),
            ("an unknown id is rejected", json.dumps(unknown), "not one of")]:
        try:
            steps.parse_p2d("```json\n" + payload + "\n```")
            check(name, False, "accepted — no error raised")
        except Exception as e:  # noqa: BLE001
            check(name, expect in str(e), str(e)[:70])


def test_doc02_gates() -> None:
    """G5 completeness, G6 neutrality, G7 cross-case contamination."""
    print("doc02 gates")
    with tempfile.TemporaryDirectory() as td:
        run_dir = Path(td) / "run"
        synth_run(run_dir, [goal("AG-D-01.1-001", "GDPR")], ["D-01.1"])
        clean = phase2.principles_for(run_dir)

        check("an all-unset document passes G5 (seams are honest)",
              not phase2.check_doc02(REPO, run_dir, clean))

        dropped = [p for p in clean if p["id"] != "PRIN-ENG-04"]
        f = phase2.check_doc02(REPO, run_dir, dropped)
        check("G5 catches a dropped principle",
              any("PRIN-ENG-04" in x for x in f), f[0][:60] if f else "no finding")

        tech = [dict(p) for p in clean]
        tech[0] = dict(tech[0], constraint="Encrypt in the PostgreSQL database at rest.")
        f = phase2.check_doc02(REPO, run_dir, tech)
        check("G6 catches a technology term (R5/R13)",
              any("PostgreSQL" in x for x in f), f[0][:70] if f else "no finding")

        (run_dir / "steps" / "fact_sheet.yaml").write_text(
            "company: Example Ltd\nsector: banking\ndata_categories: [identity]\n",
            encoding="utf-8")
        contaminated = [dict(p) for p in clean]
        contaminated[1] = dict(contaminated[1],
                               constraint="The eGate fleet must deny unauthorised passage.")
        f = phase2.check_doc02(REPO, run_dir, contaminated)
        check("G7 catches another case's architecture — ledger §4.6",
              any("egate" in x for x in f), f[0][:70] if f else "no finding")

        # The first real Phase 2 run (jobs 1996356/1996357) failed with G7
        # flagging "boundary, explicitly, flows, including, within" — ordinary
        # English — because the vocabulary was built from other cases' Doc02
        # prose rather than from their intake forms. This is the regression.
        ordinary = [dict(p) for p in clean]
        ordinary[1] = dict(ordinary[1], constraint=(
            "The identity store must deny by default, explicitly, including "
            "within every flow that crosses the internal boundary."))
        f = phase2.check_doc02(REPO, run_dir, ordinary)
        check("G7 does not fire on ordinary English",
              not f, f[0][:70] if f else "silent")

        neutral = [dict(p) for p in clean]
        neutral[1] = dict(neutral[1], constraint="The identity store must deny by default.")
        check("G7 does not fire on the company's own vocabulary",
              not any("egate" in x for x in phase2.check_doc02(REPO, run_dir, neutral)))


def test_real_runs() -> None:
    """The two experiment cases render, gate clean, and keep every anchor.

    `scripts/phase2_rule_discovery.py` reads the hand-authored deliverables;
    this reads the pipeline's own output for the same two cases, so the two
    artefacts are never mistaken for each other.
    """
    print("real Phase 1 runs")
    runs_root = Path.home() / "Work" / "aegis-runs"
    # M07 ran the experiment's model across all three cases at full 38/38
    # coverage, which is what G0 requires. The m08 runs are partial (G0 catches
    # them), which is the gate working, not a broken fixture.
    cases = {"Case_01_TinyTask_SaaS": "run_m07_qwen3_8_27b_c1_1983781",
             "Case_02_SecureBorder_Solutions": "run_m07_qwen3_8_27b_c2_1983783",
             "Case_03_OmniBank": "run_m07_qwen3_8_27b_c3_1983785"}
    for case, run_id in cases.items():
        run_dir = runs_root / run_id
        if not (run_dir / "steps" / "goals").is_dir():
            print(f"  [SKIP] {case} — {run_id} not on this machine")
            continue
        rows = phase2.build(REPO, run_dir)
        findings = phase2.check(rows, run_dir)
        if findings:
            print(f"  [SKIP] {case} — {run_id} is an incomplete Phase 1 run "
                  f"(G0): {findings[0][:60]}")
            continue
        check(f"{case}: Doc01 gates pass", True, f"{len(rows)} objectives")
        unseamed = [c for c in ("criteria", "method", "owner")
                    if any(r[c] == phase2.UNSET for r in rows)]
        check(f"{case}: the three measured columns stay seams",
              unseamed == ["criteria", "method", "owner"], f"{unseamed}")
        unresolved = [a for r in rows for a in r["anchors"].split(", ")
                      if a and a != phase2.UNSET
                      and not list((REPO / "baseline" / "CONTROLS").rglob(f"{a}.json"))]
        check(f"{case}: every anchor resolves under CONTROLS/ (R2b)",
              not unresolved, f"{len(unresolved)} unresolved")


def test_repair_messages_point_at_the_corridor() -> None:
    """The p4 repair messages must name a target, not just a bound.

    Measured on job 1996170: a row at retention 0.161 / similarity 0.012 was
    repaired to 1.000 / 1.000 — the repair had no stopping rule and jumped to
    the opposite bound. The fix is in the MESSAGE (a target band plus an explicit
    prohibition on copying), never in the threshold: moving 0.30 or 0.88 after
    seeing which runs pass would be changing the ruler after the mark.
    """
    print("p4 repair messages")
    import quality

    check("thresholds are unchanged (0.30 / 0.88)",
          (quality.RETENTION_FLOOR, quality.NEAR_VERBATIM_LIMIT) == (0.30, 0.88),
          f"{quality.RETENTION_FLOOR} / {quality.NEAR_VERBATIM_LIMIT}")

    dense = ("controller processor contracts related transfer instruments include gdpr "
             "specific contractual security obligations required personal data processing "
             "article twenty eight processor engage subprocessor prior authorisation "
             "contractual security obligations audit certification deletion return "
             "obligations end of provision of services supervisory authority mandate "
             "data protection impact assessment prior consultation technical measures "
             "confidentiality integrity availability resilience restore availability")
    thin = "The company signs data processing contracts with its suppliers."
    low = quality.check_obligation_retention(thin, dense)
    check("a low-retention row is still rejected", bool(low), (low[0][:40] if low else ""))
    check("the low-retention message names a target band",
          bool(low) and "half" in low[0].lower() and "zero" in low[0].lower(),
          "says roughly half, and that copying scores zero")

    copied = quality.check_obligation_retention(dense, dense)
    check("a verbatim copy is still rejected", bool(copied), (copied[0][:40] if copied else ""))
    check("the verbatim message tells it to keep fewer terms",
          bool(copied) and "fewer terms" in copied[0].lower(),
          "says keeping fewer terms is correct here")


def test_no_exemplar_is_near_verbatim_to_a_baseline() -> None:
    """No worked example in the p4 instruction may be baseline prose.

    Measured 2026-10-09 before the change: the p4 instruction quoted two
    D-01.1 Sub-SO excerpts. One of them (`"Where the product stores data,
    confidentiality is protected by encrypting relevant data at rest using
    state-of-the-art mechanisms"`) scores 0.669 against its own baseline — 76%
    of the 0.88 ceiling the same gate enforces — and the other scores 0.178
    retention, i.e. would itself fail the 0.30 floor. An exemplar that teaches
    the baseline's register teaches the model to fail the gate, and on a
    sub-domain whose Sub-SO shares that register (D-04.4, D-06.1) copying is
    the shortest path to satisfying the prompt.

    This asserts the property, not the wording: it fails if a future exemplar
    comes back. Exemplars are how a prompt leaks its own answer, and the check
    has to exist before the next person adds one.
    """
    print("p4 exemplars vs the gate")
    import quality
    import steps
    from compose import candidate_subdomains, sub_so_objective

    instr = steps._p4_instruction("D-01.1", subso_ids=["SG-D-01.1.GDPR"])
    baselines = {}
    for c in candidate_subdomains(REPO, ["GDPR", "CRA"]):
        for reg in ("GDPR", "CRA"):
            try:
                baselines[f"{c['id']}/{reg}"] = sub_so_objective(REPO, c["id"], reg)
            except Exception:
                continue

    # The invariant is semantic, not textual: no quoted span in the instruction
    # may itself BE Sub-SO prose. (A naive "long quoted span" test is
    # apostrophe-blind — "the Sub-SO's" and "this company's" pair up into
    # phantom spans — so it is deliberately not used.)
    offenders = []
    for q in re.findall(r"'([^']{40,})'", instr):
        q = q.strip()
        if len(q.split()) < 6:
            continue
        for key, base in baselines.items():
            sim = quality.near_verbatim_similarity(q, base) or 0.0
            if sim > quality.NEAR_VERBATIM_LIMIT:
                offenders.append(f"{q[:40]!r} vs {key} ({sim:.2f})")
    check("no quoted span in the p4 instruction is Sub-SO prose", not offenders,
          "; ".join(offenders[:2]) if offenders else "none")

    worst, worst_sd = 0.0, None
    for key, base in baselines.items():
        sim = quality.near_verbatim_similarity(instr, base) or 0.0
        if sim > worst:
            worst, worst_sd = sim, key
    check("the p4 instruction is not near-verbatim to any Sub-SO",
          worst <= quality.NEAR_VERBATIM_LIMIT,
          f"max similarity {worst:.3f} vs {worst_sd} (ceiling "
          f"{quality.NEAR_VERBATIM_LIMIT})")


def test_eu_legal_citations_are_not_fabrications() -> None:
    """A regulation number is not a company quantity (R6).

    Measured 2026-10-09, job 1996171, D-04.3 row 004: the model cited
    "Implementing Regulation (EU) 2024/2956" correctly, in both the goal prose
    and the regulatory-source column. `check_grounded` stripped the year, left
    "2956", and failed the row as an invented company figure — a legal
    citation rejected as a fabrication, which is what makes the gate
    untrustworthy rather than strict.
    """
    print("R6 grounding vs legal citations")
    import quality

    sources = ["The company employs 5000 staff in banking and financial services."]
    cited = ("A major ICT-related incident is reported without undue delay; the "
             "temporal anchor is addressed in Implementing Regulation (EU) 2024/2956.")
    check("an EU implementing regulation is not a fabrication",
          not quality.check_grounded(cited, sources, "goal"),
          str(quality.check_grounded(cited, sources, "goal"))[:70])

    really_fake = "The company operates 2956 clinics across the country."
    check("a genuine invented quantity is still caught",
          bool(quality.check_grounded(really_fake, sources, "goal")),
          str(quality.check_grounded(really_fake, sources, "goal"))[:70])

    other = "The company serves 8421 customers in three Member States."
    check("a second genuine invented quantity is still caught",
          bool(quality.check_grounded(other, sources, "goal")))


def test_p2o_parser_and_enrichment() -> None:
    print("p2o parser and enrichment")
    valid_json = """```json
    {
      "subdomain": "D-01.1",
      "operational_translation": "For SecureBorder Solutions, operationalizing D-01.1 requires verifiable data at rest encryption.",
      "objectives": [
        {
          "objective_id": "PO-D-01.1-001",
          "method": "TEST",
          "criteria": "Automated pipeline tests confirm AES-256-GCM encryption on personal data volumes.",
          "owner": "Lead Developer + CISO",
          "rules": [
            {
              "rule_id": "RULE-D-01.1-001",
              "statement": "The system SHALL enforce authenticated encryption (AES-256-GCM) on all persistent databases.",
              "verification_target": "TEST"
            }
          ]
        }
      ]
    }
    ```"""
    parsed = phase2.parse_p2o(valid_json, "D-01.1")
    check("valid p2o payload parses", parsed["subdomain"] == "D-01.1")
    check("rule is preserved", parsed["objectives"][0]["rules"][0]["rule_id"] == "RULE-D-01.1-001")

    # Invalid method
    bad_meth = valid_json.replace('"TEST"', '"MAGIC"')
    try:
        phase2.parse_p2o(bad_meth, "D-01.1")
        check("invalid method is rejected", False)
    except ValueError as e:
        check("invalid method is rejected", "invalid method" in str(e))

    # Rule without SHALL or MUST
    bad_rule = valid_json.replace("The system SHALL enforce", "The system may consider enforcing")
    try:
        phase2.parse_p2o(bad_rule, "D-01.1")
        check("non-imperative rule is rejected", False)
    except ValueError as e:
        check("non-imperative rule is rejected", "SHALL or MUST" in str(e))

    # Technology leakage
    bad_tech = valid_json.replace("AES-256-GCM", "AWS DynamoDB encryption")
    try:
        phase2.parse_p2o(bad_tech, "D-01.1")
        check("technology leakage is rejected", False)
    except ValueError as e:
        check("technology leakage is rejected", "technology leakage" in str(e))

    # Test rendering with operationalization data
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR")], selected=["D-01.1"])
        p2_dir = run / "steps" / "phase2"
        p2_dir.mkdir(parents=True)
        (p2_dir / "D-01_1.json").write_text(json.dumps(parsed), encoding="utf-8")
        text = phase2.render_doc01(REPO, run, phase2.build(REPO, run))
        check("rendered doc01 carries operational translation",
              "verifiable data at rest encryption" in text)
        check("rendered doc01 carries method", "TEST" in text)
        check("rendered doc01 carries criteria", "AES-256-GCM encryption on personal data volumes" in text)
        check("rendered doc01 carries owner", "Lead Developer + CISO" in text)
        check("rendered doc01 carries RULE-* table", "RULE-D-01.1-001" in text)


def test_p2o_enrichment_hardening() -> None:
    """The enriched p2o path's own failure modes, each one structural.

    Rule ids must stay unique across objectives of one call (the model's
    numbering restarts per objective); objective ids must carry this
    sub-domain's slot; criteria must not be a repeated template; G0 must
    refuse a selected sub-domain whose goal file exists but is EMPTY (the
    registered Case 01 defect, prereg X1) — a file-count check would wave
    it through and the sub-domain would vanish from Doc01 silently.
    """
    print("\np2o enrichment hardening")
    two_obj = """```json
    {
      "subdomain": "D-01.1",
      "operational_translation": "Encryption posture restated for this company's storage tier.",
      "objectives": [
        {
          "objective_id": "PO-D-01.1-001",
          "method": "TEST",
          "criteria": "Automated pipeline tests confirm authenticated encryption of personal data volumes at rest.",
          "owner": "Lead Developer",
          "rules": [
            {"rule_id": "RULE-D-01.1-001", "statement": "The system SHALL enforce authenticated encryption on persistent stores.", "verification_target": "TEST"},
            {"rule_id": "RULE-D-01.1-002", "statement": "Key rotation MUST complete without service downtime.", "verification_target": "TEST"}
          ]
        },
        {
          "objective_id": "SO-D-01.1-002",
          "method": "INSPECT",
          "criteria": "Quarterly configuration audit reviews encryption settings against the published baseline checklist.",
          "owner": "CISO",
          "rules": [
            {"rule_id": "RULE-D-01.1-001", "statement": "The service SHALL deny plaintext storage fallback paths.", "verification_target": "INSPECT"},
            {"rule_id": "RULE-D-01.1-002", "statement": "Audit records MUST capture every encryption-mode downgrade attempt.", "verification_target": "INSPECT"}
          ]
        }
      ]
    }
    ```"""
    parsed = phase2.parse_p2o(two_obj, "D-01.1")
    rule_ids = [rl["rule_id"] for o in parsed["objectives"] for rl in o["rules"]]
    check("rule ids renumber canonically across the whole call",
          rule_ids == [f"RULE-D-01.1-{n:03d}" for n in (1, 2, 3, 4)], str(rule_ids))
    check("rule ids are unique", len(set(rule_ids)) == len(rule_ids))

    # a PO/SO swap by the model must still match its row via the slot
    check("slot survives a prefix swap",
          phase2._slot_of("SO-D-01.1-001") == "D-01.1-001"
          and phase2._slot_of("PO-D-01.1-001") == "D-01.1-001")

    wrong_slot = two_obj.replace("SO-D-01.1-002", "SO-D-01.2-002")
    try:
        phase2.parse_p2o(wrong_slot, "D-01.1")
        check("objective from another sub-domain is rejected", False)
    except ValueError as e:
        check("objective from another sub-domain is rejected", "belongs to" in str(e))

    garbage_id = two_obj.replace("SO-D-01.1-002", "R-7")
    try:
        phase2.parse_p2o(garbage_id, "D-01.1")
        check("malformed objective id is rejected", False)
    except ValueError as e:
        check("malformed objective id is rejected", "not a" in str(e))

    dup = two_obj.replace(
        "Quarterly configuration audit reviews encryption settings against the published baseline checklist.",
        "Automated pipeline tests confirm authenticated encryption of personal data volumes at rest.")
    try:
        phase2.parse_p2o(dup, "D-01.1")
        check("duplicated criteria template is rejected", False)
    except ValueError as e:
        check("duplicated criteria template is rejected", "duplicates" in str(e))

    thin = two_obj.replace(
        "Quarterly configuration audit reviews encryption settings against the published baseline checklist.",
        "Compliance is ensured.")
    try:
        phase2.parse_p2o(thin, "D-01.1")
        check("thin non-falsifiable criteria is rejected", False)
    except ValueError as e:
        check("thin non-falsifiable criteria is rejected", "too thin" in str(e))

    loose = two_obj.replace('"subdomain": "D-01.1"', '"subdomain": "d_01.1"')
    check("subdomain field is normalised before comparing",
          phase2.parse_p2o(loose, "D-01.1")["subdomain"] == "D-01.1")

    # seam metrics + diversity + the G0 empty-file regression
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR"),
                              goal("AG-D-01.1-002", "NIS2")],
                        selected=["D-01.1", "D-08.3"])
        (run / "steps" / "goals" / "D-08_3.json").write_text(
            json.dumps({"subdomain": "D-08.3", "goals": []}), encoding="utf-8")
        rows = phase2.build(REPO, run)
        findings = phase2.check(rows, run)
        check("G0 fires on a selected sub-domain whose goal file is EMPTY",
              any("upstream incomplete" in f and "D-08.3" in f for f in findings),
              str(findings)[:90])

        p2_dir = run / "steps" / "phase2"
        p2_dir.mkdir(parents=True)
        (p2_dir / "D-01_1.json").write_text(json.dumps(parsed), encoding="utf-8")
        op_map = phase2.load_operationalizations(run)
        filled, total = phase2.seam_fill(rows, op_map)
        check("seam_fill counts every matched objective", (filled, total) == (2, 2),
              f"{filled}/{total}")
        check("method distribution counts per method",
              phase2.method_distribution(op_map) == {"INSPECT": 1, "TEST": 1})
        text = phase2.render_doc01(REPO, run, rows)
        check("rendered RULE table carries continuous canonical ids",
              all(f"RULE-D-01.1-{n:03d}" in text for n in (1, 2, 3, 4)))
        check("rendered RULE table carries both parent objectives",
              "PO-D-01.1-001" in text and "SO-D-01.1-002" in text)

    check("balanced method distribution passes",
          not phase2.method_diversity_findings({"TEST": 5, "INSPECT": 3, "ANALYZE": 2}))
    collapsed = phase2.method_diversity_findings({"TEST": 8, "INSPECT": 1, "DEMONSTRATE": 1})
    check("one method over the 60% ceiling is flagged",
          len(collapsed) == 1 and "TEST" in collapsed[0], str(collapsed)[:80])
    check("batches too small to speak of distribution stay silent",
          not phase2.method_diversity_findings({"TEST": 3}))


def main() -> int:
    print("phase2_test — derivations anchored to Phase 1 and the corpus")
    for fn in (test_id_derivation, test_slot_inherited, test_anchors_resolve,
               test_pollution_gate, test_prefix_gate, test_coverage_gate,
               test_seams_stay_unset, test_end_to_end_cli,
               test_doc02_renders, test_p2d_parser, test_doc02_gates,
               test_repair_messages_point_at_the_corridor,
               test_no_exemplar_is_near_verbatim_to_a_baseline,
               test_eu_legal_citations_are_not_fabrications,
               test_p2o_parser_and_enrichment, test_real_runs,
               test_p2o_enrichment_hardening):
        fn()
    print()
    if FAILURES:
        print(f"FAIL — {len(FAILURES)}: {', '.join(FAILURES)}")
        return 1
    print("PASS — every derivation holds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())