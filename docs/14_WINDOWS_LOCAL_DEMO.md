# Windows Local Run and Demonstration Guide

This guide is for running the CFCQI dissertation project locally on Windows using PowerShell.

## 1. Prerequisites

Install:
- Git for Windows
- Python 3.12
- Git LFS (only required for the full 80-PDF corpus)

Check in PowerShell:

```powershell
git --version
py --version
git lfs version
```

## 2. Clone the repository

```powershell
cd $HOME\Documents
git clone https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git
cd 16814044-cfcqi-climate-disclosure
```

## 3. Optional: obtain the annual-report corpus

The statistical analysis can be reproduced from the locked CSV datasets without downloading the PDFs.

For full corpus verification:

```powershell
git lfs install
git lfs pull
py scripts\verify_corpus.py
```

Expected full-corpus result:

```text
Expected reports: 80
Present:          80
Hash matched:     80
CORPUS_STATUS: PASS
```

If the remote Git LFS binary objects are unavailable, corpus verification may fail even though the analytical pipeline remains reproducible from the retained processed datasets.

## 4. One-command Windows analysis

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\run_all_windows.ps1
```

The script creates a local virtual environment, installs dependencies, runs tests, executes RQ1/RQ2/RQ3 analysis and robustness checks, and finishes with the final audit.

## 5. Expected headline results

- Mean CFCQI: 51.77
- Energy mean CFCQI: 62.91
- Firm size: beta 4.60, p = 0.018
- External assurance: beta 11.17, p = 0.185
- Board oversight: beta 23.76, p < 0.001
- Primary model R-squared: 0.478
- RQ3 Wilcoxon p = 0.896
- Repeat-scoring weighted Cohen's kappa = 0.631
- Final reproducibility audit: all_pass = true

## 6. Show the results in a supervisor meeting

Open the main result files:

```powershell
notepad results\tables\regression_rq2.txt
notepad results\tables\paired_rq3.txt
notepad results\tables\robustness.txt
notepad data\audit\FINAL_REPRODUCIBILITY_AUDIT.json
start results\figures\04_item_heatmap.png
start results\figures\06_regression_coefficients.png
start results\figures\03_paired_prior_latest.png
```

To inspect the main dataset:

```powershell
start data\processed\VASU_ANALYSIS_DATASET_LOCKED.csv
```

## 7. Recommended live-demo order

1. Open README and explain the research problem.
2. Show `data/processed/VASU_ANALYSIS_DATASET_LOCKED.csv` — 80 firm-years.
3. Show `evidence/` — report-level evidence behind the 960 CFCQI decisions.
4. Run `python scripts/03_reliability.py` — demonstrate reliability.
5. Run `python scripts/04_regression_rq2.py` — demonstrate determinants.
6. Run `python scripts/05_paired_rq3.py` — demonstrate reporting-cycle comparison.
7. Open the main figures.
8. Run `python scripts/07_final_audit.py` last and show `"all_pass": true`.

## 8. Important interpretation boundaries

- CFCQI measures disclosure depth, not legal compliance or climate performance.
- RQ2 coefficients are associations, not causal effects.
- RQ3 change is Latest (T) minus Prior (T1).
- External assurance is not statistically significant after controls.
- Board-level oversight is the strongest and most robust positive correlate.
