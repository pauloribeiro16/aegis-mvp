#!/usr/bin/env python3
"""extract_csf_maturity_tool.py — o workbook de maturidade NIST em JSON.

Lê `docs/research/maturity/NIST-CSF2.0-Maturity-Tool-v1.0.3.xlsx` (S-384, fonte
`PRACTITIONER` — ferramenta de terceiro, **não** publicação da NIST) e escreve
`csf_maturity_tool.json`, a forma que o Inspector consome para reproduzir as
sete folhas em React.

Determinístico, stdlib-only (zipfile + ElementTree — sem openpyxl), zero chamadas
ao modelo. Os valores das células são os *valores em cache* das fórmulas, que é o
que um utilizador vê ao abrir o ficheiro — o mesmo que o `SUM(...)/COUNTA(...)`
do roll-up produz.

Reproduz as sete folhas:
  Introduction        → meta (título, versão, autoria, direcções, changelog)
  Maturity Levels     → levels (1–5 com expectativas de Política e Prática)
  NIST CSF Summary    → tracks[csf].summary (target + média por categoria)
  CSF 2.0             → tracks[csf] (6 funções, 23 categorias, 106 subcategorias)
  Privacy Summary     → tracks[pf].summary
  Privacy Framework Core → tracks[pf] (5 funções, 18 categorias, 100 subcategorias)
  References          → references

Uso: python3 scripts/extract_csf_maturity_tool.py [--repo <repo>] [--check]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REPO_DEFAULT = Path(__file__).resolve().parents[1]
XLSX_REL = "docs/research/maturity/NIST-CSF2.0-Maturity-Tool-v1.0.3.xlsx"
OUT_REL = "docs/research/maturity/csf_maturity_tool.json"

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RELNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PKGREL = "{http://schemas.openxmlformats.org/package/2006/relationships}"

# `A1` → (1, 'A'); coluna-índice → letra (1 → A).
_REF = re.compile(r"^([A-Z]+)(\d+)$")


def col_to_num(letters: str) -> int:
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n


class Book:
    """Leitor mínimo de .xlsx: sharedStrings + valores em cache por folha."""

    def __init__(self, path: Path) -> None:
        self.zip = zipfile.ZipFile(path)
        self.shared = self._shared_strings()
        self.sheets = self._sheet_targets()

    def _xml(self, name: str) -> ET.Element:
        return ET.fromstring(self.zip.read(name))

    def _shared_strings(self) -> list[str]:
        if "xl/sharedStrings.xml" not in self.zip.namelist():
            return []
        out: list[str] = []
        for si in self._xml("xl/sharedStrings.xml").iter(f"{NS}si"):
            # Um `si` pode repartir o texto por vários `r` — concatenar tudo.
            out.append("".join(t.text or "" for t in si.iter(f"{NS}t")))
        return out

    def _sheet_targets(self) -> dict[str, str]:
        rels = {
            r.get("Id"): r.get("Target")
            for r in self._xml("xl/_rels/workbook.xml.rels").iter(f"{PKGREL}Relationship")
        }
        out: dict[str, str] = {}
        for sh in self._xml("xl/workbook.xml").iter(f"{NS}sheet"):
            target = rels[sh.get(f"{RELNS}id")]
            out[sh.get("name")] = "xl/" + target.lstrip("/").removeprefix("xl/")
        return out

    def rows(self, sheet: str) -> list[dict[int, str]]:
        """Cada linha como {coluna(1-based): texto}. Células vazias são omitidas."""
        root = self._xml(self.sheets[sheet])
        out: list[dict[int, str]] = []
        for row in root.iter(f"{NS}row"):
            cells: dict[int, str] = {}
            for c in row.iter(f"{NS}c"):
                m = _REF.match(c.get("r", ""))
                if not m:
                    continue
                col = col_to_num(m.group(1))
                ctype = c.get("t")
                v = c.find(f"{NS}v")
                if ctype == "s":  # índice em sharedStrings
                    text = self.shared[int(v.text)] if v is not None and v.text else ""
                elif ctype == "inlineStr":
                    is_el = c.find(f"{NS}is")
                    text = "".join(t.text or "" for t in is_el.iter(f"{NS}t")) if is_el is not None else ""
                else:
                    # Sem `t` (ou `t="n"`) é o valor em cache: número OU o
                    # resultado já calculado da fórmula (`<f>` + `<v>`).
                    text = (v.text or "") if v is not None else ""
                cells[col] = text
            out.append(cells)
        return out

    def cell(self, rows: list[dict[int, str]], row: int, col: int) -> str:
        """Valor 1-indexado em ambos, como nas fórmulas do Excel."""
        return rows[row - 1].get(col, "").strip() if 0 < row <= len(rows) else ""


# Colunas: A=1. Confirmadas contra os cabeçalhos da linha 2 de cada folha.
COL_FUNCTION, COL_CATEGORY, COL_SUBCAT = 1, 2, 3
COL_EXAMPLES, COL_REFS_A, COL_REFS_B = 4, 5, 6
COL_POLICY, COL_POLICY_WHY, COL_PRACTICE, COL_PRACTICE_WHY = 7, 8, 9, 10
PF_POLICY, PF_POLICY_WHY, PF_PRACTICE, PF_PRACTICE_WHY = 12, 13, 14, 15
PF_FUNCTION, PF_CATEGORY, PF_SUBCAT = 2, 4, 6

_SPLIT_ID = re.compile(r"^([A-Z]{2}\.[A-Z]{2}-[A-Z]?\d+)\s*:\s*(.*)$", re.S)


def _num(raw: str):
    """'3.2857142857142856' → 3.2857…, '' → None. Sem `eval`, sem float() cego."""
    if not raw:
        return None
    try:
        f = float(raw)
    except ValueError:
        return None
    return round(f, 4) if f != int(f) else int(f)


def _split_title(text: str) -> tuple[str, str]:
    """'Data Security (PR.DS): a confidentiality…' → ('Data Security (PR.DS)', 'a confidentiality…')"""
    head, sep, tail = text.partition(":")
    if not sep:
        return text.strip(), ""
    return head.strip(), tail.strip()


def _refs(examples: str, refs_a: str, refs_b: str) -> list[str]:
    """As duas colunas 'Informative References' são a mesma lista partida; junta-se
    sem duplicar e sem inventar referência nenhuma."""
    out: list[str] = []
    for cell in (examples, refs_a, refs_b):
        for line in cell.split("\n"):
            line = line.strip()
            if line and line not in out:
                out.append(line)
    return out


def read_introduction(book: Book) -> dict:
    rows = book.rows("Introduction")
    a2 = book.cell(rows, 2, 1)
    title = re.search(r"Release (.+?)\s*-", a2)
    changelog = [
        line.strip(" *")
        for line in book.cell(rows, 3, 17).split("\n")
        if line.strip(" *")
    ]
    directions = [
        line.strip()
        for line in re.split(r"\n(?=\d\))", book.cell(rows, 31, 1))
        if re.match(r"\d\)", line.strip())
    ]
    # O aviso de "dados de demonstração" não está no Introduction — está em H1 da
    # folha `CSF 2.0`, encostado às colunas de nota que ele desqualifica.
    return {
        "title": "NIST CSF 2.0 Maturity Tool",
        "release_line": title.group(1).strip() if title else "",
        "content_release": a2,
        "version": "v1.0.3",
        "released": "March 1, 2024",
        "author": "John Masserini (independent) — NOT a NIST publication",
        "is_nist_publication": False,
        "preamble": a2,
        "changelog": changelog,
        "directions": directions,
        "demo_values_notice": book.cell(book.rows("CSF 2.0"), 1, 8),
    }


def read_levels(book: Book) -> list[dict]:
    rows = book.rows("Maturity Levels")
    out = []
    for r in range(2, len(rows) + 1):
        label = book.cell(rows, r, 1)
        if not label:
            continue
        m = re.match(r"Level (\d+)\s*-\s*(.+)", label)
        out.append(
            {
                "level": int(m.group(1)) if m else None,
                "name": m.group(2).strip() if m else label,
                "policy": book.cell(rows, r, 2),
                "practice": book.cell(rows, r, 3),
            }
        )
    return out


def read_references(book: Book) -> list[dict]:
    rows = book.rows("References")
    out = []
    for r in range(2, len(rows) + 1):
        doc, link = book.cell(rows, r, 1), book.cell(rows, r, 2)
        if doc:
            out.append({"document": doc, "link": link})
    return out


def _read_track(book: Book, sheet: str, *, header_row: int, fn_col: int, cat_col: int,
                sub_col: int, pol_col: int, polw_col: int, prac_col: int, pracw_col: int,
                summary_sheet: str, sum_first_col: int, sum_count_col: int | None,
                sum_target_col: int, sum_label: str, sum_date_cell: str,
                id_re: str) -> dict:
    """Um 'track' = as duas folhas (Core + Summary) de um referencial.

    As folhas não partilham o layout: o Core põe a função na coluna A e o
    Subcategory na C; o Core do Privacy põe-nas em B/D/F e as notas em L/M/N/O.
    Passamos as colunas em vez de adivinhar dentro do reader.

    `sum_count_col=None` quando a folha Summary não tem coluna «# Controlos» —
    o Core da NIST tem-na em C, o do Privacy não (lá é Target em C), e nesse
    caso a contagem apura-se a partir das subtópicos.
    """
    rows = book.rows(sheet)
    functions: list[dict] = []
    categories: list[dict] = []
    subcategories: list[dict] = []
    cur_fn: dict | None = None
    cur_cat: dict | None = None
    seen_fn: set[str] = set()

    # Linhas de cabeçalho (`Function`/`Category`/`Subcategory`) não são dados.
    header_marker = book.cell(rows, header_row, sub_col).lower()
    assert "subcategory" in header_marker, f"{sheet}: cabeçalho inesperado em {sub_col}"

    for r in range(header_row + 1, len(rows) + 1):
        fn_txt = book.cell(rows, r, fn_col)
        cat_txt = book.cell(rows, r, cat_col)
        sub_txt = book.cell(rows, r, sub_col)

        # Uma linha de função real é `NAME (ID): descrição`. A folha do CSF
        # repete o rótulo sozinho (`GOVERN (GV)`) abaixo dos dados — sem os dois
        # pontos, é eco da navegação interna, não uma função nova.
        if fn_txt and "(" in fn_txt and ":" in fn_txt and fn_txt not in seen_fn:
            seen_fn.add(fn_txt)
            cur_fn = {"id": "", "name": _split_title(fn_txt)[0], "text": fn_txt}
            functions.append(cur_fn)
            cur_cat = None
        if cat_txt and "(" in cat_txt:
            name, desc = _split_title(cat_txt)
            cid = (re.findall(r"\(([A-Z]{2}\.[A-Z]{2}(?:-P)?)\)", name) or [""])[0]
            fn_match = re.match(r"([A-Z]{2})\.", cid)
            cur_cat = {"id": cid, "name": name, "description": desc,
                       "function": fn_match.group(1) if fn_match else ""}
            categories.append(cur_cat)
        if sub_txt:
            m = re.match(id_re, sub_txt)
            if not m:
                continue
            subcategories.append(
                {
                    "id": m.group(1),
                    "text": m.group(2).strip(),
                    "category": cur_cat["id"] if cur_cat else "",
                    "function": cur_cat["function"] if cur_cat else "",
                    "refs": _refs(book.cell(rows, r, sub_col + 1),
                                   book.cell(rows, r, sub_col + 2),
                                   book.cell(rows, r, sub_col + 3))
                    if sub_col == COL_SUBCAT else [],
                    "policy_score": _num(book.cell(rows, r, pol_col)),
                    "policy_reasoning": book.cell(rows, r, polw_col),
                    "practice_score": _num(book.cell(rows, r, prac_col)),
                    "practice_reasoning": book.cell(rows, r, pracw_col),
                }
            )

    # O id da função é o que está dentro dos parênteses: `GOVERN (GV)` → `GV`,
    # `IDENTIFY-P (ID-P)` → `ID` (o sufixo `-P` é do Privacy, não da função).
    # Só as funções; as categorias conservam o id completo (`GV.OC`, `ID.IM-P`)
    # — sobrepor aqui apagava a categoria inteira.
    for fn in functions:
        m = re.search(r"\(([A-Z]{2})(?:-P)?\)", fn["text"])
        fn["id"] = m.group(1) if m else ""

    srows = book.rows(summary_sheet)
    summary: list[dict] = []
    for r in range(2, len(srows) + 1):
        label = book.cell(srows, r, sum_first_col)
        if not label or not book.cell(srows, r, sum_target_col):
            continue
        cid = (re.findall(r"\(([A-Z]{2}\.[A-Z]{2}(?:-P)?)\)", label) or [""])[0]
        if not cid:
            continue  # a linha 3 é `Overall Average Score`, lida à parte
        name = _split_title(label)[0]
        if sum_count_col is not None:
            # A folha da NIST traz `(# controlos)` numa coluna própria, à
            # esquerda do alvo. Sem ela, a contagem vem das subtópicos.
            n = (re.findall(r"\((\d+)\)", book.cell(srows, r, sum_count_col)) or ["0"])[0]
        else:
            n = str(sum(1 for s in subcategories if s["category"] == cid))
        summary.append(
            {
                "id": cid,
                "name": name,
                "n_controls": int(n),
                "target": _num(book.cell(srows, r, sum_target_col)),
                "policy": _num(book.cell(srows, r, sum_target_col + 1)),
                "practice": _num(book.cell(srows, r, sum_target_col + 2)),
            }
        )
    overall = {
        "target": _num(book.cell(srows, 3, sum_target_col)),
        "policy": _num(book.cell(srows, 3, sum_target_col + 1)),
        "practice": _num(book.cell(srows, 3, sum_target_col + 2)),
    }

    return {
        "core_sheet": sheet,
        "summary_sheet": summary_sheet,
        "summary_label": sum_label,
        "summary_date": sum_date_cell,
        "overall_average": overall,
        "functions": functions,
        "categories": categories,
        "subcategories": subcategories,
        "summary": summary,
    }


def build(repo: Path) -> dict:
    xlsx = repo / XLSX_REL
    if not xlsx.exists():
        raise SystemExit(f"missing {xlsx}")
    book = Book(xlsx)

    csf = _read_track(
        book, "CSF 2.0",
        header_row=2, fn_col=COL_FUNCTION, cat_col=COL_CATEGORY, sub_col=COL_SUBCAT,
        pol_col=COL_POLICY, polw_col=COL_POLICY_WHY,
        prac_col=COL_PRACTICE, pracw_col=COL_PRACTICE_WHY,
        summary_sheet="NIST CSF Summary", sum_first_col=2, sum_count_col=3, sum_target_col=4,
        sum_label="NIST CSF 2.0 Categories", sum_date_cell=book.cell(book.rows("NIST CSF Summary"), 1, 5),
        id_re=r"^([A-Z]{2}\.[A-Z]{2}-\d{2})\s*:\s*(.*)$",
    )
    pf = _read_track(
        book, "Privacy Framework Core",
        header_row=3, fn_col=PF_FUNCTION, cat_col=PF_CATEGORY, sub_col=PF_SUBCAT,
        pol_col=PF_POLICY, polw_col=PF_POLICY_WHY,
        prac_col=PF_PRACTICE, pracw_col=PF_PRACTICE_WHY,
        summary_sheet="Privacy Summary", sum_first_col=2, sum_count_col=None, sum_target_col=3,
        sum_label="NIST Privacy 1.0 Categories", sum_date_cell=book.cell(book.rows("Privacy Summary"), 1, 4),
        id_re=r"^([A-Z]{2}\.[A-Z]{2}-P\d+)\s*:\s*(.*)$",
    )
    pf["shading_key"] = [
        book.cell(book.rows("Privacy Framework Core"), r, c)
        for r, c in ((4, 9), (4, 10))
    ]
    pf["shading_key"] = [t for t in pf["shading_key"] if t]
    pf["shading_applied_rows"] = 0  # medido: 0 das 100 subcategorias têm preenchimento

    return {
        "meta": {
            **read_introduction(book),
            "source": XLSX_REL,
            "source_id": "S-384",
            "evidence": "PRACTITIONER",
        },
        "levels": read_levels(book),
        "references": read_references(book),
        "tracks": [csf, pf],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    ap.add_argument("--check", action="store_true",
                    help="falha se o JSON em disco não bater com o que o workbook produz")
    args = ap.parse_args()

    doc = build(args.repo)
    out = args.repo / OUT_REL
    payload = json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=False) + "\n"

    if args.check:
        if not out.exists():
            print(f"CHECK FAIL: {out} não existe")
            return 1
        current = out.read_text(encoding="utf-8")
        if current != payload:
            print(f"CHECK FAIL: {OUT_REL} diverge do workbook")
            return 1
        print(f"CHECK OK: {OUT_REL} reproduce-se byte a byte")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload, encoding="utf-8")

    csf, pf = doc["tracks"]
    print(f"wrote {out.relative_to(args.repo)}")
    print(f"  levels     {len(doc['levels'])}  (1–{max(l['level'] for l in doc['levels'])})")
    for t in (csf, pf):
        scored = sum(1 for s in t["subcategories"] if s["policy_score"] is not None)
        print(f"  {t['summary_label']:28s} {len(t['functions'])} funções  "
              f"{len(t['categories'])} categorias  {len(t['subcategories'])} subcategorias  "
              f"({scored} com nota — dados de demonstração)")
    return 0


if __name__ == "__main__":
    sys.exit(main())