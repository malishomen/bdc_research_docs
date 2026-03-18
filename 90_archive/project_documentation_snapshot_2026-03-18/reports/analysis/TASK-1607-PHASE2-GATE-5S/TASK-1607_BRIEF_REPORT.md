# TASK-1607 BRIEF REPORT

## Scope
- Apply ADR-0008 threshold revision for Phase 2 criterion 1 (5% -> 3% with 95% CI).
- Execute canonical Phase 2 gate re-run with 5-sensor v2 configuration (`N=30`, `G=50`, `P=100`).
- Produce formal PASS/FAIL verdict for Phase 2 under revised criterion set.

## Changes
- Created `decisions/ADR-0008-phase2-threshold-revision.md`.
- Executed 30-seed gate run at `results/edp1_exp0400_cloze_v2_gate_5s/hard_topk8/seed_*` (not in git).
- Aggregated results:
  - `results/edp1_exp0400_cloze_v2_gate_5s/aggregates/phase2_gate_5s_summary.json`
  - `results/edp1_exp0400_cloze_v2_gate_5s/aggregates/phase2_gate_5s_per_seed.csv`
- Updated `docs/project/project_roadmap.md` Phase 2 status.

## Verification (L0)
- Command: 30-seed run
  - `python -m evolution.cloze_symbolic.run_generations --out_dir results/edp1_exp0400_cloze_v2_gate_5s/hard_topk8/seed_<1337..1366> --seed <...> --genome_version v2 --use_skip_bigram --fitness_mode hard --top_k_tokens 8 --population 100 --generations 50 --subset_size 100 --complexity_lambda 0.01 --mutation_sigma 0.25`
- Result: PASS (30/30 seeds complete).
- Command: aggregation (t-CI, df=29)
  - inline python -> `phase2_gate_5s_summary.json` + per-seed CSV
- Result: PASS.

## Gate Statistics (t-CI, df=29)
- `delta_mean = 0.032979093`
- `95% CI(delta) = [0.030865494, 0.035092692]`
- `final_max_accuracy_mean = 0.125242984`
- `best_baseline_mean = 0.092263891`
- `functional_diversity_final_mean = 1.000000000`
- `trajectory_slope_mean = 0.030772193`

## Criteria Verdicts
- Criterion 1 (revised, `lower_CI(delta) >= 0.03`): **PASS** (`lower_CI=0.030865494`)
- Criterion 1 (old 5% reference): **FAIL**
- Criterion 2 (`slope>0` in >=28/30): **PASS** (30/30)
- Criterion 3 (`diversity>0.3` in >=28/30): **PASS** (30/30)

## Kill Criteria Checks
- no_seed_exceeds_baseline: NOT TRIGGERED
- fitness_plateau_before_gen10: NOT TRIGGERED (count=0)
- all_seeds_identical_strategy_proxy: NOT TRIGGERED (unique=30)
- accuracy_below_baseline_plus_1pct_in_gt_25: NOT TRIGGERED (count=0)

## Final Decision
- **Phase 2 Gate = PASS** under ADR-0008 revised threshold.

## Best Seed Snapshot
- seed=1337, delta=0.044027565
- weights: w_bigram=1.184008, w_reverse=1.026286, w_skip=1.117362, w_rev_skip=1.073622

## Per-seed Table
| seed | max_accuracy | baseline | delta | slope(g50-g1) | diversity | w_bigram | w_skip | w_reverse | w_rev_skip |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1337 | 0.132210 | 0.088183 | 0.044028 | 0.029096 | 1.00 | 1.184 | 1.117 | 1.026 | 1.074 |
| 1338 | 0.121790 | 0.087250 | 0.034540 | 0.048656 | 1.00 | 0.874 | 0.895 | 0.973 | 0.977 |
| 1339 | 0.127361 | 0.095718 | 0.031644 | 0.028180 | 1.00 | 1.004 | 0.697 | 1.209 | 0.956 |
| 1340 | 0.124967 | 0.088398 | 0.036569 | 0.019995 | 1.00 | 1.231 | 1.407 | 1.130 | 1.266 |
| 1341 | 0.114247 | 0.083295 | 0.030951 | 0.040358 | 1.00 | 0.589 | 0.704 | 0.566 | 0.687 |
| 1342 | 0.123866 | 0.092286 | 0.031580 | 0.045130 | 1.00 | 1.363 | 1.331 | 1.351 | 1.325 |
| 1343 | 0.114250 | 0.082373 | 0.031876 | 0.038346 | 1.00 | 1.171 | 1.185 | 0.801 | 0.889 |
| 1344 | 0.139559 | 0.095919 | 0.043640 | 0.028895 | 1.00 | 1.253 | 1.301 | 1.366 | 1.376 |
| 1345 | 0.122912 | 0.090319 | 0.032593 | 0.039890 | 1.00 | 0.891 | 1.143 | 0.875 | 1.006 |
| 1346 | 0.129492 | 0.089831 | 0.039661 | 0.035424 | 1.00 | 1.477 | 1.388 | 1.311 | 1.531 |
| 1347 | 0.140581 | 0.111775 | 0.028807 | 0.025488 | 1.00 | 0.824 | 0.555 | 0.733 | 0.732 |
| 1348 | 0.132701 | 0.109647 | 0.023053 | 0.003874 | 1.00 | 0.652 | 0.860 | 0.836 | 0.371 |
| 1349 | 0.128291 | 0.103328 | 0.024963 | 0.005589 | 1.00 | 0.856 | 0.820 | 1.181 | 0.878 |
| 1350 | 0.130097 | 0.090561 | 0.039536 | 0.031877 | 1.00 | 0.948 | 0.971 | 1.189 | 1.302 |
| 1351 | 0.113043 | 0.083424 | 0.029620 | 0.028533 | 1.00 | 0.918 | 1.274 | 1.052 | 0.873 |
| 1352 | 0.118311 | 0.097547 | 0.020764 | 0.016444 | 1.00 | 0.433 | 0.907 | 1.115 | 0.972 |
| 1353 | 0.117656 | 0.084018 | 0.033638 | 0.024962 | 1.00 | 0.733 | 1.074 | 0.707 | 0.786 |
| 1354 | 0.138243 | 0.100452 | 0.037791 | 0.045220 | 1.00 | 1.125 | 1.032 | 1.493 | 1.139 |
| 1355 | 0.129563 | 0.094872 | 0.034691 | 0.021870 | 1.00 | 1.207 | 1.267 | 1.473 | 1.079 |
| 1356 | 0.121185 | 0.091704 | 0.029481 | 0.032889 | 1.00 | 0.734 | 1.208 | 1.150 | 1.161 |
| 1357 | 0.119283 | 0.085765 | 0.033519 | 0.030398 | 1.00 | 0.880 | 0.943 | 1.096 | 1.295 |
| 1358 | 0.116813 | 0.091791 | 0.025022 | 0.023746 | 1.00 | 0.760 | 0.522 | 0.692 | 0.726 |
| 1359 | 0.130646 | 0.092703 | 0.037943 | 0.053092 | 1.00 | 1.029 | 1.258 | 1.105 | 1.085 |
| 1360 | 0.119526 | 0.087268 | 0.032258 | 0.030232 | 1.00 | 1.095 | 0.761 | 1.027 | 1.249 |
| 1361 | 0.132701 | 0.095675 | 0.037026 | 0.043871 | 1.00 | 1.402 | 1.476 | 1.267 | 1.227 |
| 1362 | 0.128050 | 0.090620 | 0.037430 | 0.030459 | 1.00 | 1.078 | 1.046 | 0.951 | 1.011 |
| 1363 | 0.117589 | 0.090593 | 0.026996 | 0.043889 | 1.00 | 1.155 | 1.435 | 1.261 | 0.841 |
| 1364 | 0.122719 | 0.088426 | 0.034293 | 0.021188 | 1.00 | 1.624 | 1.426 | 1.367 | 1.189 |
| 1365 | 0.128424 | 0.091267 | 0.037158 | 0.037429 | 1.00 | 1.294 | 1.366 | 1.367 | 1.195 |
| 1366 | 0.121212 | 0.092907 | 0.028305 | 0.018149 | 1.00 | 0.697 | 1.386 | 1.030 | 1.487 |

## Artifacts
- `decisions/ADR-0008-phase2-threshold-revision.md`
- `reports/analysis/TASK-1607-PHASE2-GATE-5S/TASK-1607_BRIEF_REPORT.md`
- `results/edp1_exp0400_cloze_v2_gate_5s/aggregates/phase2_gate_5s_summary.json` (not in git)
- `results/edp1_exp0400_cloze_v2_gate_5s/aggregates/phase2_gate_5s_per_seed.csv` (not in git)

## Risks / Limitations
- Threshold change is governance-sensitive and must remain traceable to ADR-0008 evidence.
- No evolution code changes were made in TASK-1607.

## Rollback
- `git revert <TASK-1607-commit-hash>`
