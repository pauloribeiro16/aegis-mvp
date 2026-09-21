#!/usr/bin/env python3
"""
Generate NIST CSF 2.0 individual control JSON files for AEGIS baseline.
Replicates the schema and layout of NIST_PF and NIST_AI_RMF in baseline/CONTROLS/.

Outputs to:
  baseline/CONTROLS/NIST_CSF_2.0/
    GOVERN/ (31 subcategories)
    IDENTIFY/ (21 subcategories)
    PROTECT/ (22 subcategories)
    DETECT/ (11 subcategories)
    RESPOND/ (13 subcategories)
    RECOVER/ (8 subcategories)
    CSF_2.0.json (authoritative list of 106 active subcategories)
    _MANIFEST.json (metadata manifest)
"""

import json
import os
import re
import sys
from pathlib import Path

# Base directories
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
BASELINE_CONTROLS_DIR = REPO_ROOT / "baseline" / "CONTROLS"
TARGET_DIR = BASELINE_CONTROLS_DIR / "NIST_CSF_2.0"

# Source paths
SOURCE_JSON_CANDIDATES = [
    REPO_ROOT.parent / "methodology-main" / "03_REFERENCE_MATERIAL" / "Framework_Mappings" / "NIST_CSF" / "NIST_CSF_2.0.json",
    REPO_ROOT.parent / "Methodology_compact" / "03_REFERENCE_MATERIAL" / "Framework_Mappings" / "NIST_CSF" / "NIST_CSF_2.0.json",
]

ACTIVE_LIST_CANDIDATES = [
    REPO_ROOT.parent / "methodology_compact" / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS" / "NIST_CSF_2.0" / "CSF_2.0.json",
    REPO_ROOT.parent / "Methodology_compact" / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS" / "NIST_CSF_2.0" / "CSF_2.0.json",
]

MANIFEST_CANDIDATES = [
    REPO_ROOT.parent / "methodology_compact" / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS" / "NIST_CSF_2.0" / "_MANIFEST.json",
    REPO_ROOT.parent / "Methodology_compact" / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS" / "NIST_CSF_2.0" / "_MANIFEST.json",
]


def find_existing_path(candidates, desc):
    for p in candidates:
        if p.exists():
            return p
    print(f"ERROR: Could not find {desc} in candidate paths:")
    for p in candidates:
        print(f"  - {p}")
    sys.exit(1)


def clean_category_name(raw_name: str) -> str:
    # E.g. "Organizational Context (GV.OC): The circumstances - mission..." -> "Organizational Context (GV.OC)"
    return raw_name.split(":")[0].strip()


def clean_subcategory_text(sid: str, raw_desc: str) -> str:
    prefix = f"{sid}:"
    if raw_desc.startswith(prefix):
        return raw_desc[len(prefix):].strip()
    return raw_desc.strip()


def clean_examples(raw_examples: list) -> list:
    cleaned = []
    for ex in raw_examples:
        # Strip "Ex1: " or "Ex10: "
        c = re.sub(r"^Ex\d+:\s*", "", ex).strip()
        if c:
            cleaned.append(c)
    return cleaned


def build_assessment_objectives(sid: str, text: str, examples: list) -> list:
    clean_text = text.rstrip(".")
    words = clean_text.split()
    if words and len(words[0]) > 1 and words[0].isupper():
        target_text = clean_text
    else:
        target_text = clean_text[0].lower() + clean_text[1:] if clean_text else clean_text
    
    objectives = [f"Determine whether {target_text}."]
    
    common_verbs = {
        "create", "maintain", "deploy", "monitor", "restrict", "use", "share", "require",
        "communicate", "review", "manage", "conduct", "establish", "implement", "track",
        "perform", "design", "confirm", "request", "designate", "initiate", "document",
        "verify", "test", "assess", "train", "update", "identify", "isolate", "contain",
        "mitigate", "eradicate", "recover", "restore", "notify", "coordinate", "compare",
        "align", "integrate", "automate", "reconcile", "prioritize", "classify", "categorize",
        "define", "publish", "disseminate", "enforce", "audit", "evaluate", "investigate",
        "ensure", "protect", "configure", "apply", "execute", "retain", "dispose", "destroy",
        "store", "backup", "replicate", "sanitize", "revoke", "disable", "authenticate",
        "authorize", "validate", "inspect", "remediate", "re-evaluate", "measure"
    }

    if examples:
        for ex in examples[:2]:
            ex_clean = ex.rstrip(".")
            w1 = ex_clean.split()[0].lower() if ex_clean.split() else ""
            ex_target = ex_clean[0].lower() + ex_clean[1:] if ex_clean else ex_clean
            if w1 in common_verbs:
                objectives.append(f"Determine whether activities are conducted to {ex_target}.")
            else:
                objectives.append(f"Determine whether mechanisms ensure that {ex_target}.")
            
    objectives.append("Determine whether implementation outcomes are monitored, evaluated, and documented.")
    return objectives


def build_informative_references(sc: dict, sid: str) -> list:
    refs = [f"NIST CSF 2.0 Core: {sid}"]
    cr_dict = {}
    for cr in sc.get("crossReferences", []):
        fw = cr.get("framework")
        cr_dict[fw] = cr.get("references", [])
    
    # 1. SP 800-53 Rev 5
    sp = cr_dict.get("SP 800-53 Rev 5.1.1", []) + cr_dict.get("SP 800-53 Rev 5.2.0", [])
    if sp:
        sp_unique = sorted(list(set(sp)))
        if len(sp_unique) > 8:
            sp_str = ", ".join(sp_unique[:8]) + f" (+{len(sp_unique)-8} more)"
        else:
            sp_str = ", ".join(sp_unique)
        refs.append(f"NIST SP 800-53 Rev. 5: {sp_str}")
        
    # 2. ISO/IEC 27001
    iso = cr_dict.get("ISO/IEC 27001", [])
    if iso:
        cleaned_iso = []
        for r in iso:
            c = r.replace("2022: ", "").replace("Mandatory Clause: ", "Clause ").replace("Annex A Controls: ", "Annex A.")
            c = c.strip().rstrip(",")
            if c and c != "Clause None" and c != "Annex A." and c not in cleaned_iso:
                cleaned_iso.append(c)
        if cleaned_iso:
            if len(cleaned_iso) > 8:
                iso_str = ", ".join(cleaned_iso[:8]) + f" (+{len(cleaned_iso)-8} more)"
            else:
                iso_str = ", ".join(cleaned_iso)
            refs.append(f"ISO/IEC 27001:2022: {iso_str}")
            
    # 3. CSF v1.1
    csf11 = cr_dict.get("CSF v1.1", [])
    if csf11:
        csf11_str = ", ".join(sorted(list(set(csf11))))
        refs.append(f"CSF v1.1: {csf11_str}")
        
    # 4. CIS Controls
    cis = cr_dict.get("CIS Controls v8.1", []) or cr_dict.get("CIS Controls v8.0", [])
    if cis:
        cis_str = ", ".join(sorted(list(set(cis))))
        refs.append(f"CIS Controls v8: {cis_str}")
        
    # 5. PCI DSS
    pci = cr_dict.get("PCI DSS", [])
    if pci:
        pci_unique = sorted(list(set(pci)))
        if len(pci_unique) > 6:
            pci_str = ", ".join(pci_unique[:6]) + f" (+{len(pci_unique)-6} more)"
        else:
            pci_str = ", ".join(pci_unique)
        refs.append(f"PCI DSS: {pci_str}")
        
    # 6. SSDF
    ssdf = cr_dict.get("SSDF", [])
    if ssdf:
        ssdf_str = ", ".join(sorted(list(set(ssdf))))
        refs.append(f"NIST SP 800-218 (SSDF): {ssdf_str}")
        
    # 7. CRI Profile
    cri = cr_dict.get("CRI Profile v2.0", [])
    if cri:
        cri_str = ", ".join(sorted(list(set(cri))))
        refs.append(f"CRI Profile v2.0: {cri_str}")

    return refs


def main():
    source_json_path = find_existing_path(SOURCE_JSON_CANDIDATES, "NIST CSF 2.0 source JSON")
    active_list_path = find_existing_path(ACTIVE_LIST_CANDIDATES, "active subcategories list (CSF_2.0.json)")
    manifest_path = find_existing_path(MANIFEST_CANDIDATES, "_MANIFEST.json")

    print(f"Loading source JSON from: {source_json_path}")
    with open(source_json_path, "r", encoding="utf-8") as f:
        full_data = json.load(f)

    print(f"Loading active subcategories list from: {active_list_path}")
    with open(active_list_path, "r", encoding="utf-8") as f:
        active_data = json.load(f)
    active_ids = set(active_data["subcategories"])
    print(f"Active subcategories count: {len(active_ids)}")

    # Index all subcategories and their category groupings
    subcat_by_id = {}
    peers_by_cat = {}  # cat_code -> list of active subcat IDs
    cat_metadata = {}  # cat_code -> (func_name, cat_clean_name)

    for func_code, func_obj in full_data.items():
        func_name = func_obj.get("name")  # e.g. GOVERN, IDENTIFY, etc.
        for cat_code, cat_obj in func_obj.get("categories", {}).items():
            cat_clean = clean_category_name(cat_obj.get("name", ""))
            cat_metadata[cat_code] = (func_name, cat_clean)
            for sc in cat_obj.get("subcategories", []):
                sid = sc.get("id")
                if sid in active_ids:
                    subcat_by_id[sid] = sc
                    peers_by_cat.setdefault(cat_code, []).append(sid)

    print(f"Indexed {len(subcat_by_id)} active subcategories across {len(peers_by_cat)} categories.")

    # Create destination directories
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    # Copy / write CSF_2.0.json and _MANIFEST.json to TARGET_DIR
    target_csf_json = TARGET_DIR / "CSF_2.0.json"
    with open(target_csf_json, "w", encoding="utf-8") as f:
        json.dump(active_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest_data = json.load(f)
        target_manifest = TARGET_DIR / "_MANIFEST.json"
        with open(target_manifest, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2, ensure_ascii=False)
            f.write("\n")

    # Generate each control JSON file
    generated_counts = {}
    for cat_code, sids in peers_by_cat.items():
        func_name, cat_clean = cat_metadata[cat_code]
        func_dir = TARGET_DIR / func_name
        func_dir.mkdir(parents=True, exist_ok=True)
        generated_counts.setdefault(func_name, 0)

        for sid in sids:
            sc = subcat_by_id[sid]
            subcat_text = clean_subcategory_text(sid, sc.get("description", ""))
            examples = clean_examples(sc.get("implementationExamples", []))
            assessment_objs = build_assessment_objectives(sid, subcat_text, examples)
            informative_refs = build_informative_references(sc, sid)

            # Related controls: peers in the same category
            peer_ids = [p for p in sids if p != sid]
            related = [f"{p} (NIST CSF 2.0 — same category)" for p in peer_ids]

            control_doc = {
                "control_id": sid,
                "framework": "NIST CSF 2.0",
                "function": func_name,
                "category": cat_clean,
                "subcategory_id": sid,
                "subcategory_text": subcat_text,
                "informative_references": informative_refs,
                "implementation_examples": examples,
                "assessment_objectives": assessment_objs,
                "related_controls": related,
                "source_url": "https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf",
                "source_version": "NIST CSF 2.0 (February 26, 2024)",
            }

            file_path = func_dir / f"{sid}.json"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(control_doc, f, indent=2, ensure_ascii=False)
                f.write("\n")

            generated_counts[func_name] += 1

    print("\nGeneration summary:")
    total_generated = 0
    for func_name, cnt in sorted(generated_counts.items()):
        print(f"  {func_name}: {cnt} files")
        total_generated += cnt

    print(f"\nTotal generated control files: {total_generated}")
    if total_generated == 106:
        print("SUCCESS: Exactly 106 NIST CSF 2.0 control files generated.")
    else:
        print(f"WARNING: Expected 106 files, but generated {total_generated}!")
        sys.exit(1)


if __name__ == "__main__":
    main()
