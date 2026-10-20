# Data lineage and evidence chain

The repository is designed so each analytical result can be traced backwards:

```text
Annual-report PDF
   ↓ Report_ID + SHA-256 + source register
Evidence note (firm × cycle)
   ↓ 12 CFCQI decisions with page references
Locked coding input
   ↓ deterministic CFCQI calculation
80-row analysis dataset
   ↓ descriptive / OLS / paired / robustness scripts
Tables + figures + dissertation findings
```

The authoritative mapping between PDFs and analytical observations is `data/source_register/Vasu_Master_Annual_Report_Register.csv`.
