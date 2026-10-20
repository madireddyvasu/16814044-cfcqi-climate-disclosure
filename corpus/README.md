# Verified annual-report corpus

This directory is reserved for the **80 verified consolidated group annual reports** used in the study (40 firms × two reporting cycles). The PDFs should be stored with Git LFS using the exact relative paths recorded in `data/source_register/Vasu_Master_Annual_Report_Register.csv`.

## Verification controls

- 80 requested / 80 verified reports
- 80 unique SHA-256 hashes
- wrong-year, partial and duplicate first-pass files rejected before analysis
- company, reporting period, consolidated-group status and report completeness checked
- special-period cases (including Mobico and Tesco) documented in the source register and sensitivity analysis

## Add the corpus

```bash
git lfs install
git lfs track "corpus/annual_reports/**/*.pdf"
# Copy the Drive corpus into corpus/annual_reports preserving its sector/company folders
git add .gitattributes corpus/annual_reports data/source_register
git commit -m "Add verified annual-report corpus via Git LFS"
```

The repository source register is the authoritative map between each `Report_ID`, the local PDF path and its SHA-256 digest.
