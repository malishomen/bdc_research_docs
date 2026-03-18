# TASK-0137 BRIEF REPORT — build simplified_wiki_v0 from pinned dump (deterministic JSONL + splits + derived manifest)

Branch/HEAD (start): `test` @ `764fac9d585420e36342bb53f525cab888a9275d`

## What Changed (In Git)

- Builder script: `datasets/simplified_wiki_v0/build_dataset.py`
- Derived manifest (smoke build hashes + repro gate): `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`
- External output pointer: `datasets/simplified_wiki_v0/OUTPUT_POINTER.md`
- Monitoring commands: `reports/analysis/TASK_0137_MONITORING_COMMANDS.md`

## Input (Pinned; Refuse-To-Run Enforced)

From `datasets/simplified_wiki_v0/MANIFEST.json`:
- dump_id: `20260201`
- filename: `simplewiki-20260201-pages-articles.xml.bz2`
- sha256: `a2af6ce4c421c400f498740be8aefe77f71d52cc97fe50ed35ba28c27a3c9da6`
- size_bytes: `342917678`
- local_path (external-only): `D:\datasets\wikimedia\simplewiki\20260201\simplewiki-20260201-pages-articles.xml.bz2`

Builder behavior:
- Hard-fails (exit 2) if `sha256` or `size_bytes` mismatch (no processing on mismatched inputs).
- No network calls.

## Output (External-Only; Not In Git)

Preferred external root: `D:\datasets\bdc\simplified_wiki_v0\20260201\`

Smoke runs (max_docs=1000; deterministic):
```powershell
$m = "datasets/simplified_wiki_v0/MANIFEST.json"
$base = "D:\datasets\bdc\simplified_wiki_v0\20260201"
python datasets/simplified_wiki_v0/build_dataset.py --manifest $m --out_root (Join-Path $base "smoke_run1") --max_docs 1000
python datasets/simplified_wiki_v0/build_dataset.py --manifest $m --out_root (Join-Path $base "smoke_run2") --max_docs 1000
```

Filtering rules (in code + recorded in `DERIVED_MANIFEST.json`):
- exclude redirects
- include namespace `0` only
- drop empty text after normalization

Normalization/truncation:
- normalize newlines to `\n`, strip trailing whitespace per line, collapse 3+ blank lines to 2
- truncate `text` to `max_chars=50000` (set `truncated=true`)

Smoke stats (run1):
- pages_seen: `1427`
- docs_written: `1000`
- skipped_redirect: `315`
- skipped_non_article_ns: `112`
- truncated_docs: `22`

## Reproducibility Gate (Smoke Run1 == Run2)

Output hashes (identical across smoke_run1 and smoke_run2):
- `docs.jsonl`: `e40249fce37bbd7964a1533c63de452c93fdbdba7e6ae5f33ea3893e2f04aa5b`
- `split_train.txt`: `de70204186f8900d557ed1de4d5865e8fb5e7fbda83866822e553f69c787988f`
- `split_val.txt`: `7381bf24abb27f2c5c04c5680657a4ff74f1a01c5485ac66cb2617f839750aff`
- `split_test.txt`: `6c3459ea06e7ad6c2b27be4886a4f2a495f4e12efef89ef1671f4a290f2fc609`

Verification command:
```powershell
$r1 = "D:\datasets\bdc\simplified_wiki_v0\20260201\smoke_run1\BUILD_REPORT.json"
$r2 = "D:\datasets\bdc\simplified_wiki_v0\20260201\smoke_run2\BUILD_REPORT.json"
python -c "import json,sys; from pathlib import Path; a=json.loads(Path(sys.argv[1]).read_text('utf-8'))['outputs']; b=json.loads(Path(sys.argv[2]).read_text('utf-8'))['outputs']; print('REPRO_OK' if a==b else 'REPRO_FAIL'); sys.exit(0 if a==b else 2)" $r1 $r2
```

## Next Step

- TASK-0138: full build (no `--max_docs`) to external output root + derived manifest update (hashes, counts).

