# EXP-0700: Applied GPU+CPU Practical Track (2026-03-04)

## Background
- Phase 4 scientific line is closed as `RUN COMPLETE / GATE FAIL` (ADR-0010, ADR-0012).
- EXP-0700 is a **parallel applied track** for practical utility testing.
- Governance is fixed by ADR-0013.

## Relation To CANON/ADR
- ADR-0013 defines:
  - pilot set,
  - primary metrics,
  - stop-rules,
  - PASS/FAIL decision logic.
- `docs/ops/LOCAL_GPU_RUN_PROFILE.md` defines GPU routing/eligibility.

## Workloads

### Pilot A (GPU / Torch)
- Primary workload:
  - `scripts/wiki_pilot/run_once.py`
- Supporting GPU ops workload (smoke/health validation):
  - `cognitive/run_trl10_gpu_optimized.py`
- Device policy:
  - default `--device auto` resolves to `cuda:0` when available.

### Pilot B (CPU / Symbolic)
- Workload:
  - `python -m evolution.cloze_symbolic.run_generations`
- CPU-only by policy (no Torch refactor in this track).

## Baseline vs Optimized Arms

### Pilot A (GPU)
- Baseline arm:
  - `run_once.py` with default-safe GPU profile (`float32`, no AMP).
- Optimized arm:
  - same script + optional optimization flags (`--use_amp`, tuned batch/resource profile).
- Primary metric per seed:
  - `delta_gpu_i = final_val_loss_baseline_i - final_val_loss_optimized_i`.

### Pilot B (CPU)
- Baseline arm:
  - symbolic baseline configuration (`v0`).
- Optimized arm:
  - tuned symbolic configuration (`v2` with approved flags).
- Primary metric per seed:
  - `delta_cpu_i = final_max_accuracy_optimized_i - final_max_accuracy_baseline_i`.

## Budgets
- **Diagnostic:** `N=10` seeds per pilot.
- **Gate:** `N=30` seeds per pilot.
- Seed range convention:
  - `base_seed=1337`,
  - `seed_k = base_seed + k`, `k=0..N-1`.

## Statistics Protocol
- Paired per-seed deltas (`optimized - baseline` or baseline-loss minus optimized-loss by metric direction).
- Report:
  - `mean_delta`,
  - `std_delta`,
  - `se_delta`,
  - `ci95_low`, `ci95_high`,
  - `n`.
- CI computed over per-seed deltas (not difference of means).

## Baseline Comparators
- Pilot A comparator: baseline GPU run profile from same script family and same seed/budget.
- Pilot B comparator: baseline symbolic config from same task family and same seed/budget.

## Stop/Go Rules
- Follows ADR-0013 exactly.
- No gate N=30 unless both pilots pass diagnostic stop-rules.

## Artifacts
- Matrix runner outputs:
  - `results/exp_0700_applied/<level>/<pilot>/<variant>/seed_<id>/...`
- Aggregates:
  - `results/exp_0700_applied/<level>/aggregates/*.json|*.csv`
- Run manifests:
  - one manifest per seed run + aggregate manifest.

## Reproducibility
- Record in each run manifest:
  - git commit/branch,
  - command line,
  - requested/resolved device,
  - torch/cuda metadata when available,
  - artifact hashes.
- Recovery check must be possible from manifest only.

## Execution Addendum (2026-03-04)

### TASK-2002: Run contract/provenance v2
- Implemented:
  - `scripts/applied/run_applied_matrix.py`
  - `scripts/applied/replay_from_manifest.py`
  - `scripts/analysis/applied_aggregate_exp0700.py`
- Manifest schema: `run-manifest-v2` with command, git, env, requested/resolved device, artifact hashes.
- Recovery check: replay from manifest executed successfully on CPU baseline seed.

### TASK-2003: Smoke parity
- Smoke suite status: `PASS`
  - determinism replay: `PASS` (GPU and CPU checks),
  - fallback check: `PASS` (no silent CUDA->CPU fallback),
  - schema/artifact presence: `PASS`.

### TASK-2004/2005: Diagnostic N=10
- Aggregate: `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json`
- Pilot A (GPU): `FAIL` diagnostic gate
  - `mean_delta_gpu = -6.6757e-05`
  - `CI95 = [-7.3667e-05, -5.9847e-05]`
  - `stability_fail_rate = 0.6` (6/10 failures, optimized arm).
- Pilot B (CPU): `PASS` diagnostic gate
  - `mean_delta_cpu = 0.09293`
  - `CI95 = [0.08906, 0.09680]`
  - `stability_fail_rate = 0.0`.

### TASK-2006 gate status
- `N=30` gate run: **NOT EXECUTED** (blocked by ADR-0013 stop-rule because both pilots must pass diagnostic).

### Practical track status
- Applied track iteration verdict: `FAIL` for readiness progression in this iteration.
- Scientific verdict remains unchanged:
  - Phase 4 scientific line: `RUN COMPLETE / GATE FAIL`.

## Recovery Addendum v2 (TASK-2100..2108)

### Governance
- Recovery governance ADR: `decisions/ADR-0014-applied-gpu-recovery.md`
- ADR-0013 thresholds and criteria remain unchanged.

### Technical recovery package
- `TASK-2100`: GPU fail forensics confirmed dominant signature:
  - strict softmax assertion under AMP path.
- `TASK-2101`: numeric hardening in `scripts/wiki_pilot/run_once.py`:
  - dtype-aware softmax audit in default path,
  - finite guards,
  - debug-only strict flag `--strict_numeric_asserts`.
- `TASK-2102`: run-contract upgraded to row-level `run-index-v3` with required per-run observability fields.
- `TASK-2103`: mini-calibration (`N=5`) selected optimized GPU profile:
  - `--use_amp --batch_size 8 --steps 80` (`opt_amp_bs8`),
  - strict numeric asserts OFF.

### Diagnostic rerun N=10 (TASK-2105)
- Out root: `results/exp_0700_applied_v2/diagnostic/...`
- Pilot A (GPU):
  - `mean_delta = 0.31609`
  - `CI95 = [-0.67478, 1.30696]`
  - `stability_fail_rate = 0.0`
  - Verdict: `FAIL` (`ci95_low <= 0`)
- Pilot B (CPU):
  - `mean_delta = 0.09293`
  - `CI95 = [0.08906, 0.09680]`
  - `stability_fail_rate = 0.0`
  - Verdict: `PASS`

### Gate implication
- `TASK-2106` gate `N=30` was **not executed** because both pilot diagnostic pass was not met.

### Official decision v2
- `TASK-2107`: Practical Readiness Decision v2 = `FAIL`.
- Scope separation remains:
  - Applied verdict: `FAIL` (v2 iteration),
  - Scientific Phase 4 verdict: unchanged (`RUN COMPLETE / GATE FAIL`).

## Governance Addendum v4 (2026-03-05)

### ADR update
- New governance document: `decisions/ADR-0015-applied-fairness-twolevel.md`.
- ADR-0013 thresholds are unchanged.

### Fairness model
- **Level 1 (hard/blocking):** dataset parity, architecture parity, objective parity, seed parity, token/examples budget parity, no hidden fallback, manifest completeness.
- **Level 2 (advisory/non-blocking):** `lr_scaled_with_batch`, AMP choice, clip/scaler tuning.

### Pre-registered GPU profile space (v4)
- Baseline profile:
  - `gpu_baseline_fp32_bs12_steps80_lr3e5`
- Allowed optimized profiles:
  - `gpu_opt_amp_bs8_steps120_lr3e5_fp32crit_clip1`
  - `gpu_opt_amp_bs8_steps120_lr2e5_fp32crit_clip08`
- Selection rule:
  1. `stability_fail_rate <= 0.10`
  2. maximize `ci95_low(delta_gpu)`
  3. tie-break by `mean_delta`

### Execution policy
- `TASK-2123`: GPU-only diagnostic rerun under v4 profile registry.
- `TASK-2124`: CPU carry-forward allowed only with formal code-path equivalence evidence.

## Applied Recovery v4 Outcome (TASK-2120..2127)

### Diagnostic rerun (v4)
- GPU (`gpu_opt_amp_bs8_steps120_lr3e5_fp32crit_clip1`) passed:
  - `mean_delta = 1.5488766988`
  - `CI95 = [0.5886021347, 2.5091512630]`
  - `stability_fail_rate = 0.0`
- CPU diagnostic verdict remained valid via carry-forward equivalence check (`TASK-2124`).

### Gate execution
- GPU gate N=30 executed:
  - aggregate root: `results/exp_0700_applied_v4_gpu_gate/gate/aggregates/`
  - `mean_delta = 1.3836773343`
  - `CI95 = [0.9475860640, 1.8197686045]`
  - `stability_fail_rate = 0.0`

### Applied verdict
- Practical Readiness v3: **PASS** (see `TASK-2127` decision doc).
- Scientific Phase 4 verdict remains unchanged (`RUN COMPLETE / GATE FAIL`).

## Phase-4 Closure Addendum (TASK-4100..4600, 2026-03-05)

### Reference profile freeze
- Locked profile:
  - `configs/profiles/gpu_profile_v4_reference.yaml`
  - SHA256(parameters): `6aa623965a8937b82366258f64172333e350ceca774e2d582132b45390714e0b`
- Registry linkage:
  - `configs/applied/gpu_profile_registry_v4.json`

### Robustness metric
- Added `negative_seed_rate = N_negative / N` to aggregate pipeline.
- Standardized payload exported to:
  - `reports/metrics.json`

### Seed failure forensic
- Forensic artifacts generated for all negative-delta gate seeds:
  - `analysis/seed_forensics/seed_1339.json`
  - `analysis/seed_forensics/seed_1342.json`
  - `analysis/seed_forensics/seed_1352.json`
  - `analysis/seed_forensics/seed_1356.json`
  - `analysis/seed_forensics/seed_1359.json`
- Summary report:
  - `reports/seed_failure_analysis.md`

### Predeclared profile space
- Declared in:
  - `docs/profile_search_space.md`
- Selected profile tagged as predeclared-space selection.

### Final reproducibility run
- Output root:
  - `results/repro_run/`
- Aggregate:
  - `mean_delta = 1.3595809937`
  - `CI95 = [0.9233480782, 1.7958139091]`
  - `negative_seed_rate = 0.1666666667` (`5/30`)
- Criteria:
  - `CI95_low > 0` -> PASS
  - `negative_seed_rate < 0.25` -> PASS

### Hardening completion (TASK-4700..5200)
- Reference immutability lock:
  - `configs/profiles/gpu_profile_v4_reference.lock`
  - `scripts/validation/check_reference_lock.py`
- Determinism replay report:
  - `reports/determinism_check.md`
- Environment capture:
  - `environment_snapshot.json`
  - `environment_requirements.txt`
- Dataset immutability proof:
  - `data/dataset_manifest.json`
  - `scripts/validation/check_dataset_integrity.py`
- Phase-4 provenance ledger:
  - `experiments/PHASE4_MANIFEST.json`
- External reproducibility report:
  - `reports/external_repro_check.md`
