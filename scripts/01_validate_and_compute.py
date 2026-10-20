#!/usr/bin/env python3
"""Validate the locked coding input and recompute CFCQI deterministically."""
import argparse, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.cfcqi import validate_coding, compute_cfcqi

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', default=str(ROOT/'data/input/coding_locked.csv'))
    ap.add_argument('--output', default=str(ROOT/'data/processed/cfcqi_dataset.csv'))
    a=ap.parse_args()
    df=pd.read_csv(a.input)
    errors=validate_coding(df)
    if errors:
        print('VALIDATION ERRORS:')
        for e in errors: print(' -',e)
        raise SystemExit(1)
    out=compute_cfcqi(df)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    out.to_csv(a.output,index=False)
    print(f'Validated {len(out)} firm-years; wrote {a.output}')
    print(out[['raw_score','cfcqi']].describe().round(2).to_string())
if __name__=='__main__': main()
