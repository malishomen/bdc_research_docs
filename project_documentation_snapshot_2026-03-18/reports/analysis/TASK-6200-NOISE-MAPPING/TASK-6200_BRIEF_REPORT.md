# TASK-6200 BRIEF REPORT

## Scope
- Map impact of evaluation-noise regime on emergent cooperative role architecture.
- Full grid execution:
  - `evaluation_samples_per_genome`: `[2,5,10,20,40]`
  - `partners_per_evaluation`: `[2,5,10]`
  - `population_size`: `[32,64,128]`
- Protocol: `45 settings × 20 seeds = 900 runs`, `G=120`, `base_seed=1337`.

## Changes
- Added phase-12 grid runner:
  - `scripts/edp1/run_phase12_noise_mapping.py`
- Added phase-12 test:
  - `tests/test_phase12_noise_mapping.py`
- Added canonical task json:
  - `tasks/TASK-6200-NOISE-REGIME-MAPPING.json`

## Verification (L0)
- Command: `python -m py_compile scripts/edp1/run_phase12_noise_mapping.py tests/test_phase12_noise_mapping.py evolution/coevolution_engine.py`
- Result: PASS

- Command: `pytest -q tests/test_phase7_coevolution.py tests/test_phase12_noise_mapping.py`
- Result: PASS
- Output summary: `3 passed`.

- Command: `python scripts/edp1/run_phase12_noise_mapping.py --base_seed 1337 --seeds_per_setting 20 --generations 120 --evaluation_samples_grid 2,5,10,20,40 --partners_grid 2,5,10 --population_grid 32,64,128 --max_workers 6 --out_root results/noise_mapping`
- Result: PASS
- Output summary:
  - `settings=45`, `total_runs=900`
  - `hypothesis_supported=false`
  - `noise_correlation_max=0.43011708405395804`

## Artifacts
- `results/noise_mapping/per_seed_metrics.csv`
- `results/noise_mapping/grid_summary.csv`
- `results/noise_mapping/role_ratio_surface.csv`
- `results/noise_mapping/noise_architecture_correlation.csv`
- `results/noise_mapping/performance_regions.csv`
- `results/noise_mapping/architecture_phase_diagram.csv`
- `results/noise_mapping/noise_mapping_summary.json`

## Results
- All `45/45` parameter settings completed.
- Role-ratio variation exists (`role_ratio_variation_detected=true`), but:
  - max `|pearson(noise_index -> role_ratio_*)| = 0.4301` (< required `0.6`) -> FAIL
  - architecture regions are not distinct (`predictor-dominant` for all 45 settings) -> FAIL
- Hypothesis verdict:
  - `hypothesis_supported = false`

## Interpretation
- Noise parameters influence ratio magnitudes weakly/moderately, but not enough to explain architecture as distinct noise-governed phases under current oracle/task setup.
- Emergent architecture remained in one attractor class (`predictor-dominant`) across the full grid.

## Risks / Limitations
- Current LandscapeOracle nearest-point mechanism appears to constrain architectural diversity, which can suppress phase separation.
- High computational budget was required even with parallelism (`~5909 sec` wall-clock).

## Rollback
- Revert commits:
  - `git revert <TASK-6200-implementation-hash>`
  - `git revert <TASK-6200-hash-followup-hash>`
