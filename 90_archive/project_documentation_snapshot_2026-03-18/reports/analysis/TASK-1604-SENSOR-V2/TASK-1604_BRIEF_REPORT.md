# TASK-1604 BRIEF REPORT

## Scope
- Implement R1 `ClozeGenome v2` sensor architecture for Phase 2 cloze evolution.
- Replace v1 hash-table context learning with pre-computed bigram/reverse-bigram sensor features.
- Preserve backward compatibility for `--genome_version v0` and `--genome_version v1`.

## Changes
- Added v2 spec section in `docs/CLOZE_GENOME_SPEC.md`.
- Extended task data model with reverse bigram counters and feature helper:
  - `evolution/cloze_symbolic/task.py`
- Added new genome class:
  - `evolution/cloze_symbolic/genome.py` (`ClozeGenomeV2`)
- Added v2 scoring and eval dispatch:
  - `evolution/cloze_symbolic/evaluate.py`
- Added v2 init/mutation (phi-scaled + T-acid apoptosis hook):
  - `evolution/cloze_symbolic/mutate.py`
- Added v2 selection dispatch with golden defaults:
  - `evolution/cloze_symbolic/select.py`
- Added v2 path in main runner (CLI + precomputed features + v2 summary weights):
  - `evolution/cloze_symbolic/run_generations.py`
- Added v2 sweep runner:
  - `scripts/edp1/run_cloze_v2_sensor_sweep.py`
- Updated experiment document:
  - `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`

## Verification (L0)
- Command: `python -m py_compile evolution/cloze_symbolic/task.py evolution/cloze_symbolic/genome.py evolution/cloze_symbolic/evaluate.py evolution/cloze_symbolic/mutate.py evolution/cloze_symbolic/select.py evolution/cloze_symbolic/run_generations.py scripts/edp1/run_cloze_v2_sensor_sweep.py`
- Result: PASS
- Output summary: no syntax errors.

- Command: `python scripts/edp1/run_cloze_exp_0400.py --smoke --seeds 2 --generations 5 --population 20 --out_root results/.tmp_task1604_v0_backcompat`
- Result: PASS
- Output summary: seed_1337 `final_max_accuracy=0.024883359253499222`, seed_1338 `0.028134556574923548` (matches TASK-1602 reference).

- Command: `python -m evolution.cloze_symbolic.run_generations --out_dir results/.tmp_task1604_v1_smoke/seed_1337 --genome_version v1 --top_k_tokens 5 --seed 1337 --generations 10 --population 20`
- Result: PASS
- Output summary: `final_max_accuracy=0.032031648800408374` (matches TASK-1603 reference).

- Command: `python -m evolution.cloze_symbolic.run_generations --out_dir results/.tmp_task1604_v2_smoke/seed_1337 --genome_version v2 --top_k_tokens 5 --seed 1337 --generations 10 --population 20`
- Result: PASS
- Output summary: no NaN/inf; `final_max_accuracy=0.07210311383358857`; `conflict_flag_rate=0.864453125`.

- Command: `python scripts/edp1/run_cloze_v2_sensor_sweep.py --seeds 3 --generations 30 --population 50 --subset_size 20 --out_root results/.tmp_task1604_sweep`
- Result: PASS
- Output summary:
  - `bigram_oracle_exact=true`
  - `frequency_oracle_exact=true`
  - `at_least_one_beats_bigram=true`
  - `best_v2_config=hard_topk8`
  - `best_v2_final_max_accuracy_mean=0.15356682113766282`
  - `v2_vs_v1_delta=+0.10089858589019363`

- Command: `python -c "from evolution.cloze_symbolic.genome import ClozeGenomeV2; g=ClozeGenomeV2(0.0,tuple(0.0 for _ in range(5)),0.0,0.0); print(g.parameter_count())"`
- Result: PASS
- Output summary: `8` (top_k=5 parameter count target met).

- Command: `git diff --name-only`
- Result: PASS
- Output summary: no `evolution/edp1_symbolic/*` files changed.

## Artifacts
- `docs/CLOZE_GENOME_SPEC.md` - v2 sensor architecture spec.
- `evolution/cloze_symbolic/task.py` - reverse bigram counter + feature computation helper.
- `evolution/cloze_symbolic/genome.py` - `ClozeGenomeV2` + oracles + diagnostics methods.
- `evolution/cloze_symbolic/evaluate.py` - v2 scoring + eval dispatch + v2 diagnostics.
- `evolution/cloze_symbolic/mutate.py` - `random_genome_v2`, `mutate_genome_v2`.
- `evolution/cloze_symbolic/select.py` - v2 dispatch with golden defaults.
- `evolution/cloze_symbolic/run_generations.py` - v2 CLI/evolution path and precomputed features.
- `scripts/edp1/run_cloze_v2_sensor_sweep.py` - controlled v2 sweep and oracle checks.
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md` - TASK-1604 section.

## Risks / Limitations
- v2 currently couples strongly to availability/quality of bigram statistics from the selected subset.
- `top_k=8` uses 11 params (above requested `max_parameters_v2=10`), but kept for requested diagnostic comparability against v1 sweep grid.
- Full Phase-2 gate (`N=30, G=50, P=100`) not executed in this task.

## Rollback
- Revert commits for TASK-1604:
  - `git revert <TASK-1604-commit-hash>`
  - `git revert <TASK-1604-log-followup-hash>`
