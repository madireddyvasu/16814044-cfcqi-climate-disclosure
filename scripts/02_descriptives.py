#!/usr/bin/env python3
"""RQ1 descriptive analysis and publication-ready figures."""
import argparse, sys
from pathlib import Path
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.cfcqi import ITEMS, ITEM_LABELS

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',default=str(ROOT/'data/processed/cfcqi_dataset.csv')); ap.add_argument('--outdir',default=str(ROOT/'results')); a=ap.parse_args()
    df=pd.read_csv(a.input); T=Path(a.outdir)/'tables'; F=Path(a.outdir)/'figures'; T.mkdir(parents=True,exist_ok=True); F.mkdir(parents=True,exist_ok=True)
    df['cfcqi'].agg(['count','mean','std','min','median','max']).round(2).to_csv(T/'rq1_overall.csv',header=True)
    df.groupby('cycle')['cfcqi'].agg(['count','mean','std','min','median','max']).round(2).to_csv(T/'rq1_by_cycle.csv')
    df.groupby('tcfd_group')['cfcqi'].agg(['count','mean','std','min','median','max']).round(2).to_csv(T/'rq1_by_sector.csv')
    rows=[]
    for c in ITEMS:
        s=df[c]; rows.append({'item':c,'label':ITEM_LABELS[c],'mean':round(s.mean(),2),'pct_0':round((s==0).mean()*100,1),'pct_1':round((s==1).mean()*100,1),'pct_2':round((s==2).mean()*100,1)})
    pd.DataFrame(rows).sort_values('mean').to_csv(T/'rq1_by_item.csv',index=False)
    # CFCQI distribution
    fig,ax=plt.subplots(figsize=(7,4.5)); ax.hist(df.cfcqi,bins=np.arange(0,105,10)); ax.set(xlabel='CFCQI (0–100)',ylabel='Firm-year observations',title='Distribution of CFCQI across 80 firm-years'); fig.tight_layout(); fig.savefig(F/'01_cfcqi_distribution.png',dpi=220); plt.close(fig)
    # sector means
    sec=df.groupby('tcfd_group').cfcqi.mean().sort_values(); fig,ax=plt.subplots(figsize=(8,4.8)); ax.barh(sec.index,sec.values); ax.set(xlabel='Mean CFCQI',title='Mean CFCQI by TCFD group'); fig.tight_layout(); fig.savefig(F/'02_cfcqi_by_sector.png',dpi=220); plt.close(fig)
    # paired scatter
    w=df.pivot(index='firm_id',columns='cycle',values='cfcqi'); fig,ax=plt.subplots(figsize=(5.8,5.3)); ax.scatter(w['T1'],w['T']); lo=min(w.min()); hi=max(w.max()); ax.plot([lo,hi],[lo,hi],linestyle='--'); ax.set(xlabel='Prior cycle CFCQI (T1)',ylabel='Latest cycle CFCQI (T)',title='Within-firm CFCQI: prior vs latest'); fig.tight_layout(); fig.savefig(F/'03_paired_prior_latest.png',dpi=220); plt.close(fig)
    # heatmap without seaborn
    hm=df.groupby(['tcfd_group','cycle'])[ITEMS].mean().T; fig,ax=plt.subplots(figsize=(11,6.5)); im=ax.imshow(hm.values,aspect='auto'); ax.set_yticks(range(len(ITEMS))); ax.set_yticklabels([ITEM_LABELS[i] for i in ITEMS]); ax.set_xticks(range(len(hm.columns))); ax.set_xticklabels([f'{g}\n{c}' for g,c in hm.columns],rotation=45,ha='right'); ax.set_title('Mean CFCQI item scores by sector and cycle'); fig.colorbar(im,ax=ax,label='Mean item score (0–2)'); fig.tight_layout(); fig.savefig(F/'04_item_heatmap.png',dpi=220); plt.close(fig)
    print('RQ1 outputs written.')
if __name__=='__main__': main()
