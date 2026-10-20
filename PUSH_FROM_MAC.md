# Push the Complete Repository from macOS

This repository includes the full 80-report PDF corpus (~1.00 GB). The PDFs must be pushed with Git LFS.

## 1. Install prerequisites

```bash
brew install git git-lfs gh
```

Then authenticate GitHub if needed:

```bash
gh auth login
```

Choose GitHub.com → HTTPS → Login with a web browser.

## 2. Open the repository folder

```bash
cd ~/Downloads/Vasu_CFCQI_Research_Repository
```

## 3. Initialise Git + LFS

```bash
rm -rf .git
git init
git branch -M main
git lfs install
git lfs track "corpus/annual_reports/**/*.pdf"
```

The repository already contains a `.gitattributes` rule for these PDFs.

## 4. Add the remote

```bash
git remote add origin https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git
```

If `origin` already exists:

```bash
git remote set-url origin https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git
```

## 5. Make clean staged commits

### Commit 1 — repository foundation and documentation

```bash
git add README.md CITATION.cff LICENSE-CODE DATA_CORPUS_NOTICE.md \
  requirements.txt run_all.sh Makefile pytest.ini .gitignore .gitattributes \
  docs/ .github/
git commit -m "docs: establish CFCQI research repository and methodology"
```

### Commit 2 — analytical code and tests

```bash
git add src/ scripts/ tests/
git commit -m "feat: add reproducible CFCQI analysis pipeline and tests"
```

### Commit 3 — evidence, datasets and audit trail

```bash
git add data/ evidence/ corpus/CORPUS_MANIFEST.csv corpus/CORPUS_VERIFICATION.csv \
  corpus/CORPUS_VERIFICATION.json corpus/REPORT_INDEX.md corpus/README.md
git commit -m "data: add locked datasets, evidence audit and verified source manifest"
```

### Commit 4 — results, figures and dissertation records

```bash
git add results/ deliverables/ REPOSITORY_MANIFEST.json PUSH_CHECKLIST.md CORPUS_UPLOAD_GUIDE.md
git commit -m "results: add final analyses, figures and dissertation deliverables"
```

### Commit 5 — complete annual-report corpus via Git LFS

```bash
git add corpus/annual_reports/
git commit -m "corpus: add 80 SHA-256-verified annual reports via Git LFS"
```

## 6. Verify before pushing

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python scripts/verify_corpus.py
bash run_all.sh
```

Expected checks:

- 3/3 tests pass
- 80 reports present
- 80 hashes match
- 0 missing reports
- `all_pass: true`

## 7. Push

```bash
git push -u origin main
```

If Git LFS objects do not upload automatically:

```bash
git lfs push --all origin main
```

## 8. Final GitHub check

After the push, confirm on GitHub that:

- README renders correctly;
- `corpus/annual_reports/` contains 80 PDF entries;
- GitHub shows the PDFs as Git LFS files;
- `results/figures/04_item_heatmap.png` renders in README;
- the Actions workflow passes;
- source manifest and verification files are visible.
