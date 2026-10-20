#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

python3 scripts/01_validate_and_compute.py
python3 scripts/02_descriptives.py
python3 scripts/03_reliability.py
python3 scripts/04_regression_rq2.py
python3 scripts/05_paired_rq3.py
python3 scripts/06_robustness.py
python3 scripts/08_build_evidence_audit.py
python3 scripts/07_final_audit.py

echo "Reproduction complete. See results/ and data/audit/."
