#!/usr/bin/env python3
"""Final integrity audit: 80 reports, 40 firms, 960 CFCQI decisions, unique hashes."""
from pathlib import Path
import re,json,glob
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parents[1]
processed=ROOT/'data/processed/cfcqi_dataset.csv'; register_path=ROOT/'data/source_register/Vasu_Master_Annual_Report_Register.csv'; evidence_dir=ROOT/'evidence'; outdir=ROOT/'data/audit'; outdir.mkdir(parents=True,exist_ok=True)
df=pd.read_csv(processed); reg=pd.read_csv(register_path); items=[f'item{i}' for i in range(1,13)]
issues=[]; evidence_count=0
for fp in sorted(evidence_dir.glob('*.md')):
    m=re.match(r'(F\d{3})_(T1|T)$',fp.stem)
    if not m: continue
    fid,cyc=m.groups(); txt=fp.read_text(errors='ignore')
    rows=[]
    for line in txt.splitlines():
        mm=re.match(r'^\|\s*(\d{1,2})\s*\|\s*([012])\s*\|(.+?)\|\s*(.*?)\s*\|\s*$',line)
        if mm: rows.append((int(mm.group(1)),int(mm.group(2)),mm.group(4).strip()))
    evidence_count += len(rows)
    if len(rows)!=12: issues.append(f'{fp.name}: expected 12 item decisions, found {len(rows)}')
    d=df[(df.firm_id==fid)&(df.cycle==cyc)]
    if len(d)!=1: issues.append(f'{fp.name}: firm-cycle not unique in dataset'); continue
    r=d.iloc[0]
    for item,score,page in rows:
        if int(r[f'item{item}'])!=score: issues.append(f'{fp.name}: item{item} score mismatch')
        if score>0 and page in {'','—','-','–'}: issues.append(f'{fp.name}: item{item} non-zero without page reference')
checks={
 'rows':len(df),'firms':df.firm_id.nunique(),'cycle_T':int((df.cycle=='T').sum()),'cycle_T1':int((df.cycle=='T1').sum()),
 'evidence_decisions':evidence_count,'source_reports':len(reg),'unique_hashes':reg.SHA256.nunique(),
 'missing_items':int(df[items].isna().sum().sum()),'formula_mismatches':int((df[items].sum(axis=1)!=df.raw_score).sum()),
 'cfcqi_formula_mismatches':int((~np.isclose((df.raw_score/24*100).round(1),df.cfcqi)).sum()),'issues':issues,
}
checks['all_pass']=checks['rows']==80 and checks['firms']==40 and checks['cycle_T']==40 and checks['cycle_T1']==40 and checks['evidence_decisions']==960 and checks['source_reports']==80 and checks['unique_hashes']==80 and checks['missing_items']==0 and checks['formula_mismatches']==0 and checks['cfcqi_formula_mismatches']==0 and not issues
(outdir/'FINAL_REPRODUCIBILITY_AUDIT.json').write_text(json.dumps(checks,indent=2)); print(json.dumps(checks,indent=2)); raise SystemExit(0 if checks['all_pass'] else 1)
