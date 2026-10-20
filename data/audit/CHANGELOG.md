# Changelog

## v1.1 — 2026-10-07 — SUPERVISOR-GRADE REVIEW (audit + fixes + robustness + new docs)
**Audited:** sample register vs SAMPLE_SELECTION.md vs dataset (names, groups, cycles — all consistent); 6 evidence files spot-checked against frozen codebook (2 each from coderB, coderE, coderG); currency documentation (all non-GBP reporters have ECB rate+date); leverage definition; cycle labels; findings_summary numbers vs results tables.
**Fixed:**
- CRITICAL: F035 (M&S) T/T1 rows were coded from 90/91-page partial PDFs (strategic report missing) — invalidated; full reports obtained (208/224pp; official site bot-blocked, mirror verified genuine via figure cross-check), re-coded from scratch (coderM), rows replaced. Originals kept as F035_*_partial_ORIGINAL.pdf.
- MAJOR: leverage definition inconsistency — IMI excluded bank overdrafts while others included them. Ruling: overdrafts ARE interest-bearing borrowings → included; F028_T 0.2105→0.2281, F028_T1 0.2069→0.2435. Leases excluded where separately disclosed (uniform convention); F015 Wizz Air documented exception (inseparable line).
- MINOR: data/sample_register.csv F027 row had unquoted comma (broke strict CSV parsing) — fixed; F019 T period corrected to "15m to 31 Mar 2026".
**Added:** scripts/06_robustness.py (VIF, Breusch-Pagan, Shapiro, Cook's D, sensitivity A: drop F019, sensitivity B: drop influential points, plain-English verdict) → results/tables/robustness.txt + results/figures/robustness_residuals.png; docs/DATA_DICTIONARY.md; docs/DISSERTATION_OUTLINE.md (chapter-by-chapter writing guide wired to repo outputs).
**Updated:** README.md (completed status, results, repo-ships-PDFs), run_all.sh (01→06), .gitignore (repo ships everything by design).
**Borderline judgments left standing** (documented in decision_log.md R5; Vasu to confirm F009 board_oversight): F009 board_oversight=1, F012 item10=2, F023 item1=1, F034 item11=2.
**Residual risks:** ECB FX rates not independently re-verified; F015 used secondary fixings table; single-coder design (intra-coder κ only).

## v1.0 — 2026-10-07 — TECHNICAL IMPLEMENTATION COMPLETE
- Full 80 firm-year dataset coded (40 FTSE 350 firms × 2 cycles; sample frozen 2026-10-07, method in docs/SAMPLE_SELECTION.md).
- Codebook v1.0 frozen after 5-report pilot; every score carries verbatim quote + page in data/interim/evidence/.
- Reliability: 15% blind re-code, pooled weighted κ = 0.631 (≥ 0.60 threshold).
- Analysis pipeline run on n=80: RQ1 descriptives, RQ2 OLS w/ firm-clustered SEs (R²=0.539), RQ3 Wilcoxon (p=0.952, no significant change). [v1.0 interim numbers — superseded by the v1.1 final numbers above after M&S re-code and IMI leverage fix.]
- Headline (final, after M&S re-code + IMI leverage fix): mean CFCQI 51.77; H1 supported (p=0.018), H2 not supported (p=0.185), H3 strongly supported (p<0.001); RQ3 Wilcoxon p=0.896 (no change).
- src/cfcqi.py: pure-numpy fallback for weighted kappa when sklearn unavailable.
- F010 (Energean) + F028 (IMI) recovered via live browser after Cloudflare block.

## v0.1 — 2026-10-07
- Initial project scaffold: folder structure, README, re-baselined project plan.
- Draft CFCQI coding manual (12 items, 0–2 scale) — **to be piloted and frozen**.
- Sample register + coding templates.
- Analysis pipeline scripts 01–05 (validated end-to-end on synthetic data).
