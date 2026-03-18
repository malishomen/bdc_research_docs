# TASK-1501 BRIEF REPORT

## Scope
- Implemented Phase 1 `exp_0300` physics sweep plumbing for EDP1 hidden_rule laboratory line.
- Added explicit complexity-regime switch (`A..E`) and class-lambda support for regime `D`.
- Preserved default behavior: no `--complexity_regime` flag keeps regime `A` (`complexity = sum(|w|)`, `penalty = 0.01 * complexity`).
- No changes to kill-criteria policy files or non-EDP1 subsystems.
- Context references: `docs/project/project_main_doc.md`, `docs/project/project_roadmap.md`.

## Changes
- `evolution/edp1_symbolic/evaluate.py`
  - Added unified complexity regime logic (`A,B,C,D,E`) with:
    - `A`: `complexity = sum(|w|)` (existing behavior via `genome.complexity()`), `penalty = lambda * complexity`.
    - `B`: `complexity = sum(|w|)/K`, `penalty = lambda * complexity`.
    - `C`: `complexity = sum(|w|)/sqrt(K)`, `penalty = lambda * complexity`.
    - `D`: `complexity = sum(|w|)`, `penalty = lambda_class(genome_version) * complexity`.
    - `E`: `complexity` reported, `penalty = 0`, `fitness = accuracy`.
- `evolution/edp1_symbolic/run_generations.py`
  - Added CLI: `--complexity_regime {A,B,C,D,E}` (default `A`), `--lambda_v1`, `--lambda_v1_5`, `--lambda_v2`.
  - Added `complexity_regime` column to `metrics.csv`.
  - Added summary fields: `complexity_regime`, `complexity_lambda`, `lambda_v1`, `lambda_v1_5`, `lambda_v2`.
- `scripts/edp1/run_edp1_sweep.sh`
  - Added pass-through flags for complexity regime and class lambdas.
- `scripts/edp1/aggregate_results.py`
  - Aggregates now carry `genome_version`, `complexity_regime`.
  - Added `required_accuracy_to_beat_v1` and `feasibility_flag` fields in `metrics_agg.csv` (computed when baseline passed).
  - Added sweep mode:
    - `--sweep_root`
    - `--sweep_summary_out`
  - Sweep mode builds summary JSON/CSV with `(regime, genome, feasibility, required_accuracy_to_beat_v1, final metrics)`.
- Added runner:
  - `scripts/edp1/run_complexity_sweep_1501.py` for 15 configs (`A..E x v1/v1_5/v2`) with per-config aggregation + global sweep summary.
  - Docstring explicitly marks hidden_rule usage as laboratory-only.
- Tests:
  - `evolution/edp1_symbolic/tests/test_complexity_regime.py`
  - `scripts/edp1/tests/test_aggregate_complexity_sweep.py`
  - Updated `evolution/edp1_symbolic/tests/test_metrics_schema.py` to include `complexity_regime`.

## Verification (L0)
- Unit/integration tests:
  - Command: `pytest -q evolution/edp1_symbolic/tests/test_metrics_schema.py evolution/edp1_symbolic/tests/test_complexity_regime.py scripts/edp1/tests/test_aggregate_metrics_integrity.py scripts/edp1/tests/test_aggregate_complexity_sweep.py`
  - Result: PASS (`6 passed`).
- R0 default compatibility proof (`A`):
  - Commands:
    - `python -m evolution.edp1_symbolic.run_generations --out_dir results/.tmp_task1501_smoke/default --genome_version v1 --seed 1337 --generations 10 --population 10`
    - `python -m evolution.edp1_symbolic.run_generations --out_dir results/.tmp_task1501_smoke/regimeA --genome_version v1 --seed 1337 --generations 10 --population 10 --complexity_regime A`
    - `python -c "... assert metrics(default)==metrics(A); assert normalized_summary(default)==normalized_summary(A) ..."`
  - Result: PASS (`DEFAULT_A_IDENTICAL_OK`).
- Regime smoke (`B/C/D/E`):
  - Commands:
    - `python -m evolution.edp1_symbolic.run_generations ... --complexity_regime B|C|D|E --generations 5 --population 10`
    - schema check via `python -c` for metrics columns + summary `complexity_regime`.
  - Result: PASS (`REGIMES_BCDE_SMOKE_OK`).
- Sweep smoke (15 configs):
  - Command: `python scripts/edp1/run_complexity_sweep_1501.py --seeds 2 --generations 10 --population 20 --out_root results/.tmp_edp1_exp0300_complexity --summary_out results/.tmp_edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`
  - Result: PASS (all 15 config directories + per-config aggregates + summary JSON/CSV generated).
- Sweep summary schema check:
  - Command: `python -c "... assert len(config_dirs)==15; assert len(summary.records)==15; assert required fields present ..."`
  - Result: PASS (`SWEEP_SMOKE_15_CONFIGS_OK`).

## Artifacts
- `evolution/edp1_symbolic/evaluate.py`
- `evolution/edp1_symbolic/run_generations.py`
- `scripts/edp1/run_edp1_sweep.sh`
- `scripts/edp1/aggregate_results.py`
- `scripts/edp1/run_complexity_sweep_1501.py`
- `evolution/edp1_symbolic/tests/test_complexity_regime.py`
- `scripts/edp1/tests/test_aggregate_complexity_sweep.py`
- `reports/analysis/TASK-1501-COMPLEXITY-SWEEP/TASK-1501_BRIEF_REPORT.md`
- Non-committed smoke outputs:
  - `results/.tmp_task1501_smoke/`
  - `results/.tmp_edp1_exp0300_complexity/`
  - `results/.tmp_edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`

## Risks / Limitations
- Full canonical `N=30, G=100, P=100` sweep over all 15 configurations is compute-heavy; this task validated correctness with smoke execution.
- Regime `C` uses fixed parameter counts (`K`) per genome family; if genome schema changes, `K` mapping must be reviewed.
- Sweep summary computes feasibility using per-regime `v1` baseline from produced sweep artifacts; invalid/missing `v1` runs make feasibility `NaN/False`.

## Rollback
- `git revert <TASK-1501-commit-hash>`
