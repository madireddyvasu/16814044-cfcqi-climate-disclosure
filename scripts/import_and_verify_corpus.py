#!/usr/bin/env python3
from pathlib import Path
import argparse, csv, hashlib, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'corpus' / 'CORPUS_MANIFEST.csv'
DEST_ROOT = ROOT / 'corpus' / 'annual_reports'

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description='Import the 80 annual-report PDFs from a downloaded source folder, place them in the exact repository paths, and verify SHA-256 hashes.')
    ap.add_argument('source_folder', help='Folder containing the downloaded annual-report PDFs; nested folders are allowed.')
    args = ap.parse_args()
    source = Path(args.source_folder).expanduser().resolve()
    if not source.exists():
        sys.exit(f'Source folder does not exist: {source}')

    rows = list(csv.DictReader(MANIFEST.open(encoding='utf-8-sig')))
    by_name = {}
    for p in source.rglob('*.pdf'):
        by_name.setdefault(p.name, []).append(p)

    missing, ambiguous, bad_hash = [], [], []
    copied = 0
    for row in rows:
        rel = Path(row['Local_File_Name'])
        name = rel.name
        candidates = by_name.get(name, [])
        if not candidates:
            missing.append(name)
            continue
        if len(candidates) > 1:
            ambiguous.append((name, [str(x) for x in candidates]))
            continue
        src = candidates[0]
        got = sha256(src)
        exp = row['SHA256'].strip().lower()
        if got != exp:
            bad_hash.append((name, exp, got))
            continue
        dst = DEST_ROOT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

    print(f'Expected reports: {len(rows)}')
    print(f'Copied + verified: {copied}')
    print(f'Missing: {len(missing)}')
    print(f'Ambiguous names: {len(ambiguous)}')
    print(f'Hash mismatches: {len(bad_hash)}')
    if missing:
        print('\nMissing files:')
        for x in missing: print(' -', x)
    if ambiguous:
        print('\nAmbiguous filenames:')
        for name, paths in ambiguous:
            print(' -', name)
            for p in paths: print('    ', p)
    if bad_hash:
        print('\nHash mismatches:')
        for name, exp, got in bad_hash:
            print(f' - {name}\n   expected {exp}\n   got      {got}')
    if copied == len(rows) and not missing and not ambiguous and not bad_hash:
        print('\nCORPUS_IMPORT_STATUS: PASS')
        return
    sys.exit('\nCORPUS_IMPORT_STATUS: FAIL')

if __name__ == '__main__':
    main()
