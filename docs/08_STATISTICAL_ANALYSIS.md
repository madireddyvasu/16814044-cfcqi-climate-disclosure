# Statistical analysis

## RQ1 — Descriptive Business Analytics
Overall, cycle, sector and item-level distributions of CFCQI are reported. Each item is summarised by mean score and the percentage of observations receiving 0, 1 and 2.

## RQ2 — Organisational determinants
Primary specification:

`CFCQI ~ size + assurance + board_oversight + leverage + ROA + TCFD group + cycle`

Pooled OLS is estimated with **firm-clustered robust standard errors** because each firm contributes two observations. Diagnostics include variance inflation factors, residual checks, heteroskedasticity assessment, leverage and Cook's distance. Robustness checks include atypical-period exclusions, an alternative governance classification, influential-observation checks and a latest-cycle-only HC3 model.

## RQ3 — Paired cycle change
Change is defined **Latest (T) − Prior (T1)**. The Wilcoxon signed-rank test is primary when paired differences are non-normal, with paired t-test and exact sign-test evidence used as sensitivities. Item-level latest/prior changes are also reported.
