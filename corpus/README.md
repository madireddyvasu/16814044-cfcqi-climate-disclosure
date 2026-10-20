# Verified annual-report corpus

This directory contains the **80 verified consolidated-group annual reports** used in the study: 40 firms across two reporting cycles.

The PDFs are stored under `corpus/annual_reports/` using **Git Large File Storage (Git LFS)** and the exact sector/company paths recorded in `CORPUS_MANIFEST.csv`.

## Verification status

- Requested reports: **80**
- PDFs present: **80**
- SHA-256 matches: **80/80**
- Missing reports: **0**
- Hash mismatches: **0**
- Unique verified reports: **80**
- Total source corpus: approximately **1.00 GB**
- Corpus audit: **PASS**

Wrong-year, partial, truncated and duplicate first-pass files were rejected before the frozen corpus was created. Reporting-period boundary cases, including Mobico and Tesco, are documented in the source register and robustness analysis.

## Verify after cloning

Install Git LFS before cloning or pulling the corpus:

```bash
git lfs install
git clone https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git
cd 16814044-cfcqi-climate-disclosure
git lfs pull
python scripts/verify_corpus.py
```

The verification script checks every PDF against the frozen SHA-256 digest in `CORPUS_MANIFEST.csv`.

The source register is the authoritative map between each `Report_ID`, company, reporting cycle, local PDF path and hash.

## Rights notice

The annual reports remain copyright of their respective issuers. They are retained here as source material for academic reproducibility. The repository's code licence does not relicense those corporate publications.
