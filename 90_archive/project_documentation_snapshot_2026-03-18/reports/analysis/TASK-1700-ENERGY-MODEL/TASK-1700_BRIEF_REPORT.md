# TASK-1700 BRIEF REPORT

## Scope
- Execute full Phase 3 standard sweep `exp_0500` using frozen TASK-1700 code.
- Config grid: `3 budgets x 3 cost functions = 9 configs`, `N=10` seeds each.
- Validate Phase 3 success/kill criteria from `KILL_CRITERIA.yaml` and collect FFT/phi diagnostics.

## Execution
- Command:
  - `python scripts/edp1/run_energy_sweep.py --level standard --seeds 10 --base_seed 1337 --out_root results/edp1_exp0500_energy`
- Effective ladder level (`standard`): `P=89`, `G=55`
- Total runs completed: `90/90`
- Resume behavior used due to long runtime timeouts; final completion confirmed.

## Verification (L0)
- Aggregate file present:
  - `results/edp1_exp0500_energy/aggregates/energy_sweep_summary.json`
- Verified per-config fields:
  - `delta_mean`, `alive_ratio_mean`, `complexity_variance_mean`
  - `criteria` (4 checks), `kill_checks` (4 checks), `phase3_pass`
  - `spectral_entropy_mean`, `stagnation_count`

## 9-Config Comparison

| config_name | delta_mean | alive_ratio_mean | complexity_variance_mean | phase3_pass |
|---|---:|---:|---:|---|
| E0.5_linear | 0.036043 | 0.004494 | 0.014296 | false |
| E0.5_sublinear | 0.036057 | 0.000000 | 0.011440 | false |
| E0.5_step | 0.036031 | 0.000000 | 0.009552 | false |
| E1.0_linear | 0.036031 | 0.928090 | 0.009552 | false |
| E1.0_sublinear | 0.036031 | 0.928090 | 0.009552 | false |
| E1.0_step | 0.036031 | 0.000000 | 0.009552 | false |
| E2.0_linear | 0.036031 | 1.000000 | 0.009552 | false |
| E2.0_sublinear | 0.036031 | 1.000000 | 0.009552 | false |
| E2.0_step | 0.036057 | 0.000000 | 0.011440 | false |

## Criteria & Kill Summary
- Configs passing all 4 success criteria: `0/9`.
- Kill criteria triggered: `YES` (mass extinction triggered in 5 configs).
- Spectral diagnostics: stagnation majority in `9/9` configs (`stagnation_count=10/10` for each config).

## Best Config
- Best among passing configs: none (no passing configs).
- Highest `delta_mean` overall (diagnostic only): tie between `E0.5_sublinear` and `E2.0_step` at `0.036057`.

## phi_balance Diagnostics (final-generation means)
- E0.5_linear: `phi_balance=0.844735`, `phi_deviation=0.229925`
- E0.5_sublinear: `phi_balance=0.769357`, `phi_deviation=0.164613`
- E0.5_step: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E1.0_linear: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E1.0_sublinear: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E1.0_step: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E2.0_linear: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E2.0_sublinear: `phi_balance=0.773372`, `phi_deviation=0.167220`
- E2.0_step: `phi_balance=0.769357`, `phi_deviation=0.164613`

## Outcome
- Phase 3 standard sweep result: **FAILURE** for current success criteria.
- Main blockers:
  - `stable_complexity_distribution` not met across all configs,
  - `high_complexity_persistence` not met across all configs,
  - extinction instability in several configs.

## Artifacts
- `results/edp1_exp0500_energy/aggregates/energy_sweep_summary.json` (not in git)
- `results/edp1_exp0500_energy/aggregates/energy_sweep_summary.csv` (not in git)
- `reports/analysis/TASK-1700-ENERGY-MODEL/TASK-1700_BRIEF_REPORT.md`

## Rollback
- Report/log-only rollback for run task:
  - `git revert <TASK-1700-RUN-commit-hash>`
