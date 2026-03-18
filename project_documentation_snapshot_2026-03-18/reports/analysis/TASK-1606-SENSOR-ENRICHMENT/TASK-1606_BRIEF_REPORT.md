# TASK-1606 BRIEF REPORT

## Scope
- Run TASK-1606 enrichment diagnostics on implemented v2 skip-sensor code.
- Verify strict backward compatibility before sweep.
- Produce per-arm `delta_i` statistics and decision matrix outcome.

## Changes
- Executed only test/analysis actions (no additional code changes in this run task).
- Updated experiment documentation with final N=10 diagnostic results.
- Updated this report with per-arm mean/CI and decision matrix.

## Verification (L0)
- Command: `python -m evolution.cloze_symbolic.run_generations --genome_version v2 --fitness_mode hard --top_k_tokens 8 --population 100 --generations 50 --seed 1337 --out_dir results/.tmp_task1606_backcompat_verify`
- Result: PASS
- Output summary: exact match vs TASK-1605 seed 1337:
  - `final.max_accuracy = 0.11932108218478815`
  - `final.mean_accuracy = 0.11631955079122001`

- Command: `python scripts/edp1/run_cloze_v2_enrichment_sweep.py`
- Result: PASS (completed after resumed reruns for timed-out long jobs)
- Output summary: 4 arms x 10 seeds completed in `results/edp1_exp0400_cloze_v2_enrichment/`.

- Command: inline aggregation to `results/edp1_exp0400_cloze_v2_enrichment/aggregates/enrichment_summary_t_ci.json`
- Result: PASS
- Output summary: t-based 95% CI over per-seed `delta_i` for each arm.

- Command: oracle/sensor checks (inline python)
- Result: PASS
- Output summary:
  - `bigram_oracle_delta = 0.0`
  - skip-sensor wiring changes predictions (`315/1000` differ vs pure bigram oracle)

- Command: smoke `--use_skip_bigram`
  - `python -m evolution.cloze_symbolic.run_generations --out_dir results/.tmp_task1606_use_skip_smoke --seed 1337 --genome_version v2 --use_skip_bigram --top_k_tokens 8 --dry_run`
- Result: PASS

## Results (N=10, seeds 1337..1346)
Per-seed metric: `delta_i = final_max_accuracy_i - bigram_baseline_i`.
CI method: 95% t-distribution (`df=9`, `t*=2.262157`).

| Arm | Sensors | G | delta_mean | 95% CI(delta) |
|---|---|---:|---:|---:|
| arm_3s_G50 | 3-sensor | 50 | 0.025330 | [0.022968, 0.027692] |
| arm_5s_G50 | 5-sensor | 50 | 0.035708 | [0.032088, 0.039328] |
| arm_3s_G100 | 3-sensor | 100 | 0.025678 | [0.023292, 0.028064] |
| arm_5s_G100 | 5-sensor | 100 | 0.035823 | [0.032309, 0.039337] |

Decision matrix outcome:
- `A=false`, `B=false`, `C=false`, `D=true`

Interpretation:
- Skip-sensor enrichment gives a clear delta lift (~+0.0104 absolute vs 3-sensor at same G).
- Increasing G 50->100 gives minimal additional gain at current setup.
- No arm reaches `lower_CI(delta) >= 0.05`.

Best arm and weights:
- Best arm by `delta_mean`: `arm_5s_G100`
- Best seed in that arm: `1337`
- Weights: `w_bigram=1.0842496534129957`, `w_reverse_bigram=0.8695217987637647`, `w_skip_bigram=1.0130810045801575`, `w_rev_skip_bigram=1.0604738651870824`

## Artifacts
- `results/edp1_exp0400_cloze_v2_enrichment/aggregates/enrichment_summary.json` (script aggregate, not in git)
- `results/edp1_exp0400_cloze_v2_enrichment/aggregates/enrichment_summary_t_ci.json` (t-CI aggregate, not in git)
- `results/edp1_exp0400_cloze_v2_enrichment/aggregates/enrichment_summary.csv` (not in git)
- `reports/analysis/TASK-1606-SENSOR-ENRICHMENT/TASK-1606_BRIEF_REPORT.md`
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`

## Risks / Limitations
- Full gate-scale confirmation (`N=30`) was not part of this diagnostic run; current result is directional.
- Even improved 5-sensor mode remains below gate threshold lower bound 0.05.

## Rollback
- Revert documentation/log commit for this run task:
  - `git revert <TASK-1606-RUN-commit-hash>`
