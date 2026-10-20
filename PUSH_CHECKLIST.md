# GitHub push checklist

## Recommended repository

`16814044-cfcqi-climate-disclosure`

Keep the repository **private until dissertation marking is complete**.

## Core repository

The code, derived data, evidence notes, figures, documentation and deliverables can be pushed normally.

## Annual-report corpus

The 80 PDFs should be copied from the verified Drive corpus into `corpus/annual_reports/` while preserving the exact sector/company paths in `corpus/CORPUS_MANIFEST.csv`, then committed using Git LFS.

```bash
git lfs install
git lfs track "corpus/annual_reports/**/*.pdf"
git add .gitattributes corpus/annual_reports corpus/CORPUS_MANIFEST.csv
git commit -m "Add verified 80-report corpus via Git LFS"
git push
```

## Before publishing publicly

- Confirm whether the 12-report repeat scoring is intra-coder or inter-coder before using either label.
- Consider removing `deliverables/project_record/` if supervisor/assessment-process documents should remain private.
- Annual reports retain issuer copyright; do not imply the repository relicenses them.
- Keep the CFCQI interpretation boundary visible: disclosure-depth measure, not compliance or climate-performance score.
