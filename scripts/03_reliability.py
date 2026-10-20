#!/usr/bin/env python3
"""Repeat-scoring reliability: exact agreement and weighted Cohen's kappa.

The code deliberately uses neutral 'repeat scoring' terminology. Label the exercise
'intra-coder' or 'inter-coder' only when coder provenance is documented.
"""
import argparse,sys
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.cfcqi import ITEMS,ITEM_LABELS,percent_agreement,weighted_kappa

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--original',default=str(ROOT/'data/processed/cfcqi_dataset.csv')); ap.add_argument('--recode',default=str(ROOT/'data/input/reliability_recode.csv')); ap.add_argument('--output',default=str(ROOT/'results/tables/reliability.csv')); a=ap.parse_args()
    orig=pd.read_csv(a.original)[['firm_id','cycle']+ITEMS]; rec=pd.read_csv(a.recode)[['firm_id','cycle']+ITEMS]; m=orig.merge(rec,on=['firm_id','cycle'],suffixes=('_orig','_re'))
    rows=[]
    for c in ITEMS:
        x,y=m[f'{c}_orig'],m[f'{c}_re']; rows.append({'item':c,'label':ITEM_LABELS[c],'n':len(x),'pct_agreement':round(percent_agreement(x,y)*100,1),'weighted_kappa':round(weighted_kappa(x,y),3)})
    x=pd.concat([m[f'{c}_orig'] for c in ITEMS]); y=pd.concat([m[f'{c}_re'] for c in ITEMS]); rows.append({'item':'ALL','label':'pooled across items','n':len(x),'pct_agreement':round(percent_agreement(x,y)*100,1),'weighted_kappa':round(weighted_kappa(x,y),3)})
    out=pd.DataFrame(rows); Path(a.output).parent.mkdir(parents=True,exist_ok=True); out.to_csv(a.output,index=False); print(out.to_string(index=False))
if __name__=='__main__': main()
