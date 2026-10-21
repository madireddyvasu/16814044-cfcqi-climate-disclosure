# Vasu Deva Rao Madireddy (16814044) — Final Technical Findings Summary

## Dataset and audit status

- Final sample: **40 firms**, with **two consecutive annual-report observations per firm** (**80 firm-years**).
- Final sector allocation: Energy 10; Transportation 9; Materials and Buildings 11; Agriculture, Food and Forest Products 10.
- Source corpus: **80 verified consolidated group annual reports**, all available by the 31 August 2026 report-eligibility cut-off and all with unique SHA-256 hashes.
- CFCQI coding: **960/960 item decisions complete** (80 reports × 12 items).
- Evidence audit: all 960 decisions are represented in the final evidence table; all non-zero scores have traceable report-page evidence after final QA corrections.
- Final merged dataset: 80 rows, 40 firms, two cycles per firm, no missing model variables, no CFCQI formula mismatches.

## CFCQI descriptive results — RQ1

Across all 80 firm-years, mean CFCQI is **51.77** (SD **18.65**), median **54.2**, range **16.7–95.8**.

Cycle-level disclosure is essentially flat:
- Latest cycle (T): mean **51.76**.
- Prior cycle (T1): mean **51.77**.

Mean CFCQI by climate-sensitive group:
- Energy: **62.91**.
- Materials and Buildings: **49.80**.
- Transportation: **48.38**.
- Agriculture, Food and Forest Products: **45.82**.

The strongest disclosure dimensions are financial-planning integration, quantified scenario analysis, and asset valuation/impairment. The weakest dimensions are quantified current financial position, current financial performance, and current cash-flow effects. This supports the substantive premise that many firms discuss climate matters but connect them less consistently to current-period financial outcomes.

## RQ2 — Firm characteristics associated with CFCQI

Primary specification: pooled OLS, 80 firm-year observations / 40 firms, with **firm-clustered robust standard errors**, sector controls and reporting-cycle control.

Model fit:
- R² = **0.478**.
- Adjusted R² = **0.410**.

Main hypotheses:

### H1 — Firm size
- β = **4.60**.
- 95% CI approximately **[0.78, 8.42]**.
- p = **0.0183**.
- **Supported in the primary pooled model.**

However, in a latest-cycle-only cross-sectional HC3 model, the coefficient remains positive but p rises to approximately **0.0765**. H1 should therefore be described as supported in the main specification but somewhat sensitive to the reduced-sample cross-sectional specification.

### H2 — External sustainability assurance
- β = **11.17**.
- p = **0.1853**.
- **Not supported.**

The estimated association is positive but statistically imprecise in this sample.

### H3 — Board-level sustainability/climate oversight
- β = **23.76**.
- 95% CI approximately **[13.48, 34.05]**.
- p ≈ **5.9×10⁻⁶**.
- **Strongly supported.**

This is the strongest and most stable result. The positive association survives period-length exclusions, a conservative governance recode, influential-observation checks and the latest-cycle-only model.

Selected controls:
- ROA is positively associated with CFCQI in the primary model (p ≈ **0.042**).
- Energy is higher than the Agriculture/Food/Forest reference group in the primary model (p ≈ **0.040**).
- Leverage is not statistically significant.
- The reporting-cycle indicator is not statistically significant.

All RQ2 interpretations are **associational, not causal**.

## RQ2 diagnostics and robustness

- Maximum VIF ≈ **1.93**: no material multicollinearity concern.
- Breusch–Pagan p ≈ **0.044**: mild heteroskedasticity; firm-clustered robust standard errors are therefore retained.
- Residual Shapiro p ≈ **0.292**: no strong evidence of non-normal model residuals.
- Six firm-year observations exceed the Cook's D > 4/n screening threshold.

Sensitivity checks do not overturn the central conclusions:
- Excluding Mobico: H1 supported; H2 not supported; H3 strongly supported.
- Excluding Tesco: same substantive conclusion.
- Excluding Mobico and Tesco: same substantive conclusion.
- Conservative F009 board-oversight recode: H1 remains significant at 5%; H2 remains non-significant; H3 remains significant.
- Latest-cycle-only HC3: H3 remains strongly significant; H2 remains non-significant; H1 becomes marginal (p≈0.077).

## RQ3 — Within-firm change across reporting cycles

The final implementation defines change correctly as:

**Latest CFCQI (T) − Prior CFCQI (T1).**

Paired differences are non-normal (Shapiro p < 0.001), so the primary test is the Wilcoxon signed-rank test.

- Number of paired firms: **40**.
- Mean change: approximately **−0.003 CFCQI points**.
- Median change: **0**.
- Improved firms: **12**.
- Unchanged firms: **20**.
- Deteriorated firms: **8**.
- Wilcoxon W = **101.5**, p = **0.8959**.
- Exact sign test excluding ties: p ≈ **0.5034**.
- Paired t-test sensitivity: p ≈ **0.9988**.

**Conclusion:** there is no evidence of a systematic within-firm change in CFCQI between the two consecutive reporting cycles.

The null conclusion remains unchanged when excluding Mobico, Tesco, or both.

## Reliability

A 15% repeat-scoring reliability audit covered **12 reports / 144 item decisions**.

- Exact agreement: **66.7%**.
- Pooled weighted Cohen's κ: **0.631**.
- The reported overall κ exceeds 0.60, while item-level reliability remains uneven and is treated as a limitation.

However, reliability is not uniformly strong across all 12 items. Item-level weighted κ values vary substantially, including weak or negative values for some current-period financial-effect items. The mean item-level κ is approximately **0.306** and median approximately **0.36**. Total-score agreement is moderate rather than excellent (Pearson r ≈ **0.502**, Spearman r ≈ **0.477**; mean absolute CFCQI difference ≈ **10.76** points).

This should be reported as a methodological limitation rather than hidden. The pooled index shows acceptable overall repeatability, while several individual coding boundaries remain judgement-sensitive.

## Special cases retained in the final analysis

- **Mobico:** latest report covers approximately 15 months. The main data use reported figures without annualisation; RQ2/RQ3 sensitivity analyses exclude Mobico and do not change the central conclusions.
- **Tesco:** latest report covers 53 weeks. Results remain stable when Tesco is excluded.
- **Mondi:** integrated-report title is accepted because the document is the complete statutory annual/integrated report with audited financial statements.
- **Spirax Group:** corporate rename documented; group continuity retained.
- **Smiths Group:** FY2025 and FY2024 are the two most recent consecutive annual reports available at the sample freeze.

## Final technical conclusion

The technical implementation supports three defensible conclusions:

1. Quantified and financially connected climate disclosure is **moderate and highly heterogeneous**, with considerably stronger disclosure in planning/scenario/valuation dimensions than in current-period financial effects.
2. **Board-level sustainability/climate oversight is the strongest and most robust firm-level correlate of CFCQI.** Firm size is positively associated in the main model but is somewhat more specification-sensitive. External sustainability assurance is not statistically supported as an independent correlate in this sample.
3. Despite the reporting transition context, there is **no detectable systematic within-firm improvement** in CFCQI across the two consecutive cycles studied.

CFCQI remains a **research instrument**, not a UK SRS S2/IFRS S2 compliance score.
