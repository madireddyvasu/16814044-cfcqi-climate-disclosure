# Duplicate-Hash Audit — Vasu CFCQI Annual-Report Corpus

**Date:** 8 October 2026
**Scope:** 80 PDFs in `01_annual_reports/` (40 firms x 2 cycles)
**Method:** SHA-256 computed over the full file bytes of every PDF (`corpus_audit.json`).

## Result

- **80 files hashed, 80 unique SHA-256 values. Zero duplicates.**
- Every T (latest) and T1 (prior) file for the same company is a distinct document.

## Resolved incident (retained for the audit trail)

During the original download (7 Oct 2026), the file saved as `F027_T1.pdf` (Smiths Group FY2024)
was found to be **byte-identical** to `F027_T.pdf` (Smiths Group FY2025) - a download error that
put the wrong-year file on disk. It was replaced the same day with the genuine FY2024 report
(222 pages) downloaded from the official smiths.com URL, and the T1 coding was redone from the
correct document. The duplicate was caught by the hash comparison before any analysis used it.

## Page-count sanity check

Minimum 108 pages (Cranswick FY2024/25), maximum 481 pages. All 80 documents are full-length
annual reports - no stubs, extracts, or truncated files remain in the corpus.
