#!/usr/bin/env python3
from pathlib import Path
import hashlib
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "corpus" / "CORPUS_MANIFEST.csv"
CORPUS = ROOT / "corpus" / "annual_reports"

def sha256(path: Path, chunk=1024*1024):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()

def main():
    df = pd.read_csv(MANIFEST)
    expected = df[df["Final_Inclusion_Status"].eq("Included")].copy()
    rows=[]
    for _, r in expected.iterrows():
        rel = str(r["Local_File_Name"])
        p = CORPUS / rel
        exists = p.exists()
        actual_hash = sha256(p) if exists else ""
        expected_hash = str(r["SHA256"])
        rows.append({
            "Report_ID": r["Report_ID"],
            "Company": r["Company"],
            "Cycle": r["Cycle"],
            "Expected_Path": rel,
            "Exists": exists,
            "Hash_Match": bool(exists and actual_hash.lower()==expected_hash.lower()),
            "Expected_SHA256": expected_hash,
            "Actual_SHA256": actual_hash,
        })
    out = pd.DataFrame(rows)
    audit = ROOT / "corpus" / "CORPUS_VERIFICATION.csv"
    out.to_csv(audit,index=False)
    print(f"Expected reports: {len(out)}")
    print(f"Present:          {int(out.Exists.sum())}")
    print(f"Hash matched:     {int(out.Hash_Match.sum())}")
    missing = out[~out.Exists]
    mismatch = out[out.Exists & ~out.Hash_Match]
    if not missing.empty:
        print("\nMissing files:")
        print(missing[["Report_ID","Company","Cycle","Expected_Path"]].to_string(index=False))
    if not mismatch.empty:
        print("\nHash mismatches:")
        print(mismatch[["Report_ID","Company","Cycle","Expected_Path"]].to_string(index=False))
    ok = len(out)==80 and out.Exists.all() and out.Hash_Match.all()
    print(f"\nCORPUS_STATUS: {'PASS' if ok else 'FAIL'}")
    print(f"Audit written to: {audit}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
