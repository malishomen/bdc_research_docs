# TASK-7540 BRIEF REPORT

## Scope
- Benchmark BDC CLI v2 against v1 and empirical winners on the committed real-case suite.
- Use the benchmark verdict as the release gate for task 7550.

## Changes
- Added committed benchmark fixtures:
  - `tests/data/bdc_cli_v2_benchmark/*.json`
  - `tests/data/bdc_cli_v2_benchmark/benchmark_manifest.json`
- Added benchmark runner:
  - `scripts/analysis/run_phase45_bdc_real_case_benchmark_suite.py`
- Added benchmark test:
  - `tests/test_phase45_bdc_real_case_benchmark_suite.py`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase45_bdc_real_case_benchmark_suite.py`
- Result: PASS
- Output summary: benchmark runner compiles successfully.

- Command: `pytest -q tests/test_phase45_bdc_real_case_benchmark_suite.py`
- Result: PASS
- Output summary: `1 passed`; benchmark runner produces a positive verdict and explicitly confirms TextAI correction.

- Command: `python scripts/analysis/run_phase45_bdc_real_case_benchmark_suite.py --out_root results/bdc_cli_v2_benchmark`
- Result: PASS
- Output summary: `supported=true`; `v2_better_case_count=5` over 5 benchmark cases.

## Artifacts
- `tests/data/bdc_cli_v2_benchmark/benchmark_manifest.json` — benchmark manifest.
- `tests/data/bdc_cli_v2_benchmark/*.json` — committed benchmark case packets.
- `scripts/analysis/run_phase45_bdc_real_case_benchmark_suite.py` — phase-45 benchmark runner.
- `tests/test_phase45_bdc_real_case_benchmark_suite.py` — benchmark regression test.
- `results/bdc_cli_v2_benchmark/agreement_summary.csv` — runtime agreement matrix.
- `results/bdc_cli_v2_benchmark/v1_vs_v2_comparison.csv` — runtime comparison matrix.
- `results/bdc_cli_v2_benchmark/benchmark_verdict.json` — release-gate verdict.

## Risks / Limitations
- The benchmark suite is committed and deterministic, but still curated rather than external-world live traffic.
- v1 variant agreement is intentionally weak because v1 has no variant-level reasoning.
- Release should still preserve v1 as fallback rather than hard-replacing it.

## Rollback
- `git revert <hash>` for the benchmark-suite implementation commit.
- `git revert <hash>` for the append-only hash follow-up commit.
