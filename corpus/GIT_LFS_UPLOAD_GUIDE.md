# Complete Corpus Upload — Git LFS

The analytical/research repository is already live and reproducibility-tested. The only large-binary stage is the verified 80-report annual-report corpus.

## Prerequisites

- Git and Git LFS installed.
- GitHub CLI authenticated as `madireddyvasu`.
- A local folder containing the 80 verified annual-report PDFs (nested folders are allowed).

## Procedure

```bash
git clone https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git
cd 16814044-cfcqi-climate-disclosure

git lfs install

python3 scripts/import_and_verify_corpus.py /PATH/TO/01_annual_reports
```

Do **not** continue unless the script reports:

```text
Expected reports: 80
Copied + verified: 80
Missing: 0
Ambiguous names: 0
Hash mismatches: 0

CORPUS_IMPORT_STATUS: PASS
```

Then:

```bash
git add .gitattributes corpus/annual_reports/
git commit -m "corpus: add 80 SHA-256-verified annual reports via Git LFS"
git push origin main
git lfs push --all origin main
```

Final checks:

```bash
git lfs ls-files | wc -l
find corpus/annual_reports -type f -iname "*.pdf" | wc -l
python3 scripts/verify_corpus.py
```

Expected counts: **80** and **80**, with corpus verification **PASS**.

## Integrity rule

Do not edit, optimise, recompress, redact or metadata-strip the annual-report PDFs. Their exact SHA-256 digests are part of the provenance record. Any byte-level change would break the frozen source audit.
