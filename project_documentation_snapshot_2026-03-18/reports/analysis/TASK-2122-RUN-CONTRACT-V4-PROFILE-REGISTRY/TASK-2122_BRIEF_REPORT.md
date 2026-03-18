# TASK-2122 BRIEF REPORT

## Scope
- Implement run contract v4 for EXP-0700 with immutable GPU profile registry.
- Preserve backward-compatible legacy mode (`run-index-v3`, legacy overrides).

## Changes
- Added GPU profile registry:
  - `configs/applied/gpu_profile_registry_v4.json`
- Updated runners/contracts:
  - `scripts/applied/run_applied_matrix.py`
  - `scripts/applied/replay_from_manifest.py`
  - `scripts/analysis/applied_aggregate_exp0700.py`
  - `scripts/analysis/task2112_protocol_equivalence_audit.py`
- Added regression test:
  - `tests/test_exp0700_run_contract_v4.py`

## Verification (L0)
- Command: `python -m py_compile scripts/applied/run_applied_matrix.py scripts/applied/replay_from_manifest.py scripts/analysis/task2112_protocol_equivalence_audit.py`
- Result: PASS

- Command: `pytest -q tests/test_exp0700_run_contract_v4.py`
- Result: PASS (`3 passed`)

- Command: `python scripts/applied/run_applied_matrix.py --help`
- Result: PASS
- Output summary: new flags `--gpu_profile_id` and `--gpu_profile_registry` are exposed.

## Artifacts
- `configs/applied/gpu_profile_registry_v4.json` - pre-registered baseline/optimized GPU profiles and hard fairness checklist.
- `scripts/applied/run_applied_matrix.py` - registry-backed v4 mode (`run-index-v4`, `run-manifest-v3`) + legacy compatibility.
- `scripts/applied/replay_from_manifest.py` - row-level validation for `run-index-v3` and `run-index-v4`.
- `scripts/analysis/applied_aggregate_exp0700.py` - supports both manifest versions.
- `scripts/analysis/task2112_protocol_equivalence_audit.py` - two-level fairness audit (`critical` vs `advisory`).
- `tests/test_exp0700_run_contract_v4.py` - contract and registry regression tests.

## Risks / Limitations
- `run-index-v4` is consumed by updated tooling only; old external parsers expecting strictly v3 may require update.
- This task does not execute diagnostic runs; runtime validation is in TASK-2123.

## Rollback
- Revert with: `git revert <TASK-2122_commit_hash>`
