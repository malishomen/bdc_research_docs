# TASK-6100 BRIEF REPORT

## Scope
- Validate hypothesis that TASK-5900 law reflects survival dynamics by injecting survival-pressure scaling in selection-time fitness.
- Compare 4 regimes on full protocol:
  - `baseline_coevolution`
  - `survival_scaled`
  - `variance_only_scaling`
  - `mean_inverse_scaling`
- Use fixed experimental settings: `N=30`, `seeds=1337..1366`, `G=120`, `P=64`, partner sampling `5x10`.

## Changes
- Extended coevolution engine with survival-scaling modes:
  - `evolution/coevolution_engine.py`
  - Modes: `none`, `survival_scaled`, `variance_only`, `mean_inverse`
- Added phase-11 runner:
  - `scripts/edp1/run_phase11_survival_injection.py`
- Added phase-11 test:
  - `tests/test_phase11_survival_injection.py`
- Added canonical task json:
  - `tasks/TASK-6100-SURVIVAL-PRESSURE-INJECTION.json`

## Verification (L0)
- Command: `python -m py_compile evolution/coevolution_engine.py scripts/edp1/run_phase11_survival_injection.py tests/test_phase11_survival_injection.py`
- Result: PASS

- Command: `pytest -q tests/test_phase7_coevolution.py tests/test_phase11_survival_injection.py`
- Result: PASS
- Output summary: `3 passed`.

- Command: `python scripts/edp1/run_phase11_survival_injection.py --seeds 30 --base_seed 1337 --generations 120 --population_size 64 --partners_per_evaluation 5 --evaluation_samples_per_genome 10 --out_root results/survival_injection`
- Result: PASS
- Output summary: all four regimes completed `30/30`; final event `mechanism_confirmed=false`.

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/survival_injection/mechanism_validation.json').read_text(encoding='utf-8')); print(d['mechanism_confirmed'], d['improvements_vs_baseline']['delta_advantage_improvement'], d['improvements_vs_baseline']['positive_seed_fraction_improvement'])"`
- Result: PASS
- Output summary: `False -0.0010761539212286921 -0.033333333333333326`.

## Artifacts
- `results/survival_injection/per_seed_metrics.csv`
- `results/survival_injection/delta_timeseries.csv`
- `results/survival_injection/regime_summary.json`
- `results/survival_injection/performance_comparison.csv`
- `results/survival_injection/stability_metrics.csv`
- `results/survival_injection/mechanism_validation.json`

## Results
- Mean `delta_advantage` by regime:
  - baseline: `0.006364` (CI95 `[0.004116, 0.008612]`)
  - survival_scaled: `0.005288` (CI95 `[0.003113, 0.007463]`)
  - variance_only: `0.005300` (CI95 `[0.003223, 0.007377]`)
  - mean_inverse: `0.006364` (CI95 `[0.004116, 0.008612]`)
- Baseline vs survival_scaled improvements:
  - `delta_advantage_improvement = -0.001076` (threshold `>= +0.01`) -> FAIL
  - `positive_seed_fraction_improvement = -0.0333` (threshold `>= +0.05`) -> FAIL
- Mechanism verdict: `mechanism_confirmed = false`.

## Interpretation
- Survival-pressure injection did not improve cooperative outcomes relative to baseline.
- `mean_inverse_scaling` behaved effectively identical to baseline in aggregate metrics, while `survival_scaled` and `variance_only` degraded both delta and stability.

## Risks / Limitations
- Current scaling uses per-genome score statistics computed from partner-sampling estimates; noisy partner estimates may amplify variance under scaled regimes.
- Oracle-based evaluation keeps plateau near generation 1, so convergence-time differences are weakly informative.

## Rollback
- Revert commits:
  - `git revert <TASK-6100-implementation-hash>`
  - `git revert <TASK-6100-hash-followup-hash>`
