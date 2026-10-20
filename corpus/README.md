# Source corpus register

This directory contains the frozen **80-report corpus manifest**, report index, and SHA-256 verification records used by the technical implementation.

The issuer-owned annual-report PDF files are not stored in this GitHub repository. If a local copy of the 80 PDFs is placed under `corpus/annual_reports/` using the relative paths in `CORPUS_MANIFEST.csv`, run:

```bash
python scripts/verify_corpus.py
```

The verifier checks the local files against the exact SHA-256 digests recorded in the frozen manifest.
