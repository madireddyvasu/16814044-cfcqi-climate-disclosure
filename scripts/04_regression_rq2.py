#!/usr/bin/env python3
"""RQ2 pooled OLS with firm-clustered robust standard errors."""
import argparse
from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf
ROOT=Path(__file__).resolve().parents[1]
FORMULA='cfcqi ~ size + assurance + board_oversight + leverage + roa + C(tcfd_group) + C(cycle)'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',default=str(ROOT/'data/processed/cfcqi_dataset.csv')); ap.add_argument('--output',default=str(ROOT/'results/tables/regression_rq2.txt')); a=ap.parse_args()
    needed=['cfcqi','size','assurance','board_oversight','leverage','roa','tcfd_group','cycle','firm_id']; df=pd.read_csv(a.input).dropna(subset=needed)
    res=smf.ols(FORMULA,data=df).fit(cov_type='cluster',cov_kwds={'groups':df.firm_id}); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(str(res.summary())+'\n'); print(res.summary())
if __name__=='__main__': main()
