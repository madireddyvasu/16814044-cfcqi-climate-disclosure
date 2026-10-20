# Technical Implementation Report

## Quantified and Financially Connected Climate Disclosure in Climate-Sensitive FTSE 350 Firms

*Determinants and Reporting Gaps Ahead of UK SRS S2*

| Field | Final record |
|---|---|
| Student | Vasu Deva Rao Madireddy |
| Student ID | 16814044 |
| Programme | MSc Business Analytics, Coventry University |
| Project route | Route 1 – Research Dissertation |
| Technical stack | Excel + Python; Power BI-ready data |
| Corpus | 40 firms × 2 cycles = 80 verified annual reports |
| Final dataset | 80 firm-year observations; 960 CFCQI decisions |

> This is the technical research record, not the dissertation. CFCQI is a researcher-developed disclosure-depth index, not a regulatory-compliance percentage. RQ2 results are associational, not causal.

# 1. Executive Summary

The technical implementation is complete and reproducible. The final corpus contains 80 verified consolidated-group annual reports from 40 climate-sensitive FTSE 350 firms, with two consecutive reporting cycles per firm. Every report has a unique SHA-256 hash. Report eligibility ended on 31 August 2026; the final supervisor-reviewed sampling frame was frozen on 7 October 2026 using FTSE 350 membership and market-capitalisation ranking. That timing distinction is retained explicitly in the audit trail.

All 80 firm-years were scored using the frozen 12-item CFCQI instrument, producing 960 item-level decisions. Mean CFCQI is 51.77 (SD 18.65). The pooled weighted Cohen’s kappa from the 15% blind repeat-scoring exercise is 0.631; overall scoring stability therefore clears the pre-specified 0.60 threshold, although item-level reliability is uneven and remains a stated limitation.

The pooled RQ2 model explains 47.8% of CFCQI variation. Firm size is positively associated with CFCQI in the primary pooled model (p = 0.018), external assurance is not statistically significant (p = 0.185), and qualifying board-level sustainability/climate oversight has the largest positive association (approximately +23.8 CFCQI points, p < 0.001). The board-oversight result remains strong under all sensitivity checks. The size result remains positive but weakens to p ≈ 0.077 in the latest-cycle-only HC3 model.

For RQ3, change is Latest (T) minus Prior (T1). Mean change is effectively zero, the median is zero, and the Wilcoxon signed-rank test is non-significant (p = 0.896). Excluding Mobico, Tesco, or both does not alter that conclusion.

See [CFCQI distribution](../../results/figures/01_cfcqi_distribution.png).

# 2. Research Design and Analytical Architecture

The project uses secondary quantitative research with structured quantitative content analysis of corporate annual reports. The unit of analysis is the firm-report-year. The workflow combines an auditable evidence layer with Python-based validation/statistical analysis.

- 40 sampled non-financial FTSE 350 firms mapped to four TCFD climate-sensitive groups.
- Two consecutive annual reports per firm (T = latest; T1 = prior).
- Twelve CFCQI items scored 0, 1 or 2 under a frozen codebook.
- Main explanatory variables: size, external sustainability assurance and board-level sustainability/climate oversight.
- Controls: leverage, ROA, TCFD group and reporting cycle.
- RQ1: descriptive level/pattern analysis.
- RQ2: pooled OLS with firm-clustered robust standard errors.
- RQ3: paired within-firm analysis.

# 3. Final Sample and Corpus

The implemented sample is the documented market-cap-ranked frozen sample, not the earlier illustrative company list. Transportation contained nine defensibly mapped eligible firms, so one slot was reallocated to Materials and Buildings, producing a 10/9/11/10 distribution.

| TCFD group | Firms | Sample |
|---|---:|---|
| Agriculture Food and Forest Products | 10 | Diageo, Tesco, Coca-Cola HBC, Associated British Foods, Marks & Spencer, J Sainsbury, Mondi, Cranswick, Tate & Lyle, Ocado |
| Energy | 10 | Shell, BP, SSE, Centrica, DCC, Ithaca Energy, Harbour Energy, Drax Group, National Grid, Energean |
| Materials and Buildings | 11 | Rio Tinto, Glencore, Anglo American, Antofagasta, Fresnillo, Endeavour Mining, Diploma, Smiths Group, Weir Group, Spirax-Sarco Engineering, IMI |
| Transportation | 9 | IAG, easyJet, Inchcape, Clarkson, Wizz Air, Zigup, FirstGroup, Aston Martin Lagonda, Mobico Group |

Source-corpus validation confirmed 80/80 verified reports and 80/80 unique SHA-256 hashes. Four invalid first-pass files were rejected/replaced during corpus construction: one wrong-year duplicate, two partial M&S files and one truncated Sainsbury’s report.

# 4. CFCQI Instrument and Coding Rules

CFCQI contains 12 dimensions derived from climate-related financial-effects concepts. The common scale is:

- **0** = no qualifying financial connection after full-report review.
- **1** = qualitative or specific but unquantified financial connection.
- **2** = quantified effect or strongly specific financial-statement/planning connection.

| Item | Construct |
|---|---|
| 1 | Current financial performance |
| 2 | Current financial position |
| 3 | Current cash flows |
| 4 | Anticipated financial performance |
| 5 | Anticipated financial position |
| 6 | Anticipated cash flows |
| 7 | Capital expenditure / allocation |
| 8 | Asset valuations & impairment |
| 9 | Provisions / contingencies |
| 10 | Carbon pricing / regulatory costs |
| 11 | Financial planning integration |
| 12 | Quantified scenario analysis |

CFCQI = (sum of 12 item scores / 24) × 100.

# 5. Evidence Audit and Quality-Control Corrections

The retained 80 evidence notes are the primary human-auditable evidence layer. `scripts/08_build_evidence_audit.py` rebuilds the detailed 960-row CSV from those notes, the verified source register and the locked dataset. It checks that each evidence score matches the locked score and that every non-zero score has a page reference.

Three final QA corrections were documented without changing the substantive analysis:

- Mobico F019-T1 item 6: valid qualitative future cash-flow rationale existed; missing page reference was corrected.
- Weir Group F029 T/T1: stale summary lines were corrected to match their valid 12-item totals already present in the locked dataset.
- RQ3 direction: the script was corrected to Latest − Prior. The Wilcoxon p-value was unchanged, but item-change signs were corrected.

# 6. Firm-Level Variables

| Variable | Operationalisation | Implementation note |
|---|---|---|
| Size | ln(total assets in GBP millions) | Non-GBP reporters converted using documented reference rates |
| External assurance | 0/1 | 1 where independent assurance covers sustainability/environmental subject matter; statutory audit alone does not qualify |
| Board oversight | 0/1 | 1 for a named board committee with explicit sustainability/climate/environment remit |
| Leverage | Interest-bearing debt / total assets | Documented extraction rules applied consistently |
| ROA | Net income / total assets | Negative values permitted for loss-making observations |

All 80 rows have complete model variables.

# 7. Data Validation

| Check | Observed | Expected | Status |
|---|---:|---:|---|
| Rows in locked dataset | 80 | 80 | PASS |
| Unique firms | 40 | 40 | PASS |
| T observations | 40 | 40 | PASS |
| T1 observations | 40 | 40 | PASS |
| Duplicate firm-cycle rows | 0 | 0 | PASS |
| Missing CFCQI item values | 0 | 0 | PASS |
| Invalid CFCQI item values | 0 | 0 | PASS |
| Raw-score formula mismatches | 0 | 0 | PASS |
| CFCQI formula mismatches | 0 | 0 | PASS |
| Missing model variables | 0 | 0 | PASS |
| Evidence decisions | 960 | 960 | PASS |
| Non-zero evidence without page | 0 | 0 | PASS |
| Unique report hashes | 80 | 80 | PASS |
| Included verified reports | 80 | 80 | PASS |

# 8. Reliability Assessment

Twelve reports (15% of the corpus) were blindly re-scored. Across 144 item comparisons, exact agreement was 66.7% and pooled weighted Cohen’s κ = 0.631. Item-level agreement is heterogeneous, so pooled reliability is not used to conceal weak individual items.

| Item | Exact agreement | Weighted κ |
|---|---:|---:|
| I1 | 50.0% | -0.286 |
| I2 | 75.0% | -0.091 |
| I3 | 91.7% | 0.625 |
| I4 | 75.0% | 0.438 |
| I5 | 41.7% | 0.200 |
| I6 | 66.7% | 0.351 |
| I7 | 83.3% | 0.556 |
| I8 | 75.0% | 0.757 |
| I9 | 58.3% | 0.368 |
| I10 | 58.3% | 0.500 |
| I11 | 75.0% | 0.250 |
| I12 | 50.0% | 0.000 |
| **Pooled** | **66.7%** | **0.631** |

See [RELIABILITY_EXTENDED.csv](../../results/tables/RELIABILITY_EXTENDED.csv).

# 9. RQ1 – Level and Pattern of Disclosure

Across 80 firm-years, mean CFCQI is 51.77, median 54.20, SD 18.65 and range 16.7–95.8. Latest and prior means are virtually identical.

| TCFD group | n | Mean | Median | SD |
|---|---:|---:|---:|---:|
| Agriculture Food and Forest Products | 20 | 45.82 | 50.00 | 18.27 |
| Energy | 20 | 62.91 | 68.75 | 20.23 |
| Materials and Buildings | 22 | 49.80 | 52.10 | 17.27 |
| Transportation | 18 | 48.38 | 52.10 | 14.60 |

Financial-planning integration, quantified scenario analysis and asset valuation/impairment are strongest; current financial position, performance and cash-flow connectivity remain weakest. See [RQ1 tables](../../results/tables/) and [item heatmap](../../results/figures/04_item_heatmap.png).

# 10. RQ2 – Determinants of CFCQI

Primary model: pooled OLS with firm-clustered robust standard errors.

| Predictor | Coefficient | Clustered SE | p-value | 95% CI |
|---|---:|---:|---:|---|
| Firm size | 4.597 | 1.949 | 0.0183 | [0.777, 8.417] |
| External assurance | 11.171 | 8.433 | 0.1853 | [-5.358, 27.700] |
| Board oversight | 23.763 | 5.247 | <0.001 | [13.479, 34.047] |
| Leverage | 8.468 | 15.773 | 0.5914 | [-22.448, 39.383] |
| ROA | 49.574 | 24.334 | 0.0416 | [1.880, 97.269] |

Model R² = 0.478; adjusted R² = 0.410.

- H1 is supported in the pooled model.
- H2 is not supported.
- H3 is strongly supported and is the most robust result.
- ROA and Energy-group membership are secondary significant associations.

See [regression coefficient figure](../../results/figures/06_regression_coefficients.png).

# 11. RQ2 Diagnostics and Robustness

Maximum VIF = 1.93. Breusch–Pagan p = 0.0438 indicates mild heteroscedasticity, while residual normality is not rejected (Shapiro p = 0.2918). Six firm-years exceed Cook’s D > 4/n.

| Specification | H1 p | H2 p | H3 p |
|---|---:|---:|---:|
| Base pooled | 0.0183 | 0.1853 | <0.001 |
| Exclude Mobico | 0.0226 | 0.1907 | <0.001 |
| Exclude Mobico + Tesco | 0.0209 | 0.1905 | <0.001 |
| Exclude Tesco | 0.0169 | 0.1846 | <0.001 |
| F009 governance=0 | 0.0421 | 0.1725 | 0.0004 |
| Latest-only HC3 | 0.0765 | 0.7507 | 0.0016 |

H3 remains significant in every specification. H2 remains non-significant. H1 is stable in pooled/exclusion specifications but weakens in the latest-only 40-observation model.

# 12. RQ3 – Within-Firm Change Across Reporting Cycles

Change = Latest (T) − Prior (T1).

Mean change ≈ −0.003; median = 0. Twelve firms improve, 20 are unchanged, and eight deteriorate. Paired differences are non-normal, therefore Wilcoxon is primary: W = 101.5, p = 0.8959. Paired t-test p = 0.9988 and exact sign-test p = 0.5034.

| Specification | n pairs | Mean change | Median | Wilcoxon p | Paired t p |
|---|---:|---:|---:|---:|---:|
| Full sample | 40 | -0.003 | 0.00 | 0.8959 | 0.9988 |
| Exclude Mobico | 39 | 0.426 | 0.00 | 0.6145 | 0.7930 |
| Exclude Tesco | 39 | 0.213 | 0.00 | 0.7779 | 0.8983 |
| Exclude Mobico + Tesco | 38 | 0.658 | 0.00 | 0.4991 | 0.6899 |

See [paired-cycle figure](../../results/figures/03_paired_prior_latest.png) and [item-change figure](../../results/figures/05_item_change.png).

# 13. Special Cases and Sensitivity Flags

- Mobico F019-T covers 15 months to 31 March 2026; figures were not annualised.
- Tesco F032-T is a 53-week reporting period.
- Mondi’s integrated report is the company’s complete annual statutory report.
- Smiths Group latest uses FY2025 because FY2026 was not published by the sampling freeze.
- Spirax Group is the renamed Spirax-Sarco Engineering group.
- M&S partial first-pass files were invalidated and fully re-scored from complete reports.

# 14. Reproducibility

Principal execution sequence:

1. `01_validate_and_compute.py` – validate 0–2 coding and compute CFCQI.
2. `02_descriptives.py` – RQ1 tables/figures.
3. `03_reliability.py` – exact agreement and weighted kappa.
4. `04_regression_rq2.py` – pooled OLS with firm-clustered SE.
5. `05_paired_rq3.py` – Latest−Prior paired analysis.
6. `06_robustness.py` – diagnostics and sensitivity models.
7. `08_build_evidence_audit.py` – rebuild and verify the 960-row evidence audit.
8. `07_final_audit.py` – final integrity/reproducibility gate.

Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
bash run_all.sh
```

Expected tests: **3 passed**. Final audit: **all_pass: true**.

# 15. Final Technical Conclusions

The implementation is internally consistent and reproducible after final QA corrections. Board-level sustainability/climate oversight is the strongest empirical correlate of CFCQI. Firm size is positive in the primary pooled model but less stable in the latest-only specification. External assurance is not statistically significant. There is no systematic within-firm change across the two cycles.

Key methodological limitations are the report-cut-off/sample-freeze timing distinction, uneven item-level reliability, a small two-cycle panel, market-cap/climate-sensitive sample construction and judgement in several content-analysis boundaries.

# 16. Output Register

| Output | Purpose |
|---|---|
| VASU_FINAL_TECHNICAL_RESULTS.xlsx | Consolidated Excel workbook with sample, source register, codebook, evidence, data, validation and results |
| VASU_POWERBI_DATA.xlsx | Power BI-ready firm-year and item-long tables |
| VASU_ANALYSIS_DATASET_LOCKED.csv | Locked 80-row statistical dataset |
| CFCQI_EVIDENCE_AUDIT.csv | Regenerated 960-row evidence audit |
| CFCQI_FINAL_80.csv | Final scored CFCQI dataset |
| FIRM_VARIABLES_FINAL_80.csv | Final firm-variable dataset |
| RQ2_EXTENDED_ROBUSTNESS.csv | Expanded robustness specifications |
| RQ3_SENSITIVITY.csv | Paired-cycle sensitivity results |
| RQ3_ITEM_CHANGES.csv | Item-level Latest−Prior changes |

For repository navigation, see the root [README](../../README.md).
