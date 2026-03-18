# TASK-1803 BRIEF REPORT

## Scope
- Execute full Phase 4 exp_0600 run for 2-task MVP collective mode (`cloze + entity`) with fixed protocol:
  - `N=30` seeds (`1337..1366`)
  - `G=100`
  - `P=200`
  - `--collective --genome_version v2 --use_skip_bigram --fitness_mode hard --complexity_lambda 0.01`
- Produce aggregate artifacts with per-seed metrics and 95% CI for cooperative-advantage delta:
  - `delta_i = collective_score_i - max_individual_collective_fitness_i`
- No algorithmic/code-path changes for this run task.

## Changes
- Run artifacts generated (not committed):
  - `results/edp1_exp0600_multirole/seed_<seed>/summary.json`
  - `results/edp1_exp0600_multirole/seed_<seed>/metrics.csv`
  - `results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.json`
  - `results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.csv`
- Documentation/log updates:
  - `reports/analysis/TASK-1803-RUN/TASK-1803_BRIEF_REPORT.md`
  - `AGENTS_LOG.md` (append-only)
  - `WEEKLY_STATUS.md` (append-only)

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: only expected tracked docs/log changes; no results artifacts staged.

- Command: `python -m py_compile evolution/cloze_symbolic/run_generations.py scripts/edp1/run_phase4_multirole.py`
- Result: PASS
- Output summary: compilation successful.

- Command: `python -m evolution.cloze_symbolic.run_generations --collective --genome_version v2 --use_skip_bigram --seed 1337 --population 200 --generations 100 --subset_size 100 --top_k_tokens 8 --fitness_mode hard --complexity_lambda 0.01 --out_dir results/edp1_exp0600_multirole/seed_1337`
- Result: PASS
- Output summary: `summary_written` event produced for seed 1337.

- Command: `python -m evolution.cloze_symbolic.run_generations --collective --genome_version v2 --use_skip_bigram --seed 1366 --population 200 --generations 100 --subset_size 100 --top_k_tokens 8 --fitness_mode hard --complexity_lambda 0.01 --out_dir results/edp1_exp0600_multirole/seed_1366`
- Result: PASS
- Output summary: `summary_written` event produced for seed 1366.

- Command: batched resumable execution (parallel workers) for remaining seeds in `1337..1366` until `summary_count=30`.
- Result: PASS
- Output summary: all 30 seed summaries present.

- Command: `python -c "import json, pathlib; p=pathlib.Path('results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.json'); d=json.loads(p.read_text(encoding='utf-8')); print(d['n_seeds'], d['ci95_low'], d['ci95_high'])"`
- Result: PASS
- Output summary: `30 -0.29990798963571247 -0.2934303683783676`.

## Aggregate Results (N=30)
- `n_seeds`: `30`
- Means:
  - `max_accuracy_mean`: `0.1058925495866`
  - `max_entity_accuracy_mean`: `0.6992309076006801`
  - `collective_score_mean`: `0.40256172859364003`
  - `max_individual_collective_fitness_mean`: `0.6992309076006801`
  - `best_baseline_accuracy_mean`: `0.09226389063999685`
  - `best_entity_baseline_accuracy_mean`: `0.6925225070021864`
- Cooperative-advantage delta (`collective_score - max_individual_collective_fitness`):
  - `mean_delta`: `-0.29666917900704004`
  - `std_delta`: `0.008673692644892683`
  - `se_delta`: `0.0015835923728247897`
  - `95% CI`: `[-0.29990798963571247, -0.2934303683783676]`

## Artifacts
- `results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.json` (not in git)
- `results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.csv` (not in git)
- `reports/analysis/TASK-1803-RUN/TASK-1803_BRIEF_REPORT.md`
- `AGENTS_LOG.md`
- `WEEKLY_STATUS.md`

## Risks / Limitations
- Runtime is high for full protocol (`N=30,G=100,P=200`); completion required resumable batched execution.
- Current cooperative delta definition against `max_individual_collective_fitness` yields negative mean/CI in this run and requires interpretation at Phase 4 gate review.

## Rollback
- For docs/log-only repo changes in this task:
  - `git revert <TASK-1803-RUN-commit-hash>`
