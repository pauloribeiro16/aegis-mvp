#!/usr/bin/env python3
"""build_domain_cases.py — generate cases_domain.json from the real artefacts.

Everything a case quotes is EXTRACTED from a file on disk. The only hand
written parts are the labels and the warrant note, and every hand quoted
string is VERIFIED to appear verbatim in its source file before the file is
written — a transcription slip fails the build instead of silently becoming
a test case.

    python3 build_domain_cases.py --out cases_domain.json

Sources (workstation):
    ~/Work/aegis-runs/run_p2enr_c1/steps/          the pipeline's own artefacts
    <repo>/baseline/domains/                        the frozen corpus
    <repo>/cases/Case_01_TinyTask_SaaS/             the reference deliverables
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HOME = Path.home()
REPO = Path(__file__).resolve().parents[2]
RUN = HOME / "Work" / "aegis-runs" / "run_p2enr_c1"
STEPS = RUN / "steps"
CORPUS = REPO / "baseline" / "domains"
CASE1 = REPO / "cases" / "Case_01_TinyTask_SaaS"

VERDICTS = [
    "Fully covered (anchored)",
    "Partially covered (functional leg + explicit carve-out)",
    "No functional carrier (organizational)",
    "Design guidance",
    "N/A",
]


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"missing source: {path}")
    return path.read_text(encoding="utf-8")


def must_contain(text: str, needle: str, source: Path) -> str:
    """A hand quoted string must appear verbatim in its source."""
    if needle not in text:
        raise SystemExit(
            f"hand-quoted text is not verbatim in {source}:\n  {needle[:200]!r}")
    return needle


def tension_condition(subdomain: str, keyword: str) -> tuple[str, str]:
    """The corpus paragraph that declares a tension's activation condition.

    The whole numbered entry is returned, because the condition and its
    negation live in the same entry.
    """
    hits = list(CORPUS.glob(f"*/{subdomain}/cross/_interactions.md"))
    if not hits:
        raise SystemExit(f"no _interactions.md for {subdomain}")
    path = hits[0]
    text = read(path)
    m = re.search(r"^##+\s*Emergent tensions.*$", text, re.M)
    if not m:
        raise SystemExit(f"no 'Emergent tensions' section in {path}")
    tail = text[m.start():]
    end = re.search(r"^##\s", tail[10:], re.M)
    section = tail[: end.start() + 10] if end else tail

    parts = re.split(
        r"\n(?=\s*(?:\*\*)?\d+\s*(?:\*\*)?[a-z ]*(?:emergent tension|conditional|\.))",
        section)
    for part in parts:
        if keyword.lower() in part.lower():
            body = re.sub(r"\s+", " ", part).strip()
            return body, str(path.relative_to(REPO))
    raise SystemExit(f"tension {keyword!r} not found in {path}")


def fact_sheet() -> str:
    return read(STEPS / "fact_sheet.yaml").strip()


def confirmed_regs() -> list[str]:
    """The regulations P2 confirmed as applying, read from the verdicts table."""
    regs = []
    for line in read(STEPS / "verdicts.md").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and "applies" in cells[1] and "does not apply" not in cells[1]:
            regs.append(cells[0].strip("*` "))
    return regs


# --------------------------------------------------------------------------
# the hand-set labels and their warrants
# --------------------------------------------------------------------------
TENSION_LABELS = [
    ("T-001", "Five-track timeline divergence", "D-04.3", True,
     "The condition is multi-reg overlap on the same incident event. Two "
     "regulations are confirmed (GDPR and CRA), so the overlap holds and the "
     "tension activates."),
    ("T-002", "Recipient fragmentation", "D-04.3", True,
     "Same condition as T-001: the same incident event reaches more than one "
     "confirmed regulation, so a single routing decision is required."),
    ("T-003", "3-way retention", "D-05.2", False,
     "The condition engages only when a CRA update log or an AI log contains "
     "personal data, or a single data flow crosses regime boundaries. The "
     "fact sheet records zero AI/ML systems and the default CRA class with "
     "self-assessment conformity, so the condition does not hold."),
    ("T-004", "four-party boundary architecture", "D-06.4", False,
     "The condition is that the provider is a non-EU provider or manufacturer "
     "requiring simultaneous representatives. TinyTask is established in "
     "Portugal (EU) and is not a non-EU provider, so the condition does not "
     "hold."),
    ("T-005", "opt-out", "D-10.1", True,
     "This tension declares NO activation condition: the corpus states the "
     "conflict is structural and preserved as a Layer 2 review item because "
     "no OJ-level consolidation rule exists at D-10.1. The conflict is live "
     "for this company because CRA (which permits the product-level user "
     "opt-out) and GDPR (which imposes entity-level monitoring) both apply. "
     "The pipeline's own resolution for this company keeps GDPR Art. 32(2) "
     "monitoring at the entity layer."),
]

# The sub-domain that carries an objective unrelated to each principle.
PRINCIPLE_UNBOUND = {
    "PRIN-ENG-01": "D-09.2",
    "PRIN-ENG-02": "D-01.4",
    "PRIN-ENG-03": "D-08.1",
    "PRIN-ENG-04": "D-02.2",
    "PRIN-ENG-05": "D-05.1",
    "PRIN-ENG-06": "D-06.1",
    "PRIN-ENG-07": "D-10.3",
}


def summary_text(summaries: dict[str, str], oid: str) -> str:
    return summaries.get(oid, "(no summary recorded for this objective)")


def first_objective_of(subdomain: str, summaries: dict[str, str],
                        exclude: list[str]) -> str | None:
    for oid in sorted(summaries):
        if oid.startswith(("PO-" + subdomain, "SO-" + subdomain)) and oid not in exclude:
            return oid
    return None


def parse_matrix(md: str) -> list[dict]:
    rows = []
    for line in md.splitlines():
        if not line.startswith(("| `PO-", "| `SO-")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        state_cell = cells[4].replace("*", "")
        verdict = None
        for v in VERDICTS:
            if state_cell.startswith(v.split(" (")[0]):
                verdict = v
                break
        if verdict is None:
            for v in VERDICTS:
                if v.split(" (")[0] in state_cell:
                    verdict = v
                    break
        if verdict is None:
            continue
        rows.append({"objective": cells[0], "summary": cells[1], "carrier": cells[2],
                     "verdict": verdict, "discharge": cells[5]})
    return rows


ADJUSTMENT_PAIRS = [
    ("verbatim_d10_1_cra",
     "A product with digital elements **provides security-related information by recording "
     "and monitoring relevant internal activity, including access to or modification of "
     "data, services or functions, and provides an opt-out mechanism for the user** "
     "(Annex I Part I (2)(l) CRA); the manufacturer **facilitates the sharing of "
     "information about potential vulnerabilities** through a single contact address "
     "(Annex I Part II (6) CRA).",
     "The product provides security-related information by recording and monitoring "
     "relevant internal activity, including access to or modification of data, services "
     "or functions, with an opt-out mechanism for the user, and the company facilitates "
     "the sharing of information about potential vulnerabilities through a single contact "
     "address.",
     "Near-verbatim pair (D-10.1 / CRA, AG-D-10.1-002)."),
    ("proportional_d10_1_gdpr",
     "The controller and processor implement appropriate technical and organisational "
     "measures to ensure the **ongoing confidentiality, integrity, availability and "
     "resilience of processing systems and services** (Art. 32(1)(b) GDPR) and "
     "**regularly test, assess and evaluate their effectiveness** (Art. 32(1)(d) GDPR); "
     "personal-data processing systems and services are monitored for the five Art. 32(2) "
     "risk types, with a clear definition of the moment of `becoming aware of` a breach "
     "to anchor the Art. 33(1) 72-hour notification clock.",
     "The company implements appropriate technical and organisational measures to ensure "
     "the ongoing confidentiality, integrity, availability and resilience of processing "
     "systems and services and regularly tests, assesses and evaluates their "
     "effectiveness, monitoring for the five Art. 32(2) risk types with a clear "
     "definition of the moment of becoming aware of a breach.",
     "Proportional restatement (D-10.1 / GDPR, AG-D-10.1-001)."),
    ("narrowed_d02_2_cra",
     "Vulnerabilities of a product with digital elements are addressed and remediated "
     "through security updates without delay, including — where technically feasible — "
     "through security updates provided separately from functionality updates (Annex I "
     "Part II (2) + Annex I Part I (2)(c)); security updates are disseminated without "
     "delay to users via mechanisms that ensure the secure distribution of updates, "
     "accompanied by advisory messages describing the action users can take (Annex I Part "
     "II (7) + (8)); vulnerabilities — including those of integrated components — are "
     "handled effectively and in accordance with the Annex I Part II vulnerability-handling "
     "requirements throughout the support period determined by the manufacturer (minimum 5 "
     "years, or the expected use time if shorter — Art. 13(8)); each security update made "
     "available during the support period remains available after it has been issued for at "
     "least 10 years or for the remainder of the support period, whichever is longer "
     "(Art. 13(9)).",
     "Vulnerabilities are addressed and remediated through security updates without delay, "
     "provided separately from functionality updates where technically feasible, and "
     "disseminated to users via mechanisms ensuring secure distribution together with "
     "advisory messages describing the action users can take.",
     "Scope narrowing (D-02.2 / CRA, AG-D-02.2-002): the support-period floor and the "
     "10-year availability tail leave the goal text but stay in the Articles cell."),
]


def build() -> dict:
    facts = fact_sheet()
    reg_line = ", ".join(confirmed_regs())
    cases: list[dict] = []

    # -- tension activation -------------------------------------------------
    tension_rows = {}
    for line in read(STEPS / "tensions.md").splitlines():
        if line.startswith("| T-"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5:
                tension_rows[cells[0]] = cells
    for tid, keyword, subdomain, label, warrant in TENSION_LABELS:
        if tid not in tension_rows:
            raise SystemExit(f"{tid} is not in the pipeline's tensions.md")
        row = tension_rows[tid]
        condition, corpus_path = tension_condition(subdomain, keyword)
        state = (
            f"COMPANY FACTS (verbatim from the Phase 1 fact sheet):\n{facts}\n\n"
            f"REGULATIONS CONFIRMED AS APPLYING: {reg_line}\n\n"
            f"CORPUS TENSION CONDITION (verbatim from {corpus_path}):\n{condition}\n\n"
            f"QUESTION: does the activation condition declared above hold for this "
            f"company, so that the tension activates?"
        )
        cases.append({
            "id": f"domain.tension.{tid.lower()}",
            "tags": ["L3", "tension-activation"],
            "state": state,
            "questions": {
                "activates": {
                    "type": "noul",
                    "instructions": "Does this corpus tension activate for this company?",
                }
            },
            "expect": {"answer_type": "noul", "labels": {"activates": label}},
            "provenance": (
                f"Label from the corpus condition ({corpus_path}) applied to the fact "
                f"sheet. Warrant: {warrant} The pipeline's own row for {tid} reads: "
                f"{row[4][:400]}"),
        })

    # -- sub-domain trigger -------------------------------------------------
    selected: dict[str, str] = {}
    for line in read(STEPS / "selection.md").splitlines():
        m = re.match(r"\|\s*(D-\d\d\.\d)\s*\|\s*([^|]+)\|\s*([^|]+)\|", line)
        if m:
            selected[m.group(1)] = f"{m.group(2).strip()} — {m.group(3).strip()}"
    contested = {"D-02.4", "D-06.4", "D-08.3"}
    for sd, why in sorted(selected.items()):
        is_contested = sd in contested
        case = {
            "id": f"domain.trigger.{sd.replace('-', '_').replace('.', '_')}",
            "tags": ["L3", "subdomain-trigger"],
            "state": (
                f"COMPANY FACTS (verbatim from the Phase 1 fact sheet):\n{facts}\n\n"
                f"REGULATIONS CONFIRMED AS APPLYING: {reg_line}\n\n"
                f"CANDIDATE SUB-DOMAIN: {sd} — {why}"
            ),
            "questions": {
                "triggered": {
                    "type": "noul",
                    "instructions": f"Is sub-domain {sd} triggered for this company?",
                }
            },
            "expect": {"answer_type": "noul"},
            "provenance": (
                "Trigger rationale from run_p2enr_c1/steps/selection.md. The "
                "hand-written Case_01 deliverable lists "
                + (f"{sd} in not_addressed_subdomains, so the two artefacts "
                   "DISAGREE and the label is contested."
                   if is_contested else
                   f"{sd} as active (35 active sub-domains), which both artefacts agree on.")),
        }
        if is_contested:
            case["expect"]["labels"] = {"triggered": False}
            case["expect"]["contested"] = True
        else:
            case["expect"]["labels"] = {"triggered": True}
        cases.append(case)

    # -- principle constraints ----------------------------------------------
    principles = {p["id"]: p
                  for p in json.loads(read(STEPS / "principles.json"))["principles"]}
    summaries: dict[str, str] = {}
    for path in sorted((STEPS / "phase3a_map").glob("*.json")):
        for v in json.loads(read(path)).get("verdicts", []):
            summaries[v["id"]] = v.get("summary", "").strip()
    for pid in sorted(principles):
        constraint = principles[pid]["constraint"]
        props = json.loads(read(STEPS / "phase3a_prin" / f"{pid}.json")).get("proposals", [])
        if not props:
            continue
        bound_ids = [p["objective"] for p in props] + \
                    [o for p in props for o in p.get("also_carries", [])]
        bound = bound_ids[0]
        cases.append({
            "id": f"domain.principle.{pid.lower().replace('-', '_')}.bound",
            "tags": ["L3", "principle-constraint"],
            "state": (
                f"PRINCIPLE {pid} — CONSTRAINT (verbatim from the Phase 2 principles "
                f"artifact):\n{constraint}\n\n"
                f"CANDIDATE OBJECTIVE: {bound}\n{summary_text(summaries, bound)}"
            ),
            "questions": {
                "constrains": {
                    "type": "noul",
                    "instructions": "Does this principle constrain the candidate objective?",
                }
            },
            "expect": {"answer_type": "noul", "labels": {"constrains": True}},
            "provenance": (
                f"Label from the pipeline's own binding: run_p2enr_c1/steps/phase3a_prin/"
                f"{pid}.json binds {pid} to {bound}."),
        })
        other_sd = PRINCIPLE_UNBOUND.get(pid)
        if other_sd:
            other = first_objective_of(other_sd, summaries, bound_ids)
            if other:
                cases.append({
                    "id": f"domain.principle.{pid.lower().replace('-', '_')}.unbound",
                    "tags": ["L3", "principle-constraint"],
                    "state": (
                        f"PRINCIPLE {pid} — CONSTRAINT (verbatim from the Phase 2 principles "
                        f"artifact):\n{constraint}\n\n"
                        f"CANDIDATE OBJECTIVE: {other}\n{summary_text(summaries, other)}"
                    ),
                    "questions": {
                        "constrains": {
                            "type": "noul",
                            "instructions": "Does this principle constrain the candidate objective?",
                        }
                    },
                    "expect": {"answer_type": "noul", "labels": {"constrains": False}},
                    "provenance": (
                        f"Negative case: {other} lives in {other_sd}, a domain unrelated to "
                        f"{pid}, and is not among the objectives {pid} binds."),
                })

    # -- coverage verdict ---------------------------------------------------
    matrix = (CASE1 / "03_PHASE3_SPEC/part1_security_privacy/synthesis_rounds"
              / "OBJECTIVE_MAPPING.md")
    by_verdict: dict[str, dict] = {}
    for row in parse_matrix(read(matrix)):
        if row["verdict"] not in by_verdict:
            by_verdict[row["verdict"]] = row
    for v in VERDICTS:
        row = by_verdict.get(v)
        if row is None:
            continue
        cases.append({
            "id": f"domain.coverage.{row['objective'].strip('`').replace('-', '_').lower()}",
            "tags": ["L3", "coverage-verdict"],
            "state": (
                f"OBJECTIVE: {row['objective']}\n{row['summary']}\n\n"
                f"FUNCTIONAL CARRIER: {row['carrier']}\n\n"
                f"VC DISCHARGE: {row['discharge']}\n\n"
                f"QUESTION: which coverage verdict applies to this objective?"
            ),
            "questions": {
                "verdict": {
                    "type": "choice",
                    "instructions": "Which coverage verdict applies to this objective?",
                    "criteria": {v.replace(" ", "_"): v for v in VERDICTS},
                }
            },
            "expect": {"answer_type": "choice",
                       "labels": {"verdict": v.replace(" ", "_")}},
            "provenance": (
                f"Verdict vocabulary ADR-007 D4. Row from the reference matrix "
                f"{matrix.relative_to(REPO)}."),
        })

    # -- adjustment classification (labelling contingent) --------------------
    doc02_path = CASE1 / "01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md"
    doc02 = read(doc02_path)
    for tag, baseline, adjusted, note in ADJUSTMENT_PAIRS:
        must_contain(doc02, baseline, doc02_path)
        must_contain(doc02, adjusted, doc02_path)
        cases.append({
            "id": f"domain.adjustment.{tag}",
            "tags": ["L3", "adjustment", "unlabelled"],
            "state": f"BASELINE (regulation-neutral Sub-SO, verbatim):\n{baseline}\n\n"
                     f"ADJUSTED GOAL (verbatim):\n{adjusted}",
            "questions": {
                "relation": {
                    "type": "choice",
                    "instructions": "How does the adjusted goal relate to the baseline?",
                    "criteria": {
                        "verbatim": "The adjusted goal restates the baseline without changing it.",
                        "proportional": "The adjusted goal restates the baseline proportionately for this company.",
                        "narrowed": "The adjusted goal drops or moves out a mandatory leg of the baseline.",
                    },
                }
            },
            "expect": {"answer_type": "choice"},
            "provenance": (
                f"{note} NO LABEL: the L2 rubric that could adjudicate this does not "
                f"exist yet, so the case is measured, not scored."),
        })

    return {"version": 1, "name": "domain", "cases": cases}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out",
                    default=str(Path(__file__).resolve().parent / "cases_domain.json"))
    args = ap.parse_args()
    data = build()
    Path(args.out).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
    print(f"wrote {args.out}: {len(data['cases'])} cases")
    by_tag: dict[str, int] = {}
    for c in data["cases"]:
        for t in c.get("tags", []):
            by_tag[t] = by_tag.get(t, 0) + 1
    for tag, n in sorted(by_tag.items()):
        print(f"  {tag}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
