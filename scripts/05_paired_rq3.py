#!/usr/bin/env python3
"""05 — RQ3: within-firm change across cycles (paired t-test or Wilcoxon)."""
import argparse, sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.cfcqi import ITEMS, ITEM_LABELS

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=str(ROOT/'data/processed/cfcqi_dataset.csv'))
    ap.add_argument("--output", default=str(ROOT/'results/tables/paired_rq3.txt'))
    ap.add_argument("--item-output", default=str(ROOT/'results/tables/rq3_item_changes.csv'))
    ap.add_argument("--sensitivity-output", default=str(ROOT/'results/tables/rq3_sensitivity.csv'))
    args = ap.parse_args()
    df = pd.read_csv(args.input)
    if set(df["cycle"].unique()) != {"T", "T1"}:
        sys.exit(f"Expected cycles T and T1, found: {sorted(df['cycle'].unique())}")
    # T = latest; T1 = prior. Define change unambiguously as Latest - Prior.
    w = df.pivot(index="firm_id", columns="cycle", values="cfcqi")
    d = (w["T"] - w["T1"]).dropna()
    shapiro_p = stats.shapiro(d).pvalue if len(d) >= 3 else np.nan
    if len(d) >= 3 and shapiro_p >= 0.05:
        stat, pval = stats.ttest_rel(w.loc[d.index,"T"], w.loc[d.index,"T1"], nan_policy="omit")
        test_name="paired_t"
    else:
        stat, pval = stats.wilcoxon(w.loc[d.index,"T"], w.loc[d.index,"T1"], nan_policy="omit")
        test_name="wilcoxon"
    sd=d.std(ddof=1)
    dz=d.mean()/sd if sd else np.nan
    pos=int((d>0).sum()); neg=int((d<0).sum()); zero=int((d==0).sum())
    sign_p=stats.binomtest(pos,n=pos+neg,p=0.5).pvalue if pos+neg else np.nan

    item_rows=[]
    for c in ITEMS:
        iw=df.pivot(index="firm_id",columns="cycle",values=c)
        dd=iw["T"]-iw["T1"]
        item_rows.append({
            "item":c,"label":ITEM_LABELS[c],"mean_latest":iw["T"].mean(),"mean_prior":iw["T1"].mean(),
            "mean_change_latest_minus_prior":dd.mean(),"pct_improved":100*(dd>0).mean(),
            "pct_unchanged":100*(dd==0).mean(),"pct_deteriorated":100*(dd<0).mean()
        })
    item_change=pd.DataFrame(item_rows)
    Path(args.item_output).parent.mkdir(parents=True,exist_ok=True)
    item_change.to_csv(args.item_output,index=False)

    sens=[]
    for label,excl in [("Full sample",[]),("Exclude Mobico F019",["F019"]),("Exclude Tesco F032",["F032"]),("Exclude Mobico + Tesco",["F019","F032"])]:
        ww=w.drop(index=excl,errors="ignore"); dd=ww["T"]-ww["T1"]
        wil=stats.wilcoxon(ww["T"],ww["T1"])
        tt=stats.ttest_rel(ww["T"],ww["T1"])
        sens.append({"specification":label,"n_pairs":len(dd),"mean_change":dd.mean(),"median_change":dd.median(),"wilcoxon_W":wil.statistic,"wilcoxon_p":wil.pvalue,"paired_t":tt.statistic,"paired_t_p":tt.pvalue})
    pd.DataFrame(sens).to_csv(args.sensitivity_output,index=False)

    # Item-level latest-minus-prior change figure
    figdir=ROOT/'results/figures'; figdir.mkdir(parents=True,exist_ok=True)
    plot_df=item_change.sort_values('mean_change_latest_minus_prior')
    fig,ax=plt.subplots(figsize=(8,6)); ax.barh(plot_df['label'],plot_df['mean_change_latest_minus_prior']); ax.axvline(0,linewidth=1); ax.set_xlabel('Mean change (Latest − Prior)'); ax.set_title('Item-level change between reporting cycles'); fig.tight_layout(); fig.savefig(figdir/'05_item_change.png',dpi=220); plt.close(fig)

    lines=[
        f"Cycles compared: Prior (T1) -> Latest (T) (n firms = {len(d)})",
        f"Mean change (Latest - Prior) in CFCQI: {d.mean():.3f} (SD = {d.std(ddof=1):.2f}; median = {d.median():.2f})",
        f"Improved / unchanged / deteriorated firms: {pos} / {zero} / {neg}",
        f"Cohen's dz = {dz:.3f}",
        f"Shapiro p={shapiro_p:.4f}; primary test={test_name}: statistic={stat:.3f}, p={pval:.4f}",
        f"Exact sign test excluding ties: p={sign_p:.4f}",
        "",
        "Item-level change (positive = improvement in latest cycle):",
        item_change.round(2).to_string(index=False),
    ]
    Path(args.output).write_text("\n".join(lines)+"\n")
    print("\n".join(lines))
    print(f"\nSaved -> {args.output}, {args.item_output}, {args.sensitivity_output}")

if __name__ == "__main__":
    main()
