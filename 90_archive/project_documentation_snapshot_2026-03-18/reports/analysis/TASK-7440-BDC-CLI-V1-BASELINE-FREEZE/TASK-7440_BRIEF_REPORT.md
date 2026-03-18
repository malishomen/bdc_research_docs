# TASK-7440 BRIEF REPORT

## Scope
- Freeze current `BDC Designer CLI v1` behavior as a regression baseline.
- Commit benchmark fixtures and golden outputs for v1.
- Document v1 limitations and canonical failure cases.
- Record the known `TextAI_Auto` failure mode as a mandatory calibration gate for v2.

## Changes
- Added baseline runner:
  - `scripts/analysis/run_phase35_freeze_bdc_cli_v1_baseline.py`
- Added committed benchmark fixtures:
  - `tests/data/bdc_cli_v1_baseline/cases.json`
  - `tests/data/bdc_cli_v1_baseline/golden_outputs.json`
- Added regression tests:
  - `tests/test_phase35_freeze_bdc_cli_v1_baseline.py`
- Added v1 limitation documents:
  - `docs/BDC_CLI_V1_LIMITATIONS_AND_GAPS.md`
  - `docs/BDC_CLI_V1_CANONICAL_FAILURE_CASES.md`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase35_freeze_bdc_cli_v1_baseline.py`
- Result: PASS
- Output summary: runner compiles successfully.

- Command: `pytest -q tests/test_phase35_freeze_bdc_cli_v1_baseline.py`
- Result: PASS
- Output summary: `3 passed`; fixture integrity, snapshot regression, and TextAI_Auto failure regression all passed.

- Command: `python scripts/analysis/run_phase35_freeze_bdc_cli_v1_baseline.py --out_root results/bdc_cli_v1_baseline`
- Result: PASS
- Output summary: `golden_case_count=6`, `golden_mismatch_count=0`, `supported=true`.

## Artifacts
- `scripts/analysis/run_phase35_freeze_bdc_cli_v1_baseline.py` — baseline freeze runner.
- `tests/data/bdc_cli_v1_baseline/cases.json` — committed benchmark descriptors for v1 freeze.
- `tests/data/bdc_cli_v1_baseline/golden_outputs.json` — committed golden outputs for v1 regression.
- `tests/test_phase35_freeze_bdc_cli_v1_baseline.py` — phase-35 regression tests.
- `docs/BDC_CLI_V1_LIMITATIONS_AND_GAPS.md` — frozen v1 limitation document.
- `docs/BDC_CLI_V1_CANONICAL_FAILURE_CASES.md` — canonical failure case document.
- `results/bdc_cli_v1_baseline/v1_golden_outputs_manifest.csv` — runtime manifest of golden-case matches.
- `results/bdc_cli_v1_baseline/textai_auto_v1_failure_snapshot.json` — runtime TextAI_Auto failure snapshot.

## Risks / Limitations
- This task intentionally preserves current v1 behavior; it does not attempt to improve the TextAI_Auto result.
- The frozen fixture set is descriptor-level only because v1 itself is descriptor-level.
- Runtime artifacts under `results/bdc_cli_v1_baseline/` are generated for verification and are not committed.

## Rollback
- `git revert <hash>` for the implementation commit.
- `git revert <hash>` for the append-only hash follow-up commit.
