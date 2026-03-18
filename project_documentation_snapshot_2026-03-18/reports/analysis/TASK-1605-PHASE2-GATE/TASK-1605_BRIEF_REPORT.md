# TASK-1605 BRIEF REPORT

## Scope
- Run canonical Phase 2 gate experiment for cloze evolution with fixed TASK-1604 best config: `v2 hard_topk8`, `N=30`, `G=50`, `P=100`.
- Perform formal PASS/FAIL evaluation against roadmap criteria with L0 evidence.
- No code changes; run + analysis + documentation only.

## Changes
- Executed 30-seed gate run into: `results/edp1_exp0400_cloze_v2_gate/hard_topk8/seed_*`.
- Produced aggregate artifacts:
  - `results/edp1_exp0400_cloze_v2_gate/aggregates/phase2_gate_summary.json`
  - `results/edp1_exp0400_cloze_v2_gate/aggregates/phase2_gate_per_seed.csv`
- Updated Phase 2 experiment document (`docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`).

## Verification (L0)
- Command: `python -m evolution.cloze_symbolic.run_generations --out_dir results/edp1_exp0400_cloze_v2_gate/hard_topk8/seed_<seed> --seed <1337..1366> --genome_version v2 --fitness_mode hard --top_k_tokens 8 --generations 50 --population 100 --subset_size 100 --complexity_lambda 0.01 --mutation_sigma 0.25`
- Result: PASS (30/30 seeds completed with `summary.json` + `metrics.csv`).
- Command: aggregation script (inline python) over all 30 seed outputs.
- Result: PASS (summary and per-seed CSV generated).
- Command: `git diff --name-only | rg "^evolution/edp1_symbolic/"`
- Result: PASS (no changes in `evolution/edp1_symbolic`).

## Methodology Note (corrected criterion #1)
- Criterion #1 is computed on per-seed deltas, not difference of means:
  - `delta_i = final_max_accuracy_i - best_baseline_accuracy_i`
  - 95% CI is computed over `delta_i` across 30 seeds.
  - PASS condition: `lower_CI(delta) >= 0.05`.

## Gate Statistics
- `final_max_accuracy_mean`: 0.116007758 (95% CI [0.113367337, 0.118648180])
- `best_baseline_mean`: 0.092263891 (95% CI [0.089753453, 0.094774329])
- `delta_mean`: 0.023743867 (95% CI [0.022389615, 0.025098120])
- `final_max_fitness_mean`: 0.112112289
- `functional_diversity_final_mean`: 0.998333333
- `trajectory_slope_mean` (acc g50-g1): 0.033716494

## Criteria Evaluation
- Criterion 1 (`lower_CI(delta) >= 0.05`): **FAIL** (`lower_CI=0.022389615`)
- Criterion 2 (slope > 0 in >=27/30): **PASS** (`30/30`)
- Criterion 3 (diversity > 0.3 in >=27/30): **PASS** (`30/30`)

## Kill Criteria Checks
- No seed exceeds baseline: NOT TRIGGERED
- Fitness plateau before generation 10: NOT TRIGGERED (non-positive early slope seeds: 0)
- All seeds identical strategy: NOT TRIGGERED (unique signatures: 30)
- Accuracy < baseline +1% in >25/30: NOT TRIGGERED (count: 0)

## Per-seed Results (N=30)
| seed | final_max_accuracy | baseline_bigram | delta | slope(g50-g1) | diversity_final | w_bigram | w_freq | w_reverse |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1337 | 0.119321 | 0.088183 | 0.031138 | 0.040965 | 1.00 | 0.990 | -1.101 | 1.020 |
| 1338 | 0.109776 | 0.087250 | 0.022526 | 0.031686 | 1.00 | 1.670 | -0.171 | 1.085 |
| 1339 | 0.121379 | 0.095718 | 0.025661 | 0.039043 | 0.99 | 2.003 | 0.281 | 1.646 |
| 1340 | 0.113260 | 0.088398 | 0.024862 | 0.027624 | 1.00 | 1.520 | -0.020 | 1.356 |
| 1341 | 0.106509 | 0.083295 | 0.023213 | 0.024882 | 1.00 | 1.918 | -0.396 | 2.134 |
| 1342 | 0.113624 | 0.092286 | 0.021338 | 0.025072 | 1.00 | 1.756 | -0.333 | 1.961 |
| 1343 | 0.105728 | 0.082373 | 0.023355 | 0.032507 | 1.00 | 1.238 | -0.442 | 0.867 |
| 1344 | 0.126154 | 0.095919 | 0.030235 | 0.041704 | 0.99 | 1.533 | 0.073 | 2.007 |
| 1345 | 0.113832 | 0.090319 | 0.023512 | 0.011351 | 1.00 | 1.484 | 0.124 | 1.971 |
| 1346 | 0.117288 | 0.089831 | 0.027458 | 0.035593 | 1.00 | 1.916 | -0.361 | 2.292 |
| 1347 | 0.136201 | 0.111775 | 0.024426 | 0.040489 | 1.00 | 1.560 | 0.172 | 1.530 |
| 1348 | 0.127276 | 0.109647 | 0.017629 | 0.025959 | 1.00 | 1.096 | 0.152 | 1.019 |
| 1349 | 0.121709 | 0.103328 | 0.018381 | 0.039742 | 1.00 | 1.409 | -0.126 | 1.677 |
| 1350 | 0.118383 | 0.090561 | 0.027822 | 0.050687 | 1.00 | 1.358 | -1.083 | 1.700 |
| 1351 | 0.103125 | 0.083424 | 0.019701 | 0.025000 | 1.00 | 1.133 | -0.607 | 1.213 |
| 1352 | 0.113852 | 0.097547 | 0.016304 | 0.031773 | 1.00 | 1.332 | -0.079 | 1.490 |
| 1353 | 0.109285 | 0.084018 | 0.025266 | 0.031355 | 1.00 | 1.537 | 0.446 | 1.623 |
| 1354 | 0.128714 | 0.100452 | 0.028262 | 0.033592 | 0.99 | 1.696 | 0.295 | 2.074 |
| 1355 | 0.121267 | 0.094872 | 0.026395 | 0.053092 | 0.99 | 2.078 | 0.149 | 1.940 |
| 1356 | 0.112148 | 0.091704 | 0.020444 | 0.029333 | 0.99 | 1.641 | -0.004 | 1.451 |
| 1357 | 0.109920 | 0.085765 | 0.024155 | 0.018456 | 1.00 | 1.304 | 0.068 | 1.306 |
| 1358 | 0.109664 | 0.091791 | 0.017873 | 0.027193 | 1.00 | 0.946 | -0.219 | 0.868 |
| 1359 | 0.118555 | 0.092703 | 0.025851 | 0.030577 | 1.00 | 2.126 | -0.578 | 2.334 |
| 1360 | 0.111890 | 0.087268 | 0.024622 | 0.033816 | 1.00 | 1.528 | -0.379 | 1.789 |
| 1361 | 0.121344 | 0.095675 | 0.025669 | 0.048071 | 1.00 | 1.154 | -0.198 | 1.345 |
| 1362 | 0.117745 | 0.090620 | 0.027125 | 0.040915 | 1.00 | 1.446 | 1.083 | 1.967 |
| 1363 | 0.110301 | 0.090593 | 0.019709 | 0.028486 | 1.00 | 2.084 | -0.424 | 1.739 |
| 1364 | 0.113166 | 0.088426 | 0.024740 | 0.032333 | 1.00 | 1.836 | 0.267 | 1.820 |
| 1365 | 0.116762 | 0.091267 | 0.025495 | 0.041904 | 1.00 | 2.063 | 0.210 | 2.360 |
| 1366 | 0.112055 | 0.092907 | 0.019148 | 0.038295 | 1.00 | 1.408 | -0.019 | 1.521 |

## Artifacts
- `results/edp1_exp0400_cloze_v2_gate/hard_topk8/seed_*/summary.json` - per-seed run summaries (not in git).
- `results/edp1_exp0400_cloze_v2_gate/hard_topk8/seed_*/metrics.csv` - per-generation metrics (not in git).
- `results/edp1_exp0400_cloze_v2_gate/aggregates/phase2_gate_summary.json` - gate aggregation and criteria verdicts (not in git).
- `results/edp1_exp0400_cloze_v2_gate/aggregates/phase2_gate_per_seed.csv` - tabular per-seed metrics (not in git).

## Risks / Limitations
- Phase 2 gate is **FAIL** because Criterion 1 is not met at CI lower bound.
- Model improves over baselines (+2.37% mean delta) but not to required +5% absolute margin.
- Next iteration should target stronger signal combination or richer sensor channels before re-running gate.

## Rollback
- Documentation-only rollback: `git revert <TASK-1605-commit-hash>`.
