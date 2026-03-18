# TASK-1602 BRIEF REPORT

## Scope
- Implemented R1 search-signal fix for `evolution/cloze_symbolic`:
  - soft fitness mode (`fitness_mode=soft`) with numerically stable softmax,
  - configurable `top_k_tokens` dimensionality sweep.
- Preserved backward compatibility:
  - default `fitness_mode=hard`,
  - default `top_k_tokens=16`,
  - no changes to `evolution/edp1_symbolic/*`.

## Changes
- `evolution/cloze_symbolic/evaluate.py`
  - Added stable softmax-based scoring path.
  - Added `soft_accuracy` in `EvalResult`.
  - Added `fitness_mode hard|soft` in `evaluate_cloze_genome`.
- `evolution/cloze_symbolic/run_generations.py`
  - Added CLI `--fitness_mode hard|soft` (default `hard`).
  - Extended `metrics.csv` with `mean/max_soft_accuracy`.
  - Extended `summary.json` with `fitness_mode`, `max/mean_soft_accuracy`.
- `scripts/edp1/run_cloze_search_fix_sweep.py`
  - Added controlled 4-config sweep:
    - `{hard,soft} x {top_k=4,16}`, `N=3,G=30,P=50`.
  - Produces:
    - `results/.tmp_task1602_sweep/aggregates/sweep_summary.json`
    - `results/.tmp_task1602_sweep/aggregates/sweep_summary.csv`
- Docs:
  - `docs/CLOZE_GENOME_SPEC.md` (soft fitness + top_k configurability).
  - `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md` (Search Signal Fix section).

## Verification (L0)
- Backward compatibility (hard mode):
  - Command: `python scripts/edp1/run_cloze_exp_0400.py --smoke --seeds 2 --generations 5 --population 20 --out_root results/.tmp_task1602_backcompat`
  - Command: python assert script comparing seed_1337 output to TASK-1600 known values.
  - Result: PASS (`BACKCOMPAT_HARD_OK`).
- Soft mode smoke:
  - Command: `python -m evolution.cloze_symbolic.run_generations --out_dir results/.tmp_task1602_soft_smoke/seed_1337 --seed 1337 --generations 10 --population 20 --subset_size 30 --fitness_mode soft --top_k_tokens 4`
  - Command: python finite-check script for metrics and summary.
  - Result: PASS (`SOFT_SMOKE_FINITE_OK`), no NaN/inf.
- Controlled sweep:
  - Command: `python scripts/edp1/run_cloze_search_fix_sweep.py --seeds 3 --generations 30 --population 50 --out_root results/.tmp_task1602_sweep`
  - Result: PASS, 4 configs completed, summary JSON/CSV generated.
- Monotonicity check for best config (`hard_topk4`):
  - Command: python check over `results/.tmp_task1602_sweep/hard_topk4/seed_*/metrics.csv` verifying `max_fitness[g] >= max_fitness[g-1]`.
  - Result: PASS (all 3 seeds monotonic in best config).
- Isolation check:
  - Command: `git diff --name-only | rg "evolution/edp1_symbolic"`
  - Result: PASS (no matches).

## Sweep Results

| config | final_max_accuracy_mean | vs frequency_baseline | vs bigram_baseline | trajectory_slope_mean |
|---|---:|---:|---:|---:|
| hard_topk4 | 0.044267 | +0.016806 | -0.040392 | +0.004877 |
| hard_topk16 | 0.042739 | +0.015279 | -0.130085 | +0.013369 |
| soft_topk4 | 0.041810 | +0.014349 | -0.042849 | +0.006853 |
| soft_topk16 | 0.039975 | +0.012514 | -0.132849 | +0.011665 |

Derived decision:
- `at_least_one_meets_frequency = true` (all configs pass this threshold in mean).
- Best config by binary `final_max_accuracy_mean`: `hard_topk4`.

## Success Criteria Mapping
- Criterion: at least one config reaches/exceeds frequency baseline.
  - Status: PASS.
- Criterion: fitness trajectory grows in best config.
  - Status: PASS (monotonic `max_fitness` across generations in all 3 seeds for `hard_topk4`).
- Bigram baseline superiority:
  - Still NOT achieved by any tested config.

## Artifacts
- `evolution/cloze_symbolic/evaluate.py`
- `evolution/cloze_symbolic/run_generations.py`
- `scripts/edp1/run_cloze_search_fix_sweep.py`
- `docs/CLOZE_GENOME_SPEC.md`
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`
- `reports/analysis/TASK-1602-CLOZE-SEARCH-FIX/TASK-1602_BRIEF_REPORT.md`
- Runtime-only (not committed):
  - `results/.tmp_task1602_backcompat/`
  - `results/.tmp_task1602_soft_smoke/`
  - `results/.tmp_task1602_sweep/`

## Risks / Limitations
- Sweep is diagnostic-scale (`N=3`), not canonical Phase-2 gate run.
- Improvement over frequency baseline does not imply readiness against stronger bigram baseline.
- Recommendation for next gate run is data-dependent and should be revalidated at `N=30,G=50,P=100`.

## Rollback
- `git revert <TASK-1602-commit-hash>`
