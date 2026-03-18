# TASK-6700 BRIEF REPORT

## Scope
- Validate phase-17 hypothesis:
  - role-weight dynamics follow replicator form `Δw_r ≈ w_r (C_r − mean(C))`.
- Setup:
  - families: `predictor_dominant`, `symmetric_information`, `critic_dominant`, `aggregator_dominant`
  - `N=20` seeds per family, `G=80`, `P=64`, partners=`5`, eval_samples=`10`.
- Data collected:
  - role weights by generation
  - observed `Δw`
  - causal contributions per family
  - replicator-fit diagnostics
  - Lyapunov curve

## Changes
- Added phase-17 runner:
  - `scripts/analysis/run_phase17_gradient_dynamics.py`
- Added phase-17 test:
  - `tests/test_phase17_causal_dynamics.py`
- Added canonical task JSON:
  - `tasks/TASK-6700-CAUSAL-GRADIENT-DYNAMICS.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase17_gradient_dynamics.py tests/test_phase17_causal_dynamics.py`
- Result: PASS

- Command: `pytest -q tests/test_phase17_causal_dynamics.py`
- Result: PASS
- Output summary: `1 passed`.

- Command: `python scripts/analysis/run_phase17_gradient_dynamics.py --family_defs_json tasks/synthetic/task_family_definitions.json --synthetic_inputs_root results/task_structure_mapping/synthetic_inputs --base_seed 1337 --seeds_per_family 20 --generations 80 --population_size 64 --partners_per_evaluation 5 --evaluation_samples_per_genome 10 --out_root results/causal_dynamics`
- Result: PASS (execution completed)
- Output summary:
  - `pearson_delta_fit_overall=0.17167555409853724`
  - `pearson_delta_fit_min_group=-0.7533369643751755`
  - `lyapunov_monotonic=false`
  - `replicator_confirmed=false`

## Artifacts
- `results/causal_dynamics/weight_dynamics.csv`
- `results/causal_dynamics/replicator_fit.csv`
- `results/causal_dynamics/lyapunov_curve.csv`
- `results/causal_dynamics/dynamics_validation.json`

## Results
- Criteria:
  - `pearson_delta_fit_min >= 0.9` -> FAIL (`-0.7533`)
  - `lyapunov_monotonic == true` -> FAIL (`false`)
- Family-level notes:
  - multiple group fits are moderate (`~0.58 .. 0.74`), but not near required threshold.
  - one strong negative group correlation observed (`aggregator_dominant/predictor`).
  - Lyapunov monotonicity violated in all families (increasing steps present).
- Final verdict:
  - `replicator_confirmed = false` (hypothesis not supported under current setup).

## Risks / Limitations
- Causal contribution proxy is family-level constant (from task causal structure), while evolutionary updates include stochastic partner-sampling noise.
- Replicator form may require additional terms (noise/selection-temperature coupling) to match observed dynamics.

## Rollback
- Revert commits:
  - `git revert <TASK-6700-implementation-hash>`
  - `git revert <TASK-6700-hash-followup-hash>`
