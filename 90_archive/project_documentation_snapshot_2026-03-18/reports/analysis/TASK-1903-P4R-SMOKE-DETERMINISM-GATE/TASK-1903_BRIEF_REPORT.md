# TASK-1903 BRIEF REPORT

## Scope
- Execute ADR-0011 smoke/determinism gate before any full redesign `N=30` run.
- Validate:
  - determinism replay,
  - recompute/ablation/provenance pipeline integrity,
  - stop-rules for arm A and fallback arm B.

## Changes
- Generated smoke artifacts (runtime only, not committed):
  - `results/edp1_exp0600_multirole_3task_p4r_smoke/*`
  - `results/edp1_exp0600_multirole_3task_p4r_smoke_armB/*`
  - `results/edp1_exp0600_multirole_3task_p4r_smoke_baseline/*`
- Produced this report.

## Verification (L0)
- Command: `python scripts/edp1/run_phase4_multirole.py --level diagnostic --seeds 5 --base_seed 1337 --use_category_task --out_root results/edp1_exp0600_multirole_3task_p4r_smoke_baseline --aggregate_prefix phase4_multirole_3task_smoke_baseline_summary`
- Result: PASS
- Command: `python scripts/edp1/run_phase4_multirole.py --level diagnostic --seeds 5 --base_seed 1337 --use_category_task --collective_scheme s1_gain --category_metric_mode balanced_accuracy --role_balance_bonus 0.15 --out_root results/edp1_exp0600_multirole_3task_p4r_smoke --aggregate_prefix phase4_multirole_3task_smoke_summary`
- Result: PASS
- Command: `python scripts/edp1/run_phase4_multirole.py --level diagnostic --seeds 5 --base_seed 1337 --use_category_task --collective_scheme s1_gain --category_metric_mode balanced_accuracy --role_balance_bonus 0.30 --collective_category_weight 1.50 --out_root results/edp1_exp0600_multirole_3task_p4r_smoke_armB --aggregate_prefix phase4_multirole_3task_smoke_armB_summary`
- Result: PASS
- Command: recompute + ablation:
  - `python scripts/analysis/phase4_recompute_advantage.py --in_json <smoke_summary.json> --out_json <recomputed.json> --out_csv <recomputed.csv>`
  - `python scripts/analysis/phase4_role_ablation.py --in_json <recomputed.json> --out_json <ablation.json> --out_csv <ablation.csv>`
- Result: PASS for baseline, arm A, arm B.
- Command: provenance:
  - `python scripts/analysis/phase4_build_provenance_manifest.py --summary_json ... --summary_csv ... --recomputed_json ... --recomputed_csv ... --ablation_json ... --ablation_csv ... --out_json ...`
- Result: PASS (arm A and arm B).
- Command: deterministic replay check:
  - repeated `run_generations` with identical seed/flags (`results/.tmp_task1903_det_a`, `results/.tmp_task1903_det_b`),
  - compared core final metrics.
- Result: PASS (`core_equal=True`; elapsed time differs only by runtime).

### Key metrics

Smoke recompute (`N=5`, seeds `1337..1341`):

| Arm | A1_3 mean | A2_3 mean | gain_category mean | A3_3 pareto_rate |
|---|---:|---:|---:|---:|
| Baseline control | -0.0078416027 | -0.0091229183 | 0.0 | 0.0 |
| Arm A | 0.0123466782 | -0.0057969843 | 0.0 | 0.0 |
| Arm B | 0.0128055808 | -0.0057969843 | 0.0 | 0.0 |

Stop-rule assessment:
- Rule #1 (determinism): PASS
- Rule #2 (pipeline integrity): PASS
- Rule #3 (`gain_category_mean > 0` and `A2_3` improvement vs baseline): FAIL for both arms because `gain_category_mean = 0.0`
- Rule #4 (3-role ablation schema + verdicts): PASS

## Artifacts
- `results/edp1_exp0600_multirole_3task_p4r_smoke/aggregates/phase4_multirole_3task_smoke_summary.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke/aggregates/phase4_advantage_recomputed_3task_smoke.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke/aggregates/phase4_role_ablation_3task_smoke.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke_armB/aggregates/phase4_multirole_3task_smoke_armB_summary.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke_armB/aggregates/phase4_advantage_recomputed_3task_smoke_armB.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke_armB/aggregates/phase4_role_ablation_3task_smoke_armB.json` (runtime)
- `results/edp1_exp0600_multirole_3task_p4r_smoke_baseline/aggregates/phase4_advantage_recomputed_3task_smoke_baseline.json` (runtime)

## Risks / Limitations
- No full `N=30` redesign run is allowed after stop-rule #3 fail.
- Current redesign line did not activate positive category gain at smoke scale.

## Rollback
- `git revert <commit-hash-containing-task-1903-report>`
