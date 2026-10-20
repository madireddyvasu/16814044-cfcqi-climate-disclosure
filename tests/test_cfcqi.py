import pandas as pd
from src.cfcqi import compute_cfcqi,validate_coding
def test_compute_cfcqi():
    d=pd.DataFrame({**{f'item{i}':[2,0] for i in range(1,13)},'firm_id':['A','B']})
    assert validate_coding(d)==[]
    out=compute_cfcqi(d)
    assert out.raw_score.tolist()==[24,0]
    assert out.cfcqi.tolist()==[100.0,0.0]
