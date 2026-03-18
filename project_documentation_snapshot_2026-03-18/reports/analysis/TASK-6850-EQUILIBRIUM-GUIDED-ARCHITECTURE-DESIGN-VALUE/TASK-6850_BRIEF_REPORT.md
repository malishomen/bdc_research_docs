# TASK-6850 BRIEF REPORT

## Scope
- Evaluate practical engineering value of equilibrium-guided architecture design (`A1`) against matched-budget baselines (`A2..A5`) across 6 task families.
- Use fixed governance from prior tasks: no transition-law threshold changes, only comparative engineering utility.

## Changes
- Added runner: `scripts/analysis/run_phase20_equilibrium_guided_architecture_value.py`.
- Added task descriptor: `tasks/TASK-6850-EQUILIBRIUM-GUIDED-ARCHITECTURE-DESIGN-VALUE.json`.
- Added smoke test: `tests/test_phase20_equilibrium_guided_architecture_value.py`.
- Generated runtime artifacts:
  - `results/equilibrium_design_value/baseline_manifest.csv`
  - `results/equilibrium_design_value/raw_benchmark_results.csv`
  - `results/equilibrium_design_value/performance_summary.csv`
  - `results/equilibrium_design_value/robustness_summary.csv`
  - `results/equilibrium_design_value/engineering_value_summary.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase20_equilibrium_guided_architecture_value.py`
- Result: PASS

- Command: `pytest -q tests/test_phase20_equilibrium_guided_architecture_value.py`
- Result: PASS (`1 passed`)

- Command: `python scripts/analysis/run_phase20_equilibrium_guided_architecture_value.py --base_seed 1337 --seeds_per_family 20 --generations 80 --search_budget 20 --out_root results/equilibrium_design_value`
- Result: PASS

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/equilibrium_design_value/engineering_value_summary.json').read_text(encoding='utf-8')); print(d['engineering_value_supported'], d['checks'])"`
- Result: PASS
- Output summary:
  - `engineering_value_supported = false`
  - checks:
    - `wins_on_sample_efficiency_vs_uniform = true`
    - `wins_on_time_to_target_vs_hand_designed = true`
    - `not_dominated_by_budgeted_bruteforce = false`
    - `mean_final_fitness_advantage_vs_uniform_min = false`
    - `robustness_not_worse_than_hand_designed = false`

## Key Metrics
- `A1 mean_final_fitness = 0.1441`
- `A2 mean_final_fitness = 0.0954` (A1 better, but advantage `~0.0487 < 0.05` threshold)
- `A5 mean_final_fitness = 0.1547` (A1 dominated on final fitness)
- `A1 mean_time_to_target = 12.775` vs `A3 = 44.533` (A1 better)
- `A1 seed_variation_std = 0.0574` vs `A3 = 0.0482` (A1 worse robustness by criterion)

## Artifacts
- `scripts/analysis/run_phase20_equilibrium_guided_architecture_value.py`
- `tests/test_phase20_equilibrium_guided_architecture_value.py`
- `tasks/TASK-6850-EQUILIBRIUM-GUIDED-ARCHITECTURE-DESIGN-VALUE.json`
- `results/equilibrium_design_value/engineering_value_summary.json`

## Risks / Limitations
- Benchmark is oracle-based architecture-selection under matched budget (engineering comparison), not a full retraining benchmark per arm.
- Brute-force arm (`A5`) remains strong under current budget and search space; this is the primary reason decision is negative.

## Rollback
- Revert with: `git revert <TASK-6850-commit-hash>`.

