# ADR-0013: Practical Applicability Track (GPU+CPU) Governance

Date: 2026-03-04  
Status: ACCEPTED

## Context
- Phase 4 scientific track remains closed as:
  - `RUN STATUS: RUN COMPLETE`
  - `GATE STATUS: FAIL`
  - governed by ADR-0010 and ADR-0012.
- Practical utility evaluation is needed as a separate engineering/applied track.

## Decision
Open a parallel **Applied Track** with two pilots:
1. **Pilot A (GPU, Torch)**  
   workload family: `scripts/wiki_pilot/run_once.py` (primary) and `cognitive/run_trl10_gpu_optimized.py` (supporting smoke/ops validation).
2. **Pilot B (CPU, Symbolic)**  
   workload family: `evolution.cloze_symbolic.run_generations` path.

This track does **not** revise or override Phase 4 scientific verdict.

## Canonical Metrics And Comparators

### Pilot A (GPU) primary metric
- Per seed:
  - `delta_gpu_i = final_val_loss_baseline_i - final_val_loss_optimized_i`
- Interpretation:
  - `delta_gpu_i > 0` means optimized run is better (lower loss).

### Pilot B (CPU) primary metric
- Per seed:
  - `delta_cpu_i = final_max_accuracy_optimized_i - final_max_accuracy_baseline_i`
- Interpretation:
  - `delta_cpu_i > 0` means optimized run is better (higher accuracy).

### Statistics
- For each pilot and phase (diagnostic/gate):
  - mean delta,
  - 95% CI over per-seed deltas (paired by seed),
  - stability indicators (fail rate, missing artifacts, fallback rate).

## Budgets
- **Diagnostic:** `N=10` seeds per pilot.
- **Gate:** `N=30` seeds per pilot.
- Budget presets are fixed in EXP-0700 and must not be tuned post-hoc.

## Stop-Rules (before any N=30 gate)
1. TASK-2003 smoke parity must pass for both GPU and CPU paths:
  - schema valid,
  - manifests valid,
  - no silent fallback (`requested cuda` but resolved CPU) on GPU path.
2. Pilot A diagnostic gate:
  - `CI95_low(delta_gpu) > 0`,
  - stability fail rate `<= 10%`.
3. Pilot B diagnostic gate:
  - `CI95_low(delta_cpu) > 0`,
  - stability fail rate `<= 10%`.
4. If any condition fails:
  - do not run TASK-2006 (`N=30`),
  - publish formal closure/FAIL pathway for applied track iteration.

## Practical Readiness Decision Rule (TASK-2007)
- **PASS** if at least one pilot demonstrates statistically stable practical uplift at gate budget with controlled risk:
  - `CI95_low(delta) > 0`,
  - fail rate `<= 10%`,
  - no infra contamination invalidating interpretation.
- **FAIL** otherwise.

## Governance Constraints
- No post-hoc threshold or formula change without new ADR.
- Applied track outcomes must be reported separately from scientific verdicts.
- `results/` artifacts remain out of git.

## Consequences
- Enables pragmatic performance utility checks while preserving scientific governance integrity.
- Provides explicit stop boundaries to prevent uncontrolled compute spending.

## Rollback
- `git revert <commit-hash-containing-ADR-0013>`
