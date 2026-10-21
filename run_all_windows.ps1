$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

Write-Host "CFCQI Windows reproducibility pipeline" -ForegroundColor Cyan
Write-Host "Repository: $Root"
Write-Host ""

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    py -3.12 -m venv .venv
}

$Python = Join-Path $Root ".venv\Scripts\python.exe"

Write-Host "Installing/updating dependencies..." -ForegroundColor Yellow
& $Python -m pip install --upgrade pip
& $Python -m pip install -r requirements.txt

Write-Host ""
Write-Host "Running tests..." -ForegroundColor Yellow
& $Python -m pytest -q

Write-Host ""
Write-Host "Running analysis pipeline..." -ForegroundColor Yellow
& $Python scripts/01_validate_and_compute.py
& $Python scripts/02_descriptives.py
& $Python scripts/03_reliability.py
& $Python scripts/04_regression_rq2.py
& $Python scripts/05_paired_rq3.py
& $Python scripts/06_robustness.py
& $Python scripts/07_final_audit.py

Write-Host ""
Write-Host "Pipeline complete." -ForegroundColor Green
Write-Host "Main result files:" -ForegroundColor Cyan
Write-Host "  results\tables\rq1_overall.csv"
Write-Host "  results\tables\regression_rq2.txt"
Write-Host "  results\tables\paired_rq3.txt"
Write-Host "  results\tables\robustness.txt"
Write-Host "  results\tables\reliability.csv"
Write-Host "  data\audit\FINAL_REPRODUCIBILITY_AUDIT.json"
Write-Host ""
Write-Host "Open the results folder with:" -ForegroundColor Cyan
Write-Host "  explorer results"
