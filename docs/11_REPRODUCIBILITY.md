# Reproducibility guide

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
bash run_all.sh
```

The pipeline reads the frozen input files in `data/input/`, recomputes CFCQI, recreates the descriptive/regression/paired outputs, and finishes with the final integrity audit.

## Expected audit

`data/audit/FINAL_REPRODUCIBILITY_AUDIT.json` should report:
- 80 rows
- 40 firms
- 40 latest + 40 prior observations
- 960 evidence decisions
- 80 source reports
- 80 unique hashes
- zero missing CFCQI items
- zero score/formula mismatches
- `all_pass: true`

The annual-report PDFs are not required to rerun the statistics because the evidence-backed numeric input is frozen. The complete 80-report source corpus is included under `corpus/annual_reports/` via Git LFS for source-level audit.
