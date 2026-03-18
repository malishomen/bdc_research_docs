# TASK-0138 BRIEF REPORT — full simplified_wiki_v0 build (external outputs) + derived manifest update

Branch/HEAD (start): `test` @ `e9eca139a62bd762adab3517d02228be9cd4dc2b`

## Inputs (Pinned; Refuse-To-Run Enforced)

From `datasets/simplified_wiki_v0/MANIFEST.json`:
- dump_id: `20260201`
- filename: `simplewiki-20260201-pages-articles.xml.bz2`
- sha256: `a2af6ce4c421c400f498740be8aefe77f71d52cc97fe50ed35ba28c27a3c9da6`
- size_bytes: `342917678`
- local_path (external-only): `D:\datasets\wikimedia\simplewiki\20260201\simplewiki-20260201-pages-articles.xml.bz2`

Builder refuses to run if `sha256`/`size_bytes` mismatch (exit code `2`).

## Monitoring

Runbook: `reports/analysis/TASK_0138_MONITORING_COMMANDS.md`

## Full Build (External-Only)

out_root:
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build\`

Command:
```powershell
python datasets/simplified_wiki_v0/build_dataset.py `
  --manifest datasets/simplified_wiki_v0/MANIFEST.json `
  --out_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --progress_every_pages 20000
```

Build stats (from `full_build/BUILD_REPORT.json`):
- pages_seen: `548192`
- docs_written: `278985`
- skipped_redirect: `120968`
- skipped_non_article_ns: `148239`
- truncated_docs: `1367`

Split integrity check:
- train: `251120`, val: `13916`, test: `13949`
- disjoint + union == docs_written: PASS

Full-build output sha256:
- `docs.jsonl`: `dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687`
- `split_train.txt`: `841421d61445705d349529b19b3ee1df2f8c7bea832166b0cb49539f4d6f2b9c`
- `split_val.txt`: `79d835e6e5eeb626828c4843d536022a75414524d493cdc22f978345a8f42eeb`
- `split_test.txt`: `e3aad4a68428d08773c3be17cc6380910af73263eb1a973a4eca7c9f19a48b19`

## Determinism Spotcheck (Smoke)

Spotcheck run (max_docs=1000):
- out_root: `D:\datasets\bdc\simplified_wiki_v0\20260201\spotcheck_smoke\`
- Result: sha256 matches TASK-0137 smoke hashes exactly (PASS).

## What Changed (In Git)

- Updated: `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json` (added full build block; kept smoke hashes; recorded spotcheck PASS)
- Updated: `datasets/simplified_wiki_v0/OUTPUT_POINTER.md` (added `full_build` pointer)
- Added: `reports/analysis/TASK_0138_MONITORING_COMMANDS.md`, `reports/analysis/TASK_0138_BRIEF_REPORT.md`

## Explicitly Not Committed

- No JSONL/split outputs committed (external-only).

## Next Step

- TASK-0139: comprehension metric v0 + training harness (consuming external simplified_wiki_v0 outputs).

