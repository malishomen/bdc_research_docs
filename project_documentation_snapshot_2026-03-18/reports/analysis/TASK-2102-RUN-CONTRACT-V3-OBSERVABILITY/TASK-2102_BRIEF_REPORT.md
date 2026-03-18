# TASK-2102 BRIEF REPORT

## Scope
- Upgrade applied run contract observability from manifest-list (`v2`) to row-level index (`v3`).
- Add contract validator for run-index row fields and manifest consistency.

## Changes
- Updated `scripts/applied/run_applied_matrix.py`:
  - Added captured stdout/stderr logs per run (`run_stdout.log`, `run_stderr.log`).
  - Added `error_signature` extraction and storage in run manifest.
  - Added row-level run table in run-index with required fields:
    `seed/pilot/variant/return_code/requested_device/resolved_device/fallback_detected/error_signature/manifest_path`.
  - Upgraded run-index schema to `run-index-v3` and writes both `run_index_v2.json` (compat filename) and `run_index_v3.json`.
- Updated `scripts/applied/replay_from_manifest.py`:
  - Added `--run_index` mode to validate `run-index-v3` contract row-by-row.
  - Kept backward-compatible `--manifest` replay mode.
- Updated `scripts/analysis/applied_aggregate_exp0700.py`:
  - Synced schema to `exp0700-aggregate-v2`.
  - Added `error_signature` propagation into per-seed pair rows.

## Verification (L0)
- Command: `python -m py_compile scripts/applied/run_applied_matrix.py scripts/applied/replay_from_manifest.py scripts/analysis/applied_aggregate_exp0700.py`
- Result: PASS

- Command: `python scripts/applied/run_applied_matrix.py --level smoke --out_root results/.tmp_task2102 --base_seed 1337 --seeds 1 --pilots all`
- Result: PASS
- Output summary: `{"event":"applied_matrix_done","level":"smoke","runs":4,"failure_count":0}`.

- Command: `python scripts/applied/replay_from_manifest.py --run_index results/.tmp_task2102/smoke/aggregates/run_index_v3.json`
- Result: PASS
- Output summary: `run_index_v3_contract_ok`, `rows=4`, `missing_manifest_paths=0`.

## Artifacts
- `scripts/applied/run_applied_matrix.py` - row-level contract v3 + error signatures.
- `scripts/applied/replay_from_manifest.py` - validator mode for run-index v3.
- `scripts/analysis/applied_aggregate_exp0700.py` - aggregate schema sync with error-signature fields.
- `reports/analysis/TASK-2102-RUN-CONTRACT-V3-OBSERVABILITY/TASK-2102_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- Error signatures are pattern-based heuristics; unknown signatures are recorded as `unknown_error`.
- Existing historical run-index files remain `v2`; validator expects `v3` when invoked in `--run_index` mode.

## Rollback
- Revert with: `git revert <TASK-2102_commit_hash>`
