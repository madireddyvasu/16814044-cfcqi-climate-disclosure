# Chapter 3: Methodology and Ethics

## 3.1 Chapter Introduction and Research Onion

This chapter translates the conceptual framework into a coherent Business Analytics methodology using the Research Onion of Saunders et al. (2019). The onion moves from philosophy through approach, methodological choice, strategy and time horizon to data collection and analysis. This structure clarifies the link between research questions, hypotheses, variables and statistical procedures. Figure 3.1 and Table 3.1 summarise the selected choices.

<img src="media/image7.png" style="width:5.7in;height:6.29485in" alt="Image: image7.png" />

*Figure 3.1. Research Onion and methodological choices used in this study. Adapted from Saunders et al. (2019).*

*Table 3.1. Research Onion decisions and justification.*

| **Layer**             | **Selected choice**                                                    | **Justification**                                                                              |
|-----------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Philosophy            | Pragmatism                                                             | Addresses an applied Business Analytics problem while making measurement assumptions explicit. |
| Approach              | Deductive                                                              | Literature informs hypotheses and variables before testing.                                    |
| Methodological choice | Mono-method quantitative                                               | Final evidence is represented as numerical firm-year variables; thematic analysis is not used. |
| Strategy              | Quantitative content analysis                                          | Predefined rules convert annual-report evidence into comparable 0–2 scores.                    |
| Time horizon          | Two consecutive reporting cycles                                       | Supports pooled analysis and within-firm comparison.                                           |
| Techniques/procedures | Sample selection, data collection, CFCQI scoring, OLS and paired tests | Connects documentary evidence directly to reproducible statistical analysis.                   |

Source: Author, adapted from Saunders et al. (2019).

## 3.2 Research Philosophy – Pragmatism

Pragmatism is appropriate because the study addresses a practical measurement problem: converting heterogeneous climate-reporting evidence into a transparent indicator and relating it to organisational characteristics. It permits documentary judgement while prioritising methods that answer the research problem (Saunders et al., 2019). The project remains mono-method quantitative because the evidence is transformed into numerical variables and analysed statistically.

## 3.3 Research Approach – Deductive

The approach is deductive. Chapter 2 identifies expected relationships between organisational capacity, external assurance, board accountability and disclosure depth. Those expectations are converted into pre-specified hypotheses and operational variables before regression analysis. Likewise, the 12 CFCQI dimensions and 0–2 decision rules are defined in advance rather than generated inductively from themes in the annual reports.

## 3.4 Methodological Choice and Strategy

The methodological choice is mono-method quantitative and the strategy is quantitative content analysis. No themes are generated inductively; a frozen scoring scheme classifies annual-report evidence into predetermined categories and produces numerical variables. This is consistent with quantitative content analysis, which systematically classifies communication using explicit, replicable rules (Neuendorf, 2017).

## 3.5 Time Horizon, Sample and Data Collection

The study uses two consecutive reporting cycles for each firm. The sampling frame is non-financial Financial Times Stock Exchange 350 Index (FTSE 350) firms mapped to the four climate-sensitive Task Force on Climate-related Financial Disclosures (TCFD) groups. Eligible firms were ranked by market capitalisation, producing a supervisor-reviewed 40-firm sample. The ranking was frozen on 7 October 2026, while report eligibility ended on 31 August 2026; this boundary-timing limitation is disclosed in Chapter 6.

Two reports per firm produced 80 firm-years. Each document was checked for company identity, financial year (FY), consolidated-group status and completeness; Secure Hash Algorithm 256-bit (SHA-256) hashes confirmed 80 unique files. Mobico’s 15-month latest period and Tesco’s 53-week latest year were retained and tested through exclusion sensitivities.

## 3.6 CFCQI Scoring, Variables and Hypotheses

The Climate Financial Connectivity and Quantification Index (CFCQI) contains 12 items covering current and anticipated financial effects, capital allocation, valuation/impairment, provisions, carbon/regulatory costs, financial-planning integration and quantified scenario analysis. Scores are 0 (no qualifying financial connection after full-report review), 1 (explicit but unquantified connection) or 2 (quantified or strongly specific financial link). Equal weighting is used because no defensible ex ante basis exists for differential weights and unweighted disclosure indices are established in disclosure research (Tsalavoutas et al., 2010). CFCQI = (raw score / 24) × 100 and measures disclosure depth, not compliance or environmental performance.

Firm size is ln(total assets in Pound Sterling (GBP) millions). External sustainability assurance equals 1 for qualifying independent assurance and 0 otherwise; the statutory financial audit alone does not qualify. Board oversight equals 1 where a board-level committee has an explicit sustainability/climate remit. Leverage and Return on Assets (ROA) are financial controls, while TCFD group and cycle are categorical controls. Table 3.2 summarises the definitions.

*Table 3.2. Variables and operational definitions.*

| **Variable**       | **Operationalisation**                                                        | **Role**           |
|--------------------|-------------------------------------------------------------------------------|--------------------|
| CFCQI              | 12-item score, 0–100                                                          | Dependent variable |
| Firm size          | ln(total assets in GBP millions)                                              | Primary predictor  |
| External assurance | 1 = qualifying independent assurance; 0 = otherwise                           | Primary predictor  |
| Board oversight    | 1 = board committee with explicit sustainability/climate remit; 0 = otherwise | Primary predictor  |
| Leverage           | Interest-bearing debt / total assets                                          | Control            |
| ROA                | Profit after tax / average total assets                                       | Control            |
| TCFD group; cycle  | Categorical indicators                                                        | Controls           |

Source: Study codebook and locked data dictionary.

The supervisor requested both null and alternative hypotheses. Each pair is assessed through the sign, 95% confidence interval and p-value of the corresponding OLS coefficient. A non-significant result is described as failure to reject the null, not acceptance of it.

*Table 3.3. Null and alternative hypotheses.*

| **Test**        | **Null hypothesis**                                                                                                       | **Alternative hypothesis**                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Size            | H01: Firm size has no statistically significant association with CFCQI after controls.                                    | H11: Firm size is positively associated with CFCQI after controls.                             |
| Assurance       | H02: External sustainability assurance has no statistically significant association with CFCQI after controls.            | H12: Firms with qualifying external sustainability assurance have higher CFCQI after controls. |
| Board oversight | H03: Board-level sustainability/climate oversight has no statistically significant association with CFCQI after controls. | H13: Firms with qualifying board-level oversight have higher CFCQI after controls.             |

## 3.7 Statistical Analysis

Analysis begins with CFCQI descriptives by cycle, TCFD group and item. Determinants are estimated using pooled ordinary least squares (OLS) with firm-clustered standard errors because each company contributes two observations (Cameron & Miller, 2015; Wooldridge, 2010). OLS is retained because the 0–100 index is quasi-continuous and coefficients are interpretable in CFCQI points. Variance Inflation Factors (VIFs), Breusch–Pagan testing, residual checks, leverage and Cook’s distance assess model behaviour. Robustness checks cover influential observations, atypical periods, the borderline Drax classification and a latest-cycle-only Heteroskedasticity-Consistent type 3 (HC3) model.

For reporting-cycle change, ΔCFCQI is defined as Latest (T) − Prior (T1). Normality of paired differences determines the primary test; where normality is not supported, the Wilcoxon signed-rank test is used, with a paired t-test and exact sign test as sensitivities. Item-level change is also calculated, and Mobico/Tesco exclusion tests assess whether their atypical reporting periods drive the conclusion.

## 3.8 Reliability, Validity and Reproducibility

A blind second-pass scoring exercise covered 12 reports (15% of the corpus) using a separate workflow that had not produced their first-pass scores. It is treated as a scoring-stability check, not proof of human inter-coder agreement. Exact agreement and weighted Cohen’s kappa assess the ordinal 0–2 scores (Cohen, 1968; Milne & Adler, 1999). Content and construct validity are supported by predefined financially connected disclosure concepts and evidence requirements. Criterion validity is not claimed because no accepted external benchmark exists. Page-level evidence, hashes, decision logs, locked datasets and automated checks strengthen reproducibility.

## 3.9 Ethics and Responsible Data Use

Ethical approval was granted through Coventry University’s research ethics process. The project uses public corporate reports, recruits no human participants and does not collect personal or special-category data for analysis. Handling follows university governance and United Kingdom General Data Protection Regulation (UK GDPR) principles. Source provenance, hashes, decision logs and locked datasets protect integrity; no evidence or result is fabricated, CFCQI is not presented as legal compliance, and regression coefficients are interpreted as associations.

## 3.10 Chapter Summary

Following the Research Onion layer by layer, this chapter establishes a coherent mono-method quantitative design based on pragmatism, deduction, quantitative content analysis, predefined CFCQI scoring and reproducible statistical testing. Chapter 4 reports the empirical results; Chapters 5 and 6 provide interpretation and direct answers to the research questions.

