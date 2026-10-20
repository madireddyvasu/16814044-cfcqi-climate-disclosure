**COVENTRY UNIVERSITY**

**Student Research and Defence Notes**

*Plain-language record of what was done and what the results mean*

Vasu Deva Rao Madireddy | Student ID 16814044 | MSc Business Analytics | 7015SOM

# Project in one paragraph

The project measures how deeply climate-sensitive FTSE 350 firms connect climate issues to financial consequences in their annual reports. Forty firms were selected across four TCFD climate-sensitive groups and two consecutive annual reports were reviewed for each firm. A 12-item Climate Financial Connectivity and Quantification Index (CFCQI) converts report evidence into 0–2 item scores and a 0–100 total. The resulting 80 firm-year dataset is analysed descriptively, through pooled OLS regression with firm-clustered robust standard errors, and through paired reporting-cycle tests.

# Why the Research Onion is used

The Research Onion gives a logical sequence for methodological decisions. This study uses pragmatism because it is an applied Business Analytics problem; a deductive approach because hypotheses and scoring rules are specified before statistical testing; a mono-method quantitative choice; quantitative content analysis as the strategy; two consecutive reporting cycles as the time horizon; and structured report extraction/scoring plus statistical analysis as the techniques and procedures.

# Why this is quantitative content analysis, not thematic analysis

The study does not inductively discover themes. The 12 CFCQI dimensions and 0–2 decision rules are predefined. Annual-report passages are evidence used to assign numerical scores. Those scores, together with financial/governance variables, form the quantitative dataset. The documentary review is therefore structured quantitative content analysis rather than thematic analysis.

# What CFCQI measures

CFCQI measures disclosure depth and financial connectivity. It does not measure environmental performance and it is not an IFRS S2/UK SRS compliance score. The index asks whether reports connect climate matters to current/anticipated financial position, performance and cash flows, capital allocation, accounting estimates, regulatory/carbon costs, financial planning and quantified scenarios.

# Why the 12 items have equal weight

No validated regulatory or empirical weighting scheme establishes that one CFCQI dimension should mechanically count more than another. Equal weighting makes the index transparent and reproducible and avoids choosing weights after seeing the results. The limitation is stated explicitly.

# Sample and data

The final sample is 40 climate-sensitive non-financial FTSE 350 firms: 10 Energy, 9 Transportation, 11 Materials and Buildings, and 10 Agriculture/Food/Forest firms. Two consecutive annual reports per firm produce 80 firm-years. All 80 reports were verified for entity, year and completeness and have unique SHA-256 hashes. Report eligibility ended 31 August 2026; the final market-capitalisation sample frame was frozen 7 October 2026.

# Main variables

Dependent variable: CFCQI (0–100). Main predictors: firm size (natural logarithm of total assets in GBP millions), external sustainability assurance (1/0), and qualifying board-level sustainability/climate oversight (1/0). Controls: leverage, Return on Assets (ROA), TCFD group and reporting cycle.

# Hypotheses

H01: no significant association between firm size and CFCQI; H11: positive association. H02: no significant association between external assurance and CFCQI; H12: assured firms have higher CFCQI. H03: no significant association between board oversight and CFCQI; H13: firms with qualifying board oversight have higher CFCQI.

# How the hypotheses are tested

Pooled Ordinary Least Squares (OLS) estimates CFCQI as the dependent variable. Because each firm appears twice, standard errors are clustered by firm. For each predictor the coefficient sign, 95% confidence interval and p-value are used. A statistically non-significant result is described as failing to reject H0, not accepting H0.

# Reliability

Twelve reports (15% of the corpus) were blindly re-scored through a separate scoring workflow. Exact agreement was 66.7% and pooled weighted Cohen’s kappa was 0.631. Item-level agreement varied, so the dissertation treats reliability as acceptable overall but not uniformly strong. The exercise is presented as a scoring-stability/reproducibility check, not as proof of human inter-coder agreement.

# RQ1 result

Overall CFCQI mean = 51.77 (SD 18.65): disclosure is moderate and heterogeneous. Financial-planning integration is strongest (83.8% score 2); quantified scenario analysis and impairment/valuation links are also relatively developed. The largest gaps are current financial position, performance and cash-flow effects, where 77.5%, 68.8% and 72.5% respectively score zero.

# RQ2 result

Pooled model R² = 0.478. Firm size: β = 4.60, p = .018, supporting H11 in the primary model, but latest-cycle-only HC3 weakens to about p = .076. External assurance: β = 11.17, p = .185, so H02 is not rejected/H12 is not supported. Board oversight: β = 23.76, p < .001, strongly supporting H13 and remaining robust across sensitivity tests. ROA and Energy-sector membership are secondary significant associations.

# RQ3 result

Change is defined as Latest minus Prior. Mean change is essentially zero (about −0.003), median 0; 12 firms improve, 20 are unchanged and 8 decline. Wilcoxon p = .896, paired t-test p = .999 and exact sign test p = .503. Excluding Mobico, Tesco or both does not change the conclusion: there is no systematic two-cycle improvement.

# Diagnostics and robustness

Maximum VIF is 1.93, indicating no serious multicollinearity. Breusch–Pagan p = .044 motivates robust inference. Residual normality is acceptable (Shapiro p = .292). Six influential firm-years were examined with Cook’s distance. Additional models exclude atypical reporting periods, change the borderline Drax governance classification and run latest-cycle-only HC3 inference. H3 is the most stable finding.

# Triple Bottom Line interpretation

The conceptual pathway is: environmental climate risk → governance/accountability → financial decision-making and reporting → financially connected climate disclosure → CFCQI. The results suggest that formal board accountability is especially important in translating environmental issues into more financially connected reporting, while assurance alone is insufficient when its scope is concentrated on selected sustainability metrics.

# Main contribution

Methodologically, the study creates an auditable financial-connectivity index with page-level provenance. Empirically, it provides a pre-UK SRS baseline and tests organisational correlates across two cycles. Practically, it identifies the gap between mature climate processes and direct current financial effects and translates that gap into actions for boards, finance teams, assurers and regulators.

# Main limitations

The sample covers 40 large listed firms and only two cycles; CFCQI involves judgement; some item-level reliability is weak; governance/assurance are binary simplifications; the observational regression cannot establish causality; sample-freeze and report-eligibility dates differ; some financial data require FX conversion; and disclosure quality is not climate-performance quality.

# Fast answers for supervisor questions

| Question | Answer |
|---|---|
| What is FY? | Financial Year. |
| What is market capitalisation? | The market value of a company’s outstanding equity; it was used to rank eligible firms within the sampling frame. |
| What is pragmatism here? | A philosophy focused on using methods that appropriately answer an applied problem; it does not mean that the study is automatically mixed methods. |
| Why not thematic analysis? | Themes were not generated inductively. Predefined financial-connectivity criteria were scored numerically. |
| Why Python and Excel? | Excel is the auditable data layer; Python reproduces validation, descriptives, regression, reliability, paired tests, robustness and figures. |
| What does p < .05 mean? | The observed evidence is sufficiently inconsistent with the null hypothesis at the conventional 5% threshold; it does not prove causality. |
| Why clustered standard errors? | Each firm contributes two observations, so errors may be correlated within the same firm. |
| What is HC3? | A heteroskedasticity-consistent robust standard-error estimator used in the latest-cycle-only sensitivity model. |
| What is the strongest result? | Board-level sustainability/climate oversight: about +23.76 CFCQI points in the pooled model, p < .001, robust across sensitivity checks. |
| What is the overall conclusion? | Climate reporting processes are established, but quantified financial connectivity remains uneven; governance is more strongly associated with depth than external assurance, and there is no systematic improvement across the two observed cycles. |
