# Adding the verified 80-report corpus

The repository already contains the exact expected folder structure under `corpus/annual_reports/`.

## 1. Copy the PDFs

Copy the contents of the verified Drive folder `01_annual_reports` into:

```text
corpus/annual_reports/
```

Do **not** rename files. Paths must match `corpus/CORPUS_MANIFEST.csv`.

## 2. Verify every report

```bash
python scripts/verify_corpus.py
```

The required final output is:

```text
Expected reports: 80
Present:          80
Hash matched:     80
CORPUS_STATUS: PASS
```

`corpus/CORPUS_VERIFICATION.csv` is generated as an audit record.

## 3. Track PDFs with Git LFS

```bash
git lfs install
git lfs track "corpus/annual_reports/**/*.pdf"
git add .gitattributes
git add corpus/annual_reports corpus/CORPUS_MANIFEST.csv corpus/CORPUS_VERIFICATION.csv
git commit -m "Add verified 80-report annual-report corpus via Git LFS"
git push origin main
```

## 4. Verify LFS tracking

```bash
git lfs ls-files
```

It should list all 80 annual-report PDFs.

## Important

The annual reports remain third-party corporate publications. Including them in a private research repository is for dissertation reproducibility. Before making the repository public, review redistribution rights and consider keeping only the source register/URLs/hashes publicly if needed.
