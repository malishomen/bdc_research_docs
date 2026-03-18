# Canonical Kill Definition (Single Source of Truth)

## Resolution Rule
- Canonical source: `evolution/edp1_symbolic/run_generations.py`
- Rationale: runtime evaluation is the only authoritative PASS/FAIL producer.

## Canonical PASS/FAIL Definition
Run status is read from `summary.json`:
- `kill_status.status == "PASS"` -> PASS
- `kill_status.status == "FAIL"` -> FAIL with reason and generation from same object.

## Canonical Runtime Conditions

### diversity_collapse
- if `diversity_index < diversity_collapse_threshold` for `diversity_collapse_patience` consecutive generations -> FAIL(reason=`diversity_collapse`).

### trivial_strategy
- streak increments when `trivial_strategy_rate > trivial_strategy_threshold`.
- FAIL when streak `>= trivial_strategy_patience` and current `trivial_strategy_rate >= trivial_strategy_threshold`.

### plateau (phase 1 only)
- evaluate over rolling window size `plateau_window + 1`.
- compute `improvement_ratio = (newest - oldest) / max(abs(oldest), 1e-12)`.
- if `improvement_ratio < plateau_improvement_pct`:
  - if cooldown permits, schedule diversity shock and continue;
  - else FAIL(reason=`plateau`).

## Aggregate Rules (for TASK-1202 follow-up)
- `aggregate_results.py` must not recompute kill logic.
- It must consume `summary.json.kill_status` as authoritative.
- Optional post-hoc diagnostics may remain, but must be labeled `diagnostic_only` and must not overwrite PASS/FAIL fields.

## Proposed Refactor Plan
1. Add loader in aggregate step:
   - read `summary.json.kill_status.status/reason/generation`.
2. Remove `evaluate_kill_criteria` duplicate decision path.
3. Keep existing derived checks only as non-authoritative columns.
4. Re-run N=30 validation and confirm:
   - `metrics_agg.pass_rate` matches runtime summaries exactly.
