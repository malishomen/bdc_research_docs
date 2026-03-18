# TASK-6500 BRIEF REPORT

## Scope
- Validate causal-law hypothesis:
  - `w_r ≈ C_r / Σ C_r`
  - `C_r` defined via counterfactual intervention fitness drops.
- Inputs:
  - `results/task_structure_mapping/per_seed_metrics.csv`
  - `results/task_structure_mapping/role_ratio_by_task.csv`
- Interventions:
  - `role_ablation`
  - `role_output_randomization`
  - `role_output_permutation`
  - `role_swap_intervention`

## Changes
- Added phase-15 analysis runner:
  - `scripts/analysis/run_phase15_causal_role_analysis.py`
- Added phase-15 test:
  - `tests/test_phase15_causal_law.py`
- Added canonical task JSON:
  - `tasks/TASK-6500-CAUSAL-ROLE-CONTRIBUTION-VALIDATION.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase15_causal_role_analysis.py tests/test_phase15_causal_law.py`
- Result: PASS

- Command: `pytest -q tests/test_phase15_causal_law.py`
- Result: PASS
- Output summary: `1 passed`.

- Command: `python scripts/analysis/run_phase15_causal_role_analysis.py --per_seed_metrics_csv results/task_structure_mapping/per_seed_metrics.csv --role_ratio_by_task_csv results/task_structure_mapping/role_ratio_by_task.csv --out_root results/causal_law`
- Result: PASS
- Output summary:
  - `pearson_correlation=0.9962865817315878`
  - `mean_absolute_error=0.04190526478369999`
  - `rank_consistency=true`
  - `law_confirmed=true`

## Artifacts
- `results/causal_law/intervention_metrics.csv`
- `results/causal_law/causal_contributions.csv`
- `results/causal_law/theoretical_causal_weights.csv`
- `results/causal_law/weight_causal_comparison.csv`
- `results/causal_law/causal_law_validation.json`

## Results
- Law criteria:
  - `pearson >= 0.85` -> PASS (`0.9963`)
  - `MAE <= 0.08` -> PASS (`0.0419`)
  - `rank_consistency == true` -> PASS
- Per-family rank consistency:
  - `predictor_dominant` -> PASS
  - `critic_dominant` -> PASS
  - `aggregator_dominant` -> PASS
  - `symmetric_information` -> PASS
- Final verdict: `law_confirmed = true`.

## Interpretation
- Counterfactual causal-contribution estimation explains emergent role ratios substantially better than the mutual-information formulation from TASK-6400.
- Result supports causal-control interpretation for cooperative role weighting under current task-structure setup.

## Risks / Limitations
- Causal contributions are computed from intervention proxies over aggregate seed-level outputs, not full stepwise internal model traces.
- Role Shapley value is a weighted counterfactual estimate, not exact game-theoretic Shapley over full policy space.

## Rollback
- Revert commits:
  - `git revert <TASK-6500-implementation-hash>`
  - `git revert <TASK-6500-hash-followup-hash>`
