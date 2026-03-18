# Release Notes — Main Merge Checkpoint (2026-02-08) R2: simplified_wiki_v0 + comprehension v0 policy PASS

This release merges `test` into `main` as a checkpoint after completing the pinned `simplified_wiki_v0` dataset pipeline and the first real-data comprehension metric (v0 cloze), including a numeric progress policy and evaluator with a PASS verdict.

## Scope / Safety Constraints

- No network calls added to builders/trainers.
- Dataset and training outputs remain **external-only** / gitignored (no large artifacts in git).
- Dataset input is provenance-pinned by `sha256` + `size_bytes` (`datasets/simplified_wiki_v0/MANIFEST.json`).
- Dataset build outputs are pinned by `sha256` (`datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`).

## Included Milestones (TASK-0136 .. TASK-0140)

### simplified_wiki_v0 provenance + deterministic build

- TASK-0136: acquired official Simple English Wikipedia dump externally and pinned provenance in `datasets/simplified_wiki_v0/MANIFEST.json` (sha256/size/dump_id/url/local_path).
- TASK-0137: implemented deterministic builder `datasets/simplified_wiki_v0/build_dataset.py`:
  - streams bz2 XML, refuses to run on manifest mismatch
  - filters redirects and non-article namespaces
  - deterministic normalization + deterministic split
  - writes outputs external-only; records output hashes in `DERIVED_MANIFEST.json`.
- TASK-0138: full build to external root (`...\\full_build`) and derived manifest update with full-build counts and sha256 of `docs.jsonl` and split files.

### Comprehension v0 cloze metric + policy

- TASK-0139: introduced comprehension metric v0 (cloze reconstruction) over `simplified_wiki_v0`:
  - deterministic masking (sha256(doc_id, token_index, salt))
  - deterministic tokenizer baseline (whitespace-hash or byte)
  - training harness w/ RUN_METADATA and sanity baselines (shuffled/random)
  - reproducibility smoke (repeat run matches within required drift)
  - outputs remain under `logs/` (gitignored).
- TASK-0140: defined numeric progress policy + evaluator:
  - `docs/spec/COMPREHENSION_V0_PROGRESS_POLICY.md`
  - `tools/analysis/exp0017_progress_policy_eval.py` (exit 0 PASS / 2 FAIL / 1 ERROR)
  - governed replicate runs produced **policy verdict PASS** (recorded in `reports/analysis/TASK_0140_BRIEF_REPORT.md`).

## Key Artifacts (In Git)

- Dataset pipeline:
  - `datasets/simplified_wiki_v0/MANIFEST.json`
  - `datasets/simplified_wiki_v0/build_dataset.py`
  - `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`
  - `datasets/simplified_wiki_v0/OUTPUT_POINTER.md`
- Comprehension v0:
  - `docs/spec/COMPREHENSION_V0_CLOZE.md`
  - `experiments/exp_0017_comprehension_v0_cloze/src/{data,train,eval}.py`
  - `docs/spec/COMPREHENSION_V0_PROGRESS_POLICY.md`
  - `tools/analysis/exp0017_progress_policy_eval.py`
- Reports/runbooks:
  - `reports/analysis/TASK_0136_*`, `TASK_0137_*`, `TASK_0138_*`, `TASK_0139_*`, `TASK_0140_*`

## Upgrade Notes / Operational Notes

- Training runs are logged to `logs/exp_0017_comprehension_v0_cloze/` (gitignored).
- The dataset builder and trainer both include refuse-to-run integrity gates; do not bypass them.

