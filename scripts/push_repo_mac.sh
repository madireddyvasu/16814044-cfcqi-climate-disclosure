#!/usr/bin/env bash
set -euo pipefail

REMOTE="https://github.com/madireddyvasu/16814044-cfcqi-climate-disclosure.git"

command -v git >/dev/null || { echo "git is required"; exit 1; }
command -v git-lfs >/dev/null 2>&1 || command -v git lfs >/dev/null 2>&1 || { echo "Git LFS is required: brew install git-lfs"; exit 1; }

git init
git branch -M main
git lfs install
git lfs track "corpus/annual_reports/**/*.pdf"

git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE"

git add README.md CITATION.cff LICENSE-CODE DATA_CORPUS_NOTICE.md requirements.txt run_all.sh Makefile pytest.ini .gitignore .gitattributes docs/ .github/
git commit -m "docs: establish CFCQI research repository and methodology"

git add src/ scripts/ tests/
git commit -m "feat: add reproducible CFCQI analysis pipeline and tests"

git add data/ evidence/ corpus/CORPUS_MANIFEST.csv corpus/CORPUS_VERIFICATION.csv corpus/CORPUS_VERIFICATION.json corpus/REPORT_INDEX.md corpus/README.md
git commit -m "data: add locked datasets, evidence audit and verified source manifest"

git add results/ deliverables/ REPOSITORY_MANIFEST.json PUSH_CHECKLIST.md CORPUS_UPLOAD_GUIDE.md PUSH_FROM_MAC.md
git commit -m "results: add final analyses, figures and dissertation deliverables"

git add corpus/annual_reports/
git commit -m "corpus: add 80 SHA-256-verified annual reports via Git LFS"

echo "Repository committed locally. Run the verification commands in PUSH_FROM_MAC.md, then:"
echo "  git push -u origin main"
echo "  git lfs push --all origin main"
