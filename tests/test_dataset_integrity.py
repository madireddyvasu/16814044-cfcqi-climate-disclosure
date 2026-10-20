from pathlib import Path
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def test_locked_dataset_integrity():
    d=pd.read_csv(ROOT/'data/processed/VASU_ANALYSIS_DATASET_LOCKED.csv'); items=[f'item{i}' for i in range(1,13)]
    assert len(d)==80 and d.firm_id.nunique()==40
    assert set(d.cycle)=={'T','T1'} and (d.groupby('firm_id').cycle.nunique()==2).all()
    assert d[items].isin([0,1,2]).all().all()
    assert (d[items].sum(axis=1)==d.raw_score).all()
    assert np.allclose((d.raw_score/24*100).round(1),d.cfcqi)

def test_source_register_and_evidence():
    reg=pd.read_csv(ROOT/'data/source_register/Vasu_Master_Annual_Report_Register.csv')
    ev=pd.read_csv(ROOT/'data/audit/CFCQI_EVIDENCE_AUDIT.csv')
    assert len(reg)==80 and reg.SHA256.nunique()==80
    assert len(ev)==960
