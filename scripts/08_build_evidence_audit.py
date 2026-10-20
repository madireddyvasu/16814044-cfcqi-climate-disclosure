#!/usr/bin/env python3
"""Rebuild the 960-row CFCQI evidence audit from the retained evidence notes.

This avoids storing a manually edited audit table. Every row is derived from:
1) evidence/<firm>_<cycle>.md,
2) the verified annual-report source register, and
3) the locked firm-year dataset.
"""
from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
REGISTER = ROOT / "data/source_register/Vasu_Master_Annual_Report_Register.csv"
DATASET = ROOT / "data/processed/VASU_ANALYSIS_DATASET_LOCKED.csv"
OUTPUT = ROOT / "data/audit/CFCQI_EVIDENCE_AUDIT.csv"

SOURCE_COLS = [
    "Report_ID","Actual_Report_Title","Fiscal_Year_End","Reporting_Period_Start",
    "Reporting_Period_End","Reporting_Period_Months","Local_File_Name","SHA256",
    "Official_Source_URL","Direct_PDF_URL","Alternative_Archive_URL_if_used",
]

def parse_evidence_file(path: Path):
    m = re.fullmatch(r"(F\d{3})_(T1|T)", path.stem)
    if not m:
        return []
    firm_id, cycle = m.groups()
    report_id = f"{firm_id}-{cycle}"
    rows = []
    in_table = False
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("| Item | Score |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and not line.startswith("|"):
            break
        if not in_table or not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4 or not parts[0].isdigit() or parts[1] not in {"0","1","2"}:
            continue
        item = int(parts[0])
        score = int(parts[1])
        page = parts[-1]
        summary = "|".join(parts[2:-1]).strip()
        rows.append({
            "Evidence_ID": f"{report_id}-I{item:02d}",
            "firm_id": firm_id,
            "cycle": cycle,
            "item": item,
            "score": score,
            "page_reference": page,
            "evidence_summary": summary,
            "evidence_file": str(path.relative_to(ROOT)),
            "evidence_complete": "YES",
            "Report_ID": report_id,
        })
    return rows

def main():
    records = []
    for path in sorted(EVIDENCE.glob("F*_T*.md")):
        records.extend(parse_evidence_file(path))
    audit = pd.DataFrame(records)
    if len(audit) != 960:
        raise ValueError(f"Expected 960 evidence decisions, found {len(audit)}")

    reg = pd.read_csv(REGISTER)
    locked = pd.read_csv(DATASET)[["firm_id","firm_name","tcfd_group","cycle"]].drop_duplicates()
    audit = audit.merge(locked, on=["firm_id","cycle"], how="left", validate="many_to_one")
    audit = audit.merge(reg[SOURCE_COLS], on="Report_ID", how="left", validate="many_to_one")

    item_cols = [f"item{i}" for i in range(1,13)]
    scores = pd.read_csv(DATASET)[["firm_id","cycle"] + item_cols]
    long = scores.melt(id_vars=["firm_id","cycle"], var_name="item_name", value_name="locked_score")
    long["item"] = long["item_name"].str.replace("item","",regex=False).astype(int)
    audit = audit.merge(long[["firm_id","cycle","item","locked_score"]],
                        on=["firm_id","cycle","item"], how="left", validate="one_to_one")
    if not (audit["score"] == audit["locked_score"]).all():
        bad = audit.loc[audit["score"] != audit["locked_score"],
                        ["Evidence_ID","score","locked_score"]]
        raise ValueError(f"Evidence/locked-score mismatches:\n{bad.to_string(index=False)}")
    audit = audit.drop(columns="locked_score")

    nonzero_missing_page = (audit["score"] > 0) & audit["page_reference"].isin(["","—","-","–"])
    if nonzero_missing_page.any():
        bad = audit.loc[nonzero_missing_page, ["Evidence_ID","page_reference"]]
        raise ValueError(f"Non-zero evidence rows without page references:\n{bad.to_string(index=False)}")

    cols = [
        "Evidence_ID","firm_id","firm_name","tcfd_group","cycle","item","score",
        "page_reference","evidence_summary","evidence_file","evidence_complete",
        *SOURCE_COLS,
    ]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    audit[cols].sort_values(["firm_id","cycle","item"]).to_csv(OUTPUT,index=False)
    print(f"Wrote {len(audit)} verified evidence rows -> {OUTPUT}")

if __name__ == "__main__":
    main()
