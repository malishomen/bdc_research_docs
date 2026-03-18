# ADR: KC1_TTT vNext Update (KC1_TTT_V2) — Horizon/Threshold Adjustment (R2 Proposal)

## Status
Proposed

## Context / Problem Statement

Evidence from analysis on the 11-config queue scheduled for exp_0011 follow-ups shows that:

1. Under exp_0011 overall stack definition (includes **KC1_TTT**), 5/11 configs fail overall solely due to KC1_TTT, while final thresholds (E/D) are met at gen=50 for all 11 under exp_0012 metrics.
   - Reconciliation report: `reports/analysis/exp_0013_gate_trace_reconciliation_REPORT.md`
2. The same 5 configs that fail KC1_TTT under baseline `(H=3, T=0.10)` typically reach `D>=0.10` later (median time-to-threshold in gen ~4..7 on exp_0012 metrics).
   - Sweep report: `reports/analysis/exp_0014_kc1_ttt_horizon_sweep_REPORT.md`

Queue reference:
- `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl` (11 configs)

Baseline KC1_TTT definition (exp_0011 overall stack):
- Source: `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/src/kill_eval.py`
- Rule (seed-level): FAIL if `max(D)` over generations `<=3` is strictly `<0.10`

## Decision Drivers

- **Reduce systematic false negatives** on configs that later satisfy final thresholds by gen=50 (per exp_0012 metrics).
- **Preserve sanity as a kill-guard**: KC1 should remain an active early gate (should not trivially disappear on the evidence set).
- **Minimal change** from baseline (smallest delta from `(H=3, T=0.10)`) that achieves removal of systematic fail-all-seeds behavior on queue11.
- **No retroactive changes**: no edits to exp_0007/exp_0009/exp_0011/exp_0012 definitions or results.

## Options Considered (From Sweep Grid)

Sweep grid and trade-off table source:
- Tool: `tools/analysis/exp0012_kc1_ttt_horizon_sweep.py` (print mode: `--print_tradeoff_only`)
- Evidence report: `reports/analysis/exp_0014_kc1_ttt_horizon_sweep_REPORT.md`

Key candidates (queue11 evidence, exp_0012 metrics):

1. Baseline: `H=3, T=0.10`
   - `configs_fail_rate_1p0 = 5` (systematic fail-all-seeds on 5 configs)
2. Candidate A (recommended): `H=5, T=0.075`
   - `configs_fail_rate_1p0 = 0`
   - `configs_fail_rate_0p0 = 10` (KC1 remains active on this evidence set)
   - `mean_fail_rate_over_11 = 0.018182`
3. Candidate B (backup): `H=4, T=0.05`
   - `configs_fail_rate_1p0 = 0`
   - `configs_fail_rate_0p0 = 11` (KC1 effectively disappears on this evidence set)

## Proposed Change (vNext Only)

Introduce a new KC1 variant for vNext experiments only:

- **Name:** `KC1_TTT_V2`
- **Definition (seed-level):** FAIL if `max(D)` over generations `<= H_V2` is strictly `< T_V2`
- **Parameters:** `H_V2 = 5`, `T_V2 = 0.075`

This is a **new versioned kill-criteria semantics** and must not be applied retroactively.

## Why V2 Is Insufficient (New Evidence)

Focused validation on the remaining worst-case config under V2 shows V2 still produces a high KC1 false-negative rate:

- Task report: `reports/analysis/TASK_0120_BRIEF_REPORT.md`
- Evidence run dir (local): `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T060901Z_c05b6ee`
- Target config: `si128_clonal_init_k_point_mutation_k1p0`
  - Observed under V2 (`H=5,T=0.075`): `kc1_fail_count=57/90` => `kc1_fail_rate=0.633333`
  - 95% CI (from `tools/analysis/exp0015_single_config_ci.py`): Wilson `[0.530223,0.725527]`, Clopper-Pearson `[0.525149,0.732478]`

This blocks promoting V2 as a robust KC1 guard for vNext without further adjustment.

## KC1_TTT_V3 Proposal (Minimal Update)

Goal: reduce KC1 false negatives for `si128_clonal_init_k_point_mutation_k1p0` while avoiding a “KC1 disappears” behavior on the queue11 evidence set.

Proposed new variant (vNext only):

- **Name:** `KC1_TTT_V3`
- **Definition (seed-level):** FAIL if `max(D)` over generations `<=H_V3` is strictly `<T_V3`
- **Parameters:** `H_V3 = 5`, `T_V3 = 0.0725`

Evidence-based predicted effect on the same TASK-0120 trajectories (analysis-only, no rerun):

- Command/tool: `tools/analysis/exp0015_time_to_D_distribution.py` with `--kc1_candidates`
- Inputs: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T060901Z_c05b6ee/metrics.csv`
- Predicted KC1 failures for target config:
  - V2 `(H=5,T=0.075)`: 57/90 (0.633333)
  - V3 `(H=5,T=0.0725)`: 2/90 (0.022222)

Evidence-based queue11 guard activity check (analysis on exp_0015 queue11 run metrics, 30 seeds):

- Inputs: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T054329Z_c682472/metrics.csv`
- Under `(H=5,T=0.0725)`, two queue11 configs retain non-zero KC1 fail rates (guard remains active on this evidence set):
  - `si128_clonal_init_k_point_mutation_k1p0`: 2/30 seeds fail
  - `si64_clonal_init_per_locus_flip_p0p01`: 1/30 seeds fail

Backup (optional) if V3 still too strict after validation:

- `(H=5,T=0.072)` yields 0/90 KC1 failures for target on TASK-0120 trajectories, but reduces queue11 activity to 1 config with non-zero fail rate (more “disappears”-like).

## Scope / Non-Changes

- No changes to:
  - `experiments/exp_0007_pistream_v3_phase0_sweep`
  - `experiments/exp_0009_kc1_diagnostics`
  - `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt`
  - `experiments/exp_0012_kc2_diagnostics`
- No changes to `KILL_CRITERIA.yaml` or `VERSIONING.md` within this ADR; the ADR is a proposal for a new experiment version.

## Risks

- **Too permissive early gate:** may allow truly dead configs to run longer (CPU cost increase).
- **Sanity drift:** if KC1 becomes ineffective broadly (not just on queue11), it may fail to function as intended.
- **Evidence set bias:** queue11 is not the full sweep; generalization beyond this set requires a new validation experiment.

## Validation Plan (Pre-Registered)

Validation experiment (pre-registration, CPU-only):
- `experiments/exp_0015_kc1_ttt_vnext_validation/SPEC.md`
- `experiments/exp_0015_kc1_ttt_vnext_validation/RUN_COMMANDS.md`

Primary success metric (queue11, seeds=10, gen=50):
- reduce `configs_fail_rate_1p0` from 5 (baseline) to 0 under `KC1_TTT_V2` on the same trajectories (exp_0012 metrics), while keeping `configs_fail_rate_0p0 < 11`.

V3 validation experiment (pre-registration, CPU-only):
- `experiments/exp_0016_kc1_ttt_v3_validation/SPEC.md`
- `experiments/exp_0016_kc1_ttt_v3_validation/RUN_COMMANDS.md`

Primary endpoint for V3 (queue11, seeds=30, gen=50, include_sanity):
- reduce `kc1_fail_rate` for `si128_clonal_init_k_point_mutation_k1p0` relative to V2 on the same seeds.
Secondary endpoint:
- sanity remains stable (controls PASS, negative FAIL).

## Rollback Plan

If vNext validation shows unacceptable sanity regression (e.g., KC1 becomes ineffective beyond the evidence set), revert to baseline `KC1_TTT (H=3,T=0.10)` in the next experiment version, with explicit documentation and no retroactive changes.

If V3 validation shows unacceptable regression, revert to V2 `(H=5,T=0.075)` in the next experiment version (no retroactive changes).
