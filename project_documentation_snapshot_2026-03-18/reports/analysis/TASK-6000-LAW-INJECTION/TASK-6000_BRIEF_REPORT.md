# TASK-6000 BRIEF REPORT

## Scope
- Validate causal effect of law injection across 4 regimes:
  - `baseline_coevolution`
  - `uniform_weights`
  - `risk_law_weights` (`w_r ∝ mu_r / sigma_r^2`)
  - `discovered_law_weights` (`w_r ∝ sigma_r^alpha / mu_r^beta`, TASK-5900 params)
- Run full protocol: `N=30`, `seeds=1337..1366`, `G=120`, `P=64`, partner sampling `5x10`.

## Changes
- Extended coevolution engine with optional fixed-weight injection path:
  - `evolution/coevolution_engine.py`
- Added phase-10 runner:
  - `scripts/edp1/run_phase10_law_injection.py`
- Added tests:
  - `tests/test_phase10_law_injection.py`
  - Regression check retained for phase-7 behavior via `tests/test_phase7_coevolution.py`
- Added canonical task json:
  - `tasks/TASK-6000-LAW-INJECTION-VALIDATION.json`

## Verification (L0)
- Command: `python -m py_compile evolution/coevolution_engine.py scripts/edp1/run_phase10_law_injection.py tests/test_phase10_law_injection.py`
- Result: PASS

- Command: `pytest -q tests/test_phase7_coevolution.py tests/test_phase10_law_injection.py`
- Result: PASS
- Output summary: `3 passed`.

- Command: `python scripts/edp1/run_phase10_law_injection.py --seeds 30 --base_seed 1337 --generations 120 --population_size 64 --partners_per_evaluation 5 --evaluation_samples_per_genome 10 --out_root results/law_injection`
- Result: PASS
- Output summary: all 4 regimes completed at `30/30` seeds; final event emitted with causal verdict.

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/law_injection/causal_validation.json').read_text(encoding='utf-8')); print(d['law_is_causal'], d['improvements_vs_baseline']['delta_advantage_improvement'], d['improvements_vs_baseline']['positive_seed_fraction_improvement'], d['improvements_vs_baseline']['convergence_speed_improvement'])"`
- Result: PASS
- Output summary: `False -0.002365381104051353 -0.09999999999999998 True`.

## Artifacts
- `results/law_injection/per_seed_metrics.csv`
- `results/law_injection/delta_timeseries.csv`
- `results/law_injection/regime_summary.json`
- `results/law_injection/performance_comparison.csv`
- `results/law_injection/stability_metrics.csv`
- `results/law_injection/causal_validation.json`

## Results
- Mean `delta_advantage` by regime:
  - baseline: `0.006364` (CI95 `[0.004116, 0.008612]`)
  - uniform: `0.002991` (CI95 `[0.001436, 0.004547]`)
  - risk law: `0.002130` (CI95 `[0.001230, 0.003031]`)
  - discovered law: `0.003999` (CI95 `[0.001574, 0.006424]`)
- Causal criteria vs baseline:
  - `delta_advantage_improvement >= 0.01` -> FAIL (`-0.002365`)
  - `positive_seed_fraction_improvement >= 0.05` -> FAIL (`-0.10`)
  - `convergence_speed_improvement` -> PASS (`true`)
- Final decision: `law_is_causal = false`.

## Risks / Limitations
- Injected fixed-weight regimes intentionally suppress role-ratio evolution dynamics; this isolates weight-law effect but may underrepresent adaptive role interactions.
- Plateau metric saturates quickly (`generation_to_plateau ≈ 1`) in this oracle-driven setup, so convergence comparison is mainly informed by slope proxy.

## Rollback
- Revert commits:
  - `git revert <TASK-6000-implementation-hash>`
  - `git revert <TASK-6000-hash-followup-hash>`
