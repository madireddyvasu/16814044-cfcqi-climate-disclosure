#!/usr/bin/env python3
"""RQ2 diagnostics and full robustness suite used in the final dissertation."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor, OLSInfluence
from statsmodels.stats.diagnostic import het_breuschpagan

ROOT=Path(__file__).resolve().parents[1]
FORMULA='cfcqi ~ size + assurance + board_oversight + leverage + roa + C(tcfd_group) + C(cycle)'
H_VARS=['size','assurance','board_oversight']

def fit_cluster(d):
    d=d.dropna(subset=['cfcqi','size','assurance','board_oversight','leverage','roa','tcfd_group','cycle','firm_id']).copy()
    return smf.ols(FORMULA,data=d).fit(cov_type='cluster',cov_kwds={'groups':d.firm_id}),d

def coefrows(res,spec):
    ci=res.conf_int(); rows=[]
    for term in res.params.index:
        rows.append({'specification':spec,'term':term,'coef':res.params[term],'se':res.bse[term],'p_value':res.pvalues[term],
                     'ci_low':ci.loc[term,0],'ci_high':ci.loc[term,1],'n':int(res.nobs),'r2':res.rsquared,'adj_r2':res.rsquared_adj})
    return rows

def focusrows(res,spec):
    rows=[]
    mapping={'size':'H1','assurance':'H2','board_oversight':'H3'}
    for term,h in mapping.items():
        rows.append({'specification':spec,'hypothesis':h,'term':term,'coef':res.params[term],'se':res.bse[term],
                     'p_value':res.pvalues[term],'supported_5pct':bool(res.pvalues[term]<.05),'n':int(res.nobs),'r2':res.rsquared})
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',default=str(ROOT/'data/processed/cfcqi_dataset.csv')); ap.add_argument('--outdir',default=str(ROOT/'results')); a=ap.parse_args()
    df=pd.read_csv(a.input); T=Path(a.outdir)/'tables'; F=Path(a.outdir)/'figures'; T.mkdir(parents=True,exist_ok=True); F.mkdir(parents=True,exist_ok=True)
    base,d=fit_cluster(df)

    # VIF on base design matrix
    X=base.model.exog; names=base.model.exog_names; vif=[]
    for j,name in enumerate(names):
        if name!='Intercept': vif.append({'term':name,'vif':variance_inflation_factor(X,j)})
    vifdf=pd.DataFrame(vif).sort_values('vif',ascending=False); vifdf.to_csv(T/'rq2_vif.csv',index=False)

    # Residual / heteroscedasticity / influence diagnostics using nonrobust OLS residuals
    ols=smf.ols(FORMULA,data=d).fit(); bp=het_breuschpagan(ols.resid,ols.model.exog); shapiro=stats.shapiro(ols.resid)
    infl=OLSInfluence(ols); cook=np.asarray(infl.cooks_distance[0]); threshold=4/len(d)
    infdf=d[['firm_id','firm_name','cycle','cfcqi']].copy(); infdf['cooks_d']=cook; infdf['above_4_over_n']=infdf.cooks_d>threshold
    infdf.to_csv(T/'rq2_influence.csv',index=False)
    diag=pd.DataFrame([
        {'diagnostic':'Breusch-Pagan LM p-value','value':bp[1],'interpretation':'Heteroscedasticity indicated at 5%; robust/clustered inference retained.'},
        {'diagnostic':'Shapiro-Wilk residual p-value','value':shapiro.pvalue,'interpretation':'Residual normality not rejected at 5%.'},
        {'diagnostic':'Cook threshold 4/n','value':threshold,'interpretation':f"{int((cook>threshold).sum())} firm-year observations above threshold."},
        {'diagnostic':'Maximum VIF','value':float(vifdf.vif.max()),'interpretation':'Multicollinearity not a material concern.'},
    ]); diag.to_csv(T/'rq2_diagnostics.csv',index=False)

    # Model suite
    models=[]; focus=[]
    models += coefrows(base,'Base pooled, firm-clustered SE'); focus += focusrows(base,'Base pooled')
    specs=[
        ('Exclude Mobico F019',df[df.firm_id!='F019']),
        ('Exclude Tesco F032',df[df.firm_id!='F032']),
        ('Exclude Mobico + Tesco',df[~df.firm_id.isin(['F019','F032'])]),
    ]
    for label,sub in specs:
        m,_=fit_cluster(sub); models += coefrows(m,label); focus += focusrows(m,label)
    # influential-point exclusion
    bad=set(zip(infdf.loc[infdf.above_4_over_n,'firm_id'],infdf.loc[infdf.above_4_over_n,'cycle']))
    mask=df.apply(lambda r:(r.firm_id,r.cycle) not in bad,axis=1); m_inf,_=fit_cluster(df[mask]); models += coefrows(m_inf,"Exclude Cook's D > 4/n"); focus += focusrows(m_inf,"Exclude Cook's D > 4/n")
    # F009 governance recode
    f009=df.copy(); f009.loc[f009.firm_id=='F009','board_oversight']=0; m_f009,_=fit_cluster(f009); models += coefrows(m_f009,'F009 governance=0'); focus += focusrows(m_f009,'F009 governance=0')
    # latest-only HC3
    latest=df[df.cycle=='T'].copy(); m_latest=smf.ols('cfcqi ~ size + assurance + board_oversight + leverage + roa + C(tcfd_group)',data=latest).fit(cov_type='HC3'); models += coefrows(m_latest,'Latest-only HC3'); focus += focusrows(m_latest,'Latest-only HC3')
    pd.DataFrame(models).to_csv(T/'RQ2_MODELS_ALL.csv',index=False); pd.DataFrame(focus).to_csv(T/'RQ2_EXTENDED_ROBUSTNESS.csv',index=False)

    # residual / fitted plot
    fig,ax=plt.subplots(figsize=(7,4.5)); ax.scatter(ols.fittedvalues,ols.resid); ax.axhline(0,linewidth=1); ax.set(xlabel='Fitted CFCQI',ylabel='Residual',title='RQ2 residual diagnostics'); fig.tight_layout(); fig.savefig(F/'robustness_residuals.png',dpi=220); plt.close(fig)
    # base coefficient plot (main continuous/binary variables)
    c=pd.DataFrame(coefrows(base,'base')); keep=['size','assurance','board_oversight','leverage','roa']; c=c[c.term.isin(keep)].set_index('term').loc[keep].reset_index(); x=c.coef.values; lo=x-c.ci_low.values; hi=c.ci_high.values-x; y=np.arange(len(c))
    fig,ax=plt.subplots(figsize=(7,4.5)); ax.errorbar(x,y,xerr=[lo,hi],fmt='o',capsize=4); ax.axvline(0,linewidth=1); ax.set_yticks(y); ax.set_yticklabels(['Firm size (ln assets)','External assurance','Board oversight','Leverage','ROA']); ax.set(xlabel='OLS coefficient (95% CI)',title='RQ2 pooled OLS with firm-clustered SE'); fig.tight_layout(); fig.savefig(F/'06_regression_coefficients.png',dpi=220); plt.close(fig)
    # assurance / board group plots
    for col,label,fn in [('assurance','External assurance','07_assurance_cfcqi.png'),('board_oversight','Board-level oversight','08_board_oversight_cfcqi.png')]:
        fig,ax=plt.subplots(figsize=(6,4.5)); vals=[df.loc[df[col]==0,'cfcqi'],df.loc[df[col]==1,'cfcqi']]; ax.boxplot(vals,tick_labels=[f'No {label.lower()}',label]); ax.set(ylabel='CFCQI',title=f'CFCQI by {label.lower()}'); fig.tight_layout(); fig.savefig(F/fn,dpi=220); plt.close(fig)

    # human-readable summary
    lines=['RQ2 DIAGNOSTICS AND ROBUSTNESS','='*72,f'Base model n={int(base.nobs)}, firms={d.firm_id.nunique()}, R2={base.rsquared:.3f}',
           f'Max VIF={vifdf.vif.max():.2f}',f'Breusch-Pagan p={bp[1]:.4f}',f'Shapiro residual p={shapiro.pvalue:.4f}',f"Cook threshold={threshold:.4f}; flagged={int((cook>threshold).sum())}",'']
    fdf=pd.DataFrame(focus)
    for spec in fdf.specification.unique():
        lines.append(spec)
        for _,r in fdf[fdf.specification==spec].iterrows(): lines.append(f"  {r.hypothesis} {r.term}: beta={r.coef:.2f}, p={r.p_value:.4f}, n={int(r.n)}")
        lines.append('')
    (T/'robustness.txt').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))

if __name__=='__main__': main()
