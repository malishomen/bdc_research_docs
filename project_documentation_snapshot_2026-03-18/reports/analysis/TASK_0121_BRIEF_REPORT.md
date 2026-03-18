# TASK-0121 BRIEF REPORT — derive KC1_TTT_V3 (analysis-only) + ADR addendum + exp_0016 pre-registration

Commit: `277418eec80f4d4c3d0ed1d76b6cb81477a63c21` (start of TASK-0121)

## Inputs (evidence)

- Worst-case run (TASK-0120) metrics:
  - `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T060901Z_c05b6ee/metrics.csv`
  - Target config: `si128_clonal_init_k_point_mutation_k1p0`
- Queue11 run (TASK-0119) metrics (guard-activity sanity check):
  - `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T054329Z_c682472/metrics.csv`
- Prior evidence:
  - `reports/analysis/exp_0014_kc1_ttt_horizon_sweep_REPORT.md` (queue11 sweep on exp_0012 metrics)
  - `reports/analysis/TASK_0120_BRIEF_REPORT.md` (V2 fails 57/90, CI)

## Fact: V2 still too strict on worst-case

From TASK-0120 (`summary.csv`), under `KC1_TTT_V2 (H=5,T=0.075)`:
- `kc1_fail_count=57/90` => `kc1_fail_rate=0.633333` for `si128_clonal_init_k_point_mutation_k1p0`
- 95% CI: Wilson `[0.530223, 0.725527]`, Clopper-Pearson `[0.525149, 0.732478]` (tool: `tools/analysis/exp0015_single_config_ci.py`)

## Time-to-D evidence (from existing trajectories, no rerun)

Computed by: `tools/analysis/exp0015_time_to_D_distribution.py` on TASK-0120 `metrics.csv`.

For `si128_clonal_init_k_point_mutation_k1p0` (90 seeds):
- D>=0.10: p(time_to<=7)=0.933333; p(time_to<=8)=1.0; median time=7
- D>=0.075: p(time_to<=5)=0.366667; p(time_to<=6)=1.0; median time=6

## Selected vNext candidate: KC1_TTT_V3 (minimal delta from V2)

Primary V3 proposal:
- `KC1_TTT_V3`: `(H=5, T=0.0725)` with same seed-level semantics (FAIL if max(D, gen<=H) < T).

Predicted effect on worst-case (analysis-only, same TASK-0120 trajectories):
- V2 `(5,0.075)`: 57/90 fail (0.633333)
- V3 `(5,0.0725)`: 2/90 fail (0.022222)

Why not choose “KC1 disappears” candidates:
- `(H=5,T=0.07)` and `(H=6,T=0.075)` showed 0/30 KC1 failures across queue11 in quick checks on TASK-0119 metrics, i.e. gate becomes inactive on the evidence set.

Backup (optional):
- `(H=5,T=0.072)` predicts 0/90 KC1 failures on TASK-0120 trajectories, but further reduces evidence-set gate activity (more “disappears”-like).

## Deliverables

- ADR updated (V3 addendum): `docs/adr/ADR_KC1_TTT_VNEXT_UPDATE.md`
- Pre-registered exp_0016 plan:
  - `experiments/exp_0016_kc1_ttt_v3_validation/SPEC.md`
  - `experiments/exp_0016_kc1_ttt_v3_validation/RUN_COMMANDS.md`

