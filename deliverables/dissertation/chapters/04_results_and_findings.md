# Chapter 4: Results and Findings

## 4.1 Chapter Introduction

This chapter reports results from the locked dataset: data quality and reliability, CFCQI patterns, determinant regression, diagnostics/robustness and paired change. Literature-based interpretation is reserved for Chapter 5.

## 4.2 Data Quality and Reliability

The final dataset contains 80 firm-years from 40 firms: 10 Energy, 9 Transportation, 11 Materials and Buildings, and 10 Agriculture, Food and Forest Products firms, with two cycles per firm and no missing CFCQI items or model variables. All 960 item decisions were valid, raw scores reconciled to item totals and CFCQI formulas, and all 80 source reports had unique hashes.

The blind 12-report second-pass scoring check produced 66.7% exact agreement and pooled weighted Cohen’s κ = 0.631, above the pre-specified 0.60 threshold. Item-level κ ranged from −0.286 (current financial performance) to 0.757 (asset valuation/impairment), with several other weak items. Appendix C reports the full table. Aggregate reliability is acceptable, but individual boundary judgements require caution.

## 4.3 CFCQI Descriptive Results

Across all 80 observations, mean CFCQI was 51.77 (SD = 18.65), with a median of 54.2 and a range from 16.7 to 95.8. Latest-cycle and prior-cycle means were almost identical (51.76 and 51.77 respectively). Energy recorded the highest group mean (62.91), followed by Materials and Buildings (49.80), Transportation (48.38) and Agriculture, Food and Forest Products (45.82). Figure 4.2 shows that these sector differences are much larger than the aggregate latest–prior movement.

| **Group** | **n** | **Mean** | **SD** | **Median** | **Range** |
|---|---:|---:|---:|---:|---:|
| Overall | 80 | 51.77 | 18.65 | 54.2 | 16.7–95.8 |
| Latest cycle (T) | 40 | 51.76 | 18.02 | 58.3 | 16.7–91.7 |
| Prior cycle (T1) | 40 | 51.77 | 19.49 | 54.2 | 16.7–95.8 |
| Energy | 20 | 62.91 | 20.23 | 68.75 | 16.7–91.7 |
| Materials & Buildings | 22 | 49.80 | 17.27 | 52.1 | 25.0–95.8 |
| Transportation | 18 | 48.38 | 14.60 | 52.1 | 20.8–66.7 |
| Agriculture/Food/Forest | 20 | 45.82 | 18.27 | 50.0 | 16.7–70.8 |

The item profile reveals a sharper distinction than the total score alone. Financial-planning integration (I11) had the highest mean (1.81), with 83.8% of observations scoring 2. Quantified scenario analysis (I12) averaged 1.60 and asset valuation/impairment (I8) 1.50. In contrast, current financial position (I2) averaged 0.34, current financial performance (I1) 0.44 and current cash flows (I3) 0.51; 77.5%, 68.8% and 72.5% of observations respectively scored zero.

## 4.4 Determinants of CFCQI

The pooled ordinary least squares (OLS) model explained 47.8% of CFCQI variation (adjusted R² = 0.410; n = 80; 40 firm clusters). For firm size, the null hypothesis of no statistically significant association (H01) was rejected in the primary specification and the positive alternative (H11) was supported: β = 4.60, 95% CI [0.78, 8.42], p = .018. For external assurance, H02 was not rejected and H12 was not supported because the coefficient was positive but imprecise (β = 11.17, 95% CI [−5.36, 27.70], p = .185). For board-level oversight, H03 was rejected and H13 was strongly supported: qualifying board oversight was associated with 23.76 additional CFCQI points (95% CI [13.48, 34.05], p < .001).

Among controls, ROA was positive and significant (β = 49.57, p = .042); because ROA is a proportion, a 0.10 increase corresponds to about 4.96 CFCQI points. Energy firms scored 11.86 points above the Agriculture/Food/Forest baseline (p = .040). Materials/Buildings, Transportation, leverage and cycle were non-significant.

| **Predictor** | **β** | **Robust SE** | **p** | **95% CI** |
|---|---:|---:|---:|---:|
| Energy group | 11.86 | 5.78 | 0.040 | [0.53, 23.19] |
| Materials & Buildings | 1.16 | 5.91 | 0.844 | [-10.42, 12.75] |
| Transportation | 6.07 | 6.76 | 0.369 | [-7.17, 19.31] |
| Prior cycle (T1) | 0.67 | 1.93 | 0.730 | [-3.12, 4.45] |
| Firm size | 4.60 | 1.95 | 0.018 | [0.78, 8.42] |
| External assurance | 11.17 | 8.43 | 0.185 | [-5.36, 27.70] |
| Board oversight | 23.76 | 5.25 | 0.000 | [13.48, 34.05] |
| Leverage | 8.47 | 15.77 | 0.591 | [-22.45, 39.38] |
| ROA | 49.57 | 24.33 | 0.042 | [1.88, 97.27] |

Notes: n = 80 firm-years; 40 firm clusters; R² = 0.478; adjusted R² = 0.410. Reference sector: Agriculture/Food/Forest. Source: author’s Python analysis.

## 4.5 Regression Diagnostics and Robustness

Multicollinearity was not problematic: the maximum VIF was 1.93. The Breusch–Pagan test indicated mild heteroscedasticity (p = .044), supporting the use of robust/clustered inference, while residual normality was not rejected (Shapiro p = .292). Six firm-years exceeded the Cook’s-distance threshold of 4/n: BP in both cycles, Ithaca Energy in the latest cycle, easyJet in the prior cycle, Rio Tinto in the prior cycle and Diageo in the prior cycle. Excluding those observations strengthened H1, left H2 non-significant and left H3 strongly significant.

Sensitivity tests addressed period and classification concerns. Excluding Mobico, Tesco, or both did not change the substantive conclusions. Reclassifying Drax Group’s borderline board-oversight indicator from 1 to 0 reduced H3 to 20.34 points but it remained significant (p < .001). In the latest-cycle-only HC3 model, H1 remained positive but weakened to p = .076, H2 remained non-significant (p = .751), and H3 remained positive and significant (β = 25.34, p = .002). H1 is therefore supported but sample-size-sensitive; H3 is the most stable result.

| **Specification** | **n** | **H1 size β (p)** | **H2 assurance β (p)** | **H3 board β (p)** |
|---|---:|---:|---:|---:|
| Base pooled | 80 | 4.60 (0.018) | 11.17 (0.185) | 23.76 (0.000) |
| Exclude Mobico | 78 | 4.56 (0.023) | 11.09 (0.191) | 23.95 (0.000) |
| Exclude Tesco | 78 | 4.82 (0.017) | 11.28 (0.185) | 24.32 (0.000) |
| Exclude Mobico + Tesco | 76 | 4.79 (0.021) | 11.18 (0.191) | 24.51 (0.000) |
| Drax oversight recoded 1→0 | 80 | 4.13 (0.042) | 11.69 (0.172) | 20.34 (0.000) |
| Latest cycle only (HC3) | 40 | 4.61 (0.076) | 3.65 (0.751) | 25.34 (0.002) |

## 4.6 Paired Reporting-Cycle Results

Paired differences were non-normal (Shapiro p < .001), so the Wilcoxon signed-rank test was the primary inferential procedure. Defining change as Latest (T) − Prior (T1), mean change was −0.003 CFCQI points and the median was 0. The Wilcoxon statistic was W = 101.5 (p = .896), providing no evidence of systematic change. Twelve firms improved, 20 were unchanged and eight declined. Complementary tests reached the same conclusion: paired t = −0.002 (p = .999) and the exact sign test excluding ties gave p = .503.

The null result was robust to excluding Mobico’s 15-month latest period, Tesco’s 53-week period, or both. Item-level movement was also small. Current performance, current position and current cash flows each increased by 0.075 points on average, and capital expenditure/allocation increased by 0.075. By contrast, asset valuation/impairment declined by 0.10 and anticipated financial performance by 0.075. Most item scores were unchanged for 80–97.5% of firms. The largest remaining gaps therefore remained the current financial-effects items rather than scenario or planning disclosure.

## 4.7 Chapter Summary

The results show moderate but highly uneven financial connectivity. Planning, scenario and impairment disclosure are comparatively developed, whereas current financial effects remain weak. Firm size is positively associated with CFCQI in the pooled model but becomes weaker in the latest-only specification; assurance is not independently significant; board oversight is large and robust. There is no systematic aggregate improvement across the two reporting cycles. Chapter 5 interprets these findings against the literature, UK SRS/IFRS S2 expectations and the TBL-based conceptual framework.
